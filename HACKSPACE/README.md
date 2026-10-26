# HACKSPACE — bug bounty research library

Updated 2026-10-26. This folder prioritizes **public bug reports, payout evidence, current vulnerability research, and original hypothesis notes**. CTF writeups are deferred. It is a research library, not a list of live targets or permission to test them.

## What is here

| Layer | Contents | What it proves |
| --- | --- | --- |
| Local link library | `data/library.sqlite`: 19,191 distinct report/writeup URLs from two community indexes | A searchable discovery index; individual URLs, metadata, bounty figures, and current visibility still require verification at the original publisher |
| Source-checked payout cases | [high-payout-reports.csv](high-payout-reports.csv) and [payout analysis](PAYOUT-RESEARCH.md) | Seven historical reports/issue records whose award amounts were checked against original publisher pages |
| Curated prior art | [Reviewed records](reviewed-prior-art.jsonl), plus optional private `data/reviewed-prior-art.jsonl` | Root cause, trust boundary, versions, aliases, fix notes, original sources, and explicit review depth; the public set adds three MCP advisories |
| Current research | [AI security](research/AI-SECURITY.md), [Gray Swan methods](research/GRAY-SWAN.md), [TeamH4C public methods](research/TEAM-H4C.md), [Wiz/XBOW/Hacktron workflows](research/WIZ-XBOW-HACKTRON.md), [PHP2Shell](research/PHP2SHELL.md), and [pattern notes](research/HIGH-VALUE-PATTERNS.md) | Dated source-backed context and testable research questions, not new findings |
| Research tabs | [Public research hub](RESEARCH-HUB.md) | Curated primary sources and public knowledge bases, including Wiz, XBOW, Hacktron, and Gray Swan |
| Bulk advisory corpus | `data/sources/` and [audited snapshot](CORPUS-SNAPSHOT.md) | 5.05 GB of canonical CVE, OSV, GitHub, and NVD advisory/enrichment archives, with a separate 711 MB CVE extraction for lookup; these are **not** 5 GB of first-person bounty reports |
| Private work | `private/` | Program cards, notes, evidence, and unpublished reports; excluded from Git |
| Research workflow | [Workflow](WORKFLOW.md) and [offline evals](evals/README.md) | Scoped lead queue, artifact-first handoffs, evidence gate, and synthetic finding-judgment tests |

The 2026-10-26 link snapshot holds 12,673 HackerOne URLs and 6,526 Pentester Land links; eight URLs overlap. The HackerOne community index includes 2,337 rows with a reported bounty amount, 93 at or above $10,000. Those 93 amounts are **unverified index metadata** until the original report is read. The most recent indexed HackerOne disclosure was 2026-10-26 03:43 UTC. Pentester Land's newest row in this snapshot was dated 2024-09-18, so it is mainly historical background.

## Use it

Run from the repository root:

```sh
python3 scripts/library.py stats
python3 scripts/library.py search 'access control'
python3 scripts/library.py prior-art 'tenant predicate'
python3 scripts/library.py top --year 2026 --min-bounty 10000
python3 HACKSPACE/scripts/lead_queue.py init
python3 HACKSPACE/scripts/lead_queue.py rank --show-blocked
python3 HACKSPACE/scripts/eval_findings.py list
python3 HACKSPACE/scripts/lookup_advisory.py CVE-2026-109618 --source cve
python3 HACKSPACE/scripts/audit_corpus.py --verify-crc
```

To refresh the two local indexes:

```sh
python3 scripts/sync_hackerone_index.py sync
python3 scripts/sync_pentesterland.py sync
python3 scripts/library.py build
python3 HACKSPACE/scripts/sync_nvd_feeds.py
python3 HACKSPACE/scripts/sync_cpe_match.py
```

`data/` and `private/` are Git-ignored. Source text and attachments from bounty platforms are not bulk-mirrored into the public repository. The [source register](SOURCES.md) identifies each large download and its usage terms. The [corpus snapshot](CORPUS-SNAPSHOT.md) records exact bytes, entries, and integrity results; byte volume alone is not a quality measure. The optional Gray Swan IPI Arena source checkout is MIT licensed but its documented model benchmark needs a separate OpenRouter API key; a ChatGPT/Codex subscription does not cover that cost.

## Turning an old report into a fresh lead

1. Read the current program policy and payout table. Record the exact in-scope asset and whether automation, accounts, or a test environment are allowed.
2. Read the **original** historical report. Write its security boundary, root cause, prerequisites, fix, and date. A known CVE or old report is prior art, not a new bug.
3. Search program disclosures, advisories, release notes, and this library for the same root cause. A private duplicate can still exist; no public search can guarantee novelty.
4. Form one falsifiable, scoped hypothesis about a different boundary or implementation. Use a baseline and smallest decisive comparison; stop after sufficient proof.
5. Capture original, redacted evidence and use the user's `ywh-reporting` skill for pre-submission triage. Keep payout eligibility separate from severity and demonstrated impact.

Use the [private lead card template](templates/lead-card.md) and [research diary template](templates/diary.md) to make each attempt reviewable. Do not save secrets, target responses, or unpublished findings in public Git.

The [research-to-report workflow](WORKFLOW.md) adds a private ranked queue, independent PROOF review, a file-hash documentation gate, and synthetic evaluations. `scripts/library.py build` preserves overlapping source memberships and indexes seven source-checked payout summaries plus three original-source MCP records as prior art. One of the three includes an inspected fix commit; the others explicitly stop at maintainer advisory and patched-version review. More records can be added locally in `data/reviewed-prior-art.jsonl`.
