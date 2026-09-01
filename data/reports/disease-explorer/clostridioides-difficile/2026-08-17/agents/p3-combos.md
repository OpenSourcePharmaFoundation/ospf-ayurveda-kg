# Phase 3 — Combination Designer Report
## *Clostridioides difficile* Infection (CDI)

**Agent:** Combination Designer (skill file `.claude/skills/combination-designer/SKILL.md`, adapted for CDI)
**Phase:** 3 — final evaluation
**Date:** 2026-08-17
**Inputs read:** `disease-model.md` (§2.10, §3.3, §3.4, §4.1–4.6, §5, §6, §7, §A.2) · `debate-summary.md` · `agents/p2-pathway.md` (§1 axes, §2 UDCA, §3 berberine, §5 coverage matrix, §6 combinations) · `agents/debate-integrator.md` (§4 two-population construction, §5 lead programme, §6 experiments) · `agents/p2-literature.md` (§berberine biofilm, §4 IgY) · `agents/p2-safety.md` (§ routed notes) · `agents/p1-admet.md` (§ routed notes) · `agents/p1-ethnobotany.md` (§2.8 colostrum/IgY) · `agents/p1-disease-modeler.md` (§Phase 4 repair gap)
**Project data queried:** `data/processed/pubchem_phytochem_target_interactions.csv` · `data/processed/chembl_approved_drugs.csv`

---

## 0. SKILL FILE ADAPTATION — what changed, and the one thing that did not

My skill file was written for Oral Mucositis. Five adaptations were required:

| Skill-file assumption | CDI reality | What I did |
|---|---|---|
| Five OM pathobiology phases | **Eight CDI causal axes (C1–C8)** per `p2-pathway.md` §1 | Replaced the phase-coverage grid with the C1–C8 axis grid, using the Pathway Analyst's ██/▓▓/░░/▼▼ notation for continuity |
| "Cancer treatment supremacy" — do not compromise the primary therapy | CDI's analogue is stronger: **the SOC antibiotic is the backbone, and every candidate is an adjunct.** CDI replacement trials are **0-for-3**; CDI add-on trials are **3-for-3** | Every combination below is constructed as *SOC + module*, never *instead of SOC*. No construction in this report replaces fidaxomicin |
| Combinations delivered together (rinse/gel) | CDI combinations are **temporally staged** across a 12-week window, and the disease's own pharmacology forbids some co-administration | Made time an explicit design axis. Two of my revisions are *timing* changes, not component changes |
| Ayurvedic multi-plant formulations are the central object | Per §7.1, traditional medicine **cannot compete on antibacterial potency in CDI**. But the lead mechanism (UDCA) is literally a bear-bile isolate, and the C4 arm (colostrum/IgY) has a *piyush*/*kharvas* lineage | Kept traditional-medicine analysis, but demoted it to §9 as rationale-supportive context, not evidence |
| DDI = CYP/transporter interactions | In CDI the dominant interactions are **physicochemical and ecological**: micellisation, adsorption, competitive receptor occupancy, and suppression of a live co-administered organism | Added a physicochemical/ecological interaction layer to Step 3 of my framework. **This is where three of my four new findings came from** |

**The one thing that did not change:** the skill's guardrail *"Don't assume synergy — multi-compound ≠ automatically better; justify every combination component."* In CDI that guardrail bites unusually hard, because §4.5's failure synthesis creates a standing pressure to add components ("combinations are where the value lies"), and that pressure is exactly how unjustified components get in. **Two of my six recommendations are to remove a component, and one is to refuse to fill an empty axis.** Those are combination-design outputs too.

### Data availability, stated plainly

Per the skill's opening instruction, I checked `data/processed/`. **The project's data assets are OM-centric and cover this combination question thinly:**

- `pubchem_phytochem_target_interactions.csv` (17 MB) — usable, and I ran two original queries against it (§6.3, §9). Covers **phytochemical → host-gene** interactions only. It contains **no *C. difficile* target, no bile-acid receptor CspC, no toxin, and no bacterial gene** — so it cannot speak to C1, C2, C3, C4 or C8 at all. It is informative for **C5 and C6 only.**
- `chembl_approved_drugs.csv` — usable for physicochemistry of the approved components (§7.1). Note a data gap: **fidaxomicin's and vancomycin's `alogp`/`psa`/`mw_freebase` fields are empty**, so the micellisation analysis in §7.1 rests on literature values for fidaxomicin, not project data.
- `chembl_drug_mechanisms.csv`, `chembl_drug_targets.csv` — 1.9 KB and 3.7 KB respectively. Too sparse to support a target-overlap analysis for any pair in this report.
- `disgenet__OM_*`, `imppat_*`, `medicinal_plants_with_uses.csv`, `ttd_drug_target_genes.csv` — OM/plant-scoped; no CDI content.

**Consequence for confidence calibration:** the target-overlap analysis called for in Step 1 of my framework is, for CDI, **knowledge-based and pathway-derived rather than project-data-derived.** Where I make a claim from project data I say so and give the row count; everywhere else the provenance is the named upstream agent report. I flag this explicitly because the debate round's single most important methodological finding was a **fabricated claim that survived synthesis** (`debate-summary.md`, provenance audit). I have tried not to add another.

---

## 1. EXECUTIVE SUMMARY

**Verdict on the three combinations handed to me: two validated with revisions, one validated as-is but re-framed.**

| # | Combination as briefed | My verdict | The change that matters |
|---|---|---|---|
| **A** | Immunocompetent: Fidaxomicin → LBP + UDCA (optional) → wk 12 | **REVISED — remove UDCA** | UDCA's upside in A is explicitly "not load-bearing"; its downside is **disabling the load-bearing component** (suppressing the bile-acid-metabolising Clostridia that *are* the C7 mechanism). Asymmetric risk. Do not co-dose an optional component with a catastrophic downside |
| **B** | Immunocompromised: Fidaxomicin → UDCA/CamSA **or** oral TcdB-IgY → wk 12 | **REVISED — split the "or" into a ladder plus a module** | The slash and the "or" hide three different things: a fast clinical probe (UDCA/chenodiol), an NCE (CamSA), and a *different axis* (IgY = C4, not C1). C1 and C4 are complementary, not alternatives. **The combined construction reaches 6–6.5 axes with zero live-organism exposure — the highest coverage in the entire analysis, for the least-served population** |
| **C** | Primary prevention: Ribaxamase during IV β-lactam therapy | **VALIDATED — but stop scoring it on axis count** | Axis coverage is a *within-episode* metric. C operates *pre-episode*. Ranking a 1-axis prevention asset against a 5-axis treatment stack is a category error, and it is how the pipeline nearly lost its own top recommendation |

**The structural revision — one architecture, not three combinations.** A and B are not two combinations. They share a backbone and differ by one module:

```
═══════════════════════════════════════════════════════════════════════════════
 THE CDI COMBINATION ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

 UPSTREAM  ┌───────────────────────────────────────────────────────┐
 (pre-      │  RIBAXAMASE during IV β-lactam therapy        [C7]    │
  disease)  │  Blocks loop ENTRY. Orthogonal to everything below.   │
            └───────────────────────────────────────────────────────┘
                                    ↓ (if CDI occurs anyway)
 BACKBONE  ┌───────────────────────────────────────────────────────┐
 (all       │  FIDAXOMICIN d0–10                    [C2·C3·C8·C7↑] │
  patients) │            ↓ sequential, never concurrent (§7.1)      │
            │  C1 ANTI-GERMINANT wk 0–12                     [C1]   │
            │  UDCA/chenodiol (probe) → CamSA (asset)               │
            │  ── developed ONCE, labelled for BOTH populations ──  │
            └───────────────────────────────────────────────────────┘
                     ↓                              ↓
 MODULE          ┌──────────────────┐      ┌──────────────────────┐
 (population-    │ IMMUNOCOMPETENT  │      │ IMMUNOCOMPROMISED    │
  specific)      │ + LBP: VOWST /   │      │ + oral TcdB-IgY [C4] │
                 │   REBYOTA / VE303│      │   (or nothing, v1)   │
                 │            [C7]  │      │ ZERO live organisms  │
                 └──────────────────┘      └──────────────────────┘
                   5.0–5.5 axes                 4.5 → 6.5 axes
═══════════════════════════════════════════════════════════════════════════════
```

**Why this re-framing is the most valuable thing in this report.** The Integration Agent positioned the C1 germination programme as *"the fallback if ribaxamase diligence fails"* (`debate-integrator.md` §5). Under the architecture above, C1 is **not a fallback — it is the shared backbone of every post-infection construction, for both populations.** That changes three decisions:

1. **One asset, two labels.** A C1 anti-germinant developed for immunocompromised rCDI is the same molecule, same dose, same window as the C1 arm for immunocompetent rCDI. The immunocompromised indication is the *entry* label (smaller, faster, unmet need #1, no competing modality); the immunocompetent indication is the *expansion*. That is one development spend, not two.
2. **Ribaxamase and the C1 programme are not competitors.** They sit at different points in the recurrence loop — one blocks entry, one blocks germination after entry. `p2-pathway.md` §1 identifies these as **two of the three distinct loop-entry points.** A portfolio holds both; the diligence gate on ribaxamase is not a fork in the road for C1.
3. **It resolves the "who pays for a generic bile acid" problem.** The Repurposing Strategist's objection is real: a 505(b)(2) on generic ursodiol is negative-NPV (`p2-repurposing.md`:148). But the architecture above uses UDCA/chenodiol as a **$1–3M clinical probe whose deliverable is a biomarker, not a product**, and puts the commercial weight on **CamSA — an NCE with composition-of-matter protection.** The generic is the experiment; the NCE is the asset.

**Lead combination for development: Combination B.** Rationale, risks, staged path, costs and regulatory strategy in §8.

**Four findings that are new to this pipeline** (none appear in any Phase 1, Phase 2, or debate document):

| # | Finding | Where | Why it matters |
|---|---|---|---|
| **1** | **Potency, not species, decides whether a C1 agent can be co-dosed with a live biotherapeutic.** Bile-acid growth inhibition of commensal Clostridia is detergency-mediated and needs mM; CspC competitive antagonism is receptor-mediated and CamSA achieves it at ~1000× CDCA potency. A high-potency anti-germinant operates **below the detergent threshold that suppresses the consortium.** | §6.1 | It converts the Pathway Analyst's Combination-A veto from a *class* problem into a *molecule* problem — and names the molecule that solves it. This is the single strongest new argument for CamSA |
| **2** | **Cholestyramine is used off-label in CDI as a toxin binder, and it would abolish any bile-acid arm.** A bile-acid sequestrant co-administered with a bile-acid therapeutic is a direct, total antagonism — and it inherits the tolevamer lesson (§4.5) on the other side | §7.2 | A real-world co-medication collision that no agent flagged. It is simultaneously a **trial exclusion criterion**, a **label contraindication**, and a cheap chart-review study (E-C6) |
| **3** | **The C6 gap must be left open, not filled.** Project data shows the nominated C6 chemotype (flavonoids/triterpenes) is a **β-catenin *inhibitor* class** — quercetin 8/10 `CTNNB1` rows record *decreased* activity. C6 is internally split: tight junctions want flavonoids, crypt-stem renewal wants the opposite | §6.3 | Prevents a plausible-looking component being added to close a gap on the coverage map while working against the axis it was added for. The correct C6 agent is a GLP-2R/EGFR growth-factor class (teduglutide-class), **absent from project data and from the candidate set** |
| **4** | **The sequential architecture is endpoint hygiene, not just PK convenience.** Bile acids cause diarrhoea as their dose-limiting AE, in a disease whose acute endpoint *is* diarrhoea. Deploying the C1 arm in the post-antibiotic window moves its endpoint from *stool frequency* to *toxin-confirmed recurrence* — a binary adjudicated event the AE cannot mimic | §5.2 | The bile-acid diarrhoea confound was named by the Integration Agent as a reason ribaxamase wins. **Correct architecture makes it disappear for the bile acids too** |

---

## 2. THE COMBINATION-DESIGN RULE SET I APPLIED

Before assessing any pairing I fixed the criteria, so that the verdicts below are traceable to stated rules rather than to judgement applied after the fact. This responds directly to the debate round's finding that *"rankings not traceable to inputs"* was upheld at 90% kill probability.

Criteria 1–5 are inherited from `p2-pathway.md` §6. Criteria 6–10 are mine, derived from the Phase 2 reports and the disease model.

| # | Rule | Source | What it kills |
|---|---|---|---|
| 1 | Maximise **distinct** axes; redundant axes score zero | Pathway §6 | Any 2nd C2 agent on fidaxomicin |
| 2 | No **directional conflicts** (no component may push an axis the wrong way) | Pathway §6 | Vancomycin + C7; berberine in active disease (C6) |
| 3 | No **shared failure mode** between components | Pathway §6 | Ebselen + niclosamide (both redox-fragile in the same anaerobic lumen) |
| 4 | At least one component must touch **C7**, the only loop-*exiting* axis | Pathway §6 | Suppression-only stacks presented as cures |
| 5 | Prefer **temporally staged** over concurrent where axes are phase-bound | Pathway §6 | UDCA during acute diarrhoea |
| 6 | **Add-on, never replacement.** The SOC antibiotic is the backbone | §4.5 + CDI trial record (0-for-3 replacement, 3-for-3 add-on) | Every monotherapy construction |
| 7 | **No component may share the trial's primary endpoint as its own pharmacology or its own AE.** A component that lowers stool frequency by a non-anti-infective mechanism corrupts the readout; a component whose dose-limiting AE is diarrhoea does the same in reverse | Safety §8.3; Advocate's symptom-masking attack; Integrator's diarrhoea-confound row | Berberine in an acute-episode trial; bile acids in an acute-episode trial (**both are timing failures, and both are fixable by staging**) |
| 8 | **No component may be inactivated, adsorbed, sequestered or micellised by another** — including by co-medications the population actually receives | §6.2 sequestrant rule; Ethnobotany's tannin/vancomycin question; Pathway's fidaxomicin-micellisation flag | Bile acid + cholestyramine (§7.2); concurrent fidaxomicin + bile acid (§7.1) |
| 9 | **A live component may not be co-dosed with anything that suppresses it.** The organism is the mechanism, not a passenger | Pathway's Combination-2 engraftment risk, extended | UDCA + LBP concurrent (§6.1) — and the reason Combination A loses UDCA |
| 10 | **Coverage arithmetic must never outrun the weakest component's evidence tier.** Report axes *and* the evidence floor | Debate provenance audit (niclosamide scored above all its inputs) | Presenting B2's 6.5 axes as though it were a 6.5-axis *fact* (§6.2) |

**Rule 7 and Rule 10 are the two I would most want carried into the final synthesis.** Rule 7 explains why *timing* rather than *component selection* is the highest-leverage variable in CDI combination design. Rule 10 is the debate round's central methodological correction, restated in a form a combination designer can actually apply.

---

## 3. COMBINATION A — IMMUNOCOMPETENT — **REVISED**

```
═══════════════════════════════════════════════════════════
COMBINATION A (revised): SOC → ecological restoration
═══════════════════════════════════════════════════════════

COMPONENTS:
  1. Fidaxomicin 200 mg PO BID d0–10 (or extended-pulsed d1–25)
     — RNAP switch-region inhibition + sporulation/toxin suppression
     — axes C2 (strong), C3 (strong), C8 (strong), C7 (spares)
  2. VOWST (oral) / REBYOTA (rectal) / VE303 (Ph3) from d10 → wk 12
     — ecological restoration: bai guild, secondary bile acids, niche occupancy
     — axes C7 (strong), C1/C2/C5/C6 (partial, all ecologically mediated)
  3. ✂ UDCA — REMOVED (was "optional add"). See antagonism analysis below

COMBINATION TYPE: Complementary + sequential (failure-mode complementarity)
```

### Axis coverage

```
┌──────────────────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬─────────┐
│ Component            │  C1  │  C2  │  C3  │  C4  │  C5  │  C6  │  C7  │  C8  │ Axes    │
│                      │ germ │ fitns│ toxreg│intox│ infl │ barr │ ecol │ spore│         │
├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼─────────┤
│ Fidaxomicin d0–10    │  ░░  │  ██  │  ██  │  ░░  │  ░░  │  ░░  │  ▓▓  │  ██  │ 3.5     │
│ LBP d10→wk12         │  ▓▓  │  ▓▓  │  ░░  │  ░░  │  ▓▓  │  ▓▓  │  ██  │  ░░  │ 3.0     │
│ ✂ UDCA (removed)     │ (██) │ (▓▓) │  ░░  │  ░░  │  ░░  │  ░░  │ (▓▓) │  ░░  │ (2.0)   │
├──────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼─────────┤
│ COMBINATION A        │  ▓▓  │  ██  │  ██  │  ░░  │  ▓▓  │  ▓▓  │  ██  │  ██  │ 5.0–5.5 │
│ Source of coverage   │ ecol │ fida │ fida │ NONE │ ecol │ ecol │ LBP  │ fida │         │
└──────────────────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴─────────┘

GAPS:  C4 intoxication — EMPTY (bezlotoxumab withdrawn Jan 2025; nothing replaces it)
       C1 germination — PHARMACOLOGICALLY EMPTY; covered only ecologically, and only
                        after the guild re-establishes, which is precisely the window
                        in which recurrence happens
```

**Note on C1 in this construction.** Removing UDCA leaves C1 covered *only* by the returning `bai` guild — i.e. by the very mechanism that has not yet come back. `p2-pathway.md` §2.2 establishes that secondary-bile-acid production requires the depleted guild; §6's phase-alignment table places C1 as a "recurrence window" axis. So Combination A has a **temporal hole in C1 exactly where the guild is still absent.** That hole is real, and it is the strongest argument *for* eventually adding a C1 agent to A. My position is not that A should never have a C1 arm — it is that **UDCA is the wrong molecule to put in that hole, and E-C1 (§7.4) identifies the right one.**

### Synergy assessment — validated, and it is the strongest rationale in the analysis

**Mechanism: failure-mode complementarity.** §2.10 lists as ESTABLISHED that *"spores are the recurrence reservoir and are unaffected by current antibiotics."* Fidaxomicin's one acknowledged failure mode is that spores survive it. The LBP's mechanism is to restore the ecology that suppresses those spores' germination and outgrowth. **One agent's failure mode is the other's mechanism of action** — the strongest available form of combination rationale, and it is not merely additive.

**The temporal logic is independently clean.** Fidaxomicin's C8 sporulation suppression means the LBP faces a **static, non-replenishing** spore reservoir rather than a growing one. And live organisms must follow antibiotics, never accompany them (Rule 9; §2.8) — so the staging that pharmacology requires is the staging the biology already prefers.

**Confidence: HIGH on the pairing, and it is the only combination in this report where both components are approved *and* each has independent Phase 3-grade efficacy evidence in this exact sequence.** Combination A is, in substance, current best practice for the immunocompetent — which is both its strength (deployable now) and its limitation (it is not a differentiated development programme).

### The antagonism that removes UDCA

`p2-pathway.md` §6 Combination 2 flagged the engraftment question as "the key risk." The Integration Agent carried it forward as "test before adding." **I am going further: remove it from A now, and re-admit it only on a positive E-C1 result.** The argument is about asymmetry, not about probability.

| | UDCA's contribution to A | UDCA's risk in A |
|---|---|---|
| **Magnitude** | The Integration Agent's own words: *"UDCA is optional, not load-bearing"* — and it was included so that *"Combination A does not fail if Stage 0 kills UDCA"* | If UDCA suppresses the engrafting consortium, it degrades **C7 — the strong, load-bearing, only loop-exiting axis** |
| **Mechanism** | Pharmacological C1 cover during the guild-absent window | Bile acids broadly inhibit Clostridia by membrane detergency. The strains at risk are **specifically the bile-acid-metabolising Clostridia** (*C. scindens*, *C. hiranonis*, *C. hylemonae*) — i.e. **the organisms that constitute the C7 mechanism itself** |
| **Evidence** | UDCA at 5.5, "genuinely unresolved," LOW–MODERATE confidence; no human CDI efficacy data; IC₅₀ never measured | Direction is inferred, not measured. Bile-tolerance of VE303's eight strains and VOWST's spore population is **not established to be uniform** |

**The design conclusion follows from the shape of the payoff, not from the probability of harm.** A component described by its own advocate as *not load-bearing* cannot justify any exposure to *disabling the load-bearing component*. Even a modest chance of suppressing engraftment dominates a marginal, unmeasured C1 benefit. This is Rule 9 applied literally: **the live component's organisms are the mechanism, not passengers.**

There is a second, independent reason to remove it: a co-dosed UDCA arm would make Combination A's trial **uninterpretable on its own primary endpoint.** If recurrence rates come out worse than LBP alone, you cannot distinguish "UDCA is inactive" from "UDCA blocked engraftment" without the engraftment assay you skipped. Adding an optional component adds a confound to the trial of the component that matters.

**Countervailing consideration, stated honestly.** The removal costs Combination A the only *pharmacological* C1 coverage available to it, and C1 is the disease model's Tier 1 axis and its "most conspicuous unexploited target class." I am not dismissing that. §6.1 gives the resolution: the C1 arm should return to Combination A as **CamSA rather than UDCA**, because potency decouples receptor antagonism from detergency. E-C1 is the experiment that decides it, and it should be run with both molecules as arms.

### DDI and interaction risk

| Interaction | Assessment |
|---|---|
| **Fidaxomicin ↔ LBP** | **Temporal only** — fidaxomicin would kill the consortium if co-dosed. Resolved by the mandated d10 handoff. Note fidaxomicin's own microbiome-sparing profile makes it a *better* LBP partner than vancomycin: less guild damage to repair |
| **Systemic CYP/transporter** | **Minimal.** Fidaxomicin is minimally absorbed; LBPs are not systemically available. Per §3.3 this near-empty systemic DDI profile is a **safety asset** in this polypharmacy population |
| **Fidaxomicin ↔ P-gp** | Fidaxomicin *is* a P-gp substrate (cyclosporine raises C_max ~4×). Relevant to co-medications (cyclosporine, amiodarone, verapamil) but not to any component of A |
| **Warfarin** | §3.3: INR is destabilised by microbiome disruption via vitamin K₂. A combination that **restores** the microbiome will shift INR *back* — a real monitoring requirement, and in the beneficial direction. Flag for the protocol, not a veto |
| **PPIs (40–60% of this population)** | Alters gastric pH; matters for VOWST's pH-dependent capsule and for bowel prep. Formulation question, not a mechanism conflict |
| **Cholestyramine** | ⚑ See §7.2. Does not bind the LBP, but is a hard exclusion for any bile-acid arm — relevant if UDCA is later re-admitted |

**Overall DDI risk: LOW.** This is the cleanest interaction profile of any construction in this report.

### Verdict

> **VERDICT: RECOMMENDED as deployed clinical practice, with UDCA removed.**
> **CONFIDENCE: HIGH** on the fidaxomicin→LBP pairing; **HIGH** on the removal decision (which rests on payoff asymmetry, not on an unmeasured probability).
> **As a development programme: NOT DIFFERENTIATED.** Both components are approved and this sequence is broadly current practice. A owns no white space. It is the control arm against which B must win.

---

## 4. COMBINATION C — PRIMARY PREVENTION — **VALIDATED, RE-FRAMED**

I take C out of order because it is the least like a combination and because its correct evaluation is a methodological point that affects everything else.

```
═══════════════════════════════════════════════════════════
COMBINATION C: Ribaxamase during IV β-lactam therapy
═══════════════════════════════════════════════════════════

COMPONENTS:
  1. IV β-lactam (the PRECIPITANT, prescribed for a different infection)
  2. Ribaxamase (SYN-004) — oral, delayed-release β-lactamase enzyme
     — degrades biliary-excreted β-lactam in the intestinal lumen
     — axis C7 (#70 luminal antibiotic inactivation) — prevents LOOP ENTRY

COMBINATION TYPE: Toxicity mitigation — the fifth synergy mechanism in my
  skill file, and the ONLY construction in this analysis that uses it.
  Ribaxamase does not treat CDI. It removes the collateral toxicity of a
  drug given for something else, exactly as misoprostol does for an NSAID.
```

### The re-framing: axis count is the wrong instrument here

Ribaxamase covers **one axis**. Combination B2 covers **six**. On the pipeline's dominant metric, C loses decisively — and yet the Integration Agent's top single-programme recommendation is ribaxamase, and `p2-pathway.md` §6 calls #70 *"the cheapest unclaimed win in CDI."*

Both are right, because **axis coverage is a within-episode metric applied to a pre-episode intervention.** The C1–C8 map describes the causal structure of an *established* infection. Ribaxamase acts before any of it exists. Counting its axes against a treatment stack's axes is a category error — the equivalent of scoring a vaccine on how many pathological pathways it modulates in an infected patient.

**The correct comparison for a prevention asset** is *events prevented per patient treated*, which depends on attributable incidence in the exposed population and on the fraction of that incidence that is β-lactam-driven — **neither of which anyone in this pipeline quantified**, and the second of which is the Integration Agent's own counter-case #3.

**Why this matters beyond ribaxamase:** the pipeline's axis-count metric structurally under-rates every prevention asset, and prevention is unmet need #7 with no approved option. If the final synthesis carries the axis-coverage table forward as its headline scoring device, it will keep making this error. **Recommend the final report separate treatment constructions from prevention constructions and score them on different metrics.**

### Interaction analysis — and the question a clinician will ask first

C is unique in this report: it is the only construction combined with the **precipitating** drug rather than with the treatment. Its interaction surface is therefore with cefepime/piperacillin-tazobactam/ceftriaxone/carbapenems — not with vancomycin or fidaxomicin.

| Interaction | Assessment |
|---|---|
| ⚑ **Does ribaxamase compromise the β-lactam's treatment of the primary infection?** | **Mechanistically, no** — it acts on the fraction excreted into the intestinal lumen via bile, not on circulating drug, and the enzyme is not systemically absorbed. **But this is the first question any prescriber, formulary committee or reviewer will ask**, and a "no" that rests on compartmental separation needs measured systemic β-lactam PK ± ribaxamase to be credible. **This belongs in the diligence package (§7.4, E-C7) and I did not find it named in the pipeline's experiment lists** |
| **Spectrum ceiling** | Covers **β-lactams only.** Fluoroquinolone- and clindamycin-driven CDI are untouched. Integration counter-case #3, unquantified |
| **Co-dosed oral drugs** | An enzyme with a narrow substrate class has **no adsorptive interaction** with co-administered oral drugs. This is a genuine advantage over the adsorbent alternative — see below |
| **Systemic DDI** | Essentially nil. An orally delivered, non-absorbed enzyme. Per §3.3 and Safety §7.4, biologic modality and luminal confinement are **two independent routes to a clean DDI profile** |

### The spectrum-gap extension — and why it is a portfolio, not a combination

The obvious fix for the β-lactam-only ceiling is **DAV132** (colon-targeted activated charcoal), which adsorbs antibiotics **mechanism-agnostically** and therefore covers fluoroquinolones and clindamycin. It is tempting to propose ribaxamase + DAV132 as a broad-spectrum shield.

**I am not proposing that, and Rule 8 is why.** Activated charcoal adsorbs **indiscriminately** — including any oral drug co-administered with it, in an elderly polypharmacy population taking a median of many oral medicines (§3.3). Combining the two would also be **redundant on β-lactams** (Rule 1), paying twice for one class while stacking DAV132's adsorptive interaction burden onto ribaxamase's clean profile.

**The correct construction is class-directed selection, not combination:**

| Precipitating antibiotic | Shield | Reason |
|---|---|---|
| β-lactam (IV) | **Ribaxamase** | Substrate-specific enzyme; no adsorptive DDI; positive Phase 2b |
| Fluoroquinolone, clindamycin | **DAV132** | Only mechanism-agnostic option; accept the adsorptive DDI and the co-dosing schedule it forces |
| Both concurrently | Ribaxamase **or** DAV132, not both | Redundant on β-lactam; DAV132's DDI burden dominates |

That is a portfolio decision for the Clinical Feasibility Assessor, and it is the honest answer — proposing the two-agent shield would have inflated the coverage story while violating my own Rule 8.

### Verdict

> **VERDICT: VALIDATED as briefed. Highest-value single asset in the analysis, on a metric the pipeline's coverage map cannot express.**
> **CONFIDENCE: MODERATE on the strategic logic; LOW on the specifics** — the Phase 2b package was verified by nobody in this pipeline, and the diligence gate is the honest form of the recommendation.
> **Orthogonal to A and B; compatible with both.** C is not an alternative to the C1 backbone. They occupy two different loop-entry points (`p2-pathway.md` §1) and a portfolio holds both.
> **Two additions to the diligence list:** (i) systemic β-lactam PK ± ribaxamase, to answer the question every prescriber will ask (E-C7); (ii) the β-lactam-attributable fraction of CDI incidence in the target population, which sizes the addressable market and which nobody has quantified.
