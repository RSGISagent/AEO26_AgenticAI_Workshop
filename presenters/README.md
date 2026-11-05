# Notes for the presenters

*Participants can ignore this folder.*

## The idea in one paragraph

This one small repo is the whole workshop. Each participant clicks **Use this template** to make a
private copy, and Claude Code works in their copy. Part 1 teaches the essentials of Claude Code from
the Claude Academy intro courses. Each idea is shown for 3–4 minutes, then tried for 6–7. Part 2 is a
practical build that runs over morning tea and is checked afterwards. The analysis is deliberately
simple (indices, areas, counts). What participants practise is planning, checking and reviewing.

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

What changed: there's no custom environment (the **Default** one is enough), the copy is private,
and the run sheet has about 110 minutes of hands-on time instead of about 45. The talks drop from 80
minutes to 45.

## Run sheet (09:00–12:30, including a 30-minute morning tea)

| Time | Min | What | Workbook |
|---|---|---|---|
| 09:00 | 10 | Welcome, Acknowledgement of Country, goals, safety on one slide, the "three levels of agency" in 2 minutes | |
| 09:10 | 15 | Setup check: everyone does SETUP.md step 6, then launches the early task in a second session (Auto). Helpers fix the rest. Anyone blocked pairs up | Start, Early task |
| 09:25 | 50 | **Part 1: Claude Code essentials.** Five ideas, each shown for 3–4 minutes, then tried for 6–7 | Steps 1–5 |
| 10:15 | 15 | **Part 2: brief the build.** Plan, review, switch to **Auto**, first push | Step 6 |
| 10:30 | 20 | Talk P2: an agentic research project in practice (cut from 25) | Claude is building |
| 10:50 | 30 | *Morning tea.* People check their session on their phones | Claude is building |
| 11:20 | 20 | **Trust, but verify:** read the changes, compare with CHECK_VALUES.md, fresh-eyes review, fix, merge | Step 7 |
| 11:40 | 10 | **Make it yours:** come back to the early task first, then one extension, or a stretch task for coders | Step 8 |
| 11:50 | 25 | Talk P4: sovereign AI (live demo, then the decision matrix) | |
| 12:15 | 15 | Two or three show-and-tells, wrap-up, exit poll | |

**If you're running late,** cut in this order: Step 8 becomes homework; P2 drops to 10 minutes;
Step 4 becomes a demo only; one show-and-tell instead of three. **Never cut** launching Step 6
before morning tea, or Step 7.

**Backup:** at 08:00 on the day, one presenter runs Step 6 in their own copy. If live builds fail,
show that pull request at 11:20.

## The early task (added 5 Nov)

At 09:15, people paste an open one-line request into a second session and leave it running in
**Auto** while they do Part 1:

> i want to use python to create a remote sensing demonstration with sentinel data from australia.
> it does not have to be complex but should be effective in demonstrating claude code capabilities.
> use sub-agents to conserve context window

A presenter tried this in a fresh environment on 5 Nov and was surprised by what it produced. It gives
people an early sense of what Claude Code can do, and a lesson later on. In Step 8 people check it the way Step 7 teaches, then compare it
with their Step 6 brief: an open request can produce something impressive that's hard to check, and
a clear brief produces something you can trust.

Results in participants' copies will differ from an empty repo. Claude reads `CLAUDE.md` and will
probably use the Sentinel-2 data in `data/`. The Default environment blocks some download sites, so
Claude may fall back to the local data. That's fine, and worth pointing out: context shapes what the
agent does.

## Before Monday: checklist

1. **Promote** this repo to production `main` in one squashed pull request, merged by a person.
2. In production, go to **Settings → General** and tick **Template repository**. Without this, the
   "Make my private copy" link in SETUP.md doesn't work.
3. With a **fresh** Pro account and a **fresh** GitHub account, do SETUP.md and time it. The target
   is under 15 minutes, with no help.
4. On that fresh account, note whether **Auto** appears in the mode menu. If it doesn't, people will
   have to approve commands from their phones over morning tea (the workbook covers this).
5. Do the whole workbook once and time each step against the run sheet. Compare
   `outputs/severity_summary.csv` with CHECK_VALUES.md.
6. Check the Pro usage meter after that run, so you know a participant won't hit the limit.
   Include the early task: two sessions running at the same time use the allowance faster. If it
   gets close, tell people to stop the early-task session (the stop button) once it has made its
   first result.
   Also run the early task once in a fresh copy with the **Default** environment, and note what it
   builds and how long it takes.
7. Check that *"Send me outputs/before_after.png"* gives a download in a cloud session. If it
   doesn't, delete that line from Step 3.
8. Send the pre-work email: SETUP.md (about 15 minutes), a personal Pro plan, a personal GitHub
   account, and no work accounts.
9. Optional screenshots for SETUP.md. The most useful five are the "Make my private copy" form; the
   GitHub app's **Only select repositories** screen; the new-session screen (repo, environment and
   mode); the mode menu; and the **Changes** card with **Create PR**.
10. On Sunday, do a full dry run with two or three people who don't code.

## On the day

- **Helpers:** one each for plans and accounts, GitHub (the copy and the app), and sessions.
- **Sticky notes:** green or red at each checkpoint.
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
deliberately close to the "answers": they make the steps easier to follow.

## Left out on purpose (still on the staging branch)

Research cards R1–R7 and their evaluation harness, the full 187 MB data package, the leaderboard,
the free-plan track, the cloud setup script, and the local-AI walkthrough for the sovereign-AI talk.
Only bring one back if there's time to test it before Monday.

## Still to decide

- Whether to cut talks P1 and P3. P1's framing fits into the welcome, and P3 isn't needed for the
  build.
- A licence for the code and text. The live repo has no `LICENSE` file yet, which means people
  can read it but not reuse it. The data keep their own licences (`data/ATTRIBUTION.md`).
