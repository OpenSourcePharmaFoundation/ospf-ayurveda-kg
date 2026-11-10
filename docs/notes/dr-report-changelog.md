# DR report — changelog of changed claims

**Date** 2026-11-09 · **Supersedes** the 2026-11-03 revision of this file
**Target** `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md`
**Scope** Every claim in that report whose truth value, magnitude, or provenance changed, and
the evidence that changed it.

Section numbers in "old claim" columns refer to the **2026-10-05 original** unless marked
*(2026-11-03)*, which refers to the interim revision this one supersedes. §9 records the
structural changes.

Sources of change, cited below by short name:

| Short name | Document |
|---|---|
| **gap-closure** | `docs/notes/dr-data-gap-closure.md` — affinity, gene–disease and panel acquisition |
| **expression** | `docs/notes/ppara-retinal-expression.md` — retinal single-cell and bulk expression |
| **fgf21** | `docs/notes/fgf21-concentration-bridge.md` — the plasma/active FGF21 comparison |
| **absence-audit** | `docs/notes/dr-evidence-absence-audit.md` — systematic verification of absence claims |
| **exposure-model** | `docs/notes/retinal-exposure-model.md` — the 23-input calibrated ocular exposure model |
| **efflux** | `docs/notes/retinal-lipid-efflux-candidates.md` — the LXR axis and the burden model |
| **ligand-design** | `docs/notes/non-acidic-ppara-ligand-design.md` — AF-2 geometry, head-group screen, scaffolds |

---

## 1. CORRECTIONS TO THE 2026-11-03 REVISION OF THIS REPORT

These are errors in the interim text, not in the original. They are listed first because two of
them were arithmetic.

| Claim *(2026-11-03)* | Correction | Changed by |
|---|---|---|
| §4.2 "`0.140 ± 0.044 ng/mg = 140 ng/g = 439 nM`" | **Wrong by 10×, optimistically.** Huang 2021 reports ng/mg **of total protein**, not of tissue. Neural retina is ~10% protein by wet weight, so the figure is **14 ng/g = 43.9 nM**. Robust to the protein fraction: even at an implausible 20% it is 28 ng/g | **exposure-model** |
| §4.2 "measured human PPARα EC₅₀ 2,630 nM (pChEMBL 5.58)" | **The lowest of 18 PPARα records**, a TR-FRET co-activator assay. The median of 13 uncensored determinations is **15,000 nM** (95% CI 2,490–90,400, GSD 2.50), with five further records censored at >10,000 nM. Taking the minimum of a distribution as its value is worth a further **5.7×**, also optimistic | **exposure-model**, **gap-closure** |
| §4.2 "≈6× below, range 4.6–8.7×" | **Superseded.** Free fenofibric acid sits **~600× below its free PPARα EC₅₀ in neural retina and ~100× at the endothelium**. The two analyses reconcile exactly: 6.0× ÷ 10 (units) ÷ 5.7 (EC₅₀ selection) = 0.105×, and then the free-drug correction §4.2 itself called for ("one to two logs") brackets 600× | **exposure-model** |
| §4.2 framing of total-tissue against nominal EC₅₀ as "consistently uncorrected" | **Partly upheld, partly not.** The free-versus-nominal double-count it avoided is real and is now quantified at **2.3–5.2×**, not one log. But total-tissue-against-nominal is not internally consistent either: retinal tissue protein is ~100 mg/g against 1% FBS albumin at ~0.4 mg/mL. The model removes the protein term from both sides explicitly instead | **exposure-model** |
| §4.1 the 3.4× fenofibric-acid route penalty offered as "a measured argument for dosing the acid" | **Retained but demoted.** It is a comparison of two *routes of administration*, not a partition coefficient, and carries no information about the blood-to-retina ratio. Flagged as such in the rewrite | **exposure-model** |
| §4.4 "No parameterised ocular exposure model has been constructed" | **Closed.** 23 inputs, 200,000 draws, Sobol indices, three independent calibrations | **exposure-model** |
| §11.1 "the efflux arm is undruggable is an assumption, not a finding" | **Closed, and it was an assumption worth testing.** The axis has measured pharmacology at exactly one node | **efflux** |
| §11.2 the non-acidic ligand "has not been designed" | **Closed.** Pharmacophore measured from coordinates, 25 head groups screened, five scaffolds costed end to end | **ligand-design** |
| Abstract: "the single measurement that still decides the rest: free fenofibric acid in human aqueous humour" | **Displaced.** That measurement carries **19%** of the variance at the endothelium and RPE. The EC₅₀ and its assay serum conditions carry **69%** | **exposure-model** |

