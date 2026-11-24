---
title: "Local PPARα Is Necessary but Pharmacologically Unreachable in Diabetic Retinopathy: A Quantitative Exposure Analysis of Fibrates and Related Agents"
author: "OSPF Ayurveda Knowledge Graph Project"
date: "Revised 9 November 2026 (original analysis 5 October 2026)"
---

**Keywords:** diabetic retinopathy; PPARα; fenofibrate; pemafibrate; blood–retinal barrier; free-drug hypothesis; OATP1B; FGF21; liver X receptor; drug repurposing

**Note on evidence grading.** Every quantitative claim carries one of four tags. **[M]** measured (a primary experimental result, regulatory label or structure, source named); **[C]** computed (arithmetic on measured values, stated at the point of use); **[Mod]** modelled (output of a model over distributions chosen to span a published spread); **[R]** reasoned (a pharmacological argument with no computation). Conflating these tags, that is, presenting reasoning with the confidence of measurement, is the failure this paper is written to avoid.

# Abstract

**Background.** Fenofibrate slows diabetic retinopathy (DR) progression in the FIELD and ACCORD-Eye trials, and cell-type-restricted conditional deletion of *Ppara* worsens diabetic retinal injury in mice. Whether an orally dosed PPARα agonist can engage the receptor in retina has not been quantified.

**Methods.** We built a 23-input Monte-Carlo free-drug exposure model for four PPAR-active agents (fenofibric acid, pemafibrate, elafibranor with its active metabolite GFT1007, and seladelpar) across three retinal compartments, calibrated against the only published ocular measurement of a fibrate after systemic dosing and against three human aqueous-humour datasets. Potency was taken as inter-laboratory distributions of EC₅₀ from ChEMBL (5,271, 3,223 and 7,913 filtered activities on PPARα, PPARδ and PPARγ) and corrected for assay serum binding. Receptor and transporter expression was measured in 4.83 million adult human retinal cells (CZ CELLxGENE Census, 24 datasets), bulk retina (n = 523) and the Human Protein Atlas. The FGF21 humoral relay, the efflux (LXR) axis and neutral PPARα ligand design were analysed with separate models.

**Results.** Free drug at the retinal vascular endothelium, the most favourable compartment, was 37–51× below the free EC₅₀ at peak plasma concentration for fenofibric acid and pemafibrate (margins 0.020 and 0.027), 7.3× below for elafibranor + GFT1007 (0.136), and 1.8× below for seladelpar at PPARδ (0.558) [Mod]. Parity required 119–290× the labelled dose for the three PPARα agents. Neural retina is a further 5.3× worse (Kp,uu 0.059, 95% CI 0.009–0.354). Back-calculation against the observed clinical lipid effect requires a hepatic concentration factor of 37–92×, supplied by OATP1B1/1B3, which are 502.3 and 247.7 nTPM in liver and 0.0 in retina [M]. The shortfall is therefore mechanistic rather than a matter of dose. The FGF21 relay fails: achievable plasma FGF21 is 25× (95% CI 6–99×) below the lowest demonstrated active concentration, and human retina lacks β-Klotho (0.0 nTPM). The only compound within reach of a retinal receptor acts at PPARδ, the dominant isoform in every retinal vascular and immune compartment and a pro-angiogenic one. A non-acidic PPARα ligand is geometrically feasible (acceptor-atom span 2.222 ± 0.064 Å) but the best scaffold requires 36 g/day.

**Conclusions.** Local PPARα is necessary in retinal endothelium and microglia, and no available agent can reach it by the oral route. The ranked priority is therefore fenofibric acid as a systemic-limb lead, with elafibranor and seladelpar as mechanistic probes and a PPARδ hazard signal. The measurement that would most change the ranking is a PPARα/PPARδ EC₅₀ panel at stated, physiological albumin, which carries 69% of output variance at the endothelium and RPE. Intravitreal delivery, the existing standard of care, removes the barrier problem entirely and is the largest unexamined premise.

::: {.figure-box}

**Figure 1. Recommended compounds to advance against diabetic retinopathy, ranked by certainty of engaging a named target in a named compartment (not by potency).** Margin is free drug concentration ÷ free EC₅₀ at the retinal vascular endothelium, at Cmax; 1.0 is parity and every value is below it. All margins modelled [Mod] over 23 inputs (Sections 2.3 and 3.3).

| # | Compound | Role | Endothelial margin, Cmax | Rationale |
|---|---|---|---|---|
| **1** | **Fenofibric acid** | **Lead, systemic limb only** | **0.020** (51× short) | The compound the DR clinical evidence rests on. Certain hepatic engagement; local engagement excluded |
| **2** | Pemafibrate | **Downgraded** | 0.027 (37× short) | Most potent of the four and the worst retinal drug: its potency depends on a hepatic transporter the retina does not express |
| **3** | Elafibranor + GFT1007 | Probe, 12 wk | **0.136** (7.3× short) | Closest of the PPARα agents, and only via its active metabolite. Equal PPARδ potency makes it a pro-angiogenic risk in retinal vasculature |
| **4** | **Seladelpar** | **PPARδ probe** | **0.558** on PPARδ (1.8× short) | The only compound within reach of a retinal receptor, and it is the wrong receptor: a hazard finding before an opportunity |

*Olezarsen (matched non-PPAR apoC-III suppression) and inclisiran (3–5× the apoB effect of any fibrate) are carried as the control and falsification arms. Fenofibrate adds an esterase step to #1 without adding pharmacology. The stage is the same for every entry: mild-to-moderate non-proliferative disease.*

:::

# 1. Introduction

Diabetic retinopathy is a leading cause of vision loss in working-age adults. Current therapy acts late and, in the case of anti-VEGF and corticosteroid injection, locally. Two large trials, FIELD and ACCORD-Eye, reported reduced retinopathy progression with fenofibrate, a PPARα agonist. The mechanism is unresolved. Four mechanistic limbs have been proposed: (1) hepatic lowering of lipoprotein supply, (2) a hepatic-to-retinal FGF21 humoral relay, (3) local transrepression of inflammatory signalling in retinal endothelium, microglia and RPE, and (4) local transactivation of fatty-acid-oxidation genes in neural retina.

PPARα is a ligand-activated nuclear receptor governing fatty-acid catabolism. The retina is among the most lipid-dense and metabolically active tissues per gram, and the RPE oxidises phagocytosed photoreceptor outer-segment lipids as an energy source [R]. The receptor is present and the pathway it controls is one the tissue runs. Hard exudates in DR are not simply fat. They are retained, glycated and oxidised apoB lipoproteins deposited in Henle's layer, cytotoxic to pericytes, endothelium, Müller cells and RPE through endoplasmic-reticulum stress [R]. This may explain why plasma LDL-cholesterol tracks DR poorly while apoB particle number and remnant particles track it well.

This paper asks a narrower and more answerable question than "does fenofibrate work": **can an orally dosed PPARα-active compound reach its receptor in the compartments where genetics says the receptor matters, at a free concentration that engages it?** We treat the answer as a quantitative exposure problem and rank candidates by the certainty of engaging a named target in a named compartment, not by potency or by weight of accumulated evidence.

# 2. Methods

## 2.1 Candidate set and ranking criterion

Eight compounds were considered: fenofibric acid, pemafibrate, elafibranor (with GFT1007), seladelpar, olezarsen (control), inclisiran (falsification arm), fenofibrate (prodrug) and candesartan (comparator). Four carry a retinal exposure margin. Roles (lead, probe, control) are experimental priorities rather than assessments of commercial merit; a poor chronic drug can be the best available probe.

## 2.2 Receptor affinity

Affinities were taken from ChEMBL validity-filtered activities on human PPARA (CHEMBL239), PPARD (CHEMBL3979) and PPARG (CHEMBL235) [M]. Twenty-six PPARα EC₅₀ determinations from independent laboratories were summarised as distributions. The inter-laboratory spread is treated as the uncertainty, minimum values are not used as point estimates, and censored records (">") are reported but never averaged. Geometric standard deviation (GSD) was floored at 2.5 where n ≤ 3.

## 2.3 Free-drug exposure model

Margin is defined as free drug concentration divided by free EC₅₀ at a given compartment; 1.0 is parity and the reciprocal is the fold shortfall. Three compartments were modelled:

- **Retinal vascular endothelium**, the inner blood–retinal barrier, whose luminal membrane contacts plasma. Its ceiling is 1.0 and efflux, not partition, sets the shortfall.
- **RPE**, which faces the fenestrated choriocapillaris and is the one compartment that can exceed plasma free concentration if it concentrates organic anions.
- **Neural retina**, the only compartment behind tight junctions (two barriers).

Plasma exposure was drawn from FDA labels, with Cavg,ss derived as AUC(0–τ)/τ and Cmax reported as the best case. GFT1007 carries 3.2× the parent's exposure and was modelled as a fifth compound, equipotent with elafibranor. The model comprises 23 inputs and 200,000 Monte-Carlo draws. Because the EC₅₀ is corrected for assay serum binding (EC₅₀,free = EC₅₀,nominal × f~u,assay~), the free-fraction term appears on both sides and largely cancels. A 20-fold swing in pemafibrate's unmeasured plasma protein binding moves its margin only 2.3× [Mod].

**Calibration anchor.** Huang et al. [1] dosed C57BL/6J mice with fenofibrate 2 mg/kg/day i.p. for 7 days and measured fenofibric acid by LC-MS 6 h after the last dose: 0.140 ± 0.044 ng/mg total protein in pooled vitreous/retina against 86.304 ± 22.780 ng/mg in plasma [M]. The unit is ng per mg of *total protein*, not of tissue; conversion as a per-tissue-mass figure overstates retinal concentration roughly tenfold (neural retina is ~10% protein), and a second header ambiguity admits a 60-fold misreading. The paper's own choroid:plasma ratio (8.469/1.726 = 4.9, matching its text) confirms the common-unit reading. Because the sample pools vitreous and retina, the inversion keeps the phases separate:

C~u,retina~ = M × P / (V~vitreous~ + V~retina~ / f~u,retina~)

**Independent calibration.** Kp,uu was computed from three human cataract-surgery datasets measuring aqueous humour and plasma in the same patients [11–14] using Kp,uu = (C~aqueous~/C~plasma,total~)/f~u,plasma~, since aqueous humour is effectively protein-free.

**Sensitivity.** Saltelli/Jansen Sobol indices on log₁₀(margin) were computed over 819,200 model evaluations per compound-compartment and aggregated by input block (potency, barrier, plasma exposure), so that a block with eighteen individually small contributions is not under-ranked.

**Ionisation.** No experimental pKa, logP or logD exists for the four compounds in ChEMBL, PubChem or the reachable literature (ChEMBL no longer serves `cx_logd`, `cx_logp` or `cx_most_apka`). pKa was assumed from each head group's unsubstituted parent acid and logD(7.4) computed by Henderson–Hasselbalch [C].

## 2.4 Expression analyses

