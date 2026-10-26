# Hermes security profiles

Seven profiles keep model choice and agent roles explicit while sharing a private, scoped research workspace. Hermes Desktop's profile picker and `hermes -p <name>` select the same profiles. The `security` profile is the active desktop profile for direct Daybreak work; `default` retains the user's working `gpt-6-sol-900k` fallback and is the **delegating orchestrator**. OAuth credentials stay in Hermes/Codex local auth stores, never in this repository.

| Profile | Model and runtime | Use | Safeguards under Daybreak Blue |
|---|---|---|---|
| `security` | `gpt-6-sol`, Codex app-server through `scripts/codex-daybreak` | Authorized bug bounty and CTF work needing Daybreak Blue's supported reduced-refusal route | Requests `daybreak=true`; eligibility depends on the account/workspace |
| `astra` | `gpt-6-astra`, Codex app-server through `scripts/codex-workspace` | Demanding analysis of supplied code, artifacts, and complex challenges | Standard safeguards |
| `sol61` | `gpt-6.1-sol`, Codex app-server through `scripts/codex-workspace` | Fast daily investigation and local code review | Standard safeguards |
| `default` | User's `gpt-6-sol-900k`, Hermes-native Codex Responses loop | Large-context fallback and Hermes-native in-loop tools | Standard safeguards in this configuration |
| `buggy` | `gpt-6-sol`, Codex app-server through `scripts/codex-daybreak` | BUGGY, scoped high-value bug bounty lead research, direct or delegated | Requests `daybreak=true`; account eligibility still controls the result |
| `proof` | `gpt-6-astra`, Codex app-server through `scripts/codex-workspace` | PROOF, independent candidate validation and alternative explanations | Standard safeguards |
| `scout` | `gpt-6.1-sol`, Codex app-server through `scripts/codex-workspace` | SCOUT, primary-source policy, advisory, payout and duplicate research | Standard safeguards |

