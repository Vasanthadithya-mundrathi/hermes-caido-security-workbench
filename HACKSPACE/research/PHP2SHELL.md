# PHP2Shell — current research brief

Reviewed 2026-10-26. This is **known, disclosed prior art**, not a new bounty lead. Do not test third-party PHP installations merely because they may run an affected version.

| Claim | Primary evidence |
| --- | --- |
| CVE-2026-109618 concerns out-of-memory handling that can leave partially initialized request data; CVE-2026-109619 concerns stale request-owned state after a fatal error. Both were demonstrated as remote code execution in specified conditions. | [PHP Foundation release explanation, 2026-10-21](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) |
| Supported fixed releases are PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. Older unsupported branches need a supported upgrade or vendor-supplied equivalent fix. | [PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/), [CISA alert, revised 2026-10-23](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) |
| The original research combined model-assisted analysis with human verification and coordinated disclosure; it confirmed exploitation against several application deployments but locates the flaws in the PHP runtime. | [Wiz Research, 2026-10-21](https://www.wiz.io/blog/php2shell-php-rce) |

**Research lesson:** a runtime error path can cross a request-lifetime boundary even when application code looks ordinary. For an owned or explicitly in-scope codebase, distinguish the runtime and SAPI from the application, verify the deployed build and vendor patch, and inspect how exceptional cleanup and persistent worker state interact. Historical findings motivate a *different, falsifiable* hypothesis; a version banner or proof that a known CVE exists is not a novel report.

**Defender action:** inventory web-serving PHP, patch supported branches promptly, and use the [PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) and [CISA](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) guidance. Record whether a vendor backport actually covers the deployed build. Do not equate scan traffic with a confirmed compromise; the evidence and date matter.
