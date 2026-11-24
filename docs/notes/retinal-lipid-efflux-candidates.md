# An agent for the uncovered efflux arm

**Step 6 of `docs/prompts/dr-solve-open-questions-prompt.md`. Run 2026-11-09.**

Code: `src/analysis/efflux_axis/` — reproduce with
`python -m src.analysis.efflux_axis.run`.
Data: `data/processed/efflux_axis_*.csv`.

Every quantitative claim below is tagged **MEASURED** (read from a published
result, a label, or a database record), **MODELLED** (computed by a declared
model from declared inputs) or **REASONED** (argument, no computation behind
it). Conflating the three is the failure this chain exists to correct.

---

## Summary

The premise holds and is now quantified. The reverse-cholesterol-transport arm
is uncovered, the opening the brief identifies is real, and it is worth a
specific number: **1.16 log units of isoform selectivity**.

1. **The knowledge graph and the GNN cannot answer this question, and the GNN
   is worse than uninformative — it is anti-predictive in the direction the
   question is asked.** Ranking compounds for a gene, the model places the
   axis edges it was *trained on* at mean percentile rank **0.123** where
   random is 0.500. Compound degree alone scores 0.970. This is not a broken
   model; it is a model being asked the transpose of the question its
   benchmark evaluates. Section 2. **MEASURED**

2. **All measured pharmacology on this axis is at one node.** Of 3,732
   qualifying activities across the nine genes, **3,729 are at LXR-α/LXR-β and
   zero are at ABCA1, ABCG1, APOA1 or APOE.** The effectors are readouts, not
   pockets. The only approved drug with a recorded ABCA1 mechanism is
   probucol — an ABCA1 *inhibitor*. Section 3. **MEASURED**

3. **The structural opening is real: 802 of 1,009 potent LXR ligands are
   neutral.** Ionisation is not locked in for this target, and going neutral
   buys a **paired median 10–12× gain in neural-retina K<sub>p,uu</sub>
   (95% CI 1.9–64×, P(gain) ≈ 0.99)** under Step 5's own calibrated model.
   Section 4. **MODELLED**

4. **That gain converts directly into a relaxed safety requirement.** A 10×
   hepatic margin needs **β-selectivity ≥ 2.73 log for an acid but only
   ≥ ~1.55 log for a neutral ligand.** Against 797 potent dual-measured LXR
   ligands: **0 clear the acid bar, 8 clear the neutral bar, 5 of those also
   reach the retina.** Section 5. **MODELLED from MEASURED selectivity**

5. **But the five are one chemical series from one 2018 patent, on cell-free
   data.** In the cell-based functional tier — the only one that measures
   transactivation — the maximum β-selectivity across 106 paired molecules is
   **1.37 log, below the requirement. Not one clears it.** Section 6.
   **MEASURED**

6. **The acceptor-versus-inducer ordering is backwards, in the regime that
   defines the disease.** At zero transporter activity a 1000× inducer gives
   infinite burden and an acceptor at 10% of healthy clearance gives 10. The
   inversion has a boundary: the acceptor wins below
   `E* = k_a·A / (k_t·(F−1))`. Section 7. **MODELLED**

**Verdict.** A neutral, β-selective LXR agonist is a *defensible* programme in
a way a fibrate is not — the arithmetic that rules out the acid route is
explicit and the neutral route survives it. But no molecule in the public
record yet carries the required selectivity in a cell, and if retinal ABCA1 is
as suppressed as the lesion requires, **the inducer is the wrong arm and the
direct acceptor is the right one.** The honest ordering is: acceptor first,
inducer as the combination partner, supply-lowering last.

---

## 1. The axis, and why it is not nine targets

`src/analysis/efflux_axis/axis.py`. The nine genes take three different kinds
of evidence, and the division is not editorial — Section 3 confirms it from
the data.