---

## 2. REVERSALS — claims that are now false

| Old claim (§) | New status | Changed by |
|---|---|---|
| §1 retinal PPARα "is reported to *decrease* in diabetes — the classic configuration for an agonist to **restore a deficit**" | **False.** Macula +0.046 log₂ (p = 0.836), periphery −0.096 (p = 0.367), no severity gradient. Bounded null: minimum detectable effect 1.40× / 1.26× at 80% power | **expression** |
| §5.5 the hepatic→FGF21→retina relay is the **best-evidenced limb** | **Withdrawn.** 25× shortfall (95% CI 6–99×); native FGF21 at ~10⁴× endogenous had no retinal effect; human retina lacks KLB (0.0 nTPM vs 16.6 in liver); the fenofibrate-induced FGF21 rise itself predicted *worse* outcomes in 9,697 patients | **fgf21** |
| §6.5 "the conditional deletion's continued absence is **itself informative**" | **False, and struck.** Endothelial-specific (PMID 41485550) and microglia-specific (PMID 36497130, published 2022) conditional *Ppara* deletions exist, both with gain-of-function arms | **absence-audit** |
| §6.5 citing the global knockout for the local limb "is **circular**" — unresolved | **Resolved for endothelium and microglia.** Both models leave hepatic PPARα, triglycerides, ketogenesis and FGF21 intact and still reproduce the diabetic phenotype. **Still open for rods, cones, RPE, Müller glia** | **absence-audit** |
| §6.1 retinal free drug concentration "**Never measured in any species**" | **False as stated.** Four studies quantify fenofibrate/fenofibric acid in rodent retina, vitreous or aqueous humour by LC-MS since 2019. The load-bearing version survives: no bounded ocular concentration after **oral** dosing in any species, none in any human sample | **absence-audit** |
| §5.1 local transactivation excluded because the partition ratio "cannot exceed 1" and the drug is "10–100× below free EC₅₀" | **Right conclusion, wrong structure, and the magnitude was understated.** Endothelium and RPE are **not behind a barrier** — the endothelium *is* the inner barrier and the RPE faces fenestrated choriocapillaris, so their ceiling is 1.0 and what puts them below is efflux. Neural retina is ~600× below, not 10–100× | **exposure-model** |
| §5.2 partition "roughly tenfold better" in endothelium/RPE than neural retina, asserted at 0.2–0.7 vs 0.01–0.15 | **Near-right in magnitude, wrong in reason.** Calibrated: neural retina Kp,uu **0.059 [0.009–0.354]**; blood-facing compartments median **0.32** with ceiling 1.0 — **5.3× apart**, with the reason named and measured rather than asserted | **exposure-model** |
| §5.3 pemafibrate is "~5 orders of magnitude more potent" and its margin is "about one order better" | **Potency 3.4 log best-vs-best / 4.5 log median-vs-median. And the margin is not better — it is worse.** Pemafibrate's endothelial margin (0.0035) is below fenofibric acid's (0.0084) at Cavg. **A more selective PPARα agonist is a worse retinal drug** | **gap-closure**, **exposure-model** |
| §5.6 the neutral chemotype as an open opportunity; "spend the same LLE at logD 2.8 instead of 5.5" | **Refuted.** The free-drug margin rises **monotonically with logP** across the drug-like range; the move costs ≈200× (neutral) to ≈350× (acid). Neutral PPARα ligands sit at LLE ≈ 1.0, not pemafibrate's anionic 3.45 | **ligand-design** |
| §5.7 the fibrates "do not secretly cover" the efflux arm because gene activation is absent locally | **Upheld for fibrates, and the generalisation is wrong.** At Kp,uu ≈ 0.9 a neutral LXR ligand *can* occupy its receptor. The "two-step relay, more sensitive to the shortfall" argument applies to the acid chemotype, not to the neutral one | **efflux** |
| §6.6 item 7, conditional retinal deletion costed at $300–500k from zero | **Rescoped to RPE/photoreceptor/Müller only, $150–300k** | **absence-audit** |
| §2.3 "Gene–disease associations for DR: None" / "Drug–target binding affinity: None" / "PPARα effector genes in the panel: None" | **All false.** 9,931 associations across six diabetic complications; 62,219 measured activities, 16,407 on the PPAR receptors; panel extended 27 → 43 genes | **gap-closure** |

