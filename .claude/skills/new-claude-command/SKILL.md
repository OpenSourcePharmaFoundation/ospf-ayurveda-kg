---
name: new-claude-command
description: Create a new Claude skill for this project
when_to_use: When creating a new Claude Code skill or command file for this project
allowed-tools: Bash(ls *) Bash(find *) Read
---

First, reread the following files to ensure you understand the project context and this skill creation process:
1. The CLAUDE.md file at the root of the project
2. This skill file itself (`.claude/skills/new-claude-command/SKILL.md`)

Now, create a new Claude skill in the `.claude/skills/` directory.

The skill should:
1. Be a directory named with kebab-case containing a `SKILL.md` file
2. Include appropriate YAML frontmatter with name, description, when_to_use, and allowed-tools
3. Contain clear instructions for Claude to follow when the skill is invoked
4. Follow the project's guidelines and conventions from CLAUDE.md
5. Include a note at the beginning to re-read the CLAUDE.md file and the skill file itself for context

Frontmatter fields to include:
- `name` — kebab-case skill name
- `description` — what the skill does (shown in skill list)
- `when_to_use` — additional context for when Claude should auto-invoke this skill
- `allowed-tools` — which tools the skill needs (e.g., `Bash(git *) Read`)

After creating the skill, briefly explain what the new skill does and how to use it.

---

Use the text that follows this command as the description of the skill to create.
