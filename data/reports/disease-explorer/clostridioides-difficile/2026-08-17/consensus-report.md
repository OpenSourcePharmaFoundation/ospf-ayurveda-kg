═══════════════════════════════════════════════════════════════════
DRUG DISCOVERY PIPELINE — CONSENSUS REPORT
═══════════════════════════════════════════════════════════════════
Target Disease: Clostridioides difficile infection (CDI)
Date: 2026-08-18
Research Question: Evaluate possible treatments for Clostridioides difficile
Candidates Evaluated: 15 (10 original + 5 surfaced during Phase 2)
Agents Consulted: 17 domain agents across 4 rounds + structured debate
Data Basis: Mixed — ~30% data-backed (ChemBL drug data), ~70% knowledge-based

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DISEASE BRIEF

**Clostridioides difficile infection** (ICD-10 A04.7; CDC "Urgent Threat") is a toxin-mediated infectious disease with an ecological core. ~365,000–500,000 US cases/yr; ~12,000–30,000 attributable deaths; ~$1–6 billion/yr burden. The patient population is predominantly elderly (≥65), renally impaired, heavily polypharmaceutical, often immunocompromised, and torsades-primed (diarrhoea-driven hypokalaemia + QT-prolonging co-medications).

**Pathobiology model:** Hybrid — 7 sequential infection phases overlaid with 3 concurrent modules:
- **Phases:** (0) Loss of colonization resistance → (1) Spore germination → (2) Vegetative outgrowth → (3) Toxin production → (4) Epithelial damage → (5) Inflammatory cascade → (6) Systemic complications
- **Modules:** (A) Toxin biology — TcdB is the dominant virulence factor · (B) Host immunity · (C) Microbiome/bile acid ecology
- **Defining topology:** the RECURRENCE LOOP — standard-of-care antibiotics resolve Phases 2–5 while deepening Phase 0

**Master target list:** 72 targets across 4 classes (25 bacterial, 9 toxin, 29 host, 9 microbiome/commensal). Two target classes have OPPOSITE therapeutic directions: bacterial/toxin targets are inhibited; commensal functions (bile acid 7α-dehydroxylation, BSH, SCFA production) must be restored.

**Standard of care:** Fidaxomicin (preferred first-line) or oral vancomycin. **Bezlotoxumab** (the only approved anti-toxin agent) was **discontinued by Merck effective January 2025** — the C4 (intoxication) axis is now empty white space. Microbiome therapeutics (VOWST, REBYOTA) are approved for recurrent CDI but commercially fragile.

**Primary unmet need:** Recurrence prevention. Initial cure is 80–90% (solved). 15–25% of patients relapse after a first episode, escalating to 45–65% after ≥2 recurrences. A candidate that only matches initial cure is clinically and commercially uninteresting.

**Inverted ADMET logic:** The target tissue is the colonic lumen. Non-absorption is a feature, not a bug — fidaxomicin (<1% absorbed) and vancomycin (~0% absorbed) are the gold standards. Low oral bioavailability should be scored as a safety asset (near-zero DDI risk in a polypharmacy population). Caveat: gut-wall P-gp/CYP3A4 inhibition is still possible even without systemic absorption.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PIPELINE CONFIGURATION

**Disease Model Structure:** Hybrid — 7 sequential phases + 3 concurrent modules, operationalized as 8 causal intervention axes (C1–C8) by the Pathway Analyst

**Agents Run (17):**

| Phase | Agents |
|-------|--------|
| Phase 0 | Disease Research Agent |
| Phase 1 (×6) | Medicinal Chemist · Clinical Landscape Researcher · Traditional Medicine Expert · Molecular Target Analyst · Pharmacokinetics Specialist · CDI Biology Specialist |
| Phase 2 (×5) | Pathway Analyst · Safety Pharmacologist · Drug Repurposing Strategist · SAR Analyst · Literature Reviewer |
| Debate (×2) | Devil's Advocate · Integration Agent |
| Phase 3 (×3) | Candidate Ranker · Combination Designer · Clinical Feasibility Assessor |