---

## 3. ESTIMATES THAT BECAME MEASUREMENTS OR MODELLED VALUES

| Old claim (§) | Old provenance | New value | Changed by |
|---|---|---|---|
| §1 PPARα "is expressed in RPE, Müller glia and retinal vascular endothelium" | antibody literature | **Measured per cell type** across 4,828,235 human retinal cells: rods 67.97%, RPE 64.77%, cones 54.51% … horizontal 7.89%, against a six-control ambient floor of 0.00–0.1%. Corroborated in three bulk cohorts | **expression** |
| §5.1/§5.2 partition ratios 0.2–0.7 and 0.01–0.15, assigned by argument | reasoned | **Calibrated** against the one measured ocular fibrate concentration after systemic dosing: neural retina Kp,uu **0.059 [0.009–0.354]**. Externally checked against human aqueous-humour partition for three non-efflux-substrate drugs converted to free/free (**0.41–1.27**), an order of magnitude above, as the measured efflux machinery predicts | **exposure-model** |
| "Free EC₅₀ margins" quoted per compound without a model | reasoned | **Modelled**, 23 inputs, 200,000 draws. Endothelial margins at Cmax: fenofibric acid **0.020**, pemafibrate **0.027**, elafibranor + GFT1007 **0.136**, seladelpar/PPARδ **0.558**, seladelpar/PPARα 0.00074. Dose multiples 119× / 290× / 135× / 4.8× / 3,570× | **exposure-model** |
| The whole programme sequenced behind retinal PK | reasoned | **Sobol-decomposed.** Endothelium and RPE: potency block ST **0.694**, barrier **0.194**, plasma exposure 0.111. Neural retina: barrier 0.509, potency 0.428 | **exposure-model** |
| "The acid head is mandatory"/"bidentate pair ~2.2–3.2 Å apart" | structural reasoning | **Measured from five agonist complexes: 2.222 ± 0.064 Å (range 2.13–2.29), geminal**, with four donors onto **two** atoms, each accepting two hydrogen bonds | **ligand-design** |
| "PPARα's arm I is narrower than PPARγ's; footprint is the first filter" | asserted | **Refuted.** Head-region free volume 40.8 ± 7.1 Å³ (α) vs 38.6 ± 1.1 (γ) — equal within error. The discriminator is acceptor-array geometry: 2.22 Å over two atoms (α) vs 4.46 Å over three (γ) | **ligand-design** |
| "Neutral head → partial agonist by construction, Emax 25–55%" | reasoned | **Modelled: 57–82% in tissue [95% CI 8–95%], 92–98% in a coactivator-rich reporter line.** The interval is dominated by two never-measured receptor parameters (ρ 0.73 and 0.59), not by chemistry (≤0.06) | **ligand-design** |
| §5.7 "burden = influx ÷ clearance; as clearance → 0 the system integrates" | reasoned | **Modelled.** At E = 0 a **1000× transporter inducer gives infinite burden** and an acceptor at 0.1× healthy clearance gives 10. The inversion boundary is `E* = k_a·A / (k_t·(F−1))`; at E = 0.02 the inducer still wins | **efflux** |
| §5.7 "the LXR pocket does not mandate an acid — chemically conceivable" | reasoned | **Measured and costed.** 802 of 1,009 potent LXR ligands are neutral; neutrality buys a paired median **10–12× Kp,uu gain** and relieves the β-selectivity requirement by **1.16 log** | **efflux** |
| §3 ranking "Basis" column — potency claims | class pharmacology | **Measured pChEMBL at all three isoforms**, plus modelled per-compartment margins | **gap-closure**, **exposure-model** |
| §3.1 the quercetin collapse | an internal null model | **Confirmed against measured affinity.** Quercetin: 26 curated coverage hits → 3 genes at ≤1 µM, 0 effectors. 15 of 153 compounds bind any panel gene at ≤1 µM; 3 of 153 bind any effector | **gap-closure** |

---

## 4. CLAIMS OF ABSENT EVIDENCE — VERIFIED OR REFUTED

| Claim | Verdict | Changed by |
|---|---|---|
| No cell-type-restricted conditional *Ppara* deletion in retina | **REFUTED** — two exist (2022 microglial, 2026 endothelial) | **absence-audit** |
| No intraocular ANGPTL4 stratified by fibrate exposure | **VERIFIED ABSENT** across ten query strings, any species | **absence-audit** |
| No fibrate concentration in retinal tissue or aqueous humour in any species | **REFUTED for the literal claim; narrowed version survives** — nothing after oral dosing in any species, nothing human | **absence-audit** |
| No human diabetic neural-retina single-cell atlas | **VERIFIED ABSENT.** 13,075,889 human eye cells available, zero diabetic | **expression** |
| No FGF21 concentration-response below 50 ng/mL on any retinal preparation | **VERIFIED ABSENT** | **fgf21** |
| No validated PPARα immunostain on human retina | **VERIFIED ABSENT.** The reference resource's retina IHC panel is 113 proteins and contains no PPAR isoform | **expression** |
| No measured pKa, logP or logD for any of the four compounds | **VERIFIED ABSENT**, with the upstream cause: ChEMBL's API no longer serves `cx_logd`, `cx_logp` or `cx_most_apka` for any of them | **exposure-model** |
| No measured plasma protein binding for pemafibrate | **VERIFIED ABSENT** in every label, PubMed, PMC and Europe PMC | **exposure-model** |
| No measured hepatic Kp,uu for any fibrate | **VERIFIED ABSENT.** The 37–92× figures are the model's prediction, not a literature value | **exposure-model** |
| No efflux-ratio measurement for any fibrate or LXR ligand at any ocular barrier | **VERIFIED ABSENT** | **exposure-model**, **efflux** |
| No measurement of ABCA1/ABCG1 activity in human diabetic retina | **VERIFIED ABSENT in any species** — and it decides acceptor versus inducer outright | **efflux** |

---

## 5. NEW FINDINGS WITH NO PRIOR CLAIM TO CHANGE