| Gene | Class | Arm | Ligandable | Role |
|---|---|---|---|---|
| NR1H3 (LXR-α) | RECEPTOR | efflux | yes | Transcriptional switch for ABCA1/ABCG1/APOE; **also the hepatic lipogenic isoform** |
| NR1H2 (LXR-β) | RECEPTOR | efflux | yes | Same efflux programme, far less hepatic lipogenesis; ubiquitous incl. retina |
| ABCA1 | EFFECTOR | efflux | no | Rate-limiting efflux to lipid-poor apoA-I — the clearance term |
| ABCG1 | EFFECTOR | efflux | no | Efflux to mature HDL, downstream of ABCA1 |
| APOA1 | EFFECTOR | efflux | no | The acceptor itself — a protein, not a pocket |
| APOE | EFFECTOR | efflux | no | Locally synthesised by RPE and Müller glia |
| CD36 | SCAVENGER | uptake | yes | oxLDL uptake in RPE and microglia — the influx term |
| OLR1 (LOX-1) | SCAVENGER | uptake | no | Endothelial oxLDL entry at the inner BRB |
| MSR1 (SR-A) | SCAVENGER | uptake | no | Microglial uptake; the foam-cell arm |

The distinction that matters: **ABCA1 and ABCG1 have no agonist pharmacology.**
No small molecule binds ABCA1 and makes it pump faster. What the literature
calls an "ABCA1 inducer" acts upstream, almost always at LXR. So a prediction
that "compound X targets ABCA1" is a claim about transcription, and a model
that cannot tell the two apart will mislead. Section 2 shows that ours cannot.

## 2. The GNN, and why its answer cannot be used

`src/analysis/efflux_axis/gnn_rank.py`; outputs
`efflux_axis_gnn_predictions.csv`, `efflux_axis_gnn_benchmark.csv`,
`efflux_axis_edge_semantics.csv`.

The model is
`local-llm/data/models/link_prediction/2026-09-14_Compound_TARGETS_Gene` — a
2-layer hetero-GraphSAGE with an MLP decoder, trained on 35,691 positive
Compound→Gene edges. It had never been pointed at this question. It was
pointed at it, and the result is a methodological finding rather than a
candidate list.

### 2a. What the edges actually assert — **MEASURED**

The `Compound-TARGETS-Gene` relation is rebuilt from
`pubchem_phytochem_target_interactions.csv`. Across the 238 axis edges:

| | share of axis edges |
|---|---|
| From the Comparative Toxicogenomics Database | **100%** |
| Expression-change statements | **88%** |
| Binding-like statements | **5%** |
| *Nested* — compound modifies a reaction between two other entities | **36%** |
| Name a co-treatment | **29%** |

A representative edge reads *"[fructose co-treated with dietary fats
co-treated with cholesterol, dietary] results in increased expression of ABCA1
mRNA"*. The compound slot holds a dietary confound and the relationship to the
gene is third-order. **There is no binding-grade evidence on this axis in the
knowledge graph at all** — which is why Section 3 had to go and fetch some.

### 2b. The retrieval benchmark — **MEASURED**

Can the model rank a gene's known binders above the other 920 compounds? That
is the question Step 6 asks. Mean percentile rank of the known positives;
0.500 is random, 1.000 perfect. These positives were **in the training set**,
so every column is an upper bound.

| Gene | n | raw score | degree-residualised | embedding kNN | **compound degree alone** |
|---|---|---|---|---|---|
| NR1H3 | 13 | 0.053 | 0.260 | 0.736 | 0.977 |
| NR1H2 | 5 | 0.177 | 0.813 | 0.016 | 0.963 |
| ABCA1 | 15 | 0.048 | 0.225 | 0.775 | 0.978 |
| ABCG1 | 7 | 0.160 | 0.828 | 0.041 | 0.961 |
| APOA1 | 16 | 0.091 | 0.430 | 0.767 | 0.965 |
| APOE | 14 | 0.083 | 0.338 | 0.830 | 0.982 |
| CD36 | 14 | 0.105 | 0.546 | 0.682 | 0.973 |
| OLR1 | 10 | 0.146 | 0.631 | 0.317 | 0.963 |
| MSR1 | 6 | 0.242 | 0.966 | 0.033 | 0.972 |
| **MEAN** | **100** | **0.123** | **0.560** | **0.466** | **0.970** |

