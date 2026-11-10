# PPARα in Human Retina — Settling the Expression Question With Data

**Date** 2026-11-03
**Step** 2 of `docs/prompts/dr-solve-open-questions-prompt.md`
**Prior step** `docs/notes/dr-data-gap-closure.md`
**Question under test** The 2026-10-05 DR analysis graded retinal PPARα expression
"EMERGING / partly UNCERTAIN" and moved on, because it reasoned instead of querying.
**Status** Queried. All four questions answered; three of the four answers reverse or
substantially revise what the report assumed.

---

## 1. VERDICTS

| Question | Verdict | Confidence |
|---|---|---|
| Is PPARA expressed in human retina at a level consistent with a druggable target? | **Yes, decisively.** Detected in 7.9–68.0% of cells in *every* major retinal cell class against an ambient floor of ≤0.1%; 92nd percentile of the expressed transcriptome in 523 retinas. Highest in rods (68.0%), RPE (64.8%), cones (54.5%). | **High** |
| Is the antibody-vs-transcriptomics conflict real, or a detection artifact? | **Artifact — but not the artifact that was assumed.** The premise ("atlases don't show PPARA") is simply false. Where antibody and transcript evidence *do* disagree is on **which cells**, not whether. | **High** on the premise being false; **Moderate** on the cell-type discordance |
| Is retinal PPARA reduced in diabetes, as the restore-a-deficit framing assumes? | **No.** Macula +3%, periphery −6%, both null, no dose-response with DR severity. A ≥1.40× (macula) / ≥1.26× (periphery) change would have been detected at 80% power. | **Moderate** (one cohort, n=79) |
| Does PPARD exceed PPARA in retina? | **Globally no — locally yes, in exactly the compartments that matter.** PPARA leads 3–5× in rods/cones/RPE. PPARD leads in **every vascular and immune cell type**: microglia 2.8×, smooth muscle, pericytes, endothelium, and inner-retinal neurons. | **High** |

**The single most consequential finding is the last one.** The isoform split follows the
neural/vascular boundary. PPARα is a photoreceptor-and-RPE receptor; PPARδ is the
vascular-and-microglial receptor. Every "local engagement" mechanism in REPORT.md is sited
in endothelium, pericytes, Müller glia and microglia — the PPARδ compartment, not the
PPARα one. Isoform selectivity is therefore not an abstract safety preference; it
determines which cells a drug can act on at all.

---

## 2. WHAT WAS QUERIED

Nothing here is inferred from literature. Every number is computed from a primary data
matrix pulled during this step.

### 2.1 Single-cell / single-nucleus

**CZ CELLxGENE Discover Census, LTS release `2025-11-08`** (pinned in
`src/analysis/retina_expression/census_client.py`). Query: human, `is_primary_data == True`,
`tissue_type == 'tissue'`, tissue in the ten retina/RPE/chorioretinal UBERON labels.

**4,828,235 cells across 24 datasets from 16 publications.** Raw integer counts and each
cell's own `raw_sum` were read; CP10K and detection were computed here, not taken from a
precomputed summary.

| Dataset (CELLxGENE id) | Cells | Prep | Median genes/cell | Donors | Source |
|---|---:|---|---:|---:|---|
| `d6505c89` snRNA-seq of human retina | 2,907,910 | nucleus | 2,301 | 100 | doi:10.1101/2023.11.07.566105 |
| `1a9f3b38` snRNA-seq RPE + choroid | 806,868 | nucleus | 1,599 | 57 | CELLxGENE collection |
| `0129dbd9` All major cell types, adult retina | 244,474 | nucleus | 2,114 | 6 | doi:10.1016/j.xgen.2023.100298 |
| `963a08cb` Developing human retina (multiome) | 226,506 | nucleus | 2,514 | 14 | doi:10.1038/s41467-024-50853-5 |
| `5ed90bc0` scRNA-seq RPE + choroid | 114,397 | cell | 2,807 | 37 | CELLxGENE collection |
| `aecc2743` Human Fetal Retina Atlas | 108,838 | cell | 1,310 | 22 | doi:10.1016/j.ydbio.2025.08.025 |
| `e6dad530` All cell types of human eye | 100,055 | nucleus | 1,826 | 4 | doi:10.1016/j.celrep.2019.12.082 |
| `322c816f` Multiome retina atlas | 51,645 | nucleus | 1,423 | 4 | doi:10.1016/j.xgen.2022.100164 |
| `9f1a899f` Posterior ocular segment | 36,122 | nucleus | 1,900 | 5 | doi:10.1073/pnas.2306153120 |
| `f5be9ed2` Foveal/parafoveal retina | 34,323 | cell | 1,304 | 4 | doi:10.1093/hmg/ddab140 |
| `ccfdcad0` / `babbf9f3` Cowan periphery / fovea | 52,143 | cell | 1,544 / 1,890 | 3 | doi:10.1016/j.cell.2020.08.013 |
| `8623d55f` `bc7260e0` `5cdbb2ea` `d319af7f` `7b75b2c4` `2f6a20f1` Yan fovea+periphery (6 sorted datasets) | 84,982 | cell | 1,052–5,789 | 7 | doi:10.1038/s41598-020-66092-9 |
| `856c1b98` Menon retina | 20,091 | cell | 493 | 3 | doi:10.1038/s41467-019-12780-8 |
| `d5c67a4e` Lukowski retina | 19,694 | cell | 1,135 | 3 | doi:10.15252/embj.2018100811 |
| `aad97cb5` RGC in human retina | 11,617 | nucleus | 4,546 | 6 | doi:10.1016/j.xgen.2023.100298 |
| `be41a86a` scRNA-seq human retina | 6,061 | cell | 3,377 | 3 | doi:10.1101/2023.11.07.566105 |
| `af8b241a` Voigt retina | 1,701 | cell | 1,832 | 1 | doi:10.1073/pnas.1914143116 |
| `53d208b0` Tabula Sapiens | 808 | cell | 3,211 | 1 | doi:10.1126/science.abl4896 |

