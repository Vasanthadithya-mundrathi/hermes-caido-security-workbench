#!/usr/bin/env python3
"""Build a local searchable SQLite index from optional public-link metadata."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
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
            program TEXT, authors TEXT, published TEXT, visibility TEXT
        )""")
        db.executemany(
            "INSERT OR IGNORE INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ((row["url"], "HackerOne community index", row["title"], row["weakness"],
              row["program"], row["reporter"], row["disclosed_at"], row["visibility"])
             for row in hackerone),
        )
        db.executemany(
            "INSERT OR IGNORE INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ((row["url"], "Pentester Land", row["title"], row["bugs"],
              row["programs"], row["authors"], row["publication_date"], "external article")
             for row in pentesterland),
        )
        db.execute("CREATE INDEX entries_published ON entries(published DESC)")
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
    with sqlite3.connect(DATABASE) as db:
        for source, count in db.execute("SELECT source, count(*) FROM entries GROUP BY source ORDER BY source"):
            print(f"{source}: {count}")
        print("Distinct URLs:", db.execute("SELECT count(*) FROM entries").fetchone()[0])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "search", "stats"))
    parser.add_argument("query", nargs="?")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    try:
        if args.command == "build":
            build()
        elif args.command == "stats":
            stats()
        elif args.query:
            search(args.query, max(1, min(args.limit, 200)))
        else:
            parser.error("search requires a query")
    except (FileNotFoundError, sqlite3.Error) as error:
        parser.exit(1, f"Error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
