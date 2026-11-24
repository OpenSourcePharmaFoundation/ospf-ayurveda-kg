# P1 — Disease Biology Specialist: Coverage, Stage-Matching and Gap Analysis
**Agent:** Diabetic Retinopathy Biology Specialist
**Date:** 2026-10-05
**Run:** BLINDED benchmark run
**Framework:** three-axis DR model (`disease-model.md`) — clinical stages S0–S5, pathway
modules P1–P9, anatomical compartments. The `disease-modeler` SKILL.md's Oral Mucositis
five-phase model was **not** used; only its methodology (phase mapping, gap analysis,
disease-relevance scoring, patient-context assessment) was carried over and re-pointed at DR.

---

## 0. Headline findings

1. **The candidate set is a near-pure S0–S2 set.** That is the right half of the disease
   to be in — unmet need #1 — but it means the set is almost empty against unmet needs
   #2 (incomplete-responder DME, in the *established-edema* sense), #6 (reperfusion) and
   #7 (anti-fibrosis). This is a defensible allocation, not a defect, but it must be stated.

2. **The central paradox of the PPARα hypothesis is a stage offset, not an exposure
   problem.** PPARα's exposure-robust limb — reducing the systemic supply of apoB/remnant
   lipoprotein — only produces retinal benefit *once the barrier already leaks*, i.e. S1–S3.
   PPARα's right-stage limb — retinal FAO, ceramide and DAG control at S0–S1 — is precisely
   the limb that requires retinal receptor occupancy, which the scout's arithmetic puts
   ~2 logs short. **The best-exposed mechanism acts at the wrong stage; the right-stage
   mechanism has the worst exposure case.** Everything else in this report follows from that.

3. **The candidate set covers only the supply side of P8.** All fifteen compounds, in every
   combination, reduce or redirect what *arrives* in the retina. **Not one accelerates what
   *leaves*.** The reverse-cholesterol-transport / efflux arm (P8.3 — LXR→ABCA1/ABCG1→
   ApoA1/ApoE acceptors, and scavenger-receptor blockade of CD36/OLR1/MSR1) is entirely
   uncovered. That is the largest uncovered gap inside this run's own declared thesis.

4. **The set's best pathway×stage×compartment fit may not be a PPARα agent.** Dimethyl
   fumarate hits the upstream ROS/NRF2 node the model itself nominates as the highest-leverage
   intervention point (Brownlee logic), covers P5+P2(GLO1)+P6+P8.7, acts from S0, and has the
   best blood–retinal-barrier physicochemistry in the entire set — with a plausible *active
   uptake* route the fibrates lack (§6.3). The pipeline should see that disagreement explicitly.

5. **The ANGPTL4 risk–benefit genuinely inverts across stage**, and it inverts from both
   ends simultaneously: benefit falls toward S4 while hazard rises. Stage restriction is
   warranted. A late-stage trial is not "certainly dangerous" but should not be the lead
   indication, and requires prespecified neovascular-event surveillance (§8).

---

## 1. Methodology and scoring conventions

### 1.1 Engagement notation

| Symbol | Meaning |
|---|---|
| `●●●` | Direct, mechanistically primary engagement of the module |
| `●●` | Moderate / indirect — engages the module through one intermediate step |
| `●` | Weak or speculative — plausible but small, or model-only |
| `○` | No meaningful engagement |
| `⊗` | **Wrong-sign risk** — plausible mechanism by which the candidate worsens that module |

### 1.2 Evidence-quality notation

| Symbol | Meaning |
|---|---|
| `K` | General class pharmacology (allowed knowledge; not DR-specific) |
| `D` | Backed by this run's blinded project data (structure, physicochemistry, interaction rows) |
| `E` | CTD **expression-level** association only — "X alters PPARA mRNA" — the weakest class. Per brief §9, row count is not evidence weight |
| `M` | Model/animal-only mechanistic report |

### 1.3 Two-column engagement scoring

For every candidate I score the module **twice**:

- **Mechanism column** — would this module be engaged if the drug were present at the
  retina at a pharmacologically active free concentration?
- **Exposure-discounted column** — is that engagement likely to actually occur in retinal
  tissue after chronic oral dosing, given `disease-model.md` §6.2?

The gap between those two columns is where this entire run's uncertainty lives. Compounds
whose primary limb is **systemic** (plasma/liver) are not discounted, because they do not
need to reach the retina to work. This is the single most important scoring decision in
my report and it is the reason fenofibric acid and pemafibrate do not collapse under the
scout's exposure objection the way their retina-intrinsic limbs do.

---

## 2. (a) THE COVERAGE MATRIX — 15 candidates × 9 pathway modules

### 2.1 Mechanism-level engagement (if drug reaches target)

| ID | Candidate | P1 polyol | P2 AGE/RAGE | P3 PKC | P4 hexosamine | P5 oxidative/NRF2 | P6 inflamm/leukostasis | P7 hypoxia/VEGF | P8 lipid | P9 NVU |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Fenofibric acid | ○ | `●`K | `●●`K | ○ | `●●`K | `●●●`K | `⊗`M | `●●●`K | `●●`M |
| A2 | Fenofibrate | ○ | `●`K | `●●`K | ○ | `●●`K | `●●●`K | `⊗`M | `●●●`D/K | `●●`M |
| A3 | Pemafibrate | ○ | `●`K | `●`K | ○ | `●`K | `●●`K | `⊗`M | `●●●`K | `●`M |
| A4 | Elafibranor | ○ | `●`K | `●●`K | ○ | `●●`K | `●●●`K | `⊗⊗`M | `●●●`K | `●●`M |
| A5 | Seladelpar | ○ | ○ | `●`K | ○ | `●●`K | `●●`K | `⊗`M | `●●`K | `●`M |
| B1 | Linoleic acid | ○ | ○ | `⊗`K | ○ | `⊗`K | `⊗`K | ○ | `⊗`K | ○ |
| B2 | α-Linolenic acid | ○ | ○ | ○ | ○ | `●`K | `●`D/K | ○ | `●●`D/K | `●`K |
| B3 | Linalool | ○ | ○ | ○ | ○ | `●●`D/E | `●●`D/E | ○ | `●●`D | `●`E |
| B4 | Icosapent ethyl | ○ | ○ | `●`K | ○ | `●`K | `●●`K | ○ | `●●●`K | `●●`K |
| C1 | Quercetin | `●●`E | `●●`E/K | `●`E | ○ | `●●`E | `●●`E | `●`E | `●`E | `●`E |
| C2 | Melatonin | ○ | `●`E | ○ | ○ | `●●●`K | `●●`K | `●`E | ○ | `●●●`K |
| D1 | Epalrestat | `●●●`K | `●●`K | `●`K | ○ | `●●`K | `●`K | ○ | `⊗`K | `●●`K |
| D2 | Dimethyl fumarate | ○ | `●●`K | ○ | ○ | `●●●`K | `●●`K | `●`K | `●●`K | `●●`K |
| D3 | Minocycline | ○ | `●`K | ○ | ○ | `●●`K | `●●●`K | `●`K | ○ | `●●●`K |
| D4 | Candesartan cilexetil | ○ | `●`K | `●●`K | ○ | `●●`K | `●●`K | `●●`K | ○ | `●`K |

### 2.2 Exposure-discounted engagement (what is likely to actually happen in retinal tissue)

Compartment abbreviations: **PL** plasma/liver (no BRB crossing required), **iBRB** inner
blood-retinal barrier endothelium (luminal-accessible but intracellular targets still require
membrane crossing), **oBRB** RPE, **NR** neural retina, **GL** glia/microglia.

| ID | Candidate | Primary compartment reached | What survives the discount | What is lost to the discount |
|---|---|---|---|---|
| A1 | Fenofibric acid | **PL** | P8 supply-side (`●●●`) — needs no retina | P6 transrepression → `●`; P8.8 retinal FAO → `●`; P9 → `●` |
| A2 | Fenofibrate | **PL** | identical to A1 post-conversion | identical, plus formulation/food-effect variance |
| A3 | Pemafibrate | **PL** (hepatoselective **by design**) | P8 supply-side (`●●●`, strongest in set) | *All* retinal limbs → `●`/`○`. OATP-mediated hepatic uptake actively suppresses extrahepatic exposure |
| A4 | Elafibranor | **PL**, some iBRB | P8 supply (`●●●`); best retinal-occupancy case in Group A (low-nM, non-hepatoselective) | still `●●` at best retinally; aLogP 5.16, Ro5v 1, QED 0.41 |
| A5 | Seladelpar | **PL** | P8.8 FAO (`●●`) | δ-selectivity **weakens the apoB/remnant supply limb** — the limb that matters most here |
| B1 | Linoleic acid | NR/oBRB (dietary incorporation) | membrane incorporation is real | direction is wrong (§2.4) |
| B2 | α-Linolenic acid | NR/oBRB (poorly) | marginal n-3 substrate supply | human ALA→EPA→DHA conversion is inefficient; most is β-oxidised |
| B3 | Linalool | **NR/GL (good access)** | MW 154, neutral, logP ~3 — the only Group B member physicochemically able to reach retina | no chronic human dosing vehicle; rapid glucuronidation; single-source evidence |
| B4 | Icosapent ethyl | **PL + NR/oBRB** | TG/remnant lowering (PL) **and** genuine membrane incorporation (NR) — rare dual reach | EPA ≠ DHA; VLC-PUFA/ELOVL4 arm untouched |
| C1 | Quercetin | — | **nothing**. Oral bioavailability <2%, extensive phase-II conjugation | the entire 26-target annotation collapses |
| C2 | Melatonin | **NR/GL/oBRB (free access)** | essentially all of its mechanism | nothing — this is the point of the control |
| D1 | Epalrestat | iBRB/NR (moderate) | AKR1B1 inhibition in pericytes/Müller | — |
| D2 | Dimethyl fumarate | **oBRB/NR (plausibly active uptake, §6.3)** | NRF2 program, GLO1, GPX4/aldehyde detox | MMF is anionic; uptake hypothesis is `[EMERGING]` and must be verified |
| D3 | Minocycline | **NR/GL (CNS-penetrant)** | microglial deactivation, MMP9 | — |
| D4 | Candesartan | **iBRB luminal surface** | AT1R is a **cell-surface GPCR on the luminal endothelial membrane** — no BRB crossing required (§6.2) | AT1R on Müller/RGC (abluminal) → `●` |

