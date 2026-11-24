# Diabetic retinopathy: solve the open scientific questions

category: Research
model: opus
effort: high
permissions: auto
cwd: /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg

A sixteen-agent analysis of PPARα as a target in diabetic retinopathy produced a defensible
ranking and a correct staging conclusion, and left roughly a dozen questions open. It closed
with the claim that "one rodent study and one aqueous humour sample would contribute more than
the sixteen agents that produced this report."

**That is half right. The analysis only ever reasoned — it never computed, never collected, and
never queried.** Several of the questions it declared unanswerable are answerable right now,
with this repository's own scrapers, knowledge graph and GNN, plus public expression atlases and
the published literature. They were declared unknown from an armchair.

This chain closes the ones that can be closed, and sharpens the ones that cannot into
specifications for the bench.

**Source analysis:** `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md`
and the supporting documents in that directory. Read the report before Step 1.

Run with:
`./ospf chain docs/prompts/dr-solve-open-questions-prompt.md --stop-on-fail`

**Rules for every step:**
- Work in the `ospf-ayurveda-kg` repo. Do not use worktree isolation.
- **Never read `data/holdout/`, `data/processed-blinded-*/`, or
  `.../2026-10-05/agents/UNBLINDING-part-b.md`** — they hold a benchmark answer key that must
  stay sealed for future blinded runs. Nothing in this chain is blinded; you simply must not
  spoil that key.
- Every quantitative claim carries a source and an uncertainty. Distinguish measured, modelled
  and reasoned values explicitly — conflating them is the specific failure this chain corrects.
- A negative or null result is a deliverable. If a mechanism fails to close, that is more
  valuable than confirming it, and it should be stated plainly rather than hedged.
- Commit on the current branch with conventional commits. No AI attribution trailers. Do not
  push or open PRs.

## Step 1: Close the DR data gaps the analysis could not close

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The analysis concluded that essentially every quantitative claim it made
was reasoning rather than measurement. That was true, and it was partly self-inflicted: the
project's data could not speak to the question being asked.

Verified gaps, all of which are fixable with scrapers already in this repo:

- **Zero gene-disease associations for diabetic retinopathy.** The only DisGeNET files are
  `data/processed/disgenet__OM_*.csv`, scoped to the earlier Oral Mucositis project. Every
  gene-disease link in the entire DR analysis is knowledge-based.
- **The target panel is blind to its own subject.** `data/reports/disease-explorer/
  diabetic-retinopathy/2026-10-05/evidence/compound-dr-target-matrix.tsv` contains all three
  PPAR receptors and **not one PPAR effector gene** — no ANGPTL4, CPT1A, ACOX1, HMGCS2,
  FABP1/4/5, LPL, APOA1, APOA5, ABCA1, ABCG1, FGF21, PDK4, ACADM, EHHADH.
- **No drug-target affinity anywhere.** `chembl_drug_mechanisms.csv` has 11 rows,
  `chembl_drug_targets.csv` 44, `chembl_bioactivities.csv` 23, against 3,276 approved drugs.
  `grep -ci PPAR` returns 0 in all three.
- **`chembl_drug_metabolism.csv` is corrupt.** 10,000 rows collapse to 1,000 unique records;
  only 10 distinct `drug_name` values exist across 152 drug IDs. Root cause is at
  `src/scrapers/chembl/chembl_scraper.py:261` — the metabolism endpoint is filtered on
  `molecule_chembl_id`, which that endpoint does not support, so ChEMBL ignores it and returns
  the same first page every call. Line 889 then takes `drug_name` from the loop variable while
  line 888 takes the ID from the response.

**Your task.**

1. **Fix the metabolism scraper bug.** Filter on a field the endpoint supports, assert the
   returned ID matches the requested one before writing, and add a post-write check that
   identical record counts across distinct queries fail loudly. Re-scrape.
2. **Generalise the DisGeNET scraper.** `src/scrapers/disgenet/disgenet_scraper.py` is
   hardcoded to Oral Mucositis. Parameterise it by disease, then pull gene-disease associations
   for diabetic retinopathy, diabetic macular edema, and diabetic microvascular complications.
