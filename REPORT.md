# Hermes and Caido security workbench: research and verification

**Reviewed:** 2026-10-26 · **Platform:** Apple Silicon macOS · **Purpose:** desktop-first, evidence-led work on authorized bug bounty programs and CTFs.

## Sources and decisions

The setup follows current primary documentation for [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop), [profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles), [Codex app-server runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime), [Caido MCP](https://docs.caido.io/app/tutorials/mcp), [OpenAI Daybreak](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview), [OBS](https://obsproject.com/kb/mac-installation), [OWASP WSTG](https://wstg.owasp.org/), and the public-report publishers linked in the catalog. Installed versions and test results below came from local commands or app UI, not release-page assumptions.

The active Hermes `security` profile requests Daybreak Blue with `gpt-6-sol` through Codex CLI 0.164.0. `astra` and `sol61` are selectable alternatives on the same ChatGPT/Codex subscription. The user's `default` profile remains a working `gpt-6-sol-900k` fallback. [OpenAI's model table](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) says Daybreak Blue reduces refusals on GPT-6 Sol/Luna, while Astra and GPT-6.1 Sol retain standard safeguards. The local Daybreak launcher and completed responses do not expose server-side access-program metadata, so the **effective Daybreak state was not independently confirmed**. No profile promises a refusal-free result.

## Local setup verified

| Component | Directly observed | Limit |
|---|---|---|
| Hermes Agent Desktop/CLI | v0.22.5; Desktop backend showed ready, profile picker listed `security`, `astra`, `sol61`; a `security` session answered `DESKTOP_SECURITY_READY` on GPT-6 Sol | A short UI and CLI check is not a security-quality benchmark |
| Model profiles | `security` returned `SECURITY_READY`; `astra` returned `ASTRA_READY`; `sol61` returned `SOL61_READY`; all via the subscription | Model access can change with account/workspace settings |
| Caido Desktop | v0.58.3 signed in; local instance restarted at `127.0.0.1:8081`; UI showed 0 projects | Instance must be started after it stops; no project or target traffic was created |
| Caido MCP | Community server v4.3.0 OAuth-approved; Hermes `mcp test caido` connected and discovered 66 tools; Hermes `security` listed 0 projects through the Codex app-server route | Read-only project listing only; other MCP actions were not exercised |
| Codex ↔ Caido | Fresh Codex CLI invoked `caido_list_projects`, returning 0 projects | Read-only connection test only |
| OBS Studio | v33.0.0; Screen Recording permission enabled; macOS Screen Capture displayed a live Retina display preview; capture audio sources muted | No final recorded clip or export was inspected; OBS output settings observed as Hybrid MOV and 1280×720 output, so [1080p/MKV guidance](docs/recording.md) is still a recommendation |
| Security CLI | Nuclei 3.11.1, Subfinder 2.17.0, Katana 1.8.0, ffuf 2.3.0, dnsx 1.3.1, ProjectDiscovery httpx 1.12.0, Nmap 7.992, Wireshark CLI 4.6.9, Z3 5.3.1 | No third-party host scanned; Wireshark desktop app was not installed |
| Local code/CTF tools | Semgrep CE 1.182.0, Trivy 0.76.1, Gitleaks 8.30.1, Ghidra 12.2, OpenJDK 25.0.2, Python 3.12 venv with pwntools 4.15.0 / Scapy 2.8.0 / Z3 5.3.1.0 | Tool versions are a dated snapshot; Gitleaks was not asked to verify live credentials |
| Skills | `bug-bounty-workflow`, `finding-validation`, `local-code-security`, `ctf-workflow`, `ctf-writeup`, and `ywh-reporting` appeared enabled in the Hermes profiles; portable skills also installed in Codex | Skills guide behavior; they do not establish a finding or grant testing scope |

## Functional checks on local fixtures

