# The retinal exposure model

**Step 5 of `docs/prompts/dr-solve-open-questions-prompt.md`.**
Date: 2026-11-09. Branch: `local-llm-subproject`.

---

## 0. VERDICT

**Local PPARα engagement is not achievable for any of the four compounds at any
labelled dose. The one compound that comes close is seladelpar, and it comes close on
PPARδ, not PPARα.**

Best case per compound — free concentration against free EC50, at the compartment that
faces the blood directly and is therefore the *most* favourable one, using peak rather
than average plasma concentration:

| Compound | Receptor | Margin at the endothelium (Cmax) | Fold short |
|---|---|---:|---:|
| Fenofibric acid 135 mg/d | PPARα | **0.0198** [0.0017 – 0.245] | 51× |
| Pemafibrate 0.2 mg/d | PPARα | **0.0267** [0.0018 – 0.387] | 37× |
| Elafibranor 80 mg/d, parent **+ GFT1007** | PPARα | **0.136** [0.0035 – 5.67] | 7.3× |
| Seladelpar 10 mg/d | **PPARδ** | **0.558** [0.0375 – 8.59] | **1.8×** |
| Seladelpar 10 mg/d | PPARα | 0.00074 [5.0e-05 – 0.0116] | 1,340× |

Three findings matter more than the ratios themselves, and each was computed here
rather than argued:

1. **Two of the three compartments are not behind a barrier at all.** The retinal
   vascular endothelium *is* the inner blood-retinal barrier — its luminal membrane
   faces plasma — and the RPE faces the fenestrated choriocapillaris. Assigning them a
   partition ratio of 0.2–0.7 treated them as though they sat behind the junction they
   form. Their ceiling is 1.0, and what puts them below it is efflux, not partition.
   §2.
2. **The variance is not where the argument has been.** At the endothelium and RPE —
   the compartments that matter for vascular leakage — the **EC50 and the serum
   conditions it was measured in carry 69% of the output variance** (Sobol ST 0.694),
   and the entire barrier block carries 19%. The programme has spent its attention on
   the parameter that contributes a fifth of the uncertainty in the compartment that
   matters. §9.
3. **The reason fibrates work on the liver is a transporter the retina does not
   express.** Run backwards against the clinical lipid effect, the model says the liver
   must reach 37–92× its free plasma concentration. OATP1B1 is **502.3 nTPM in liver
   and 0.0 nTPM in retina** (9th percentile); OATP1B3 is 247.7 against 0.0. Measured,
   this step. Hepatoselectivity is not incidental to these drugs — it is the mechanism —
   and it is the property that denies them the eye. §10.

**What this replaces.** The DR analysis assigned 0.2–0.7 for endothelium and RPE and
0.01–0.15 for neural retina, by argument. The neural-retina figure turns out to be
approximately right for the wrong reason: calibrated against the one measured ocular
concentration of a fibrate after systemic dosing in any species, **Kp,uu = 0.059
[95% CI 0.009 – 0.354]**, a 17-fold exclusion (95% CI 2.8 – 111×).

The endothelium/RPE figure was wrong in **structure** rather than in magnitude, and the
distinction matters. The model's blood-facing prior (0.1–1.0, median 0.32) sits close to
the asserted 0.2–0.7, so the numbers barely move; what changes is that the ceiling is now
1.0 rather than 0.7, the reason for being below it is named and measured, and these
compartments are placed **5.3× above the neural retina** (0.32 vs 0.059) instead of
being three draws from one range. Every part of that correction runs in the compounds'
favour, which is why it is worth saying that it still does not save them.

---

## 1. WHAT WAS ASKED, AND THE RULE THIS NOTE FOLLOWS

The step asked for a parameterised model in place of an estimate, because a documented
orchestrator error in this analysis came from reporting one term of a product as if it
were the whole product. The structural defence against that is not care; it is making
the provenance of every number machine-checkable. In
`src/analysis/ocular_exposure/parameters.py` a number cannot reach the model except as
a `Param` carrying a distribution and one of three tags:

| Tag | Meaning |
|---|---|
| **MEASURED** | Read directly from a published result or a regulatory label |
| **CONVERTED** | A measured value transformed by stated arithmetic (units, molarity, protein normalisation). No new assumption |
| **ASSUMED** | A distribution spanning a published spread, or a prior where no measurement exists. Judgement, justified at the point of use |

A point estimate has to be declared `point()` explicitly, and then it appears as such in
the parameter table. Nothing in this note is a point estimate.

**Everything numeric below is this command's output**, not transcription:

```bash
venv/bin/python -m src.analysis.ocular_exposure.report
```

---

## 2. THE STRUCTURAL CORRECTION — THREE COMPARTMENTS, NOT ONE RANGE

This is the part that changes the answer before any arithmetic.

**Retinal vascular endothelium.** This cell *is* the inner blood-retinal barrier. Its
luminal membrane is in contact with plasma; there is no barrier between plasma and that
membrane. Its free exposure is therefore the free plasma concentration, reduced only by
what its own ATP-driven pumps return to the lumen. A "partition ratio of 0.2–0.7"
describes a compartment behind a barrier; this one is the barrier.

**Retinal pigment epithelium.** Faces the choriocapillaris, which is fenestrated, so
choroidal interstitial free concentration is plasma free concentration. Also one
membrane from the blood side.

The RPE is additionally the one compartment here that can *exceed* plasma free
concentration, because it expresses concentrative organic-anion **uptake** transporters.
MEASURED, this step, human RPE single-cell nCPM:

| Transporter | Gene | Human RPE | Retinal vascular endothelium | Hepatocyte |
|---|---|---:|---:|---:|
| OAT3 (anion uptake) | SLC22A8 | **464.7** | 0.5 | 0.2 |
| OAT1 (anion uptake) | SLC22A6 | **63.9** | 1.2 | 0.1 |
| MRP5 (anion efflux) | ABCC5 | **822.8** | 18.8 | 4.1 |
| OATP1A2 | SLCO1A2 | 225.9 | 27.6 | 2.4 |

An anionic drug facing a tissue with OAT-mediated uptake can be concentrated, not
excluded. Net direction is unmeasured for any fibrate, so the prior spans both sides of
unity (0.1–10×).

**Neural retina.** The only compartment genuinely behind a tight junction, and behind
two of them — the endothelial junctions of the inner BRB and the RPE junctions of the
outer. Its steady-state free ratio is a competition between clearances:

```
Kp,uu = PS_passive / (PS_passive + CL_efflux + CL_bulk)
```

**Why that form, and why logD is not the answer people expect.** Passive permeability
*cancels out of a steady-state partition ratio across a purely passive barrier*: if the
only way out is the way in, the ratio is 1 however slow it is, and low permeability buys
time to equilibrium rather than a lower plateau. Since these drugs are taken daily for
years, time to equilibrium is not the constraint. Permeability lowers the plateau only
when it competes with a route out that is **not** the way in. For these compounds that
route exists, and it is measured — human retinal vascular endothelium, nCPM:

| Pump | Gene | Retinal endothelium | Hepatocyte | Ratio |
|---|---|---:|---:|---:|
| P-gp | ABCB1 | **507.4** | 75.2 | 6.7× |
| MRP4 (anion efflux) | ABCC4 | **178.2** | 2.4 | 74× |
| BCRP | ABCG2 | **142.0** | 32.6 | 4.4× |

All MEASURED (HPA `rna_single_cell_type`), files
`data/processed/retina_hpa_celltype_ncpm.tsv` and
`data/processed/retina_hpa_bulk_ntpm.tsv`, regenerated this step with a new
`barrier_transport` gene class (§13).