3. **Scrape ChEMBL properly for the PPAR axis.** Mechanisms, targets and bioactivities for
   PPARA, PPARD, PPARG and every fibrate, glitazone, glitazar and PPAR-active compound you can
   resolve. You need real binding affinities, not class pharmacology.
4. **Build the effector panel.** Extend the DR gene panel with the PPARα transcriptional
   programme listed above, and regenerate the compound-target matrix against the extended panel.

**Deliverables.** Fixed scraper code; new CSVs under `data/processed/`; a regenerated matrix;
and `docs/notes/dr-data-gap-closure.md` stating, per gap, what was closed, what was not, and
what the new data changes about the claims in
`data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md`.

**Do not** touch `data/holdout/` or `data/processed-blinded-*`. This step is not blinded.

-----[NEXT_PROMPT]-----

## Step 2: Settle the retinal PPARA expression question with data

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The analysis could not resolve whether PPARα is meaningfully expressed
in human retina. Antibody-based studies report it across Müller glia, RPE, endothelium, ganglion
cells and microglia; single-cell transcriptomic atlases reportedly do not show PPARA as a
prominent retinal transcript. The analysis graded this "EMERGING / partly UNCERTAIN" and moved
on, because it was reasoning rather than querying.

**That conflict is resolvable with public data, and nobody queried it.** It matters: it caps the
signal amplitude of every local-engagement mechanism, independent of drug exposure.

**Your task.** Query public single-cell and single-nucleus retina atlases directly — human
where available, diabetic donors where they exist, with a non-diabetic comparison.

For PPARA, PPARD, PPARG and the effector panel from Step 1, determine per retinal cell type:
expression detected or not; the fraction of cells expressing; expression level relative to a
housekeeping baseline and to a known-expressed retinal receptor as a positive control; and
whether diabetes changes it.

Name the atlases you used and their accessions. Where an atlas lacks the gene, say whether it
is absent or below detection threshold for that platform — those are different claims, and
dropout in single-cell data is the obvious confound to address explicitly.

**Then answer:**
- Is PPARA expressed in human retina at a level consistent with a druggable target, and in which
  cell types?
- Is the antibody-versus-transcriptomics conflict real, or an artifact of detection sensitivity?
- Is retinal PPARA expression reduced in diabetes, as the restore-a-deficit framing assumes?
- **Does PPARD exceed PPARA in retina?** If so, the isoform-selectivity argument changes, because
  PPARδ is pro-angiogenic and shares the transrepression machinery.

**Deliverable.** `docs/notes/ppara-retinal-expression.md` with the per-cell-type table, the
atlases and accessions, the dropout analysis, and a plain verdict on each question. State the
confidence and what would change it.

-----[NEXT_PROMPT]-----

## Step 3: Close the FGF21 concentration bridge

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem — this is the single most important unresolved item in the analysis.**

The best-evidenced mechanism is a hepatic-to-retinal humoral relay: a fibrate raises plasma
FGF21, and FGF21 protects retinal vasculature. Both halves are published. **Nobody has checked
whether they are the same concentration.**

The downstream retinal work uses pharmacological recombinant FGF21. A fibrate produces a modest
physiological rise in the endogenous hormone. If the therapeutic rise is one or two orders of
magnitude below the protective concentration, the relay is an artifact of comparing two
literatures that never met — and it is the limb the clinical evidence most favours.

This failure mode has already appeared twice elsewhere in this disease's analysis: herbal fatty
acids, and endogenous PPARα ligands whose plasma concentration already sits at their own EC50.
**A real effect demonstrated at a dose the intervention cannot deliver is the characteristic
error of mechanism-first reasoning.** Test for it here.

**Your task.**

1. Extract **human plasma FGF21** concentrations: baseline in diabetic and non-diabetic adults,
   and on-treatment at therapeutic fibrate doses. Absolute units, with assay and variance. Note
   that FGF21 immunoassays disagree substantially between platforms — handle that explicitly.
2. Extract the **concentration-response for FGF21** on retinal endothelial, Müller and RPE
   readouts: the concentrations at which protection is demonstrated, and the preparation used.
3. **Put them on one axis.** Compute the ratio of achievable plasma concentration to active
   concentration, with uncertainty bounds.
4. Address the two obvious objections: whether the free or total hormone is the relevant
   comparator given β-Klotho co-receptor dependence, and whether chronic exposure changes the
   picture relative to acute dosing.

