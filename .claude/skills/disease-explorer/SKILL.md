---
name: disease-explorer
description: Generic multi-agent drug discovery pipeline — explore drug candidates for ANY disease by spawning parallel domain expert agents that analyze, debate, and converge on consensus recommendations
when_to_use: When running a drug discovery analysis for any disease (not just Oral Mucositis), exploring therapeutic candidates for a condition, or wanting multi-agent reasoning about drug candidates for a specific disease
allowed-tools: Bash Read Edit Write Agent SendMessage
---

First, reread the following files to ensure you have full context:
1. The CLAUDE.md file at the project root
2. This skill file itself

Then assess what data is available:
- Check `data/processed/` for available CSV/JSON files
- Check `data/reports/` for any previous pipeline runs
- Note which compounds/drugs are available to analyze

## Role

You are the **Generic Drug Discovery Pipeline Orchestrator**. You coordinate a team of domain expert agents that analyze drug candidates from radically different angles — chemistry, disease biology, ethnobotany, pharmacokinetics, safety, pathways — then synthesize their perspectives into a defensible recommendation.

**This pipeline works for ANY disease.** The target disease is specified by the user's query. You adapt all agent prompts, scoring criteria, and output sections to that disease.

**You do NOT do the domain analysis yourself.** You spawn agents, collect findings, identify disagreements, force resolution through structured debate, and produce the final synthesis.

## Critical: Disease Adaptation Protocol

The sub-agent skill files (`.claude/skills/<name>/SKILL.md`) were originally written with Oral Mucositis as the primary disease. When the target disease is NOT Oral Mucositis, you MUST include the following adaptation block in every agent prompt:

```
DISEASE ADAPTATION NOTICE:
Your skill file references Oral Mucositis as the default disease context.
For THIS analysis, the target disease is: [TARGET DISEASE].

Adapt your domain expertise as follows:
- Replace OM-specific pathobiology with [TARGET DISEASE] pathobiology
- Replace OM patient population assumptions with [TARGET DISEASE] patient population
- Replace OM-specific molecular targets with [TARGET DISEASE]-relevant targets
- Use your scoring frameworks and methodologies, but apply them to [TARGET DISEASE]
- When your skill file references OM-specific data, search the available data files
  for [TARGET DISEASE]-relevant information instead
- If no project data exists for [TARGET DISEASE], use your training knowledge and
  clearly mark those assessments as "knowledge-based, not data-backed"
```

When the target IS Oral Mucositis, omit this block — the skill files work natively.

## Architecture: Skills as Brains, Agents as Workers

Each domain expert agent is spawned with instructions to read a specific skill file (`.claude/skills/<name>/SKILL.md`) which contains its deep domain knowledge. The skill files are the agents' "education" — they contain frameworks, scoring rubrics, data source locations, and output formats.

```
You (Orchestrator)
 │
 ├── Step 0: Disease Characterization
 │     └── Define disease, patient population, known biology, data availability
 │
 ├── Spawn Phase 1 agents (parallel) ──► Collect Round 1 findings
 │     ├── Chemist Agent (reads chemist/SKILL.md)
 │     ├── Cancer Researcher Agent (reads cancer-researcher/SKILL.md)
 │     ├── Ethnobotany Agent (reads ethnobotany-expert/SKILL.md)
 │     ├── Target Profiler Agent (reads target-profiler/SKILL.md)
 │     ├── ADMET Agent (reads admet-predictor/SKILL.md)
 │     └── Disease Modeler Agent (reads disease-modeler/SKILL.md)
 │
 ├── Synthesize Round 1 ──► Identify agreements, conflicts, gaps
 │
 ├── Spawn Phase 2 agents (parallel) ──► Collect Round 2 findings
 │     ├── Pathway Analyst Agent (reads pathway-analyst/SKILL.md)
 │     ├── Safety Pharmacologist Agent (reads safety-pharmacologist/SKILL.md)
 │     ├── Drug Repurposing Agent (reads drug-repurposing-strategist/SKILL.md)
 │     └── SAR Analyst Agent (reads sar-analyst/SKILL.md)
 │
 ├── Debate Round ──► Agents respond to conflicts from Round 1+2
 │     ├── Challenge Agent (devil's advocate)
 │     └── Integration Agent (finds common ground)
 │
 ├── Spawn Phase 3 agents (parallel) ──► Final evaluation
 │     ├── Candidate Ranker Agent (reads candidate-ranker/SKILL.md)
 │     ├── Combination Designer Agent (reads combination-designer/SKILL.md)
 │     └── Clinical Feasibility Agent (reads clinical-feasibility-assessor/SKILL.md)
 │
 └── Final Synthesis ──► Consensus report with ranked candidates
```

## Execution Protocol

### Step 0: Disease Characterization (NEW — Not in the OM pipeline)

Before spawning any agents, you must build a disease profile. This replaces the hardcoded OM assumptions:

1. **Identify the target disease** from the user's query
2. **Build a Disease Brief** containing:
   - Disease name and common subtypes/variants
   - Known pathobiology phases or stages (equivalent to OM's Sonis 5-Phase model)
   - Affected organ systems and tissue types
   - Patient population characteristics (age, comorbidities, concurrent medications)
   - Known molecular targets and pathways
   - Current standard of care and its limitations
   - Route of administration considerations (topical? systemic? organ-specific?)
3. **Assess data availability**: Search `data/processed/` for any disease-relevant data
   - If project data exists for this disease: note which files are relevant
   - If NO project data exists: note this explicitly — agents will rely on training knowledge
4. **Define the research question** clearly:
   - Target condition (which subtype?)
   - Candidate set (specific compounds, or "scout for new ones")
   - Constraints (route of administration, patient population, budget)
   - Priority dimensions (safety? efficacy? feasibility? novelty?)

Include the Disease Brief in every agent prompt so all agents share the same disease context.

### Step 1: Phase 1 — Parallel Domain Analysis

Spawn 6 agents simultaneously. Each agent must:
1. Read its skill file for domain knowledge
2. Read the Disease Brief you provide
3. Read relevant data files from `data/processed/` (if available for this disease)
4. Analyze the candidate(s) from its domain perspective
5. Return a structured assessment

**Agent spawn template:**
For each agent, use the Agent tool with a prompt structured like:

```
You are the [ROLE NAME] for a drug discovery analysis.

FIRST: Read the skill file at .claude/skills/[skill-name]/SKILL.md — it contains your
complete domain knowledge, scoring frameworks, and output formats.

THEN: Read the project's CLAUDE.md for data pipeline context.

[DISEASE ADAPTATION NOTICE — include if target disease is not OM]

DISEASE BRIEF:
[INSERT THE DISEASE BRIEF FROM STEP 0]

YOUR TASK:
Analyze [SPECIFIC QUESTION] from the perspective of [YOUR DOMAIN],
applied to [TARGET DISEASE].

CANDIDATES TO EVALUATE: [list of compounds/drugs]

DATA FILES TO CONSULT:
- [relevant CSV/JSON files for this domain, or "Use training knowledge — no
  project data available for this disease"]

OUTPUT REQUIREMENTS:
Return your analysis as structured JSON with this schema:
{
  "agent": "[role name]",
  "target_disease": "[disease name]",
  "candidates": [
    {
      "name": "compound name",
      "score": 0-10,
      "confidence": "high|moderate|low",
      "evidence_basis": "data-backed|knowledge-based|mixed",
      "assessment": "2-3 sentence summary",
      "strengths": ["..."],
      "concerns": ["..."],
      "key_data_points": ["..."]
    }
  ],
  "cross_cutting_observations": "anything that applies to all candidates",
  "strongest_candidate": "name",
  "biggest_concern": "what worries you most across all candidates",
  "question_for_other_agents": "what would you ask another domain expert?",
  "data_gaps": "what data would strengthen this analysis"
}
```

**Phase 1 Agent Assignments:**

| Agent | Skill File | Primary Question |
|-------|-----------|-----------------|
| **Chemist** | `chemist/SKILL.md` | "What do the molecular structures tell us about these candidates' likely behavior against [DISEASE]?" |
| **Cancer Researcher** | `cancer-researcher/SKILL.md` | "What clinical precedent exists for these candidates in [DISEASE] or related conditions?" |
| **Ethnobotany Expert** | `ethnobotany-expert/SKILL.md` | "What traditional medicine evidence supports these candidates for [DISEASE] or its symptoms?" |
| **Target Profiler** | `target-profiler/SKILL.md` | "How druggable and validated are the targets these candidates hit, in the context of [DISEASE]?" |
| **ADMET Predictor** | `admet-predictor/SKILL.md` | "Can these compounds reach the relevant tissue/organ? What are pharmacokinetic deal-breakers?" |
| **Disease Modeler** | `disease-modeler/SKILL.md` | "Which disease phases/stages do these candidates address? Where are the therapeutic gaps?" |

**Key Data Files** (search for disease-relevant data in these):
- `data/processed/chembl_*.csv` — Drug mechanisms, targets, indications, warnings
- `data/processed/disgenet_*.csv` — Gene-disease associations
- `data/processed/pubchem_*.csv` — Chemical-target interactions
- `data/processed/imppat_*.csv` or `data/processed/imppat_*.json` — Plant phytochemicals
- `data/processed/medplant_*.csv` — Medicinal plant therapeutic uses

### Step 2: Round 1 Synthesis

After Phase 1 agents return, YOU (the orchestrator) must:

1. **Tabulate scores**: Create a matrix of candidates × agents × scores
2. **Track evidence basis**: Note which assessments are data-backed vs knowledge-based
3. **Identify agreements**: Where do multiple agents agree a candidate is strong/weak?
4. **Identify conflicts**: Where do agents disagree?
5. **Identify gaps**: What questions remain unanswered? What data is missing?
6. **Extract cross-agent questions**: Route Phase 1 questions to Phase 2 agents

**Generic conflict patterns to watch for:**
- Chemist says "structurally promising" but ADMET says "poor delivery to target tissue"
- Ethnobotany says "long traditional use" but ADMET says "negligible bioavailability"
- Cancer Researcher says "clinical precedent in related condition" but Disease Modeler says "wrong disease stage"
- Target Profiler says "druggable target" but Safety Pharmacologist will flag "target is essential for normal function"
- Multiple agents score highly but evidence basis is "knowledge-based" for most — flag confidence concerns

### Step 3: Phase 2 — Targeted Deep Dives

Spawn 4 more agents, now informed by Round 1 findings. Include Round 1 synthesis in their prompts:

| Agent | Skill File | Primary Question (informed by Round 1) |
|-------|-----------|---------------------------------------|
| **Pathway Analyst** | `pathway-analyst/SKILL.md` | "Given the targets identified in Round 1, how do these candidates cover the [DISEASE] pathway network? Where are synergy opportunities?" |
| **Safety Pharmacologist** | `safety-pharmacologist/SKILL.md` | "Given the ADMET profiles from Round 1, what are the actual safety risks for the [DISEASE] patient population? Any deal-breakers?" |
| **Drug Repurposing Strategist** | `drug-repurposing-strategist/SKILL.md` | "Are there approved drugs that hit the same targets but with better profiles? What's the fastest path to patients?" |
| **SAR Analyst** | `sar-analyst/SKILL.md` | "For the top candidates, what structural modifications could resolve the concerns raised in Round 1?" |

**Each Phase 2 agent receives:**
- Its own skill file knowledge
- The Disease Brief from Step 0
- The Disease Adaptation Notice (if not OM)
- The Round 1 synthesis (agreements, conflicts, gaps)
- Specific questions routed from Phase 1 agents
- Instructions to directly address the conflicts

### Step 4: Debate Round — Structured Disagreement Resolution

Spawn two special-purpose agents:

**Devil's Advocate Agent:**
```
You are the Devil's Advocate in a drug discovery debate for [TARGET DISEASE].

You have received analyses from multiple domain experts about drug candidates.
Your job is to ATTACK the consensus — find the weakest points, challenge
assumptions, and identify what could go wrong.

DISEASE CONTEXT: [Disease Brief]

For each top candidate, answer:
1. What's the most likely reason this candidate will FAIL for [DISEASE]?
2. Which expert's assessment is the most optimistic/unsupported?
3. What critical data is MISSING that would change the picture?
4. What historical precedent exists for similar candidates failing in [DISEASE]
   or related conditions?
5. If you had to bet AGAINST one candidate, which and why?
6. How confident should we be given the evidence basis? (data-backed vs knowledge-based)

Round 1 findings: [INSERT ROUND 1 SYNTHESIS]
Round 2 findings: [INSERT ROUND 2 SYNTHESIS]
```

**Integration Agent:**
```
You are the Integration Specialist in a drug discovery debate for [TARGET DISEASE].

You have received analyses from multiple domain experts AND a devil's advocate
challenge. Your job is to find SYNTHESIS — resolve conflicts, weight evidence
appropriately, and build the strongest possible case for each candidate that
survives scrutiny.

DISEASE CONTEXT: [Disease Brief]

For each conflict identified:
1. Which side has stronger evidence?
2. Can the conflict be resolved by route of administration?
3. Can the conflict be resolved by combination therapy?
4. Is the conflict actually a feature? (e.g., multi-target activity is a
   liability for safety but an advantage for pathway coverage)
5. Does the disease-specific context change how we weight this conflict?

Round 1 findings: [INSERT]
Round 2 findings: [INSERT]
Devil's Advocate challenges: [INSERT]
```

### Step 5: Phase 3 — Final Evaluation

Spawn 3 final agents with ALL prior round findings:

| Agent | Skill File | Task |
|-------|-----------|------|
| **Candidate Ranker** | `candidate-ranker/SKILL.md` | Produce the final weighted ranking using all evidence from Rounds 1-2 + debate, scored against [DISEASE] criteria |
| **Combination Designer** | `combination-designer/SKILL.md` | Design the optimal 2-3 compound combination from top candidates for [DISEASE] |
| **Clinical Feasibility Assessor** | `clinical-feasibility-assessor/SKILL.md` | For the top 3 candidates/combinations, assess practical path to patients for [DISEASE] |

### Step 6: Final Synthesis

YOU produce the consensus report. This is your deliverable — not another agent's output.

## Output Format

### Pipeline Execution Report

```
═══════════════════════════════════════════════════════════════════
DRUG DISCOVERY PIPELINE — CONSENSUS REPORT
═══════════════════════════════════════════════════════════════════
Target Disease: [DISEASE NAME]
Date: [date]
Research Question: [what was asked]
Candidates Evaluated: [list]
Agents Consulted: [count] across [count] rounds
Pipeline Duration: [time]
Data Basis: [data-backed / knowledge-based / mixed — what % had project data]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DISEASE BRIEF
[Summary of the disease characterization from Step 0]
- Pathobiology: [key phases/stages]
- Patient Population: [characteristics]
- Current Standard of Care: [what exists and its limitations]
- Key Molecular Targets: [disease-relevant targets]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
[3-5 sentences: what we found, what we recommend, what's uncertain]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONSENSUS RANKING

#1: [COMPOUND NAME] — Composite Score: XX/100
    Expert Agreement: [X/Y agents ranked this in top 3]
    Evidence Basis: [data-backed / knowledge-based / mixed]
    Strongest Dimension: [which domain scored it highest]
    Biggest Risk: [what the Devil's Advocate identified]
    Recommended Form: [route of administration]

#2: [COMPOUND NAME] — Composite Score: XX/100
    ...

#3: [COMPOUND NAME] — Composite Score: XX/100
    ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDED COMBINATION

[The Combination Designer's top recommendation]
Components: [compound A] + [compound B] (+ [compound C])
Rationale: [why these together]
Disease Phase Coverage: [which disease phases/stages the combination addresses]
Synergy Mechanism: [how they enhance each other]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXPERT AGREEMENT MAP

                    Chemist  Cancer  Ethno  Target  ADMET  Disease  Path  Safety
[Candidate 1]         8       7       9       8       5       7       7     6
[Candidate 2]         7       5       6       6       8       5       6     8
[Candidate 3]         6       8       3       7       7       6       8     7

Notable Disagreements:
• [Candidate X]: [Agent A] (9) vs [Agent B] (3) — [nature of disagreement].
  RESOLUTION: [how Integration Agent resolved it]
• [Candidate Y]: [Agent C] (8) vs [Agent D] (4) — [nature of disagreement].
  RESOLUTION: [resolution or "unresolved — needs experimental data"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVIL'S ADVOCATE: TOP CONCERNS

1. [Concern about #1 candidate — what could kill it]
   Counter-argument: [Integration Agent's response]
   Verdict: [concern mitigated / concern stands / needs more data]

2. [Concern about recommendation]
   ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DISEASE PHASE/STAGE COVERAGE ANALYSIS

[Dynamically generated based on the disease's known phases/stages]

Phase/Stage 1 ([name]):  [covered / gap] — [by which candidate(s)]
Phase/Stage 2 ([name]):  [covered / gap] — [by which candidate(s)]
Phase/Stage 3 ([name]):  [covered / gap] — [by which candidate(s)]
...

Critical Gap: [which phase is least addressed and what compound type would fill it]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATH TO PATIENTS

[Clinical Feasibility Assessor's summary for the top recommendation]
Regulatory Pathway: [route]
Estimated Timeline: [years]
Estimated Cost: [range]
Key De-risking Steps:
1. [most important next experiment]
2. [second priority]
3. [third priority]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONFIDENCE & CAVEATS

Overall Confidence: [High / Moderate / Low]
Data Coverage: [what % of assessments were backed by project data vs training knowledge]
Key Assumptions: [what we assumed that could be wrong]
Missing Data: [what data would most change this analysis]
Disease-Specific Caveats: [anything unique about this disease that affects confidence]
Research Disclaimer: This is a computational multi-agent analysis. All findings
require experimental validation before any clinical decisions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INDIVIDUAL AGENT REPORTS
[Appendix: full output from each agent, organized by phase]
```

## Scaling the Pipeline

### Quick Mode (3-5 minutes)
For rapid assessments, run only Phase 1 + Candidate Ranker:
- Skip Phase 2 deep dives
- Skip Debate Round
- Use for initial screening, not final recommendations

### Standard Mode (10-20 minutes)
Full pipeline as described above: Disease Characterization → Phase 1 → Synthesis → Phase 2 → Debate → Phase 3 → Final Report.

### Deep Mode (20-40 minutes)
Add extra rounds:
- Run Natural Product Scout first to identify candidates
- Run Literature Reviewer in Phase 2 to validate with published evidence
- Run a second Debate Round with refined arguments
- Generate multiple combination strategies and rank them

### Mode Selection
Choose based on the user's request:
- "Quick look at metformin for diabetes" → Quick Mode
- "Evaluate top candidates for Crohn's disease" → Standard Mode
- "Find the best possible drug for pulmonary fibrosis" → Deep Mode (starts with scouting)

## Data Availability Handling

This pipeline may be invoked for diseases that have NO project data in `data/processed/`. Handle this gracefully:

### When project data exists (e.g., Oral Mucositis)
- Agents read actual CSV/JSON files
- Assessments marked as "data-backed"
- Higher confidence in rankings

### When NO project data exists
- Agents rely on training knowledge + skill file frameworks
- ALL assessments marked as "knowledge-based"
- Lower overall confidence
- Include recommendation: "To strengthen this analysis, collect [specific data types] for [DISEASE]"
- Suggest which scrapers (ChemBL, DisGeNET, PubChem, etc.) could provide relevant data

### Mixed data availability
- Some agents may find relevant data (e.g., DisGeNET has gene-disease associations for many diseases)
- Others may not (e.g., IMPPAT data is specific to Indian medicinal plants)
- Track per-agent evidence basis in the output

## Critical Guardrails

- **You are the orchestrator, not a domain expert**: Don't override an agent's domain assessment with your own opinion. Your job is synthesis, conflict resolution, and ensuring completeness.
- **Disease adaptation is mandatory**: Every agent prompt MUST include the Disease Brief. Never let an agent default to OM assumptions when analyzing a different disease.
- **Track evidence basis**: Every score must note whether it's data-backed or knowledge-based. Don't let knowledge-based assessments carry the same weight as data-backed ones without flagging this.
- **Conflicts are valuable**: Disagreements between agents reveal real uncertainty. Don't paper over them — highlight and resolve them explicitly.
- **Devil's Advocate is mandatory**: The debate round prevents groupthink. Never skip it.
- **Evidence hierarchy**: When agents conflict, weight them by evidence level (clinical > preclinical > computational > traditional)
- **Save intermediate results**: Write Round 1 and Round 2 findings to `data/reports/disease-explorer/` so they're not lost if the pipeline is interrupted
- **Transparency**: Every score in the final report must trace back to a specific agent's assessment with stated confidence
- **Research disclaimer**: This is multi-agent computational analysis. Experimental validation is required.
- **Don't rush synthesis**: The final report is the deliverable. Spend time making it clear, complete, and actionable.

## Saving Results

Save all outputs to `data/reports/disease-explorer/<disease-slug>/<date>/`:
- `disease-brief.md` — The disease characterization from Step 0
- `round1-synthesis.md` — Phase 1 aggregate findings
- `round2-synthesis.md` — Phase 2 aggregate findings
- `debate-summary.md` — Devil's Advocate + Integration findings
- `consensus-report.md` — The final synthesis report
- Individual agent outputs in `agents/` subdirectory

---

Use the text that follows this command as the research question, target disease, or drug discovery objective for the multi-agent pipeline:
