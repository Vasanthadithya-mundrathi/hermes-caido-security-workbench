---
name: finding-validation
description: Check whether a proposed bug bounty finding is reproducible, in scope, security-relevant, and supported by controlled evidence before reporting.
---

# Finding validation

Separate the hypothesis from the observations. Identify the claimed boundary, required roles and preconditions, the exact evidence artifact, and a competing benign explanation. A scanner alert, one HTTP status, a client-side UI change, or a model prediction is not sufficient by itself.

For an authorized live test, compare an expected baseline with one changed input or identity. Use a negative control where feasible, confirm that the server-side effect belongs to the controlled test account, and repeat only enough to rule out caching, timing, or stale state. Do not access unrelated users' data or cause unnecessary changes. If testing is not authorized, inspect supplied evidence only and mark reproduction as unknown.

Capture the smallest redacted request/response or artifact pair that proves the result. Record test time, host, account/role labels, object ownership, request IDs, expected versus actual behavior, and every relevant limitation. Preserve contradictions; do not rewrite evidence to fit the hypothesis.

Build a private claim-to-evidence map: each bounded consequence must cite an original artifact. Name the baseline, changed condition, negative control or specific reason it was unsafe, run count, state reset, and the artifact that rules out each competing explanation. For an AI-agent result, separate lower-trust input, actual tool/state action, and user-visible response; measure concealment only when both action and response traces exist. A changed answer without a privileged effect is a different observation.

Check prior art before calling a finding report-ready: program disclosures, vendor advisories, CVE/GHSA aliases, relevant fixes, and comparable reports in the local library. Record why this looks like the same root cause, a regression, or a distinct boundary. Public searching can lower duplicate risk but cannot reveal private submissions.

Ask an independent PROOF reviewer to inspect the original artifacts, controls, hashes, and contradictions before marking a candidate supported. The parent can generate an artifact-first brief with `python3 HACKSPACE/scripts/handoff.py PROOF HACKSPACE/private/candidate.json`; this deliberately withholds the producer's conclusion. Run `python3 HACKSPACE/scripts/gate_candidate.py HACKSPACE/private/candidate.json` before drafting. `DOCUMENTATION_READY` confirms packet coverage and matching hashes, not bug validity, in-scope behavior, uniqueness, or severity.

Return one of: **supported**, **unverified**, **disproved**, or **out_of_scope**. Explain the decisive observation and the next safe check only when it changes the verdict. Severity follows demonstrated consequence and the program's method, not the class name. Hand a supported, documented result to the user's `ywh-reporting` or `evidence-based-reporting` skill.
