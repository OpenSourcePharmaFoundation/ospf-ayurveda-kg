# The FGF21 concentration bridge

**Step 3 of `docs/prompts/dr-solve-open-questions-prompt.md`.**
Date: 2026-11-03. Branch: `local-llm-subproject`.

---

## 0. VERDICT

**The relay fails.** Not marginally, and not only on arithmetic.

A fibrate raises human plasma FGF21 by **1.28–1.61×** over a diabetic baseline of
~550 pg/mL, reaching at most **~1,000 pg/mL**. Retinal protection has never been
demonstrated below a concentration equivalent to **~10,000 pg/mL** of native FGF21, and
the receptor-level EC50 is **22,620 pg/mL**. The achievable concentration is
**25× below the active concentration (95% CI 6–99×; 1.4 log, 95% CI 0.8–2.0 log)**, and
in 200,000 Monte-Carlo draws over the published spread of every input, the achievable
concentration reached the active concentration **zero times**.

Three independent findings make this worse than a pure arithmetic shortfall, and each
is a harder constraint than the ratio:

1. **Native FGF21 at 5 mg/kg twice daily — roughly 10⁴× endogenous — did not work.**
   In the one experiment that tested it, native hormone had no effect on retinal
   neovascularisation; only the 28-hour-half-life conjugate did (Fu 2017,
   PMID 28199833). A fibrate's +40% cannot do what 10⁴× of the native hormone failed
   to do.
2. **The human retina does not express the obligate FGF21 co-receptor.** KLB is
   **0.0 nTPM** in human retina (9th percentile of the retinal transcriptome) against
   16.6 nTPM in liver, while FGFR1 is abundant (retina 14.4 nTPM, 77th percentile;
   Müller glia 214 nCPM). FGF21 cannot signal through FGFR1 without β-Klotho. This is a
   **newly computed result** — §5 — and it is not a concentration argument at all. No
   plasma concentration fixes a missing co-receptor.
3. **The epidemiological sign is wrong.** In the only large human dataset linking
   plasma FGF21 to retinopathy — FIELD, n = 9,697 — higher FGF21 predicted *more*
   microvascular disease, and a larger *fenofibrate-induced* FGF21 rise predicted
   *faster* glycaemic progression (PMID 26055067, PMID 28606915).

**What this removes.** `REPORT.md` §5.5 ranked the hepatic-to-retinal FGF21 relay as the
best-evidenced limb. It is not evidenced; it is two literatures that never met. The
upstream half (fibrate → FGF21) and the downstream half (FGF21 → retinal protection)
are each real and each well-measured. They are separated by a factor of 25 in
concentration and by a missing receptor subunit.

**What survives.** The downstream retinal biology is real but is **adiponectin-mediated**,
and the retina expresses ADIPOR1 at the **98th percentile** of its transcriptome
(125.7 nTPM) while expressing KLB at the 9th. The route that is open is
liver → FGF21 → **adipose** (KLB-rich) → adiponectin → retina (ADIPOR1-rich). That is a
different mechanism with a different rate-limiting step, and the fibrate → adiponectin
leg in humans has never been quantified against a retinal readout. §8 specifies it.

---

## 1. WHAT WAS ASKED AND WHAT WAS DONE

The step asked whether anyone had checked that the two published halves of the relay
operate at the same concentration. They had not — with one partial exception that
matters and is recorded in §3.4: the pemafibrate investigators noticed the gap against
the FGF21-*analog* trials, stated it plainly, and did not pursue it to a retinal readout.

Everything below is either extracted from a named PMID or computed here. Every
quantitative claim carries one of three provenance tags, because conflating them is the
specific failure this chain corrects:

| Tag | Meaning |
|---|---|
| **MEASURED** | Read directly from a published result |
| **CONVERTED** | A measured value transformed by stated arithmetic (units, molarity). No new assumption |
| **ASSUMED** | A distribution chosen to span the published spread. Judgement; justified at the point of use |

---

## 2. THE UNIT TRAP THAT HAD TO BE CLEARED FIRST

Every retinal in-vitro result in this literature is reported as "ng/mL FGF21". It is
not FGF21. It is **PF-05231023**, a CovX-body: two modified FGF21 molecules
([dHis/Ala129Cys]FGF21) conjugated to the CVX-2000 humanised IgG1κ scaffold,
**2:1 stoichiometry, ~190 kDa total** (MEASURED, Pfizer/CovX characterisation).

Mature human FGF21 is **19.5 kDa** (MEASURED; UniProt Q9NSA1, mature chain 29–209).
The conjugate is therefore ~90% scaffold by mass. Reading "100 ng/mL FGF21" in a
retinal paper and "600 pg/mL FGF21" in a clinical paper as the same analyte
**overstates the retinal dose by a factor of ~5 in the wrong direction** — it makes the
gap look larger than it is.

CONVERTED, via moles:

```
100 ng/mL PF-05231023 ÷ 190,000 g/mol        = 0.526 nM conjugate
                        × 2 FGF21 arms        = 1.053 nM FGF21-equivalent
                        × 19,500 g/mol        = 20,526 pg/mL native-FGF21-equivalent
 50 ng/mL PF-05231023                         = 10,263 pg/mL native-FGF21-equivalent
```

Code: `src/analysis/fgf21_bridge/bridge.py::pf_to_fgf21_equiv_ng_ml`.

Correcting this trap **halves the apparent gap** and is the single reason the final
answer is 25× rather than 50×. It is also the reason the result is trustworthy: the
correction runs against the conclusion.

---

## 3. DATASET 1 — HUMAN PLASMA FGF21

### 3.1 Baseline, non-diabetic adults

| Cohort | Value (pg/mL) | Assay | Source |
|---|---|---|---|
| Healthy controls, n = 50 | 85.0 (IQR 53.9–131.8), median | not stated | PMC9047692 |
| Non-diabetic children/adults | ~99 (median) | not stated | PMC10411091 |
| Controls, n = 82 | 131.9 (IQR 44.8–236.3), median | BioVendor | PMC11509456 |
| Controls (Lin 2014) | 125.9 (mean) | not stated | via PMC5735335 |
| Healthy, n = 76 | **250-fold range across individuals** | Linco/Lilly | PMID 18680716 |

All MEASURED. Working range for a non-diabetic adult: **85–235 pg/mL** by study median.

The last row is the one that constrains everything: Gälman 2008 found serum FGF21
varied **250-fold among 76 healthy individuals**, unrelated to age, sex, BMI, lipids or
glucose. Any single-cohort "normal value" is a point on a very wide distribution.

### 3.2 Baseline, diabetes and diabetic retinopathy

| Group | Value (pg/mL) | Assay | Source |
|---|---|---|---|
| T2D, no DR | 326.8 ± 81.6 | Abcam ab222506 | PMC8016097, n = 654 |
| T2D, non-sight-threatening DR | 572.7 ± 79.5 | Abcam ab222506 | PMC8016097 |
| T2D, sight-threatening DR | 625.8 ± 83.7 | Abcam ab222506 | PMC8016097 |
| Whole T2D cohort, median | 450.5 (IQR 190.1–545.6) | Abcam ab222506 | PMC8016097 |
| T2D no DR / NPDR / PDR (Lin 2014) | 326.8 / 631.9 / 669.4 | not stated | via PMC5735335 |
| Hypertriglyceridaemic, 35.8% T2D | ~610 (baseline) | not stated | PMC8097867, n = 1,253 |

All MEASURED.

> **Data-integrity flag.** PMC8016097's "T2D, no DR" value (326.8) is **numerically
> identical** to Lin 2014's. These are presented as independent Chinese T2D cohorts.
> Either this is coincidence to four significant figures, or one reproduces the other.
> I could not resolve which from the open-access text. The two are therefore treated as
> **one** anchor, not two, in §6.

Working range for a diabetic adult with retinopathy: **450–670 pg/mL**.

### 3.3 Assay disagreement — handled explicitly, as asked

The step warned that FGF21 immunoassays disagree between platforms. They do, and the
disagreement is not separable from cohort differences in the published record. I did not
find a head-to-head method-comparison study for plasma FGF21 in the searchable
literature, so I bounded it empirically instead: across the kits appearing in the survey
above and in a 25-paper PMC sweep — **BioVendor, R&D Systems/Quantikine, Millipore,
Abcam, Eagle Biosciences, Phoenix, Antibody & Immunoassay Services (HKU)** — reported
**healthy-control medians span 85 to 235 pg/mL, a 2.8× spread**.

That 2.8× is the honest uncertainty on the numerator. It is carried into §6 as a wide
lognormal rather than being argued away. It is not, however, large enough to matter: a
2.8× assay uncertainty against a 25× shortfall does not change the verdict, and the
Monte-Carlo in §6 confirms that directly.

**A second, sharper assay problem — and the one that actually bites.** FGF21 is cleaved
in circulation at three proline residues: Pro-2 and Pro-4 by DPP-IV (N-terminal), and
**Pro-171 by fibroblast activation protein (FAP)** (MEASURED, PMID 26635356;
corroborated PMID 26797127, PMID 26962859). The C-terminus is the **β-Klotho-binding
determinant**. In a cohort of healthy volunteers, the relative abundance of
C-terminally-cleaved FGF21 was **10–34%** (MEASURED, PMID 26635356).

The potency cost of losing that C-terminus is large and measured: FGF21-dC10 (last 10
residues deleted) shifted the EC50 for ERK phosphorylation in human adipocytes by
**~50-fold** (MEASURED, PMC4218812).

Nearly all published FGF21 immunoassays are **total** assays. They therefore count a
10–34% fraction that is ~50× less potent as though it were active hormone. This is the
correct, quantified form of the step's "free versus total" objection — see §7.1.