The raw decoder score is **anti-predictive**. Residualising the degree trend
recovers chance. Embedding kNN is chance and unstable. A scorer that knows
nothing about the gene and only asks *how well studied is this compound*
scores 0.970.

### 2c. Why — and why the model card did not catch it — **MEASURED**

The scoring path is correct: the decoder agrees with `score_all` to 1e-5, and
the global protocol reproduces the model card (MRR 0.216 here vs 0.232
published). The model is not broken. It is being asked the transpose of its
benchmark.

```
corr(gene degree,     mean column score) = +0.957
corr(compound degree, mean row score)    = -0.509
```

The model card evaluates *rank genes for a compound*: one positive against 100
randomly drawn genes. Gene degree is genuinely informative there, and on the
axis that protocol returns MRR 0.375 and hits@10 **0.99** — the axis genes sit
in the 91st–98th percentile of degree, so "is this pair real?" is answered by
"is the gene popular?" and they win trivially.

Ranking *down a column* holds the gene fixed. The only variance left is the
compound-side term, and that term is inverted: the highest scores go to the
most isolated compounds. The top raw predictions are hexanoic acid,
5-hydroxymethylfurfural, β-maltose and *cis*-3-hexen-1-ol — flavour chemicals
with degree 1–3. **A model can pass its own benchmark at hits@10 = 0.99 and be
anti-predictive on the question you need answered.**

`efflux_axis_gnn_predictions.csv` carries the ranking with `z_gene`,
`z_compound` and the endpoint degrees so the artefact is visible in the file
itself. **It should not be used to nominate compounds**, and nothing
downstream in this note does.

> **For Step 8.** Any claim in `REPORT.md` resting on GNN-ranked
> compound-target predictions inherits this. The fix is cheap: evaluate
> link-prediction models in *both* directions, and report the degree-only
> baseline next to the model, as the model card already does for the global
> task.

## 3. What is actually measurable on this axis — **MEASURED**

`src/analysis/efflux_axis/chembl_axis.py`; outputs
`efflux_axis_targets.csv`, `efflux_axis_bioactivities.csv`. Human SINGLE
PROTEIN targets, IC50/EC50/Ki/Kd in nM with a `pchembl_value`.

| Gene | Class | ChEMBL target | Activities | Mechanisms |
|---|---|---|---|---|
| NR1H3 | RECEPTOR | CHEMBL2808 | **1,715** | 4 |
| NR1H2 | RECEPTOR | CHEMBL4093 | **2,014** | 5 |
| ABCA1 | EFFECTOR | CHEMBL2362986 | 0 | 1 |
| ABCG1 | EFFECTOR | *no target exists* | 0 | 0 |
| APOA1 | EFFECTOR | CHEMBL5984 | 0 | 0 |
| APOE | EFFECTOR | *no target exists* | 0 | 0 |
| CD36 | SCAVENGER | CHEMBL1744526 | 1 | 0 |
| OLR1 | SCAVENGER | CHEMBL3421522 | 0 | 0 |
| MSR1 | SCAVENGER | CHEMBL5811 | 2 | 0 |

**RECEPTOR 3,729 · EFFECTOR 0 · SCAVENGER 3.**

Two consequences. First, the ligandable/non-ligandable split in Section 1 is
confirmed by data rather than asserted. Second, **the only way to act on the
efflux arm pharmacologically is through LXR** — or by not using a small
molecule at all, which is Section 7.

The single ABCA1 mechanism record is **probucol (CHEMBL608), an ABCA1
inhibitor, max_phase 4**. The one marketed drug that engages the clearance
transporter directly drives it the wrong way.

## 4. The structural opening, quantified

### 4a. Ionisation is not locked in — **MEASURED**

ChEMBL's ChemAxon fields (`cx_logd`, `cx_most_apka`, `molecular_species`)
return **null for all 1,009** potent ligands — the same gap Step 5 documented
for the fibrates — so `physchem.ionisation_class` derives the class by SMARTS
on the canonical SMILES.