### 2.3 Module coverage summary — who is covered, who is empty

| Module | Candidates with `●●` or better (mechanism) | Candidates with `●●` or better (exposure-discounted) | Verdict |
|---|---|---|---|
| **P1 polyol** | D1, C1(E) | **D1 only** | **Thin — 1 real candidate**, in a mechanism class the model flags as clinically disappointing |
| **P2 AGE/RAGE** | D1, D2, C1(E) | **D2 (via GLO1), D1** | **Thin.** No RAGE antagonist, no dicarbonyl scavenger with real exposure |
| **P3 PKC** | A1/A2/A4, D4 | **D4 only (weakly)** | **Effectively empty.** No direct PKC agent. Only the indirect P8→DAG→PKC bridge, which is exposure-dependent |
| **P4 hexosamine** | **none** | **none** | **Empty — and correctly so.** Model §P4: "mechanistically important, pharmacologically unattractive." Not a defect |
| **P5 oxidative/NRF2** | A1/A2/A4/A5, B3, C1(E), C2, D1, D2, D3, D4 | **D2, C2, D3, D1** | **Well covered** |
| **P6 inflammation** | A1/A2/A4, B4, C2, D2, D3, D4 | **D3, D2, C2, D4** | **Well covered on mechanism; the fibrate contribution is the most exposure-fragile part of it** |
| **P7 hypoxia/VEGF** | D4 (weak) | **D4 (weak)** | **Deliberately near-empty.** Correct: S3–S4 is where effective therapy exists. But note **five candidates carry `⊗` here** (ANGPTL4) |
| **P8 lipid** | A1–A5, B2, B3, B4 | **A1/A2/A3/A4 (supply only), B4, D2 (P8.7 only)** | **Well covered on the supply side; see §2.5 — half of P8 is empty** |
| **P9 NVU/neuroprotection** | A1/A2/A4, B4, C2, D1, D2, D3 | **C2, D3, D2** | **Covered, but by the non-PPARα arm** |

### 2.4 Direction-coherence audit — two candidates engage modules in the *wrong* direction

**B1 Linoleic acid — the most important negative finding in the matrix.**
Linoleic acid carries the strongest PPARα *binding* evidence in the entire project dataset
(binds, activates, recruits NCOA1/NCOA2/CREBBP across ≥4 PMIDs). Binding evidence is not
benefit-direction evidence, and in DR the direction is **wrong**:

- LA is the n-6 precursor of arachidonate. The model (§P8.4) states that in diabetes the
  retinal n-6:n-3 ratio **already shifts toward arachidonate**; supplementing LA pushes it
  further in the direction the disease is already moving.
- More arachidonate = more substrate for the P8.6 pro-inflammatory eicosanoid arm
  (PTGS2→PGE2, ALOX5→LTB4, ALOX12/15→12/15-HETE — the last of which the model rates as
  one of the better-validated lipid mediators in DR, KO-protective).
- The model (§P8.7) names **4-HNE as specifically n-6 derived**. LA is its direct precursor.
  Increasing LA load in the most PUFA-rich, most oxidatively stressed tissue in the body
  increases the substrate pool for the aldehyde that adducts mitochondrial enzymes and
  activates JNK.

**Conclusion: B1 is an excellent mechanistic probe of the PPARα ligand pocket and a poor
therapeutic direction for this disease.** It should be retained as the mechanistic anchor
the scout intended and scored low as a candidate. The pipeline must not let "STRONG evidence"
in the PPARA evidence file propagate into a high therapeutic score.

**D1 Epalrestat — a retina-specific wrong-sign limb nobody has flagged.**
`disease-model.md` §5.1 row 10 notes, almost in passing, that **AKR1B1 also detoxifies 4-HNE**.
Aldose reductase is one of the enzymes that reduces reactive lipid aldehydes to their alcohols.
In most tissues this is a footnote. In the retina — the most PUFA-laden tissue in the body,
with the highest lipid-peroxidation load (§P5, §P8.7) — inhibiting AKR1B1 plausibly impairs
aldehyde detoxification in exactly the compartment where that detoxification matters most.
AKR1B1 is also highly expressed in pericytes and Müller cells, the cells that die first.

This does not make epalrestat harmful on balance — the polyol/NADPH-drain benefit is real and
the osmotic benefit in pericytes is real — but it is a genuine, retina-specific, under-appreciated
counter-argument, and it is additive to the model's existing verdict that the P1 class has been
clinically disappointing. I weight it as a meaningful downgrade.

### 2.5 THE P8 SUB-MODULE MATRIX — where the lipid axis is actually covered

This is the table that matters most for this run. P8 is not one thing; it is eight
sub-processes, and the candidate set covers them very unevenly.

| P8 sub-process | What it is | Covered by | Coverage |
|---|---|---|---|
| **P8.1 supply** | Systemic apoB/TG-rich remnant/small-dense-LDL particle number | A1, A2, A3, A4, B4 (A5 weakly) | **✓✓ strongly covered — 5 candidates** |
| **P8.1 extravasation** | Barrier failure letting lipoprotein in | A1/A2/A4 (via P6 transrepression, exposure-limited), D4 (luminal) | **◐ partial** |
| **P8.2 modification** | In-situ glycation/oxidation to gly-oxLDL | D2 (NRF2→antioxidant program), A-group (CAT induction, exposure-limited) | **◐ partial — and D2 fits better than any PPARα agent** |
| **P8.3 efflux / RCT** | **ABCA1/ABCG1 → ApoA1/ApoE acceptors; LXRα/β; CYP46A1/CYP27A1; CD36/OLR1/MSR1 foam-cell uptake** | **A-group: weak, indirect, speculative only (§5.4)** | **✗ EMPTY — THE GAP** |
| **P8.4 membrane PUFA** | DHA/VLC-PUFA, ELOVL4, ADIPOR1, FADS/ACSL6 | B4, B2 (both EPA/ALA, not DHA); A-group ambiguous (§5.6) | **◐ partial, and with the wrong fatty acid** |
| **P8.5 ceramide/S1P** | SPTLC/CERS→ceramide → pericyte and endothelial apoptosis | A-group indirectly (↓palmitate flux via FAO) — exposure-limited | **◐ indirect only; no direct agent** |
| **P8.6 eicosanoids/resolution** | ALOX5/12/15, PTGS2, Lp-PLA2; **SPM resolution failure** | B4 (EPA → E-series resolvins, AA displacement) | **◐ one candidate; B1 is net negative here** |
| **P8.7 peroxidation** | 4-HNE, MDA, CEP, oxysterols; GPX4/ferroptosis; ALDH2/GST detox | **D2** (NRF2 → GCLC/GSR/GPX4/GST/ALDH); D1 `⊗` | **✓ covered — by the non-PPARα comparator** |
| **P8.8 FAO/lipotoxicity** | CPT1A, ACOX1, HMGCS2, FABP4/5, lipid droplets, RPE ketogenesis | A1–A5 (this is the canonical PPARα module) — **exposure-limited** | **◐ mechanism strong, exposure weak** |

**Read this table carefully.** The candidate set is strong on the *afferent* half of P8 —
how much lipid arrives — and on peroxidation downstream. It is **empty on the efferent half**:
nothing in it moves deposited lipid out of the retina. For a disease whose signature P8 lesion
is a persistent, slowly-resorbing lipid plaque that anti-VEGF does not clear and that causes
permanent subfoveal scotoma, that is the structurally important hole.

---

## 3. (b) STAGE-MATCHING ANALYSIS

### 3.1 The stage matrix

`▓` = primary window where this candidate would plausibly change the trajectory.
`░` = secondary/partial. `·` = no meaningful effect. `⚠` = plausible net harm.

| ID | Candidate | S0 preclin | S1 mild | S2 mod | S3 severe | S4 PDR | S5 tractional | Matches need #1 (S0–S2)? |
|---|---|---|---|---|---|---|---|---|
| A1 | Fenofibric acid | `░` | `▓` | `▓` | `░` | `⚠` | `·` | **Partially** — S1/S2 yes, S0 weakly |
| A2 | Fenofibrate | `░` | `▓` | `▓` | `░` | `⚠` | `·` | Partially |
| A3 | Pemafibrate | `·` | `▓` | `▓` | `░` | `⚠`(lower) | `·` | **Partially — and S0 is lost entirely** |
| A4 | Elafibranor | `░` | `▓` | `▓` | `░` | `⚠⚠` | `·` | Partially |
| A5 | Seladelpar | `░` | `░` | `░` | `·` | `⚠` | `·` | Weakly |
| B1 | Linoleic acid | `⚠` | `⚠` | `⚠` | `·` | `·` | `·` | **No** |
| B2 | α-Linolenic acid | `░` | `░` | `░` | `·` | `·` | `·` | Weakly |
| B3 | Linalool | `░` | `░` | `░` | `·` | `·` | `·` | Weakly (scaffold, not drug) |
| B4 | Icosapent ethyl | `░` | `▓` | `▓` | `·` | `⚠`(bleeding) | `·` | **Yes** |
| C1 | Quercetin | `·` | `·` | `·` | `·` | `·` | `·` | **No — exposure collapses it** |
| C2 | Melatonin | `▓` | `░` | `░` | `·` | `·` | `·` | **Yes — best S0 reach in the set** |
| D1 | Epalrestat | `▓` | `▓` | `░` | `·` | `·` | `·` | **Yes** |
| D2 | Dimethyl fumarate | `▓` | `▓` | `▓` | `░` | `·` | `·` | **Yes — widest early-stage span in the set** |
| D3 | Minocycline | `▓` | `▓` | `▓` | `·` | `·` | `·` | **Yes** |
| D4 | Candesartan cilexetil | `░` | `▓` | `▓` | `▓` | `·` | `·` | **Yes, and extends to S3** |

### 3.2 Stage-window findings

**(i) Nothing in the set is an S4/S5 agent — so the model's "penalise S4/S5-only mechanisms"
prior does no work here.** No candidate earns a penalty on that ground. Instead, five
candidates (A1–A5) carry an inverse penalty: a plausible **S4 hazard** via ANGPTL4 (§8).
That is a more serious finding than the one the prior was designed to catch.

**(ii) The S0 column is the sparsest.** Only four candidates have a credible S0 limb:
**melatonin, dimethyl fumarate, minocycline, epalrestat** — i.e. the two controls and two
of the four non-PPARα comparators. **No Group A PPARα agonist has a strong S0 case**, for the
reason set out in §5: at S0 the barrier is intact, so there is no extravasation for the
supply limb to prevent, and the only operative PPARα limb at S0 is retinal FAO/ceramide
control, which is the most exposure-fragile limb in the whole hypothesis.

> **This is the stage-offset finding.** The brief's #1 unmet need is S0–S2. PPARα's robust
> limb begins at S1–S2. PPARα's S0 limb is its weakest. The hypothesis and the need overlap
> at S1–S2 and diverge at S0 — meaning the PPARα arm addresses the *back half* of the
> highest-value window, not the front half. A trial enrolling true S0 (no visible lesions)
> would be testing the limb with the worst exposure case and would likely be negative for
> reasons that say nothing about the target.

**(iii) Pemafibrate loses S0 completely.** Hepatoselectivity removes the only S0-active
limb. For a supply-side thesis this costs nothing — pemafibrate remains the strongest
supply-side agent and the safest in CKD. For an S0 disease-modification thesis it is the
wrong molecule by design. The scout's fork is therefore *also* a stage fork, not only a
mechanism fork, and the ranker should be told that.

**(iv) Candesartan is the only candidate credibly reaching S3.** Ang II→AT1R→NOX→VEGF and
the loss of retinal autoregulation (model §S1) are both operative into the ischemic switch,
and AT1R sits on the luminal endothelial surface where systemic drug actually is. It is the
only candidate that extends past S2 without a wrong-sign flag.

**(v) The set has no S4/S5 coverage at all.** Unmet needs #6 (reperfusion) and #7
(anti-fibrosis) are untouched. This is a reasonable allocation given that S4 has effective
therapy, but #6 and #7 remain open and no candidate speaks to them.

---

## 4. (c) THE P8 LIPID AXIS — the core analysis

### 4.1 How much of DR's natural history is actually lipid-driven? An honest apportionment

The question has to be split three ways, because the three framings give different answers.

**(1) Between-patient variance in DR *incidence*: lipid is a minor contributor.**
Glycemic exposure (HbA1c integrated over duration) and diabetes duration dominate, with
blood pressure next. Classical risk-factor models explain a surprisingly modest share of
total variance overall, and plasma lipid measures add little beyond glycemia and BP for
*incidence of any retinopathy*. The model states this plainly (§P8.2): "plasma LDL
cholesterol correlates only weakly with DR severity, which historically argued against a
lipid mechanism." That argument should not be waved away — it is the honest baseline.

**(2) Variance in the *exudative phenotype*: lipid is a major contributor.**
For hard exudate burden, circinate rings and exudative maculopathy, lipid measures are
among the strongest correlates available — and specifically **apoB particle number, LDL
particle size, ApoB:ApoA1 ratio and remnant/TG-rich lipoprotein concentration**, which
track better than LDL-C does. This is the model's own resolution of the paradox: the right
analyte was never being measured. The T2D phenotype (§3.2) — high TG, low HDL, small dense
LDL — is exactly the lipoprotein profile that extravasates and is modified.

**(3) The intraretinal arms: magnitude unknown, plausibly larger, and essentially
unmeasured in humans.** Modification to gly-oxLDL (P8.2), retinal FAO failure and
ceramide/DAG lipotoxicity (P8.5/P8.8), and membrane PUFA depletion (P8.4) are all supported
by model systems and by tissue-level human findings, but there is no human assay for any of
them. "Untested" is not "large." The field's repeated lesson — aldose reductase, PKCβ,
antioxidants — is that compelling intraretinal mechanisms with strong animal data fail
clinically. I apply that discount here honestly.

**Net verdict:** the lipid axis is under-served **not because it is the largest driver of
DR, but because it is the largest *untreated* driver of a specific, identifiable, and
currently un-addressed phenotype.** That is a weaker claim than "DR is a lipid disease" and
a stronger claim than "lipids are a minor risk factor." It also dictates the development
strategy: **enrich for the phenotype, do not run all-comers** (§6).

### 4.2 The six sub-processes — and whether a systemic PPARα agonist intervenes

> For each sub-process: mechanism → is it rate-limiting? → would a systemic PPARα agonist
> plausibly intervene, by what route, at which stage, and with what confidence?

---

#### (i) Systemic lipoprotein supply

**Mechanism.** Circulating apoB-containing particle number — LDL, VLDL remnants, and
particularly small dense LDL and TG-rich remnants — sets the concentration of lipoprotein
available to cross a compromised barrier. In the model's framing (§P8.2), intraretinal
modified-LDL concentration ≈ *barrier permeability × particle number × modification capacity*.
Supply is one of three multiplicands.

**Is it rate-limiting?** Only partially. At low permeability (S0), supply is irrelevant
because nothing crosses. At high permeability, supply becomes meaningfully rate-limiting
for the exudative phenotype. Supply is a **permissive modifier whose importance rises with
barrier failure.**

**Would a systemic PPARα agonist intervene? — YES. Unambiguously, and this is the only
limb that survives the scout's exposure objection intact.** PPARα agonism in hepatocytes
induces LPL and APOA5, represses APOC3, and accelerates TG-rich-lipoprotein and remnant
clearance. The target organ is the liver, which concentrates fibrate anions via OATP1B1/1B3
— the exact transport system the retina lacks. **No retinal drug exposure is required.**

**At which stage?** **S1–S3, peaking at S2.** And the stage boundary is sharp and
mechanistically forced: **this limb is inoperative at S0.** With an intact barrier there is
no extravasation, so reducing the supply of a particle that cannot cross produces no
retinal benefit. The limb switches on with the first MAs and leaking capillaries.

**Confidence:** HIGH on the mechanism, MODERATE on the effect size in retina.

**Differentiation within Group A.** This limb ranks: **pemafibrate ≈ fenofibric acid >
elafibranor > seladelpar**. Pemafibrate's potency and hepatoselectivity are *assets* here.
Seladelpar's δ-selectivity is a liability: PPARδ drives FAO in muscle and raises HDL but is
a substantially weaker driver of hepatic apoB/remnant clearance than PPARα. **If the P8.1
supply limb is the operative mechanism, seladelpar should underperform — and that is a
cleaner falsification test than the scout framed it as.**

---

#### (ii) Extravasation through a compromised barrier

**Mechanism.** Inner-BRB failure via PKCβ→occludin Ser490, CLDN5 repression, VEGF→SRC→
VE-cadherin internalisation, plus the often-forgotten transcellular arm (CAV1/PLVAP). Lipid
is *cargo* here, not driver. Upstream of extravasation sits leukostasis: ICAM1-mediated
leukocyte plugging causing FAS/FASLG endothelial apoptosis and capillary dropout.

**Is it rate-limiting?** **Yes — this is the most rate-limiting step of the whole exudative
cascade.** A patient with severe dyslipidemia and an intact barrier does not get hard
exudate. Permeability, not supply, gates the process.

**Would a systemic PPARα agonist intervene? — PARTIALLY, and this is where the exposure
objection bites hardest.** The mechanism is real: ligand-bound PPARα transrepresses
NFKB1/RELA and AP-1, tethering NCoR/SMRT at inflammatory promoters and suppressing ICAM1,
VCAM1, TNF, IL6, CCL2 — without requiring a PPRE. It also raises NOS3, lowers EDN1 and
SERPINE1. That maps directly onto the S2 leukostasis hub.

Two honest qualifications, pointing in opposite directions:

- *Favourable:* the target cell is **retinal capillary endothelium on the luminal side**.
  The drug does not have to cross the BRB — it has to cross one plasma membrane from plasma.
  That is a materially easier ask than reaching Müller cells or photoreceptors, and the
  scout's "BRB attenuation" framing slightly overstates the barrier for this specific limb.
- *Unfavourable:* it is still an intracellular nuclear receptor, and free fenofibric acid at
  ~0.1–0.4 µM against a tens-of-µM EC50 is ~2 logs short **in plasma, before any membrane
  step at all.** Being on the luminal side does not fix a two-log potency deficit. Only
  elafibranor (low-nM, non-hepatoselective) has a credible shot at this limb.

**At which stage?** **S2, extending into S1 and S3.** This is also where the scout's
"bootstrapping problem" applies: retinal exposure improves as the barrier fails, so the drug
arrives in useful quantity only after the process it would prevent has begun. For this limb
that is less damning than it first appears — amplification-limiting at S2 is still valuable
— but it does mean the limb cannot prevent the *first* leak.

**Confidence:** MODERATE on mechanism, **LOW on retinal delivery** for A1/A2/A3;
LOW-to-MODERATE for A4.

---

#### (iii) Intraretinal modification of lipoprotein to a cytotoxic species

**Mechanism.** Once retained, native LDL is glycated and oxidised in situ to "gly-oxLDL,"
which is far more cytotoxic than native LDL: it kills pericytes, drives ER stress
(ATF4/ATF6/CHOP/XBP1s) in capillary endothelium, induces VEGFA and gliosis in Müller cells,
and causes autophagy failure and lipid-droplet accumulation in RPE. **The modification step
is what converts a passive deposit into an active toxin.**

**Is it rate-limiting?** Plausibly yes, and it is the step the model argues resolves the
clinical paradox — it explains why plasma LDL-C tracks DR poorly while intraretinal lipid
toxicity is real. The rate depends on retinal oxidative capacity, methylglyoxal/dicarbonyl
load (P2), and residence time, not on plasma cholesterol.

**Would a systemic PPARα agonist intervene? — WEAKLY, and this is the sub-process where
PPARα is the *wrong tool*.** Two indirect arms exist: PPARα directly induces **catalase
(CAT)** — a genuine, canonical PPARα target gene — and reciprocally induces NFE2L2. But
(a) both require retinal receptor occupancy, (b) catalase is not the rate-limiting
antioxidant for lipoprotein oxidation (that is more a lipid-phase problem — GPX4,
peroxyl-radical chemistry, transition-metal availability), and (c) the glycation half of
"gly-oxLDL" runs on methylglyoxal chemistry governed by **GLO1**, which PPARα does not
control. PPARα also reduces residence time only indirectly, by reducing how much arrives.