### 3.4 On fibrate treatment

| Intervention | n | Duration | Effect on FGF21 | Source |
|---|---|---|---|---|
| Fenofibrate 200 mg/d, hypertriglyceridaemic non-diabetic | small | 2 wk | **+28%** | PMID 18680716 |
| GW590735 (PPARα) 20 µg/d, overweight/obese men | 6 | 2 wk | **+39%** | PMID 19531592 |
| GW501516 (PPARδ) 10 mg/d | 6 | 2 wk | +32% | PMID 19531592 |
| Rosiglitazone (PPARγ) | 10 | 2 wk | no change | PMID 19531592 |
| Fenofibrate, obese + T2D | 37 | 3 mo | "significantly increased" (magnitude not given) | PMID 19702724 |
| **Pemafibrate 0.4 mg/d** | 244 | 12 wk | **+369.5 pg/mL on ~610 baseline = +61%** | PMC8097867 |
| Fenofibrate 200 mg/d (FIELD run-in) | 9,697 | 6 wk | increase measured; **absolute values paywalled** | PMID 28606915 |

All MEASURED. Working range: **fold-change 1.28–1.61**, highest value from the largest
and most potent-agonist study. Maximum achieved absolute concentration across all of
these: **~1,000 pg/mL** (pemafibrate 0.4 mg/d; PMC8097867 states the range reached
"610.0 pg/mL to approximately 1000 pg/mL").

**FIELD is the gap in this table and it is the DR-relevant trial.** The Clin Chem 2017
paper measured plasma FGF21 before and after a 6-week fenofibrate run-in in 9,697 type 2
diabetic patients — by far the largest fibrate-on-FGF21 dataset in existence — and the
absolute concentrations are behind a paywall. What is public is the *direction*: see §9.

**The pemafibrate investigators made part of this comparison themselves** (PMC8097867,
Discussion):

> "After administration of an FGF21 analog, FGF21 blood levels were reported to be
> within a range of **17.5 to 150 ng/mL**. However, in our study, FGF21 blood levels
> ranged from 610.0 pg/mL to approximately 1000 pg/mL (= 1 ng/mL), even for pemafibrate
> 0.4 mg/day. **These results clearly did not reach the level achieved by the FGF21
> analog.**"

So the step's premise — "nobody has checked whether they are the same concentration" —
is *almost* right. Someone checked the fibrate against the analog trials and found a
17.5–150× gap. Nobody carried that forward to the retinal literature, which is where it
matters for this analysis, and nobody corrected for the conjugate mass (§2) or the
intact fraction (§3.3).

---

## 4. DATASET 2 — CONCENTRATION-RESPONSE ON RETINAL READOUTS

### 4.1 The literature is one laboratory

Every primary retinal FGF21 result below comes from the Smith laboratory at Boston
Children's Hospital, with the FGF21 analog supplied by Merck/Pfizer co-authors. This is
not a criticism of the work — it is consistent and well-controlled — but it means the
downstream half of the relay has **no independent replication**, and the concentrations
tested reflect one group's dosing choices.

### 4.2 In vitro — the only true concentration-response

| Preparation | Readout | Concentrations tested | Result | Source |
|---|---|---|---|---|
| Primary **human retinal microvascular endothelial cells** (HRMEC) | FITC-dextran permeability vs hVEGF 10 ng/mL | **50, 100 ng/mL** PF-05231023 | both protective | PMC7072824 |
| HRMEC | trans-endothelial electrical resistance | **100 ng/mL** PF-05231023 | TEER preserved | PMC7072824 |
| HRMEC | Claudin-1 protein | 100 ng/mL PF-05231023 | increased | PMC7072824 |

All MEASURED. CONVERTED to native-FGF21-equivalent (§2):

| As reported | FGF21-equivalent |
|---|---|
| 50 ng/mL PF-05231023 | **10,263 pg/mL** |
| 100 ng/mL PF-05231023 | **20,526 pg/mL** |

**No concentration below 50 ng/mL was tested.** The threshold for retinal endothelial
protection is therefore *unknown and ≤ 10,263 pg/mL FGF21-equivalent*. This is a real
limitation and it is the single most load-bearing uncertainty in the whole bridge — it
is handled in §6 by extending the lower tail of the active-concentration distribution to
5,000 pg/mL, well below anything ever tested.

I found **no** published concentration-response for FGF21 on Müller glia or RPE. The
Müller result that exists (PMC8079476) is an in-vivo mouse study in a retinitis
pigmentosa model, and reports a receptor-localisation finding (Fgfr1 in Müller
glia/astrocytes), not a concentration.

### 4.3 In vivo — and the experiment that decides this

