---
name: create-pr
description: >
  Create or update a pull request from the current branch with auto-generated description.
  Also handles updating an existing PR's title or body when given a PR URL or number.
tools: Bash(git status:*), Bash(git log:*), Bash(git diff:*), Bash(git push:*), Bash(git rev-parse:*), Bash(gh pr create:*), Bash(gh pr view:*), Bash(gh api:*)
when_to_use: >
  create PR, open PR, update PR, edit PR description, tighten PR, rewrite PR body,
  update pull request, change PR title, improve PR description
---

## Detect mode

If the user provides a PR URL or number, or asks to update/edit/tighten a PR, this is an **update**. Otherwise it's a **create**.

---

## Create mode

Create a pull request from the current branch.

1. **Check branch status and analyze changes** (run in parallel where possible)
   - `git status` — ensure all changes are committed; if on main, inform the user and stop
   - `git rev-parse --abbrev-ref HEAD` — get current branch name
   - `git log main..HEAD --oneline` — commits in this branch
   - `git diff main...HEAD --stat` — changed files summary
   - `git diff main...HEAD` — detailed changes (read selectively if large)

2. **Push if needed**
   - Run `git push origin <current_branch_name>` (safe; no-ops if already up to date)

3. **Generate PR title and description**

   **Title:** Keep concise. May add `etc` at the end for refactor PRs with many small changes.

   **Body format** (generate directly as concise — no verbose-then-simplify):
   - **Summary**: 1-2 sentences on what and why
   - **Changes**: 3-5 key bullets max
   - **Testing**: Brief, actionable test plan (not just a list of changes). Exclude for docs-only PRs.
   - **Links**: GitHub issues as bullet links if referenced in commits.

   If the argument is VERBOSE (or a variant: verbose, --verbose, -v), make the description more detailed instead of concise.

4. **Create the PR**
   ```
   gh pr create --title "<title>" --body "<body>" --base main
   ```

5. **Output the PR URL.**

---

## Update mode

Update an existing PR's title and/or body.

1. **Fetch the current PR** (run in parallel where possible)
   - `gh pr view <number> --repo <owner/repo> --json title,body,headRefName,baseRefName,commits,files,additions,deletions`
   - If the branch is checked out locally, also run `git log` and `git diff` against the base branch for richer context

2. **Draft the new title and/or body** following the same formatting rules as create mode. Preserve any content the user didn't ask to change.

3. **Update the PR via the REST API**

   `gh pr edit` is broken on repos that ever used GitHub Projects Classic — it fails with:
   ```
   GraphQL: Projects (classic) is being deprecated...
   ```

   **Always use the REST API instead:**
   ```bash
   # Write body to a temp JSON file to avoid shell escaping issues
   cat > "$TMPDIR/pr-body.json" <<'ENDJSON'
   {
     "title": "new title here",
     "body": "new body here"
   }
   ENDJSON

   gh api repos/<owner>/<repo>/pulls/<number> \
     --method PATCH \
     --input "$TMPDIR/pr-body.json" \
     --jq '.html_url'
   ```

   Omit `title` or `body` from the JSON to leave that field unchanged.

4. **Output the PR URL.**

---

## Rules

- Don't ask the user if they want to commit uncommitted changes.
- If already on main branch (and creating), inform the user and stop.
- Keep descriptions professional and concise — focus on what changed and why.
- NEVER mention a TODO list file change unless it's the only change in the PR.
- Use the correct base branch per repo (check `.claude/base-branches.txt` if it exists, otherwise default to `main`).