| Class | n | median logP | median logD<sub>7.4</sub> | median MW |
|---|---|---|---|---|
| **NEUTRAL** | **802** | 4.70 | **4.70** | 475 |
| BASE | 119 | 4.71 | 3.58 | 504 |
| ACID | 71 | 7.17 | 3.97 | 510 |
| ZWITTERION | 17 | 8.48 | 5.28 | 596 |
| *fenofibric acid (reference)* | — | *3.81* | ***−0.49*** | *319* |

**79% of potent LXR ligands are neutral.** For a neutral ligand logD = logP;
for fenofibric acid, pK<sub>a</sub> 3.1 costs 4.3 log units. The premise holds.

### 4b. What neutrality buys at the barrier — **MODELLED**

`physchem.kpuu_neural_retina` calls Step 5's own `barrier.kpuu_transfer` and
`ionisation.log_d` with Step 5's declared parameter distributions, transferring
the K<sub>p,uu</sub> Step 5 calibrated against Huang 2021. **Validation:** the
fenofibric-acid reference reproduces at 0.0594 against Step 5's published
0.0586 (`ocular_exposure_margins.tsv`) — 1.5%, Monte-Carlo noise.

The statistic is the **paired** ratio — same anchor and barrier draws top and
bottom — because the Huang calibration uncertainty is common to both compounds
and cancels. Unpaired, the intervals overlap and the gain looks
non-significant; that comparison would be wrong.

| Molecule | Class | logD<sub>7.4</sub> | K<sub>p,uu</sub> median | fold vs FFA (median) | 95% CI | P(>1) |
|---|---|---|---|---|---|---|
| Fenofibric acid | ACID | −0.49 | 0.059 | 1.00 | — | — |
| CHEMBL5899878 | NEUTRAL | 3.17 | 0.85 | **10.5×** | 1.9–64 | 0.998 |
| CHEMBL5938562 | NEUTRAL | 3.73 | 0.85 | 10.1× | 1.3–66 | 0.986 |
| CHEMBL5747669 | NEUTRAL | 4.03 | 0.92 | 11.5× | 1.8–73 | 0.996 |
| CHEMBL2326845 | NEUTRAL | 4.21 | 0.94 | 12.1× | 2.1–76 | 0.998 |
| CHEMBL6040137 | BASE | 2.70 | 0.93 | 12.2× | 2.3–74 | 0.999 |

**Caveat (REASONED).** The transfer crosses a 3.7-log logD gap. Step 5's
`perm_logd_slope` prior (0.30–1.00) is justified as "typical within a
congeneric series", and these compounds are not congeneric with fenofibric
acid. The 95% CI spans 1.9–64× partly because of that, and the point estimate
should be read as "roughly an order of magnitude", not "10.5×".

### 4c. What the filter removed — **MODELLED**

`physchem.apply_filter`, CNS-penetrant window: MW ≤ 500, TPSA ≤ 90, HBD ≤ 3,
1 ≤ logD<sub>7.4</sub> ≤ 5, not ionised. **297 of 1,009 pass.**

The dominant rejection is **excess** lipophilicity — 416 carry a "logD > 5"
flag, median logP 6.21. **The LXR chemotype has swapped the fibrate's
ionisation problem for a lipophilicity-and-size problem.** Every named
clinical agent fails:

| Compound | Phase | Class | logP | logD | MW | Verdict |
|---|---|---|---|---|---|---|
| BMS-852927 | 1 | NEUTRAL | 6.57 | 6.57 | 610 | logD, MW, TPSA |
| Abequolixron (RGX-104) | 1 | ZWITTERION | 8.48 | 5.28 | 596 | logD, MW, **ionised** |
| BMS-779788 | 1 | NEUTRAL | 6.15 | 6.15 | 509 | logD, MW |
| LXR-623 | 1 | NEUTRAL | 6.70 | 6.70 | 423 | logD |
| Bexarotene | **4** | **ACID** | 6.10 | 2.90 | 348 | **ionised — the fibrate failure mode, in an approved drug** |
| T0901317 | tool | NEUTRAL | 4.76 | 4.76 | 481 | **passes** |