| Finding | Why it matters | Source |
|---|---|---|
| **Hepatoselectivity is the mechanism that denies these drugs the eye.** Required liver Kp,uu 37–92×; **OATP1B1 502.3 nTPM in liver vs 0.0 in retina**, OATP1B3 247.7 vs 0.0 | Raising the dose does not fix a missing transporter. The model recovers the four compounds' known hepatoselectivity ordering with no hepatoselectivity parameter in it — the strongest single validation in the file | **exposure-model** |
| **Retinal vascular endothelium expresses ABCB1 507 nCPM, ABCC4 178, ABCG2 142 — each above hepatocyte; RPE expresses OAT3 465 and ABCC5 823** | Names and measures the reason the blood-facing compartments sit below their ceiling of 1.0, and identifies the RPE as the one compartment that could *concentrate* an anion | **exposure-model** |
| **Seladelpar is the only compound within reach of a retinal receptor** — PPARδ endothelial margin 0.558 at Cmax, 4.8× dose short, P(margin ≥ 1) = 0.34 | Combined with PPARδ dominance in the vasculature, this is the report's one live local hypothesis **and** a hazard finding, since PPARδ is pro-angiogenic | **exposure-model** + **expression** |
| **PPARδ exceeds PPARα in every vascular and immune retinal compartment** — microglia 2.78×, RGC 1.77×, VSMC 1.18×, endothelium 1.15×, pericytes 1.10× | Converts isoform selectivity from a safety preference into a targeting constraint, and makes elafibranor's equal PPARα/PPARδ potency a liability rather than a feature | **expression** |
| **The serum correction is 2.3–5.2×, and it makes pemafibrate's missing binding measurement harmless** — a 20× swing in free fraction moves the margin 2.3× | Quantifies the "worth about a log" intuition, and shows that the uncorrected comparison is dominated by a parameter that should be nearly irrelevant | **exposure-model** |
| **Huang 2021's columns are on one scale** — resolved from the paper's own choroid:plasma arithmetic (8.469 / 1.726 = 4.9 against a stated "approximately five-fold") | Resolves a 60× ambiguity in the only systemic ocular measurement that exists, in the direction that makes retinal exposure look worse | **exposure-model** |
| **The entire measurable pharmacology of the efflux axis is at one node** — 3,729 of 3,732 activities at LXR-α/β, zero at ABCA1, ABCG1, APOA1 or APOE. The only approved drug with an ABCA1 mechanism is probucol, an **inhibitor** | Settles that the effectors are readouts, not pockets, and that LXR is the only pharmacological route | **efflux** |
| **No acidic LXR ligand clears the selectivity bar an acid's Kp,uu demands: 0 of 83**, best 2.66 against 2.73 required | "It cannot be done from the liver" recovered as arithmetic rather than asserted | **efflux** |
| **The five LXR candidates are one 2018 patent series on cell-free data, and the cellular tier does not reproduce the selectivity** — max 1.37 log over 106 paired molecules, none clearing its requirement | Prevents a chemical hypothesis being read as a candidate list | **efflux** |
| **DR is already treated by injection into the target compartment** | The candidates were ranked by oral-systemic feasibility. An intravitreal acceptor makes the whole exposure analysis moot for whatever is delivered that way. **The most consequential reframing in the file** | **efflux** |
| **Tetrazole fails on lone-pair capacity, not footprint** — 1.32× the carboxylate's volume, *smaller* than the oxazolidinone that passes; no tetrazole atom can accept two hydrogen bonds | Right conclusion, wrong reason — and the correct reason cannot be engineered around | **ligand-design** |
| **The 1,2,4-oxadiazol-5(4H)-one fails**, having been the lead head-group recommendation | One double-acceptor atom; it can serve at most two of the four donors | **ligand-design** |
| **The best neutral scaffold needs 36 g/day; a lipophilicity-stripped acid control needs 3.7 g/day** and beats every neutral by 9.7× | The neutral heads deliver the predicted 19.7× partition gain and still lose. And the gain lands behind the tight junction, not at the endothelium where the lesion is | **ligand-design** |
| **The same molecule reads Emax 92% in a reporter line and 57% in tissue** | A systematic, directional assay bias that a conventional cascade would not catch | **ligand-design** |
| **The human retina lacks KLB and is rich in ADIPOR1** — 0.0 nTPM (9th percentile) vs 125.7 (98th) | Explains the adiponectin dependence of the mouse retinal protection and reframes the surviving route | **fgf21** |
| **HMGCS2 is RPE-specific** (22.95% of RPE cells, ≤0.1% elsewhere) | The one tractable local-transactivation readout in human eye | **expression** |
| **PPARγ, not PPARα, carries the human genetic signal for DR** — rank 9 of 2,652 with genetic score 0.750 vs PPARA rank 66 with none | Hypothesis-generating; most plausibly propagated from type 2 diabetes across the ontology. One query resolves it | **gap-closure** |

