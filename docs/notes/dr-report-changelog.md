# DR report — changelog of changed claims

**Date** 2026-11-03
**Target** `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md`
**Scope** Every claim in that report whose truth value, magnitude, or provenance changed, and
the evidence that changed it.

Section numbers in the "old claim" columns below refer to the **2026-10-05 report as it
stood before this rewrite**; the rewritten document is renumbered, and §8 of this changelog
records the structural changes.

Sources of change, cited below by short name:

| Short name | Document |
|---|---|
| **gap-closure** | `docs/notes/dr-data-gap-closure.md` — affinity, gene–disease and panel acquisition |
| **expression** | `docs/notes/ppara-retinal-expression.md` — retinal single-cell and bulk expression |
| **fgf21** | `docs/notes/fgf21-concentration-bridge.md` — the plasma/active FGF21 comparison |
| **absence-audit** | `docs/notes/dr-evidence-absence-audit.md` — systematic verification of three absence claims |
| **computed here** | Arithmetic performed during this rewrite, from values in the above |

---

## 1. REVERSALS — claims that are now false

| Old claim (§) | New status | Changed by |
|---|---|---|
| §1 "its retinal expression is reported to *decrease* in diabetes — the classic configuration for an agonist to **restore a deficit**" | **False.** Retinal *PPARA* is unchanged in diabetes: macula +0.046 log₂ (p = 0.836), periphery −0.096 (p = 0.367), no severity gradient. Bounded null — minimum detectable effect 1.40× / 1.26× at 80% power (GSE160306, n = 79, 43 donors) | **expression** |
| §5.5 the hepatic→FGF21→retina relay is the **best-evidenced limb**, "human-proven upstream, animal-proven downstream" | **Withdrawn.** Achievable plasma FGF21 is 25× below the lowest demonstrated active concentration (95% CI 6–99×; P(achievable ≥ active) = 0.0000 over 200,000 draws). Native FGF21 at ~10⁴× endogenous had no retinal effect (PMID 28199833). Human retina lacks the obligate co-receptor (KLB 0.0 nTPM, 9th percentile vs 16.6 in liver). The fenofibrate-induced FGF21 rise itself predicted *worse* outcomes in 9,697 patients (PMID 28606915) | **fgf21** |
| §6.5 "After roughly fifteen years of interest in this target, the conditional deletion's continued absence is **itself informative**" | **False, and struck entirely.** Two cell-type-restricted conditional *Ppara* deletions in mouse retina exist: endothelial-specific (*Vecad-CreERT2*, PMID 41485550) and microglia-specific (*Cx3Cr1-CreERT2*, PMID 36497130, published 2022). Both carry gain-of-function arms | **absence-audit** |
| §6.5 citing the global knockout for the local limb "is **circular**" — unresolved | **Resolved for endothelium and microglia.** Both conditional models leave hepatic PPARα, triglycerides, ketogenesis and FGF21 intact and still reproduce worsened diabetic ERG decline, retinal thinning, leakage and pericyte loss. The confound is structurally absent, not statistically adjusted. **Still open for rods, cones, RPE and Müller glia** | **absence-audit** |
| §6.1 free drug concentration in retinal tissue "**Never measured in any species**" | **False as stated.** Fenofibrate and fenofibric acid have been quantified by LC-MS in rodent retina, vitreous and aqueous humour by four independent studies since 2019 (PMIDs 34943243, 41580131, 41407273, 30912953). **The load-bearing version survives, narrowed:** no bounded ocular concentration exists after **oral** dosing in any species, and none in any human sample | **absence-audit** |
| §2.3 "Gene–disease associations for DR: **None**" | **False.** 9,931 scored associations across six diabetic complications, including 2,652 for DR | **gap-closure** |
| §2.3 "Drug–target binding affinity: **None.** Mechanism and target tables are near-empty test extracts with zero PPAR content" | **False.** 62,219 measured activities, 16,407 on the three PPAR receptors; 1,644 / 1,264 / 2,590 compounds at ≤1 µM on PPARA / PPARD / PPARG | **gap-closure** |
| §2.3 "PPARα effector genes in the target panel: **None**" | **False.** Panel extended 27 → 43 genes, each annotated with the limb it discriminates | **gap-closure** |
| §2.3 "**The pathway under study was invisible to the data used to study it.**" | **No longer true of the receptors or the effector programme.** Remains true of exposure | **gap-closure**, **expression** |