Tryprostatin A also passes but is an artefact: a **single SPR K<sub>d</sub>**
at LXR-α with no functional data, correctly tiered "direction unknown".

## 5. Steatosis: the requirement, not the warning — **MODELLED**

`src/analysis/efflux_axis/steatosis.py`; `efflux_axis_selectivity_grid.csv`.

LXR agonism raises ABCA1/ABCG1 and also SREBF1, FASN and SCD1 in hepatocytes.
T0901317 produces frank steatosis and hypertriglyceridaemia in rodents;
BMS-852927 raised plasma and hepatic triglyceride in humans; LXR-623 was
stopped in phase 1 for CNS effects. The isoforms divide the labour: **LXR-α is
hepatocyte-dominant and carries the lipogenic output; LXR-β carries the efflux
programme.** So the requirement is a number.

Writing `Cu` for free plasma concentration, the retina sees `Kp,uu·Cu` and the
hepatocyte `H·Cu`. Engaging retinal LXR-β while leaving hepatic LXR-α
under-occupied by a factor `S` requires

```
beta_selectivity  >  log10(S) + log10(H) - log10(Kp,uu)
```

| Chemotype | K<sub>p,uu</sub> | S=10, H=1 | S=10, H=10 | S=30, H=10 |
|---|---|---|---|---|
| **Neutral LXR ligand** | 0.91 | **1.04** | 2.04 | 2.52 |
| **Fibrate-like acid** | 0.059 | **2.23** | 3.23 | 3.70 |

**The acid pays 1.16 log units more for the same hepatic margin, purely
because it reaches the retina ~15× less well.** At the central assumption
(S = 10, H = 3.16) the bars are ≈1.55 log (neutral) and 2.73 log (acid).

Against **797** potent dual-measured LXR ligands:

| | n |
|---|---|
| Clear their own 10× hepatic margin | **8** |
| …and pass the retinal-access filter | **5** |
| …and clear it on **worst-case** selectivity too | **4** |
| **Acidic/zwitterionic molecules clearing the acid bar (2.73 log)** | **0** of 83 |

**The acid route is empirically unoccupied.** Not one of 83 measured acidic LXR
ligands carries the selectivity a fibrate-like K<sub>p,uu</sub> demands; the
most selective reaches 2.66 log against a 2.73 requirement. This is the
brief's claim — *it cannot be done from the liver* — recovered as arithmetic.

## 6. The candidates, and what is wrong with them — **MEASURED**

`efflux_axis_candidates.csv`. Potency is tiered by what the assay could show:
`cell_functional` (EC50, cell-based), `lbd_recruitment` (EC50, cell-free LBD),
`displacement` (IC50/Ki/Kd, direction unknown). Selectivity is only differenced
*within* a tier.

| Rank | ChEMBL ID | β-sel | worst-case | p(LXR-β) | p(LXR-α) | logP | MW | TPSA | K<sub>p,uu</sub> | margin |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CHEMBL5899878 | 2.31 | **1.43** | 7.82 | 5.51 | 3.17 | 383 | 67 | 0.85 | +0.74 |
| 2 | CHEMBL5938562 | 2.22 | 2.22 | 7.80 | 5.58 | 3.73 | 453 | 77 | 0.85 | +0.65 |
| 3 | CHEMBL5762664 | 1.87 | 1.87 | 7.37 | 5.50 | 3.73 | 453 | 77 | 0.85 | +0.30 |
| 4 | CHEMBL5838420 | 1.76 | 1.76 | 7.60 | 5.84 | 3.73 | 453 | 77 | 0.85 | +0.19 |
| 5 | CHEMBL6003444 | 1.75 | 1.75 | 6.47 | 4.72 | 4.10 | 423 | 67 | 0.93 | +0.22 |

