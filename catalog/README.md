# Public reports and writeups catalog

The [CSV catalog](resources.csv) points to the largest useful **public discovery surfaces**: disclosed bounty reports, vulnerability records, original research, CTF writeups, practice labs, and standards. It intentionally links to publishers rather than copying reports. Run `python3 scripts/catalog.py build` from the repository root to regenerate the browsable [index](index.md), or `python3 scripts/catalog.py search access-control` for a quick local filter.

## What a source contains

- **HackerOne Hacktivity:** use the **Disclosed** filter; HackerOne says undisclosed entries show redacted titles and only disclosed reports expose their details.
- **Bugcrowd CrowdStream:** public activity may include a summary or full report depending on the program's coordinated-disclosure settings.
- **Advisory databases:** CVEs and advisories are structured vulnerability records. Many are not first-person bug bounty reports and may omit reproduction detail.
- **CTFtime:** community writeups by event and challenge. Respect event embargoes and challenge authors' licenses.
- **Community indexes:** useful for discovery but completeness, accuracy, and reuse rights vary. Follow the original report link for citations.

These distinctions matter: a platform's public feed cannot be counted as every report submitted to it, and a third-party index cannot establish worldwide completeness. Search each source for the vulnerability class and technology you are studying, then read the primary report in context.

## Search order

1. Search the original platform or advisory for the exact product, class, and year.
2. Use the relevant research blog or CTF index for technical explanation.
3. Compare with OWASP WSTG/ASVS and vendor documentation for expected controls.
4. Record the URL, publisher, publication date, observed version, and any access or disclosure limits in local notes.

For a new bug bounty report, review the program's current rules and prior disclosures. Do not assume a historical writeup grants permission to revisit its target.

Pentester Land publishes an optional [JSON download](https://pentester.land/writeups.json). Run `python3 scripts/sync_pentesterland.py sync` to make a **local** CSV of its public metadata and links in `data/`, which Git ignores. This can organize thousands of historical external writeups without republishing their articles or the source dataset. Run `python3 scripts/sync_pentesterland.py search idor` to filter the local index. The source's most recent entries may be old; inspect publication dates and original links before using a result.

The community [HackerOne Disclosed Reports index](https://github.com/ajaysenr/HackerOne-Disclosed-Reports) offers metadata for public HackerOne URLs. Run `python3 scripts/sync_hackerone_index.py sync` to create another Git-ignored local CSV, then `python3 scripts/sync_hackerone_index.py search csrf`. Its repository has no declared license as of 2026-10-25, so this workbench does not republish its index. Its metadata is not HackerOne's own verification; follow each report URL and check current visibility and details.

After both syncs, run `python3 scripts/library.py build` for one Git-ignored SQLite library. `python3 scripts/library.py search 'access control'` searches titles, publisher tags, programs, and authors across both sources; `python3 scripts/library.py stats` shows source counts. The library stores links and metadata only, not report bodies. Rebuild it after each sync.

## Maintenance

`resources.csv` is a curated starting point, not an exhaustive dump. Add primary sources with stable URLs, label community mirrors explicitly, and use `python3 scripts/catalog.py check`. The [topic map](classes.md) provides a study route by category.