---

## 2. ESTIMATES THAT BECAME MEASUREMENTS

| Old claim (§) | Old provenance | New value | Changed by |
|---|---|---|---|
| §1 PPARα "is expressed in retinal pigment epithelium, Müller glia and retinal vascular endothelium" | asserted from antibody literature | **Measured per cell type** across 4,828,235 human retinal cells, 24 datasets: rods 67.97%, RPE 64.77%, cones 54.51%, astrocytes 20.91%, pericytes 19.90%, VSMC 18.97%, Müller 18.17%, microglia 15.50%, endothelium 15.39%, RGC 13.04%, bipolar 12.62%, amacrine 11.76%, horizontal 7.89% — against a six-negative-control ambient floor of 0.00–0.1%. Corroborated in three bulk cohorts (EyeGEx n = 523: 143.5 CPM, 92.4th percentile, detected in 99.8% of retinas) | **expression** |
| §5.1 "Even complete barrier failure leaves fenofibric acid **10–100× below its free EC₅₀** in neural retina" | reasoned; no measured partition, permeability or binding value | **Measured:** 0.140 ± 0.044 ng/mg fenofibric acid in mouse retina + vitreous after IP 2 mg/kg/day × 7 d (PMID 34943243) = **439 nM, range 301–577 nM** (tissue density 1.0 g/mL, MW 318.75). Against the **measured** PPARα EC₅₀ of 2,630 nM (pChEMBL 5.58): **≈6× below, range 4.6–8.7×**, both sides uncorrected for protein binding. Wrong route, pooled compartment, total not free — but no longer an arithmetic exclusion | **absence-audit** + **gap-closure**, **computed here** |
| §5.3 pemafibrate is "**~5 orders of magnitude** more potent than fenofibric acid" | class pharmacology | **Measured:** 3.4 log units best-vs-best (pChEMBL 9.00 vs 5.58), 4.5 log units median-vs-median. *n = 3 for pemafibrate, all EC₅₀ — thin.* The report's actual argument (a ~4-order free-concentration deficit cancels most of it) survives, now bounded by data | **gap-closure** |
| §3 ranking table, "Basis" column — potency claims for every candidate | class pharmacology, no affinities | **Measured pChEMBL at PPARα / PPARδ / PPARγ** added for all eight: fenofibric acid 5.58/—/4.00; pemafibrate 9.00/5.80/5.96; fenofibrate 6.00/—/6.24; elafibranor 8.00/8.00/6.76; seladelpar 5.82/8.72/— | **gap-closure** |
| §3.1 the quercetin collapse — a null model over coverage counts | computed within the original analysis, uncorroborated | **Confirmed against measured affinity.** Quercetin: 26 of 27 curated coverage hits → 3 genes bound at ≤1 µM, 0 PPARα effectors. Across the legacy set, 15 of 153 compounds bind any panel gene at ≤1 µM and 3 of 153 bind any effector; mean effector genes bound 0.046 | **gap-closure** |
| §5.6 oleoylethanolamide ligand efficiency 0.41 vs fenofibric acid 0.29, pemafibrate 0.34 | reasoned | **Unchanged**, now explicitly tagged computed-from-measured-affinity rather than asserted | — |
| §6.1 the proposed aqueous-humour assay, implicitly treated as a capability to be built | implied absent | **The assay is mature.** Ocular LC-MS for fenofibrate and fenofibric acid validated by three independent groups since 2019, with ng/g detection limits in aqueous humour. What is missing is the human oral cohort, not the capability | **absence-audit** |

---

## 3. CLAIMS OF ABSENT EVIDENCE — VERIFIED OR REFUTED