> **Caveat, stated plainly.** This is mRNA, not protein, and no fibrate is a confirmed
> substrate of any of these pumps at any ocular barrier. The expression data establish
> that the machinery is present and abundant; they do not establish that these
> particular molecules are moved by it. That is exactly why `barrier.efflux_rel` is a
> 0.2–5× prior rather than a value, and why the sensitivity analysis is asked to rank it.

---

## 3. THE CALIBRATION ANCHOR, AND THE UNIT TRAP IN IT

**Huang et al. 2021**, *Biology (Basel)* 10(12):1328, PMID 34943243, PMCID PMC8698460,
Table 1. C57BL/6J mice, fenofibrate **2 mg/kg/day intraperitoneally for 7 days**, LC-MS
6 h after the final dose. This is the only measurement of any fibrate in ocular tissue
after systemic dosing, in any species — Step 4 established that, and it is the whole
empirical basis for the barrier term.

| Compartment | Fenofibric acid (IP arm) |
|---|---|
| Vitreous/retina | **0.140 ± 0.044** ng/mg total protein |
| Plasma | **86.304 ± 22.780** ng/mg total protein |

Both MEASURED (mean ± SEM, n = 5–12).

**The trap.** The tissue and plasma columns share one header, "ng/mg of total protein",
and nothing in the Methods describes a plasma protein normalisation. Read as a common
unit the retina:plasma ratio is 0.0016; read as tissue-per-protein against
plasma-per-volume it is ~0.16. **The two readings differ by 60×** and between them lies
the entire question.

It is resolvable from the paper's own arithmetic. The Discussion states that choroidal
fenofibrate is "approximately five-fold higher than the concentration in the peripheral
blood"; the table gives choroid 8.469 and plasma 1.726, and 8.469 / 1.726 = 4.9. **The
authors take the ratio directly, so the columns are on one scale.** The common-unit
reading is the correct one.

> This correction runs *against* the conclusion by a factor of 60 — it makes retinal
> exposure look far worse than the alternative reading — which is the reason to trust it.
> Had it gone the other way it would deserve more scepticism than it is getting here.

**Step 4's recommendation was wrong and is corrected.** The evidence-absence audit
suggested anchoring the partition prior on "the Huang 2021 IP-vs-topical ratio
(≈0.02–0.3)". That ratio compares two *routes of administration*; it is not a partition
coefficient and contains no information about the blood-to-retina ratio. The right
anchor is retina:plasma **within** the IP arm, which is what is used here.

### Inverting the anchor properly

The sample is **pooled vitreous + retina**. Vitreous carries drug but essentially no
protein, so it adds to the numerator and not the denominator: treating the pooled figure
as a retinal tissue concentration overstates retinal exposure. Keeping the phases
separate, for retinal protein mass `P`, retinal volume `V_ret`, vitreous volume `V_vit`
and retinal tissue binding `fu_ret`:

```
M [ng/mg protein] = (Cu * V_vit + (Cu / fu_ret) * V_ret) / P
  =>  Cu,retina  = M * P / (V_vit + V_ret / fu_ret)
      Cu,plasma  = M_plasma * [plasma protein] * fu_plasma
```

Code: `src/analysis/ocular_exposure/barrier.py::kpuu_neural_retina_reference`.

**Result: Kp,uu (neural retina, fenofibric acid) = 0.0594 [95% CI 0.0090 – 0.3544]**,
i.e. a 16.8× exclusion (95% CI 2.8 – 111×).

The DR analysis asserted 0.01–0.15. The calibrated value sits inside that band. **The
assertion was approximately right, and it was right by luck rather than by derivation** —
it now has a measurement behind it, a stated bias direction, and bounds that extend
3.6× above the asserted ceiling.

### Anchor parameters

| Parameter | Value [95% CI] | Provenance | Source |
|---|---|---|---|
| `anchor.retina_ffa` | 0.140 ± 0.044 (SEM) ng/mg | MEASURED | Huang 2021 Table 1, vitreous/retina, IP arm |
| `anchor.plasma_ffa` | 86.304 ± 22.780 (SEM) ng/mg | MEASURED | Huang 2021 Table 1, plasma, IP arm |
| `anchor.retina_protein_mg` | 0.20 – 0.45 mg | ASSUMED | mouse neural retina ~2.5–3.5 mg wet, ~10% protein |
| `anchor.vitreous_vol_ul` | 4.4 – 6.0 µL | ASSUMED | adult mouse vitreous volume, published range |
| `anchor.retina_vol_ul` | 2.2 – 3.5 µL | ASSUMED | wet weight 2.3–3.7 mg at ~1.05 g/mL |
| `anchor.plasma_protein_mouse` | 45 – 65 mg/mL | ASSUMED | mouse total plasma protein reference interval |
| `anchor.fu_plasma_mouse_ffa` | 0.010 [0.004 – 0.030] | ASSUMED | human value 0.01 (label); allows 3× species difference |
| `anchor.fu_tissue_retina` | 0.15 – 0.80 | ASSUMED | **no fibrate value exists** for any neural tissue |
| `anchor.late_sample_bias` | 1.3 [0.7 – 3.0] (divisor) | ASSUMED | direction from PK first principles; magnitude is judgement |

On the last row: a single 6 h time point on a falling plasma curve is not a steady-state
ratio. For a slowly-equilibrating tissue the late ratio reads **high**, so the prior is
centred above 1 and divides the measured ratio. The direction is defensible; the
magnitude is not measured, and it is carried as uncertainty rather than asserted.

---

## 4. INDEPENDENT CALIBRATION — MEASURED OCULAR PARTITION FOR OTHER DRUGS

One experiment is a point, not a calibration. The check is human studies that measured a
systemically dosed drug in aqueous humour *and* plasma in the same patients at cataract
surgery. Aqueous humour is effectively protein-free (total protein ~0.5 mg/mL against
plasma's ~70), so the measured aqueous concentration **is** a free concentration and

```
Kp,uu = (C_aqueous / C_plasma,total) / fu_plasma
```

converts a published ratio into the quantity the model computes. Making that conversion
is the point: raw aqueous-to-plasma ratios are routinely read as "penetration" when for
a highly bound drug they are mostly a statement about plasma binding.

| Drug | Charge | Aqueous/plasma (total) | fu plasma | **Kp,uu (free/free)** | Source |
|---|---|---:|---:|---:|---|
| Aciclovir | neutral | 0.37 | 0.78–0.91 | **0.41–0.48** | Hung 1984, PMID 6696872, 5 × 400 mg oral, n = ? at cataract extraction |
| Levofloxacin | zwitterion | 0.33–0.57 | 0.62–0.76 | **0.43–0.92** | Pea 2005, PMID 15917572, 2 × 500 mg oral |
| Pefloxacin | zwitterion | 0.50–0.89 | 0.70–0.80 | **0.62–1.27** | Salvanet-Bouccara 1991, PMID 1955654, 400 mg bd × 3 d, n = 38 |
| Indometacin | **anion**, 99% bound | below assay limit | 0.01 | **< detection** | Sanders 1983, PMID 6626018, oral, serum 642 ng/mL |

**What this establishes.** At a tight-junction ocular barrier, a drug that is *not* an
anionic efflux substrate reaches roughly half of free plasma — Kp,uu ≈ 0.4–1.3 across
three drugs, three studies and three decades. The model places an anionic fibrate at
0.059, about **an order of magnitude below** that, and the measured efflux machinery of
§2 is the stated reason. Had the model returned ~0.5 for a fibrate it would be saying the
pumps do not exist.

The indometacin row is the only acid in the set and it is a bound, not a value: in 1983
"below the assay limit" against 642 ng/mL serum is consistent with Kp,uu anywhere from
0.5 down. It constrains the direction and nothing more, and is reported that way.

**Mechanistic anchor for the efflux term, at the retinal barrier proper.** Fujii 2015,
*Drug Metab Dispos* 43:1956, PMID 26431714: pravastatin, an anionic statin acid, at the
rat BRB — retinal uptake index **below** that expected from its lipophilicity, vitreal
elimination rate constant **1.66× that of the bulk-flow marker mannitol**, and efflux
reduced by pravastatin, digoxin and benzylpenicillin. The authors conclude
retina-to-blood transport is dominant. That is the closest structural analogue anyone has
studied at this barrier, and it is the direction the efflux term encodes.

> **Caveat.** The blood-aqueous barrier (ciliary epithelium, iris vessels) is not the
> blood-retinal barrier. Both are tight-junction barriers carrying ABC and SLC
> transporters, but they are different tissues. This is a plausibility check, not a
> substitute measurement.

---

## 5. IONISATION

The step specified that logD must come from measurement or calculation, not from
`alogp`. Two things turned up while complying.

**The `logd` column is empty for a reason upstream of this repository.** Confirmed:
`data/processed/chembl_approved_drugs.csv` has 3,276 rows, `logd` non-null **0**,
`alogp` non-null 2,973. The cause is not the scraper. ChEMBL's own API no longer serves
the ChemAxon-derived fields — `cx_logd`, `cx_logp` and `cx_most_apka` all return `null`
for all seven fibrates queried directly (`CHEMBL981`, `CHEMBL247951`, `CHEMBL3707395`,
`CHEMBL230158`, `CHEMBL672`, `CHEMBL264374`, `CHEMBL457`). No amount of re-scraping will
fill that column.

**No experimental pKa exists for any of the four** in PubChem's experimental-properties
record (`pug_view` returns `PUGVIEW.NotFound` for Dissociation Constants on fenofibric
acid, CID 64929), in ChEMBL, or in the papers reached by this search. pKa is therefore
ASSUMED, from the measured values of the unsubstituted parent acid of each headgroup.

Henderson-Hasselbalch, computed in `src/analysis/ocular_exposure/ionisation.py`:

| Compound | pKa (prior) | logP | **logD(7.4)** | Neutral fraction | Cytosol/plasma free (pH 7.1 vs 7.4) |
|---|---|---:|---:|---:|---:|
| Fenofibric acid | 2.8–3.5 | 3.81 | **−0.44** | 5.6 × 10⁻⁵ | 0.50 |
| Pemafibrate | 3.0–3.7 | 5.55 | +1.50 | 8.9 × 10⁻⁵ | 0.50 |
| Elafibranor | 2.8–3.5 | 5.16 | +0.91 | 5.6 × 10⁻⁵ | 0.50 |
| GFT1007 | 2.8–3.5 | 4.60 | +0.35 | 5.6 × 10⁻⁵ | 0.50 |
| Seladelpar | 2.8–3.4 | 5.05 | +0.75 | 5.0 × 10⁻⁵ | 0.50 |

**Internal consistency check.** The step description states logD(7.4) is "roughly −0.5
against a nominal logP near 3.8". With logP 3.81 that figure is reproduced only at
pKa 3.10:

```
logD = 3.81 − log10(1 + 10^(7.4 − 3.10)) = 3.81 − 4.30 = −0.49
```

The brief's own number and the chemotype assignment agree, independently. That is the
closest thing to a measurement of these pKa values available here, and it is worth more
than the assertion it replaces.

**Two conclusions from the ionisation block.** The compounds are 99.99% ionised at
pH 7.4, so passive transcellular permeability is poor — but per §2 that sets the time to
equilibrium, not the plateau. And the cytosol/plasma pH-partition term is **0.50**, a
factor of two, not the orders of magnitude that ion trapping gives a base in a lysosome.
It also **cancels** from the final comparison, because the EC50 assay's target receptor
sat in a cytosol at the same pH offset from its own medium. The model therefore does not
apply it, and that is deliberate.

---

## 6. COMPOUND PARAMETERS

Plasma exposure is taken from the FDA label wherever one exists, because a label PK table
is the one number in this literature audited by someone whose job was to disbelieve it.
**Cavg,ss is derived as AUC(0–τ)/τ**, not taken as Cmax, because a nuclear receptor at
steady state sees the average; Cmax is carried alongside and reported as the best case.

| Compound | MW | Dose | **Cavg,ss (ng/mL)** [95% CI] | Cmax,ss | **fu** | fu provenance |
|---|---:|---:|---|---|---|---|
| Fenofibric acid | 318.76 | 135 mg/d | **5,114** [2,600 – 11,000] | 12,000 | 0.010 [0.005–0.020] | MEASURED — Trilipix label 12.3, "approximately 99%" |
| Pemafibrate | 490.56 | 0.2 mg/d | **0.271** [0.087 – 0.847] | 2.1 | 0.001 – 0.020 | **ASSUMED — no accessible measured value** |
| Elafibranor | 384.50 | 80 mg/d | **156.6** [65.7 – 372.9] | 802 | 0.003 [0.0015–0.006] | MEASURED — Iqirvo label 12.3, 99.7% |
| GFT1007 | 386.52 | (same dose) | **499.4** [169 – 1,472] | 2,058 | 0.003 [0.0015–0.006] | MEASURED — Iqirvo label 12.3, 99.7% |
| Seladelpar | 444.47 | 10 mg/d | **34.0** [14.9 – 77.6] | 90.5 | 0.001 – 0.010 | MEASURED as a **bound** — Livdelzi label, ">99%" |

Sources, in full:

- **Fenofibric acid** — Trilipix FDA label (DailyMed setid `3057fc9c-ff77-43eb-b687-776660423742`)
  §12.3: CL/F 1.1 L/h, F 81%, t½ 20 h, steady state in 8 days, "slightly more than
  double" the single dose. Cavg is CONVERTED from the label's own clearance
  (135 mg / (1.1 L/h × 24 h) = 5,114 ng/mL); the interval is widened beyond a plain 40% CV
  to span the independently published Cmax 10–15 / trough 4–6 µg/mL band for 200 mg
  micronised fenofibrate, which implies Cavg 6–8 µg/mL. The label states no Cmax in mass
  units, which is why the derivation is shown.
- **Pemafibrate** — PMC11883216, steady state at 4 weeks, IR 0.2 mg/day fasted, n = 20
  patients with hypertriglyceridaemia: Cmax,ss **2.1 ng/mL (CV 37.9%)**, AUC(0–τ)
  **6.5 ng·h/mL (CV 63.5%)**, t½ 2.0 h. Corroborated independently: the PARMODIA package
  insert gives Cmax **3.57 ng/mL (7.28 nM)** at the 0.4 mg/day maximum after 7-day
  repeats, quoted in PMC9102038 — consistent with 2.1 ng/mL at half that dose.
- **Elafibranor and GFT1007** — IQIRVO FDA label (setid `d78aa14f-…`) §12.3 Table 5,
  steady state in PBC patients at 80 mg once daily. GFT1007 is the **major active
  metabolite at 3.2× the parent's exposure**; omitting it would discard most of
  elafibranor's PPARα drive, so it is modelled as a fifth compound.
- **Seladelpar** — LIVDELZI FDA label (setid `89f79d98-…`) §12.3: median Cmax,ss
  **90.5 ng/mL (CV 42.5%)**, AUC **817 ng·h/mL (CV 44%)**, Vd/F 110.3 L, CL/F 12.6 L/h,
  t½ 6 h, all three major metabolites pharmacologically inactive.

> **The one parameter with no measurement anywhere** is pemafibrate's plasma protein
> binding: absent from every FDA and EMA label (the drug is approved in Japan only) and
> not found in PubMed, PMC or Europe PMC. It is carried as a 0.001–0.020 prior. §8 shows
> why that turns out not to matter, which is not an excuse for the gap but is the honest
> consequence of it.

### Potency

26 PPARα EC50 determinations from independent laboratories, read from
`data/processed/chembl_panel_bioactivities.csv` (built in Step 1 of this chain).
The inter-laboratory spread **is** the uncertainty; quoting one paper's figure would
hide it. Censored records (`>`) are kept and reported but never averaged in — doing so
would pull a weak compound's EC50 down towards its own detection limit.

| Compound | Receptor | n (=) | Median EC50 | 95% CI | GSD | Censored (>) |
|---|---|---:|---:|---|---:|---|
| Fenofibric acid | PPARα | 13 | **15,000 nM** | 2,490 – 90,400 | 2.50 | 10,000 ×4, 100,000 |
| Pemafibrate | PPARα | 3 | **1.0 nM** | 0.17 – 6.0 | 2.50† | — |
| Elafibranor | PPARα | 8 | **290.5 nM** | 12.8 – 6,610 | 4.92 | — |
| Seladelpar | **PPARδ** | 3 | **2.0 nM** | 0.33 – 12.1 | 2.50† | — |
| Seladelpar | PPARα | 1 | 1,500 nM | 249 – 9,040 | 2.50† | 1,000 |

† GSD floored at 2.5. Three laboratories agreeing to one significant figure is agreement
about the order of magnitude, not evidence that between-assay spread is zero.

**Seladelpar is evaluated against both receptors.** The DR analysis cares about PPARα;
seladelpar is a PPARδ agonist whose PPARα EC50 is 750× weaker. Reporting only its PPARα
margin would judge it on a receptor it was not built for, and reporting only its PPARδ
margin would quietly change the question.

---

## 7. THE MODEL

```
margin = Cu(compartment) / EC50(free)
```

with the free fraction removed from **both** sides. A margin of 1 means free
concentration sits at the free EC50; the reciprocal is the fold shortfall.

Per compartment:

```
Cu(endothelium)   = Cu,plasma x endo_retention          # one membrane from blood
Cu(RPE)           = Cu,plasma x rpe_net                 # fenestrated choriocapillaris
Cu(neural retina) = Cu,plasma x Kp,uu                   # behind two tight junctions
```

and `Kp,uu` is transferred from the calibrated fenofibric-acid value by writing the
reference as a clearance ratio and moving only the compound-specific part:

```
theta_ref = 1/Kp,uu_ref - 1 = (CL_efflux + CL_bulk) / PS
theta     = theta_ref * [(1 - share) + share * r_efflux] / r_perm
Kp,uu     = 1 / (1 + theta)
```

Bulk flow out of the eye is a property of the eye, not of the molecule, so only the
`share` that is active efflux is allowed to move when the compound changes. `r_perm`
comes from logD(7.4) and molecular weight with both slopes carried as uncertainties, and
`r_efflux` is a 0.2–5× prior because no fibrate efflux ratio has been measured at any
ocular barrier.

**23 inputs, 200,000 draws, seed 20261109.** Barrier and assay priors:

| Parameter | Value | Provenance | Basis |
|---|---|---|---|
| `barrier.endo_retention` | 0.10 – 1.00 | ASSUMED | ceiling 1.0 is structural (§2); floor bounded by measured ABCB1/ABCC4/ABCG2 abundance |
| `barrier.rpe_net` | 0.10 – 10.0 | ASSUMED | measured OAT1/OAT3 uptake *and* ABCC5 efflux; net direction unmeasured |
| `barrier.efflux_rel` | 0.2 – 5.0× | ASSUMED | no fibrate efflux-ratio measurement exists at any ocular barrier |
| `barrier.efflux_share` | 0.0 – 1.0 | ASSUMED | unmeasured split between active efflux and bulk flow |
| `barrier.perm_logd_slope` | 0.30 – 1.00 | ASSUMED | typical slope of log Papp on logD within a congeneric series |
| `barrier.perm_mw_slope` | 0 – 0.010 /Da | ASSUMED | size penalty; 0 = none, 0.01 = strong |
| `compound.logp` error | 0 ± 0.7 log | ASSUMED | RMSE of a calculated logP; **no measured logP for any of the four** |
| `assay.serum_fraction` | 0.005 – 0.10 | ASSUMED | 0.7% measured for the one fully-specified PPAR protocol; 10% is the common default |
| `assay.fbs_albumin_ratio` | 0.40 – 0.75 | ASSUMED | bovine serum albumin ~20–30 g/L vs human plasma ~40–45 g/L |

---

## 8. THE SERUM CORRECTION, AND WHY IT MAKES THE ANSWER ROBUST

The step flagged that comparing free drug against a nominal EC50 double-counts protein
binding and that the inconsistency is "worth about a log". It is, and the model gives the
figure precisely.

A cell assay reports the **total** concentration added to the well; albumin in the medium
bound some of it. With binding linear in albumin — true well below saturation, which is
where an EC50 sits:

```
1/fu - 1 = K[albumin]   =>   fu_assay = 1 / (1 + (1/fu_plasma - 1) * s)
EC50_free = EC50_nominal * fu_assay
```

where `s` is the medium's albumin as a fraction of plasma's.

**The assay condition is measurable, and for once it is stated.** Kamata 2022
(PMC9102038) is the one PPAR transactivation protocol in this literature that reports its
medium in full: COS-7 cells seeded in 90 µL DMEM + **1% FBS**, ligands added in 25 µL
**serum-free** DMEM, i.e. **~0.7% FBS final**. Most ChEMBL assay descriptions state
nothing, so `s` is carried as a 0.5–10% prior rather than applied as a single factor.

| Compound | Receptor | Median EC50 overstatement | 95% CI | In logs |
|---|---|---:|---|---:|
| Fenofibric acid | PPARα | **2.3×** | 1.2 – 7.9× | 0.35 log |
| Pemafibrate | PPARα | **3.8×** | 1.3 – 30.6× | 0.58 log |
| Elafibranor / GFT1007 | PPARα | **5.2×** | 1.8 – 24.3× | 0.72 log |
| Seladelpar | PPARδ | **5.0×** | 1.5 – 33.3× | 0.70 log |

"About a log" is right at the high-serum end and a third of that at the low-serum end.
Correcting it **lowers** the EC50 — it runs in the compounds' favour — which is the second
correction in this note that works against its own conclusion.

### The correction is also what makes the one missing measurement harmless

Once the EC50 carries the same binding term, `fu` appears on both sides and largely
cancels: margin ∝ `fu / fu_assay` ≈ `(fu + s)`. Computed, with every other input held at
its median:

| Compound | fu range spanned | fu fold-range | Margin fold-range |
|---|---|---:|---:|
| Fenofibric acid | 0.0034 – 0.0298 | 8.9× | **2.6×** |
| **Pemafibrate** | 0.0010 – 0.0199 | **19.9×** | **2.3×** |
| Elafibranor / GFT1007 | 0.0010 – 0.0090 | 8.9× | 1.6× |
| Seladelpar | 0.0010 – 0.0100 | 10.0× | 1.6× |

A **20-fold** swing in pemafibrate's unmeasured free fraction moves its margin **2.3×**.
The parameter with no published measurement barely moves the answer.

**The converse is the real warning.** An analysis that compares free drug against an
*uncorrected* nominal EC50 gets a margin scaling with the full `fu` fold-range — so its
conclusion is dominated by the parameter that should be nearly irrelevant, and for
pemafibrate that is a factor of 20 of pure artefact. This is the same class of error as
the documented orchestrator mistake: a term reported as if it were the product.

---

## 9. SENSITIVITY — WHERE THE VARIANCE ACTUALLY IS

Saltelli/Jansen first-order and total Sobol indices on **log10(margin)**, 23 inputs,
n = 32,768 (= 819,200 model evaluations per compound-compartment). Log scale, because
variance decomposition on a linear margin built from a product of lognormals describes
the top percentile and calls it the model.

### Grouped — the decision-relevant decomposition

A per-input ranking makes the barrier look unimportant purely because its uncertainty is
spread over eighteen parameters while potency sits in one. The decision — where to spend
measurement effort — is made between blocks, so blocks are indexed as units.

**Neural retina:**

| Input block | mean ST | range across compounds |
|---|---:|---|
| Barrier (partition ratio, all 18 inputs) | **0.509** | 0.356 – 0.633 |
| Potency (EC50 + its assay conditions) | **0.428** | 0.279 – 0.601 |
| Plasma exposure (dose, PK, binding) | 0.064 | 0.041 – 0.097 |

**Endothelium** (and by the same structure, RPE):

| Input block | mean ST | range across compounds |
|---|---:|---|
| **Potency (EC50 + its assay conditions)** | **0.694** | 0.589 – 0.818 |
| Barrier (partition ratio, all 18 inputs) | 0.194 | 0.117 – 0.260 |
| Plasma exposure (dose, PK, binding) | 0.111 | 0.055 – 0.204 |

### Per input, endothelium

| Input | mean S1 | mean ST |
|---|---:|---:|
| `compound.ec50_nominal` | 0.505 | **0.516** |
| `barrier.endo_retention` | 0.185 | 0.194 |
| `assay.serum_fraction` | 0.169 | **0.171** |
| `compound.c_plasma` | 0.091 | 0.094 |
| `compound.fu_plasma` | 0.017 | 0.017 |

### Per input, neural retina

| Input | mean S1 | mean ST |
|---|---:|---:|
| `compound.ec50_nominal` | 0.321 | **0.325** |
| `compound.logp` | 0.122 | 0.136 |
| `assay.serum_fraction` | 0.095 | 0.099 |
| `barrier.perm_mw_slope` | 0.072 | 0.083 |
| `anchor.fu_plasma_mouse_ffa` | 0.064 | 0.071 |
| `compound.c_plasma` | 0.052 | 0.054 |
| `barrier.perm_logd_slope` | 0.035 | 0.051 |
| `anchor.late_sample_bias` | 0.039 | 0.042 |
| `anchor.retina_ffa` | 0.037 | 0.041 |
| `barrier.efflux_rel` | 0.028 | 0.037 |

First-order indices sum to ~1.0, so the model is close to additive in log space and
interactions are minor.

### What this says, and it is not what the programme assumed

**For the endothelium and RPE — the compartments relevant to vascular leakage, and the
two that are not behind a barrier — the dominant uncertainty is the EC50 and the serum
conditions under which it was measured (ST 0.516 and 0.171, 0.694 as a block). The
partition ratio contributes 19%.** The DR analysis sequenced its whole programme behind
an ocular PK measurement, and for these compartments the partition ratio is not the
binding uncertainty.

**For the neural retina the two blocks are near-equal** (0.509 barrier, 0.428 potency).
Neither alone resolves it, and an ocular PK study that settles the barrier block would
leave a 0.43 share standing.

**So the ranked measurement list is:**

1. **A PPARα EC50 determined at a stated, physiological protein concentration**, for all
   four compounds in one assay. This is the single highest-variance input in the two
   compartments that matter, it is a cell-culture experiment, and it needs no animal.
   Nobody has done it because nobody knew it was the bottleneck.
2. **Mouse plasma protein binding of fenofibric acid** (`anchor.fu_plasma_mouse_ffa`,
   ST 0.071 and the second-ranked input for fenofibric acid specifically at 0.14). A
   one-day equilibrium-dialysis experiment that tightens the calibration anchor.
3. **A measured logP** for the four compounds (`compound.logp`, ST 0.136 — second overall
   in the neural retina). Shake-flask, one week. None of the four has one.
4. **Ocular PK after oral dosing** — the experiment the programme is sequenced behind.
   Still worth doing, still the only thing that settles the neural-retina barrier block,
   but it is third or fourth on variance, not first.

---

## 10. CALIBRATION — THE CHECK THAT DECIDES WHETHER TO BELIEVE ANY OF THIS

A model saying free fenofibric acid sits 100× below its free PPARα EC50 has an obvious
problem: **fenofibrate at 200 mg/day demonstrably activates hepatic PPARα.**
Triglycerides fall 30–50%. If the model cannot explain how the liver manages it, the
model is wrong.

Run backwards, the model states the hepatic concentration factor the observed effect
**requires**:

| Compound | Receptor | Required liver Kp,uu | 95% CI |
|---|---|---:|---|
| Fenofibric acid | PPARα | **37.5×** | 4.0 – 335× |
| **Pemafibrate** | PPARα | **91.6×** | 7.5 – 1,160× |
| Elafibranor | PPARα | 42.7× | 1.2 – 1,420× |
| GFT1007 | PPARα | 13.5× | 0.37 – 476× |
| **Seladelpar** | **PPARδ** | **1.5×** | 0.14 – 16.5× |
| Seladelpar | PPARα | 1,130× | 101 – 12,400× |

**Three things make this a real check and not a rationalisation.**

1. **The mechanism is the right one and is sourced.** For a compound with low passive
   diffusion clearance — which a 99.99%-ionised acid is by construction — transporter-
   mediated uptake dominates intracellular concentration and Kp,uu(liver) can exceed 1
   (PMC3898878). For contrast, ketoconazole, a neutral drug with no concentrative uptake,
   has a measured hepatic Kp,uu of **0.32–4.67** across six methods (PMC7518636) — i.e.
   near 1. Values of 37–92× require active uptake; they are not what passive partition
   gives you.
2. **The ordering falls out, and it is the right ordering.** Required hepatic factor:
   pemafibrate (91.6×) > elafibranor (42.7×) ≈ fenofibric acid (37.5×) > seladelpar on
   PPARδ (1.5×). Pemafibrate is marketed precisely as the selective PPARα **modulator**
   with enhanced hepatic targeting, and it comes out as the most
   hepatic-concentration-dependent of the four. **That ordering was not put into the
   model.** No hepatoselectivity parameter exists anywhere in the code.
3. **The transporter that would do it is measured, and measured absent from retina.**
   MEASURED this step, bulk nTPM:

| Gene | Liver | Retina | Retina percentile |
|---|---:|---:|---:|
| **SLCO1B1** (OATP1B1) | **502.3** | **0.0** | 9.2 |
| **SLCO1B3** (OATP1B3) | **247.7** | **0.0** | 9.2 |

   In retinal vascular endothelium specifically, SLCO1B1 is 0.4 nCPM and SLCO1B3 is 0.0.

**So the mechanism that makes a fibrate a drug is the mechanism that denies it the
eye.** These compounds are not under-dosed for the retina; they are correctly dosed for
a tissue that concentrates them 40–90× and the retina is not that tissue. Raising the
dose does not fix a missing transporter, in the same way that §5 of the FGF21 bridge
found no plasma concentration fixes a missing co-receptor.

> **What I did not verify.** I did not pull a measured hepatic Kp,uu for any fibrate
> specifically. The 37–92× figures are the model's *prediction*, independently testable
> against sandwich-cultured human hepatocytes, and the support above is the mechanism,
> the contrast case and the ordering — not a matching literature value. That is an
> identifiable follow-up, and the inference rests on the ordering and the expression data
> more than on the absolute number.

---

## 11. PER-COMPOUND VERDICT

Margins at Cavg,ss, median [95% CI]:

| Compound | Receptor | Cu plasma | Free EC50 | Endothelium | RPE | Neural retina | P(endo ≥ 1) |
|---|---|---:|---:|---|---|---|---:|
| Fenofibric acid | PPARα | 160.2 nM | 6,113 nM | 0.0084 [6.8e-4 – 0.110] | 0.027 [9.9e-4 – 0.736] | 0.0016 [8.7e-5 – 0.027] | 0.000 |
| Pemafibrate | PPARα | 0.0025 nM | 0.241 nM | 0.0035 [2.0e-4 – 0.058] | 0.011 [3.1e-4 – 0.373] | 0.0012 [1.3e-5 – 0.043] | 0.000 |
| Elafibranor | PPARα | 1.22 nM | 52.5 nM | 0.0074 [1.8e-4 – 0.326] | 0.024 [3.1e-4 – 1.85] | 0.0034 [3.5e-5 – 0.226] | 0.005 |
| GFT1007 | PPARα | 3.87 nM | 52.5 nM | 0.024 [5.4e-4 – 1.09] | 0.075 [9.4e-4 – 6.12] | 0.0055 [4.8e-5 – 0.463] | 0.028 |
| Elafibranor **+ GFT1007** | PPARα | — | — | **0.031** [7.2e-4 – 1.42] | 0.098 [1.3e-3 – 7.96] | 0.0090 [8.5e-5 – 0.689] | 0.038 |
| Elafibranor **+ GFT1007**, at **Cmax** | PPARα | — | — | **0.136** [3.5e-3 – 5.67] | 0.430 [6.1e-3 – 32.4] | 0.041 [4.1e-4 – 2.90] | 0.147 |
| Seladelpar | **PPARδ** | 0.242 nM | 0.378 nM | **0.210** [0.014 – 3.26] | **0.667** [0.021 – 21.3] | 0.047 [6.9e-4 – 1.73] | 0.135 |
| Seladelpar | PPARα | 0.242 nM | 283.8 nM | 2.8e-4 [1.9e-5 – 4.3e-3] | 8.9e-4 [2.8e-5 – 0.028] | 6.3e-5 [9.2e-7 – 2.3e-3] | 0.000 |

Dose multiple required to reach margin 1 at the endothelium, at Cavg:

| Compound | Labelled dose | Median fold increase needed | 95% CI |
|---|---|---:|---|
| Fenofibric acid | 135 mg/d | **119×** | 9 – 1,480× |
| Pemafibrate | 0.2 mg/d | **290×** | 17 – 4,930× |
| Elafibranor | 80 mg/d | 135× | 3.1 – 5,620× |
| GFT1007 | (same) | 42× | 0.92 – 1,870× |
| **Seladelpar (PPARδ)** | 10 mg/d | **4.8×** | 0.31 – 71× |
| Seladelpar (PPARα) | 10 mg/d | 3,570× | 230 – 53,500× |

**Fenofibric acid — fails, by ~120× at the labelled dose.** The compound the DR clinical
evidence actually rests on has the weakest intrinsic potency in the set (median EC50
15 µM across 13 determinations, with five censored records saying no activity below
10 µM). Its clinical benefit in FIELD and ACCORD-Eye is not explained by local retinal
PPARα engagement at any plausible setting of this model, and that conclusion is robust
across all 23 inputs.

**Pemafibrate — fails worst, and fails for an informative reason.** Its 15,000-fold
potency advantage over fenofibric acid is almost exactly cancelled by a 19,000-fold lower
plasma concentration (0.27 ng/mL at the labelled dose). It is the most
hepatic-concentration-dependent of the four (required liver Kp,uu 91.6×) and the retina
has none of the transporter that provides it. **A more selective PPARα agonist is a
worse retinal drug, not a better one**, and the selectivity that makes it safer in the
liver is the thing that makes it inert in the eye.

**Elafibranor — fails, best of the PPARα three.** Only because its active metabolite
carries 3.2× the parent's exposure; the combined endothelial margin is 0.031 at Cavg and
0.136 at Cmax, against the parent's 0.0074 and 0.038. P(margin ≥ 1) = 0.038 at Cavg and
0.147 at Cmax — a 4-15% chance, which is not a programme. **Caveat:
GFT1007's own EC50 is not separately determined in the ChEMBL record and is modelled as
equipotent with the parent, so 0.031 is an upper bound if the metabolite is weaker.**

**Seladelpar — the only one within reach, and not on the receptor under discussion.** At
Cmax its endothelial margin on PPARδ is 0.558 [0.038 – 8.59] and at the RPE 1.77, with
P(margin ≥ 1) of 0.34 at the endothelium and 0.62 at the RPE. A 4.8× dose increase would put the median at 1. The
reason is structural: seladelpar needs a hepatic concentration factor of only **1.5×**,
so its free plasma concentration is already near its free EC50 and it is not relying on a
transporter the retina lacks. On PPARα it is 1,340× short and irrelevant.

---

## 12. WHAT WOULD CHANGE THE VERDICT

In sensitivity order, which is not the order the programme has been using:

1. **A PPARα/δ EC50 panel at stated protein concentration.** All four compounds, one
   laboratory, one assay, with medium albumin measured and reported — plus a parallel arm
   at physiological (40 g/L) albumin. This removes the single largest variance
   contributor in the two compartments that face the blood. Cell culture; weeks; no
   animal. **If the free EC50s come back 10× below the corrected values here, elafibranor
   and seladelpar reach parity at the endothelium and the verdict on those two is
   withdrawn.**
2. **Equilibrium dialysis for mouse fenofibric acid plasma binding**, and a measured
   shake-flask logP for all four. Both are days of work and together they carry ST ≈ 0.21
   in the neural retina.
3. **Re-analysis of Huang 2021's samples with retina and vitreous separated**, which
   removes the pooling inversion (§3) and would narrow the anchor directly. Cheaper than
   a new study if the tissue is banked.
4. **The oral-dosing ocular PK study.** Still the only thing that settles the
   neural-retina barrier block, and still worth doing — but it is third or fourth on
   variance, and on its own it would leave 43% of the neural-retina variance and 69% of
   the endothelial variance standing.
5. **An efflux-substrate assay** for the four compounds against ABCB1, ABCG2, ABCC4 and
   ABCC5 (`barrier.efflux_rel`, ST 0.037). Low variance share but it converts a 25-fold
   prior into a measurement, and it is a standard vesicle assay.

**The experiment that would most change the framing, as opposed to the numbers:**
measure whether human RPE's OAT1/OAT3 take up any of these four. The RPE is the only
compartment that can exceed plasma free concentration, its OAT3 is at 464.7 nCPM, and the
model's prior on its net direction spans a hundred-fold because nobody has looked. If
the RPE concentrates these acids, the compartment ordering in this note inverts.

---

## 13. FILES AND REPRODUCTION

**New code** — `src/analysis/ocular_exposure/`

| Module | Role |
|---|---|
| `parameters.py` | Every input as a `Param` with distribution and provenance tag. Inverse-CDF based, so Sobol sampling works; no scipy dependency |
| `compounds.py` | The five molecules (four plus GFT1007), PK from FDA labels, with the Cavg derivation shown |
| `ionisation.py` | Henderson-Hasselbalch: logD(7.4), neutral fraction, pH partition |
| `binding.py` | Free-fraction arithmetic and the serum correction on a published EC50 |
| `potency.py` | EC50 distributions from the repository's ChEMBL pull, censored records handled separately |
| `barrier.py` | The compartment model and the calibration inversion of the Huang anchor |
| `anchors.py` | External calibration set: measured human aqueous-humour partition, converted to Kp,uu |
| `model.py` | 23-input Monte Carlo; margins per compartment |
| `sensitivity.py` | Saltelli/Jansen Sobol indices, per input and per block |
| `report.py` | Produces every table in this note |

**Modified**

- `src/analysis/retina_expression/gene_panel.py` — added a `barrier_transport` class
  (15 genes: ABCB1/G2/C1/C4/C5, SLC22A6/8/11, SLCO1A2/1B1/1B3/2B1/3A1/4A1, SLC16A1),
  with the rationale in the module docstring.
- `src/analysis/retina_expression/hpa.py` — **bug fix.** The per-gene JSON cache was
  poisoned by truncated downloads: the sandbox egress proxy cuts some responses mid-body,
  curl exits 0, a short file lands in the cache, and every later run then fails to parse
  it. The failure is sticky because the bad file looks like a cache hit. Now the payload
  is parsed before being trusted, and a short read is deleted and retried. **This is the
  same class of failure Step 3 reported as "the HPA v23 `normal_tissue.tsv` download
  returned a non-zip payload"**, and with the fix in place that file regenerated too.

**Regenerated** — `data/processed/retina_hpa_bulk_ntpm.tsv` (236 rows, up from 207),
`data/processed/retina_hpa_celltype_ncpm.tsv`,
`data/processed/retina_hpa_antibody_reliability.tsv` (118 rows — **not** produced by
Step 3).

**New data** — `data/processed/ocular_exposure_margins.tsv` (36 rows: compound ×
receptor × exposure × compartment, with medians, bounds and P(margin ≥ 1)).

```bash
venv/bin/python -m src.analysis.ocular_exposure.report            # everything above
venv/bin/python -m src.analysis.ocular_exposure.report --quick    # smoke test, ~2 s
venv/bin/python src/analysis/retina_expression/hpa.py --work-dir $TMPDIR/hpa
```

### Not done

- **No measured pemafibrate plasma protein binding** was found in any accessible source.
  §8 shows the margin is insensitive to it; the gap is real nonetheless.
- **No measured pKa or logP** for any of the four. pKa is anchored on the parent acids
  and cross-checked against the brief's own logD figure (§5); logP is ChEMBL `alogp`
  with a ±0.7 log error term. `compound.logp` is the second-ranked input in the neural
  retina, so this is a real limitation and not a footnote.
- **No measured hepatic Kp,uu for any fibrate.** §10's 37–92× figures are the model's
  prediction, supported by mechanism, contrast case and ordering, not by a matching
  literature value.
- **GFT1007's EC50 is not separately determined**; it is modelled as equipotent with the
  parent, making the combined elafibranor margin an upper bound.
- **No protein-level transporter measurement.** §2 and §10 are mRNA. For an
  endothelium-restricted transporter, bulk nTPM understates abundance badly, which is why
  the single-cell arm is quoted alongside — but both are HPA, i.e. one consortium.
- **The Huang anchor is one experiment, in mouse, at one time point, after IP rather than
  oral dosing.** Every one of those is a limitation, and the late-time-point bias is the
  only one carried as an explicit parameter.
- `barrier.rpe_net` spans a hundred-fold because the RPE's net anion transport direction
  is unmeasured. The RPE margins in §11 are correspondingly the least trustworthy numbers
  in this note.

---

## 14. EFFECT ON `REPORT.md`

**`REPORT.md` has already been rewritten since the 2026-10-05 original** (see
`docs/notes/dr-report-changelog.md`), and its current §4.2 reaches this same anchor
independently. Checked at run time rather than taken from an earlier step's report, as
the chain requires. The partition ranges this step was asked to replace are no longer the
live text; what is live is a different calculation, and it disagrees with this model by
two orders of magnitude. That disagreement is worth resolving in full.

### 14.1 Reconciling §4.2's 6.0× with this model's ~600×

`REPORT.md` §4.2 states:

```
0.140 ± 0.044 ng/mg  =  140 ng/g  =  439 nM total fenofibric acid   (range 301 – 577 nM)
measured human PPARα EC50, pChEMBL 5.58                =  2,630 nM
                                        ratio  =  6.0× below   (range 4.6 – 8.7×)
```

This model puts fenofibric acid ~600× below its free PPARα EC50 in the neural retina. The
gap between 6× and 600× is fully accounted for by three steps, two of which `REPORT.md`
flags itself:

1. **A dropped unit step — `ng/mg protein` is not `ng/mg tissue`.** Huang 2021 reports
   "ng/mg **of total protein**". The conversion `0.140 ng/mg = 140 ng/g` applies only the
   mg→g factor, which is the arithmetic for a per-tissue-mass measurement. Converting a
   per-protein figure needs the tissue's protein content: neural retina is ~10% protein
   by wet weight, i.e. ~100 mg protein per g, so

   ```
   0.140 ng/mg protein × 100 mg protein/g tissue = 14 ng/g  =  43.9 nM total
   ```

   not 140 ng/g / 439 nM. **A factor of 10, in the optimistic direction.** The conclusion
   is robust to the protein fraction: even at an implausible 20% protein the figure is
   28 ng/g, still 5× below 140.
2. **EC50 selection.** 2,630 nM (pChEMBL 5.58) is the **lowest** of the 18 PPARα records
   for fenofibric acid in the repository's own ChEMBL pull — a TR-FRET co-activator
   recruitment assay. The median of the 13 uncensored determinations is **15,000 nM**, and
   five further records are censored at >10,000 nM, i.e. they report no activity where
   this value sits. Taking the minimum of a distribution as its value is worth a further
   **5.7×**, also in the optimistic direction. §6.
3. **Total versus free, which `REPORT.md` states rather than hides.** Its caveat 3 reads:
   "Retinal tissue binding is unmeasured… if intracellular binding is comparable, the free
   concentration is one to two logs lower."

**The two analyses agree once step 3 is actually applied.** 6.0× ÷ 10 ÷ 5.7 = 0.105×,
i.e. ~9.5-fold below — and then `REPORT.md`'s own "one to two logs" for the free
correction puts it at 95–950× below, which brackets this model's 600×. This note does not
overturn §4.2 so much as carry out the corrections §4.2 lists and declines to make.

> **To be fair to §4.2 on the point it was careful about:** it explicitly frames 6.0× as a
> "consistently uncorrected" total-against-nominal comparison and names the free-versus-
> nominal double-count as "the error this comparison avoids rather than commits". That
> framing is right, and §8 here quantifies that double-count at 2.3–5.2× rather than the
> assumed one log. The disagreement is with the unit step and the EC50 selection, not with
> the framing.
>
> **And one point against this model:** a total-tissue-against-nominal-EC50 comparison is
> not actually internally consistent either, because the two binding capacities differ by
> orders of magnitude — retinal tissue protein is ~100 mg/g against 1% FBS albumin at
> ~0.4 mg/mL. Neither comparison is clean; this one is clean *by construction*, because
> `binding.py` removes the protein term from both sides explicitly.

### 14.2 Dispositions

| Claim | Disposition |
|---|---|
| §4.2 "`0.140 ng/mg = 140 ng/g`" | **Corrected to 14 ng/g.** Per-protein, not per-tissue-mass. 10×, optimistic |
| §4.2 "6.0× below (range 4.6–8.7×)" | **Superseded.** ~600× below free EC50 in neural retina, ~100× at the endothelium. §14.1 reconciles the two |
| §4.2 EC50 of 2,630 nM | **Replaced by the distribution.** Median 15,000 nM over 13 determinations, GSD 2.50, plus 5 censored records at >10,000 nM |
| §4.4 "No parameterised ocular exposure model has been constructed… which input dominates output variance is unanswered" | **Closed.** `src/analysis/ocular_exposure/`, 23 inputs, Sobol indices in §9 |
| §4.4 "the measured logD column is empty for all 3,276 drug records" | **Confirmed, with the cause.** `logd` 0 non-null of 3,276. Not a scraper fault: ChEMBL's API no longer serves `cx_logd` / `cx_most_apka` for any of these compounds. §5 |
| §4.4 "No measured free fraction in retinal tissue, for any fibrate" | **Confirmed.** Carried as `anchor.fu_tissue_retina`, 0.15–0.80, ST 0.016 — low variance share, so not the priority it looks like |
| §2.3 "measured pharmacokinetics: none" | **Partly closed.** One systemic-dosing ocular measurement exists (mouse, IP) and is now the model's calibration anchor. Human oral ocular PK remains unmeasured |
| §4.4 "No measured partition ratio" | **Still true as a measurement; now derived.** Kp,uu = 0.059 [0.009 – 0.354] from the one systemic ocular concentration that exists |
| Original partition ratio 0.2–0.7 for endothelium and RPE | **Wrong in structure, near-right in magnitude.** Neither compartment is behind a barrier; ceiling 1.0, not 0.7, and the reason for being below it is efflux. §2 |
| Original partition ratio 0.01–0.15 for neural retina | **Confirmed, and now derived**, with the upper bound 3.6× above the asserted ceiling |
| "Three mutually exclusive programmes depend on which end of those ranges is right" | **Dissolved.** All three compartments fail for every PPARα compound at every setting of the range |
| Free retinal drug concentration as the critical-path unknown | **Demoted.** 19% of variance at the endothelium and RPE; the EC50 and its assay protein concentration carry 69%. §9 |
| §4.1 "3.4× penalty for fenofibric acid" as an argument for dosing the acid | **Untouched, but it is a route comparison, not a partition ratio** — it carries no information about the blood-to-retina ratio. Step 4 made the same substitution; §3 |
| Fibrate benefit in FIELD / ACCORD-Eye | **Untouched and still unexplained.** This note removes local PPARα engagement as an explanation at the labelled dose; it does not remove the observation |
| Pemafibrate as the more attractive PPARα agonist | **Reversed for this indication.** Highest potency, lowest retinal margin, most dependent on a hepatic transporter the retina does not express. §10 |
| PPARδ agents as a secondary consideration | **Promoted.** Seladelpar is the only compound of the four within ~2–5× of local engagement, because it alone does not need a hepatic concentration step |

---

## Status — 2026-11-09 — step 5: replace the estimated retinal exposure with a parameterised model

**Done.** Built `src/analysis/ocular_exposure/` — a 23-input Monte-Carlo exposure model
for the fibrate chemotype, calibrated rather than asserted, with every input carrying a
distribution and a MEASURED / CONVERTED / ASSUMED tag enforced in code.

**Verdict: local PPARα engagement is not achievable for any of the four at any labelled
dose.** Endothelial margins at Cmax: fenofibric acid 0.020, pemafibrate 0.027,
elafibranor + GFT1007 0.136, seladelpar on PPARα 0.00074. Dose multiples required:
119× / 290× / 135× / 3,570×. **Seladelpar on PPARδ is the sole exception** —
margin 0.558 at Cmax, 4.8× dose short, P(margin ≥ 1) = 0.34.

**Verified three ways.** (1) The calibrated neural-retina Kp,uu, 0.059 [0.009–0.354],
lands inside the previously asserted 0.01–0.15 band but from the one measured systemic
ocular concentration that exists. (2) Independent external anchors — human
aqueous-humour partition for aciclovir, levofloxacin and pefloxacin, converted to
free/free — give Kp,uu 0.41–1.27 for non-efflux-substrate drugs, an order of magnitude
above the model's value for an anionic fibrate, which is the expected direction given the
measured efflux machinery. (3) Run backwards against the known clinical lipid effect, the
model demands a hepatic concentration factor of 37–92× and **orders the four compounds by
their known hepatoselectivity, with no hepatoselectivity parameter in the code**.

**A third correction, to the live `REPORT.md`.** Its §4.2 has already been rewritten to
use this same Huang 2021 anchor and reports fenofibric acid as **6.0× below** its EC50.
Two optimistic steps account for most of the distance to this model's ~600×: the
conversion `0.140 ng/mg = 140 ng/g` treats a per-**protein** measurement as per-tissue-mass
and so overstates retinal concentration **10×** (neural retina is ~10% protein by wet
weight, giving 14 ng/g), and the EC50 used, 2,630 nM, is the **lowest** of 18 PPARα
records against a median of 15,000 nM over 13 determinations — a further **5.7×**. Apply
those two and then §4.2's own stated "one to two logs" for the free-drug correction, and
the two analyses agree. §14.1 sets this out in full, including the point where §4.2 was
right and this model is not cleaner than it claims.

**Two corrections to earlier steps.** Step 4's recommendation to anchor the partition
prior on Huang 2021's IP-vs-topical ratio is wrong — that is a route comparison, not a
partition coefficient; the right anchor is retina:plasma within the IP arm. And a sticky
cache bug in `hpa.py` (truncated proxy responses cached as valid JSON) is fixed, which
also regenerated the `retina_hpa_antibody_reliability.tsv` that Step 3 reported as
failed.

**For the next step.**
1. **The sensitivity result reorders the programme.** At the endothelium and RPE the
   EC50 plus its assay protein concentration carry 69% of the variance and the partition
   ratio 19%. The highest-value next experiment is a PPAR EC50 panel at stated
   physiological albumin, not an ocular PK study. §12 ranks all five.
2. **Step 6 should use `src/analysis/ocular_exposure/` for its physicochemical filter**,
   as that step's own text requires. The relevant structural finding for it: passive
   permeability cancels out of a steady-state partition ratio, so a neutral LXR ligand's
   advantage over an acid is **not** mainly permeability — it is (a) not being a substrate
   for the measured anion pumps and (b) not depending on hepatic OATP uptake for its
   potency. `barrier.py` encodes that distinction.
3. **New measured result for Step 6 and 7:** human retinal vascular endothelium expresses
   ABCB1 507 nCPM, ABCC4 178, ABCG2 142 — each above hepatocyte — and human RPE expresses
   OAT3 465 and ABCC5 823. Any candidate from the GNN ranking should be filtered against
   these, and the RPE's concentrative uptake transporters are an opportunity, not only a
   liability.
4. **Open and unresolved:** pemafibrate's plasma protein binding (no accessible
   measurement anywhere), measured logP and pKa for all four, GFT1007's own EC50, and
   whether human RPE OAT1/OAT3 take up any fibrate — the last of which would invert the
   compartment ordering in this note.
