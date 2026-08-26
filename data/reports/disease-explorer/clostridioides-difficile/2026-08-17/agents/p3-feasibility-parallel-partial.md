# Phase 3 — Clinical Feasibility Assessment (SECOND, PARALLEL AGENT) — PARTIAL

> **⚠️ PROVENANCE / WRITE-COLLISION NOTICE**
> A second Clinical Feasibility Assessor ran concurrently and wrote to the same
> path (`p3-feasibility.md`). The two reports were concatenated. This file
> preserves the parallel agent's surviving text.
>
> **Its opening section (`§0`, executive summary) was destroyed by the write
> collision and is NOT recoverable from disk** — the text below begins at its
> `§1` and contains forward references to `§0.2`/`§0.3` that no longer resolve.
> Re-request the full report from that agent if it is needed intact.
>
> The primary, complete report is `p3-feasibility.md`.

---


## 1. CROSS-CUTTING PARAMETERS THAT DRIVE EVERY ESTIMATE BELOW

Three things determine feasibility in CDI more than any candidate-specific property: how fast you can enrol, what probability of technical success you are honestly entitled to claim, and what a patient costs. All three are modelled here once, then applied uniformly in §3 so the candidates are compared on identical machinery.

**Notation.** **[modelled]** marks a number I derived from stated assumptions — it is auditable and re-runnable, and I show the inputs. **⚠️verify** marks a factual claim inherited from an upstream agent or my tasking that nobody in this pipeline has confirmed. The two are epistemically different and the report keeps them separate.

### 1.1 The recruitment model — CDI's binding constraint, quantified

My skill file treats recruitment as a favourable dimension. In CDI it is the dimension that sets trial cost, because cost ≈ (patients) × (per-patient cost) and *site count* ≈ (patients) ÷ (accrual rate), and accrual rate in a recurrent-CDI trial is startlingly low. Here is the funnel for the design §0.3 concluded is mandatory — **post-response randomisation, toxin-confirmed, add-on to SOC**:

| Gate | Pass rate | Remaining per 100 consecutive CDI diagnoses |
|---|---|---|
| CDI diagnosis of any kind at the site | — | **100** |
| **Toxin EIA-positive** (excludes PCR⁺/EIA⁻ colonisation and low toxin burden) | ~55% | 55 |
| Episode is a **recurrence** (1st or later) — the value-defining subtype (§1.5b) | ~25% | 14 |
| Survives exclusions: IBD, concurrent systemic antibiotics, prior FMT/LBP, pregnancy, life expectancy <3 mo, protocol-conflicting comorbidity | ~55% | 7.6 |
| **Consent obtainable** — patient competent, or LAR reachable, inside the window | ~65% | 4.9 |
| **Achieved clinical response to SOC and randomised inside the 24–72 h post-EOT window** | ~60% | **≈3.0** |

**≈3 randomisations per 100 CDI diagnoses.** **[modelled]**

A mid-size academic centre diagnoses 80–150 CDI episodes/year, which yields **2.4–4.5 randomisations/site/year ≈ 0.20–0.38 patients/site/month.** **[modelled]**

That model is calibrated, not invented: it reproduces the observed geometry of the trials that succeeded. ECOSPOR III enrolled ≈281 patients across ≈75 sites over roughly 2 years ⚠️verify — about **0.16 patients/site/month**, at the pessimistic end of my range, which is what you would expect of a trial with a bowel-prep requirement on top of the funnel above.

**Consequences that follow directly, and that no upstream agent priced:**

| Trial size | Site-years required | Realistic construction | Enrolment duration |
|---|---|---|---|
| n = 150 (Phase 2) | 33–63 | 25–40 sites | 15–24 mo |
| n = 300 (one Phase 3) | 67–125 | **60–90 sites** | **24–36 mo** |
| n = 600 (two Phase 3) | 133–250 | 90–150 sites, multi-national | 30–42 mo |

Add 6–9 months of site activation before the first patient. **A two-trial Phase 3 package in recurrent CDI cannot be enrolled in under about 3.5 years at any realistic site count** — and site count is the dominant cost driver in a trial with cheap procedures and expensive logistics. This is why every timeline in §3 that involves a treatment indication lands at 6+ years no matter how clean the regulatory path is.

#### 1.1.1 The toxin-EIA decision, resolved arithmetically

Toxin-EIA enrolment nearly halves the eligible pool, and there is a standing temptation to enrol on PCR alone to accelerate. The trade is calculable rather than a matter of taste.

Suppose PCR-only enrolment raises the pool from 55% to ~95% of diagnoses (**1.7× faster accrual**) but ~25% of those enrolled have colonisation or non-toxin-mediated diarrhoea and therefore contribute approximately zero treatment effect. Effect size is diluted by 25%, and required sample size scales as the inverse square of effect size:

```
n_PCR / n_EIA  ≈  1 / 0.75²  ≈  1.78×
```

**[modelled]** So you gain 1.7× on accrual rate and lose 1.78× on required n. **Calendar time is a wash; cost rises ~78%; and the probability of a failed trial rises, because dilution biases toward the null.** Every design in §3 therefore enrols toxin-EIA-positive patients. The one exception is ribaxamase, whose endpoint is *incident* CDI and which must use whatever diagnostic standard the participating hospitals actually run — a real and under-appreciated source of endpoint noise for that programme (§3.1).

### 1.2 The PTS framework — how CDI's 36% translation rate is applied

My tasking instructs me to incorporate CDI's 36% preclinical→clinical translation rate (6,918 paired samples) ⚠️verify. The debate round established the correct way to do that: the base rate is **conditioned** (it is dominated by antibacterial replacement me-toos), but two of its components are **mechanism-independent** and apply flat — the sustained-response endpoint penalty (SRC −0.20, p=1.5×10⁻⁵⁴) and the young-animal penalty. I implement this as a multiplicative chain rather than a single haircut, so that each candidate's discount is traceable to a named property:

```
PTS  =  B  ×  E  ×  T  ×  Y  ×  C
```

| Factor | Meaning | Values used |
|---|---|---|
| **B** — positioning base rate | Phase 1→approval, conditioned on positioning, not on disease | Replacement antibacterial in CDI **0.10**; add-on repurposed agent with human safety in hand **0.30–0.40**; primary prevention with positive human Phase 2 **0.45–0.55**; NCE on an unprecedented axis **0.15** |
| **E** — endpoint penalty | Applies iff the primary is sustained response / recurrence at 30–90 d | **0.75** if yes, **1.00** if the primary is incidence or initial cure |
| **T** — evidence-tier translation | The 36% figure, resolved by tier | Human Phase 2 positive **1.00**; two-lab rodent **0.55**; single-lab mouse **0.45**; hamster only **0.35**; in vitro only **0.20** |
| **Y** — young-animal penalty | Applies iff the supporting efficacy data is rodent | **0.85** if rodent-derived, **1.00** if human |
| **C** — candidate-specific serial gates | Formulation, CMC, redox stability, selectivity, class-level questions — each an independent pass/fail | Product of named gate probabilities, stated per candidate |

Two disciplines this imposes. First, **T and Y are not applied to candidates whose best evidence is human** — that is the conditioning the debate demanded, and it is the single largest reason ribaxamase separates from the field. Second, **C is where most of the variance lives**, and it is where the report earns its keep: a candidate with three unresolved serial gates at 50% each has already lost 87% of its value before a single clinical dollar is spent, however good its mechanism.

**A note on what PTS is not.** PTS is probability of *technical* success — reaching approval. It says nothing about whether the approved product survives. In CDI those are close to independent questions, and the second one is where the field's corpses are (§0.4). I therefore report both, and the number that should drive capital allocation is the product:

```
P(marketed and still marketed at +5 yrs)  =  PTS  ×  P(commercial survival)
```

### 1.3 Cost basis

Per-patient costs, which I apply uniformly:

| Trial type | Fully-loaded cost/patient | Why |
|---|---|---|
| **rCDI treatment / add-on, 8–12 wk follow-up** | **$50–90K** | Cheap procedures, expensive logistics: 60–90 sites, high screen-failure ratio (§1.1 — you screen ~33 to randomise 1), central toxin lab, blinded endpoint adjudication, 90-day follow-up tail in a population with high interim mortality |
| **Primary prevention, inpatient, short follow-up** | **$20–30K** | Enrolment at admission, drug given during an existing admission, endpoint is an event captured by routine hospital diagnostics, follow-up 4–8 wk |
| **Phase 2 dose-finding, same population** | **$60–100K** | Same logistics, smaller n, more sampling |

⚠️verify on all three — these are calibrated to published anti-infective Phase 3 per-patient benchmarks adjusted upward for CDI's screen-failure ratio and follow-up length, and they are the single most consequential assumption in the report. Note that they **reconcile a discrepancy in the upstream reports**: the Clinical Landscape agent's "$300M–1B" for a replacement-positioned NCE assumed two Phase 3 trials of 550–650 plus a complete de-novo NCE package; at $50–90K/patient two such trials cost $60–115M in direct clinical spend, and the rest of that figure is CMC, nonclinical, regulatory and years of corporate burn. Both numbers can be right; they are measuring different things, and §3.5 states which is which.

---

## 2. COMMERCIAL SURVIVAL — THE SCORE THAT MATTERS MOST IN THIS DISEASE

§0.4 established that CDI's commercial failure mode is benefit-capture mismatch, not market size. This section turns that into a number per candidate, because a programme with 40% PTS and 15% commercial survival is worth less than one with 20% PTS and 65%.

