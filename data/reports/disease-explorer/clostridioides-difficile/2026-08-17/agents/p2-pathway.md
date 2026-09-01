# Phase 2 — Pathway Analyst Report
## *Clostridioides difficile* Infection (CDI)

**Agent:** Pathway Analyst (network pharmacology / multi-target strategy)
**Round:** Phase 2 (targeted deep dive)
**Date:** 2026-08-18
**Inputs:** `disease-model.md` §2 (Pathobiology), §5 (Master Target List), §6 (Route); `round1-complete-scores.md`; project data in `data/processed/`
**Skill file:** `.claude/skills/pathway-analyst/SKILL.md` — **adapted**, see below

---

## 0. SKILL FILE ADAPTATION — what changed and why

My skill file encodes six *host signal transduction* cascades (NF-κB, MAPK, PI3K/AKT, ceramide, Wnt, TLR) built for Oral Mucositis, a sterile chemo/radiation injury where the entire causal graph lives inside human cells.

**CDI breaks that abstraction in three ways:**

1. **The causal graph spans three organisms** — *C. difficile*, the human host, and the commensal community. Most high-value nodes (CspC, TcdR, PrdB, `bai` operon) are not host signaling proteins at all. A pure signal-transduction framing would miss ~60% of the Master Target List.
2. **Two axes run in the RESTORE direction.** Every cascade in my OM skill file is inhibited. In CDI, targets #64–#69 must be *augmented*. Applying inhibition logic uniformly would invert the therapeutic direction on the single largest strategic gap.
3. **The topology is hybrid, not linear.** Phases 0→6 are sequential *and* Modules A/B/C run concurrently across all of them, with a **recurrence loop** feeding Phase 6 back to Phase 0. The loop, not any single node, is the disease's defining network feature — and it is what every candidate must be scored against.

**What I retained** from the skill file: the pathway-coverage matrix method, the phase-alignment guardrail ("a pathway harmful in one phase may be beneficial in another"), the crosstalk-tracing discipline, the polypharmacology double-edge principle, and the network metrics (coverage, redundancy, connectivity, crosstalk risk). Those transfer intact.

**What I rebuilt:** the cascade definitions themselves. I derived **eight CDI causal axes (C1–C8)** from §2 of the Disease Brief, defined below. These replace the six OM pathways as the columns of the coverage matrix.

---

## 1. THE CDI CAUSAL AXES (C1–C8)

Derived from the hybrid phase/module model. Each axis is a chain of causally-linked nodes where intervention at any point propagates downstream.

```
═══════════════════════════════════════════════════════════════════════════════
 THE CDI NETWORK — 8 causal axes over the hybrid phase/module topology
═══════════════════════════════════════════════════════════════════════════════

 C7 ECOLOGICAL RESTORATION  ◄──────────── THE RECURRENCE LOOP ──────────────┐
 ┌──────────────────────────────────────────────────────────────────────┐   │
 │  antibiotic ──► bai guild loss ──► DCA/LCA collapse ──► TA accumulates│   │
 │  (#70 shield)     (#64 RESTORE)      (#66 SUPPLY)      (#65 BSH)     │   │
 │  Also: valerate (#68) ↓, butyrate (#67) ↓, niche vacant (#69)        │   │
 └───────────────────────────────┬──────────────────────────────────────┘   │
                                 │ permits + actively triggers              │
 C1 GERMINATION AXIS  ◄───────────┘                                          │
 ┌──────────────────────────────────────────────────────────────────────┐   │
 │  taurocholate ──►[CspC #7]──► CspB #9 ──► pro-SleC ──► SleC #10      │   │
 │        ▲          glycine/Ca²⁺                          │            │   │
 │        │          via CspA #8                           ▼            │   │
 │  COMPETITIVE INHIBITORS (#11): CDCA, LCA, UDCA, CamSA   cortex lysis │   │
 │                                                    → DPA release     │   │
 └───────────────────────────────┬──────────────────────────────────────┘   │
                                 ▼ outgrowth                                │
 C2 VEGETATIVE FITNESS AXIS                                                 │
 ┌──────────────────────────────────────────────────────────────────────┐   │
 │  viability core: RNAP #1 · PolC #3 · MetRS #4 · PG D-Ala-D-Ala #2    │   │
 │  metabolism:  Stickland PrdB #21 / GrdA #22 (SELENOPROTEINS)         │   │
 │               sialic acid nan #23 · succinate→butyrate · ethanolamine│   │
 │  ecology-in:  Enterococcus cross-feed #72 (Leu, Orn) ──► fitness ↑   │   │
 │  surface:     SlpA/Cwp84/SrtB #24 · FliC/FliD #25 · biofilm          │   │
 └───────────────────────────────┬──────────────────────────────────────┘   │
                                 ▼ density + stress/stationary phase         │
 C3 TOXIN REGULATORY AXIS                        C8 SPORULATION AXIS         │
 ┌──────────────────────────────────────────┐   ┌────────────────────────┐  │
 │  nutrient sufficiency ──► CodY #16 ──┐   │   │  Spo0A #12 ──► SigF/E/ │  │
 │  glucose/carbon ──────► CcpA #17 ──┤ REPRESS│  G/K #13 ──► CotE/BclA │  │
 │  SigD(FliA) #18 ──────────────────┐ │      │   │  #14 ──► NEW SPORES ──┼──┘
 │  Agr QS #19 ──────────────────────┤ ACTIVATE   │  (recurrence seed)     │
 │  RstA ─────────────────────────┐  │ │      │   └────────────────────────┘
 │                                ▼  ▼ ▼      │
 │                          ┌──[ TcdR #15 ]──┐│   ◄── THE SINGLE BOTTLENECK
 │                          ▼               ▼ │        of the toxin axis
 │                       tcdA           tcdB  │
 │                          └──► TcdE #20 ────┼──► toxin released to lumen
 └────────────────────────────────────────────┘
                                 ▼
 C4 TOXIN INTOXICATION AXIS (Module A)
 ┌──────────────────────────────────────────────────────────────────────┐
 │  free TcdB                                                            │
 │    │  CROPS #27 ◄══ BEZLOTOXUMAB (approved)                          │
 │    ▼                                                                  │
 │  RECEPTORS: CSPG4 #35 (stromal) · FZD1/2/7 #36 (crypt stem cells)    │
 │             PVRL3 #37 · TFPI #38 (variant TcdB) · GAG/LDLR            │
 │    │                                          │                       │
 │    ├──► GTD-INDEPENDENT NECROSIS ──► NOX1 #43 ──► ROS  (high dose)   │
 │    │    ** receptor-binding alone is sufficient **                    │
 │    ▼                                                                  │
 │  clathrin endocytosis ──► v-ATPase #41 acidification                  │
 │    ▼                                                                  │
 │  delivery/pore domain #30 inserts  ◄══ niclosamide (claimed)          │
 │    ▼  Hsp90/FKBP/cyclophilin #40 assist  ◄══ celastrol, gedunin       │
 │  cytosolic InsP6 #29 ──► CPD #26 autoproteolysis ◄══ EBSELEN          │
 │    ▼                                                                  │
 │  free GTD #28 + UDP-glucose + Mn²⁺                                    │
 │    ▼                                                                  │
 │  RhoA-Thr37 / Rac1-Thr35 / Cdc42-Thr35 GLUCOSYLATED  #42 UNDRUGGABLE  │
 └───────────────────┬──────────────────────────┬───────────────────────┘
                     ▼                          ▼
 C5 HOST INFLAMMATORY AXIS          C6 BARRIER / REPAIR AXIS
 ┌─────────────────────────────┐   ┌──────────────────────────────────────┐
 │ Rho off + K⁺ efflux         │   │ Rho off ──► ZO-1/occludin/claudin    │
 │   ▼                         │   │            #56 disassembly           │
 │ NLRP3/casp-1 #44 ──► IL-1β  │   │   MLCK #57 ──► junction contraction  │
 │   #45 ──► IL-18, pyroptosis │   │   ▼                                  │
 │ NF-κB + p38/ERK/JNK         │   │ PARACELLULAR LEAK = THE DIARRHEA     │
 │   ▼                         │   │                                      │
 │ IL-8/CXCL1/2 ──► CXCR2 #48  │   │ TcdB·FZD occupancy ──► Wnt/β-catenin │
 │   ▼ **MODULATE, NOT BLOCK** │   │   #59 BLOCKED ──► crypt stem cells   │
 │ NEUTROPHILS → pseudomembrane│   │   cannot renew ──► REPAIR FAILURE    │
 │                             │   │   (independent injury axis)          │
 │ TLR4·SlpA · TLR5·FliC #50   │   │ EGFR #58 AGONIZE · GLP-2R #60        │
 │ IL-23 #46 PATHOGENIC ──┐    │   │ HIF-1α #55 STABILIZE                 │
 │ IL-22 #47 PROTECTIVE ◄─┘    │   └──────────────────────────────────────┘
 │ NK1R #51 · AhR #52 · PPARγ  │
 │ #53 · VDR #54               │        ── C6 failure is why the mucosa
 │ anti-TcdB IgG #63 AUGMENT   │           stays broken after toxin clears
 └─────────────────────────────┘
═══════════════════════════════════════════════════════════════════════════════
```

### Axis definitions and the highest-value node in each