Single-cell detection (% of cells with ≥1 UMI) was computed from raw counts in the CZ CELLxGENE Discover Census LTS release 2025-11-08: 4,828,235 adult non-diseased human retinal cells, 24 datasets, 16 publications. PPARA, PPARD and PPARG were present in the feature space of all 24 datasets, so every reported zero is a measured non-detection. Six negative-control genes (ALB, INS, PRM1, KRT1, MYH7 and others) set an ambient floor of 0.00–0.1%. Independent bulk sources were EyeGEx (GEO GSE115828, n = 523 retinas), GSE160306 (79 samples from 43 donors, macula and periphery analysed separately, with graded diabetic status) and the Human Protein Atlas (HPA). Power to detect a diabetic change in *PPARA* was computed at 80%.

## 2.5 Auxiliary analyses

*FGF21 relay.* Plasma and active FGF21 concentrations were placed on one axis in 200,000 Monte-Carlo draws over published spreads, after converting PF-05231023 (a ~190 kDa CovX-body with two FGF21 arms; mature FGF21 19.5 kDa) to FGF21-equivalents through moles. *Efflux axis.* ChEMBL activities on nine LXR-axis genes were tabulated, 1,009 potent LXR ligands were filtered physicochemically, and a two-compartment burden model dL/dt = J~in~ − k~t~·E·L − k~a~·A·L was solved. *Neutral PPARα ligand design.* The AF-2 pocket geometry was measured from five agonist complexes, 25 candidate head groups were screened by computed acceptor span, efficacy was modelled with a two-state H12 model, and five scaffolds were carried through the exposure model. Full model code and data are listed in the Data Availability section.

# 3. Results

## 3.1 PPARα is abundantly expressed in human retina but not where the mechanisms are

PPARA was detected in 7.9–68.0% of cells in every retinal cell class against an ambient floor of 0.00–0.1%, and sits at the 92.4th percentile of the expressed transcriptome in 523 retinas (143.5 CPM, detected in 99.8%). In HPA bulk retina it is 16.6 nTPM, 54% of its level in liver [C] (Table 1).

**Table 1.** Detection (% of cells with ≥1 UMI) of PPAR isoforms by retinal cell type [M]. *n* cells in millions (M) or thousands (k).

| Cell type | n | PPARA | PPARD | PPARG | PPARD : PPARA |
|---|---:|---:|---:|---:|---:|
| Rod | 1.21M | **67.97** | 13.33 | 0.29 | 0.20 |
| RPE | 121k | **64.77** | 13.03 | 1.56 | 0.20 |
| Cone | 149k | **54.51** | 15.57 | 3.87 | 0.29 |
| Astrocyte | 39k | 20.91 | 14.53 | 11.22 | 0.69 |
| Müller glia | 256k | 18.17 | 16.13 | 1.36 | 0.89 |
| Pericyte | 20k | 19.90 | 21.93 | 17.17 | 1.10 |
| Endothelium | 141k | 15.39 | 17.67 | 3.66 | 1.15 |
| Vascular smooth muscle | 16k | 18.97 | 22.45 | 23.92 | 1.18 |
| Retinal ganglion cell | 444k | 13.04 | 23.13 | **46.31** | 1.77 |
| Amacrine | 596k | 11.76 | 26.39 | 5.36 | 2.24 |
| Microglia | 77k | 15.50 | **43.03** | 15.15 | 2.78 |

Receptor abundance is highest behind the barrier (rods, RPE, cones) and lowest in endothelium and microglia. The isoform ratio reverses at the neural/vascular boundary: PPARδ exceeds PPARα in every vascular and immune compartment (microglia 2.78×, ganglion cells 1.77×, smooth muscle 1.18×, endothelium 1.15×, pericytes 1.10×), although PPARα leads 3–5× in bulk because rods constitute roughly 70% of cells. PPARG is the ganglion-cell isoform (46.3% vs PPARA 13.0%).

The apparent conflict between antibody-based literature and retinal atlases is largely a detection artefact [M]. In rods, PPARA detection rises from 4.07% to 40.58% from the lowest to highest sequencing-depth decile, while negative controls stay at 0.00%. Whole-cell rod detection is 11.7–29.1% but single-nucleus detection is 53.0–82.0%, consistent with a nuclear-enriched transcript. What survives is a real discordance about which cells express the protein: the antibody literature emphasises Müller glia, endothelium, ganglion cells and microglia, which have the lowest transcript levels. The HPA retina immunohistochemistry panel (113 proteins) contains no PPAR isoform and grades PPARα immunofluorescence "Uncertain" for both antibodies.

**Retinal PPARA is not deficient in diabetes.** In GSE160306, PPARA changed by +0.046 log₂ in macula (p = 0.836) and −0.096 log₂ in periphery (p = 0.367), with no correlation to retinopathy severity (ρ = +0.057 and −0.102). The minimum detectable effect at 80% power was 1.40× (macula) and 1.26× (periphery), so this is a bounded null. Any agonist effect must be supraphysiological activation of a normally expressed receptor, not correction of a deficit.

## 3.2 Local PPARα is necessary in retinal endothelium and microglia

Two inducible, cell-type-restricted *Ppara* deletions have been reported in mouse retina (Table 2). Because hepatic PPARα is intact in both, plasma triglycerides, ketogenesis and FGF21 production are intact. The systemic confound that undermines interpretation of the global knockout is structurally absent rather than statistically adjusted. Neither paper measured ANGPTL4. No conditional deletion exists for RPE, Müller glia or photoreceptors, the three highest-PPARA compartments; findings from the global knockout in those cells [8] remain confounded.

**Table 2.** Conditional *Ppara* deletion studies in mouse retina [M].

| Compartment | Driver | Phenotype under diabetes | Source |
|---|---|---|---|
| Endothelium | *Vecad-CreERT2* | Declined ERG amplitude, decreased retinal thickness on OCT, increased vascular leakage; mitochondrial dysfunction and senescence | [2] |
| Microglia | *Cx3Cr1-CreERT2* | Decreased ERG response, exacerbated pericyte loss, increased STING/TNFα; no baseline phenotype; gain-of-function arm protective | [3] |

