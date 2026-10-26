---
name: bug-bounty-workflow
description: Plan a scoped, time-efficient bug bounty investigation from current program rules through one falsifiable hypothesis, controlled verification, and evidence-based reporting.
---

# Bug bounty investigation

First establish the current written scope, exclusions, allowed accounts, automation rules, rate limits, and disclosure terms. This skill does not authorize contact with a target. If scope is incomplete, use read-only research and state the one missing fact that blocks active work.

Create a short investigation card: asset and policy source; actor/role; trust boundary; expected control; testable alternative; smallest decisive comparison; stop condition; time/rate budget. Choose a lead by likely security significance, evidence quality, duplicate risk, and current program reward rules, not scanner count or advertised maximum payout alone. Prior public reports are context, not proof that the behavior still exists.

Use `HACKSPACE/private/leads.jsonl` when the workbench is available (`python3 HACKSPACE/scripts/lead_queue.py init` and `rank --show-blocked`). Mark each asset Attackable, Allow Visit, or Blocked from the current policy; track controlled roles, redirects, third parties, automation rules, and the **shared** request budget. Rank Attackable leads by information gain and bounded impact against evidence readiness, duplicate risk, and cost. The numeric score orders questions only. Give each lead a cheap falsifier and stop condition; keep disproved, duplicate, out-of-scope, and completed outcomes with a dated revisit trigger instead of retesting them reflexively.

When a local `HACKSPACE` library is available, search it and the program's own disclosures for product, component, root cause, version, and fix before investing in a lead. Mark an old CVE or report as prior art. Distinguish a separate boundary or incomplete fix with evidence; a private duplicate may still exist, so never promise a unique or paid result. Treat community-index payout numbers as unverified until the original report shows the award, and keep past awards distinct from current program ceilings.

In an authorized Caido project, follow one user journey and label requests by account, role, object, tenant, and time. Preserve a baseline. Change one variable at a time in a controlled replay and compare server behavior with an appropriate negative control. Prefer manually reviewed requests; use automation only when the program permits it and the result remains auditable. Stop after the minimum proof.

The Hermes `default` parent can delegate separate questions to SCOUT and BUGGY with `HACKSPACE/scripts/handoff.py`, then pass original artifact pointers to PROOF for an independent verdict. Do not send PROOF the producer's severity or conclusion before review. One parent owns the ledger and request budget; parallel agents must not each consume the full allowance.

Use `finding-validation` to challenge a promising result and `evidence-capture` to preserve it. Report with the user's `ywh-reporting` or `evidence-based-reporting` skill; unsupported impact belongs in the private working notes, while the final report uses only bounded supported facts. If a hypothesis fails, record the observation briefly and move to the next highest-value question.
