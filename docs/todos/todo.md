TODO - next steps
=================
Reset using Claude
------------------
[x] Get Claude Code to write a plan
[x] Find plan
[x] Look into alternatives to Neo4j [NebulaGraph is promising]
    {DECISION: we're sticking with Neo4j, for now}
[ ] Implement docs/databases/chembl/chembl-scraping-plan.md
[ ] Get Claude to regenerate the structure, taking into account the new home of reusable script files, in the src directory
[ ] Create a CLI tool that lets you run scripts from the top level of the repository


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