**Deliverable.** `docs/notes/fgf21-concentration-bridge.md` with both datasets, the computed
ratio, and a verdict: **does the relay close, fail, or remain undetermined, and by how much?**

If it fails, say so plainly — that would remove the limb the analysis ranked best-evidenced, and
that is a more valuable result than confirming it.

-----[NEXT_PROMPT]-----

## Step 4: Verify the three claims of absent evidence

model: sonnet
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The analysis made three load-bearing claims that specific evidence does
not exist. Load-bearing absence claims should be verified by systematic search, not asserted —
and two of them were used to downgrade or demote a mechanism.

**Verify or refute each:**

1. **No cell-type-restricted conditional `Ppara` deletion in retina has been reported.** This is
   the only experiment that establishes necessity. The analysis treated its absence as itself
   informative after roughly fifteen years of interest in the target. If it exists, the
   necessity question may already be answered.
2. **No published measurement of intraocular ANGPTL4 stratified by fibrate exposure.** This was
   the proposed empirical settlement of the wrong-sign risk.
3. **No measurement of fibrate concentration in retinal tissue or aqueous humour in any
   species.** This is the critical-path unknown the whole programme is sequenced behind. Search
   ocular PK literature, veterinary ophthalmology, and any study measuring any fibrate in any
   ocular compartment.

Search systematically — PubMed, Europe PMC, preprint servers, conference abstracts, and
model-organism databases for the knockout. Record the queries you ran so the search is
reproducible.

**Also resolve a fourth question that bears on all of them:** does the global `Ppara` knockout
retinal phenotype survive correction for its systemic confounds? The knockout carries
hypertriglyceridaemia, abolished ketogenesis and FGF21, hepatic steatosis and an altered
diabetes response — so "worse retinopathy" may be fully explained by the competing systemic
hypothesis, making the citation circular. Has anyone controlled for this?

**Deliverable.** `docs/notes/dr-evidence-absence-audit.md`: per claim, verified-absent or
refuted-with-citations, the queries run, and what each finding changes. **A refutation is the
more valuable outcome — it means the analysis built on a false absence.**

-----[NEXT_PROMPT]-----

## Step 5: Replace the estimated retinal exposure with a parameterised model

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The entire analysis turns on retinal free-drug exposure, and every
number for it is an estimate with no model behind it. The partition ratio was assigned a range
(0.2–0.7 for endothelium and RPE, 0.01–0.15 for neural retina) by argument. Three mutually
exclusive programmes depend on which end of those ranges is right, and the dataset contains no
measured distribution, permeability or protein-binding value for any drug.

A documented orchestrator error in this analysis came from exactly this: a term was reported as
if it were the full product, producing a headline conclusion the run's own numbers contradicted.
**Ranges collapsed into point estimates is the failure mode. Build a model instead.**

**Your task.** Construct a quantitative ocular exposure model for the fibrate chemotype.

- Parameterise properly: dose, absorption, plasma concentration over time at steady state,
  measured fraction unbound, ionisation at physiological pH (these are acids with pKa near 3 —
  logD at pH 7.4 is roughly −0.5 against a nominal logP near 3.8, and the dataset's `logd`
  column is empty for all 3,276 rows, so this must come from measurement or calculation, not
  from `alogp`), passive permeability, and efflux at the barrier.
- Treat the compartments separately: retinal vascular endothelium and RPE face the blood side or
  fenestrated choriocapillaris and require crossing one membrane; neural retina sits behind the
  tight junction.
- Anchor against any measured ocular partition data for structurally similar acids — NSAIDs,
  sartans, statin acids — to calibrate rather than assert.
- **Run a sensitivity analysis.** Which input dominates the output variance? That is where
  measurement effort should go, and nobody has identified it.

**Then compute, for fenofibric acid, pemafibrate, elafibranor and seladelpar:** free
concentration per compartment, the margin against free EC50 corrected consistently for binding
on both sides, and the bounds. Where a published EC50 was measured in serum-containing medium,
correct it — comparing free drug against a nominal EC50 double-counts protein binding, and that
inconsistency is worth about a log.

**Deliverable.** Model code under `src/analysis/`, plus
`docs/notes/retinal-exposure-model.md` with the parameter table and provenance for every value,
the computed margins with bounds, the sensitivity analysis, and a verdict on whether local
engagement is achievable for any of them. **Every number carries a source and an uncertainty.**

