#!/usr/bin/env python3
"""Check a private finding packet for documented evidence, not bug validity."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SHA256 = re.compile(r"[0-9a-f]{64}")


def filled(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and not value.strip().startswith("[")


def require_text(item: dict[str, Any], key: str, label: str, issues: list[str]) -> str:
    value = item.get(key)
    if not filled(value):
        issues.append(f"{label}.{key}: provide a specific value")
        return ""
    return value.strip()


def parse_date(value: Any, label: str, as_of: date, issues: list[str], *, max_age: int | None = None) -> None:
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError):
        issues.append(f"{label}: use YYYY-MM-DD")
        return
    if parsed > as_of:
        issues.append(f"{label}: date is in the future")
    if max_age is not None and (as_of - parsed).days > max_age:
        issues.append(f"{label}: review is older than {max_age} days; refresh before submission")


def within_private_area(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(ROOT)
    except ValueError:
        return True  # A private workspace outside this public repository.
    return relative.parts[:2] in {("HACKSPACE", "private"), ("HACKSPACE", "data")}


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate(candidate: dict[str, Any], packet_path: Path, as_of: date) -> tuple[list[str], list[str]]:
    issues: list[str] = []
    warnings: list[str] = []
    require_text(candidate, "candidate_id", "candidate", issues)
    require_text(candidate, "hypothesis", "candidate", issues)
    require_text(candidate, "boundary", "candidate", issues)
    require_text(candidate, "expected_control", "candidate", issues)

    scope = candidate.get("scope")
    if not isinstance(scope, dict):
        scope = {}
        issues.append("scope: provide a scope object")
    mode = scope.get("mode")
    if not isinstance(mode, str) or mode not in {"bounty", "owned_lab"}:
        issues.append("scope.mode: use bounty or owned_lab")
    if scope.get("access") != "Attackable":
        issues.append("scope.access: only an explicitly Attackable asset can pass this gate")
    policy_url = require_text(scope, "policy_url", "scope", issues)
    if mode == "bounty" and not policy_url.startswith("https://"):
        issues.append("scope.policy_url: bounty policy must be an HTTPS source")
    parse_date(scope.get("policy_reviewed_at"), "scope.policy_reviewed_at", as_of, issues, max_age=30)
    require_text(scope, "asset", "scope", issues)
    roles = scope.get("roles")
    if not isinstance(roles, list) or not roles or not all(filled(role) for role in roles):
        issues.append("scope.roles: provide the controlled account/role labels")
    if mode == "bounty" and not within_private_area(packet_path):
        issues.append("candidate packet is inside public Git; move it to HACKSPACE/private or an external private workspace")

    artifacts = candidate.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        artifacts = []
        issues.append("artifacts: provide baseline and observed evidence")
    by_id: dict[str, dict[str, Any]] = {}
    for index, artifact in enumerate(artifacts):
        label = f"artifacts[{index}]"
        if not isinstance(artifact, dict):
            issues.append(f"{label}: expected object")
            continue
        evidence_id = require_text(artifact, "id", label, issues)
        if evidence_id in by_id:
            issues.append(f"{label}.id: duplicate evidence ID {evidence_id}")
        elif evidence_id:
            by_id[evidence_id] = artifact
        require_text(artifact, "fact", label, issues)
        if not isinstance(artifact.get("provenance"), str) or artifact["provenance"] not in {"observed", "researcher_reported", "reference"}:
            issues.append(f"{label}.provenance: use observed, researcher_reported, or reference")
        relative_path = require_text(artifact, "path", label, issues)
        digest = artifact.get("sha256")
        if not isinstance(digest, str) or not SHA256.fullmatch(digest.lower()):
            issues.append(f"{label}.sha256: provide the file's 64-character SHA-256")
        if relative_path:
            path = Path(relative_path)
            if not path.is_absolute():
                path = packet_path.parent / path
            if mode == "bounty" and not within_private_area(path):
                issues.append(f"{label}.path: keep bounty evidence outside public Git")
            try:
                actual = hash_file(path)
                if isinstance(digest, str) and actual != digest.lower():
                    issues.append(f"{label}.sha256: file does not match the recorded hash")
            except (OSError, ValueError) as error:
                issues.append(f"{label}.path: cannot read evidence file ({error.__class__.__name__})")

    def evidence_ref(value: Any, label: str, *, observed: bool = True) -> None:
        if not filled(value) or value not in by_id:
            issues.append(f"{label}: reference an existing evidence ID")
        elif observed and by_id[value].get("provenance") != "observed":
            issues.append(f"{label}: report-ready claims require directly observed evidence")

    baseline = candidate.get("baseline_id")
    variant = candidate.get("variant_id")
    evidence_ref(baseline, "baseline_id")
    evidence_ref(variant, "variant_id")
    if baseline and baseline == variant:
        issues.append("baseline_id and variant_id must differ")
    control = candidate.get("negative_control_id")
    if control:
        evidence_ref(control, "negative_control_id")
        if isinstance(control, str) and control in (baseline, variant):
            issues.append("negative_control_id must differ from the baseline and variant")
    elif not filled(candidate.get("negative_control_exception")):
        issues.append("negative_control_id: provide a control or a specific safety/feasibility exception")
    else:
        warnings.append("negative control omitted with an explicit exception; reviewer must assess its effect")

    reproduction = candidate.get("reproduction")
    if not isinstance(reproduction, dict):
        reproduction = {}
        issues.append("reproduction: record the controlled runs")
    attempts, successes = reproduction.get("attempts"), reproduction.get("successes")
    if type(attempts) is not int or attempts < 1 or type(successes) is not int or not 0 <= successes <= attempts:
        issues.append("reproduction: attempts must be positive and successes between zero and attempts")
    elif attempts == 1:
        warnings.append("one controlled run recorded; assess whether a repeat would add value safely")
    require_text(reproduction, "state_reset_or_reason", "reproduction", issues)

    explanations = candidate.get("competing_explanations")
    if not isinstance(explanations, list) or not explanations:
        issues.append("competing_explanations: record at least one plausible alternative")
        explanations = []
    for index, explanation in enumerate(explanations):
        label = f"competing_explanations[{index}]"
        if not isinstance(explanation, dict):
            issues.append(f"{label}: expected object")
            continue
        require_text(explanation, "explanation", label, issues)
        if explanation.get("disposition") != "ruled_out":
            issues.append(f"{label}: an alternative remains open")
        refs = explanation.get("evidence_ids")
        if not isinstance(refs, list) or not refs:
            issues.append(f"{label}.evidence_ids: cite the control that ruled it out")
        else:
            for ref in refs:
                evidence_ref(ref, f"{label}.evidence_ids")

    claims = candidate.get("impact_claims")
    if not isinstance(claims, list) or not claims:
        issues.append("impact_claims: give at least one bounded observed consequence")
        claims = []
    for index, claim in enumerate(claims):
        label = f"impact_claims[{index}]"
        if not isinstance(claim, dict):
            issues.append(f"{label}: expected object")
            continue
        require_text(claim, "claim", label, issues)
        refs = claim.get("evidence_ids")
        if not isinstance(refs, list) or not refs:
            issues.append(f"{label}.evidence_ids: cite directly observed artifacts")
        else:
            for ref in refs:
                evidence_ref(ref, f"{label}.evidence_ids")

    prior = candidate.get("prior_art")
    if not isinstance(prior, dict):
        prior = {}
        issues.append("prior_art: record original-source comparison")
    parse_date(prior.get("searched_at"), "prior_art.searched_at", as_of, issues, max_age=30)
    sources = prior.get("sources")
    if mode == "bounty" and (not isinstance(sources, list) or not sources or not all(isinstance(source, str) and source.startswith("https://") for source in sources)):
        issues.append("prior_art.sources: list HTTPS original disclosures/advisories searched")
    if not isinstance(prior.get("comparison"), str) or prior["comparison"] not in {"distinct_root", "regression", "incomplete_fix", "no_public_match"}:
        issues.append("prior_art.comparison: use distinct_root, regression, incomplete_fix, or no_public_match")
    require_text(prior, "reason", "prior_art", issues)

    review = candidate.get("independent_review")
    if not isinstance(review, dict):
        review = {}
        issues.append("independent_review: obtain a PROOF or other independent verdict")
    require_text(review, "reviewer", "independent_review", issues)
    if review.get("verdict") != "supported":
        issues.append("independent_review.verdict: independent reviewer has not marked this supported")
    require_text(review, "reason", "independent_review", issues)
    refs = review.get("evidence_ids")
    if not isinstance(refs, list) or not refs:
        issues.append("independent_review.evidence_ids: identify what the reviewer inspected")
    else:
        for ref in refs:
            evidence_ref(ref, "independent_review.evidence_ids")

    ai_agent = candidate.get("ai_agent")
    if isinstance(ai_agent, dict) and ai_agent.get("enabled") is True:
        require_text(ai_agent, "model_and_tools", "ai_agent", issues)
        evidence_ref(ai_agent.get("action_evidence_id"), "ai_agent.action_evidence_id")
        evidence_ref(ai_agent.get("user_visible_evidence_id"), "ai_agent.user_visible_evidence_id")
        require_text(ai_agent, "success_definition", "ai_agent", issues)
        if ai_agent.get("concealment_claim") is True and ai_agent.get("action_evidence_id") == ai_agent.get("user_visible_evidence_id"):
            issues.append("ai_agent: concealed action and visible response need separate traces")
    return issues, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="Private JSON finding packet")
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today(), help="Evaluation date YYYY-MM-DD")
    parser.add_argument("--json", action="store_true", help="Machine-readable result")
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        parser.exit(2, f"Cannot read packet: {error}\n")
    if not isinstance(packet, dict):
        parser.exit(2, "Packet must be a JSON object\n")
    issues, warnings = validate(packet, args.packet.resolve(), args.as_of)
    result = {
        "status": "DOCUMENTATION_READY" if not issues else "NEEDS_EVIDENCE",
        "issues": issues,
        "warnings": warnings,
        "note": "This checks documentation and file hashes, not target scope, bug validity, novelty, severity, or bounty eligibility.",
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["status"])
        for issue in issues:
            print(f"- {issue}")
        for warning in warnings:
            print(f"! {warning}")
        print(result["note"])
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
