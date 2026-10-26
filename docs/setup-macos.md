# macOS desktop setup

This setup was exercised on Apple Silicon macOS on 2026-10-26. Use the current vendor documentation when installing on another OS or after a major release. The installed Hermes profiles use a ChatGPT/Codex subscription; see [profile setup and model limits](hermes-profile.md).

## 1. Install the desktop tools

1. Install [Hermes Agent Desktop](https://hermes-agent.nousresearch.com/docs/getting-started/installation) from its official site or inspected official installer. The CLI and desktop share `~/.hermes/config.yaml`, sessions, skills, and model credentials. Verify with `hermes --version` and `hermes doctor`.
2. Install [Caido Desktop](https://docs.caido.io/app/quickstart/setup). On macOS, `brew install --cask caido` is an option. Start a **local** instance; use `127.0.0.1:8080` if free, or another loopback port such as `8081` if another app owns 8080. Sign in to that instance in Caido.
3. Install [OBS Studio](https://obsproject.com/kb/mac-installation) if you need repeatable evidence videos. macOS's built-in `Shift-Command-5` recorder is enough for simple captures.
4. Sign in to the `openai-codex` provider with the ChatGPT/Codex account you intend to use. Verify `hermes auth status openai-codex`, then create and test the `security`, `astra`, and `sol61` profiles in [Hermes profile setup](hermes-profile.md). Select `security` in Hermes Desktop for the Daybreak Blue route; the existing `default` profile remains the `gpt-6-sol-900k` fallback on this machine.

The focused free tool additions are [Semgrep Community Edition](https://semgrep.dev/products/community-edition/) for source patterns, [Trivy](https://github.com/aquasecurity/trivy) for local configuration/dependency review, [Gitleaks](https://github.com/gitleaks/gitleaks) for redacted secret candidates, and [Ghidra](https://github.com/NationalSecurityAgency/ghidra) for supplied binaries. They complement Caido's HTTP workflow. On macOS Homebrew:

```sh
brew install semgrep trivy gitleaks ghidra
semgrep --version
trivy --version
gitleaks version
command -v ghidraRun
```

For Codex's macOS workspace sandbox, install `scripts/semgrep-offline` as described in [profile setup](hermes-profile.md). It runs local rules without registry/metrics traffic and uses sandbox-compatible temporary paths. Review current upstream releases and tool-specific licenses before upgrading.

For CTF scripting, the workbench also uses a separate Python 3.12 environment with [pwntools](https://github.com/Gallopsled/pwntools), [Scapy](https://scapy.net/), and [Z3](https://github.com/Z3Prover/z3):

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements-ctf.txt
.venv/bin/python -c 'import pwn, scapy, z3; print("CTF helpers ready")'
```

Use a Linux VM/container for Linux binary exploitation and untrusted challenge programs; a macOS venv alone does not reproduce their execution environment.

## 2. Install and authenticate the Caido MCP server

Caido's [MCP tutorial](https://docs.caido.io/app/tutorials/mcp) describes the community server. Get a reviewed release from [`c0tton-fluff/caido-mcp-server`](https://github.com/c0tton-fluff/caido-mcp-server/releases), verify its published checksum/digest, and put the executable on your `PATH`. The installed snapshot for this workbench is v4.3.0. A newer release should be reviewed before replacing it.

With your local Caido instance running:

```sh
caido-mcp-server login -u http://127.0.0.1:8081
```

Approve the device authorization in your own browser/Caido UI. The server stores its OAuth token in your user profile. Do not paste it into a repository, chat, or skill file. Caido warns that its proxy traffic itself is unprotected; keep the instance bound to loopback unless you have an explicitly secured remote design.

## 3. Connect Hermes and Codex

Use the path and port actually installed on your machine. Configure every Hermes profile you plan to use; this matters for the Hermes-native fallback and lets `mcp test` inspect each profile. For example, on this workbench:

```sh
for profile in default security astra sol61; do
  hermes -p "$profile" config set mcp_servers.caido.command /absolute/path/to/caido-mcp-server
  hermes -p "$profile" config set mcp_servers.caido.args '["serve"]'
  hermes -p "$profile" config set mcp_servers.caido.env.CAIDO_URL http://127.0.0.1:8081
done
hermes -p security mcp test caido
```

For Codex:

```sh
codex mcp add caido --env CAIDO_URL=http://127.0.0.1:8081 -- /absolute/path/to/caido-mcp-server serve
codex mcp get caido
```

Restart Hermes Desktop or reconnect its gateway after changing MCP configuration. Open a **new Codex chat** after adding a server, because an existing chat may not acquire new tools mid-session. Validate with a read-only call such as listing Caido projects after OAuth is complete. A configuration entry alone does not prove authentication. Caido Desktop can remain open while its local instance is stopped; click **Start** on the instance before testing again.

## 4. Install the portable skills

Copy each directory under `skills/` into `~/.hermes/skills/security/<skill-name>/`, `~/.hermes/profiles/<profile>/skills/security/<skill-name>/` for each profile, and `~/.codex/skills/<skill-name>/`; use the frontmatter name `evidence-based-reporting` for the `skills/reporting/` directory. Hermes uses category directories; Codex uses skill directories at the root. Keep the repository outside those destinations so updates can be reviewed as Git changes. Hermes's [skill documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) explains discovery and enabling; Codex reads its own skills directory at chat start. Verify with `hermes -p security skills list --source local` and a fresh Codex chat. The user's separate GPL-licensed `ywh-reporting` skill was installed locally in all four Hermes profiles but is not redistributed in this repository.

For a convenient Hermes shortcut, create a bundle with `caido-research`, `source-research`, `evidence-capture`, and `evidence-based-reporting`, and another with `ctf-workflow`, `source-research`, and `evidence-capture`. The installed workbench uses `/bug-bounty-research` and `/ctf-practice` as the bundle commands.

The Caido research skill in this repository uses MCP and the agent's existing auth. Caido's own [Claude-focused skill](https://docs.caido.io/app/tutorials/skills) uses a different CLI/secret store and is not required for this setup.

## 5. Configure a scoped browser session

- Create a separate Caido project per authorized program or CTF.
- Read the program's current policy before configuring browser traffic or scans. Keep an allowlist and rate budget in your private project notes.
- Proxy only the browser profile used for that project. Install Caido's certificate only for that profile if HTTPS interception is needed; never export it or credentials to this repository.
- Keep credentials for different roles separate and labeled in private notes. Clear or switch the proxy before browsing unrelated personal sites.

## Verify

```sh
hermes --version
hermes doctor
hermes profile list
hermes -p security mcp list
hermes -p security mcp test caido
codex mcp get caido
caido-mcp-server --version
```

Expected result: Hermes Desktop launches, the configured model answers a short test prompt, Caido's local instance is logged in, `hermes mcp test caido` discovers tools, and a **fresh** Codex chat can see Caido tools. Treat each check separately so a partial setup is obvious.