Both models show no phenotype without diabetic stress, the signature of a mechanism that operates during early injury and hence of mild-to-moderate non-proliferative disease as the relevant stage [M].

## 3.3 No available agent reaches the receptor

**Potency.** Fenofibric acid is a weak binder at its own receptor: median PPARα EC₅₀ 15,000 nM across 13 determinations (95% CI 2,490–90,400), with five further records censored at >10,000 nM [M]. Pemafibrate (1.0 nM, n = 3) is 3.4 log units more potent best-versus-best and 4.5 median-versus-median, yet circulates at roughly four orders lower free concentration (Table 3). Serum correction lowers EC₅₀ by 2.3× (fenofibric acid), 3.8× (pemafibrate), 5.2× (elafibranor) and 5.0× (seladelpar), which favours the compounds [C].

**Table 3.** PPAR EC₅₀ distributions [M]. † GSD floored at 2.5.

| Compound | Receptor | n (=) | Median EC₅₀ (nM) | 95% CI | Censored (>) |
|---|---|---:|---:|---|---|
| Fenofibric acid | PPARα | 13 | 15,000 | 2,490–90,400 | 10,000 ×4; 100,000 |
| Pemafibrate | PPARα | 3 | 1.0 | 0.17–6.0† | none |
| Elafibranor | PPARα | 8 | 290.5 | 12.8–6,610 | none |
| Seladelpar | PPARδ | 3 | 2.0 | 0.33–12.1† | none |
| Seladelpar | PPARα | 1 | 1,500 | 249–9,040† | 1,000 |

**Margins.** At Cmax, endothelial margins were fenofibric acid 0.0198 (51× short), pemafibrate 0.0267 (37×), elafibranor + GFT1007 0.136 (7.3×; P(margin ≥ 1) = 0.147) and seladelpar at PPARδ 0.558 (1.8×; P = 0.34) [Mod]. Seladelpar at PPARα was 0.00074 (1,340× short). At Cavg the endothelial margins were lower still (Table 4). Dose multiples required to reach parity were 119× (fenofibric acid), 290× (pemafibrate) and 135× (elafibranor); seladelpar at PPARδ needed 4.8× (95% CI 0.31–71×).

**Table 4.** Free-drug margin at Cavg, median [95% interval] [Mod].

| Compound | Receptor | Endothelium | RPE | Neural retina | P(endo ≥ 1) |
|---|---|---|---|---|---:|
| Fenofibric acid | PPARα | 0.0084 [6.8e-4–0.110] | 0.027 [9.9e-4–0.736] | 0.0016 [8.7e-5–0.027] | 0.000 |
| Pemafibrate | PPARα | 0.0035 [2.0e-4–0.058] | 0.011 [3.1e-4–0.373] | 0.0012 [1.3e-5–0.043] | 0.000 |
| Elafibranor + GFT1007 | PPARα | 0.031 [7.2e-4–1.42] | 0.098 [1.3e-3–7.96] | 0.0090 [8.5e-5–0.689] | 0.038 |
| Seladelpar | PPARδ | 0.210 [0.014–3.26] | 0.667 [0.021–21.3] | 0.047 [6.9e-4–1.73] | 0.135 |
| Seladelpar | PPARα | 2.8e-4 [1.9e-5–4.3e-3] | 8.9e-4 | 6.3e-5 | 0.000 |

**Barrier calibration.** Inversion of the Huang anchor gave Kp,uu (neural retina, fenofibric acid) = 0.0594 (95% CI 0.0090–0.3544), a 16.8× exclusion (CI 2.8–111×) [Mod]. Human aqueous-humour data for drugs that are not anionic efflux substrates give Kp,uu of 0.41–0.48 (aciclovir), 0.43–0.92 (levofloxacin) and 0.62–1.27 (pefloxacin), whereas indometacin, an anion that is 99% protein bound, was below assay limit [11–14] [C]. The model places an anionic fibrate an order of magnitude below the neutral drugs, as the measured transporter expression predicts: ABCB1 507.4, ABCC4 178.2 and ABCG2 142.0 nCPM in retinal endothelium, and ABCC5 822.8 and OAT3 464.7 nCPM in RPE [M]. No fibrate is a confirmed substrate of any of these pumps. The efflux term is carried as a 0.2–5× prior.

**The shortfall is mechanistic.** The model was run backwards against the observed clinical triglyceride effect (30–50% reduction) to obtain the hepatic concentration factor each compound requires (Table 5). Values of 37–92× require active uptake; for contrast ketoconazole, a neutral drug with no concentrative uptake, has measured hepatic Kp,uu of 0.32–4.67 [M]. The ordering matches the known hepatoselectivity of the four drugs even though no hepatoselectivity parameter appears in the model. The uptake transporters are measured and absent from retina: SLCO1B1 (OATP1B1) 502.3 nTPM in liver vs 0.0 in retina, SLCO1B3 (OATP1B3) 247.7 vs 0.0 [M]. These drugs are correctly dosed for a tissue that concentrates them 40–90×, and the retina is not that tissue.

**Table 5.** Hepatic Kp,uu required to reproduce the clinical effect [Mod].

| Compound | Receptor | Required liver Kp,uu | 95% CI |
|---|---|---:|---|
| Pemafibrate | PPARα | 91.6× | 7.5–1,160× |
| Elafibranor | PPARα | 42.7× | 1.2–1,420× |
| Fenofibric acid | PPARα | 37.5× | 4.0–335× |
| GFT1007 | PPARα | 13.5× | 0.37–476× |
| Seladelpar | PPARδ | 1.5× | 0.14–16.5× |

