# Topic map

Use these topics to navigate [the resource catalog](index.md). They are study prompts, not a checklist to run against an unapproved target. [OWASP WSTG](https://wstg.owasp.org/) and [PortSwigger Academy](https://portswigger.net/web-security) provide the primary web learning paths.

| Track | Questions to study | Evidence to preserve |
|---|---|---|
| Authentication and sessions | Which identity proof or session transition failed? | Role and session context; redacted before/after requests |
| Authorization / IDOR | Which object or action crossed a role or tenant boundary? | Two controlled roles and the exact object ownership relation |
| Business logic | Which server-side state or rule was bypassed? | Baseline workflow and changed sequence |
| API and GraphQL | Which endpoint or schema assumption differs from the UI? | Exact API operation and response with context |
| Injection | Where did untrusted input cross into an interpreter? | Input location and minimal observable result |
| XSS and client-side | What output context executed or exposed data? | Context and controlled execution evidence |
| SSRF and URL handling | Which network boundary was crossed? | Controlled destination and observed request provenance |
| Request smuggling / parser mismatch | Which two components parsed the same bytes differently? | Paired protocol view and non-disruptive proof |
| Cache and CDN behavior | Which identity or request property was missing from a cache key? | Cache headers; controlled cross-context comparison |
| File upload / path handling | Which path or file type rule failed? | Filename/type/path and observed server result |
| Secrets and misconfiguration | What secret or unsafe setting was actually exposed? | Redacted location and validity evidence; avoid using secrets |
| Supply chain / dependency | Which package and version are affected? | Advisory; lockfile/version; actual reachable context |
| Mobile | Which app/API/storage trust boundary failed? | App build and device state; relevant API or local artifact |
| CTF web | What is the challenge's intended boundary? | Rules, instance, solve notes |
| CTF crypto | Which primitive or implementation assumption breaks? | Given parameters and reproducible derivation |
| CTF reverse / pwn | Which program behavior supports the solve? | Artifact hash, environment, debugger/disassembly notes |
| CTF forensics / OSINT | Which provided artifact supports the answer? | Source artifact hash and transformation trail |

For remediation language use [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) and [ASVS](https://asvs.owasp.org/). For classification use [MITRE CWE](https://cwe.mitre.org/data/index.html). For severity use the program's required [FIRST CVSS](https://www.first.org/cvss/) version and only supported consequences.
