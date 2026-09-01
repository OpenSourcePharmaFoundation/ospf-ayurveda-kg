# Phase 3 — Candidate Ranker (FINAL EVALUATION)

**Disease:** *Clostridioides difficile* infection (CDI)
**Date:** 2026-08-17
**Evidence base:** 13 agents / 3 rounds (Phase 1 ×6, Phase 2 ×5, Debate ×2)
**Reproducible scoring:** `scoring/p3_rank.py`, `scoring/p3_sens.py` (run with `python3`, no dependencies)

---

## 0. EXECUTIVE SUMMARY

**The post-debate ranking is REVISED, not validated.** Applying the four methodological instructions literally — score on sustained response, do not average, discount symmetrically, treat redox as a gate — reorders the middle of the table and compresses the bottom. Three changes are material:

| Change | From | To | Driver |
|---|---|---|---|
| **Ibezapolstat rises to #2** | 6.2 (#4) | **6.25 (#2)** | It is one of only **two** assets with human data. Once the discount schedule is applied symmetrically, human evidence is the only thing that survives it — and the C2-graveyard objection is a *modifier*, which the ±1.5 cap prevents from outvoting an evidence advantage. |
| **Niclosamide falls to #3** | 6.5 (#2) | **4.75 (#3)** | The coupled efficacy/safety filter, applied as a **structural defect** rather than as a weighted safety score, costs it 1.75 points. The Devil's Advocate's 70% kill probability survived the debate; a surviving refutation cannot be outvoted by a mechanistic package. |
| **CamSA falls to #4** | 6.3 (#3) | **4.50 (#4)** | Its case is chemistry, and chemistry is a **modifier** under instruction #2. Its efficacy anchor is 3.0. This is also the ranking's single largest sensitivity — see §6. |

**What does NOT change:** Ribaxamase remains #1 and the recommendation remains **acquire, gated on the $150–300K diligence pass**. Ebselen, conessine and aprepitant remain dead; ebselen is now formally **disqualified on the redox gate** rather than merely low-ranked.

**The finding that matters more than the ranking:** after symmetric discounting, **the dimension that separates candidates is evidence tier — not mechanism, not chemistry, not safety, not axis position.** Eight of ten candidates are capped below 7.0 before a single modifier is applied. The two that are not are the two with human data. This is not a coincidence to be scored around; it is the pipeline's actual result, and it points the strategy at *acquiring evidence* rather than at *acquiring molecules*.

---

## 1. METHODOLOGY — AND WHY IT IS NOT THE SKILL FILE'S

### 1.1 The default MCDA is invalid here, by instruction

The candidate-ranker skill file specifies `Composite = Σ(dimension_score × weight)` across eight dimensions. **That formula is what the Devil's Advocate scored at 90% kill probability, and Integration concurred.** A weighted sum permits four mediocre-but-positive dimensions to outvote one refutation — precisely how UDCA reached 7.5 on pathway position (7.5), chemistry (7.5) and regulatory speed (6.9) while Literature had refuted it at 3.0.

The methodology is therefore replaced, not tuned:

```
  Composite = EfficacyAnchor + clamp( Σ modifiers , −1.5 , +1.5 )

  EfficacyAnchor = evidence-tier ceiling − itemised, named efficacy deductions
  Modifiers      = axis position · compartment/chemistry · safety
                   · regulatory & capital · traditional use
```

**The ±1.5 clamp is the entire mechanism.** It encodes "adjudicate on efficacy first, use everything else as a modifier" as an arithmetic constraint rather than an intention. No combination of favourable chemistry, regulatory speed and pathway elegance can move a candidate more than 1.5 points off its evidence base. The clamp **binds** for five candidates (Ibezapolstat, CamSA, UDCA, Ebselen, Conessine) — meaning that for half the set, the old averaging method was doing real work that is now correctly suppressed.

### 1.2 Gates — applied before scoring, three-state

Per instruction #5, redox stability is a **gate**, not a weighted criterion.

| Gate | States | Effect |
|---|---|---|
| **G1 — Redox at Eh ≈ −200 mV** | PASS / CONDITIONAL / FAIL | FAIL = disqualification. CONDITIONAL (reducible group present, but *in vivo* counter-evidence exists) = −0.3 modifier + a named gating experiment. |
| **G2 — Coupled efficacy/safety** | NO / INVERTED / SERIOUS / FATAL | FATAL = disqualification (therapeutic-index reasoning is formally invalid). SERIOUS = −1.0. INVERTED = +0.5. |
| **G3 — Compartment coherence** | K1 luminal / K2 colonocyte-intracellular / K3 systemic | Scored *before* bioavailability, per instruction #6. Inverted ADMET applies to K1 only. |
| **G4 — §4.5 duplication** | — | Does the candidate repeat a documented failure? Priced into the anchor as base-rate evidence, not as a modifier. |

**Notation warning — two independent "C" schemes are in play across the upstream reports, and conflating them is easy:**

| Scheme | Source | Meaning |
|---|---|---|
| **C1–C8** | Pathway Analyst's causal-axis decomposition | C1 germination · C2 vegetative fitness · C3 toxin regulation · C4 intoxication · C5 host inflammation · C6 barrier/repair · C7 ecological restoration · C8 sporulation |
| **K1–K3** *(renamed here)* | ADMET Predictor's compartment model, written as "C1/C2/C3" upstream | K1 luminal · K2 colonocyte-intracellular · K3 systemic |

This report uses **C** for axes and **K** for compartments throughout. The renaming is mine and should be propagated — "niclosamide's target is C2, not C1" (round2-synthesis.md:139) means *compartment*, while "ibezapolstat adds nothing to C2" (round2-synthesis.md:32) means *axis*. These are different claims about different things and currently read as if they were the same.

### 1.3 Evidence-tier ceilings — the anchor's upper bound

The Literature Reviewer's schedule (`p2-literature.md` §8) verbatim, extended upward for human tiers:

| Evidence configuration | Ceiling |
|---|---|
| Positive human Phase 2b on a hard clinical endpoint | 8.0 *(extension)* |
| Independently replicated mouse **recurrence** model, therapeutic dosing, epidemic strain | 7.0 |
| Positive human Phase 2, small n, endpoint of interest untested | 6.5 *(extension)* |
| Single-lab mouse recurrence/survival, therapeutic dosing, epidemic strain | 6.5 |
| Single-lab mouse, prophylactic dosing, lab strain, no survival endpoint | 4.0 |
| Hamster survival/prophylaxis only | 3.5 |
| Purified-toxin instillation only | 2.5 |
| *In vitro* only | 2.0 |

**Symmetric application (instruction #3) is implemented as follows:** a negative result carries the *weight of its own instrument*. UDCA's hamster null is a 3.5-grade instrument, underpowered ~3× (5/8 vs 5/8, p=0.78, n≈27/arm required). It is therefore **not scored as a refutation at all** — it neither raises nor lowers UDCA's anchor. UDCA's anchor is set by its *positive* evidence, which is *in vitro* (2.0). The negative study does not sink it; the absence of positive *in vivo* evidence is what holds it at 2.5.

This is the honest reading, and note that it is **worse for UDCA than a partial-credit approach would be** — symmetric discounting protects UDCA from the refutation but does not manufacture evidence in its place.

### 1.4 Two flat penalties that survive base-rate conditioning

The Devil's Advocate's Concern 3 was partially blunted but survived. Integration accepted that two components are **mechanism-independent properties of the measurement**, apply flat, and had never been applied:

- **Sustained-response endpoint penalty: −0.50.** The strongest negative correlate of preclinical→clinical translation (SRC −0.20, p = 1.5 × 10⁻⁵⁴). Every candidate here is scored on durability.
- **Young-animal penalty: −0.25.** Every rodent study in the corpus used young laboratory animals; the §3.1 population is elderly, immunosenescent and polypharmaceutical.

Applied to all preclinical-only candidates. Ribaxamase escapes both (human data, incidence endpoint); ibezapolstat escapes the second and partly the first.

---

## 2. FINAL COMPOSITE SCORES

```
CANDIDATE    | CEIL | ANCHOR | MOD raw | MOD appl | COMPOSITE | REDOX GATE  | COUPLED FILTER
------------------------------------------------------------------------------------------------------
Ribaxamase   |  8.0 |   6.50 |    1.20 |     1.20 |      7.70 | PASS        | NO
Ibezapolstat |  6.5 |   4.75 |    1.70 |     1.50 |      6.25 | PASS        | NO
Niclosamide  |  6.5 |   5.75 |   -1.00 |    -1.00 |      4.75 | CONDITIONAL | YES (serious, structural)
CamSA        |  4.0 |   3.00 |    1.70 |     1.50 |      4.50 | PASS        | NO (inverted - favourable)
Berberine    |  7.0 |   5.00 |   -0.85 |    -0.85 |      4.15 | CONDITIONAL | NO
UDCA         |  2.0 |   2.50 |    1.90 |     1.50 |      4.00 | PASS        | NO
TUDCA        |  2.0 |   1.50 |    0.80 |     0.80 |      2.30 | PASS        | NO
Aprepitant   |  2.5 |   1.50 |   -0.50 |    -0.50 |      1.00 | PASS        | NO
Ebselen      |  4.0 |   1.75 |   -2.00 |    -1.50 |      0.25 | FAIL        | YES (fatal)
Conessine    |  2.0 |   1.00 |   -1.80 |    -1.50 |     -0.50 | n/a         | n/a
```

### 2.1 Ranking with confidence and cost-of-being-wrong

The composite scores *quality of the bet*. It does not score *what it costs to be wrong* — and in CDI, where 6 of 12 programme failures were financial, that second column changes decisions. Both are shown.

| Rank | Candidate | Composite | Δ vs post-debate | Confidence | Cost of being wrong | Disposition |
|---|---|---|---|---|---|---|
| — | *Fidaxomicin (SOC)* | *9.0* | — | *HIGH* | *n/a* | *Benchmark, not fundable* |
| **1** | **Ribaxamase** *(in-license)* | **7.70** | ⬆ +0.20 | **MODERATE** on score; **LOW–MOD** on specifics | **$150–300K to find out** | **FUND the diligence, then the programme** |
| **2** | **Ibezapolstat** | **6.25** | ⬆ +0.05, **⬆⬆ 2 ranks** | **MODERATE–HIGH** | **$80–150M — only a Phase 3 resolves it** | **Do not fund. Highest score-to-risk mismatch in the set.** |
| **3** | **Niclosamide** | **4.75** | ⬇ −1.75, ⬇ 1 rank | **MODERATE** | $140–270K to gate | Gate on two experiments; best *second* programme if both pass |
| **4** | **CamSA** *(NCE)* | **4.50** | ⬇ −1.80, ⬇ 1 rank | **LOW** — widest sensitivity band | $50–100K to reclassify | **Resolve the evidence tier before ranking it at all** |
| **5** | **Berberine** | **4.15** | ⬇ −1.35 | **MODERATE** | $150–300K to disconfirm | Keep, do not lead; pair with fidaxomicin, never vancomycin |
| **6** | **UDCA** | **4.00** | ⬇ −1.50 | **LOW–MODERATE** | $1–3M option | **Buy the option, not the programme** — the score's *structure* proves this |
| 7 | TUDCA | 2.30 | ⬇ −3.20 | LOW | — | Formulation contingency inside UDCA, not a separate asset |
| 8 | Aprepitant | 1.00 | ⬇ −2.00 | MODERATE | — | **DEAD** — evidence anchored on the disproven toxin |
| — | **Ebselen** | **0.25** | ⬇ −3.75 | **HIGH** | — | **DISQUALIFIED — G1 redox FAIL + G2 FATAL** |
| — | **Conessine** | **−0.50** | ⬇ −2.50 | **HIGH** | — | **DISQUALIFIED — RED safety + hypothesis falsified** |
| — | Bezlotoxumab | n/a | — | HIGH | — | **WITHDRAWN** Jan 2025 — C4 is empty white space |
| — | *urso-CamSA (U-3)* | *not ranked* | — | — | $50–150K | **Not a candidate — a synthesis line item inside the CamSA programme.** It has never been made; it has no efficacy evidence to anchor. Ranking it at 6.0 gave a hypothetical the standing of an asset. |

**Two structural readings of this table that matter more than the ordering:**

1. **Composite and cost-of-being-wrong are anti-correlated at the top.** #1 costs $150–300K to test; #2 costs $80–150M and is only resolvable in Phase 3. On expected value, the gap between ribaxamase and ibezapolstat is far wider than 1.45 points.
2. **UDCA's score shape is itself the recommendation.** Anchor 2.5, modifiers capped out at the +1.5 maximum. An asset whose value lives almost entirely in *optionality* (axis, regulatory speed, population access) rather than in *evidence* is, definitionally, an option — not a programme. Integration reached "buy the option, not the programme" by judgement; the scoring structure derives it.

---

## 3. CANDIDATE SCORECARDS

Axis coverage bars use the C1–C8 causal decomposition. `██` = strong, `▓▓` = partial, `░░` = none.

### ═══ #1 — RIBAXAMASE (SYN-004, Theriva) — in-license, not a repurpose ═══

```
COMPOSITE 7.70/10  │  RANK #1  │  CONFIDENCE: MODERATE (LOW–MOD on specifics)
Anchor 6.50  +  Modifiers +1.20 (uncapped)

Axis:  C1 ░░  C2 ░░  C3 ░░  C4 ░░  C5 ░░  C6 ░░  C7 ██  C8 ░░     Compartment: K1 luminal
Phase: 0 ██   1 ░░   2 ░░   3 ░░   4 ░░   5 ░░   6 ░░              Gates: G1 PASS · G2 NO · G3 exact
```

| Component | Value | Justification | Source |
|---|---|---|---|
| Tier ceiling | 8.0 | Positive human **Phase 2b**, hard endpoint (new-onset CDI incidence) | p2-repurposing.md §4.9 |
| − Unverified package | −1.00 | **Verified by nobody in this pipeline.** Flagged "⚠verify" | debate-integrator.md §5, §8 |
| − Population ceiling | −0.50 | β-lactam-driven CDI only; FQ/clindamycin untouched, never quantified | debate-integrator.md §5 counter-case 3 |
| **Anchor** | **6.50** | | |
| + Axis #70/C7 | +1.00 | **Sole occupant.** The only loop-*entry*-preventing asset; zero candidates on this axis | p2-pathway.md; §5.5 Tier 1 |
| + Compartment | +0.30 | K1 luminal, target *is* the luminal β-lactam — exact match; no redox-fragile pharmacophore | §6.2 |
| + Safety | +0.50 | Zero systemic exposure → near-zero DDI in a polypharmacy population | §6.4, p2-safety.md §7.3 |
| − Regulatory/capital | −0.60 | BLA, enzyme CMC, no RLD, large prevention Phase 3, prophylaxis payer logic | p2-repurposing.md:123, 162 |

**Why it wins — stated as the four things that kill CDI programmes:**

| Field-wide failure mode | Exposure |
|---|---|
| Initial-cure non-inferiority bar (killed 8 programmes) | **Escapes entirely** — never competes on cure |
| Sustained-response endpoint (SRC −0.20, p=1.5×10⁻⁵⁴) | **Escapes** — endpoint is incidence |
| Diarrhoea-endpoint confound (afflicts every bile acid) | **Escapes** — a luminal enzyme has no such axis |
| 36% preclinical translation rate | **Largely escapes** — already human-positive |
| Financial failure (6 of 12) | **This is why it is available.** A capital defect is correctable; a pharmacodynamic one is not |

**KEY STRENGTHS:** The only asset in the analysis whose best evidence is human rather than rodent. Occupies the one axis that *exits* the recurrence loop rather than suppressing within it, and the candidate set contains no other primary-prevention asset at all.

**KEY RISKS:** The Phase 2b design and results are unverified — the top recommendation rests on an unconfirmed claim, which is exactly why it is gated rather than committed. Acquisition cost unknown. Enzyme BLA CMC is harder than any small molecule here. Prophylaxis reimbursement is genuinely difficult: you are asking a payer to fund an event that does not happen.

**NEXT STEP:** $150–300K diligence pass, 3–4 months. **0.2% of the programme it gates.**

---

### ═══ #2 — IBEZAPOLSTAT (ACX-362E) ═══

```
COMPOSITE 6.25/10  │  RANK #2  │  CONFIDENCE: MODERATE–HIGH
Anchor 4.75  +  Modifiers +1.50 (raw +1.70 — CAP BINDING)

Axis:  C1 ░░  C2 ██  C3 ▓▓  C4 ░░  C5 ░░  C6 ░░  C7 ▓▓  C8 ░░     Compartment: K1 luminal
Phase: 0 ░░   1 ░░   2 ██   3 ▓▓   4 ░░   5 ░░   6 ░░              Gates: G1 PASS · G2 NO · G3 exact
```

| Component | Value | Justification | Source |
|---|---|---|---|
| Tier ceiling | 6.5 | Human Phase 2, ~50–60 subjects, endpoint of interest untested | debate-integrator.md §2.5 |
| − Non-inferiority bar | −1.50 | **Initial-cure NI vs an 85–92% comparator is undemonstrated — and the axis base rate is 0-for-8** (ridinilazole, surotomycin, cadazolid, LFF571, DS-2969b, OPS-2071, ramoplanin, Ramizol). Filed in the anchor, not as a modifier: this is base-rate *evidence* about Phase 3 success, not pathway aesthetics | p2-literature.md:456 |
| − Endpoint | −0.25 | Recurrence claim rests on the untested sustained-response endpoint | Advocate Concern 3 |
| **Anchor** | **4.75** | | |
| + Axis net | +0.10 | C2 saturation −0.4; under-credited C7 bile-acid/microbiome touch +0.5 | p2-pathway.md:619 |
| + Compartment | +0.80 | **LSAS 9/10** — second only to fidaxomicin. Purpose-designed luminal delivery; redox-clean | p2-safety.md §7.3 |
| + Commensal data | +0.40 | **The only candidate in the entire set with measured commensal-spectrum data** — the field's largest blind spot | Round1 Gap #1, Lit Gap #2, Safety §8.6 |
| + Regulatory | +0.40 | FDA open to a single Phase 3; QIDP/GAIN eligible | p1-clinical-landscape.md |

**Why it moved up two ranks — and why that is not an endorsement.** Ibezapolstat rises for one reason: it has human data, and symmetric discounting is brutal to everything that does not. Its rise is a statement about *the rest of the field*, not about ibezapolstat.

**KEY STRENGTHS:** DNA pol IIIC has no *Bacteroidetes* homolog and no human homolog. It is the only asset that has already answered the question every other candidate ducks. Cheapest clear regulatory path in the set.

**KEY RISKS:** A ninth entrant on an eight-programme graveyard axis, facing the exact bar that killed the eighth. Total human exposure ~50–60 subjects. **The decisive question is answerable only in Phase 3** — making it, per §2.1, the single worst score-to-risk mismatch in the analysis.

**NEXT STEP:** **Do not fund.** Track it. If a third party runs the Phase 3 and clears the NI bar, the asset re-rates immediately and can be evaluated then at a fraction of the risk.

---

### ═══ #3 — NICLOSAMIDE ═══

```
COMPOSITE 4.75/10  │  RANK #3  │  CONFIDENCE: MODERATE
Anchor 5.75  +  Modifiers −1.00

Axis:  C1 ░░  C2 ░░  C3 ░░  C4 ██  C5 ▓▓  C6 ░░  C7 ▓▓  C8 ░░     Compartment: K2 colonocyte
Phase: 0 ░░   1 ░░   2 ░░   3 ░░   4 ██   5 ▓▓   6 ░░              Gates: G1 CONDITIONAL · G2 SERIOUS
```

| Component | Value | Justification | Source |
|---|---|---|---|
| Tier ceiling | 6.5 | Single-lab mouse **recurrence + survival**, therapeutic dosing, epidemic strain. 100% vs 45% survival; 100% vs >60% moribund in the vancomycin recurrence model; microbiota preserved | Tam et al., *Nat Commun* 2018;9:5233 |
| − Endpoint / young animal | −0.75 | Flat, mechanism-independent | Advocate Concern 3 |
| **Anchor** | **5.75** | **Highest preclinical anchor in the set** | |
| + C4 white space | +0.70 | Bezlotoxumab withdrawn → the redundancy deduction is **void**. Strain-agnostic, covers TcdA/TcdB **and CDT**. But endosomal escape is *downstream of the receptor-binding branch* — misses the NOX1 necrosis arm | debate-integrator.md §2.3 |
| + Compartment | +0.20 | K2 coherent — "high uptake, low systemic" is a **metabolic-clearance spec** (UGT/SULT), not a permeability one. The insolubility paradox is retired | p2-sar.md §2.7 |
| − **G1 CONDITIONAL** | −0.30 | Nitro is reducible at Eh −200 mV and **has never been measured**. Only *in vivo* counter-evidence (the Tam mouse gut was live and anaerobic) | Chemist, ADMET, Lit §11, SAR §2.8 |
| − **G2 SERIOUS** | −1.00 | **The protonophore that deacidifies endosomes is intrinsically a mitochondrial uncoupler.** Chemical coupling — unfixable by des-nitro *or* formulation. **The therapeutic index narrows as the patient gets sicker** | Safety Findings 4×5; Advocate Concern 2 (70%, survived) |
| − Regulatory | −0.40 | Contingent RLD; full CMC; 7–10 yrs; $75–140M | p2-repurposing.md |
| − Genotoxicity | −0.20 | Nitroso/hydroxylamine alert at **10–14× the anthelmintic cumulative dose** (20–28 g vs 2 g), in a population 15–25% of whom have active malignancy on DNA-damaging chemotherapy | debate-integrator.md §2.3 |

**Why it fell 1.75 points.** Nothing new was learned. The change is that the coupled filter is now applied as instruction #4 specifies — as a **structural defect in the mechanism**, not as one weighted safety dimension among eight. Under averaging, a −1.0 safety score against seven other dimensions moves the composite by ~0.15. Under this method it moves it by 1.0, and the redox and genotoxicity items are no longer diluted. **The Devil's Advocate's 70% kill probability survived the debate; a surviving refutation must not be outvoted by a mechanistic package, however good.**

**KEY STRENGTHS:** On every design axis that matters — epidemic strain, therapeutic dosing, dose-response, survival, recurrence, microbiota-sparing — the best-designed preclinical study in the set. Now the **only** small molecule with any claim on C4.

**KEY RISKS:** The uncoupling-vs-anti-TcdB selectivity ratio **does not exist**. Anaerobic colonic stability has never been measured. An inverted risk structure in the severe stratum specifically.

**NEXT STEP:** Two cheap gating experiments — selectivity ratio ($60–120K) and the fecal-slurry redox panel ($80–150K). **Both must pass.** A ratio >10× moves it to 5.45; a redox failure disqualifies it outright.

---

### ═══ #4 — CamSA (cholic acid *m*-aminobenzenesulfonamide) — NCE ═══

```
COMPOSITE 4.50/10  │  RANK #4  │  CONFIDENCE: LOW — widest sensitivity band in the analysis
Anchor 3.00  +  Modifiers +1.50 (raw +1.70 — CAP BINDING)

Axis:  C1 ██  C2 ░░  C3 ░░  C4 ░░  C5 ░░  C6 ░░  C7 ░░  C8 ░░     Compartment: K1 luminal
Phase: 0 ░░   1 ██   2 ░░   3 ░░   4 ░░   5 ░░   6 ░░              Gates: G1 PASS · G2 INVERTED
```

| Component | Value | Justification | Source |
|---|---|---|---|
| Tier ceiling | **4.0** | Mouse protection reported, **[EMERGING]**, single-lab. Dosing schedule, strain and endpoint are **not documented anywhere in this corpus** → scored conservatively per the skill file's "never inflate for missing data" | p1-target-profiler.md:258; p2-sar.md §6.3 |
| − Endpoint / young animal | −0.75 | Flat | Advocate Concern 3 |
| − Class validity | −0.25 | **"Can *any* anti-germinant hold against a replenished reservoir?" is unaddressed by anything in the analysis** | disease-model §2.3; integrator §7.1 |
| **Anchor** | **3.00** | | |
| + Axis C1 | +1.00 | Tier 1, near-empty; serves unmet need **#2** (spore reservoir) and **#1** (non-live) | §5.5, §4.6 |
| + **G1 PASS** | +0.50 | **Zero reducible groups.** Redox-clean by construction | p2-sar.md §6.3 |
| + **G2 INVERTED** | +0.50 | **The sulfonate that drives potency is the same group that guarantees non-absorption — same atom, same direction.** Integration called this "the strongest single argument for CamSA in this analysis" | debate-integrator.md §9 |
| + Safety | +0.30 | No systemic exposure, no DDI, cholic-acid derivative | §6.4 |
| − Regulatory | −0.60 | NCE, zero human exposure, full 505(b)(1), 9–12 yrs; partly offset by being **one amide coupling from a commodity API** | p2-repurposing.md |

**Why it fell 1.8 points, and why that may be an artefact.** CamSA's entire case is chemistry, and instruction #2 makes chemistry a **modifier**. Its modifiers max out the cap — the method is giving it everything it structurally can — and it still lands at 4.50 because the anchor is 3.00.

**But the anchor rests on a documentation gap, not on a finding.** Nobody in this pipeline recorded whether the CamSA mouse study used therapeutic or prophylactic dosing, an epidemic or lab strain, or a survival endpoint. If it is a tier-6.5 study, **CamSA scores 7.00 and ranks #2.** That is a 2.5-point swing turning on a literature question, and it is the single most valuable cheap thing left to check in the whole analysis. Do not rank CamSA before resolving it.

**KEY STRENGTHS:** ~1000× CDCA anti-germinant potency (knowledge-based, germination-assay). The only candidate whose efficacy and safety levers point the *same* way. Cheap to make.

**KEY RISKS:** The potency figure is an assay number, not an efficacy number. NCE timeline. And **there is a reason it stalled** — no sponsor has taken a cholic acid derivative forward, which usually means either an unpublished failure or no commercial case.

**NEXT STEP:** Two things, both cheap. (1) **Literature retrieval on the mouse study design** — free, and worth 2.5 points. (2) Bile-acid germination dose-response, $50–100K.

---

### ═══ #5 — BERBERINE ═══

```
COMPOSITE 4.15/10  │  RANK #5  │  CONFIDENCE: MODERATE
Anchor 5.00  +  Modifiers −0.85

Axis:  C1 ░░  C2 ▓▓  C3 ░░  C4 ░░  C5 ██  C6 ⚠  C7 ██  C8 ⚠      Compartment: K1 luminal
Phase: 0 ▓▓   1 ░░   2 ▓▓   3 ░░   4 ⚠   5 ▓▓   6 ░░              Gates: G1 CONDITIONAL · G2 NO
                                        ⚠ = DIRECTIONAL CONFLICT (negative contribution)
```

| Component | Value | Justification | Source |
|---|---|---|---|
| Tier ceiling | **7.0** | **Two independent labs, ten years apart, both positive, both in the recurrence configuration** (Lv 2015; IJAA 2025) — the best-replicated package in the set, in the add-on configuration that is 3-for-3 clinically | p2-literature.md |
| − Verification | −0.75 | Group sizes unverified; characterised from abstracts; natural-product publication bias | p2-literature.md:522 |
| − ***spo0A*** | −0.50 | **Sub-MIC *spo0A* upregulation directly contradicts the recurrence endpoint berberine is proposed for.** A mechanistic contradiction, so it is filed in the anchor, not as a safety modifier | debate-integrator.md §2.4 |
| − Endpoint / young animal | −0.75 | Flat | Advocate Concern 3 |
| **Anchor** | **5.00** | | |
| + Axis net | +0.10 | Exits the C2 graveyard into C5+C7+#72 enterococcal cross-feed (+0.5); **directional conflict on C6 via Wnt/anti-proliferative activity — the zero-coverage axis, which cannot absorb a negative contributor** (−0.4) | p2-pathway.md:620 |
| − Compartment | −0.45 | K1 confinement is real (A=4, equal to fidaxomicin); **G1 CONDITIONAL** — microbial reduction to absorbable dihydroberberine; cationic fecal binding, now largely **moot** under the host/microbiota reclassification | Chemist; p2-safety.md §7.3 |
| − Safety/DDI | −0.50 | **LSAS 6 — loses 3 of its 4 "free" points at the gut wall.** Real human DDI (cyclosporine +35% AUC) excludes CNI-transplant, digoxin and P-gp DOAC patients — over-represented in exactly this cohort | p2-safety.md §7.3 |
| − Comparator | −0.40 | No drug RLD; **zero human CDI data**; after reclassification its comparator is approved LBPs with FMT-class efficacy | debate-integrator.md §2.4 |
| + Traditional use | +0.40 | **Genuinely on-indication** — Ayurvedic/TCM use for infectious diarrhoea and dysentery, not a generic wellness claim. Scored against CDI symptoms per the re-anchoring instruction | p1-ethnobotany.md; §7.2 |

**Note on the record:** the "sub-MIC toxin induction at 6–12 h" claim was **fabricated by the synthesis fork** and appears in no source document. Toxin in fact *falls* at ½ MIC (TcdA −57%, TcdB −54%, comparable to vancomycin). The proposed hard stop does not trigger. That correction is a genuine **upgrade** which the Round 2 synthesis had inverted into a downgrade.

**KEY STRENGTHS:** Best-replicated preclinical package in the set, generated in the add-on configuration. Strongest and most on-indication traditional-medicine evidence of any candidate here.

**KEY RISKS:** *spo0A* works against the exact endpoint it is sold on. Biofilm enhancement with vancomycin at ½ MIC (p=0.02) — **in precisely the combination the mouse data supports.** And reclassification moved it out of a bad neighbourhood into one where approved incumbents outclass it.

**NEXT STEP:** The $150–300K *spo0A* in vivo disconfirming experiment before anything larger. **Pair with fidaxomicin, never vancomycin** — the biofilm signal is vancomycin-specific.

---

### ═══ #6 — UDCA (ursodiol) ═══

```
COMPOSITE 4.00/10  │  RANK #6  │  CONFIDENCE: LOW–MODERATE (genuinely unresolved)
Anchor 2.50  +  Modifiers +1.50 (raw +1.90 — CAP BINDING)

Axis:  C1 ██  C2 ▓▓  C3 ░░  C4 ░░  C5 ░░  C6 ░░  C7 ▓▓  C8 ░░     Compartment: K1 (escape fraction)
Phase: 0 ▓▓   1 ██   2 ▓▓   3 ░░   4 ░░   5 ░░   6 ░░              Gates: G1 PASS · G2 NO
```

| Component | Value | Justification |
|---|---|---|
| Tier ceiling | **2.0** | Best *positive* evidence is **in vitro** (strong, reproducible germination *and* growth inhibition), plus one n=1 case report |
| + Measured delivery | +0.50 | **43.5% of the fecal BA pool in the antibiotic-treated state** — and dysbiosis *increases* parent UDCA (≤4.28% without antibiotics). Measured, disease-relevant, favourable |
| **Anchor** | **2.50** | |
| *(negative hamster study)* | **0.00** | **Symmetric discounting, applied.** A 3.5-grade instrument, underpowered ~3× (5/8 vs 5/8, p=0.78; n≈27/arm needed), in replacement configuration against a 10⁴-spore bolus in an animal that cannot recover. It is **not scored as a refutation** — but neither does it supply positive evidence |
| + Axis C1 | +1.00 | Sole *clinical-stage* occupant; serves unmet need **#1** (non-live option for the immunocompromised) and **#2** |
| + Compartment | +0.20 | Redox-clean; delivery measured. But **43.5% of the *pool* is not free monomer** — fecal-water concentration has never been measured |
| + G2 clean | +0.20 | Efficacy and safety levers cleanly separated |
| + Regulatory | +0.30 | Approved generic, RLD exists, fastest/cheapest 505(b)(2) (+0.6); **negative-NPV for a commercial sponsor** — off-label prescribable the day after publication (−0.3) |
| + Safety | +0.20 | Well tolerated at PBC dose; ORANGE at 28–30 mg/kg (PSC trial harm) |

**The score's *shape* is the recommendation.** Anchor 2.50 with modifiers pinned at the +1.5 ceiling: nearly all of UDCA's value is optionality — axis position, regulatory speed, population access — and almost none is evidence. That is the definition of an option. **Buy the $1–3M Stage 0; do not buy the $45–85M programme.**

**Standing corrections carried forward:** (a) LSAS A=1 → **A=2**, raising UDCA's LSAS from 5 to **6** (the measured 43.5% governs over the "~90% absorbed, not a luminal drug" claim). (b) Colon-targeted UDCA, UDCA + IBAT inhibitor, and dose escalation are **permanently stood down** — they solve a delivery problem that does not exist in the dysbiotic patient, and the IBAT combination additionally shunts *taurocholate*, the germinant, to the colon. (c) The observational denominator appears as both 4/12 and 4/16; 25% is consistent only with 4/16. **Verify before citing externally.**

**NEXT STEP:** **Sequencing correction — Stage 0 as currently specified compares a fecal concentration to an anti-germination IC₅₀ that does not exist.** Run the $50–100K dose-response assay **first** so Stage 0 has a threshold to compare against.

---

### ═══ DISQUALIFIED — gate failures, not low ranks ═══

**EBSELEN (0.25) — G1 redox FAIL + G2 FATAL.** Not "ranked last"; **excluded**. The thiol-quenching reaction that destroys efficacy is the same reaction that liberates selenium (115–230 mg/day = **290–575× UL**). Dose escalation buys no efficacy and all of the toxicity, so therapeutic-index reasoning is formally invalid. Activity abolished by 5% blood; RT078 intrinsically resistant; Stickland metabolism *enhanced*, not inhibited.

> **The durable output is the class rule, and it outlives the compound:** *any warhead whose mechanism is exchange with a cysteine thiol will be consumed by millimolar free cysteine, glutathione and bacterial H₂S at Eh ≈ −200 mV before reaching target — and will have no selectivity if it does.* This generalises to auranofin (#21) and disulfiram, and constrains any replacement programme to **reversible-covalent chemistry with fast off-rates against small thiols and slow off-rates against target**, a **non-covalent** CPD inhibitor, or a **mucosally-activated prodrug**. **Target #26 remains Tier 1 and valid.**

**CONESSINE (−0.50) — RED safety, hypothesis independently falsified.** Four independent disqualifiers (H₃/CNS-active in a delirium-prone cohort where delirium independently predicts mortality; hERG/QT in a torsades-primed population; antimotility → megacolon; absorbed cationic) with **no surviving efficacy case** — the CspC pharmacophore hypothesis scored 0/3 structural elements.

**APREPITANT (1.00) — DEAD.** All efficacy evidence is anchored on **TcdA, the clinically disproven toxin** (§5.5 Tier 3). Triple CYP liability, LSAS 3 — "aprepitant *is* the DDI" in a polypharmacy population. Its one merit (a unique C5/NK1R arm, and the only touch on fulminant CDI) does not survive an anchor built on the wrong target.

**BEZLOTOXUMAB — WITHDRAWN** (Merck, Jan 2025). Invalid as a comparator. **Its withdrawal is the most consequential single fact in the competitive landscape:** C4 is now empty white space, and every deduction taken against another candidate for "C4 redundancy with bezlotoxumab" is void.

---

## 4. THE SINGLE STRONGEST FUNDABLE DEVELOPMENT PROGRAMME

> ## **Acquire and develop RIBAXAMASE, gated on a $150–300K diligence pass.**
> **Confidence: HIGH on the strategic logic. LOW–MODERATE on the specifics — which is exactly why it is gated rather than committed.**

**This validates the post-debate recommendation, and the Phase 3 methodology strengthens rather than weakens it.** Ribaxamase is the only candidate whose score survives symmetric discounting intact, because it is the only one whose evidence is human. Every competing asset lost 0.75–2.5 points to instruments that ribaxamase structurally escapes.

**The strategic diagnosis behind it, restated:** the binding constraint in CDI is **not candidate quality — it is axis allocation and capital structure.** Six of ten candidates crowd C2, where eight programmes have failed. C6 has zero coverage; C1/C3/C7/C8 have one each; C4 was just emptied. Meanwhile **6 of 12 CDI programme failures were financial, not scientific.** Read from a clinician's seat that is a graveyard; read from a business-development seat it is a **market inefficiency — positive Phase 2 data available below replacement cost.**

**The honest counter-case, carried forward in full and not softened:**

1. It is an **acquisition, not a repurpose** — unknown cost, and an enzyme **BLA** with harder CMC than any small molecule here.
2. Prevention indications need **large, expensive Phase 3s**; the $80–150M estimate excludes acquisition and is probably optimistic.
3. It prevents only **β-lactam-driven** CDI. Fluoroquinolone- and clindamycin-driven CDI are untouched, and **nobody in this pipeline quantified that ceiling.** (Scored: −0.50 on the anchor.)
4. **Payer logic for prophylaxis is genuinely hard** — funding an event that does not happen.
5. ⚠️ **The Phase 2b design and results have been verified by nobody.** The top recommendation rests on an unverified claim.

**What would change this recommendation:** evidence that the Phase 2b endpoint does not support a Phase 3, or that the β-lactam-only ceiling makes the market non-viable. Both are diligence questions, and both are answered by the same $150–300K.

**If diligence fails:** the fallback is the **C1 germination programme** — CamSA as the molecule, UDCA as the fast clinical probe, positioned for Combination B (immunocompromised) where there is no competing modality. **This is a genuinely different bet, not a consolation prize** — different axis, different failure mode, different population. But note §6: the entire C1 cluster shares one class-level failure mode, so it is *one* bet, not four.

---

## 5. PORTFOLIO CONSTRUCTION

### 5.1 Diversify by failure mode, not by mechanism

The standard error here would be to buy "an antibacterial, an anti-germinant and an anti-toxin" and call it diversified. Those three can share a failure mode (all luminal, all redox-exposed, all facing the same NI bar). The portfolio is constructed so that **no two funded bets fail for the same reason**:

| Bet | Axis | Dominant failure mode | Correlated with |
|---|---|---|---|
| Ribaxamase | C7 (loop entry) | **Commercial / regulatory** — payer logic, BLA CMC, addressable population | nothing else in the set |
| Niclosamide | C4 (intoxication) | **Pharmacological** — uncoupling selectivity, redox stability | ebselen (shared redox fragility — hence never pair them) |
| CamSA / UDCA | C1 (germination) | **Biological-class** — can any anti-germinant hold a reservoir? | **each other, completely** |

### 5.2 Staged allocation

**⬛ STAGE 0 — $700K–1.4M. Unconditional, and it precedes every asset decision.**

Buy information before buying assets. This resolves every live conflict in the analysis for **under 1% of a single programme's cost**, and the top three items alone can redirect the entire strategy.

| Priority | Experiment | Cost | Decides |
|---|---|---|---|
| 1 | **Ribaxamase Phase 2b diligence** | $150–300K | Confirms or destroys the #1 recommendation |
| 1b | **CamSA mouse-study design retrieval** ⭐ *new* | **~$0** | **Worth 2.5 points and 2 ranks. Free. Do it first.** |
| 2 | **Anaerobic fecal-slurry stability panel** (niclosamide, berberine, CamSA, UDCA, ± ebselen) | $80–150K | Four agents independently nominated it; **never done for any candidate.** Resolves G1 for the whole set at once |
| 3 | **Commensal-spectrum MIC panel** (Lachnospiraceae, Ruminococcaceae, Bacteroidetes) | $100–200K | The central §6.4 question; only ibezapolstat has this data |
| 4 | **Bile-acid germination dose-response** (UDCA / TUDCA / CDCA / CamSA / urso-CamSA) | $50–100K | First-ever UDCA IC₅₀; resolves the TUDCA conflict; **must precede UDCA Stage 0** |
| 5 | **Niclosamide selectivity ratio** (uncoupling vs anti-TcdB) | $60–120K | Gates the #3 candidate |
| 6 | **Berberine *spo0A* in vivo** | $150–300K | Highest-value *disconfirming* experiment |
| 7 | **HCQ TcdB entry-blockade in vitro** | $30–60K | Lottery ticket on the empty C4 axis |

**⬛ SINGLE-BET BUDGET (~$80–150M + acquisition): Ribaxamase only.** Do not split. A prevention Phase 3 is the expensive part and underfunding it reproduces the failure mode that made the asset available.

**⬛ TWO-BET BUDGET (~$85–155M): Ribaxamase + the C1 option ($1–3M).**
The best marginal dollar in the analysis. The C1 option costs ~2% of the ribaxamase programme, sits on a different axis, has an uncorrelated failure mode, and serves a **different population** (immunocompromised recurrence vs primary prevention). Structure it as UDCA Stage 0 with CamSA as the follow-on molecule — but see §6: **this is one bet, not two.**

**⬛ THREE-BET BUDGET (~$160–295M): add Niclosamide — conditional, not automatic.**
Fund only if **both** gates pass: selectivity ratio >10× **and** fecal-slurry redox stability confirmed. If either fails, do not reallocate to ibezapolstat — take the money off the table. Niclosamide earns its slot on C4 white space and strain-agnostic coverage including CDT, which nothing else in the portfolio has.

**⬛ DO NOT FUND, at any budget:**

| | Why |
|---|---|
| **Ibezapolstat** | Ranked #2 and still not fundable. $80–150M to answer a question only Phase 3 can answer, on an axis that is 0-for-8 at that exact bar. The worst score-to-risk ratio in the set. |
| **A second C2 agent on fidaxomicin** | Zero added axes on the most over-served axis in the disease. |
| **Ebselen, conessine, aprepitant** | Gate failures and a falsified evidence anchor. |
| **TUDCA as a separate programme** | A formulation contingency inside UDCA. Its regulatory premise is likely void. |
| **urso-CamSA as a programme** | A $50–150K synthesis line item inside CamSA. It has never been made. |

### 5.3 Combination constructions (validated, carried forward)

| | Population | Construction | Axes |
|---|---|---|---|
| **A** | Immunocompetent | Fidaxomicin d0–10 → VOWST/REBYOTA/VE303 (+ UDCA optional) → wk 12 | C1+C2+C3+C7+C8 = 5 |
| **B** ⭐ | **Immunocompromised** | Fidaxomicin d0–10 → UDCA/CamSA **or** oral TcdB-IgY → wk 12 | C1+C2+C3+C8 (+C4) = 4–5 |
| **C** | Primary prevention | Ribaxamase during IV β-lactam therapy | C7 — prevents loop entry entirely |

**Combination B is the strategically important one:** zero live-organism exposure, and the **only** construction serving §4.6 unmet need #1. In Combination A, UDCA is explicitly *not load-bearing* — A does not fail if Stage 0 kills UDCA.

**Vetoed combinations:** ebselen + anything (selenium; and shared redox failure mode with niclosamide = *correlated* risk, the opposite of diversification) · vancomycin + any C7 agent (sterilises the consortium it is co-dosed with) · berberine in active Phase 4 disease (Wnt/C6 conflict) · **UDCA + IBAT inhibitor** (shunts the germinant to the colon) · any second C2 agent on fidaxomicin.

---

## 6. SENSITIVITY — WHAT WOULD CHANGE THE RANKING

```
IF THIS RESOLVES...                                              CANDIDATE       NOW    THEN   RESOLVED BY
CamSA mouse study is therapeutic / epidemic strain / survival    CamSA           4.50 → 7.00   Lit retrieval (~$0) + $50-100K
Ribaxamase Phase 2b does NOT support a Phase 3 endpoint          Ribaxamase      7.70 → 2.70   Diligence, $150-300K
Ribaxamase Phase 2b fully verified as reported                   Ribaxamase      7.70 → 8.70   Diligence, $150-300K
Ibezapolstat axis base rate weighted -0.5 rather than -1.5       Ibezapolstat    6.25 → 7.25   Only a Phase 3
UDCA free fecal-water conc exceeds a measured IC50               UDCA            4.00 → 5.50   $50-100K, then $1-3M
Niclosamide selectivity ratio returns >10x                       Niclosamide     4.75 → 5.45   $60-120K
Niclosamide anaerobic stability FAILS                            Niclosamide     4.75 → DQ     $80-150K
Berberine spo0A not reproduced in vivo                           Berberine       4.15 → 4.65   $150-300K
Anti-germinant CLASS question answered NO                        C1 cluster      all  → DQ     nobody has proposed a design
```

**Three observations that matter more than the individual numbers:**

1. **The largest single swing is free.** CamSA moves 2.5 points and two ranks on a literature question nobody in this pipeline asked. Resolve it before the ranking is used for anything.
2. **The #1 recommendation is the most fragile and the cheapest to test.** Ribaxamase's band is 2.70–8.70 — the widest in the analysis — and $150–300K collapses it entirely. That asymmetry *is* the argument for the gate.
3. ⚠️ **The C1 cluster is correlated risk and the portfolio must treat it as one bet.** CamSA, UDCA, TUDCA and urso-CamSA **all die together** if anti-germinants cannot hold against a replenished reservoir. **Nothing in the entire 13-agent analysis addresses this class question, and no agent has proposed an experiment for it.** It is the largest single uncertainty behind the fallback programme.

---

## 7. GAP ANALYSIS

### 7.1 Axis coverage after final ranking

| Axis | Coverage | Occupants (post-DQ) | Assessment |
|---|---|---|---|
| **C1 germination** | 1.5 | UDCA, CamSA, (TUDCA) | Tier 1, thin, and **internally correlated** — one class question kills all of it |
| **C2 vegetative fitness** | **OVER-SERVED** | Ibezapolstat (+ berberine partial) | **0-for-8.** Do not add |
| **C3 toxin regulation** | 0.5 | Fidaxomicin (incidental) | TcdR #15 is the most connected druggable node in CDI and **nothing targets it** |
| **C4 intoxication** | **1 (incomplete)** | Niclosamide only | **Emptied by bezlotoxumab's withdrawal.** Niclosamide is downstream of the receptor-binding branch |
| **C5 host inflammation** | 1 (partial) | Berberine | Aprepitant's death leaves it thinner |
| **C6 barrier / repair** | **ZERO** ⚠ | — | **Widest white space in the disease.** And berberine actively contributes *negatively* via Wnt |
| **C7 ecological restoration** | 1 | **Ribaxamase** | The only loop-**exiting** axis. The #1 recommendation is here, and it had no candidate in the original set |
| **C8 sporulation** | 0.5 | Fidaxomicin (incidental) | Unmet need #2; nothing targets it deliberately |

### 7.2 Underserved axes — what would fill them

- **C6 (zero coverage):** a host-directed mucosal-restitution agent — **IL-22 agonism (#47)** is the named Tier 2 target, K2/K3 compartment, conventional ADMET. This is the emptiest high-value space in CDI and no candidate in this analysis touches it. Note the **incompatibility trap**: IL-23 (#46) and IL-22 (#47) are mutually exclusive — ustekinumab would suppress the protective axis.
- **C4 (incomplete):** the *complete* C4 agent is **receptor blockade**, which sits upstream of the branch between glucosylation-dependent injury and NOX1 necrosis. An **oral TcdB-directed IgY** or a small-molecule CSPG4/FZD blocker would be the first oral agent to cover both arms. Unmet need #4, now with no incumbent.
- **C3 (TcdR #15):** blocking it collapses C3→C4→C5→C6 simultaneously. Elegant and hard to drug — the highest-leverage node nobody is working on.

### 7.3 Cross-cutting scoring patterns

**Pattern 1 — evidence tier, not mechanism, is what separates candidates.** Eight of ten are capped below 7.0 before a single modifier applies; the two exceptions both have human data. The corollary is strategic: **the highest-EV action in CDI is acquiring evidence, not acquiring molecules** — which is exactly what the ribaxamase recommendation is.

**Pattern 2 — the modifier cap binds for half the set** (ibezapolstat, CamSA, UDCA, ebselen, conessine). For these five, the old weighted-average method was letting non-efficacy dimensions do real work on the composite. This is the quantitative signature of the failure the Devil's Advocate identified.

**Pattern 3 — the coupled efficacy/safety filter is the most productive discriminator in the analysis, and it works in both directions.** FATAL for ebselen; SERIOUS for niclosamide; **INVERTED and favourable for CamSA**, whose potency atom and safety atom are the same and point the same way. A filter that only ever penalises is a bias; this one distinguishes.

**Pattern 4 — traditional-medicine evidence contributes almost nothing here, and that is the correct result.** Only berberine earns a positive traditional-use modifier (+0.4), because CDI is a disease where §7.1 correctly says traditional medicine cannot compete on antibacterial potency. Re-anchored to CDI symptoms, "infectious diarrhoea and dysentery" is a genuine on-indication match; nothing else in the ethnobotany set (curcumin, EGCG, triphala, allicin) clears the bar. Allicin additionally **fails G1** — its thiosulfinate is chemically unstable at Eh −200 mV.

**Pattern 5 — one missing measurement outranks every decimal in this report.** No candidate except ibezapolstat has measured commensal-spectrum MICs. §6.4 names selectivity for *C. difficile* over Lachnospiraceae, Ruminococcaceae and Bacteroidetes as **the central medicinal chemistry problem in this disease**, and nine of ten candidates simply have not been tested. At $100–200K for the whole panel, this is the best information-per-dollar in the analysis after the ribaxamase diligence.

---

## 8. CONFIDENCE ASSESSMENT

| Claim | Confidence | Basis |
|---|---|---|
| Ebselen and conessine are disqualified | **HIGH** | Gate failures with independent, measured confirmation |
| Aprepitant is dead | **HIGH** | Evidence anchor is the clinically disproven toxin |
| Strategic diagnosis (axis mis-allocation; capital as binding constraint) | **HIGH** | Multiply supported across Phase 2 and the debate |
| Ribaxamase as the #1 *programme* | **HIGH on strategic logic; LOW–MODERATE on specifics** | The Phase 2b package was verified by nobody. Hence the gate |
| Niclosamide's fall to 4.75 | **MODERATE** | Follows necessarily from instruction #4; the underlying 70% concern survived the debate |
| Ibezapolstat at #2 | **MODERATE–HIGH on the score; LOW on it being actionable** | Correct on evidence; the cost-of-being-wrong column is the operative one |
| CamSA at 4.50 | **LOW** | Rests on a documentation gap. **2.5-point band.** Resolve before use |
| Berberine at 4.15 | **MODERATE** | Real upgrade (toxin induction refuted) net of two real endpoint-specific downgrades |
| UDCA at 4.00 | **LOW–MODERATE** | Genuinely unresolved; the score's *structure* (low anchor, capped modifiers) is more reliable than its value |
| C1 is one correlated bet, not four | **HIGH** | Follows directly from the unaddressed class question |
| Rank *order* below #2 | **LOW** | Ranks 3–6 span 0.75 points. **Treat as a tied band, not an ordering** |

**Most likely way this ranking is wrong:** the evidence-tier ceilings do most of the work, and two of them rest on documentation quality rather than on science — CamSA's mouse-study tier (undocumented in this corpus) and ribaxamase's Phase 2b tier (unverified). Both are cheap to fix, and both are in Stage 0.

**Second most likely:** filing the C2 graveyard base rate in ibezapolstat's *anchor* rather than as a *modifier* is a judgement call worth 1.0 point. I believe it is correct — "8 programmes failed at this exact bar" is evidence about Phase 3 success, not pathway aesthetics — but a reasonable analyst could file it the other way, and ibezapolstat would then score 7.25 and rank #1 among non-acquisition assets. **This is the most contestable single decision in the report, and it is flagged rather than buried.** Note that even at 7.25 the recommendation does not change: the cost-of-being-wrong column, not the composite, is what makes ibezapolstat unfundable.

---

## 9. CORRECTIONS AND PROPAGATIONS REQUIRED BEFORE FINAL SYNTHESIS

1. **Disambiguate the two "C" schemes** — adopt **C1–C8 = causal axes**, **K1–K3 = compartments**, across all documents. Currently "C2" means two different things in two adjacent lines of `round2-synthesis.md`.
2. **UDCA LSAS: A=1 → A=2, total 5 → 6.** The measured 43.5% governs over "~90% absorbed, not a luminal drug."
3. **Split U-1 CamSA (8/10 feasibility) from U-3 urso-CamSA (6/10)** wherever "U-1 Urso-CamSA (8.0)" appears. Do not fund the novel one on the known one's score.
4. **Remove the fabricated berberine claim** ("sub-MIC toxin induction at 6–12 h") everywhere. Toxin *falls* at ½ MIC. The proposed hard stop does not trigger.
5. **Void every "C4 redundancy with bezlotoxumab" deduction** — bezlotoxumab was withdrawn Jan 2025.
6. **Reorder UDCA Stage 0:** the germination dose-response IC₅₀ assay must run **first**; Stage 0 currently compares a concentration to a threshold that does not exist.
7. **Verify before any external use:** TUDCA listed-drug status · the UDCA observational denominator (4/12 vs 4/16) · the ribaxamase Phase 2b data package · CamSA's mouse-study design.
8. **Add a class-level experiment for the anti-germinant question.** No agent has proposed one, and four candidates depend on it.

---

## 10. LIMITATIONS

- **Reproducibility:** all arithmetic is in `scoring/p3_rank.py` and `scoring/p3_sens.py`. Every deduction and modifier is a named string with its value; another analyst can change any single line and see the effect. Nothing is hidden in a weighting vector.
- **No false precision.** Ranks 3–6 span 0.75 points and should be read as a **tied band**. The meaningful separations are #1 vs the field, the #1/#2 gap in *evidence tier* (human vs rodent), and disqualified vs ranked. **A 4.75 versus a 4.50 means nothing.**
- **Project knowledge-graph support is minimal.** Consistent with the Round 1 finding that the corpus is ~15–30% data-backed: **no bacterial or toxin target layer exists in the knowledge graph, and there are no CDI gene–disease associations in project data.** SMILES, MW, aLogP, TPSA and QED values referenced upstream are data-backed from project CSVs; every *C. difficile*-side activity claim in this ranking is knowledge-based and inherited from the Phase 1–2 agents. **This ranking is therefore a synthesis of agent reasoning, not a database query.**
- **Two extended evidence tiers (8.0 and 6.5 for human data) are my additions** to the Literature Reviewer's schedule, which stopped at 7.0 because it only considered preclinical configurations. They are the load-bearing assumption behind ribaxamase's and ibezapolstat's positions. If human Phase 2 evidence deserves no premium over replicated mouse recurrence data, the top of this ranking changes.
- **The ±1.5 modifier cap is a parameter, not a finding.** It was chosen so that no modifier set can overturn a one-tier evidence difference. A cap of ±2.5 would restore something close to the post-debate ranking. The cap's *value* is a judgement; the *need* for a cap is the debate's finding.

---

**RESEARCH DISCLAIMER.** This is computational and literature-synthesis analysis performed by an agent pipeline without live literature retrieval. No candidate here has been validated experimentally in this work. Several load-bearing facts are explicitly flagged unverified (§9.7). **No clinical decision should follow from this document.** Every recommendation is a research-prioritisation and capital-allocation proposal requiring experimental validation, formal regulatory advice, and independent verification of the underlying literature before any external use.
