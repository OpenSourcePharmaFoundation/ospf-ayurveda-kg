---
name: freeze
description: Freeze this session's state for later resumption with claude --resume
when_to_use: When pausing work sessions to reclaim memory and wanting to resume them later
allowed-tools: Bash(ls *), Bash(basename *), Bash(head *), Bash(tr *), Bash(date *), Bash(git status:*), Bash(git branch:*), Bash(git log:*), Read, Write
---

# Freeze Session

Freeze this session so it can be resumed later with `claude --resume <session-id>`.

**Run `/freeze` in only ONE session at a time.** The session detection relies on this being the most recently active session for this project.

## Step 1: Detect Your Session ID

This session's JSONL file is the most recently modified one (because this skill is actively executing right now):

```bash
PROJECT_HASH=$(echo "$PWD" | tr '/.' '-')
SESSION_FILE=$(ls -t ~/.claude/projects/${PROJECT_HASH}/*.jsonl | head -1)
SESSION_ID=$(basename "$SESSION_FILE" .jsonl)
echo "Session ID: $SESSION_ID"
```

Store the UUID — this is your session's resume ID.

## Step 2: Gather Objective State

```bash
git branch --show-current
git status --short
```

## Step 3: Introspect and Summarize

YOU must introspect deeply on this conversation. Think about:
- What was the main task or feature being worked on?
- What specific decisions were made?
- What's done vs. still in progress?
- What was the VERY NEXT thing you were about to do?
- Which files matter most?

Be **specific** — a fresh Claude reading this needs enough context to continue seamlessly. Don't be generic ("working on frontend stuff"). Be precise ("building the drug candidate comparison table component in src/frontend/components/ComparisonTable.tsx, had just finished the sorting logic and was about to add the filter dropdown").

## Step 4: Write to Freeze File

Create or append to `.claude/frozen-sessions/sessions.md`.

If the file doesn't exist, create it with this header:
```markdown
# Frozen Sessions

Run `/thaw` in a fresh Claude session to get resume commands.

---
```

Then append an entry in this exact format:

```markdown
## [Short 2-4 Word Label]
- **Session ID**: `<uuid>`
- **Resume**: `claude --resume <uuid>`
- **Branch**: `<branch-name>`
- **What we were doing**: <1-3 sentences — be specific about the task, not vague>
- **Current status**: <what's done, what's in progress, any blockers>
- **Immediate next step**: <the very next concrete action to take>
- **Key files**: <most important files, comma-separated>
- **Frozen**: <YYYY-MM-DD HH:MM>
---
```

## Step 5: Confirm to User

Tell the user:
1. This session is frozen — show the resume command
2. They can safely close this terminal
3. Remind: run `/freeze` in remaining sessions before closing them
4. When ready to resume all sessions, start a fresh Claude and run `/thaw`
