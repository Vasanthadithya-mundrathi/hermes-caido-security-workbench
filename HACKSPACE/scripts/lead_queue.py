#!/usr/bin/env python3
"""Rank private bug-bounty hypotheses without sending target traffic."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

DEFAULT_QUEUE = Path(__file__).resolve().parents[1] / "private" / "leads.jsonl"
RATINGS = ("impact", "evidence_readiness", "information_gain", "novelty", "duplicate_risk", "effort")
TERMINAL_STATES = {"disproved", "duplicate", "reported", "closed"}


def read_queue(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist; run lead_queue.py init")
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"line {line_number}: invalid JSON ({error.msg})") from error
        if not isinstance(record, dict):
            raise ValueError(f"line {line_number}: expected a JSON object")
        records.append(record)
    return records


def score(record: dict[str, Any]) -> int:
    """Relative triage score, never severity, exploitability, or expected payout."""
    return (
        2 * record["impact"] + 2 * record["information_gain"]
        + record["evidence_readiness"] + record["novelty"]
        - record["duplicate_risk"] - record["effort"]
    )


def assess(record: dict[str, Any], as_of: date) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    blockers: list[str] = []
    for key in ("id", "program", "asset", "hypothesis", "decisive_check", "stop_condition", "automation_rule", "redirect_rule", "third_party_rule"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            errors.append(f"{key} is required")
    for key in RATINGS:
        value = record.get(key)
        if type(value) is not int or not 1 <= value <= 5:
            errors.append(f"{key} must be an integer from 1 to 5")
    status = record.get("status")
    if not isinstance(status, str) or status not in {"idea", "researching", "ready", "testing", *TERMINAL_STATES}:
        errors.append("status must be idea, researching, ready, testing, disproved, duplicate, reported, or closed")
    mode = record.get("scope_mode")
    if not isinstance(mode, str) or mode not in {"bounty", "owned_lab"}:
        errors.append("scope_mode must be bounty or owned_lab")
    access = record.get("access")
    if not isinstance(access, str) or access not in {"Attackable", "Allow Visit", "Blocked"}:
        errors.append("access must be Attackable, Allow Visit, or Blocked")
    roles = record.get("account_roles")
    if not isinstance(roles, list) or not roles or not all(isinstance(role, str) and role.strip() for role in roles):
        errors.append("account_roles must list controlled role labels")
    remaining, planned = record.get("budget_remaining"), record.get("planned_requests")
    if type(remaining) is not int or remaining < 0 or type(planned) is not int or planned < 0:
        errors.append("budget_remaining and planned_requests must be nonnegative integers")
    policy_url = record.get("policy_url")
    if not isinstance(policy_url, str) or not policy_url.strip():
        blockers.append("policy source is missing")
    elif mode == "bounty" and not policy_url.startswith("https://"):
        blockers.append("bounty policy needs an HTTPS source")
    try:
        reviewed = date.fromisoformat(record.get("policy_reviewed_at", ""))
        if reviewed > as_of or (as_of - reviewed).days > 30:
            blockers.append("policy review date is future or older than 30 days")
    except (TypeError, ValueError):
        blockers.append("policy_reviewed_at must be a current YYYY-MM-DD date")
    if access == "Blocked":
        blockers.append("asset is Blocked")
    elif access == "Allow Visit":
        blockers.append("asset permits reference browsing only")
    if isinstance(status, str) and status in TERMINAL_STATES:
        blockers.append(f"lead is {status}")
    elif status not in ("ready", "testing"):
        blockers.append("lead has not been marked ready")
    if not isinstance(record.get("automation_rule"), str) or record["automation_rule"] not in {"manual_only", "automation_permitted"}:
        blockers.append("automation rule is unknown or prohibits the planned work")
    for key in ("redirect_rule", "third_party_rule"):
        if record.get(key) == "unknown":
            blockers.append(f"{key} is unknown")
    if type(remaining) is int and type(planned) is int:
        if planned == 0:
            blockers.append("planned_requests is zero")
        elif planned > remaining:
            blockers.append("planned requests exceed the remaining shared budget")
    return errors, blockers


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("init", "check", "rank", "summary"))
    parser.add_argument("--file", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    parser.add_argument("--limit", type=int, default=15)
    parser.add_argument("--show-blocked", action="store_true")
    args = parser.parse_args()
    if args.command == "init":
        args.file.parent.mkdir(parents=True, exist_ok=True)
        if args.file.exists():
            print(f"Exists: {args.file}")
        else:
            args.file.write_text("", encoding="utf-8")
            print(f"Created private queue: {args.file}")
        return 0
    try:
        records = read_queue(args.file)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Queue error: {error}\n")
    seen = set()
    ready = []
    blocked = []
    invalid_count = 0
    for index, record in enumerate(records, 1):
        label = record.get("id") if isinstance(record.get("id"), str) else f"line {index}"
        errors, blockers = assess(record, args.as_of)
        if label in seen:
            errors.append("duplicate lead ID")
        seen.add(label)
        if errors:
            invalid_count += 1
            print(f"INVALID {label}: {'; '.join(errors)}")
        elif blockers:
            blocked.append((label, blockers))
        else:
            ready.append((score(record), record))
    if args.command == "check":
        print(f"{len(records)} leads: {len(ready)} ready, {len(blocked)} research-only/blocked, {invalid_count} invalid")
        for label, reasons in blocked:
            print(f"RESEARCH_ONLY {label}: {'; '.join(reasons)}")
    elif args.command == "summary":
        counts: dict[str, int] = {}
        for record in records:
            state = str(record.get("status", "missing"))
            counts[state] = counts.get(state, 0) + 1
        print(json.dumps({"total": len(records), "ready_for_rank": len(ready), "research_only_or_closed": len(blocked), "by_status": counts}, indent=2))
    else:
        for priority, record in sorted(ready, key=lambda item: (-item[0], item[1]["id"]))[: max(1, args.limit)]:
            print(f"{priority:>2}  {record['id']}  {record['program']}  {record['asset']}")
            print(f"    hypothesis: {record['hypothesis']}")
            print(f"    decisive check: {record['decisive_check']} ({record['planned_requests']} planned requests)")
        if args.show_blocked:
            for label, reasons in blocked:
                print(f"RESEARCH_ONLY {label}: {'; '.join(reasons)}")
        print("Priority is a relative triage heuristic, not permission, severity, uniqueness, or expected payout.")
    return 1 if invalid_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
