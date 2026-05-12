TODO - next steps
=================
2026-05-04
----------
[ ] Evaluate the output of the analysis
[ ] Find drugs for each phase
[ ] Decision tree, finding what's eliminated - show different layers of drugs considered
    [ ] Then at each layer show them getting narrowed down
    [ ] Think concentric circles with different layers, and in the centre, the drugs selected
[ ] Create data visualization agent
[ ] Build the frontend (call it a "prototype")
[ ] Get experts to evaluate the output
[ ] CHECK EACH DRUG FOR WHETHER IT'S BEEN STUDIED IN THIS CONTEXT (before giving it to experts)
    [ ] Think about whether to include non-novel drugs (maybe, since it verifies that the system is sane, maybe not, because it might be viewed as a trivial finding and thus discredit the system)
[ ] Think about what to tackle next
[ ] Get the data scraper to scrape more data from more places and wire it together


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
