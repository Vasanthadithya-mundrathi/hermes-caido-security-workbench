# Public security resources

Generated from [resources.csv](resources.csv) with `python3 scripts/catalog.py build`.
The links point to publishers and discovery feeds; this is not an archive of every report.

## Public disclosures and advisories

| Resource | Topics | Access | Note |
|---|---|---|---|
| [Bugcrowd CrowdStream](https://bugcrowd.com/crowdstream) | bug-bounty, web, api | public-filter | Visibility varies by program and disclosure level |
| [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | cve, prioritization | public | Known exploited catalog rather than writeups |
| [CVE Program](https://www.cve.org/) | cve, advisory | public | Identifier records and references |
| [EU Vulnerability Database](https://euvd.enisa.europa.eu/) | cve, advisory | public | European vulnerability records and references |
| [GitHub Advisory Database](https://github.com/advisories) | open-source, cve, supply-chain | public | Advisories are not necessarily full researcher reports |
| [HackerOne Hacktivity](https://hackerone.com/hacktivity/overview) | bug-bounty, web, api, idor, access-control | public-filter | Select Disclosed to view public report contents |
| [NIST NVD](https://nvd.nist.gov/vuln/search) | cve, advisory | public | Enriched vulnerability records; check source advisories |
| [OSV](https://osv.dev/) | open-source, cve, supply-chain | public | Aggregated vulnerability records with source references |

## Community report indexes

| Resource | Topics | Access | Note |
|---|---|---|---|
| [HackerOne Disclosed Reports index](https://github.com/ajaysenr/HackerOne-Disclosed-Reports) | bug-bounty, dataset | public | Third-party mirror; check current coverage and reuse terms |
| [PentesterLand bug bounty writeups](https://pentester.land/writeups/) | bug-bounty, writeups | public | Curated external writeup links; coverage varies |
| [WriteupDB](https://www.writeup-db.com/writeups-list/) | bug-bounty, writeups | public | Community directory; verify original articles and freshness |

## Original research and publisher blogs

| Resource | Topics | Access | Note |
|---|---|---|---|
| [Assetnote research](https://blog.assetnote.io/) | recon, web, api | public | Original research and asset discovery posts |
| [Bugcrowd blog](https://www.bugcrowd.com/blog/) | bug-bounty, reporting | public | Platform guidance and selected research |
| [GitHub Security Lab research](https://securitylab.github.com/research/) | open-source, code-review, writeups | public | Original research and advisory context |
| [Google Project Zero blog](https://googleprojectzero.blogspot.com/) | exploitation, writeups | public | Original technical research |
| [HackerOne blog](https://www.hackerone.com/blog) | bug-bounty, reporting | public | Platform guidance and selected research |
| [HackingHub](https://www.hackinghub.io/) | bug-bounty, web, ctf | public | Training platform associated with the source-labeled extraction |
| [Intigriti researcher blog](https://www.intigriti.com/researchers/blog) | bug-bounty, web, api | public | Techniques and selected writeup links |
| [Orange Tsai - The Art of PHP](https://blog.orange.tw/posts/2025-08-the-art-of-php-ch/) | ctf, php, web, writeups | public | First-person technical CTF essay used as a writing-structure reference |
| [PortSwigger Research](https://portswigger.net/research) | web, api, writeups | public | Original web security research |
| [YesWeHack learning](https://www.yeswehack.com/learn-bug-bounty) | bug-bounty, reporting | public | Learning and report-writing guidance |

## CTF writeups

| Resource | Topics | Access | Note |
|---|---|---|---|
| [CryptoHack blog](https://blog.cryptohack.org/) | ctf, crypto, writeups | public | Publisher blog with CTF writeups |
| [CTFtime writeups](https://ctftime.org/writeups) | ctf, web, pwn, crypto, reverse | public | Community writeup index by event and tags |

## CTF and lab practice

| Resource | Topics | Access | Note |
|---|---|---|---|
| [CryptoHack challenges](https://cryptohack.org/challenges/) | ctf, crypto | account-for-progress | Cryptography challenges and archive |
| [Hack The Box Academy](https://academy.hackthebox.com/) | ctf, web, systems | account | Training modules; some paid access |
| [HackingHub Hubs](https://app.hackinghub.io/hubs) | web, ctf, labs | account | Hands-on labs; check access terms |
| [OverTheWire wargames](https://overthewire.org/wargames/) | ctf, linux, pwn | public | Authorized challenge servers and rules |
| [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) | web, labs | public | Intentionally vulnerable training app |
| [OWASP WebGoat](https://owasp.org/www-project-webgoat/) | web, labs | public | Intentionally vulnerable training app |
| [picoCTF practice](https://play.picoctf.org/practice) | ctf, web, crypto, reverse | account | Practice challenges and learning material |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | web, api, labs, idor, access-control | public | Free web security labs and explanations |
| [pwn.college dojos](https://pwn.college/dojos) | ctf, pwn, linux, systems | account-for-progress | Structured practical curriculum |

## Primary references

| Resource | Topics | Access | Note |
|---|---|---|---|
| [Caido documentation](https://docs.caido.io/) | proxy, web, api | public | Primary Caido setup and features reference |
| [FIRST CVSS](https://www.first.org/cvss/) | severity, reporting | public | Use version required by the program |
| [GitHub Code Security docs](https://docs.github.com/en/code-security) | open-source, advisory | public | Advisory and vulnerability reporting documentation |
| [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs) | agent, desktop, mcp | public | Primary Hermes Desktop and MCP reference |
| [MITRE ATT&CK](https://attack.mitre.org/) | threat-model, adversary | public | Behavioral knowledge base; not a bug bounty report index |
| [MITRE CWE](https://cwe.mitre.org/data/index.html) | classification, reporting | public | Weakness taxonomy; class alone is not severity |
| [OBS Studio knowledge base](https://obsproject.com/kb/) | recording, evidence | public | Primary screen recording setup reference |
| [OWASP API Security](https://owasp.org/API-Security/) | api, methodology | public | API risk and testing guidance |
| [OWASP ASVS](https://asvs.owasp.org/) | web, api, requirements | public | Security verification requirements |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | web, api, remediation | public | Defensive controls and implementation guidance |
| [OWASP Mobile Application Security](https://mas.owasp.org/) | mobile, methodology | public | Mobile security standards and testing guide |
| [OWASP Web Security Testing Guide](https://wstg.owasp.org/) | web, api, methodology, idor, access-control | public | Use versioned chapters for stable citations |
| [ProjectDiscovery documentation](https://docs.projectdiscovery.io/) | recon, nuclei, automation | public | Primary tool documentation |

## Community references

| Resource | Topics | Access | Note |
|---|---|---|---|
| [Caido skills](https://github.com/caido/skills) | proxy, agent | public | Claude-focused skill; review auth and storage assumptions |
| [HackTricks](https://book.hacktricks.wiki/) | web, systems, ctf | public | Community notes; verify against primary sources |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | web, api, ctf | public | Community techniques; use only within scope |
| [ProjectDiscovery Nuclei templates](https://github.com/projectdiscovery/nuclei-templates) | nuclei, templates | public | Template source; validate safety and results |
| [SecLists](https://github.com/danielmiessler/SecLists) | wordlists, recon | public | Wordlist collection; respect rate and scope limits |
| [YesWeHack Claude Kit](https://github.com/yeswehack/claude-kit) | reporting, agent | public | Upstream reporting ideas; review its license |
