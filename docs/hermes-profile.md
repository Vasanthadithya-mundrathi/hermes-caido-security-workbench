# Hermes security profiles

Four profiles keep model choice explicit while sharing a private, scoped research workspace. Hermes Desktop's profile picker and `hermes -p <name>` select the same profiles. The `security` profile is the active desktop default; `default` remains the user's working `gpt-6-sol-900k` fallback. OAuth credentials stay in Hermes/Codex local auth stores, never in this repository.

| Profile | Model and runtime | Use | Safeguards under Daybreak Blue |
|---|---|---|---|
| `security` | `gpt-6-sol`, Codex app-server through `scripts/codex-daybreak` | Authorized bug bounty and CTF work needing Daybreak Blue's supported reduced-refusal route | Requests `daybreak=true`; eligibility depends on the account/workspace |
| `astra` | `gpt-6-astra`, Codex app-server through `scripts/codex-workspace` | Demanding analysis of supplied code, artifacts, and complex challenges | Standard safeguards |
| `sol61` | `gpt-6.1-sol`, Codex app-server through `scripts/codex-workspace` | Fast daily investigation and local code review | Standard safeguards |
| `default` | User's `gpt-6-sol-900k`, Hermes-native Codex Responses loop | Large-context fallback and Hermes-native in-loop tools | Standard safeguards in this configuration |

As checked on **2026-10-26**, [OpenAI's Daybreak overview](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) lists reduced refusals for GPT-6 Sol/Luna under approved Daybreak Blue, while Astra and GPT-6.1 Sol keep standard safeguards under Blue. [OpenAI's Codex CLI guide](https://help.openai.com/en/articles/20001607-using-daybreak-in-codex-cli) requires CLI 0.163.0 or newer and uses `daybreak=true` for headless requests. The old `gpt-daybreak-blue-latest` alias is [deprecated](https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest). The installed CLI is 0.164.0. A local response proves the route works; it does **not** prove the server applied Daybreak to that response. No prompt or profile can guarantee a refusal-free answer or override platform safeguards. State the authorized context and exact challenge clearly, then use the supported Sol profile when reduced refusals are important.

## Workspace and instructions

Each profile has its own settings, SOUL, skills, and sessions. `config/HERMES-SOUL.md` is installed as the profile's SOUL. A private work directory holds `templates/HERMES-AGENTS.md`, current scope notes, fixtures, proxy evidence, and challenge files. The `terminal.cwd` of the three security profiles points to that directory. `scripts/codex-daybreak` and `scripts/codex-workspace` set Codex's `:workspace` permission **for those Hermes runs only**, so tools can write inside the private lab without changing the global Codex configuration. Network access in the tested Codex sandbox was off; live target work still requires program authorization and an appropriate network route.

The Codex app-server runtime supplies Codex's shell, patch, sandbox, and configured MCP servers, including Caido. The three profiles have the original and local workbench skills, plus the user's `ywh-reporting` skill installed locally. The GPL-licensed `ywh-reporting` files are not copied into this MIT-licensed repository. The Hermes-native `delegate_task`, manual `memory`, `session_search`, and `todo` tools are unavailable in the app-server loop; use `default` when those matter. See [Hermes' runtime documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime) and [profiles guide](https://hermes-agent.nousresearch.com/docs/user-guide/profiles).

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

for profile in security astra sol61; do
  cp config/HERMES-SOUL.md "$HOME/.hermes/profiles/$profile/SOUL.md"
done
cp config/HERMES-SOUL.md "$HOME/.hermes/SOUL.md"

hermes profile use security
```

Set `terminal.cwd` on all three profiles to your private workspace. Install each portable `skills/` directory into each profile's `skills/security/` tree and into `~/.codex/skills/` (see [macOS setup](setup-macos.md)). Set reasoning effort per task; the local snapshot used XHigh for `security` and High for `astra` and `sol61`. Keep low-cost triage short and raise effort only for genuinely hard analysis.

## Verify each layer

```sh
hermes profile list
hermes -p security auth status openai-codex
hermes -p security mcp test caido
hermes -p security -z 'Reply exactly SECURITY_READY.'
hermes -p astra -z 'Reply exactly ASTRA_READY.'
hermes -p sol61 -z 'Reply exactly SOL61_READY.'
hermes -p default -z 'Reply exactly DEFAULT_READY.'
```

Start the **local Caido instance** before a Caido MCP call. If it is stopped, `mcp test` or the agent may return an error even though OAuth and configuration are intact. After starting it, a read-only `caido_list_projects` through `security` returned `0 projects` in this setup. These checks demonstrate connectivity and local tool use; they do not validate a live finding or every MCP action.