**Variance.** At endothelium and RPE the potency block (EC₅₀ and its assay serum conditions) accounted for a mean total Sobol index of 0.694 (range 0.589–0.818), barrier 0.194 and plasma exposure 0.111. In neural retina the barrier block dominated (0.509) with potency at 0.428. First-order indices summed to ~1.0 (near-additive in log space).

## 3.4 The FGF21 relay fails

Reported retinal protection used PF-05231023 at 50–100 ng/mL, equivalent to 10,263–20,526 pg/mL of FGF21 once the ~90% scaffold mass is removed [C]; no concentration below 50 ng/mL has been tested on any retinal preparation. Achievable plasma FGF21 on a fibrate is limited to a 1.28–1.61× rise over a baseline of 85–235 pg/mL in healthy adults (450–670 pg/mL in T2D with retinopathy), with a maximum observed absolute concentration of ~1,000 pg/mL [M]. The Monte-Carlo ratio gave baseline 550 pg/mL [249–1,213], achievable 598 [260–1,378] and active 15,049 [5,012–44,809], a shortfall of **25.0× [6.3–98.7×]**, with P(achievable ≥ active) = 0.000 [Mod]. Three constraints are independent of the arithmetic:

1. Native FGF21 at ~10³–10⁴× endogenous exposure (5 mg/kg twice daily) had no effect on retinal neovascularisation in mouse oxygen-induced retinopathy, while the 28-h half-life conjugate was protective [4] [M].
2. Human retina lacks the obligate co-receptor β-Klotho (KLB 0.0 nTPM, 9.2th percentile, vs 16.6 in liver); Müller glia and endothelium have abundant FGFR1 (214.4 and 116.7 nCPM) but KLB of 1.0 and 1.1 nCPM [M]. FGF21 itself is flat zero in every retinal cell type.
3. The epidemiological sign is wrong. Higher plasma FGF21 predicted more microvascular disease (n = 9,697) [6], and a larger fenofibrate-induced FGF21 rise predicted faster glycaemic progression (HR 1.18, top tertile) [7] [M].

The retinal biology of FGF21 is real but adiponectin-mediated: adiponectin deletion completely abolished FGF21's retinal protection in two models [4,5], and the retina is built to receive adiponectin (ADIPOR1 125.7 nTPM, 98th percentile). The fibrate-to-adiponectin step in humans is unquantified.

## 3.5 Local transactivation is excluded quantitatively

Free fenofibric acid sits roughly 600× below its free PPARα EC₅₀ in neural retina [Mod], robust across all 23 inputs. The effector programme is nevertheless present and expressed: CPT1A, ACADM, ACOX1, ABCG1, ABCA1 and others were detected in 10–50% of retinal cells [M]. HMGCS2 is RPE-specific (23.0% vs ≤0.1% elsewhere) and a direct PPARα target, making it the one tractable local-transactivation readout in human eye. PPARα outnumbers its obligate RXR partner by at least 6.4:1 in rods (a hypothesis from transcript detection, not a finding).

ANGPTL4, a direct PPARα target and pro-permeability factor, is expressed in pericytes (23.1%), smooth muscle (22.9%) and endothelium (12.0%), PPARδ-dominant compartments. Its induction cannot exceed a ceiling set by the observed fall in triglycerides (ANGPTL4 inhibits lipoprotein lipase). Fenofibrate and pemafibrate reliably raise circulating ANGPTL4 2–4× [M], so plasma ANGPTL4 is a mandatory biomarker. If local engagement is too weak to help, it is too weak to harm.

## 3.6 Seladelpar reaches a retinal receptor, but the wrong one

Seladelpar needs a hepatic concentration factor of only 1.5×, so it does not depend on the missing transporter. Its endothelial margin at PPARδ is 0.558 [0.038–8.59] at Cmax, with RPE margin 1.77 and P(margin ≥ 1) = 0.34 and 0.62 respectively [Mod]. Because PPARδ is pro-angiogenic and dominant in retinal vasculature and microglia, **the only local retinal receptor engagement achievable from an oral dose in this class is at a receptor whose engagement may worsen the disease.** Elafibranor engages PPARα and PPARδ equally (both pChEMBL 8.00) and is not a neutral dual agonist in retinal vasculature.

## 3.7 The efflux arm is the one place the arithmetic favours a new agent

Of 3,732 qualifying activities across nine lipid-efflux axis genes, 3,729 were at LXRα/β and none at ABCA1, ABCG1, APOA1 or APOE [M]. The only approved drug with a recorded ABCA1 mechanism, probucol, is an inhibitor. LXR ligands are 79% neutral (802 of 1,009), unlike the PPARα pocket's mandate for a lipophilic acid. Going neutral yields a paired median 10–12× gain in neural-retina Kp,uu (95% CI 1.9–64×) and relaxes the β-isoform selectivity needed for a 10× hepatic margin from ~2.73 to ~1.55 log units (a 1.16 log advantage) [Mod]. Of 83 measured acidic LXR ligands, none exceeds 2.73 log (best 2.66). However, no public molecule demonstrates the required selectivity in a cell: the maximum cell-based β-selectivity across 106 paired molecules is 1.37 log, and the five candidates that pass the neutral bar and a retinal-access filter derive from one 2018 patent using cell-free data [M]. Lipophilicity is the new liability (416 of 1,009 ligands have logD > 5).

In the burden model, a transporter inducer (even 1000×) leaves steady-state burden infinite when transporter activity E = 0, whereas a direct acceptor at 0.1× healthy clearance gives a finite burden of 10.0 (Table 6). The acceptor contributes more only below E\* = k~a~·A/(k~t~·(F−1)) ≈ 0.011 for the cases modelled; E in diabetic human retina has not been measured in any species and decides between the two programmes. Apolipoprotein A-I mimetics, reconstituted HDL and cyclodextrins do not cross the blood–retinal barrier, so a direct acceptor is an intravitreal proposition. That route is already standard of care in DR.