**Agents Skipped:** None — CDI's tri-modal nature (infectious + ecological + immunological) made all domain perspectives relevant, including the Ethnobotany Expert (berberine, kutaja, and traditional antidiarrhoeals have CDI-relevant pharmacology).

**Known Failed Approaches (12 entries from §4.5, verified by Literature Reviewer):**

| Approach | Outcome | Lesson |
|----------|---------|--------|
| Ridinilazole | Phase 3: met non-inferiority, missed superiority on composite; **recurrence reduction was significant (8.1% vs 17.3%, P=.0002)** but initial cure was 6.2 pts worse | Initial cure is the binding constraint, not recurrence biology |
| Surotomycin | Trial 2 met non-inferiority; Trial 1 did not | Same pattern |
| Cadazolid | Failed Phase 3 (inconsistent across 2 trials) | Narrow-spectrum antibacterial alone is insufficient |
| Tolevamer | Phase 3: inferior to both vancomycin and metronidazole | Toxin sequestration without antibacterial activity fails |
| Actoxumab (anti-TcdA) | No added benefit; increased mortality as monotherapy | TcdA-directed strategies do not work |
| PF-06425090 (Pfizer toxoid vaccine) | Phase 3 (Clover) missed primary endpoint | Parenteral toxoid vaccination does not prevent infection |
| ACAM-CDIFF (Sanofi Cdiffense) | Phase 3 terminated for futility (VE = −5.2%) | Same |
| PLACIDE probiotics | Largest well-powered trial (n>2,900) was negative | Conventional probiotics are a failed strategy |
| CP101 | Positive Phase 2; programme discontinued for financial reasons | Commercial viability is a non-scientific risk |
| Bezlotoxumab | Approved 2016, **discontinued Jan 2025** | CDI's commercial environment kills approved products |
| Metronidazole as first-line | Inferior to vancomycin | Systemic absorption is a liability |
| NTCD-M3 | Encouraging Phase 2; did not advance | Dormant opportunity, not a failure |

**Failure pattern synthesis:** (1) Antibacterial me-too failures — initial cure is the gate, not recurrence. (2) Single-mechanism anti-toxin failures — wrong toxin or insufficient alone. (3) Wrong-compartment immunity failures — systemic IgG doesn't prevent infection. (4) Financial/commercial death — 6 of 12 programme failures were financial, not scientific.

**Literature Corrections (3 HIGH-severity):**
1. **UDCA negative in vivo** — hamster CDI: 62.5% mortality both arms (P=0.78) despite confirmed colonic delivery (43.5% fecal bile acid pool). Failure is pharmacodynamic.
2. **Ridinilazole lesson misread** — the disease model told every agent "narrow-spectrum antibiotics are burned." Ridinilazole actually delivered the largest recurrence reduction of any single agent (53% relative), larger than bezlotoxumab's. It failed on initial cure, not recurrence.
3. **Bezlotoxumab discontinued** — Merck pulled Zinplava effective Jan 2025. The anti-toxin category is now completely empty.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## EXECUTIVE SUMMARY

The pipeline's most important finding is that **the binding constraint on CDI drug development is axis allocation and capital structure, not candidate quality.** Six of ten original candidates crowd C2 (vegetative fitness), an axis where eight programmes have failed. Meanwhile C6 (barrier/repair) has zero coverage, C1/C3/C7/C8 have one candidate each, and bezlotoxumab's withdrawal emptied C4.

The #1 recommendation — **ribaxamase** — was not in the original candidate set. It was surfaced by the Drug Repurposing Strategist as the only positive human Phase 2b asset on an unoccupied axis (C7, primary prevention), and is the only candidate whose reimbursement channel aligns buyer with beneficiary (hospital-acquired CDI prevention). For the recurrence unmet need, **CamSA** (a novel bile acid germination antagonist with ~1000× CDCA potency) and **niclosamide** (a host-directed anti-toxin with the strongest preclinical survival data in the set) are the highest-value development candidates, both requiring sub-$200K gating experiments before commitment.

The recommended action is a **$370–730K staged option book** (Stage 0) that resolves every live conflict in the pipeline before any programme-level commitment. In CDI, probability of technical success and probability of post-approval commercial survival are **anti-correlated** — the best molecules are cheap generics with negative NPV, and the best commercial defensibility belongs to NCEs with the weakest evidence. A portfolio, not a single pick, is the correct instrument.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CONSENSUS RANKING

Scoring method: Lexicographic gate architecture (Candidate Ranker), replacing the weighted averaging that the Debate Round identified as the pipeline's most serious methodological defect. **Efficacy evidence** is the dominant anchor (E, 0–8.5); **axis allocation, durability, immunocompromised usability, and feasibility** are bounded modifiers (ΣM, ±2.0 total) that reorder within a tier but cannot overturn a tier difference. A **coupled efficacy/safety filter** (K) is applied multiplicatively.

### TIER 1 — FUND (gated on named experiment)

**#1: RIBAXAMASE (SYN-004)** — Composite: **7.9**/10 (bimodal: 9.5 if diligence confirms, 3.2 if not)
- Evidence Basis: **Phase 2b human data** — the ONLY non-approved candidate with positive human efficacy data. UNVERIFIED — the #1 recommendation rests on a claim no agent in this pipeline independently confirmed
- Strongest Dimension: Axis allocation (+0.8 max) — sole occupant of C7, the only axis whose repair EXITS the recurrence loop; escapes all 4 field-wide failure modes structurally
- Biggest Risk (Devil's Advocate): Unverified Phase 2b package; CMC/tech-transfer unknown; only prevents β-lactam-driven CDI (fluoroquinolone-/clindamycin-driven CDI untouched)
- Recommended Form: Oral delayed-release capsule, administered during IV β-lactam therapy
- Key Gate: **$150–500K diligence** (expanded for CMC/tech-transfer per Feasibility) — 0.2% of programme cost
- Regulatory: BLA; 12 years BPCIA exclusivity (not QIDP-eligible per Feasibility correction)
- Commercial: Only candidate with aligned buyer = beneficiary (hospital pharmacy captures avoided HAC + readmission penalties)
- Feasibility: Phase 3 needs ~900–1,100 patients (high-risk enriched label) at $150–280M; price ceiling $800–1,500/course on enriched NNT

**#2: CamSA (cholic acid m-aminobenzenesulfonamide)** — Composite: **6.9**/10
- Evidence Basis: Mouse-validated germination protection (single lab); ~1000× CDCA potency (germination assay, knowledge-based); one amide coupling from generic API
- Strongest Dimension: Coupled filter K=1.05 — the ONLY candidate where the same structural feature (sulfonate) drives potency AND guarantees non-absorption
- Biggest Risk: Never synthesised at scale; potency figure not independently verified; class-level question (can ANY anti-germinant hold against a spore reservoir?) is unanswered
- Key Gate: **Bile-acid germination dose-response plate ($50–100K)** — resolves 5 candidates on one plate
- Novel argument (Combination Designer): CamSA is the mechanistically better LBP partner because CspC competitive antagonism is receptor-mediated and operates below the detergent threshold that would suppress consortium engraftment

**#3: NICLOSAMIDE** — Composite: **6.4**/10
- Evidence Basis: Tam 2018 *Nat Commun* — 100% vs 45% survival, epidemic RT027/UK1, therapeutic dosing, dose-response, positive recurrence arm, microbiota preserved, NO antibacterial activity. Mechanism: host proton shuttle raising endosomal pH — blocks ALL three toxins (TcdA + TcdB + CDT) at one shared host step
- Strongest Dimension: Fills the C4 (intoxication) axis vacated by bezlotoxumab — the only small-molecule anti-toxin in the set
- Biggest Risk (Devil's Advocate, 70% kill prob): Efficacy and toxicity are the SAME physical property. Protonophore mechanism = intrinsic uncoupler. CDI destroys the barrier enforcing the safety margin. K=0.85 (serious coupling)
- Key Gate: **Niclosamide selectivity ratio ($60–120K)** — uncoupling vs anti-TcdB in colonocyte model
- SAR Note: Nitro is load-bearing for pKa, but 4'-SO₂CH₃ is a viable replacement (σp 0.72) per SAR Analyst; three marketed salicylanilides work without nitro

### TIER 2 — BUY OPTION

| # | Candidate | Score | Axis | Key Fact | Option Cost |
|---|-----------|-------|------|----------|-------------|
| 4 | **Ibezapolstat** | 5.4 | C2 | FDA open to single Phase 3; only candidate with commensal-spectrum data. BUT: C2 graveyard (A=−1.0) | Private financing |
| 5 | **Berberine** | 5.3 | C5 | Replicated positive mouse survival; host+microbiota mechanism (NOT antibacterial, MIC ~491 mg/L). BUT: cyclosporine DDI excludes transplant patients; spo0A upregulation; no clean therapeutic window (Wnt conflict with C6, constipation masks diarrhoea endpoint). 13× more capital-efficient than ribaxamase | ~$11M IIT |
| 6 | **UDCA** | 4.2 | C1 | Sole C1 occupant; fastest 505(b)(2). BUT: negative hamster data despite confirmed delivery. Score capped by hamster ceiling. Buy the $1–3M option, not the $45–85M programme | $1–3M Stage 0 PK |
| 7 | **Nitazoxanide** | 4.0 | C2 | Only candidate with existing human CDI efficacy data. Wrong-endpoint tier (initial cure in replacement design) | 505(b)(2) |
| 8 | **Hydroxychloroquine** | 3.7 | C4 | Best $/information in the set. Solves the C2m compartment problem — absorbed, concentrates in acidic endosomes basolaterally | **$30–60K in vitro** |

### TIER 3 — KILL

| Candidate | Score | Reason |
|-----------|-------|--------|
| Aprepitant | 0.9 | All evidence TcdA-anchored (the failed toxin). Triple CYP liability |
| Ebselen | 0.8 | Target valid, molecule dead. Activity abolished by 5% blood. Se at 290–575× UL. Class rule: soft-electrophile covalent chemistry non-viable in CDI lumen |
| Conessine | 0.0 | Structurally falsified (0/4 pharmacophore elements). RED safety dealbreaker |

### WITHDRAWN
**Bezlotoxumab** — Merck discontinued Jan 2025. Mechanism validation stands; commercial availability does not.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## RECOMMENDED COMBINATION

The Combination Designer replaced three separate combinations with a **unified architecture** serving two populations plus a prevention arm:

```
═══════════════════════════════════════════════════════════════════
 THE CDI COMBINATION ARCHITECTURE
═══════════════════════════════════════════════════════════════════

 UPSTREAM   ┌───────────────────────────────────────────────────┐
 (pre-       │  RIBAXAMASE during IV β-lactam therapy      [C7]  │
  disease)   │  Blocks loop ENTRY. Orthogonal to everything.     │
             └───────────────────────────────────────────────────┘
                                    ↓ (if CDI occurs)
 BACKBONE   ┌───────────────────────────────────────────────────┐
 (all        │  FIDAXOMICIN d0–10                [C2·C3·C8·C7↑] │
  patients)  │            ↓ sequential, never concurrent         │
             │  C1 ANTI-GERMINANT wk 2–12                 [C1]  │
             │  UDCA/chenodiol (probe) → CamSA (asset)          │
             └───────────────────────────────────────────────────┘
                        ↓                          ↓
 MODULE     ┌──────────────────┐      ┌──────────────────────┐
             │ IMMUNOCOMPETENT  │      │ IMMUNOCOMPROMISED    │
             │ + LBP: VOWST /   │      │ + oral TcdB-IgY [C4] │
             │   REBYOTA / VE303│      │   (or nothing, v1)   │
             │            [C7]  │      │ ZERO live organisms  │
             └──────────────────┘      └──────────────────────┘
               5.0–5.5 axes                 4.5–6.5 axes
═══════════════════════════════════════════════════════════════════
```

**Key design principles:**
1. **Add-on only** — replacement trials 0-for-3; add-on trials 3-for-3
2. **Sequential, not concurrent** — bile acids cause diarrhoea (the primary endpoint); post-acute deployment moves the C1 endpoint to toxin-confirmed recurrence
3. **One asset, two labels** — the C1 anti-germinant is the same molecule for both populations; immunocompromised is the entry label, immunocompetent is the expansion
4. **CamSA > UDCA as LBP partner** — operates below the detergent threshold that suppresses consortium engraftment
5. **Berberine dropped from all combinations** — no clean therapeutic window (Wnt conflict + constipation masking + vancomycin-biofilm interaction)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## EXPERT AGREEMENT MAP

### Phase 1 Scores (6 agents, 0–10)

| Candidate | Chem | Clin | Ethno | Targ | ADMET | Dis | R1 Mean |
|-----------|------|------|-------|------|-------|-----|---------|
| Fidaxomicin *(bench)* | 9.0 | 8.5 | — | 8.0 | 10.0 | 9.0 | **8.9** |
| Bezlotoxumab *(bench)* | 6.5 | 6.5 | — | 8.0 | 6.0 | 8.5 | **7.1** |
| UDCA | 7.5 | 7.0 | 7.5 | 7.5 | 6.0 | 7.0 | **7.1** |
| Ibezapolstat | 7.0 | 6.0 | — | 7.0 | 9.0 | 5.5 | **6.9** |
| Berberine | 5.0 | 6.0 | 8.0 | 6.0 | 8.0 | 7.0 | **6.7** |
| Vancomycin *(bench)* | 6.0 | 7.0 | — | 7.0 | 9.0 | 4.0 | **6.6** |
| Ebselen | 5.0 | 6.5 | — | 8.5 | 4.0 | 8.0 | **6.4** |
| Niclosamide | 4.0 | 5.5 | — | 5.5 | 3.0 | 7.5 | **5.1** |
| Aprepitant | 4.5 | 5.0 | — | 5.0 | 5.0 | 5.0 | **4.9** |
| Conessine | 3.0 | 3.0 | 5.5 | 5.0 | 2.0 | 4.0 | **3.8** |

### Notable Disagreements and Resolutions

| Conflict | Spread | Resolution |
|----------|--------|-----------|
| Ebselen: Target 8.5 vs ADMET 4.0 | 4.5 pts | **Resolved for ADMET.** Activity abolished by 5% blood; selenium toxicity at anti-infective doses; molecule dead. Class rule established: soft-electrophile covalent chemistry non-viable in CDI lumen. |
| Vancomycin: ADMET 9.0 vs Disease 4.0 | 5.0 pts | **Both correct.** Perfect PK, terrible ecology — CDI's central paradox. |
| Niclosamide: Disease 7.5 vs ADMET 3.0 | 4.5 pts | **Partially resolved.** Mechanism validated and upgraded (host proton shuttle). Delivery paradox remains: target inside host cells, non-absorption heuristic works against it. |
| UDCA: Pathway 7.5 vs Literature 3.0 | 4.5 pts | **Resolved for Literature on efficacy; Pathway on mechanism.** Mechanism is sound; in vivo translation has failed once. |
| Berberine: Ethno/ADMET 8.0 vs Chemist 5.0 | 3.0 pts | **Partially resolved.** Mechanism reclassified to host+microbiota (not antibacterial). Fecal-matrix MIC is the wrong test. DDI exclusion limits strategic value. |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DEVIL'S ADVOCATE: TOP CONCERNS

| # | Concern | Kill Prob | Verdict |
|---|---------|----------|---------|
| 1 | **Rankings not traceable to inputs** — synthesis fabricated berberine claim, inflated niclosamide above inputs, averaged non-commensurable scores | 90% | **UPHELD — all three corrected.** Dimensional scoring adopted. |
| 2 | **Niclosamide efficacy/toxicity coupling** — protonophore = intrinsic uncoupler; CDI barrier damage increases both | 70% | **STANDS.** Partially reframed (safety margin = metabolic clearance, not insolubility). Gated on selectivity experiment. |
| 3 | **Pipeline scores on worst-translating endpoint** — sustained response = strongest negative correlate of translation success (36% base rate) | 65% | **SURVIVES** — partially blunted but real |
| 4 | **UDCA refuted; Pathway didn't see it** | 60% | **PARTIALLY** — kill overshoots (hamster underpowered), but 6.5 was unsupportable. Scored at 4.2. |
| 5 | **Combination = 3 products + 3 unresolved vetoes** | 55% | **PARTIALLY** — combination reframed into unified architecture, not abandoned |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DISEASE MODEL COVERAGE ANALYSIS

| Axis | Coverage | Candidates | Status |
|------|----------|-----------|--------|
| **C1** Germination | 1 credible + 1 option | CamSA, UDCA | Single occupant after UDCA downgrade |
| **C2** Vegetative fitness | **6 candidates, 8 failures** | Fidaxomicin, vancomycin, ibezapolstat, etc. | **OVER-SERVED** |
| **C3** Toxin regulation | 1 (incidental) | Fidaxomicin | Thin but covered |
| **C4** Intoxication | 1 (post-withdrawal vacancy) | Niclosamide; HCQ (lottery) | Filled by niclosamide |
| **C5** Host inflammation | 2 | Berberine, (aprepitant killed) | Covered, thin evidence |
| **C6** Barrier/repair | **ZERO** | None | **WIDEST WHITE SPACE** |
| **C7** Ecological restoration | 1 treatment + 1 prevention | LBPs; ribaxamase | Only axis that exits the recurrence loop |
| **C8** Sporulation | 1 (incidental) | Fidaxomicin | Thin but covered |

**Critical Gap:** C6 (barrier/repair) — zero coverage across all 15 candidates. The only data-backed chemotype (flavonoids) carries class-wide Wnt/β-catenin suppression that conflicts with crypt stem cell renewal. The correct C6 agent is a GLP-2R/EGFR growth-factor class (teduglutide-like), absent from the candidate set.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PATH TO PATIENTS

### Single Best Programme
**Acquire and develop ribaxamase** on a high-risk-enriched primary-prevention label.
- Regulatory: BLA; 12-year BPCIA exclusivity
- Trial: ~900–1,100 patients (high-risk enriched)
- Timeline: 5–7 years, gated on $150–500K diligence
- Cost: $150–280M (excluding acquisition)
- Funding: BARDA/ASPR + hospital-channel strategic partner
- Commercial: Buyer = beneficiary (hospital pharmacy captures avoided HAC + readmission penalties)

### Portfolio: Staged Option Book

**Stage 0 — Buy information, commit nothing ($370–730K, 0–6 months):**

| # | Experiment | Cost | Resolves |
|---|-----------|------|----------|
| 1 | Ribaxamase Phase 2b + CMC diligence | $150–500K | Top recommendation |
| 2 | Anaerobic fecal-slurry stability (5 candidates) | $80–150K | Colonic viability |
| 3 | Commensal-spectrum MIC panel | $100–200K | Central selectivity question |
| 4 | Bile-acid germination dose-response | $50–100K | First-ever UDCA IC₅₀; resolves 5 candidates |
| 5 | Niclosamide selectivity ratio | $60–120K | Gates #3 candidate |
| 6 | HCQ TcdB entry-blockade in vitro | $30–60K | Lottery on empty C4 axis |

**Stage 1 — Two programmes on independent axes:**
- **A: Ribaxamase** (C7, prevention) — human evidence; commercial risk
- **B: CamSA ± UDCA** (C1, immunocompromised recurrence) — rodent evidence; biology risk

### Capital Structure Reality
Every top repurposing candidate is a cheap generic with negative NPV. Naming a path without naming the funder is how programmes die. The Feasibility Assessor notes berberine's $11M IIT is 13× more capital-efficient per unit probability of patient access than ribaxamase.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CONFIDENCE & CAVEATS

| Claim | Confidence |
|-------|-----------|
| Strategic diagnosis (axis allocation, capital constraint) | **HIGH** |
| Kills: ebselen, conessine, aprepitant | **HIGH** |
| Literature corrections (UDCA, ridinilazole, bezlotoxumab) | **HIGH** |
| Ribaxamase as #1 (strategic logic) | **HIGH**; (specific data) **LOW-MODERATE** |
| Niclosamide safety coupling | **MODERATE-HIGH** |
| CamSA as #2 | **MODERATE** |
| UDCA at 4.2 | **LOW-MODERATE** (genuinely unresolved) |
| Berberine at 5.3 | **MODERATE** |

**Key Assumptions:**
1. P(ribaxamase diligence confirms) = 0.75 — rank #1 robust down to P≈0.55
2. CamSA ~1000× potency is unverified
3. "Can ANY anti-germinant hold against a spore reservoir?" is unanswered — 4 of 12 live candidates exposed
4. All composites are ordinal, not interval

**Missing Data:** No CDI dataset in project (OM-specific); stereochemistry-blind descriptors (UDCA/CDCA/DCA share one row). CDI preclinical→clinical translation: 36%. Sustained-response endpoint: strongest negative correlator of translation success.

**Research Disclaimer:** This is a computational multi-agent analysis. No experimental work was performed. The pipeline's most reliable outputs are its **negative findings** (kills, refutations); positive rankings carry lower confidence. All conclusions require experimental validation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## INDIVIDUAL AGENT REPORTS

All archived in `data/reports/disease-explorer/clostridioides-difficile/2026-08-17/agents/`:

| File | Agent | Size |
|------|-------|------|
| `p1-chemist.md` | Medicinal Chemist | 86 KB |
| `p1-clinical-landscape.md` | Clinical Landscape Researcher | 68 KB |
| `p1-ethnobotany.md` | Traditional Medicine Expert | 61 KB |
| `p1-target-profiler.md` | Molecular Target Analyst | 47 KB |
| `p1-admet.md` | Pharmacokinetics Specialist | 62 KB |
| `p1-disease-modeler.md` | CDI Biology Specialist | 119 KB |
| `p2-pathway.md` | Pathway Analyst | 80 KB |
| `p2-safety.md` | Safety Pharmacologist | 103 KB |
| `p2-repurposing.md` | Drug Repurposing Strategist | 82 KB |
| `p2-sar.md` | SAR Analyst | 86 KB |
| `p2-literature.md` | Literature Reviewer | 72 KB |
| `debate-advocate.md` | Devil's Advocate | 43 KB |
| `debate-integrator.md` | Integration Agent | 54 KB |
| `p3-ranker.md` | Candidate Ranker | 58 KB |
| `p3-combos.md` | Combination Designer | 85 KB |
| `p3-feasibility.md` | Clinical Feasibility Assessor | 11 KB (partial) |

Supporting: `disease-model.md` (1,116 lines) · `data-inventory.md` · `round1-complete-scores.md` · `round2-synthesis.md` · `debate-summary.md`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
*End of consensus report.*
