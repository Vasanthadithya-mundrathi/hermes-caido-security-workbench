#!/usr/bin/env python3
"""Run and score synthetic evidence-judgment cases; never contacts a target."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HACKSPACE = Path(__file__).resolve().parents[1]
DEFAULT_CASES = HACKSPACE / "evals" / "cases"
DEFAULT_RUNS = HACKSPACE / "data" / "evals"
VERDICTS = {"supported", "unverified", "disproved", "out_of_scope"}


def read_cases(folder: Path) -> list[dict[str, Any]]:
    cases = []
    for path in sorted(folder.glob("*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(case, dict) or not case.get("id") or case.get("expected_verdict") not in VERDICTS:
            raise ValueError(f"{path}: invalid case metadata")
        cases.append(case)
    if not cases:
        raise ValueError(f"No JSON cases in {folder}")
    return cases


def prompt(case: dict[str, Any]) -> str:
    evidence = {key: value for key, value in case.items() if key not in {"expected_verdict", "must_cite", "forbidden_claims", "evaluator_note"}}
    return (
        "You are independently triaging a synthetic, offline security evidence packet. "
        "It is a reasoning benchmark, not permission to test a target. Use only the packet. "
        "Treat each observation as a synthetic fixture, check competing explanations and scope, "
        "and do not invent requests, logs, consequences, or severity. "
        "Return exactly one JSON object with keys: verdict (supported, unverified, disproved, or out_of_scope), "
        "evidence_ids (array of cited artifact IDs), reason (one concise sentence), "
        "impact (the smallest observed consequence, or empty string).\n\n"
        + json.dumps(evidence, indent=2, ensure_ascii=False)
    )


def parse_answer(output: str) -> dict[str, Any]:
    for match in re.finditer(r"\{", output):
        try:
            answer, _ = json.JSONDecoder().raw_decode(output[match.start():])
        except json.JSONDecodeError:
            continue
        if isinstance(answer, dict) and "verdict" in answer:
            return answer
    raise ValueError("no JSON verdict object in model output")


def score_one(case: dict[str, Any], answer: dict[str, Any]) -> dict[str, Any]:
    ids = {artifact["id"] for artifact in case.get("artifacts", [])}
    citations = answer.get("evidence_ids", [])
    if not isinstance(citations, list):
        citations = []
    cited = {item for item in citations if isinstance(item, str)}
    required = set(case.get("must_cite", []))
    reason = answer.get("reason", "")
    impact = answer.get("impact", "")
    prose = f"{reason} {impact}".lower()
    forbidden = [phrase for phrase in case.get("forbidden_claims", []) if phrase.lower() in prose]
    verdict = answer.get("verdict")
    checks = {
        "verdict": verdict == case["expected_verdict"],
        "known_citations": bool(cited) and cited.issubset(ids),
        "required_controls_cited": required.issubset(cited),
        "no_forbidden_claim": not forbidden,
        "reason_present": isinstance(reason, str) and bool(reason.strip()),
    }
    return {
        "id": case["id"], "expected": case["expected_verdict"], "actual": verdict,
        "checks": checks, "passed": all(checks.values()),
        "false_confirmation": verdict == "supported" and case["expected_verdict"] != "supported",
        "invalid_citations": sorted(cited - ids), "missing_controls": sorted(required - cited),
        "forbidden_claims_found": forbidden,
    }


def read_responses(path: Path) -> dict[str, dict[str, Any]]:
    responses = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        responses[item["case_id"]] = item
    return responses


def report(cases: list[dict[str, Any]], responses: dict[str, dict[str, Any]]) -> dict[str, Any]:
    results = []
    for case in cases:
        item = responses.get(case["id"])
        if not item:
            continue
        if item.get("error"):
            results.append({"id": case["id"], "error": item["error"], "passed": False})
            continue
        results.append(score_one(case, item["answer"]))
    summary = {
        "cases_available": len(cases), "cases_scored": len(results),
        "passed": sum(bool(item.get("passed")) for item in results),
        "false_confirmations": sum(bool(item.get("false_confirmation")) for item in results),
        "results": results,
    }
    return summary


def run_live(cases: list[dict[str, Any]], profile: str, run_budget: int, limit: int) -> Path:
    DEFAULT_RUNS.mkdir(parents=True, exist_ok=True)
    destination = DEFAULT_RUNS / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{profile}"
    destination.mkdir(parents=True, exist_ok=False)
    records = []
    for case in cases[:limit]:
        command = ["hermes", "-p", profile, "chat", "--query-file", "-", "--oneshot", "--quiet", "--max-turns", "1", "--run-budget", str(run_budget)]
        try:
            result = subprocess.run(command, input=prompt(case), text=True, capture_output=True, timeout=run_budget + 30, check=False)
            (destination / f"{case['id']}.raw.txt").write_text(result.stdout + "\nSTDERR:\n" + result.stderr, encoding="utf-8")
            if result.returncode:
                record = {"case_id": case["id"], "error": f"Hermes exited {result.returncode}; inspect private raw output"}
            else:
                try:
                    record = {"case_id": case["id"], "answer": parse_answer(result.stdout)}
                except ValueError as error:
                    record = {"case_id": case["id"], "error": str(error)}
        except (OSError, subprocess.TimeoutExpired) as error:
            record = {"case_id": case["id"], "error": str(error)}
        records.append(record)
        print(f"{case['id']}: {'answered' if 'answer' in record else record['error']}", flush=True)
    response_file = destination / "responses.jsonl"
    response_file.write_text("\n".join(json.dumps(item, ensure_ascii=False) for item in records) + "\n", encoding="utf-8")
    print(f"Private run: {destination}")
    return response_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "run", "score"))
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--responses", type=Path)
    parser.add_argument("--profile", default="proof")
    parser.add_argument("--case", action="append", help="Select a case ID; repeat to select more")
    parser.add_argument("--run-budget", type=int, default=90)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    try:
        cases = read_cases(args.cases)
        if args.case:
            selected = set(args.case)
            cases = [case for case in cases if case["id"] in selected]
            unknown = selected - {case["id"] for case in cases}
            if unknown:
                raise ValueError(f"Unknown case IDs: {', '.join(sorted(unknown))}")
        if args.command == "list":
            for case in cases:
                print(f"{case['id']}: {case['boundary']} [{case['expected_verdict']}]")
            return 0
        if args.command == "run":
            args.responses = run_live(cases, args.profile, max(20, args.run_budget), max(1, args.limit))
        if not args.responses:
            parser.error("score requires --responses")
        summary = report(cases, read_responses(args.responses))
        print(json.dumps(summary, indent=2))
        return 0 if summary["cases_scored"] and summary["passed"] == summary["cases_scored"] else 1
    except (OSError, ValueError, KeyError) as error:
        parser.exit(2, f"Evaluation error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