**Table 6.** Steady-state lipid burden at E = 0 [Mod].

| Arm | Burden |
|---|---|
| Untreated | ∞ |
| Supply-lowering (influx ÷ 10) | ∞ |
| Transporter inducer (1000×) | ∞ |
| Direct acceptor (0.1× healthy clearance) | 10.0 |

## 3.8 A non-acidic PPARα ligand is buildable but not worth building

Across five PPARα agonist complexes, the two engaged ligand acceptor atoms lie 2.222 ± 0.064 Å apart (range 2.13–2.29), which requires a geminal pair, with four hydrogen-bond donors (Ser280, Tyr314, His440, Tyr464) converging on two atoms [M]. Tetrazole fails on lone-pair capacity (no atom can accept two hydrogen bonds), and the 1,2,4-oxadiazol-5(4H)-one fails because it presents one double-acceptor atom. Three of 25 neutral head groups survive: oxazolidin-2-one (2.29 Å), dimethyl sulfone (2.52 Å) and methanesulfonamide (2.53 Å) [C]. The head-region free volume is equal for PPARα (40.8 ± 7.1 Å³) and PPARγ (38.6 ± 1.1 Å³); the discriminator against γ is geometry (PPARγ spans 4.46 Å using three atoms), but it gives no handle against PPARδ (2.10 Å) [C].

Neutral heads raise neural-retina Kp,uu 19.7× (0.041 to 0.82–0.96), but the endothelium is blood-facing and its retention term is compound-independent in the model, so the gain appears only behind the tight junction. Predicted tissue Emax is 57–82% (95% CI 8–95%) against 92–98% in a coactivator-rich reporter assay, a systematic assay bias; two unmeasured H12 conformational-energetics parameters account for most variance (rank correlations 0.73 and 0.59) [Mod]. Potency from pEC₅₀ = LLE + logP, calibrated on oleoylethanolamide (predicted 126 nM, measured 120 nM–3 µM), is poor because neutral PPARα ligands sit at LLE ≈ 1.0 compared with pemafibrate's anionic 3.45 [C]. Free-drug margin rises monotonically with logP across the whole drug-like range, so the low-logD design strategy is inverted: logP 5.57 → 2.79 costs ≈200× (neutral) to ≈350× (acid) (Table 7).

**Table 7.** Scaffolds carried through the exposure model [Mod].

| | OXZ-1 | SULF-1 | PHOS-1 | ACID-LOW (control) | HYDX-1 |
|---|---|---|---|---|---|
| Head group | oxazolidin-2-one | methyl sulfone | phosphonamidate | carboxylate | hydroxamic acid |
| logD₇.₄ | 2.66 | 3.43 | 3.50 | −1.16 | 3.14 |
| Derived EC₅₀ | 64 µM | 42 µM | 3.3 µM | 2.0 µM | 20 µM |
| Kp,uu, neural retina | 0.82 | 0.94 | 0.96 | 0.041 | 0.94 |
| Tissue Emax | 0.61 | 0.57 | 0.82 | 1.00 | 0.57 |
| Dose for free-EC₅₀ occupancy | 833 g/day | 1,058 g/day | 36 g/day | 3.7 g/day | 541 g/day |

The best neutral scaffold requires 36 g/day and a lipophilicity-stripped acid control still beats every neutral by 9.7×. If endothelial retention scaled with the same efflux liability as neural retina, every neutral scaffold would improve by up to ~20× (PHOS-1 to ~1.8 g/day), which is still not a dose. The probability of technical success to a Phase 2a retinal biomarker readout is 3–8% [R].

## 3.9 Ranking

Table 8 gives the resulting ranking. Hit counts from curated interaction databases are unreliable for ranking: for quercetin, the curated count was 26 of 27 panel genes, whereas ChEMBL showed three genes bound at ≤1 µM and none of the PPARα effector genes. Across 153 compounds, only 15 bind any panel gene at ≤1 µM, catalogue size correlates with hit count (r = 0.911), and the mean number of effector genes bound is 0.046 [M]. Note that a blank in ChEMBL means "not measured", not "no interaction".

**Table 8.** Candidate ranking (endothelial margin at Cmax [Mod]).

| # | Compound | Role | PPARα / δ / γ (pChEMBL) | Margin | Basis |
|---|---|---|---|---|---|
| 1 | Fenofibric acid | Lead, systemic limb only | 4.82 median / n.d. / 4.00 | 0.020 (51×) | Certain hepatic engagement; the compound the DR clinical evidence rests on; local engagement excluded |
| 2 | Pemafibrate | Downgraded | 9.00 / 5.80 / 5.96 | 0.027 (37×) | Most potent, worst retinal drug: depends most on hepatic OATP uptake (required Kp,uu 91.6×) |
| 3 | Elafibranor + GFT1007 | Probe, 12 wk | 8.00 / 8.00 / 6.76 | 0.136 (7.3×) | Closest of the PPARα agents via active metabolite; equal PPARδ potency is a pro-angiogenic risk |
| 4 | Seladelpar | PPARδ probe | 5.82 / 8.72 / n.d. | 0.558 at PPARδ (1.8×) | Only compound within reach of a retinal receptor, and it is the wrong receptor |
| 5 | Olezarsen | Control | n.d. | n.d. | Matched non-PPAR apoC-III suppression |
| 6 | Inclisiran | Falsification arm | n.d. | n.d. | 3–5× the apoB effect of any fibrate |
| 7 | Fenofibrate | Prodrug of #1 | 6.00 / n.d. / 6.24 | n.d. | Adds an esterase step; 42× worse ocular distribution than the acid by the systemic route [C] |
| 8 | Candesartan | Comparator | n.d. | n.d. | Engagement certain at a luminal target; blocked by background therapy |

