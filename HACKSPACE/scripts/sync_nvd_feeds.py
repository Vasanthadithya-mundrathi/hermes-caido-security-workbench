#!/usr/bin/env python3
"""Download official NVD yearly CVE enrichment feeds for the local research corpus."""

from __future__ import annotations

import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from zipfile import BadZipFile, ZipFile


ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "data" / "sources" / "nvd"
URL = "https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-{year}.json.zip"


def valid_zip(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        with ZipFile(path) as archive:
            return len(archive.namelist()) == 1 and archive.testzip() is None
    except (BadZipFile, OSError):
        return False


def download(year: int) -> tuple[int, str, int]:
    target = DEST / f"nvdcve-2.0-{year}.json.zip"
    if valid_zip(target):
        return year, "cached", target.stat().st_size
    part = target.with_suffix(target.suffix + ".part")
    command = [
        "curl", "-L", "-f", "-sS", "--retry", "4", "--retry-delay", "3",
        "--connect-timeout", "20", "--max-time", "600", "-C", "-",
        "-o", str(part), URL.format(year=year),
    ]
    subprocess.run(command, check=True)
    if not valid_zip(part):
        raise RuntimeError(f"NVD feed for {year} is not a valid complete ZIP")
    part.replace(target)
    return year, "downloaded", target.stat().st_size


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2002)
    parser.add_argument("--end-year", type=int, default=date.today().year)
    args = parser.parse_args()
    if args.start_year < 2002 or args.end_year < args.start_year:
        parser.error("expected a year range starting at 2002 or later")
    DEST.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as pool:
        pending = [pool.submit(download, year) for year in range(args.start_year, args.end_year + 1)]
        for future in as_completed(pending):
            year, status, size = future.result()
            print(f"{year}: {status} {size} bytes", flush=True)


if __name__ == "__main__":
    main()
