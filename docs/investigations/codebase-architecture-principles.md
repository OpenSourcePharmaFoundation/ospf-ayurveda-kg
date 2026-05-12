# Codebase Architecture Principles for Python Data Pipelines

> Investigation document — general principles not tied to any specific project.
> Created: 2026-04-08

---

## 1. Vertical Slice Architecture for Data Projects

Traditional horizontal layering organizes code by technical concern:

```
# Horizontal (anti-pattern for data projects)
scrapers/          # ALL scrapers flat in one directory
validators/        # ALL validators flat in one directory
transformers/      # ALL transformers flat in one directory
```

Vertical slice architecture organizes by **domain feature** instead:

```
# Vertical (preferred)
src/
├── scrapers/
│   ├── source_a/      # Everything for Source A: scraping, parsing, validation
│   ├── source_b/      # Everything for Source B: self-contained
│   └── source_c/      # Each slice is independent
├── analysis/           # Cross-cutting analysis that consumes processed data
└── utils/              # Genuinely shared utilities
```

### Why Vertical Slices Work Better for Data Pipelines

- **Independence**: Each data source has unique APIs, rate limits, schemas, and failure modes. Grouping by source keeps related complexity together.
- **Deployability**: You can run, test, or debug one source without touching others.
- **Onboarding**: A new contributor can understand one slice without learning the whole system.
- **Deletion**: When a data source is deprecated, you delete one directory — no hunting across layers.

### The Key Test

Ask: "If I removed this data source entirely, how many directories would I touch?" In a good vertical architecture, the answer is **one** (plus maybe removing a line from an integration module).

---

## 2. The Module-per-Feature Pattern

Each vertical slice should be a proper Python package:

```
src/scrapers/source_a/
├── __init__.py              # Makes it an importable package
├── source_a_scraper.py      # Main entry point (directly executable)
├── parser.py                # Optional: parsing logic if complex
└── README.md                # Optional: source-specific notes
```

### Key Characteristics

1. **`__init__.py` is mandatory** — Without it, the directory is just a folder, not a package. Other modules can't import from it, and tools like pytest can't discover it.
2. **Main entry point is directly executable** — `python src/scrapers/source_a/source_a_scraper.py --test` should work. This means including `if __name__ == "__main__":` with argument parsing.
3. **Self-contained** — All logic specific to this source lives here. Don't scatter source-specific parsing across shared utilities.
4. **Outputs to a shared location** — Typically `data/processed/` or `data/raw/`. The module produces files; downstream consumers read from the shared data directory, not from the module itself.

### When a Module Gets Complex

If a scraper needs multiple files (e.g., separate API client, data transformer, validator), keep them in the same module directory. The module boundary is the **data source**, not the technical concern:

```
src/scrapers/complex_source/
├── __init__.py
├── complex_source_scraper.py   # Orchestrator / entry point
├── api_client.py               # API interaction logic
├── transformer.py              # Raw -> processed data transformation
└── validator.py                # Source-specific validation rules
```

This is still one vertical slice — it just has internal structure.

---

## 3. Directory Taxonomy for Python Data Pipelines

A well-organized data pipeline project uses these top-level directories:

```
project/
├── src/              # Importable production code (the pipeline)
├── scripts/          # CLI tools, setup scripts, operational glue
├── tests/            # Mirrors src/ structure
├── data/             # Data at various stages of processing
├── docs/             # Documentation organized by purpose
├── .claude/          # AI tooling configuration (if applicable)
└── [config files]    # requirements.txt, pyproject.toml, Makefile, etc.
```

### `src/` — Production Code

Everything that IS the data pipeline. Importable, testable, version-controlled.

| Subdirectory | Purpose | Example |
|-------------|---------|---------|
| `scrapers/` | Data collection from external sources | One subpackage per source |
| `analysis/` | Insights, scoring, validation of processed data | candidate_scorer.py |
| `integration/` | Cross-source data linking and mapping | source_a_source_b_mapper.py |
| `utils/` | Genuinely shared utilities (used by 2+ modules) | csv_escaping.py |
| `reporting/` | Formatted output generation | report_generator.py |