**Cross-candidate finding worth flagging to the ranker:** **dimethyl fumarate fits this
sub-process better than any PPARα agonist does.** NRF2 activation induces GLO1 (the
methylglyoxal detoxifier, directly addressing the glycation arm), GCLC/GCLM/GSR (the GSH
pool, depleted by the P1 NADPH drain), GPX4 (the phospholipid-hydroperoxide reductase and
ferroptosis brake), and the GST/ALDH aldehyde-detox set. That is a mechanistically precise
match to "modification of retained lipoprotein and its downstream aldehyde products" — and
it hits the glycation arm that PPARα cannot touch.

**At which stage?** S2–S3. **Confidence:** LOW for PPARα; MODERATE for an NRF2 agent.

---

#### (iv) Hard-exudate deposition — and the egress problem

**Mechanism.** Retained lipoprotein concentrates in the outer plexiform (Henle) layer as
water is resorbed by RPE pumping and Müller aquaporin transport. Macrophages and activated
microglia take up modified lipoprotein via **CD36, OLR1 (LOX-1), MSR1**, become foam cells,
fail to efflux the cholesterol, die, and release it again. The result is a persistent plaque.
Subfoveal hard exudate is, per the model, **the single worst local prognostic sign in DME** —
it organises into a subretinal fibrotic plaque causing permanent central scotoma even in an
anatomically dried eye. Anti-VEGF does not clear it, and exudate can paradoxically *increase*
as fluid resorbs and lipid concentrates.

**Is it rate-limiting?** For vision outcome in the exudative phenotype, deposition at the
fovea is the terminal, irreversible event. Egress is rate-limiting for resolution, and
egress depends on **ABCA1/ABCG1 → ApoA1/ApoE acceptors under LXRα/β control** — a system the
model says is **downregulated in diabetic retina and in human diabetic donor eyes.**

**Would a systemic PPARα agonist intervene? — PARTIALLY, on the deposition side only, and
with one speculative egress limb worth stating because nothing else in the set has one.**

- *Deposition (supported):* less supply (i) + less leak (ii) = less new exudate. This is
  genuine and is the main claim PPARα can make here. It is **prevention of new exudate**,
  not clearance of existing plaque.
- *Egress (speculative, `[EMERGING]`):* PPARα directly induces **ABCA1** and **APOA1**.
  Two routes follow. Retinal/macrophage ABCA1 induction requires retinal occupancy —
  exposure-limited, so weak. But hepatic APOA1 induction raises **circulating ApoA1/HDL**,
  and in a retina whose barrier is leaking enough to admit a ~500 kDa LDL particle, a
  ~28 kDa ApoA1 will also cross. That would deliver a **cholesterol acceptor into the
  interstitium at exactly the sites where lipid is retained** — i.e. the same barrier failure
  that causes the lesion could deliver part of the remedy. This is the only efflux-side
  argument available to any candidate in the set. It is mechanistically coherent, entirely
  untested, and I mark it `[EMERGING / speculative]`. It is worth a specific question to
  the pathway and literature agents.
- *Not addressed at all:* an organised, fibrotic subfoveal plaque. Nothing reverses that.
  Transcriptional pharmacology does not remove a scar.

**At which stage?** **S2 onward, and prevention ≫ clearance.** This has a direct and
uncomfortable trial-design consequence: the obvious enrichment biomarker (existing hard
exudate) selects patients in whom the mechanism is weakest. See §6.3.

**Confidence:** MODERATE on prevention; LOW/speculative on egress.

---

#### (v) Retinal fatty-acid oxidation and ceramide/DAG lipotoxicity

**Mechanism.** Retinal fuel use is compartmentalised: photoreceptors are intensely
glycolytic; the RPE β-oxidises the DHA-rich lipid it phagocytoses daily from shed outer
segments and exports ketones back to photoreceptors (HMGCS2); Müller cells sit between. In
diabetes, substrate oversupply plus impaired CPT1A-mediated mitochondrial import and reduced
ACOX1 peroxisomal oxidation produces **lipid-droplet accumulation in RPE and Müller cells,
acylcarnitine intermediates, ceramide and DAG accrual**, and lipotoxic ER/mitochondrial
stress. Two high-value consequences:

- **Ceramide → pericyte and endothelial apoptosis** (P8.5). Pericyte dropout is the *first
  structural lesion of DR* (S1). A mechanism that reduces retinal ceramide load is aimed
  directly at the earliest lesion in the disease.
- **DAG → PKCβ** (the P8→P3 bridge the model explicitly flags). Normalising retinal lipid
  handling reduces PKC activation **without being a kinase inhibitor** — which matters,
  because direct PKCβ inhibition is one of the field's named failures.

**Is it rate-limiting?** Plausibly, for S0–S1 progression. This is the only P8 sub-process
that operates **before any barrier failure** — it is intrinsic metabolic failure, not an
extravasation consequence.

**Would a systemic PPARα agonist intervene? — YES IN PRINCIPLE; this is the canonical PPARα
module (CPT1A, ACOX1, HMGCS2, FABPs are all direct target genes). But this is the limb most
dependent on retinal receptor occupancy, and therefore the limb most damaged by the scout's
arithmetic — and the limb pemafibrate's hepatoselective design actively defeats.**

**At which stage? S0–S1 — and this is the crux of the entire report.**

> **The stage offset, stated precisely.**
>
> | PPARα limb | Stage it acts at | Exposure case |
> |---|---|---|
> | (i) systemic supply | **S1–S3** (requires a leaking barrier) | **Strong — no retinal exposure needed** |
> | (v) retinal FAO / ceramide / DAG | **S0–S1** (operates before barrier failure) | **Weakest in the hypothesis** |
>
> The #1 unmet need is S0–S2 disease modification. PPARα's exposure-robust limb switches on
> at S1 and is strongest at S2. PPARα's S0 limb is the one the exposure arithmetic most
> undermines. **The mechanism and the unmet need are offset by one stage.** An honest
> development plan therefore targets **S1–S2 (mild-to-moderate NPDR with dyslipidemia and
> early exudate), not S0**, and should say so rather than claiming the S0 window.

**Confidence:** HIGH that the biology matters; **LOW** that a systemic fibrate engages it.

---

#### (vi) Photoreceptor membrane lipid turnover

**Mechanism.** The retina has the highest DHA content of any human tissue; outer-segment
discs are ~50% DHA by fatty acid. Beyond DHA, photoreceptors synthesise **VLC-PUFAs (≥C28)
via ELOVL4**, required for disc membrane curvature — and *ELOVL4* mutations cause
Stargardt-like macular dystrophy, which is hard Mendelian proof that this lipid class is
critical to macular survival. **ADIPOR1** is required for retinal DHA retention; its loss
causes photoreceptor degeneration. In diabetes, retinal DHA and VLC-PUFA fall and the
n-6:n-3 ratio shifts toward arachidonate, reducing generation of specialised pro-resolving
mediators (resolvins, NPD1, maresins) — i.e. **failure of inflammation *resolution*, not
just excess initiation.**

**Is it rate-limiting?** For photoreceptor-driven oxidative burden, plausibly yes. The model
makes a counterintuitive and important claim (§P9): the photoreceptor is a *source* of the
oxidative and inflammatory burden, not merely a victim, and models lacking photoreceptors
show markedly less vascular disease. **That means outer-retinal lipid biology has a vascular
pay-off** — which is the strongest argument in the model for an outer-retina-directed agent.

**Would a systemic PPARα agonist intervene? — INDIRECTLY AND AMBIGUOUSLY. Direction is
genuinely uncertain and I will not pretend otherwise.**

- *Argument for:* the final step of DHA biosynthesis (the Sprecher pathway) is a
  **peroxisomal β-oxidation** retroconversion of 24:6n-3 → 22:6n-3, and **ACOX1 is a direct
  PPARα target gene**. PPARα agonism could therefore support DHA synthesis. This is a real,
  non-obvious positive link.
- *Argument against:* PPARα is the master regulator of fatty-acid **catabolism**. Upregulating
  peroxisomal and mitochondrial β-oxidation in a tissue whose problem is PUFA *depletion* could
  plausibly accelerate the loss of the very species it needs to retain.
- Neither arm touches ELOVL4 or ADIPOR1, which are the genetically validated nodes.

**At which stage?** S0 (and continuously). **Confidence: LOW, direction `[UNCERTAIN]`.**

**Better-matched candidates:** **icosapent ethyl** (direct n-3 substrate supply, membrane
incorporation, AA displacement, E-series resolvin precursor — and it is the only candidate
in the set that addresses the *resolution-failure* framing the model calls under-exploited)
and, more weakly, **α-linolenic acid** (direction-correct but with inefficient human
conversion to EPA/DHA). Important honesty: **EPA is not DHA.** The retina's critical species
are DHA and the ELOVL4-derived VLC-PUFAs; EPA→DHA retroconversion in humans is limited. So
even B4 addresses this sub-process only partially.

### 4.3 P8 summary verdict

| Sub-process | Would a systemic PPARα agonist intervene? | Stage | Confidence |
|---|---|---|---|
| (i) systemic lipoprotein supply | **YES — robustly, no retinal exposure needed** | S1–S3 (inoperative at S0) | HIGH |
| (ii) extravasation / barrier | **PARTIALLY — luminal endothelial target, but ~2 logs short on free drug** | S1–S3 | LOW–MODERATE |
| (iii) intraretinal modification | **WEAKLY — wrong tool; NRF2 fits better** | S2–S3 | LOW |
| (iv) hard-exudate deposition | **PARTIALLY — prevention yes, clearance essentially no** | S2+ | MODERATE / speculative on egress |
| (v) retinal FAO & ceramide/DAG | **IN PRINCIPLE YES — but this is the most exposure-fragile limb** | **S0–S1** | HIGH biology / LOW delivery |
| (vi) photoreceptor membrane PUFA | **INDIRECTLY, direction ambiguous** | S0 | LOW, `[UNCERTAIN]` |

