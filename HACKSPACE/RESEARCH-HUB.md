# Public research hub

Reviewed 2026-10-26. These are **source tabs** for research, not a list of authorized targets. Start with the original researcher, vendor, program policy, or maintainer record; note publication and fix dates before using a technique. Commercial product pages describe the vendor's workflow, not independent proof of effectiveness.

## Wiz: research and knowledge bases

| Public source | Use in this workbench |
| --- | --- |
| [Wiz Research](https://www.wiz.io/research) | First-party cloud, AI, and vulnerability investigations; follow each article's evidence and disclosure timeline. |
| [Wiz Vulnerability Database](https://www.wiz.io/vulnerability-database) | Search a CVE or technology, then verify affected versions and fixes at the maintainer/CVE source. The database mixes vendor enrichment and source records. |
| [Wiz CloudSec Academy](https://www.wiz.io/academy) and [AI Security Academy](https://www.wiz.io/academy/ai-security) | Concepts and controls; educational material is a starting point, not proof that an asset is exposed. |
| [Open Cloud Vulnerability DB](https://www.cloudvulndb.org/) and its [open source repository](https://github.com/wiz-sec/open-cvdb) | Cloud provider isolation and platform security issues, including cross-tenant prior art. Check the underlying original disclosure. |
| [Wiz Cloud Threat Landscape](https://threats.wiz.io/) | Publicly disclosed cloud incidents, actors, techniques, and defenses. Incident patterns inform hypotheses but do not establish current target conditions. |
| [Wiz security advisories](https://www.wiz.io/security-advisories) | First-party Wiz product advisories and fix notes. |
| [Wiz Atlas research](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher) and [Wiz Code workflow](https://www.wiz.io/blog/agentic-code-security) | AI-assisted code analysis with exploit validation and code-to-cloud prioritization; see the [workflow comparison](research/WIZ-XBOW-HACKTRON.md). |
| [Exposed MCP server research](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers) and [AI infrastructure honeypots](https://www.wiz.io/blog/ai-infrastructure-honeypot) | Wiz-reported observations of AI infrastructure risks. Their population estimates describe Wiz's telemetry, not a particular bounty target. |
| [PHP2Shell disclosure](https://www.wiz.io/blog/php2shell-php-rce) | Original research account; pair it with the [PHP Foundation release](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) for fixed versions. |

## AI red-team and autonomous testing research

| Public source | Use in this workbench |
| --- | --- |
| [XBOW documentation](https://docs.xbow.com/) and [Labs advisories](https://xbow.com/labs/advisories) | Vendor-described autonomous testing controls, validation, traces, coverage gaps, and disclosed original advisories. Console access is organizational; public docs do not grant testing access. |
| [Hacktron research](https://www.hacktron.ai/blog), [white-box method](https://www.hacktron.ai/pentests), and [Gumroad assessment](https://www.hacktron.ai/reports/Gumroad_01.pdf) | Source-aware agent review, human triage, proof and patch workflow. A vendor-produced assessment needs its scope and status read before reuse. |
| [Gray Swan Research](https://www.grayswan.ai/research), [IPI Arena study](https://www.grayswan.ai/research/how-vulnerable-are-ai-agents-to-indirect-prompt-injections-insights-from-a-large-scale-public-competition), and [open evaluation kit](https://github.com/GraySwanAI/ipi_arena_os) | Public agent hijack and concealment research for controlled evaluations; see [Gray Swan methods](research/GRAY-SWAN.md). Prize challenges and security bug bounties have different rules. |
| [TeamH4C](https://h4c.team/) and its [member research](research/TEAM-H4C.md) | Official examples of local LLM + Ghidra tool use, multi-agent design, and AI tool-boundary testing. A member tutorial does not establish the team's private stack. |
| [OpenAI prompt-injection guidance](https://openai.com/safety/prompt-injections/) and [Safety Bug Bounty overview](https://openai.com/index/safety-bug-bounty/) | Threat model and current reward-category distinctions. Recheck the actual program rules before a submission. |
| [Microsoft Copilot Bounty](https://www.microsoft.com/en-us/msrc/bounty-ai) and [Google Chrome VRP rules](https://bughunters.google.com/about/rules/chrome-friends/chrome-vulnerability-reward-program-rules) | Current AI-product and browser eligibility examples; reward ceilings are separate from paid reports. |

## Primary standards and public data

- [OWASP Web Security Testing Guide](https://wstg.owasp.org/): manual test design and controls.
- [OWASP GenAI Security Project](https://genai.owasp.org/): AI application threat taxonomy and guidance.
- [MITRE ATLAS](https://atlas.mitre.org/): adversarial ML case mapping.
- [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): evidence of known exploitation, not a bounty eligibility list.
- [CVE List](https://github.com/CVEProject/cvelistV5), [OSV data](https://google.github.io/osv.dev/data/), [GitHub Advisory Database](https://github.com/github/advisory-database), and [NVD feeds](https://nvd.nist.gov/vuln/data-feeds): bulk advisory context, with substantial identifier overlap. Their local copies are recorded in [SOURCES.md](SOURCES.md).
- [Google Project Zero](https://googleprojectzero.blogspot.com/) and [GitHub Security Lab](https://securitylab.github.com/research/): original technical research and coordinated disclosures.

For report-ready claims, follow the original case and record what was **observed**, **reported by a researcher**, **inferred**, or **unknown**. Do not promote a tool demo, vendor benchmark, or CVE record into a verified new bounty finding.
