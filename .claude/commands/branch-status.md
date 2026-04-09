---
category: git
allowed-tools: Bash(git branch:*), Bash(git status:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git fetch:*), Bash(git for-each-ref:*), Bash(git merge-base:*), Bash(git show-ref:*)
description: Quick overview of all branches — merged status, divergence, last activity
---

## Purpose

Show a concise dashboard of all branches and their relationship to main. This is read-only — it never modifies anything.

## Instructions

Run these commands to gather data:

```bash
git fetch --prune 2>/dev/null

# For each local branch, determine:
# 1. Merged into main? (git branch --merged main)
# 2. Commits ahead of main (git log main..<branch> --oneline | wc -l)
# 3. Commits behind main (git log <branch>..main --oneline | wc -l)
# 4. Last commit date and message (git log -1 --format="%cr|%s" <branch>)
# 5. Whether it has a remote tracking branch
```

Then display a table like this:

```
Branch Status (relative to main)
=================================

  Branch                        │ Status  │ Ahead │ Behind │ Last Activity     │ Remote
  ──────────────────────────────┼─────────┼───────┼────────┼───────────────────┼────────
* cleanup-2026-02-09            │ active  │  +27  │    0   │ 4 days ago        │ yes
  local-llm-experiment          │ active  │   +5  │  -22   │ 3 months ago      │ yes
  scraping-chembl               │ merged  │    0  │    0   │ 5 months ago      │ yes
  scraping-drugbank             │ active  │   +1  │  -25   │ 6 months ago      │ yes
  main-bk-pre-drugbank-merge    │ merged  │    0  │    0   │ 8 months ago      │ yes
  main-bk-prechembl             │ merged  │    0  │    0   │ 10 months ago     │ yes
  ...

Remote-only branches (no local tracking):
  origin/draft                  │ merged  │    0  │    0   │ 12 months ago     │ -
  origin/2024-10-07-csv-edits   │ ???     │   +3  │   -8   │ 18 months ago     │ -
  ...

Legend: * = current branch | merged = all commits in main | active = has unmerged commits
```

### Column Definitions

- **Status**: `merged` if fully merged into main, `active` if unmerged commits exist
- **Ahead**: number of commits in this branch but not in main
- **Behind**: number of commits in main but not in this branch
- **Last Activity**: relative time of the most recent commit on the branch
- **Remote**: whether a corresponding remote branch exists

### Additional Notes to Include

After the table, add a brief summary:
- Total branches (local / remote-only)
- How many are merged and could be cleaned up (mention `/branch-cleanup`)
- How many are actively diverged from main
- Flag any branches that are significantly behind main (>10 commits) as candidates for rebasing

### Arguments

If the user passes text after the command:
- `--local` — only show local branches
- `--remote` — only show remote branches
- A branch name — show detailed info for just that branch (ahead/behind, commit list, tracking status)

---

Process any arguments passed after the command:
