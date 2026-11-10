# Diabetic Retinopathy — Data Gap Closure

**Date** 2026-11-02
**Scope** Closing the four data gaps identified in
`data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md` §2.3
**Status** Three gaps closed, one closed in part. Two upstream sources have become
access-gated since the original scrapers were written.

---

## SUMMARY

The 2026-10-05 DR analysis concluded that essentially every quantitative claim it made was
reasoning rather than measurement. That was accurate. This note records what measurement is
now available, what remains unavailable, and which specific claims in REPORT.md the new data
supports, corrects, or leaves untouched.

| Gap (REPORT.md §2.3) | Status | Headline |
|---|---|---|
| `chembl_drug_metabolism.csv` corrupt | **Closed** | 10,000 fabricated rows → 1,433 verified rows; root cause fixed with two regression guards |
| Zero gene–disease associations for DR | **Closed via substitute** | 9,931 scored associations across 6 diabetic complications. DisGeNET itself is now key-gated |
| No drug–target affinity | **Closed** | 62,219 measured affinities vs. 23 previously; 16,407 on the PPAR receptors alone |
| Panel blind to PPARα effectors | **Closed; result is mostly negative** | Panel extended 27 → 43 genes. Only 7 of 16 effectors have any compound measured at ≤1 µM; 6 have no ChEMBL target at all |

**The single most consequential finding is negative.** The PPARα *effector* programme — the
genes that would demonstrate local transactivation in the retina — is nearly absent from both
new datasets. That is discussed in §6, including why it is *not* independent confirmation of
the report's conclusion.

---

## GAP 1 — Metabolism scraper bug

### What was wrong

`src/scrapers/chembl/chembl_scraper.py` requested
`/metabolism?molecule_chembl_id={id}`. The ChEMBL metabolism endpoint does not support
`molecule_chembl_id`. It does not reject the unknown filter — it **silently ignores it and
returns unfiltered page 1**, every call.

Verified against the live API:

| Query | `total_count` |
|---|---|
| `metabolism.json?molecule_chembl_id=CHEMBL417` | 2,147 — the entire table |
| `metabolism.json?drug_chembl_id=CHEMBL417` | 7 |

The writer then took `drug_chembl_id` from the response and `drug_name` from the loop
variable, pasting an unrelated drug's name onto every record. Row 1 of the old file asserted
that **prazosin metabolises epidoxorubicinol**.

### What was closed

| | Before | After |
|---|---|---|
| Rows | 10,000 | 1,433 |
| Distinct underlying records | 921 | 1,363 |
| Distinct drugs | 1 real / 10 names | 185 |
| Distinct pathway IDs | 3 | 4 |
| Rows where response ID ≠ requested ID | ~all | **0** |

Row 1 is now nicotine → nicotine-N-oxide via flavin-containing monooxygenase 3, which is
correct pharmacology. The row-count *drop* is the correct outcome: ChEMBL holds only 2,147
metabolism records in total, and only a subset belong to approved drugs.

Three guards were added:

1. **Startup sentinel** — if a filtered query's `total_count` equals the unfiltered
   `total_count`, raise immediately. This is the signature of the filter being ignored and
   catches this exact bug class on any future endpoint change.
2. **Per-record assertion** — records whose `drug_chembl_id` ≠ the requested ID are dropped
   and counted; >50% mismatch raises.
3. **Post-write check** — distinct drug IDs mapping to identical record sets are
   investigated rather than assumed corrupt. All 8 such groups in the current data are
   salt/ester siblings sharing a `molecule_hierarchy.parent_chembl_id` (diclofenac ×4 →
   CHEMBL139; erythromycin ×3 → CHEMBL532; plus six salt pairs), which legitimately share
   metabolism citations. These warn. Groups with *differing* parents, or any group of ≥10
   IDs, raise.

A failed parent lookup reports `INCONCLUSIVE` and explicitly states it is not evidence of
corruption — an unreachable API must never be reported as bad data. Run the check alone with
`--check-metabolism-only`.