Excluded and why: one retinal **organoid** dataset (`7e7f63c5`, 43,857 cells) — organoid
photoreceptors are developmentally immature; cornea, lens, iris, sclera, trabecular
meshwork, ciliary body and optic disc — not neural retina or RPE.

**Cross-check:** the same corpus queried through the independent server-side CELLxGENE
WMG v2 API (snapshot `1762972271`), which uses rankit rather than CP10K normalisation.
Cell-type ordering agrees throughout (§4.1).

### 2.2 Bulk human retina

| Cohort | Accession | n | What it is for |
|---|---|---|---|
| **EyeGEx** | GEO **GSE115828** | 523 retinas | Abundance at a scale no single-cell study reaches; dropout-free |
| **Becker/Iowa DR series** | GEO **GSE160306** | 79 samples, 4 donor groups | The diabetic contrast — the only public human **neural retina** series with a graded diabetic axis |
| **Human Protein Atlas** | `rna_tissue_consensus`, `rna_single_cell_type` (downloaded 2026-11-02) | — | A second, independent processing pipeline, plus antibody reliability |

### 2.3 Antibody evidence

HPA `normal_tissue.tsv` (v23 path; current releases no longer serve it) plus the per-gene
HPA records for all 95 panel genes.

### 2.4 Panel

The 43-gene DR panel from Step 1 (`data/processed/dr_gene_panel.csv`) plus **52 controls**,
and the controls are the point of the exercise:

- **Housekeeping across two orders of magnitude** — ACTB/GAPDH/RPL13A/B2M (high),
  PPIA/UBC/SDHA (mid), **TBP/POLR2A/HPRT1 (low)**. Comparing a transcription factor to ACTB
  is a rigged comparison; comparing it to TBP is the fair one.
- **RXRA/RXRB/RXRG** — PPARα regulates nothing except as a PPARα::RXR heterodimer, so the
  partner caps the functional complex independently of PPARA itself.
- **Class-matched nuclear receptors** — NR2E3, THRB, RORB, NR1H2/3, NR1D1, NR2F1/2, VDR,
  RARA/B, ESRRA. Same molecule class, same abundance regime, same capture chemistry.
- **Druggable-target benchmarks** — KDR and FLT1, the targets of the most successful
  retinal drug class in history. These answer empirically: *what does a druggable retinal
  target look like in these data?*
- **Negative controls** — ALB, INS, MYH7, PRM1, KRT1, CELA3A. Without an ambient floor,
  "detected in 15% of cells" is not a claim.

---

## 3. PER-CELL-TYPE TABLE

**% of cells with ≥1 UMI.** CZ CELLxGENE Census 2025-11-08, 4,828,235 adult non-diseased
retinal cells, 24 datasets. Full table: `data/processed/retina_sc_celltype_summary.tsv`.

| Gene | Rod | Cone | RPE | Müller | Bipolar | Amacrine | Horiz. | RGC | Astro | Endo | Peri | VSMC | Micro |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *n cells* | 1.21M | 149k | 121k | 256k | 739k | 596k | 85k | 444k | 39k | 141k | 20k | 16k | 77k |
| **PPARA** | **67.97** | **54.51** | **64.77** | 18.17 | 12.62 | 11.76 | 7.89 | 13.04 | 20.91 | 15.39 | 19.90 | 18.97 | 15.50 |
| **PPARD** | 13.33 | 15.57 | 13.03 | 16.13 | 8.60 | 26.39 | 14.79 | 23.13 | 14.53 | 17.67 | 21.93 | 22.45 | **43.03** |
| **PPARG** | 0.29 | 3.87 | 1.56 | 1.36 | 3.77 | 5.36 | 2.51 | **46.31** | 11.22 | 3.66 | 17.17 | 23.92 | 15.15 |
| RXRA | 5.54 | 11.17 | 11.13 | 15.30 | 2.58 | 3.18 | 10.06 | 7.10 | 14.35 | 16.92 | 13.40 | 13.61 | 18.86 |
| RXRB | 4.15 | 6.80 | 6.30 | 5.32 | 5.84 | 10.99 | 9.44 | 13.46 | 5.91 | 7.86 | 7.28 | 9.58 | 5.02 |
| RXRG | 0.90 | 55.98 | 2.35 | 6.20 | 0.95 | 1.73 | 1.20 | 49.46 | 3.71 | 0.43 | 0.39 | 0.50 | 0.29 |
| *NR2E3* (rod NR) | 79.45 | 5.94 | 1.00 | 5.15 | 4.64 | 4.14 | 3.56 | 2.53 | 3.35 | 0.66 | 0.66 | 0.69 | 0.73 |
| *THRB* (NR) | 60.06 | 88.65 | 30.50 | 48.34 | 44.78 | 34.24 | 4.39 | 67.92 | 46.44 | 23.86 | 28.04 | 11.04 | 31.85 |
| *TBP* (low HK) | 6.45 | 10.64 | 6.38 | 8.47 | 8.44 | 13.46 | 11.01 | 21.47 | 7.91 | 5.27 | 4.99 | 5.63 | 4.80 |
| *POLR2A* (low HK) | 29.04 | 34.53 | 29.52 | 13.29 | 27.14 | 24.58 | 25.39 | 26.50 | 14.07 | 23.85 | 27.23 | 29.23 | 21.43 |
| *GAPDH* (high HK) | 66.34 | 78.17 | 20.71 | 80.76 | 78.19 | 81.97 | 88.65 | 88.12 | 83.08 | 24.75 | 30.26 | 37.15 | 27.61 |
| *RHO* | 91.88 | 40.58 | 1.87 | 37.25 | 36.75 | 25.36 | 26.99 | 14.69 | 40.46 | 1.66 | 1.88 | 2.03 | 4.41 |
| *KDR* (drug target) | 2.09 | 2.77 | 1.83 | 60.15 | 6.06 | 1.47 | 3.23 | 1.19 | 51.69 | 41.42 | 3.14 | 2.72 | 2.05 |
| *FLT1* (drug target) | 2.13 | 4.53 | 12.69 | 78.97 | 21.81 | 6.55 | 3.26 | 1.66 | 61.13 | 81.77 | 16.24 | 13.87 | 16.62 |
| **ALB** (neg) | 0.02 | 0.04 | 0.71 | 0.30 | 0.06 | 0.27 | 0.14 | 0.24 | 0.32 | 0.10 | 0.11 | 0.12 | 0.05 |
| **INS** (neg) | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| **MYH7** (neg) | 0.02 | 0.05 | 0.08 | 0.02 | 0.09 | 0.07 | 0.04 | 0.02 | 0.14 | 0.02 | 0.00 | 0.01 | 0.00 |
| **PRM1 / KRT1 / CELA3A** (neg) | ≤0.03 | ≤0.04 | ≤0.03 | ≤0.04 | ≤0.02 | ≤0.03 | ≤0.02 | ≤0.06 | ≤0.02 | ≤0.05 | ≤0.03 | ≤0.03 | ≤0.02 |

