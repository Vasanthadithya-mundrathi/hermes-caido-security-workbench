#!/usr/bin/env python3
"""Validate, browse, and render the link-only public resource catalog."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "catalog" / "resources.csv"
OUTPUT = ROOT / "catalog" / "index.md"
FIELDS = ("id", "kind", "name", "topics", "publisher", "url", "access", "notes")
KINDS = {
    "public_disclosures": "Public disclosures and advisories",
    "community_index": "Community report indexes",
    "research": "Original research and publisher blogs",
    "ctf_writeups": "CTF writeups",
    "ctf_practice": "CTF and lab practice",
    "reference": "Primary references",
    "community_reference": "Community references",
}


def load() -> list[dict[str, str]]:
    with SOURCE.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError(f"Expected columns: {', '.join(FIELDS)}")
        return list(reader)


def validate(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    urls: set[str] = set()
    for number, row in enumerate(rows, start=2):
        missing = [field for field in FIELDS if not row.get(field, "").strip()]
        if missing:
            errors.append(f"line {number}: missing {', '.join(missing)}")
        if row["kind"] not in KINDS:
            errors.append(f"line {number}: unknown kind {row['kind']!r}")
        parsed = urlparse(row["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"line {number}: URL must be HTTPS with a host")
        if row["id"] in ids:
            errors.append(f"line {number}: duplicate ID {row['id']}")
        if row["url"] in urls:
            errors.append(f"line {number}: duplicate URL {row['url']}")
        ids.add(row["id"])
        urls.add(row["url"])
    return errors


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def build(rows: list[dict[str, str]]) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["kind"]].append(row)
    lines = [
        "# Public security resources",
        "",
        "Generated from [resources.csv](resources.csv) with `python3 scripts/catalog.py build`.",
        "The links point to publishers and discovery feeds; this is not an archive of every report.",
        "",
    ]
    for kind, title in KINDS.items():
        if not grouped[kind]:
            continue
        lines += [f"## {title}", "", "| Resource | Topics | Access | Note |", "|---|---|---|---|"]
        for row in sorted(grouped[kind], key=lambda entry: entry["name"].casefold()):
            name = f"[{cell(row['name'])}]({row['url']})"
            lines.append(
                f"| {name} | {cell(row['topics'].replace('|', ', '))} | "
                f"{cell(row['access'])} | {cell(row['notes'])} |"
            )
        lines.append("")
    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(rows)} resources")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "build", "search"))
    parser.add_argument("query", nargs="?", help="Text to find for the search command")
    args = parser.parse_args()
    rows = load()
    errors = validate(rows)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.command == "check":
        print(f"Catalog valid: {len(rows)} unique HTTPS resources")
    elif args.command == "build":
        build(rows)
    else:
        if not args.query:
            parser.error("search requires a query")
        matches = [row for row in rows if args.query.casefold() in " ".join(row.values()).casefold()]
        for row in matches:
            print(f"{row['id']}\t{row['name']}\t{row['url']}")
        print(f"{len(matches)} match(es)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
