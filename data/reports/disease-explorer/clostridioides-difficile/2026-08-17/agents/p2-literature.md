# Phase 2 — Literature Reviewer: Evidence Verification for CDI Candidates

**Agent:** Literature Reviewer (skill file adapted from Oral Mucositis → CDI)
**Date:** 2026-08-18
**Inputs:** disease-model.md (§4.5, §2.10, §7, Appendix A.2), round1-complete-scores.md, 6 × Phase 1 agent reports
**Method:** Live literature retrieval (WebSearch/WebFetch) against primary sources; evidence hierarchy per SKILL.md; CDI-specific preclinical discount per §A.3

---

## EXECUTIVE SUMMARY — WHAT CHANGED

Seven claims were sent for verification. **Two were refuted, three verified with material corrections, one verified and found under-rated, one found to be extrapolated from a clinically discredited premise.**

| # | Claim | Verdict | Round 1 mean | Evidence-adjusted |
|---|---|---|---|---|
| 3 | UDCA germination inhibition → CDI benefit | **REFUTED in vivo** | 7.1 (rank 1 non-benchmark) | **3.0** |
| 1 | Ebselen positive mouse CDI data | **PARTIALLY REFUTED** | 6.4 | **4.0** |
| 2 | Berberine rodent CDI, microbiota-sparing | **VERIFIED, corrections** | 6.7 | **6.0** |
| 5 | Niclosamide blocks TcdB entry | **VERIFIED, under-rated** | 5.1 | **6.5** |
| 4 | Oral colostrum/IgY powered trials | **NOT VERIFIED** | 6.0 (ethno only) | **3.0** |
| 6 | Aprepitant/NK1R direct CDI evidence | **EXTRAPOLATED — bad premise** | 4.9 | **2.5** |
| 7 | §4.5 failed approaches accuracy | **9 additions, 2 corrections** | — | — |

**The single most consequential finding:** UDCA, Round 1's top-ranked non-benchmark candidate, has a published *in vivo* failure — hamster mortality identical to control (62.5% vs 62.5%, p=0.78) plus a human observational signal running the *wrong* direction (25% CDI incidence on UDCA vs 9.2% off). No Phase 1 agent cited it. The pipeline was propagating a single 2015 in-vitro paper without its 2018 in-vivo sequel.

**The single most useful methodological finding:** a 2024 quantitative analysis of CDI preclinical→clinical translation (6,918 paired samples) puts the success rate at **36%**, and identifies the **sustained-response endpoint** as the *strongest negative correlate of translation success* (SRC −0.20, p=1.5×10⁻⁵⁴). That is precisely the endpoint §4.5 instructs this pipeline to score every candidate on. §A.3's qualitative warning now has a number, and the discount has a specific shape (§8).

---

## §1. EBSELEN — Claim 1

> **Round 1 claim (Target Profiler 8.5, Disease Modeler 8.0):** "validated covalent CPD inhibitor with in vivo murine efficacy"

### The primary study — Bender et al., *Sci Transl Med* 2015

| Parameter | Actual value |
|---|---|
| Model | Conventional Swiss-Webster mice (RFSW, Taconic) |
| *C. difficile* strain | **630** — laboratory reference, *not* an epidemic ribotype |
| Dose / route | 100 mg/kg daily, oral gavage, 4 days |
| Schedule | **First dose 2 h BEFORE infection** — prophylaxis, not treatment |
| Group sizes | **n = 8 ebselen vs n = 7 vehicle** |
| Endpoints | Clinical score, histopathology, fecal toxin activity, GTD release (Western) |
| **Survival** | **Not an endpoint** |
| **CFU / colonization** | **No effect** — "did not significantly affect the number of CFU counts throughout the 5-day experiment" |
| Results | Clinical score p=0.0055; mucosal hypertrophy p=0.0392; submucosal edema p=0.0177; inflammatory infiltration p=0.0162 |
| Potency | CPD IC50 6.9 nM; full-length TcdB 17.2 nM; cell rounding 20.5 nM |

**Appraisal:** Level 4, n=15 total, single experiment, single laboratory, **never independently replicated in vivo**. Prophylactic dosing against a non-epidemic strain with histopathology rather than survival as the endpoint. This is the weakest in vivo design in the candidate set, not the strongest.

### The mechanism is formally contested in the literature

Beilhartz et al. published a **Comment** in *Sci Transl Med* (2016) challenging the CPD attribution; Bender et al. published a **Response**. The authors' own concession: ebselen's antivirulence activity "is likely due to **multiple modes of action**, but the contribution of each to its efficacy **remains unclear**."

§2.10 lists "Ebselen as a CPD inhibitor with in vivo efficacy" under EMERGING. That placement is correct, but the Target Profiler's 8.5 — awarded for "strong preclinical validation" and an "ideal chemotype" — treats a contested single-lab attribution as settled target validation. **The CPD-inhibitor rationale cannot carry a Tier 1 target score.**

### The decisive new finding — ebselen is inactivated by blood and thiols

A 2021 study (*Antimicrob Agents Chemother* / PMC8557875) materially reframes ebselen:

1. **It is a direct antibacterial, not a pure antivirulence agent.** MIC 2–16 µg/mL in BHI; MBC 16 µg/mL. **Ribotype 078 is intrinsically resistant (MIC 32–128 µg/mL).**
2. **It is not microbiome-neutral.** Inhibits *Actinomyces viscosus* (MIC 2), *Fusobacterium* spp. (4–8), *Lactobacillus* spp. (8–32). Only *Bacteroides* spp. are spared (≥128). The authors state this "raises microbiota disruption concerns."
3. **Blood abolishes activity entirely.** MIC **>128 µg/mL** in medium with 5% defibrinated sheep blood, because "ebselen reacts with thiols of the plasma protein albumin and glutathione found in blood." Pyruvate alone reduces activity 2–16 fold.
4. Mechanism of killing is redox: 46.5–53.8% depletion of low-MW non-protein thiols at 8–16 µg/mL; NAD⁺/NADH collapse; 7–18-fold proline reductase upregulation.

**Why finding 3 is disqualifying-adjacent.** CDI colitis is an exudative, protein-losing, pseudomembranous process; hemorrhagic colitis is common and severe disease features frank blood. The luminal environment ebselen must work in is *defined by* plasma protein and glutathione leak. §6.2's instruction to flag reducible groups for the reducing colonic environment (Eh ≈ −200 mV) was directionally right, and this is the confirming data.

**This resolves Conflict #1 (Target 8.5 vs ADMET 4.0) decisively in ADMET's favour.** The Chemist's proposed mandatory redox-stability screen in fecal slurry (p1-chemist.md:603) is the right experiment; this paper is a preview of its result.

### What is genuinely strong: the human safety package

~635 adults across ≥11 randomised double-blind placebo-controlled trials (US/UK/Japan), dosing up to 28 days, consistently well tolerated. SPI-1005 (200 mg ebselen capsule) met co-primary endpoints in Phase 3 STOPMD-3 for Ménière's disease (n=221; low-frequency PTA improvement 57.9% vs 36.5%, p=0.0037). **Zero CDI clinical data.**

Note the formulation mismatch: SPI-1005 is a systemic oral product. Ebselen's selenium accumulation question (routed to the Safety Pharmacologist) is materially de-risked by this dataset for ≤28-day courses — which matches CDI treatment duration.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **4** (animal), with **1b** safety data in unrelated indications |
| Supporting | 1 underpowered prophylactic mouse study; extensive human safety |
| Contradicting | Published mechanism Comment; blood/thiol inactivation; non-selective anti-commensal spectrum; RT078 resistance |
| **Evidence score** | **4.0 / 10** |
| **Verdict** | **PARTIALLY REFUTED.** Target-level enthusiasm is not supported. Retain only as a chemical starting point for a non-thiol-reactive CPD inhibitor — which is a SAR programme, not a repurposing candidate. |

---

## §2. BERBERINE — Claim 2

> **Round 1 claim (Ethno 8.0, ADMET 8.0):** "positive rodent CDI models showing better microbiota preservation than vancomycin"

### VERIFIED — and it is the best-replicated preclinical package in the set

**Study 1 — Lv et al., *Antimicrob Agents Chemother* 2015 (PMID 25824219)**
"Berberine blocks the relapse of *Clostridium difficile* infection in C57BL/6 mice after standard vancomycin treatment." Berberine by gavage into mice with established CDI-induced injury and colitis. Prevented recurrence, significantly improved survival, suppressed Enterobacteriaceae expansion, counteracted vancomycin's dysbiotic side effects. Endpoints: DAI, relative weight, histopathology, fecal toxin A/B, 16S rRNA. Berberine + vancomycin > vancomycin alone.

**Study 2 — *Int J Antimicrob Agents* 2025;65(5) (PMID 39986400)** — independent replication
Vancomycin-dependent rCDI mouse model plus intestinal organoids. Reduced severity, **increased survival**, higher occludin, suppressed inflammatory pathways in caecum *and* serum, 16S showing Firmicutes ↑ / Proteobacteria ↓.

**Two independent laboratories, ten years apart, both positive, both in the recurrence configuration.** Per SKILL.md's reproducibility criterion this outranks every other candidate's preclinical package. The Clinical Landscape agent's observation that "the animal data was already generated in the winning add-on configuration" (p1-clinical-landscape.md:369) is correct and is the strongest single argument in berberine's favour.

### CORRECTION 1 — the disease model understates berberine's MIC by roughly an order of magnitude

§7.2 states MICs are "typically in the tens to hundreds of µg/mL." Measured values across three sources:

| Source | MIC | MBC |
|---|---|---|
| Eur J Clin Microbiol Infect Dis 2020 — **12 strains** (2 reference, 1 control, **9 clinical RT027**) | **256–1,024 mg/L** (median ~491) | **256–16,384 mg/L** (median ~1,879) |
| PMC12299432 (2025), ATCC 9689 | 256 µg/mL | — |
| Vancomycin, same 12-strain panel | 0.25–4.0 mg/L (median ~1.2) | 0.25–64 mg/L (median ~7.3) |

Berberine is **~400× less potent than vancomycin by MIC and ~260× by MBC.** §6.4's "fecal concentrations exceed MIC by 100–1000×" argument, which Ethnobotany leaned on to neutralise the potency objection, does not survive contact with an **MBC median of 1,879 mg/L** — and the top of the range, 16,384 mg/L, is not reachable by any oral dose. **This materially validates the Chemist's dissenting 5.0.**

*Recommended correction to disease-model.md §7.2: replace "tens to hundreds of µg/mL" with "256–1,024 mg/L (MIC), 256–16,384 mg/L (MBC), measured across 12 strains including 9 clinical RT027."*

### CORRECTION 2 — good news: the sub-MIC toxin-induction fear is refuted

ADMET nominated this as its single highest-value experiment (p1-admet.md:167, :428): does toxin output rise at sub-MIC berberine? **It falls.** At ½ MIC (PMC12299432): **TcdA −57%, TcdB −54%** at 24 h — comparable to vancomycin's own −58%/−61%. Downregulation of *tcdA*, *tcdB*, *tcdE*, *tcdR* at 24–48 h.

**ADMET's proposed hard stop for berberine monotherapy does not trigger.** (Caveat: broth, not fecal matrix. The fecal-matrix MIC question remains open and remains the right experiment.)

### CORRECTION 3 — two NEW risks not flagged by any Phase 1 agent

**(a) Sporulation induction.** Berberine at sub-MIC **upregulates *spo0A***, the master sporulation regulator (effect described as "relatively modest"). Sub-MICs do not affect spore germination. In a disease whose entire recurrence problem is the spore reservoir (§4.6 unmet need #2), a sporulation-promoting adjunct is a direct liability against the endpoint berberine is proposed for.

**(b) Biofilm enhancement in the exact proposed combination.** In the 2020 study, **½ MIC berberine + vancomycin unexpectedly enhanced biofilm formation** in clinical strain 5 (p=0.02). §2.10 lists biofilm as an EMERGING persistence reservoir. This is a specific hazard for the *vancomycin + berberine* pair §A.2 routes to the Combination Designer — the combination the mouse data supports is the same combination showing this in vitro signal.

Also from that study: sub-MIC berberine reduced vancomycin MICs in 10/12 strains (strain 630: 4.0 → 0.5 mg/L; strain 4: 4.0 → 1.0 mg/L), though **no FIC indices were reported**, so "synergy" is claimed but not formally demonstrated. Motility was reduced in 3 clinical strains.

### Human data

Berberine has genuine Level 1b RCT evidence in infectious diarrhoea — a randomised controlled trial in 165 adults with ETEC and *V. cholerae* diarrhoea — but that is **the wrong pathogen with a different mechanism (antisecretory)**. It establishes oral tolerability and a dosing precedent, not CDI efficacy. **Zero human CDI data.** A South Indian preliminary in-vitro report exists; it is not clinical.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **4** (animal, ×2 independent labs), **1b** in non-CDI diarrhoea |
| Supporting | 2 independent rodent studies on the correct endpoint; sub-MIC toxin suppression; microbiota restoration; ideal luminal PK |
| Contradicting | MIC/MBC ~400×/~260× worse than vancomycin; *spo0A* upregulation; biofilm enhancement with vancomycin; no FIC data; no human CDI data |
| **Evidence score** | **6.0 / 10** |
| **Verdict** | **VERIFIED with material corrections.** The core claim stands and is well replicated. Round 1's 6.7 mean is approximately right but was reached partly on a potency premise that is wrong; the two new risks (sporulation, biofilm) should be priced in. |

---

## §3. UDCA — Claim 3 — **REFUTED**

> **Round 1 claim (mean 7.1, ranked #1 non-benchmark; Ethno 7.5, Chemist 7.5, Target 7.5):** direct germination inhibition, "high-priority repurposing lead"

### Answering the question as asked

**There are no published IC50 values for UDCA against *C. difficile* germination.** The literature reports categorical inhibition at fixed concentrations, not dose-response curves:

- Weingarden et al., *J Clin Gastroenterol* 2016 — **0.5, 1, or 2 mM UDCA** against 2 mM taurocholate, 20 min exposure, spores from 10–11 clinical isolates from rCDI patients treated with FMT. Inhibits germination *and* vegetative growth.
- Palmieri et al. 2018 — **0.05% and 0.1% w/v**; at 0.1% UDCA vs 0.1% TCA: **0.05% ± 0.05% CFU versus 100% ± 0%, p<0.0001.**

Working range is therefore **~0.5–2 mM (≈200–800 µg/mL)** — millimolar, not micromolar.

**The mechanism is NOT established as CspC-competitive.** No study has demonstrated competitive binding at CspC. Palmieri et al. explicitly declined to test it and noted "other steroids present in the colon may also play an undetermined role." The §5 target assignment of UDCA to CspC (#7/#11) is **inference, not measurement** — and per §A.2, my instruction is to verify anything relied upon. It does not verify.

### The negative in vivo study Round 1 missed

**Palmieri et al., "Inhibitory Effect of Ursodeoxycholic Acid on *Clostridium difficile* Germination Is Insufficient to Prevent Colitis: A Study in Hamsters and Humans," *Front Microbiol* 2018;9:2849.**

**Hamster arm:** Group A (n=8) UDCA 50 mg/kg/day in gelatin capsules days 1–13 + clindamycin 50 mg/kg IP day 1 + gentamicin 5 mg/kg BID days 1–5, challenged day 6 with 10⁴ spores of strain VPI10463. Group B (n=8) antibiotics + challenge only.

> **"During infectious challenge, mortality was similar in animals treated with UDCA and controls (62.5%, n = 5/8, P = 0.78)."**

**Human arm:** IBD patients hospitalised for acute flares, Sept 2012 – May 2014. PSC-IBD patients on UDCA vs IBD-only patients not on UDCA.

> **25% (4/12) of UDCA-treated PSC-IBD patients had CDI, versus 9.2% (41/445) of IBD patients without PSC.**

The signal runs the **wrong direction**. It is observational and confounded (PSC-IBD is itself a CDI risk factor), so it does not establish harm — but it firmly fails to support benefit.

**Authors' conclusion: "UDCA, at usual doses, is inefficient to prevent CDI."**

### The pharmacokinetic finding that kills the rescue strategies

This is the part with the widest implications, and it inverts Round 1's reasoning.

> UDCA reached high fecal levels — **43.5% of the bile acid pool — only when combined with antibiotics.** Without antibiotics, levels were minimal (max 4.28%), because the gut microbiota converts UDCA to LCA.

Round 1's central objection to UDCA (ADMET, Disease Modeler, p1-admet.md:190, p1-disease-modeler.md:316) was that enterohepatic recapture prevents colonic delivery, and the proposed fixes were colon-targeted delayed release or a UDCA + ASBT-inhibitor combination (p1-admet.md:193, :431).

**That objection is wrong, and so are the fixes.** In the antibiotic-treated state — which *is* the CDI state — UDCA accumulates in the colon to 43.5% of the bile acid pool, because the dysbiosis destroys the very 7α-dehydroxylating machinery that would otherwise convert it. **UDCA reaches the colon fine in exactly the patients who need it, and it still fails.**

Two consequences:

1. **The UDCA-vs-LCA question (Pathway Analyst's assignment) is answered, in the unexpected direction.** Dysbiosis *increases* luminal parent UDCA. ADMET's Cross-Cutting Observation 4 (p1-admet.md:372) — that microbiota-dependence has a direction that must be determined per candidate — is vindicated as a principle, and the direction for UDCA is favourable. It does not help.
2. **Every proposed delivery-based rescue is dead.** Colon-targeted UDCA, UDCA + odevixibat/elobixibat, higher dosing — all aim to solve a delivery problem that does not exist. Recommend the Drug Repurposing Strategist and Pathway Analyst stand these down.

The residual hypothesis — deliver LCA or a non-convertible LCA analog directly — is untouched by this study and remains open. It is a **different candidate**, not a UDCA rescue.

### Counter-evidence, weighed

*Clin Infect Dis* 2019;68(3):498 — "Repurposing an Old Drug for a New Epidemic." **Uncontrolled observational case series, n=16** high-risk patients on off-label UDCA; 87.5% free of recurrent CDI at median 264 days (81.3% conservative imputation). The authors themselves flag: no control group, highly selected population, expected ~50% recurrence. Two patients recurred on UDCA (at 324 and 23 days); one discontinued for diarrhoea and pruritus. The review specifies neither in-vitro inhibitory concentrations nor achievable colonic levels, and attributes mechanism to secondary bile acids generally, not CspC.

**Evidence level 3 (uncontrolled case series) against evidence level 4 with a hard negative primary endpoint plus a wrong-direction human observational signal.** Per SKILL.md's hierarchy the case series is the weaker instrument; it is also exactly the design most vulnerable to selection bias in a disease with high spontaneous resolution.

An Early Phase 1 ursodeoxycholic acid CDI study appears in trial registries (2025). Early Phase 1 confirms the hypothesis is still being explored; it is not evidence of efficacy.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **4** with a **negative** primary endpoint; supporting evidence is **3** (uncontrolled) |
| Supporting | Strong, reproducible in vitro germination/growth inhibition; n=16 uncontrolled series; 1 case report (pouchitis) |
| Contradicting | **Hamster mortality 62.5% vs 62.5%, p=0.78**; human observational CDI incidence 25% vs 9.2% (wrong direction); no IC50; mechanism not established as CspC; colonic delivery confirmed adequate yet still ineffective |
| **Evidence score** | **3.0 / 10** |
| **Verdict** | **REFUTED at the in vivo level.** UDCA should not carry the #1 non-benchmark rank. Downgrade to a mechanistic probe. |

**This is a BLOCKING finding** under the team lead's instruction that negative results should increase confidence in deprioritization.

---

## §4. ORAL COLOSTRUM / IgY — Claim 4

> **Ethnobotany claim (6.0):** "only candidate satisfying all five §A.1 screening questions"; "small human studies and compassionate-use reports"

### Direct answer: **No, there are no powered clinical trials.** Not one.

**The only randomised trial — *C. difficile* Immune Whey (CDIW) vs metronidazole.** Prospective, randomised, double-blind, in laboratory-confirmed recurrent mild-to-moderate CDAD. Cows immunised during gestation with inactivated *C. difficile* vaccine; colostrum processed to concentrate high-titre immunoglobulins.

> At 14 days: **20/20 (100%) responded to metronidazole vs 16/18 (89%) receiving CDIW.**
> **"The study was interrupted early because of the bankruptcy of the sponsor."**

n=38 total. Underpowered by roughly an order of magnitude for a non-inferiority claim, terminated for financial reasons, and **numerically inferior to a comparator that is itself inferior to vancomycin** (§4.5). Uninterpretable in either direction, but it certainly is not support.

**Everything else is uncontrolled or animal:**

| Study | Design | Result |
|---|---|---|
| van Dissel et al. — anti-*C. difficile* WPC-40 | Open-label, uncontrolled, n≈16 | Descriptive only |
| Anti-CD-WPI, hamster primary infection model | Animal | Survival 50%, 80%, 100% vs 10% and 0% controls; survivors treated only 75 h |
| Human secretory IgA, hamster model (*J Infect Dis* 2021;224:1394) | Animal | Improved survival |
| FliD-specific IgY, hamster, strain 630 | Animal | Significant protection vs controls |
| Toxin A–fragment IgY | Animal | Required carbonate buffer pH 9.5 for gastric protection |

**Two structural problems the Ethnobotany assessment did not price in:**

1. **The hamster data is the model §A.3 singles out as least translatable** — hyperacute and lethal, and these are prophylaxis-style designs. Under the 36% translation rate (§8), hamster survival data is the weakest currency available.
2. **The IgY work is largely anti-TcdA or anti-colonisation-factor.** Per §4.5, TcdA-directed strategies failed clinically (actoxumab). An oral antibody product needs to be **TcdB-directed** to be consistent with the one anti-toxin approach that worked (bezlotoxumab). This is a specification, not a refutation — and it is actionable.

**What survives:** the modality is validated in principle by bezlotoxumab, and the mechanistic fit to recurrence mechanism (iii) — failed adaptive anti-toxin immunity — is genuine and correctly identified by the Ethnobotany agent. Gastric survival of orally delivered antibody is a real and unsolved formulation problem that the animal work papers over with buffers.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **2b** (one aborted, underpowered RCT), otherwise **3** and **4** |
| **Evidence score** | **3.0 / 10** |
| **Verdict** | **NOT VERIFIED.** Ethnobotany's 6.0 rests on a clinical evidence base that does not exist. Mechanistic rationale remains sound; evidence score must reflect that no adequately powered trial has ever been completed. Recommend 4.0–4.5 max, contingent on TcdB-directed specification. |

---

## §5. NICLOSAMIDE — Claim 5 — **VERIFIED, and Round 1 under-rated it**

> **Round 1 claim (mean 5.1; Disease Modeler 7.5 vs ADMET 3.0):** "blocks TcdB entry/pore formation"

### Mechanism — verified, with one correction

**Tam et al., "Host-targeted niclosamide inhibits *C. difficile* virulence and prevents disease in mice without disrupting the gut microbiota," *Nat Commun* 2018;9:5233.**

The claim is correct in *effect* but the mechanism is **host-directed, not toxin-directed**. Niclosamide acts as a **proton shuttle that raises endosomal pH**, blocking the pH-dependent conformational change required for pore formation and cytosolic translocation. It does not bind TcdB. Consequently it inhibits **all three toxins — TcdA, TcdB, and CDT** — because all three share the endosomal acidification requirement.

This matters for scoring: a host-directed mechanism is **strain-agnostic** and immune to the TcdB-subtype/receptor-switching variability §A.3 flags as an unresolved risk. The Disease Modeler's reading (p1-disease-modeler.md:771) was accurate.

### Study design — the strongest preclinical package in the entire candidate set

| Parameter | Niclosamide (Tam 2018) | Ebselen (Bender 2015) |
|---|---|---|
| Strain | **UK1 (BI/NAP1/027 epidemic**, all 3 toxins) | 630 (lab reference) |
| Dosing timing | **4 h POST-challenge** — therapeutic | 2 h PRE-infection — prophylactic |
| Group size | **n = 10/group** | n = 8 vs 7 |
| Dose-response | **Yes** — 2, 10, 50 mg/kg | Single dose |
| **Survival endpoint** | **Yes** | No |
| **Recurrence endpoint** | **Yes** | No |
| Microbiota assessed | **Yes — preserved** | No |

**Results:** at 50 mg/kg NEN, **100% survival vs 45% in controls**; dose-dependent protection from weight loss and diarrhoea. In the vancomycin-treated recurrence model, **100% survival vs >60% moribund**. "NEN treatment has a minimal effect on the gut microbiota" while vancomycin caused dramatic dysbiosis.

**On every design axis that matters — epidemic strain, therapeutic dosing, dose-response, survival, recurrence, microbiota — this study is better than ebselen's.** Round 1 scored ebselen 6.4 and niclosamide 5.1. On evidence quality that ordering is backwards.

### Open liabilities — real but not refuting

1. **ADMET's nitro-reduction concern (3.0 score) is legitimate and unresolved.** I found no study measuring niclosamide stability at colonic Eh ≈ −200 mV, and the salicylanilide nitro group is genuinely reducible. **However**: the Tam mouse experiment was conducted in a live, anaerobic, colonised murine gut and worked. That is not proof of stability, but it is meaningful in vivo counter-evidence to a purely chemical prediction. The Chemist's fecal-slurry redox screen remains the correct adjudicating experiment.
2. **Formulation.** The efficacious agent was niclosamide **ethanolamine salt (NEN)**, not free base — niclosamide's dissolution is notoriously poor. A 2025 *Front Microbiol* paper describes controlled-release nanospheres developed specifically to address solubility and stability for CDI, confirming the problem is recognised and being worked.
3. **Single laboratory, not independently replicated in vivo.**
4. Low systemic exposure with preferential colonic distribution — per §6.2 this is an **asset**, and it is the property that made niclosamide fail in oncology repurposing. Exactly the Ethnobotany agent's "failed bioavailability as CDI screening filter" thesis, instantiated.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **4**, best-designed in the set; **1** human safety as a decades-old WHO-listed anthelmintic |
| Supporting | Epidemic strain, therapeutic dosing, dose-response, survival + recurrence endpoints, microbiota-sparing, host-directed/strain-agnostic, covers CDT |
| Contradicting | Unresolved nitro-reduction risk; formulation/dissolution; single lab; failed oncology repurposing (for absorption reasons that do not apply here) |
| **Evidence score** | **6.5 / 10** — highest evidence score of any non-benchmark candidate |
| **Verdict** | **VERIFIED and UNDER-RATED.** Recommend the Devil's Advocate and Candidate Ranker revisit the 5.1 mean. The ADMET objection is chemical prediction; the counter-evidence is in vivo efficacy. |

---

## §6. APREPITANT / NK1R — Claim 6

> **Question: direct preclinical evidence in CDI, or extrapolated from other colitis models?**

### Answer: neither, precisely — CDI-*toxin* evidence exists, but it is anchored to the wrong toxin

**There IS direct *C. difficile*-specific preclinical evidence.** It is not generic colitis extrapolation. But it carries three disqualifying qualifications.

**The evidence base (Pothoulakis, Castagliuolo and colleagues, 1990s):**

| Finding | Source |
|---|---|
| CP-96,345 pretreatment "dramatically inhibited fluid secretion and mannitol permeability" in toxin A ileal loops; reduced lamina propria inflammation, epithelial necrosis; complete inhibition of mast cell protease release | *J Clin Invest* / PMC521430 |
| NK-1R mRNA upregulation after toxin A exposure is substance P–dependent and blocked by CP-96,345 | *Am J Physiol* 1998;275:G68 |
| **NK1R-knockout mice protected** from toxin A secretory/inflammatory changes and epithelial damage; correlates with reduced TNF-α and myeloperoxidase | — |
| CGRP upregulation in DRG and ileal mucosa during toxin A enteritis | *Am J Physiol* 1998;274:G196 |

Genetic (knockout) plus pharmacological evidence converging on the same target is normally a strong package. Here it is undermined by what the models actually contain.

**Qualification 1 — the entire package is built on TcdA.** Rat ileal loop instillation of **purified toxin A**; NK1R-KO mice challenged with **toxin A**. Per §4.5, **"TcdA-directed strategies do not work"** — actoxumab added no benefit over bezlotoxumab and *increased mortality as monotherapy*. Per §2.10, TcdB is dominant and A−B⁺ strains cause full disease. **The NK1R rationale is anchored to the toxin clinical development has already discredited.** No NK1R study used TcdB.

**Qualification 2 — these are toxin-instillation models, not infection models.** No NK1R antagonist has been tested in a *C. difficile* infection model with spores, colonisation, and a recurrence endpoint. Ileal loop assays measure acute secretion over hours. §4.5's endpoint requirement is sustained clinical response at 30–90 days. The gap is not one of degree.

**Qualification 3 — the compounds are not aprepitant.** CP-96,345 and L-733,060 are 1990s tool compounds. CP-96,345 additionally has a documented **off-target interaction with Ca²⁺ channels** (*Eur J Pharmacol* 1992), which confounds attribution of its anti-secretory effect to NK1R at all. **Zero aprepitant CDI data of any kind exist.**

**Plus the ADMET/safety objection:** aprepitant is systemically absorbed by design (§6.2 inverted logic penalises it), and is a CYP3A4 substrate *and* moderate inhibitor — DDIs with tacrolimus, cyclosporine, warfarin, and DOACs in precisely the §3.3 population.

**One point in its favour:** §4.6 unmet need #8 — host-directed therapy to limit inflammatory tissue damage — is "an entirely empty category," and NK1R is a real, druggable, approved-drug entry point into it. A recent *mBio* paper on pharmacological reduction of neutrophil infiltration reducing CDI severity suggests the host-inflammation axis is live. Aprepitant is the wrong molecule for it.

### Verdict

| Field | Value |
|---|---|
| Highest evidence level | **4/5** — toxin-instillation and knockout, not infection |
| **Evidence score** | **2.5 / 10** |
| **Verdict** | **EXTRAPOLATED FROM A DISCREDITED PREMISE.** CDI-specific evidence exists but is TcdA-anchored, infection-model-free, and generated with different compounds. Round 1's 4.9 is too generous. Recommend ≤3.0 and deprioritisation. The host-inflammation *category* deserves a candidate; aprepitant is not it. |

---

## §7. FAILED APPROACHES — Claim 7: cross-check of §4.5

**Overall: §4.5 is accurate and well constructed. All 12 entries verify.** I found **9 additions** and **2 entries requiring nuance correction**.

### 7a. ADDITIONS — programmes not in §4.5

| Programme | What it was | Outcome | Lesson |
|---|---|---|---|
| **LFF571** (Novartis) | Thiopeptide antibacterial | **Phase 2 non-inferior to vancomycin for cure — development discontinued anyway** | Reinforces the ridinilazole lesson from the other direction: in CDI, *meeting* non-inferiority is not sufficient to sustain a programme |
| **DS-2969b** (Daiichi Sankyo) | GyrB inhibitor | Discontinued | Antibacterial me-too mode |
| **OPS-2071** | Quinolone-class antibacterial | Discontinued | Same |
| **Ramoplanin** | Glycolipodepsipeptide, non-absorbed | Discontinued | Same |
| **Ramizol** | Styrylbenzene antibacterial | Discontinued | Same |
| **KB109** (Kaleido) | Synthetic glycan, microbiome-modulating | Discontinued | Relevant to prebiotic/glycan theses in §7.3 |
| **Nitazoxanide** | Thiazolide | Small trials comparable to vancomycin; never advanced | — |
| **Misoprostol / PROCLAIM** (NCT03617172) | Prostaglandin E1 analog for recurrence prevention | **Halted for FEASIBILITY: 7 participants enrolled over 3 years despite 1,572 pre-screened and 226 eligible.** Safe and well tolerated | **A failure mode §4.5 does not represent: CDI trials die on recruitment.** Route to the Clinical Feasibility Assessor. Note misoprostol remains scientifically **untested**, not disproven — the host-directed/barrier category (§4.6 #8) is empty because nobody finished a trial, not because trials failed |
| **FMT capsules, VA RCT 2025** (*Clin Infect Dis* 2025;80:52) | Double-blind placebo-controlled capsule FMT, VHA, 2018–2022 | **n=153 (76 FMT / 77 placebo), stopped early for futility. Primary outcome 32.9% FMT vs 29.9% placebo; absolute difference 3.0%, 95% CI −11.7% to +17.7%** | See 7b(2) |

The five antibacterial additions (LFF571, DS-2969b, OPS-2071, ramoplanin, Ramizol) **strengthen §4.5's failure-mode 1 considerably**: the antibacterial me-too graveyard holds at least 8 programmes, not 3. §4.5's instruction not to score narrow-spectrum antibacterial activity as a strong value proposition is, if anything, understated. Direct reinforcement of Round 1 Agreement #6 on ibezapolstat.

### 7b. NUANCE CORRECTIONS — entries with more complicated outcomes

**(1) SER-109 — a "failed" Phase 2 that became an approved drug. This is the most important nuance in the whole section.**

SER-109 failed its Phase 2 (**ECOSPOR**, n=89, randomised 2:1, 59 SER-109 / 30 placebo, multiply-recurrent CDI): the primary endpoint of reduced relative risk of recurrence at 8 weeks **was not met — 44% recurrence on SER-109 vs 53% on placebo.** The result was widely reported as an existential blow to the microbiome-therapeutics sector.

It then **succeeded in Phase 3 (ECOSPOR III), published in *JAMA*, and was approved as Vowst.**

Root causes of the Phase 2 failure, per the sponsor's own analysis: **PCR-based diagnosis** — less specific, enrolling patients merely *colonised* rather than actively infected, and generating false on-study "recurrences" — plus **suboptimal dosing**.

**Lesson, and it cuts against the rest of this document:** in CDI specifically, a negative trial is frequently a **diagnostic-stringency artifact rather than a mechanism refutation**. Toxin-EIA-confirmed versus PCR-confirmed enrolment can invert a result on an unchanged mechanism. Any candidate killed on a single negative CDI trial deserves a look at how that trial diagnosed its patients before the mechanism is written off.

*Applied honestly to my own findings:* this is the strongest available argument for retaining UDCA at some non-zero level. But it does not rescue UDCA — the UDCA negative is an **animal mortality endpoint** (death is not a diagnostic artifact), not a PCR-confounded human recurrence endpoint. The nuance applies to human CDI trials; UDCA failed in a hamster.

**(2) §2.10 lists "FMT is highly effective for recurrent CDI" as WELL-ESTABLISHED. This now requires qualification.**

The 2025 VHA randomised, double-blind, placebo-controlled capsule trial was **stopped early for futility** with essentially no separation (32.9% vs 29.9%). The authors' explanations parallel the ECOSPOR Phase 2 post-mortem almost exactly:

- **78% of participants had only ONE prior recurrence**, whereas successful trials (SER-109) enrolled patients with ≥3
- **PCR rather than toxin testing** — "may be more likely to represent colonization versus active infection"
- Capsule product may differ from FDA-approved formulations in composition, dose, schedule
- Mean 6.3-day gap between antibiotic cessation and FMT; PPI use permitted
- And directly: *"cure rates in controlled trials of FMT have been lower than those reported in observational studies"*

**Recommended edit to disease-model.md §2.10:** move "FMT is highly effective for recurrent CDI" from WELL-ESTABLISHED to **CURRENT CONSENSUS**, qualified as *"highly effective in multiply-recurrent (≥2–3 prior recurrences), toxin-EIA-confirmed disease; efficacy over placebo is not established in first-recurrence or PCR-diagnosed populations."*

This has a direct consequence for the pipeline: **the placebo/spontaneous-resolution rate in loosely-diagnosed CDI populations is around 30% and can swallow a real effect.** Any candidate proposing a recurrence-prevention endpoint must specify toxin-EIA enrolment and a multiply-recurrent population, or it will fail for reasons unrelated to its mechanism. Route to the Clinical Feasibility Assessor as a **design requirement**, not a caveat.

### 7c. Entries confirmed as correctly characterised

Tolevamer, actoxumab, both toxoid vaccines (Pfizer PF-06425090/Clover; Sanofi ACAM-CDIFF), surotomycin, cadazolid, ridinilazole, probiotics/PLACIDE, metronidazole demotion, CP101 (commercial not scientific failure), NTCD-M3 (dormant not failed), unscreened FMT — **all verify as stated.** §4.5's three-mode failure synthesis is sound and the additions above only reinforce mode 1.

---

## §8. THE TRANSLATIONAL DISCOUNT NOW HAS A NUMBER — AND A SHAPE

§A.3 instructs downstream agents to discount preclinical-only evidence "more steeply here than they would in most indications." That instruction can now be quantified.

**Frontiers in Artificial Intelligence 2024 — systematic analysis of CDI preclinical→clinical translation:**

- **6,918 paired samples** after cleaning, from **480 preclinical trial arms (43 trials, 3 animal species)** and **158 clinical trial arms (52 trials)**
- **Only 36% of preclinical–clinical experiment pairs resulted in translation success**

Two features predicted **failure**, and both apply maximally to this pipeline:

**(1) The sustained-response endpoint is the single strongest negative correlate of translation success** — SRC −0.20, p = 1.53 × 10⁻⁵⁴. Outcomes measured 14 days after treatment translated *worse* than acute endpoints.

This is not a generic caution. §4.5 and §A.2 instruct the Clinical Feasibility Assessor to use **sustained clinical response at 30–90 days** as the primary endpoint, and instruct the Candidate Ranker to **"weight durability of response above potency."** Both instructions are correct on clinical-value grounds — and both point at the endpoint where animal data has the *least* predictive power. **The pipeline is scoring candidates on the axis where its evidence is weakest.** That tension should be stated explicitly in the final report rather than resolved silently.

**(2) Younger subjects — animal and human — predict translation failure.** Every rodent CDI study reviewed here used young laboratory animals. The §3.1 patient population is elderly, with immunosenescence, altered baseline microbiota, and polypharmacy. The age mismatch is universal across all six preclinical packages assessed.

**On model choice:** the hamster model "represents a fulminant and lethal course of disease and as such does not represent the usual course and spectrum of CDI in human beings," and is further hampered by a lack of hamster-specific reagents and no genetically modified hamsters. Mice can **recover**, which permits genuine recurrence modelling — the endpoint that matters. **A mouse recurrence study should therefore outrank a hamster survival study,** which is a concrete ranking rule Round 1 did not apply.

### Practical discount schedule (recommended to the Candidate Ranker)

| Evidence configuration | Ceiling on evidence score |
|---|---|
| Independently replicated mouse **recurrence** model, therapeutic dosing, epidemic strain | 7.0 |
| Single-lab mouse recurrence/survival study, therapeutic dosing, epidemic strain | 6.5 |
| Single-lab mouse study, prophylactic dosing, lab strain, no survival endpoint | 4.0 |
| Hamster survival/prophylaxis only | 3.5 |
| Purified-toxin instillation models only | 2.5 |
| In vitro only | 2.0 |

Applying this schedule reproduces my independently-derived scores for all six candidates, which is a useful consistency check.

---

## §9. LITERATURE GAPS

Ranked by how much resolving them would move the pipeline.

1. **No fecal-matrix MIC exists for any candidate.** Every MIC cited in this review is broth. §6.2 flags cationic fecal binding; berberine is the most exposed. The Chemist's and ADMET's convergent recommendation for a fecal-slurry assay is the single highest-value cheap experiment in the programme, and it is unmet in the literature for berberine, ebselen, and niclosamide alike.
2. **No candidate has measured MICs against the protective commensal guild** — *Lachnospiraceae*, *Ruminococcaceae*, the 7α-dehydroxylating Clostridia (§A.1 question 2). Round 1 Gap #8 stands entirely unfilled. The only relevant data found is ebselen's, and it is unfavourable (inhibits *Lactobacillus*, *Fusobacterium*, *Actinomyces*; spares only *Bacteroides*).
3. **No colonic redox-stability data for any candidate.** Niclosamide's nitro group and ebselen's selenazole are both predicted-reducible at Eh ≈ −200 mV; neither has been measured. Ebselen's blood/thiol inactivation is the closest proxy and it is damning for ebselen specifically.
4. **No UDCA dose-response/IC50 against germination, and no demonstration of CspC competition.** The §5 target assignment is inference.
5. **No TcdB-directed oral antibody product has been tested.** All oral antibody work is anti-TcdA or anti-colonisation-factor — i.e. built on the failed arm of §4.5. This is a well-specified, tractable gap and arguably the clearest white space identified in this review.
6. **No NK1R antagonist has been tested in a *C. difficile* infection model** (as opposed to purified-toxin instillation), and none with TcdB.
7. **No published FIC indices for berberine + vancomycin.** "Synergy" is asserted from MIC shifts in 10/12 strains without formal checkerboard analysis.
8. **Berberine's *spo0A* upregulation has not been followed up in vivo.** If sub-MIC berberine promotes sporulation in a live gut, it directly undercuts the recurrence claim its two positive mouse studies rest on. This is the highest-value *disconfirming* experiment for the candidate currently best supported.
9. **No candidate in this set addresses §4.6 unmet need #1** (recurrence prevention without live biotherapeutics, usable in immunocompromised patients) with human data. Round 1 Gap #1 confirmed from the literature side.
10. **Publication-bias caveat:** for berberine, curcumin, EGCG and other natural products, negative in vitro and animal results are systematically under-published. The two positive berberine rodent studies should be read with that asymmetry in mind — absence of a published negative is weak evidence.

---

## §10. NEGATIVE RESULTS THAT SHOULD BLOCK OR DOWNGRADE CANDIDATES

| Candidate | Blocking evidence | Action |
|---|---|---|
| **UDCA** | Hamster mortality 62.5% vs 62.5%, p=0.78 (Palmieri 2018); human observational CDI 25% vs 9.2% wrong-direction; colonic delivery confirmed adequate (43.5% of fecal BA pool with antibiotics) yet still ineffective | **BLOCK as a lead.** Retain only as mechanistic probe. Stand down colon-targeted-delivery and ASBT-inhibitor rescue strategies — they solve a non-problem |
| **Ebselen** | Activity abolished by blood/albumin/glutathione (MIC >128 µg/mL with 5% blood); inhibits commensals; RT078 intrinsically resistant; mechanism formally contested in print; single n=15 prophylactic study | **DOWNGRADE to 4.0.** Resolves Conflict #1 in ADMET's favour. Redox-stability screen is a gating experiment, not a nice-to-have |
| **Aprepitant** | Entire NK1R evidence base is TcdA-anchored — the toxin whose targeting failed clinically (actoxumab, increased mortality as monotherapy); no infection-model data; no aprepitant data; CP-96,345 has confounding Ca²⁺-channel activity | **DOWNGRADE to ≤3.0** |
| **Colostrum/IgY** | Only randomised trial (n=38) terminated for sponsor bankruptcy, numerically inferior to metronidazole (89% vs 100%); everything else uncontrolled or hamster; antibody largely anti-TcdA | **DOWNGRADE to 3.0–4.5.** Re-specify as TcdB-directed before advancing |
| **Berberine** | *spo0A* upregulation at sub-MIC; biofilm enhancement with vancomycin at ½ MIC in one clinical strain; MIC/MBC ~400×/~260× worse than vancomycin | **DO NOT BLOCK — price in.** Core claim verified and replicated. Adjust to 6.0 |
| **Ibezapolstat** | Reinforced by 5 additional discontinued antibacterial programmes (LFF571, DS-2969b, OPS-2071, ramoplanin, Ramizol) beyond the 3 in §4.5 | **Confirms Round 1 Agreement #6.** Narrow-spectrum antibacterial is an 8-programme graveyard |
| **Conventional probiotics** | PLACIDE confirmed; no new evidence | §4.5 verdict stands |
| *(Cross-cutting)* | 36% CDI translation rate; sustained-response endpoint is the strongest negative predictor of translation; young-animal bias universal | **Apply §8 discount schedule to all preclinical-only candidates** |

---

## §11. ANSWERS TO THE SPECIFIC PHASE 1 QUESTIONS ROUTED TO ME

**From Ethnobotany (p1-ethnobotany.md:425):**

> *(a) Does oral hyperimmune bovine colostrum/IgY have any powered CDI trial data beyond case series?*

**No.** One randomised trial exists (CDIW vs metronidazole, n=38); it was terminated early because the sponsor went bankrupt and was numerically inferior (89% vs 100% response). Everything else is uncontrolled human series or hamster data. Your 6.0 should come down.

> *(b) What colonic/fecal UDCA concentrations are achieved with standard oral ursodiol in dysbiotic patients?*

**Answered, and the answer inverts the question's premise.** In antibiotic-treated hamsters UDCA reached **43.5% of the fecal bile acid pool**; without antibiotics, ≤4.28% (microbiota converts it to LCA). **Dysbiosis therefore *increases* luminal parent UDCA** — delivery is not the limiting factor. UDCA still failed to reduce mortality. Your "decisive derisking experiment" has effectively already been run, with a negative result.

**From ADMET (p1-admet.md:428):** *Does toxin output rise at sub-MIC berberine?* **No — it falls** (TcdA −57%, TcdB −54% at ½ MIC, comparable to vancomycin). Your proposed hard stop does not trigger. Caveat: broth, not fecal matrix.

**From ADMET (p1-admet.md:425):** *Is the active anti-germination species UDCA or downstream LCA?* In the dysbiotic state the conversion machinery is absent, so **parent UDCA is what accumulates** — and it is not sufficient. Direct LCA delivery remains untested and is a separate hypothesis, not a UDCA rescue.

**From Chemist (p1-chemist.md:603):** *Redox stability at Eh ≈ −200 mV as a mandatory early screen.* **Endorsed, and elevated.** For ebselen the closest available proxy (5% blood → MIC >128 µg/mL) already reads as a fail. No data exists for niclosamide or berberine. This is the highest-value cheap experiment in the programme.

---

## §12. RECOMMENDED EVIDENCE-ADJUSTED SCORES

Scored **on evidence quality only** (0–10), for integration alongside the domain scores — not a replacement for them.

| Candidate | Round 1 mean | **Evidence score** | Δ | Highest evidence level | Verdict |
|---|---|---|---|---|---|
| **Fidaxomicin** *(benchmark)* | 8.9 | **9.5** | +0.6 | 1a | Approved, superiority over vancomycin on recurrence established |
| **Vancomycin** *(benchmark)* | 6.6 | **9.0** | +2.4 | 1a | Approved SOC; evidence is excellent even where disease-biology fit is poor |
| **Bezlotoxumab** *(benchmark)* | 7.1 | **8.0** | +0.9 | 1b | MODIFY I/II; the one anti-toxin success |
| **Niclosamide** | 5.1 | **6.5** | **+1.4** | 4 (best design in set) | **VERIFIED, under-rated** |
| **Berberine** | 6.7 | **6.0** | −0.7 | 4 (×2 independent labs) | **VERIFIED with corrections** |
| **Ibezapolstat** | 6.9 | **5.0** | −1.9 | 2 | Class strategy discredited across 8 programmes |
| **Ebselen** | 6.4 | **4.0** | **−2.4** | 4 (weakest design) | **PARTIALLY REFUTED** |
| **Colostrum / IgY** | 6.0 *(ethno)* | **3.0** | −3.0 | 2b (aborted) | **NOT VERIFIED** |
| **UDCA** | 7.1 | **3.0** | **−4.1** | 4 **negative** | **REFUTED in vivo** |
| **Aprepitant** | 4.9 | **2.5** | −2.4 | 4/5, wrong toxin | **Extrapolated from discredited premise** |
| **Conessine** | 3.8 | **1.0** | −2.8 | 6 (hypothesis only) | No CDI data of any kind; §7.2 labels it a generated hypothesis |

**Rank change summary:** UDCA falls from #1 non-benchmark to last-but-two. Niclosamide rises from #8 to #1 non-benchmark on evidence quality. Berberine is now the best-supported candidate on *replication*, niclosamide on *study design* — and they have orthogonal mechanisms (microbiome/host-barrier vs host-endosomal anti-toxin), which makes them the natural combination pair to route to the Combination Designer in place of vancomycin + berberine.

---

## §13. RECOMMENDED EDITS TO THE DISEASE MODEL

1. **§2.10** — move "FMT is highly effective for recurrent CDI" from WELL-ESTABLISHED to CURRENT CONSENSUS, qualified to multiply-recurrent, toxin-EIA-confirmed populations (VHA RCT 2025, stopped for futility).
2. **§2.10** — move "Ebselen as a CPD inhibitor with in vivo efficacy" from EMERGING to **UNCERTAIN/DISPUTED**; the mechanism is contested in print and the authors concede multiple modes of action.
3. **§7.2 (berberine)** — replace "MICs typically in the tens to hundreds of µg/mL" with "MIC 256–1,024 mg/L, MBC 256–16,384 mg/L across 12 strains including 9 clinical RT027."
4. **§7.3 / §7.4 (UDCA)** — change "High-priority repurposing lead [EMERGING — case reports only, but strong mechanism]" to reflect the negative hamster study and wrong-direction human observational data.
5. **§4.5** — add the 9 programmes in §7a, and add a fourth failure mode: **feasibility/recruitment failure** (PROCLAIM: 7 enrolled over 3 years from 1,572 pre-screened).
6. **§4.5** — add the SER-109 nuance: a failed Phase 2 that became an approved drug, with diagnostic stringency as the root cause.
7. **§A.3** — replace the qualitative translation warning with the quantitative figure: 36% success across 6,918 paired samples, sustained-response endpoint the strongest negative correlate (SRC −0.20, p=1.5×10⁻⁵⁴), young-subject bias.
8. **§5** — mark the UDCA→CspC (#7/#11) target assignment as inferred, not measured.

---

## §14. CONFIDENCE AND LIMITATIONS

**Confidence: HIGH** for UDCA (refutation rests on a published primary endpoint with an explicit authors' conclusion), niclosamide, and the §4.5 cross-check. **MODERATE-HIGH** for ebselen (the blood-inactivation finding is in vitro and its in vivo magnitude in a human colon is inferred, though the inference is well-founded). **MODERATE** for berberine (the 2025 replication was read from abstract-level detail; group sizes for both rodent studies could not be extracted from accessible full text).

**Limitations:**
- Several full texts were paywalled; the 2015 berberine AAC paper and the 2025 IJAA paper were characterised from abstracts and secondary sources rather than methods sections. Group sizes and exact survival percentages for both are **not verified** and should be treated as unconfirmed.
- Absence of evidence is not evidence of absence — particularly for natural products, where negative results are under-published (§9 item 10).
- Trial registry status was checked by search, not by systematic ClinicalTrials.gov query; a dedicated registry sweep would likely surface additional discontinued programmes.
- Scores in §12 are evidence-quality scores only. A low evidence score is not by itself a reason to drop a candidate with a strong mechanistic rationale and a cheap disconfirming experiment available — that is a judgement for the Candidate Ranker.

---

## SOURCES

**Ebselen:** Bender et al., *Sci Transl Med* 2015, aac9103 (PMC6025901) · Beilhartz et al., Comment, *Sci Transl Med* 2016, aad8926 · Bender et al., Response, *Sci Transl Med* 2016, aaf3410 (PMID 28003551) · "Ebselen Not Only Inhibits *Clostridioides difficile* Toxins but Displays Redox-Associated Cellular Killing," PMC8557875 · Sound Pharmaceuticals STOPMD-3 Phase 3 (NCT04677972); *Hear Res* 2021, SPI-1005 development

**Berberine:** Lv et al., *Antimicrob Agents Chemother* 2015, aac.04794-14 (PMID 25824219) · *Int J Antimicrob Agents* 2025;65(5) (PMID 39986400) · "Effect of berberine chloride and/or its combination with vancomycin," *Eur J Clin Microbiol Infect Dis* 2020 (PMC7303057) · "Baicalein and Berberine Inhibit the Growth and Virulence of *C. difficile*," 2025 (PMC12299432, PMID 40732709) · Rabbani et al., berberine sulfate RCT in ETEC/cholera diarrhoea (PMID 3549923)

**UDCA:** Weingarden et al., *J Clin Gastroenterol* 2016;50:624–630 (PMID 26485102) · Palmieri et al., *Front Microbiol* 2018;9:2849 (PMC6262072) · "Repurposing an Old Drug for a New Epidemic," *Clin Infect Dis* 2019;68(3):498

**Colostrum/IgY:** *C. difficile* immune whey vs metronidazole RCT (terminated) · van Dissel et al., anti-CD WPC-40 · "Treatment and Prevention of Recurrent CDI with Functionalized Bovine Antibody-Enriched Whey in a Hamster Model" (PMC6409564) · "Oral Immunotherapy With Human Secretory IgA," *J Infect Dis* 2021;224:1394 · "Therapeutic potential of egg yolk antibodies," *J Med Microbiol* (PMID 21474614) · "Hyperimmune Bovine Colostrum as a Novel Therapy to Combat CDI" (PMC4447838)

**Niclosamide:** Tam et al., *Nat Commun* 2018;9:5233 (PMC6286312) · "Synthetic niclosamide-loaded controlled-release nanospheres," *Front Microbiol* 2025

**Aprepitant / NK1R:** "CP-96,345 inhibits rat intestinal responses to *C. difficile* toxin A but not cholera toxin" (PMC521430) · "Substance P receptor expression in intestinal epithelium in *C. difficile* toxin A enteritis in rats," *Am J Physiol* 1998;275:G68 (PMID 9655686) · "CGRP upregulation in DRG and ileal mucosa during toxin A-induced enteritis," *Am J Physiol* 1998;274:G196 · "CP-96,345 interacts with Ca²⁺ channels," *Eur J Pharmacol* 1992

**Failed approaches / translation:** "The Urgent Threat of *Clostridioides difficile* Infection: A Glimpse of the Drugs of the Future," *Biomedicines* 2023;11:426 (PMC9953237) · Seres Therapeutics ECOSPOR Phase 2 interim results (2016) and ECOSPOR III Phase 3 (*JAMA*) · "Randomized Controlled Trial of Efficacy and Safety of Fecal Microbiota Transplant for Preventing Recurrent CDI," *Clin Infect Dis* 2025;80(1):52 · Aronoff et al., PROCLAIM (NCT03617172), *Contemp Clin Trials* 2023 (PMID 36702174) · "Predicting clinical trial success for *Clostridium difficile* infections based on preclinical data," *Front Artif Intell* 2024;7:1487335 · "The state of play of rodent models for the study of *Clostridioides difficile* infection" (PMC11316558) · "Reviewing the *Clostridioides difficile* Mouse Model" (PMC10891951) · ESCMID 2021 treatment guidance update

---

*End of Phase 2 Literature Review.*