---

## 6. METHODOLOGICAL FINDINGS NOT CARRIED INTO THE REPORT

Recorded here because they bear on the project's tooling rather than on diabetic retinopathy.

| Finding | Consequence |
|---|---|
| **The GNN link-prediction model is anti-predictive when ranking compounds for a fixed gene.** Mean percentile rank of known positives 0.123 against 0.500 random; compound degree alone scores 0.970. The model passes its own benchmark (hits@10 = 0.99) because that benchmark ranks *genes for a compound*, where gene degree is informative | **No claim in the report rests on GNN-ranked predictions, and none should.** The fix is cheap: evaluate link-prediction models in both directions and report the degree-only baseline alongside |
| **The knowledge graph holds no binding-grade evidence on the efflux axis.** 100% of its 238 axis edges come from a toxicogenomics database, 88% are expression-change statements, 36% are nested third-order relations, 29% name a co-treatment | A graph edge labelled `TARGETS` may assert that a dietary confound altered a gene's expression in a co-treatment experiment |
| **A sticky cache bug in the HPA fetcher** — truncated proxy responses cached as valid JSON, failing every later run and looking like a cache hit | Fixed; regenerated `retina_hpa_antibody_reliability.tsv`, which an earlier pass had reported as a failed download |
| **Two modelling bugs found and fixed during the ligand work** — an uncapped ΔΔG that made losing the H12 contact score better than weakening it, and a neutral logD–protein-binding relation applied to an anion, which predicted fenofibric acid 80% unbound against a measured 1% | Both documented in the code |
| **An earlier recommendation to anchor the partition prior on the Huang IP-vs-topical ratio was wrong** — that is a route comparison, not a partition coefficient. The right anchor is retina:plasma within the IP arm | Corrected in the model and flagged in the report |

---

## 7. CLAIMS EXPLICITLY UNCHANGED

Recorded so that silence is not read as revision.

| Claim | Status |
|---|---|
| §4 staging — mild-to-moderate non-proliferative disease | **Unchanged, and the most robust conclusion in the report.** Reinforced: both conditional knockouts show no baseline phenotype and a diabetes-induced one |
| §1.1 hard exudates are retained modified apoB lipoproteins; remnants track DR where LDL does not | **Unchanged.** Still reasoned, now tagged as such |
| §5.4 the two ANGPTL4 objections are mutually destructive; triglycerides fall rather than rise | **Unchanged, and the exposure half is now modelled rather than argued** |
| §5.6 "the AF-2 cage is all-donor; the ligand supplies only acceptors"; charge is an acceptor-strength multiplier, not a requirement | **Upheld, now measured.** Caveat: hydrogens are not observed and His440's tautomer is assignable, not observed |
| §5.6 oleoylethanolamide as the neutral existence proof, LE 0.41 | **Upheld**, and used as the potency calibration for every derived EC₅₀ |
| §5.7 retinal reverse cholesterol transport cannot be performed from the liver | **Unchanged, and now arithmetic** |
| §6.9 scavenger-receptor blockade is wrong-signed | **Unchanged** |
| §6.7 observation windows must be justified against clearance, not calendar | **Unchanged** |
| Fibrate benefit in FIELD / ACCORD-Eye | **Untouched and now unexplained by any of the four limbs.** Removing candidate explanations does not remove the observation |
| §2.3 "measured pharmacokinetics: none" for **human oral** dosing | **Unchanged.** One mouse IP measurement exists and is the model's calibration anchor; no human ocular value exists by any route |

---

## 8. WHAT REMAINS OPEN

