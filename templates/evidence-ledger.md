# Evidence ledger — local copy for one finding

Keep this filled copy outside the public repository. Use a separate ledger for each finding.

| Field | Entry |
|---|---|
| Program / CTF and policy URL | [unknown until supplied] |
| Policy reviewed at | [date/time] |
| In-scope asset | [exact asset and source of scope] |
| Test account / role | [private label; no credential] |
| Caido project | [project name] |
| Hypothesis | [expected control and bounded difference] |
| Broken boundary being claimed | [actor, object, tenant, tool or state boundary] |
| Baseline / changed condition / negative control IDs | [E1] / [E2] / [E3 or specific safety exception] |
| Reproduction | [attempts, successes, reset/changed state, timestamps] |
| Plausible alternative | [cache, intended sharing, stale state, role confusion, etc.] |
| Control that ruled it out | [artifact ID and precise observation, or still open] |
| Directly observed behavior | [what the inspected artifact shows] |
| Researcher-reported behavior | [what notes say but was not inspected] |
| Inference | [reasoning from observations] |
| Unknowns | [missing scope, steps, versions, impact, etc.] |
| Prior-art comparison | [original reports/advisories searched; same root, regression, incomplete fix, or distinct root] |
| Independent reviewer / verdict | [PROOF or other reviewer; supported / unverified / disproved / out of scope] |

## Artifacts

| ID | Private path | SHA-256 | Captured at | Role and context | Establishes | Does not establish | Redactions |
|---|---|---|---|---|---|---|---|
| E1 | [path] | [hash] | [time] | [role] | [precise fact] | [limit] | [what was removed] |

## Reproduction notes

Record the exact existing steps and their results. Do not reconstruct missing requests, responses, or screenshots from memory.

## Claim-to-evidence map

| Exact impact claim | Observed artifact IDs | Competing explanation and control | Supported extent |
|---|---|---|---|
| [bounded claim] | [E2] | [alternative ruled out by E3] | [role/object/tenant and conditions] |

For an AI-agent finding, separately link the lower-trust input, actual tool/state effect, and user-visible response. Record model/tool versions, run count, state resets, success definition, and whether concealment was observed. Keep raw traces private.

Use `python3 HACKSPACE/scripts/gate_candidate.py HACKSPACE/private/candidate.json` on a matching private JSON packet. A passing documentation gate checks field coverage and file hashes; it does not verify that the bug or its severity is real.