| Claim (§) | Verdict | Changed by |
|---|---|---|
| No cell-type-restricted conditional *Ppara* deletion in retina (§6.5) | **REFUTED** — two exist (2022 endothelial-adjacent microglial; 2026 endothelial) | **absence-audit** |
| No published measurement of intraocular ANGPTL4 stratified by fibrate exposure (§6.1) | **VERIFIED ABSENT** across ten distinct query strings, any species. The proposed experiment remains novel and unclaimed. Nearest adjacent result is in-vitro ARPE19 mRNA (PMID 39768065), which does not qualify | **absence-audit** |
| No measurement of fibrate concentration in retinal tissue or aqueous humour in any species (§6.1) | **REFUTED for the literal claim; narrowed version survives** — see §1 and §2 above | **absence-audit** |
| No human diabetic neural-retina single-cell atlas | **NEWLY VERIFIED ABSENT.** 13,075,889 human eye cells available, zero diabetic; every public diabetic eye single-cell dataset profiles fibrovascular membranes or blood | **expression** |
| No FGF21 concentration-response below 50 ng/mL on any retinal preparation | **NEWLY VERIFIED ABSENT.** The threshold for retinal endothelial protection is unknown and only bounded above | **fgf21** |
| No validated PPARα immunostain on human retina | **NEWLY VERIFIED ABSENT.** The reference antibody resource's retina IHC panel covers 113 proteins and includes no PPAR isoform; it grades PPARα immunofluorescence "Uncertain" on both its antibodies | **expression** |

---

## 4. NEW FINDINGS WITH NO PRIOR CLAIM TO CHANGE

| Finding | Why it matters | Source |
|---|---|---|
| **PPARδ exceeds PPARα in every vascular and immune retinal compartment** — microglia 2.78×, RGC 1.77×, VSMC 1.18×, endothelium 1.15×, pericytes 1.10× | Converts isoform selectivity from a safety preference into a targeting constraint. Every proposed local-engagement mechanism is sited in a PPARδ-dominant compartment | **expression** |
| **Elafibranor engages PPARα and PPARδ equally (both pChEMBL 8.00)** | In PPARδ-dominant retinal vasculature it is a pro-angiogenic risk, not a neutral dual agonist. This changes its role as the designated probe | **gap-closure** + **expression** |
| **Seladelpar is functionally a PPARδ agonist** (PPARδ 8.72 vs PPARα 5.82) | Reclassified from "isoform control" to a direct probe of the dominant vascular isoform, with the matching angiogenic hazard | **gap-closure** + **expression** |
| **Pemafibrate's 3.2-log PPARα/PPARδ margin excludes the compartments where DR pathology lives** | The selectivity that makes it safe also makes it a poor local probe | **gap-closure** + **expression** |
| **The human retina does not express FGF21** — 0.00–0.01% of 4.8M cells, 0.00 CPM across 523 retinas | Removes any local-production escape hatch for the humoral limb. The relay was necessarily hepatic-to-retinal even before it failed | **expression** |
| **The human retina lacks KLB and is rich in ADIPOR1** — KLB 0.0 nTPM (9th percentile) vs ADIPOR1 125.7 (98th) | Explains the adiponectin dependence of the mouse retinal protection, and reframes the surviving route as liver → FGF21 → adipose → adiponectin → retina | **fgf21** |
| **HMGCS2 is RPE-specific** (22.95% of RPE cells, ≤0.1% elsewhere) | The one tractable local-transactivation readout in human eye. A concrete assay that did not exist as a proposal | **expression** |
| **ANGPTL4 in retina is a mural/endothelial transcript** — pericytes 23.1%, VSMC 22.9%, endothelium 12.0%, photoreceptors ~1% | Locates the wrong-sign permeability risk in the correct compartment, which strengthens it — and that compartment is PPARδ-dominant | **expression** |
| **The fatty-acid-oxidation effectors are robustly expressed in neural retina** — CPT1A 34.1% of rods, ACADM 22.1%, ACOX1 13.9%, ABCG1 42.0% | Limb 4's readouts exist. Their absence from binding and association databases reflected what has been studied, not the biology | **expression** |
| **PPARγ, not PPARα, carries the human genetic signal for DR** — rank 9 of 2,652 with genetic score 0.750, versus PPARA rank 66 with none | Hypothesis-generating only; the signal most plausibly propagates from type 2 diabetes susceptibility across the disease ontology. One query would resolve it | **gap-closure** |
| **PPARα outnumbers its obligate RXR partner at least 6.4 : 1 in rods** | Would cap transactivation independently of drug concentration — the first such constraint not derived from exposure. **Hypothesis from transcript ratios, explicitly not a finding** | **expression** |
| **The prodrug pays a 42× ocular distribution penalty by the systemic route; the active acid pays only 3.4×** | An argument for dosing the acid, with a measured basis | **absence-audit**, **computed here** |
| **Six negative controls establish an ambient detection floor of 0.00–0.1%** | Without it, "detected in 15% of cells" is not a claim. This is what makes the expression result interpretable rather than suggestive | **expression** |
| Nominal, FDR-failing signals: *RXRA* rises with DR severity (ρ = +0.462, p = 0.003); *PDK4* falls in periphery (log₂FC −0.62, p = 0.015) | Flagged as hypotheses. The *RXRA* direction is the opposite of what a deficit model predicts | **expression** |

