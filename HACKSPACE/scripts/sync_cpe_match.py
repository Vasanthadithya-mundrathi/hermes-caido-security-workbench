#!/usr/bin/env python3
"""Resume NVD's large public CPE Match archive with checked HTTP byte ranges.

The archive is advisory enrichment, not a bug-bounty report collection.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import shutil
import time
import urllib.request
from pathlib import Path

URL = "https://nvd.nist.gov/feeds/json/cpematch/2.0/nvdcpematch-2.0.tar.gz"
RANGE_RE = re.compile(r"bytes (\d+)-(\d+)/(\d+)")


def request_range(url: str, start: int, end: int, total: int | None = None, etag: str | None = None):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}", "User-Agent": "HACKSPACE-research-archive/1.0"})
    response = urllib.request.urlopen(req, timeout=90)
    match = RANGE_RE.fullmatch(response.headers.get("Content-Range", ""))
    if response.status != 206 or not match:
        response.close()
        raise RuntimeError("server did not return a valid 206 byte range")
    got_start, got_end, got_total = map(int, match.groups())
    got_etag = response.headers.get("ETag")
    if (got_start, got_end) != (start, end) or (total is not None and got_total != total):
        response.close()
        raise RuntimeError("archive changed size or server returned the wrong range")
    if etag and got_etag != etag:
        response.close()
        raise RuntimeError("archive ETag changed during transfer")
    return response, got_total, got_etag


def fetch_chunk(url: str, start: int, end: int, total: int, etag: str, part: Path):
    expected = end - start + 1
    for attempt in range(40):
        have = part.stat().st_size if part.exists() else 0
        if have == expected:
            return part
        if have > expected:
            raise RuntimeError(f"oversized part: {part}")
        try:
            response, _, _ = request_range(url, start + have, end, total, etag)
            with response, part.open("ab") as out:
                while True:
                    block = response.read(1024 * 1024)
                    if not block:
                        break
                    out.write(block)
        except Exception as exc:
            if attempt == 39:
                raise RuntimeError(f"range {start}-{end} failed after 40 attempts") from exc
            time.sleep(min(2 + attempt, 15))
    if part.exists() and part.stat().st_size == expected:
        return part
    raise RuntimeError(f"incomplete range {start}-{end}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "data/sources/nvd/nvdcpematch-2.0.tar.gz")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--chunk-mib", type=int, default=48)
    args = parser.parse_args()
    if args.workers < 1 or args.chunk_mib < 1:
        parser.error("workers and chunk-mib must be positive")
    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    response, total, etag = request_range(URL, 0, 0)
    with response:
        response.read()
    if not etag:
        raise RuntimeError("archive has no ETag; cannot guard a multi-range snapshot")
    prefix_size = output.stat().st_size if output.exists() else 0
    if prefix_size > total:
        raise RuntimeError("existing output is longer than the current archive")
    if prefix_size:
        # A resumed prefix may come from an earlier run. Compare its start, middle,
        # and end to the current source before extending it.
        with output.open("rb") as prefix:
            for offset in sorted({0, prefix_size // 2, max(0, prefix_size - 1024)}):
                length = min(1024, prefix_size - offset)
                response, _, _ = request_range(URL, offset, offset + length - 1, total, etag)
                with response:
                    sample = response.read()
                prefix.seek(offset)
                if sample != prefix.read(length):
                    raise RuntimeError("existing prefix differs from today's NVD archive; remove or rename it and retry")
    if prefix_size == total:
        print(f"complete {output}: {total} bytes (archive structure still needs verification)")
        return
    part_dir = output.with_name(output.name + ".parts")
    part_dir.mkdir(exist_ok=True)
    chunk_bytes = args.chunk_mib * 1024 * 1024
    tasks = []
    for start in range(prefix_size, total, chunk_bytes):
        end = min(total - 1, start + chunk_bytes - 1)
        tasks.append((start, end, part_dir / f"{start}-{end}.part"))
    print(f"NVD CPE Match: {total} bytes, ETag {etag}; prefix {prefix_size}; {len(tasks)} remaining ranges", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_chunk, URL, start, end, total, etag, part): (start, end) for start, end, part in tasks}
        for future in concurrent.futures.as_completed(futures):
            start, end = futures[future]
            future.result()
            print(f"complete range {start}-{end}", flush=True)
    temporary = output.with_name(output.name + ".complete.tmp")
    with temporary.open("wb") as combined:
        if prefix_size:
            with output.open("rb") as prefix:
                shutil.copyfileobj(prefix, combined, 1024 * 1024)
        for start, end, part in tasks:
            if part.stat().st_size != end - start + 1:
                raise RuntimeError(f"wrong part size: {part}")
            with part.open("rb") as stream:
                shutil.copyfileobj(stream, combined, 1024 * 1024)
    if temporary.stat().st_size != total:
        raise RuntimeError("assembled archive has wrong size")
    temporary.replace(output)
    for _, _, part in tasks:
        part.unlink()
    part_dir.rmdir()
    print(f"assembled {output}: {total} bytes; run audit_corpus.py --verify-crc next")


if __name__ == "__main__":
    main()
