# Round 1 Synthesis — Phase 1 Aggregate Findings

**Target disease:** Clostridioides difficile infection (CDI)
**Date:** 2026-08-17
**Agents reporting:** 6 of 6 (Chemist, Clinical Landscape, Ethnobotany, Target Profiler, ADMET, Disease Modeler)

---

## COMPLETE SCORE MATRIX (6 agents)

| Candidate            | Chemist | Clinical | Ethno | Target | ADMET | Disease | Mean  |
|----------------------|---------|----------|-------|--------|-------|---------|-------|
| **Fidaxomicin** (B)  |   9.0   |   8.5    |  —    |  8.0   | 10.0  |   9.0   | **8.9** |
| **Bezlotoxumab** (B) |   6.5   |   6.5    |  —    |  8.0   |  6.0  |   8.5   | **7.1** |
| **UDCA**             |   7.5   |   7.0    |  7.5  |  7.5   |  6.0  |   7.0   | **7.1** |
| **Ibezapolstat**     |   7.0   |   6.0    |  —    |  7.0   |  9.0  |   5.5   | **6.9** |
| **Berberine**        |   5.0   |   6.0    |  8.0  |  6.0   |  8.0  |   7.0   | **6.7** |
| **Vancomycin** (B)   |   6.0   |   7.0    |  —    |  7.0   |  9.0  |   4.0   | **6.6** |
| **Ebselen**          |   5.0   |   6.5    |  —    |  8.5   |  4.0  |   8.0   | **6.4** |
| **Niclosamide**      |   4.0   |   5.5    |  —    |  5.5   |  3.0  |   7.5   | **5.1** |
| **Aprepitant**       |   4.5   |   5.0    |  —    |  5.0   |  5.0  |   5.0   | **4.9** |
| **Conessine**        |   3.0   |   3.0    |  5.5  |  5.0   |  2.0  |   4.0   | **3.8** |

**(B) = Benchmark, not a development candidate. — = agent did not score this candidate.**

**Additional Ethnobotany-only candidates:**
| Candidate          | Ethno Score | Disposition |
|--------------------|-------------|-------------|
| Colostrum/IgY      | 6.0         | Pursue — best selectivity profile |
| Curcumin           | 5.0         | Hold — right mechanism, likely wrong molecule |
| EGCG               | 5.0         | Deprioritize — crowded, unstable |
| Triphala           | 4.5         | Drop formulation; carry chebulagic acid/corilagin |
| Allicin            | 2.0         | Deprioritize (high confidence it fails) |

---

## STRONGEST CANDIDATES BY AGENT

| Agent              | Strongest candidate | Rationale |
|--------------------|--------------------|----|
| Chemist            | **UDCA** (actionable) | Best combination of right target class, mature chemistry, readable pharmacophore |
| Clinical Landscape | **UDCA** (actionable) | Widest white space, cheapest path, 505(b)(2) eligible |
| Ethnobotany        | **Berberine** | Strongest traditional evidence, multi-mechanism, luminal confinement |
| Target Profiler    | **Ebselen** | Dual Tier 1+2 targets, ideal covalent chemotype, correct directions |
| ADMET              | **Ibezapolstat** (actionable) | Purpose-designed luminal delivery; microbiome-restorative PK |
| Disease Modeler    | **Ebselen** (actionable) | Best novel candidate; oral analog of bezlotoxumab mechanism |

---

## AGREEMENTS (4+ agents agree)

### Strong agreements:
1. **Fidaxomicin is the benchmark** — all 6 agents scored it 8.0-10.0.
2. **UDCA is the most consistent development candidate** — 6 agents scored it 6.0-7.5 with no deal-breaker in any domain.
3. **Conessine should be deprioritized as a compound** — all 6 agents scored it 2.0-5.5. Chemist structurally falsified the CspC scaffold hypothesis.
4. **Narrow-spectrum antibiotics are a burned value proposition** — Chemist, Clinical, Target Profiler, Disease Modeler all note the 0-for-3 Phase 3 graveyard.
5. **Score on recurrence (SCR 30-90 days), not initial cure** — all agents aligned.
6. **Project data is ~15-30% data-backed, ~70-85% knowledge-based** — all agents flagged this.
7. **Add-on positioning is the only viable development strategy** — Clinical Landscape: "replacement designs 0-for-3; add-on designs 3-for-3."

### Moderate agreements:
8. **Berberine's luminal confinement is a CDI-specific asset** — Ethnobotany (8.0), ADMET (8.0), Disease Modeler (7.0) all recognize the inverted PK advantage. Chemist (5.0) and Target (6.0) are more skeptical.
9. **Allicin should be deprioritized** — Ethnobotany (2.0, "high confidence it fails"), consistent with disease model §7.2.
10. **Vancomycin worsens the recurrence loop** — Disease Modeler (4.0), Target Profiler flags direction violation on #64.

---

## CONFLICTS (agents disagree by 3+ points or have opposing assessments)