---

## 5. EXPERIMENTAL PROGRAMME — WHAT CHANGED

| Old item (§6.6) | Disposition |
|---|---|
| 1. Lipid-change covariate analysis, ~$0 | **Unchanged.** Still free, still first |
| 2. Human aqueous drug + ANGPTL4, $50–100k | **Unchanged and promoted.** Both halves verified still undone; the assay is mature |
| 3. Rodent transactivation vs transrepression, $150–250k | **Kept, sharpened.** Add paired ocular LC-MS so the pharmacodynamic readout is anchored to a measured concentration; the knockout arm is now available off the shelf for endothelium and microglia; add HMGCS2-in-RPE as the transactivation readout; measure PPARδ alongside PPARα throughout |
| 4. FGF21 concentration bridge, ~$50k | **Dropped — answered.** The relay fails. Residual: a sub-50 ng/mL concentration-response on retinal endothelial cells, retained as a cheap item that would overturn the verdict if positive |
| 5. ApoA1-mimetic explant, transporter silenced, ~$75k | **Unchanged** |
| 6. Lipid clearance rate constant, ~$75k | **Unchanged** |
| 7. Conditional retinal receptor deletion, $300–500k | **Rescoped and re-costed to $150–300k.** Done for endothelium and microglia; remaining scope is RPE-, photoreceptor- and Müller-glia-specific deletion — the high-expression compartments |
| — | **New item 2: validated PPARα immunostain on human donor retina**, per cell type, with knockout or peptide-competition controls, ~$15–30k. The only surviving part of the antibody/transcript conflict and the cheapest decisive experiment in the programme |
| — | **New acquisitions:** a second diabetic human retina cohort; a diabetic human retina single-cell atlas; single-cell confirmation of retinal KLB; the PPARG ontology-propagation query; protein-level PPARα:RXR stoichiometry |
| §6.8 kill criteria | **One added:** validated immunostain showing PPARα protein absent from endothelium and microglia would require a non-cell-autonomous explanation of the conditional-knockout phenotypes |
| Total, items 1–6 | $400–550k → **$370–530k** |

---

## 6. CLAIMS EXPLICITLY UNCHANGED

Recorded so that silence is not read as revision.

| Claim | Status |
|---|---|
| §4 staging — mild-to-moderate non-proliferative disease | **Unchanged, and the most robust conclusion in the report.** Reinforced: both conditional knockouts show no baseline phenotype and a diabetes-induced one |
| §1.1 hard exudates are retained modified apoB lipoproteins, not "fat"; remnants track DR where LDL does not | **Unchanged.** Still reasoned, now tagged as such |
| §5.2 compartment matters more than the barrier — endothelial PPARα faces the blood side, RPE faces fenestrated choriocapillaris | **Unchanged in direction.** The partition ratios attached to it remain reasoned; no model was built to replace them |
| §5.4 the two ANGPTL4 objections are mutually destructive; triglycerides fall rather than rise, bounding induction | **Unchanged**, and strengthened by compartment localisation |
| §5.7 clearance-limited burden integrates as clearance → 0; a supply agent buys delay | **Unchanged.** Still reasoned; the clearance rate constant is still unmeasured |
| §5.7 retinal reverse cholesterol transport cannot be performed from the liver | **Unchanged** |
| §6.9 scavenger-receptor blockade is wrong-signed | **Unchanged** |
| §6.7 observation windows must be justified against clearance, not calendar | **Unchanged** |
| §2.3 "Measured pharmacokinetics: None" — for **oral** dosing | **Unchanged and still the binding constraint.** Partly closed for local and parenteral routes only |

---

## 7. QUESTIONS THAT REMAIN UNEXAMINED

Three questions were posed and not answered. They are carried in the report as specifications
with the structural argument intact, not as findings.