**Two or three of six sub-processes are credibly addressed, one of them (i) very well and
without needing to reach the retina at all. The two sub-processes that act earliest — (v)
and (vi) — are the two the agonist is least likely to engage.**

---

## 5. (d) DME PHENOTYPE MATCHING AND THE ENRICHMENT BIOMARKER

### 5.1 Phenotype coverage across the set

| DME phenotype | Mechanism | Covered by | Coverage |
|---|---|---|---|
| **Lipid / exudative** | Lipoprotein extravasation + in-situ modification; hard exudate, circinate rings | **A1–A4, B4** | **✓ — the set's best-matched phenotype, supply side only** |
| **Inflammatory** | Hyperreflective foci, subretinal fluid, high vitreous IL-6/MCP-1 | A1/A2/A4 (transrepression, exposure-limited), **D2, D3** | **✓** |
| **Ischemic / mixed** | DRIL, enlarged FAZ, macular nonperfusion | **none** | **✗ EMPTY** (and the model says anti-VEGF may worsen perfusion here) |
| **Müller-cytotoxic** | Kir4.1/AQP4 uncoupling → cellular swelling | **none** | **✗ EMPTY** |
| **Outer-BRB pump failure** | RPE Na/K-ATPase, AQP1, CFTR/bestrophin; subretinal fluid | A-group speculative (RPE FAO/ketogenesis restoring pump energetics) | **✗ effectively empty** |

### 5.2 Which phenotype does a PPARα agonist serve?

**Primary: the lipid/exudative phenotype.** Unambiguously. It is the only phenotype whose
defining lesion is produced by the exact process PPARα's robust limb modulates.

**Secondary: the inflammatory phenotype**, via NF-κB transrepression — but this is
exposure-limited and in practice the weaker claim.

**Not served: ischemic, Müller-cytotoxic, outer-BRB pump failure.** Three of five phenotypes.

This matters enormously for unmet need #2. The 30–50% anti-VEGF incomplete-responder
fraction is **not one population** — the model lists six distinct mechanistic explanations
(inflammatory phenotype, kallikrein-driven permeability, Müller cytotoxic edema, outer-BRB
pump failure, macular ischemia, lipid burden). A PPARα agonist addresses **one, possibly
one-and-a-half, of six.** An all-comers incomplete-responder trial dilutes a real effect in
one sixth of the population across six mechanisms. **That is, on its own, sufficient to
explain a null result from a mechanistically correct drug.**

### 5.3 The enrichment biomarker — be specific

Candidate markers, ranked by how directly each proves the phenotype is present:

| Rank | Marker | What it proves | Strength | Weakness |
|---|---|---|---|---|
| **1** | **OCT hyperreflective foci (HRF) in the OPL/ONL, plus subretinal/subfoveal lipid** | Lipid has *already crossed and been retained* — proves both barrier failure and arrival | Quantifiable on dense volume scans, reproducible, responsive over months, available on existing clinic hardware | **HRF are not lipid-specific** — inner-retinal HRF are likely migrating microglia. Must specify location and morphology |
| **2** | **Hard exudate area on colour fundus photography (ETDRS grid)** | The phenotype itself, directly | Cheap, gradable, LMIC-deployable, a reading-centre-validated endpoint | Coarse; insensitive at low burden; misses pre-visible lipid |
| **3** | **Remnant cholesterol (non-HDL-C − LDL-C) and/or apoB** | Systemic supply is elevated | **Computable from a standard lipid panel at zero marginal cost**; the model states apoB/particle number tracks DR and exudate better than LDL-C | Risk factor for the phenotype, not proof of it |
| 4 | Serum triglycerides alone | Weak proxy for remnants | Universally available | Poorest discrimination of the four; do not use alone |
| 5 | Serum Lp-PLA2 (PLA2G7) activity | The lipoprotein-associated modification arm | Travels with LDL; generates lysoPC at retention sites | Research-grade; not validated for this use |
| 6 | Vitreous/aqueous FABP4, IL-6, MCP-1 | Direct intraocular phenotyping | Most specific | Requires a tap; only feasible in eyes already being injected |

**Recommended enrichment gate — a two-gate design:**

> **Gate 1 (systemic supply present):** T2DM **and** elevated remnant cholesterol
> (≈ ≥0.8 mmol/L / ≥30 mg/dL) or elevated apoB.
> **Gate 2 (intraretinal lipid demonstrably arriving):** ≥1 hard exudate within the ETDRS
> grid **or** OPL/ONL hyperreflective-foci count above a prespecified threshold —
> **but excluding eyes that already have organised subfoveal lipid plaque.**

**Why both gates, and why the exclusion.** Gate 1 alone selects a risk factor, not a
phenotype — most dyslipidemic diabetics have no exudate. Gate 2 alone would admit patients
with normal lipoprotein supply, in whom the supply limb has nothing to lower. Together they
select patients in whom all three multiplicands of the model's equation (permeability ×
particle number × modification) are demonstrably non-zero.

The exclusion matters because of the §4.2(iv) finding: **PPARα prevents new exudate far
better than it clears old exudate.** Enriching naively on "worst exudate burden" would
select the patients in whom the mechanism is weakest — a self-defeating enrichment. The
target is the **window phenotype**: lipid is arriving, but has not yet organised at the
fovea. This is a specific and, I think, non-obvious trial-design point.