As checked on **2026-10-26**, [OpenAI's Daybreak overview](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) lists reduced refusals for GPT-6 Sol/Luna under approved Daybreak Blue, while Astra and GPT-6.1 Sol keep standard safeguards under Blue. [OpenAI's Codex CLI guide](https://help.openai.com/en/articles/20001607-using-daybreak-in-codex-cli) requires CLI 0.163.0 or newer and uses `daybreak=true` for headless requests. The old `gpt-daybreak-blue-latest` alias is [deprecated](https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest). The installed CLI is 0.164.0. A local response proves the route works; it does **not** prove the server applied Daybreak to that response. No prompt or profile can guarantee a refusal-free answer or override platform safeguards. State the authorized context and exact challenge clearly, then use the supported Sol profile when reduced refusals are important.

When an authorized security or CTF request is blocked on `astra`, `sol61`, `proof`, or `scout`, the Hermes instructions call for one retry via Daybreak-enabled **GPT-6 Sol**: the `buggy` route from native `default`, or a direct `security` chat. Keep the same scope and facts. Never turn on `daybreak=true` for Astra or GPT-6.1 Sol; those profiles deliberately use `scripts/codex-workspace`. If the retry is blocked, record what happened and proceed with the allowed research or evidence review.

## Workspace and instructions

Each profile has its own settings, SOUL, skills, and sessions. `config/HERMES-SOUL.md` supplies the common Hermes identity; `config/BUGGY-SOUL.md`, `PROOF-SOUL.md`, and `SCOUT-SOUL.md` supply concise role identities. A private work directory holds `templates/HERMES-AGENTS.md`, current scope notes, fixtures, proxy evidence, and challenge files. The app-server profiles' `terminal.cwd` points to that directory. `scripts/codex-daybreak` and `scripts/codex-workspace` set Codex's `:workspace` permission **for those Hermes runs only**, so tools can write inside the private lab without changing the global Codex configuration. Network access in the tested Codex sandbox was off; live target work still requires program authorization and an appropriate network route.

The updated SOULs make `default` own the shared request budget and artifact ledger, BUGGY prioritize falsifiable high-value leads, SCOUT compare original root causes and fixes, and PROOF issue an independent evidence-cited verdict. [HACKSPACE's workflow](../HACKSPACE/WORKFLOW.md) has the local queue, handoff, and candidate-gate commands. Direct `security` chats use the same workspace instructions and skills, while native `default` remains the orchestrator for subagent handoffs.

In this installation, the private lab has the writable `leads.jsonl`; Git-ignored `HACKSPACE/private/leads.jsonl` points to it so the native parent and app-server profiles share the queue. The lab's `AGENTS.md` records the checkout's absolute path because the app-server current directory is outside the repository. A direct `security` tool call ran the queue check there with exit 0.

The Codex app-server runtime supplies Codex's shell, patch, sandbox, and configured MCP servers, including Caido. The profiles have the original and local workbench skills, including `hackspace-research`; the user's `ywh-reporting` skill stays installed locally. The GPL-licensed `ywh-reporting` files are not copied into this MIT-licensed repository. The Hermes-native `delegate_task`, manual `memory`, `session_search`, and `todo` tools are unavailable in the app-server loop. A direct `security` smoke test confirmed that `delegate_task` was absent. Use `default` to delegate; its native runtime has the official [advanced-delegation plugin](https://hermes-agent.nousresearch.com/docs/plugins/advanced-delegation) pinned to `e404b681`, with `buggy`, `proof`, and `scout` as the only allowed profile routes and a three-child concurrency cap. A read-only test routed to SCOUT on `gpt-6.1-sol` and returned the 19,191-link local count. See [Hermes' runtime documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime) and [profiles guide](https://hermes-agent.nousresearch.com/docs/user-guide/profiles).

## Recreate on a signed-in installation

Review the scripts before copying them. Use an absolute private workspace path of your choice and copy `templates/HERMES-AGENTS.md` there as `AGENTS.md`. Back up any SOUL you want to retain before replacing it. The existing `default` provider must be logged in to `openai-codex` with a ChatGPT/Codex subscription.

```sh
install -m 755 scripts/codex-daybreak "$HOME/.local/bin/hermes-codex-daybreak"
install -m 755 scripts/codex-workspace "$HOME/.local/bin/hermes-codex-workspace"
install -m 755 scripts/semgrep-offline "$HOME/.local/bin/semgrep-offline"

hermes profile create security --clone-from default
hermes -p security config set model.default gpt-6-sol
hermes -p security config set model.openai_runtime codex_app_server
hermes -p security config set model.codex_bin "$HOME/.local/bin/hermes-codex-daybreak"

hermes profile create astra --clone-from security
hermes -p astra config set model.default gpt-6-astra
hermes -p astra config set model.codex_bin "$HOME/.local/bin/hermes-codex-workspace"

hermes profile create sol61 --clone-from security
hermes -p sol61 config set model.default gpt-6.1-sol
hermes -p sol61 config set model.codex_bin "$HOME/.local/bin/hermes-codex-workspace"

hermes profile create buggy --clone-from security
hermes profile create proof --clone-from astra
hermes profile create scout --clone-from sol61

for profile in security astra sol61; do
  cp config/HERMES-SOUL.md "$HOME/.hermes/profiles/$profile/SOUL.md"
done
cp config/HERMES-SOUL.md "$HOME/.hermes/SOUL.md"
for profile in buggy proof scout; do
  cp "config/$(printf '%s' "$profile" | tr '[:lower:]' '[:upper:]')-SOUL.md" "$HOME/.hermes/profiles/$profile/SOUL.md"
done

hermes -p default plugins install advanced-delegation
hermes -p default plugins enable advanced-delegation
hermes -p default delegation config

hermes profile use security
```

Set `terminal.cwd` on all six app-server security profiles to your private workspace. In the interactive delegation configuration, choose **Profile routes**, allow only `buggy`, `proof`, and `scout`, leave the default route unset so unrouted tasks stay with the parent, and limit concurrency to three. Install each portable `skills/` directory into each profile's `skills/security/` tree and into `~/.codex/skills/` (see [macOS setup](setup-macos.md)). Set reasoning effort per task; the local snapshot used XHigh for `security` and High for `astra` and `sol61`. Keep low-cost triage short and raise effort only for genuinely hard analysis.

## Verify each layer

```sh
hermes profile list
hermes -p security auth status openai-codex
hermes -p security mcp test caido
hermes -p security -z 'Reply exactly SECURITY_READY.'
hermes -p astra -z 'Reply exactly ASTRA_READY.'
hermes -p sol61 -z 'Reply exactly SOL61_READY.'
hermes -p default -z 'Reply exactly DEFAULT_READY.'
hermes -p default delegation config --show
python3 HACKSPACE/scripts/eval_findings.py run --profile proof --limit 2
```

Start the **local Caido instance** before a Caido MCP call. If it is stopped, `mcp test` or the agent may return an error even though OAuth and configuration are intact. After starting it, a read-only `caido_list_projects` through `security` returned `0 projects` in this setup. These checks demonstrate connectivity and local tool use; they do not validate a live finding or every MCP action.