| Question | State |
|---|---|
| **Why fibrates work in DR** | Open, and now sharper: none of the four candidate limbs explains it. The free covariate analysis discriminates the supply limb first |
| **Whether any local pharmacodynamic effect occurs at a measured ocular concentration** | Open. The rodent study with paired LC-MS is the frame-testing experiment |
| **The PPARα/δ EC₅₀ at physiological albumin** | Open, and the highest-variance input — 69% at the compartments that matter |
| **Whether RPE OAT1/OAT3 take up any fibrate** | Open. Would invert the compartment ordering |
| **`E` — ABCA1/ABCG1 activity in human diabetic retina** | Open in any species. Decides acceptor versus inducer outright |
| **Cellular β-selectivity for the LXR candidate series** | Open. Would move five candidates from cell-free claim to cellular fact, or kill them |
| **The H12 closure energy and the Tyr464 contact worth for PPARα** | Never measured. They carry more Emax variance than every chemistry parameter combined |
| **Necessity in RPE, photoreceptors and Müller glia** | Open, and these are the high-expression compartments |
| **Human ocular fibrate PK after oral dosing** | Open — and now eighth on variance rather than first |

---

## 9. STRUCTURAL CHANGES TO THE DOCUMENT

- **Provenance tags throughout.** Every quantitative claim carries **[M]** measured, **[C]**
  computed, **[Mod]** modelled or **[R]** reasoned. An untagged number is an error.
- **A state-of-knowledge table leads** (§1), so the reader learns the position before any
  argument.
- **The method and rediscovery-benchmark sections were removed** in the previous revision and
  remain out. `BENCHMARK-RESULT.md` is unchanged and keeps the methodological retrospective.
- **§4 was rebuilt around the exposure model** — compartment structure, calibration anchor and
  its unit trap, external calibration, ionisation, the serum correction, potency as a
  distribution, margins, the hepatic back-calculation, and the sensitivity decomposition.
- **§6 was renamed "necessary, and unreachable"** and now states the central tension explicitly,
  with the three live resolutions and the experiments that separate them.
- **§11 is new**: where a drug could still act — PPARδ in the vasculature, the efflux arm, and
  the non-acidic ligand, each now a result rather than a specification.
- **§12 was reordered by variance share** rather than by narrative priority. The aqueous-humour
  tap moved from first to eighth; an EC₅₀ panel at physiological albumin moved to second behind
  the free covariate analysis.
- No other file in the report directory was modified.

---

## Status — 2026-11-09 — report rewrite from the complete evidence set

**Done.** `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md` rewritten
from all seven investigations. The three that were missing at the previous revision —
`retinal-exposure-model.md`, `retinal-lipid-efflux-candidates.md` and
`non-acidic-ppara-ligand-design.md` — now exist and are committed, and all three are
incorporated. Verified against the repository and `git log`, not against the chain state file,
which still records steps 5–7 as `failed` and is stale.

**The headline changed.** Previously: a necessary local target, with retinal exposure measured
at ~6× below EC₅₀ and the aqueous-humour tap as the decisive measurement. Now: **a necessary
local target that no compound in the class can reach**, by 37–1,340× at the most favourable
compartment, for a mechanistic reason (OATP1B hepatoselectivity) that dose cannot fix — and the
decisive measurement is an **EC₅₀ panel at physiological albumin**, because the aqueous tap
carries 19% of the variance where the EC₅₀ carries 69%.

**Two arithmetic errors in the previous revision are corrected and recorded in §1.** The Huang
2021 figure is ng/mg of **total protein**, not of tissue — a 10× optimistic conversion — and the
EC₅₀ used was the lowest of 18 records against a median 5.7× weaker. The reconciliation is
exact and is set out in §1 and in REPORT.md §4.2.

**Not done / limits.** No new computation was performed for this rewrite beyond checking the
reconciliation arithmetic; every number is transcribed from a named source document with its
provenance tag preserved. The three open methodological items in §6 are recorded here and
deliberately kept out of REPORT.md, which reports the science rather than the tooling.
