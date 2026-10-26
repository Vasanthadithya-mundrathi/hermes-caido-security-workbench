# Gray Swan AI: agent-break research to use in controlled evaluations

Reviewed 2026-10-26. Gray Swan AI's [research hub](https://www.grayswan.ai/research) collects adversarial AI work, including GCG, representation engineering and circuit breakers, HarmBench, AgentHarm, CyBench, and agent red teaming. These publications cover different threat models. A model producing prohibited text, an agent taking an unauthorized action, and a sandbox escape are different results; no single “godmode” label proves all three.

## Indirect prompt injection with hidden side effects

[Gray Swan's IPI Arena report](https://www.grayswan.ai/blog/your-ai-agent-can-be-compromised-youd-never-know) describes a public red-team competition against agents working with email, shopping, smart-home, coding, and computer-use tools. In this setting, the attacker controls lower-trust content the agent reads. The study scored a win only when the agent both **performed an attacker-desired unauthorized action** and **hid that action from the user**. This dual condition is more stringent than measuring whether the agent repeated the attacker's words.

Gray Swan reports 464 participants, more than 272,000 attempts, and 8,648 successful attacks across 13 model-backed agents. Those are the organizer's dataset counts, not evidence that every deployed agent is vulnerable at that rate. [NIST's account of the competition](https://www.nist.gov/blogs/caissi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition) supplies an independent institutional description of the collaboration and evaluation setting. The [open IPI Arena kit](https://github.com/GraySwanAI/ipi_arena_os) is MIT licensed and useful for **owned or expressly authorized** test agents. Its documented benchmark runs require an OpenRouter API key for both target model and judge, which is separate from ChatGPT/Codex subscriptions and may cost money; use its source and dry-run mode without claiming a free live run.

The practical insight is to inspect two traces independently:

1. **Actual action:** tool calls, external effects, changed files/data, and policy boundary crossed.
2. **User-visible account:** what the agent said it did, omitted, or misrepresented.

A hidden action can make ordinary output-only monitoring look reassuring. Conversely, a suspicious answer with no wrong action is a different, usually weaker result. Preserve both traces and a baseline run using the same legitimate task without the injected content.

## Technique families to study

| Family | Research question for an owned lab | What would count as evidence |
| --- | --- | --- |
| Lower-trust instruction laundering | Can a web page, email, repository file, document, or tool response make the agent treat source content as a higher-priority command? | The controlled content, retrieval/tool trace, the unauthorized action, and a control run. |
| Tool-output and MCP boundary confusion | Does an agent obey a server-supplied instruction that exceeds the tool's role or the user's authorization? | Exact tool output, tool identity/trust, subsequent tool call or data flow, and a negative control. |
| Hidden-action manipulation | Can attacker-controlled content induce an unauthorized action and prevent the agent from reporting it to the user? | Action log **and** user-facing response, scored separately. This is the IPI Arena's central distinction. |
| Multimodal instruction placement | Can text/visual cues inside an image or rendered content change the agent's behavior during a legitimate visual task? | Original media, model-visible rendering, downstream action, and a comparable benign image. See [Gray Swan's Visual Vulnerabilities Challenge](https://www.grayswan.ai/blog/gray-swan-announces-the-visual-vulnerabilities-challenge). |
| Automated prompt search | Do reusable adversarial suffix or optimization methods transfer to the *specified* model and task? | Trial budget, model/version, exact scoring rule, held-out results. A [GCG paper](https://arxiv.org/abs/2307.15043) result is not proof of a specific deployed product break. |
| Agent benchmark regression | Did a change fix one action path while leaving equivalent routes through other tools or formats? | Repeatable test cases, per-path outcomes, and preserved regression results. [AgentHarm](https://arxiv.org/abs/2410.09024) and [CyBench](https://arxiv.org/abs/2408.08926) are research benchmarks, not live-target authorization. |

## Workbench procedure

1. Set the legitimate user task, agent/tool identities, data classification, and exact boundary under test.
2. Place controlled content only in an owned or authorized lower-trust source. Save its exact bytes and model-visible rendering.
3. Run a baseline and the changed condition with comparable state. Record model/version, tools, permissions, timestamps, and trial budget.
4. Score **instruction following**, **unauthorized tool/state effect**, **data movement**, and **concealment** separately. Repeat enough to distinguish a reliable behavior from a one-off result.
5. Have PROOF try a benign alternative explanation and identify which control blocks the chain. Keep any out-of-scope or unrun escalation as a hypothesis.
6. For a bounty program, check AI-specific eligibility and impact language before drafting; [OpenAI's Safety Bug Bounty](https://openai.com/index/safety-bug-bounty/) and [Microsoft's Copilot Bounty](https://www.microsoft.com/en-us/msrc/bounty-ai) illustrate why a generic jailbreak or a harmless prompt leak may not qualify.

Gray Swan's [Proving Ground](https://www.grayswan.ai/news/introducing-the-gray-swan-ai-proving-ground) is an organized challenge environment for authorized practice. Gray Swan's Shade/Cygnal product descriptions are commercial claims; this workbench links the public research and free evaluation kit without claiming those products are installed.
