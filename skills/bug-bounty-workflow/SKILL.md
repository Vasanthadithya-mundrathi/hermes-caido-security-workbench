---
name: bug-bounty-workflow
description: Plan a scoped, time-efficient bug bounty investigation from current program rules through one falsifiable hypothesis, controlled verification, and evidence-based reporting.
---

# Bug bounty investigation

First establish the current written scope, exclusions, allowed accounts, automation rules, rate limits, and disclosure terms. This skill does not authorize contact with a target. If scope is incomplete, use read-only research and state the one missing fact that blocks active work.

Create a short investigation card: asset and policy source; actor/role; trust boundary; expected control; testable alternative; smallest decisive comparison; stop condition; time/rate budget. Choose a lead by likely security significance and evidence quality, not scanner count or novelty alone. Prior public reports are context, not proof that the behavior still exists.

In an authorized Caido project, follow one user journey and label requests by account, role, object, tenant, and time. Preserve a baseline. Change one variable at a time in a controlled replay and compare server behavior with an appropriate negative control. Prefer manually reviewed requests; use automation only when the program permits it and the result remains auditable. Stop after the minimum proof.

Use `finding-validation` to challenge a promising result and `evidence-capture` to preserve it. Report with `evidence-based-reporting`; unsupported impact belongs in an explicit question or caveat. If a hypothesis fails, record the observation briefly and move to the next highest-value question.