One scaffold: a chiral 2-isopropylpiperazine bearing an aryl methylsulfone,
N4-capped with Boc (1, 5) or a trifluoromethylpyridine (2, 3, 4). Properties
are genuinely good — MW 383–453, TPSA 67–77, **HBD 0**, logD 3.2–4.1, neutral,
no efflux-risk flags on 1 and 5 (2–4 carry two each).

**Three things are wrong with this list, and they are not small.**

1. **All five come from one document, CHEMBL5725956 — a 2018 patent,
   "Piperazine derivatives as liver X receptor modulators".** It contributes
   812 of 3,732 axis activities and 382 molecules. This is one series,
   measured by one group, never independently replicated. Patent potency data
   is reported by a party with an interest in it.

2. **The evidence tier is cell-free.** All five rest on a coactivator-
   recruitment FRET assay on the isolated ligand-binding domain. That reports
   a conformational response, not transcription — and the source assay is run
   in **both agonist and antagonist mode**, so even the EC50 is not
   unambiguously agonist. Nothing here demonstrates ABCA1 induction in a cell,
   let alone a retinal cell.

3. **The cellular tier does not reproduce the selectivity.** Among the 106
   molecules with paired *cell-based functional* data, the maximum
   β-selectivity is **1.37 log and the best margin is −0.13. Not one clears
   its own requirement.** The selectivity that makes the top five viable has
   never been shown in a cell by anyone.

Candidate 1 carries a further specific defect: its two reported LXR-α EC50s
differ **57-fold** (409 nM and 23,192 nM, 1.76 log). Taking the lower value its
selectivity is 1.43 log and **it fails**. Across the axis, 29% of molecule-gene
pairs with ≥2 EC50s span more than a log — which is why `candidates.py` carries
`beta_selectivity_worst` and why candidate 1 should be ranked below candidate 2
despite the higher median.

**The defensible reading:** a neutral β-selective LXR agonist with the required
profile is *chemically reachable* — one series has claimed it — but no public
molecule has demonstrated it where it counts. The next experiment is not a
screen; it is an ABCA1/ABCG1 transactivation assay on candidates 2–4 in a
retinal cell, with SREBF1 in a hepatocyte alongside.

## 7. Acceptor versus inducer — the ordering is backwards

`src/analysis/efflux_axis/acceptor.py`; `efflux_axis_burden_model.csv`.

### The model — **MODELLED**

```
dL/dt  =  J_in  -  k_t·E·L  -  k_a·A·L
```

`L` retinal lipid burden; `J_in` scavenger influx (where all 29 compounds act);
`k_t·E` transporter efflux, `E` = ABCA1/ABCG1 activity relative to healthy;
`k_a·A` direct removal by an administered extracellular acceptor. Steady state
is `L_ss = J_in / (k_t·E + k_a·A)`.

**An inducer multiplies `E`. An acceptor adds a term.** That is the whole
argument, and it is structural rather than quantitative.

### At E = 0 exactly

| Arm | Steady-state burden | Time to 5× threshold |
|---|---|---|
| Untreated | **∞** | 4.0 |
| Supply-lowering, influx halved | **∞** | 8.0 |
| Supply-lowering, influx cut 10× | **∞** | 40.0 |
| Transporter inducer, 10× | **∞** | **4.0** |
| Transporter inducer, **1000×** | **∞** | **4.0** |
| **Direct acceptor, 0.1× healthy clearance** | **10.0** | 5.9 |

A 1000-fold inducer changes nothing — not the steady state, not even the time
course — because it scales a term that is zero. A supply-lowering agent
multiplies the slope of an unbounded ramp: cutting influx tenfold buys 10× the
time and no control. **This is the brief's claim confirmed exactly: a
supply-lowering agent buys only delay, and so does an inducer at E = 0.**

### Where the ordering inverts — **MODELLED**

The inversion is not unconditional. The inducer's *incremental* clearance is
`k_t·E·(F−1)` and the acceptor's is `k_a·A`; they cross at

```
E*  =  (k_a·A) / (k_t·(F − 1))
```

