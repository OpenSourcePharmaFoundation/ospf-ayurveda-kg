---
name: tag-release
description: Create annotated milestone or data tags with changelog
when_to_use: When creating git tags for version milestones, data collection events, or release tagging
allowed-tools: Bash(git tag:*), Bash(git log:*), Bash(git rev-parse:*), Bash(git status:*), Bash(git push:*), Bash(git describe:*), Bash(git diff:*), Bash(git show:*)
---

First, reread the following files:
1. The CLAUDE.md file at the project root
2. This skill file itself (`.claude/skills/tag-release/SKILL.md`)

## Purpose

Create annotated git tags for project milestones and data collection events. This project uses two tag namespaces:

### Version Tags (Semantic Versioning)
```
v<major>.<minor>.<patch>

v0.1.0  — Initial data pipeline working (all scrapers functional)
v0.2.0  — Full ChemBL integration (secondary datasets complete)
v0.3.0  — Cross-database integration (ChemBL-IMPPAT mapping at scale)
v0.4.0  — Analysis layer (candidate scoring, ranking)
v0.5.0  — RAG system operational
v1.0.0  — End-to-end pipeline producing research-grade output
```

### Data Tags (Collection Milestones)
```
data/chembl-full-<YYYY-MM-DD>        — After a full ChemBL collection run
data/neo4j-import-<YYYY-MM-DD>       — After a successful full graph import
analysis/candidates-v<N>             — When candidate list is regenerated
```

## Instructions

### Step 1: Assess Current State

```bash
# List existing tags (most recent first)
git tag -l --sort=-creatordate

# If tags exist, show what's changed since the last one
git describe --tags --abbrev=0 2>/dev/null  # most recent tag
# Then: git log <last-tag>..HEAD --oneline
```

### Step 2: Determine Tag Type

Based on the user's input after the command, or by asking:

**If the user specifies a version (e.g., `v0.1.0`):**
- Use that version directly
- Validate it follows semver and is greater than any existing version tag

**If the user says "data" or specifies a data tag:**
- Use the appropriate data tag format with today's date
- e.g., `data/chembl-full-2026-04-06`

**If the user doesn't specify:**
1. Check existing tags
2. If no tags exist, suggest `v0.1.0` as the initial milestone (or a data tag if this is a data collection event)
3. If tags exist, analyze changes since the last tag and suggest the appropriate version bump:
   - **Major**: Breaking changes to data schema, pipeline redesign
   - **Minor**: New scrapers, new analysis capabilities, new data sources integrated
   - **Patch**: Bug fixes, documentation, small improvements

### Step 3: Generate Tag Message

For **version tags**, create an annotated tag with a changelog:

```
v0.X.Y — <one-line summary>

Changes since <previous-tag-or-initial>:
- <category>: <description>
- <category>: <description>
...

Data status:
- ChemBL approved drugs: <count> (full/test)
- ChemBL secondary datasets: <status>
- Neo4j graph: <node/relationship counts if known>
- Scrapers migrated: <list>
```

For **data tags**, create a shorter annotation:

```
data/<type>-<date>

Collection details:
- Dataset: <name>
- Records collected: <count>
- Duration: <if known>
- Mode: full/test/incremental
```

### Step 4: Present and Confirm

Show the user:
1. The proposed tag name
2. The full annotation message
3. Which commit it will point to (HEAD, or a specific commit if they specify one)

Ask for confirmation before creating.

### Step 5: Create the Tag

```bash
# Annotated tag (always use -a for this project)
git tag -a <tag-name> -m "<annotation message>"
```

After creating, show the tag details:
```bash
git show <tag-name>
```

### Step 6: Push (Only If Asked)

Do NOT automatically push tags to remote. Ask:
> "Tag created locally. Push to remote with `git push origin <tag-name>`?"

Only push if the user confirms. To push all tags: `git push origin --tags`

### Important Rules

- **Always use annotated tags** (`-a`) — never lightweight tags. Annotated tags store the tagger, date, and message.
- **Never overwrite existing tags** — if a tag name conflicts, inform the user and suggest an alternative
- **Never push without confirmation** — tags are hard to undo on remote
- **Follow the project's two tag namespaces** — don't invent new formats
- **No Claude attribution** in tag messages (project rule)

---

Process any arguments passed after the command (tag name, version number, or "data"):