A second, pre-existing defect was fixed in the same writer: values were passed through
`escape_csv_field` *and* `csv.DictWriter`, double-escaping them. The old file's parsed
`substrate_name` was literally `"Epidoxorubicinol, 4'-epiadriamycinol"` — quote characters
included. Now 0 double-escaped values.

### What was not closed

The same double-escaping affects **every other ChEMBL output** in `data/processed/`
(indications, warnings, targets, bioactivities, natural products, toxicity). Those writers
were deliberately left alone: fixing them requires re-scraping each table, which is a
separate job. **`chembl_drug_metabolism.csv` and the new `chembl_panel_*` files are clean;
the older ChEMBL CSVs are not.**

### Effect on REPORT.md

None directly — the DR analysis never used metabolism data. The relevance is methodological:
a silently-ignored filter produces data that looks complete and is entirely fabricated, and
nothing in the pipeline detected it for eleven months.

---

## GAP 2 — Gene–disease associations for DR

### The intended source is no longer open

DisGeNET moved behind a registered API key.
`api.disgenet.com/api/v1/gda/summary` returns **HTTP 401 "Missing or invalid API Key"**; the
legacy `www.disgenet.org/api/...` 301-redirects away. No key exists in this repo or
environment. The host is reachable, so a key would work immediately.

### What was closed

**The scraper was generalised as specified.** `src/scrapers/disgenet/disgenet_scraper.py` is
now parameterised by `--disease-slug`, `--disease-name`, `--disease-cui` and `--input`,
with an `--api` mode that reads `DISGENET_API_KEY` and exits 2 with an actionable message
when it is absent. Running with no arguments reproduces the original Oral Mucositis
behaviour exactly.

**A real latent bug was fixed in passing.** The original deduplicated on `PMID` alone, which
silently discarded every gene after the first for any multi-gene paper. Deduplicating on
`PMID + Gene + Disease_id + Association_Type` recovers **93 → 228 rows** — the legacy OM
dataset was missing 59% of its own associations, and every downstream OM analysis used the
truncated version.

**DR gene–disease data was obtained from Open Targets instead** — free, no key, and drawing
on substantially the same underlying evidence. New module
`src/scrapers/opentargets/opentargets_scraper.py`:

| Disease | Ontology ID | Associations |
|---|---|---|
| Diabetic retinopathy | MONDO_0005266 | 2,652 |
| Proliferative DR | MONDO_0001660 | 1,124 |
| Non-proliferative DR | EFO_0009760 | 336 |
| Diabetic macular edema | MONDO_0004728 | 469 |
| Diabetic kidney disease | MONDO_0005016 | 4,092 |
| Diabetic neuropathy | MONDO_0006626 | 1,258 |
| **Total** | | **9,931** |

Open Targets has no ontology term for "diabetic microvascular complications" (only
`EFO_0010977 macrovascular complications of diabetes` exists). The last three entries
operationalise the microvascular set as its three standard clinical endpoints — retina,
kidney, nerve. This is documented in the module.

### What was not closed

- **No DisGeNET data.** Only the code path. The scraper is ready; it needs a key.
- **Open Targets is not DisGeNET.** Scores are not interchangeable; `overall_score` is a
  weighted harmonic sum across datatypes, not a DisGeNET `gdaScore`. Do not mix them.
- **⚠ Indication leakage.** Open Targets `known_drug` and `clinical` datatype scores encode
  approved-indication and trial evidence. **Any future blinded run must drop those two
  columns** or the blind is void on the first row. The columns are emitted separately
  precisely so they can be dropped. This is flagged in the module and printed on every run.

### Effect on REPORT.md

§2.3 row "Gene–disease associations for DR: **None**" is no longer true. See §6 for what the
associations say about PPARα specifically.

---

## GAP 3 — Drug–target affinity

### What was closed

This gap is closed decisively.

| | Before | After |
|---|---|---|
| Bioactivity rows | 23 | **62,219** |
| Mechanism rows | 11 | 170 |
| `grep -ci ppar` in bioactivities | **0** | 16,417 |

