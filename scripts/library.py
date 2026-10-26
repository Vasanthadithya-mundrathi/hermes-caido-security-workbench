#!/usr/bin/env python3
"""Build a local searchable SQLite index from optional public-link metadata."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "HACKSPACE" / "data"
DATABASE = DATA / "library.sqlite"
REVIEWED = DATA / "reviewed-prior-art.jsonl"
PUBLIC_REVIEWED = ROOT / "HACKSPACE" / "reviewed-prior-art.jsonl"
PAYOUT_SEEDS = ROOT / "HACKSPACE" / "high-payout-reports.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path.relative_to(ROOT)}; run its sync script first")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def reviewed_records() -> list[dict]:
    """Read public and optional private, human-reviewed original-source records."""
    records = []
    seen = set()
    for path in (PUBLIC_REVIEWED, REVIEWED):
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{number}: invalid JSON ({error.msg})") from error
            if not isinstance(record, dict) or not all(record.get(key) for key in ("id", "title", "root_cause", "reviewed_at")):
                raise ValueError(f"{path}:{number}: id, title, root_cause, reviewed_at required")
            if record["id"] in seen:
                raise ValueError(f"{path}:{number}: duplicate reviewed ID {record['id']}")
            seen.add(record["id"])
            sources = record.get("sources")
            if not isinstance(sources, list) or not sources or not all(isinstance(item, dict) and str(item.get("url", "")).startswith("https://") and item.get("role") for item in sources):
                raise ValueError(f"{path}:{number}: sources needs HTTPS URL/role objects")
            if not isinstance(record.get("aliases", []), list):
                raise ValueError(f"{path}:{number}: aliases must be a list")
            if record.get("review_depth") not in {"root_cause_reviewed", "advisory_root_and_patch_version_checked", "root_cause_and_fix_reviewed"}:
                raise ValueError(f"{path}:{number}: unsupported review_depth")
            records.append(record)
    return records


def build() -> None:
    hackerone = read_csv(DATA / "hackerone-disclosed-index.csv")
    pentesterland = read_csv(DATA / "pentesterland-writeups.csv")
    payout_seeds = read_csv(PAYOUT_SEEDS)
    reviewed = reviewed_records()
    DATA.mkdir(parents=True, exist_ok=True)
    temporary = DATABASE.with_suffix(".sqlite.tmp")
    temporary.unlink(missing_ok=True)
    db = sqlite3.connect(temporary)
    try:
        db.execute("""CREATE TABLE entries (
            url TEXT PRIMARY KEY, source TEXT NOT NULL, title TEXT, topics TEXT,
            program TEXT, authors TEXT, published TEXT, visibility TEXT,
            severity TEXT, bounty_usd REAL
        )""")
        db.execute("CREATE TABLE entry_sources (url TEXT NOT NULL, source TEXT NOT NULL, PRIMARY KEY(url, source))")
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
        db.executemany("INSERT OR IGNORE INTO entry_sources VALUES (?, ?)", ((row["url"], "HackerOne community index") for row in hackerone))
        db.executemany("INSERT OR IGNORE INTO entry_sources VALUES (?, ?)", ((row["url"], "Pentester Land") for row in pentesterland))
        db.execute("""CREATE TABLE prior_art (
            id TEXT PRIMARY KEY, title TEXT NOT NULL, program TEXT, bug_class TEXT,
            root_cause TEXT NOT NULL, trust_boundary TEXT, affected_versions TEXT,
            fixed_versions TEXT, fix_summary TEXT, aliases TEXT, reviewed_at TEXT,
            review_depth TEXT NOT NULL, award_usd REAL
        )""")
        db.execute("""CREATE TABLE prior_art_sources (
            record_id TEXT NOT NULL, url TEXT NOT NULL, role TEXT NOT NULL,
            PRIMARY KEY(record_id, url, role)
        )""")
        for row in payout_seeds:
            record_id = f"payout:{row['report_id']}"
            db.execute(
                "INSERT INTO prior_art VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (record_id, f"{row['program']}: {row['bug_class']}", row["program"], row["bug_class"],
                 row["root_cause_summary"], "", "", "", "", "[]", row["reviewed_at"],
                 "award_and_summary_checked", float(row["award_usd"])),
            )
            db.execute("INSERT INTO prior_art_sources VALUES (?, ?, ?)", (record_id, row["original_url"], "original_report"))
        for row in reviewed:
            record_id = f"reviewed:{row['id']}"
            db.execute(
                "INSERT INTO prior_art VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (record_id, row["title"], row.get("program", ""), row.get("bug_class", ""), row["root_cause"],
                 row.get("trust_boundary", ""), row.get("affected_versions", ""), row.get("fixed_versions", ""),
                 row.get("fix_summary", ""), json.dumps(row.get("aliases", []), ensure_ascii=False),
                 row["reviewed_at"], row.get("review_depth", "root_cause_reviewed"), row.get("award_usd")),
            )
            db.executemany("INSERT OR IGNORE INTO prior_art_sources VALUES (?, ?, ?)",
                           ((record_id, source["url"], source["role"]) for source in row["sources"]))
        db.execute("CREATE INDEX entries_published ON entries(published DESC)")
        db.execute("CREATE INDEX entries_bounty ON entries(bounty_usd DESC)")
        db.execute("CREATE INDEX prior_art_program ON prior_art(program)")
        count = db.execute("SELECT count(*) FROM entries").fetchone()[0]
        prior_count = db.execute("SELECT count(*) FROM prior_art").fetchone()[0]
        db.commit()
    except Exception:
        db.close()
        temporary.unlink(missing_ok=True)
        raise
    db.close()
    os.replace(temporary, DATABASE)
    print(f"Built {DATABASE.relative_to(ROOT)} with {count} distinct URLs")
    print(f"Preserved source memberships and indexed {prior_count} reviewed/seed prior-art records")
    print("Metadata comes from third-party indexes. Verify each original page before citing it.")


def search(query: str, limit: int) -> None:
    if not DATABASE.exists():
        raise FileNotFoundError("Run 'build' first")
    pattern = f"%{query}%"
    with sqlite3.connect(DATABASE) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            """SELECT entries.published, entries.title, entries.url,
                      (SELECT group_concat(source, ' + ') FROM entry_sources
                       WHERE entry_sources.url = entries.url) AS sources
               FROM entries
               WHERE title LIKE ? OR topics LIKE ? OR program LIKE ? OR authors LIKE ?
               ORDER BY published DESC LIMIT ?""",
            (pattern, pattern, pattern, pattern, limit),
        ).fetchall()
    for row in rows:
        print(f"{row['published'][:10]}\t{row['sources']}\t{row['title']}\t{row['url']}")
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
        print("Source memberships:", db.execute("SELECT count(*) FROM entry_sources").fetchone()[0])
        print("Curated prior-art records:", db.execute("SELECT count(*) FROM prior_art").fetchone()[0])
        print("Prior-art original-source links:", db.execute("SELECT count(*) FROM prior_art_sources").fetchone()[0])
        print("Prior-art records with fix review:", db.execute("SELECT count(*) FROM prior_art WHERE review_depth = 'root_cause_and_fix_reviewed'").fetchone()[0])
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


def prior_art(query: str, limit: int) -> None:
    if not DATABASE.exists():
        raise FileNotFoundError("Run 'build' first")
    pattern = f"%{query}%"
    with sqlite3.connect(DATABASE) as db:
        db.row_factory = sqlite3.Row
        rows = db.execute(
            """SELECT * FROM prior_art WHERE title LIKE ? OR program LIKE ? OR bug_class LIKE ?
               OR root_cause LIKE ? OR trust_boundary LIKE ? OR affected_versions LIKE ?
               OR fixed_versions LIKE ? OR fix_summary LIKE ? OR aliases LIKE ?
               ORDER BY reviewed_at DESC LIMIT ?""",
            (*([pattern] * 9), limit),
        ).fetchall()
        for row in rows:
            sources = db.execute("SELECT url, role FROM prior_art_sources WHERE record_id = ? ORDER BY role, url", (row["id"],)).fetchall()
            print(f"{row['id']}  {row['review_depth']}  reviewed {row['reviewed_at']}")
            print(f"  {row['title']} | {row['program']} | {row['bug_class']}")
            print(f"  Root cause: {row['root_cause']}")
            if row["trust_boundary"]:
                print(f"  Boundary: {row['trust_boundary']}")
            if row["affected_versions"] or row["fixed_versions"]:
                print(f"  Versions: affected {row['affected_versions'] or 'unknown'}; fixed {row['fixed_versions'] or 'unknown'}")
            if row["fix_summary"]:
                print(f"  Fix: {row['fix_summary']}")
            for url, role in sources:
                print(f"  {role}: {url}")
    print(f"Showing {len(rows)} result(s). A prior-art match is a research lead, not a private-duplicate verdict.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "search", "stats", "top", "prior-art"))
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
        elif args.command == "prior-art" and args.query:
            prior_art(args.query, max(1, min(args.limit, 100)))
        elif args.query:
            search(args.query, max(1, min(args.limit, 200)))
        else:
            parser.error("search and prior-art require a query")
    except (FileNotFoundError, ValueError, sqlite3.Error) as error:
        parser.exit(1, f"Error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
