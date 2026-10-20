# Disease Brief — Diabetic Retinopathy (BLINDED RUN)
Orchestrator framing document. Every pipeline agent reads this first.

## 1. MANDATORY BLINDING PROTOCOL

This is a **blinded benchmark run**. Facts about which drugs are already used for
diabetic retinopathy (DR) or diabetic macular edema (DME) were deliberately removed from
the dataset so a later step can score whether this pipeline rediscovers them.

1. Read project data ONLY from `data/processed-blinded-diabetic-retinopathy/`.
   NEVER read `data/processed/chembl_approved_drugs.csv`, anything under
   `data/holdout/`, or any file named `answer-key*`. Do not use git history, git
   objects, or any other route to recover redacted values. Do not try to identify which
   rows were redacted — reconstructing the key by elimination defeats the run.
2. Reason from MECHANISM and the blinded data. Do NOT use, assert, or cite as supporting
   evidence the fact that any drug is already indicated for, approved for, guideline-
   recommended for, or trialed in DR or DME — even if you know it from training.
   Treat every candidate's DR status as unknown.
3. You MAY freely use general pharmacology, medicinal chemistry, physiology, genetics,
   and NON-DR clinical knowledge.
   - Allowed: "fenofibrate is a PPARα agonist approved for dyslipidemia; ~99% albumin
     bound; renally eliminated as the acyl glucuronide."
   - Forbidden: "fenofibrate reduced DR progression in FIELD / ACCORD-Eye."
   - Allowed: "PPARα-knockout mice show worse experimental retinopathy" (genetic
     mechanism evidence, not drug indication status).
4. **Exception — Literature Reviewer only.** That agent may surface DR-specific trial
   evidence, but ONLY inside a section headed `## POST-HOC UNBLINDING (EXCLUDED FROM
   SCORING)`. Nothing in that section may influence any score it reports.
5. End your output with a **blinding compliance statement**: confirm which files you
   read, and disclose honestly any place where DR-specific knowledge influenced your
   judgment, including negative decisions (choosing to exclude something).

## 2. DISEASE MODEL — read the full model

Read `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-model.md`
(1,555 lines). Structure summary:

**Three-axis hybrid model.**
- **Axis A — clinical stage S0→S5:** S0 preclinical neurodegeneration · S1 mild NPDR ·
  S2 moderate NPDR · S3 severe NPDR · S4 PDR · S5 advanced/tractional. DME is a
  cross-cutting complication with distinct phenotypes (inflammatory, lipid/exudative,
  ischemic, Müller-cytotoxic, outer-BRB pump failure).
- **Axis B — nine concurrent pathway modules P1–P9:** P1 polyol/aldose reductase ·
  P2 AGE/RAGE · P3 PKC · P4 hexosamine · P5 oxidative/mitochondrial · P6 inflammation
  and leukostasis (NF-κB hub) · P7 hypoxia/VEGF · P8 **lipid handling — the
  under-served axis** · P9 neurovascular unit degeneration. These run concurrently from
  day one, not sequentially.