| Axis | Name | Phase/Module | Highest-value node | Why |
|---|---|---|---|---|
| **C1** | Germination | 1 (+0, C) | **CspC #7 / taurocholate site #11** | Obligatory, committed, chemically triggered, validated competitive inhibitor (CDCA), targets the *recurrence reservoir* directly. Tier 1. |
| **C2** | Vegetative fitness | 2 | **RNAP switch region #1** | Only node with bactericidal clinical validation *and* microbiome sparing. Metabolic sub-nodes carry the induction hazard in §4. |
| **C3** | Toxin regulation | 3 | **TcdR #15** | True single bottleneck — six regulatory inputs converge on it, both toxins depend on it. Hardest to drug, highest elegance. |
| **C4** | Intoxication | A | **Receptor engagement (#27/#35/#36)** | Only intervention point *upstream of the branch* between glucosylation-dependent and glucosylation-independent injury. See §5. |
| **C5** | Host inflammation | B (4–6) | **NLRP3/IL-1β #44/#45** | Best-druggable node with unambiguous direction. Most of C5 is bidirectional. |
| **C6** | Barrier / repair | 4 | **Wnt/β-catenin #59** | The axis nothing addresses; failure here is why healing lags toxin clearance. |
| **C7** | Ecological restoration | 0, C | **`bai` guild #64 / DCA-LCA #66** | The only axis whose repair *exits the recurrence loop*. No small molecule exists. |
| **C8** | Sporulation | 1/3 | **Spo0A #12** | Controls transmission and re-seeding; the loop's write-head. |

### Network-topology observations

**Hub nodes** (connect ≥3 axes):
- **TcdR #15** — C3 hub, gates all of C4→C5→C6. Blocking it collapses four axes at once. This is the single most connected druggable-in-principle node in CDI.
- **Rho GTPases #42** — C4/C5/C6 convergence point, and explicitly **undruggable for reactivation**. Everything therapeutic must act *upstream* of it. This is the most important structural constraint in the whole network.
- **Secondary bile acids (DCA/LCA) #66** — simultaneously C7 (product of ecology), C1 (germination inhibitor), and C2 (growth inhibitor). One chemical class, three axes. This is why bile acid chemistry is disproportionately valuable in CDI.
- **Spo0A #12** — C8 and C3 (toxin crosstalk, strain-dependent).

**Bottleneck nodes** (many signals converge, single output): TcdR #15 (six inputs), CspC #7 (germinant + co-germinant integration), v-ATPase #41 (all endocytic toxin entry).

**Feedback-loop entry points** — the recurrence loop `Phase 6 → antibiotic/dysbiosis → Phase 0` is entered at exactly three places:
1. **#70 luminal antibiotic inactivation** — prevents loop entry (primary prevention)
2. **#64/#69 ecological restoration** — exits the loop after entry
3. **C1 germination block + C8 sporulation block** — holds the loop open without exiting it (suppression, not cure)

Fidaxomicin's advantage is that it *minimises loop re-entry* while treating C2. Vancomycin's failure is that it treats C2 by *maximising loop re-entry*. **That single sentence is the whole recurrence problem.**

---

## 2. QUESTION 1 — UDCA: what is the active species, and can it reach concentration?

### 2.1 The structural argument: UDCA itself is the anti-germinant

This resolves cleanly on stereochemistry, and the answer is **UDCA is itself an anti-germinant — it is not a prodrug for LCA.**

The germinant/inhibitor split at CspC tracks the **C7 and C12 hydroxyl pattern**, not conjugation state:

| Bile acid | C3 | C7 | C12 | CspC behaviour | Confidence |
|---|---|---|---|---|---|
| Cholate / taurocholate / glycocholate | 3α-OH | **7α-OH** | **12α-OH** | **GERMINANT** (primary trigger) | [ESTABLISHED] |
| Deoxycholate (DCA) | 3α-OH | — | **12α-OH** | Germinant *and* growth inhibitor | [ESTABLISHED] |
| **Chenodeoxycholate (CDCA)** | 3α-OH | **7α-OH** | *none* | **COMPETITIVE INHIBITOR** | [ESTABLISHED] |
| **Ursodeoxycholate (UDCA)** | 3α-OH | **7β-OH** | *none* | **INHIBITOR** | [CURRENT CONSENSUS] |
| Lithocholate (LCA) | 3α-OH | — | *none* | Inhibitor (germination + growth) | [CURRENT CONSENSUS] |

**The pattern:** loss of the **12α-hydroxyl** converts a germinant into an inhibitor. UDCA is the 7β-epimer of CDCA — the validated competitive inhibitor — and shares its defining feature (no 12α-OH). Conjugation is **not** the determinant: taurochenodeoxycholate inhibits germination just as CDCA does, so the taurine head group is not what makes taurocholate a germinant. UDCA's activity therefore does not require conversion to anything.

This is corroborated functionally: UDCA has been reported to inhibit both *C. difficile* spore germination **and** vegetative growth in vitro, and the human signal comes from recurrent CDI in ileal pouch patients maintained on UDCA — a setting where UDCA, not LCA, is the species present at high luminal concentration. **The dual activity is itself evidence against the prodrug hypothesis**, because germination inhibition and growth inhibition are different assays and UDCA scores in both.

### 2.2 The metabolic argument: dysbiosis protects the parent drug

Round 1 framed 7α-dehydroxylation as UDCA's liability. **On the pathway map it is the opposite — it is a self-correcting feature**, and this is my central finding on UDCA.

Converting UDCA to LCA in the colon requires the **`bai` guild** — either by direct 7-dehydroxylation, or via bacterial 7β-HSDH/7α-HSDH epimerisation to CDCA followed by `bai`-mediated 7α-dehydroxylation. Both routes are executed by the *same small guild of Clostridia* (*C. scindens*, *C. hiranonis*, *C. hylemonae*) that §2.2 identifies as **the guild whose depletion causes CDI in the first place**.

```
HEALTHY COLON (bai guild intact)          CDI COLON (bai guild depleted)
────────────────────────────────          ──────────────────────────────
UDCA                                       UDCA
  │ 7β-HSDH/7α-HSDH epimerisation            │
  ▼ (or direct 7-dehydroxylation)            │  ✗ guild absent
CDCA ──► [bai operon] ──► LCA                │
  │                        │                 ▼
  ▼                        ▼            UDCA ACCUMULATES AS PARENT
inhibitor              inhibitor        (plus glyco-/tauro- conjugates,
                       + hepatotoxic     since BSH #65 is also depleted)
                       at high exposure

⇒ In healthy people UDCA is consumed.  ⇒ In CDI patients it persists.
   Both products are still inhibitors      The patients who need it are
   — the axis is robust either way.        the patients who retain it.
```

Three consequences, all favourable:

1. **The active species question is moot for efficacy.** UDCA, CDCA (its epimer), and LCA (its dehydroxylation product) are *all* C1 inhibitors. There is no metabolic route from UDCA to a germinant. The axis is robust to the conversion question — which is unusual and valuable.
2. **Target-population enrichment.** UDCA's colonic exposure as parent drug is *highest* in exactly the dysbiotic patients who need it, and lowest in healthy people who don't. The drug's PK co-varies with the disease state in the right direction. Few repurposing candidates have this property.
3. **The LCA toxicity ceiling is relaxed** in the same population, because the conversion that generates LCA is impaired. LCA exposure (hepatotoxicity, colonic injury at sustained high exposure) is the classic constraint on high-dose UDCA; it is *least* constraining in the dysbiotic patient. Note the corollary risk in §2.4.

### 2.3 Achievable colonic concentrations — the real bottleneck

This, not the active-species question, is where UDCA is actually at risk. My estimate, with the arithmetic shown so the Literature Reviewer and ADMET agent can attack it:

**Delivery estimate**

| Step | Value | Basis |
|---|---|---|
| Standard dose (PBC/PSC) | 13–15 mg/kg/day ≈ 900–1,200 mg/day | Approved labelling |
| High dose (chemoprevention/PSC trials) | up to 28–30 mg/kg/day ≈ 2,000–2,500 mg/day | Human-dosed precedent exists |
| Small-intestinal passive absorption | ~30–60% | UDCA is unconjugated, MW 392.6, alogp 4.48 (**project data:** `chembl_approved_drugs.csv`, CHEMBL1551 URSODIOL) |
| Reaching colon (unabsorbed + biliary recycled conjugates) | ~300–600 mg/day at standard dose | 40–70% of dose escapes or recycles |
| Colonic luminal water | ~100–200 mL | Standard estimate; **higher and faster-transiting in active CDI diarrhoea** |
| **Nominal colonic concentration** | **≈ 4–15 mM at standard dose** | 300–600 mg ÷ 392.6 g/mol ÷ 0.15 L |

**Requirement estimate**

Reported in-vitro anti-germination and growth-inhibitory activity for UDCA sits in the **high-µM to low-mM** range — appreciably weaker than the millimolar-scale detergency of DCA/LCA and roughly comparable to or weaker than CDCA in competitive germination assays. Call the requirement **0.5–5 mM free UDCA**.

**Verdict: the nominal margin is adequate; the free-fraction margin is not established.** Three deductions from the nominal figure:

- **CMC ceiling.** Above its critical micelle concentration, monomeric UDCA plateaus. Unconjugated UDCA is a poorly soluble, weakly detergent bile acid with a comparatively high CMC; the competitive inhibitor at CspC is presumably the *monomer*. Nominal mM does not guarantee monomeric mM.
- **Solids partitioning.** Bile acids adsorb to fecal solids, mucin, and dietary residue. This is the same criticism the Chemist levelled at berberine and it applies here — less severely, since UDCA is anionic and fecal matrix binding is largely cationic-selective, but it applies.
- **Transit.** Active CDI means profuse diarrhoea. Contact time in the distal colon — where §6.1 places the disease — is sharply reduced during the acute episode.

**Consequence for positioning: UDCA is a maintenance/prevention agent, not an acute-episode agent.** During acute CDI, transit is too fast and luminal volume too high. During the 8–12 week post-antibiotic recurrence window — when transit has normalised, the guild is still absent, and the spore reservoir is intact — the pharmacology lines up. This is precisely the window in which recurrence happens, and it is where the ileal-pouch human signal was generated.

### 2.4 Two pathway risks Round 1 did not surface

**(a) The FXR feedback risk — the inhibitor may raise its own competitor.**

C1 inhibition is **competitive**, so efficacy depends on the **UDCA : taurocholate ratio at CspC**, not on the UDCA concentration alone. UDCA is at best a weak FXR (#61) ligand and, unlike CDCA — the most potent endogenous FXR agonist — provides little FXR agonist tone. If sustained UDCA therapy dilutes CDCA's share of the pool and thereby relieves FXR-mediated feedback repression of hepatic bile acid synthesis, the primary bile acid pool (and hence colonic **taurocholate**, the germinant) could expand.

Direction is **[UNCERTAIN]** — UDCA therapy is not known to markedly de-repress CYP7A1, and §5.3 explicitly flags #61 FXR as "direction UNCERTAIN." But the network structure makes this the *right* question, because it targets the ratio rather than the numerator.

> **Decisive experiment (to Literature Reviewer / ADMET):** measure the **colonic or fecal UDCA : taurocholate molar ratio** on UDCA therapy in antibiotic-dysbiotic subjects. That single ratio, not the absolute UDCA concentration, predicts C1 efficacy. If the ratio does not move favourably, UDCA fails regardless of dose.

**(b) The sub-inhibitory biofilm risk.**

Sub-inhibitory bile acid exposure has been reported to **induce *C. difficile* biofilm formation** (best characterised for DCA) [EMERGING]. §2.4 names biofilm as a probable persistence and recurrence reservoir. A UDCA concentration that lands *below* its growth-inhibitory threshold — precisely the marginal-exposure scenario in §2.3 — could convert a suppressive intervention into a persistence-promoting one. This is the bile acid analogue of §2.5's sub-inhibitory-antibiotic toxin-induction warning, and it should be tested at the *low* end of the concentration range, not just the high end.

### 2.5 Formulation implication: TUDCA is the more rational colonic-delivery vehicle

**Project data finding:** `chembl_approved_drugs.csv` contains **TAURURSODIOL (CHEMBL272427, tauroursodeoxycholic acid), first approval 2022** — MW 499.7, **PSA 123.9, alogp 3.40**, versus UDCA (CHEMBL1551) at **PSA 77.8, alogp 4.48**.

The taurine conjugate is substantially more polar and less lipophilic, which **reduces passive small-intestinal absorption and increases the fraction delivered to the colon** — the exact ADMET inversion §6.2 asks for. And per §2.1, conjugation does not convert an inhibitor into a germinant: taurochenodeoxycholate inhibits. Two further points:

- In CDI, **BSH #65 is depleted**, so TUDCA would arrive *and remain* conjugated — a second dysbiosis-protects-the-drug effect stacking on the `bai` effect.
- TUDCA is a **TGR5 (#62, GPBAR1) agonist** where UDCA is not, adding anti-inflammatory/barrier tone on **C5/C6** — axes UDCA does not touch. This converts UDCA from a 2-axis to a 3–4-axis agent.

**Recommendation to SAR Analyst and Drug Repurposing Strategist: evaluate tauroursodiol (approved 2022) alongside UDCA as the preferred colonic-delivery form.** It is a distinct approved product with better colonic delivery physics and broader axis coverage, and it has not been considered by any Round 1 agent. Caveats: anti-germination potency of the conjugate versus parent needs direct measurement, and the 2022 approval was as a fixed-dose combination — the regulatory path for the single agent needs checking.

### 2.6 UDCA answer summary

| Question | Answer | Confidence |
|---|---|---|
| Is UDCA itself active, or only LCA? | **UDCA itself is active.** Determined by the absent 12α-OH, which it shares with CDCA. Not a prodrug. | **High** — structural logic plus dual-assay in vitro activity |
| Does dysbiosis destroy it? | **No — dysbiosis preserves it.** Both conversion routes require the depleted `bai` guild. All downstream products are also inhibitors. | **High** |
| Achievable colonic concentration? | Nominal **4–15 mM** at standard dose; requirement **0.5–5 mM**. Nominal margin adequate; **free monomeric margin unproven** (CMC, solids binding, diarrhoeal transit). | **Moderate** |
| What actually decides it? | The **UDCA : taurocholate ratio**, not absolute concentration. Competitive inhibition. | **High** (logic), **Low** (value unmeasured) |
| Best positioning | **Post-antibiotic maintenance across the 8–12 week recurrence window**, not acute therapy. | **Moderate–High** |
| Better molecule? | **Tauroursodiol (TUDCA)** — better colonic delivery, resists BSH-depleted deconjugation, adds TGR5. | **Moderate** (novel, untested) |

---

## 3. QUESTION 2 — Berberine: genuine polypharmacology, or noise?

### 3.1 Data availability — stated plainly

**Berberine has ZERO direct target-interaction rows in project data.** I queried `pubchem_phytochem_target_interactions.csv` (60,521 rows, 15,587 unique genes): 20 rows mention "berberine," and **all 20 are CTD co-treatment annotations for other compounds** (niacinamide, rutin, chlorogenic acid, Huang-lien-chieh-tu-tang). There is not one `pubchem_name = berberine → gene` row. Berberine is also absent from IMPPAT per the data inventory.

**Everything below is knowledge-based, not data-backed.** That matters for how much weight the score should carry.

### 3.2 The four claimed actions, mapped

```
BERBERINE (quaternary protoberberine alkaloid, MW ~336, permanent cation, oral F <1%)
   │
   ├─► C5 ── NF-κB suppression ──────┐
   │                                 ├─► ONE AXIS, SERIALLY COUPLED
   ├─► C5 ── NLRP3 inhibition ───────┘   (see §3.3 — not two)
   │
   ├─► C6 ── tight junction ZO-1/occludin upregulation ──► BARRIER (+)
   │    └─► C6 ── Wnt/β-catenin SUPPRESSION ──► REPAIR (−)  ◄── CONFLICT
   │
   ├─► C7 ── microbiome modulation (shifts toward butyrate producers,
   │          suppresses Enterobacteriaceae/Enterococcus)
   │
   └─► C2 ── weak direct anti-C. difficile (MIC ~64–256 µg/mL)
        └─► C2 ── anti-enterococcal ──► cuts #72 cross-feed  ◄── NON-OBVIOUS ASSET
```

### 3.3 Finding 1 — the polypharmacology is narrower than claimed (3 axes, not 4)

**NF-κB suppression and NLRP3 inhibition are not independent coverage.** They are serially coupled on a single axis: NF-κB drives transcription of *NLRP3 itself and of pro-IL-1β*; the NLRP3/caspase-1 inflammasome then *processes* pro-IL-1β to mature IL-1β. Hitting both is **reinforcement of one axis**, not coverage of two.

That is not worthless — serial inhibition of a single amplification cascade gives steeper, more robust suppression than either step alone, and it is the classic natural-product advantage. But **it must not be counted twice in a coverage matrix**, which is precisely what a naive "berberine hits four things" reading does. Berberine's genuine coverage is **C5 (one axis, doubly hit) + C6 (net direction contested) + C7 (modulate) + C2 (weak)**.

### 3.4 Finding 2 — the Wnt conflict is a direction error, and it is the most serious thing in this report about berberine

**Berberine's anticancer pharmacology is substantially built on suppression of Wnt/β-catenin signalling and on AMPK activation / mTOR inhibition — i.e. it is an anti-proliferative agent in colonic epithelium.**

Now read that against **C6**:

- TcdB occupies **FZD1/2/7 (#36)** and thereby **already blocks Wnt/β-catenin (#59)**, so crypt stem cells cannot renew. §2.9 calls repair failure "an independent injury axis"; §5.3 gives #59 the direction **RESTORE**.
- Berberine, delivered at high luminal concentration (oral F <1% means ~99% stays in the lumen, reaching mg/g fecal levels) directly onto a colonic epithelium whose crypts are already failing to regenerate, would **further suppress the axis that needs restoring**.

**This is a violation of my skill file's primary guardrail — "Direction matters: activating a pathway when it needs inhibiting could worsen disease."** It is the same class of error as blocking NF-κB during the healing phase in OM, and it is the reason I score berberine *below* its Round 1 mean.

Supporting note from project data: the phytochem file contains 55 `CTNNB1` (β-catenin) interaction rows and 76 tight-junction rows (`TJP1`/`OCLN`/`CLDN1`), confirming that flavonoid/alkaloid-class natural products routinely modulate *both* — so the barrier-positive and repair-negative actions genuinely co-occur in this chemical class rather than being a berberine-specific quirk. The net direction in an actively-injured colon is **not** predictable from the barrier data alone.

> **To SAR Analyst:** the berberine question is no longer "can we improve selectivity for potency." It is **"can the tight-junction/anti-inflammatory activity be separated from the anti-proliferative Wnt/AMPK activity?"** If not, berberine is contraindicated by mechanism in Phase 4 disease, not merely underpowered. **Decisive experiment: berberine's effect on colonic organoid or crypt regeneration in the presence of TcdB.** If it worsens regeneration, berberine is out regardless of its inflammatory profile.

### 3.5 Finding 3 — the enterococcal cross-feed hit is berberine's best and least-appreciated asset

§2.8 flags *Enterococcus*–*C. difficile* cross-feeding to the Pathway Analyst specifically: enterococcal release of **leucine and ornithine** supports *C. difficile* Stickland metabolism and **elevates toxin production** (#72, direction **SUPPRESS**).

Berberine has meaningful activity against Gram-positive organisms including enterococci. On the network this means berberine's "non-selective, too-weak-to-matter" antibacterial breadth — the property the Chemist scored down — is **pointed at a validated indirect anti-*C. difficile* node**. It does not need to reach *C. difficile*'s MIC to matter; it needs to reach *Enterococcus*'s.

This reframes berberine's C2 contribution from "weak antibiotic" to "**cross-feed disruptor**," which is a differentiated and non-obvious mechanism no other candidate in the set provides. It also partly answers the Chemist's fecal-binding objection: the required potency bar is lower than assumed, because the target organism is more susceptible than *C. difficile*.

### 3.6 Finding 4 — moderate potency is the correct shape for C5

§2.7 is explicit that C5 is **bidirectional**: neutrophil depletion *worsens* outcomes in mice, so CXCR2 #48 carries the direction "**MODULATE** (not fully block)," and a blanket antagonist "is as likely to harm as help."

A moderate-potency, multi-node, incompletely-penetrant polypharmacological agent is arguably a **better structural fit** for a bidirectional axis than a potent selective inhibitor, because it dampens rather than ablates. This is a genuine argument for a berberine-class agent over an MCC950-class NLRP3 inhibitor in CDI specifically — and it inverts the usual "natural products are just weak drugs" objection.

### 3.7 Berberine verdict

**Genuinely synergistic on C5 + C7 + C2(#72); genuinely conflicted on C6; and narrower than the four-mechanism story implies.** Not noise — but not the clean multi-target win Round 1's Ethnobotany/ADMET pair (8.0/8.0) described. The Wnt liability is disqualifying if real, and it is testable.

| Claim | Verdict |
|---|---|
| NLRP3 + NF-κB = two-axis coverage | **No** — one axis, serially reinforced. Real benefit, must not be double-counted. |
| Tight junction upregulation | **Real but net-uncertain** — co-occurs with Wnt suppression in this chemical class. |
| Microbiome modulation | **Plausible, direction favourable** (C7). Weakest evidence of the four. |
| Anti-*C. difficile* | **Weak directly; meaningful indirectly** via #72 enterococcal cross-feed. Best-value reframe. |
| Overall polypharmacology | **Coherent on 3 of 4 axes, adversely directed on the 4th.** |

---

## 4. QUESTION 3 — Ebselen: dual mechanism, and does the colon neutralise the warhead?

### 4.1 Are the two targets synergistic in principle? Partly — and they may be internally antagonistic

Ebselen's two claimed nodes sit on **different axes**, which is the precondition for synergy:

- **#26 TcdB CPD** (C4, Module A) — covalent modification of the catalytic cysteine, blocking autoproteolytic GTD release. In vivo mouse efficacy, anti-virulence without affecting bacterial burden [EMERGING].
- **#21/#22 PrdB/GrdA** (C2, Phase 2) — Stickland selenoproteins; the selenocysteine selenol is a plausible target for a selenium electrophile.

Non-redundant on the causal graph: one reduces *damage per organism*, the other reduces *organism fitness*. That is textbook complementarity.

**But there is a hazard inside ebselen's own polypharmacology, and it is the most interesting thing I found in this report.**

### 4.2 The nutrient-limitation / toxin-induction hazard — a cross-cutting warning

Read §2.5's regulatory architecture literally:

```
        CodY #16 senses  GTP + branched-chain amino acids  (= nutrient SUFFICIENCY)
        CcpA #17 senses  glucose / rapid carbon
                              │
                     both REPRESS tcdR when nutrients are plentiful
                              │
        ⇒ NUTRIENT LIMITATION RELIEVES REPRESSION ⇒ tcdR DE-REPRESSED ⇒ MORE TOXIN

  and §2.5 states it directly: "Toxin production is not constitutive — it is tightly
  regulated and INDUCED BY STRESS AND NUTRIENT LIMITATION, typically in stationary phase."
```

**Any agent whose mechanism is to starve *C. difficile* is, by the model's own regulatory architecture, an agent that de-represses `tcdR`.** Ebselen's PrdB/GrdA inhibition blocks Stickland fermentation — the organism's principal energy-yielding route — which is nutrient limitation imposed pharmacologically. Ebselen's CPD arm would then be fighting a **larger toxin pool that its own C2 arm created**.

This is not a berberine-or-ebselen-specific problem. It is a **class-level hazard spanning the entire "starve the pathogen" target set**:

| Target | Mechanism | Induction hazard |
|---|---|---|
| #21/#22 PrdB/GrdA (Stickland) | Blocks primary energy metabolism | **High** |
| #23 sialic acid catabolism | Removes a key nutrient | **High** |
| Module C "DEPLETE luminal proline/glycine" | Removes Stickland acceptors | **High** |
| Module C "DEPLETE taurocholate" | No effect on nutrient sensing | None — C1, not C2 |
| #1 RNAP (fidaxomicin) | **Bactericidal**; also suppresses toxin at sub-MIC | **None — inverted** |
| #3 PolC (ibezapolstat) | Bactericidal | Low |

**Contrary evidence, stated honestly.** The enterococcal cross-feeding data (§2.8) run *against* this logic: removing enterococci removes leucine (a BCAA, a CodY ligand) and ornithine, which by CodY logic should *de-repress* toxin — yet the observed effect of enterococcal removal is **reduced** toxin. So in vivo the simple CodY rule does not predict outcomes; biomass, stationary-phase timing, and growth-rate effects evidently dominate. I therefore state this as a **flagged, mechanistically-grounded hazard requiring measurement — not an established result.**

> **Decisive experiment (to Literature Reviewer and Combination Designer):** for any nutrient-limiting candidate, measure **toxin per CFU**, not toxin per mL or bacterial burden alone. A candidate that lowers CFU while raising toxin/CFU is a net harm in a disease whose morbidity is entirely toxin-mediated. §2.5 already flags this as "a real failure mode, not a theoretical one" for sub-MIC antibiotics; I am extending the same test to the whole metabolic-inhibitor class.

This also explains a piece of fidaxomicin's dominance that Round 1 treated as two separate virtues: fidaxomicin is **bactericidal *and* toxin-suppressing at sub-MIC**, so it is the one C2 agent with *no* induction hazard at any exposure level. That is a third mechanism of its superiority, alongside microbiome sparing and sporulation inhibition.

### 4.3 The reducing-colon question: the warhead is not destroyed — it is diluted and de-catalysed

This is the ADMET (4.0) versus Target-Profiler (8.5) conflict. **My reading favours ADMET, but for a different and more precise reason than "the Se warhead is destroyed."**

Ebselen's chemistry: the Se–N bond opens on attack by a thiol, forming a **selenenyl sulfide adduct** (Se–S). Against a protein target this is the productive event — covalent modification of the CPD catalytic cysteine. Against bulk thiol it is a sink.

**The colonic lumen is the most thiol-rich, most reducing, most anaerobic compartment in the body:**

| Species | Approx. colonic concentration | Effect on ebselen |
|---|---|---|
| Glutathione / cysteine | high µM–mM | Rapid selenenyl-sulfide formation; ebselen–SG is the dominant species within seconds–minutes |
| **Hydrogen sulfide (H₂S)** | **~0.2–3.4 mM in human feces** | Reacts to give selenide/persulfide species; **largely a terminal sink** — insoluble/volatile selenium end-products |
| **Peroxides / O₂** | **essentially absent (strictly anaerobic)** | **No oxidant to regenerate the active selenazole** |

Two distinct problems, and the second is the decisive one:

**(a) Mass-action dilution.** Millimolar bulk thiol against a nanomolar-or-lower target protein. Mass action puts essentially all ebselen into adduct form. The counter-argument is real — selenenyl sulfides are *exchangeable*, so ebselen–SG can still transfer selenium to a more nucleophilic acceptor, and the CPD catalytic cysteine is exactly that (activated, low pKa, in a protease active site), giving genuine kinetic selectivity. So this problem alone would be surmountable by dose.

**(b) Loss of catalytic turnover — the decisive point.** Ebselen's well-known glutathione-peroxidase-mimetic cycle **requires a peroxide to reoxidise the selenol back to the active selenazole**. In a strictly anaerobic, peroxide-free colonic lumen, **that cycle cannot close.** Ebselen in the colon is therefore **strictly stoichiometric — single-turnover.** One molecule modifies at most one thiol, and the overwhelming majority are consumed by bulk GSH/cysteine/H₂S before encountering CPD or PrdB.

**Combined with (a), the required dose scales with the bulk thiol pool, not with the target concentration** — and the bulk thiol pool is millimolar in a ~150 mL compartment, i.e. sub-millimole to millimole *per day* of pure sacrificial consumption.

**(c) Delivery makes it worse.** Ebselen is small (MW ~274) and lipophilic — it is **orally absorbed** and its known disposition is to bind plasma albumin Cys34. That is the wrong direction entirely for §6.2's inverted ADMET logic: systemic ebselen dosing delivers the drug to albumin, not to the colonic lumen. Its documented human exposure (SPI-1005-class dosing, hundreds of mg BID) was designed for *systemic* delivery. **Reaching the colon requires a colon-targeted formulation** — and §6.1 warns that microbiota-triggered release systems fail in CDI dysbiosis, so a pH- or time-dependent coating is required, with PPI co-administration (common in this population) defeating pH-dependent coatings.

### 4.4 One more pathway argument: ebselen's C4 coverage is mechanistically incomplete

Independent of chemistry, **CPD inhibition covers less of C4 than receptor blockade does.**

§2.6 A.3 is explicit: at high toxin dose there is a **glucosyltransferase-independent necrosis pathway** requiring **only receptor binding**, proceeding via NOX1-derived ROS. §5.2 spells out the consequence: "a GTD-active-site inhibitor would **not** block high-dose necrosis. Receptor-blocking or neutralizing approaches are more complete."

The same logic applies to CPD inhibition — CPD acts *after* receptor binding and translocation, so blocking it leaves the receptor-binding-dependent necrosis arm fully intact.

```
 TcdB ──► RECEPTOR BINDING ──┬──► endocytosis ──► CPD ──► GTD ──► Rho off
                             │                     ▲
   ◄── BEZLOTOXUMAB blocks   │                     └── EBSELEN blocks here
       HERE (covers both)     │
                             └──► NOX1 ROS necrosis  ◄── EBSELEN MISSES THIS
                                  (receptor binding alone is sufficient)
```

**This is a structural argument that bezlotoxumab's single node is worth more than ebselen's two**, and it is why I score bezlotoxumab above ebselen on the pathway lens despite ebselen's dual mechanism. Intervening upstream of a branch point beats intervening downstream of it on one arm — a general network principle, and it applies cleanly here.

### 4.5 Ebselen verdict

| Question | Answer |
|---|---|
| Do #26 and #21/#22 create genuine synergy? | **Structurally yes** (different axes, complementary), **but plausibly self-antagonising** — the Stickland arm may de-repress `tcdR` and enlarge the toxin pool the CPD arm must neutralise. Must be measured as toxin/CFU. |
| Does the reducing colon neutralise the warhead? | **It does not destroy it — it dilutes it and removes its catalytic turnover.** Millimolar bulk thiol + H₂S sink + **no oxidant to close the GPx-mimetic cycle** ⇒ strictly stoichiometric, sacrificially consumed. |
| Is dose a way out? | Only in principle. Required dose scales with the millimolar thiol pool; and ebselen is *absorbed*, so a colon-targeted formulation is mandatory — with the §6.1 dysbiosis and PPI caveats on release triggers. |
| Is CPD the right toxin node anyway? | **No — it is downstream of the injury branch point.** It misses the receptor-binding-dependent NOX1 necrosis arm that receptor blockade covers. |
| Net | **Target Profiler's 8.5 credits target quality; ADMET's 4.0 credits delivery reality. ADMET is closer.** My score: 5.0. |

---

## 5. PATHWAY COVERAGE MATRIX

██ strong · ▓▓ partial/weak · ░░ none · **▼▼ adverse direction (worsens the axis)**

```
┌──────────────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬─────────┐
│ Candidate        │  C1  │  C2  │  C3  │  C4  │  C5  │  C6  │  C7  │  C8  │ Axes    │
│                  │ germ │ fitns│ tox  │ intox│ host │barrer│ ecol │ spore│ covered │
│                  │      │      │ reg  │      │ infl │ repar│ restr│      │         │
├──────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼─────────┤
│ Fidaxomicin      │  ░░  │  ██  │  ██  │  ░░  │  ░░  │  ░░  │  ▓▓  │  ██  │ 3.5 ✔   │
│ Vancomycin       │  ░░  │  ██  │  ░░  │  ░░  │  ░░  │  ░░  │  ▼▼  │  ░░  │ 1 −1 ✘  │
│ Bezlotoxumab     │  ░░  │  ░░  │  ░░  │  ██  │  ▓▓  │  ▓▓  │  ░░  │  ░░  │ 1.5 ✔   │
│ UDCA             │  ██  │  ▓▓  │  ░░  │  ░░  │  ░░  │  ░░  │  ▓▓  │  ░░  │ 2 ✔     │
│  └ TUDCA variant │  ██  │  ▓▓  │  ░░  │  ░░  │  ▓▓  │  ▓▓  │  ▓▓  │  ░░  │ 3.5 ✔✔  │
│ Berberine        │  ░░  │  ▓▓  │  ░░  │  ░░  │  ██  │  ▼▼? │  ▓▓  │  ░░  │ 2.5 ⚠   │
│ Ibezapolstat     │  ░░  │  ██  │  ░░  │  ░░  │  ░░  │  ░░  │  ▓▓  │  ▓▓  │ 2 ✔     │
│ Ebselen          │  ░░  │  ▓▓? │  ▼▼? │  ▓▓  │  ░░  │  ░░  │  ░░  │  ░░  │ 1.5 ⚠   │
│ Niclosamide      │  ░░  │  ▓▓  │  ░░  │  ▓▓  │  ░░  │  ░░  │  ░░  │  ░░  │ 1 ⚠     │
│ Aprepitant       │  ░░  │  ░░  │  ░░  │  ░░  │  ▓▓  │  ▓▓  │  ░░  │  ░░  │ 1 ✔     │
│ Conessine        │  ▓▓? │  ▓▓  │  ░░  │  ░░  │  ░░  │  ░░  │  ░░  │  ░░  │ 0.5 ✘   │
├──────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼─────────┤
│ FMT / VOWST /    │  ▓▓  │  ▓▓  │  ░░  │  ░░  │  ▓▓  │  ▓▓  │  ██  │  ░░  │ 3 ✔✔    │
│ VE303 (reference)│      │      │      │      │      │      │      │      │         │
├──────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼─────────┤
│ SET REDUNDANCY   │  1   │  6   │  1   │  2   │  2   │  0   │  1   │  1   │         │
│ (strong hits)    │ UDCA │ over-│ fida │bezlo,│berb, │ NONE │ LBP  │ fida │         │
│                  │ only │served│ only │ (ebs)│(aprp)│      │ only │ only │         │
└──────────────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴─────────┘
```

### Reading the matrix

**Massive redundancy on one axis, near-total absence on the rest.** Six of ten candidates hit C2 (vegetative fitness). This is the "narrow-spectrum antibacterial is a burned value proposition" finding of §2.4 rendered as a network diagram — the candidate set is piled onto the one axis where four Phase 3 programmes (ridinilazole, surotomycin, cadazolid, and vancomycin-comparator trials generally) already failed to differentiate, while **C6 has zero coverage and C1, C3, C7 have exactly one candidate each.**

**Single points of failure.** C1 depends entirely on UDCA. C3 depends entirely on fidaxomicin (and only as a sub-MIC side effect, not by design). C7 depends entirely on live biotherapeutics — no small molecule. If UDCA fails on the concentration question in §2.3, the germination axis — the Disease Brief's **Tier 1, "most conspicuous unexploited target class in CDI"** — is empty.

**Vancomycin is the only candidate with net-negative coverage.** It hits one axis and actively degrades another (C7), which is the mechanism of the recurrence loop. The pathway lens is the harshest possible lens on vancomycin, and it explains the 5.0-point Round 1 spread exactly: ADMET scores the delivery (perfect), the pathway/disease view scores the network effect (net-negative).

### Gap analysis

| Axis | Status | Assessment |
|---|---|---|
| **C6 barrier / repair** | **ZERO coverage** | **The critical gap.** TcdB-FZD-mediated Wnt blockade means the mucosa cannot repair even after toxin clears (§2.9). Nothing in the set addresses it, and berberine may *worsen* it. Widest open white space, and the only axis where no candidate even claims activity. |
| **C7 ecological restoration** | 1 (biologics only) | Round 1's "biggest strategic hole" — confirmed. It is the **only axis whose repair exits the recurrence loop**; everything else suppresses. #70 (ribaxamase/DAV132) is the cheapest unclaimed win and is *absent from the candidate set entirely*. |
| **C3 toxin regulation** | 1 (incidental) | TcdR #15 is the network's most connected druggable-in-principle node and nothing targets it by design. Highest elegance, hardest chemistry. |
| **C1 germination** | 1 (UDCA) | Tier 1 axis on a single candidate. Fragile. |
| **C2 vegetative fitness** | 6 | **Over-served and de-risked to the point of being a liability.** Adding a seventh C2 agent adds no coverage. |
| **C4 intoxication** | 2 | Bezlotoxumab (complete, IV, expensive) + ebselen (incomplete, fragile). **No oral small-molecule toxin inhibitor exists** — §2.6 calls this transformative if solved. |
| **C5 host inflammation** | 2 | Berberine + aprepitant, both weak. Zero approved host-directed agents for CDI. Natural-product niche per §2.7. |
| **C8 sporulation** | 1 (incidental) | Fidaxomicin only, and again as a side effect. |

### Data-backed leads for the two worst gaps

From `pubchem_phytochem_target_interactions.csv` — these are **actual rows in project data**, not recall:

| Gap | Lead | Data-backed evidence | Note |
|---|---|---|---|
| **C7/C1** — bile acid receptor | **Oleanolic acid → GPBAR1 (TGR5, #62) FULL AGONIST** | PMID:17825251; binding PMID:23022524, 23041323 (4 rows) | **Corroborates the Ethnobotany agent's *Cyperus rotundus* → oleanolic acid → TGR5 lead with project data.** ⚠️ **But the same file shows oleanolic acid INHIBITS IL22 (PMID:26513295) — the wrong direction for #47, which is AGONIZE.** Mixed-direction lead; test both. |
| **C7/C1** | **Betulinic acid → GPBAR1 FULL AGONIST** | PMID:19911773 | Second data-backed TGR5 agonist triterpene. Also → CTNNB1 (2 rows) — same Wnt caution as berberine. |
| **C4** — toxin translocation | **Celastrol → HSP90AA1 inhibition** | PMID:17010675, PMID:32470352 | **Data-backed support for the Ethnobotany agent's gedunin/celastrol → Hsp90 (#40) → TcdB translocation-blockade hypothesis.** Also → IL23A inhibition (#46, correct direction). Genuinely novel, 2-node coherent. Celastrol's toxicity is the obvious problem. |
| **C6** — barrier | Quercetin (14 TJP1/OCLN/CLDN1 rows), kaempferol, luteolin, myricetin, genistein | Multiple | The only chemotype with substantial data-backed barrier activity. ⚠️ Quercetin also has 10 `CTNNB1` rows — **the barrier/Wnt co-modulation problem is class-wide in flavonoids**, not berberine-specific. |

---

## 6. QUESTION 4 — COMBINATION RECOMMENDATIONS

Selection criteria: (a) maximise distinct axes; (b) no directional conflicts; (c) no shared failure mode; (d) at least one component must touch **C7**, the only loop-exiting axis; (e) prefer temporally-staged over concurrent where the axes are phase-bound.

### ⭐ Combination 1 — *Fidaxomicin → UDCA/TUDCA maintenance* (highest confidence)

```
 DAY 0 ─────────── DAY 10 ──────────────────────────────── WEEK 12
 │◄── FIDAXOMICIN ──►│◄──── UDCA (or TUDCA) MAINTENANCE ────────►│
 │  C2 kill          │  C1 germination block sustained through
 │  C3 toxin suppr.  │  the entire recurrence window
 │  C8 sporulation   │
 │  C7 spared        │  C7 guild recovers under bile-acid cover
 │                   │
 │ Fidaxomicin's failure mode = spores survive treatment
 │ UDCA's mechanism   = spores cannot germinate
 └─────────────────── EXACT COMPLEMENT ──────────────────────────┘
```

**Axes: C1 + C2 + C3 + C7(partial) + C8 = 4.5.** Highest coverage available from approved agents with no directional conflict.

**Why this pairing is mechanistically special:** fidaxomicin's single acknowledged failure mode is that **spores survive** — §2.10 lists "spores are the recurrence reservoir and are unaffected by current antibiotics" as ESTABLISHED. UDCA's entire mechanism is preventing those surviving spores from germinating. The complementarity is not merely additive; **one agent's failure mode is the other's mechanism of action.** That is the strongest form of combination rationale.

**The temporal logic is equally clean.** §2.3 asks whether anti-germinants can hold against "a continuously replenished spore load" — fidaxomicin answers that by clearing vegetative cells and inhibiting *new* spore formation (C8), so UDCA faces a *static, non-replenishing* reservoir instead of a growing one. And UDCA's transit/dilution weakness (§2.3) is a problem during acute diarrhoea but not during the post-treatment window — so deploying it *after* fidaxomicin dodges its own worst PK liability.

**Risks / must-check:**
- **Physicochemical DDI, unassessed by any Round 1 agent.** Fidaxomicin is large (MW 1058) and very poorly water-soluble; its efficacy depends on high *luminal* concentration and minimal absorption. **Bile salts are solubilising agents.** Co-administered UDCA could micellise fidaxomicin, raising its dissolved fraction and potentially its absorption — lowering luminal exposure. **Mitigation: sequential, not concurrent, dosing** — which the temporal logic already prefers. Flag to ADMET/Chemist as a concrete formulation question.
- Sub-inhibitory bile-acid biofilm induction (§2.4b) if UDCA exposure lands low.
- The UDCA : taurocholate ratio question (§2.4a) governs the whole benefit.

**Confidence: Moderate–High.** Both agents approved; each mechanism independently supported; the interaction is inferred, not demonstrated.

---

### ⭐⭐ Combination 2 — *Fidaxomicin → UDCA/TUDCA + oral live biotherapeutic* (best total coverage)

```
 DAY 0 ────── DAY 10 ─────────────────────────────────── WEEK 12
 │◄ FIDAXOMICIN ►│
                 │◄──────── UDCA / TUDCA ─────────────────────►│
                 │◄──── VOWST (oral spores) or VE303 ─────────►│
                 │        C7 RESTORE — exits the loop
                 │
                 │  THE SELF-TAPERING HANDOFF:
                 │  as the bai guild re-establishes, UDCA is
                 │  progressively converted to LCA — itself a
                 │  germination AND growth inhibitor. The drug
                 │  becomes unnecessary exactly as it becomes
                 │  metabolised. Pharmacology hands off to ecology.
```

**Axes: C1 + C2 + C3 + C5(partial) + C6(partial) + C7(strong) + C8 = 5.5–6.** The only construction in this analysis that puts strong coverage on **C7**, the sole loop-exiting axis.

**The self-tapering handoff is the novel argument here, and it falls directly out of §2.2's biology.** UDCA provides *pharmacological* C1 coverage during the window when the *ecological* C1/C7 defence is absent. As the consortium re-establishes the `bai` guild, that same guild begins converting UDCA → LCA — and LCA is itself a C1 germination inhibitor *and* a C2 growth inhibitor. The bridging drug is consumed precisely as the endogenous mechanism it substitutes for comes back online, and its metabolite is on-mechanism. There is no wean-off cliff. This is the kind of construction that only becomes visible on a network map.

**Risks / must-check:**
- **Testable antagonism (the key risk):** DCA/LCA broadly inhibit Clostridia. Does high luminal UDCA suppress the engrafting consortium? *C. scindens* and relatives are bile-acid–metabolising and presumably bile-tolerant, but VE303's eight strains and VOWST's spore population are not uniformly so. **Decisive experiment: engraftment efficiency of the consortium ± UDCA.** If UDCA blocks engraftment, the combination inverts from synergistic to antagonistic.
- Live biotherapeutics are adjunctive and require prior antibiotic therapy plus careful timing (§2.8) — the staging above respects that.
- §2.8 flags **[UNCERTAIN] commercial viability** of Rebyota/Vowst; VE303 is Phase 3. Route to Clinical Feasibility Assessor.

**Confidence: Moderate.** Each component is individually strong (FMT-class efficacy is among the largest in modern therapeutics); the three-way interaction is unstudied.

---

### ⭐ Combination 3 — *Fidaxomicin + bezlotoxumab + UDCA* (maximum approved-agent coverage, high-risk patients)

**Axes: C1 + C2 + C3 + C4 + C8 = 5.** Adds the **C4 intoxication axis** — the only axis that protects the host while the other agents work on the organism — and does so with the *mechanistically complete* C4 agent (receptor blockade covers both the glucosylation-dependent and NOX1-necrosis arms; see §4.4).

All three are approved, so this is deployable now rather than a development proposal. **Positioning: patients with ≥2 recurrence risk factors** where the toxin burden is the proximate threat.

**Risks:** bezlotoxumab is IV-only, expensive, single-dose, TcdB-only (no CDT coverage), carries a **boxed heart-failure-exacerbation concern in an elderly, CHF-prevalent population** (route to Safety Pharmacologist), and §2.6 flags **[UNCERTAIN] commercial availability**. Leaves C5/C6/C7 uncovered — so it suppresses well but does not exit the loop.

**Confidence: Moderate–High** on the pathway logic; feasibility is the constraint, not the biology.

---

### Combinations to AVOID — and why the network says so

| Combination | Why it fails on the network |
|---|---|
| **Ebselen + bezlotoxumab** | **Redundant on C4** — same axis, and ebselen covers strictly *less* of it (misses the receptor-binding-dependent NOX1 necrosis arm, §4.4). Pays twice for one axis, and the cheaper component is the incomplete one. |
| **Ebselen + niclosamide** | Both target C4 Module A entry/processing (#26 and #30), **and both have redox-fragile pharmacophores in the same anaerobic compartment** — a *shared* failure mode, which is the opposite of what combination design is for. Correlated failure, not diversified risk. |
| **Ebselen + any Stickland/nutrient-depletion agent** | **Compounds the `tcdR` de-repression hazard** (§4.2). Two agents both imposing nutrient limitation on an organism whose toxin genes are de-repressed *by* nutrient limitation. |
| **Vancomycin + any C7 restoration agent** | Direct directional conflict. Vancomycin's mechanism of harm *is* C7 destruction; it would sterilise the consortium it is co-administered with. (This is why live biotherapeutics are given *after*, not with, antibiotics.) |
| **Berberine + anything, in active Phase 4 disease** | Until the **Wnt/anti-proliferative liability (§3.4)** is excluded, berberine risks worsening C6 — the axis that already has zero coverage and cannot afford a negative contributor. |
| **Any second C2 agent added to fidaxomicin** | Zero added axes. Six of ten candidates already crowd C2, where four Phase 3 programmes failed to differentiate. |

### Phase-alignment strategy

| Window | Axes that matter | Agents | Note |
|---|---|---|---|
| **Primary prevention** (on broad-spectrum antibiotic, pre-CDI) | C7 (prevent loop entry) | **#70 ribaxamase / DAV132** | **Not in the candidate set at all.** Clinically validated concept (Phase 2/3 positive), no approved product. The cheapest unclaimed win in CDI. |
| **Acute episode** (days 0–10) | C2, C3, C4 | Fidaxomicin ± bezlotoxumab | UDCA is *wrong here* — diarrhoeal transit defeats it. |
| **Recurrence window** (weeks 2–12) | **C1, C7, C8** | **UDCA/TUDCA + live biotherapeutic** | Where recurrence actually happens and where the candidate set is thinnest. **The highest-value window, and the least-served.** |
| **Post-resolution repair** | **C6** | **Nothing** | Unaddressed. TcdB-FZD Wnt blockade means repair lags clearance. Open white space. |
| **Fulminant / Phase 6** | C4 systemic, C5 | Bezlotoxumab IV, rectal vancomycin | §6.1: ileus abolishes oral delivery — **every oral candidate above is unavailable here.** The one context where systemic PK is desirable. |

---

## 7. CANDIDATE SCORES — PATHWAY LENS

Scored on: axis coverage · uniqueness of axes hit · directional correctness · network position (upstream of branch points, hub/bottleneck) · absence of internal antagonism · loop-exit contribution.

| Candidate | R1 Mean | **Pathway** | Δ | Rationale |
|---|---|---|---|---|
| **Fidaxomicin** | 8.9 | **9.0** | +0.1 | 3.5 axes; **only C2 agent with no toxin-induction hazard** (bactericidal + sub-MIC toxin suppression) — a third mechanism of superiority Round 1 counted as two. Spares C7. Ceiling: no C1/C4/C5/C6. |
| **UDCA** | 7.1 | **7.5** | +0.4 | Sole occupant of **C1**, a Tier 1 axis. Active-species question resolves *favourably* — dysbiosis preserves parent drug, and every metabolite is also an inhibitor. Deductions: free-fraction margin unproven, FXR ratio risk, biofilm risk at low exposure. **TUDCA variant would score 8.0.** |
| **Bezlotoxumab** | 7.1 | **7.5** | +0.4 | Only 1.5 axes, but it is **the mechanistically complete C4 agent** — receptor blockade sits *upstream of the branch* between glucosylation-dependent injury and NOX1 necrosis. Upstream-of-branch beats downstream-of-branch. Route/cost/CHF are other agents' concerns. |
| **Ibezapolstat** | 6.9 | **6.5** | −0.4 | 2 axes; bactericidal so low induction hazard; reported secondary-bile-acid/microbiome shift is a real, under-credited **C7** touch. But adds nothing to the over-served C2 axis where four programmes already failed. |
| **Berberine** | 6.7 | **6.0** | −0.7 | Real C5 (serially reinforced) + C7 + the **non-obvious #72 enterococcal cross-feed** asset; moderate potency is the *correct shape* for bidirectional C5. **But: 3 axes not 4 (NF-κB/NLRP3 double-counted), and a directional conflict on C6 via Wnt/anti-proliferative activity** — the axis with zero coverage that cannot afford a negative. Zero direct project-data support. |
| **Ebselen** | 6.4 | **5.0** | −1.4 | Two axes on paper, but: **(i)** plausible internal antagonism — Stickland block may de-repress `tcdR`; **(ii)** **single-turnover in an anaerobic colon** (no oxidant to close the GPx-mimetic cycle) against a millimolar thiol/H₂S sink; **(iii)** CPD sits *downstream* of the C4 injury branch, so it misses NOX1 necrosis; **(iv)** absorbed, so needs colon-targeted delivery with §6.1 caveats. Resolves the 8.5-vs-4.0 conflict toward ADMET. |
| **Aprepitant** | 4.9 | **5.0** | +0.1 | 1 axis, but **NK1R #51 is a C5 arm nothing else touches** — pathway uniqueness earns a small hold despite every other lens disliking it. Requires systemic exposure (wrong direction per §6.2) and carries DDI burden. |
| **Vancomycin** | 6.6 | **4.5** | −2.1 | **The only candidate with net-negative coverage:** 1 axis hit, 1 axis actively degraded (**C7**). Its mechanism of harm *is* the recurrence loop. The pathway lens is the harshest lens on vancomycin and fully explains the 4.0–9.0 Round 1 spread. |
| **Niclosamide** | 5.1 | **4.0** | −1.1 | Redundant on C4 with a fragile pharmacophore. **Plus a pathway-level inversion no agent caught: its target (#30 delivery domain / endosomal acidification) is INSIDE HOST CELLS** — so niclosamide must *enter colonocytes*, meaning the "non-absorption is good" heuristic that favours every other candidate **works against it**. Nitro-reduction liability compounds this. |
| **Conessine** | 3.8 | **3.0** | −0.8 | Speculative C1 claim with the scaffold hypothesis largely falsified by the Chemist; no coherent network position. |

---

## 8. CROSS-CUTTING FINDINGS FOR OTHER PHASE 2 AGENTS

1. **→ Combination Designer & Literature Reviewer — the nutrient-limitation / toxin-induction hazard (§4.2).** By §2.5's own regulatory architecture (CodY/CcpA repress `tcdR` under nutrient *sufficiency*), every "starve the pathogen" mechanism — Stickland #21/#22, sialic acid #23, proline/glycine depletion — is a mechanism that **de-represses `tcdR`**. Contradicted in vivo by the enterococcal cross-feeding data, so: **flagged hazard, not established result.** **Screening rule: measure toxin per CFU, not toxin per mL.** A candidate that lowers burden while raising toxin/CFU is net-harmful in a disease whose morbidity is entirely toxin-mediated.

2. **→ SAR Analyst — the berberine question has changed.** It is not "improve potency/selectivity." It is **"can barrier/anti-inflammatory activity be separated from anti-proliferative Wnt/AMPK activity?"** Project data shows this is a *class-wide* flavonoid/alkaloid problem (quercetin: 14 tight-junction rows *and* 10 β-catenin rows), not berberine-specific. Decisive assay: colonic organoid regeneration ± TcdB.

3. **→ Drug Repurposing Strategist — evaluate tauroursodiol (TUDCA, CHEMBL272427, approved 2022).** Better colonic delivery physics than UDCA (PSA 123.9 vs 77.8; alogp 3.40 vs 4.48), resists deconjugation in BSH-depleted CDI, adds TGR5 #62 agonism, and per §2.1 conjugation does not convert an inhibitor into a germinant. **No Round 1 agent considered it.** Would raise UDCA's pathway score from 7.5 to 8.0.

4. **→ Drug Repurposing Strategist — #70 luminal antibiotic inactivation is absent from the candidate set.** Ribaxamase/DAV132: clinically validated (Phase 2/3 positive), no approved product, addresses **primary prevention** — the only intervention that prevents *loop entry* rather than treating after it. §2.2 calls it "arguably the highest-value white space in CDI." The set has no primary-prevention candidate at all.

5. **→ All agents — C6 (barrier/repair) has zero coverage, and it is the widest white space.** TcdB-FZD-mediated Wnt blockade means the mucosa cannot repair even after toxin clears — §2.9 calls this "an independent injury axis." No candidate addresses it; berberine may worsen it. Best data-backed chemotype is the flavonoids (quercetin/kaempferol/luteolin, 76 tight-junction rows in project data) — with the Wnt caveat above.

6. **→ Safety Pharmacologist — physicochemical DDI risk in Combination 1.** Bile salts solubilise poorly-soluble lipophiles. UDCA co-administered with fidaxomicin (MW 1058, very poorly soluble, efficacy depends on *luminal* retention) could micellise it and increase absorption, reducing luminal exposure. **Argues for sequential rather than concurrent dosing** — which the phase logic independently prefers.

7. **→ Ethnobotany / Natural Product Scout — two leads corroborated by project data.** (a) **Oleanolic acid → GPBAR1/TGR5 full agonist** (PMID:17825251) confirms the *Cyperus rotundus* lead — **but the same file shows it inhibits IL22 (PMID:26513295), the wrong direction for #47**; mixed-direction lead, test both arms. (b) **Celastrol → HSP90AA1 inhibition** (PMID:17010675, 32470352) supports the gedunin/celastrol → Hsp90 #40 → TcdB-translocation hypothesis, and celastrol also inhibits IL23A (#46, correct direction) — a 2-node coherent anti-virulence lead, with celastrol's toxicity as the obvious problem.

---

## 9. CONFIDENCE AND LIMITATIONS

**Overall confidence: Moderate.**

| Finding | Confidence | Basis |
|---|---|---|
| UDCA is itself the anti-germinant (not an LCA prodrug) | **High** | Structural: the 12α-OH determines germinant vs inhibitor; UDCA shares CDCA's pattern. Plus dual-assay in vitro activity. |
| Dysbiosis preserves parent UDCA | **High** | Both conversion routes require the depleted `bai` guild. Directly from §2.2. |
| Ebselen is single-turnover in the anaerobic colon | **Moderate–High** | The GPx-mimetic cycle requires a peroxide; the colon is strictly anaerobic. Chemically sound; not measured in colonic conditions. |
| CPD inhibition is downstream of the C4 injury branch | **High** | Stated in §2.6 A.3 and §5.2 for GTD inhibitors; CPD is on the same arm. |
| Berberine's Wnt conflict | **Moderate** | Berberine's anti-proliferative pharmacology is well documented; its *net* effect on a TcdB-injured crypt is inferred, not measured. Testable. |
| NF-κB/NLRP3 are one axis, not two | **High** | NF-κB transcribes NLRP3 and pro-IL-1β; the inflammasome processes it. Standard immunology. |
| Nutrient-limitation → toxin induction | **Low–Moderate** | Follows from §2.5's CodY/CcpA architecture, but contradicted in vivo by the enterococcal cross-feeding result. **Explicitly flagged as hypothesis.** |
| Combination 1 (fidax → UDCA) rationale | **Moderate–High** | Each mechanism independently supported; the complementarity is inferred. |
| Combination 2 self-tapering handoff | **Moderate** | Falls out of §2.2 biology cleanly; the three-way interaction is unstudied, and consortium/bile-acid antagonism is a real unquantified risk. |
| Colonic UDCA concentration estimate | **Moderate** | Arithmetic is transparent (§2.3) but rests on literature values for absorption, luminal volume, and IC50 that the Literature Reviewer should verify. Free-fraction correction is unquantified. |

**Limitations, stated plainly:**

- **~85% of this analysis is knowledge-based.** Project data contributed: physicochemical properties for UDCA/TUDCA/niclosamide/aprepitant/DCA/obeticholic acid (`chembl_approved_drugs.csv`), and four host-target leads (`pubchem_phytochem_target_interactions.csv`). **DisGeNET has no CDI data** (OM-specific only). **Berberine has zero direct target rows in project data** — its entire network profile is recall.
- **No CDI-specific pathway annotations exist in the knowledge graph.** Per my skill file's stated strategy, I mapped target → axis using domain knowledge against §2/§5 of the Disease Brief. The C1–C8 axis decomposition is my construction, not a curated resource — a different decomposition would shift the coverage counts, though I do not think it would change the gap ranking.
- **All concentration estimates are order-of-magnitude.** They are shown as arithmetic specifically so downstream agents can attack the inputs.
- **The absence of a candidate from an axis is not proof of inactivity**, only of unreported activity — my skill file's "don't over-interpret absence" guardrail. This applies most to the C5/C6 columns for the antibacterial candidates, which have simply never been assayed for host effects.
- **Every combination recommendation is a hypothesis about an untested interaction.** Each carries a named decisive experiment; none should be read as a clinical recommendation.

---

## 10. STRUCTURED OUTPUT (JSON)

```json
{
  "agent": "pathway-analyst",
  "phase": 2,
  "disease": "Clostridioides difficile infection",
  "date": "2026-08-18",
  "skill_file_adaptation": {
    "original_cascades": ["NF-kB", "MAPK", "PI3K/AKT/mTOR", "ceramide", "Wnt/beta-catenin", "TLR"],
    "reason_for_rebuild": "OM cascades are entirely host signal transduction; CDI's causal graph spans pathogen, host and commensal community, includes two RESTORE-direction axes, and has a recurrence loop as its defining topological feature",
    "cdi_axes_defined": {
      "C1": "Germination (Phase 1) - taurocholate/CspC/CspB/SleC",
      "C2": "Vegetative fitness (Phase 2) - RNAP/PolC/MetRS/PG + Stickland/sialic acid/cross-feed",
      "C3": "Toxin regulation (Phase 3) - CodY/CcpA/SigD/Agr converging on TcdR",
      "C4": "Intoxication (Module A) - receptors/endosome/CPD/GTD/Rho",
      "C5": "Host inflammation (Module B) - NLRP3/IL-1b/CXCR2, IL-23 vs IL-22, NK1R",
      "C6": "Barrier and repair (Phase 4) - tight junctions/MLCK/Wnt-FZD/EGFR",
      "C7": "Ecological restoration (Phase 0 + Module C) - bai guild/BSH/DCA-LCA/niche",
      "C8": "Sporulation (Phase 1/3 reverse) - Spo0A/sigma factors/coat"
    },
    "retained_from_skill_file": ["coverage matrix method", "phase alignment guardrail", "crosstalk tracing", "polypharmacology double-edge", "network metrics"]
  },

  "network_topology": {
    "hub_nodes": [
      {"node": "TcdR (#15)", "axes": ["C3", "C4", "C5", "C6"], "note": "single bottleneck of the toxin axis; six regulatory inputs converge; most connected druggable-in-principle node in CDI"},
      {"node": "Rho GTPases (#42)", "axes": ["C4", "C5", "C6"], "note": "convergence point and explicitly UNDRUGGABLE for reactivation - the network's key structural constraint: all therapy must act upstream"},
      {"node": "Secondary bile acids DCA/LCA (#66)", "axes": ["C1", "C2", "C7"], "note": "one chemical class spanning three axes - why bile acid chemistry is disproportionately valuable in CDI"},
      {"node": "Spo0A (#12)", "axes": ["C8", "C3"], "note": "the recurrence loop's write-head"}
    ],
    "bottleneck_nodes": ["TcdR #15 (six inputs)", "CspC #7 (germinant + co-germinant integration)", "v-ATPase #41 (all endocytic toxin entry)"],
    "recurrence_loop_entry_points": [
      {"point": "#70 luminal antibiotic inactivation", "effect": "prevents loop ENTRY - primary prevention", "candidate_coverage": "NONE in candidate set"},
      {"point": "#64/#69 ecological restoration", "effect": "EXITS the loop", "candidate_coverage": "live biotherapeutics only, no small molecule"},
      {"point": "C1 germination + C8 sporulation block", "effect": "HOLDS loop open without exiting - suppression not cure", "candidate_coverage": "UDCA (C1), fidaxomicin (C8, incidental)"}
    ],
    "key_insight": "Fidaxomicin minimises loop RE-ENTRY while treating C2; vancomycin treats C2 by maximising loop re-entry. That is the entire recurrence problem in one sentence, and it explains vancomycin's 4.0-9.0 Round 1 spread exactly."
  },

  "candidate_scores": [
    {"candidate": "Fidaxomicin", "score": 9.0, "round1_mean": 8.9, "delta": 0.1,
     "axes_covered": ["C2 strong", "C3 strong", "C8 strong", "C7 partial"], "axis_count": 3.5,
     "unique_contribution": "Only C2 agent with NO toxin-induction hazard - bactericidal AND suppresses toxin at sub-MIC",
     "rationale": "A third mechanism of superiority that Round 1 counted as two: microbiome sparing + sporulation inhibition + immunity to the nutrient-limitation induction hazard",
     "ceiling": "No coverage of C1, C4, C5, C6"},
    {"candidate": "UDCA", "score": 7.5, "round1_mean": 7.1, "delta": 0.4,
     "axes_covered": ["C1 strong", "C2 partial", "C7 partial"], "axis_count": 2,
     "unique_contribution": "Sole occupant of C1, a Tier 1 axis the Disease Brief calls the most conspicuous unexploited target class in CDI",
     "rationale": "Active-species question resolves FAVOURABLY - dysbiosis preserves parent drug and all metabolites are also inhibitors. Deductions: free monomeric fraction unproven, FXR ratio risk, sub-inhibitory biofilm risk",
     "variant_note": "TUDCA formulation would score 8.0"},
    {"candidate": "Bezlotoxumab", "score": 7.5, "round1_mean": 7.1, "delta": 0.4,
     "axes_covered": ["C4 strong", "C5 partial", "C6 partial"], "axis_count": 1.5,
     "unique_contribution": "The mechanistically COMPLETE C4 agent - receptor blockade sits upstream of the branch between glucosylation-dependent injury and NOX1-dependent necrosis",
     "rationale": "Fewest axes of any high scorer, but intervening upstream of a branch point beats intervening downstream on one arm. This is why it outscores ebselen despite ebselen's dual mechanism"},
    {"candidate": "Ibezapolstat", "score": 6.5, "round1_mean": 6.9, "delta": -0.4,
     "axes_covered": ["C2 strong", "C7 partial", "C8 partial"], "axis_count": 2,
     "unique_contribution": "Reported secondary-bile-acid/microbiome shift is a real C7 touch that Round 1 under-credited; bactericidal so low induction hazard",
     "rationale": "Adds nothing to the over-served C2 axis where four Phase 3 programmes already failed to differentiate"},
    {"candidate": "Berberine", "score": 6.0, "round1_mean": 6.7, "delta": -0.7,
     "axes_covered": ["C5 strong", "C7 partial", "C2 partial", "C6 ADVERSE"], "axis_count": 2.5,
     "unique_contribution": "Non-obvious hit on #72 enterococcal cross-feeding; moderate potency is the CORRECT shape for bidirectional C5 where the model says MODULATE not BLOCK",
     "rationale": "Three axes not four (NF-kB and NLRP3 are serially coupled on one axis) plus a DIRECTIONAL CONFLICT on C6 via Wnt/beta-catenin and AMPK/mTOR anti-proliferative activity - the axis with zero coverage that cannot afford a negative contributor",
     "data_note": "ZERO direct berberine-target rows in project data (20 mentions, all CTD co-treatment annotations for other compounds)"},
    {"candidate": "Ebselen", "score": 5.0, "round1_mean": 6.4, "delta": -1.4,
     "axes_covered": ["C4 partial", "C2 uncertain", "C3 ADVERSE-possible"], "axis_count": 1.5,
     "unique_contribution": "Only oral small-molecule anti-toxin concept with in vivo data",
     "rationale": "Four compounding problems: (1) plausible internal antagonism - Stickland block may de-repress tcdR; (2) STRICTLY SINGLE-TURNOVER in an anaerobic colon because the GPx-mimetic cycle needs a peroxide to regenerate the selenazole, against a millimolar GSH/cysteine/H2S sink; (3) CPD is downstream of the C4 injury branch so it misses NOX1 necrosis; (4) absorbed, needs colon-targeted delivery with the dysbiosis and PPI release-trigger caveats",
     "conflict_resolution": "Resolves Target Profiler 8.5 vs ADMET 4.0 toward ADMET - the warhead is not destroyed, it is diluted and de-catalysed"},
    {"candidate": "Aprepitant", "score": 5.0, "round1_mean": 4.9, "delta": 0.1,
     "axes_covered": ["C5 partial", "C6 partial"], "axis_count": 1,
     "unique_contribution": "NK1R #51 is a C5 arm nothing else in the set touches",
     "rationale": "Pathway uniqueness earns a small hold despite every other lens disliking it; requires systemic exposure (wrong direction per the inverted ADMET logic) and carries DDI burden"},
    {"candidate": "Vancomycin", "score": 4.5, "round1_mean": 6.6, "delta": -2.1,
     "axes_covered": ["C2 strong", "C7 ADVERSE"], "axis_count": 1, "net_axis_count": 0,
     "unique_contribution": "None - fully substituted by fidaxomicin on the pathway lens",
     "rationale": "The only candidate with NET-NEGATIVE coverage: one axis hit, one axis actively degraded. Its mechanism of harm IS the recurrence loop. The pathway lens is the harshest possible lens on vancomycin and fully explains the 4.0-9.0 Round 1 spread"},
    {"candidate": "Niclosamide", "score": 4.0, "round1_mean": 5.1, "delta": -1.1,
     "axes_covered": ["C4 partial", "C2 partial"], "axis_count": 1,
     "unique_contribution": "None - redundant on C4 with a fragile pharmacophore",
     "rationale": "NEW pathway-level finding: its target (#30 delivery domain / endosomal acidification) is INSIDE HOST CELLS, so niclosamide must enter colonocytes. The non-absorption heuristic that favours every other candidate WORKS AGAINST IT. Nitro-reduction liability compounds this"},
    {"candidate": "Conessine", "score": 3.0, "round1_mean": 3.8, "delta": -0.8,
     "axes_covered": ["C1 speculative", "C2 weak"], "axis_count": 0.5,
     "unique_contribution": "None",
     "rationale": "Speculative C1 claim with the CspC scaffold hypothesis largely falsified by the Chemist; no coherent network position"}
  ],

  "pathway_coverage_assessment": {
    "axis_redundancy": {"C1": 1, "C2": 6, "C3": 1, "C4": 2, "C5": 2, "C6": 0, "C7": 1, "C8": 1},
    "critical_gap": {
      "axis": "C6 barrier and repair",
      "coverage": 0,
      "why": "TcdB occupancy of FZD1/2/7 blocks Wnt/beta-catenin so crypt stem cells cannot renew - repair failure is an independent injury axis and is why the mucosa stays broken after toxin clears. No candidate addresses it and berberine may worsen it",
      "best_data_backed_chemotype": "flavonoids - quercetin (14 tight-junction rows), kaempferol, luteolin, myricetin, genistein in pubchem_phytochem_target_interactions.csv",
      "caveat": "the same chemotype co-modulates CTNNB1 (quercetin: 10 rows) - the barrier-positive / Wnt-negative coupling is CLASS-WIDE, not berberine-specific"
    },
    "single_points_of_failure": [
      "C1 depends entirely on UDCA - if the concentration question fails, the Tier 1 germination axis is empty",
      "C3 depends entirely on fidaxomicin, and only as an incidental sub-MIC effect rather than by design",
      "C7 depends entirely on live biotherapeutics - no small molecule exists"
    ],
    "over_served": {
      "axis": "C2 vegetative fitness",
      "candidates": 6,
      "why_a_liability": "This is the axis where ridinilazole, surotomycin and cadazolid all had adequate activity and adequate narrowness and all failed to differentiate from vancomycin. A seventh C2 agent adds zero coverage"
    },
    "absent_from_candidate_set_entirely": {
      "target": "#70 luminal antibiotic inactivation (ribaxamase / DAV132)",
      "why_it_matters": "The only intervention that prevents recurrence-loop ENTRY rather than treating after entry. Clinically validated (Phase 2/3 positive), no approved product, and the Disease Brief calls it arguably the highest-value white space in CDI. The set has no primary-prevention candidate at all"
    }
  },

  "answers_to_primary_questions": {
    "Q1_UDCA_active_species": {
      "answer": "UDCA ITSELF is the active anti-germinant - it is not a prodrug for LCA",
      "structural_basis": "Germinant vs inhibitor at CspC is determined by the C12 hydroxyl, not by conjugation. Cholate/taurocholate/DCA all carry 12alpha-OH and germinate; CDCA, UDCA and LCA all lack it and inhibit. UDCA is the 7beta-epimer of CDCA, the validated competitive inhibitor, and shares its defining feature",
      "conjugation_note": "Taurochenodeoxycholate inhibits, so the taurine head group is not what makes taurocholate a germinant",
      "metabolic_finding": "Round 1 framed 7alpha-dehydroxylation as a liability; on the network it is a FEATURE. Both UDCA-to-LCA routes (direct 7-dehydroxylation, or 7beta/7alpha-HSDH epimerisation to CDCA then bai) require the SAME bai guild whose depletion causes CDI. So UDCA accumulates as parent in exactly the dysbiotic patients who need it, and is consumed in healthy people who do not. The drug's PK co-varies with disease state in the right direction",
      "robustness": "Moot for efficacy - UDCA, its epimer CDCA, and its product LCA are ALL C1 inhibitors. There is no metabolic route from UDCA to a germinant",
      "toxicity_corollary": "The LCA exposure ceiling that normally constrains high-dose UDCA is relaxed in the same dysbiotic population",
      "colonic_concentration": {
        "nominal_estimate_mM": "4-15 at standard 13-15 mg/kg/day",
        "arithmetic": "300-600 mg/day reaching colon / 392.6 g/mol / ~0.15 L luminal water",
        "requirement_estimate_mM": "0.5-5 free UDCA (reported anti-germination and growth-inhibitory activity is high-uM to low-mM)",
        "verdict": "Nominal margin adequate; FREE MONOMERIC margin NOT established",
        "three_deductions": ["CMC ceiling - monomeric UDCA plateaus above its critical micelle concentration and the competitive inhibitor at CspC is presumably the monomer", "fecal solids / mucin partitioning", "diarrhoeal transit sharply reduces distal-colon contact time during the acute episode"],
        "high_dose_precedent": "up to 28-30 mg/kg/day has human dosing precedent"
      },
      "positioning_consequence": "MAINTENANCE/PREVENTION agent across the 8-12 week post-antibiotic recurrence window, NOT an acute-episode agent. During acute CDI transit is too fast and luminal volume too high. The recurrence window is exactly when transit has normalised, the guild is still absent, and the spore reservoir is intact - and it is where the human ileal-pouch signal was generated",
      "what_actually_decides_it": "The UDCA:taurocholate MOLAR RATIO at CspC, not the absolute UDCA concentration - inhibition is competitive",
      "two_new_risks": [
        {"risk": "FXR feedback - the inhibitor may raise its own competitor", "mechanism": "UDCA is at best a weak FXR (#61) ligand and unlike CDCA provides little agonist tone. If it dilutes CDCA's share of the pool and relieves FXR-mediated feedback repression of hepatic synthesis, the primary bile acid pool and hence colonic TAUROCHOLATE could expand", "confidence": "UNCERTAIN - the Disease Brief itself flags #61 direction as uncertain", "decisive_experiment": "measure fecal/colonic UDCA:taurocholate molar ratio on therapy in antibiotic-dysbiotic subjects"},
        {"risk": "Sub-inhibitory biofilm induction", "mechanism": "Sub-inhibitory bile acid exposure has been reported to induce C. difficile biofilm (best characterised for DCA); biofilm is a probable persistence and recurrence reservoir. A UDCA concentration landing BELOW its growth-inhibitory threshold - the marginal-exposure scenario - could convert suppression into persistence promotion", "confidence": "EMERGING", "note": "the bile acid analogue of the sub-inhibitory-antibiotic toxin-induction warning; test the LOW end of the range, not just the high end"}
      ],
      "formulation_recommendation": {
        "molecule": "Tauroursodiol / TUDCA (CHEMBL272427, first approval 2022)",
        "project_data": "PSA 123.9 and alogp 3.40 vs UDCA (CHEMBL1551) PSA 77.8 and alogp 4.48 - substantially more polar, less lipophilic",
        "advantages": ["reduced passive small-intestinal absorption means a larger colonic fraction - the exact ADMET inversion the route section asks for", "BSH #65 is depleted in CDI so TUDCA arrives and REMAINS conjugated - a second dysbiosis-protects-the-drug effect stacking on the bai effect", "TGR5/GPBAR1 #62 agonist where UDCA is not, adding C5/C6 tone and taking it from a 2-axis to a 3.5-axis agent"],
        "caveats": ["anti-germination potency of conjugate vs parent needs direct measurement", "2022 approval was as a fixed-dose combination - single-agent regulatory path needs checking"],
        "status": "NOVEL - not considered by any Round 1 agent"
      }
    },

    "Q2_berberine_network": {
      "verdict": "GENUINELY SYNERGISTIC on C5 + C7 + C2(#72); GENUINELY CONFLICTED on C6; and NARROWER than the four-mechanism story implies. Not noise, but not the clean multi-target win the Ethnobotany 8.0 / ADMET 8.0 pair described",
      "data_availability": "ZERO direct berberine-target rows in project data. Queried pubchem_phytochem_target_interactions.csv (60,521 rows, 15,587 unique genes): 20 rows mention berberine, ALL are CTD co-treatment annotations for other compounds. Berberine also absent from IMPPAT. Entire network profile is knowledge-based",
      "finding_1_double_counting": {
        "claim": "NLRP3 inhibition + NF-kB suppression = two-axis coverage",
        "verdict": "FALSE - one axis, serially coupled",
        "mechanism": "NF-kB transcribes NLRP3 itself and pro-IL-1beta; the NLRP3/caspase-1 inflammasome then processes pro-IL-1beta to mature IL-1beta. Hitting both is REINFORCEMENT of one axis, not coverage of two",
        "nuance": "Serial inhibition of one amplification cascade does give steeper, more robust suppression - the classic natural-product advantage. It just must not be counted twice in a coverage matrix",
        "corrected_coverage": "C5 (one axis, doubly hit) + C6 (net direction contested) + C7 (modulate) + C2 (weak) = 3 genuine axes, not 4"
      },
      "finding_2_wnt_conflict": {
        "severity": "MOST SERIOUS finding on berberine - potentially disqualifying",
        "mechanism": "Berberine's anticancer pharmacology is substantially built on Wnt/beta-catenin suppression and AMPK activation / mTOR inhibition - it is an ANTI-PROLIFERATIVE agent in colonic epithelium",
        "conflict": "TcdB already occupies FZD1/2/7 (#36) and thereby blocks Wnt/beta-catenin (#59), whose required direction is RESTORE. Berberine at high luminal concentration (oral F <1% means ~99% stays luminal, reaching mg/g fecal levels) delivered onto a colon whose crypts already cannot regenerate would FURTHER suppress the axis that needs restoring",
        "guardrail_violated": "The skill file's primary guardrail - direction matters. Same class of error as blocking NF-kB during the healing phase in OM",
        "class_wide": "Project data shows this is not berberine-specific: 55 CTNNB1 rows and 76 tight-junction rows in the phytochem file, with quercetin appearing in BOTH (14 tight-junction, 10 CTNNB1). The barrier-positive / Wnt-negative coupling is class-wide in flavonoids and alkaloids",
        "decisive_experiment": "berberine's effect on colonic organoid or crypt regeneration in the presence of TcdB. If it worsens regeneration, berberine is contraindicated by mechanism in Phase 4 disease, not merely underpowered",
        "reframed_SAR_question": "Not 'improve potency/selectivity' but 'can barrier/anti-inflammatory activity be SEPARATED from anti-proliferative Wnt/AMPK activity?'"
      },
      "finding_3_best_asset": {
        "asset": "Anti-enterococcal activity cutting the #72 cross-feed",
        "mechanism": "The Disease Brief flags Enterococcus-C. difficile cross-feeding to the Pathway Analyst specifically: enterococcal leucine and ornithine support C. difficile Stickland metabolism and ELEVATE toxin production, direction SUPPRESS",
        "reframe": "Berberine's 'non-selective, too-weak-to-matter' antibacterial breadth - the property the Chemist scored down at 5.0 - is pointed at a validated INDIRECT anti-C. difficile node. It does not need to reach C. difficile's MIC; it needs to reach Enterococcus's, which is a lower bar",
        "consequence": "Partly answers the Chemist's fecal-binding objection by lowering the required potency threshold. Differentiated mechanism no other candidate provides"
      },
      "finding_4_potency_shape": {
        "insight": "Moderate potency is the CORRECT SHAPE for C5, not a weakness",
        "basis": "The Disease Brief is explicit that C5 is bidirectional - neutrophil depletion WORSENS outcomes in mice, so CXCR2 #48 carries direction MODULATE not fully BLOCK and a blanket antagonist is as likely to harm as help",
        "consequence": "A moderate-potency, multi-node, incompletely-penetrant agent is arguably a BETTER structural fit for a bidirectional axis than a potent selective inhibitor, because it dampens rather than ablates. A genuine argument for a berberine-class agent over an MCC950-class NLRP3 inhibitor in CDI specifically - and it inverts the usual 'natural products are just weak drugs' objection"
      }
    },

    "Q3_ebselen_dual_mechanism": {
      "synergy_in_principle": "STRUCTURALLY YES - #26 TcdB CPD (C4) and #21/#22 PrdB/GrdA (C2) sit on different axes and are non-redundant: one reduces damage per organism, the other reduces organism fitness. Textbook complementarity",
      "synergy_in_practice": "PLAUSIBLY SELF-ANTAGONISING - see the nutrient-limitation hazard below",
      "internal_antagonism": {
        "mechanism": "CodY #16 senses GTP + branched-chain amino acids and CcpA #17 senses carbon; both REPRESS tcdR under nutrient SUFFICIENCY. The Disease Brief states directly that toxin production is induced by stress and nutrient limitation. Ebselen's PrdB/GrdA inhibition blocks Stickland fermentation - the organism's principal energy-yielding route - which is nutrient limitation imposed pharmacologically. Ebselen's CPD arm would then be fighting a LARGER toxin pool its own C2 arm created",
        "confidence": "LOW-MODERATE - flagged hazard, NOT established",
        "contrary_evidence": "The enterococcal cross-feeding data run against this: removing enterococci removes leucine (a BCAA, a CodY ligand) which by CodY logic should de-repress toxin, yet the observed effect is REDUCED toxin. In vivo, biomass, stationary-phase timing and growth-rate effects evidently dominate the simple CodY rule"
      },
      "reducing_colon_question": {
        "answer": "The colon does NOT destroy the Se warhead - it DILUTES it and REMOVES ITS CATALYTIC TURNOVER. That distinction is the resolution",
        "problem_a_mass_action": {"description": "Millimolar bulk thiol (GSH/cysteine) plus 0.2-3.4 mM fecal H2S against a nanomolar-or-lower target protein. Mass action puts essentially all ebselen into selenenyl-sulfide adduct form", "counter_argument": "selenenyl sulfides are EXCHANGEABLE, so ebselen-SG can still transfer Se to a more nucleophilic acceptor, and the CPD catalytic cysteine is exactly that - activated, low pKa, in a protease active site - giving genuine kinetic selectivity", "verdict": "surmountable by dose alone"},
        "problem_b_no_turnover": {"description": "DECISIVE. Ebselen's GPx-mimetic cycle REQUIRES a peroxide to reoxidise the selenol back to the active selenazole. In a strictly anaerobic, peroxide-free colonic lumen that cycle CANNOT CLOSE. Ebselen in the colon is STRICTLY STOICHIOMETRIC - single-turnover: one molecule modifies at most one thiol, and the overwhelming majority are consumed by bulk GSH/cysteine/H2S before encountering CPD or PrdB", "consequence": "required dose scales with the MILLIMOLAR BULK THIOL POOL, not with target concentration - sub-millimole to millimole per day of purely sacrificial consumption"},
        "problem_c_delivery": {"description": "Ebselen (MW ~274, lipophilic) is ORALLY ABSORBED and its known disposition is binding to plasma albumin Cys34 - exactly the wrong direction for CDI's inverted ADMET logic. Its documented human dosing was designed for SYSTEMIC delivery. Reaching the colon requires a colon-targeted formulation, and microbiota-triggered release fails in CDI dysbiosis while pH-dependent coatings are defeated by the PPI co-administration common in this population"}
      },
      "fourth_problem_wrong_node": {
        "finding": "Independent of chemistry, CPD inhibition covers LESS of C4 than receptor blockade does",
        "mechanism": "At high toxin dose there is a GLUCOSYLTRANSFERASE-INDEPENDENT necrosis pathway requiring ONLY receptor binding, via NOX1-derived ROS. The Disease Brief spells out that a GTD-active-site inhibitor would not block high-dose necrosis and that receptor-blocking approaches are more complete. CPD acts AFTER receptor binding and translocation, so the same logic applies - blocking it leaves the receptor-binding-dependent necrosis arm fully intact",
        "general_principle": "Intervening upstream of a branch point beats intervening downstream of it on one arm",
        "consequence": "A structural argument that bezlotoxumab's SINGLE node is worth more than ebselen's TWO - and the reason bezlotoxumab outscores ebselen on the pathway lens despite ebselen's dual mechanism"
      },
      "conflict_resolution": "Target Profiler's 8.5 credits target quality and is right about that; ADMET's 4.0 credits delivery reality. ADMET is closer. Pathway score 5.0"
    },

    "Q4_combinations": [
      {
        "rank": 1,
        "name": "Fidaxomicin (days 0-10) then UDCA or TUDCA maintenance (weeks 2-12)",
        "axes": ["C1", "C2", "C3", "C7 partial", "C8"],
        "axis_count": 4.5,
        "staging": "SEQUENTIAL, not concurrent",
        "why_special": "Fidaxomicin's single acknowledged failure mode is that SPORES SURVIVE (an ESTABLISHED point in the brief). UDCA's entire mechanism is preventing those surviving spores from germinating. One agent's failure mode is the other's mechanism of action - the strongest form of combination rationale, not merely additive",
        "temporal_logic": "Fidaxomicin's C8 sporulation inhibition means UDCA faces a STATIC, non-replenishing spore reservoir rather than a growing one - which directly answers the brief's open question about anti-germinants holding against a continuously replenished load. And UDCA's transit/dilution weakness applies during acute diarrhoea but not during the post-treatment window, so deploying it after fidaxomicin dodges its own worst PK liability",
        "risks": [
          {"risk": "Physicochemical DDI - UNASSESSED by any Round 1 agent", "detail": "Bile salts are solubilising agents. Fidaxomicin is MW 1058 and very poorly water-soluble, and its efficacy depends on high LUMINAL concentration with minimal absorption. Co-administered UDCA could micellise it, raising dissolved fraction and absorption and lowering luminal exposure", "mitigation": "sequential rather than concurrent dosing - which the phase logic independently prefers", "route_to": "ADMET Predictor and Chemist"},
          {"risk": "Sub-inhibitory bile-acid biofilm induction if UDCA exposure lands low"},
          {"risk": "The UDCA:taurocholate ratio question governs the entire benefit"}
        ],
        "confidence": "Moderate-High - both approved, each mechanism independently supported, interaction inferred not demonstrated"
      },
      {
        "rank": 2,
        "name": "Fidaxomicin then UDCA/TUDCA + oral live biotherapeutic (VOWST or VE303)",
        "axes": ["C1", "C2", "C3", "C5 partial", "C6 partial", "C7 strong", "C8"],
        "axis_count": "5.5-6",
        "distinction": "The ONLY construction in this analysis with strong coverage on C7, the sole loop-EXITING axis. Everything else suppresses",
        "novel_argument_self_tapering_handoff": "UDCA provides PHARMACOLOGICAL C1 coverage during the window when the ECOLOGICAL C1/C7 defence is absent. As the consortium re-establishes the bai guild, that same guild begins converting UDCA to LCA - and LCA is itself a C1 germination inhibitor AND a C2 growth inhibitor. The bridging drug is consumed precisely as the endogenous mechanism it substitutes for comes back online, and its metabolite is on-mechanism. No wean-off cliff. Falls directly out of the brief's Phase 0 biology and is only visible on a network map",
        "risks": [
          {"risk": "TESTABLE ANTAGONISM - the key risk", "detail": "DCA/LCA broadly inhibit Clostridia. Does high luminal UDCA suppress the engrafting consortium? C. scindens and relatives are bile-acid-metabolising and presumably tolerant, but VE303's eight strains and VOWST's spore population are not uniformly so", "decisive_experiment": "consortium engraftment efficiency plus or minus UDCA. If UDCA blocks engraftment the combination INVERTS from synergistic to antagonistic"},
          {"risk": "Live biotherapeutics are adjunctive, require prior antibiotic therapy and careful timing - the staging respects this"},
          {"risk": "Commercial viability of Rebyota/Vowst flagged UNCERTAIN in the brief; VE303 is Phase 3", "route_to": "Clinical Feasibility Assessor"}
        ],
        "confidence": "Moderate - components individually strong (FMT-class effect sizes are among the largest in modern therapeutics), three-way interaction unstudied"
      },
      {
        "rank": 3,
        "name": "Fidaxomicin + bezlotoxumab + UDCA",
        "axes": ["C1", "C2", "C3", "C4", "C8"],
        "axis_count": 5,
        "distinction": "Maximum coverage achievable from APPROVED agents - deployable now rather than a development proposal. Adds C4, the only axis that protects the HOST while the others work on the organism, using the mechanistically COMPLETE C4 agent",
        "positioning": "Patients with 2 or more recurrence risk factors, where toxin burden is the proximate threat",
        "risks": ["IV-only, expensive, single-dose, TcdB-only with no CDT coverage", "BOXED heart-failure-exacerbation concern in an elderly CHF-prevalent population - route to Safety Pharmacologist", "commercial availability flagged UNCERTAIN", "leaves C5/C6/C7 uncovered - suppresses well but does not exit the loop"],
        "confidence": "Moderate-High on pathway logic; feasibility is the constraint, not the biology"
      }
    ],

    "Q4_combinations_to_avoid": [
      {"combination": "Ebselen + bezlotoxumab", "reason": "Redundant on C4, and ebselen covers strictly LESS of it - misses the receptor-binding-dependent NOX1 necrosis arm. Pays twice for one axis and the cheaper component is the incomplete one"},
      {"combination": "Ebselen + niclosamide", "reason": "Both target C4 Module A entry/processing AND both have redox-fragile pharmacophores in the same anaerobic compartment - a SHARED failure mode. Correlated failure, not diversified risk, which is the opposite of what combination design is for"},
      {"combination": "Ebselen + any Stickland or nutrient-depletion agent", "reason": "Compounds the tcdR de-repression hazard - two agents both imposing nutrient limitation on an organism whose toxin genes are de-repressed BY nutrient limitation"},
      {"combination": "Vancomycin + any C7 restoration agent", "reason": "Direct directional conflict - vancomycin's mechanism of harm IS C7 destruction; it would sterilise the consortium it is co-administered with"},
      {"combination": "Berberine + anything, in active Phase 4 disease", "reason": "Until the Wnt/anti-proliferative liability is excluded, berberine risks worsening C6 - the axis that already has zero coverage and cannot afford a negative contributor"},
      {"combination": "Any second C2 agent added to fidaxomicin", "reason": "Zero added axes. Six of ten candidates already crowd C2, where four Phase 3 programmes failed to differentiate"}
    ]
  },

  "cross_cutting_findings": [
    {
      "id": "CC1",
      "title": "The nutrient-limitation / toxin-induction hazard - a class-level warning",
      "to": ["Combination Designer", "Literature Reviewer", "SAR Analyst"],
      "finding": "By the brief's own regulatory architecture (CodY #16 and CcpA #17 REPRESS tcdR under nutrient SUFFICIENCY), every 'starve the pathogen' mechanism is a mechanism that DE-REPRESSES tcdR. This spans Stickland #21/#22, sialic acid #23, and Module C's DEPLETE-proline/glycine strategies",
      "hazard_by_target": {"PrdB/GrdA #21/#22": "High", "sialic acid #23": "High", "deplete luminal proline/glycine": "High", "deplete taurocholate": "None - C1 not C2", "RNAP #1 fidaxomicin": "None - INVERTED, bactericidal and toxin-suppressing at sub-MIC", "PolC #3 ibezapolstat": "Low - bactericidal"},
      "screening_rule": "MEASURE TOXIN PER CFU, not toxin per mL or bacterial burden. A candidate that lowers CFU while raising toxin/CFU is a NET HARM in a disease whose morbidity is entirely toxin-mediated",
      "confidence": "LOW-MODERATE - mechanistically grounded, empirically contested by the enterococcal cross-feeding result. Flagged hazard requiring measurement, NOT an established result",
      "bonus_insight": "Explains a third mechanism of fidaxomicin's dominance that Round 1 treated as two separate virtues: it is bactericidal AND toxin-suppressing at sub-MIC, so it is the one C2 agent with NO induction hazard at any exposure level"
    },
    {
      "id": "CC2",
      "title": "Evaluate tauroursodiol (TUDCA) as the preferred colonic-delivery bile acid",
      "to": ["Drug Repurposing Strategist", "SAR Analyst", "ADMET Predictor"],
      "finding": "CHEMBL272427, approved 2022. Project data: PSA 123.9 / alogp 3.40 vs UDCA's 77.8 / 4.48. More polar means less small-intestinal absorption and a larger colonic fraction; BSH depletion in CDI keeps it conjugated; it adds TGR5 #62 agonism that UDCA lacks. Conjugation does not convert an inhibitor into a germinant (taurochenodeoxycholate inhibits)",
      "impact": "Would raise UDCA's pathway score from 7.5 to 8.0",
      "status": "NOVEL - no Round 1 agent considered it"
    },
    {
      "id": "CC3",
      "title": "#70 luminal antibiotic inactivation is absent from the candidate set entirely",
      "to": ["Drug Repurposing Strategist", "Clinical Feasibility Assessor"],
      "finding": "Ribaxamase (SYN-004) and DAV132 are clinically validated (Phase 2/3 positive) with no approved product, and they address PRIMARY PREVENTION - the only point that prevents recurrence-loop ENTRY rather than treating after entry. The brief calls this arguably the highest-value white space in CDI. The candidate set has no primary-prevention candidate at all"
    },
    {
      "id": "CC4",
      "title": "C6 barrier/repair has zero coverage and is the widest white space",
      "to": ["all agents"],
      "finding": "TcdB-FZD-mediated Wnt blockade means the mucosa cannot repair even after toxin clears - an INDEPENDENT injury axis. No candidate addresses it; berberine may worsen it. Best data-backed chemotype is flavonoids (quercetin 14 tight-junction rows, plus kaempferol, luteolin, myricetin, genistein) - with the class-wide Wnt caveat"
    },
    {
      "id": "CC5",
      "title": "Two Ethnobotany leads corroborated by project data, one with a directional catch",
      "to": ["Ethnobotany Expert", "Natural Product Scout", "Target Profiler"],
      "leads": [
        {"lead": "Oleanolic acid to GPBAR1/TGR5 #62", "evidence": "FULL AGONIST, PMID:17825251; binding PMID:23022524 and PMID:23041323 (4 rows in pubchem_phytochem_target_interactions.csv)", "status": "CORROBORATES the Cyperus rotundus / Musta lead with project data", "catch": "The SAME file shows oleanolic acid INHIBITS IL22 (PMID:26513295) - the WRONG direction for #47, which is AGONIZE. Mixed-direction lead; test both arms"},
        {"lead": "Betulinic acid to GPBAR1/TGR5", "evidence": "FULL AGONIST, PMID:19911773", "catch": "also 2 CTNNB1 rows - same Wnt caution as berberine"},
        {"lead": "Celastrol to HSP90AA1 #40", "evidence": "inhibition, PMID:17010675 and PMID:32470352", "status": "DATA-BACKED support for the gedunin/celastrol to Hsp90 to TcdB-translocation-blockade hypothesis. Celastrol also inhibits IL23A #46 in the correct direction - a 2-node coherent anti-virulence lead", "caveat": "celastrol's toxicity is the obvious problem"}
      ]
    },
    {
      "id": "CC6",
      "title": "Niclosamide's target is intracellular - the non-absorption heuristic inverts",
      "to": ["ADMET Predictor", "Chemist", "SAR Analyst"],
      "finding": "Niclosamide's node (#30 delivery domain / endosomal acidification) is INSIDE HOST CELLS, so niclosamide must ENTER colonocytes to work. The 'non-absorption is the dominant positive predictor' heuristic that all six Round 1 agents applied - and that favours every other candidate - WORKS AGAINST niclosamide. This is independent of, and compounds, the nitro-reduction pharmacophore problem"
    }
  ],

  "confidence": "Moderate",
  "data_provenance": {
    "knowledge_based_fraction": "~85%",
    "project_data_used": [
      "data/processed/chembl_approved_drugs.csv - physicochemical properties for URSODIOL (CHEMBL1551), TAURURSODIOL (CHEMBL272427), NICLOSAMIDE (CHEMBL1448), APREPITANT (CHEMBL1471), DEOXYCHOLIC ACID (CHEMBL406393), OBETICHOLIC ACID (CHEMBL566315), CHOLIC ACID (CHEMBL205596), FIDAXOMICIN (CHEMBL1255800), VANCOMYCIN (CHEMBL262777), METRONIDAZOLE (CHEMBL137)",
      "data/processed/pubchem_phytochem_target_interactions.csv - 60,521 rows / 15,587 genes queried for the 31 CDI host targets; yielded the oleanolic acid TGR5, betulinic acid TGR5, celastrol Hsp90 and flavonoid barrier leads, and established the class-wide barrier/Wnt co-modulation problem"
    ],
    "negative_data_findings": [
      "BERBERINE: zero direct target-interaction rows (20 mentions, all CTD co-treatment annotations for other compounds); also absent from IMPPAT",
      "EBSELEN: absent from all project CSVs",
      "LITHOCHOLIC ACID: absent from all project CSVs",
      "DisGeNET: contains NO CDI data - the three disgenet files are OM-specific",
      "MLCK/MYLK #57: absent as MLCK, 8 rows as MYLK"
    ],
    "limitations": [
      "No CDI-specific pathway annotations exist in the knowledge graph; the C1-C8 axis decomposition is my construction from the Disease Brief, not a curated resource. A different decomposition would shift coverage counts, though probably not the gap ranking",
      "All concentration estimates are order-of-magnitude, shown as explicit arithmetic so downstream agents can attack the inputs",
      "Absence of a candidate from an axis indicates unreported activity, not proven inactivity - applies most to the C5/C6 columns for antibacterial candidates never assayed for host effects",
      "Every combination recommendation is a hypothesis about an untested interaction; each carries a named decisive experiment; none is a clinical recommendation"
    ]
  }
}
```

---

*Pathway Analyst — Phase 2, CDI drug discovery pipeline. Research analysis only; not clinical guidance.*