| Model | Agent | Dose | Result | Source |
|---|---|---|---|---|
| Mouse OIR | **native FGF21** | **5 mg/kg, twice daily, i.p.** | **no effect on neovascularisation** | PMID 28199833 |
| Mouse OIR | PF-05231023 | 1 mg/kg daily i.p. | **suppressed** neovascularisation | PMID 28199833 |
| Vldlr−/− (RAP) | PF-05231023 | 0.5 mg/kg daily | lesions attenuated | PMID 28199833 |
| Laser CNV | PF-05231023 | 10 mg/kg every other day | lesions inhibited | PMID 28199833 |
| T1D mouse (ERG, OCT) | PF-05231023 | — | photoreceptor function restored | PMID 29487115 |
| VEGF-induced leakage | PF-05231023 | i.p. pre-treatment | leakage reduced | PMC7072824 |
| Phase-I-ROP model | FGF21 | — | physiological vascularisation promoted; **abolished in Apn−/−** | PMID 36943533 |

All MEASURED.

**The decisive line** (PMID 28199833, Results):

> "Native FGF21 with a short half-life (0.4 hours) **did not affect neovascularization**
> while administration of PF-05231023 with a biological half-life of 28 hours
> significantly decreased neovascularization."

Endogenous mouse serum FGF21 in that paper: **658.3 ± 66.4 pg/mL** — the same order as
human. The administered native dose was 5 mg/kg twice daily. Against a mouse plasma
volume of ~40 mL/kg, even allowing a distribution volume several-fold larger, that is a
peak exposure of order **10⁴–10⁵ ng/mL**, i.e. **10³–10⁴× the active concentration** and
~10⁵× endogenous. **It did not work.**

The constraint that experiment reveals is not amplitude — it is **duration**. Half-life
0.4 h failed; half-life 28 h succeeded. This is the strongest argument *in favour* of the
relay, and §7.2 gives it its due.

### 4.4 The mechanism is adiponectin-dependent — a second relay

In two separate models, deleting adiponectin **completely abolished** FGF21's retinal
protection (PMID 28199833, OIR; PMID 36943533, Phase-I ROP). FGF21 raised retinal *Apn*
and suppressed *Tnfα*; both effects vanished in Apn−/−.

This means the FGF21 concentration *at the retina* may not be the operative quantity at
all. The operative quantity would be the FGF21 concentration **at the adipocyte**, and
then the adiponectin concentration at the retina. §5 shows the expression data agree
with that reading.

---

## 5. NEW RESULT — THE RETINA LACKS THE CO-RECEPTOR

This was not in the task description. It emerged while addressing the β-Klotho
objection, and it is a harder constraint than the concentration ratio.

FGF21 has negligible affinity for FGFR alone. It signals only as
**FGF21 · β-Klotho (KLB) · FGFR1c**. KLB is the specificity subunit; without it an
FGFR1-rich tissue is simply not an FGF21 target tissue.

I extended the Step 2 gene panel with an `fgf21_receptor` class
(`src/analysis/retina_expression/gene_panel.py`) and re-ran the Human Protein Atlas arm.

**Bulk consensus RNA (HPA `rna_tissue_consensus`), nTPM:**

| Gene | Retina | Liver | Retina percentile within its own transcriptome |
|---|---:|---:|---:|
| **KLB** (obligate co-receptor) | **0.0** | 16.6 | **9.2** |
| FGFR1 | 14.4 | 8.0 | 76.9 |
| FGF21 (ligand) | **0.0** | 79.4 | 9.2 |
| **ADIPOR1** | **125.7** | 99.2 | **98.0** |
| PPARA | 16.6 | 30.8 | 79.8 |

**Single-cell (HPA `rna_single_cell_type`), nCPM:**

| Cell type | KLB | FGFR1 | ADIPOR1 | FGF21 |
|---|---:|---:|---:|---:|
| Müller glia | 1.0 | **214.4** | 27.0 | 0.0 |
| Vascular endothelium | 1.1 | **116.7** | 36.1 | 0.0 |
| Retinal pigment epithelium | **0.0** | 25.6 | 38.4 | 0.0 |
| Rod photoreceptor | 0.8 | 4.3 | 48.9 | 0.0 |
| Cone photoreceptor | **0.0** | 6.2 | 39.3 | 0.0 |
| Retinal ganglion cell | 3.9 | 11.6 | 11.6 | 0.0 |
| Horizontal cell | 4.0 | 46.1 | 22.0 | 0.0 |
| Microglia | 0.6 | 7.4 | 20.3 | 0.0 |
| *Hepatocyte (reference, non-retinal)* | **54.1** | — | — | 7.7 |

All MEASURED (HPA). Files: `data/processed/retina_hpa_bulk_ntpm.tsv`,
`data/processed/retina_hpa_celltype_ncpm.tsv`.

**Three things follow.**

1. **The retina has the receptor and not the co-receptor.** FGFR1 in Müller glia
   (214 nCPM) and endothelium (117 nCPM) is among the highest in the panel; KLB is
   0.0–4.0 nCPM everywhere, against 54.1 in hepatocytes. The two cell types the retinal
   FGF21 literature implicates — Müller glia and microvascular endothelium — are
   precisely the two with abundant FGFR1 and essentially no KLB.
2. **This explains the adiponectin dependence rather than contradicting it.** ADIPOR1 in
   retina is at the **98th percentile** of the retinal transcriptome. The retina is
   built to receive adiponectin and is not built to receive FGF21. The Smith
   laboratory's Apn−/− result and this expression profile are the same finding seen
   from two directions.
3. **No concentration argument can repair this.** A missing co-receptor is not a dose
   problem.

**Caveats, stated plainly.** This is mRNA, not protein. KLB is a low-abundance membrane
protein and HPA bulk nTPM of 0.0 in retina is a detection statement about a pooled
tissue, not proof of zero molecules — a small KLB⁺ subpopulation would be invisible here.
The mouse study (PMID 28199833, Figure 2A) reported *Klb* mRNA detectable in whole mouse
retina by RT-PCR, which is a lower bar than quantitative absence and is a different
species. A single-cell confirmation across the 24 CZ CELLxGENE retina datasets was
launched for this step and had not completed at time of writing; the command is recorded
in §10 and it is the first thing the next step should check. **The HPA single-cell arm
alone, however, already covers nine retinal cell types from an independent pipeline and
agrees with the bulk.**

---

## 6. THE BRIDGE — BOTH DATASETS ON ONE AXIS

`src/analysis/fgf21_bridge/bridge.py`. 200,000 Monte-Carlo draws, seed 20261103.

### Inputs

| Quantity | Distribution | Basis |
|---|---|---|
| Baseline plasma FGF21, T2D with DR | lognormal, median 550 pg/mL, 95% CI 250–1,200 | ASSUMED, spanning §3.2 cohorts **and** the 2.8× assay spread of §3.3 |
| Fibrate fold-change | lognormal, median 1.40, 95% CI 1.25–1.70 | ASSUMED, spanning the +28%/+39%/+61% of §3.4 |
| Intact (C-terminally uncleaved) fraction | uniform 0.66–0.90 | ASSUMED over the MEASURED 10–34% cleaved, PMID 26635356 |
| Active concentration | lognormal, median 15,000 pg/mL, 95% CI 5,000–45,000 | ASSUMED, spanning the retinal anchor (10,263) and the receptor anchor (22,620), with the lower tail extended to 5,000 to cover the **untested** sub-50 ng/mL region of §4.2 |

### The two anchors on the denominator

| Anchor | Value | Independence |
|---|---:|---|
| **A — retinal.** Lowest HRMEC-protective concentration, 50 ng/mL PF-05231023 | **10,263 pg/mL** FGF21-eq | the readout the relay actually needs |
| **B — receptor.** FGF21 EC50 for glucose uptake, human adipocytes, 1.16 nM | **22,620 pg/mL** | different tissue, different readout, different laboratory (PMC4218812) |

They agree within 2.2×, from entirely separate experiments. That convergence is why the
denominator is trustworthy.

### Results

```
baseline                     550 pg/mL   [249 – 1,213]
achievable, total FGF21      770 pg/mL   [341 – 1,741]
achievable, intact FGF21     598 pg/mL   [260 – 1,378]
active concentration      15,049 pg/mL   [5,012 – 44,809]

ratio  (achievable / active), total     0.051   [0.013 – 0.202]
ratio  (achievable / active), intact    0.040   [0.010 – 0.159]

SHORTFALL, total     19.5×   [5.0× – 75.9×]
SHORTFALL, intact    25.0×   [6.3× – 98.7×]
log10 shortfall      1.40    [0.80 – 1.99]

P(achievable ≥ active)          = 0.0000
P(achievable ≥ 10% of active)   = 0.095
```

### Calibration — three checks that this is not my arithmetic

1. **The modelled active concentration lands where a therapeutic band should.** Clinical
   FGF21-analog trials achieved 17,500–150,000 pg/mL (PMC8097867). The modelled active
   concentration, 15,049 pg/mL, sits **1.2× below the bottom** of that band — exactly
   where an EC should sit relative to the exposures a developer chooses. If my
   denominator were wrong by an order of magnitude, this would not hold.
2. **Required versus delivered fold-rise.** Reaching the active concentration from a
   550 pg/mL baseline needs a **27× rise**. A fibrate delivers **1.28–1.61×**. The gap in
   required fold-rise is **17–21×**.
3. **The yardstick's own weakness, stated.** Endogenous FGF21 in T2D already sits
   **41× below** the adipocyte EC50. So the in-vitro EC50 cannot be read as "nothing
   happens below this" — endogenous FGF21 is not inert. This is why **anchor A, the
   retinal one, carries the argument** and anchor B is corroboration only.

---

## 7. THE TWO OBJECTIONS