- **Code review:** Semgrep found the single planted `eval(...)` pattern in a local Python fixture. Its first invocation inside Hermes hit a macOS sandbox certificate-store error; `scripts/semgrep-offline` set local certificate/cache paths and disabled registry/metrics traffic. Hermes `sol61` then ran that wrapper successfully and reported 1 finding. This proves scanner execution on the fixture, not exploitability in an application.
- **Infrastructure review:** Trivy `config` found one HIGH misconfiguration in a local Terraform fixture with SSH open to `0.0.0.0/0`. This was an intentionally unsafe test file, not a deployed resource.
- **Reverse engineering:** Ghidra's headless analyzer imported and completed analysis of a locally compiled toy Mach-O binary; exit code 0.
- **CTF:** Hermes `astra` recovered `flag{local_xor_checked}` and the XOR key `0x5a` from a toy local ciphertext, then re-encoded it to an exact match.
- **CTF writing:** Hermes `astra` used the `ctf-writeup` skill to draft an original account of the local fixture. The [writing guide](docs/ctf-writing.md) records the style reference and evidence boundary.
- **Reporting:** Hermes `security`, using `ywh-reporting`, marked a fictional “critical IDOR affecting all users” draft **DO NOT SUBMIT** when the only supplied note was an HTTP 200 with no ownership proof, response body, baseline, or scope. It distinguished the researcher-reported status from a validated boundary failure.
- **Hermes subagents:** Native `default` routed read-only tasks through official profile delegation to SCOUT (`gpt-6.1-sol`), BUGGY (`gpt-6-sol`), and PROOF (`gpt-6-astra`). SCOUT returned the local 19,191-link count; BUGGY identified the source-checked historical Chrome $250,000 award; PROOF rejected a toy IDOR claim based only on HTTP 200/403. A direct `security` app-server test showed that `delegate_task` is unavailable there, so orchestration stays on native `default`.
- **Runtime:** The Codex app-server session log showed `workspace-write` scoped to the private lab, network disabled, and the requested profile model/effort. A prior read-only sandbox blocked Semgrep temporary files; the profile-local launchers corrected that without changing global Codex permissions.

## Public material organized

- `catalog/resources.csv`: 58 curated source links grouped by disclosures, advisories, original research, CTF writeups, practice labs, and standards. `catalog/index.md` is generated from it.
- `HACKSPACE/data/pentesterland-writeups.csv`: 6,526 distinct links from [Pentester Land's JSON export](https://pentester.land/writeups.json), stored locally and excluded from Git.
- `HACKSPACE/data/hackerone-disclosed-index.csv`: 12,673 distinct report URLs from a [community catalog](https://github.com/ajaysenr/HackerOne-Disclosed-Reports), stored locally and excluded from Git. This is third-party metadata; verify at the original report.
- `HACKSPACE/data/library.sqlite`: 19,191 distinct URLs after local deduplication, searchable with `scripts/library.py`. Eight URLs overlap between the two CSV inputs; the current importer attributes those rows to the HackerOne community index.
- [`HACKSPACE/`](HACKSPACE/README.md): seven original-page-verified high-payout examples, current PHP2Shell, AI security, Gray Swan, TeamH4C, Wiz/XBOW/Hacktron, and root-cause notes, plus private diary and lead-card templates. The [audited local corpus](HACKSPACE/CORPUS-SNAPSHOT.md) contains 5.05 GB of canonical advisory data, separate from first-person bounty reports and overlapping by identifier.
- `research/hackinghub/`: 115 source-labeled tips and tool, website, post, outbound-link, and media-coverage tables from the referenced research task. The 315 feed entries and 90 separately indexed post pages overlap; many videos were not fully inspected.

These counts are snapshots of public indexes, not a worldwide total. Reports may be private, removed, duplicated, or licensed against mirroring. The repository links to original publishers and includes no third-party report bodies.

## Workflow and current limits

Use a private [engagement card](templates/engagement-card.md) to record current rules, scope, accounts, rates, and stop conditions. In Caido, preserve one authorized baseline, change one variable, use a negative control where possible, and stop at the minimum sufficient proof. Capture a redacted HTTP pair and a [private evidence ledger](templates/evidence-ledger.md). Report observed impact with [the report template](templates/bug-report.md) and the user's `ywh-reporting` skill; do not invent severity or downstream effects. See [workflow](docs/workflow.md) and [profile routing](docs/hermes-profile.md).

The functional checks above used local fixtures and read-only integration. The Codex workspace sandbox used for those Hermes checks had shell network access disabled; Caido MCP connectivity was verified separately. Live recon or request sending requires the specific program's authorization and rate rules, plus an appropriate network route. The catalog is deliberately link-based and cannot be exhaustive.