- **Axis C — anatomical compartment:** inner BRB (capillary endothelium, pericyte,
  glial sheath) · outer BRB (RPE/Bruch's) · neural retina · vitreoretinal interface.

**Score every candidate as a (pathway, stage, compartment, route) tuple.**

## 3. UNMET NEEDS — ranked

1. Disease-modifying therapy for early S0–S2 DR, deliverable systemically. Largest
   population, longest runway, zero competition.
2. A non-VEGF mechanism for the 30–50% incomplete-responder DME fraction.
3. Neuroprotection independent of anatomy.
4. Reduced treatment burden (oral adjunct lowering injection frequency).
5. Prevention/resolution of hard exudate and intraretinal lipid (the P8 axis).
6. Reperfusion of nonperfused retina.
7. Anti-fibrotic for proliferative/tractional disease.
8. Deployable without specialist infrastructure in low- and middle-income settings.

## 4. SCORING PRIORS FROM FAILED APPROACHES

Things that should LOSE points:
- "Antioxidant" as the sole mechanism — repeatedly null in DR.
- Single-branch blockade downstream of the ROS node (the P1 and P3 precedents).
- Topical delivery claims for a posterior-segment target — strong prior against.
- Promiscuous polyphenols without a specific mechanistic argument.
- Mechanisms acting only at S4/S5 where effective therapy already exists.
- Fluid retention (the PPARγ class precedent), hypoglycemia potentiation, myopathy
  signal, or a need for therapeutic drug monitoring.

**Isoform discipline:** PPARγ agonism causes fluid retention and is associated with
worsening macular edema. PPARα and PPARγ must be scored separately. Do not transfer
PPARγ liabilities to PPARα, nor putative PPARα benefits to PPARγ.

## 5. PATIENT POPULATION

Diabetic adults, T1D and T2D (biologically distinct — see model §3.2). Near-universal
comorbidity: diabetic kidney disease, neuropathy, cardiovascular disease, dyslipidemia,
hypertension, obesity. Concurrent medication classes for DDI analysis: metformin and
other oral hypoglycemics, insulin, statins, RAS blockers, antiplatelets, diuretics.
**Renal impairment is the norm, not an edge case** — it constrains drug choice heavily.
Chronic lifelong dosing in a polypharmacy population.

## 6. ROUTE CONSTRAINTS

The blood-retinal barrier is tight-junctioned with active efflux. Acidic, highly
protein-bound molecules penetrate poorly; the retina has no analogous uptake transporter
to the liver's OATP system. See disease-model.md §6.2 for the physicochemical predictors.
An oral agent that worked would be transformative because every current DR-specific
therapy is a procedure.

## 7. THE FOCUS QUESTION

The user's analysis specifically targets **PPARα (gene PPARA)**. Read the PPARα deep
assessment at disease-model.md §5.2 and the full scout report at
`agents/p0-ppara-scout.md`.

**The critical path item is retinal exposure after oral dosing, not target validity.**
The scout's central objection: free fenofibric acid in plasma sits roughly two orders of
magnitude below the PPARα half-maximal concentration because ~99% is albumin-bound, and
the retina has no transporter to concentrate it. If a PPARα agonist helps the retina,
retinal PPARα engagement may not be the reason — systemic lipoprotein lowering may be.
**Score systemic lipid-lowering plausibility and anti-inflammatory transrepression as
separate axes from retinal PPARα occupancy.**

Counter-consideration the model raises: retinal PPARα expression is reported *decreased*
in diabetes, so an agonist would restore rather than supraphysiologically stimulate.
Conditional genetic evidence (knockout worse, retina-targeted expression protective)
supports a retina-intrinsic component.

**Wrong-sign risk:** ANGPTL4 is a direct PPARα target gene and a potent pro-permeability,
pro-angiogenic factor in ischemic retina. Agonism predicts its induction, which could be
net harmful in proliferative disease. Every agent must address this if it scores a PPARα
candidate highly.

## 8. CANDIDATE SET (15)

From `agents/p0-ppara-scout.md` §8. Full justifications there.

### Group A — direct PPARα agonists, approved
| ID | Compound | ChEMBL | Mechanism |
|---|---|---|---|
| A1 | Fenofibric acid | CHEMBL981 | PPARα agonist, weak (tens of µM), ~10x vs γ. QED 0.85, best drug-likeness in class |
| A2 | Fenofibrate | CHEMBL672 | Obligate ester prodrug → A1. Prodrug conversion confirmed in project data |
| A3 | Pemafibrate | CHEMBL247951 | SPPARMα, sub-nM, >2000x selective. Hepatoselective by design. Safest in CKD |
| A4 | Elafibranor | CHEMBL3707395 | PPARα/δ dual, low-nM. Flag the Michael-acceptor enone |
| A5 | Seladelpar | CHEMBL230158 | PPARδ-selective. **Isoform falsification control** — if δ ≥ α, the PPARα hypothesis fails |

### Group B — PPARα natural products and endogenous ligands
| ID | Compound | Evidence |
|---|---|---|
| B1 | Linoleic acid | STRONG — binds, activates, recruits NCOA1/NCOA2/CREBBP across ≥4 PMIDs. Non-selective, not a drug |
| B2 | Alpha-linolenic acid | STRONG — binds and activates |
| B3 | Linalool | MODERATE — binds and activates; PPARA-mutant alters susceptibility. Single source |
| B4 | Icosapent ethyl | CHEMBL2095209. ω-3 ester prodrug → EPA. The druggable form of the Group B finding |

### Group C — PPARα-adjacent multi-target
| ID | Compound | Role |
|---|---|---|
| C1 | Quercetin | 26/27 DR-panel genes. **WEAK for PPARα and direction-incoherent** (antagonizes GW 7647). The frequent-hitter control. Oral bioavailability <2% |
| C2 | Melatonin | 19/27 genes. WEAK for PPARα. **The exposure control** — MW 232, neutral, crosses the BRB freely, synthesized in retina. Tests whether access beats affinity |

### Group D — non-PPARα mechanistic comparators
| ID | Compound | ChEMBL | Mechanism |
|---|---|---|---|
| D1 | Epalrestat | CHEMBL56337 | Aldose reductase (AKR1B1) inhibitor, P1 |
| D2 | Dimethyl fumarate | CHEMBL2107333 | NRF2 activator via KEAP1, P5 — tests the Nrf2 limb directly rather than via PPARα crosstalk |
| D3 | Minocycline | CHEMBL1434 | Microglial deactivation / neuroprotection, P9 |
| D4 | Candesartan cilexetil | CHEMBL1014 | AT1R blockade, local retinal RAS. Zero PPAR involvement |

### Group E — the mechanism-discriminating control (ADDED AFTER ROUND 1)

| ID | Compound | ChEMBL | Mechanism |
|---|---|---|---|
| E1 | Ezetimibe | CHEMBL1138 | NPC1L1 cholesterol-absorption inhibitor. Lowers apoB/LDL. **Zero PPAR activity.** Oral, generic, well tolerated in diabetics |

**Why E1 was added.** Four Round 1 agents independently converged on the concern that the
PPARα hypothesis may be a *lipid-lowering* hypothesis wearing a receptor's name, and that
the original 15-compound set **cannot distinguish those two readings** — every
lipid-lowering candidate in it is also a PPAR ligand. Ezetimibe lowers apoB through a
completely unrelated intestinal mechanism, so it isolates the question:

> **If a matched apoB-lowering non-PPAR agent produces the same retinal benefit, the
> receptor is not what is doing the work, and the whole PPARα framing is wrong.**

This is a more informative control than the PPARδ-selective arm (A5), which the Target
Analyst showed is confounded — PPARδ is the most abundant retinal PPAR, is pro-angiogenic,
is at least as strong an ANGPTL4 inducer as PPARα, and shares the identical transrepression
machinery, so both a positive and a negative seladelpar result are ambiguous.

**Honest limitation of E1:** the match is partial. Fibrates lower triglyceride-rich
remnant particles; ezetimibe lowers predominantly LDL cholesterol. Since the disease model
identifies the toxic species as the *modified apoB particle* rather than cholesterol load
(hard exudates are retained glycated-and-oxidised apoB lipoproteins, not "fat"), the
comparison is informative but not clean. No non-PPAR remnant-lowering generic exists to do
better. Bempedoic acid (CHEMBL3545313, ACL inhibitor) carries the same LDL-vs-remnant
mismatch and has a far smaller chronic-use database. **Agents must weigh E1's result with
this mismatch stated, not treat it as a decisive null.**

**Controls, not candidates:** gedunin (PPARα antagonist — negative control);
dibutyl phthalate (best-controlled activation evidence in the file, with GW 6471
antagonist reversal, but a reproductive toxicant — mechanistic positive control only).

**Known curation defects — do not score these as compounds:** D-fructose, sucrose,
glucose, galactose appear with high DR-target counts but are experimental perturbagens,
not candidates. If one surfaces in your ranking, that is a bug.

## 9. DATA

- Inventory and caveats: `data-inventory.md`
- Data-quality defects: `data-quality-findings.md` — note especially that
  `chembl_drug_metabolism.csv` has a corrupt `drug_name` column and is 10x duplicated,
  and that the ChEMBL mechanism/target tables are near-empty test extracts with zero
  PPAR content, so **no drug→target edge in this project is data-backed**.
- Pre-computed evidence pack in `evidence/`:
  - `ppara-interactions.tsv` — all 143 PPARA rows, cleaned
  - `compound-dr-target-matrix.tsv` — 153 compounds × 27 DR-panel genes
  - `ppar-class-drug-properties.tsv` — 13 PPAR-class drugs with physicochemical fields
- PubChem evidence is predominantly Comparative Toxicogenomics Database **expression-level**
  association, not binding. "X results in increased expression of PPARA mRNA" is NOT
  target engagement. **Row count is not evidence weight.**

## 10. OUTPUT CONTRACT

Return structured JSON:
```json
{
  "agent": "role name",
  "candidates": [{
    "name": "...", "score": 0-10, "confidence": "high|moderate|low",
    "evidence_basis": "data-backed|knowledge-based|mixed",
    "pathway": "P1-P9", "stage": "S0-S5", "compartment": "...", "route": "...",
    "assessment": "2-3 sentences", "strengths": ["..."], "concerns": ["..."],
    "key_data_points": ["..."]
  }],
  "cross_cutting_observations": "...",
  "strongest_candidate": "...",
  "biggest_concern": "...",
  "question_for_other_agents": "...",
  "data_gaps": "...",
  "blinding_compliance": "..."
}
```
Scores are 0-10. Use the full range. A score of 7+ requires you to state what evidence
would falsify it.
