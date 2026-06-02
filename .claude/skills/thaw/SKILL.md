---
name: thaw
description: List frozen sessions and provide resume commands for all panels
when_to_use: When returning to resume previously frozen sessions
allowed-tools: Read, Bash(ls:*), Bash(cat:*), Bash(wc:*), Bash(mv:*)
---

# Thaw Frozen Sessions

Help the user resume all their previously frozen sessions.

## Step 1: Read Frozen Sessions

Read `.claude/frozen-sessions/sessions.md`. If it doesn't exist, tell the user:
> No frozen sessions found. Run `/freeze` in active sessions before closing them.

## Step 2: Present Resume Plan

Show all frozen sessions in a clear, actionable format. For each session, present it as a panel the user should open:

```
Welcome back! You have N frozen sessions ready to resume:

┌──────────────────────────────────────────────────────────────────┐
│ Panel 1: [Label]                                                 │
│ Branch: [branch]                                                 │
│ Status: [current status]                                         │
│ Next step: [what to do first]                                    │
│                                                                  │
│   claude --resume [uuid]                                         │
├──────────────────────────────────────────────────────────────────┤
│ Panel 2: [Label]                                                 │
│ ...                                                              │
└──────────────────────────────────────────────────────────────────┘
```

## Step 3: Quick-Start Block

After the detailed view, also give a plain copy-paste block:

```
# Quick resume — run each in a separate terminal panel:
claude --resume <uuid1>
claude --resume <uuid2>
claude --resume <uuid3>
claude --resume <uuid4>
```

## Step 4: Offer Cleanup

Ask if the user wants to archive the freeze file (move to `.claude/frozen-sessions/archive/sessions-YYYY-MM-DD.md`) so it's clean for next time.

If the user says yes, move the file. If no, leave it.
