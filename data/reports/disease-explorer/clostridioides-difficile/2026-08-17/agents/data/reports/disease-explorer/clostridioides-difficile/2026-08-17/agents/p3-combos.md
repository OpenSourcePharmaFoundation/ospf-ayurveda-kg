# Phase 3 — Combination Designer Report
## *Clostridioides difficile* Infection (CDI)

**Agent:** Combination Designer (final evaluation)
**Date:** 2026-08-18
**Skill file:** `.claude/skills/combination-designer/SKILL.md`
**Inputs:** `disease-model.md` (§2.10, §3.3, §3.4, §4.5, §4.6, §6, Appendix A.2) · `agents/p2-pathway.md` (C1–C8 axes, §5 coverage matrix, §6 combinations) · `debate-summary.md` · `agents/debate-integrator.md` §4–5 · `agents/p2-safety.md` §2, §9.1 · `agents/p1-clinical-landscape.md` §3, §5 · `agents/p2-repurposing.md` §4.9
**Project data independently queried:** `data/processed/chembl_approved_drugs.csv`, `data/processed/pubchem_phytochem_target_interactions.csv`

---

## 0. SKILL FILE ADAPTATION — what I changed and why

My skill file was written for Oral Mucositis: a **host-only, five-phase, self-limiting** injury in which combination design means stacking host-pathway inhibitors into a single oral rinse. CDI breaks four of its load-bearing assumptions.

| Skill-file assumption | Holds in CDI? | What I substituted |
|---|---|---|
| Combination = **concurrent co-formulation** (one rinse, one gel) | **No** | CDI's axes are *phase-bound and mutually hostile in time* — antibiotic and consortium cannot coexist. Combination design here is **sequencing design**. Every construction below is a timeline, not a formulation. |
| **Yogavahi / bioenhancer** (piperine-style absorption enhancement) is a synergy mechanism | **Inverted — it is a harm mechanism** | §6.2 states low absorption is a *feature*. A bioenhancer moves drug out of the compartment where it works into the compartment where it causes DDIs. **See §5.4 — this makes the classic berberine + piperine pairing actively contraindicated in CDI.** |
| Multi-pathway convergence on one outcome = synergy | Partly | In CDI the highest-value convergence is not "two routes to one node" but **one agent's failure mode being another agent's mechanism** (fidaxomicin leaves spores; anti-germinants act on spores). I promoted this to the primary synergy criterion. |
| "Cancer treatment supremacy" — don't compromise the primary therapy | **Reframed as microbiome supremacy** | The thing that must not be compromised is the **commensal community** and the **SOC antibiotic's luminal concentration**. Both are new failure modes with no OM analogue. |
| Ayurvedic multi-plant formulations get evaluated for rational polypharmacology | **Yes, retained** — but scored against §7.1's framing | Traditional medicine competes in CDI on microbiome modulation, host-directed anti-inflammation and anti-virulence — **not** antibacterial potency, and **not** antidiarrhoeal astringency (§5.4). |

**Retained unchanged:** target-overlap analysis, pathway coverage matrix, DDI checking, the additive/synergistic/potentiating/complementary/antagonistic taxonomy, the 2–4-component ceiling, and the "don't assume synergy" guardrail.

**One instruction I am following literally.** §4.5's synthesis ends: *"The pattern strongly suggests that combination or multi-mechanism approaches — not single-target monotherapy — are where the remaining value lies. This is a direct instruction to the Combination Designer agent."* And §3, clinical landscape: **add-on trials are 3-for-3; replacement trials are 0-for-3.** Every construction below is therefore an **adjunct to fidaxomicin**, scored on **recurrence through week 8**, on the ECOSPOR III template. Nothing here replaces standard of care.

---

## 1. THE DESIGN FRAME — the vulnerable window

Before proposing components, the design target has to be named. Every upstream report contains a piece of it; none states it as an object.

```
═══════════════════════════════════════════════════════════════════════════════
 THE VULNERABLE WINDOW — the interval every CDI combination is actually for
═══════════════════════════════════════════════════════════════════════════════

 d0            d10        d13     d14        d21          d28              wk 8
 ├──────────────┼──────────┼───────┼──────────┼────────────┼────────────────┤
 │◄ FIDAXOMICIN ►│         │       │          │            │                │
 │  C2 ██ C3 ██  │         │       │          │            │                │
 │  C8 ██ C7 spared        │       │          │            │                │
 │               │         │       │          │            │                │
 │               │◄════════ THE VULNERABLE WINDOW ════════►│                │
 │               │  Drug pressure OFF.  Ecology NOT YET BACK.               │
 │               │  Spore reservoir intact (§2.10 ESTABLISHED).             │
 │               │  Taurocholate still elevated — bai guild still absent.   │
 │               │  ▲ PEAK RECURRENCE HAZARD ▲                              │
 │               │         │       │          │            │                │
 │               │         │◄─ LBP dosed ─►   │            │                │
 │               │         │   engraftment lag ───────────►│ guild online   │
 │               │         │                               │ DCA/LCA return │
 │               │                                         │                │
 │               └── C1 and C7 are BOTH unoccupied here ────┘               │
 │                   THIS interval is the combination target.               │
═══════════════════════════════════════════════════════════════════════════════
```

**Why this is the right target, in four established facts:**

