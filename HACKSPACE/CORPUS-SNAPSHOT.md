# Local corpus snapshot — 2026-10-26

The [local audit script](scripts/audit_corpus.py) checked the ZIP central directories and every ZIP member's CRC, read the NVD CPE Match TAR and its full gzip stream through the CRC trailer, and recorded SHA-256 digests on 2026-10-26 06:53 UTC. The full machine-readable manifest is at Git-ignored `data/corpus-manifest.json`. All 30 audited files were marked complete. Refreshing sources changes these numbers; rerun the audit before citing a later snapshot.

| Source archive | Compressed bytes | Inspected file entries | Meaning |
| --- | ---: | ---: | --- |
| OSV bulk ZIP | 2,796,793,763 | 2,287,939 | Advisory record files; identifiers and aliases overlap other sources. |
| Official CVE List download ZIP | 642,793,607 | 1 | The one member is another ZIP named `cves.zip`. |
| GitHub Advisory Database ZIP | 494,674,389 | 394,849 | Archive file entries, not verified distinct flaws. |
| NVD yearly CVE ZIP feeds, 2002–2026 | 242,385,341 | 25 | One JSON payload per yearly feed; each payload contains many CVE analyses. |
| NVD CPE Match TAR.GZ | 873,135,850 | 74 | Applicability/enrichment files, not bug reports. |
| **Canonical source archives** | **5,049,782,950 bytes (5.05 GB; 4.70 GiB)** | | Source volume, with identifier overlap. |

The CVE List download's inner `cves.zip` was extracted as `data/sources/cve-2026-10-26-records.zip` for direct lookup. It adds **711,012,574 file bytes** and has **414,057 JSON record files**; the inner copy passed ZIP CRC and SHA-256 checks. It duplicates the CVE source archive, so the canonical 5.05 GB total **does not count it twice**. The audited archive file sizes sum to 5,760,795,524 bytes (5.76 GB), under the requested optional 7 GB ceiling. Small CSV/SQLite indexes and the four-megabyte Gray Swan source checkout are separate.

The bug-bounty layer is **19,191 distinct public report/writeup links**, not 5 GB of mirrored report bodies: 12,673 HackerOne community-index URLs plus 6,526 Pentester Land links with eight overlapping URLs. Ninety-three HackerOne rows have an *index-reported* bounty of at least $10,000; [seven historical high-payout cases](PAYOUT-RESEARCH.md) were checked against original pages. An index row is neither proof of a valid current bug nor a guarantee against a private duplicate. CVE, OSV, GitHub Advisory, and NVD records are advisory context, not first-person bug bounty reports.

## Reproduce the checks

```sh
python3 scripts/library.py stats
python3 HACKSPACE/scripts/lookup_advisory.py CVE-2026-109618 --source cve --max-chars 500
python3 HACKSPACE/scripts/audit_corpus.py --verify-crc
```

Use the [source register](SOURCES.md) for provenance and reuse terms. Keep `data/`, unpublished notes, evidence, credentials, and recordings outside public Git.
