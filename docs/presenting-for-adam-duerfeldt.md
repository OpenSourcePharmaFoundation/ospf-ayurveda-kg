Part 1: existing output
=======================
- Show what we have
  - Show the academic consensus report for c. difficile: `data/reports/disease-explorer/clostridioides-difficile/2026-08-17/consensus-report-academic.md`
    - Show the result table - in preview mode
    - Explain the:
      - database scraping (show at top)
      - knowledge graph linking the database outputs together
        - e.g. drug-to-indication, drug-to-side effects, drug-to-binding site
      - fleet of trained agents that trawl the graph and make inferences
        - the multi-layer, multi-stage "competitive" process between different agents concurrently analyzing and inferring higher-level information from the knowledge graph
      - cross-referencing against content of specific research papers for confirmation
        - honing the results based on the findings from research papers
  - Show the website output to give a second example (with oral mucositis):
    - https://ospf-ayurveda-kg-frontend.vercel.app/

### Advantages
- Comprehensive analysis (as far as we know)
  - We need this rated though
  - We don't know how good the results are
    - We need to get these results in front of an expert

### Disadvantages
- One-shot
- Extremely processing and token-intensive
- Allows no back-and-forth or honing queries

Part 2: next directions
=======================
- Create network of local AIs / LLMs / GraphRAGs
  - Top-level: SLM (small language model) to take queries in
  - Shrink the size of the knowledge graph to discrete relevant sections
    - Use other AI tools for this, namely structural pruning using Graph Neural Networks
  - Analyze those subsections with other small AIs and traditional machine learning methods like SVMs (Support Vector Machines), random forests, multilayer perceptrons, etc
  - Feed it back into an LLM to generate text output

### Purpose:
- Allows unlimited generation of potential drug candidates for different conditions, combinations of conditions, etc.
- Allows back and forth "discussion" with the system
  - That is, try different prompts out
- Allow creation of a frontend for it

### What's done?
- Planned approach

What we are interested in
=========================
1. To get results in front of experts in each field to make sure the outputs make sense
2. Hone what we're doing with condition-specific researchers (related to #1)
   - Ensure the outputs make sense
3. Help progress 2nd offshoot of the knowledge graph: the local LLM project

Motivation
==========
- Use our experience with LLMs from our day jobs and our science backgrounds for a more meaningful and usable/practical purpose
  - Antidote to our frustration with pointless and harmful uses of AI
- Build a valuable open-source project that helps further medical knowledge
