---
name: finding-validation
description: Check whether a proposed bug bounty finding is reproducible, in scope, security-relevant, and supported by controlled evidence before reporting.
---

# Finding validation

Separate the hypothesis from the observations. Identify the claimed boundary, required roles and preconditions, the exact evidence artifact, and a competing benign explanation. A scanner alert, one HTTP status, a client-side UI change, or a model prediction is not sufficient by itself.

For an authorized live test, compare an expected baseline with one changed input or identity. Use a negative control where feasible, confirm that the server-side effect belongs to the controlled test account, and repeat only enough to rule out caching, timing, or stale state. Do not access unrelated users' data or cause unnecessary changes. If testing is not authorized, inspect supplied evidence only and mark reproduction as unknown.

Capture the smallest redacted request/response or artifact pair that proves the result. Record test time, host, account/role labels, object ownership, request IDs, expected versus actual behavior, and every relevant limitation. Preserve contradictions; do not rewrite evidence to fit the hypothesis.

Check prior art before calling a finding report-ready: program disclosures, vendor advisories, CVE/GHSA aliases, relevant fixes, and comparable reports in the local library. Record why this looks like the same root cause, a regression, or a distinct boundary. Public searching can lower duplicate risk but cannot reveal private submissions.

Return one of: **supported**, **promising but unverified**, **disproved**, or **out of scope/unknown scope**. Explain the decisive observation and the next safe check only when it changes the verdict. Severity follows demonstrated consequence and the program's method, not the class name. Hand a supported, documented result to `evidence-based-reporting`.
