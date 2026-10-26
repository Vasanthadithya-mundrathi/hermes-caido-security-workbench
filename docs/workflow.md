# Authorized research workflow

Use a program's published rules as the source of truth. For a CTF, use the event's challenge rules and isolated artifacts. The [OWASP Web Security Testing Guide](https://wstg.owasp.org/) supplies a broad technical reference; [PortSwigger Web Security Academy](https://portswigger.net/web-security) supplies reproducible labs. The HackingHub notes in this repository are source-labeled ideas rather than a testing authorization.

## 1. Define the engagement

Record the program or CTF name, policy URL, date reviewed, allowed hosts/apps, excluded paths/classes, test accounts, automation and rate limits, disclosure rules, and stop conditions. If an asset is ambiguous, ask the program before sending active traffic. Historical reports and similarly named domains do not establish scope.

Use a private copy of the [engagement card](../templates/engagement-card.md) so the policy, roles, request budget, and hypothesis queue stay together. Re-check it when a program changes scope or a new asset is proposed.

## 2. Understand one application

Map roles, objects, tenant boundaries, important workflows, APIs, browser behavior, integrations, and error paths. Read product documentation and public disclosures for background. Use Caido to group only scoped requests and responses; annotate which account/role generated each observation. Use passive discovery first, then prioritize leads instead of collecting maximum volume.

Rank questions by the importance of the boundary if broken, the quality of current evidence, the cost of the smallest decisive check, and program restrictions. Timebox reconnaissance and reevaluate when it stops producing new hypotheses. A well-chosen role/object comparison usually teaches more than a large unreviewed scan. Keep a short queue of disconfirmed ideas to avoid retesting the same assumption.

## 3. Form and test a bounded hypothesis

State the expected control and the precise alternative behavior to check. In an authorized environment, compare a controlled baseline with one changed input or role at a time. Use manual replay when possible. Automation should respect the program's limits and produce reviewable evidence, not just a hit count. Do not use a scanner result as the proof of a vulnerability.

Examples of *questions* to ask: Does an object authorization check cover a second account? Does a workflow preserve the server-side state transition? Does a cache key vary with the relevant identity? Does an API accept an input that the UI hides? Consult [OWASP ASVS](https://asvs.owasp.org/) for expected controls and [PortSwigger Academy](https://portswigger.net/web-security) for lab demonstrations.

If source is legitimately available, trace the request to the server-side decision before scanning broadly. Use `local-code-security` for a targeted Semgrep rule, Trivy configuration check, or Gitleaks review. A match needs reachability and consequence checks; a clean scan only says its chosen rules found nothing.

## 4. Validate the boundary and impact

Keep the smallest demonstration that establishes the security boundary crossing. Stop before unnecessary data access, changes, disruption, or use of third-party accounts. Record role, request/response identifiers, timestamps, expected and actual behavior, and relevant versions when actually known. Separate direct observations from researcher recollection, inference, and unknowns. If a finding is not reproduced, say so.

## 5. Report and preserve evidence

Use [the evidence ledger](../templates/evidence-ledger.md) as you work. Draft with [the report template](../templates/bug-report.md), state a narrow impact, and apply the program's requested format and severity scale. Exclude unsupported account takeover, population-wide, or financial claims. Preserve redacted request/response pairs and a short video only if it materially clarifies the sequence.

## CTF track

1. Read rules, category, downloadable artifact hashes, and flag format.
2. Keep the original artifact immutable; work on a copy in an isolated directory or VM.
3. Build an observation log: inputs, output, environment, hypothesis, test, result.
4. Use category tools deliberately: CyberChef/Python for encodings; Wireshark for packet captures; Ghidra/radare2 for reversing; `gdb`/pwntools for binary labs; Z3 for constraint problems; Caido for web challenges.
5. Record the final solve path in your own words, including false leads only when they explain the solution. Keep event embargoes and flag-sharing rules.

For a first-person article, use [`ctf-writeup`](../skills/ctf-writeup/SKILL.md) and the [writeup template](../templates/ctf-writeup.md). Verify which actions were yours, which were agent-run, and whether the flag was only derived locally or accepted by the service. The [writing guide](ctf-writing.md) explains the requested technical narrative style.

## Tool choice

| Need | Primary tool | Check before trusting output |
|---|---|---|
| HTTP history, replay, API workflow | Caido | Correct project, host, role, timestamp, redaction |
| Passive DNS inventory | Subfinder, dnsx | Current scope and ownership; stale DNS |
| HTTP inventory/crawl | httpx, Katana | Rate limits, redirects, authenticated context |
| Focused content discovery | ffuf | Program permission, wordlist fit, response baseline |
| Template-based checks | Nuclei | Template version, request safety, manual validation |
| Service review | Nmap | Explicit port-scan authorization and rate |
| Static code / binary analysis | Ghidra, radare2, Semgrep/CodeQL when applicable | Artifact provenance and exact version |
| Local source and IaC patterns | Semgrep CE, Trivy | Rule coverage, deployment context, source path, false positives |
| Candidate secrets in authorized code | Gitleaks | Redacted output, fixture versus real material, disclosure rules |
| Recording | macOS recorder, OBS | Tokens, personal data, audio, scope in frame |

Avoid installing every tool merely because it is popular. Maintain a small, reproducible core and add category tools when a scoped task needs them.