-----[NEXT_PROMPT]-----

## Step 6: Find an agent for the uncovered efflux arm

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** Every one of the 29 compounds considered reduces what *arrives* in the
retina. **Not one accelerates what leaves.** The reverse-cholesterol-transport arm is the single
largest uncovered module, and it sits inside the analysis's own thesis.

This matters more than a coverage gap. The lesion is a self-renewing cycle: modified lipoprotein
→ scavenger uptake → transporter downregulated → cholesterol cannot leave → inflammasome
activation and foam-cell death → lipid re-released → re-uptake. Solving it as a two-compartment
system gives burden = influx ÷ clearance exactly. **But as clearance approaches zero the system
has no steady state — it integrates, and a supply-lowering agent buys only delay.**

The fibrates do not cover this: transporter induction is gene-activation driven, which is the
limb shown absent at achievable local occupancy, and it is a two-step relay, so more sensitive
to that shortfall, not less. **And it cannot be done from the liver.**

**One structural opening:** the PPARα pocket mandates a lipophilic acid, which couples potency to
hepatoselectivity. **The LXR pocket does not — its ligands are neutral.** Ionisation is not
structurally locked in for that target.

**Your task — this is a discovery task, not an analysis task.**

1. Define the efflux axis as targets: NR1H2, NR1H3, ABCA1, ABCG1, APOA1, APOE, and the
   scavenger-uptake side (CD36, OLR1, MSR1) for completeness.
2. **Use the knowledge graph and the GNN link-prediction model in `local-llm/gnn`** to rank
   compounds predicted to engage that axis. That model was built for compound-target prediction
   and has never been pointed at this question.
3. Filter the predictions on retinal-access physicochemistry — neutral or weakly basic preferred,
   moderate molecular weight, polar surface area in the penetrant window, not an efflux
   substrate. Use the Step 5 model, not `alogp`.
4. Assess the top candidates for the known liability that has killed systemic agents of this
   class: hepatic steatosis and hypertriglyceridaemia. Isoform selectivity or tissue restriction
   is the entire problem, not a detail.
5. Separately, evaluate whether a **direct extracellular acceptor** beats a transporter inducer.
   Adding a direct removal term keeps burden finite even at zero transporter activity, whereas a
   transporter inducer multiplies a term that may already be near zero. If that holds, the
   preference ordering the analysis carried is backwards.

**Deliverable.** `docs/notes/retinal-lipid-efflux-candidates.md` — the ranked predictions with
scores and rationale, the physicochemical filter and what it removed, the steatosis assessment,
and a verdict on acceptor versus transporter inducer. Save predictions as CSV under
`data/processed/`.

-----[NEXT_PROMPT]-----

## Step 7: Design the non-acidic PPARalpha ligand

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The analysis concluded — then retracted — that no drug in the fibrate
class can probe local PPARα engagement, because the acid head is mandatory and potency therefore
trades against tissue access by construction.

**The retraction was correct and the structural argument behind it is strong, but nobody built
the molecule.** The AF-2 cage is all-donor: Ser280, Tyr314, His440 and Tyr464 each donate a
hydrogen bond, so the ligand supplies only acceptors. The geometry demands a bidentate acceptor
pair roughly 2.2–3.2 Å apart — **not a formal charge.** Charge is an acceptor-strength multiplier
worth a bounded 2.3–3.1 kcal/mol per contact.

The existence proof is already in hand: oleoylethanolamide is neutral, binds near 120 nM, and has
**ligand efficiency 0.41 — higher than fenofibric acid (0.29) or pemafibrate (0.34).** The
neutral head pays no efficiency penalty. The chemical space is empty because every PPARα
indication has been hepatic, where high protein binding and transporter uptake are *features*.
Nobody ever needed a high-free-fraction PPARα ligand.

**Your task.**

1. **Build the pharmacophore** from the AF-2 donor cage geometry — acceptor positions, distance
   constraints, the hydrophobic arm vectors. Note that PPARα's arm I is narrower than PPARγ's, so
   head-group *footprint* is the first filter, not electronics.