### 7.1 Free versus total hormone, given β-Klotho dependence

**The objection as posed dissolves and is replaced by a sharper one.** FGF21 is an
*endocrine* FGF precisely because it lacks the heparan-sulfate-binding region that
tethers paracrine FGFs to matrix, and no high-affinity plasma carrier protein has been
characterised for it. There is therefore no meaningful free/bound split of the kind that
applies to steroids or thyroxine. β-Klotho is a *membrane* co-receptor, not a circulating
binder; it does not sequester hormone in plasma. A free-fraction correction has nothing
to correct.

The real version of the objection is **intact versus cleaved**, and it goes the wrong way
for the relay:

- FAP cleaves circulating FGF21 after Pro-171 (MEASURED, PMID 26635356, 26797127, 26962859).
- The C-terminus is the β-Klotho-binding determinant.
- **10–34%** of circulating FGF21 is C-terminally cleaved (MEASURED, PMID 26635356).
- Deleting the C-terminal 10 residues costs **~50×** in EC50 (MEASURED, PMC4218812).
- Essentially all published assays, including every one in §3, are **total** assays.

So the measured numerator **overstates** active hormone. Correcting it moves the
shortfall from 19.5× to **25.0×**.

And then §5 supersedes the whole question: the binding-availability argument is moot
when the tissue does not express the co-receptor. **Human retina: KLB 0.0 nTPM, 9th
percentile. Liver: 16.6 nTPM.**

One asymmetry worth noting, because it cuts the other way and should not be buried:
PF-05231023 is a 190 kDa IgG conjugate. Large proteins cross the blood-retinal barrier
poorly, so the retinal tissue concentration achieved by the systemically dosed conjugate
was probably *well below* its plasma concentration — which would mean the true active
concentration at the retina is lower than anchor A suggests. That argument is real, but
it is bounded: the authors also showed **intravitreal** PF-05231023 worked (PMID 28199833,
Figure S1), i.e. direct retinal delivery was effective, and the in-vitro HRMEC anchor is a
direct cell-exposure measurement with no barrier term at all. Anchor A is a cell-exposure
number, so the barrier argument does not reduce it.

### 7.2 Chronic versus acute exposure

**This is the strongest argument for the relay, and it does not close the gap.**

The decisive in-vivo experiment (§4.3) separates amplitude from duration cleanly:

| | Amplitude | Duration | Retinal effect |
|---|---|---|---|
| Native FGF21, 5 mg/kg BID | ~10³–10⁴× active | t½ 0.4 h — pulsatile | **none** |
| PF-05231023, 0.5–10 mg/kg | ~1–10× active | t½ 28 h — sustained | **protective** |
| **Fibrate in humans** | **0.04× active** | **sustained for months** | **never tested** |

A fibrate gives the *right kinetics* and the *wrong amplitude*. The native-FGF21 arm gave
the right amplitude and the wrong kinetics. **The cell of the table that matters — modest
amplitude, sustained for months, retinal readout — is empty.** That is the honest
residual uncertainty, and it is why §8 specifies an experiment rather than declaring the
question closed forever.

Three considerations stop that empty cell from rescuing the mechanism:

1. **Duration cannot substitute for sub-threshold amplitude at a receptor.** Occupancy is
   set by concentration. Sustained exposure 25× below the active concentration gives
   sustained sub-threshold occupancy, not accumulated effect — unless the readout
   integrates over time, which has not been shown for any of these endpoints.
2. **Chronic exposure in the relevant population plausibly makes it worse, not better.**
   In *mouse pancreatic islets*, both db/db islets and normal islets exposed to high
   glucose ex vivo showed reduced β-Klotho expression and resistance to FGF21
   (MEASURED, PMID 23897951). **This is islets, not retina, and mouse, not human — it is
   an analogy, not evidence about the eye**, and I am flagging it as such rather than
   letting it carry weight it has not earned. Its relevance is directional only: the
   co-receptor the human retina barely expresses (§5) is one that hyperglycaemia is known
   to downregulate in at least one other tissue, and the patients who would receive the
   fibrate are hyperglycaemic by definition. Whether retinal KLB behaves the same way is
   unmeasured in any species.
3. **The fibrate elevation is itself chronic in humans and has been observed for 12
   weeks** at +61% (PMC8097867) **with no retinal readout attached.** The duration arm of
   the argument has been available for a decade and nobody has connected it to an eye.

**One honest point against my verdict.** *Fgf21*−/− mice had **increased**
neovascularisation (PMID 28199833). Endogenous FGF21, at ~658 pg/mL, is therefore not
inert in the retina. That is a genuine observation and it deserves to be stated rather
than explained away. It does not, however, license the inference the relay needs: a
lifelong, whole-body knockout removes the hormone from liver, adipose and the systemic
lipid-handling that feeds the adiponectin arm, from conception. **A knockout phenotype
establishes that a hormone matters. It does not establish that a 40% increment above
baseline moves a retinal endpoint.** Dose-response is not recoverable from a null allele.

