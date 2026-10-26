#!/usr/bin/env python3
"""Find an advisory by exact filename ID inside the local bulk ZIPs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "data" / "sources"
ARCHIVES = {
    "osv": SOURCES / "osv-all.zip",
    "cve": SOURCES / "cve-2026-10-26-records.zip",
    "github_advisory": SOURCES / "github-advisory-main.zip",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("id", help="Exact CVE-, GHSA-, or OSV- identifier")
    parser.add_argument("--source", choices=ARCHIVES, help="Search one archive")
    parser.add_argument("--max-chars", type=int, default=5000)
    args = parser.parse_args()
    needle = args.id.upper() + ".JSON"
    if not args.id.upper().startswith(("CVE-", "GHSA-", "OSV-")):
        parser.error("provide an exact CVE-, GHSA-, or OSV- identifier")
    found = False
    for source, archive_path in ARCHIVES.items():
        if args.source and source != args.source:
            continue
        if not archive_path.exists():
            continue
        with ZipFile(archive_path) as archive:
            for member in archive.namelist():
                if Path(member).name.upper() != needle:
                    continue
                found = True
                record = json.loads(archive.read(member))
                payload = json.dumps(record, indent=2, ensure_ascii=False)
                print(f"SOURCE: {source}\nMEMBER: {member}\n{payload[:args.max_chars]}")
                if len(payload) > args.max_chars:
                    print(f"... truncated {len(payload) - args.max_chars} characters")
    if not found:
        raise SystemExit("No filename match. Aliases may appear only inside another record; try the original identifier.")


if __name__ == "__main__":
    main()
