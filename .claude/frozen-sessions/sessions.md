# Frozen Sessions

Run `/thaw` in a fresh Claude session to get resume commands.

---

## KG Node Extraction & Import
- **Session ID**: `2233b000-c0eb-4ba0-8cda-6c754d2d6285`
- **Resume**: `claude --resume 2233b000-c0eb-4ba0-8cda-6c754d2d6285`
  - OR: claude --resume "graph-exploration-query-expansion"
- **Branch**: `frontend-prototype-demo`
- **What we were doing**: Completed step 4 of todo.md — extracted 7 new node types (Enzyme, Metabolite, Indication, MoleculeType, ActionType, TargetType, Organism) from existing drug properties into the Neo4j knowledge graph. Also did a full clean reimport of all data (scripts 1-8), fixed the IMPPAT APOC import by bypassing it with the Python neo4j driver, and restored 2,328 Indication nodes from the indication_class field. Wrote 25 exploration queries in exploration_queries.txt.
- **Current status**: Step 4 is done and committed. Neo4j database is fully populated with 25,899 nodes across 19 labels and 129,862 relationships. APOC file import is still broken (apoc.conf setting not being read despite being in neo4j.conf) — worked around with Python driver. The ChemBL mechanisms, targets, warnings, and bioactivities CSVs are still test data (10, 49, 9, and 23 records respectively) — need full scrape to populate. The bridge query (Ayurvedic compounds meeting drug targets) returns empty because of the limited mechanism/target data.
- **Immediate next step**: Step 5 in todo.md — more complex frontend (drug candidate drawer, dashboard tab, network graph visualizer). Or alternatively, run the full ChemBL scrape for mechanisms/targets/warnings to fill the data gaps that make the bridge query work.
- **Key files**: `docs/todos/todo.md`, `scripts/cypher_scripts/exploration_queries.txt`, `scripts/cypher_scripts/10_extract_new_node_types.txt`, `scripts/import_metabolism.py`, `scripts/setup_neo4j.py`
- **Frozen**: 2026-05-21 17:00
---

## Frontend Improvements Todo List
- **Session ID**: `b6f89e9d-a903-40f2-9041-fb556cb33b01`
- **Resume**: `claude --resume b6f89e9d-a903-40f2-9041-fb556cb33b01`
  - OR: claude --resume "frontend-improvements-audit"
- **Branch**: `frontend-prototype-demo`
- **What we were doing**: Added a "Frontend Prototype Improvements" section to `docs/todos/todo.md` based on a thorough audit of every source file in `frontend-demo/src/`. The audit found 3 bugs, 4 missing visualization components, 5 markdown components inlined rather than modular, zero test coverage, and several UX/performance gaps. First attempt was too broad (rewrote the whole top of todo.md with all project next steps) — user asked to revert and focus specifically on frontend improvements, which we did.
- **Current status**: Done. The improvements list is committed-ready in `docs/todos/todo.md` (27 items across 7 categories: missing visualizations, markdown components, Drug Candidates tab, bugs, UX, performance, tests). No other files were changed.
- **Immediate next step**: User may want to start tackling items from the list — most impactful would be the 3 bugs (quick wins) or the PropertyRadar visualization component (highest visual impact).
- **Key files**: `docs/todos/todo.md`, `frontend-demo/src/components/visualization/DataTableViz.tsx`, `frontend-demo/src/components/markdown/MarkdownRenderer.tsx`, `frontend-demo/src/lib/csv-loader.ts`, `frontend-demo/src/components/drug-candidates/CandidateCard.tsx`
- **Frozen**: 2026-05-21 17:15
---

## Bioinformatics Database Catalog
- **Session ID**: `a37b9733-fb3c-4f18-8908-50a63dd1eb59`
- **Resume**: `claude --resume a37b9733-fb3c-4f18-8908-50a63dd1eb59`
  - OR: claude --resume "bioinformatics-database-catalog"
- **Branch**: `frontend-prototype-demo`
- **What we were doing**: Researched and wrote a comprehensive 545-line catalog of 33 drug/biomedical databases for expanding the knowledge graph. Explored existing scraper architecture (ChemBL, PubChem, DisGeNET, IMPPAT, MedPlant patterns), researched each database's API/download methods, authentication requirements, and data formats, then wrote the full catalog document.
- **Current status**: Done. The catalog is written at `docs/databases/drug-database-catalog.md` — covers 33 databases across 9 categories with access methods, formats, OM relevance, and integration approach for each. Includes 3-tier priority ranking and a suggested parallel build order for new scrapers. The file is uncommitted.
- **Immediate next step**: Commit the catalog, then begin building scrapers for Tier 1 databases (STRING + Reactome first, then ClinicalTrials.gov + SIDER). Each scraper follows the pattern in `src/scrapers/{name}/{name}_scraper.py`.
- **Key files**: `docs/databases/drug-database-catalog.md`, `src/scrapers/chembl/chembl_scraper.py` (reference pattern), `src/utils/escape_csv_field.py`, `docs/next-steps/bridging-the-gap.md`
- **Frozen**: 2026-05-21 17:30
---

## Frontend Demo Build Session
- **Session ID**: `22856b28-7a16-4aa7-a308-5d795c87d7f0`
- **Resume**: `claude --resume 22856b28-7a16-4aa7-a308-5d795c87d7f0`
  - OR: claude --resume "drug-analysis-dashboard"
- **Branch**: `frontend-prototype-demo`
- **What we were doing**: Built the complete frontend-demo SPA from scratch based on a detailed implementation plan. Read all 3 analysis markdown files, designed the architecture (plan at `docs/notes/frontend-demo-implementation-plan.md`), then scaffolded Vite+React+TypeScript+Shadcn v4 and implemented all 34 source files: markdown parser, preprocessor pipeline (box-drawing/score bars/safety verdicts/coverage blocks), analysis registry, section-based navigation with 2 dropdowns, Summary dashboard with CompositeScoreChart, All Output concatenated view, Drug Candidates tab with CSV parsing and search/filter, and teal/science color theme.
- **Current status**: Phase 1-6 of 7-phase plan complete. All code compiles cleanly (`npm run build` passes). Frontend-demo directory is committed on `frontend-prototype-demo` branch. Shadcn v4 uses `@base-ui/react` (not Radix) — required API adjustments for Select `onValueChange` signature and Accordion (no `type` prop). Had to work around TS 7 deprecation of `baseUrl`/`paths` with `ignoreDeprecations: "6.0"`. Shadcn init created components in a literal `@/` directory — manually moved to `src/components/ui/`.
- **Immediate next step**: Phase 7 — visual verification in browser (attempted but user denied browser nav permission), responsive design polish, Jest/RTL test setup and unit tests for markdown-parser/table-extractor/preprocessor, then Vercel deployment. A prior session (`b6f89e9d`) already audited the frontend and wrote 27 improvement items to `docs/todos/todo.md`.
- **Key files**: `frontend-demo/src/App.tsx`, `frontend-demo/src/lib/markdown-parser.ts`, `frontend-demo/src/lib/markdown-preprocessor.ts`, `frontend-demo/src/lib/table-extractor.ts`, `frontend-demo/src/components/analysis/AnalysisView.tsx`, `frontend-demo/src/components/analysis/SummaryView.tsx`, `frontend-demo/src/components/visualization/CompositeScoreChart.tsx`, `frontend-demo/src/components/drug-candidates/DrugCandidatesView.tsx`, `docs/notes/frontend-demo-implementation-plan.md`
- **Frozen**: 2026-05-21 21:55
---