---

## 8. WHAT SURVIVES, AND THE EXPERIMENT THAT WOULD SETTLE IT

The FGF21 → retina limb fails. The **FGF21 → adipose → adiponectin → retina** route is
not refuted by anything here, and the expression data actively favour it:

| Step | Status | Evidence |
|---|---|---|
| Fibrate → plasma FGF21 ↑ 1.28–1.61× | **established** | §3.4, four human studies |
| FGF21 → adipocyte (KLB-rich tissue) | **plausible**; adipose expresses KLB | — |
| Fibrate → plasma adiponectin in humans | **UNQUANTIFIED — the open gap** | no clean human fibrate RCT value found |
| FGF21 analog → adiponectin ↑ in humans | **established** | PMID 26959184, PMID 24011069 |
| Adiponectin → retinal protection | **established in mouse** | PMID 28199833, PMID 36943533 |
| Retina can receive adiponectin | **established** | ADIPOR1 125.7 nTPM, 98th pctile (§5) |

The third row is the whole question now. Note that the fourth row's evidence comes from
analog trials at 17,500–150,000 pg/mL — so even the adiponectin arm has only been
demonstrated at concentrations a fibrate cannot reach.

**The decisive experiment, specified.** In an existing fibrate trial with stored
plasma — FIELD has 9,697 participants with paired pre/post run-in samples and the
retinopathy endpoint already adjudicated — measure (a) **intact** FGF21 by a
C-terminus-dependent assay, not a total assay, and (b) total and high-molecular-weight
adiponectin, in the same samples. Then test whether the *within-patient* change in each
predicts the retinopathy endpoint. This needs no new recruitment and no animal. It would
either produce the first dose-response linking a fibrate-achievable concentration to a
human retinal outcome, or close the limb for good.

Cheaper and available immediately: an **FGF21 concentration-response on HRMECs below
50 ng/mL**, which has never been run. If protection persists at 1 ng/mL
PF-05231023 (~205 pg/mL FGF21-equivalent), the arithmetic above is wrong and I would
withdraw the verdict. If it does not, the gap is confirmed from the direction that
matters.

---

## 9. THE SIGN CHECK — INDEPENDENT OF ALL ARITHMETIC

If raising plasma FGF21 protects the retina, higher plasma FGF21 should track with less
retinopathy. It tracks with more.

| Finding | n | Source |
|---|---:|---|
| Higher baseline FGF21 → more prevalent microvascular disease (T2D) | 9,697 | PMID 26055067 |
| Higher baseline FGF21 → more **new** microvascular disease over 5 y (OR 1.09 per SD) | 6,465 | PMID 26055067 |
| Higher **fenofibrate-induced** FGF21 rise → faster glycaemic progression (HR 1.18, top tertile) | 9,697 | PMID 28606915 |
| FGF21 > 554.7 pg/mL → **>8×** risk of sight-threatening DR | 654 | PMC8016097 |
| FGF21 rises monotonically no-DR → NPDR → PDR | — | Lin 2014 via PMC5735335 |

All MEASURED.

**This must be read carefully and I will not overclaim it.** The most likely explanation
is reverse causation: FGF21 is a stress hormone that rises with hepatic and metabolic
disease severity, and DR severity tracks diabetes severity. An elevated biomarker is
weak evidence against a protective effect of the *exogenous* hormone.

But the third row is not reverse causation. It is the **within-patient, treatment-induced**
change — the exact quantity the relay proposes is therapeutic — and in 9,697 patients
it predicted a **worse** outcome. At minimum, there is no dose-response signal in the
right direction anywhere in the largest human dataset that could show one. A mechanism
ranked "best-evidenced" should have left a trace there.

---

## 10. FILES AND REPRODUCTION

**New code** — `src/analysis/fgf21_bridge/`

| Module | Role |
|---|---|
| `pubmed.py` | NCBI E-utilities client (`esearch` over PubMed **and** PMC full text, `efetch_abstracts`). Reuses `census_client.fix_proxy_env` for the sandbox proxy |
| `pmc.py` | PMC open-access full text via the BioC API, tags stripped — absolute concentrations live in Methods and Results, never in abstracts |
| `harvest.py` | The five query sets behind §3 and §4, re-runnable |
| `bridge.py` | Unit conversions, Monte-Carlo ratio, calibration checks |

**Modified** — `src/analysis/retina_expression/gene_panel.py`: added the
`fgf21_receptor` class (KLB, FGFR1–4, ADIPOQ, ADIPOR1/2), with the rationale in the
module docstring.

**Regenerated** — `data/processed/retina_hpa_bulk_ntpm.tsv`,
`data/processed/retina_hpa_celltype_ncpm.tsv` (now 103 genes, up from 95).