### 2.1 Ribaxamase — quantifying the one candidate where buyer and beneficiary coincide

Everything about the ribaxamase commercial case rests on a single structural fact, and it is worth doing the arithmetic rather than asserting it.

| Line item | Value | Source / basis |
|---|---|---|
| Incremental cost of one hospital-onset CDI case (attributable LOS + treatment + isolation) | **$20,000–30,000** | Health-economics range in general circulation ⚠️verify |
| CDI incidence in inpatients receiving IV β-lactams, 4–8 wk horizon | **2–4%**; **5–6%** in an enriched high-risk stratum | ⚠️verify; enrichment definition in §3.1 |
| Cases avoided per 100 treated, at 50% relative reduction, enriched stratum | **≈2.75** | **[modelled]** from 5.5% → 2.75% |
| Gross avoided cost per 100 treated | **$55,000–82,500** | **[modelled]** |
| **Break-even price per course** | **$550–825** | **[modelled]** |

**[modelled]** So a course priced at $300–600 is cost-*saving* to the hospital on the direct-cost line alone, before counting two further levers that fall on the same P&L:

- **HACRP.** CDI standardised infection ratio is a scored domain in the CMS Hospital-Acquired Condition Reduction Program, and bottom-quartile hospitals forfeit **1% of all Medicare inpatient payments** ⚠️verify. For a hospital with $200M of Medicare inpatient revenue that is a **$2M** annual cliff that a CDI-rate intervention bears directly on. No pharmacy-budget analysis captures this, and it is worth more than the drug's entire direct-cost case at hospitals near the threshold.
- **Readmissions.** CDI recurrence drives 30-day readmission, itself penalised.

**Why this matters more than any efficacy argument in the report.** Bezlotoxumab worked — ~10 percentage points of absolute recurrence reduction, approved, labelled — and was discontinued, because it was billed to a payer through prior authorisation while the hospital banked the savings. Ribaxamase is bought by a hospital pharmacy, administered inside a DRG-bundled admission, and the avoided cost lands on the same institution's ledger in the same fiscal year. **It is the only candidate in this set that is sold to the entity that benefits.**

The honest counterweight, stated with equal force: **prophylaxis pricing is the hardest pricing in medicine**, because you are invoicing for an event that did not happen, and the buyer sees 100 courses for every ~3 cases avoided. Hospitals discount avoided-cost arguments heavily, formulary committees are conservative about routine prophylaxis, and antibiotic-stewardship pharmacists may reasonably object to co-administering an enzyme that destroys the antibiotic they just selected — a cultural objection that is not in any upstream report and that I regard as a genuine adoption risk. The mitigation is stratum restriction: **do not seek "everyone on IV β-lactams," seek the enriched high-risk stratum**, where the number-needed-to-treat is defensible to a formulary committee and where the trial is also cheapest (§3.1).

### 2.2 Commercial survival scores for the full set

| Candidate | Channel | Buyer = beneficiary? | Exclusivity | Genericisation exposure | **P(survival at +5 yr)** |
|---|---|---|---|---|---|
| **Ribaxamase** | Hospital pharmacy, inpatient, DRG-bundled | **Yes** | 12 yr BLA reference-product | **None** — biologic, no ANDA; biosimilar economics poor at this scale | **60–70%** |
| **CamSA** | Retail/specialty, post-SOC, immunocompromised-first | No | 5 yr NCE, **10 yr with QIDP** (§0.2) | Moderate — cheap synthesis invites generics at exclusivity expiry | **40–50%** |
| **Niclosamide** | Retail, add-on anti-toxin — **the bezlotoxumab channel** | No | 3 yr new-dosage-form + formulation patents | High — API is a 1982 commodity; only the enabling formulation is protectable | **25–35%** |
| **Ibezapolstat** | Retail, replacement antibacterial | No | 5 NCE + 5 QIDP = 10 yr ⚠️verify | Low during exclusivity, but **comparator is genericising fidaxomicin** | **20–30%** |
| **UDCA** | Retail generic | No | 3 yr (8 with QIDP, §0.2) | **Total** — off-label prescribable the day the Phase 3 publishes | **10–15%** |
| **Berberine** | Already available as a supplement under DSHEA | No | **None** | **Total, and already realised** | **<10% as a product** |

**Read the last column against the first.** The two candidates my tasking scores highest after ribaxamase (niclosamide 6.5, CamSA 6.3) have middling commercial survival, and the two cheapest-to-develop (UDCA, berberine) have essentially none. **In CDI, development cost and commercial survival are inversely correlated across this candidate set**, which is the same anti-correlation §0.2 found for regulatory incentives. That is not a coincidence — it is the disease's economics, and it means the portfolio cannot be built by picking the cheapest path.