1. **Fidaxomicin's course ends at day 10** and its failure mode is stated in §2.10 as ESTABLISHED: *"spores are the recurrence reservoir and are unaffected by current antibiotics."* The moment dosing stops, C2/C3/C8 coverage goes to zero and the reservoir is still there.
2. **The ecological defence has not returned.** §2.8/C7: the `bai` guild is absent, so secondary bile acids (DCA/LCA #66 — the endogenous C1 *and* C2 inhibitor) are still collapsed and taurocholate — the germinant — is still accumulating. The patient's own anti-germination system is offline.
3. **Live biotherapeutics cannot be given earlier.** They are dosed after antibiotic washout (Rebyota 24–72 h, Vowst 2–4 days post-antibiotic ⚠️verify), and then need time to engraft. The product that fixes C7 is structurally incapable of covering the front of the window it is meant to close.
4. **The regulatory endpoint is recurrence through week 8** (ECOSPOR III / PUNCH CD3 / MODIFY I–II template, §3). Recurrence events accrue predominantly in this window. **The endpoint and the window are the same object.**

> **Design consequence.** The highest-value combination component in CDI is not "another agent" — it is a **bridge**: something that occupies **C1 (and ideally C8)** from the last dose of fidaxomicin until the consortium is demonstrably engrafted, and then gets out of the way. This reframes UDCA/CamSA from *maintenance therapy through week 12* (the Round 2 and integrator framing) to **a time-boxed bridge across days ~10–28**. That single change is the most consequential design decision in this report, and §2.5 below explains why the shorter course is not merely cheaper but **mechanistically safer**.

### 1.1 Five design rules I am imposing on every construction

| # | Rule | Source |
|---|---|---|
| **R1** | **Adjunct only.** Every component sits on top of fidaxomicin. No replacement designs. | §3 clinical landscape: add-on 3-for-3, replacement 0-for-3 |
| **R2** | **No second C2 agent.** C2 is served by six candidates and has buried eight programmes. Adding a seventh adds zero axes. | Pathway §5; integrator §2 |
| **R3** | **Sequential unless proven safe concurrent.** Antibiotic and consortium are directionally hostile; bile salts micellise poorly-soluble lipophiles. Concurrency must be *earned*, not assumed. | Pathway §6 risk note; integrator §4 |
| **R4** | **Preserve the commensal community.** A component that suppresses commensals to treat CDI is re-running vancomycin's mistake at a different dose. | §5.4 RESTORE direction; Pathway topology |
| **R5** | **Time-box every bridge to a measurable endpoint** (engraftment or bile-acid ratio normalisation), not to a fixed calendar date. | This report, §2.5 |

---

## 2. COMBINATION 1 — the immunocompetent flagship
# *Fidaxomicin → live biotherapeutic, with a C1-selective anti-germinant bridge*

```
═══════════════════════════════════════════════════════════════════════════════
COMBINATION DESIGN: "Bridged Handoff" — Combination A (immunocompetent)
═══════════════════════════════════════════════════════════════════════════════

COMPONENTS:
  1. FIDAXOMICIN 200 mg PO BID, d0–d10   — RNAP #1 inhibition; sub-MIC toxin
                                           suppression; sporulation inhibition
                                         — C2 ██ · C3 ██ · C8 ██ · C7 spared
                                         — ROLE: backbone / SOC (R1)

  2. VOWST (oral) or REBYOTA (rectal)     — `bai` guild reconstitution;
     or VE303 (8-strain, defined),          7α-dehydroxylation restored;
     dosed per label after washout          DCA/LCA #66 supply resumes
                                         — C7 ██ · C1 ▓▓ · C2 ▓▓ · C5 ▓▓ · C6 ▓▓
                                         — ROLE: primary anti-recurrence agent
                                                 (the only loop-EXITING component)

  3. ANTI-GERMINANT BRIDGE, d11 → engraftment confirmed (~d28)
     Near-term:  UDCA / ursodiol         — CspC #7 competitive antagonism
     Preferred:  CamSA (NCE)             — C1 ██ (CamSA) / C1 ██ C2 ▓▓ (UDCA)
                                         — ROLE: BRIDGE — covers C1 only while
                                                 the ecological C1 defence is
                                                 absent, then stands down
                                         — ⚠ OPTIONAL, NOT LOAD-BEARING (see
                                           §2.4 — the combination must survive
                                           the bridge being deleted)
═══════════════════════════════════════════════════════════════════════════════
```

### 2.1 Sequencing and dosing window

```
 d0 ─────────── d10 ── d13 ─────────── d21 ─────── d28 ──────────────── wk 8
 │◄ FIDAXOMICIN ►│                                                        │
 │               │◄ washout ►│                                            │
 │               │           │◄─── LBP per label ───►│ engrafting ────────│
 │               │◄════ BRIDGE (UDCA or CamSA) ════════════►│ STOP        │
 │               │                                          ▲             │
 │               │                             stop on engraftment marker,│
 │               │                             not on a calendar date (R5)│
 │                                                                        │
 │  PRIMARY ENDPOINT: recurrence through week 8 (ECOSPOR III template)    │
```

**Never concurrent with fidaxomicin.** Two independent arguments converge on this, and they were derived separately:
- **Physicochemical (Pathway §6, cross-cutting finding 6):** bile salts are solubilising agents; fidaxomicin is MW **1058.05** (`chembl_approved_drugs.csv`) and very poorly soluble, with efficacy dependent on high *luminal* concentration. Co-dosed UDCA could micellise it, raising the absorbed fraction and lowering luminal exposure. This is a direct attack on the backbone.
- **Pharmacodynamic (Pathway §2.3):** UDCA's weakness is diarrhoeal transit and dilution. During the acute episode that weakness is maximal; after resolution it is minimal. Deploying the bridge *after* fidaxomicin dodges the bridge's own worst PK liability.

The two arguments agree, so this is not a close call. **Sequential.**

### 2.2 Combination type and synergy mechanism

**Type: Complementary + Sequential, with a self-tapering handoff.**

**Mechanism 1 — failure-mode complementarity (the strongest form of combination rationale).**
Fidaxomicin's single acknowledged failure mode is that spores survive. The bridge's entire mechanism is that surviving spores cannot germinate. One agent's failure mode *is* the other's mechanism of action. This is not additive; it is the closure of a specific, named hole.

**Mechanism 2 — the reservoir is made static before the bridge has to hold it.**
§2.3 asks whether an anti-germinant can hold against "a continuously replenished spore load." Fidaxomicin answers that question in the bridge's favour: by clearing vegetative cells (C2) and suppressing *new* sporulation (C8), it converts the reservoir from **growing** to **static**. The bridge therefore faces the easiest version of its own problem. Order matters — the reverse sequence would not work.

**Mechanism 3 — the self-tapering handoff (from Pathway §6, and the reason the bridge can be time-boxed).**
As the consortium re-establishes the `bai` guild, that guild begins converting UDCA → LCA — and LCA is itself a C1 germination inhibitor *and* a C2 growth inhibitor. **The bridge drug is consumed exactly as the endogenous mechanism it substitutes for comes back online, and its metabolite is on-mechanism.** There is no wean-off cliff. Pharmacology hands off to ecology.

> **My addition to Mechanism 3.** If the handoff is real, then continued dosing past engraftment is not neutral — it is *pointless drug exposure carrying live risk* (the diarrhoea AE that mimics the primary endpoint, §9.1 safety). The handoff argument, taken seriously, **implies** the time-boxed bridge rather than week-12 maintenance. Round 2 and the integrator both drew the timeline to week 12; the biology they cited argues for stopping earlier. **Stop the bridge on an engraftment or bile-acid-ratio marker (R5).**

### 2.3 The engraftment-antagonism risk — and the design fix nobody has proposed

This is the one genuine antagonism risk in Combination A, and Pathway named it correctly: *"Does high luminal UDCA suppress the engrafting consortium?"* DCA/LCA broadly inhibit Clostridia; VE303's eight strains and Vowst's spore population are not uniformly bile-tolerant. If UDCA blocks engraftment, **the combination inverts from synergistic to antagonistic** — and it would do so against the component that is actually doing the work.

**The design fix follows from separating C1 from C2 activity.** Look at the coverage matrix rows:

```
                    C1 (germination)   C2 (fitness/growth)
  UDCA                  ██                 ▓▓   ◄── the ▓▓ is the problem
  CamSA                 ██                 ░░   ◄── C1-selective by design
  DCA / LCA             ██                 ██   ◄── worst possible bridge
```

**The antagonism risk is carried entirely by the C2 column, not the C1 column.** Germination antagonism is a *receptor-occupancy* event at CspC #7 on *C. difficile* spores — commensal Lachnospiraceae and Ruminococcaceae do not germinate through CspC and are not affected by a competitive antagonist at that site. Growth inhibition is a *general anti-Clostridial* effect and hits the engrafting consortium directly. UDCA has both; CamSA, as a cholate-core CspC-site antagonist with a bulky C24 aryl sulfonamide, has essentially only the first.

> **Design conclusion.** **CamSA is the mechanistically correct bridge partner for a live biotherapeutic and UDCA is not** — precisely because CamSA is the *weaker* agent on C2. This is a case where reduced polypharmacology is the desired property, which inverts the usual combination-design instinct. It is also the strongest non-obvious argument for funding the CamSA programme that this analysis has produced, and it is independent of CamSA's ~1000× potency advantage.
>
> **But CamSA is an NCE** (integrator rank #3, 6.3, heavy time penalty). So the near-term Combination A uses UDCA if it uses a bridge at all, and carries the antagonism risk as a **gate**, not an assumption.

### 2.4 The bridge is optional — and that is a feature

Per the integrator: *"the LBP is the primary agent; UDCA is optional, not load-bearing. This matters, because it means Combination A does not fail if Stage 0 kills UDCA."* I endorse this without qualification and would go further: **Combination A's base case is fidaxomicin → LBP, full stop.** That construction is already 4 axes (C2 + C3 + C7 + C8, with C1 partial via restored DCA/LCA), already approved end-to-end, and already has an approval-grade precedent.

The bridge is a **randomised add-on arm**, not a required component. Trial design: fidaxomicin → LBP ± bridge, recurrence at week 8. The add-on arm answers the engraftment-antagonism question and the efficacy question on the same patients. If the bridge arm underperforms the LBP-alone arm, that is the antagonism result — read directly off the primary endpoint.

### 2.5 Pathway coverage

```
┌──────────────────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬──────┐
│ Component            │ C1  │ C2  │ C3  │ C4  │ C5  │ C6  │ C7  │ C8  │ Axes │
├──────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──────┤
│ Fidaxomicin d0–10    │ ░░  │ ██  │ ██  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ██  │ 3.5  │
│ VOWST/REBYOTA/VE303  │ ▓▓  │ ▓▓  │ ░░  │ ░░  │ ▓▓  │ ▓▓  │ ██  │ ░░  │ 3.0  │
│ Bridge: UDCA         │ ██  │ ▓▓  │ ░░  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ░░  │ 2.0  │
│  └ or CamSA (pref.)  │ ██  │ ░░  │ ░░  │ ░░  │ ░░  │ ░░  │ ░░  │ ░░  │ 1.0  │
│  └ or TUDCA (§6.3)   │ ██  │ ▓▓  │ ░░  │ ░░  │ ▓▓  │ ▓▓  │ ▓▓  │ ░░  │ 3.5  │
├──────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──────┤
│ COMBINED (UDCA)      │ ██  │ ██  │ ██  │ ░░  │ ▓▓  │ ▓▓  │ ██  │ ██  │ 6.0  │
│ COMBINED (no bridge) │ ▓▓  │ ██  │ ██  │ ░░  │ ▓▓  │ ▓▓  │ ██  │ ██  │ 5.0  │
└──────────────────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴──────┘
   GAPS: C4 (intoxication — empty since bezlotoxumab's Jan-2025 withdrawal)
         C6 (barrier/repair — LBP touches it only indirectly)
```

**6.0 axes with the bridge; 5.0 without.** Both are the highest coverage available from approved or Phase-3 agents. Critically, **C7 is covered strongly** — the only axis whose repair *exits* the recurrence loop rather than suppressing within it.

### 2.6 Risk assessment

| Risk | Severity | Mechanism | Mitigation / gate |
|---|---|---|---|
| **Bridge suppresses consortium engraftment** | **HIGH — combination-inverting** | UDCA's C2 activity is anti-Clostridial; engrafting strains may not be bile-tolerant | **Gate on the engraftment ± UDCA experiment (§9, Exp. C-1).** Default to no bridge until it reads out. CamSA structurally avoids this. |
| **Bile-salt micellisation of fidaxomicin** | Moderate | Bile salts solubilise poorly-soluble lipophiles; fidaxomicin MW 1058, luminal-dependent | **Sequential dosing only.** Never co-administer. Already required by R3. |
| **UDCA dose escalation to reach colonic concentration** | **HIGH if mishandled** | Colonic exposure may require supra-PBC dosing; the PSC trial at 28–30 mg/kg/d was **terminated early for excess death and transplant** (Lindor 2009) | **Colon-targeted formulation, not dose escalation.** Safety §9.1 is explicit that this is a *safety* requirement, not a PK optimisation. Any protocol that escalates systemic dose is disqualified. |
| **Diarrhoea AE mimics the primary endpoint** | Moderate — biases toward false negative | UDCA's commonest AE (~2–9%) is dose-related diarrhoea; the endpoint is recurrent diarrhoea | Adjudicate recurrence by toxin/PCR positivity, not symptoms alone. **Time-boxing the bridge shortens the exposure window and reduces this bias.** |
| **Sub-inhibitory bile-acid biofilm induction** | Low–Moderate | §2.4b — biofilm induction if bridge exposure lands low | Argues against under-dosing; interacts with the formulation requirement above |
| **Warfarin INR destabilisation** | Moderate, population-wide | §3.3 — microbiome shifts alter vitamin K₂ production; this applies to the **LBP**, not the bridge | INR monitoring through the engraftment window. Applies to LBP therapy generally, not specific to this construction. |
| **Commercial fragility of the LBP category** | Moderate — non-scientific | Vowst divested at a distressed valuation ⚠️verify; CP101 discontinued for financing | Programme-level, not patient-level. Route to Clinical Feasibility. |

**Directional conflicts: NONE.** No component degrades an axis another component repairs. **DDI: LOW.** Fidaxomicin and OP-1118 are P-gp substrates but the label requires no adjustment; sequential dosing removes the physicochemical interaction; UDCA is not a meaningful CYP perturbant.

### 2.7 Verdict

**RECOMMENDED as the base case (fidaxomicin → LBP), with the bridge as a gated add-on arm.**
**Confidence: Moderate–High** on the two-component base case (every element approved or Phase 3, with an approval-grade precedent). **Moderate–Low** on the bridge, which rests on an unmeasured antagonism question and an unmeasured UDCA IC₅₀.

---

## 3. COMBINATION 2 — the strategically important one
# *Fidaxomicin → anti-germinant bridge, no live organisms* (immunocompromised)

```
═══════════════════════════════════════════════════════════════════════════════
COMBINATION DESIGN: "Dry Bridge" — Combination B (immunocompromised)
═══════════════════════════════════════════════════════════════════════════════

COMPONENTS:
  1. FIDAXOMICIN 200 mg PO BID, d0–d10   — C2 ██ · C3 ██ · C8 ██
                                         — ROLE: backbone / SOC

  2. ANTI-GERMINANT, d11 → week 12       — CspC #7 competitive antagonism
     Near-term:  UDCA (colon-targeted)     THE reservoir-suppressing component
     Preferred:  CamSA (NCE)             — C1 ██
                                         — ROLE: PRIMARY anti-recurrence agent
                                           ⚠ LOAD-BEARING here, unlike Comb. A

  3. [SECOND-GENERATION, optional]        — oral TcdB-directed IgY
     oral TcdB-IgY                        — C4 ██ (luminal toxin neutralisation)
                                         — ROLE: replaces the withdrawn C4 agent
                                           ⚠ must be re-specified TcdB-directed;
                                             all existing IgY work is anti-TcdA,
                                             the arm that FAILED (actoxumab)

  EXPLICITLY EXCLUDED: all live biotherapeutics, all probiotics, FMT
═══════════════════════════════════════════════════════════════════════════════
```

### 3.1 Why this is the flagship, not Combination A

**Combination A serves a population that already has three approved options. Combination B serves a population that has none.**

§4.6 ranks unmet needs, and **#1 is: "Prevent recurrence without requiring live biotherapeutics — usable in immunocompromised and transplant patients, who are currently the least served. Highest-value target profile."** §3.4 is blunter: this group is *"arguably the most underserved sub-group in CDI"* — excluded from or poorly served by every new therapy, because live biotherapeutics and probiotics carry bacteraemia/fungaemia risk in exactly the patients who cannot clear an organism. The PLACIDE-era probiotic literature contains reported fungaemia in immunocompromised patients; this is not theoretical.

**The Round 2 flagship failed the flagship unmet need**, as the integrator found: its live-biotherapeutic arm excludes the population §4.6 ranks first. Combination B is the correction.

### 3.2 The design property that makes B *easier* than A, not harder

This is counterintuitive and worth stating plainly.

**Combination A's single biggest risk — does the bile acid suppress the engrafting consortium? — does not exist in Combination B.** There is no consortium. The antagonism question is moot in exactly the population where the anti-germinant matters most.

```
   COMBINATION A                          COMBINATION B
   ┌────────────────────────┐             ┌────────────────────────┐
   │ UDCA ──┐               │             │ UDCA ────► C1 block    │
   │        ├─► C1 block ✔  │             │                        │
   │        └─► C2 ─────────┼─► may       │  (no consortium to     │
   │            anti-       │   SUPPRESS  │   suppress — the C2    │
   │            Clostridial │   the LBP ✘ │   activity is free)    │
   └────────────────────────┘             └────────────────────────┘
     UDCA's C2 activity is a LIABILITY      UDCA's C2 activity is
     (it fights the primary agent)          HARMLESS, even helpful
```

**The same molecular property — partial anti-Clostridial C2 activity — is a liability in A and an asset in B.** That is a real, non-obvious combination-design finding: UDCA is a *better* fit for the harder population. It also means the two combinations should not be developed as one programme with a subgroup; they have different risk structures and different gating experiments.

### 3.3 Sequencing and dosing window

```
 d0 ─────────── d10 ─────────────────────────────────────────────── wk 12
 │◄ FIDAXOMICIN ►│
 │               │◄════ ANTI-GERMINANT (UDCA colon-targeted / CamSA) ══════►│
 │               │
 │               │◄════ [Gen-2] oral TcdB-IgY, TID with meals ═════════════►│
 │
 │  Bridge runs FULL DURATION here — not time-boxed.
 │  Rationale: in Combination A the bridge hands off to a returning `bai`
 │  guild. In an immunocompromised patient on continuing immunosuppression
 │  and often continuing antibiotics, THAT GUILD MAY NEVER RETURN.
 │  There is nothing to hand off to. The self-tapering argument does not
 │  apply, so the anti-germinant is chronic suppression, not a bridge.
 │
 │  PRIMARY ENDPOINT: recurrence through week 8–12
```

> **This is the sharpest divergence between the two combinations, and it falls out of the handoff logic.** The self-tapering mechanism (§2.2, Mechanism 3) is what licenses stopping the drug in Combination A. In Combination B that mechanism is absent by construction. **Same molecule, same dose, opposite duration logic** — because the ecological context differs, not because the pharmacology differs. Any protocol that copies A's duration into B has misunderstood why A's duration is short.

**Consequence to flag honestly:** chronic dosing raises the cumulative exposure to UDCA's dose-related diarrhoea AE, in the population where distinguishing AE from recurrence matters most. This strengthens — does not weaken — the case that **colon-targeted formulation is mandatory here**, and it strengthens the case for CamSA, whose sulfonate guarantees luminal confinement structurally rather than by formulation.

### 3.4 Pathway coverage

```
┌──────────────────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬──────┐
│ Component            │ C1  │ C2  │ C3  │ C4  │ C5  │ C6  │ C7  │ C8  │ Axes │
├──────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──────┤
│ Fidaxomicin d0–10    │ ░░  │ ██  │ ██  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ██  │ 3.5  │
│ UDCA or CamSA        │ ██  │ ▓▓  │ ░░  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ░░  │ 2.0  │
│ [Gen-2] oral TcdB-IgY│ ░░  │ ░░  │ ░░  │ ██  │ ▓▓  │ ▓▓  │ ░░  │ ░░  │ 1.5  │
├──────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼──────┤
│ COMBINED (core)      │ ██  │ ██  │ ██  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ██  │ 4.5  │
│ COMBINED (+ IgY)     │ ██  │ ██  │ ██  │ ██  │ ▓▓  │ ▓▓  │ ▓▓  │ ██  │ 6.0  │
└──────────────────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴──────┘
   RESIDUAL GAP — stated plainly: C7 is NOT covered.
```

**On the C7 gap, which I will not paper over.** Combination B suppresses the loop; it does not exit it. C7 restoration currently requires living organisms, and living organisms are the one thing this population cannot have. There is no small molecule that restores the `bai` guild — Pathway §5 states this and my own query of `pubchem_phytochem_target_interactions.csv` found no candidate for it either. Direct secondary-bile-acid replacement (DCA/LCA supplementation) is not a serious proposal: those are the compounds whose colonic accumulation carries the long-standing carcinogenicity literature, and dosing them chronically in an immunosuppressed patient is not a trade anyone should make on current evidence.

**So the honest statement is: Combination B holds the loop open indefinitely rather than closing it.** For a transplant patient on continuing immunosuppression, indefinite suppression may in fact be the correct therapeutic goal — this is the model used for other opportunistic infections in this population. But it should be *chosen*, not backed into. **The pharmacological, non-live C7 agent remains the widest genuine white space in CDI, and this report does not fill it.**

**On the IgY arm — a caution the ranking already contains.** Oral TcdB-IgY sits at 4.0 post-debate: the modality is validated (bezlotoxumab proved luminal/systemic TcdB neutralisation works clinically) but the evidence base does not exist, and the one trial (n=38) terminated for sponsor bankruptcy and was numerically inferior to metronidazole. **Critically: all existing IgY work is anti-TcdA** — the arm that actoxumab proved does not work and *increased mortality as monotherapy* (§4.5). Any IgY programme entering here must be **re-specified as TcdB-directed from the antigen up**. Treating existing anti-TcdA IgY data as supportive would be re-running a known failure. This is why I place it as a second-generation option, not a core component.

### 3.5 Risk assessment

| Risk | Severity | Mechanism | Mitigation / gate |
|---|---|---|---|
| **Can any anti-germinant hold a spore reservoir?** | **HIGH — class-level, kills the whole construction** | Unanswered class question (§2.3, integrator §7). UDCA, CamSA, chenodiol and urso-CamSA **all die together** if the answer is no | The single largest uncertainty behind Combination B. **Nothing in the analysis addresses it.** Requires a dedicated design — see §9, Exp. C-3 |
| **UDCA IC₅₀ vs achievable colonic concentration** | **HIGH** | The first-ever UDCA IC₅₀ has not been measured; §2.3's estimate compares a concentration to a threshold that does not exist | Bile-acid germination dose-response (integrator Exp. 4). **Must precede any Stage 0 decision** |
| **UDCA : taurocholate ratio, not absolute concentration** | **HIGH** | C1 inhibition is *competitive* — efficacy depends on the molar ratio at CspC. UDCA is a weak FXR ligand; sustained dosing could dilute CDCA's share, relieve FXR feedback repression and **expand the taurocholate pool** | Pathway §2.4a's decisive measurement: fecal UDCA : taurocholate molar ratio on therapy in dysbiotic subjects. **If the ratio does not move favourably, UDCA fails at any dose.** CamSA, as a non-FXR-engaging antagonist, does not carry this risk |
| **Chronic dosing → diarrhoea AE burden** | Moderate | Dose-related, ~2–9%; endpoint confound | Colon-targeted formulation mandatory; toxin-confirmed endpoint adjudication |
| **Continuing antibiotics / immunosuppression** | Moderate | This population often remains on the precipitating antibiotic; C7 never recovers | Argues for the chronic duration in §3.3. Also makes this population a natural **co-indication for ribaxamase** (Combination C) |
| **IgY: wrong antigen** | **HIGH if unmanaged** | All existing work is anti-TcdA — the failed arm | Hard requirement: TcdB-directed antigen. Do not credit anti-TcdA precedent |
| **IgY: gastric/proteolytic survival** | Moderate | Oral antibody must survive stomach and pancreatic proteases to reach the colon | Enteric formulation; this is a solved-in-principle problem but unsolved for this product |

**Directional conflicts: NONE. DDI: LOW — and this is a load-bearing property.** §3.4's immunocompromised population is on tacrolimus and cyclosporine, narrow-TI dual CYP3A4/P-gp substrates. Neither UDCA nor CamSA meaningfully perturbs intestinal P-gp or enterocyte CYP3A4. **This is precisely where berberine is disqualified** (§5.1) and it is the reason the bile-acid chemotype, not the alkaloid chemotype, wins this population.

### 3.6 Verdict

**RECOMMENDED as the strategically differentiated programme — with the honest caveat that its core efficacy premise (that an anti-germinant can hold a spore reservoir) is unproven at the class level.**

**Confidence: Moderate on the design logic; Low–Moderate on the efficacy premise.** The construction is right — it is the only one serving §4.6's #1 unmet need, it has no directional conflicts, it has a near-empty DDI surface in a polypharmacy population, and its principal risk in Combination A vanishes here. What it lacks is any demonstration that the mechanism produces durable clinical benefit, which §2.10 lists under **UNCERTAIN/DISPUTED**: *"whether anti-germinants can achieve durable clinical benefit."* That is the gate.

---

## 4. COMBINATION 3 — primary prevention
# *Ribaxamase during IV β-lactam therapy* (+ the class-coverage problem)

```
═══════════════════════════════════════════════════════════════════════════════
COMBINATION DESIGN: "Shield" — Combination C (primary prevention)
═══════════════════════════════════════════════════════════════════════════════

COMPONENTS:
  1. IV β-LACTAM (the precipitating therapy — ceftriaxone, cefepime,
     pip-tazo, carbapenem)                — the thing being protected against
                                          — NOT a therapeutic component

  2. RIBAXAMASE (SYN-004) PO, delayed-release, TID,
     for the duration of β-lactam therapy + short tail
                                          — oral β-lactamase; degrades residual
                                            β-lactam in the intestinal lumen
                                            BEFORE it destroys the microbiota
                                          — C7 ██ (SHIELD direction, #70)
                                          — ROLE: prevents LOOP ENTRY

  ⚠ NOT a combination in the usual sense: it is the only intervention that
    operates BEFORE the disease. Orthogonal to A and B, compatible with both.
═══════════════════════════════════════════════════════════════════════════════
```

### 4.1 Why this sits in a combination report at all

Combinations A and B both operate *inside* the recurrence loop. Pathway §1 identifies exactly three entry points to that loop, and only one of them prevents entry:

```
   #70 luminal antibiotic inactivation ──► PREVENTS loop entry      ◄── Comb. C
   #64/#69 ecological restoration      ──► EXITS the loop           ◄── Comb. A
   C1 germination + C8 sporulation     ──► HOLDS the loop open      ◄── Comb. B
       block                                (suppression, not cure)
```

**Combination C is the only construction in this analysis that keeps the patient from ever needing A or B.** It is also the only asset in the pipeline with **positive human Phase 2b data** — every other non-approved candidate's best evidence is rodent.

### 4.2 Why it escapes the failure modes that killed the field

| Field-wide failure mode | Combination C's exposure |
|---|---|
| Initial-cure non-inferiority bar (killed 8 programmes) | **Escapes entirely** — never competes on cure. Endpoint is **new-onset CDI incidence** |
| Sustained-response endpoint (strongest negative correlate of preclinical→clinical translation) | **Escapes** — endpoint is incidence, not sustained response |
| Diarrhoea-endpoint confound (afflicts every bile acid) | **Escapes** — a luminal enzyme has no such axis |
| 36% preclinical translation rate | **Largely escapes** — evidence is already human Phase 2b |
| Directional conflict with SOC | **None** — ribaxamase is a **β-lactamase**; it does not touch glycopeptides or macrocycles, so it is chemically incapable of degrading vancomycin or fidaxomicin |

That last row is a combination-compatibility fact worth stating explicitly, because it does **not** generalise across the #70 class — see §4.3.

### 4.3 The class-coverage gap, and the complementary asset

Ribaxamase has a hard ceiling the integrator named: **it only prevents β-lactam-driven CDI.** Fluoroquinolone- and clindamycin-driven CDI — both major precipitants per §3.3 — are untouched, because there is no enzyme to degrade them. Nobody in this pipeline quantified that fraction of the addressable population, and it should be quantified before any acquisition closes.

**The complementary asset within the same axis is DAV132** — an activated-charcoal colonic adsorbent, which is **antibiotic-class-agnostic** because it works by adsorption rather than catalysis.

```
   #70 / C7 SHIELD AXIS — two mechanisms, complementary coverage
   ┌────────────────────────────────────────────────────────────────┐
   │ RIBAXAMASE (enzyme, catalytic)  │ DAV132 (adsorbent, physical)  │
   │  ✔ β-lactams                    │  ✔ β-lactams                  │
   │  ✘ fluoroquinolones             │  ✔ fluoroquinolones           │
   │  ✘ clindamycin                  │  ✔ clindamycin                │
   │  ✔ compatible with oral vanco / │  ✘ WOULD ADSORB oral vanco /  │
   │    fidaxomicin                  │    fidaxomicin — see below    │
   └────────────────────────────────────────────────────────────────┘
     SELECT BY REGIMEN. DO NOT STACK — same axis, zero added coverage.
```

> **⚠ NEW AVOID-LIST ENTRY (not in any prior report): DAV132 or any colonic adsorbent co-administered with oral vancomycin or fidaxomicin.** An adsorbent that non-selectively binds luminal antibiotic will bind the *therapeutic* luminal antibiotic too — directly attacking the backbone's mechanism, which depends entirely on high luminal concentration. There is precedent for exactly this class of interaction: `p2-safety.md` §L2 cites **cholestyramine binding vancomycin** as a known gut-wall interaction. **Ribaxamase does not have this problem and DAV132 does. That is a decisive selection criterion between the two assets if either is ever to be combined with CDI treatment rather than used purely prophylactically.**

### 4.4 Risk assessment

| Risk | Severity | Note |
|---|---|---|
| **Phase 2b data unverified by anyone in this pipeline** | **HIGH** | The integrator's #1 recommendation rests on it. Gated on a $150–300K diligence pass — which is the honest form of the recommendation |
| **Acquisition, not repurposing** | High (commercial) | No RLD, no 505(b)(2) path; BLA for an enzyme biologic with harder CMC than any small molecule here |
| **β-lactam-only ceiling** | **High and unquantified** | See §4.3. Quantify the β-lactam-attributable fraction of hospital-onset CDI before closing |
| **Prevention Phase 3s are large and expensive** | High | Must enrol many at-risk patients to accrue events; $80–150M estimate excludes acquisition and is probably optimistic |
| **Payer logic for prophylaxis** | High | Paying for an event that does not happen is a genuinely hard sell |
| **Degrades the therapeutic β-lactam?** | **Low — but must be measured** | The whole premise is that IV β-lactam reaches its systemic target before biliary excretion delivers residue to the gut. Phase 2b reportedly showed no loss of systemic β-lactam efficacy ⚠️verify — this is a diligence item, not an assumption |

### 4.5 Verdict

**RECOMMENDED as the highest-expected-value programme, gated on diligence** — consistent with the integrator's §5. From a combination-design seat specifically, its distinguishing property is that **it is orthogonal to everything else in this report**: it can be layered onto any patient's regimen without a single directional conflict, because it acts on a different compartment (the precipitating antibiotic) at a different time (before disease).

**Confidence: Low–Moderate on the specifics** (the Phase 2b package is unverified) **/ High on the strategic logic.**

---

## 5. DESIGNED AND REJECTED — combinations that do not survive their own timeline

This section exists because rejecting a construction for a *specific, stated* reason is more useful than omitting it silently.

### 5.1 Berberine + fidaxomicin — **the no-clean-window problem**

The integrator kept berberine alive at 5.5, corrected the fabricated toxin-induction claim, and specified: pair with fidaxomicin, **not** vancomycin (the ½-MIC biofilm signal, p=0.02, is specific to the vancomycin pair). It also excluded berberine from active Phase 4 disease on the Wnt/anti-proliferative concern. Both constraints are correct. **When you apply them as a timeline rather than as a list, they close on each other.**

```
 d0 ──────────── d10 ─────── d14 ──────── d21 ──────── d28 ─────────── wk 8
 │◄ FIDAXOMICIN ►│
 │                                                                      │
 │   ACUTE / PHASE 4 (ulceration)     │   RECOVERY / REPAIR             │
 │   ├─ berberine EXCLUDED here ──────┤                                 │
 │   │  (Wnt liability in active      │                                 │
 │   │   ulcerative disease)          │                                 │
 │   │                                │                                 │
 │   │                                ├─ berberine's C5 window opens... │
 │   │                                │  ...but crypt REGENERATION is   │
 │   │                                │  Wnt/β-catenin-DEPENDENT, and   │
 │   │                                │  that is exactly what berberine │
 │   │                                │  suppresses.  ◄── CONFLICT      │
 │   └────────────────────────────────┴─────────────────────────────────┘
 │        excluded by the Wnt risk        the Wnt risk is MAXIMAL here
```

> **The finding: berberine's permitted window and its liability window are the same window.** The exclusion in active disease is meant to protect C6 during ulceration. But C6's repair requirement does not end when ulceration ends — §2.9 and Pathway §5 describe TcdB-FZD-mediated Wnt blockade as *"an independent injury axis"* and the reason **"the mucosa stays broken after toxin clears."* Crypt stem cell renewal in the recovery phase is Wnt-dependent by definition. So the interval in which berberine's C5 anti-inflammatory contribution would be welcome is the interval in which its anti-proliferative Wnt activity does the most harm. **There is no clean window, and this only becomes visible when the constraints are drawn on a timeline instead of listed.**

**Three further disqualifiers in the specific populations that matter:**
1. **The transplant contradiction (safety §2.7).** Berberine 0.2 g TID raised cyclosporine trough ~29% and AUC ~35% *in renal transplant recipients* — human data, not theoretical. Tacrolimus, being dual CYP3A4/P-gp-limited with lower and more variable F, should behave the same or worse. This is a **contraindication, not a monitoring problem**, because the perturbation is superimposed on the resolving-diarrhoea confounder — troughs would chase two moving inputs. **So berberine is excluded from Combination B's population**, which is the only population where a non-live luminal agent is differentiating. Its differentiation story and its safety profile point in opposite directions.
2. **The DDI is amplified, not removed, by non-absorption** (safety §L2). Berberine acts on intestinal P-gp/CYP3A4 in the *proximal* small bowel — in transit, not at its site of action. Luminal confinement makes this worse, not better. It is formulation-addressable in principle (colon-targeted delivery bypasses the high-CYP3A4 zone), but PPI use (40–60% of this population) and dysbiosis defeat the two commonest colonic-release trigger mechanisms.
3. **Zero project-data support — verified, not assumed.** I queried `pubchem_phytochem_target_interactions.csv` directly: berberine returns **20 matching rows, and not one is a berberine target record.** Every hit is a co-treatment mention inside *another* compound's evidence string (e.g. `[berberine co-treated with niacinamide] results in decreased expression of SIRT1`, PMID:26712469). **Berberine has no direct target rows in this project's data.** Its entire network profile is recall — which is exactly what Pathway §9 stated, and which I can now confirm independently rather than repeat.

**Verdict: NOT RECOMMENDED for any construction in this report.** Not because the pharmacology is absent — the C5 anti-inflammatory activity and the #72 enterococcal cross-feed effect are real and interesting — but because **it has no window and no population.** If the spo0A disconfirmation experiment (integrator Exp. 6) and a colonic-organoid regeneration assay (± TcdB) both came back clean, it could re-enter. Both are needed; either alone is insufficient.

### 5.2 Fidaxomicin + bezlotoxumab + anti-germinant — **obsoleted by withdrawal**

Pathway §6 proposed this as the maximum-approved-agent construction (5 axes, adding the mechanistically complete C4 agent). **Merck discontinued bezlotoxumab in January 2025.** The construction is not wrong; it is unavailable. Its loss is what emptied C4, and C4 is now white space rather than a covered axis — which is precisely why Combination B's second-generation oral TcdB-IgY arm has a strategic rationale it would not have had eighteen months ago.

### 5.3 Any second C2 agent added to fidaxomicin — **zero added coverage**

Ibezapolstat, ridinilazole-class, niclosamide's antibacterial arm: all land on C2, where six of ten candidates already sit and **eight programmes have failed** (ridinilazole, surotomycin, cadazolid, LFF571, DS-2969b, OPS-2071, ramoplanin, Ramizol). Adding one adds no axes and inherits the initial-cure non-inferiority bar that killed all eight. **R2 rejects these by rule, not by case-by-case analysis** — which is the point of having the rule.

### 5.4 Traditional-medicine constructions that do NOT translate — two principle inversions

My skill file maps Ayurvedic combination principles onto modern pharmacology. Two of those mappings **invert** in CDI, and both inversions produce actively harmful designs. This is a genuine contribution of the traditional-medicine lens, arrived at by taking the principles seriously rather than by discarding them.

| Ayurvedic principle | Skill-file mapping | **What it does in CDI** |
|---|---|---|
| **Yogavahi** (carrier / bioenhancer — piperine + curcumin, piperine + berberine) | "CYP/P-gp inhibition, absorption enhancement" — a synergy mechanism | **⚠ HARM.** §6.2 inverts the bioavailability logic: for a luminal candidate, absorption *removes drug from the compartment where it works* and *delivers it into a dense polypharmacy environment* in a renally- and hepatically-impaired elderly population. **Piperine + berberine — a classic pairing — is doubly contraindicated here**: it raises systemic berberine exposure *and* piperine is itself a CYP3A4/P-gp inhibitor, stacking a third same-direction perturbation onto tacrolimus. **NEW AVOID-LIST ENTRY.** |
| **Grahi / Stambhana** (astringent, binding, transit-slowing — the classical approach to *atisara*/diarrhoea) | "Symptomatic control" | **⚠ HARM.** §3.3 and §3.4: **antimotility agents are relatively contraindicated in CDI** — slowing transit prolongs toxin contact time and risks **toxic megacolon**. The entire classical antidiarrhoeal category is pharmacologically antimotility-like and is disqualified *by the mechanism that makes it traditionally effective*. **NEW AVOID-LIST ENTRY.** |

| Ayurvedic principle | Skill-file mapping | **What it does in CDI** |
|---|---|---|
| **Prativisha** (mutual antagonism of toxicity) | Toxicity mitigation | **Translates cleanly, and Combination C is an instance of it** — ribaxamase is literally an agent that destroys the harmful residue of another agent while preserving its intended action. A 21st-century enzyme is doing exactly what the principle describes. |
| **Vijatiya dravya** (different-class combination) | Multi-pathway complementary effect | **Translates cleanly** — Combinations A and B are both vijatiya constructions: antibacterial + bile acid + (ecology or antibody), three different classes on three different axes. |
| **Sajatiya dravya** (same-class combination) | Same-pathway additive | **Rejected by R2** — same-class stacking on C2 is exactly the failure mode. |

> **Where traditional medicine actually competes in CDI (§7.1): microbiome modulation, host-directed anti-inflammation, anti-virulence — not antibacterial potency and not astringency.** By that standard, the strongest traditional-medicine-derived leads in this analysis are **not** berberine. They are the TGR5 (#62/GPBAR1) agonist triterpenes, and my own query of `pubchem_phytochem_target_interactions.csv` confirms the rows exist: **oleanolic acid → GPBAR1, 4 rows, full agonist** (PMID:17825251; binding PMID:23022524, 23041323) — corroborating the Ethnobotany agent's *Cyperus rotundus* lead with actual project data. ⚠️ **The same file shows oleanolic acid inhibits IL22 (PMID:26513295) — the wrong direction for #47, which is AGONIZE.** Mixed-direction lead; both arms need testing before it enters any construction. Not ready for a combination in this report, but it is the right place to look next, and it is the only traditional-medicine lead here with data-backed C7/C5 activity in the correct direction on at least one arm.

---

## 6. THE FULL AVOID LIST — carried forward and extended

Entries marked **NEW** are contributed by this report; the remainder are carried from Pathway §6 and the integrator §4 and are restated so this document stands alone.

| Combination | Why it fails | Source |
|---|---|---|
| **Ebselen + anything** | Selenium 290–575× UL; activity abolished by 5% blood; no recognition element; shares a redox-fragile failure mode with niclosamide (**correlated** risk — the opposite of what combination design is for) | Debate; Pathway §4 |
| **Ebselen + bezlotoxumab** | Redundant on C4, and ebselen covers strictly *less* of it (misses the receptor-binding NOX1 necrosis arm). Pays twice for one axis, and the cheaper component is the incomplete one | Pathway §6 |
| **Ebselen + any Stickland / nutrient-depletion agent** | Compounds the `tcdR` de-repression hazard — two agents both imposing nutrient limitation on an organism whose toxin genes are de-repressed *by* nutrient limitation | Pathway §4.2 |
| **Vancomycin + any C7 restoration agent** | Direct directional conflict — vancomycin's mechanism of harm *is* C7 destruction; it sterilises the consortium it is co-dosed with | Pathway §6 |
| **Berberine + vancomycin** | ⚑ The specific pair with the biofilm signal (½ MIC, p=0.02) — and it is the pair the mouse data supports. If berberine is combined at all, pair with fidaxomicin | Integrator §4 |
| **Berberine in active Phase 4 disease** | Wnt/anti-proliferative risk on C6 — the axis with zero coverage, which cannot absorb a negative contributor | Pathway §3.4 |
| **Berberine in any transplant / calcineurin-inhibitor patient** | Human data: cyclosporine trough +29%, AUC +35% in renal transplant recipients. Contraindication, not a monitoring problem | Safety §2.7 |
| **Berberine in the recovery window** | **NEW** — its permitted window is its liability window; Wnt-dependent crypt regeneration is exactly what it suppresses (§5.1) | This report |
| **Berberine + piperine (or any yogavahi bioenhancer)** | **NEW** — bioenhancement is inverted in CDI: it moves drug out of the working compartment and stacks a third same-direction CYP3A4/P-gp perturbation onto narrow-TI immunosuppressants (§5.4) | This report |
| **Any classical grahi/stambhana antidiarrhoeal** | **NEW** — antimotility mechanism → prolonged toxin contact → toxic megacolon risk. Disqualified by the mechanism that makes it traditionally effective (§5.4) | This report |
| **DAV132 (or any colonic adsorbent) + oral vancomycin / fidaxomicin** | **NEW** — an adsorbent binds the therapeutic luminal antibiotic too, attacking the backbone's mechanism directly. Precedent: cholestyramine binds vancomycin. **Ribaxamase does not have this problem; DAV132 does** (§4.3) | This report |
| **UDCA + IBAT inhibitor** | ⚑ Veto — shunts **taurocholate, the germinant**, to the colon alongside the inhibitor | Integrator §4 |
| **Any second C2 agent on fidaxomicin** | Zero added axes on the most over-served axis in the disease; inherits the bar that killed eight programmes | R2 |
| **UDCA/CamSA co-administered *with* fidaxomicin** | **NEW (as an explicit entry)** — bile-salt micellisation of a MW-1058 poorly-soluble macrocycle whose efficacy is luminal-concentration-dependent. Sequential only | Pathway §6.6, formalised here as R3 |
| **TUDCA presented as consensus** | The Pathway-vs-SAR conflict is resolved in Pathway's favour but is **not** settled; and the regulatory premise (Relyvrio) is likely void | Integrator §4 |
| **Live biotherapeutics in immunocompromised patients** | Bacteraemia/fungaemia risk; this is the constraint that generates Combination B | §3.4 |

---

## 7. COMBINED COVERAGE — all three constructions against the eight axes

```
┌────────────────────────────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬───────┐
│ Construction               │ C1  │ C2  │ C3  │ C4  │ C5  │ C6  │ C7  │ C8  │ Axes  │
│                            │germ │fitns│ tox │intox│ host│barri│ ecol│spore│       │
├────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┤
│ SOC ALONE (fidaxomicin)    │ ░░  │ ██  │ ██  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ██  │ 3.5   │
├────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┤
│ ⭐ COMB. A (immunocompetent)│ ██  │ ██  │ ██  │ ░░  │ ▓▓  │ ▓▓  │ ██  │ ██  │ 6.0   │
│    fidax → LBP + bridge    │     │     │     │     │     │     │     │     │       │
│    └ base case, no bridge  │ ▓▓  │ ██  │ ██  │ ░░  │ ▓▓  │ ▓▓  │ ██  │ ██  │ 5.0   │
├────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┤
│ ⭐ COMB. B (immunocompr.)   │ ██  │ ██  │ ██  │ ░░  │ ░░  │ ░░  │ ▓▓  │ ██  │ 4.5   │
│    fidax → anti-germinant  │     │     │     │     │     │     │     │     │       │
│    └ + Gen-2 TcdB-IgY      │ ██  │ ██  │ ██  │ ██  │ ▓▓  │ ▓▓  │ ▓▓  │ ██  │ 6.0   │
├────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┤
│ ⭐ COMB. C (prevention)     │ ░░  │ ░░  │ ░░  │ ░░  │ ░░  │ ░░  │ ██  │ ░░  │ 1.0   │
│    ribaxamase              │     │     │     │     │     │     │ SHLD│     │ (but  │
│                            │     │     │     │     │     │     │     │     │ pre-  │
│                            │     │     │     │     │     │     │     │     │ vents │
│                            │     │     │     │     │     │     │     │     │ entry)│
├────────────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┤
│ RESIDUAL WHITE SPACE       │  —  │  —  │  —  │ ⚠A  │ ⚠   │ ⚠⚠ │ ⚠B  │  —  │       │
└────────────────────────────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴───────┘

  ⚠⚠ C6 (barrier/repair) — ZERO real coverage in any construction. The widest
     white space in CDI is still white after three combination designs. The
     LBP's ▓▓ is indirect. Best data-backed chemotype is the flavonoids
     (quercetin: 6 TJP1 + 5 OCLN + 3 CLDN1 rows in project data) — but the
     SAME file shows quercetin with 10 CTNNB1 rows, kaempferol 2, luteolin 1.
     ⚠ The barrier/Wnt co-modulation problem is CLASS-WIDE in flavonoids, not
       berberine-specific. Verified independently in this report.
  ⚠A C4 — empty for immunocompetent patients since bezlotoxumab's withdrawal
  ⚠B C7 — uncovered in the immunocompromised; no non-live restorative exists
```

**Read against the starting position.** Coverage entering Phase 3 was `C1:1 · C2:6 · C3:1 · C4:1 · C5:2 · C6:0 · C7:1 · C8:1` — heavily piled on the one axis that has buried eight programmes. **The three constructions above take a single patient from 3.5 covered axes on SOC alone to 6.0, and they do it without adding a single C2 agent.** That is the specific thing combination design was supposed to accomplish here, and it is achieved by sequencing existing assets rather than by discovering new ones.

---

## 8. DRUG–DRUG INTERACTION SUMMARY

Assessed against §3.3's checklist for the actual CDI population: elderly, renally impaired, CHF-prevalent, heavily polypharmaceutical.

| Pair | CYP / transporter | Target competition | Physicochemical | Overall |
|---|---|---|---|---|
| Fidaxomicin ↔ UDCA | None meaningful | None — different axes | **⚠ Micellisation risk if concurrent** | **LOW if sequential** |
| Fidaxomicin ↔ CamSA | None | None | Sulfonate; low micellising capacity vs UDCA | **LOW** |
| Fidaxomicin ↔ LBP | None | ⚠ Directional — antibiotic kills consortium | Sequential by label | **LOW if sequential** |
| UDCA ↔ LBP | None | **⚠ THE open question — engraftment antagonism** | None | **MODERATE — gated** |
| CamSA ↔ LBP | None | **Low by design — C1-selective** | None | **LOW (predicted)** |
| Anti-germinant ↔ tacrolimus / cyclosporine | **None** — bile acids are not meaningful intestinal P-gp/CYP3A4 inhibitors | None | None | **LOW — load-bearing for Comb. B** |
| Ribaxamase ↔ IV β-lactam | N/A (enzymatic degradation of luminal residue) | ⚠ Must not reduce systemic efficacy — diligence item | None | **LOW, pending verification** |
| Ribaxamase ↔ oral vanco/fidax | None — wrong substrate class | None | None | **LOW** |
| **DAV132 ↔ oral vanco/fidax** | — | — | **⚠⚠ ADSORPTION of the therapeutic antibiotic** | **HIGH — AVOID** |
| **Berberine ↔ tacrolimus / cyclosporine** | **⚠⚠ Intestinal P-gp + CYP3A4, human-demonstrated** | None | None | **HIGH — CONTRAINDICATED** |
| Berberine ↔ apixaban / rivaroxaban | ⚠ Dual CYP3A4 + P-gp — berberine is exactly the combined inhibitor that produces large effects | None | None | **MODERATE–HIGH** |
| Berberine ↔ digoxin | ⚠ Three-way convergence: P-gp inhibition + CKD + CDI-driven hypokalaemia, plus an ecological arm via *E. lenta* | None | None | **HIGH** |
| Any component ↔ warfarin | Indirect — microbiome shifts alter vitamin K₂ | None | None | **MODERATE — monitor INR** (applies to LBP arms) |

**Population-level notes.** Antimotility agents (loperamide, and the traditional astringent category per §5.4) are relatively contraindicated across all three constructions. Metformin causes diarrhoea independently and confounds the efficacy endpoint. PPI use (40–60% of this population) defeats pH-triggered colonic-release formulations, and dysbiosis defeats microbiota-triggered ones — **both of the two commonest colon-targeting mechanisms are compromised in exactly this patient**, which is a formulation constraint on any colon-targeted UDCA product and a further structural argument for CamSA, whose luminal confinement is a property of the molecule rather than of the capsule.

---

## 9. FORMULATION FEASIBILITY

| Component | Route | Physicochemistry (project data) | Feasibility |
|---|---|---|---|
| Fidaxomicin | Oral tablet | MW **1058.05**; poorly soluble; luminal-retained (`chembl_approved_drugs.csv`) | **Approved.** No change |
| UDCA / ursodiol | Oral | MW **392.58**, alogP **4.48**, PSA **77.76**, HBD 3, Ro5 violations **0**, first approval **1987** | **⚠ Requires colon-targeted reformulation.** Good permeability is the *problem* here — it is absorbed proximally via ASBT. Colon targeting is a **safety** requirement (avoids the PSC high-dose harm range), not a PK nicety |
| TUDCA / taurursodiol | Oral | MW **499.71**, alogP **3.40**, PSA **123.93**, HBD 4, first approval **2022** | **Better colonic-delivery physics than UDCA** — higher PSA and lower alogP predict lower passive absorption, and taurine conjugation resists deconjugation in a BSH-depleted colon. Adds TGR5 #62 agonism (C5/C6 tone). ⚠ Regulatory premise likely void; mechanism resolved in Pathway's favour but **not settled** |
| CamSA | Oral | Cholate core + bulky C24 aryl **sulfonate**; zero reducible groups | **Best-in-class luminal confinement by structure.** The sulfonate that drives potency is the same group that guarantees non-absorption — efficacy and safety levers are the same atom pointing the same way. One amide coupling from a commodity API. ⚠ NCE: no human exposure |
| VOWST / REBYOTA / VE303 | Oral capsule / rectal | Living organisms | **Approved (VOWST, REBYOTA) / Phase 3 (VE303).** Oral route is the genuine advance; rectal is a commercial drag |
| Oral TcdB-IgY | Oral, enteric | Protein — must survive gastric acid and pancreatic proteases | Solved in principle for oral antibodies; **unsolved for this product.** Plus the antigen re-specification requirement (§3.4) |
| Ribaxamase | Oral, delayed-release | Enzyme biologic | Phase 2b formulation exists ⚠️verify. BLA-grade CMC is the hard part |

**Co-formulation assessment: NONE of the three constructions should be co-formulated.** Every one is a sequence. This is the single largest departure from the skill file's OM framing, where a combined rinse was the default deliverable. Here, co-formulation would create the micellisation problem, the antibiotic-consortium conflict, or both. **Sequential administration is not a compromise in CDI — it is the design.**

---

## 10. THE SINGLE BEST COMBINATION PER POPULATION

### 10.1 Immunocompetent, first or second recurrence

> ## **Fidaxomicin d0–10 → VOWST (or VE303) per label**
> ## **± UDCA bridge d11 → engraftment, as a randomised add-on arm**

**Why this and not something else.** It is the only construction that covers **C7**, the sole loop-*exiting* axis, and it does so with a component that has an approval-grade precedent (ECOSPOR III, n≈182 → approval). Every element is approved or Phase 3. It has no directional conflicts and no meaningful DDIs. **The bridge is deliberately not load-bearing** — the combination does not fail if the UDCA option is killed, which is the correct risk posture for a component whose IC₅₀ has never been measured.

**Decision gate:** the engraftment ± UDCA experiment (§11, C-1). Until it reads out, the deployable regimen is **fidaxomicin → LBP with no bridge** (5.0 axes), which is already the best available standard of care and requires no development at all.

### 10.2 Immunocompromised / transplant — ⭐ **the strategic recommendation**

> ## **Fidaxomicin d0–10 → colon-targeted UDCA (near-term) or CamSA (preferred)**
> ## **d11 → week 12+, chronic rather than time-boxed**
> ## **± second-generation oral TcdB-directed IgY**

**Why this is the flagship despite lower axis coverage than 10.1.** Coverage is not the objective function; **unmet need is.** §4.6 ranks *"prevent recurrence without requiring live biotherapeutics"* as **#1**, and this is the only construction in the entire analysis that serves it. It also has three structural advantages over Combination A that are easy to miss:

1. **Combination A's principal risk does not exist here.** No consortium means no engraftment antagonism — in the population where the anti-germinant matters most.
2. **The DDI surface is near-empty** in a population defined by narrow-TI CYP3A4/P-gp substrates. This is exactly where berberine and every other gut-wall-active candidate is disqualified, and where the bile-acid chemotype's *lack* of pharmacology is the asset.
3. **It has no competitor.** VE303 is taking the bile-acid-restoration narrative with Phase 3 data — but it cannot take this population, because it is alive.

**Decision gate:** the bile-acid germination dose-response (integrator Exp. 4) must produce a UDCA IC₅₀ and a UDCA : taurocholate ratio before any Stage 0 decision. **Today, Stage 0 compares a concentration to a threshold that does not exist.** And behind that sits the class question (§11, C-3): *can any anti-germinant hold a spore reservoir?* If the answer is no, UDCA, CamSA, chenodiol and urso-CamSA all die together. That is the honest shape of this recommendation.

### 10.3 Primary prevention, patients on IV β-lactams

> ## **Ribaxamase throughout β-lactam therapy** — gated on a $150–300K diligence pass

**Why it wins the portfolio question even though it wins no coverage contest.** It is the only intervention that operates *before* the disease, the only asset with **positive human Phase 2b** data, and the only one that structurally escapes all three failure modes that killed this field. From a combination seat, its distinguishing property is **orthogonality**: it layers onto any patient in 10.1 or 10.2 without a single conflict.

**Decision gates:** (a) the Phase 2b data package — unverified by anyone in this pipeline; (b) the β-lactam-attributable fraction of the addressable CDI population, which nobody has quantified and which sets the commercial ceiling.

---

## 11. COMBINATION-SPECIFIC EXPERIMENTS

These are **additional to** the integrator's seven de-risking experiments, not a restatement. Each is generated specifically by a combination-level question that no single-agent assessment would surface.

| # | Experiment | Cost (est.) | Time | What it decides |
|---|---|---|---|---|
| **C-1** | **Consortium engraftment ± bile acid.** VE303/Vowst strains in an anaerobic continuous-culture or humanised-mouse model, ± UDCA and ± CamSA at achievable luminal concentrations. Read out per-strain engraftment by shotgun metagenomics | **$120–250K** | 3–4 mo | **Whether Combination A's bridge is synergistic or antagonistic.** Also directly tests the §2.3 prediction that CamSA is safe where UDCA is not — the strongest single argument for the CamSA programme |
| **C-2** | **Fidaxomicin luminal-concentration ± bile acid.** In vitro dissolution/micellisation in simulated colonic fluid, then fecal fidaxomicin concentration in a co-dosed vs sequential animal arm | **$40–80K** | 1–2 mo | Whether the sequential-dosing requirement (R3) is genuinely load-bearing or merely conservative. Cheap, and it either retires a constraint or hardens it |
| **C-3** | **The class question: can an anti-germinant hold a spore reservoir?** Relapse-model design with a defined, non-replenishing spore load; anti-germinant started after antibiotic clearance; endpoint is relapse at 4–8 weeks, not initial cure | **$200–400K** | 6–9 mo | **The largest single uncertainty behind Combination B, and nothing in the analysis addresses it.** UDCA, CamSA, chenodiol and urso-CamSA all live or die together on this result. §2.10 lists it under UNCERTAIN/DISPUTED. **This is the experiment I would run before spending anything on molecule optimisation** |
| **C-4** | **Vulnerable-window characterisation in humans.** Serial fecal bile-acid profiling (taurocholate, CDCA, DCA, LCA) and `baiCD` qPCR from last fidaxomicin dose through week 8, in patients with and without an LBP | **$150–300K** | 6–12 mo | **Defines the window this entire report is designed around, and converts R5's "engraftment marker" from a concept into a measurable stopping rule.** Also generates the UDCA : taurocholate denominator Pathway §2.4a needs |
| **C-5** | **TcdB-directed IgY feasibility.** Raise IgY against TcdB (not TcdA), confirm neutralisation in a Vero/organoid assay, and test gastric+proteolytic survival of the enteric formulation | **$80–150K** | 4–6 mo | Whether Combination B's C4 arm is real or a placeholder. Cheap relative to the axis it would fill, and C4 is empty white space since bezlotoxumab's withdrawal |

**If only one is funded: C-3.** It is the only experiment that can invalidate the entire anti-germinant thesis, and every downstream molecule decision — UDCA vs CamSA vs urso-CamSA, formulation spend, Stage 0 design — is conditional on it. **If only one *cheap* one is funded: C-2**, at $40–80K, which either retires or hardens a constraint that shapes both A and B.

---

## 12. CONFIDENCE AND LIMITATIONS

| Claim | Confidence | Basis |
|---|---|---|
| Combinations must be adjunctive to SOC, not replacements | **HIGH** | Add-on 3-for-3, replacement 0-for-3; §4.5's three failure modes |
| Sequential, never concurrent, for antibiotic + bile acid | **HIGH** | Two independent arguments (physicochemical and pharmacodynamic) converge |
| The vulnerable window (d~10–28) is the correct design target | **MODERATE–HIGH** | Assembled from four established facts, but the window's exact boundaries are **not measured** — that is experiment C-4 |
| The bridge should be time-boxed in A and chronic in B | **MODERATE** | Follows cleanly from the self-tapering handoff argument and its absence in B. Neither duration has been tested |
| **CamSA is a safer LBP partner than UDCA because it is C1-selective** | **MODERATE** | The C1/C2 separation is mechanistically sound (CspC occupancy vs general anti-Clostridial growth inhibition) but **CamSA's lack of C2 activity is inferred from its mechanism, not measured.** This is the report's most novel claim and its most testable — experiment C-1 |
| Combination B is the strategically differentiated construction | **HIGH** on the strategic logic; **LOW–MODERATE** on efficacy | §4.6 #1 is unambiguous. But "whether anti-germinants achieve durable clinical benefit" is listed under UNCERTAIN/DISPUTED |
| Berberine has no clean window | **MODERATE** | The timeline conflict is a sound inference from the Wnt-dependence of crypt regeneration; berberine's *net* effect on a TcdB-injured, regenerating crypt is inferred, not measured. Testable by organoid regeneration ± TcdB |
| Berberine is contraindicated in transplant patients | **HIGH** | Human clinical data (cyclosporine +29% trough / +35% AUC in renal transplant recipients) |
| Berberine has zero direct target rows in project data | **HIGH — verified in this report** | Direct query of `pubchem_phytochem_target_interactions.csv`: 20 matches, all co-treatment mentions in other compounds' evidence strings |
| Colonic adsorbents must not be co-dosed with oral vanco/fidaxomicin | **MODERATE–HIGH** | Mechanistically necessary; supported by the cholestyramine–vancomycin precedent, but not demonstrated for DAV132 specifically |
| The yogavahi and grahi principles invert in CDI | **HIGH** | Follows directly from §6.2's inverted ADMET logic and §3.3's antimotility contraindication |
| Ribaxamase orthogonality (no conflict with any construction) | **MODERATE–HIGH** | Substrate-class argument is sound (β-lactamase cannot degrade a glycopeptide or a macrocycle); the systemic-efficacy question is a diligence item |
| C6 remains uncovered after all three designs | **HIGH** | No construction addresses it; independently confirmed against project data (§7) |

**Limitations, stated plainly:**

- **Every combination here is a hypothesis about an untested interaction.** None of the three-way or even two-way interactions proposed has been studied clinically. Each carries a named decisive experiment; none should be read as a clinical recommendation.
- **The most important number in this report does not exist.** UDCA's germination IC₅₀ has never been measured. Combination B's core component is being positioned against a threshold nobody has determined. I have flagged this rather than estimated around it.
- **The vulnerable window's boundaries are inferred, not measured.** Engraftment kinetics for VOWST/VE303 and the precise recurrence hazard curve are ⚠️verify items drawn from the clinical-landscape report, itself prepared without live literature retrieval.
- **Project data contributed physicochemistry and a negative result, not combination evidence.** `chembl_approved_drugs.csv` supplied the UDCA/TUDCA/fidaxomicin/niclosamide properties used in §9. `pubchem_phytochem_target_interactions.csv` supplied the flavonoid barrier/Wnt row counts in §7, the oleanolic acid → GPBAR1 rows in §5.4, and the **berberine null result** in §5.1. **DisGeNET contains no CDI data** (OM-specific only), and there are no CDI pathway annotations in the knowledge graph. **No combination-level data exists in this project's databases for any pair proposed here** — the combination logic is entirely mechanistic reasoning over the C1–C8 map.
- **The C1/C2 separation argument for CamSA is my construction.** It is chemically and microbiologically reasonable, and it makes a falsifiable prediction (experiment C-1). It is not drawn from a source document, and it should be read as a hypothesis with a test attached rather than as a finding.
- **I did not solve C6.** Three combination designs, and the widest white space in CDI is still white. The best data-backed chemotype (flavonoids) carries the same Wnt co-modulation problem that disqualifies berberine, which my own data query confirms is class-wide rather than compound-specific. **Naming that honestly is more useful than proposing a quercetin arm I cannot defend.**

---

## 13. STRUCTURED OUTPUT (JSON)

```json
{
  "agent": "combination-designer",
  "phase": 3,
  "disease": "Clostridioides difficile infection",
  "date": "2026-08-18",
  "design_frame": {
    "target": "the vulnerable window",
    "definition": "interval from last fidaxomicin dose (d10) to confirmed consortium engraftment (~d28), during which drug pressure is off, the spore reservoir is intact, and the ecological anti-germination defence has not returned",
    "why": "recurrence events accrue here and the regulatory endpoint (recurrence through week 8) measures exactly this interval",
    "design_rules": {
      "R1": "adjunct to SOC only - add-on trials 3-for-3, replacement 0-for-3",
      "R2": "no second C2 agent - 6 of 10 candidates already there, 8 programmes failed",
      "R3": "sequential unless concurrency is proven safe",
      "R4": "preserve the commensal community",
      "R5": "time-box every bridge to a measurable endpoint, not a calendar date"
    }
  },
  "combinations": [
    {
      "id": "A",
      "name": "Bridged Handoff",
      "population": "immunocompetent, first or second recurrence",
      "components": [
        {"agent": "fidaxomicin", "window": "d0-d10", "role": "backbone", "axes": ["C2", "C3", "C8"]},
        {"agent": "VOWST or REBYOTA or VE303", "window": "per label after washout", "role": "primary anti-recurrence, only loop-exiting component", "axes": ["C7", "C1-partial", "C5-partial", "C6-partial"]},
        {"agent": "UDCA (near-term) or CamSA (preferred)", "window": "d11 to confirmed engraftment (~d28)", "role": "OPTIONAL bridge, not load-bearing", "axes": ["C1"]}
      ],
      "axes_covered": 6.0,
      "axes_covered_without_bridge": 5.0,
      "combination_type": "complementary + sequential, self-tapering handoff",
      "key_risk": "bridge may suppress consortium engraftment - combination-inverting",
      "key_design_finding": "engraftment antagonism is carried by C2 (growth-inhibitory) activity, not C1 (germination-antagonist) activity; CamSA is C1-selective and UDCA is not, making the WEAKER polypharmacology the desired property",
      "gate": "experiment C-1 (engraftment plus/minus bile acid)",
      "verdict": "RECOMMENDED as base case (fidax to LBP); bridge as randomised add-on arm",
      "confidence": "Moderate-High on base case; Moderate-Low on bridge"
    },
    {
      "id": "B",
      "name": "Dry Bridge",
      "population": "immunocompromised / transplant - no live organisms",
      "components": [
        {"agent": "fidaxomicin", "window": "d0-d10", "role": "backbone", "axes": ["C2", "C3", "C8"]},
        {"agent": "colon-targeted UDCA (near-term) or CamSA (preferred)", "window": "d11 to week 12+, CHRONIC not time-boxed", "role": "PRIMARY anti-recurrence, load-bearing", "axes": ["C1"]},
        {"agent": "oral TcdB-directed IgY", "window": "d11 onward", "role": "second-generation optional", "axes": ["C4"], "hard_requirement": "TcdB-directed antigen - all existing IgY work is anti-TcdA, the arm that failed (actoxumab)"}
      ],
      "axes_covered": 4.5,
      "axes_covered_with_IgY": 6.0,
      "why_flagship": "the only construction serving section 4.6 unmet need #1 (recurrence prevention without live biotherapeutics)",
      "structural_advantages": [
        "Combination A's engraftment-antagonism risk does not exist - no consortium to suppress",
        "near-empty DDI surface in a narrow-TI CYP3A4/P-gp polypharmacy population",
        "no competitor - VE303 cannot take this population because it is alive"
      ],
      "duration_divergence": "the self-tapering handoff licenses stopping the bridge in A; in B the bai guild may never return, so there is nothing to hand off to and the anti-germinant becomes chronic suppression",
      "residual_gap": "C7 NOT covered - no non-live pharmacological restorative exists; this combination holds the loop open rather than exiting it",
      "gates": ["bile-acid germination dose-response (first-ever UDCA IC50)", "experiment C-3 (class question: can any anti-germinant hold a spore reservoir)"],
      "verdict": "RECOMMENDED as the strategically differentiated programme",
      "confidence": "Moderate on design logic; Low-Moderate on efficacy premise"
    },
    {
      "id": "C",
      "name": "Shield",
      "population": "primary prevention, patients on IV beta-lactams",
      "components": [
        {"agent": "ribaxamase (SYN-004)", "window": "duration of beta-lactam therapy + short tail", "role": "prevents loop entry", "axes": ["C7-shield"]}
      ],
      "axes_covered": 1.0,
      "why_it_matters": "only intervention operating before the disease; only asset with positive human Phase 2b; escapes all three field-wide failure modes; orthogonal to A and B with zero conflicts",
      "class_coverage_gap": "beta-lactam-only. DAV132 (adsorbent) is class-agnostic and complementary - SELECT BY REGIMEN, DO NOT STACK",
      "new_avoid_entry": "DAV132 or any colonic adsorbent must NEVER be co-dosed with oral vancomycin or fidaxomicin - it would adsorb the therapeutic antibiotic. Precedent: cholestyramine binds vancomycin. Ribaxamase does NOT have this problem (wrong substrate class)",
      "gates": ["Phase 2b diligence ($150-300K)", "quantify beta-lactam-attributable fraction of addressable CDI"],
      "verdict": "RECOMMENDED, gated on diligence",
      "confidence": "Low-Moderate on specifics; High on strategic logic"
    }
  ],
  "designed_and_rejected": [
    {
      "combination": "berberine + fidaxomicin",
      "reason": "NO CLEAN WINDOW - berberine is excluded from active Phase 4 disease on the Wnt liability, but its C5 window opens in the recovery phase, which is exactly when Wnt-dependent crypt regeneration matters most. Permitted window and liability window are the same window.",
      "additional_disqualifiers": [
        "contraindicated (not merely monitorable) in transplant patients: cyclosporine trough +29%, AUC +35%, human data",
        "gut-wall DDI is AMPLIFIED by non-absorption, not removed",
        "zero direct target rows in project data - verified: 20 matches in pubchem_phytochem_target_interactions.csv are ALL co-treatment mentions in other compounds' evidence strings"
      ],
      "re_entry_conditions": ["spo0A in vivo disconfirmation clean", "colonic organoid regeneration plus/minus TcdB clean"],
      "verdict": "NOT RECOMMENDED in any construction"
    },
    {"combination": "fidaxomicin + bezlotoxumab + anti-germinant", "reason": "obsoleted - Merck discontinued bezlotoxumab January 2025; not wrong, unavailable"},
    {"combination": "any second C2 agent on fidaxomicin", "reason": "rejected by rule R2 - zero added axes on an 8-programme graveyard axis"}
  ],
  "traditional_medicine_principle_inversions": [
    {"principle": "Yogavahi (bioenhancer, e.g. piperine)", "om_mapping": "synergy via absorption enhancement", "cdi_reality": "HARM - absorption removes drug from the working compartment and stacks CYP3A4/P-gp perturbation onto narrow-TI immunosuppressants. Berberine + piperine is doubly contraindicated", "status": "NEW AVOID ENTRY"},
    {"principle": "Grahi / Stambhana (astringent antidiarrhoeal for atisara)", "om_mapping": "symptomatic control", "cdi_reality": "HARM - antimotility mechanism prolongs toxin contact time, toxic megacolon risk. Disqualified by the mechanism that makes it traditionally effective", "status": "NEW AVOID ENTRY"},
    {"principle": "Prativisha (mutual antagonism of toxicity)", "cdi_reality": "TRANSLATES - Combination C (ribaxamase) is a literal instance: an agent that destroys the harmful residue of another while preserving its intended action"},
    {"principle": "Vijatiya dravya (different-class combination)", "cdi_reality": "TRANSLATES - Combinations A and B are both vijatiya constructions across three classes and three axes"}
  ],
  "best_per_population": {
    "immunocompetent": "Fidaxomicin d0-10 -> VOWST/VE303 per label, plus/minus UDCA bridge d11-engraftment as a randomised add-on arm. Deployable today WITHOUT the bridge (5.0 axes).",
    "immunocompromised": "Fidaxomicin d0-10 -> colon-targeted UDCA (near-term) or CamSA (preferred), d11-week 12+, chronic. STRATEGIC RECOMMENDATION - the only construction serving unmet need #1.",
    "primary_prevention": "Ribaxamase throughout IV beta-lactam therapy, gated on $150-300K diligence."
  },
  "new_experiments": [
    {"id": "C-1", "name": "consortium engraftment plus/minus bile acid", "cost": "$120-250K", "decides": "whether Combination A's bridge is synergistic or antagonistic; tests the CamSA C1-selectivity prediction"},
    {"id": "C-2", "name": "fidaxomicin luminal concentration plus/minus bile acid", "cost": "$40-80K", "decides": "whether the sequential-dosing rule R3 is load-bearing; cheapest constraint-retiring experiment"},
    {"id": "C-3", "name": "can any anti-germinant hold a spore reservoir (class question)", "cost": "$200-400K", "decides": "THE largest uncertainty behind Combination B; UDCA, CamSA, chenodiol and urso-CamSA all live or die together. FUND THIS FIRST if only one"},
    {"id": "C-4", "name": "vulnerable-window characterisation in humans", "cost": "$150-300K", "decides": "converts R5's engraftment marker from concept to stopping rule; generates the UDCA:taurocholate denominator"},
    {"id": "C-5", "name": "TcdB-directed IgY feasibility", "cost": "$80-150K", "decides": "whether Combination B's C4 arm is real or a placeholder"}
  ],
  "coverage_summary": {
    "SOC_alone": 3.5,
    "combination_A": 6.0,
    "combination_A_no_bridge": 5.0,
    "combination_B": 4.5,
    "combination_B_with_IgY": 6.0,
    "combination_C": 1.0,
    "residual_white_space": {
      "C6_barrier_repair": "ZERO real coverage after three designs - the widest white space in CDI is still white. Flavonoids are the only data-backed chemotype and they carry the same class-wide Wnt co-modulation problem (verified: quercetin 6 TJP1 + 5 OCLN + 3 CLDN1 rows AND 10 CTNNB1 rows in project data)",
      "C4_intoxication": "empty for immunocompetent patients since bezlotoxumab's withdrawal",
      "C7_ecological": "uncovered in the immunocompromised - no non-live pharmacological restorative exists"
    },
    "note": "three constructions take a single patient from 3.5 covered axes on SOC alone to 6.0, WITHOUT adding a single C2 agent"
  },
  "data_sources_used": [
    "data/processed/chembl_approved_drugs.csv - physicochemistry for URSODIOL, TAURURSODIOL, FIDAXOMICIN, VANCOMYCIN, NICLOSAMIDE",
    "data/processed/pubchem_phytochem_target_interactions.csv - flavonoid barrier/Wnt row counts, oleanolic acid GPBAR1 agonism, berberine NULL result"
  ],
  "limitations": [
    "every combination is a hypothesis about an untested interaction",
    "UDCA's germination IC50 has never been measured - Combination B is positioned against a threshold nobody has determined",
    "vulnerable-window boundaries are inferred, not measured",
    "no combination-level data exists in project databases for any pair proposed here",
    "the C1/C2 separation argument for CamSA is my construction, falsifiable by C-1",
    "C6 is not solved by any design in this report"
  ]
}
```

---

## 14. HANDOFF TO THE FINAL SYNTHESIS

**Three things this report contributes that are not in any upstream document:**

1. **The vulnerable window as an explicit design object**, and its consequence: the anti-germinant is a **bridge with a stopping rule**, not week-12 maintenance. The self-tapering-handoff biology that Round 2 cited actually argues for the shorter course it did not propose — and for the *longer* course in Combination B, where the handoff target does not exist.

2. **The C1/C2 selectivity argument.** Engraftment antagonism is carried by growth-inhibitory (C2) activity, not germination-antagonist (C1) activity. This makes **CamSA a mechanistically better partner for a live biotherapeutic than UDCA precisely because it is the weaker agent** — an inversion of the usual combination-design instinct, a new and non-potency-based argument for the CamSA programme, and a falsifiable prediction (experiment C-1).

3. **Three new avoid-list entries**, two of them from taking the traditional-medicine lens seriously rather than discarding it: **colonic adsorbents + oral SOC antibiotic** (mechanism-level, with a cholestyramine precedent), **yogavahi bioenhancers** (inverted by §6.2's ADMET logic), and **classical astringent antidiarrhoeals** (disqualified by the antimotility contraindication that makes them traditionally effective).

**One thing the final synthesis should not let this report obscure:** none of the three constructions covers **C6**. Three combination designs later, the widest white space in CDI is exactly as empty as it was at the start of Phase 3, and the best data-backed chemotype for it carries a class-wide Wnt liability that this report's own data query confirms. That is a genuine negative result and it belongs in the consensus.

---

*All combination designs in this report are hypothetical and require experimental validation — ideally in combination assays, not by inference from single-agent data. Nothing here is a clinical recommendation.*
