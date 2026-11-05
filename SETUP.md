# Setup before the workshop

It takes **about 15 minutes**. Please do it at home before Monday 9 November, so the morning is about
learning, not logging in. On the day we start with a quick check, and helpers will sort out anything
that's stuck.

Use the same web browser for every step, and use **personal** accounts, not work ones.

**Jump to a step:** [1](#1-get-a-claude-pro-plan) · [2](#2-get-a-github-account) · [3](#3-make-your-own-private-copy-of-this-repo) · [4](#4-open-claude-code-and-connect-github) · [5](#5-let-claude-see-your-copy-and-nothing-else) · [6](#6-say-hello) · [If something goes wrong](#if-something-goes-wrong)

## 1. Get a Claude Pro plan

*About 5 minutes.*

1. Go to [claude.ai](https://claude.ai) and sign in, or sign up, with your personal email.
2. Upgrade to **Pro** (or a higher individual plan, such as Max). Pro is a monthly subscription, so
   you can cancel it after the workshop. Prices: [claude.com/pricing](https://claude.com/pricing).

Have a guest pass from the presenters instead? Open its link and follow the prompts. It gives you a
7-day Pro trial.

**Next →** [2. Get a GitHub account](#2-get-a-github-account) · [All steps](README.md#your-steps)

## 2. Get a GitHub account

*About 3 minutes.*

1. Go to [github.com](https://github.com) and sign up with your personal email. The free plan is
   fine.
2. Your username is your **handle**. Note it down.

**Next →** [3. Make your own private copy of this repo](#3-make-your-own-private-copy-of-this-repo) · [All steps](README.md#your-steps)

## 3. Make your own private copy of this repo

*About 2 minutes.*

1. While signed in to GitHub, click this link:
   **[Make my private copy](https://github.com/new?template_owner=RSGISagent&template_name=AEO26_AgenticAI_Workshop&owner=@me&visibility=private&name=aeo26-workshop)**
2. Check that **Owner** is you, that the name is `aeo26-workshop`, and that **Private** is selected.
3. Click the button to create the repository.

You now have `github.com/<your-handle>/aeo26-workshop`, marked **Private**. Everything you do in the
workshop is saved there, and only you can see it.

*Why a copy and not a "fork"? A fork of a public repo is always public. A copy made from a template
is yours, and it can be private.*

*The link doesn't work?* Open
[github.com/RSGISagent/AEO26_AgenticAI_Workshop](https://github.com/RSGISagent/AEO26_AgenticAI_Workshop),
click **Use this template**, then **Create a new repository**, and fill in the same details.

**Next →** [4. Open Claude Code and connect GitHub](#4-open-claude-code-and-connect-github) · [All steps](README.md#your-steps)

## 4. Open Claude Code and connect GitHub

*About 3 minutes.*

1. Go to [claude.ai/code](https://claude.ai/code).
2. Click **Connect GitHub** and approve it. Check that it shows your personal GitHub account.

**Next →** [5. Let Claude see your copy, and nothing else](#5-let-claude-see-your-copy-and-nothing-else) · [All steps](README.md#your-steps)

## 5. Let Claude see your copy, and nothing else

*About 2 minutes.*

1. When asked, install the **Claude GitHub App**. You can also start the install from
   [github.com/apps/claude/installations/new](https://github.com/apps/claude/installations/new).
2. Choose your personal account.
3. Choose **Only select repositories**, pick `aeo26-workshop`, and install.

*Already installed the Claude app before, for example on another repo?* On GitHub, go to
**Settings → Applications → Installed GitHub Apps → Claude → Configure**. Add `aeo26-workshop` under
**Only select repositories**, and click **Save**.

**Next →** [6. Say hello](#6-say-hello) · [All steps](README.md#your-steps)

## 6. Say hello

*About 3 minutes.*

1. At [claude.ai/code](https://claude.ai/code), choose `aeo26-workshop` in the repository list.
2. Leave the environment as **Default**. There's nothing to set up.
3. In the mode menu under the message box, choose **Plan**.
4. Send: `Hello! In one sentence, what is this repo for?`

If Claude answers, you're done. See you on Monday!

**All done!** On the day, start with the [workbook](WORKBOOK.md#start-open-your-session). · [All steps](README.md#your-steps)

---

## If something goes wrong

- **"Claude Code isn't available on your account."** Check that you're on Pro, and that you're
  signed in to the personal account you upgraded. After upgrading, sign out and back in.
- **My copy isn't in the list at claude.ai/code.** The Claude GitHub App must be allowed on
  `aeo26-workshop` (step 5). Check that you connected the same GitHub account that owns the copy,
  then reload the page.
- **My copy came out public, or went to an organisation.** If it's public, go to **Settings →
  General → Danger Zone → Change visibility** and choose **Private**. If it went to an organisation,
  delete it and repeat step 3 with yourself as the owner.
- **The first session is slow.** The first start copies your repo into a fresh cloud computer. Give
  it a couple of minutes.
- **Claude keeps asking for permission.** In **Accept edits** mode it asks before running each
  command. That's normal: read the command, then approve it. **Auto** mode asks much less.
- **Anything else.** Bring it on the day: helpers fix setups in the first 15 minutes. You can also
  [open an issue](https://github.com/RSGISagent/AEO26_AgenticAI_Workshop/issues).

Official help: [Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web) ·
[Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