```bash
venv/bin/python -m src.analysis.fgf21_bridge.bridge          # §6 and the calibration
FGF21_OUT=$TMPDIR/fgf21 venv/bin/python -m src.analysis.fgf21_bridge.harvest
venv/bin/python src/analysis/retina_expression/hpa.py --work-dir $TMPDIR/hpa
```

### Not done

- **The single-cell KLB confirmation did not finish.** Launched and still running at
  time of writing:
  ```bash
  venv/bin/python src/analysis/retina_expression/query_census.py \
    --genes KLB,FGFR1,FGFR2,FGFR3,FGFR4,ADIPOQ,ADIPOR1,ADIPOR2,FGF21,PPARA,RLBP1,CLDN5,TBP \
    --prefix retina_sc_fgf21_
  ```
  It will write `data/processed/retina_sc_fgf21_*.tsv` across the 24 CZ CELLxGENE retina
  datasets (~4.8M cells). PPARA, RLBP1, CLDN5 and TBP are included as internal controls:
  their values must reproduce the Step 2 tables or the run is not trustworthy. **The §5
  conclusion currently rests on HPA alone** — two HPA arms (bulk and single-cell), which
  is one consortium, not two.
- `retina_hpa_antibody_reliability.tsv` was **not** regenerated; the HPA v23
  `normal_tissue.tsv` download returned a non-zip payload. That file is Step 2's and is
  not used here. No KLB antibody evidence in this note.
- **FIELD absolute FGF21 concentrations are paywalled** (PMID 28606915). The largest
  fibrate-on-FGF21 dataset contributes direction but not magnitude to §3.4.
- **No protein-level measurement anywhere in this note.** §5 is mRNA.
- **The fibrate → human adiponectin magnitude was not found** in a clean randomised
  human dataset. §8 marks it as the open gap rather than guessing it.

---

## 11. EFFECT ON `REPORT.md`

| Claim | Disposition |
|---|---|
| §5.5 hepatic-to-retinal FGF21 relay, **ranked best-evidenced** | **Withdrawn.** 25× concentration shortfall (95% CI 6–99×), a 10³–10⁴× native-hormone dose that failed, a missing co-receptor in human retina, and the wrong epidemiological sign |
| §5.5 relay is necessarily hepatic (Step 2: retina makes no FGF21) | **Confirmed and extended.** The retina does not make FGF21 *and* cannot receive it |
| Fibrate retinal benefit in FIELD / ACCORD-Eye | **Untouched and still unexplained.** This note removes one candidate explanation; it does not remove the observation |
| Adiponectin as a mediator | **Promoted from a footnote to the leading hypothesis.** Retinal ADIPOR1 is at the 98th percentile and the mouse protection is Apn-dependent |
| §2.3 "measured pharmacokinetics: none" | **Partly closed.** Human plasma FGF21 is now measured and bounded end to end. Intraocular FGF21 remains unmeasured in any species |

---

## Status — 2026-11-03 — step 3: close the FGF21 concentration bridge

**Done.** Extracted human plasma FGF21 (baseline non-diabetic 85–235 pg/mL; T2D with DR
450–670 pg/mL; fibrate fold-change 1.28–1.61, maximum achieved ~1,000 pg/mL) and the
retinal concentration-response (HRMEC protection at 50 and 100 ng/mL PF-05231023 only;
no lower concentration ever tested). Corrected the 190 kDa / 2:1 conjugate mass, which
halves the apparent gap and runs against the conclusion. Computed the ratio by Monte
Carlo over the published spread of every input.

**Verdict: the relay fails.** Shortfall 25× (95% CI 6–99×), 1.4 log (0.8–2.0);
P(achievable ≥ active) = 0.0000 in 200,000 draws. Three independent constraints agree:
native FGF21 at ~10⁴× endogenous did not work in the one experiment that tested it; the
human retina expresses KLB at 0.0 nTPM / 9th percentile against FGFR1 at the 77th; and
higher FGF21 — including the fenofibrate-induced rise itself, in 9,697 patients — tracks
with worse microvascular outcomes.

**Verified.** Denominator calibrated three ways: two independent anchors agreeing within
2.2× (retinal 10,263 pg/mL; receptor EC50 22,620 pg/mL), and a modelled active
concentration landing 1.2× below the bottom of the clinically dosed FGF21-analog band.

**For the next step.**
1. The Census single-cell KLB run was still going at hand-off — command in §10. §5
   currently rests on HPA alone. Check the PPARA/RLBP1/CLDN5/TBP controls against the
   Step 2 tables before trusting it.
2. `REPORT.md` §5.5 must be rewritten: the best-evidenced limb is gone, and the ranking
   above it changes.
3. The adiponectin arm is now the leading candidate and its human fibrate leg is
   unquantified (§8).
4. Step 4 inherits one verified claim of absent evidence: **no FGF21 concentration-
   response below 50 ng/mL exists on any retinal preparation.**
