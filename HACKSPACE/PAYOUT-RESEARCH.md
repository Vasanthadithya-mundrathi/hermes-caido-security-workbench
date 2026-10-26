# High-payout bug reports: what the evidence supports

Reviewed 2026-10-26. See [seven source-checked examples](high-payout-reports.csv). These are **historical, disclosed awards**, not unclaimed bugs. Original report or vendor issue pages show the awards; amounts from the larger community index remain provisional until checked there.

| Pattern | Observed award | Why the report was persuasive | Original report |
| --- | ---: | --- | --- |
| AI-assisted browser exploit chained three fixed flaws across sandbox boundaries | $250,000 | The [public Chromium issue](https://issues.chromium.org/issues/547965190) records `vrp-reward: 250000`; XBOW describes the human/agent workflow and the duplicate in its [research account](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit). This was one chain reward, not three separate $250,000 awards. | [Chromium #547965190](https://issues.chromium.org/issues/547965190) |
| Packaged app shipped a repository-write credential | $50,000 | Shopify confirmed the token's access, revoked it, and explained the infrastructure risk in its public summary. | [Shopify #1087489](https://hackerone.com/reports/1087489) |
| Account-recovery request sent a victim's reset link to an attacker address | $35,000 total | GitLab's public timeline shows a $1,000 award plus a $34,000 award for the same report. | [GitLab #2293343](https://hackerone.com/reports/2293343) |
| Internal package namespace resolved through public npm | $30,000 total | PayPal's public summary describes the trust boundary; its timeline records two $15,000 collaborator awards. | [PayPal #925585](https://hackerone.com/reports/925585) |
| Authorization failure leaked private data in an error response | $15,000 | The report identified a rejected request whose **body** still contained private report context; the timeline shows the award. | [HackerOne #3862641](https://hackerone.com/reports/3862641) |
| Anonymous GraphQL filter reached JavaScript evaluation | $12,000 | The report tied a controlled input to a specific library operator and a server-side result; the timeline shows the award. | [Mozilla #3782701](https://hackerone.com/reports/3782701) |
| Socket reference-count bug | $10,000 | The PlayStation report and public timeline document the memory-safety issue and award. | [PlayStation #3320669](https://hackerone.com/reports/3320669) |

The common signal is a **specific broken trust boundary with reproducible evidence**. A broad scanner label, old CVE, or the amount another researcher received is not evidence of current eligibility or payout.

## Program ceilings are different from awards

- [Apple's current bounty categories](https://security.apple.com/bounty/categories/) list up to **$2 million** for a qualifying no-interaction network-to-kernel chain. [Apple says bonuses can raise the maximum above $5 million](https://security.apple.com/bounty/). These are exceptional ceilings with specific demonstrated outcomes and target-flag requirements, not typical payouts.
- [Stargate on Immunefi](https://immunefi.com/bug-bounty/stargate/information/) lists a **$10 million maximum** for critical smart-contract impact, calculated against directly affected funds and subject to its current rules. That is a ceiling, not a verified paid report.
- [Google's 2025 VRP review](https://blog.google/security/vrp-2025-year-in-review/) reports over $17 million awarded across its programs in 2025 and expanded AI and Chrome categories. Program-specific policies, not that aggregate, control an individual award.

Choose a program by current scope, realistic access to the required environment, its actual reward schedule, responsiveness, and your ability to prove the impact. A high ceiling with a narrow exploit-chain requirement can be a worse use of time than a moderate program with a clear boundary and test environment.

## Before treating a lead as new

1. Search its exact product, version, endpoint or component, class, and root cause in the local library, the program's disclosed reports, vendor advisories, CVE/GHSA records, and release notes.
2. Determine whether the proposed issue is the same root cause, a regression, an incomplete fix, a distinct reachable path, or merely a new presentation of an old bug. Record that reasoning; do not assert uniqueness from a title search alone.
3. Verify current program scope and whether reports of known/third-party vulnerabilities are eligible. Historical disclosures and public CVEs often make the straightforward report a duplicate or ineligible.
4. For authorized testing only, obtain the smallest reproducible, non-harmful proof with a negative control and preserve exact observed output. Then apply the user's `ywh-reporting` pre-submission triage.

Private submissions are not searchable. Even thorough public research cannot guarantee a non-duplicate verdict or any payout.
