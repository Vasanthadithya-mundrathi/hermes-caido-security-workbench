#!/usr/bin/env python3
"""Build small, artifact-first briefs for parent-mediated Hermes delegation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from gate_candidate import SHA256, hash_file
from lead_queue import read_queue


def lines_of_scope(scope: dict[str, Any]) -> list[str]:
    roles = scope.get("roles", scope.get("account_roles", []))
    if not isinstance(roles, list):
        roles = []
    return [
        f"- Program policy: {scope.get('policy_url', '[missing]')} (reviewed {scope.get('policy_reviewed_at', '[missing]')})",
        f"- Asset/access: {scope.get('asset', '[missing]')} / {scope.get('access', '[missing]')}",
        f"- Controlled roles: {', '.join(role for role in roles if isinstance(role, str))}",
    ]


def lead_brief(lead: dict[str, Any], role: str) -> str:
    if role not in {"BUGGY", "SCOUT"}:
        raise ValueError("lead brief supports BUGGY or SCOUT")
    if not all(isinstance(lead.get(key), str) and lead[key].strip() for key in ("id", "policy_url", "asset", "access", "hypothesis")) or not isinstance(lead.get("account_roles"), list):
        raise ValueError("lead handoff requires a lead-queue record with id, scope, roles, and hypothesis")
    scope = {
        "policy_url": lead.get("policy_url"),
        "policy_reviewed_at": lead.get("policy_reviewed_at"),
        "asset": lead.get("asset"),
        "access": lead.get("access"),
        "account_roles": lead.get("account_roles", []),
    }
    header = [f"# {role} handoff — {lead.get('id', '[missing ID]')}", "", "## Scope", *lines_of_scope(scope)]
    header += [
        f"- Automation: {lead.get('automation_rule', '[missing]')}",
        f"- Redirects: {lead.get('redirect_rule', '[missing]')}",
        f"- Third parties: {lead.get('third_party_rule', '[missing]')}",
        f"- Shared budget: {lead.get('budget_remaining', '[missing]')} remaining; {lead.get('planned_requests', '[missing]')} planned",
        "", "## Question",
        f"- Hypothesis: {lead.get('hypothesis', '[missing]')}",
        f"- Proposed decisive check: {lead.get('decisive_check', '[missing]')}",
        f"- Stop condition: {lead.get('stop_condition', '[missing]')}", "",
    ]
    if role == "SCOUT":
        header += ["Find current primary sources and original reports/advisories. Compare root causes, versions, fixes, and aliases. Return dated URLs and contradictions. Research only; do not send target traffic or claim a private duplicate has been excluded."]
    else:
        header += ["Build a bounded test plan and identify the cheapest decisive baseline, changed condition, and negative control. Do not initiate traffic unless the parent separately confirms current scope, account control, method, and shared request budget. Return evidence IDs and failed hypotheses to the parent."]
    return "\n".join(header) + "\n"


def proof_brief(packet: dict[str, Any], packet_path: Path | None = None) -> str:
    if not isinstance(packet.get("candidate_id"), str) or not packet["candidate_id"].strip() or packet["candidate_id"].startswith("["):
        raise ValueError("PROOF handoff requires a candidate packet with candidate_id")
    scope = packet.get("scope", {})
    if not isinstance(scope, dict):
        raise ValueError("candidate scope must be an object")
    artifacts = packet.get("artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError("candidate artifacts must be a nonempty list")
    for artifact in artifacts:
        if not isinstance(artifact, dict) or not all(isinstance(artifact.get(key), str) and artifact[key].strip() and not artifact[key].startswith("[") for key in ("id", "path", "sha256")) or not SHA256.fullmatch(artifact["sha256"].lower()):
            raise ValueError("each PROOF artifact needs a real ID, path, and SHA-256")
        path = Path(artifact["path"])
        if not path.is_absolute() and packet_path:
            path = packet_path.parent / path
        try:
            if hash_file(path) != artifact["sha256"].lower():
                raise ValueError(f"{artifact['id']}: evidence file hash mismatch")
        except OSError as error:
            raise ValueError(f"{artifact['id']}: cannot read evidence file ({error.__class__.__name__})") from error
    result = [f"# PROOF handoff — {packet.get('candidate_id', '[missing ID]')}", "", "## Scope", *lines_of_scope(scope), "", "## Hypothesis to falsify", f"- Hypothesis: {packet.get('hypothesis', '[missing]')}", f"- Boundary: {packet.get('boundary', '[missing]')}", f"- Expected control: {packet.get('expected_control', '[missing]')}", "", "## Original artifacts (inspect files; summary facts are producer claims)"]
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        result.append(f"- {artifact.get('id', '?')}: {artifact.get('path', '[missing path]')} | sha256 {artifact.get('sha256', '[missing]')} | {artifact.get('provenance', '[missing]')} | asserted fact: {artifact.get('fact', '[missing]')}")
    result += [
        "", "## Control pointers",
        f"- Baseline: {packet.get('baseline_id', '[missing]')}",
        f"- Changed condition: {packet.get('variant_id', '[missing]')}",
        f"- Negative control: {packet.get('negative_control_id', '[missing]')}",
        f"- Exception, if any: {packet.get('negative_control_exception', '')}",
        "", "Independently inspect the files and hashes. Look for benign alternatives, inconsistent roles/state/timing, missing conditions, and disproof. Return supported / unverified / disproved / out of scope, with exact artifact IDs and a bounded observed consequence. Do not assume the producer's severity, payout, or report conclusion. No new target traffic unless the parent separately authorizes and budgets it.",
    ]
    return "\n".join(result) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("role", choices=("BUGGY", "SCOUT", "PROOF"))
    parser.add_argument("packet", type=Path, help="private JSON packet, or JSONL queue with --lead-id")
    parser.add_argument("--lead-id", help="select one lead ID from a private JSONL queue")
    args = parser.parse_args()
    try:
        if args.lead_id:
            if args.role == "PROOF":
                raise ValueError("--lead-id applies only to BUGGY or SCOUT")
            matches = [row for row in read_queue(args.packet) if row.get("id") == args.lead_id]
            if len(matches) != 1:
                raise ValueError(f"expected exactly one lead with ID {args.lead_id}; found {len(matches)}")
            packet = matches[0]
        else:
            packet = json.loads(args.packet.read_text(encoding="utf-8"))
        if not isinstance(packet, dict):
            raise ValueError("packet must be a JSON object")
        print(proof_brief(packet, args.packet.resolve()) if args.role == "PROOF" else lead_brief(packet, args.role), end="")
    except (OSError, ValueError) as error:
        parser.exit(2, f"Handoff error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
