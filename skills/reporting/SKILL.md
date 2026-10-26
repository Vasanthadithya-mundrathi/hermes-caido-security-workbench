---
name: evidence-based-reporting
description: Draft or review a bug bounty report from supplied evidence, with explicit boundaries between observed facts, reported observations, inference, and unknowns.
---

# Evidence-based reporting

Use the program's current template and rules if provided. Inspect existing notes and artifacts without executing requests or testing a target. Do not invent discovery history, versions, requests, screenshots, successful outcomes, or impact.

Draft a concise title, affected asset, description, preconditions, evidence/steps already observed, expected versus actual behavior, demonstrated impact, and remediation when supported. Link each factual claim to an artifact or citation. Label researcher-reported details separately from what you personally inspected. Leave missing proof as an explicit gap.

For triage, decide whether the supplied documentation is ready, needs fixes, or should not be submitted, and name only material gaps. Scope and program exclusions must be checked. Severity follows supported effects and the program's required method; a vulnerability class alone is not a score. Do not publish or submit a report without the user's explicit request.

Use `templates/bug-report.md` and `templates/evidence-ledger.md`. The local Codex `ywh-reporting` skill is the fuller workflow when available.
