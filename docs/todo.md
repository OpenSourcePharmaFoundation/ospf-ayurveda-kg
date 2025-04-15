
TODO - next steps (actual project)
==================================
1. ! Scrape medplantdatabase

2. Scrape Dr. Duke's USDA data

3. Do a comprehensive scrape of Drugbank that grabs everything in the data structure we set up last time (see drugbank_notes.md).

4. Create nodes based on drugs (note: there can be other types of nodes. DRUG is just one type of node)

5. Create a very simple initial structure that has each drug as a node, and each [anything] as a property
  - Figure out how best to subdivide traits of drugs (it'll probably match the data structure in drugbank_notes.md)
    - Make different traits of interest different node types
    - Draw a graph database schema

6. Write the Neo4j code for the above structure

7. Test: write a simple search that extracts drugs with a set of 4 chosen characteristics of interest

8. Subdivide the data structure by characteristics


------------------------------------------
TODO list (setup code)
======================
- ! Get pushing to git working again locally
- ! Add gitattributes
- ! Remove VSCode files from repository
- ! Push all prior changes to GitHub
- ! Create local file for notes that don't get added to the repository

- [2/3] Script the setup
  - Have a setup script that when run:
    - Checks for python environment binaries (pyenv, virtualenv) and installs them if not present
    - Installs the required python version (with pyenv?)
    - Sets up a python virtual environment in the project
    - Installs required dependencies

- Get existing data bank script working

- Write quick script that grabs "all" data from one drugbank page in a big clump (as a starting point)

- Complete data model? [see below]
  - Nibedita will look into this more
  - Basically - figure out what sections we actually need

- Figure out where to get adverse effects data
  - Pharmacovigilance data
  - Nibi will do this

------------------------------------------
Assume network is built
- Narrow drugs down:
  - Based on effects that look like they'd potentially be helpful for oral mucositis
  - Receptor binding sites

# What tells us something is a candidate?
Example: for TB
- They looked for autophagy, then landed on all candidates that augmented autophagy

For us:
- Example searches:
  - For "drooling" or "increased liquid in the mouth"
  - For reduced mouth inflammation
  - For reduced pain
  - Reduce infection
  - Anything affecting mucus membranes
  - Look for anything binding to alpha IL2, IL-10

Oral mucositis itself
- Goes from grade 1 to grade 5 (WHO)
  - Grade 1 is mouth only
  - Grade 3-4+ also goes to your digestive tract
  - etc.