| Question | State |
|---|---|
| **A parameterised ocular exposure model** for the fibrate chemotype — free concentration per compartment, margins against consistently corrected free EC₅₀, and a sensitivity analysis identifying which input dominates output variance | **Not built.** The partition ratios in §5.2 therefore remain reasoned rather than modelled, and the question of where measurement effort should go is unanswered. The one real anchor available is the Huang 2021 route comparison |
| **Candidates for the lipid-efflux arm** — ranked predictions against NR1H2, NR1H3, ABCA1, ABCG1, APOA1, APOE and the scavenger-uptake side, filtered on retinal-access physicochemistry and assessed for the steatosis liability; and whether a direct extracellular acceptor beats a transporter inducer | **Not assembled.** The report states plainly that "the efflux arm is undruggable" is an assumption, not a finding, and that the acceptor-versus-inducer preference may be backwards |
| **A non-acidic PPARα ligand** — pharmacophore from the all-donor AF-2 cage, a screen of the neutral head-group window, the partial-agonist efficacy asymmetry quantified, and 3–5 scaffolds with full predicted profiles | **Not designed.** The structural argument that it is possible stands unchanged, including the oleoylethanolamide ligand-efficiency existence proof. The assay-cascade blocker is stated in the report: no cascade exists for optimising against free-drug retinal exposure |

---

## 8. STRUCTURAL CHANGES TO THE DOCUMENT

- **Provenance tags added throughout.** Every quantitative claim now carries **[M]** measured,
  **[C]** computed, **[Mod]** modelled or **[R]** reasoned. An untagged number is an error.
- **A state-of-knowledge table leads the document** (§1), so the reader learns which compound,
  which stage, which mechanism, what the exposure is, and what single measurement remains
  before reading any argument.
- **The method section and the rediscovery-benchmark section were removed.** The methodological
  retrospective lives in `BENCHMARK-RESULT.md`, which is unchanged.
- **Limbs 2, 3 and 4 were promoted to their own sections** (§5, §6, §7), because each now
  resolves differently and at different confidence.
- **Expression and exposure were given dedicated sections** (§3, §4) ahead of the mechanism
  adjudication that depends on them.
- No other file in the report directory was modified.

---

## Status — 2026-11-03 — report rewrite

**Done.** `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md` rewritten
to report results rather than reasoning, from the four completed investigations
(`dr-data-gap-closure.md`, `ppara-retinal-expression.md`, `fgf21-concentration-bridge.md`,
`dr-evidence-absence-audit.md`). Every quantitative claim now carries a measured / computed /
modelled / reasoned tag. The abstract leads with compound, stage, live mechanism, measured
retinal exposure, and the single remaining decisive measurement. The method and
rediscovery-benchmark sections were removed; `BENCHMARK-RESULT.md` is unchanged and remains
the home of the methodological retrospective.

**Computed during the rewrite** (not present in any source note): the measured rodent retinal
fenofibric acid concentration (0.140 ± 0.044 ng/mg, PMID 34943243) converted to molarity
(439 nM, range 301–577 nM) and placed against the measured human PPARα EC₅₀ (2,630 nM,
pChEMBL 5.58) — **≈6× below, range 4.6–8.7×**, both sides uncorrected for binding. Also the
route asymmetry within that study: a 42× systemic-versus-topical ocular penalty for the
prodrug against only 3.4× for the active acid. Caveats are enumerated in REPORT.md §4.2.

**Verified at run time, not taken from any prior report.** Three of the seven preceding
investigations did not complete and produced no deliverable: the **parameterised ocular
exposure model**, the **lipid-efflux candidate set**, and the **non-acidic PPARα ligand
design**. `docs/notes/retinal-exposure-model.md`,
`docs/notes/retinal-lipid-efflux-candidates.md` and
`docs/notes/non-acidic-ppara-ligand-design.md` do not exist, and no exposure-model code exists
under `src/analysis/`. The rewrite therefore does **not** cite a model, a candidate ranking, or
a scaffold set. Those three questions are carried in REPORT.md §4.4, §11.1 and §11.2 as open
specifications with their structural arguments intact, and are itemised in §7 of this
changelog. Nothing was inferred or asserted in their place.

**Also still open, carried forward:** the single-cell confirmation of retinal KLB (the
co-receptor result rests on one consortium's bulk and single-cell arms), a second diabetic
human retina cohort, and the sub-50 ng/mL FGF21 concentration-response that would overturn the
relay verdict if positive. All three are in REPORT.md §12.6.

**Not touched.** Every other file in the report directory, `data/holdout/`,
`data/processed-blinded-*/`, and the unblinding key.
