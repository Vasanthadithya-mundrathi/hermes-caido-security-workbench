# Source and corpus register

Reviewed 2026-10-26. The local archive lives under Git-ignored `HACKSPACE/data/`; only this source register and original analysis are published. A downloaded archive is not proof that every contained record is current, unique, or a confirmed vulnerability.

| Source | Local content | Provenance and use |
| --- | --- | --- |
| [HackerOne disclosed-report community index](https://github.com/ajaysenr/HackerOne-Disclosed-Reports) | `data/hackerone-disclosed-index.csv` | 12,673 public report URLs and metadata in this snapshot. Community index, no declared repository license observed; kept local. Check original [HackerOne Hacktivity](https://hackerone.com/hacktivity/overview) page for report body, award, and visibility. |
| [Pentester Land export](https://pentester.land/writeups.json) | `data/pentesterland-writeups.csv` | 6,526 historical public writeup links. Kept local; original publishers control the articles. |
| [OSV database bulk dump](https://google.github.io/osv.dev/data/) | `data/sources/osv-all.zip` | Official cross-ecosystem vulnerability **advisory records**, including source attribution and aliases. OSV publishes this bulk archive for downstream use; individual source licensing and attribution still matter. |
| [CVE List V5](https://github.com/CVEProject/cvelistV5) | `data/sources/cve-2026-10-26-baseline.zip` and extracted `cve-2026-10-26-records.zip` | Official CVE **records** from the 2026-10-26 UTC baseline. The downloaded ZIP contains one nested `cves.zip`; the extracted copy makes individual IDs searchable. It duplicates the outer archive's content and is **excluded** from the canonical corpus byte count. Use under the [CVE Program terms](https://www.cve.org/Legal/TermsOfUse), including attribution. This snapshot becomes stale as new records arrive. |
| [GitHub Advisory Database](https://github.com/github/advisory-database) | `data/sources/github-advisory-main.zip` | GitHub-originated and curated open-source advisories in OSV format. [CC BY 4.0](https://github.com/github/advisory-database/blob/main/LICENSE.md). Many records overlap OSV by GHSA/CVE alias; they are retained for direct publisher provenance and must not be counted as distinct vulnerabilities twice. |
| [NVD 2.0 data feeds](https://nvd.nist.gov/vuln/data-feeds) | `data/sources/nvd/nvdcve-2.0-YYYY.json.zip` and `nvdcpematch-2.0.tar.gz` | NIST's CVE enrichment and CPE applicability data. Yearly CVE feeds overlap CVE List records but add NVD analysis; CPE match data maps product/version criteria. These are **not** bounty reports. NVD recommends checking `.meta` and downloading changed feeds instead of needlessly re-fetching. |
| [Gray Swan IPI Arena open kit](https://github.com/GraySwanAI/ipi_arena_os) | `data/tools/ipi_arena_os/` | MIT-licensed source checkout at `5e2e285910d581c97767195f1d113ef323f9ab07` for controlled indirect-prompt-injection evaluation. The documented benchmark run needs a separate OpenRouter API key for target and judge calls, so the checkout is free but live model runs may cost money and are not covered by the ChatGPT/Codex subscription. Its size is not counted toward the advisory or report corpus. |

HackerOne's [report export documentation](https://docs.hackerone.com/en/articles/8514502-export-reports) describes bulk exports for reports **within one's own program**. It does not grant access to other programs' private reports. This library does not crawl private reports or download report attachments.

## Counting rules

- **Link count:** distinct canonical report/writeup URLs in the local SQLite index. It is not a count of verified bugs.
- **Source-checked count:** rows in `high-payout-reports.csv` whose original page explicitly records the amount. Historical awards do not predict a new reward.
- **Advisory count:** count source records, then deduplicate analytical results using GHSA/CVE/OSV aliases. A CVE entry and an OSV entry for the same flaw are two records, not two bugs.
- **Byte count:** measure completed local files only. Do not include partial downloads, Git history, duplicate copies, caches, generated padding, or indexes in a claim of unique report content.

The requested roughly 5 GB is a **local storage target**, with 7 GB as an upper bound if added material improves research. Record actual bytes, archive integrity, record counts, and advisory/report split after each refresh. Preserve the smaller high-quality source-checked layer even if the byte target remains unmet.