**Endpoint, matched to the enrichment.** BCVA is the wrong primary endpoint for this
population — it is insensitive until the fovea is involved, which is the event you are trying
to prevent. Use **change in hard exudate area and OPL HRF count**, with **proportion
developing new subfoveal lipid** as the clinically meaningful binary, and **BCVA plus
injection-count reduction** (unmet need #4) as secondaries. Exudate area on colour photography
is reading-centre-gradable and LMIC-deployable, which fits the oral-agent thesis.

**Enrichment is plausibly the difference between a failed and a successful trial here, and
the single most important variable is Gate 2, not Gate 1** — because Gate 2 proves the
barrier is passing lipoprotein, which is the step that gates everything downstream.

---

## 6. (e) NEUROPROTECTION (P9) AND THE S0 WINDOW

### 6.1 Which candidates have a plausible neuroprotective limb?

| Rank | Candidate | Neuroprotective mechanism | Reaches neural retina? | Verdict |
|---|---|---|---|---|
| **1** | **C2 Melatonin** | Anti-apoptotic, mitochondrial, microglial modulation; MT1/MT2 present in retina | **Yes — freely. MW 232, neutral, physiologically synthesised in retina** | **The only candidate with unambiguous access to the S0 compartment.** Its purpose in this set is to test whether access beats affinity |
| **2** | **D3 Minocycline** | Microglial deactivation — ramified→amoeboid transition is an S0 event; also MMP9, IL1B, TNF | **Yes — CNS-penetrant** | **The most mechanistically specific P9 agent in the set.** Microglial priming is the S0 inflammatory amplifier |
| **3** | **D2 Dimethyl fumarate** | NRF2 in neurons and glia; mitochondrial protection; IL6/IL1B transrepression | **Likely (§6.3)** | Neuroprotective in a different CNS context (non-DR knowledge); strong mechanistic fit to the oxidative component of RGC loss |
| 4 | A1/A2/A4 (PPARα) | Reported: ↓RGC apoptosis, preserved ERG, ↓GFAP gliosis, ↓microglial activation, via AMPK/SIRT1/PGC-1α, Wnt inhibition, ↓ceramide | **Exposure-limited** | Real in models. The model warns: "a target reported to improve everything in animal models warrants scepticism." Effect size `[UNCERTAIN]` |
| 5 | B4 / B2 (n-3) | Membrane PUFA, SPM-mediated resolution | Partially | Slow, modest, direction-correct |
| 6 | D4 Candesartan | AT1R on Müller/RGC | Abluminal targets poorly reached | BP lowering is not neuroprotection; do not conflate |
| 7 | C1 Quercetin | Claimed broadly | **No** — <2% oral bioavailability | Not credible |

**Finding: the neuroprotective limb of this candidate set belongs almost entirely to the
non-PPARα arm.** The three best P9 candidates are the exposure control and two of the four
mechanistic comparators. If the pipeline's output is "PPARα for early DR," the
neuroprotection claim in that output will be the weakest part of it.

### 6.2 How would benefit be measured at S0?

Ranked by biological aptness × reproducibility × regulatory realism:

| Endpoint | What it measures | Reproducibility | Timescale | Assessment |
|---|---|---|---|---|
| **mfERG implicit time** | Localised outer/middle retinal function; delayed implicit time is among the earliest and most reproducible DR abnormalities and *predicts where lesions later appear* | Good | **12 months** | **Best primary biomarker endpoint for S0.** Predictive, localisable, responsive within a tractable trial duration |
| **OCT GCL-IPL thickness** | Structural RGC loss — the canonical S0 readout | **Excellent (~1–2 µm)** | **24–36 months** | **Best co-primary structural endpoint**, but thinning is slow (~0.5–1 µm/yr), so it needs duration and N |
| **Microperimetry (mean sensitivity, dB)** | Localised retinal function; correlates with DRIL and with real-world vision | Moderate (test-retest ~2–3 dB) | 12–24 months | **Best *clinically meaningful* functional endpoint.** Needs averaging/large N |
| **Pattern ERG** | RGC-specific function | Moderate | 12–24 months | Good mechanistic confirmation; more technically demanding than mfERG |
| **Flicker-induced retinal vasodilation** | Neurovascular coupling — the unit itself | Moderate; limited equipment base | 6–12 months | **The most mechanistically apt endpoint in the disease** and the fastest-responding. Weakest infrastructure |
| **DRIL** | Inner-retinal architectural failure | Good | — | **An established-DME marker, not an S0 marker.** Use as a prognostic stratifier and in the DME arm; it is the wrong S0 endpoint |

**Recommended S0 endpoint package:** mfERG implicit time (primary biomarker) + GCL-IPL
thickness and microperimetry (co-secondaries) + flicker-induced vasodilation in a mechanistic
substudy. **DRIL belongs in the DME arm, not the S0 arm.**

**The honest caveat the model already states:** none of these is regulatorily qualified.
DRSS cannot move from a stage with no lesions, so an S0 trial must either use an unqualified
functional endpoint or run long enough to capture incident DRSS progression — which converts
an S0 trial into a multi-year S0→S1/S2 prevention trial. **For a candidate set this early,
endpoint risk exceeds pharmacological risk**, and the regulatory-strategy agent should treat
that as the gating issue.

---

## 7. (f) WHERE THE CANDIDATE SET FAILS THE DISEASE

### 7.1 Ranked gap table

| Rank | Gap | Module / stage | Covered by | Why it ranks here |
|---|---|---|---|---|
| **1** | **Egress of deposited intraretinal lipid** | **P8.3 / S2–DME** | **Nothing** | Inside this run's own declared under-served axis; all 15 candidates act on supply, none on clearance; target class is known and tractable; pairs with unmet need #5, which nothing addresses |
| **2** | **Müller cytotoxic edema (Kir4.1/AQP4 uncoupling)** | S0/DME | **Nothing** | **Larger in absolute population terms** — a named contributor to the 30–50% incomplete-responder fraction, invisible to every anti-permeability mechanism. Ranks below #1 only because the target class is far less tractable (ion-channel localisation, not ligand occupancy) |
| **3** | **VEGF-independent permeability via kallikrein–kinin** | S4/DME | Nothing | KLKB1/F12/BDKRB1-2 are druggable, have human vitreous validation (C-level), and are orally tractable in principle. The model's own note that it needs phenotype enrichment makes it a good fit for this pipeline's enrichment logic |
| **4** | **Macular ischemia / capillary reperfusion** | S3/DMI | Nothing | Highest scientific value, no validated path anywhere. Not a failure of *this* set |
| **5** | **Anti-fibrotic for S5** | S5 | Nothing | Smaller population, surgical alternative exists. Legitimately deprioritised |
| 6 | Direct P3 (PKC) agent | P3 / S1–S2 | Nothing direct | Correctly deprioritised — a named clinical failure |
| 7 | P4 hexosamine | P4 | Nothing | Correctly empty — model rates it pharmacologically unattractive |

### 7.2 The largest uncovered gap, stated explicitly

> **THE LARGEST UNCOVERED GAP: there is no efflux/clearance mechanism for intraretinal lipid.
> The candidate set covers the afferent half of P8 and leaves the efferent half completely
> empty.**
>
> Every one of the fifteen compounds reduces, redirects or detoxifies what *arrives* in the
> retina. None accelerates what *leaves*. For a disease whose signature P8 lesion is a
> persistent lipid plaque that anti-VEGF does not clear, that paradoxically increases as
> fluid resorbs, and that causes permanent subfoveal scotoma even in an anatomically dried
> eye, the clearance side is the half that determines the vision outcome once deposition has
> occurred — and it is the half that is untouched.

**The compound profile that would fill it:**

- **Target:** the reverse-cholesterol-transport axis the model says is *downregulated in
  diabetic retina and in human diabetic donor eyes* — **LXRα/β (NR1H3/NR1H2) agonism →
  ABCA1/ABCG1 induction**, with **ApoA1/ApoE acceptor supply**; and/or **scavenger-receptor
  blockade (CD36, OLR1, MSR1)** to stop the foam-cell death–release cycle that regenerates
  the deposit. CYP46A1/CYP27A1 induction (side-chain oxidation to membrane-permeable,
  exportable oxysterols) is an adjacent route.
- **Compartment:** must reach **Müller cells, microglia/macrophages and RPE** in the outer
  plexiform layer — i.e. this is a *neural-retina* target, not a plasma target. Unlike the
  PPARα supply limb, this one cannot be done from the liver.
- **Physicochemistry:** neutral or weakly basic, **MW < 400, cLogP 2–4, TPSA < 70, HBD ≤ 2,
  not a P-gp/BCRP substrate, PPB < 98%** — explicitly *not* the lipophilic-carboxylic-acid
  chemotype that the entire Group A occupies and that §6.2 of the model penalises.
- **Stage:** S2 onward, deployed on the **window phenotype** of §5.3.
- **Known liability to design against:** systemic LXR agonism causes hepatic steatosis and
  hypertriglyceridemia via SREBP-1c induction — which would *worsen* the P8.1 supply limb.
  This argues for an **LXRβ-biased or non-steatotic LXR modulator**, or for the ApoA1-mimetic
  / scavenger-receptor route instead. A systemic pan-LXR agonist would be self-defeating in
  this disease.
- **Elegant combination logic:** a supply-side agent (PPARα) plus an egress-side agent
  (LXR/ABCA1/ApoA1) is a mechanistically non-redundant pair covering both halves of P8 — and
  notably, **PPARα itself induces ABCA1 and APOA1**, so a PPARα agonist is the weakest
  possible version of the egress agent and the strongest version of the supply agent. The
  combination agent is the one the set is missing.

**Secondary profile, for gap #2:** a **Kir4.1 (KCNJ10) localisation restorer or AQP4
modulator** reaching Müller endfeet — no credible chemical matter exists, which is why that
gap persists despite its size.

---

## 8. (g) THE ANGPTL4 STAGE-DEPENDENCY QUESTION

### 8.1 Does the risk–benefit invert?

**Yes — and the inversion is driven from both ends at once, which makes it steeper than it
first appears.**

**The mechanism.** ANGPTL4 is a **direct PPARα target gene** with a PPRE; agonism predicts
its induction wherever PPARα is occupied. Its retinal biology is bidirectional and
proteolytically split: the **N-terminal coiled-coil domain inhibits LPL** (raising TG — i.e.
working *against* the P8.1 supply limb), while the cleaved **C-terminal fibrinogen-like
domain acts on retinal endothelium to increase permeability and promote angiogenesis,
partly through integrin/neuropilin engagement and junctional disruption, and substantially
independently of VEGF.** It is also **HIF-inducible**.

**Why stage matters.**

| | S0–S2 (non-ischemic) | S3–S4 (ischemic/proliferative) |
|---|---|---|
| Baseline retinal ANGPTL4 | Low — no HIF drive | **Already elevated by HIF** |
| Added PPARα input | Adds a second, independent transcriptional input (PPRE ≠ HRE) | Adds the same input **on top of an existing hypoxic stimulus** |
| Expected net effect | Small absolute increase from a low base; plausibly inconsequential against the lipid + transrepression benefit | **Additive by default** — distinct response elements do not share a ceiling. Increase from an already-pathological base |
| Benefit available | **Real**: supply reduction, transrepression, FAO | **Near zero** — scout §5.3: PPARα cannot touch HIF-driven VEGFA, cannot reverse structure, cannot restore lost cells |
| Risk | Low | **Maximal — pro-permeability and pro-angiogenic input into an already neovascularising retina** |

**The inversion.** Benefit falls monotonically from S2 to S4 (because PPARα's mechanisms are
preventive and metabolic, and S4 pathology is structural and hypoxia-driven). Risk rises
monotonically over the same interval (because ANGPTL4 is HIF-co-regulated and the tissue is
primed to respond to a permeability/angiogenic signal). **A ratio whose numerator falls while
its denominator rises degrades faster than either term alone.** The risk–benefit does not
merely weaken toward late disease — it inverts.

One genuine caveat against over-reading this: the fibrate class demonstrably lowers
triglycerides in humans, so hepatic/adipose ANGPTL4 induction evidently does not dominate
the systemic LPL effect (APOC3 repression and LPL induction outweigh it). That tells us the
induction is not overwhelming *systemically*. It tells us nothing about the **local retinal**
balance in a tissue where ANGPTL4 is already HIF-driven — which is the case that matters.

### 8.2 Does it argue for stage-restricted use? — Yes, and concretely

**Recommended stage restriction for any PPARα-agonist DR programme:**
- **Include:** mild-to-moderately-severe NPDR, approximately DRSS 35–47 (and arguably to 53
  only with the surveillance below).
- **Exclude:** any proliferative disease (DRSS ≥ 61); prior or active neovascularisation,
  including NVI/NVA; vitreous hemorrhage.
- **Exclude or stratify:** eyes with significant macular nonperfusion (enlarged FAZ on OCT-A)
  or substantial peripheral nonperfusion on widefield FA — these are the eyes with the
  highest HIF tone and therefore the highest ANGPTL4 baseline, i.e. the eyes where additivity
  is most likely to bite.
- **Note the interaction with §5.3:** the lipid/exudative enrichment gate and the ANGPTL4
  stage restriction are **compatible and mutually reinforcing** — exudative maculopathy is a
  predominantly non-proliferative, T2D phenotype. The two constraints select the same patient.
  That is a fortunate convergence and strengthens the overall development case.

### 8.3 Would a late-stage trial be actively dangerous?

**Calibrated answer: not demonstrably dangerous, but it should not be the lead indication,
and it cannot ethically be run without active neovascular surveillance.**

I decline to say "actively dangerous," because the evidence is a mechanistically predicted
wrong-sign limb, not an observed harm. But three considerations make the hazard serious
enough to design around:

1. **Asymmetry of error.** If the hypothesis is wrong in early NPDR, the cost is a negative
   trial and lost time. If it is wrong in proliferative disease, the cost is irreversible
   vision loss from vitreous hemorrhage or tractional detachment, within months, in eyes that
   had an effective alternative therapy available.
2. **No offsetting benefit to justify the risk.** At S4, every mechanism PPARα offers is
   either irrelevant (structural lesions, HIF-driven VEGFA) or redundant with an already
   effective modality. There is no upside against which to price the hazard.
3. **The hazard is co-located with the existing standard of care.** S4 patients are already
   receiving effective intravitreal therapy; adding a systemic agent with a plausible
   pro-angiogenic limb inverts the usual adjunct calculus.

**Required mitigations if a late-stage trial is run at all:**
- Prespecified **DMC with unmasked review of neovascular events** (new NVD/NVE, vitreous
  hemorrhage, progression to high-risk PDR) — these are the ANGPTL4-predicted events and must
  be adjudicated as safety signals, not merely counted as efficacy failures.
- A protocol stopping rule on progression to high-risk PDR characteristics.
- **Measure the mechanism directly:** ANGPTL4 in aqueous (and vitreous where a tap is already
  clinically indicated) in treated vs untreated eyes. This is feasible — these patients
  undergo intraocular procedures routinely — and it converts a theoretical liability into a
  measurable one. **This is the single highest-value de-risking experiment in the programme.**

### 8.4 The molecule-selection consequence — and a direct inversion of the scout's logic

The scout treats pemafibrate's hepatoselectivity as a liability: it suppresses the
extrahepatic exposure a retinal mechanism needs. **Under the ANGPTL4 argument, that same
property is a safety asset** — a hepatoselective SPPARMα minimises retinal PPARα occupancy
and therefore minimises retinal ANGPTL4 induction, while fully preserving the systemic
supply limb, which is the limb most likely to be doing the work in the first place.

| | Retina-intrinsic hypothesis | Supply-side hypothesis |
|---|---|---|
| Best molecule | **Elafibranor** (low-nM, non-hepatoselective) | **Pemafibrate** (potent, hepatoselective, CKD-safe) |
| Hepatoselectivity is | a **liability** | an **asset** — including on ANGPTL4 safety |
| ANGPTL4 retinal risk | **Highest** — the mechanism you want is the mechanism that induces it | **Lowest** |
| Falsifiable by | pemafibrate failing where elafibranor succeeds | seladelpar and melatonin performing comparably |

**The two considerations point in opposite directions, and which dominates depends entirely
on which mechanism in §4.2 is operative.** The ranker must be handed this as a fork, not a
single name — which is precisely what the scout concluded for different reasons. **The
remarkable thing is that the retinal-exposure argument and the ANGPTL4 argument are the same
argument with opposite signs: whatever retinal PPARα occupancy you achieve buys you the FAO
limb *and* the ANGPTL4 liability together. You cannot have one without the other.**

---

## 9. Per-candidate disease-biology assessment

Scores are **disease-biology fit** — (pathway × stage × compartment × route) match to the
ranked unmet needs — not overall development scores. ADMET, safety and feasibility agents
will apply their own lenses. Per the brief, any score ≥7 carries an explicit falsification
statement.

### A3 — Pemafibrate — **7.0**
Strongest supply-side P8.1 engagement in the set and the only Group A molecule comfortable in
a CKD-dominant population. Hepatoselectivity removes the S0 limb entirely and minimises the
retinal FAO/ceramide arm — but under §8.4 that same property reduces retinal ANGPTL4 risk.
**Falsifier:** if a trial in the §5.3-enriched population shows no reduction in hard exudate
area or OPL HRF count despite confirmed apoB/remnant lowering, the supply-side mechanism —
and with it this score — fails. Secondarily: if seladelpar matches it, the α-specific claim fails.

### A1 — Fenofibric acid — **6.5**
Best drug-likeness in class (QED 0.85, D), broadest P8+P6 mechanism coverage, cheap and
chronically dosed. Downgraded against A3 on renal elimination as the acyl glucuronide in a
population where the brief states renal impairment is the norm, plus the creatinine rise that
confounds eGFR monitoring and the myopathy interaction with concurrent lipid-lowering therapy.
Weak µM potency against ~99% PPB makes its retinal limbs largely notional.

### D2 — Dimethyl fumarate — **7.0**
The set's best pure pathway × stage × compartment fit. Hits the **upstream ROS/NRF2 node** the
model nominates as the highest-leverage point (Brownlee logic: blocking one downstream branch
is leaky; restoring the NRF2 arm hits four). Covers P5 (`●●●`), P2 via GLO1 — the methylglyoxal
arm no PPARα agent touches — P6 via IL6/IL1B transrepression, and **P8.7** (GPX4/ferroptosis,
GST/ALDH aldehyde detox) — i.e. it is inside the under-served lipid axis too. Spans S0–S2,
the widest early-stage window in the set. The model's "penalise antioxidants" prior does **not**
apply: NRF2 nuclear translocation is *impaired* in diabetic retina, so KEAP1 inhibition restores
a deficient system rather than adding stoichiometric scavenger — structurally the identical
argument the model uses to defend PPARα. **Best physicochemistry in the set** (MW 144, PSA 52.6,
Ro5v 0, D) with a specific uptake hypothesis (§6.3 of the model: RPE SLC16A/MCT monocarboxylate
transporters; MMF is a small monocarboxylate of roughly lactate dimensions). **Falsifiers:**
(1) if MMF proves to be an MCT/NaDC non-substrate with an efflux ratio >2, the compartment
argument collapses and this becomes a systemic anti-inflammatory with no retinal reach;
(2) chronic lymphopenia at the exposures required would be disqualifying in a diabetic
population with elevated infection risk, independent of efficacy.

### A2 — Fenofibrate — **6.0**
Mechanistically identical to A1 after obligate esterase conversion (confirmed in project data).
Adds formulation and food-effect variance and a further conversion step; subtracts nothing.
Scored marginally below its own active moiety on that basis. Retained as the
prodrug/exposure comparator the scout intended.

### B4 — Icosapent ethyl — **6.0**
The broadest *sub-module* P8 coverage in the set: supply (P8.1 TG/remnant lowering), substrate
(P8.4 membrane incorporation), and — uniquely — the **resolution arm (P8.6)**, generating
E-series resolvin precursors and displacing arachidonate. The model explicitly calls failure
of inflammation *resolution*, not just excess initiation, an under-exploited framing; B4 is
the only candidate that speaks to it. Concerns: EPA is not DHA, and the retina's critical
species are DHA and the ELOVL4-derived VLC-PUFAs; the bleeding/AF signal is a **stage-specific
hazard** mirroring ANGPTL4 — vitreous hemorrhage risk in S4 disease in an antiplatelet-treated
population — which argues for the same S1–S3 restriction.

### D4 — Candesartan cilexetil — **6.0**
The only candidate whose target **does not require crossing the BRB**: AT1R is a cell-surface
GPCR on the luminal endothelial membrane, directly accessible from plasma. The local retinal
RAS is genuine (Ang II → NOX → VEGF, inflammation, RGC loss; the counter-regulatory
ACE2→Ang-(1-7)→MAS1 arm suppressed), and the model notes diabetes abolishes retinal
autoregulation so systemic BP excursions transmit directly to capillaries — making BP control
mechanistically on-pathway at S1, not merely a background risk factor. Only candidate reaching
S3. Already indicated in this exact comorbidity profile, so the chronic-safety bar is cleared.
Concerns: zero P8 and minimal P9 coverage; hyperkalemia with CKD plus other RAS agents;
hypotension in autonomic neuropathy; and **teratogenicity — contraindicated in pregnancy,
which the model names as the window of most rapid DR acceleration in T1DM.**

### C2 — Melatonin — **5.5**
The exposure control, and it does its job. MW 232, neutral, crosses the BRB freely,
synthesised in the retina — the only candidate with unambiguous access to the S0 compartment,
and the best P9 reach in the set. Null for PPARα (the project's rows are
cisplatin-protection expression associations only), so it cannot test the PPARα hypothesis —
it tests whether access beats affinity. Concerns: MTNR1B genetics link melatonin receptor
signalling to impaired insulin secretion and higher fasting glucose (non-DR human genetics),
so chronic exogenous dosing in T2D carries a real glycemic concern; circadian perturbation in
a photoreceptor-driven system; zero P8 coverage; and the "antioxidant as sole mechanism"
prior partially applies. **If melatonin matches or beats the fibrates on any retinal readout,
the exposure objection is confirmed as the dominant variable in this whole analysis.**

### D3 — Minocycline — **5.5**
The most mechanistically specific P9 agent: microglial deactivation targets the S0
inflammatory amplifier directly, plus MMP9/IL1B/TNF at S2, with genuine CNS penetration and
oral dosing. Concerns are all about **chronic lifelong use**: idiopathic intracranial
hypertension (an *ocular* adverse event — papilledema and vision loss — which is a
particularly poor fit for an ophthalmic indication), vestibular toxicity, pigmentation,
drug-induced lupus, and multi-year antibiotic exposure with microbiome and resistance
consequences. Mechanistically apt, pharmaceutically awkward.

### A4 — Elafibranor — **5.5**
Best retinal-occupancy case in Group A: low-nM dual PPARα/δ with no hepatoselective design,
so it is the only molecule that could genuinely test the retina-intrinsic limbs. Offset
heavily: the Michael-acceptor enone is a poor feature for lifelong dosing in a polypharmacy
population; aLogP 5.16 with Ro5v 1 and QED 0.41 (D) is at the far end of the model's §6.2
rubric (too lipophilic → melanin trapping, high PPB, low free fraction); and **δ co-agonism
compounds the ANGPTL4 liability**, since ANGPTL4 is induced by δ as well as α — the `⊗⊗` in
the matrix.

### A5 — Seladelpar — **4.0**
The isoform falsification control, and a sharper one than it was framed as. PPARδ drives FAO
and endothelial function but is a substantially weaker driver of hepatic apoB/remnant
clearance than PPARα — so it is **specifically weak on P8.1, the limb most likely to be
operative**, while retaining the ANGPTL4 liability. That makes it a well-designed negative
test: **if δ performs at or above α on any lipid or retinal readout, the PPARα-specific
hypothesis is not what is doing the work.**

### D1 — Epalrestat — **4.0**
AKR1B1 is the correct target in the correct cells (pericytes, Müller) at the correct stage
(S0–S1), with good physicochemistry (MW 319, aLogP 2.92, Ro5v 0, D) and decades of non-DR
chronic use. Two serious downgrades: the model classifies aldose-reductase inhibition as a
clinically disappointing single-branch blockade downstream of the ROS node, and — specific to
this tissue — **AKR1B1 also detoxifies 4-HNE**, so inhibiting it plausibly impairs reactive
lipid-aldehyde clearance in the most PUFA-laden tissue in the body (§2.4). A retina-specific
wrong-sign limb that, to my reading, nobody upstream has flagged.

### B2 — α-Linolenic acid — **3.5**
Direction-correct n-3 with genuine PPARα binding evidence in the project data (7 rows,
3 independent PMIDs). But human ALA→EPA→DHA conversion is inefficient — most is β-oxidised —
so the substrate arm it serves is weak, and only 8/27 DR-panel targets. A dietary
intervention, not a pharmacological one.

### B3 — Linalool — **3.5**
Scored low as a compound, flagged high as a **medicinal-chemistry lesson**. The PPARA-mutant
genetic-dependency evidence is unusually good for a natural product and hard to explain away
— but it is single-source (PMID 24752549). Its real significance: **MW 154, neutral, logP ~3
makes it the only Group B member physicochemically capable of reaching the retina, and it
demonstrates that the PPARα pocket accepts a neutral non-acidic ligand.** That is exactly
resolution (v) of the model's §6.2 dilemma — a non-acidic PPARα agonist chemotype. As a drug
it has no chronic-dosing vehicle, rapid glucuronidation, and a fragrance-sensitiser liability.
**Recommend the chemistry/SAR agent treat it as a scaffold starting point, not a candidate.**

### C1 — Quercetin — **2.5**
The frequent-hitter control, behaving exactly as designed. 26/27 DR-panel targets (D), but
every PPARA row is expression-level (E) and the direction is incoherent — it antagonises
GW 7647. Oral bioavailability <2% with extensive phase-II conjugation collapses the entire
annotation at the exposure step. Triggers three of the model's explicit negative priors at
once: promiscuous polyphenol without a specific mechanistic argument, antioxidant-as-sole-
mechanism, and PAINS/pan-assay-interference risk. **Breadth here is a liability, not a feature.**

### B1 — Linoleic acid — **2.0**
The most important negative finding in my matrix. It carries the strongest PPARα *binding*
evidence in the entire dataset — and the wrong *direction* for this disease. As the n-6
precursor of arachidonate it feeds the P8.6 pro-inflammatory eicosanoid arm (PTGS2, ALOX5,
and the KO-protective ALOX12/15 axis), it is the direct precursor of **4-HNE** (which the
model names as n-6 derived), and supplementing it pushes the retinal n-6:n-3 ratio further in
the direction diabetes has already moved it. **Retain as the mechanistic anchor the scout
intended; do not let "STRONG evidence" in the PPARA file propagate into a therapeutic score.**

---

## 10. Cross-cutting observations for the pipeline

1. **The set splits cleanly into two non-overlapping theories of the disease** — a
   *systemic metabolic* theory (Group A/B: reduce the lipid load presented to a leaky
   barrier, act from the liver and plasma) and a *retinal-intrinsic* theory (C2, D1, D2, D3:
   get into the neural retina and fix the cell biology). **These are not competing rankings;
   they are different compartments and would combine without mechanistic redundancy.** The
   obvious combination is a supply-side agent plus a retina-penetrant upstream-node agent.

2. **The set's P8 coverage is one-sided and its P9 coverage belongs to the comparators.**
   If the pipeline's output is "PPARα for early DR," the two weakest parts of that output
   will be the lipid-clearance claim (nothing supports it) and the neuroprotection claim
   (the comparators support it better).

3. **Three independent falsification tests are built into this set and they test different
   things.** Seladelpar tests *isoform* (δ vs α). Melatonin tests *compartment* (access vs
   affinity). Pemafibrate vs elafibranor tests *mechanism* (supply-side vs retina-intrinsic).
   All three should be run and reported separately — collapsing them into a single ranking
   destroys the experimental design the scout built.

4. **Phenotype enrichment is more likely to determine trial success than molecule choice.**
   Three of the model's five DME phenotypes and five of its six incomplete-responder
   mechanisms are untouched by every candidate here. An all-comers trial of any of these
   compounds dilutes a real effect across populations in which the mechanism cannot operate.

5. **The chemotype problem is systemic to Group A.** Five of five Group A compounds are
   lipophilic carboxylic acids with high protein binding — the exact profile the model's
   §6.2 rubric penalises. The one compound in the entire set that shows the pocket accepts a
   neutral ligand (linalool) is not a drug. **A neutral, non-acidic, sub-µM PPARα agonist
   scaffold does not exist in this set and is the chemistry gap**, distinct from the
   biology gap in §7.2.

---

## 11. Blinding compliance statement

**Files read.**
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-brief.md`
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-model.md` (full, 1,555 lines)
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/agents/p0-ppara-scout.md` (§0, §5, §6, §7, §8, §9)
- `.claude/skills/disease-modeler/SKILL.md`
- `.../evidence/ppar-class-drug-properties.tsv`, `.../evidence/compound-dr-target-matrix.tsv`,
  `.../evidence/ppara-interactions.tsv` (row counts and targeted greps)

**Files deliberately NOT read.** `data/processed/chembl_approved_drugs.csv`; anything under
`data/holdout/`; any `answer-key*` file. I did not use git history, git objects, stashes, or
any other route to recover redacted values, and I made no attempt to determine which rows
were redacted.

**Reasoning basis.** Every judgment in this report rests on (a) the three-axis disease model
provided to me, (b) structure and physicochemistry from the blinded evidence pack, (c) general
pharmacology, medicinal chemistry, physiology and human genetics, and (d) NON-DR clinical
knowledge. **No candidate is scored up or down anywhere in this document on the basis of any
DR or DME indication, approval, guideline position, or trial result.**

**Honest disclosures — including negative decisions.**

1. **I hold DR/DME-specific trial knowledge for at least four mechanism classes in this set —
   the fibrate class, RAS blockade, ω-3 supplementation, and microglial/tetracycline
   approaches — and I did not use any of it.** It influenced neither a score nor an exclusion.
   Where my conclusions happen to align or conflict with that knowledge, the alignment is not
   evidence of anything and should not be read as such. I am flagging the knowledge rather
   than claiming not to have it.

2. **The elevation of dimethyl fumarate to joint-top is the place where I most want to be
   audited, and it is derived entirely from in-document reasoning**: the model's own Brownlee
   argument that the upstream ROS/NRF2 node dominates single downstream branches
   (`disease-model.md` Axis B preamble); the model's statement that NRF2 nuclear translocation
   is impaired in diabetic retina (§P5); the model's §6.1 statement that RPE SLC16A/MCT
   transporters are "an exploitable route"; and the physicochemical properties in the blinded
   evidence pack. It is not derived from any DR trial knowledge, and to the best of my
   knowledge I hold no DR-specific clinical result for this compound either way.

3. **The ANGPTL4 argument (§8) comes from retinal vascular biology and PPAR target-gene
   biology, not from any DR trial result.** I note, as the scout did, that ANGPTL4's retinal
   role is studied predominantly in a DR/DME context, so the line between "general retinal
   physiology" and "DR-specific literature" is genuinely thin there. I judged it within the
   allowance because the argument is constructed from gene regulation (PPRE, HRE) and
   protein domain function, not from outcomes.

4. **The AKR1B1/4-HNE wrong-sign argument for epalrestat (§2.4)** is derived from a single
   parenthetical in the provided model (§5.1, row 10: "also detoxifies 4-HNE") combined with
   the model's own §P8.7 aldehyde chemistry. It is general enzymology, not DR clinical knowledge.

5. **The MTNR1B/insulin-secretion concern for melatonin** is human population genetics in
   type 2 diabetes — explicitly non-DR, and within the "genetics and NON-DR clinical
   knowledge" allowance of brief §1.3.

6. **Negative decisions.** I excluded no candidate and softened no criticism on the basis of
   DR-specific knowledge. I did not consider any compound outside the supplied 15 as a
   candidate; where §7.2 names a desired compound *profile* (LXR/ABCA1/ApoA1/scavenger-receptor,
   Kir4.1/AQP4, kallikrein–kinin), those are target classes named in the provided disease
   model, not drugs I selected.

7. **I inherit the scout's disclosure 2** — the Group D mechanism categories arrived already
   shaped by DR drug-development history via the original brief. My stage and pathway
   assignments for D1–D4 are my own and derived from the model, but I cannot claim the
   mechanism *categories* are blind, and I have not tried to launder that.

**Overall: I consider this analysis compliant**, with disclosure 1 (held-back DR trial
knowledge for four mechanism classes) and disclosure 3 (ANGPTL4's literature being
DR-concentrated) as the two places where the boundary required an active judgment call.

---

## SCOREBLOCK

SCORE|Fenofibric acid|6.5|moderate|mixed|Broad P8+P6 at S1-S3; renal elimination mismatches CKD population; retinal limbs notional
SCORE|Fenofibrate|6.0|moderate|mixed|Identical pharmacology post-conversion; adds variance, subtracts nothing
SCORE|Pemafibrate|7.0|moderate|mixed|Strongest supply-side P8.1 and safest in CKD; hepatoselectivity removes S0
SCORE|Elafibranor|5.5|moderate|mixed|Only molecule testing retina-intrinsic limbs; Michael acceptor, poor QED, compounded ANGPTL4
SCORE|Seladelpar|4.0|moderate|mixed|Isoform control; delta is weak on the operative supply limb
SCORE|Linoleic acid|2.0|high|data-backed|Best binding evidence, wrong direction: arachidonate and 4-HNE precursor
SCORE|Alpha-linolenic acid|3.5|moderate|data-backed|Direction-correct n-3 but inefficient human conversion; dietary, not pharmacological
SCORE|Linalool|3.5|low|data-backed|Scaffold lesson not candidate; proves neutral non-acidic PPARalpha chemotype possible
SCORE|Icosapent ethyl|6.0|moderate|mixed|Broadest P8 sub-module span including the neglected resolution arm; EPA not DHA
SCORE|Quercetin|2.5|high|data-backed|Frequent-hitter control; sub-2-percent bioavailability collapses all 26 targets
SCORE|Melatonin|5.5|moderate|mixed|Only unambiguous S0 compartment access; zero P8; MTNR1B glycemic concern
SCORE|Epalrestat|4.0|moderate|mixed|Right cells and stage; failed branch, plus AKR1B1 4-HNE detox wrong-sign
SCORE|Dimethyl fumarate|7.0|moderate|mixed|Upstream ROS node, S0-S2 span, best BRB physicochemistry; lymphopenia liability
SCORE|Minocycline|5.5|moderate|mixed|Most specific P9 agent at S0; chronic-use liabilities include intracranial hypertension
SCORE|Candesartan cilexetil|6.0|moderate|mixed|Luminal surface target escapes BRB objection; reaches S3; no P8