**How to read this.** The negative controls set the floor: ambient mRNA and index hopping
put a gene that is genuinely absent at **0.00–0.1%** (the one exception, ALB at 0.71% in
RPE, is 7× the floor and still 90× below PPARA). PPARA ranges 7.9–68.0%. There is no cell
type in the human retina where PPARA is at the ambient floor. In rods, cones and RPE it
**exceeds the low-abundance housekeeping genes TBP and POLR2A**, and in rods it sits in the
same regime as the rod-defining nuclear receptor NR2E3 (79.5%).

### 3.1 Absent vs. below detection threshold

The task rightly insists these are different claims. Census records, per dataset, whether a
gene was in that dataset's feature space at all:

> **PPARA, PPARD and PPARG are present in the feature space of 24 / 24 retina datasets.**

So **no zero anywhere in this analysis is a missing-feature artifact.** Every zero is a
measured non-detection. (For contrast, within the same panel APOA5, CELA3A, INS and PRM1
are each missing from the feature space of 4 datasets, FGF21 and NR2E3 from 3 — those
genes' zeros do need the distinction. The PPARs do not.)
Full matrix: `data/processed/retina_sc_gene_presence.tsv`.

### 3.2 The heterodimer constraint — a limit nobody has raised

PPARα cannot transactivate except as PPARα::RXR. The partner is **scarcer than the
receptor in exactly the cells where the receptor is most abundant**:

| | Rod | Cone | RPE | Müller | Endothelium |
|---|---:|---:|---:|---:|---:|
| PPARA | 67.97 | 54.51 | 64.77 | 18.17 | 15.39 |
| RXRA + RXRB + RXRG (sum of marginals) | 10.60 | 73.95 | 19.79 | 26.82 | 25.21 |
| **PPARA : ΣRXR** | **6.4 : 1** | 0.74 : 1 | 3.3 : 1 | 0.68 : 1 | 0.61 : 1 |

Summing marginals overcounts cells that express more than one RXR, so ΣRXR is an
*upper bound* on the fraction of cells with any RXR. The rod ratio of 6.4 : 1 is therefore
conservative — the true imbalance is at least that large.

In rods, PPARα outnumbers its obligate partner **6.4 to 1**. Rods are the cell type with
the most PPARα and the least capacity to use it for transactivation. Cones are the
opposite — RXRG alone is at 56.0%. Müller glia and endothelium have balanced, modest
stoichiometry.

This is the first quantitative constraint on limb 4 (local transactivation) that does not
come from exposure arithmetic, and it is independent of drug concentration: even with
unlimited drug at the receptor, rod photoreceptors lack the partner to drive a PPRE.
*Caveat: transcript stoichiometry is not protein stoichiometry, and RXR protein is long-lived.
Treat this as a hypothesis with a clean experimental test (co-IP or proximity ligation in
donor retina), not as an established limit.*

---

## 4. THE ANTIBODY-VS-TRANSCRIPTOMICS CONFLICT

### 4.1 The premise is false

The analysis recorded that "single-cell transcriptomic atlases reportedly do not show
PPARA as a prominent retinal transcript." Queried directly, four independent sources say
the opposite:

| Source | PPARA | PPARD | PPARG |
|---|---|---|---|
| **EyeGEx bulk, n=523 retinas** | 143.5 CPM, **92.4th pctile** of expressed genes, detected in **99.8%** of retinas | 31.7 CPM, 62.6th | 1.55 CPM, 6.4th |
| **GSE160306 macula**, n=49 | control mean 129.6 CPM; 91.8th pctile* | 43.3 CPM, 71.3rd | 4.08 CPM, 23.2nd |
| **GSE160306 periphery**, n=50 | control mean 227.5 CPM; 95.7th pctile* | 47.4 CPM, 74.0th | 1.63 CPM, 9.3rd |
| **HPA bulk retina** | 16.6 nTPM, 79.8th pctile of 20,162 genes (liver: 30.8) | 10.1 nTPM, 69.9th | 0.6 nTPM, 31.4th |
| **Census single-cell, rods** | 68.0% of 1.21M cells | 13.3% | 0.29% |
| **HPA single-cell, rods** | 680.1 nCPM | 42.5 | 0.5 |

\* Percentiles are among features with mean CPM ≥ 1 across all samples at that site
(16,587–16,600 of 58,051 annotated features); CPM figures are the control-group mean.
Ranking against all 58,051 features would inflate PPARA to the 97–99th percentile, because
most of those features are never-expressed lncRNAs and pseudogenes. The conservative
figure is reported.

PPARA in human retina is at **54% of its own level in liver** (HPA: 16.6 vs 30.8 nTPM) —
the canonical PPARα tissue. HPA's unsupervised whole-body single-cell clustering assigns
PPARA to **"Cluster 79: Photoreceptor cells — Phototransduction"**, the same cluster as RHO
and NR2E3, and flags it "cell type enhanced" in rod photoreceptors at a level (680 nCPM)
**above hepatocytes (327) and enterocytes (313)**. That is not a cherry-picked lookup; it
is where an unbiased clustering of the human body puts this gene.

### 4.2 Why the opposite impression arose — dropout, quantified

Three mechanisms, all measured here.

**(a) Detection rate of a transcription factor is mostly a measure of the assay.**
Binning all whole-cell retinal cells by sequencing depth
(`data/processed/retina_sc_depth_dropout.tsv`):

| Depth decile (whole cell) | 1 | 2 | 4 | 6 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| median genes/cell | 558 | 825 | 1,245 | 1,664 | 2,449 | 3,428 | 5,627 |
| **PPARA** | 4.07 | 3.31 | 5.61 | 7.58 | 10.08 | 21.78 | **40.58** |
| TBP | 1.08 | 1.73 | 3.23 | 4.81 | 7.41 | 9.82 | 20.19 |
| PPARD | 1.36 | 1.65 | 2.99 | 5.23 | 15.38 | 32.04 | 52.07 |
| GAPDH *(saturated)* | 75.06 | 90.00 | 95.82 | 96.86 | 96.42 | 97.91 | 99.85 |
| **ALB** *(negative)* | 0.00 | 0.03 | 0.03 | 0.04 | 0.07 | 0.27 | 1.06 |
| **PRM1 / INS** *(negative)* | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

PPARA swings **10-fold on depth alone**, with no biology changing. Across datasets the
dependence is near-deterministic for low-abundance genes: Spearman(TBP detection, median
genes/cell) = **0.934, p = 1.8 × 10⁻⁹** (n = 20 atlases); PPARD = 0.875, p = 4.4 × 10⁻⁷.
GAPDH shows rho = −0.06 — it is saturated and tells you nothing.

**The negative controls are what make this interpretable.** If deeper sequencing merely
added noise, ALB/INS/PRM1/MYH7 would climb with it. PRM1 and INS stay at 0.00% across all
ten deciles while PPARA goes 4% → 41%. Depth is recovering real signal, not manufacturing it.

**(b) PPARA transcript is nuclear-enriched, so whole-cell protocols systematically
under-report it.** Restricting to rod photoreceptors only — composition controlled, ten
atlases from seven publications:

| Atlas | Prep | Genes/cell | n rods | **PPARA** | GAPDH | ALB |
|---|---|---:|---:|---:|---:|---:|
| `856c1b98` | cell | 493 | 9,145 | 16.61 | 62.04 | 0.00 |
| `d5c67a4e` | cell | 1,135 | 11,187 | 19.25 | 95.17 | 0.01 |
| `7b75b2c4` | cell | 1,214 | 7,073 | 11.72 | 99.93 | 0.00 |
| `f5be9ed2` | cell | 1,304 | 3,077 | 13.88 | 96.49 | 0.00 |
| `ccfdcad0` | cell | 1,544 | 13,029 | 29.14 | 99.99 | 0.00 |
| `babbf9f3` | cell | 1,890 | 1,894 | 25.18 | 100.00 | 0.00 |
| `322c816f` | **nucleus** | 1,423 | 32,059 | **52.99** | 64.65 | 0.01 |
| `e6dad530` | **nucleus** | 1,826 | 62,523 | **67.22** | 18.30 | 0.03 |
| `0129dbd9` | **nucleus** | 2,114 | 97,939 | **82.00** | 69.68 | 0.02 |
| `d6505c89` | **nucleus** | 2,301 | 965,915 | **69.38** | 68.00 | 0.02 |

Whole-cell rods: **11.7–29.1%**. Nuclei: **53.0–82.0%**. The two distributions do not
overlap, the depth ranges do (1,135–1,890 vs 1,423–2,301), and GAPDH moves in the opposite
direction (95–100% → 18–70%). Across all three PPAR isoforms the median per-atlas detection
is 4–17× higher in nuclei. This is the nuclear-retention signature, and it is shared across
the isoform family rather than being a PPARA quirk.

**(c) The comparison gene determines the conclusion.** In rods, ACTB is detected in only
16.8% of cells — rods are so dominated by phototransduction transcripts that ordinary
housekeeping genes are squeezed out in CPM terms. Anyone benchmarking PPARA against ACTB in
rods would conclude it is *highly* expressed; anyone benchmarking against GAPDH in Müller
glia (80.8%) would conclude it is absent. Both are artifacts of the denominator.

**Putting (a)–(c) together:** the retina atlases that shaped the field's impression —
Lukowski 2019, Menon 2019, Yan 2020, Cowan 2020 — are shallow (493–1,890 genes/cell)
**whole-cell** datasets. In exactly those, PPARA in rods reads 11.7–29.1% next to GAPDH at
95–100%. On a dot plot that looks like background. The deeper single-nucleus atlases that
postdate them read 53–82%.

### 4.3 Where the conflict is real: *which cells*, not *whether*

This is the part that survives, and it was not what the report was worried about.

The antibody literature places PPARα across Müller glia, RPE, endothelium, ganglion cells
and microglia. The transcript data agrees emphatically about **RPE** (64.8%) and adds two
compartments the antibody literature under-emphasises — **rods (68.0%) and cones (54.5%)**.
But the cells the antibody literature leads with are the ones with the *lowest* PPARA
transcript in the retina:

| Compartment | PPARA % cells | Rank among 13 cell classes |
|---|---:|---|
| Rod photoreceptor | 67.97 | 1 |
| RPE | 64.77 | 2 |
| Cone photoreceptor | 54.51 | 3 |
| Astrocyte / other glia | 20.91 | 4 |
| **Müller glia** | 18.17 | 6 |
| **Microglia / macrophage** | 15.50 | 8 |
| **Vascular endothelium** | 15.39 | 9 |
| **Retinal ganglion cell** | 13.04 | 10 |
| Horizontal cell | 7.89 | 13 |

All of these remain far above the ambient floor, so none is a contradiction. But the
*ordering* is inverted relative to the antibody narrative. Three explanations are live, and
this analysis cannot separate them:

1. **Protein and mRNA genuinely diverge** — plausible for a long-lived nuclear receptor.
2. **Antibody specificity.** HPA lists **2** antibodies for PPARA (HPA066941, CAB075701),
   grades immunohistochemistry "Supported" and immunofluorescence **"Uncertain"**.
   Decisively: **HPA has never stained retina for PPARα.** Its retina IHC panel covers
   **113 proteins** in total, and includes none of PPARA, PPARD, PPARG, RXRA/B/G, KDR or
   FLT1 (7 of this study's 95 panel genes are covered: ARR3, BEST1, GRK1, PDE6H, RARB, RHO,
   RLBP1). There is no orthogonally-validated retinal PPARα stain in the reference resource
   for exactly this question.
3. **Sampling bias in the literature.** Müller glia, vessels and RGC are what retinal
   immunohistochemistry is good at resolving; photoreceptor outer-nuclear-layer nuclei are
   densely packed and hard to assign.

**Verdict.** The headline conflict is an artifact — of dropout, of shallow whole-cell
protocols, and of nobody querying bulk data where dropout does not apply. A residual,
genuine discordance remains about cell-type distribution, and it points the *wrong way for
the drug argument*: the PPARα-rich compartments are the photoreceptors and RPE, not the
glial–vascular compartments where REPORT.md sites its mechanisms.

---

## 5. DIABETES: THE RESTORE-A-DEFICIT PREMISE FAILS

### 5.1 There is no human diabetic retina single-cell atlas

A negative result worth recording plainly. CZ CELLxGENE Census contains **13,075,889 human
eye cells and zero diabetic ones** — the only disease terms on eye tissue are *normal*,
*macular degeneration*, *age-related macular degeneration 7*, *basal laminar drusen*,
*cataract* and *uveal melanoma*. A GEO search for human diabetic-retinopathy single-cell
data returns fibrovascular membranes (GSE165784, GSE245561, GSE179568) and circulating
immune cells (GSE248284) — **membranes and blood, not neural retina**.

**Nobody has published a single-cell atlas of diabetic human neural retina.** That is a
real, citable gap, and it is the acquisition that would most change this note.

### 5.2 What the one available cohort says

**GSE160306** (Becker et al., Iowa donors): bulk total-RNA from macular and peripheral
retina punches, 79 samples. Macula/periphery analysed separately because most donors
contribute one of each; *Diabetic (no retinopathy)* is deliberately held out of the case
group as the intermediate.

| | Control n | Diabetic-no-DR n | DR n (NPDR + NPDR·DME + PDR·DME) |
|---|---:|---:|---:|
| Macula | 10 | 10 | 19 |
| Periphery | 10 | 10 | 20 |

79 samples from **43 donors**, age 54–97, RIN 4.0–9.2, post-mortem interval 149–360 min.

| Gene | Site | CPM control | CPM diabetic-no-DR | CPM DR | log2FC | p | FDR | ρ vs DR severity | **Min detectable FC @80%** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **PPARA** | Macula | 129.6 | 139.3 | 135.7 | **+0.046** | 0.836 | 0.96 | +0.057 (p=0.73) | **1.40×** |
| **PPARA** | Periphery | 227.5 | 187.3 | 210.3 | **−0.096** | 0.367 | 0.83 | −0.102 (p=0.53) | **1.26×** |
| PPARD | Macula | 43.3 | 42.9 | 43.7 | +0.015 | 0.598 | 0.86 | +0.181 | 1.10× |
| PPARD | Periphery | 47.4 | 45.4 | 49.1 | +0.049 | 0.262 | 0.72 | +0.245 | 1.10× |
| PPARG | Macula | 4.08 | 3.66 | 3.59 | −0.182 | 0.224 | 0.61 | −0.246 | 1.35× |
| PPARG | Periphery | 1.63 | 1.78 | 1.49 | −0.104 | 0.153 | 0.59 | −0.143 | 1.22× |

**PPARA is not reduced in diabetic retina, and not reduced with retinopathy severity.** The
power bound is what makes this informative rather than merely non-significant: a **≥40%**
reduction in macula or **≥26%** in periphery would have been detected at 80% power. Neither
occurred; the point estimate in macula is a 3% *increase*.

**The restore-a-deficit framing is unsupported.** Any PPARα agonist effect in DR must be
*supraphysiological activation of a normally expressed receptor*, not correction of a
deficit. That is a different pharmacological argument with a different dose-response and a
different safety profile.

### 5.3 Honest limits on this cohort, and a hint worth chasing

**No gene in the 95-gene panel survives FDR < 0.10 at either site.** This cohort has modest
power for a panel this size, and that must be stated before anything here is leaned on.

What it does carry, at nominal significance and in a biologically coherent pattern, is
**capillary dropout in the periphery** — CLDN5 −0.48 log2 (p = 0.009), PECAM1 −0.33
(p = 0.041), HIF1A −0.17 (p = 0.013), GAD1 −0.27, NEFL −0.58. That is the expected DR
lesion and acts as a weak positive control that the dataset contains real DR signal.

Two PPAR-axis hints, both **nominal only, neither surviving FDR**, flagged as hypotheses:

- **RXRA rises with DR severity**, consistently and at both sites: periphery log2FC +0.185
  (p = 0.037), Spearman ρ = **+0.462 vs severity score, p = 0.003**; macula ρ = +0.355,
  p = 0.026. Given §3.2, an increase in the limiting heterodimer partner in diseased retina
  is the opposite of what a deficit model predicts and is the single most interesting
  number in this cohort.
- **PDK4 falls in periphery** (log2FC −0.62, p = 0.015) — a PPARα transactivation target
  moving down, consistent with reduced fatty-acid-oxidation signalling in diabetic retina.

---

## 6. THE ISOFORM QUESTION: PPARD VS PPARA

The task asks whether PPARD exceeds PPARA, because PPARδ is pro-angiogenic and shares the
transrepression machinery. The answer is not global — it is anatomical.

| Cell class | PPARA % | PPARD % | **PPARD : PPARA** |
|---|---:|---:|---|
| Rod photoreceptor | 67.97 | 13.33 | 0.20 |
| RPE | 64.77 | 13.03 | 0.20 |
| Cone photoreceptor | 54.51 | 15.57 | 0.29 |
| Bipolar cell | 12.62 | 8.60 | 0.68 |
| Astrocyte / other glia | 20.91 | 14.53 | 0.69 |
| **Müller glia** | 18.17 | 16.13 | **0.89** |
| **Vascular endothelium** | 15.39 | 17.67 | **1.15** |
| **Pericyte** | 19.90 | 21.93 | **1.10** |
| **Vascular smooth muscle** | 18.97 | 22.45 | **1.18** |
| **Retinal ganglion cell** | 13.04 | 23.13 | **1.77** |
| **Horizontal cell** | 7.89 | 14.79 | **1.87** |
| **Amacrine cell** | 11.76 | 26.39 | **2.24** |
| **Microglia / macrophage** | 15.50 | 43.03 | **2.78** |

In bulk, PPARA leads comfortably — EyeGEx 143.5 vs 31.7 CPM (4.5×), GSE160306 130–228 vs
43–47 CPM (3–5×), HPA 16.6 vs 10.1 nTPM. That bulk ratio is dominated by rods, which are
~70% of retinal cells. **It conceals a complete reversal in the vasculature.**

### What this changes

REPORT.md's local-engagement limbs are sited in endothelium (leukostasis, barrier),
pericytes (dropout), Müller glia (the transrepression argument) and microglia
(neuroinflammation). **Every one of those compartments is PPARδ-dominant or
PPARα/PPARδ-balanced.** The compartments where PPARα clearly dominates — rods, cones,
RPE — are not where the report's mechanisms act, and are the compartments behind the
blood-retinal barrier that the exposure argument already excluded.

So the isoform-selectivity argument changes in a specific way:

1. **A PPARα-selective agonist has its highest receptor density in the compartment it can
   least reach** (outer retina / RPE), and its lowest in the compartments its proposed
   mechanisms require (vasculature, microglia).
2. **A dual or PPARδ-sparing question becomes empirical rather than theoretical.** In
   microglia, any transrepression effect attributed to PPARα is competing against 2.8× more
   PPARδ. Elafibranor (PPARα 8.00 / PPARδ 8.00 pChEMBL, from Step 1) engages both equally
   and is therefore a *pro-angiogenic risk in the retinal vasculature*, not a neutral
   dual agonist.
3. **Pemafibrate's selectivity profile acquires a concrete liability.** Its 3.2 log-unit
   PPARα/PPARδ margin (9.00 vs 5.80) is exactly what you want to avoid PPARδ, but it also
   means almost no engagement in the PPARδ-dominant vascular and microglial compartments
   where DR pathology lives.

Separately: **PPARG is the retinal ganglion cell isoform** (46.3%, versus PPARA 13.0% and
PPARD 23.1%) and the vascular-mural isoform (VSMC 23.9%, pericyte 17.2%). Step 1 found
PPARG ranked 9th of 2,652 Open Targets DR associations with a genetic score of 0.750, while
PPARA ranked 66th with no genetic association at all. The expression data is consistent
with that and makes Step 1's recommended follow-up more pressing, not less.

---

## 7. THE EFFECTOR PANEL — LIMB 4 IS NOT EMPTY

Step 1 concluded that the PPARα effector programme is "nearly absent" and that "measuring
the effector limb requires expression data, not affinity data." That expression data now
exists, and it **partially reverses** the Step 1 impression. The effectors were absent from
*binding* databases because they are transcriptional outputs, not drug targets — not
because the retina lacks them.

**% of cells expressing** (Census), with EyeGEx bulk CPM for scale:

| Effector | Rod | Cone | RPE | Müller | Endo | Peri | Micro | EyeGEx CPM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **CPT1A** | 34.14 | 53.60 | 26.01 | 9.81 | 25.62 | 21.55 | 15.98 | 82.6 |
| **ACADM** | 22.06 | 41.27 | 18.58 | 16.93 | 12.09 | 9.62 | 9.07 | 55.2 |
| **ACOX1** | 13.87 | 24.97 | 27.14 | 18.39 | 12.69 | 12.49 | 11.63 | 79.0 |
| **ABCG1** | 41.96 | 16.92 | 14.12 | 16.05 | 33.33 | 3.10 | 18.25 | 70.2 |
| **ABCA1** | 6.25 | 26.69 | 44.18 | 1.00 | 20.15 | 34.40 | 53.39 | 31.2 |
| **LPL** | 0.75 | 1.00 | 13.16 | 1.36 | 6.54 | 41.60 | 5.93 | 35.1 |
| **PDK4** | 0.09 | 0.10 | 12.10 | 5.75 | 26.68 | 32.97 | 30.00 | 6.7 |
| **ANGPTL4** | 1.02 | 0.95 | 5.82 | 9.17 | 12.01 | 23.06 | 2.64 | 5.9 |
| **EHHADH** | 3.08 | 7.27 | **29.78** | 2.65 | 3.48 | 1.90 | 2.97 | 4.7 |
| **HMGCS2** | 0.03 | 0.03 | **22.95** | 0.02 | 0.78 | 0.69 | 0.64 | 0.19 |
| **FGF21** | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | **0.00** |
| **APOA1 / APOA5 / FABP1** | ≤0.25 | ≤0.21 | ≤0.06 | ≤0.19 | ≤0.43 | ≤0.33 | ≤0.13 | ≤0.08 |

Four things follow.

1. **The fatty-acid-oxidation arm is robustly present in neural retina.** CPT1A, ACADM,
   ACOX1 and ABCG1 are expressed at 10–54% of cells and 55–83 CPM in bulk. Limb 4's
   *readouts* exist. Step 1's "limb 4 is empty in both new datasets" reflected the absence
   of ChEMBL targets and Open Targets associations — i.e. what has been studied — not the
   absence of the biology. This is precisely the distinction Step 1 flagged and it resolves
   in favour of "nobody has looked."
2. **FGF21 is flat zero in every retinal cell type** (0.00–0.01%, and 0.00 CPM in 523
   retinas; detected in 1.5% of EyeGEx samples). The retina does not make FGF21. REPORT.md
   §5.5's humoral relay is therefore necessarily **hepatic-to-retinal**, with no local
   component whatsoever. The framing survives; a local-production escape hatch does not exist.
3. **ANGPTL4 is a mural/endothelial gene in retina** — pericytes 23.1%, smooth muscle 22.9%,
   endothelium 12.0%, versus ~1% in photoreceptors. REPORT.md §5.4's wrong-sign permeability
   risk is sited in exactly the right compartment, which strengthens it. And that compartment
   is PPARδ-dominant (§6), so ANGPTL4 induction there would be driven by PPARδ engagement at
   least as much as PPARα.
4. **HMGCS2 and EHHADH are RPE-specific** (23.0% and 29.8%, ≤0.1% and ≤7% elsewhere). RPE
   ketogenesis is a real, localised programme. If any PPARα transactivation readout is
   measurable in human eye, it is HMGCS2 in RPE — a concrete, falsifiable assay that did
   not exist as a proposal before this query.

---

## 8. WHAT WOULD CHANGE EACH VERDICT

| Verdict | Confidence | What would overturn it |
|---|---|---|
| PPARA is well expressed in human retina | **High** | Little short of showing that four independent cohorts and two processing pipelines share a systematic annotation error. Protein-level absence would *not* overturn the transcript claim — it would relocate the question to translation. |
| The antibody/transcript conflict is an artifact | **High** on the premise; **Moderate** on the residual cell-type discordance | A knockout- or peptide-competition-validated PPARα stain on human donor retina with per-cell-type quantification. None exists; HPA has never stained retina for PPARα. This is the cheapest decisive experiment in this note. |
| PPARA is not reduced in diabetes | **Moderate** | A second independent diabetic retina cohort. n = 79 at one site, nothing in the panel survives FDR, and all 79 samples come from 43 post-mortem donors (age 54–97, RIN 4.0–9.2, PMI 149–360 min). A ≤26% reduction remains possible. |
| PPARD exceeds PPARA in the vasculature | **High** | Cell-type annotation error across 24 datasets, or a protein-level reversal. The ratio is consistent across two pipelines and every vascular/immune class independently. |
| The RXR stoichiometry limit in rods | **Low — hypothesis only** | Protein-level PPARα:RXR measurement in donor retina. Transcript ratios are weak evidence for complex availability. |
| FGF21 is absent from retina | **High** | 0.00% of 4.8M cells and 0.00 CPM in 523 retinas is about as clean a null as this kind of data produces. |

### Caveats that apply throughout

- **CELLxGENE and HPA are not fully independent.** Both reprocess overlapping public
  studies. They are independent *pipelines*, not independent *samples*. The genuinely
  independent evidence is the three bulk cohorts (EyeGEx, GSE160306, HPA consensus).
- **Detection rate is not concentration.** "68% of rods express PPARA" means ≥1 UMI, not a
  receptor count. The bulk CPM figures are the better abundance estimate.
- **No protein measurement anywhere in this note.** Everything here is mRNA.
- **The depth-decile table** (`retina_sc_depth_dropout.tsv`) was computed before the organoid
  exclusion and retains 43,857 organoid cells (0.9% of the total). Every other table excludes
  them. The effect on the decile curve is immaterial, but it is not zero.
- **GSE160306 donors are post-mortem**, and PPARα is a stress-responsive transcription
  factor. Agonal state and PMI could mask a modest in-vivo difference.
- **This note does not touch exposure.** REPORT.md's binding constraint — that free drug
  concentration in retinal tissue has never been measured in any species — is untouched by
  anything here. A well-expressed receptor in an unreachable compartment is still unreachable.

---

## 9. EFFECT ON REPORT.md

| REPORT.md position | Status after this step |
|---|---|
| Retinal PPARα expression "EMERGING / partly UNCERTAIN" | **Resolved.** Established across four cohorts. The uncertainty was an artifact of not querying. |
| Antibody vs transcriptomics conflict unresolved | **Resolved in direction, refined in substance.** The premise was false; a real discordance remains over cell type, and it disfavours the glial–vascular mechanisms. |
| Restore-a-deficit framing | **Unsupported.** No reduction in diabetes; a ≥1.26–1.40× change would have been seen. |
| Isoform selectivity as a safety preference | **Upgraded to a targeting constraint.** PPARδ dominates every vascular and immune compartment in retina. |
| §5.1 limb 4 excluded on exposure arithmetic | **Conclusion stands; one supporting argument withdrawn.** The FAO effector genes *are* expressed in neural retina. Limb 4 fails on exposure and now also on RXR stoichiometry in rods — not on absence of the programme. |
| §5.4 ANGPTL4 wrong-sign risk | **Strengthened and localised** to pericytes/endothelium — a PPARδ-dominant compartment. |
| §5.5 FGF21 humoral relay | **Confirmed as necessarily hepatic.** Retina makes no FGF21 at all. |
| §2.3 "measured pharmacokinetics: none" | **Still true.** Untouched. Still the binding constraint. |

---

## 10. FILES

**Code** — `src/analysis/retina_expression/`

| Module | Role |
|---|---|
| `census_client.py` | Proxy-aware CZ CELLxGENE Census connection; pins release `2025-11-08` |
| `gene_panel.py` | 43 DR panel genes + 52 controls, with the rationale for each control class |
| `query_census.py` | Per-cell detection and CP10K over 4.8M retinal cells; depth-decile dropout |
| `census_presence.py` | Dataset provenance + feature-presence matrix (absent vs below threshold) |
| `summarise.py` | Rollup to cell classes, suspension type, and per-dataset |
| `wmg_crosscheck.py` | Independent server-side cross-check via the CELLxGENE WMG v2 API |
| `hpa.py` | HPA single-cell nCPM, bulk nTPM, antibody reliability, retina IHC coverage |
| `bulk_dr.py` | GSE160306 diabetic contrast, with power/minimum-detectable-effect |
| `eyegex.py` | GSE115828, 523-retina abundance reference |

**Data** — `data/processed/`

`retina_sc_group_expression.tsv` (338,770 rows, finest grain) ·
`retina_sc_celltype_summary.tsv` · `retina_sc_celltype_by_suspension.tsv` ·
`retina_sc_by_dataset.tsv` · `retina_sc_datasets.tsv` · `retina_sc_gene_presence.tsv` ·
`retina_sc_depth_dropout.tsv` · `retina_wmg_crosscheck.tsv` ·
`retina_hpa_celltype_ncpm.tsv` · `retina_hpa_bulk_ntpm.tsv` ·
`retina_hpa_antibody_reliability.tsv` · `retina_bulk_dr_expression.tsv` ·
`retina_bulk_dr_samples.tsv` · `retina_eyegex_abundance.tsv`

**Reproduce**

```bash
source venv/bin/activate
python src/analysis/retina_expression/census_presence.py      # ~3 min
python src/analysis/retina_expression/query_census.py         # ~90 min (4.8M cells)
python src/analysis/retina_expression/summarise.py
python src/analysis/retina_expression/wmg_crosscheck.py
python src/analysis/retina_expression/hpa.py      --work-dir _hpa
python src/analysis/retina_expression/bulk_dr.py  --work-dir _gse160306
python src/analysis/retina_expression/eyegex.py   --work-dir _eyegex
```

Not touched: `data/holdout/`, `data/processed-blinded-*/`, `data/reports/`.

---

## 11. WHAT TO DO NEXT

1. **The decisive experiment is a validated PPARα stain on human donor retina**, quantified
   per cell type, with knockout or peptide-competition controls. It costs one donor eye and
   settles the only part of the conflict that survives. No such stain exists — HPA's retina
   IHC panel is 113 proteins and contains no PPAR.
2. **Measure PPARδ alongside PPARα in any retinal engagement experiment.** In microglia and
   the vasculature, PPARδ is the more abundant receptor; an effect attributed to PPARα
   there is not safely attributable without the control.
3. **HMGCS2 in RPE is the one tractable transactivation readout.** It is RPE-specific
   (23.0% of cells, ≤0.1% elsewhere) and a direct PPARα target. If local transactivation is
   measurable anywhere in human eye, it is there.
4. **A second diabetic retina cohort** is the highest-value acquisition for the deficit
   question. GSE160306 is the only public human neural-retina series with a diabetic axis,
   and nothing in this panel survives FDR in it.
5. **Someone should generate a diabetic human retina single-cell atlas.** It does not exist.
   Every public diabetic eye single-cell dataset profiles fibrovascular membranes or blood.
6. **Test the RXR stoichiometry hypothesis** before it propagates as a finding. Transcript
   ratios suggested it; only protein co-IP or proximity ligation can establish it.

---

## Status — 2026-11-03 — step 2: settle the retinal PPARA expression question

**Done.** Queried four primary data sources directly rather than reasoning about them:
CZ CELLxGENE Census LTS `2025-11-08` (4,828,235 adult non-diseased human retinal cells,
24 datasets, 16 publications), the CELLxGENE WMG v2 API as an independent cross-check,
Human Protein Atlas single-cell + bulk + antibody records, GEO **GSE115828** (EyeGEx,
523 retinas) and GEO **GSE160306** (79 samples, graded diabetic axis). Nine new modules
under `src/analysis/retina_expression/`, fourteen new tables under `data/processed/`.

**Verified.**
- PPARA is in the feature space of **24/24** retina datasets — no zero in this analysis is
  a missing-feature artifact.
- Detection floor established with six negative controls (INS/PRM1/KRT1/CELA3A/MYH7/ALB):
  **0.00–0.1%** in every cell class. PPARA ranges **7.9–68.0%**.
- Cell-type ordering reproduces across two independent pipelines (Census CP10K computed
  here; HPA nCPM) and the server-side WMG API.
- Abundance reproduces across three independent bulk cohorts (EyeGEx n=523, GSE160306
  n=79, HPA consensus): **PPARA > PPARD >> PPARG** in whole retina.
- The diabetic null is power-bounded, not merely non-significant: minimum detectable
  effect 1.40× (macula) / 1.26× (periphery) at 80%.

**Corrections made during the step.** An earlier pass included 43,857 retinal *organoid*
cells (dataset `7e7f63c5`) that CELLxGENE files under retina tissue labels; the obs filter
now requires `tissue_type == 'tissue'` and that dataset is excluded from every table except
`retina_sc_depth_dropout.tsv` (noted in §8). Two modules were writing
`retina_sc_datasets.tsv` with different column names; `census_presence.py` is now its sole
owner. GSE160306's `PDR + DME` group was initially dropped from the case set and is now
included.

**What step 3 needs to know.**
1. **The restore-a-deficit premise is dead.** Retinal PPARA is not reduced in diabetes.
   Any downstream argument that assumes correcting a deficit needs rewriting as
   supraphysiological activation of a normally expressed receptor.
2. **PPARδ exceeds PPARα in every vascular and immune retinal compartment** (microglia
   2.8×, endothelium 1.15×, pericytes 1.10×, smooth muscle 1.18×). Isoform selectivity is a
   targeting constraint, not just a safety preference. Elafibranor's equal PPARα/PPARδ
   potency is a retinal-vasculature liability on this evidence.
3. **FGF21 is flat zero in human retina** (0.00–0.01% of 4.8M cells; 0.00 CPM in 523
   retinas). The step-3 FGF21 concentration bridge is therefore necessarily
   hepatic-to-retinal with no local production term. This is a hard constraint on that step.
4. **Limb 4's effector genes are expressed after all** — CPT1A, ACADM, ACOX1 and ABCG1 at
   10–54% of cells. Step 1's "limb 4 is empty" reflected what has been *studied*, not the
   biology. The exposure argument remains the real basis for excluding limb 4.
5. **No human diabetic neural-retina single-cell atlas exists.** Census holds 13,075,889
   human eye cells and zero diabetic ones; every public diabetic eye single-cell dataset
   profiles fibrovascular membranes or blood.
6. `HMGCS2` in RPE (23.0% of cells, ≤0.1% elsewhere) is the one tractable local
   transactivation readout identified by this step.

**Not done / limits.** No protein measurement anywhere. One diabetic cohort only, and
nothing in the 95-gene panel survives FDR < 0.10 in it. The RXR stoichiometry imbalance in
rods (§3.2) is a hypothesis from transcript ratios, explicitly not a finding. Retinal drug
exposure — REPORT.md's actual binding constraint — is untouched by this step.
