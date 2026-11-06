# Notes for the presenters

*Participants can ignore this folder.*

## The idea in one paragraph

This one small repo is the whole workshop. Each participant clicks **Use this template** to make a
private copy, and Claude Code works in their copy. Part 1 teaches the essentials of Claude Code from
the Claude Academy intro courses. Each idea is shown on the shared screen and tried
straight away, in about 5 minutes. Part 2 is a practical build that runs over morning tea and is
checked afterwards. The analysis is deliberately
simple (indices, areas, counts). What participants practise is planning, checking and reviewing.
Everyone works in **Auto** mode (**Plan** only when planning or reviewing), so nothing waits for
approval.

## Why it's this simple (sanity check, 5 Nov 2026)

The previous design asked too much of a 3½-hour morning:

- **Mostly setup.** About 40 of the "hands-on hour's" 60 minutes went on a fork, the GitHub app and
  a custom cloud environment with a pasted setup script. People got about 15 minutes of actually
  using Claude before 80 minutes of talks.
- **The unattended runs would have stalled.** In a cloud session, **Accept edits** mode still stops
  to ask before every command
  ([permission modes](https://code.claude.com/docs/en/permission-modes)). Anyone without **Auto** mode
  would have come back to an agent that had done nothing.
- **Forks can't be private.** A fork of a public repo is always public
  ([GitHub docs](https://docs.github.com/en/pull-requests/reference/forks)). GitHub Pages doesn't
  work on private repos with a free account either.
- **The research cards needed expert checking.** They involved spatial cross-validation, bootstrap
  intervals, area estimation and transfer tests. The last 25 minutes also held an audit,
  show-and-tells and a leaderboard.
- **Slow, unpredictable installs.** In tests on 5 Nov, a fresh install of the Python packages in a
  cloud session took anywhere from under a minute to 12 minutes.

What changed: each person makes one simple environment (**Full** network access, no setup
script), the copy is private,
and there are 85 minutes of hands-on time (09:35–10:30 and 11:25–11:55) instead of about 45. The
builds keep running, unattended, between the two sessions.

## Run sheet (hands-on: 09:35–10:30 and 11:25–11:55, then the closing talk)

The builds run unattended between the two sessions, from 10:30 to 11:25. People can check on them
from their phones.

| Time | Min | What | Workbook |
|---|---|---|---|
| 09:35 | 10 | **Hands-on, session 1** (led on a shared screen). Everyone opens a session, then launches the early task in a second session (Auto). Helpers fix setup problems; anyone blocked pairs up | Start, Early task |
| 09:45 | 30 | **Part 1: Claude Code essentials.** Five ideas, each shown and tried in about 5 minutes (Step 3 gets 10) | Steps 1–5 |
| 10:15 | 15 | **Part 2: brief the build.** Stop the early task if it's still running, then plan, review, switch to **Auto**, and see it start | Step 6 |
| 11:25 | 20 | **Hands-on, session 2. Trust, but verify:** read the changes, compare with CHECK_VALUES.md, fresh-eyes review, fix, merge | Step 7 |
| 11:45 | 10 | **Make it yours:** two minutes on the early task (open request or full brief; the Blue Mountains page agrees with FESM on only 42.6% of its area), then everyone fills in the brief template for a question from their own work, approves the plan and leaves it running | Step 8 |
| 11:55 | 20 | Sovereign AI: running open AI models on your own hardware (presentation and live demo). The Step 8 builds keep working | |

**If you're running late,** cut in this order. Before morning tea: Step 4 becomes a demo on the
shared screen, then skip the line comment in Step 5. In session 2: drop the early-task discussion in
Step 8, and if it's later still, people launch their own question at home.
**Never cut** launching Step 6 before morning tea, or Step 7.

**Backup:** at 08:00 on the day, one presenter runs Step 6 in their own copy. If live builds fail,
show that pull request at 11:25.

## The early task (added 5 Nov)

At 09:40, people paste an open one-line request into a second session and leave it running in
**Auto** while they do Part 1:

> i want to use python to create a remote sensing demonstration with sentinel data from australia.
> it does not have to be complex but should be effective in demonstrating claude code capabilities.
> use sub-agents to conserve context window

A presenter tried this in a fresh environment on 5 Nov and was surprised by what it produced. It gives
people an early sense of what Claude Code can do, and a lesson later on. Step 8 opens with a
two-minute discussion that compares it with the Step 6 brief: an open request can produce something
impressive that's hard to check, and a clear brief produces something you can trust. People check
their early task properly at home.

Results in participants' copies will differ from an empty repo. Claude reads `CLAUDE.md` and will
probably use the Sentinel-2 data in `data/`, although with **Full** network access it can also
download fresh images. Either is fine, and worth pointing out: context shapes what the
agent does.

`examples/early_task/` holds two presenter tests. `session_start.png` is a screenshot from early in
a test of a similar request, in a session with no repo and every website allowed (shown in the
workbook's early task). `blue_mountains_demo.zip` is the web page from a later test with a longer
request: Sentinel-2 burn severity for the 2019–20 Black Summer fires in the Greater Blue Mountains,
NSW, compared with the NSW FESM severity map with 95% intervals, plus recovery to 2026, with the code
and output for each step. `blue_mountains_preview.jpg` is its summary figure, shown in the workbook.

## Before Monday: checklist

1. **Promote** this repo to production `main` in one squashed pull request, merged by a person.
2. In production, go to **Settings → General** and tick **Template repository**. Without this, the
   "Make my private copy" link in SETUP.md doesn't work. (Checked 6 Nov: the public repo shows as
   a template.)
3. With a **fresh** Pro account and a **fresh** GitHub account, do SETUP.md and time it. The target
   is under 20 minutes, with no help.
4. On that fresh account, check that **Auto** appears in the mode menu. The workshop runs in
   **Auto** throughout (**Plan** only for planning and the review), so if it's missing, find out
   why before Monday.
5. Do the whole workbook once and time each step against the run sheet. Compare
   `outputs/severity_summary.csv` with CHECK_VALUES.md. Also check that the Step 7 review, in
   **Plan** mode, can install the packages and run the tests: Plan mode may block commands that
   change things. If it can't, move "run the tests" into Step 7's fix-and-merge step, which runs in
   **Auto**.
6. Check the Pro usage meter after that run, so you know a participant won't hit the limit.
   Include the early task: two sessions running at the same time use the allowance faster. If it
   gets close, tell people to stop the early-task session (the stop button) once it has made its
   first result.
   Also run the early task once in a fresh copy with the **AEO** environment (Full network), and note what it
   builds and how long it takes.
7. Check that *"Send me outputs/before_after.png"* gives a download in a cloud session. If it
   doesn't, delete that line from Step 3.
8. Send the pre-work email: SETUP.md (about 20 minutes), a personal Pro plan, a personal GitHub
   account, no work accounts, and a question from their own work to bring (SETUP.md step 8).
9. Screenshots for every SETUP.md step are in `examples/setup/`.
   Optional extras: the "Make my private copy" form showing the template (from the fresh test
   account in item 3), the GitHub app's **Only select repositories** screen, the mode menu, and the
   **Changes** card with **Create PR**.
10. On Sunday, do a full dry run with two or three remote sensing people who don't use AI tools:
    the audience. Note every place they hesitate. Include Step 8 with their own question, and
    check that the open-data catalogues in the workbook's "Start your own project" answer from a
    fresh **AEO** session.
11. Make a three-question feedback form, and link it at the end of the workbook: confidence to use
    Claude Code on their own data, before and now (1–5); one thing they'll try next; what nearly
    stopped them.

## On the day

- **Helpers:** one each for plans and accounts, GitHub (the copy and the app), and sessions.
- **Sticky notes:** two colours that colour-blind people can tell apart (for example blue and
  yellow, not green and red), marked ✓ (there) or ? (stuck), at each checkpoint.
- **No paid plan:** pair them with a neighbour. A few guest passes (7-day Pro trials) are available
  from a presenter's own Pro account.

## Where the data came from

The seven files in `data/` were copied from the AEO26 data package built on 5 Nov 2026:

- the DEA Sentinel-2 autumn composites for 2019, 2020 and 2025;
- the NSW FESM 2019/20 fire-severity map;
- the ESA WorldCover 2020 land-cover map;
- the Atlas of Living Australia greater glider records inside the study area, with the
  non-commercial records left out.

Their SHA-256 hashes are in `data/MANIFEST.csv`. The STAC item lists and query details are in
`data/provenance/`. The full data package and its build scripts are on the staging branch
(`claude/dazzling-goldberg-b6k2ns`).

`CHECK_VALUES.md` comes from `python presenters/check_values.py`, and the example pictures in
`examples/` (shown in the README and workbook Steps 3 and 6) come from
`python presenters/make_examples.py`. Re-run both if anything in `data/` changes. The pictures are
deliberately close to the "answers": they make the steps easier to follow. The files in `examples/early_task/` and
`examples/setup/` aren't generated: they're a presenter's own early-task test and setup screenshots.

## Left out on purpose (still on the staging branch)

Research cards R1–R7 and their evaluation harness, the full 187 MB data package, the leaderboard,
the free-plan track, the cloud setup script, and the local-AI walkthrough for the sovereign-AI talk.
Only bring one back if there's time to test it before Monday.

## Still to decide

- A licence for the code and text. The live repo has no `LICENSE` file yet, which means people
  can read it but not reuse it. The data keep their own licences (`data/ATTRIBUTION.md`). It
  matters more now that people are meant to reuse the Step 8 brief and `CLAUDE.md` at work.
- Is 12:15–12:30 free? If so, give people those minutes to look at their Step 8 result, write their
  next step, and fill in the feedback form.
- The notes above point to a staging branch (`claude/dazzling-goldberg-b6k2ns`) for the full data
  package and the left-out material, but on 6 Nov only `main` was on GitHub. Say where they live
  now, or remove the pointer.
