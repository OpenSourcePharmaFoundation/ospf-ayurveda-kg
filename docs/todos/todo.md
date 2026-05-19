TODO - next steps
=================
2026-05-04
----------
[x] Evaluate the output of the analysis
[x] Build the basic frontend (call it a "prototype")
[x] Create data visualization agent

4. [x] Add more data to the knowledge graph - that is, more nodes
    [x] Make a list of all possible nodes that can be made by extracting properties from drugs
    [x] Make these nodes
    New node types created (script: 10_extract_new_node_types.txt):
      - Indication (2,328) — extracted from Drug.indication_class
      - Metabolite (591) — from chembl_drug_metabolism.csv
      - Enzyme (90) — from chembl_drug_metabolism.csv
      - Organism (24) — from Target.organism
      - TargetType (7) — from Target.target_type
      - ActionType (3) — from Mechanism.action_type
      - MoleculeType (1) — from Drug.molecule_type
    Skipped (no data available): MolecularSpecies, WithdrawalEvent (reasons empty), BindingSite (test data)

5. [ ] More complex frontend
    [ ] Clicking drugs in the Drug Candidates page should display data for the drug in a drawer
    [ ] Create a "dashboard" that summarizes the things we actually care about
        [ ] This should be a tab
        [ ] Default to this tab - it should be the first tab
        [ ] Outline steps to create this on a more granular level
    [ ] Create specific page for each drug of interest
    [ ] Create a frontend that renders the knowledge graph and lets you navigate through it
      [ ] Export the knowledge graph data from neoj
          [ ] Include the bad and good candidates worth looking at - But make it 100s of nodes
          [ ] Include the medical conditions/diseases/disorders it treats as nodes
          [ ] Include things like proteins it binds to, etc as nodes (that is, the new nodes)
      [ ] Add a tab for the network graph
        [ ] Give it a sane name (the tab, that is)
        [ ] Make a visualizer with a network graph - containing JUST the drugs of interest - place in the network graph tab
            [ ] Show drug nodes, condition/disease/disorder nodes, and each of the newly generated nodes from step 4
            [ ] Show connections between nodes
            [ ] Create a "data table" area
                [ ] Show data for each node on clicking node
                [ ] Show data for each relationship on clicking relationship

[ ] Think about what to tackle next
[ ] Find drugs for each phase
[ ] Decision tree, finding what's eliminated - show different layers of drugs considered
    [ ] Then at each layer show them getting narrowed down
    [ ] Think concentric circles with different layers, and in the centre, the drugs selected
[ ] Get experts to evaluate the output
[ ] CHECK EACH DRUG FOR WHETHER IT'S BEEN STUDIED IN THIS CONTEXT (before giving it to experts)
    [ ] Think about whether to include non-novel drugs
        - Maybe, since it verifies that the system is sane, maybe not, because it might be viewed as a trivial finding and thus discredit the system
[ ] Get the data scraper to scrape more data from more places and wire it together


-----------------------------------------
Frontend Prototype Improvements
===============================
Missing visualization components
  [ ] PropertyRadar — radar chart for MW/LogP/PSA/HBD/HBA (use on CandidateCard + summary)
  [ ] PhaseCoverageHeatmap — 5-phase × N-strategy coverage grid
  [ ] SafetyVerdictGrid — color-coded candidate × safety verdict grid
  [ ] TierBarChart — grouped bar chart for tiered candidate scores

Missing custom markdown components (currently inlined in MarkdownRenderer)
  [ ] CustomTable — extract table styling into own component
  [ ] CustomCodeBlock — add syntax highlighting (rehype-highlight is installed but not wired up)
  [ ] CustomHeading — add anchor link IDs to H1/H2/H3
  [ ] SafetyBadge — extract from SummaryView into reusable component
  [ ] ScoreBar — extract from markdown-preprocessor into React component

Drug Candidates tab
  [ ] CandidateList — filterable/sortable grid wrapper (sort by score, MW, name, etc.)
  [ ] Add sort options (A-Z, highest score, MW range, LogP range)
  [ ] Add mini PropertyRadar to each CandidateCard

Bugs
  [ ] DataTableViz tooltip hardcoded white background — breaks dark mode
  [ ] csv-loader: is_natural_product only checks lowercase 'true' — misses 'True'
  [ ] CandidateCard property filter hides legitimate zero values (HBD=0, HBA=0)

UX improvements
  [ ] URL-based state (?analysis=may-03&section=methodology) so navigation survives refresh
  [ ] Loading skeletons instead of plain "Loading analysis..." text
  [ ] Error boundary at app level to catch rendering crashes
  [ ] More specific error messages (404 vs network error vs timeout)
  [ ] "Copy to clipboard" button on ChemBL IDs
  [ ] Search result highlighting in Drug Candidates tab

