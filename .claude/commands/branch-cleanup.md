---
category: git
allowed-tools: Bash(git branch:*), Bash(git status:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git push:*), Bash(git fetch:*), Bash(git for-each-ref:*), Bash(git show-ref:*), Bash(git merge-base:*)
description: Identify and clean up stale/merged branches (local and remote)
---

First, reread the following files:
1. The CLAUDE.md file at the project root
2. This command file itself (`.claude/commands/branch-cleanup.md`)

## Purpose

Scan all local and remote branches, identify which are stale (fully merged into main, or abandoned), and offer to clean them up. This is a **destructive operation** — always present findings first and get explicit user approval before deleting anything.

## Instructions

### Phase 1: Assessment

Run these commands to build a complete picture:

```bash
# Ensure we have up-to-date remote info
git fetch --prune

# Current branch (never delete this)
git rev-parse --abbrev-ref HEAD

# Main branch tip
git rev-parse main

# All local branches with their merge status relative to main
git branch --merged main
git branch --no-merged main

# All remote branches with their merge status relative to main
git branch -r --merged main
git branch -r --no-merged main

# For unmerged branches, check how far they've diverged
# (run git log main..<branch> --oneline for each)
```

### Phase 2: Classify Branches

Organize branches into these categories:

#### Protected (Never Delete)
- `main` — the main branch
- The currently checked-out branch
- Any branch the user explicitly says to keep

#### Safe to Delete (Fully Merged)
Local and remote branches where `git branch --merged main` includes them. These branches' commits are all reachable from main — deleting them loses nothing.

#### Backup Branches
Branches named `*-bk-*` or `*-backup*`. These were likely created as safety snapshots. Flag them for the user's attention — they may want to keep some, but if they're merged into main they're redundant.

#### Potentially Stale (Unmerged but Inactive)
Branches that are NOT merged into main but haven't had commits in a long time. Check the date of the last commit:
```bash
git log -1 --format="%ci %s" <branch>
```
If the last commit is older than 3 months, flag as potentially stale.

#### Active (Unmerged and Recent)
Branches with recent commits that aren't merged. These should be preserved.

### Phase 3: Present Findings

Display a clear table of all branches organized by category:

```
Branch Cleanup Report
=====================

Protected (will not touch):
  * main
  * <current-branch>

Safe to Delete (fully merged into main):
  LOCAL:
    - main-bk-prechembl           (merged, last commit: 2024-xx-xx)
    - neo4j-prep                   (merged, last commit: 2024-xx-xx)
    ...
  REMOTE:
    - origin/draft                 (merged, last commit: 2024-xx-xx)
    ...

Backup Branches (review recommended):
    - main-bk-pre-drugbank-merge   (merged/unmerged, last commit: ...)

Potentially Stale (unmerged, no commits in 3+ months):
    - scraping-drugbank            (1 unmerged commit, last: 2024-xx-xx)

Active (unmerged, recent activity):
    - cleanup-2026-02-09           (27 commits ahead, last: 2026-04-02)
```

Include commit counts ahead of main and the last commit date for each branch.

### Phase 4: Get Approval

Ask the user which categories to clean up. Suggest options:
1. **Delete all "Safe to Delete" branches** (local + remote)
2. **Delete only local "Safe to Delete" branches** (conservative — keep remote)
3. **Cherry-pick specific branches to delete** (show numbered list)
4. **Do nothing** (just wanted the report)

### Phase 5: Execute (Only After Approval)

For approved local deletions:
```bash
git branch -d <branch>   # -d (not -D) since they're merged — this is a safety check
```

For approved remote deletions:
```bash
git push origin --delete <branch>
```

After all deletions, run `git branch -a` to show the cleaned-up state.

### Important Rules

- **NEVER delete `main` or the current branch**
- **NEVER use `git branch -D`** (force delete) — only use `-d` (safe delete). If `-d` refuses, the branch isn't actually merged and should be flagged to the user.
- **NEVER delete remote branches without explicit user approval for remote cleanup**
- **Always present findings before any deletion**
- If the user passes arguments after the command (e.g., `/branch-cleanup local-only`), respect those:
  - `local-only` or `--local` — only assess and clean local branches
  - `remote-only` or `--remote` — only assess and clean remote branches
  - `report` or `--dry-run` — only show the report, don't offer to delete

---

Process any arguments passed after the command:
