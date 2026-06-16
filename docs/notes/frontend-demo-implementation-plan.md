# Frontend Demo Implementation Plan

## Context

The OSPF Ayurveda Knowledge Graph project has produced rich drug discovery analysis reports (markdown files with tables, scores, safety verdicts, ASCII visualizations). These reports exist only as raw markdown files and have no user-facing presentation layer. The goal is to build a prototype SPA that transforms these reports into an interactive, visually polished demo — making the project's findings accessible to researchers, stakeholders, and collaborators without requiring them to read raw markdown.

Three analysis documents exist today, with more expected in the same format. The frontend must handle them generically.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **React + TypeScript** | UI framework |
| **Vite** | Build system |
| **Shadcn/ui** | Component library (Radix UI + Tailwind CSS) |
| **Recharts** | Data visualization (React-native, 23k stars, covers bar/radar/heatmap) |
| **react-markdown + remark-gfm + rehype-raw + rehype-sanitize + rehype-highlight** | Markdown rendering pipeline |
| **PapaParse** | CSV parsing for drug candidates data |
| **npm** | Package manager |
| **ESLint + Prettier** | Code quality |
| **Jest + React Testing Library** | Testing |
| **Vercel** | Deployment |

### Why Recharts over alternatives
- React-native component API (not a wrapper around Canvas/D3)
- Built-in `ResponsiveContainer` for responsive charts
- Covers all chart types needed: bar, radar, heatmap-style custom, horizontal bar
- Most popular React charting lib (1.7M weekly npm downloads)
- Lighter than Nivo, more maintained than Victory

---

## Directory Structure

```
frontend-demo/
├── index.html
├── package.json
├── tsconfig.json, tsconfig.app.json, tsconfig.node.json
├── vite.config.ts
├── vercel.json
├── jest.config.ts
├── .eslintrc.cjs
├── .prettierrc
├── components.json                          # Shadcn config
│
├── public/
│   └── data/
│       └── analysis/                        # Analysis files served statically
│           ├── oral_mucositis_drug_candidates-2026-01-29.md
│           ├── oral_mucositis_drug_candidates-2026-05-03.md
│           ├── oral_mucositis_multi_agent_drug_discovery-2026-05-04.md
│           └── oral_mucositis_candidates.csv
│
├── src/
│   ├── main.tsx
│   ├── App.tsx                              # Root: tabs + state
│   ├── index.css                            # Tailwind directives + globals
│   │
│   ├── types/
│   │   ├── analysis.ts                      # AnalysisDocument, Section, TableData
│   │   └── drug-candidate.ts               # DrugCandidate (from CSV)
│   │
│   ├── lib/
│   │   ├── utils.ts                         # Shadcn cn() utility
│   │   ├── markdown-parser.ts               # Split MD into sections by H2
│   │   ├── table-extractor.ts               # Extract markdown tables → structured data
│   │   ├── markdown-preprocessor.ts         # Transform ═══, ████, safety verdicts, score bars
│   │   ├── analysis-registry.ts             # Registry of available analyses + metadata
│   │   └── csv-loader.ts                    # PapaParse wrapper
│   │
│   ├── hooks/
│   │   ├── use-analysis-document.ts         # Fetch + parse a single MD document
│   │   ├── use-drug-candidates.ts           # Fetch + parse the CSV
│   │   └── use-section-navigation.ts        # Track selected section
│   │
│   ├── components/
│   │   ├── ui/                              # Shadcn auto-generated (tabs, select, accordion, card, badge, table, scroll-area, separator)
│   │   │
│   │   ├── layout/
│   │   │   ├── AppHeader.tsx                # Title bar + project branding
│   │   │   ├── AnalysisToolbar.tsx          # Two dropdowns (analysis + section selectors)
│   │   │   └── PageShell.tsx                # Overall layout wrapper
│   │   │
│   │   ├── markdown/
│   │   │   ├── MarkdownRenderer.tsx         # react-markdown with custom component overrides
│   │   │   ├── CustomTable.tsx              # Styled table for markdown tables
│   │   │   ├── CustomCodeBlock.tsx          # Syntax-highlighted code blocks
│   │   │   ├── CustomHeading.tsx            # H1/H2/H3 with anchor links
│   │   │   ├── SafetyBadge.tsx              # GREEN/YELLOW/ORANGE/RED color badges
│   │   │   └── ScoreBar.tsx                 # Progress bar from ████░░ patterns
│   │   │
│   │   ├── visualization/
│   │   │   ├── DataTableViz.tsx             # Accordion wrapper: chart above, raw table below
│   │   │   ├── CompositeScoreChart.tsx      # Horizontal bar chart for consensus rankings
│   │   │   ├── PhaseCoverageHeatmap.tsx     # 5-phase × N-strategy coverage grid
│   │   │   ├── PropertyRadar.tsx            # Radar chart for MW/LogP/PSA/HBD/HBA
│   │   │   ├── SafetyVerdictGrid.tsx        # Color-coded candidate × verdict grid
│   │   │   └── TierBarChart.tsx             # Grouped bar for tiered candidates
│   │   │
│   │   ├── analysis/
│   │   │   ├── AnalysisView.tsx             # Main analysis tab: routes to correct sub-view
│   │   │   ├── SectionContent.tsx           # Renders one section with inline visualizations
│   │   │   ├── SummaryView.tsx              # Cross-analysis summary dashboard (default view)
│   │   │   └── AllOutputView.tsx            # Concatenated full document view
│   │   │
│   │   └── drug-candidates/
│   │       ├── DrugCandidatesView.tsx       # Drug candidates tab
│   │       ├── CandidateCard.tsx            # Individual drug card with properties + radar
│   │       └── CandidateList.tsx            # Filterable/sortable grid of cards
│   │
│   └── __tests__/
│       ├── markdown-parser.test.ts
│       ├── table-extractor.test.ts
│       ├── markdown-preprocessor.test.ts
│       └── App.test.tsx
```

