# Practical and Sovereign AI for Earth Observation
### A hands-on agentic coding workshop — AEO26

📍 **Monday 9 November 2026 · 9:00 am – 12:30 pm · [Advancing Earth Observation Forum 2026](https://www.earthobsforum.org/), Nipaluna/Hobart, Lutruwita/Tasmania**

> **This is a holding page.** Full coursework, notebooks and hands-on exercises will be published here before the conference. Star or watch this repo to be notified when they land. For the official conference program and workshop tickets, see the [AEO26 website](https://www.earthobsforum.org/) and [registration page](https://www.earthobsforum.org/registration) — workshop details there are *coming soon* and this page will be kept in sync.

---

## What this workshop is about

A practical, hands-on introduction to agentic AI for remote sensing, GIS and Earth observation, taught entirely with **Australian environmental case studies and open data**. You will leave having actually driven an AI agent, not just watched one.

We cover three levels of working with AI, all inside safe sandboxes:

| Level | What it means | What you'll do |
|---|---|---|
| 🏄 **Vibe coding** | Describing outcomes in plain language and letting the model write, run and fix the code | Build a working geospatial analysis from a prompt — no coding experience required |
| 🛠️ **Agentic tool use** | Giving the model tools (search, code execution, files, APIs) and letting it decide when to use them | Chain tools together to pull open satellite and environmental data and turn it into maps and answers |
| 🤖 **Autonomous agents** | Setting a goal, walking away, and verifying what the agent did — safely, inside a sandbox | Run a browser-based autonomous agent on a real remote-sensing task, then audit its work |

Case studies draw on open Australian data — [Digital Earth Australia](https://www.dea.ga.gov.au/), [Copernicus/Sentinel](https://dataspace.copernicus.eu/), [Geoscience Australia](https://www.ga.gov.au/), [TERN](https://www.tern.org.au/) and the [Atlas of Living Australia](https://www.ala.org.au/) — in an Australian environmental context: vegetation, biodiversity, land cover and disaster resilience.

**Presenters:** Adam Roff (Senior Research Scientist, Vegetation & Biodiversity Mapping, DCCEEW NSW) and Fang Yuan (Earth Observation Australia), with guest speakers to be announced. The session also includes a segment on running **open-weights models on local hardware** — sovereign AI you can hold in your hand.

*Program details are draft and subject to change until the official AEO26 program is published.*

---

## ✅ Before you arrive — the only two prerequisites

**All you need is a Claude account (free is fine) and either a laptop with a browser or the Claude mobile app.** No installs, no Python environment, no GPU. Please sign up *before* the day so we can spend the time doing, not registering.

### 1. Create a Claude account

1. Go to **[claude.ai](https://claude.ai)**
2. Sign up with your email address (you'll receive a verification link), or use Google/Apple sign-in
3. That's it — no credit card required, and the free tier does not expire

**Free vs paid — which do you need?**

| Plan | Cost | Enough for this workshop? |
|---|---|---|
| **Free** | $0 | **Yes.** Chat, web search, file creation, code execution and artifacts on web and mobile — everything the hands-on exercises use. Free accounts have daily usage limits, which are workable for a workshop. |
| **Pro** | US$20/mo (US$17/mo annual) | Optional. Adds much higher usage limits plus **Claude Code** — the terminal/cloud agentic coding tool. Choose this if you want to keep going after the workshop or follow the advanced training below. |
| **Max** | from US$100/mo | For heavy daily users; not needed here. |

Full details: [claude.com/pricing](https://claude.com/pricing)

### 2. Bring a browser or install the mobile app

Any modern browser on a laptop works — just log in at [claude.ai](https://claude.ai). Or install the official mobile app:

- 🍎 **iOS / iPadOS:** [Claude by Anthropic on the App Store](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684)
- 🤖 **Android:** [Claude on Google Play](https://play.google.com/store/apps/details?id=com.anthropic.claude)

All app downloads for every platform: [claude.com/download](https://claude.com/download)

### ⚠️ A word on the Claude Desktop app

**We recommend you do *not* use the Claude Desktop app for this workshop** — use the browser or mobile app instead.

The desktop app is powerful precisely because it can work directly on your machine: it reads and modifies local files, and its agentic modes (Cowork, Claude Code, computer use) act with the same permissions as your own user account. That's wonderful on a dedicated machine, and risky on the laptop that holds your email, credentials and department documents — especially while you're learning what autonomous agents do.

Use the desktop app only if:
- it's a **dedicated or disposable machine**, or
- you have **experience sandboxing autonomous agents** (containers, VMs, permission modes — see Anthropic's guide to [choosing a sandbox environment](https://code.claude.com/docs/en/sandbox-environments)).

Everything in this workshop runs in the browser or mobile app, where the agent operates inside Anthropic's sandbox — not on your machine. That boundary is, in fact, one of the things we'll be teaching.

---

## 📚 Pre-workshop learning (optional, free)

Anthropic offers free, self-paced courses through the **[Anthropic Academy](https://www.anthropic.com/learn)** — most include a certificate of completion. None are required for the workshop, but they're an excellent warm-up. Pick your track:

### 🌱 Absolute beginners (free Claude account is enough)

| Course | Time | What it covers |
|---|---|---|
| [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | ~3–4 h | **Start here.** The 4D framework — Delegation, Description, Discernment, Diligence — for working with AI effectively, efficiently and safely. No coding required. Also [free on Coursera](https://www.coursera.org/learn/ai-fluency-framework-foundations). |
| [AI Capabilities and Limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations) | 11 short modules | Builds an honest mental model of what language models can and can't do, and *why* — the best inoculation against both hype and fear. |
| [Claude 101](https://anthropic.skilljar.com/claude-101) | 14 lessons | A practical tour of Claude itself: first conversations, Projects, Artifacts, file handling and research tools. Ideal the week before the workshop. |
| [Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) (ch. 1–3) | ~1–2 h | Hands-on exercises in writing clear, structured prompts — the skill that underpins vibe coding. |

### 🚀 More advanced users (developers, or anyone with a Pro plan)

| Course | Time | What it covers |
|---|---|---|
| [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | 8 modules | Introduction to agentic coding with Claude Code: the agent loop and the Explore → Plan → Code → Commit workflow. *(Requires a Pro plan or API key.)* |
| [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | 14 modules | **Closest to this workshop's heart:** long unsupervised agent runs, permission modes, hooks, and verifying work you didn't watch happen. |
| [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 11 sections | The flagship developer course — API fundamentals, tool use, retrieval, and agents vs. workflows. Python assumed. |
| [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | 4 sections | Build MCP servers that give agents new tools — how you'd wire an agent to your own geospatial data services. ([Advanced topics course](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) follows on.) |
| [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) · [Introduction to Subagents](https://anthropic.skilljar.com/introduction-to-subagents) | 4–6 modules each | Packaging expertise so agents apply it automatically, and delegating work across multiple agents. |
| [anthropics/courses](https://github.com/anthropics/courses) | self-paced | Jupyter-notebook deep dives: API fundamentals, real-world prompting, prompt evaluations and tool use. |

**On agent safety and sandboxing** (the theme running through the whole workshop): Anthropic's docs on [choosing a sandbox environment](https://code.claude.com/docs/en/sandbox-environments) and [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) explain the isolation model we'll be demonstrating.

---

## 🗂️ Coursework

Workshop notebooks, exercises and case-study materials will appear in [`coursework/`](coursework/) before the conference. Watch this space.

---

## 🎟️ Attending

- **Conference:** [AEO26 — Advancing Earth Observation Forum](https://www.earthobsforum.org/), 9–12 November 2026, Nipaluna/Hobart
- **Registration:** [ti.to/earth-observation-australia/aeo-forum-2026](https://ti.to/earth-observation-australia/aeo-forum-2026) — note that **workshop tickets are purchased separately**, and conference registration is *not* required to attend a workshop
- **Questions about this workshop:** open an [issue on this repo](../../issues)

---

*We acknowledge the First Nations peoples of Australia as the original observers of our Earth, and the Muwinina people, traditional owners of the land on which AEO26 gathers in Nipaluna/Hobart.*
