# AEO26 workbook: build with Claude Code

*Practical and Sovereign AI for Earth Observation* · AEO26 Workshop 1 · Nipaluna/Hobart · Monday
9 November 2026

> **Live copy:** if the presenters announce a fix on the day, use the copy in the workshop repo:
> [WORKBOOK.md](https://github.com/RSGISagent/AEO26_AgenticAI_Workshop/blob/main/WORKBOOK.md).

**Today you won't write code.** You tell Claude Code what you want, it writes and runs the code,
and you check the result. Everything happens in **this private repo**, so it all stays yours.

- **Part 1 (09:45–10:15):** the essentials of Claude Code, from the free
  [Claude Academy](https://academy.claude.com) intro courses. One idea at a time, each tried
  straight away on real data.
- **Part 2 (10:15–11:55):** a practical build. You brief Claude to build a small fire-and-glider
  habitat explorer, leave it working over morning tea, then check its work like a supervisor.

**Hands-on times:** 09:35–10:30 and 11:25–12:15, ending with a demo of running open AI models on
your own hardware.

**Jump to a step:** [Start](#start-open-your-session) · [Early task](#early-task-let-claude-surprise-you) · [1](#step-1-meet-the-agent) · [2](#step-2-plan-before-you-build) · [3](#step-3-let-it-build-and-make-it-check-its-own-work) · [4](#step-4-memory-and-context) · [5](#step-5-review-commit-merge) · [6](#step-6-brief-it-then-walk-away) · [7](#step-7-trust-but-verify) · [8](#step-8-make-it-yours) · [After the workshop](#after-the-workshop)

## How this workbook works

- **Grey boxes are prompts.** Copy one, paste it into the Claude Code message box, and send it.
- **Each step says which mode to use.** The mode menu is under the message box:

  | Mode | What Claude can do without asking you |
  |---|---|
  | **Plan** | Read and suggest. It changes nothing |
  | **Accept edits** | Change files. It asks before it runs any command, and you approve each one |
  | **Auto** | Everything, with an automatic safety check on each action. Use it when you walk away |

- **"You should see"** tells you what success looks like. The pictures are example results: yours
  will differ a little, and that's fine. In the room, put up a 🟩 sticky note if you're there, or 🟥
  if you're stuck.
- **"If you code"** lines are optional extras.

---

## Start: open your session

*09:35 · 5 minutes*

**What you'll do:** open your private repo in Claude Code and check that it answers.

**Do this**

1. Open [claude.ai/code](https://claude.ai/code).
2. In the repo list, pick **this repo** (`<your-handle>/aeo26-workshop`, marked private).
3. Leave the environment as **Default**. There's nothing to set up.
4. Set the mode to **Plan**.
5. Send: `Hello! In one sentence, what is this repo for?`

**You should see:** a reply within a minute or two. The first start takes longer while the cloud
computer copies your repo.

**Stuck?** See [If something goes wrong](SETUP.md#if-something-goes-wrong), or put up a 🟥 sticky
note.

**Next →** [Early task: let Claude surprise you](#early-task-let-claude-surprise-you) · [All steps](README.md#your-steps)

## Early task: let Claude surprise you

*09:40 · 3 minutes to start, then it runs by itself*

**What you'll do:** give Claude a short, open request in a second session, and leave it working
while you do Part 1.

**Why it matters:** it shows what one plain sentence can do. Later, in Step 8, you come back to it
with a more critical eye.

**Do this**

1. Go back to [claude.ai/code](https://claude.ai/code) and start a **new session** on this repo. Your
   first session stays as it is.
2. Set the mode to **Auto**. If **Auto** isn't in the menu, choose **Accept edits**, then check on it
   between steps, because it will wait for you to approve each command.
3. Paste this exactly as it is, and send it:

```text
i want to use python to create a remote sensing demonstration with sentinel data from australia. it does not have to be complex but should be effective in demonstrating claude code capabilities. use sub-agents to conserve context window
```

4. Go back to your first session and start Step 1. This one keeps working by itself in the cloud.

*Sub-agents* are helpers that Claude starts for parts of the job. Each one has its own working
memory and reports back a short summary, so the main session's memory (its *context window*) stays
uncluttered. Look out for them in the session as separate blocks of work.

**Good to know**

- **If it asks you a question,** answer briefly, or say "you choose".
- **It may try to download more satellite data.** Some websites are blocked in the workshop's cloud
  computer, so it may use the data in this repo instead. That's fine.
- **If it opens a pull request, don't merge it yet.** Its work stays on its own branch, so it won't
  get in the way of Part 1.

**You should see:** two sessions in your session list, with the new one busy. Everyone's result
will be different, and that's the point.

![Screenshot of a Claude Code session: the request at the top, Claude's first steps below it, and the Context panel on the right](examples/early_task/session_start.png)

*A presenter's test of a similar request, a few minutes in, in a session with no repo and every
website allowed. Before handing work to sub-agents, Claude checks which data sites it can reach,
installs packages and tests a small download. The **Context** panel on the right shows how much of
its working memory is in use. Your screen will differ: the model, the numbers and the environment
name depend on your account.*

**What that test made:** a web page about the January 2025 Los Angeles fires, with a
before-and-after slider, burn-severity maps, and the code and output for each step. To see it, open
[`examples/early_task/la_fires_demo.html`](examples/early_task/la_fires_demo.html) on GitHub, click
**Download raw file**, then open the downloaded file in your browser (about 10 MB).

**Come back to it** at morning tea (have a look from your phone), and in
[Step 8](#step-8-make-it-yours), where you check it properly.

**Learn more:** Claude Code 101,
["Your first prompt"](https://academy.claude.com/courses/claude-code-101/your-first-prompt).

**Next →** [Step 1: Meet the agent](#step-1-meet-the-agent) · [All steps](README.md#your-steps)

---

## Part 1: Claude Code essentials

*09:45–10:15 · five short steps, all in your first session*

### Step 1: Meet the agent

*09:45 · 5 minutes · mode: **Plan***

**What you'll do:** ask Claude to explain the repo, and watch how it works it out.

**Why it matters:** Claude Code is an agent, not a chatbot. It works in a loop: it **gathers
information** (reads files, searches), **acts** (edits files, runs commands) and **checks** (runs
things and looks at the result), until the job is done. Each grey block in the conversation is one
of those actions. It works in a disposable cloud computer that holds a copy of this repo, and your
GitHub password never goes into it.

**Do this**

```text
What's in this repository? Explain each file in data/ in plain English: what it shows, its units,
its dates and its map projection. Then suggest three small things we could build with it in under
an hour. Don't change anything.
```

**You should see**

- Grey blocks you can click open to see exactly which file Claude read, or which command it ran.
- An answer that covers the satellite images' units (reflectance × 10,000, with −999 for "no
  data"), the map projection (EPSG:3577, 10 m pixels), the fire-severity classes, and that the
  glider locations are latitude and longitude.

**If you code:** ask *"Which files did you read, and why those?"* Notice that it read `CLAUDE.md`
without being told.

**Learn more:** Claude Code 101,
["What is Claude Code?"](https://academy.claude.com/courses/claude-code-101/what-is-claude-code) and
["How Claude Code works"](https://academy.claude.com/courses/claude-code-101/how-claude-code-works).

**Next →** [Step 2: Plan before you build](#step-2-plan-before-you-build) · [All steps](README.md#your-steps)

### Step 2: Plan before you build

*09:50 · 5 minutes · mode: **Plan***

**What you'll do:** ask for a plan for your first figure, then change the plan before anything is
built.

**Why it matters:** checking a plan takes a minute; fixing a wrong build takes ten. Say what "done"
looks like, and ask how Claude will check it.

**Do this**

```text
Plan a Python script, before_after.py, that shows the study area in autumn 2019 (before the fire),
2020 (after the fire) and 2025 (five years on) as three false-colour images side by side
(red = SWIR1, green = NIR, blue = red), with the same colour stretch on all three, saved to
outputs/before_after.png. Tell me how you will check that the figure is right. Plan only.
```

Read the plan. Does it name the three image files, divide by 10,000, leave out the −999 "no data"
pixels, use **one** colour stretch for all three years, and say how it will check the figure? Then
change one thing:

```text
One change: also show the greater glider records from 2000-2019 as small white dots on the 2019
panel. The coordinates are latitude/longitude, so reproject them to the rasters' projection.
```

**You should see:** a revised plan that includes the glider dots and the change of coordinates.

**Learn more:** Claude Code 101,
["Your first prompt"](https://academy.claude.com/courses/claude-code-101/your-first-prompt) and
["The explore → plan → code → commit workflow"](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow).

**Next →** [Step 3: Let it build, and make it check its own work](#step-3-let-it-build-and-make-it-check-its-own-work) · [All steps](README.md#your-steps)

### Step 3: Let it build, and make it check its own work

*09:55 · 10 minutes · mode: **Accept edits***

**What you'll do:** let Claude build the figure, then make it check its own result.

**Why it matters:** this is the most useful habit of all. Ask for evidence (the command and its
output, the figure, a test) rather than taking "done" on trust. If it heads the wrong way, press
stop and say what you want instead.

**Do this**

1. Switch the mode to **Accept edits**, then send:

```text
The plan is good. Build it.
```

2. Watch it work. When it asks to run a command (to install packages or run the script), read the
   command, then approve it. If it offers to always allow that command, you can say yes.
3. Then ask it to check its work:

```text
Open outputs/before_after.png and check it critically: are the three panels comparable, labelled
with the year, and is the burnt area obvious in 2020? Then print the minimum and maximum reflectance
you plotted, so I can check the units.
```

4. Ask for **one** change you'd want as a reviewer, in your own words, such as bigger titles or a
   scale bar.

**You should see** something like this. The 2020 panel shows a large burnt patch in dark magenta,
which has mostly greened up again by 2025, and the reflectance values are between 0 and 1.

![Example result: false-colour images of the study area in autumn 2019, 2020 and 2025](examples/before_after.png)

*An example result. It already has the caption you'll add in Step 4. Want to see yours now? Ask
"Send me outputs/before_after.png". Otherwise you'll see it on GitHub in Step 5.*

**Learn more:** Claude Code 101,
["The explore → plan → code → commit workflow"](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow),
and the Claude Code [best practices](https://code.claude.com/docs/en/best-practices).

**Next →** [Step 4: Memory and context](#step-4-memory-and-context) · [All steps](README.md#your-steps)

### Step 4: Memory and context

*10:05 · 5 minutes · mode: **Accept edits***

**What you'll do:** look at Claude's working memory, then add a standing rule that it follows from
now on.

**Why it matters:** `CLAUDE.md` holds Claude's standing instructions. Claude reads it at the start
of every session, so you can teach it your lab's conventions once instead of in every prompt. The
*context window* is Claude's working memory: long sessions get summarised automatically, and a new
task deserves a fresh session.

**Do this**

1. Type this command and send it:

```text
/context
```

2. Then send:

```text
Add this rule to CLAUDE.md under "Rules": "Every figure gets a one-line caption underneath that
names the data sources and dates." Then re-run before_after.py so the figure follows the new rule.
```

**You should see**

- `/context` shows how much of the working memory is in use, and what it's used for.
- The figure now has a caption, like the example in Step 3.
- Your new rule in `CLAUDE.md`, in the **Changes** view.

**If you code:** `/compact keep the figure decisions` summarises the conversation, keeping what you
name. `/clear` starts over with an empty memory.

**Learn more:** Claude Code 101,
["The CLAUDE.md file"](https://academy.claude.com/courses/claude-code-101/the-claude-md-file) and
["Context management"](https://academy.claude.com/courses/claude-code-101/context-management);
Claude Code in Action,
["A CLAUDE.md that follows"](https://academy.claude.com/courses/claude-code-in-action/a-claude-md-that-follows).

**Next →** [Step 5: Review, commit, merge](#step-5-review-commit-merge) · [All steps](README.md#your-steps)

### Step 5: Review, commit, merge

*10:10 · 5 minutes · mode: **Accept edits***

**What you'll do:** read what Claude changed, then add it to your project.

**Why it matters:** you are the reviewer. Claude works on its own *branch*, a separate line of
changes. A *pull request* (PR) asks to add that branch to `main`, your project's main line.
Always read the changes (the *diff*) before you merge them.

**Do this**

1. Send:

```text
Commit the script, the figure and the CLAUDE.md change with a clear message, and push.
```

2. Open the **Changes** card beside the chat, then click a file to see what changed.
3. Click one line and leave a comment, for example *"Why this stretch?"*. Send it, and read the
   answer.
4. Click **Create PR**. On GitHub, open **Files changed**: your figure shows as a picture.
5. Click **Merge pull request**, then **Confirm merge**.

**You should see:** the PR merged, and `outputs/before_after.png` on your `main` branch.

**What else Claude Code can do** (a 2-minute tour from the presenters): *sub-agents* (helpers with
their own memory), *skills* (reusable instructions), *MCP* (connections to other tools and data
services), *hooks* (scripts that run automatically at set moments) and GitHub Actions. You can try
them in Step 8.

**Learn more:** Claude Code 101,
["Code review"](https://academy.claude.com/courses/claude-code-101/code-review),
["Subagents"](https://academy.claude.com/courses/claude-code-101/subagents),
["Skills"](https://academy.claude.com/courses/claude-code-101/skills),
["MCP"](https://academy.claude.com/courses/claude-code-101/mcp) and
["Hooks"](https://academy.claude.com/courses/claude-code-101/hooks).

**Next →** [Step 6: Brief it, then walk away](#step-6-brief-it-then-walk-away) · [All steps](README.md#your-steps)

---

## Part 2: A practical build

*10:15–11:55 · a fire-and-glider habitat explorer*

### Step 6: Brief it, then walk away

*10:15 · 15 minutes, then morning tea · mode: **Plan**, then **Auto***

**What you'll do:** give Claude one complete brief, check its plan, then let it build while you're
at morning tea.

**Why it matters:** a good brief is a mission, not a chat. It says what to make, how to check it,
and what to do when unsure.

**Do this**

1. Start a **new session** on this repo. It starts from your updated `main` with an empty memory.
   Set the mode to **Plan**.
2. Paste the brief:

```text
Build a small, reusable tool in this repo: explorer.py. Running `python explorer.py` should write
these to outputs/:

1. ndvi_change.png: NDVI change from autumn 2019 to 2020 (the fire) and from 2020 to 2025
   (recovery), as two panels with one shared, colour-blind-safe diverging colour scale centred on
   zero and a labelled colour bar.
2. severity_summary.csv: one row per fire-severity class (unburnt/outside, low, moderate, high,
   extreme) with the area in hectares, the mean NDVI in 2019, 2020 and 2025, and the number of
   greater glider records from 2000 to 2019 inside that class.
3. REPORT.md: a one-page, plain-English summary with the table, the figures, how each number was
   calculated, and any assumptions you made.
4. glider_map.html: an interactive map of fire severity and the glider records. Skip this if it
   takes more than 10 minutes, and say so in REPORT.md.

Also:
- Write tests in tests/test_explorer.py (at least NDVI of known values, and the hectares of a tiny
  made-up raster) and run them.
- Add a "How to run" section to README.md.
- Commit and push after each output works. When everything works, open a pull request into main
  that summarises the results.

First show me your plan. Once I approve it, work without asking me questions: record assumptions in
REPORT.md, and open every figure to check it before moving on.
```

3. Check the plan. Does it leave out the "no data" values (−999 in the images, 255 in the severity
   map), convert the glider coordinates, work out areas from pixel counts (one pixel = 0.01 ha), use
   one shared colour scale, and include tests? If not, tell it.
4. Switch the mode to **Auto** and reply `Approved. Go ahead.` If **Auto** isn't in the menu, use
   **Accept edits** and keep the session open on your phone, because it will stop at each command
   until you approve it.
5. Wait for the first commit, then go to morning tea. It keeps working in the cloud even if you close
   your laptop.

**You should see:** a to-do list and a first push. At morning tea, open the **Code** tab in the
Claude mobile app to watch it, or to answer it if it asks something.

**What it should make:** something like these two pictures, plus the table in Step 7.

![Example result: NDVI change from 2019 to 2020 and from 2020 to 2025](examples/ndvi_change.png)

*Example `ndvi_change.png`. The fire shows as brown (less green), then the recovery as green.*

![Example result: fire severity with the greater glider records](examples/fire_severity_and_gliders.png)

*A still picture of what `glider_map.html` shows. The real file is a map you can zoom and click.*

**Learn more:** Claude Code in Action,
["Steering long sessions"](https://academy.claude.com/courses/claude-code-in-action/steering-long-sessions)
and ["Permission modes"](https://academy.claude.com/courses/claude-code-in-action/permission-modes).

**Next →** [Step 7: Trust, but verify](#step-7-trust-but-verify) · [All steps](README.md#your-steps)

### Step 7: Trust, but verify

*11:25 · 20 minutes · mode: **Plan**, then **Accept edits***

**What you'll do:** check the work you didn't watch, then merge it.

**Why it matters:** an agent can be confidently wrong. Check in this order: read what changed, check
the numbers, then get a fresh pair of eyes.

**Do this**

1. **Read what changed.** Open the pull request on GitHub, then **Files changed**. Read `REPORT.md`
   and look at the figures. Do they look like the examples in [Step 6](#step-6-brief-it-then-walk-away)?
2. **Check the numbers.** Compare your `severity_summary.csv` with these answers:

   | Fire severity | Area (ha) | Mean NDVI 2019 | 2020 | 2025 | Glider records 2000–2019 |
   |---|---:|---:|---:|---:|---:|
   | Unburnt / outside | 19,163 | 0.62 | 0.71 | 0.65 | 12 |
   | Low | 3,074 | 0.74 | 0.69 | 0.73 | 10 |
   | Moderate | 5,406 | 0.75 | 0.64 | 0.73 | 42 |
   | High | 4,679 | 0.78 | 0.51 | 0.75 | 63 |
   | Extreme | 7,679 | 0.74 | 0.34 | 0.71 | 29 |

   Do yours match? If not, ask Claude why. The usual reasons are "no data" pixels counted as data,
   glider points not converted from latitude/longitude, or areas worked out in degrees. Full
   details: [CHECK_VALUES.md](CHECK_VALUES.md).
3. **Get a fresh pair of eyes.** Start a **new session** in **Plan** mode. It has no memory of
   building the code, so it reviews it with fresh eyes:

```text
Review the open pull request as a sceptical reviewer. Check explorer.py for mistakes with units,
nodata and map projections, check that every number in REPORT.md matches severity_summary.csv, and
run the tests. List the problems in order of importance. Don't change anything.
```

4. **Fix and merge.** Ask for the most important fix (in that session with **Accept edits**, or as a
   comment on the PR), then merge the PR.

**You should see:** the PR merged, and your numbers matching the answers, or you know why they
don't.

**Learn more:** Claude Code in Action,
["Trust it: verifying unsupervised runs"](https://academy.claude.com/courses/claude-code-in-action/trust-it-verifying-unsupervised-runs);
Claude Code 101, ["Code review"](https://academy.claude.com/courses/claude-code-101/code-review).

**Next →** [Step 8: Make it yours](#step-8-make-it-yours) · [All steps](README.md#your-steps)

### Step 8: Make it yours

*11:45 · 10 minutes*

**What you'll do:** pick one thing to try, and write the prompt in your own words. You know what a
good brief looks like now.

**Back to your early task (try this first)**

- Open the session from the [early task](#early-task-let-claude-surprise-you). Ask: *"Summarise
  what you built, how to run it, and how you checked it."* Look at what it made.
- Check it the way you did in Step 7: what changed, does it run, and are the numbers and units
  believable? What would you need to see before you showed it to a colleague?
- Compare the one-line request with your Step 6 brief. Which result can you trust more, and why?
  Then ask the early-task session for one improvement.

**Or extend your explorer**

- *Since the fire:* add the glider records from 2020 onwards as a second count. Where have gliders
  been seen since the fire?
- *Location accuracy:* leave out records whose location is uncertain by more than 1 km, and show how
  the counts change.
- *Moisture:* add NDMI next to NDVI.
- *Recovery:* map where 2025 NDVI is back within 0.05 of 2019.
- *Forest or farmland?* Split each severity class into tree cover and everything else, using
  `data/land_cover_2020.tif`. Why does NDVI in the unburnt class go *up* in 2020?

**If you code**

- *Command-line tool:* options for the years and the output folder, plus a test for each function.
- *Automatic tests:* a GitHub Actions workflow that runs the tests on every pull request. Private
  repos on GitHub Free get a limited monthly allowance.
- *Hook:* a `.claude/settings.json` hook that tidies (formats) every Python file Claude edits, using
  `ruff`. Claude Code 101: ["Hooks"](https://academy.claude.com/courses/claude-code-101/hooks).
- *Skill:* `.claude/skills/check-figure/SKILL.md`, a checklist Claude applies whenever it makes a
  figure. Claude Code 101: ["Skills"](https://academy.claude.com/courses/claude-code-101/skills).
- *Sub-agent:* `.claude/agents/reviewer.md`, a reviewer that can read but not change anything. Then
  ask Claude to "use the reviewer subagent on this PR". Claude Code 101:
  ["Subagents"](https://academy.claude.com/courses/claude-code-101/subagents).

**Next →** [After the workshop](#after-the-workshop) · [All steps](README.md#your-steps)

---

## After the workshop

- Your early-task session is still there: you can keep building on it.
- This repo is private and yours to keep. Keep the attributions in `data/ATTRIBUTION.md` with
  anything you share.
- Tidy up when you're done: archive your sessions at claude.ai/code. If you like, remove this repo
  from the Claude GitHub App on GitHub (**Settings → Applications → Installed GitHub Apps → Claude →
  Configure**). Cancel the Pro plan if you only got it for today.
- Keep learning, for free:
  [Claude Code 101](https://academy.claude.com/courses/claude-code-101) (1.5 hours) and
  [Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action) (1 hour), then
  [Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills) and
  [Introduction to subagents](https://academy.claude.com/courses/introduction-to-subagents).

**You've finished.** Thank you for coming! · [All steps](README.md#your-steps)