Performance
  [ ] Lazy-load Drug Candidates CSV (only fetch when tab is opened)
  [ ] Dynamic import for Recharts components (bundle is 1.1MB pre-gzip)

Tests (zero test coverage currently)
  [ ] Set up Jest + React Testing Library (not yet installed)
  [ ] markdown-parser.test.ts — section splitting, preamble, numbered vs. uppercase H2
  [ ] table-extractor.test.ts — table parsing, numeric detection, skip non-pipe tables
  [ ] markdown-preprocessor.test.ts — each transform function, regression on valid markdown
  [ ] App.test.tsx — renders, both tabs present, default shows summary


------------------------

Reset using Claude
------------------
[x] Get Claude Code to write a plan
[x] Find plan
[x] Look into alternatives to Neo4j [NebulaGraph is promising]
    {DECISION: we're sticking with Neo4j, for now}
[x] Implement scraping steps from docs/databases/chembl/chembl-scraping-plan.md
[x] Implement Data Integration steps from docs/databases/chembl/chembl-scraping-plan.md
[x] Implement Neo4j Import steps from docs/databases/chembl/chembl-scraping-plan.md

[ ] Integrate MedPlant data into data set

-----------------------------------------
Updated tasks - 2026-02-02
==========================
[ ] Create a guide for usage. How to:
    [ ] Get terminal running
    [ ] Set up repo
    [ ] Set up Neo4j
    [ ] Set up all terminal tools
    [ ] Set up Claude Code
        [ ] Get Claude Code (sign up, etc)
    [ ] Run queries
[ ] Make sure Claude understands the repository
    [ ] Get it to map the structure out
    [ ] Identify the important data files and what they are
    [ ] Commands and subagents?
    [ ] Update Claude initialization file
[ ] 1/2 Clean up garbage files
    [ ] ...so Claude isn't grabbing crap and generating spurious results


-----------------------------------------
-----------------------------------------
-----------------------------------------
-----------------------------------------

NEW DIRECTION - 2026-01-26
==========================
[ ] Look into trying classic machine learning methods like SVMs and multilayer perceptrons
    - Basically we're looking for things that cluster around:
      - Existing drugs for oral mucositis
      - Known treatments for the specific symptoms of the side effect used in other contexts
      - Drugs with side effects that suggest usefulness for addressing a specific
    [ ] K-Nearest Neighbours
    [ ] SVM
    [ ] Multilayer perceptrons
    [ ] Random forest
    [ ] (various other forest algorithms)
    [ ] Etc
[ ] SET UP LOCAL LLM - SEE docs/notes/prompts/claude-prompts.md
    - New plan: create a local LLM that learns from the medical data we've scraped. Use it to come up with experiments?
[ ] Andrew: run this by:
    [ ] Amedeo [neuroscience, etc]
    [ ] Kylie [psychology, neuroscience, medicine, etc]
    [ ] CANImmunize colleagues (Yulric, Catherine, Xuan, Julian) [vaccinations]
[ ] Janice: run this by your professional network:
    [ ] Mercor
    [ ] Various chemistry colleagues
[ ] Brodie: feature branch with a demo of a classic machine learning analysis (like K-nearest neighbours or SVM)
[ ] Investigate validity of the "politely asked Claude to solve the problem" experiment

-----------------------------------------
-----------------------------------------
-----------------------------------------
[ ] Get Claude to regenerate the structure, taking into account the new home of reusable script files, in the src directory
[ ] Create a CLI tool that lets you run scripts from the top level of the repository


-----------------------------------------
-----------------------------------------
-----------------------------------------
-----------------------------------------
Misc
====
[ ] Learn what the standard place to put tests in a python codebase, and how the files should be structures (in terms of directory/file system structure)


-----------------------------------------
Automations
===========
[x] Fix whitespace trimming in editorconfig
[x] Create slash command to remind us of what we were doing last time we worked on it
[ ] CLI command to auto-open the project in VS Code in a new VS Code instance
[ ] Write a Claude Code command to mark down what we're currently doing. Modify the last-session command to read from it.
[ ] Get Claude to understand the new structure of the project
[ ] Figure out how to store current Claude instance context, to immediately load back from where you were last time you worked on it.


-----------------------------------------
TODO list (setup code)
======================
- [ ] [2/3] Script the setup
  - Have a setup script that when run:
    - [ ] Checks for python environment binaries (pyenv, virtualenv) and installs them if not present
    - [ ] Installs the required python version (with pyenv?)
    - [ ] Sets up a python virtual environment in the project
    - [ ] Installs required dependencies


------------------------------------------
Misc
====
- [ ] Narrow drugs down. See docs/notes/narrowing-drugs-down-notes.md