---

## Data Architecture

### Loading Strategy: Fetch from `public/` at runtime

Analysis markdown files are copied into `public/data/analysis/` and fetched via `fetch('/data/analysis/filename.md')`. This keeps the JS bundle small and makes adding new analyses trivial (drop a file, add a registry entry).

### Data Flow

```
public/data/analysis/*.md  ──fetch()──>  raw markdown string
                                              │
                                     markdownParser.ts
                                     (split by H2 headers)
                                              │
                                     AnalysisDocument {
                                       title, date, metadata,
                                       sections: Section[]
                                     }
                                              │
                              ┌───────────────┴───────────────┐
                    MarkdownRenderer               DataTableViz
                    (preprocessor → react-markdown)   (Recharts chart + accordion)
```

### Analysis Registry

A TypeScript module that lists all available analyses:

```typescript
interface AnalysisEntry {
  id: string;
  label: string;           // Display name in dropdown
  filename: string | null; // null for generated views (summary, all-output)
  date: string | null;
  type: 'individual' | 'multi-agent' | 'summary' | 'conglomerate';
  description: string;
}
```

Entries:
1. `jan-29-candidates` → `oral_mucositis_drug_candidates-2026-01-29.md`
2. `may-03-comprehensive` → `oral_mucositis_drug_candidates-2026-05-03.md`
3. `may-04-multi-agent` → `oral_mucositis_multi_agent_drug_discovery-2026-05-04.md`
4. `summary` → (no file — hardcoded React component)
5. `all-output` → (concatenates all documents)

New analyses: add an `.md` file to `public/data/analysis/` and a new entry to the registry.

---

## Markdown Parsing & Preprocessing

### Section Splitting (`markdown-parser.ts`)

Split documents by `## ` (H2) headers. Each H2-to-next-H2 block becomes a `Section` with:
- `id` (slugified title), `title` (raw H2 text), `content` (raw markdown), `tables` (extracted `TableData[]`)

Content before the first H2 becomes a "preamble" section.

Must handle both document styles:
- Numbered: `## 1. The Oral/Mucosal Drug Fingerprint`
- Uppercase: `## EXECUTIVE SUMMARY`

### Preprocessing Pipeline (`markdown-preprocessor.ts`)

Follows the conventions from the existing `frontend-developer` SKILL.md. The pipeline runs before `react-markdown`:

```
raw markdown
  → preprocessSkillOutput()       // ═══ → <hr>, ━━━ → <hr>, box-drawing → GFM
  → renderScoreBars()             // ████████░░  8/10 → styled HTML progress bars
  → renderCoverageIndicators()    // ██ → green span, ░░ → gray span
  → wrapSafetyVerdicts()          // GREEN/RED/YELLOW/ORANGE → colored badge spans
  → processed markdown (passed to react-markdown with rehype-raw)
```

### Table Extraction (`table-extractor.ts`)

For each section, extract pipe-delimited markdown tables into `TableData` objects:
- Parse headers, detect numeric columns (>50% of values are numbers)
- Skip the Expert Agreement Map (space-aligned, not pipe-delimited — render as monospace code block)

---

## Component Architecture

### App State (React built-in — no external state library needed)

```typescript
const [selectedAnalysis, setSelectedAnalysis] = useState<string>('summary');
const [selectedSection, setSelectedSection] = useState<string | null>(null);
const [activeTab, setActiveTab] = useState<'analysis' | 'candidates'>('analysis');
```

### Tab 1: Analysis View

**AnalysisToolbar**: Two Shadcn `Select` dropdowns side by side.
- Dropdown 1: Analysis selector (from registry). Default: "Summary".
- Dropdown 2: Section selector (populated from document's H2 headers). **Disabled** when "Summary" or "All Output" is selected.

**Content routing**:
- `summary` → `SummaryView` (hardcoded dashboard with key findings, top candidates, charts)
- `all-output` → `AllOutputView` (all documents concatenated with separators)
- Any individual analysis + section → `SectionContent` (renders that section with inline `DataTableViz`)

### Tab 2: Drug Candidates

**DrugCandidatesView**: Loads the CSV via PapaParse, displays `CandidateCard` components in a filterable grid.

Each card shows: drug name, ChemBL ID, MW/LogP/PSA/HBD/HBA, natural product flag, current indications, safety verdict badge (cross-referenced from multi-agent report Appendix C), and a mini radar chart of molecular properties.

---

## Data Visualization Details

### Inline Chart + Accordion Pattern (`DataTableViz`)

When a section contains a table with numeric data:
1. Render a Recharts visualization above the table (chart type selected by heuristic)
2. Raw data table shown in a Shadcn `Accordion` below (collapsed by default)
3. If no numeric data, show only the styled table (no chart, no accordion)

### Chart Type Heuristic

```typescript
function selectChartType(table: TableData): 'bar' | 'radar' | 'horizontal-bar' {
  if (table.numericColumns.length >= 3 && hasEntityColumn(table)) return 'radar';
  if (table.numericColumns.some(col => col.includes('Score') || col.includes('Rank'))) return 'horizontal-bar';
  return 'bar';
}
```

### Planned Visualizations

| Chart Component | Data Source | Sections |
|-----------------|------------|----------|
| `CompositeScoreChart` | Consensus ranking (scores 56-72) | Summary, Consensus Ranking |
| `PropertyRadar` | MW/LogP/PSA/HBD/HBA per drug | Drug Candidate cards, Fingerprint sections |
| `PhaseCoverageHeatmap` | 5-phase x 3-strategy matrix | Summary, Phase Coverage section |
| `SafetyVerdictGrid` | Appendix C safety verdicts | Summary, Safety section |
| `TierBarChart` | Tier 1/2/3 candidate properties | Repurposing Candidates sections |

---

## Summary View (Default Landing Page)

`SummaryView.tsx` is a curated React dashboard — NOT a rendered markdown file. It:

1. Hardcodes extracted key findings from all three analyses' executive summaries
2. Shows a `CompositeScoreChart` with the 8 consensus-ranked candidates
3. Shows a `PhaseCoverageHeatmap` for the recommended combination strategies
4. Shows a `SafetyVerdictGrid` with color-coded verdicts
5. Lists top candidates as cards with one-line rationale each
6. Provides links to jump to specific sections of specific analyses for deeper reading

This avoids complex cross-document NLP — the data is hardcoded since the content is stable and pre-generated.

---

## Key Files to Reuse

| Existing Resource | Path | How Used |
|-------------------|------|----------|
| Frontend developer skill | `.claude/skills/frontend-developer/SKILL.md` | Preprocessing pipeline patterns, custom component overrides, design guidelines (colors, typography), rendering pipeline architecture |
| Analysis file 1 | `data/analysis/oral_mucositis_drug_candidates-2026-01-29.md` | Simplest document — test rendering first |
| Analysis file 2 | `data/analysis/oral_mucositis_drug_candidates-2026-05-03.md` | Largest document (543 lines, 7 major tables) |
| Analysis file 3 | `data/analysis/oral_mucositis_multi_agent_drug_discovery-2026-05-04.md` | Most complex rendering (box-drawing, ASCII maps, safety verdicts, phase coverage) |
| Candidates CSV | `data/analysis/oral_mucositis_candidates.csv` | Drug Candidates tab data (131 rows) |

---

## Implementation Phases

### Phase 1: Foundation (~1-2 hours)
1. Create `frontend-demo/` and scaffold with `npm create vite@latest . -- --template react-ts`
2. Initialize Shadcn/ui (Tailwind CSS v4 + Radix)
3. Install Shadcn components: `tabs`, `select`, `accordion`, `card`, `badge`, `table`, `scroll-area`, `separator`
4. Install: `recharts`, `react-markdown`, `remark-gfm`, `rehype-raw`, `rehype-sanitize`, `rehype-highlight`, `papaparse`
5. Copy analysis files into `public/data/analysis/`
6. Set up path aliases (`@/`), ESLint, Prettier
7. Create `PageShell`, `AppHeader`, basic two-tab layout with Shadcn Tabs
8. Configure Jest + React Testing Library

### Phase 2: Markdown Rendering Engine (~2-3 hours)
9. Build `markdown-parser.ts` (H2 section splitting)
10. Build `markdown-preprocessor.ts` (box-drawing, score bars, safety verdicts, coverage indicators)
11. Build `MarkdownRenderer.tsx` with custom components (table, heading, code, blockquote, list)
12. Build `SafetyBadge.tsx` and `ScoreBar.tsx`
13. Write unit tests for parser and preprocessor
14. Verify rendering with the Jan 29 file first, then all three

### Phase 3: Navigation & Analysis Tab (~2-3 hours)
15. Build `analysis-registry.ts`
16. Build `AnalysisToolbar.tsx` (two Shadcn Select dropdowns)
17. Build `use-analysis-document.ts` hook (fetch + parse + memoize)
18. Build `SectionContent.tsx`
19. Wire toolbar selections to content display
20. Test: switching between all 3 documents, navigating between sections

### Phase 4: Data Visualization (~2-3 hours)
21. Build `table-extractor.ts` (parse tables, detect numeric columns)
22. Build `DataTableViz.tsx` (chart + accordion pattern)
23. Build `CompositeScoreChart.tsx`, `PropertyRadar.tsx`, `PhaseCoverageHeatmap.tsx`, `SafetyVerdictGrid.tsx`, `TierBarChart.tsx`
24. Wire charts into `SectionContent` for sections with numeric tables

### Phase 5: Summary & Special Views (~1-2 hours)
25. Build `SummaryView.tsx` (hardcoded cross-analysis dashboard with charts)
26. Build `AllOutputView.tsx` (concatenated documents with separators)
27. Wire into analysis selector; ensure summary is default; section dropdown disabled for summary/all-output

### Phase 6: Drug Candidates Tab (~1-2 hours)
28. Build `csv-loader.ts` + `use-drug-candidates.ts`
29. Build `CandidateCard.tsx` with property display + mini radar chart
30. Build `CandidateList.tsx` (scrollable, filterable grid)
31. Build `DrugCandidatesView.tsx`

### Phase 7: Polish & Deploy (~1-2 hours)
32. Responsive design adjustments
33. Loading states, error boundaries
34. Run full test suite
35. Add `vercel.json` with SPA rewrites
36. Deploy to Vercel
37. Visual review of all documents and edge cases

---

## Vercel Deployment

### `vercel.json`
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": "vite",
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

### Deployment steps
1. Push `frontend-demo/` to the repo
2. Connect repo to Vercel, set root directory to `frontend-demo/`
3. Vercel auto-detects Vite, runs `npm run build`, serves from `dist/`
4. SPA rewrite rule ensures client-side routing works
5. Static files in `public/data/analysis/` are served automatically by Vercel's edge network

---

## Testing Strategy

### Unit Tests (pure logic, no DOM)
- `markdown-parser.test.ts` — section count, titles, preamble handling, both numbered and unnumbered H2 styles
- `table-extractor.test.ts` — table parsing, numeric column detection, skip non-pipe-delimited tables
- `markdown-preprocessor.test.ts` — each transform (box-drawing, coverage blocks, safety badges), regression: valid markdown not corrupted

### Integration Tests (React Testing Library)
- `App.test.tsx` — renders without crash, both tabs present, default shows summary, section dropdown disabled initially

### Visual verification
- After each phase, start dev server and verify in browser
- Check all three documents render correctly
- Verify charts appear for numeric tables
- Test dropdown interactions (switching analyses, switching sections, summary disabling section dropdown)

---

## Potential Challenges & Mitigations

| Challenge | Mitigation |
|-----------|------------|
| Expert Agreement Map (space-aligned, not pipe-delimited) | Detect as non-table; render in monospace `<pre>` block |
| Block characters inside pipe-delimited tables | Preprocessor runs BEFORE react-markdown, replaces with `<span>` HTML |
| Composite scores in H3 headers (`### #1: DRUG -- Score: 72/100`) | `CustomHeading` parses score text and renders a visual badge |
| CSV indications field (semicolons, trailing spaces) | Split on `; `, filter empties in csv-loader |
| Adding future analyses | Drop `.md` in `public/data/analysis/`, add entry to registry — no code changes needed |
| Sanitization vs raw HTML from preprocessor | Configure `rehype-sanitize` with custom schema allowing `className`, `style`, `title` on `span`/`div` |
