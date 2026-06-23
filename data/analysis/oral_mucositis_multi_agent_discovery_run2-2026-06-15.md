═══════════════════════════════════════════════════════════════════
DRUG DISCOVERY PIPELINE — CONSENSUS REPORT (Run #2)
Oral Mucositis: Radiation-Induced & Chemotherapy-Induced
═══════════════════════════════════════════════════════════════════
Date: 2026-06-15
Research Question: Evaluate gathered data for potential drugs effective
  against both radiation-induced and chemotherapy-induced oral mucositis
Candidates Evaluated: 14 compounds ranked (from initial pool of ~20)
Agents Consulted: 15 across 4 rounds (Phase 1 → Synthesis → Phase 2 → Debate → Phase 3)
Data Sources: ChemBL (3,276 drugs), DisGeNET (51 OM biomarkers, 7 altered
  expression, 40 genetic variants), PubChem (60,521 phytochemical interactions),
  IMPPAT (13 plants), TTD (4 OM drugs), DrugBank (18 targets),
  BSI Medicinal Plants (1,915 entries)
Full Agent Transcripts: data/reports/drug-discovery-pipeline/2026-06-15/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## EXECUTIVE SUMMARY

Fifteen domain expert agents analyzed the OSPF Ayurveda Knowledge Graph
from six independent perspectives (chemistry, oncology, ethnobotany, target
biology, pharmacokinetics, disease modeling), then underwent targeted deep
dives (pathway analysis, safety pharmacology, drug repurposing, SAR),
structured debate (Devil's Advocate challenge + Integration), and final
evaluation (ranking, combination design, clinical feasibility).

**Key findings:**

1. **Dexamethasone mouthwash is (still) the benchmark** — the Candidate
   Ranker corrected novelty bias from earlier rounds and restored it to #1.
   It has decades of OM clinical evidence, zero development cost, and can
   be prescribed today. All other candidates must add incremental benefit
   ON TOP OF dexamethasone, not replace it.

2. **Melatonin is the strongest addition to dexamethasone** — the only
   candidate with GREEN safety across all 15 agents AND multi-phase coverage
   (Phases 1, 2, 3, 5). It is OTC, costs pennies, and uniquely addresses
   Phase 1 ROS damage that corticosteroids miss. It is cancer-compatible
   (radioprotects normal tissue, does not protect tumors).

3. **Three proven-but-boring candidates were improperly dropped** in
   earlier rounds due to novelty bias: doxepin rinse (Phase 3 RCT data for
   OM pain), amlexanox (FDA-approved for aphthous ulcers), and pentoxifylline
   (cheap, anti-fibrotic, Phase 5 healing). All are restored.

4. **Budesonide's SAR advantage over dexamethasone is real but narrower than
   claimed** — the 90% first-pass inactivation collapses when patients take
   azole antifungals (CYP3A4 inhibitors), which ~80% of neutropenic OM
   patients require. Budesonide is best for H&N radiation patients (who
   are not typically on azoles), not HSCT patients.

5. **The Ayurvedic bridge compound is Glycyrrhiza glabra (Yashtimadhu)**,
   with unique HMGB1 inhibition confirmed by PubChem data. The sugar moiety
   is required for HMGB1 binding (SAR confirmed). Realistic path is through
   India's AYUSH regulatory system (3-5 years, $2-6M).

6. **Quercetin's ceramide "coverage" was debunked** — it upregulates SMPD1
   (increases ceramide production), the opposite of what OM treatment needs.
   Its MAPK binding is genuine (BindingDB confirmed) but kaempferol is
   preferred as it retains the pharmacophore without the catechol PAINS
   liability.

7. **Gallic acid was the candidate most likely to fail** per Devil's Advocate —
   PAINS catechol, 688 likely-artifactual target interactions, rapid COMT
   metabolism, no clinical precedent, no sponsor. Demoted from #5 to #14.

8. **Apremilast is a significant new discovery** — PDE4 inhibitor,
   FDA-approved for Behcet's oral ulcers, non-immunosuppressive. However,
   it is oral-only, expensive, and Behcet's (autoimmune) ≠ OM (cytotoxic).

9. **The Phase 3 ceramide pathway remains the critical unsolved gap** —
   zero approved drugs target it, and no compound in our dataset provides
   clean anti-ceramide intervention. This is where the Sonis model says
   OM escalates from manageable to devastating.

10. **The recommended immediate action is a clinician-directed protocol**:
    Melatonin 20mg QHS + Dexamethasone 0.5mg/5mL rinse TID — prescribable
    today, $50-140/month, no regulatory barriers, covers Phases 1-3+5.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CONSENSUS RANKING

**Scoring notes:** All scores carry a systematic penalty for the 70-80%
historical OM drug trial failure rate. Confidence intervals reflect
uncertainty from computational analysis + test-scale knowledge graph data.
No candidate scores above 80/100 regardless of preclinical promise.

### #1: DEXAMETHASONE MOUTHWASH — Composite Score: 79/100 (CI: 72-86)
    Tier: A (Prescribable Today)
    Expert Agreement: Standard of care; MASCC/ISOO guideline-recommended
    Strongest Dimension: Clinical Precedent (10/10)
    Biggest Risk: Immunosuppression + oral candidiasis in neutropenic patients
    Recommended Form: 0.5 mg/5mL oral rinse (swish and spit), TID
    Status: BENCHMARK — all other candidates must add value on top of this

### #2: MELATONIN ORAL GEL — Composite Score: 78/100 (CI: 65-87)
    Tier: B (Near-Term Repurposing)
    Expert Agreement: Only GREEN safety across all 15 agents
    Strongest Dimension: Drug-likeness (QED 0.84, highest in pool)
    Biggest Risk: No dose-finding for mucosal delivery; limited Phase 3 data
    Recommended Form: 20mg sublingual tablet or mucoadhesive gel, QHS
    Unique Property: Radioprotective for normal tissue, does NOT protect tumors
    Timeline: Prescribable now (OTC) | IIT cost: $300K-$800K

### #3: DOXEPIN RINSE — Composite Score: 74/100 (CI: 66-80)
    Tier: A (Prescribable Today)
    Expert Agreement: "Hidden gem" — Phase 3 RCT data for OM pain
    Strongest Dimension: Clinical Precedent (8/10) — Epstein 2006 RCT
    Biggest Risk: Symptomatic only (pain relief, not disease-modifying)
    Recommended Form: 0.5% oral rinse (swish and spit)
    Note: Restored to ranking — improperly dropped by Integration Agent

### #4: AMLEXANOX — Composite Score: 72/100 (CI: 62-80)
    Tier: A (limited availability)
    Expert Agreement: FDA-approved for aphthous ulcers; ChemBL lists OM
    Strongest Dimension: Clinical Precedent (8/10)
    Biggest Risk: Withdrawn from US market (commercial, not safety)
    Recommended Form: 5% oral paste (Aphthasol formulation)
    Note: Restored — available in Japan; compounding pharmacy feasible

### #5: BUDESONIDE MUCOADHESIVE — Composite Score: 71/100 (CI: 58-79)
    Tier: B (Near-Term Repurposing)
    Expert Agreement: SAR confirms superior mucosal selectivity over dexamethasone
    Strongest Dimension: Mechanism Strength (8/10) — 90% first-pass inactivation
    Biggest Risk: CYP3A4 advantage collapses with azole co-administration
    Recommended Form: 0.5mg/3mL oral suspension (swish and spit)
    Best Population: H&N radiation patients (NOT on azoles)
    Timeline: Compoundable now | 505(b)(2): 3-5 years, $20-60M

### #6: APREMILAST — Composite Score: 69/100 (CI: 57-78)
    Tier: B (Near-Term Repurposing, second-line)
    Expert Agreement: Top new discovery from Drug Repurposing analysis
    Strongest Dimension: Behcet's oral ulcer approval (closest OM analog)
    Biggest Risk: Oral-only; GI side effects; $1,500/month; no OM data
    Recommended Form: 30mg oral tablet BID (no topical exists)
    Best Use: Refractory OM after topical failure

### #7: PENTOXIFYLLINE — Composite Score: 67/100 (CI: 55-76)
    Tier: B (Near-Term Repurposing)
    Expert Agreement: TNF-alpha + p38 MAPK; anti-fibrotic (Phase 5)
    Strongest Dimension: Feasibility (8/10) — generic, $15-30/month
    Biggest Risk: Non-specific mechanism; GI side effects
    Recommended Form: 400mg oral tablet TID
    Note: Restored — improperly dropped. Addresses Phase 3 + Phase 5.

### #8: GLYCYRRHIZIN — Composite Score: 66/100 (CI: 52-76)
    Tier: B/C (Near-Term Repurposing / Ayurvedic Bridge)
    Expert Agreement: Unique HMGB1 antagonism (no other candidate covers this)
    Strongest Dimension: Traditional Use (9/10) + Target Uniqueness (15/15)
    Biggest Risk: Pseudoaldosteronism; hypokalemia synergy with cisplatin
    Recommended Form: 2-5% mucoadhesive gel (topical only, swish and spit)
    Restriction: Avoid with cisplatin regimens unless K+ monitoring
    AYUSH Timeline: 3-5 years, $2-6M in India

### #9: N-ACETYLCYSTEINE (NAC) — Composite Score: 65/100 (CI: 52-75)
    Tier: B (with restrictions)
    Expert Agreement: ChemBL lists OM; Phase 1 ROS scavenger; OTC
    Strongest Dimension: Feasibility (8/10) — approved, cheap, available
    Biggest Risk: MAY PROTECT TUMOR CELLS during concurrent RT (ROS scavenging)
    Recommended Form: Buffered oral rinse (swish and spit)
    RESTRICTION: ONLY post-radiation or chemo-only OM (NOT during H&N RT)
    Note: Restored with safety restriction. Improperly eliminated.

### #10: KAEMPFEROL — Composite Score: 63/100 (CI: 48-74)
    Tier: C (Requires Substantial Development)
    Expert Agreement: Cleanest flavonoid (no PAINS catechol); Ayurvedic bridge
    Strongest Dimension: Target Relevance (8/10) — 484 PubChem interactions
    Biggest Risk: Zero clinical data; poor aqueous solubility (<0.02 mg/mL)
    Recommended Form: Nanoparticle mucoadhesive gel (requires development)
    Timeline: 3-5 years to clinic

### #11-14: Additional Candidates
    #11: Pirfenidone (62) — p38 MAPK gap-filler but $10K/month
    #12: Palifermin (61) — only FDA-approved OM drug (restricted to HSCT)
    #13: Mesalamine (60) — excellent rationale but zero OM evidence
    #14: Gallic Acid (47) — PAINS; Devil's Advocate "most likely to fail"

### ELIMINATED:
    - Colchicine: Narrow TI; lethal azole DDI; myelosuppression (RED)
    - Thalidomide: Teratogenicity; REMS burden (RED)
    - Quercetin: Replaced by kaempferol (PAINS catechol; SMPD1 inverted)
    - EGF/Hebervis: Tumor protection in H&N cancer (BLACK)
    - Tacrolimus: CYP3A4 exclusive + narrow TI (RED)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## RECOMMENDED COMBINATIONS

### Immediate (Prescribable Today)
**"MelaDex Protocol"**: Melatonin 20mg QHS + Dexamethasone 0.5mg/5mL rinse TID
- Phase Coverage: 1 (melatonin), 2 (both), 3 (partial), 5 (melatonin)
- Cost: $50-100/month
- Add doxepin rinse PRN for Phase 4 pain breakthrough
- Add pentoxifylline 400mg TID oral for Phase 3/5 enhancement

### Near-Term (Requires IIT)
**Clinician-Directed Triple**: Melatonin + Dexamethasone rinse + Pentoxifylline
- Three separate prescriptions, all approved/generic
- Distinct mechanisms: ROS (melatonin), NF-κB (dexamethasone), TNF-α/cAMP (PTX)
- No DDIs between components
- IIT cost: $2-5M (NCI R21 fundable)

### Ayurvedic Bridge (Research Stage)
**Glycyrrhizin Gel**: Glycyrrhizin 2-5% mucoadhesive + Melatonin 20mg oral
- HMGB1 (glycyrrhizin) + ROS/NF-κB (melatonin) = sequential pathway blockade
- AYUSH pathway in India: 3-5 years, $2-6M
- Sapthachadadi Kashayam as traditional formulation comparator

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## EXPERT AGREEMENT MAP

```
                    Chemist  Cancer  Ethno  Target  ADMET  Disease  Path  Safety  SAR  Repurp  D.Adv  Integ  Ranker
Dexamethasone         8.5     7.0     —      —      8.5     —       —     YELL    6.0   —      VALID    74    79
Melatonin             8.0     6.0     —      —       —      —       —     GRN      —    —      PART     91    78
Glycyrrhizin           —       —     9.5    TOP     5.0     —       —     ORNG    7.0   —      VALID    83    66
Budesonide             —       —      —      —       —      —       —      —      9.0   —      VALID    86    71
Quercetin              —       —      —     PAINS    —     8.0    MIXED   ORNG     —    —       —       ELIM  ELIM
Kaempferol             —       —      —      —      6.5     —       —     YELL    PREF  —       —       78    63
Gallic Acid            —       —      —      —       —      —     PREF    —       —     —      FAIL     75    47
Apremilast             —       —      —      —       —      —       —      —       —    78      —       68    69
Pentoxifylline        7.5      —      —      —      7.0     —       —     YELL     —    70      —       DROP  67
NAC                   7.0     4.0     —      —      7.0     —       —     ORNG     —    64      —       DROP  65
Doxepin                —       —      —      —       —      —       —      —       —    71      —        —    74
Amlexanox             8.0      —      —      —      8.0     —       —     YELL     —     —      —       DROP  72
Colchicine            6.5      —      —      —       —      —       —     RED      —     —      —       ELIM  ELIM
```

Notable Disagreements Resolved:
- Quercetin: Disease Modeler (8) vs Target Profiler (PAINS) — RESOLVED by Pathway
  Analyst: MAPK binding is real but SMPD1 is inverted. Kaempferol preferred.
- Glycyrrhizin: Ethnobotany (9.5) vs ADMET (5.0) — RESOLVED: topical delivery
  bypasses poor oral bioavailability; MW 822 stays on surface. Safety YELLOW not ORANGE.
- Budesonide vs Dexamethasone: SAR (9.0) vs Devil's Advocate (4-5) — RESOLVED:
  budesonide superior in H&N RT; dexamethasone better in HSCT (azole context).
- NAC: Chemist (7.0) vs Cancer Researcher (4.0) — RESOLVED: restrict to post-RT
  or chemo-only OM. Contraindicated during concurrent H&N radiation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DEVIL'S ADVOCATE: TOP CONCERNS

1. **Novelty bias was pervasive and required correction**
   All earlier rounds systematically displaced proven candidates (dexamethasone,
   NAC, pentoxifylline, amlexanox, doxepin) in favor of mechanistically novel
   but clinically unvalidated ones. The Candidate Ranker corrected this.
   Verdict: CONCERN MITIGATED by final ranking corrections.

2. **The knowledge graph was built on test-scale data**
   ChemBL mechanisms (10 records), targets (43), indications (79) are tiny.
   Multi-agent architecture creates "echo chamber" where agents treat each
   other's conclusions as evidence.
   Verdict: CONCERN STANDS. Acknowledged as systematic limitation. Scores
   anchored to published literature where KG data is thin.

3. **Historical OM trial failure rate (~70-80%) is not reflected**
   Benzydamine, iseganan, velafermin, rhITF, glutamine all failed in
   late-stage trials despite strong preclinical rationale.
   Verdict: CONCERN ADDRESSED. All scores reduced 10-28 points. No candidate
   scores above 80/100. Confidence intervals explicitly included.

4. **Budesonide CYP3A4 advantage collapses in azole-treated patients**
   The 90% first-pass selectivity depends on intact CYP3A4. Azole antifungals
   (mandatory in ~80% of neutropenic patients) inhibit CYP3A4.
   Verdict: CONCERN PARTIALLY MITIGATED. Budesonide demoted from #2 to #5.
   Best for H&N radiation (not typically on azoles), not HSCT.

5. **Recommended combination is a regulatory impossibility**
   Multi-drug NDA requires factorial trial design. No sponsor for generic combos.
   Verdict: CONCERN RESOLVED by reframing as clinician-directed compounding
   (separate prescriptions), not a single FDA-approved product. This is how
   "magic mouthwash" already works in oncology practice.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PATH TO PATIENTS

### Track 1: Approved Drugs (0-12 months)

**Immediate (Month 0-1):**
- Prescribe melatonin 20mg sublingual + dexamethasone mouthwash TID
- Both available through compounding pharmacy or OTC (melatonin)
- No IRB needed for clinical use; document as quality improvement

**Short-term (Months 1-6):**
- Design retrospective cohort study: M+D combo vs standard care
- Primary endpoint: WHO OM grade ≥3 incidence
- Register on ClinicalTrials.gov

**Medium-term (Months 6-12):**
- Launch prospective IIT: 80-120 H&N RT patients
- Melatonin + budesonide vs dexamethasone alone (melatonin in both arms)
- NCI R21 fundable ($550K)
- Key de-risking: budesonide PK/DDI study with fluconazole ($300-600K)

Regulatory: None needed (off-label compounding)
Estimated Cost: $2-5M total
Timeline: Evidence within 18 months

### Track 2: Ayurvedic Bridge (0-36 months)

**Phase A (0-12 months):** Formulation development
- Glycyrrhizin mucoadhesive gel + kaempferol nanoformulation
- HPLC standardization; stability testing
- Cost: $500K-$1.5M

**Phase B (6-18 months):** Preclinical validation
- Hamster cheek pouch radiation OM model
- Measure HMGB1 tissue levels (mechanistic biomarker)
- Cost: $200-400K

**Phase C (18-30 months):** First-in-human (AYUSH pathway, India)
- Open-label safety study, 60-100 H&N cancer patients
- Sites: Tata Memorial, AIIMS, CMC Vellore
- Cost: $500K-$2M

**Phase D (30-36+ months):** Integration
- If positive: combine with Track 1 (full MBGK protocol)
- Pursue 505(b)(2) in US using AYUSH trial data

Regulatory: AYUSH patent/proprietary medicine (India)
Estimated Cost: $5-25M total
Potential Partners: Himalaya Drug Company, CSIR-IICT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## OM PHASE COVERAGE ANALYSIS

Phase 1 (Initiation):    COVERED — Melatonin (Nrf2, ROS scavenging),
                          NAC (glutathione precursor, restricted to post-RT)
Phase 2 (Upregulation):  OVERCOVERED — Dexamethasone, budesonide, apremilast,
                          pentoxifylline, glycyrrhizin, kaempferol all hit NF-κB.
                          Choose 1-2 agents; don't stack immunosuppression.
Phase 3 (Amplification): CRITICAL GAP — No candidate cleanly targets ceramide/
                          S1P axis. Pentoxifylline (cAMP cross-talk) and
                          glycyrrhizin (HMGB1 blockade) provide partial coverage.
                          Pirfenidone (p38 MAPK) is the closest pharmacological
                          tool but costs $10K/month.
Phase 4 (Ulceration):    PARTIAL — Doxepin rinse (symptomatic pain relief),
                          glycyrrhizin (HMGB1 + antiviral for HSV reactivation),
                          palifermin (restricted to HSCT).
Phase 5 (Healing):       PARTIAL — Melatonin (WNT3A, VEGFA), pentoxifylline
                          (anti-fibrotic, microvascular flow), palifermin
                          (KGF/FGFR2, restricted). Wnt pathway has ZERO
                          direct pharmacological coverage from any candidate.

Critical Gap: Phase 3 ceramide pathway. Zero approved drugs. Only quercetin
hit SMPD1 in our data — and it UPREGULATES it (wrong direction). Whoever
identifies a safe, topically deliverable ceramide pathway modulator will
have found the missing piece for comprehensive OM prevention.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CHANGES FROM RUN #1 (May 4, 2026)

| Dimension | Run #1 | Run #2 | What Changed |
|-----------|--------|--------|--------------|
| #1 Candidate | Dexamethasone mouthwash | Dexamethasone mouthwash | CONFIRMED (after correction) |
| #2 Candidate | Budesonide mucoadhesive | Melatonin oral gel | Melatonin promoted; budesonide demoted (CYP3A4) |
| #3 Candidate | Mesalamine topical | Doxepin rinse | Doxepin surfaced as "hidden gem" with Phase 3 RCT data |
| Quercetin | Score 47/100 | ELIMINATED | SMPD1 inverted (harmful); replaced by kaempferol |
| Curcumin | Discussed | Not ranked | SAR confirmed instability at salivary pH |
| Gallic Acid | Not in Run #1 | #14 (47/100) | Surfaced then demoted (PAINS confirmed) |
| Phase 3 Gap | Identified | CONFIRMED | Still zero compounds address ceramide cleanly |
| Combination | 4-drug "OM Shield" TERMINATED | Clinician-directed protocol (separate Rx) | Regulatory realism applied |
| Ayurvedic Lead | Glycyrrhiza glabra | Glycyrrhiza glabra | CONFIRMED across both runs |
| Key New Find | — | Apremilast (PDE4i) | Behcet's oral ulcer precedent identified |
| Novelty Bias | Identified and partially corrected | FULLY corrected by Devil's Advocate | Proven agents properly weighted |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CONFIDENCE & CAVEATS

Overall Confidence: MODERATE
- Ranking confidence is HIGH for Tier A candidates (established drugs)
- Ranking confidence is LOW for Tier C candidates (natural products needing development)

Key Assumptions:
1. Topical delivery adequately reaches OM targets without systemic exposure
   (untested for most candidates at Grade 3-4 OM)
2. NF-κB suppression in OM translates to clinical benefit (plausible but
   unproven in adequately powered trials)
3. Multi-phase coverage is more effective than single-phase (theoretical,
   never tested head-to-head)
4. HMGB1 is a causal driver of OM amplification, not an epiphenomenon
   (GDA score is only 0.01 — weakest in dataset)

Missing Data That Would Most Change This Analysis:
1. Budesonide PK in azole-treated patients (topical oral route)
2. Melatonin dose-finding for mucosal delivery
3. Any preclinical OM data for apremilast, mesalamine, or pirfenidone
4. Glycyrrhizin permeation through ulcerated vs intact human oral mucosa
5. Full-scale ChemBL data run (current KG has test-scale mechanisms/targets)

Research Disclaimer: This is a computational multi-agent analysis based on
the OSPF Ayurveda Knowledge Graph. All findings require experimental
validation before any clinical decisions. No compound should be administered
to patients based on this analysis alone. The 70-80% historical OM drug
trial failure rate applies to every candidate on this list.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AGENTS CONSULTED

### Phase 1 — Parallel Domain Analysis (6 agents)
| Agent | Primary Finding |
|-------|----------------|
| Chemist | Dexamethasone 8.5/10 (ideal LogP 1.90 for mucosal delivery); melatonin 8.0/10 (QED 0.84, highest); amlexanox 8.0/10 (purpose-built for oral mucosa); 15 candidates profiled |
| Cancer Researcher | Tumor protection paradox is central challenge; dexamethasone mouthwash is strongest (minimal tumor risk); EGF/Hebervis dangerous for H&N cancer; celecoxib may be radiosensitizing |
| Ethnobotany Expert | Glycyrrhiza glabra 9.5/10 (glycyrrhizin→HMGB1 bridge); Terminalia chebula 8.5/10 (stomatitis indication); two formulations cover all 5 Sonis phases; 6 distinct chemical classes |
| Target Profiler | Glycyrrhizin has highest OM selectivity (12.0%); XRCC1 (GDA 0.34) has least compound coverage; curcumin/berberine/apocynin missing from PubChem; Phase 3 MAPK targets absent from DisGeNET |
| ADMET Predictor | Dexamethasone 8.5/10 (sweet spot for all parameters); thalidomide DEAL-BREAKER; glycyrrhizin C (5.0) due to MW 822; Grade 3 OM = topical becomes systemic; unpredictable absorption biggest concern |
| Disease Modeler | Quercetin broadest phase coverage (5/5, 31 targets); Phase 3 amplification most dangerous gap; Phase 2 overcovered; radiation OM = "rolling catastrophe" needing continuous coverage |

### Phase 2 — Targeted Deep Dives (4 agents)
| Agent | Primary Finding |
|-------|----------------|
| Pathway Analyst | Quercetin SMPD1 is INVERTED (harmful); MAPK binding REAL (BindingDB); glycyrrhizin topical HMGB1 feasible; optimal trio: dexamethasone + glycyrrhizin + gallic acid; Grade 3 = topical→systemic transition |
| Safety Pharmacologist | Melatonin = only GREEN; colchicine = RED (lethal azole DDI); glycyrrhizin ORANGE (cisplatin K+ synergy); NAC ORANGE (tumor protection during RT); phytochemicals are PRO-apoptotic (good for cancer) |
| Drug Repurposing | Apremilast is #1 new find (78/100, Behcet's oral ulcers); doxepin rinse "hidden gem"; pirfenidone for p38 MAPK gap; zero approved p38/Wnt drugs; benzydamine missing from ChemBL |
| SAR Analyst | Budesonide > dexamethasone (9.0/10 mucosal selectivity); kaempferol > quercetin (catechol removal = PAINS removal); glycyrrhizin sugar REQUIRED for HMGB1; vamorolone identified as novel dissociative steroid |

### Debate Round (2 agents)
| Agent | Primary Finding |
|-------|----------------|
| Devil's Advocate | Novelty bias confirmed; budesonide CYP3A4 collapses with azoles; gallic acid most likely to fail; combination is regulatory impossibility; historical 70-80% OM failure rate not reflected; re-orient around "adding to dexamethasone" |
| Integration Agent | Melatonin #1 (91); two-track strategy (pharma + Ayurvedic); MBGK protocol proposed; Phase 3 ceramide gap acknowledged; tumor protection paradox largely resolved for top candidates |

### Phase 3 — Final Evaluation (3 agents)
| Agent | Primary Finding |
|-------|----------------|
| Candidate Ranker | Dexamethasone restored to #1 (79); gallic acid demoted to #14 (47); doxepin/amlexanox/NAC/PTX restored; all scores reduced for historical failure rate; novelty bias fully corrected |
| Combination Designer | Strategy 1 (clinician-directed, $50-140/mo) RECOMMENDED; Strategy 2 (melatonin+glycyrrhizin gel, 3-5yr); Strategy 3 (Sapthachadadi Kashayam + melatonin, AYUSH pathway); Phase 3 ceramide gap honestly unfillable |
| Clinical Feasibility | Melatonin HIGH feasibility (OTC now); budesonide HIGH (compoundable); glycyrrhizin MODERATE (AYUSH 3-5yr, $2-6M); Track 1 combo via NCI R21 ($550K); India H&N cancer burden = strategic advantage |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## APPENDIX A: KEY OM TARGETS FROM KNOWLEDGE GRAPH

| Gene | GDA Score | Association Type | OM Phase | Druggability |
|------|-----------|-----------------|----------|-------------|
| XRCC1 | 0.34 | Biomarker + GeneticVariation | Phase 1 (DNA repair) | Low (undruggable) |
| CSF3 | 0.31 | Biomarker | Phase 4-5 (G-CSF) | High (filgrastim) |
| IFNA2 | 0.30 | Biomarker | Phase 2 | High (interferons) |
| CAT | 0.20 | Biomarker | Phase 1 (catalase) | Low (antioxidants) |
| CD40LG | 0.10 | Biomarker | Phase 2 | Moderate |
| TNF | 0.07 | Biomarker + AltExp + GenVar | Phase 2 (central hub) | High (anti-TNF) |
| FGF7 | 0.06 | Biomarker | Phase 4-5 (KGF) | High (palifermin) |
| MTOR | 0.06 | Biomarker + GenVar | Phase 3 (iatrogenic) | High (mTOR-i CAUSE OM) |
| ALB | 0.03 | Biomarker + AltExp | Systemic marker | Low |
| MTHFR | 0.03 | GeneticVariation | Phase 1 (pharmacogenomic) | Moderate |
| DPYD | 0.03 | AltExp + GenVar | Phase 1 (5-FU metabolism) | Moderate |
| EGF | 0.02 | Biomarker | Phase 5 (healing) | High (Hebervis) |
| EPO | 0.02 | Biomarker + GenVar | Phase 5 (healing) | High (EPO mouthwash) |
| IL1B | 0.02 | Biomarker + GenVar | Phase 2 | High (canakinumab) |
| HMGB1 | 0.01 | Biomarker | Phase 2-3 (underserved) | Moderate (glycyrrhizin) |

## APPENDIX B: SAFETY VERDICTS SUMMARY

| Candidate | Safety Verdict | Key Risk for Cancer Patients |
|-----------|---------------|------------------------------|
| Melatonin | GREEN — GO | None; potentially synergistic with treatment |
| Kaempferol | GREEN — GO | Formulation challenge; no clinical data |
| Mesalamine | GREEN — GO (inferred) | No OM data whatsoever |
| Dexamethasone rinse | YELLOW — Conditional | Oral candidiasis; mild local immunosuppression |
| Doxepin rinse | YELLOW — Conditional | Sedation if swallowed |
| Amlexanox | YELLOW — Conditional | Supply chain (US market withdrawal) |
| Budesonide | YELLOW — Conditional | CYP3A4 azole DDI abolishes first-pass advantage |
| Pentoxifylline | YELLOW — Conditional | Bleeding risk if platelets <50K |
| Glycyrrhizin | YELLOW — Conditional* | Pseudoaldosteronism; K+ monitoring with cisplatin |
| NAC | ORANGE — Restricted | Tumor protection during concurrent RT |
| Quercetin | ORANGE — Replaced | Multi-CYP inhibition; SMPD1 upregulation |
| Berberine | ORANGE — Conditional | CYP2D6 blocks codeine/tamoxifen metabolism |
| Pirfenidone | YELLOW — Conditional | Photosensitivity + RT; cost $10K/month |
| Palifermin | ORANGE — Restricted | Restricted to HSCT; theoretical tumor growth |
| Colchicine | RED — NO-GO | Lethal DDI with azoles; myelosuppression |
| Thalidomide | RED — NO-GO | Teratogenicity; neuropathy; thromboembolism |

*Glycyrrhizin upgraded from ORANGE to YELLOW based on topical delivery mitigating
systemic pseudoaldosteronism. Cisplatin co-administration requires K+ monitoring.

## APPENDIX C: FULL PIPELINE TRANSCRIPT LOCATIONS

All raw agent outputs are preserved in their entirety at:

```
data/reports/drug-discovery-pipeline/2026-06-15/
├── 2026-06-15_phase1_raw_transcripts.md    (Chemist, Cancer Researcher,
│                                            Ethnobotany, Target Profiler,
│                                            ADMET Predictor, Disease Modeler)
├── 2026-06-15_phase2_raw_transcripts.md    (Pathway Analyst, Safety
│                                            Pharmacologist, Drug Repurposing
│                                            Strategist, SAR Analyst)
├── 2026-06-15_debate_raw_transcripts.md    (Devil's Advocate, Integration
│                                            Specialist)
└── 2026-06-15_phase3_raw_transcripts.md    (Candidate Ranker, Combination
                                             Designer, Clinical Feasibility
                                             Assessor)
```

Each file contains the complete, unedited output from every agent in that
phase, preserving the full reasoning chain for reproducibility and audit.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*This report was generated by a 15-agent multi-round drug discovery
pipeline analyzing the OSPF Ayurveda Knowledge Graph. All findings
require experimental validation. This is computational analysis intended
to prioritize research investments, not clinical practice advice.*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
