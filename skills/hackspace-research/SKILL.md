---
name: hackspace-research
description: Research public bug bounty reports, source-checked awards, current advisories, root-cause patterns, and duplicate risk with the local HACKSPACE library. Use for bounty intelligence and lead selection; not for CTF writeups or live target testing.
---

# HACKSPACE bug bounty research

Locate the workbench's `HACKSPACE/README.md` and source register. If the local library is unavailable, say so and use original public sources; do not imply a search was performed. The SQLite index and bulk archives are local-only; do not copy them into public Git or expose private notes.

For report discovery, run `python3 scripts/library.py search '<product or root cause>'`; `top --year YYYY --min-bounty N` sorts third-party index amounts. `prior-art '<root cause or alias>'` searches the smaller curated layer by cause, boundary, versions, fix, and aliases. The link index preserves all source memberships for overlapping URLs. The seven payout seed records have award and summary checks only; `root_cause_and_fix_reviewed` is a separate depth and requires inspection of original sources. Add reviewed records to Git-ignored `HACKSPACE/data/reviewed-prior-art.jsonl` with source URLs and review depth. Open the **original** report to verify visibility, date, observed behavior, fix, and each claimed award. Keep source-checked awards separate from community metadata and current program payout ceilings. Advisory records from OSV, CVE, GHSA, and NVD are context, not first-person bounty reports; match aliases before counting a flaw.

Turn a report into a hypothesis by stating the original trust boundary and root cause, then checking the program's current disclosures, vendor advisories, release notes, and relevant code/version. Record whether the new question concerns the same root, a regression, an incomplete fix, or a distinct boundary. Public research cannot rule out private duplicate reports or promise a payout.

For AI agent, MCP/tool, retrieval, cloud, and sandbox questions, start with `HACKSPACE/research/AI-SECURITY.md`, the public research hub, and the Wiz/XBOW/Hacktron and Gray Swan notes. In controlled agent tests, preserve both the action/tool trace and the user-visible response; an indirect prompt injection that changes words, one that takes an unauthorized action, and one that conceals the action are different outcomes. Vendor benchmarks and public techniques are prior art, not a verified new target finding.

For any proposed lead, return a short private lead card: source URLs and review dates; current scope/policy status; exact hypothesis; evidence needed to falsify it; prior-art comparison; expected impact **if proven**; smallest authorized verification; and stop condition. Track the hypothesis and outcome in the private `lead_queue.py` queue. Use `bug-bounty-workflow` for scoped testing and `finding-validation` before a finding is called supported. Use the synthetic `eval_findings.py` suite to check finding judgment offline, not as evidence about a live target. For reporting or pre-submission triage, follow the user's `ywh-reporting` skill. Research alone grants no authorization for target traffic or submission.
