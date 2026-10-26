#!/usr/bin/env python3
"""Build a local searchable SQLite index from optional public-link metadata."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "HACKSPACE" / "data"
DATABASE = DATA / "library.sqlite"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path.relative_to(ROOT)}; run its sync script first")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build() -> None:
    hackerone = read_csv(DATA / "hackerone-disclosed-index.csv")
    pentesterland = read_csv(DATA / "pentesterland-writeups.csv")
    DATABASE.unlink(missing_ok=True)
    with sqlite3.connect(DATABASE) as db:
        db.execute("""CREATE TABLE entries (
            url TEXT PRIMARY KEY, source TEXT NOT NULL, title TEXT, topics TEXT,
            program TEXT, authors TEXT, published TEXT, visibility TEXT,
            severity TEXT, bounty_usd REAL
        )""")
        db.executemany(
            "INSERT OR IGNORE INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ((row["url"], "HackerOne community index", row["title"], row["weakness"],
              row["program"], row["reporter"], row["disclosed_at"], row["visibility"],
              row.get("severity", ""), float(row["bounty"]) if row.get("bounty", "").strip() not in ("", "None") else None)
             for row in hackerone),
        )
        db.executemany(
            "INSERT OR IGNORE INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ((row["url"], "Pentester Land", row["title"], row["bugs"],
              row["programs"], row["authors"], row["publication_date"], "external article", "", None)
             for row in pentesterland),
        )
        db.execute("CREATE INDEX entries_published ON entries(published DESC)")
        db.execute("CREATE INDEX entries_bounty ON entries(bounty_usd DESC)")
        count = db.execute("SELECT count(*) FROM entries").fetchone()[0]
    print(f"Built {DATABASE.relative_to(ROOT)} with {count} distinct URLs")
    print("Metadata comes from third-party indexes. Verify each original page before citing it.")


def search(query: str, limit: int) -> None:
    if not DATABASE.exists():
        raise FileNotFoundError("Run 'build' first")
    pattern = f"%{query}%"
    with sqlite3.connect(DATABASE) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            """SELECT source, published, title, url FROM entries
               WHERE title LIKE ? OR topics LIKE ? OR program LIKE ? OR authors LIKE ?
               ORDER BY published DESC LIMIT ?""",
            (pattern, pattern, pattern, pattern, limit),
        ).fetchall()
    for row in rows:
        print(f"{row['published'][:10]}\t{row['source']}\t{row['title']}\t{row['url']}")
    print(f"Showing {len(rows)} result(s); source coverage is incomplete")


def stats() -> None:
    if not DATABASE.exists():
        raise FileNotFoundError("Run 'build' first")
    hackerone_urls = {row["url"] for row in read_csv(DATA / "hackerone-disclosed-index.csv")}
    pentesterland_urls = {row["url"] for row in read_csv(DATA / "pentesterland-writeups.csv")}
    print("HackerOne community index URLs:", len(hackerone_urls))
    print("Pentester Land links:", len(pentesterland_urls))
    print("URLs in both indexes:", len(hackerone_urls & pentesterland_urls))
    with sqlite3.connect(DATABASE) as db:
        print("Distinct URLs:", db.execute("SELECT count(*) FROM entries").fetchone()[0])
        print("Indexed bounty amounts:", db.execute("SELECT count(*) FROM entries WHERE bounty_usd > 0").fetchone()[0])
        print("Indexed bounties >= $10,000:", db.execute("SELECT count(*) FROM entries WHERE bounty_usd >= 10000").fetchone()[0])
        print("Newest disclosure:", db.execute("SELECT max(published) FROM entries WHERE source = 'HackerOne community index'").fetchone()[0])


def top(limit: int, min_bounty: float, year: str | None) -> None:
    if not DATABASE.exists():
        raise FileNotFoundError("Run 'build' first")
    with sqlite3.connect(DATABASE) as db:
        rows = db.execute(
            """SELECT bounty_usd, published, severity, program, title, url FROM entries
               WHERE bounty_usd >= ? AND (? IS NULL OR published LIKE ?)
               ORDER BY bounty_usd DESC, published DESC LIMIT ?""",
            (min_bounty, year, f"{year}%" if year else "", limit),
        ).fetchall()
    for bounty, published, severity, program, title, url in rows:
        print(f"${bounty:,.2f}\t{published[:10]}\t{severity}\t{program}\t{title}\t{url}")
    print("Amounts are third-party index metadata; verify each original report before citing.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "search", "stats", "top"))
    parser.add_argument("query", nargs="?")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--min-bounty", type=float, default=10000)
    parser.add_argument("--year")
    args = parser.parse_args()
    try:
        if args.command == "build":
            build()
        elif args.command == "stats":
            stats()
        elif args.command == "top":
            top(max(1, min(args.limit, 200)), max(0, args.min_bounty), args.year)
        elif args.query:
            search(args.query, max(1, min(args.limit, 200)))
        else:
            parser.error("search requires a query")
    except (FileNotFoundError, sqlite3.Error) as error:
        parser.exit(1, f"Error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