2. **Screen the neutral and weakly acidic window.** Prioritise head groups that preserve
   bidentate acceptor geometry without a permanent charge: 1,2,4-oxadiazol-5(4H)-one, acylsulfonamide,
   hydroxyisoxazole, phosphine oxide and phosphonamide. **Rule out tetrazole explicitly and say
   why** — it raises pKa by only about 1.6, has a larger footprint, and remains a full hepatic
   uptake transporter substrate, which is why the sartans are hepatically taken up.
3. **Model the efficacy asymmetry.** Tyr464 sits on mobile helix 12 and pays for AF-2 closure, so
   it is lost first — a neutral head should produce a partial agonist by construction, with
   efficacy degrading before affinity. Quantify how much maximal efficacy is lost, because a
   partial agonist that cannot drive the transcriptional programme is not useful.
4. **Propose 3–5 concrete scaffolds.** For each: structure, predicted potency range, predicted
   logD at pH 7.4, predicted free fraction, predicted retinal partition from the Step 5 model,
   isoform selectivity strategy against both PPARγ and PPARδ, and **what breaks first.**
5. **State the assay problem.** No cascade exists for optimising against free-drug retinal
   exposure — free-drug-corrected EC50, measured free fraction, measured partition in a species
   with a comparable barrier. Specify the cascade that would need to be built.

**Deliverable.** `docs/notes/non-acidic-ppara-ligand-design.md` with the pharmacophore, the
screen, the scaffolds with full predicted profiles, the assay cascade, and an honest probability
of technical success. Be a medicinal chemist, not an optimist.

-----[NEXT_PROMPT]-----

## Step 8: Rewrite the report from results instead of reasoning

model: opus
effort: high

**Standard chain-step constraints — follow these before and during the task below:**

1. **Read the plan doc first.** If this step (or the chain) references a plan or
   ticket doc (usually under `docs/tickets/`), read it in full before doing
   anything else. Follow what it establishes; do not rediscover or contradict it.
2. **All browser work goes through /pinchtab.** Use the `/pinchtab` skill for any
   browser automation. Never use Claude-in-Chrome (`mcp__claude-in-chrome__*`
   tools) — this step runs as an unattended background agent with no attended
   Chrome session, so those tools will hang or fail.
3. **Re-verify PR and Jira state at run time.** Reports from earlier chain steps
   about PR or Jira state may be stale or wrong. Before acting on such state,
   check it yourself: the `gh` CLI for PR/check/review state, the Jira REST API
   for ticket state. Trust what you verify, not what a previous step said.
4. **Append a dated status section on completion.** When this step's work is
   done, append a status section to the referenced plan doc (e.g.
   `## Status — YYYY-MM-DD — step N: <name>`) recording what was done, what was
   verified, and anything the next step needs. Use today's real date. If the
   step has no plan doc, put the same summary in your final message instead.
5. **End your final message with a `result:` line.** The very last line must be
   `result: <one-line summary of what this step did>` — nothing after it, not a
   sign-off, not a question, not a tool tally. The chain reads that line to know
   the step finished. Without it the runner has to infer completion from how
   your closing sentence is phrased, which is what makes chains stall.

**Scientific problem.** The current report at
`data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md` is a reasoning
document. Steps 1–7 replaced several of its reasoned claims with computed and collected results.
Rewrite it so it reports what is now known.

**Read every deliverable from Steps 1–7 before writing anything.**

**What changes:**
- Claims that were estimates become measurements or modelled values with bounds.
- Claims of absent evidence become verified or refuted, with citations.
- The retinal expression question becomes a data answer rather than a graded uncertainty.
- The FGF21 relay either closes, fails, or is quantified as undetermined.
- The efflux arm either has candidates or is shown to have none, with reasons.
- The non-acidic ligand is designed or shown to be undesignable.

**Rules for the rewrite:**
- **Report the science, not the process.** No references to pipelines, agents, rounds, chains,
  steps, or how the document was produced. If a finding is true, state it; its provenance within
  this workflow is not the reader's concern. Cite external sources normally.
- **No self-assessment.** Whether an earlier analysis was right is not this document's subject.
  The methodological retrospective lives in `BENCHMARK-RESULT.md` and stays there.
- **Every quantitative claim carries a source and an uncertainty.** Mark measured, modelled and
  reasoned values distinctly. The failure this whole exercise is correcting is reasoning
  presented with the confidence of measurement.