### `scripts/` — Operational Tooling

Things humans run but that aren't part of the pipeline itself.

- **CLI tools**: Data display utilities, inspection tools
- **Setup scripts**: Environment configuration, database preparation
- **Import scripts**: Database-specific import commands (e.g., Cypher/SQL)
- **NOT scrapers, analyzers, or data processors** — those belong in `src/`

### `tests/` — Mirrors `src/`

```
tests/
├── scrapers/
│   ├── test_source_a.py
│   └── test_source_b.py
├── analysis/
│   └── test_candidate_scorer.py
└── conftest.py
```

### `data/` — Processing Tiers

| Tier | Mutability | Purpose |
|------|-----------|---------|
| `raw/` | Immutable | Original fetched data, never modified |
| `interim/` | Temporary | Intermediate processing artifacts |
| `processed/` | Stable | Clean, validated, ready for downstream use |
| `analysis/` | Generated | Analysis output (reports, candidate lists) |

### `docs/` — Organized by Purpose

| Subdirectory | Content Type | Lifecycle |
|-------------|-------------|-----------|
| `databases/` | Source-specific reference docs | Updated when source APIs change |
| `setup/` | Installation and configuration guides | Updated when environment changes |
| `notes/` | Research notes, implementation plans | Living documents, may become stale |
| `investigations/` | Architectural decisions, option analyses | Written once, referenced long-term |
| `next-steps/` | Roadmaps, gap analyses | Updated as work progresses |
| `todos/` | Task tracking | Frequently updated |

---

## 4. Dependency Direction Rules

```
ALLOWED DEPENDENCY FLOW:

    utils/          (depended on by everything)
      ^
      |
  scrapers/*        (independent of each other, may use utils)
      ^
      |
  integration/      (bridges between scraper outputs)
      ^
      |
  analysis/         (consumes processed data, may use utils)
      ^
      |
  reporting/        (formats analysis output)
```

### The Rules

1. **Dependencies flow inward** — toward shared utilities, never sideways between peer modules.
2. **Scrapers NEVER import from each other** — If two scrapers need the same logic, extract it to `utils/`.
3. **Integration modules bridge outputs, not internals** — They read from `data/processed/`, not by importing scraper code.
4. **Analysis consumes data files, not scraper logic** — Analyzers read CSVs/JSONs from `data/`, not by calling scraper functions.
5. **`utils/` stays lean** — Only code used by 2+ modules belongs here. One user = keep it in that module.

### Why This Matters

Sideways dependencies create cascading breakage. If Scraper A imports from Scraper B, and Scraper B's API changes format, Scraper A breaks for reasons having nothing to do with its own data source. Independent scrapers can be developed, tested, and maintained in isolation.

---

## 5. Migration Playbook: Scattered to Structured

When inheriting a codebase where scripts, processors, and tools are mixed together in flat directories:

### Step 1: Audit and Categorize

For every file in the scattered directory, answer:
- Is this **production pipeline code** (scraper, analyzer, processor)? -> `src/`
- Is this a **standalone CLI tool** for humans? -> `scripts/`
- Is this **deprecated or superseded**? -> Delete or archive
- Is this a **stray file** (wrong type, unclear purpose)? -> Investigate, then delete or relocate

### Step 2: Group by Feature

Cluster related files by their data source or domain:
- All DisGeNET-related files -> one migration batch
- All IMPPAT-related files -> one migration batch
- Each batch becomes one vertical slice

### Step 3: Migrate One Batch at a Time

For each batch:
1. Create the target module directory with `__init__.py`
2. Copy (don't move yet) the main script into the module
3. **Adapt to the module pattern**: Add CLI argument parsing, standardize output paths, fix imports
4. Verify the output is identical to the original (CSV diff, record counts)
5. Update any downstream consumers that reference the old path
6. Delete the original only after verification

### Step 4: Clean Up

- Remove empty directories left behind
- Delete `__pycache__` directories from old locations
- Update documentation references to new paths
- Add the old location to a "deprecated" note if other tooling referenced it

### Critical Rule

**Migration is not just moving files.** Adapting to the module pattern (adding `__init__.py`, CLI args, proper imports, standardized output paths) is the actual work. A file moved without adaptation is still technical debt — it's just in a different directory.

---

## 6. When to Create a New Module vs. Extend

### Create a new top-level module under `src/` when:

- It represents a **genuinely new domain area** (e.g., LLM integration, reporting)
- It has its **own data sources and outputs** distinct from existing modules
- It could theoretically be **extracted into its own project**
- Existing modules would become incoherent if it were shoehorned in

### Extend an existing module when:

- The new functionality is a natural extension of an existing feature
- It shares data sources, schemas, or output formats with an existing module
- Creating a new module would result in a directory with only 1-2 small files
- The new code would immediately need tight coupling to the existing module

### The "Regret Test"

Ask: "In 6 months, will I regret that this is a separate module (because it's too fragmented) or that it's inside an existing module (because it doesn't belong there)?" Err on the side of fewer modules — you can always split later, but merging is harder.

---

## 7. Documentation Organization Principles

### The Four Types of Documentation

| Type | Question It Answers | Location | Update Frequency |
|------|-------------------|----------|-----------------|
| **Reference** | "How does this work?" | `docs/databases/`, `docs/setup/` | When things change |
| **Planning** | "What should we build next?" | `docs/next-steps/` | As work progresses |
| **Investigation** | "Why did we choose this approach?" | `docs/investigations/` | Written once |
| **Operational** | "What's the status?" | `docs/todos/`, `docs/cleanup/` | Continuously |

### Rules for Documentation Placement

1. **Docs about a specific data source** -> `docs/databases/<source>/`
2. **Docs about how to set up the environment** -> `docs/setup/`
3. **Docs about architectural decisions or research** -> `docs/investigations/`
4. **Docs about what to build next** -> `docs/next-steps/`
5. **Task tracking** -> `docs/todos/`
6. **Session/activity records** -> `docs/cleanup/` or `docs/notes/`
7. **In-progress research not yet categorized** -> `docs/notes/` (acceptable as a staging area)

### Anti-Pattern: Docs at the Root

Files directly in `docs/` (not in a subdirectory) tend to be orphans — unclear purpose, unclear audience. Every doc should live in a subdirectory that signals its type.

Exception: `docs/PROJECT-GOALS.md` or similar project-level documents that genuinely span all categories.

---

## 8. Anti-Patterns to Watch For

### Flat Script Dump
**Symptom**: 15+ Python files in a single flat directory, each processing a different data source.
**Fix**: Extract into vertical slices under `src/scrapers/`.

### God-Util File
**Symptom**: A `utils.py` file that's 500+ lines and imported by everything.
**Fix**: Split into focused utility modules. If a utility is only used by one module, move it into that module.

### Import Cycles
**Symptom**: Module A imports from Module B which imports from Module A.
**Fix**: Extract the shared dependency into `utils/` or restructure to depend on data files instead of code imports.

### Premature Abstraction
**Symptom**: A `BaseScraperClass` with 5 abstract methods, used by exactly one concrete scraper.
**Fix**: Delete the abstraction. Write concrete code. Abstract only when you have 3+ concrete implementations that genuinely share structure.

### Orphaned Prototypes
**Symptom**: Files named `test_*.py`, `old_*.py`, `*_backup.py` scattered in production directories.
**Fix**: Delete them. If they have historical value, they're in git history. If they're actual tests, move to `tests/`.

### Documentation Sprawl
**Symptom**: 10 markdown files at the root of `docs/` with no subdirectory organization.
**Fix**: Categorize by type (reference, planning, investigation, operational) and move to appropriate subdirectories.