Quercetin, minocycline (papilloedema risk attacks the endpoint), epalrestat (excellent engagement of a falsified target) and dietary fatty acids (plasma concentrations already sit at their own EC₅₀) ranked below the field.

# 4. Discussion

## 4.1 Principal finding

Two solid results point in opposite directions. Genetics shows that local PPARα in endothelium and microglia matters, and quantitative pharmacology shows that no oral compound in this class can reach it. The fibrate benefit in FIELD and ACCORD-Eye is real and is explained by none of the four proposed limbs. Three resolutions remain live and are experimentally separable: (i) the clinical benefit comes from the systemic limb after all, and the conditional-knockout phenotypes describe real biology the drug does not use; (ii) the benefit is receptor-independent (fenofibrate has documented receptor-independent effects, and much supporting in-vitro work uses concentrations above where these appear, without knockout controls); or (iii) the exposure model is wrong somewhere, most plausibly in the net direction of RPE anion transport (prior spans 100×), the compound-independence of endothelial retention, or the EC₅₀ distribution itself.

## 4.2 Why potency does not rank retinal drugs

Pemafibrate is the most potent PPARα agonist yet the worst retinal drug, because its hepatic selectivity is bought with a transporter dependence the retina cannot satisfy. A more selective PPARα agonist is a worse retinal drug, not a better one. This inverts the usual ordering by potency and explains why this ranking is by certainty of engagement.

## 4.3 Staging, enrichment and the wrong-sign risk

Supply-lowering is mechanically inoperative before the barrier leaks, as there is no extravasation to prevent [R]. The conditional knockouts show no baseline phenotype without diabetic stress. Together these indicate mild-to-moderate non-proliferative disease as the stage, the most robust conclusion in this work. Enrichment on existing hard exudate selects patients in whom a supply-lowering mechanism is weakest, because an established deposit is self-renewing and clearance-limited. Enrichment should therefore be on rate (elevated remnants despite statin; new or worsening lesions over a prior interval, excluding organised subfoveal plaque). Intraocular ANGPTL4 stratified by fibrate exposure has never been measured in any species (ten query strings searched [M]).

## 4.4 Experimental programme

Table 9 sequences ten experiments. Items 1–7 cost roughly $300–470k over 9–12 months. The critical path has moved: the programme had been sequenced behind an ocular PK measurement that carries 19% of the variance in the blood-facing compartments, whereas the PPARα/δ EC₅₀ at stated albumin carries 69%, and resolving it is cell culture. **If the free EC₅₀s come back 10× below the corrected values here, elafibranor and seladelpar reach parity at the endothelium and their verdicts are withdrawn.**

**Table 9.** Sequenced experiments.

| # | Experiment | Cost | Time | Decides |
|---|---|---|---|---|
| 1 | Lipid-change covariate analysis of existing trial data | ~$0 | weeks | Supply limb vs everything else |
| 2 | PPARα/δ EC₅₀ panel, four compounds, one assay, stated physiological albumin | $30–60k | 2–3 mo | 69% of variance at endothelium/RPE |
| 3 | Equilibrium dialysis (mouse fenofibric acid) + shake-flask logP ×4 | ~$15k | 1 mo | Tightens anchor |
| 4 | Validated PPARα immunostain on donor retina | $15–30k | 2–3 mo | Antibody/transcript conflict |
| 5 | Rodent transactivation vs transrepression, paired ocular LC-MS, knockout and non-PPAR lipid arms, PPARδ controls | $150–250k | 6–9 mo | Whether any local engagement occurs |
| 6 | ABCA1/ABCG1 activity in diabetic human retina | $50–75k | 6 mo | Acceptor vs inducer |
| 7 | LXR candidate transactivation in retinal cell; SREBF1 in hepatocyte | ~$40k | 3–4 mo | Cellular selectivity |
| 8 | Human aqueous drug + ANGPTL4 at cataract surgery | $50–100k | 6–12 mo | Neural-retina barrier; wrong-sign question |
| 9 | Lipid clearance rate constant | ~$75k | 6 mo | Bounded vs delayed benefit |
| 10 | RPE/photoreceptor-specific conditional deletion | $150–300k | 18–24 mo | Necessity in high-expression compartments |

Kill criteria are: a flat rodent study with confirmed ocular drug concentration (no achievable local engagement; local chemistry stops); reproduction of the effect by a matched non-PPAR lipid arm; failure of receptor knockout to abolish the effect; a benefit that tracks lipid change tightly; confirmation of the current EC₅₀s; absence of PPARα protein from endothelium and microglia on validated stain; and failure of cellular β-selectivity in the LXR series. Observation windows must be justified against clearance rather than calendar: a stock readout (lesion burden) has time constant 1/clearance, the parameter this disease suppresses, and can read flat at twelve months while the mechanism is working, so flux should be primary.

## 4.5 The route assumption

Every candidate here was judged on oral systemic feasibility for a disease whose standard of care is injection into the target compartment. Intravitreal delivery makes the entire exposure analysis moot for whatever is delivered that way. This is not an uncritical preference, since chronic intravitreal dosing carries its own burden and risk, but oral bioavailability should not be treated as a precondition. The strongest combination concept is oral supply-lowering plus a locally delivered ApoA1-mimetic acceptor at an injection visit patients already attend. Combining supply-lowering with scavenger-receptor blockade is wrong-signed, since macrophage uptake is the only catabolic route for retained retinal lipoprotein.

## 4.6 Limitations

