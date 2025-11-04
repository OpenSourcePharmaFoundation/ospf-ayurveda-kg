# Review Recent Project Activity

Please analyze the recent project activity and remind me what was being worked on last time. Follow these steps:

## Analysis Steps

1. **Check recent git commits** - Review the last 10-15 commits to understand recent changes
2. **Review current branch** - Identify the current branch and its purpose
3. **Examine file status** - Look at modified/untracked files in git status
4. **Check recent modifications** - Review recently modified files and their timestamps
5. **Review documentation** - Check TODO files, CLAUDE.md updates, and any work documentation

## Summary Format

Provide a concise summary that includes:

- **Current Task/Feature**: What was being worked on
- **Progress Status**: What was completed vs. what remains
- **Branch Context**: Current branch and its purpose
- **All Files Modified**: List ALL changed files from git status and recent commits
  - Mark important/key files with ⭐ AND bold formatting
  - Group by category if helpful (e.g., scripts, docs, data)
  - Include both tracked and untracked files
- **Next Steps**: Any incomplete work or documented next actions
- **Context Notes**: Any relevant context from commit messages or documentation

Focus on giving actionable context to quickly resume work from where it was left off. Be specific about file locations and any partial implementations that need completion.

Priorities
==========
1. PRIORITIZE UNSTAGED AND UNCOMMITTED CHANGES. That's *always* going to be the most recent, if it's present.
2. PRIORITIZE RECENT COMMITS. Those are always going to be the second most recent.
   Look at what was *actually* changed.

Note: ignore Claude Code changes.
