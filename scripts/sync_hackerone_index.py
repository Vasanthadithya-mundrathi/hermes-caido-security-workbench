#!/usr/bin/env python3
"""Make a private local search index from a third-party disclosed-report catalog."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPO = "https://github.com/ajaysenr/HackerOne-Disclosed-Reports"
SOURCE_JSON = "https://raw.githubusercontent.com/ajaysenr/HackerOne-Disclosed-Reports/main/index.json"
DESTINATION = ROOT / "HACKSPACE" / "data" / "hackerone-disclosed-index.csv"
FIELDS = (
    "id", "url", "title", "visibility", "program", "reporter", "severity", "bounty",
    "weakness", "reported_at", "disclosed_at", "source_index",
)


def safe_text(value: object) -> str:
    """Keep third-party text inert when a CSV is opened in a spreadsheet."""
    result = "" if value is None else str(value).replace("\x00", "")
    return "'" + result if result[:1] in ("=", "+", "-", "@") else result


def normalize(data: object) -> list[dict[str, str]]:
    if not isinstance(data, list):
        raise ValueError("Unexpected source schema: expected an array")
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in data:
        if not isinstance(item, dict):
            continue
        url = str(item.get("url", "")).strip()
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != "hackerone.com" or not parsed.path.startswith("/reports/"):
            continue
        if url in seen:
            continue
        seen.add(url)
        rows.append({field: safe_text(item.get(field)) for field in FIELDS if field != "source_index"} | {"source_index": SOURCE_REPO})
    return rows


def sync() -> None:
    request = Request(SOURCE_JSON, headers={"User-Agent": "Hermes-Caido-Workbench/1.0 (personal metadata index)"})
    with urlopen(request, timeout=45) as response:
        content = response.read(15_000_001)
    if len(content) > 15_000_000:
        raise ValueError("Source exceeds the 15 MB limit")
    rows = normalize(json.loads(content))
    if not rows:
        raise ValueError("Source contained no valid report URLs")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Indexed {len(rows)} unique report URLs in {DESTINATION.relative_to(ROOT)}")
    print("Third-party metadata can be incomplete or stale. Confirm each report on HackerOne before citing it.")


def search(query: str) -> None:
    if not DESTINATION.exists():
        raise FileNotFoundError("Run 'sync' first")
    with DESTINATION.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    matches = [row for row in rows if query.casefold() in " ".join(row.values()).casefold()]
    for row in matches[:50]:
        print(f"{row['disclosed_at']}\t{row['title']}\t{row['url']}")
    print(f"{len(matches)} match(es); showing at most 50")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("sync", "search"))
    parser.add_argument("query", nargs="?")
    args = parser.parse_args()
    try:
        if args.command == "sync":
            sync()
        elif args.query:
            search(args.query)
        else:
            parser.error("search requires a query")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
