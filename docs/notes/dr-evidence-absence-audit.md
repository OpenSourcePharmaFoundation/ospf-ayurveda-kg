# Diabetic Retinopathy — Evidence-Absence Audit

**Date** 2026-11-03
**Step** 4 of `docs/prompts/dr-solve-open-questions-prompt.md`
**Scope** Three claims that specific evidence does not exist, plus one confound question
about the global *Ppara* knockout, all drawn from
`data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/REPORT.md` §6.1, §6.2 and
§6.5.
**Status** Two of three absence claims **refuted with citations**. One **verified absent**.
The confound question is **resolved for two of several retinal cell types**, by better
experiments than a statistical correction.

---

## 0. HEADLINE

**Two of the three "nobody has done this" claims in REPORT.md are false, and the stronger
one — the necessity experiment the report calls "the field has never run" — was published in
2022, four years before the report that cites its absence.** The third claim (intraocular
ANGPTL4 vs. fibrate exposure) holds up under systematic search. This is exactly the failure
mode the chain exists to correct: an absence of evidence was asserted from reasoning, not
from search, and the search finds something the reasoning missed.

| # | Claim | Verdict |
|---|---|---|
| 1 | No cell-type-restricted conditional *Ppara* deletion in retina | **REFUTED.** Two exist: endothelial-specific (2026) and microglia-specific (2022) |
| 2 | No published measurement of intraocular ANGPTL4 stratified by fibrate exposure | **VERIFIED ABSENT** |
| 3 | No measurement of fibrate concentration in retinal tissue or aqueous humour, in any species | **REFUTED for the literal claim; the clinically load-bearing version (oral dosing) survives narrowed** |
| 4 | Does the global KO phenotype survive correction for systemic confounds? | **Resolved for 2 of ≥5 retinal cell types** — not by statistical correction, by a better experiment |

---

## 1. CLAIM 1 — Cell-type-restricted conditional *Ppara* deletion in retina

### REPORT.md's claim (§6.5, verbatim)

> "Cell-type-restricted conditional *Ppara* deletion in retina. The global knockout cannot
> substitute — it carries hypertriglyceridaemia, abolished ketogenesis and FGF21, and
> hepatic steatosis, so 'worse retinopathy' is fully explained by the competing systemic
> hypothesis. Citing it for the local limb is circular. **After roughly fifteen years of
> interest in this target, the conditional deletion's continued absence is itself
> informative.**"

### Verdict: REFUTED

**Two independent cell-type-restricted conditional *Ppara* knockouts in mouse retina have
been published**, both from the same group (Ma JX, Wake Forest / previously Oklahoma Health
Sciences Center), using two different Cre drivers:

| Model | Cre driver | Paper | Published |
|---|---|---|---|
| **Endothelial-specific** PPARα cKO (PPARαECKO) + conditional transgenic (PPARαECTG) | *Vecad-CreERT2* (VE-cadherin, tamoxifen-inducible) | Xu, Cheng, Zhou, Ma. "Peroxisome Proliferator-Activated Receptor α Deficiency Induces Vascular Pathologies through Endothelial Senescence in Diabetic Retinopathy." *Am J Pathol.* 2026 Apr;196(4):960-975. **PMID 41485550**, PMCID PMC13084685 | **2026** — same year as the analysis, after it |
| **Microglia-specific** Pparα cKO (PCKO) + conditional transgenic (PCTG) | *Cx3Cr1-CreERT2* (tamoxifen-inducible) | Yuan, Dong, Pearsall, Zhou, Cheng, Ma. "The Protective Role of Microglial PPARα in Diabetic Retinal Neurodegeneration and Neurovascular Dysfunction." *Cells.* 2022 Dec 1;11(23):3869. **PMID 36497130**, PMCID PMC9739170 | **2022 — four years before the original 2026-10-05 analysis** |

**Both are necessity experiments** (loss-of-function, with gain-of-function controls), and
both report retinal phenotypes under diabetic stress:

- **Endothelial cKO**: decreased retinal vascular density (postnatal), enlarged avascular
  area and fewer endothelial progenitor cells in oxygen-induced retinopathy (OIR), and in
  6-month STZ diabetes — **declined ERG amplitude, decreased retinal thickness (OCT), and
  increased vascular leakage** relative to floxed-but-uninduced littermates. Mechanism:
  EC mitochondrial dysfunction and senescence.