New module `src/scrapers/chembl/chembl_target_axis.py` resolves gene symbol → UniProt
accession → ChEMBL target (filtering to `SINGLE PROTEIN` / *Homo sapiens*, which is
necessary — PPARA's accession also returns a SELECTIVITY GROUP and a PROTEIN FAMILY entry),
then pulls activities and mechanisms. Measured affinity on the three receptors:

| Receptor | ChEMBL target | Activities (filtered) | Compounds | Compounds ≤1 µM | Max pChEMBL |
|---|---|---|---|---|---|
| PPARA | CHEMBL239 | 5,271 | 3,622 | 1,644 | 10.59 |
| PPARD | CHEMBL3979 | 3,223 | 2,293 | 1,264 | 10.99 |
| PPARG | CHEMBL235 | 7,913 | 5,223 | 2,590 | 10.74 |

The fibrate / glitazone / glitazar class resolved without any hand-curation — they fall out
of the target queries. **Measured** max pChEMBL by receptor:

| Compound | PPARA | PPARD | PPARG |
|---|---|---|---|
| Pemafibrate | **9.00** | 5.80 | 5.96 |
| Elafibranor | 8.00 | 8.00 | 6.76 |
| Aleglitazar | 7.42 | 7.28 | 7.72 |
| Rosiglitazone | 8.40 | 5.44 | 9.00 |
| Seladelpar | 5.82 | **8.72** | — |
| GW501516 | 6.64 | **10.32** | 6.10 |
| Fenofibrate | 6.00 | — | 6.24 |
| **Fenofibric acid** | **5.58** | — | 4.00 |
| Bezafibrate | 5.15 | 4.72 | 5.52 |
| Gemfibrozil | 4.93 | — | 4.17 |
| Clofibrate | 4.26 | — | — |

### What was not closed

**Pharmacokinetics.** REPORT.md §2.3's fourth row — "Measured pharmacokinetics: None.
Distribution, permeability and bioavailability fields empty across all 3,276 drug records" —
**remains true**. ChEMBL does not hold tissue distribution data. The report's central claim
stands untouched: *free drug concentration in retinal tissue has never been measured in any
species*, and every exposure argument in the analysis still rests on estimated partition
ratios. Nothing in this work changes that.

### Effect on REPORT.md

**§5.3 "Potency does not buy engagement" — overstated, conclusion intact.** The report
claims pemafibrate is "~5 orders of magnitude more potent than fenofibric acid." Measured:

- Best-vs-best: 9.00 vs 5.58 = **3.4 log units (~2,600×)**
- Median-vs-median: **4.5 log units (~30,000×)**

So "~5 orders" is defensible at the median and overstated by more than an order of magnitude
at best-measured. *Caveat: pemafibrate has only n=3 measurements in ChEMBL, all EC50. This is
thin and should not be over-read.* The report's actual argument — that a ~4-order deficit in
free circulating concentration cancels most of the potency advantage — survives, with the
real margin now bounded by data rather than assumed.

**NEW — the top-ranked lead fails a conventional activity threshold at its own target.**
Fenofibric acid's best measured PPARA affinity is pChEMBL **5.58 (~2.6 µM)**, below the
standard ≤1 µM cut. Fenofibrate (6.00), pemafibrate (9.00) and elafibranor (8.00) pass;
fenofibric acid and seladelpar (5.82) do not. This does not overturn the ranking — the report
ranked on *certainty of hepatic engagement*, not potency, and hepatic portal concentrations
are high enough that a micromolar EC50 is engaged in liver. But the margin is thinner than
a #1 ranking implies, and this number was not available when the ranking was made.

**§3.1 "The natural products collapsed" — confirmed and strengthened.** See §5.

---

## GAP 4 — The effector panel

### What was closed

`data/processed/dr_gene_panel.csv` extends the panel from **27 → 43 genes**, verified as an
exact superset of the original 27. The 16 additions are the PPARα transcriptional programme:
ANGPTL4, FGF21, LPL, APOA1, APOA5, ABCA1, ABCG1, CPT1A, ACOX1, ACADM, EHHADH, HMGCS2, PDK4,
FABP1, FABP4, FABP5.

Each gene is annotated with the **limb of REPORT.md §1.2 it discriminates**, so the panel
tests the report's own framing rather than merely adding rows: limb 1 lipoprotein supply,
limb 2 humoral relay, limb 3 local transrepression, limb 4 local transactivation.

### The matrix could not be rebuilt on its original source

CTD is now captcha-gated: `ctdbase.org/tools/batchQuery.go` 302-redirects to a captcha for
every format and report combination. A like-for-like rebuild is impossible.

This is not much of a loss. The original matrix's own header warns that its counts measure
study volume, not pharmacology (r = 0.911 between a source catalogue's size and its hit
count). Rebuilding from CTD would have reproduced that artifact. The matrix was instead
rebuilt on **measured ChEMBL affinity**, which is what the task required — real binding
data, not class pharmacology. Three outputs, each with a header block stating what the
numbers do and do not mean:

- `data/processed/dr_compound_target_matrix.tsv` — 38,818 compounds × 43 genes
- `data/processed/dr_matrix_legacy_compound_comparison.tsv` — all 153 original compounds, CTD count vs. measured binding
- `data/processed/dr_panel_coverage_summary.tsv` — per-gene druggability

Counts are reported both ungated and gated at pChEMBL ≥ 6 (≤1 µM). The gate matters: 4,110
activities are weaker than 10 µM, and counting those equally with sub-nanomolar binders would
repeat the exact evidence-quality error the original matrix was criticised for.

The 2026-10-05 report directory was not modified. It is a dated historical artifact.

### What was not closed — and this is the finding

**Most of the effector programme is not druggable and barely measured.**

| | of 16 effectors |
|---|---|
| Resolve to a ChEMBL target | 10 |
| Have ≥1 activity surviving validity filters | 8 |
| Have ≥1 compound measured at ≤1 µM | **7** |

Six have **no ChEMBL target at all**: ANGPTL4, FGF21, APOA5, ABCG1, EHHADH, HMGCS2 —
including both genes carrying the report's two load-bearing mechanistic arguments. ACADM's
sole measurement is a Kd of 185,710 nM flagged "Outside typical range" and is correctly
dropped.

This is expected for transcriptional *outputs* — they are readouts, not drug targets — but it
means the panel cannot be interrogated by compound-binding data the way the receptors can.
**Measuring the effector limb requires expression data, not affinity data.** That is a
different acquisition problem than the one this work solved.

---

## 5. WHAT THE NEW DATA DOES TO §3.1 (the quercetin collapse)

The report's most striking methodological result was that quercetin ranked first on raw
target coverage (26 of 27 genes) and finished last after the traditional-medicine agent ran
a null model. The measured data confirms this emphatically.

| Quercetin | Value |
|---|---|
| CTD count, 27-gene panel | **26** |
| ChEMBL genes bound, 43-gene panel, ungated | 4 |
| ChEMBL genes bound at ≤1 µM | **3** (AKR1B1 7.83, MMP9 6.76, KDR 6.55) |
| PPARα effector genes bound at ≤1 µM | **0** |
| PPARG | 4.58 — ~26 µM, not meaningful |

Across the full legacy set the collapse is general:

- **15 of 153** original compounds bind ≥1 panel gene at ≤1 µM.
- **3 of 153** bind any PPARα effector gene at ≤1 µM.
- Mean effector genes bound across the 152 matched compounds: **0.046**.

The CTD ranking and the affinity ranking are close to unrelated. §3.1 was right, and the
measurement now exists to say so rather than infer it.

One caution the file header states and which must not be dropped: a blank is not a zero.
Absence of a ChEMBL activity means *not measured in ChEMBL*, not *no interaction*. Unmatched
compounds carry empty cells, never 0.

---

## 6. WHAT THE NEW DATA DOES TO THE MECHANISM ARGUMENT

### PPARα has literature support for DR and no human genetic support

Position of the PPAR axis among 2,652 Open Targets DR associations:

| Gene | Rank | Overall | Genetic association | Literature |
|---|---|---|---|---|
| **PPARG** | **9** | 0.478 | **0.750** | 0.722 |
| **PPARA** | 66 | 0.339 | **none** | 0.231 |
| ANGPTL4 | 273 | 0.094 | none | 0.776 |
| FGF21 | 434 | 0.058 | none | 0.474 |
| PPARD | 1,883 | 0.004 | none | 0.030 |

**PPARα ranks 66th and carries no genetic association for DR.** Its signal is literature
only. The report selected PPARα on mechanistic grounds and was correct against the withheld
evidence, so this is not a refutation — but the human genetic evidence in this panel sits on
**PPARγ**, not PPARα, and the analysis never examined that.

This should be treated as hypothesis-generating, not as a finding. PPARγ's genetic score
most plausibly propagates from type 2 diabetes susceptibility (the Pro12Ala variant) rather
than from retinopathy specifically, and Open Targets propagates evidence across the disease
ontology. **Verifying whether PPARG's DR genetic signal is DR-specific or inherited from
parent diabetes terms is the single most useful follow-up query against this new dataset.**

### §5.4 (ANGPTL4 wrong-sign risk) — supported, and still not directly druggable

ANGPTL4 ranks 273rd with a **literature score of 0.776** — among the highest literature
scores in the panel, and higher than PPARA's own. The report's treatment of ANGPTL4 as a
serious mechanistic consideration was well-founded; this is a genuinely active area.

ANGPTL4 has **no ChEMBL target**, so it cannot be engaged by a small molecule directly. That
is consistent with, and strengthens, the report's conclusion that **plasma ANGPTL4 is a
mandatory, cheap biomarker** rather than a target. The recommendation is unchanged.

### §5.5 (FGF21 humoral relay) — real but modest

FGF21 ranks 434th, literature 0.474. The relay the debate round elevated to the
under-weighted limb has real published support for DR, though less than ANGPTL4's. No ChEMBL
target. The report's framing survives.

### Limb 4 (local transactivation) is empty in both new datasets — with a caveat

The fatty-acid-oxidation effectors are absent from the DR association set entirely:

| Gene | Open Targets DR | ChEMBL target |
|---|---|---|
| ACOX1 | not associated | yes (3 compounds ≤1 µM) |
| ACADM | not associated | yes (0 valid activities) |
| EHHADH | not associated | **none** |
| HMGCS2 | not associated | **none** |
| PDK4 | not associated | yes |
| CPT1A | rank 2,501 (0.0015) | yes (476 compounds ≤1 µM) |

REPORT.md §5.1 excluded limb 4 on exposure arithmetic — the drug never arrives at neural
retina in sufficient free concentration. The new data is **consistent** with that conclusion
but **does not independently confirm it**, and conflating the two would repeat precisely the
error this exercise exists to correct.

Both Open Targets and ChEMBL reflect *what has been studied*. A pathway nobody has
investigated in a disease is indistinguishable, in these datasets, from a pathway that is
genuinely uninvolved. The honest statement is: **no one has looked.** The report's exposure
argument remains the real basis for excluding limb 4; the data gap is a separate fact that
happens to point the same direction.

---

## 7. REPORT.md §2.3, RE-SCORED

| Needed | REPORT.md said | Now |
|---|---|---|
| Drug–target binding affinity | None. Zero PPAR content | **62,219 activities; 16,407 on the PPAR receptors** |
| Measured pharmacokinetics | None | **Still none.** Unchanged, and still the binding constraint |
| Gene–disease associations for DR | None. Only a legacy OM set | **9,931 associations across 6 diabetic complications** |
| PPARα effector genes in the panel | None | **Panel extended to 43 genes; 7 of 16 effectors have usable affinity data** |

"The pathway under study was invisible to the data used to study it" is no longer true of the
receptors. It remains true of the effector programme, and it remains true of exposure.

---

## 8. FILES

**Code**

| Path | Change |
|---|---|
| `src/scrapers/chembl/chembl_scraper.py` | Metabolism filter fixed; sentinel, per-record assertion, parent-aware post-write check; `--check-metabolism-only`; double-escaping removed |
| `src/scrapers/disgenet/disgenet_scraper.py` | Parameterised by disease; `--api` mode; PMID-only dedupe bug fixed |
| `src/scrapers/opentargets/opentargets_scraper.py` | New — Open Targets GraphQL, 6 diseases, leakage warning |
| `src/scrapers/chembl/chembl_target_axis.py` | New — gene → UniProt → ChEMBL target resolution, bioactivities, mechanisms |
| `src/analysis/dr_matrix/build_matrix.py` | New — binding-evidence matrix, pChEMBL-gated |
| `requirements.txt` | `openpyxl==3.1.5` added (required by the pre-existing DisGeNET scraper, never declared) |

**Data** — all under `data/processed/`

`dr_gene_panel.csv` (43 genes) · `chembl_drug_metabolism.csv` (regenerated) ·
`chembl_panel_targets.csv` · `chembl_panel_bioactivities.csv` · `chembl_panel_mechanisms.csv` ·
`chembl_ppar_compounds.csv` · `opentargets__{DR_only,PDR,NPDR,DME,DKD,DN,DR}_gene_disease.csv` ·
`dr_compound_target_matrix.tsv` · `dr_matrix_legacy_compound_comparison.tsv` ·
`dr_panel_coverage_summary.tsv` · `disgenet__OM_*.csv` (regenerated, 93 → 228 rows)

Not touched: `data/holdout/`, `data/processed-blinded-*/`, `data/reports/`.

---

## 9. WHAT TO DO NEXT

1. **Obtain a DisGeNET API key** (https://disgenet.com/). The scraper is ready.
2. **Drop `score_known_drug` and `score_clinical`** before any blinded re-run. These leak
   indication status.
3. **Resolve the PPARG genetic signal.** Determine whether its DR genetic association is
   DR-specific or propagated from parent diabetes terms. This is answerable from the data
   now on disk plus one Open Targets evidence query.
4. **Acquire expression data.** Affinity cannot interrogate a transcriptional programme.
   Testing the effector limb needs retinal expression datasets, not binding constants.
5. **Re-scrape the remaining ChEMBL tables** to clear the double-escaping, which still
   affects every other `chembl_*.csv`.
6. **The retinal exposure measurement is still the bottleneck.** Nothing here changes
   REPORT.md's conclusion that one unmade measurement stands between this target and a
   decision.

---

## Status — 2026-11-03 — step 2 follow-through

§9 item 4 of this note ("Acquire expression data. Affinity cannot interrogate a
transcriptional programme.") has been actioned. See
**`docs/notes/ppara-retinal-expression.md`**.

Two conclusions in this note are revised by it:

- **§6 "Limb 4 (local transactivation) is empty in both new datasets" — the caveat was
  right and the data now confirms it.** CPT1A, ACADM, ACOX1 and ABCG1 are expressed in
  10–54% of human retinal cells. Their absence from ChEMBL and Open Targets reflected what
  has been studied, not the biology. The honest statement in this note — "no one has
  looked" — holds, and someone has now looked.
- **§6 "ANGPTL4 … mandatory, cheap biomarker" — strengthened and localised.** ANGPTL4 in
  retina is a mural/endothelial transcript (pericytes 23.1%, smooth muscle 22.9%,
  endothelium 12.0%, photoreceptors ~1%), i.e. expressed in exactly the compartment where
  the wrong-sign permeability risk would act — and that compartment is PPARδ-dominant.

Unchanged: everything in §7 about exposure. Step 2 measured receptor expression, not drug
concentration.
