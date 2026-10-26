# Private engagement card

Keep a filled copy outside the public repository.

| Field | Value and source |
|---|---|
| Program or CTF | |
| Current policy URL / reviewed date | |
| Allowed assets and accounts | |
| Attackable assets / methods | [exact hosts, paths, roles and permitted interaction] |
| Allow Visit only | [supporting sites/documents permitted for browsing, without active testing] |
| Blocked assets / methods | [excluded hosts, third parties, destructive or prohibited actions] |
| Redirect and third-party handling | [where to stop when a permitted flow leaves scope] |
| Exclusions and prohibited methods | |
| Automation / rate budget | [written rule, total and remaining request budget, shared across agents] |
| Disclosure, recording, and retention rules | |
| Stop conditions and contact path | |

## Investigation queue

| Priority | Asset / role / boundary | Falsifiable question | Smallest permitted check | Request/time cost | Result / evidence ID |
|---|---|---|---|---|---|
| 1 | | | | | |

Before active traffic, confirm every tested host, redirect, account and method against the policy. Prefer one decisive baseline and one controlled comparison. After each timebox, stop, change hypothesis, or document the supported result. The local `HACKSPACE/scripts/lead_queue.py` ranks private leads by expected impact, evidence readiness, information gain, duplicate risk and cost; its ranking is not permission to test.