- **Microglial cKO**: no baseline phenotype without diabetes, but under STZ diabetes —
  **decreased ERG response, exacerbated pericyte loss**, increased subretinal microglial
  migration, metabolic shift to glycolysis, and increased STING/TNFα. The gain-of-function
  arm (PCTG, microglia-specific *Pparα* overexpression) alleviated the diabetic phenotype,
  the cleanest form of necessity-and-sufficiency evidence available in this literature.

**Both papers explicitly state the same motivation REPORT.md gives for wanting this
experiment** — isolating the receptor's local role from the global knockout's systemic
confounds:

> "To **exclude the impact of dyslipidemia** on the retinal microvasculature in global PPARα
> KO mice... the present study generated EC-specific PPARα conditional KO and transgenic
> mice." — Xu et al. 2026

> "To specifically study the role of PPARα in microglia and **exclude the effects of
> surrounding cells**, such as photoreceptors, vascular endothelial cells, and Müller glia,
> we generated microglial *Pparα* conditional knockout mice." — Yuan et al. 2022

Both include a Cre-toxicity control (comparing Cre-only mice against flox-only controls) and
both use inducible (tamoxifen-dependent) Cre to avoid developmental confounds.

**Neither paper measures ANGPTL4** (checked by full-text search of both PMC records — zero
hits in either).

### What remains genuinely absent

No conditional deletion was found for **RPE, Müller glia, or photoreceptors** — the three
other major PPARα-expressing retinal compartments identified in Step 2
(`docs/notes/ppara-retinal-expression.md`, where PPARA is highest in rods, RPE and cones, not
endothelium or microglia). So the necessity question is **answered for the two lowest-PPARA
compartments** (endothelium, microglia: 15.4% and 15.5% of cells) and **unaddressed for the
three highest** (rods 68.0%, RPE 64.8%, cones 54.5%). That inversion matters: the cell types
with conditional-KO evidence of necessity are not the cell types where the receptor is most
abundant.

### What this changes

- **§6.5's claim that the conditional deletion's absence is "itself informative" is false and
  should be removed.** The experiment has been run twice, with gain-of-function controls, and
  the field answer is "yes, cell-autonomous PPARα loss in endothelium and microglia worsens
  diabetic retinal phenotypes" — i.e., **the result REPORT.md predicted did not happen; the
  opposite happened and nobody checked.**
- **§6.2's proposed knockout arm** ("a receptor-knockout arm... without knockout or antagonist
  controls") is partially pre-empted: receptor-knockout controls now exist for two cell
  types. The remaining knockout gap is RPE/Müller/photoreceptor-specific.