(i) All margins are modelled; no fibrate concentration has been measured in any ocular compartment after oral dosing in any species, and the one reported oral rat attempt (below detection) rests on a secondhand citation. (ii) The calibration anchor is a single mouse experiment using i.p. dosing of the prodrug and pooled vitreous + retina. (iii) The aqueous-humour calibration uses the blood–aqueous barrier, a related but different tissue from the blood–retinal barrier. (iv) Transporter data are mRNA from one consortium; no protein-level measurement exists, and no fibrate is a confirmed substrate of the efflux pumps. (v) The RPE margins are the least trustworthy numbers (net anion transport direction unmeasured), and if RPE OAT1/OAT3 concentrate these acids the compartment ordering inverts. (vi) No experimental pKa, logP or logD exists for any of the four compounds, and pemafibrate plasma protein binding is unmeasured. (vii) GFT1007's own EC₅₀ is unmeasured, so the combined elafibranor margin is an upper bound. (viii) Pemafibrate potency rests on n = 3. (ix) GSE160306 is the only public human neural-retina diabetic series, nothing in a 95-gene panel survives FDR in it, and no single-cell atlas of diabetic human retina exists (13,075,889 human eye cells are available, none diabetic). (x) The retinal KLB result rests on one consortium's two arms; single-cell confirmation is specified but not completed. (xi) The RXR stoichiometry argument rests on transcript detection. (xii) A blank in ChEMBL denotes absence of measurement, not absence of interaction. This is a computational and literature-based analysis; nothing here is a clinical recommendation and all findings require experimental validation.

# 5. Conclusions

1. Local PPARα in retinal endothelium and microglia is necessary, and no fibrate reaches it: every PPARα compound is 37–1,340× short at the most favourable compartment at peak plasma concentration.
2. The shortfall is mechanistic. A 37–92× hepatic concentration step supplied by OATP1B, absent from retina, cannot be overcome by dose.
3. The fibrate benefit in FIELD and ACCORD-Eye is real and now unexplained by any of the four proposed limbs.
4. The FGF21 relay fails (25× concentration shortfall, missing co-receptor, wrong epidemiological sign); the surviving route is adiponectin-mediated and unquantified in humans.
5. The restore-a-deficit framing is unsupported: retinal PPARA is not reduced in diabetes.
6. The one compound that reaches a retinal receptor reaches a pro-angiogenic one; PPARδ activity is a hazard finding before an opportunity.
7. The relevant stage is mild-to-moderate non-proliferative disease.
8. A non-acidic PPARα ligand is buildable but not worth building (36 g/day; probability of technical success 3–8%).
9. The efflux arm (LXR) is the one place the arithmetic favours a new agent, contingent on cellular isoform selectivity not yet shown and on one unmeasured retinal parameter, E.
10. The critical path is an EC₅₀ panel at physiological albumin, not an ocular pharmacokinetic study.
11. The largest unexamined premise is route: DR is treated by injection into the target compartment.

# Data and Code Availability

Analysis code is in the project repository under `src/analysis/` (`ocular_exposure/`, `retina_expression/`, `fgf21_bridge/`, `efflux_axis/`, `ppara_ligand_design/`, `dr_matrix/`). Processed outputs are in `data/processed/`, including `ocular_exposure_margins.tsv` (36 rows), `retina_sc_celltype_summary.tsv`, `retina_bulk_dr_expression.tsv`, `chembl_panel_bioactivities.csv` (62,219 measured activities; 16,407 on PPAR receptors) and `opentargets__DR_gene_disease.csv` (2,652 gene–disease associations). Public sources are CZ CELLxGENE Discover Census (LTS 2025-11-08), GEO GSE115828 and GSE160306, the Human Protein Atlas, ChEMBL and Open Targets.

# References

1. Huang et al. *Biology (Basel)* 2021;10(12):1328. PMID 34943243. (Fenofibrate ocular distribution in mouse; calibration anchor.)
2. Endothelial-specific conditional *Ppara* deletion in diabetic mouse retina. *Am J Pathol* 2026;196(4):960–975. PMID 41485550.
3. Microglia-specific conditional *Ppara* deletion in diabetic mouse retina. *Cells* 2022;11(23):3869. PMID 36497130.
4. FGF21 (PF-05231023) in oxygen-induced retinopathy; adiponectin dependence. PMID 28199833.
5. Adiponectin-dependent retinal protection by FGF21. PMID 36943533.
6. Plasma FGF21 and microvascular disease (n = 9,697). PMID 26055067.
7. Fenofibrate-induced FGF21 change and glycaemic progression (n = 9,697). PMID 28606915.
8. Global *Ppara* knockout, photoreceptor and RPE phenotypes. *PLoS One* 2019;14(2):e0208399. PMID 30716067.
9. Pemafibrate and ANGPTL4 mRNA in a human RPE cell line. PMID 39768065.
10. Pravastatin transport at the rat blood–retinal barrier. PMID 26431714.
11. Aciclovir aqueous humour penetration in humans. PMID 6696872.
12. Levofloxacin aqueous humour penetration in humans. PMID 15917572.
13. Pefloxacin aqueous humour penetration in humans (n = 38). PMID 1955654.
14. Indometacin aqueous humour penetration in humans. PMID 6626018.
15. CZ CELLxGENE Discover Census, LTS release 2025-11-08.
16. EyeGEx, GEO GSE115828; GEO GSE160306.
17. Human Protein Atlas (bulk and single-cell retina; antibodies HPA066941, CAB075701).
18. ChEMBL targets CHEMBL239 (PPARA), CHEMBL3979 (PPARD), CHEMBL235 (PPARG).

*Reference titles for entries 1–14 are descriptive summaries inferred from how each source is used in the underlying report; verify against PubMed before submission.*