- **Where something remains genuinely unmeasurable, say so and say what would measure it.**
  Preserve the experimental programme, updated to drop anything Steps 1–7 answered.

**Lead with the conclusion.** A reader should know from the abstract: which compound, which
disease stage, which mechanism is live, what the retinal exposure actually is, and what single
measurement still decides the rest.

**Deliverable.** The rewritten `REPORT.md` at the same path, plus a short
`docs/notes/dr-report-changelog.md` listing every claim that changed and what changed it. Do not
modify the other files in that report directory.

-----

## Status — 2026-11-09 — step 6: Find an agent for the uncovered efflux arm

**Done.** `docs/notes/retinal-lipid-efflux-candidates.md`; code in
`src/analysis/efflux_axis/` (`axis`, `gnn_rank`, `chembl_axis`, `candidates`,
`physchem`, `steatosis`, `acceptor`, `run`); nine CSVs at
`data/processed/efflux_axis_*.csv`. Reproduce with
`python -m src.analysis.efflux_axis.run`.

**Verified.**
- Axis defined as nine genes in three evidence classes. The ligandable /
  non-ligandable split was *confirmed by data*, not asserted: of 3,732
  qualifying ChEMBL activities, **3,729 are at LXR-α/LXR-β and 0 at ABCA1,
  ABCG1, APOA1, APOE**. The only ABCA1 mechanism record is probucol, an
  *inhibitor*.
- **The GNN was run and its output must not be used.** Ranking compounds for a
  gene, it places its own training positives at mean percentile rank 0.123
  (random 0.500); compound degree alone scores 0.970. Scoring path validated
  against the model card (MRR 0.216 vs 0.232 published), so the model is not
  broken — it is the *transpose* of the direction its benchmark evaluates
  (corr(gene degree, column score) +0.957; corr(compound degree, row score)
  −0.509). Benchmark reproducible via
  `gnn_rank.benchmark_axis_retrieval`.
- Step 5's model reused directly, not reimplemented: the fenofibric-acid
  reference reproduces at K<sub>p,uu</sub> 0.0594 against Step 5's published
  0.0586. Neutral ligands gain a **paired median 10–12× (95% CI 1.9–64×)**.
- Steatosis expressed as a requirement: **≥2.73 log β-selectivity for an acid
  vs ≈1.55 for a neutral ligand.** Of 797 dual-measured ligands, **0 of 83
  acids clear the acid bar**; 8 clear the neutral bar, 5 also reach the retina,
  4 survive worst-case.
- Acceptor vs inducer solved: at E = 0 a **1000× inducer gives infinite burden**
  and an acceptor at 0.1× healthy clearance gives 10. Inversion boundary
  `E* = k_a·A/(k_t·(F−1))`.

**What the next step needs to know.**
1. **Do not cite GNN-ranked compound-target predictions.** Anything in
   `REPORT.md` resting on them inherits §2 of the note. Fix: evaluate link
   prediction in both directions and report the degree-only baseline.
2. **The five candidates are one chemical series from one 2018 patent
   (CHEMBL5725956), on cell-free coactivator-recruitment data.** In the
   cell-based tier the best β-selectivity across 106 molecules is 1.37 log —
   below requirement; **not one clears it.** Rank candidate 2 (CHEMBL5938562)
   above candidate 1: candidate 1's two LXR-α EC50s differ 57-fold and it fails
   on the lower one.
3. **The acceptor arm is intravitreal, and that is not a disqualification** —
   DR is already treated by intravitreal injection. The analysis ranked
   candidates by oral-systemic feasibility for a disease dosed into the target
   compartment. This is the most consequential reframing in the note.
4. **The decisive unmeasured number is `E`** — ABCA1/ABCG1 activity in human
   diabetic retina relative to healthy. It decides acceptor versus inducer
   outright and does not exist in any species.

**Note on chain state.** The runner recorded step 5 as `failed`, but its
artefacts (`docs/notes/retinal-exposure-model.md`,
`src/analysis/ocular_exposure/`, `data/processed/ocular_exposure_margins.tsv`)
were present and complete at run time and were used as the brief directs. Step
6 had also been recorded `failed` with no artefacts; this is its completed run.