Transporter activity `E` (fraction of healthy) below which the acceptor
contributes more:

| acceptor \ inducer fold | 2× | 3× | 5× | 10× |
|---|---|---|---|---|
| 0.05 | 0.050 | 0.025 | 0.013 | 0.006 |
| 0.10 | 0.100 | 0.050 | 0.025 | 0.011 |
| 0.25 | 0.250 | 0.125 | 0.063 | 0.028 |
| 0.50 | 0.500 | 0.250 | 0.125 | 0.056 |

At E = 0.02 — transporter at 2% of healthy — a 10× inducer reaches burden 5.0
and an acceptor at 0.1 reaches 8.3: **the inducer still wins there.** Below
E ≈ 0.011 it does not, and at E = 0 it loses to any acceptor whatsoever.

### Verdict — **REASONED from the above**

**Yes, the preference ordering the analysis carried is backwards — in the
regime the lesion describes.** The qualification is the honest part: the
inversion depends on `E` being below roughly 1–3% of healthy, and **`E` in
human diabetic retina is not measured.** That is the single number that
decides between the two programmes, and nobody has it.

What can be said without it:

- The acceptor arm is the only one that **guarantees** a steady state. It is
  robust to `E`; the inducer arm is not.
- The inducer arm is **not** ruled out the way it is for fibrates. Step 5
  showed the gene-activation limb absent at achievable fibrate occupancy; at
  K<sub>p,uu</sub> ≈ 0.9 a neutral LXR ligand *can* occupy the receptor. The
  brief's "two-step relay, more sensitive to the shortfall" argument applies
  to the acid chemotype, not to this one.
- They are **complementary, not competing**: the acceptor adds `k_a·A`, the
  inducer multiplies `k_t·E`. Combination is the rational configuration, and
  the model shows acceptor 0.1 + inducer 3× at E = 0.02 reaching 6.25 against
  8.33 for the acceptor alone.

**Practical note (REASONED).** apoA-I mimetic peptides, reconstituted HDL and
cyclodextrins do not cross the blood-retinal barrier, so the acceptor arm is an
**intravitreal** proposition. That is a different development path from an oral
fibrate — but it is the path this disease already uses: intravitreal dosing is
standard of care in DR. The barrier that disqualifies the acceptor as a systemic
drug is irrelevant to the route the indication already takes. **This is the
single most consequential reframing in this note**: the analysis ranked
candidates by oral-systemic feasibility for a disease treated by injection into
the target compartment.

## 8. What this changes, and what it does not

**Closed.**
- The axis has measured pharmacology at exactly one node, LXR; the effectors
  cannot be drugged directly. **MEASURED**
- The neutral-ligand opening is real and worth ~1.16 log of selectivity
  requirement. **MODELLED**
- The acid route is empirically unoccupied: 0 of 83. **MEASURED**
- The GNN cannot rank this axis and is anti-predictive in this direction.
  **MEASURED**

**Open, and now specified.**
- **`E` in human diabetic retina** — ABCA1/ABCG1 activity relative to healthy.
  Decides acceptor versus inducer outright. Not measured in any species.
- **Cellular β-selectivity** for the piperazine series: ABCA1/ABCG1
  transactivation in a retinal cell, SREBF1 in a hepatocyte. Would move five
  candidates from cell-free claim to cellular fact, or kill them.
- **Hepatic free-concentration multiple `H`** for a neutral lipophilic LXR
  ligand. Swings the selectivity requirement by a full log unit.
- **Efflux ratio at the blood-retinal barrier** for any LXR ligand. Zero
  measurements exist; `physchem._efflux_risk` is a declared heuristic, not a
  prediction.

**Not closed, and should not be claimed.** No molecule in this note has been
shown to raise ABCA1 in a retinal cell, to reach the retina in any species, or
to spare the liver in vivo. The five ranked candidates are a chemical
hypothesis from one patent. The strongest statement the data supports is that
**the programme is arithmetically defensible where the fibrate programme is
not** — and that is a statement about which experiment to run, not about a drug.
