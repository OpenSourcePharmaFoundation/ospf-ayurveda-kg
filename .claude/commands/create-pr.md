---
category: git
description: Create a pull request from the current branch with auto-generated description
---

First, re-read the following files to ensure you understand the project context:
1. The CLAUDE.md file at the root of payment-sdk-workspaces
2. This command file itself at payment-sdk-workspaces/.claude/commands/create-pr.md

## Command Overview

This command creates a pull request from the current branch to the main branch with an automatically generated description based on the differences between the branches.

## Instructions

1. **Check current branch status**
   - Run `git status` to ensure all changes are committed
   - Get the current branch name
   - Verify we're not on the main branch

2. **Analyze branch differences**
   - Run `git log main..HEAD --oneline` to see all commits in this branch
   - Run `git diff main...HEAD --stat` to see changed files summary
   - Run `git diff main...HEAD` to see detailed changes (if needed for context)

3. **Generate PR description - First Pass**
   Create a comprehensive PR description that includes:
   - **Summary**: 2-3 sentences describing what this PR accomplishes
   - **Changes**: Bullet list of key changes made
   - **Testing**: Suggestions for how to test the changes
     - If the entire commit is just documentation, exclude this section.
     - Otherwise, check that the Testing section actually includes a test plan, and doesn't just include another list of changes in the PR. If it DOES just contain a list of changes, generate a new section, with an explicit prompt not to just give a list of the changes, but to instead come up with a step-by-step plan to test the changes.
   - **Related Issues**: If commit messages reference Jira issues, include them

   Make this first version detailed and thorough.

4. **Simplify the description - Second Pass**
   - If the word given after the colon at the end of this command is VERBOSE (or some variant of it), skip this step.
   After generating the initial description, immediately simplify it:
   - Keep the summary to 1-2 sentences
   - Reduce the changes list to only the most important items (3-5 bullets max)
   - Keep testing notes brief and actionable
   - Remove any verbose explanations

5. **Create the pull request**
   Use the `gh pr create` command with:
   - `--title`: A concise, descriptive title based on the main change
   - `--body`: The simplified description from step 4
   - `--base main`: Target the main branch

   **IMPORTANT**: Do NOT include any "Generated with Claude Code" or similar tags in the PR title or body. The PR should appear as if written directly by the developer.

6. **Provide the PR URL**
   After creation, output the PR URL so the user can review it on GitHub.

## Notes

- If there are uncommitted changes, ask the user if they want to commit them first. But don't require it.
- If already on main branch, inform the user and stop
- Keep the final PR description professional and concise
- Focus on what changed and why, not implementation details
- The simplification step is crucial - aim for clarity and brevity in the final version

----

Check the word after the colon at the end of this line (the user input after the command), and if it says VERBOSE, verbose, --verbose, -v, or some variant of those, skip step 4:
