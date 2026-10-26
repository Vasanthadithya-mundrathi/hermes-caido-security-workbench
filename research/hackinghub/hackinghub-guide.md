# HackingHub: extracted tips, tools and websites

Research date: 14 October 2026. Source: [HackingHub LinkedIn posts](https://www.linkedin.com/company/hackinghub/posts/).

Processed **315 distinct entries** from the signed-in feed until LinkedIn displayed the footer and stopped loading more entries. Also reviewed **90 distinct indexed post pages**, including older material and overlapping posts. These counts must not be added together as a unique-post total.

The extraction contains **115 tips and testing leads**, **44 tool / utility entries**, and **26 website / learning-resource entries**. It also records incidental UI names separately. **31 attached images**, **7 video posters**, and selected frames from **3 demos** were inspected.

**Coverage limit:** this is an extraction of the available feed and indexed sources. Complete all-time coverage is unverified. Most attached videos were not transcribed, and some images were not inspected. The separate video-coverage.csv and post-index.csv show these gaps. A caption that only announces a tip does not establish the missing steps.

Evidence labels distinguish author captions, directly inspected images/frames, reposted contributor material, and analysis of illustrative code. Code-review observations below describe the shown examples; surrounding middleware and real-target behavior are unknown. Official tool URLs were independently matched where possible. Historical sales and payout promises are excluded from practical recommendations.

## Most useful themes

- Learn one application deeply: users, objects, tenant boundaries and its business workflows.
- Turn recon into priorities: map assets, fingerprint them, reduce noisy data, then investigate promising surfaces.
- Read docs, JavaScript, old routes, emails and integrations for leads the main UI hides.
- Investigate disagreements between parsers, routing layers, HTTP methods and authorization checks.
- Choose XSS tests for the actual output context; capture context from validated blind execution.
- Treat automation and AI output as candidates that require validation. Establish the actual consequence before reporting it.

## Tools and utilities

### Recon

| Tool | Use shown or mentioned | Evidence | Sources |
|---|---|---|---|
| [Subfinder](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery | caption | [B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH), B187 (feed / source index), B199 (feed / source index), B223 (feed / source index) |
| [dnsx](https://github.com/projectdiscovery/dnsx) | Resolve and filter DNS results | caption; inspected image | B199 (feed / source index), B223 (feed / source index) |
| [httpx (ProjectDiscovery)](https://github.com/projectdiscovery/httpx) | Probe live HTTP endpoints; collect titles and technology data. The Go probing tool in their pipelines. | caption; inspected image | B187 (feed / source index), B189 (feed / source index), B199 (feed / source index), B223 (feed / source index) |
| [Katana](https://github.com/projectdiscovery/katana) | Crawl and discover URLs with query parameters | inspected image | B189 (feed / source index) |
| [Naabu](https://github.com/projectdiscovery/naabu) | Port discovery in a DNS-to-port pipeline | inspected image | B198 (feed / source index) |
| [RustScan](https://github.com/RustScan/RustScan) | Fast initial port discovery before focused Nmap enumeration | caption | B169 (feed / source index) |
| [Nmap](https://nmap.org/) | Service enumeration and default scripts; understand scan visibility | caption; inspected image | B124 (feed / source index), B169 (feed / source index), B308 (feed / source index) |
| [waybackurls](https://github.com/tomnomnom/waybackurls) | Recover historical URLs and filter interesting routes | inspected image | B220 (feed / source index) |
| [uro](https://github.com/s0md3v/uro) | Clean and deduplicate crawled URLs | inspected image | B189 (feed / source index) |
| [WHOXY](https://www.whoxy.com/reverse-whois/) | WHOIS and reverse-WHOIS asset correlation. A shared registrant email is a lead; it does not prove complete asset ownership. | video frames at 00:11 | [B150](https://www.linkedin.com/posts/hackinghub_what-if-you-could-find-every-unique-asset-activity-7456055740848521216-LxsQ) |
| [c99 Subdomain Finder](https://subdomainfinder.c99.nl/) | Web-based subdomain discovery | caption; poster inspected | B043 (feed / source index), B231 (feed / source index) |
| [ProjectDiscovery Chaos](https://chaos.projectdiscovery.io/) | Public bug-bounty subdomain datasets | caption | B234 (feed / source index), B312 (feed / source index) |
| [bounty-targets-data](https://github.com/arkadiyt/bounty-targets-data) | Machine-readable bounty scope datasets. Name is visible in an AI-generated workflow summary. Data freshness and generated CSV accuracy were not verified. | video poster inspected | B015 (feed / source index) |

### HTTP testing

| Tool | Use shown or mentioned | Evidence | Sources |
|---|---|---|---|
| [Caido](https://caido.io/) | Traffic inspection, replay, automation, workflows and WebSocket testing | caption; selected video frames | [B032](https://www.linkedin.com/posts/hackinghub_analyze-js-files-with-a-caido-plugin-activity-7506088489772544001-y3TD), [B033](https://www.linkedin.com/posts/hackinghub_want-to-hunt-websockets-vulns-heres-how-activity-7505681053723045889-Ic-S), [B058](https://www.linkedin.com/posts/hackinghub_making-100k-with-caido-most-hackers-use-activity-7498038294308519936-QTyS), B254 (feed / source index) |
| [JS Analyzer (Caido)](https://github.com/caido-community/JS-Analyzer) | Passive analysis of JavaScript responses for URLs and endpoints. The demonstrated menu is JS Analyzer > Run JS Analyzer - Passive scan. | video frames at 00:30 and 00:50 | [B032](https://www.linkedin.com/posts/hackinghub_analyze-js-files-with-a-caido-plugin-activity-7506088489772544001-y3TD) |
| [Burp Suite](https://portswigger.net/burp) | Request replay, Intruder, scanning and comparison with Caido. Bambda, Repeater and Intruder are named in the comparison. Performance figures are one reported comparison, not general benchmarks. | caption; indexed post | B143 (feed / source index), [W_BURP_COMPARE](https://www.linkedin.com/feed/update/urn:li:activity:7433157394337021952) |
| [ffuf](https://github.com/ffuf/ffuf) | Content, extension and date-based log discovery | caption | [B120](https://www.linkedin.com/posts/hackinghub_easily-fuzz-log-files-using-a-wordlist-of-activity-7471569799580393472-Pta7), [B165](https://www.linkedin.com/posts/hackinghub_your-ffuf-command-isnt-returning-anything-activity-7446240755003846656-YFqq), [W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM), [W_FFUF_AC](https://www.linkedin.com/posts/hackinghub_is-your-ffuf-output-too-noisytry-using-activity-7359270018028589059--AQh) |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | Template-based checks and custom detection workflows | caption | [B153](https://www.linkedin.com/posts/hackinghub_looking-to-level-up-your-recon-with-nuclei-activity-7455020806557835264-xJHp), B187 (feed / source index), B255 (feed / source index), B302 (feed / source index) |
| [Nuclei Template Assistant](https://docs.projectdiscovery.io/cloud/editor/overview) | AI-assisted generation of Nuclei templates. Official documentation supplied as the reference. The precise product URL used in the clip was not recovered. | caption; poster inspected | B236 (feed / source index) |
| [Smuggler](https://github.com/defparam/smuggler) | HTTP request smuggling and desynchronization checks | caption; HackingHub comment link recovered | [B055](https://www.linkedin.com/posts/hackinghub_how-do-you-identify-an-http-request-smuggling-activity-7499157890889543680-94yf) |
| [Clairvoyance](https://github.com/nikitastupin/clairvoyance) | GraphQL schema reconstruction from field suggestions | caption; post link card | [B067](https://lnkd.in/p/dwTNjKPn) |
| [CRLFsuite](https://github.com/Nefcore/CRLFsuite) | CRLF and HTTP response-splitting checks. The post calls it Go. The matching maintainer repository is Python and says the project is no longer managed. | caption; independently matched maintainer repository | B087 (feed / source index) |
| [crlfuzz](https://github.com/dwisiswant0/crlfuzz) | CRLF injection scanning. Exact intended repository was not linked in the recovered caption. | caption; independently matched maintainer repository | B087 (feed / source index) |
| [Crlfix](https://github.com/RevoltSecurities/Crlfix) | Concurrent CRLF injection scanning. The post describes a patching utility. The matching maintainer project describes a scanner; intended identity remains uncertain. | caption; independently matched maintainer repository | B087 (feed / source index) |
| [Lupin-Holmes Sandwich](https://github.com/Lupin-Holmes/sandwich) | Generate candidate identifiers between observed UUIDv1 values. Predictability depends on generator behavior, timing, clock sequence and token validation. | caption; post link card | B143 (feed / source index) |

### Secrets / reversing

| Tool | Use shown or mentioned | Evidence | Sources |
|---|---|---|---|
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Search source and decoded app content for secrets. The APK pipeline frame uses --no-verification. Findings from that setting are not proof a credential is valid. | caption; selected video frame | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb), [B113](https://www.linkedin.com/posts/hackinghub_is-there-a-quick-way-to-find-juicy-information-activity-7476349076075073536-PG2a) |
| [apkeep](https://github.com/EFForg/apkeep) | Download Android APK packages | video frame at 00:28 | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb) |
| [Apktool](https://apktool.org/) | Decode Android APK resources and contents | video frame at 00:28 | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb) |
| [GDB](https://www.gnu.org/software/gdb/) | Debug and inspect programs | caption | B122 (feed / source index) |
| [GEF](https://github.com/hugsy/gef) | GDB Enhanced Features plugin. Their linked setup endpoint is https://gef.blah.cat/py. | caption | B122 (feed / source index) |

### AI assistance

| Tool | Use shown or mentioned | Evidence | Sources |
|---|---|---|---|
| [ChatGPT](https://chatgpt.com/) | Dataset collection and assistance with pentesting tasks. The demonstrated generated workflow is not independent validation of its output. | caption; poster inspected | B015 (feed / source index), [B076](https://www.linkedin.com/posts/hackinghub_this-is-how-nahamsec-uses-chatgptclaude-activity-7492272481823797248-k-G3) |
| [Claude / Claude Code](https://claude.ai/) | AI-assisted pentesting and bug-bounty setup. Specific setup instructions are in the attached video and were not recovered. | caption | [B076](https://www.linkedin.com/posts/hackinghub_this-is-how-nahamsec-uses-chatgptclaude-activity-7492272481823797248-k-G3), B080 (feed / source index) |
| Parseltongue | A named tool for exploring LLM guardrail bypasses. Several distinct projects share the name. The exact project and URL used by HackingHub were not confirmed. | caption only | B110 (feed / source index) |

### Command-line utilities

| Tool | Use shown or mentioned | Evidence | Sources |
|---|---|---|---|
| [curl](https://curl.se/docs/manpage.html) | Change User-Agent and inject custom request headers | caption; inspected images | B207 (feed / source index), [B227](https://www.linkedin.com/posts/hackinghub_many-wafs-auto-block-the-default-curl-user-agent-activity-7419401038283333634-jayc), B310 (feed / source index), [W_CURL](https://www.linkedin.com/posts/hackinghub_how-to-change-the-user-agent-header-from-activity-7338369933648588803-uZou) |
| [wget](https://www.gnu.org/software/wget/) | Download the GEF setup file in the shown command | caption | B122 (feed / source index) |
| [grep / sort / cat / xargs](https://www.gnu.org/software/coreutils/manual/coreutils.html) | Filter, deduplicate and pipe recon output. grep has its own manual: https://www.gnu.org/software/grep/manual/grep.html; xargs is part of GNU Findutils. | inspected images | B189 (feed / source index), B198 (feed / source index), B199 (feed / source index), B220 (feed / source index), [B227](https://www.linkedin.com/posts/hackinghub_many-wafs-auto-block-the-default-curl-user-agent-activity-7419401038283333634-jayc) |
| [dig](https://www.isc.org/bind/) | Resolve names before port discovery | inspected image | B198 (feed / source index) |
| [jq](https://jqlang.org/) | JSON processing in the APK secret-discovery script | video frame at 00:28 | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb) |
| [Sed / Awk / Vim](https://www.gnu.org/software/sed/) | Text processing and editing taught in Linux fundamentals. Awk: https://www.gnu.org/software/gawk/; Vim: https://www.vim.org/. | caption | B182 (feed / source index), B197 (feed / source index), B200 (feed / source index) |
| [alias](https://www.gnu.org/software/bash/manual/bash.html) | Shorten frequently used shell commands | caption | B068 (feed / source index), B160 (feed / source index) |
| [printenv / tr / rev / base64](https://www.gnu.org/software/coreutils/manual/coreutils.html) | Environment inspection and string transformations in the command-injection sheet. rev reference: https://github.com/util-linux/util-linux. | inspected image | B086 (feed / source index) |
| [Bash / PowerShell / Windows CMD](https://www.gnu.org/software/bash/manual/bash.html) | Shell behavior, environment variables and platform-dependent parsing. PowerShell reference: https://learn.microsoft.com/powershell/. The Windows snippet uses cmd.exe for report-command execution. | inspected image; selected video frame | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb), B086 (feed / source index), B203 (feed / source index), [B188](https://www.linkedin.com/posts/hackinghub_look-closely-running-microsoft-iis-on-a-activity-7436154259286478848-POOy) |
| [SSH / crontab](https://www.openssh.com/) | SSH keys and persistence examples involving authorized_keys and scheduled jobs. Techniques are summarized as concepts; no persistence was established on any system. | caption; inspected image | B075 (feed / source index), B203 (feed / source index) |
| [Python 3 / Java / GNU timeout](https://www.python.org/) | Runtime dependencies shown for the APK scanning pipeline. Java is a listed dependency. timeout reference: https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html. | video frame at 00:28 | [B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb) |

## Websites and learning resources

| Website | Why it appears | Evidence / qualification | Sources |
|---|---|---|---|
| [HackingHub](https://www.hackinghub.io/) | Platform, courses, labs and walkthroughs | caption | [B066](https://www.linkedin.com/posts/hackinghub_before-you-use-ai-for-web-app-hacking-build-activity-7495501444599705602-JVGs), B167 (feed / source index), B290 (feed / source index) |
| [HackingHub Hubs](https://app.hackinghub.io/hubs) | Hands-on labs | caption | [B066](https://www.linkedin.com/posts/hackinghub_before-you-use-ai-for-web-app-hacking-build-activity-7495501444599705602-JVGs), B093 (feed / source index), B193 (feed / source index) |
| [HackingHub Challenges](https://app.hackinghub.io/hubs?type=challenge) | Challenge catalog | caption | B209 (feed / source index), B276 (feed / source index) |
| [Assetnote Wordlists](https://wordlists.assetnote.io/) | Wordlists for content discovery | caption | [W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM) |
| [Additional ffuf wordlist link](https://lnkd.in/d-r2Keq) | A second wordlist resource linked in the ffuf post | caption — Destination could not be recovered; do not assume it is SecLists. | [W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM) |
| [GitHub](https://github.com/) | Code search, regex-based recon and a Subfinder data provider | caption | [B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH), B251 (feed / source index) |
| [Shodan](https://www.shodan.io/) | API-key source named for enriched Subfinder discovery | caption | [B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH) |
| [Censys](https://censys.com/) | API-key source named for enriched Subfinder discovery | caption | [B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH) |
| [Postman Documenter](https://documenter.getpostman.com/) | Search public API documentation for exposed examples or credentials | caption | [B142](https://www.linkedin.com/posts/hackinghub_youre-mapping-the-main-api-of-your-target-activity-7459603851524911104-0J0J) |
| [Google](https://www.google.com/) | Search indexed Postman documentation; compare search-engine coverage | caption | [B142](https://www.linkedin.com/posts/hackinghub_youre-mapping-the-main-api-of-your-target-activity-7459603851524911104-0J0J) |
| [Internet Archive / Wayback Machine](https://web.archive.org/) | Historical routes, old subdomains and legacy application surfaces | caption | B042 (feed / source index), B220 (feed / source index) |
| [WHOXY](https://www.whoxy.com/) | WHOIS lookups and reverse-WHOIS correlation | inspected video frame | [B150](https://www.linkedin.com/posts/hackinghub_what-if-you-could-find-every-unique-asset-activity-7456055740848521216-LxsQ) |
| [c99.nl](https://www.c99.nl/) | Developer-tool collection and Subdomain Finder | caption; poster inspected — APIs, File Uploader, Hide Files in Zip, Maximum user Info and Discord Status are visible on the homepage preview; individual use was not demonstrated. | B231 (feed / source index) |
| [ProjectDiscovery Chaos](https://chaos.projectdiscovery.io/) | Public bug-bounty subdomain data | caption | B234 (feed / source index), B312 (feed / source index) |
| [ProjectDiscovery Template Editor](https://docs.projectdiscovery.io/cloud/editor/overview) | Reference for the Nuclei Template Assistant | caption; poster inspected; official documentation | B236 (feed / source index) |
| [Wordfence Vulnerability Database](https://www.wordfence.com/threat-intel/vulnerabilities) | Review WordPress plugin vulnerability history and recurring patterns | poster inspected — Wordfence branding and this URL are visible in B238's poster. | [B238](https://www.linkedin.com/posts/hackinghub_stuck-on-a-wordpress-target-check-the-activity-7413988431917309952-hLfl), B288 (feed / source index) |
| [HackerOne](https://www.hackerone.com/) | A bounty-scope data source; also used as a recon example | posters / images inspected — Demo URLs do not establish client relationships or authorization to test those domains. | B015 (feed / source index), B189 (feed / source index), B220 (feed / source index) |
| [Bugcrowd](https://www.bugcrowd.com/) | Bounty-scope data and the BSidesSF collaboration | poster inspected; caption | B015 (feed / source index), B178 (feed / source index) |
| [Intigriti](https://www.intigriti.com/) | Bounty-scope data source named in an AI-generated workflow | poster inspected — The frame describes a proposed data collection workflow, not verified completeness. | B015 (feed / source index) |
| [YesWeHack](https://www.yeswehack.com/) | Bounty-scope data source named in an AI-generated workflow | poster inspected — The frame describes a proposed data collection workflow, not verified completeness. | B015 (feed / source index) |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Referenced in a HackingHub-reshared SSTI walkthrough | reshared contributor text — Mentioned by Jacob Simmons in the reshared post; not an assertion about HackingHub's internal workflow. | [B129](https://www.linkedin.com/posts/hackinghub_how-to-hack-a-website-with-ssti-hackinghub-activity-7468679617533472768-DM2o) |
| [PortSwigger Research](https://portswigger.net/research) | HackingHub reposts work on CRLF-powered desynchronization | reposted contributor caption | B073 (feed / source index) |
| [NahamCon](https://www.nahamcon.com/) | Conference and CTF resources | caption | B250 (feed / source index), B256 (feed / source index), B258 (feed / source index) |
| [Snyk Fetch the Flag](https://snyk.co/ujxq4) | A training CTF co-hosted with HackingHub | caption — The recovered event dates are historical; the link is preserved as a resource. | B217 (feed / source index), B225 (feed / source index) |
| [HackingHub Discord](https://discord.com/invite/Nnde3YpwCC) | Community invite recovered from their post | post link card — Invite validity was not tested. | [B282](https://www.linkedin.com/posts/hackinghub_join-the-hackinghub-discord-server-activity-7394811895322591232-plmR) |
| [GEF setup endpoint](https://gef.blah.cat/py) | Endpoint linked in the GDB/GEF post | caption | B122 (feed / source index) |

The outbound-links.csv preserves additional course, Hub, walkthrough and event links found in the feed. Shortened links are retained when their destinations were not recovered. Names in a reshared event or a software sidebar are not treated as demonstrated workflow use.

## Tips and testing leads

All entries are also in tips.csv for filtering by category, source or evidence type.

### Methodology

- **T001 — Follow a repeatable hunting process.** Choose a target, understand users and data, form a hypothesis, test paths deeply, then validate impact. ([B215](https://www.linkedin.com/posts/hackinghub_how-do-you-turn-a-maybe-bug-into-a-real-activity-7426007401759199232-dz1g); Inspected process image).
- **T002 — Learn one program deeply.** Focus on a target long enough to understand its product, workflows and recurring implementation patterns. ([W_FOCUS](https://www.linkedin.com/posts/hackinghub_chasing-every-bug-bounty-program-kills-your-activity-7356561128484737024-KJ6U), [W_BEGINNER](https://www.linkedin.com/posts/hackinghub_beginner-bug-bounty-hunters-fail-because-activity-7354552425510326272-Heu2); Author caption).
- **T003 — Read previous disclosures.** Study a program's public reports to learn its historical weak points and accepted finding types. ([W_FOCUS](https://www.linkedin.com/posts/hackinghub_chasing-every-bug-bounty-program-kills-your-activity-7356561128484737024-KJ6U); Author caption).
- **T004 — Match tests to business logic.** Prioritize features and consequences that matter to the application rather than running the same checklist everywhere. ([W_BEGINNER](https://www.linkedin.com/posts/hackinghub_beginner-bug-bounty-hunters-fail-because-activity-7354552425510326272-Heu2), B082 (feed / source index); Author caption).
- **T005 — Build consistent practice.** The beginner roadmap recommends regular short sessions, written progress notes and weekly reflection. ([W_BEGINNER](https://www.linkedin.com/posts/hackinghub_beginner-bug-bounty-hunters-fail-because-activity-7354552425510326272-Heu2); Author caption). The promised payout is not a guaranteed outcome.
- **T006 — Use a four-week learning structure.** The suggested sequence is program selection, deep exploration, methodical testing, and combining validated flaws. ([W_BEGINNER](https://www.linkedin.com/posts/hackinghub_beginner-bug-bounty-hunters-fail-because-activity-7354552425510326272-Heu2); Author caption).
- **T007 — Read documentation first.** API docs, changelogs and error messages reveal intended behavior and overlooked entry points. (B078 (feed / source index); Author caption).
- **T008 — Ask how an entry point was found.** Learn the researcher's reasoning and discovery path, alongside the final payload. ([B185](https://www.linkedin.com/posts/hackinghub_where-is-the-write-up-is-the-wrong-question-activity-7437271640649949184-sig4), [B095](https://www.linkedin.com/posts/hackinghub_reading-about-a-vulnerability-and-exploiting-activity-7485348529649934336-yEfc); Author caption).
- **T009 — Practice and debug actively.** Use realistic labs and work through failed attempts instead of relying entirely on watched tutorials. (B196 (feed / source index), [B066](https://www.linkedin.com/posts/hackinghub_before-you-use-ai-for-web-app-hacking-build-activity-7495501444599705602-JVGs); Author caption).
- **T010 — Investigate authorized gated products.** Business-facing applications and less-obvious user journeys can add useful attack surface. ([B219](https://www.linkedin.com/posts/hackinghub_want-to-find-the-bugs-everyone-else-is-missing-activity-7424558140874088448-rf7O); Author caption).
- **T011 — Keep report quality in the workflow.** A finding's explanation and evidence matter alongside the technical discovery. (B126 (feed / source index); Author caption). The detailed report-writing advice is in a video and was not transcribed.
- **T012 — Read the scope.** Use the program's scope to guide asset selection and permitted testing. (B216 (feed / source index); Author caption).

### Recon

- **T013 — Map, fingerprint, enrich, prioritize.** Collect domains, IPs and ASNs; identify headers, libraries and CMSs; map complexity and endpoints; focus manual effort on promising applications. (B195 (feed / source index); Author caption).
- **T014 — Configure Subfinder providers.** Add relevant provider credentials and understand the effect of the -all option on available sources. ([B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH); Author caption).
- **T015 — Check recursive enumeration behavior.** The post highlights -recursive for deeper discovery. Read the provider behavior rather than assuming the flag brute-forces every descendant. ([B155](https://www.linkedin.com/posts/hackinghub_you-ran-default-subfinder-and-are-wondering-activity-7453156202361827328-32qH); Author caption with documentation caveat).
- **T016 — Build a DNS-to-HTTP pipeline.** The shown workflow connects Subfinder, dnsx and httpx, retaining status, title, technology and IP information. (B199 (feed / source index), B223 (feed / source index); Inspected image; caption).
- **T017 — Preserve useful non-200 responses.** Their httpx example retains redirects and 403/404 responses as well as 200s; these can help map behavior. (B199 (feed / source index); Inspected image). A response code by itself is not proof an endpoint exists or is vulnerable.
- **T018 — Crawl parameterized URLs.** Use Katana to collect query URLs, uro to reduce duplication, then httpx to identify live endpoints. (B189 (feed / source index); Inspected image).
- **T019 — Resolve before port discovery.** The mass-recon image connects a domain list, dig and Naabu's top-port discovery. (B198 (feed / source index); Inspected image).
- **T020 — Separate discovery from enumeration.** Use fast initial discovery with RustScan, focused Nmap enumeration, and background verification. (B169 (feed / source index); Author caption).
- **T021 — Understand Nmap options.** The scanning image names service-version detection and default scripts as different enumeration steps. (B308 (feed / source index); Inspected image). The image is a meme, not a validated packet-evasion tutorial.
- **T022 — Filter historical URLs.** Use waybackurls, then filter for interesting API, admin and versioned routes and deduplicate the result. (B220 (feed / source index); Inspected image).
- **T023 — Compare legacy and current surfaces.** Look for old login/admin/API paths, archived subdomains and versioned routes after platform migrations. (B042 (feed / source index); Author caption).
- **T024 — Compare legacy authentication.** On permitted test accounts, compare current credentials and unauthenticated behavior against legacy endpoints. (B042 (feed / source index); Author caption).
- **T025 — Inspect leftover migration files.** A posted example highlights a backup web.config remaining after an IIS-to-Nginx migration. (B181 (feed / source index), B184 (feed / source index); Inspected image; caption). The image does not establish which secrets, if any, the file contains.
- **T026 — Correlate WHOIS records.** Use shared registrant details as leads for reverse-WHOIS discovery; WHOXY is visible in the demo. ([B150](https://www.linkedin.com/posts/hackinghub_what-if-you-could-find-every-unique-asset-activity-7456055740848521216-LxsQ); Caption and inspected video frame). Privacy redaction and unrelated registrations limit completeness and ownership conclusions.
- **T027 — Use passive subdomain datasets.** ProjectDiscovery Chaos and c99's Subdomain Finder are repeatedly mentioned as discovery resources. (B043 (feed / source index), B231 (feed / source index), B234 (feed / source index), B312 (feed / source index); Author caption).
- **T028 — Go beyond simple GitHub searches.** The post recommends advanced regex-based code searches instead of only entering a domain name. (B251 (feed / source index); Author caption). Specific regex patterns are in a video and were not recovered.
- **T029 — Search public Postman documentation.** Search indexed Documenter pages for target documentation, example Authorization headers, API keys and client secrets. ([B142](https://www.linkedin.com/posts/hackinghub_youre-mapping-the-main-api-of-your-target-activity-7459603851524911104-0J0J); Author caption). The post's claims about publishing defaults and frequent live tokens were not independently validated.
- **T030 — Compare search-engine coverage.** Use more than one search engine when looking for published documentation and overlooked assets. ([B142](https://www.linkedin.com/posts/hackinghub_youre-mapping-the-main-api-of-your-target-activity-7459603851524911104-0J0J); Author caption).
- **T031 — Read newsletters and integrations.** Marketing emails, unsubscribe links and third-party workflows may reveal raw IDs absent from the main application. ([B141](https://www.linkedin.com/posts/hackinghub_i-was-recently-hunting-for-idor-in-a-web-activity-7460403905311453186-s44A), B159 (feed / source index); Author caption).

### Content discovery

- **T032 — Use an explicit fuzz position.** Choose the part of a URL or request to fuzz and use a relevant wordlist rather than an arbitrary large list. ([W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM); Author caption).
- **T033 — Calibrate noisy ffuf output.** Use -ac for baseline calibration and -fs when a known response size creates noise. ([W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM), [W_FFUF_AC](https://www.linkedin.com/posts/hackinghub_is-your-ffuf-output-too-noisytry-using-activity-7359270018028589059--AQh); Author caption).
- **T034 — Try extensions and recursion.** The ffuf introduction highlights extension candidates and recursive discovery after finding directories. ([W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM); Author caption).
- **T035 — Inspect status and response patterns.** Prioritize unusual files and response differences while checking custom 404s and wildcard responses. ([W_FFUF](https://www.linkedin.com/posts/hackinghub_how-to-use-ffuf-for-the-first-time-1-activity-7375939906684010498-bdUM), [W_FFUF_AC](https://www.linkedin.com/posts/hackinghub_is-your-ffuf-output-too-noisytry-using-activity-7359270018028589059--AQh); Author caption). Do not automatically discard every same-size or 404 response; they are signals to investigate.
- **T036 — Tune the request rate.** If discovery produces little useful output, investigate filtering and rate limits, reduce rate, and use appropriate headers. ([B165](https://www.linkedin.com/posts/hackinghub_your-ffuf-command-isnt-returning-anything-activity-7446240755003846656-YFqq); Author caption).
- **T037 — Use date-based log wordlists.** Find the log directory, then test date-derived filenames; the example combines auto-calibration with matching 200 responses. ([B120](https://www.linkedin.com/posts/hackinghub_easily-fuzz-log-files-using-a-wordlist-of-activity-7471569799580393472-Pta7); Author caption).
- **T038 — Check familiar high-value flows.** Login, reset-password, upload, object APIs, search, file views and admin functions are suggested places to focus. ([B177](https://www.linkedin.com/posts/hackinghub_keep-your-eyes-peeled-on-these-endpoints-activity-7440472615665688576-k5El); Author caption). Path names are clues, not vulnerability diagnoses.
- **T039 — Use context when prioritizing.** Old or complex applications can be promising for manual work, but the endpoint's actual behavior determines the useful test. (B195 (feed / source index), [W_BEGINNER](https://www.linkedin.com/posts/hackinghub_beginner-bug-bounty-hunters-fail-because-activity-7354552425510326272-Heu2); Author caption).

### Access control / business logic

- **T040 — Test controlled object substitutions.** Compare access to objects belonging to two test users; object IDs can appear in APIs and secondary workflows. ([B139](https://www.linkedin.com/posts/hackinghub_hacking-tricks-that-may-still-work-in-2026-activity-7461808384506507264-ICAI), [B141](https://www.linkedin.com/posts/hackinghub_i-was-recently-hunting-for-idor-in-a-web-activity-7460403905311453186-s44A); Author caption).
- **T041 — Try identifier type variations.** Booleans, arrays, zero and whitespace variants can reveal coercion or inconsistent ID handling. ([B205](https://www.linkedin.com/posts/hackinghub_sometimes-idor-isnt-just-about-changing-activity-7430325737297035264-fKJQ); Author caption). A boolean matching an admin record is a suggested possibility, not a universal database behavior.
- **T042 — Check duplicate JSON keys.** Compare how validation layers and the backend interpret repeated keys for the same field. (B151 (feed / source index); Author caption).
- **T043 — Check repeated query or form parameters.** Repeated IDs, arrays and list-like formats can reveal parser disagreement between layers. (B127 (feed / source index), [B139](https://www.linkedin.com/posts/hackinghub_hacking-tricks-that-may-still-work-in-2026-activity-7461808384506507264-ICAI); Author caption). Exact first/last/array behavior depends on the stack and configuration.
- **T044 — Derive mass-assignment candidates.** Compare fields returned by GET with fields accepted by updates; also inspect docs, JavaScript and errors. (B132 (feed / source index); Author caption).
- **T045 — Check sensitive update fields.** Investigate whether role, plan, admin status, organization or tenant fields are accepted from a client. (B132 (feed / source index), B190 (feed / source index); Author caption; analysis of inspected code). Returned values alone do not prove a persisted privilege change.
- **T046 — Distinguish authentication from ownership.** The code example verifies a token yet selects the target object using a client-controlled ID. (B190 (feed / source index); Analysis of inspected code). Additional middleware or schema restrictions are not shown.
- **T047 — Check tenant boundaries.** Test whether organization and tenant identifiers can change access across controlled test tenants. (B132 (feed / source index); Author caption).
- **T048 — Inspect price and amount handling.** Check whether the server trusts client-supplied prices or financial amounts. ([B139](https://www.linkedin.com/posts/hackinghub_hacking-tricks-that-may-still-work-in-2026-activity-7461808384506507264-ICAI), B161 (feed / source index); Author caption; analysis of inspected code).
- **T049 — Look for negative amount flaws.** The withdrawal example lacks a positive-amount check, making negative values an important review case. (B161 (feed / source index); Analysis of inspected code). Illustrative code; not a confirmed finding in a live application.
- **T050 — Review atomicity of state changes.** The withdrawal example separates the balance check from its update and includes a delay; review concurrent execution and locking. (B161 (feed / source index); Analysis of inspected code). Exploitability depends on concurrency and the surrounding implementation.
- **T051 — Inspect cross-application trust.** Profile synchronization from a hardened core application into a less-protected sub-application can create authorization gaps. (B162 (feed / source index), B172 (feed / source index); Author caption).
- **T052 — Recognize UUIDv1 reset-token risks.** Version-one UUIDs encode time-related data; the post links a sandwich generator for exploring candidate values between controlled samples. (B143 (feed / source index); Author caption; linked tool). UUIDv1 alone does not establish account takeover or feasible token prediction.
- **T053 — Check identity headers at trust boundaries.** The Go snippet directly consumes X-Authenticated-User before returning account data; verify trusted-gateway enforcement. ([B173](https://www.linkedin.com/posts/hackinghub_did-you-see-the-flaw-activity-7441544716812431360-3iP_); Analysis of inspected code). The snippet does not show deployment middleware or which clients can reach it.
- **T054 — Reject client-controlled privilege flags.** The Python example trusts the truthiness of a supplied is_admin field; validate types and derive privileges on the server. (B211 (feed / source index); Analysis of inspected code).

### Routing / HTTP behavior

- **T055 — Compare HTTP methods.** Authorization and CSRF checks may differ across GET, POST, PUT and PATCH paths. (B118 (feed / source index), [B139](https://www.linkedin.com/posts/hackinghub_hacking-tricks-that-may-still-work-in-2026-activity-7461808384506507264-ICAI); Author caption).
- **T056 — Inspect method-override handling.** The post mentions X-HTTP-Method-Override and _method parameters as alternate routes through server behavior. (B118 (feed / source index); Author caption).
- **T057 — Compare normalized path variants.** Double slashes, dot segments, encoded slashes and trailing slashes can expose disagreement between edge and application routing. ([B028](https://www.linkedin.com/posts/hackinghub_want-to-access-the-admin-panel-try-these-activity-7507537958053412864-lF6-), [B139](https://www.linkedin.com/posts/hackinghub_hacking-tricks-that-may-still-work-in-2026-activity-7461808384506507264-ICAI); Author caption).
- **T058 — Inspect rewrite headers.** Check whether X-Original-URL or X-Rewrite-URL can influence origin routing differently from edge checks. ([B028](https://www.linkedin.com/posts/hackinghub_want-to-access-the-admin-panel-try-these-activity-7507537958053412864-lF6-); Author caption). The headers need explicit server support; sending them is not automatically an authorization bypass.
- **T059 — Check forwarded-IP trust.** The cURL image sets forwarding and remote-IP headers; test whether untrusted values alter protected behavior. (B207 (feed / source index); Inspected image). This is not CRLF injection and does not itself prove a bypass.
- **T060 — Compare User-Agent behavior.** Use curl's -A option to compare browser and mobile responses when basic client filtering affects requests. ([B227](https://www.linkedin.com/posts/hackinghub_many-wafs-auto-block-the-default-curl-user-agent-activity-7419401038283333634-jayc), B310 (feed / source index), [W_CURL](https://www.linkedin.com/posts/hackinghub_how-to-change-the-user-agent-header-from-activity-7338369933648588803-uZou); Caption; inspected images).
- **T061 — Review Nginx URI replacement.** A mismatched location/proxy_pass slash boundary can create surprising upstream paths. ([B147](https://www.linkedin.com/posts/hackinghub_are-you-testing-an-app-that-uses-nginx-as-activity-7457496993876033537-wa11); Author caption). Forwarding an /etc/passwd-shaped URI is not proof the server can read a local file.

### XSS

- **T062 — Identify the exact output context.** Inspect whether input reaches HTML, an attribute, a script, a style block or a JavaScript string before choosing a test. ([W_XSS_CONTEXT](https://www.linkedin.com/posts/hackinghub_your-payload-wont-fire-if-it-lands-in-the-activity-7372315465941049344-aG-3); Author caption).
- **T063 — Preserve surrounding syntax.** The XSS post describes closing the relevant context and handling trailing syntax so an attempted payload can execute. ([W_XSS_CONTEXT](https://www.linkedin.com/posts/hackinghub_your-payload-wont-fire-if-it-lands-in-the-activity-7372315465941049344-aG-3); Author caption).
- **T064 — Inspect interaction-dependent handlers.** An event handler may require user interaction; onmouseover is named in a post. (B229 (feed / source index); Author caption).
- **T065 — Use JavaScript-appropriate encoding.** The PHP challenge inserts HTML-escaped data into a JavaScript template literal; HTML escaping does not address every JavaScript interpolation case. (B123 (feed / source index); Analysis of inspected code).
- **T066 — Review DOM clobbering.** The challenge assigns HTML to innerHTML and reads a named window property as configuration before creating a script element. (B192 (feed / source index); Analysis of inspected code). Behavior depends on browser named-property handling and any surrounding sanitization.
- **T067 — Capture blind-execution context.** For a validated blind-XSS execution, the post suggests recording its URL, origin and document title to understand the affected workflow. ([B035](https://www.linkedin.com/posts/hackinghub_triggering-blind-xss-isnt-the-end-goal-activity-7504955991172657152-J_nU); Author caption).
- **T068 — Use execution context as a lead.** Internal route and parameter names revealed by a callback may guide further permitted investigation. ([B035](https://www.linkedin.com/posts/hackinghub_triggering-blind-xss-isnt-the-end-goal-activity-7504955991172657152-J_nU); Author caption). A callback alone does not establish internal-tool takeover.
- **T069 — Account for delayed processing.** A support-ticket meme highlights that blind-XSS callbacks can arrive later when submitted input is processed. ([B131](https://www.linkedin.com/posts/hackinghub_me-staring-at-my-callback-server-waiting-activity-7468029339880615936-II2U); Caption-backed inference). The meme's three-week delay is not a measured general waiting period.

### CSRF

- **T070 — Check token presence and validity.** Compare missing and malformed CSRF-token behavior on a state-changing operation. ([W_CSRF](https://www.linkedin.com/posts/hackinghub_csrf-protections-arent-always-as-strong-activity-7370881289375109120-uO-v); Author caption).
- **T071 — Check session binding.** Compare a token from one controlled session with a request from another controlled session. ([W_CSRF](https://www.linkedin.com/posts/hackinghub_csrf-protections-arent-always-as-strong-activity-7370881289375109120-uO-v); Author caption).
- **T072 — Compare state-changing methods.** The post suggests checking whether a state change also occurs through GET and can be triggered by browser elements. ([W_CSRF](https://www.linkedin.com/posts/hackinghub_csrf-protections-arent-always-as-strong-activity-7370881289375109120-uO-v); Author caption). Confirm a real cross-origin browser action; SameSite cookies and other protections can prevent exploitation.

### Injection / code review

- **T073 — Understand command separators.** The command-injection sheet compares separators, pipelines, conditional execution and URL encodings. (B086 (feed / source index); Inspected image). Shell and operating-system behavior differ.
- **T074 — Check normalization and filtering assumptions.** The sheet includes whitespace substitutions, environment substrings, quoting, case transformations and encodings as review ideas. (B086 (feed / source index); Inspected image). No claim that these evade every filter.
- **T075 — Review dynamic SQL identifiers.** A parameterized WHERE clause does not automatically make a client-controlled ORDER BY expression safe. (B121 (feed / source index); Analysis of inspected code). Actual behavior depends on query-builder escaping and surrounding validation.
- **T076 — Do not rely on blacklists around eval.** The Python challenge filters strings and then evaluates the supplied expression; review this as a dangerous evaluation boundary. (B164 (feed / source index); Analysis of inspected code).
- **T077 — Check XML entity settings.** The XML challenges explicitly enable entity expansion in lxml and libxmljs. (B163 (feed / source index), B221 (feed / source index); Analysis of inspected code). File/network access depends on parser options and execution environment.
- **T078 — Review path concatenation.** The ASP.NET examples concatenate user-controlled names with file paths; review canonicalization and permitted directory boundaries. ([B188](https://www.linkedin.com/posts/hackinghub_look-closely-running-microsoft-iis-on-a-activity-7436154259286478848-POOy), [B191](https://www.linkedin.com/posts/hackinghub_did-you-notice-it-too-if-not-read-activity-7435006740636729344-upsW); Analysis of inspected code).
- **T079 — Review shell-command construction.** The Windows snippet concatenates a report parameter into a command passed to cmd.exe. ([B188](https://www.linkedin.com/posts/hackinghub_look-closely-running-microsoft-iis-on-a-activity-7436154259286478848-POOy); Analysis of inspected code).
- **T080 — Inspect deserialization side effects.** The PHP example unserializes a cookie into a class whose destructor writes a file. ([B186](https://www.linkedin.com/posts/hackinghub_tell-us-how-busted-is-this-one-activity-7436848781955903488-Dpry); Analysis of inspected code). Arbitrary write or code execution depends on writable paths and server execution behavior.
- **T081 — Separate upload acceptance from execution.** The upload post combines image signatures with executable-looking extensions; inspect the entire storage and execution path. ([B133](https://www.linkedin.com/posts/hackinghub_hackinghub-activity-7466594717674258432-IKzW); Author caption). An accepted upload alone is not remote code execution.
- **T082 — Validate login input types.** The Express/MongoDB example passes an email value into a database lookup; review object-valued input and query semantics. (B176 (feed / source index); Analysis of inspected code). No live NoSQL injection or authentication bypass was established.
- **T083 — Compare login timing carefully.** The example returns early for an absent user but performs bcrypt work for an existing user, suggesting a timing-review lead. (B176 (feed / source index); Analysis of inspected code). Reliable enumeration requires measurement and evaluation of surrounding controls.
- **T084 — Handle optional state consistently.** The Python logging challenge defaults logs to None but uses it as a container without initializing it. ([B218](https://www.linkedin.com/posts/hackinghub_most-python-devs-scroll-past-this-should-activity-7424882230730055680-VOR6); Analysis of inspected code). This demonstrates a reliability bug; no security impact is established.
- **T085 — Use bounded regex patterns.** The hash-extraction challenge asks for complete MD5-shaped strings while avoiding matches embedded in longer identifiers. (B166 (feed / source index); Inspected challenge image). A 32-character hexadecimal shape does not prove that a value is an MD5 digest.
- **T086 — Inspect controlled error responses.** Malformed JSON, unusual input or missing pages can reveal debug traces, software versions or internal infrastructure details. (B105 (feed / source index); Author caption). Use measured test inputs; no debug disclosure was observed on a real target.

### Cache / desynchronization

- **T087 — Compare CDN and origin parsing.** The cache-deception post uses suffixes, delimiters and encoded path variants to investigate different interpretations of a private endpoint. ([B027](https://www.linkedin.com/posts/hackinghub_web-cache-deception-tricks-get-apime-activity-7507822592330956801-Lcgo); Author caption).
- **T088 — Verify a cache-deception consequence.** Confirm whether a private response becomes retrievable from the cache by an unauthorized session. ([B027](https://www.linkedin.com/posts/hackinghub_web-cache-deception-tricks-get-apime-activity-7507822592330956801-Lcgo); Analytical qualification of the author's testing idea). Cache headers or a modified URL alone do not establish a data leak.
- **T089 — Combine CRLF scanning with manual review.** The post recommends initial coverage with tools, then manual investigation of reflected header input and context-dependent chains. (B087 (feed / source index); Author caption).
- **T090 — Investigate desynchronization as a framing issue.** Smuggler is explicitly recommended; a repost connects HTTP header injection with response-queue poisoning research. ([B055](https://www.linkedin.com/posts/hackinghub_how-do-you-identify-an-http-request-smuggling-activity-7499157890889543680-94yf), B073 (feed / source index); Author caption; reposted researcher caption). Attached demonstrations were not fully transcribed.

### GraphQL

- **T091 — Use error suggestions as schema clues.** Disabled introspection may still leave field and type suggestions in malformed-query errors. ([B067](https://lnkd.in/p/dwTNjKPn); Author caption).
- **T092 — Reconstruct incrementally.** The post recommends probing candidate field names and walking valid field/type suggestions; Clairvoyance is linked. ([B067](https://lnkd.in/p/dwTNjKPn); Author caption).
- **T093 — Review per-request versus per-operation limits.** The post highlights aliases and batching as areas where accounting may differ. ([B067](https://lnkd.in/p/dwTNjKPn); Author caption). Some servers reject batching. Faster enumeration is not proof of unauthorized data access.

### Secrets / reversing

- **T094 — Inspect decoded app content.** The observed pipeline downloads APKs, decodes bundles, then scans their content with TruffleHog. ([B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb), [B113](https://www.linkedin.com/posts/hackinghub_is-there-a-quick-way-to-find-juicy-information-activity-7476349076075073536-PG2a); Caption; video frame at 00:28).
- **T095 — Keep structured provenance.** The shown APK script records package-tagged findings, counts and failures in JSONL and continues after package failures. ([B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb); Video frame at 00:28).
- **T096 — Treat unverified findings as candidates.** The pipeline uses --no-verification; distinguish a matching secret string from a valid, usable credential. ([B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb); Video frame at 00:28; analytical qualification).
- **T097 — Use GEF with GDB.** The GDB post links the GEF setup file to add reverse-engineering features. (B122 (feed / source index); Author caption).
- **T098 — Understand scan visibility.** The Void Step lab description emphasizes recognizing Nmap activity from a defender's perspective. (B124 (feed / source index); Author caption).
- **T099 — Inspect persistence mechanisms as separate paths.** The Bash image shows startup scripts, cron jobs and authorized SSH keys as persistence mechanisms. (B203 (feed / source index); Inspected image). No persistence commands were executed.

### AI security / assistance

- **T100 — Keep human judgment in the workflow.** The post highlights context, business logic and creative chaining as skills not replaced by AI automation. (B082 (feed / source index); Author caption).
- **T101 — Preserve dataset provenance.** The AI-generated scope-to-APK workflow distinguishes store links, publisher pages, extracted names and inferred package guesses. (B015 (feed / source index); Inspected video poster). Its resulting dataset and completeness were not validated.
- **T102 — Validate generated automation.** The APK demo's generated summary says only syntax and mocked scenarios were checked; live downloads and scans were untested. ([B016](https://www.linkedin.com/posts/hackinghub_mass-hunting-of-secrets-has-never-been-this-activity-7511446577710841856-Gdmb); Inspected video frame). Do not turn an AI-generated success statement into an observed result.
- **T103 — Include indirect prompt sources.** Documents, emails, web content and connectors can carry instructions that an AI application mistakenly trusts. ([B072](https://www.linkedin.com/posts/hackinghub_what-is-indirect-prompt-injection-and-why-activity-7493447775943225344-tZeb), B069 (feed / source index); Author caption).
- **T104 — Test backend-tool boundaries.** The chatbot case study emphasizes integrated tools and business logic when front-end HTML or markdown rendering is restricted. ([B053](https://www.linkedin.com/posts/hackinghub_this-is-how-you-exfiltrate-sensitive-data-activity-7499927781183475712-CKls); Author caption).
- **T105 — Compare semantic input variants.** The case study describes changed wording and business-context framing as ways of probing keyword-based guardrails. ([B053](https://www.linkedin.com/posts/hackinghub_this-is-how-you-exfiltrate-sensitive-data-activity-7499927781183475712-CKls); Author case-study recap). A described technique is not evidence of a universal guardrail bypass.
- **T106 — Observe permitted callback channels.** The case study describes a domain-checking tool and DNS callbacks as an alternate data path. ([B053](https://www.linkedin.com/posts/hackinghub_this-is-how-you-exfiltrate-sensitive-data-activity-7499927781183475712-CKls); Author case-study recap). No callback or exfiltration was performed during this research.
- **T107 — Inspect chat requests.** The caption highlights intercepting the HTTP request behind an AI chat as a testing surface. ([B022](https://www.linkedin.com/posts/hackinghub_intercepting-the-http-request-your-browser-activity-7509667149909532673-M8t2); Caption-backed testing lead). The exact fields and tampering examples are inside an untranscribed video.
- **T108 — Treat agent memory as an attack surface.** The Copilot-memory caption identifies persistent assistant state as a security-research topic. (B037 (feed / source index); Caption-backed testing lead). The mechanism and demonstrated exploit were not recovered.
- **T109 — Review AI-generated Nuclei templates.** The Template Assistant is shown as a generator; review matchers, requests and detection logic before relying on a template. (B236 (feed / source index), B255 (feed / source index); Caption; poster inspected; official documentation qualification).

### Shell workflow

- **T110 — Use aliases for frequent commands.** Two posts recommend shell aliases for common command sequences. (B068 (feed / source index), B160 (feed / source index); Author caption).
- **T111 — Learn text-processing tools.** The Linux course posts explicitly add Sed, Awk and Vim for editing and processing data. (B182 (feed / source index), B197 (feed / source index), B200 (feed / source index); Author caption).

### Learning resources

- **T112 — Use realistic labs and walkthroughs.** HackingHub repeatedly points to Hubs built from disclosed findings and walkthroughs that explain researcher choices. ([B066](https://www.linkedin.com/posts/hackinghub_before-you-use-ai-for-web-app-hacking-build-activity-7495501444599705602-JVGs), B093 (feed / source index), [B095](https://www.linkedin.com/posts/hackinghub_reading-about-a-vulnerability-and-exploiting-activity-7485348529649934336-yEfc); Author caption).
- **T113 — Practice full reconnaissance in Missions.** Missions are described as larger business-like environments requiring asset discovery and linked findings. (B240 (feed / source index); Author caption).
- **T114 — Learn historical vulnerability patterns.** The WordPress post shows Wordfence's database and recommends reviewing a plugin's vulnerability history and related-plugin patterns. ([B238](https://www.linkedin.com/posts/hackinghub_stuck-on-a-wordpress-target-check-the-activity-7413988431917309952-hLfl), B288 (feed / source index); Caption; inspected poster).
- **T115 — Assign and track team practice.** The Teams post describes selecting a Hub, assigning learners and a deadline, then tracking completion. (B059 (feed / source index), B088 (feed / source index); Author caption).

## Corrections and limits worth preserving

| Source claim / shortcut | What the evidence supports |
|---|---|
| CRLFsuite described as Go | The [matching maintainer repository](https://github.com/Nefcore/CRLFsuite) identifies Python and says it is no longer managed. The intended repository was not linked in the caption. |
| crlfix described as a request-patching utility | The [matching Crlfix maintainer project](https://github.com/RevoltSecurities/Crlfix) describes a CRLF scanner. Exact intended identity is uncertain. |
| A missing or invalid CSRF token proves CSRF | A real cross-origin browser-triggered state change must still be demonstrated; other protections may block it. |
| An Nginx traversal-shaped upstream URI means filesystem access | URI forwarding, accessible internal routes and local file reading are different observations. The latter depends on origin behavior. |
| A magic-byte upload bypass means RCE | Acceptance, storage path, executable extension handling and execution require separate evidence. |
| UUIDv1 necessarily means account takeover | Token-generation details and validation determine feasible prediction and actual account impact. |
| A blind-XSS callback means internal takeover | Confirm actual script execution and the affected authorization context before extending the impact claim. |
| An AI-generated pipeline is tested | The inspected APK-script summary explicitly says live downloads and execution were not tested. |
| One Burp/Caido comparison proves a general performance ranking | The post reports a single comparison. It is useful context, not a general benchmark. |

## Incidental names and illustrative technologies

- **Resurface; Screenshot Mode; Panes; Shift; Workflows Store:** Plugin names visible in the JS Analyzer demo sidebar. Presence in the sidebar only; use or endorsement of these plugins was not demonstrated. ([B032](https://www.linkedin.com/posts/hackinghub_analyze-js-files-with-a-caido-plugin-activity-7506088489772544001-y3TD)).
- **Nginx; IIS / ASP.NET; WordPress; Tomcat; Next.js:** Platforms mentioned in labs, challenge snippets or target-testing tips. These are technologies to recognize, not a confirmed internal HackingHub software stack. ([B147](https://www.linkedin.com/posts/hackinghub_are-you-testing-an-app-that-uses-nginx-as-activity-7457496993876033537-wa11), [B188](https://www.linkedin.com/posts/hackinghub_look-closely-running-microsoft-iis-on-a-activity-7436154259286478848-POOy), [B238](https://www.linkedin.com/posts/hackinghub_stuck-on-a-wordpress-target-check-the-activity-7413988431917309952-hLfl), B296 (feed / source index), B292 (feed / source index)).
- **Flask; Express; MongoDB; TypeORM; lxml; libxmljs; bcrypt:** Libraries or frameworks visible in challenge images. Included as vocabulary from the examples; no claims about production targets. (B121 (feed / source index), B161 (feed / source index), B163 (feed / source index), B176 (feed / source index), B190 (feed / source index), B221 (feed / source index)).

## How to follow a source

B001–B315 are entries in the captured signed-in feed, in recent-first order. W001–W090 are indexed post pages. W_FFUF and similar labels are aliases for known indexed pages. post-index.csv contains recovered individual URLs, visible relative ages, media coverage and associated tips. When an individual permalink was not recovered, the title and feed URL are provided, and an inspected image URL is included where available. Image URLs are signed CDN URLs and may expire.

The original web search and browser capture overlap. Source IDs are evidence records, not a claim that every indexed page is an additional unique post. Video topics with missing steps remain visible in the coverage file rather than being expanded into invented instructions.
