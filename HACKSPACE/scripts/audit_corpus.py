#!/usr/bin/env python3
"""Audit downloaded source archives without treating aliases as unique bugs."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import tarfile
from datetime import datetime, timezone
from pathlib import Path
from zipfile import BadZipFile, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "data" / "sources"
OUTPUT = ROOT / "data" / "corpus-manifest.json"
ARCHIVES = {
    "osv": "osv-all.zip",
    "cve": "cve-2026-10-26-baseline.zip",
    "github_advisory": "github-advisory-main.zip",
}
DERIVED_ARCHIVES = {"cve_records": "cve-2026-10-26-records.zip"}


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect(name: str, path: Path, crc: bool) -> dict[str, object]:
    result: dict[str, object] = {"source": name, "path": str(path.relative_to(ROOT))}
    if not path.exists():
        return {**result, "status": "missing"}
    result["bytes"] = path.stat().st_size
    try:
        if path.name.endswith(".tar.gz"):
            with tarfile.open(path, "r:gz") as archive:
                entries = archive.getmembers()
                result["entries"] = sum(entry.isfile() for entry in entries)
                result["uncompressed_bytes"] = sum(
                    entry.size for entry in entries if entry.isfile()
                )
            if crc:
                with gzip.open(path, "rb") as stream:
                    for _ in iter(lambda: stream.read(8 * 1024 * 1024), b""):
                        pass
                result["gzip_crc"] = "ok"
            result["status"] = "complete"
            result["sha256"] = hash_file(path)
            return result
        with ZipFile(path) as archive:
            entries = archive.infolist()
            result["entries"] = sum(not entry.is_dir() for entry in entries)
            result["uncompressed_bytes"] = sum(
                entry.file_size for entry in entries if not entry.is_dir()
            )
            if crc:
                bad = archive.testzip()
                result["crc"] = "ok" if bad is None else f"failed: {bad}"
                result["status"] = "complete" if bad is None else "invalid"
            else:
                result["status"] = "zip_directory_ok"
        result["sha256"] = hash_file(path)
    except (BadZipFile, OSError, ValueError, tarfile.TarError) as error:
        result["status"] = "invalid_or_partial"
        result["error"] = str(error)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-crc", action="store_true", help="Read and CRC-check every ZIP member")
    args = parser.parse_args()
    records = [inspect(name, SOURCES / filename, args.verify_crc) for name, filename in ARCHIVES.items()]
    for name, filename in DERIVED_ARCHIVES.items():
        derived = inspect(name, SOURCES / filename, args.verify_crc)
        derived["derived_from"] = "cve"
        records.append(derived)
    nvd = SOURCES / "nvd"
    records.extend(
        inspect("nvd_cve", path, args.verify_crc)
        for path in sorted(nvd.glob("nvdcve-2.0-*.json.zip"))
    )
    records.append(inspect("nvd_cpe_match", nvd / "nvdcpematch-2.0.tar.gz", args.verify_crc))
    manifest = {
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "crc_checked": args.verify_crc,
        "archives": records,
        "complete_archive_bytes": sum(
            int(record["bytes"]) for record in records
            if record["status"] == "complete" and "derived_from" not in record
        ),
        "on_disk_archive_bytes": sum(
            int(record["bytes"]) for record in records if record["status"] == "complete"
        ),
        "note": "The extracted CVE records ZIP is a derived copy and excluded from complete_archive_bytes. Source records overlap by CVE/GHSA/OSV alias; byte and entry totals are not distinct bugs or bounty reports.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
