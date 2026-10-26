"""Offline checks for evidence gating, triage, handoffs, and evaluation."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "HACKSPACE" / "scripts"))
import eval_findings  # noqa: E402
import gate_candidate  # noqa: E402
import handoff  # noqa: E402
import lead_queue  # noqa: E402

AS_OF = date(2026, 10, 26)


class GateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.packet_path = Path(self.workspace.name) / "candidate.json"
        artifacts = []
        for number in range(1, 4):
            path = Path(self.workspace.name) / f"E{number}.txt"
            path.write_text(f"Synthetic observation {number}\n", encoding="utf-8")
            artifacts.append({"id": f"E{number}", "path": str(path), "sha256": gate_candidate.hash_file(path), "provenance": "observed", "fact": f"controlled observation {number}"})
        self.packet = {
            "candidate_id": "LAB-1", "hypothesis": "one controlled role reads another's record",
            "boundary": "tenant to record", "expected_control": "tenant ownership check",
            "scope": {"mode": "owned_lab", "policy_url": "local://owned-fixture", "policy_reviewed_at": "2026-10-26", "asset": "local fixture", "access": "Attackable", "roles": ["A", "B"]},
            "artifacts": artifacts, "baseline_id": "E1", "variant_id": "E2", "negative_control_id": "E3",
            "reproduction": {"attempts": 2, "successes": 2, "state_reset_or_reason": "state restored between trials"},
            "competing_explanations": [{"explanation": "record intentionally shared", "disposition": "ruled_out", "evidence_ids": ["E3"]}],
            "impact_claims": [{"claim": "read one controlled record", "evidence_ids": ["E2"]}],
            "prior_art": {"searched_at": "2026-10-26", "sources": [], "comparison": "no_public_match", "reason": "local training fixture"},
            "independent_review": {"reviewer": "PROOF", "verdict": "supported", "reason": "control distinguishes the records", "evidence_ids": ["E1", "E2", "E3"]},
            "ai_agent": {"enabled": False},
        }

    def test_complete_packet_passes_documentation_gate(self) -> None:
        issues, warnings = gate_candidate.validate(self.packet, self.packet_path, AS_OF)
        self.assertEqual(issues, [])
        self.assertEqual(warnings, [])

    def test_missing_control_and_hash_mismatch_fail(self) -> None:
        candidate = copy.deepcopy(self.packet)
        candidate.pop("negative_control_id")
        candidate["artifacts"][1]["sha256"] = "0" * 64
        issues, _ = gate_candidate.validate(candidate, self.packet_path, AS_OF)
        self.assertTrue(any("negative_control_id" in issue for issue in issues))
        self.assertTrue(any("does not match" in issue for issue in issues))

    def test_unresolved_alternative_and_missing_agent_action_fail(self) -> None:
        candidate = copy.deepcopy(self.packet)
        candidate["competing_explanations"][0]["disposition"] = "open"
        candidate["ai_agent"] = {"enabled": True, "model_and_tools": "test model/tool", "user_visible_evidence_id": "E2", "success_definition": "write occurred", "concealment_claim": True}
        issues, _ = gate_candidate.validate(candidate, self.packet_path, AS_OF)
        self.assertTrue(any("alternative remains open" in issue for issue in issues))
        self.assertTrue(any("action_evidence_id" in issue for issue in issues))

    def test_proof_handoff_withholds_producer_conclusion(self) -> None:
        brief = handoff.proof_brief(self.packet)
        self.assertIn("E1", brief)
        self.assertNotIn("read one controlled record", brief)
        self.assertNotIn("control distinguishes the records", brief)

    def test_bounty_packet_in_public_repo_fails_privacy_gate(self) -> None:
        candidate = copy.deepcopy(self.packet)
        candidate["scope"]["mode"] = "bounty"
        candidate["scope"]["policy_url"] = "https://example.org/program"
        candidate["prior_art"]["sources"] = ["https://example.org/advisory"]
        issues, _ = gate_candidate.validate(candidate, ROOT / "public-candidate.json", AS_OF)
        self.assertTrue(any("inside public Git" in issue for issue in issues))

    def test_placeholder_proof_handoff_is_rejected(self) -> None:
        template = json.loads((ROOT / "HACKSPACE" / "templates" / "candidate-packet.template.json").read_text(encoding="utf-8"))
        with self.assertRaises(ValueError):
            handoff.proof_brief(template)


class LeadTests(unittest.TestCase):
    def setUp(self) -> None:
        path = ROOT / "HACKSPACE" / "templates" / "leads.example.jsonl"
        self.lead = json.loads(path.read_text(encoding="utf-8"))

    def test_ready_synthetic_lead_ranks(self) -> None:
        errors, blockers = lead_queue.assess(self.lead, AS_OF)
        self.assertEqual((errors, blockers), ([], []))
        self.assertGreater(lead_queue.score(self.lead), 0)

    def test_allow_visit_and_stale_policy_cannot_rank(self) -> None:
        self.lead["access"] = "Allow Visit"
        self.lead["policy_reviewed_at"] = "2026-08-01"
        errors, blockers = lead_queue.assess(self.lead, AS_OF)
        self.assertEqual(errors, [])
        self.assertTrue(any("browsing only" in item for item in blockers))
        self.assertTrue(any("older than 30" in item for item in blockers))

    def test_malformed_status_and_scope_report_errors(self) -> None:
        self.lead["status"] = []
        self.lead["scope_mode"] = []
        errors, _ = lead_queue.assess(self.lead, AS_OF)
        self.assertTrue(any("status must" in issue for issue in errors))
        self.assertTrue(any("scope_mode must" in issue for issue in errors))


class EvalTests(unittest.TestCase):
    def test_verdict_and_required_citations(self) -> None:
        cases = {case["id"]: case for case in eval_findings.read_cases(ROOT / "HACKSPACE" / "evals" / "cases")}
        strong = eval_findings.score_one(cases["cross-tenant-canary"], {"verdict": "supported", "evidence_ids": ["E1", "E3", "E4"], "reason": "Controlled B record returned to A", "impact": "one controlled B record read"})
        self.assertTrue(strong["passed"])
        weak = eval_findings.score_one(cases["status-only"], {"verdict": "supported", "evidence_ids": ["E2", "E99"], "reason": "cross-tenant data read", "impact": "sensitive data exposed"})
        self.assertTrue(weak["false_confirmation"])
        self.assertIn("E99", weak["invalid_citations"])
        self.assertFalse(weak["checks"]["no_forbidden_claim"])


if __name__ == "__main__":
    unittest.main()