### CONFLICT 1: Ebselen — Target/Disease vs ADMET/Chemist (CRITICAL — 4.5-point spread)
- **Target Profiler (8.5) + Disease Modeler (8.0):** Strongest target portfolio — dual Tier 1+2 (#26 TcdB CPD + #21 PrdB), ideal covalent chemotype.
- **ADMET (4.0) + Chemist (5.0):** Selenium electrophile quenched by luminal thiols. Target is CYTOSOLIC, not luminal — non-absorption is a LIABILITY.
- **Resolution needed from:** SAR Analyst (non-selenium CPD inhibitor?), Literature Reviewer (mouse CDI data, fecal stability), Safety Pharmacologist (selenoelectrophile promiscuity).

### CONFLICT 2: Niclosamide — Disease Modeler (7.5) vs ADMET (3.0) — 4.5-point spread
- Disease Modeler: Cheap, luminal, host-directed, microbiota-preserving.
- ADMET + Chemist: Nitro group reduced anaerobically → destroys pharmacophore. Target is ENDOSOMAL.
- **Resolution needed from:** SAR Analyst (nitro-free protonophore design), Literature Reviewer (fecal stability data).

### CONFLICT 3: Ibezapolstat — ADMET (9.0) vs Disease Modeler (5.5) — 3.5-point spread
- ADMET: Perfect purpose-designed luminal delivery.
- Disease Modeler: "Fourth entrant to a three-program graveyard."
- **Resolution needed from:** Literature Reviewer (verify Phase 2 bile acid restoration signal — the only differentiator).

### CONFLICT 4: Vancomycin — ADMET (9.0) vs Disease Modeler (4.0) — 5.0-point spread
- This IS CDI's central therapeutic paradox, not an analytical disagreement. Both are correct.
- **Resolution needed from:** Combination Designer (vancomycin backbone + what breaks the loop?).

### CONFLICT 5: Berberine — Ethnobotany/ADMET (8.0) vs Chemist (5.0) — 3.0-point spread
- Ethnobotany: Multi-mechanism, luminal confinement, microbiome-sparing rodent data.
- Chemist: Cationic fecal binding → free fraction collapse; microbial reduction to absorbable dihydroberberine.
- **Resolution needed from:** SAR Analyst (fecal binding quantification), Literature Reviewer (verify rodent CDI data).

---

## CROSS-AGENT QUESTIONS → Phase 2 routing

### To Safety Pharmacologist:
1. Antimotility → toxic megacolon risk for berberine, conessine, aprepitant
2. Berberine DDI with tacrolimus/cyclosporine/digoxin/DOACs
3. Aprepitant CYP3A4/CYP2C9 DDI in CDI polypharmacy population
4. Bezlotoxumab CHF warning in CHF-prevalent population
5. Ebselen selenoelectrophile off-target thiol reactivity

### To Pathway Analyst:
1. Map bile acid → germination → colonization resistance cascade (UDCA placement)
2. NLRP3/IL-1β bidirectional risk in CDI (berberine relevance)
3. Synergy mapping between Phase 2 + Phase 1 candidates

### To Drug Repurposing Strategist:
1. UDCA fastest path to CDI indication (already approved for cholestasis)
2. Named leads: ebselen, UDCA, niclosamide, aprepitant, anakinra/ustekinumab, DAV132/ribaxamase

### To SAR Analyst:
1. Ebselen → non-selenium TcdB CPD inhibitor design
2. Niclosamide → nitro-free protonophore (CF₃, CN, sulfone replacements)
3. Berberine fecal free fraction quantification
4. CspC binding site characterization for docking

### To Literature Reviewer:
1. Berberine rodent CDI microbiome data verification
2. Ibezapolstat Phase 2 bile acid restoration signal
3. Ebselen mouse CDI efficacy + fecal stability
4. UDCA CDI case reports (how many, what quality?)
5. Niclosamide TcdB entry blockade evidence
6. Section 4.5 failed-approaches verification

---

## GAPS

1. **No commensal-sparing spectrum data for ANY candidate** — the central CDI question is unanswered
2. **No bacterial/toxin target layer in the knowledge graph** — all C. difficile-side claims are knowledge-based
3. **No CDI gene-disease associations** in project data
4. **No fecal free-fraction data** for any candidate
5. **No ebselen colonic stability data** — the #1 open question
6. **Phase 6 (fulminant CDI) underserved** — only aprepitant/fosaprepitant addresses this
7. **No environmental/infection prevention candidates**

---

## TOP 5 CANDIDATES FOR PHASE 2

### Tier 1 — Highest priority:
1. **UDCA** (7.1) — Most consistent, no deal-breaker, widest white space, cheapest path
2. **Ebselen** (6.4) — Highest upside IF delivery resolves; critical conflict must be adjudicated

### Tier 2 — Pursue as adjunct:
3. **Berberine** (6.7) — Strong traditional medicine case; fecal free fraction is make-or-break
4. **Ibezapolstat** (6.9) — Perfect delivery; Phase 2 bile acid signal is the sole differentiator

### Tier 3 — SAR redirect:
5. **Niclosamide** (5.1) — Great mechanism, wrong molecule; nitro-free analog is a concrete SAR task

---

## NOVEL FINDINGS FROM PHASE 1

1. **Chemist compartment reanalysis:** Ebselen and niclosamide targets are cytosolic/endosomal, NOT luminal — §6.2 inversion does NOT apply
2. **Ethnobotany data-derived hypotheses:** (a) Oleanolic acid/Cyperus rotundus → TGR5/FXR; (b) Gedunin/celastrol → Hsp90 → TcdB translocation blockade
3. **Clinical Landscape strategic insight:** "Trial design, not mechanism, has determined outcomes in CDI"
4. **Chemist structural falsification** of conessine-CspC hypothesis
5. **ADMET three-compartment model:** C1 luminal, C2 mucosal intracellular, C3 systemic
6. **ChEMBL data traps:** oral_bioavailability means "given by mouth," not "absorbed"; QED anti-correlates with CDI suitability