- **§6.6 item 7** ("Conditional retinal receptor deletion, $300–500k, 18–24 mo, decides
  Necessity") should be re-costed: the experiment exists for 2 of 5+ compartments. The
  residual spend is for the compartments where PPARA is most highly expressed, which is
  arguably the more important gap, not a from-scratch $300–500k item.
- This also **directly answers Claim 4** (confound correction) for these two cell types —
  see §4 below.

---

## 2. CLAIM 2 — Intraocular ANGPTL4 stratified by fibrate exposure

### REPORT.md's claim (§6.1, implicit; the proposed experiment presupposes the absence)

> "Pair it with aqueous ANGPTL4 in the same tap: two of three central unknowns from one
> draw." — i.e., nobody has yet measured aqueous/vitreous ANGPTL4 in fibrate-exposed vs.
> unexposed patients or animals.

### Verdict: VERIFIED ABSENT

No published measurement of intraocular (aqueous humour or vitreous) ANGPTL4 **stratified by
fibrate exposure**, in any species, was found. ANGPTL4-in-DR and ANGPTL4-in-aqueous-humour
are both well-studied independently (dozens of hits — ANGPTL4 is implicated in proliferative
DR, lymphatic-like remodeling, and anti-VEGF response), but none of those studies report
fibrate-treatment status as a stratifying variable, and none of the fibrate-ANGPTL4 studies
(all plasma-based: fenofibrate and pemafibrate reliably raise circulating ANGPTL4 2–4×, e.g.
Oldoni 2026, Yamashita 2026) measured an ocular fluid.

**The one adjacent finding**, which is relevant context but does not refute the claim: an
in vitro study (Ohguro et al., *Bioengineering (Basel)* 2024;11(12):1247, PMID 39768065)
treated ARPE19 (human RPE cell line) with pemafibrate and found ANGPTL4 mRNA upregulated, but
**less** than with the non-selective PPARα agonist GW7647 — framed by the authors as a reason
pemafibrate's intraocular risk may be lower than a non-selective agonist's. This is cell
culture, not an intraocular fluid measurement, and not stratified by in vivo fibrate exposure.
It is evidence *about* the mechanism, not the measurement the claim is about.

### Queries run (Europe PMC REST API, `pageSize` 8–10, reproducible)

```
ANGPTL4 AND (aqueous humor OR aqueous humour OR intraocular) AND fibrate        → 10 hits, none relevant
ANGPTL4 AND vitreous AND fibrate                                                → 4 hits, none relevant
ANGPTL4 AND aqueous humor                                                       → 83 hits, none fibrate-stratified
ANGPTL4 AND vitreous AND (diabetic retinopathy)                                 → 110 hits, none fibrate-stratified
angiopoietin-like 4 AND fenofibrate AND eye                                     → 132 hits, none an in vivo intraocular measurement
ANGPTL4 fenofibrate OR pemafibrate human                                        → 7,251 hits (broad; scanned top 10, all systemic/plasma)
ANGPTL4 AND fenofibrate AND (rat OR mouse OR rabbit OR rodent) AND (retina OR eye OR ocular) → 43 hits, none an animal intraocular-fluid measurement
FIELD study ANGPTL4 / ACCORD eye ANGPTL4 / angiopoietin-like 4 fibrate clinical trial eye     → no FIELD/ACCORD sub-study with ocular ANGPTL4
```

### What this changes

Nothing in REPORT.md's framing. This is the one claim of the three that holds. **§6.1's
proposed experiment (pair aqueous drug concentration with aqueous ANGPTL4 at the same
cataract-surgery tap) remains a genuinely novel, unclaimed measurement** and should stay in
the experimental programme unchanged.

---

## 3. CLAIM 3 — Fibrate concentration in retinal tissue or aqueous humour, in any species

### REPORT.md's claim (§6.1, the critical-path unknown)

> "Free drug concentration in retinal tissue, and the receptor occupancy it implies. **Never
> measured in any species.**"

### Verdict: REFUTED for the literal claim. The clinically load-bearing version — concentration achieved by oral dosing specifically — survives, but narrower and weaker than REPORT.md states.

**The literal claim is false.** Fenofibrate and fenofibric acid concentrations have been
directly measured, by LC-MS, in retinal/vitreous tissue and in aqueous humour, in rodents,
more than once:

| Study | Species | Route | Retina/vitreous result | Aqueous humour result |
|---|---|---|---|---|
| **Huang et al. 2021**, *Biology (Basel)* 10(12):1328, PMID 34943243, PMCID PMC8698460 | Mouse (C57BL/6J) | **Intraperitoneal injection, 2 mg/kg/day × 7 days** (systemic, not oral) vs. topical 0.1% eye drop | Fenofibrate **0.033 ± 0.014 ng/mg**, fenofibric acid **0.140 ± 0.044 ng/mg** (IP, systemic); vs. 1.402 ± 0.341 / 0.472 ± 0.064 ng/mg (topical) | Not reported separately (vitreous/retina pooled) |
| **Kaffash et al. 2026**, *J Control Release* 391:114656, PMID 41580131, PMCID PMC13011889 | Rat (SD) | Topical microemulsion eye drop (not oral) | Not separately reported (cornea/conjunctiva/sclera reported) | Fenofibrate **7.5 ± 1.2 ng/g** (1h) → 3.5 ± 0.4 ng/g (4h); fenofibric acid **131.0 ± 28.2 ng/g** (1h) → 27.5 ± 11.2 ng/g (4h) |
| **Poudel et al. 2026**, *Int J Pharm* 689:126503, PMID 41407273, PMCID PMC12794465 | Rat and rabbit | **Intravitreal injection** (not oral) | "Sustained drug levels in the retina for at least 6 months" (microparticle depot) | Not reported |
| **Qiu et al. 2019**, *Mol Pharm* 16(5):1958-1970, PMID 30912953, PMCID PMC6502649 | Rat (Brown Norway) | **Intravitreal injection** (free drug and nanoparticle) | Quantified by LC-MS, declining to below quantification within days for free drug; sustained ≥60 days for nanoparticle | — |

**So the field has repeatedly built and validated the exact LC-MS assay REPORT.md's proposed
experiment calls for** (§6.1's "pair it with aqueous ANGPTL4 in the same tap" presupposes this
assay doesn't exist as a capability — it does, and has existed since at least 2019).

### What does *not* exist, and is the load-bearing gap

**None of these measurements used oral dosing — the clinically relevant route.** All
"systemic" comparator arms used intraperitoneal injection, not oral gavage, and every direct
ocular-tissue measurement used local (intravitreal or topical) administration. The one place
an oral-dosing attempt is referenced, it is reported as a **negative** result, in a single
sentence embedded in Qiu et al. 2019's introduction:

> "No fenofibrate or fenofibric acid was detected in Brown Norway rats' eyes following oral
> administration of fenofibrate."

This sentence carries a citation in the original PDF that I was not able to independently
resolve to a PMID within this search (the BioC full-text extraction used here strips inline
reference markers; the reference-list title at that position, "Therapeutic Potential of
Topical Fenofibrate Eyedrops in Diabetic Retinopathy and AMD Rat Models," did not return an
exact Europe PMC match under that title). **Treat this one data point as reported-but-not-
independently-verified** — it is a secondhand citation of a primary result I could not pull
and check directly, which is exactly the standard this audit is trying to hold everything
else to. It is nonetheless a second, independent line of evidence (from the same lab's own
introduction, arguing against their own paper's delivery-route thesis) that oral dosing was
specifically tried and specifically produced a below-detection result in ocular tissue — not
silence, a negative measurement.

**No study anywhere in this search quantifies fenofibrate, fenofibric acid, or any other
fibrate in human aqueous humour, vitreous, or retina after therapeutic oral dosing in
patients** — the exact measurement REPORT.md's §6.1 proposes (cataract-surgery aqueous tap in
chronic oral-fibrate patients) remains undone in humans.

### Queries run

```
fenofibrate AND (aqueous humor OR aqueous humour) AND concentration     → 17 hits (reviews/formulation papers; led to Kaffash 2026)
fenofibrate AND vitreous AND concentration                              → 286 hits (scanned top 8; led to Poudel 2026, Kaffash 2026)
fenofibrate AND retina AND pharmacokinetics AND tissue                  → 128 hits
fenofibric acid AND ocular AND pharmacokinetics                         → 22 hits
pemafibrate AND ocular AND pharmacokinetics                             → 7 hits, no ocular tissue-level study for pemafibrate specifically
fibrate AND "whole body autoradiography" AND eye                       → 1 hit, irrelevant (PFAS food-safety review)
fenofibrate tissue distribution eye rat                                 → 271 hits
fenofibrate dog OR cat OR veterinary ocular toxicity retina             → 209 hits — no veterinary-ophthalmology fibrate PK study found
oral fenofibrate AND retina AND concentration AND rat                   → 191 hits, none an oral-dosing quantitative retinal measurement
fenofibrate cataract surgery aqueous humor sample                       → 30 hits, none an actual cataract-surgery PK sub-study
fenofibrate aqueous humor oral dose patients                            → 76 hits, none a human measurement
fenofibric acid plasma retina ratio                                     → 30 hits, no partition-ratio measurement found
fenofibrate blood-retinal barrier penetration systemic                  → 159 hits, all narrative/review, no new PK data
```

No veterinary-ophthalmology fibrate PK study and no FDA/EMA tissue-distribution
(whole-body-autoradiography) fenofibrate dataset covering the eye was located; fibrate
regulatory packages were not independently pulled from FDA/EMA archives in this pass — that
remains a specific, identifiable follow-up (not searched: Drugs@FDA pharmacology/toxicology
review PDFs for fenofibrate, fenofibric acid, pemafibrate).

### Independent corroboration that this gap is real, not a search-coverage artifact

A 2026 narrative review (Ho et al., *J Pharm Pharm Sci* 29:16995, PMID 42713229) — written by
an independent group with no connection to the papers above — states as its own conclusion
that fenofibrate's ophthalmic repurposing needs "further randomized trials, mechanistic
studies, **pharmacokinetic evaluation**, and long-term safety assessments... to define its
therapeutic role." An independent domain review in 2026 is still asking for the same PK
dataset REPORT.md flags as missing — a second line of evidence that this specific gap, in its
clinically relevant (oral-dosing, human) form, is real.

### What this changes

- **§2.3 "measured pharmacokinetics: none" (restated in §6.1 as "never measured in any
  species")** should be corrected to: ocular tissue concentration **has** been measured,
  repeatedly, for local (intravitreal, topical) fibrate delivery in rodents; it has **not**
  been measured for oral/systemic dosing in any species with a quantified, bounded value —
  the one reported oral attempt found it below the assay's detection limit. This is a
  materially different (and more informative) state of knowledge than "never measured":
  **the delivery-route comparison itself is the finding** — systemic dosing in mice achieved
  ~40× less retinal fenofibrate than topical dosing of the same drug (Huang 2021), which is
  independent, quantitative support for Step 5's exposure-model concern, not merely an
  assumption.
- **§6.1's practical route (human aqueous humour at cataract surgery) remains the correct,
  still-undone experiment** in humans — nothing here closes that gap, it only establishes
  that the assay and animal-model precedent for it are mature and already validated by three
  independent groups.
- **Step 5's exposure model** (`docs/notes/retinal-exposure-model.md`, if written after this
  step) should anchor its neural-retina partition-ratio prior against the Huang 2021 IP-vs-
  topical ratio (≈0.02–0.3, depending on analyte) rather than treating the whole partition
  question as unconstrained by any measurement.

---

## 4. THE CONFOUND QUESTION — Does the global *Ppara* KO phenotype survive correction for systemic confounds?

### The question (from the step brief, echoing REPORT.md §6.5)

The global knockout carries hypertriglyceridaemia, abolished ketogenesis and FGF21, hepatic
steatosis, and an altered diabetes response. Has anyone controlled for this, so that "worse
retinopathy" in the global KO is not simply the competing systemic hypothesis in disguise?

### Verdict: Resolved for 2 of ≥5 retinal cell types — not by statistical correction of the global-KO data, but by a design that makes the correction unnecessary

**Nobody has gone back and statistically corrected the original global-KO retinopathy papers
for triglycerides, FGF21, or hepatic steatosis as covariates.** No such re-analysis or
matched-control (e.g., a triglyceride-lowering non-PPAR comparator arm, which is exactly what
REPORT.md §6.2 and §6.6 propose as a still-needed experiment) was found in this search, and
REPORT.md's own proposed experiment is still the only place that idea appears.

**But the cell-type-specific conditional knockouts found for Claim 1 make the correction moot
for the compartments they cover, which is a stronger answer than a statistical adjustment
would have been.** Both papers are explicit about this being their motivation:

- The endothelial-specific paper states its purpose is **"to exclude the impact of
  dyslipidemia"** that confounds the global KO, and finds that EC-restricted PPARα loss
  — with hepatic PPARα, systemic triglycerides, ketogenesis and FGF21 production all intact
  — **still reproduces** worsened diabetic ERG decline, retinal thinning and vascular
  leakage relative to flox controls.
- The microglial paper states its purpose is **"to exclude the effects of surrounding
  cells"** and, separately, by construction, excludes systemic confounds the same way: only
  microglial PPARα is deleted, hepatic PPARα is untouched. It finds microglia-restricted loss
  **still reproduces** worsened diabetic ERG decline and pericyte loss, and the reciprocal
  gain-of-function (microglial PPARα overexpression) **rescues** both — necessity and
  sufficiency, in the same paper, with the systemic confound structurally absent rather than
  statistically removed.

**This directly answers the circularity concern for these two cell types: "worse
retinopathy" in diabetic mice lacking PPARα in endothelium or microglia specifically is *not*
explained by the global knockout's systemic lipid/ketone/FGF21 derangements, because those
systemic variables are normal in these mice.** The receptor's local, cell-autonomous role is
established independently of the competing systemic hypothesis, at least in these two
compartments.

**It is not answered for the remaining compartments.** REPORT.md and the Step 2 note both
identify rods, cones and RPE as the compartments with the *highest* PPARA expression (Step 2:
68.0%, 54.5%, 64.8% of cells respectively, versus 15.4–15.5% in endothelium and microglia).
Findings attributed to global-KO photoreceptor or RPE phenotypes — e.g. the neuroprotection
and mitochondrial-efficiency results in Pearsall et al. 2019 (*PLoS One* 14(2):e0208399, PMID
30716067), which used global *Pparα*−/− mice and ties PPARα to retinal-neuron mitochondrial
function and oxidative stress — **remain exactly as confounded as REPORT.md describes.** No
photoreceptor-, RPE-, or Müller-glia-specific conditional deletion was found anywhere in this
search, so the circularity objection stands unresolved for the cell types where the receptor
is most abundant and where Step 2 found the local-engagement mechanisms are actually sited.

### What this changes

- **REPORT.md §6.5 should be rewritten, not merely softened.** "The conditional deletion's
  continued absence is itself informative" is false; two conditional deletions exist and
  both show the predicted direction of effect, with the systemic confound structurally
  excluded rather than merely argued away.
- **The necessity question is now split by cell type, which is new information REPORT.md did
  not have:** resolved (endothelium, microglia) vs. still open and still confounded
  (photoreceptors, RPE, Müller glia) — and the still-open compartments are the
  higher-PPARA, more mechanistically central ones per Step 2.
- **§6.6 item 7** ("Conditional retinal receptor deletion... Necessity") should be rescoped
  to target RPE/photoreceptor-specific deletion specifically, since that is the part of the
  necessity question that remains open, not a from-scratch repeat of work already done twice.

---

## 5. QUERY LOG (for reproducibility)

All queries run against the Europe PMC REST API
(`https://www.ebi.ac.uk/europepmc/webservices/rest/search`, `format=json`) and NCBI
E-utilities (`esearch`/`efetch`, via `src/analysis/fgf21_bridge/pubmed.py`, reused unchanged
from Step 3), proxy-routed through `src/analysis/retina_expression/census_client.fix_proxy_env`.
Full-text retrieval used `src/analysis/fgf21_bridge/pmc.py` (BioC API) against open-access PMC
IDs. No new modules were added; this step is a literature search, not a data pipeline, so no
code changes were made under `src/`.

**Claim 1 queries:**
```
Ppara AND retina AND conditional
Ppara AND retina AND conditional knockout                                    [Europe PMC]
(Ppara OR PPARalpha) AND (Muller OR "retinal pigment epithelium" OR photoreceptor)
  AND (conditional knockout OR Cre OR floxed) AND retina
PPARA conditional knockout retina OR retinal
Pparaflox retina
"Pparafl/fl" retina
Cx3Cr1-Cre Ppara retina
Vecad-Cre Ppara OR "VE-cadherin-Cre" Ppara retina
```

**Claim 2 queries:** listed in §2 above.
**Claim 3 queries:** listed in §3 above.

**Not searched in this pass** (identified as specific follow-ups, not exhausted):
MGI/IMPC allele-level cross-check for undisclosed *Ppara* conditional strains (attempted;
the MGI marker page fetch failed on an incomplete HTTP read and was not retried under budget
— this is a tooling gap, not a negative result, and should be retried); FDA/EMA
Drugs@FDA pharmacology-toxicology review archives for fenofibrate/pemafibrate
whole-body-autoradiography eye data; conference-abstract-only veterinary-ophthalmology
fibrate toxicology reports (searched via the same Europe PMC queries, which do index EASD/
ARVO abstracts, but none surfaced).

---

## 6. SUMMARY TABLE FOR STEP 8 (the report rewrite)

| REPORT.md position | Status after this step |
|---|---|
| §6.5 "conditional deletion's continued absence is itself informative" | **False. Struck.** Two conditional deletions exist (2022, 2026), both show the predicted direction of necessity, confound-free by design. |
| §6.5 circularity of citing the global KO | **Resolved for endothelium and microglia; still open for RPE/photoreceptors/Müller glia** — and those are the higher-PPARA compartments. |
| §6.1 "aqueous ANGPTL4... same tap" (implies unmeasured) | **Confirmed still unmeasured.** This proposed experiment is still novel and still worth running. |
| §6.1 "free drug concentration in retinal tissue... never measured in any species" | **False for local/parenteral dosing** (measured repeatedly, with numbers, since 2019). **True for oral dosing with a quantified value** — one reported oral attempt found it below detection; no bounded concentration exists for oral/systemic dosing in any species or for any human sample. |
| §6.6 item 7 "Conditional retinal receptor deletion... Necessity" | **Partially complete.** Rescope to RPE/photoreceptor-specific deletion; do not re-cost as if starting from zero. |
| §6.2 "receptor-knockout arm" needed in the rodent transactivation/transrepression experiment | **Now available off-the-shelf** for endothelium and microglia (PPARαECKO, PCKO lines); still absent for RPE/photoreceptors. |

---

## Status — 2026-11-03 — step 4: verify the three claims of absent evidence

**Done.** Systematically searched PubMed (NCBI E-utilities, reusing
`src/analysis/fgf21_bridge/pubmed.py` and `pmc.py` unchanged from Step 3) and Europe PMC
(including preprints and conference abstracts, via its REST API) for each of the three
absence claims in REPORT.md §6.1/§6.2/§6.5, plus the global-knockout confound question in
§6.5. No code was written; this is a literature-verification step, and `data/holdout/`,
`data/processed-blinded-*/` and the UNBLINDING doc were not touched or read.

**Verified.**
- **Claim 1 (conditional *Ppara* retina deletion) — REFUTED.** Two published, peer-reviewed
  conditional knockouts exist: endothelial-specific (Xu et al. 2026, PMID 41485550,
  *Vecad-CreERT2*) and microglia-specific (Yuan et al. 2022, PMID 36497130, *Cx3Cr1-CreERT2*
  — four years before the analysis that asserted the absence). Both include gain-of-function
  controls and both were pulled in full text (PMC13084685, PMC9739170) and checked for Cre
  driver, confound controls, and ANGPTL4 content (none report ANGPTL4).
- **Claim 2 (intraocular ANGPTL4 × fibrate) — VERIFIED ABSENT.** No in vivo intraocular-fluid
  ANGPTL4 measurement stratified by fibrate exposure was found in any species, across 10
  distinct query strings. The nearest adjacent result (an in vitro ARPE19 mRNA study) was
  checked and does not qualify.
- **Claim 3 (fibrate concentration in retinal tissue/aqueous humour) — REFUTED for the literal
  claim, narrowed for the load-bearing one.** Four peer-reviewed studies (Huang 2021 PMID
  34943243; Kaffash 2026 PMID 41580131; Poudel 2026 PMID 41407273; Qiu 2019 PMID 30912953)
  measure fenofibrate/fenofibric acid in rodent retina, vitreous or aqueous humour by LC-MS,
  with reported numbers, via local or parenteral-systemic routes. No study was found
  quantifying ocular-tissue fibrate concentration after **oral** dosing in any species or in
  any human sample; one secondhand citation reports an oral-dosing attempt in rat eyes as
  below the assay's detection limit, which I could not independently verify to a primary PMID
  within this pass and have flagged as such rather than treated as confirmed.
- **Confound question — resolved for 2 of ≥5 retinal cell types.** The two conditional
  knockouts from Claim 1 each structurally exclude the global knockout's systemic confounds
  (hepatic PPARα, and therefore triglycerides/ketogenesis/FGF21, is intact in both) and each
  still reproduce a worsened diabetic retinal phenotype. This settles the circularity concern
  for endothelium and microglia. It remains open for rods, cones, RPE and Müller glia — the
  higher-PPARA compartments per Step 2 — where no conditional model exists.

**Corrections and honesty notes made during the step.** Flagged one secondhand citation
(the Brown Norway oral-dosing non-detect) as not independently traced to a primary PMID,
rather than presenting it as confirmed. Flagged the MGI allele cross-check as attempted and
failed on a transport error, not as a negative result. Distinguished local/parenteral dosing
(measured) from oral dosing (not measured with a bounded value) throughout Claim 3, since
collapsing that distinction would repeat the exact error this chain exists to correct.

**What step 5 needs to know.**
1. The retinal exposure model should anchor its neural-retina partition-ratio prior against
   the Huang 2021 systemic(IP)-vs-topical ratio — a real measured data point, not merely an
   assumed range — while still treating the oral-dosing value as genuinely unconstrained.
2. Claim 1's refutation means Step 8's rewrite of §6.5 must drop the "absence is itself
   informative" framing entirely, not soften it.
3. §6.6 item 7 (conditional retinal receptor deletion, costed at $300–500k as if starting
   from zero) should be rescoped to RPE/photoreceptor-specific deletion only.

**Not done / limits.** FDA/EMA tissue-distribution archives for fenofibrate and pemafibrate
were not pulled. The MGI/IMPC allele database cross-check for Claim 1 did not complete (HTTP
transport error, not retried under budget) — the two peer-reviewed primary papers are
sufficient to refute the claim regardless, but a full allele-level sweep could surface
additional unpublished or IMPC-only conditional lines. No veterinary-ophthalmology fibrate PK
literature was found despite a dedicated query; this was treated as a negative result within
the search's coverage, not as proof of absence beyond it.
