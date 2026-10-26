# Research-to-report workflow

This workflow organizes authorized bug bounty and owned-lab work. The scripts rank hypotheses, validate evidence packets, and score offline reasoning. They do not contact a target or establish permission.

## 1. Select a decisive question

Read the current program policy and map each asset or route to **Attackable**, **Allow Visit**, or **Blocked**. Record account roles, redirects, third-party boundaries, automation rules, disclosure terms, and a request budget shared by every agent. Start a private queue with `python3 HACKSPACE/scripts/lead_queue.py init`; copy a record shape from `HACKSPACE/templates/leads.example.jsonl` into `HACKSPACE/private/leads.jsonl`. Run `check` to see missing facts and `rank --show-blocked` to order ready leads. The score is `2×impact + 2×information_gain + evidence_readiness + novelty − duplicate_risk − effort`, with each rating from 1 to 5. This is only a triage heuristic. A large score never overrides scope, rate limits, or a weak hypothesis.

For each lead, state one plausible root cause, the expected control, a falsifier, the smallest permitted comparison, and a stop condition. Research known causes and fixes before spending requests. Keep the outcome even when the hypothesis fails, with a specific reason to revisit it.

## 2. Compare with public prior art

Use `python3 scripts/library.py search 'component or boundary'` for broad discovery and `python3 scripts/library.py prior-art 'root cause or alias'` for the curated layer. The 19,191-link index preserves multiple source memberships per URL. The seven payout seed records are labeled `award_and_summary_checked`; they do not imply their fixes or versions were fully reviewed. [Three public MCP records](reviewed-prior-art.jsonl) show more detailed root-cause, version, and fix-source comparisons with explicit review depth. Add private original-source records to `HACKSPACE/data/reviewed-prior-art.jsonl` using `HACKSPACE/templates/reviewed-prior-art.example.jsonl`, then rebuild the index. Search by aliases, versions, root cause, and fix; distinguish the same root, a regression, an incomplete fix, a distinct boundary, and no public match. A public search cannot rule out a private duplicate.

## 3. Delegate through one parent

The native Hermes `default` profile is the parent orchestrator. It can send a private lead to SCOUT for source checking and BUGGY for a bounded plan. `python3 HACKSPACE/scripts/handoff.py SCOUT HACKSPACE/private/leads.jsonl --lead-id ID` (or `BUGGY` with the same arguments) produces a short brief for one queue entry. Only the parent allocates any permitted active traffic and tracks the shared budget. Codex app-server profiles can answer directly but do not delegate.

After a candidate has original artifacts, the parent runs `python3 HACKSPACE/scripts/handoff.py PROOF HACKSPACE/private/candidate.json` and asks PROOF to inspect the files independently. This brief deliberately omits the producer's impact and verdict. PROOF returns supported, unverified, disproved, or out of scope with cited artifact IDs and competing explanations. Record the verdict and corrections in the private packet.

## 4. Gate the evidence before drafting

Use `HACKSPACE/templates/candidate-packet.template.json` as the field guide. Keep the filled JSON and raw redacted artifacts in `HACKSPACE/private/` or another private workspace. Hash each artifact. Map baseline, changed condition, negative control, reproduction, competing explanations, bounded impact claims, prior-art comparison, and independent review to evidence IDs. For AI-agent work, separately link the untrusted input, action/tool trace, and user-visible reply; record trials, state resets, model/tool versions, and the exact success definition.

Run `python3 HACKSPACE/scripts/gate_candidate.py HACKSPACE/private/candidate.json`. `DOCUMENTATION_READY` means the packet covers required fields and artifact hashes match. It is not a validation of target behavior, severity, payout, or uniqueness. Resolve all factual contradictions with PROOF and the original evidence. For reports, apply `ywh-reporting`; keep provenance, absent-proof questions, and unsupported impact in working notes. The publish-ready report presents the actual check and bounded result.

## 5. Test the agent's judgment offline

Use `python3 HACKSPACE/scripts/eval_findings.py list` and `run --profile proof` to check whether a profile labels synthetic supported, weak, contradictory, out-of-scope, and agent-action cases correctly. The runner stores raw replies and scores in Git-ignored `HACKSPACE/data/evals/`. Its checks cover false confirmations, evidence IDs, required controls, and overclaim phrases. These fixtures test reasoning quality; they do not verify any real finding.
