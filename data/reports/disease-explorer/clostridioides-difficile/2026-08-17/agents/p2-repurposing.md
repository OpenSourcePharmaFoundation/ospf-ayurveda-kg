# Phase 2 — Drug Repurposing Strategist

**Disease:** *Clostridioides difficile* infection (CDI), primary focus **recurrent CDI (rCDI)**
**Agent:** Drug Repurposing Strategist (`.claude/skills/drug-repurposing-strategist/SKILL.md`, adapted from OM to CDI)
**Round:** Phase 2 — targeted deep dive, building on 6 Round 1 domain agents
**Date:** 2026-08-17 analysis set
**Evidence basis:** project CSV data (`data/processed/`) + disease model + Round 1 agent outputs + domain knowledge. **No live literature retrieval in this session.** Claims marked ⚠️verify are time-sensitive or regulatory-status-dependent and must be confirmed before external use.

---

## 0. Executive summary

**The single most important correction in this report:** my tasking, and the disease model's Appendix A.2, treat six items as an interchangeable "repurposing list." They are not. Only **four of them are approved drugs with a US Reference Listed Drug (RLD)**, which is the precondition for a 505(b)(2). Two of the six flagged leads — **ebselen** and **DAV132/ribaxamase** — are not approved anywhere and therefore have **no 505(b)(2) path at all**. "Prior human exposure" is not the same thing as an RLD, and Phase 2 safety data held by another sponsor cannot be relied upon without a right of reference. This single distinction reorders the list.

**Answer to the primary question (fastest 505(b)(2) path to patients):**

> **Immediate-release ursodiol (UDCA) at an already-approved dose, positioned as an add-on to standard-of-care antibiotic, with recurrence through week 8 as the primary endpoint.** Estimated **5–6 years, $45–75M**. It is the only candidate in the set for which *every non-biological barrier is already cleared*: RLD exists, dose sits inside the approved range, no CMC development, safety package fully transferable, and the trial design has 3-for-3 regulatory precedent (§3 of the Clinical Landscape report).

**But** — and this is the operative recommendation, not a caveat — the program should not start with Phase 2. It should start with a **$1–3M, 9–12 month fecal bile acid pharmacokinetic study in CDI patients**, measuring free UDCA and LCA in fecal water against the germination IC₅₀. That study resolves the ADMET agent's central objection (score C: "colonic delivery is enterohepatic spillover only; likely sub-therapeutic"), closes Round 1 gap #7, and costs under 4% of the program. If free colonic UDCA is an order of magnitude below the anti-germination IC₅₀, the entire UDCA thesis is dead and the money is saved. If it is at or above IC₅₀, UDCA becomes the best risk-adjusted asset in the CDI landscape.

**Second, a strategic reframing the repurposing lens forces:** the Clinical Landscape agent found that **6 of 12 CDI program failures were financial, not scientific**. Read as a repurposing strategist rather than a clinician, that is not a warning — it is a **shopping list**. CDI contains an unusual density of clinically de-risked, positive-Phase-2, financially orphaned assets: **ribaxamase** (Phase 2b positive, stalled for funding), **NTCD-M3** (Phase 2 positive, never advanced), **CP101** (Phase 2 positive, discontinued for financing). Acquiring one of these is faster and better-evidenced than repurposing most of the approved drugs on my list. **Ribaxamase scores 7.4/10 on my rubric — the highest score in this analysis** — and it is the only asset that addresses Tier 1 target #70 (luminal antibiotic inactivation), for which **no approved drug exists**.

**Third, new candidates surfaced (Q6).** Screening the project's 3,276-drug approved set plus domain knowledge against the four Tier 1 targets produced four approved drugs not on the flagged list:

| New candidate | Tier 1 target | Why it was missed |
|---|---|---|
| **Chenodiol (CDCA)** | #11 taurocholate-competitive germination | The disease model **names CDCA in the #11 target row** as a known compound with *Preclinical (strong)* validation — and then omits it from the A.2 repurposing list. It is an FDA-approved oral drug (CHEMBL240597, first approval 1983) |
| **Nitazoxanide** | #5/#2 (antibacterial), with **human CDI efficacy data** | Sits in §4.3 (alternatives), not §4.5 (failures) — it never failed, it was **never developed**. The only candidate in this whole set with existing human CDI efficacy data |
| **Hydroxychloroquine** | #41 v-ATPase / endosomal acidification (Module A) | The disease model names chloroquine/HCQ in the #41 row but the target sits outside Tier 1, so no agent picked it up. Its PK profile uniquely fits the compartment problem that killed ebselen and niclosamide |
| **Odevixibat / maralixibat (IBAT inhibitors)** | Delivery enabler for #11/#66 | Approved 2021, present in project data. **Carries a mechanistic veto — see §6.4.** Surfaced and then rejected, which is itself a useful result |

**Fourth, three mechanistic contradictions that the arithmetic in Round 1 could not see** (§7). The most consequential: **targets #46 (inhibit IL-23) and #47 (agonize IL-22) are mutually incompatible** — IL-23 is the principal driver of ILC3-derived IL-22. Ustekinumab, the drug flagged for #46, would suppress the protective axis the model asks us to augment. These two targets cannot both be pursued, and the Pathway Analyst should be asked to adjudicate.

---

## 1. Method: how the repurposing rubric was re-weighted for CDI

### 1.1 Why the skill file's rubric does not transfer

My skill file scores candidates on Target Overlap (25%), Mechanism Direction (20%), Safety (20%), Route (15%), Clinical Precedent (10%), Regulatory/IP (10%). That weighting encodes an assumption — that finding the right target–drug match is the hard part — which is **false in CDI**, for three documented reasons:

1. **Target matching is not the bottleneck.** §4.5 shows three narrow-spectrum antibacterials (surotomycin, cadazolid, ridinilazole) that hit correct, validated targets and all failed Phase 3. Ridinilazole even achieved non-inferiority with excellent microbiome data. The molecules worked; the *positioning* did not.
2. **Positioning is the bottleneck.** The Clinical Landscape agent's decisive finding: **replacement trials 0-for-3, add-on trials 3-for-3**. The same molecule scores differently depending purely on trial design. A rubric that scores molecules and not positions cannot see this.
3. **Money is the dominant failure mode.** Six of twelve §4.5 failures died of financing. My rubric weighted Regulatory/IP at 10% — roughly half of what CDI's empirical failure distribution justifies.

### 1.2 The CDI-adapted repurposing feasibility rubric

| # | Dimension | Weight | What it measures |
|---|---|---|---|
| 1 | **Compartment access** | 20% | Does the drug reach its *actual* target compartment intact and free? Uses the ADMET agent's three-compartment model (C1 luminal / C2 mucosal-intracellular / C3 systemic), not the luminal-vs-systemic binary |
| 2 | **Mechanism validation in CDI** | 15% | Strength of CDI-specific evidence, discounted per §A.3 (preclinical CDI efficacy predicts Phase 3 unusually poorly) |
| 3 | **Safety-package transferability** | 15% | Does the *existing* human safety data cover the CDI **dose, duration, and population**? Approval alone is not sufficient — the exposures must match |
| 4 | **Formulation / CMC gap** | 15% | Can the marketed formulation be used as-is, or is a new dosage form required? |
| 5 | **Regulatory path clarity** | 10% | Is an RLD available? 505(b)(2) vs 505(b)(1) vs BLA. Exclusivity earned |
| 6 | **Trial design & endpoint precedent** | 10% | Does the positioning inherit the 3-for-3 add-on precedent or the 0-for-3 replacement precedent? |
| 7 | **Commercial / funding viability** | 15% | COGS, sponsor economics, generic-erosion risk. Raised from 10% to 15% on the CDI failure distribution |

**Plus a binary VETO flag**, reported separately rather than folded into the arithmetic. A veto means a mechanistic or clinical contradiction that a weighted average structurally cannot express — for example, a drug whose mechanism points the wrong way against another Tier 1 target. Three candidates carry vetoes. **Reporting them as flags rather than as score deductions is deliberate**: it keeps the score interpretable as "how easy is the development path" and prevents the Candidate Ranker from silently double-counting a biology objection that other agents have already scored.

### 1.3 What this rubric does and does not measure — a note to the Candidate Ranker

This rubric measures **development-path feasibility**. It deliberately does not re-score disease biology, which the Disease Modeler, Target Profiler and Pathway Analyst already scored. A candidate can therefore score well here and poorly overall (aprepitant is the clearest case: an easy pathway to an endpoint nobody can define). **Do not sum my score with the Clinical Landscape agent's** — we are measuring overlapping things and both of us are, by construction, generous to approved drugs and harsh to discovery-stage chemistry. The Clinical Landscape agent flagged the same double-penalization risk for conessine; the same logic applies in reverse here.

---

## 2. Data provenance — what the project's own data could and could not answer

Per the skill file's guardrail ("cite data sources"), here is exactly what came from `data/processed/`.

### 2.1 Coverage

`chembl_approved_drugs.csv` (3,276 rows) **contains**: URSODIOL `CHEMBL1551` (1987) · CHENODIOL `CHEMBL240597` (1983) · DEOXYCHOLIC ACID `CHEMBL406393` · TAURURSODIOL `CHEMBL272427` · CHOLIC ACID `CHEMBL205596` · OBETICHOLIC ACID `CHEMBL566315` · NICLOSAMIDE `CHEMBL1448` (1982) · NITAZOXANIDE `CHEMBL1401` (2002) · APREPITANT `CHEMBL1471` (2003) · ODEVIXIBAT `CHEMBL4297588` (2021) · MARALIXIBAT `CHEMBL363392` (2021) · RIFAXIMIN `CHEMBL1617` · FIDAXOMICIN `CHEMBL1255800` · VANCOMYCIN `CHEMBL262777` · BERBERINE `CHEMBL295124`.

**Absent**: ebselen, ustekinumab, anakinra, ibezapolstat, bezlotoxumab, ramoplanin, teicoplanin, sucralfate, rebamipide, teduglutide, elobixibat, larazotide. Those were assessed knowledge-based. This matches the ADMET agent's coverage finding (6 of 10 candidates in project data).

`chembl_drug_mechanisms.csv` is **~10 rows** and `chembl_drug_targets.csv` **~40 rows** — both are OM-era stubs. **The systematic target-overlap workflow in my skill file (Strategy 1, steps 1–3) is not executable against this data for CDI.** Additionally, `disgenet__OM_*.csv` and `ttd_drug_target_genes.csv` are Oral-Mucositis-specific and contain nothing CDI-relevant (the TTD file has four rows, all OM). **Recommendation to the Data Scraper agent: the project has no CDI gene-disease or CDI target-drug dataset.** Every CDI target assignment in this pipeline currently rests on the disease model's hand-curated §5 master list, with no database backing. That is a structural gap worth logging.

### 2.2 Finding: the approved-drug set is stereochemistry-blind, and in CDI that is disqualifying

Bile acid activity in CDI is *entirely* a stereochemistry and hydroxylation-pattern story. Taurocholate is the germinant; CDCA and UDCA are competitive inhibitors; DCA and LCA are growth-inhibitory. These are the same atoms in different arrangements. The project data cannot tell them apart:

| Drug | CHEMBL ID | MW | AlogP | TPSA | HBD | HBA | InChIKey |
|---|---|---|---|---|---|---|---|
| CHENODIOL (CDCA) | CHEMBL240597 | 392.58 | 4.48 | 77.76 | 3 | 3 | `RUDATBOHQWOJDD-BSWAIDMHSA-N` |
| URSODIOL (UDCA) | CHEMBL1551 | 392.58 | 4.48 | 77.76 | 3 | 3 | `RUDATBOHQWOJDD-UZVSRGJWSA-N` |
| DEOXYCHOLIC ACID | CHEMBL406393 | 392.58 | 4.48 | 77.76 | 3 | 3 | `KXGVEGMKQFWNSR-LLQZFEROSA-N` |

**Three drugs, one descriptor row.** UDCA and CDCA differ only in the stereo layer of the InChIKey (`RUDATBOHQWOJDD` skeleton, 7α-OH vs 7β-OH); DCA is a positional isomer with, again, byte-identical 2D descriptors. Any descriptor-based or Lipinski-style similarity screen run over this dataset treats a germination inhibitor and a secondary bile acid as the same molecule, and would rank cholic acid — the precursor of the *germinant* — as a near neighbour of its own antagonists.

> **Instruction to the Chemist, SAR Analyst and Natural Product Scout:** for any bile-acid-class candidate in CDI, screen on **SMILES/InChI stereochemistry or 3D pharmacophore**, never on the tabulated descriptors. A 2D similarity hit in this chemical space carries essentially zero information about direction of effect. The ADMET agent independently noticed the same collision (its line 458, on ursodiol vs deoxycholic acid) — treating it as a data curiosity. It is not a curiosity; it is a methodology veto for this compound class.

### 2.3 Finding: physicochemical luminal screening does not find CDI drugs

I ran the obvious systematic screen — approved drugs with a luminal-confinement physicochemical profile (MW > 600 **or** TPSA > 150), which is the profile fidaxomicin (MW 1058) and vancomycin (MW 1449) share and which §6.2 tells us to reward. It returns **403 of 2,973 scorable drugs**, and the top of the list by TPSA is: diquafosol, gozetotide, trypan blue, paromomycin, streptomycin, dihydrostreptomycin, amikacin, amphotericin B, kanamycin, tobramycin, plazomicin, ceftolozane, ceftobiprole.

That is a list of **aminoglycosides, cephalosporins and diagnostic dyes** — every one of which would flatten the commensal Lachnospiraceae/Ruminococcaceae/Bacteroidetes guild that §6.4 identifies as the thing we must protect.

**This is a negative result worth recording explicitly.** It empirically confirms §6.4's assertion that colonic delivery is *necessary but nowhere near sufficient*, and that **selectivity, not delivery, is the binding constraint**. A physicochemical screen optimises for the easy half of the problem and is actively misleading if used alone. Any future repurposing screen in this project must filter on commensal-sparing spectrum *before* filtering on luminal physicochemistry — which, per Round 1 gap #8, **no candidate currently has measured data for**.

---

## 3. Question 1 — Which repurposing candidate has the fastest 505(b)(2) path?

### 3.1 First, the eligibility gate that reorders the list

A 505(b)(2) NDA relies for some portion of its evidence on data the applicant neither generated nor owns — in practice, FDA's prior finding of safety and effectiveness for a **listed drug (RLD)**, and/or adequate published literature. The mechanics that matter here:

- **An RLD must exist.** No listed drug, no reliance. (Literature-only 505(b)(2)s are accepted but rarely, and never for the nonclinical package.)
- **You inherit only the exposures the RLD's label covers.** If the CDI dose or duration exceeds the approved dose or duration, that increment needs its own nonclinical and clinical support. 505(b)(2) reduces the burden; it does not eliminate it.
- **A new dosage form is a full CMC program plus a bridging study.** For a locally-acting GI drug, plasma PK is a poor bridge — FDA has accepted combinations of local-concentration data and clinical endpoint studies for locally acting GI products (the delayed-release mesalamine precedent). That is a *favourable* wrinkle for a colon-targeted bile acid, and worth an early Type C meeting.
- **Exclusivity is 3 years**, not 5 — the moiety is not new. With QIDP's +5 that becomes **8 years**, as the Clinical Landscape agent correctly derived.

Applying the gate:

| Flagged lead | Approved? | US RLD available? | Available pathway |
|---|---|---|---|
| **UDCA (ursodiol)** | ✅ Yes (1987) | ✅ Yes — Actigall / Urso 250 / Urso Forte | **505(b)(2)** ✅ |
| **Aprepitant** | ✅ Yes (2003) | ✅ Yes — Emend | **505(b)(2)** ✅ |
| **Niclosamide** | ✅ Yes (1982) | ⚠️ **Uncertain** — US marketing discontinued; a "discontinued" listing can serve as RLD **only if** withdrawal was not for safety/efficacy reasons. Requires a formal listed-drug determination ⚠️verify | 505(b)(2), **contingent** |
| **Anakinra** | ✅ Yes | ❌ Biologic — **no 505(b)(2) exists for biologics** | BLA supplement / 351(a) |
| **Ustekinumab** | ✅ Yes | ❌ Biologic | BLA supplement |
| **Ebselen** | ❌ **Not approved anywhere** | ❌ **None** | **505(b)(1) full NDA** |
| **DAV132 / ribaxamase** | ❌ Investigational | ❌ None | BLA (ribaxamase, enzyme) / device-drug (DAV132) — **in-licensing, not repurposing** |

**Only three of the six flagged leads have a genuine 505(b)(2) path**, and one of those three (niclosamide) needs a regulatory determination before you know. The tasking's framing — "which repurposing candidate has the fastest 505(b)(2) path" — presupposes a race that four of the six entrants cannot enter.

### 3.2 The winner, and what the program actually looks like

**Immediate-release ursodiol, existing approved dose, add-on to fidaxomicin or vancomycin, primary endpoint = CDI recurrence through week 8.**

| Stage | Design | Duration | Cost |
|---|---|---|---|
| **Stage 0 — Fecal bile acid PK** *(the critical de-risking step)* | n≈20–30 CDI patients on SOC ± ursodiol 15 mg/kg/d; measure free UDCA, LCA, TCA in **fecal water** (not total fecal, not plasma); compare to anti-germination IC₅₀ | 9–12 mo | **$1–3M** |
| Pre-IND / Type B meeting | Agree 505(b)(2) reliance, endpoint, and whether fecal concentration is an acceptable dose-justification bridge | 4–6 mo (parallel) | $0.2M |
| **Phase 2** | n≈120–150, randomised, placebo-controlled add-on, recurrence through wk 8, toxin-confirmed adjudication | 18–24 mo | $8–15M |
| **Phase 3** | 1–2 trials, n≈250–300 each, same design | 30–36 mo | $30–60M |
| NDA + review | 505(b)(2), 3-yr exclusivity (8 with QIDP if granted) | 12–15 mo | $3–5M |
| **Total** | | **5–6 yrs** (Stage 0 partly parallel) | **$45–85M** |

These figures agree with the Clinical Landscape agent's independent estimate ($40–80M, 4–6 yrs) — arrived at by a different route, which is mild corroboration. **My addition is Stage 0**, which that report does not include and which I regard as non-optional.

**Why Stage 0 is non-optional.** The ADMET agent scored UDCA's colonic delivery a **C** and stated the colonic concentration at cholestatic dosing is "likely well short" of the effective range. That is the single largest uncertainty in the highest-ranked candidate in the entire pipeline, it is answerable for 3% of the program cost, and every downstream dollar is contingent on it. Running Phase 2 before Stage 0 would be spending $15M to learn something $2M could have told you.

Stage 0 should also measure **chenodiol** in a parallel arm (§6.1) and **taurocholate**, so the study simultaneously answers the UDCA-vs-CDCA potency question and the "is the germinant still present" question. Marginal cost of the extra arms is small relative to running a second study later.

### 3.3 The strategic fork nobody has stated: who pays?

Every top-ranked candidate here is a **cheap generic**. A 505(b)(2) on generic ursodiol earns 3 years of exclusivity on a molecule that costs pennies and is already prescribable off-label by any physician the day after the Phase 3 publishes. That is a **negative-NPV project for a commercial sponsor** — and CDI's dominant failure mode is precisely this. Naming the fastest scientific path without naming the funding route repeats the mistake that killed CP101, NTCD-M3, and ribaxamase.

| Fork | Description | Time / cost | Who funds it | Outcome |
|---|---|---|---|---|
| **A — Speed** | IR ursodiol, marketed formulation, no IP moat | **5–6 yrs, $45–85M** | **NIAID / BARDA / DoD / CARB-X / academic consortium**; possibly a payer or health-system-funded pragmatic trial | A guideline recommendation for a generic. Maximum patient benefit, zero commercial capture |
| **B — Defensibility** | Proprietary colon-targeted bile acid formulation (new dosage form), composition-of-matter + method-of-use IP | **7–9 yrs, $60–110M** | Specialty pharma / VC | An ownable product. Slower, and carries the PPI-defeats-pH-coating technical risk (ADMET cross-cutting obs. 8) |

**Recommendation: Fork A**, because the stated objective is *fastest path to patients*, not *best return*. But state the tradeoff plainly to whoever commissions this — Fork A will not attract industry capital, and a program with no owner is exactly how CDI assets die. The realistic Fork A sponsor is a government infectious-disease funder, and the pitch to them is unusually strong: an approved, off-patent, pennies-per-dose drug aimed at the highest-value unmet need (§4.6 #1) in a pathogen on FDA's qualifying-pathogen list.

### 3.4 Ranked "fastest path to patients"

| Rank | Asset | Path | Time to first patient in a pivotal trial | Total to approval | Cost | Confidence |
|---|---|---|---|---|---|---|
| **1** | **UDCA (ursodiol), IR, add-on** | 505(b)(2) | **~18 mo** (after Stage 0) | 5–6 yrs | $45–85M | High on pathway, **moderate on biology** |
| **2** | **Ribaxamase (in-license)** ⚑ *not a repurpose* | BLA | ~12–18 mo (Phase 3-ready) | 5–7 yrs | $80–150M + acquisition | Moderate — best human evidence in the set |
| **3** | **Chenodiol (CDCA), add-on** | 505(b)(2) | ~18–24 mo | 5–7 yrs | $50–90M | Moderate — better potency, worse safety |
| **4** | **Nitazoxanide, add-on to fidaxomicin** | 505(b)(2) | ~12–18 mo | 5–7 yrs | $45–85M | Moderate — best existing human CDI data, worst positioning |
| **5** | **Hydroxychloroquine, add-on** | 505(b)(2) | ~24–30 mo (needs in vitro + PK first) | 6–8 yrs | $50–90M | Low — hypothesis stage, one cheap experiment away from a verdict |
| **6** | **Colon-targeted UDCA (Fork B)** | 505(b)(2) new dosage form | ~40–48 mo | 7–9 yrs | $60–110M | Moderate |
| **7** | **Anakinra, fulminant CDI** | BLA supplement / IIT | Endpoint qualification first | ≥10 yrs | Unbounded | Low |
| **8** | **Aprepitant** | 505(b)(2) | Endpoint undefined | ≥8 yrs | Unbounded | Low — DDI profile is likely disqualifying |
| **9** | **Niclosamide** | 505(b)(2) contingent | ~48–60 mo (CMC first) | 7–10 yrs | $75–140M | Low |
| **10** | **Ebselen** | **505(b)(1) full NDA** | ~48–60 mo | 9–12 yrs | $125–225M | Low |
| — | **Ustekinumab** | BLA supplement | **Not recommended** — registry analysis only | n/a | $0.1–0.3M for the analysis | n/a |

---

## 4. Candidate reports

Format follows the skill file's Repurposing Candidate Report, adapted: "Target Overlap"→"Compartment access", "Route Compatibility"→"Formulation/CMC gap", plus explicit safety-transferability and commercial rows.

### 4.1 UDCA (URSODIOL) — `CHEMBL1551`

```
═══════════════════════════════════════════════════════════
REPURPOSING CANDIDATE: Ursodiol / UDCA (CHEMBL1551)
═══════════════════════════════════════════════════════════
ORIGINAL INDICATION: Primary biliary cholangitis (13–15 mg/kg/d);
                     radiolucent gallstone dissolution (8–10 mg/kg/d)
FIRST APPROVAL: 1987 (project data: chembl_approved_drugs.csv)
CDI TARGETS: #11 taurocholate-competitive germination block (Tier 1)
             #66 secondary bile acid supply/mimicry (Tier 1)
STRATEGY: Target-based + mechanism-based
FEASIBILITY SCORE: 6.9/10        VETO FLAGS: none
═══════════════════════════════════════════════════════════

COMPARTMENT ACCESS ......................................... 5/10
  Required compartment: C1 (luminal free) — the CspC germinant
  receptor is on the spore surface, in the lumen.
  Route: absorbed proximally + ileal ASBT → hepatic conjugation →
  biliary secretion → 50–80% ileal recapture per cycle. Only the
  SPILLOVER fraction reaches the colon. Enterohepatic recirculation
  is a system DESIGNED to prevent colonic bile acid delivery.
  ADMET agent verdict: C — "likely sub-therapeutic without
  colon-targeting."
  Favourable inversion (ADMET obs. 5): diarrhoea defeats ileal ASBT
  recapture, so colonic spillover INCREASES during active disease.
  Delivery is self-amplifying exactly when needed. This is the one
  candidate where §6.2's transit-time warning points backwards.
  → UNRESOLVED. This is what Stage 0 exists to answer.

MECHANISM VALIDATION IN CDI ................................ 6/10
  In vitro: inhibits taurocholate-mediated germination and vegetative
  growth [disease model §7.3, target #11].
  Human: case reports in recurrent CDI. No controlled trial.
  UNRESOLVED FORK (ADMET agent, formally posed to Pathway Analyst):
  is the effector UDCA itself, or LCA produced downstream by bai-guild
  7α-dehydroxylation? If LCA, UDCA depends on the exact enzymology CDI
  destroys — and the rational move is to deliver LCA directly.
  Discount per §A.3 (preclinical CDI evidence predicts Ph3 poorly).

SAFETY-PACKAGE TRANSFERABILITY ............................. 9/10
  Four decades of CHRONIC dosing at 13–15 mg/kg/d. A 10–12 week CDI
  course is a small fraction of the approved exposure — the safety
  package transfers almost completely. Benign profile.
  ⚠ DOSE CEILING — the constraint that caps this candidate:
  high-dose UDCA (28–30 mg/kg/d) in primary sclerosing cholangitis
  produced HARM — increased death/transplantation and serious adverse
  events vs placebo. You cannot answer a sub-therapeutic colonic
  concentration by simply escalating the dose. Practical ceiling
  ~20 mg/kg/d without inheriting that signal. ⚠verify
  ⚠ ENDPOINT CONFOUND — UDCA's most common adverse effect is
  DIARRHOEA, and CDI's primary endpoint is diarrhoea recurrence.
  Mitigations: toxin-confirmed adjudicated recurrence (already
  standard in CDI trials), blinded endpoint committee, and pre-specified
  analysis of stool frequency as a safety rather than efficacy variable.
  Manageable, but it must be designed in from the protocol synopsis.
  Do NOT co-administer with bile acid sequestrants (§6.2).
  Hepatic impairment is overrepresented in CDI (§3.2) and alters bile
  acid PK — stratify.

FORMULATION / CMC GAP ..................................... 10/10
  None. Marketed IR capsules and tablets, multiple generics.

REGULATORY PATH ............................................ 8/10
  Clean 505(b)(2). RLD: Actigall / Urso 250 / Urso Forte.
  Dose within approved range → maximal reliance on the RLD's finding.
  Exclusivity: 3 yrs (new indication), 8 yrs if QIDP granted.
  QIDP: ARGUABLE (Clinical Landscape §4.1) — anti-germination is
  antibacterial in effect, but a bile acid positioned as
  microbiome-restorative may not read as an antibacterial to FDA.
  Do not build the base case on QIDP.
  Orphan designation for rCDI specifically is plausible (§4.1) ⚠verify.

TRIAL DESIGN & ENDPOINT PRECEDENT .......................... 9/10
  Add-on to SOC, recurrence through wk 8 — the ECOSPOR III /
  PUNCH CD3 / MODIFY template. 3-for-3 approval precedent.
  Placebo-controlled, never withholds effective therapy.

COMMERCIAL / FUNDING ....................................... 3/10
  Pennies per dose. 3-year exclusivity on a molecule any physician can
  prescribe off-label the day the Phase 3 publishes. Negative NPV for
  industry. REQUIRES non-commercial funding (Fork A) or a proprietary
  formulation (Fork B). This is the failure mode that killed 6 of 12
  §4.5 programs and it applies squarely here.

═══════════════════════════════════════════════════════════
VERDICT: STRONG candidate — fastest path, contingent on one experiment
KEY ADVANTAGE: Every non-biological barrier already cleared
KEY RISK: Colonic free concentration may be an order of magnitude
          below IC50, and the dose ceiling blocks the obvious fix
NEXT STEP: Stage 0 fecal bile acid PK in CDI patients (n=20–30,
           $1–3M, 9–12 mo) with parallel chenodiol and taurocholate
           measurement. Go/no-go on the whole thesis.
═══════════════════════════════════════════════════════════
```

### 4.2 CHENODIOL (CDCA) — `CHEMBL240597` — **new candidate, Q6**

```
═══════════════════════════════════════════════════════════
REPURPOSING CANDIDATE: Chenodiol / CDCA (CHEMBL240597)
═══════════════════════════════════════════════════════════
ORIGINAL INDICATION: Radiolucent gallstone dissolution (13–16 mg/kg/d,
                     approved 1983); cerebrotendinous xanthomatosis
                     (project data indication_class confirms both)
CDI TARGETS: #11 (Tier 1) — the disease model NAMES "Chenodeoxycholate
             (CDCA)" in the #11 row, validation "Preclinical (strong)"
             #61 FXR (direction UNCERTAIN — see veto discussion)
STRATEGY: Target-based
FEASIBILITY SCORE: 6.5/10        VETO FLAGS: none, but see FXR note
═══════════════════════════════════════════════════════════

WHY THIS IS A FINDING: The disease model's own Tier 1 target row for
#11 lists CDCA as a known compound with the strongest preclinical
validation in that row — and then the A.2 repurposing pointer omits it.
CDCA is not a research chemical. It is an FDA-approved oral drug with
four decades of marketing history and an available RLD. It was missed
because the analysis inherited A.2's list rather than re-reading §5.

COMPARTMENT ACCESS ......................................... 6/10
  Same enterohepatic architecture as UDCA — spillover only. BUT CDCA
  is reported as the more potent taurocholate-competitive germination
  inhibitor (low-µM range vs UDCA's higher requirement) ⚠verify, so
  the same colonic concentration goes further. Scored one point above
  UDCA on that basis.
  ADVANTAGE OVER UDCA on the effector fork: the ADMET agent's central
  UDCA worry is that the active species may be LCA, requiring bai-guild
  7α-dehydroxylation that CDI has destroyed. CDCA does not have this
  problem — CDCA ITSELF is the named inhibitor at #11. Its downstream
  product is also LCA (also an inhibitor), so BOTH the parent and the
  metabolite are active and the missing enzymology is not a
  single point of failure. This is a genuine mechanistic advantage
  over UDCA that has not been noted anywhere in Round 1.

MECHANISM VALIDATION IN CDI ................................ 7/10
  Named in target #11, "Preclinical (strong)". No human CDI data — not
  even the case reports UDCA has.

SAFETY-PACKAGE TRANSFERABILITY ............................. 5/10
  This is where chenodiol loses to UDCA, and it loses badly.
  ⚠ HEPATOTOXICITY — dose-related serum aminotransferase elevation is
  chenodiol's characteristic, labelled toxicity ⚠verify. §3.2 notes
  hepatic impairment and cirrhosis are OVERREPRESENTED in the CDI
  population, and §3.3 describes heavy polypharmacy. This is the wrong
  toxicity in the wrong population.
  ⚠ DIARRHOEA in roughly 30–40% at gallstone-dissolution doses ⚠verify
  — materially worse than UDCA's rate, against a diarrhoea endpoint.
  Requires hepatic monitoring built into the protocol, and probably
  exclusion of Child-Pugh B/C — which removes a meaningful slice of the
  target population.

FORMULATION / CMC GAP ...................................... 9/10
  Marketed oral capsules/tablets.

REGULATORY PATH ............................................ 8/10
  505(b)(2), RLD available (Chenodal; Ctexli for CTX ⚠verify).
  Same 3-yr / 8-yr-with-QIDP arithmetic as UDCA.

TRIAL DESIGN & ENDPOINT PRECEDENT .......................... 9/10
  Identical add-on template.

COMMERCIAL / FUNDING ....................................... 3/10
  Small-market generic/orphan pricing. Same sponsor problem as UDCA.

FXR NOTE (not a veto, but flag to the Pathway Analyst):
  CDCA is the most potent endogenous FXR agonist. Target #61 (FXR) is
  marked "direction UNCERTAIN" in the disease model. FXR agonism
  represses CYP7A1 and shrinks the total bile acid pool — which could
  REDUCE downstream colonic secondary bile acids, i.e. work against
  target #66 while working for #11. The direction of the net effect is
  genuinely unknown and should be resolved before chenodiol advances
  past Stage 0.

═══════════════════════════════════════════════════════════
VERDICT: MODERATE-STRONG — the higher-potency germination play,
         with a materially worse safety fit
KEY ADVANTAGE: Better potency at #11; no dependence on the depleted
               bai guild (both parent and metabolite are active)
KEY RISK: Hepatotoxicity in a hepatically-impaired population;
          higher diarrhoea rate against a diarrhoea endpoint
NEXT STEP: Include as a parallel arm in the Stage 0 fecal PK study.
           Marginal cost is small; it converts a two-study question
           into one study. If CDCA's colonic free concentration clears
           IC50 and UDCA's does not, the program pivots to chenodiol
           with a hepatic-monitoring protocol.
═══════════════════════════════════════════════════════════
```

### 4.3 NITAZOXANIDE — `CHEMBL1401` — **new candidate, Q6**

```
═══════════════════════════════════════════════════════════
REPURPOSING CANDIDATE: Nitazoxanide (CHEMBL1401)
═══════════════════════════════════════════════════════════
ORIGINAL INDICATION: Cryptosporidiosis, giardiasis (approved 2002)
CDI TARGETS: bacterial (PFOR-class), Phase 2 outgrowth
STRATEGY: Phenotypic/clinical — this is the ONLY candidate in the
          entire pipeline with existing HUMAN CDI EFFICACY DATA
FEASIBILITY SCORE: 6.75/10       VETO FLAGS: none (positioning risk)
═══════════════════════════════════════════════════════════

WHY THIS WAS MISSED: nitazoxanide appears in disease model §4.3 as
"Alternative — comparable to metronidazole/vancomycin in small trials;
NEVER DEVELOPED for this indication." It sits in the alternatives
table, not the failures table. Every agent reading §4.5 for burned
approaches correctly skipped it; nobody read §4.3 as a repurposing
source. It did not fail. It was never funded — which is the same
disease that killed 6 of the 12 §4.5 programs, arriving one step
earlier in the lifecycle.

COMPARTMENT ACCESS ......................................... 7/10
  Oral; hydrolysed to tizoxanide, which is absorbed, but a substantial
  fraction of dose transits to the colon. Crucially, this does not
  need to be inferred: the small comparative CDI trials demonstrating
  activity comparable to vancomycin/metronidazole are direct human
  evidence that adequate luminal exposure is achieved. Highest-confidence
  compartment score in the set, because it rests on outcome rather
  than on physicochemistry.
  ⚠ Nitro group → §6.2 flags reducible groups at Eh ≈ −200 mV. But
  unlike niclosamide, nitazoxanide's PFOR-inhibition mechanism does not
  depend on preserving an intact nitroaromatic in the way niclosamide's
  does, and the human efficacy data empirically overrides the inference.
  Where clinical outcome and a chemical inference disagree, the outcome
  wins.

MECHANISM VALIDATION IN CDI ................................ 8/10
  Human comparative trial data — the highest evidence tier held by any
  candidate here, benchmarks excepted. Small and old, but human.
  Reported activity against sporulation and toxin production ⚠verify.

SAFETY-PACKAGE TRANSFERABILITY ............................. 8/10
  Approved 2002 including paediatric use; benign profile; short courses
  match the CDI duration. Transfers well.

FORMULATION / CMC GAP ...................................... 9/10
  Marketed 500 mg tablets and oral suspension. Usable as-is.

REGULATORY PATH ............................................ 8/10
  505(b)(2), RLD Alinia. QIDP eligible — it IS an antibacterial, so
  unlike UDCA and ebselen the GAIN premise straightforwardly holds.
  This is the only 505(b)(2)-eligible candidate for which QIDP is not
  arguable but clear, giving a real 8-year exclusivity.

TRIAL DESIGN & ENDPOINT PRECEDENT .......................... 5/10
  ⚠ THIS IS THE PROBLEM. Nitazoxanide's evidence base is a REPLACEMENT
  design (head-to-head vs vancomycin/metronidazole) — the 0-for-3 path.
  Repositioned as an add-on it inherits the 3-for-3 precedent, but the
  add-on RATIONALE is weaker for an antibacterial than for an
  anti-germinant or anti-toxin: adding a second antibacterial on top of
  fidaxomicin does not obviously reduce recurrence, and §4.5's synthesis
  is explicit that "killing C. difficile better is not the bottleneck."
  The honest framing: nitazoxanide's existing data support the endpoint
  that no longer matters, and it is unproven on the endpoint that does.

COMMERCIAL / FUNDING ....................................... 2/10
  Generic, cheap, and the reason it was never developed. Lowest
  commercial score in the set.

═══════════════════════════════════════════════════════════
VERDICT: MODERATE — best human evidence, worst strategic positioning
KEY ADVANTAGE: Human CDI efficacy already demonstrated; clean QIDP;
               no formulation work; genuinely cheap
KEY RISK: It is a me-too antibacterial, which is the single most
          reliably fatal profile in this disease (§4.5, 0-for-3)
NEXT STEP: Do NOT develop as a vancomycin replacement. If pursued,
           test whether it adds anything on RECURRENCE when layered on
           fidaxomicin — and require sporulation/toxin-suppression data
           to justify the add-on rationale before committing. Realistic
           sponsor is NIAID, not industry.
═══════════════════════════════════════════════════════════
```

### 4.4 EBSELEN — **not approved; no 505(b)(2)**

```
═══════════════════════════════════════════════════════════
REPURPOSING CANDIDATE: Ebselen (absent from project data)
═══════════════════════════════════════════════════════════
STATUS: NOT APPROVED IN ANY JURISDICTION. Prior Phase 2 exposure in
        stroke (Daiichi, 1990s, Japan) and as SPI-1005 (Sound
        Pharmaceuticals — Ménière's, noise-induced hearing loss,
        tinnitus, COVID). ⚠verify
CDI TARGET: #26 TcdB cysteine protease domain (Tier 1) — the best
            small-molecule anti-toxin lead in the disease model
FEASIBILITY SCORE: 4.0/10        VETO FLAGS: none formally, but the
                                 ADMET chemistry objection is close
═══════════════════════════════════════════════════════════

THE REGULATORY CORRECTION — this is the headline for ebselen:
My tasking asks for "the fastest CDI development path" and cites
"extensive Phase 2 safety data." Both halves need qualification.
  • There is NO RLD. Ebselen is not a listed drug. A 505(b)(2) requires
    reliance on FDA's prior finding for a listed drug, or on adequate
    published literature. Neither is available.
  • The Phase 2 safety data belongs to OTHER SPONSORS. Without a right
    of reference it cannot be cited in a marketing application. It is
    scientifically informative and regulatorily inert.
  • Therefore ebselen requires a FULL 505(b)(1) NDA: complete nonclinical
    package at CDI dose and duration, CMC, Phase 1, Phase 2, Phase 3.
  • QIDP is DOUBTFUL (Clinical Landscape §4.1) — ebselen is anti-toxin,
    not antibacterial, and GAIN requires an antibacterial.
  Prior human exposure buys perhaps 12–18 months of Phase 1 risk
  reduction and a better-informed starting dose. It does not buy the
  four-plus years the "repurposing" framing implies.
  ESTIMATE: 9–12 years, $125–225M.

CAN AN ORAL FORMULATION ACHIEVE ADEQUATE COLONIC CONCENTRATION?
  Delivery is not the limiting step, and framing it as a formulation
  question misdiagnoses the problem. Ebselen is practically insoluble
  in water (BCS II/IV) — which means most of an oral dose is NOT
  absorbed and therefore DOES reach the colon. You can put grams of
  ebselen into the colonic lumen.
  What you cannot do is have it arrive intact and free:
   (1) DISSOLUTION — free concentration is capped by aqueous solubility,
       regardless of mass delivered.
   (2) THIOL QUENCHING — the entire mechanism is Se–S exchange. The
       colon is a thiol-saturated reducing sink (Eh ≈ −200 mV, mM
       cysteine and glutathione, plus H2S from sulfate-reducing
       Desulfovibrio). Ebselen is converted to ebselen-selenol and mixed
       selenosulfides before crossing the mucus layer. Unlike
       metronidazole, where reduction IS the mechanism, here reduction
       is pure inactivation.
   (3) WRONG COMPARTMENT — the CPD target is triggered by CYTOSOLIC
       InsP6, inside the colonocyte (C2). Luminal delivery is not even
       the right destination.
   (4) THE SYSTEMIC RESCUE FAILS THE SAME WAY — delivering ebselen
       basolaterally would bypass the luminal thiol sink, but plasma is
       also thiol-rich and ebselen binds albumin Cys34 essentially
       quantitatively (>99%). Both routes are blocked by one chemistry.
  (Analysis (1)–(4) is the ADMET agent's; I concur and add only that it
  makes the FORMULATION question moot — no delivery system fixes a
  molecule that is consumed by the medium it must cross.)

═══════════════════════════════════════════════════════════
VERDICT: WEAK as a repurposing candidate; EXCELLENT as a tool compound
KEY ADVANTAGE: Validates a Tier 1 target with in vivo mouse efficacy
KEY RISK: No RLD, no accessible safety package, no QIDP, and a warhead
          the target compartment destroys
NEXT STEP: Stop treating ebselen as a development candidate. The fast
           path in this space belongs to the TARGET (#26), not to this
           molecule. Hand to the SAR Analyst as a warhead-replacement
           problem — a non-selenium, lower-promiscuity covalent or
           reversible CPD inhibitor inherits the validated mechanism
           without the quenching. Keep ebselen as the benchmark probe
           in the assay. (Concurs with ADMET and Chemist.)
═══════════════════════════════════════════════════════════
```

### 4.5 NICLOSAMIDE — `CHEMBL1448`

```
═══════════════════════════════════════════════════════════
REPURPOSING CANDIDATE: Niclosamide (CHEMBL1448, first approval 1982)
═══════════════════════════════════════════════════════════
ORIGINAL INDICATION: Anthelmintic (tapeworm) — 2 g single chewable dose
CDI TARGET: #30 TcdB delivery/pore-forming domain, entry blockade
            [EMERGING]
FEASIBILITY SCORE: 3.85/10       VETO FLAGS: none formal; three serial
                                 preclinical kill-risks
═══════════════════════════════════════════════════════════

Q: COULD IT BE REPOSITIONED WITH THE EXISTING FORMULATION?
   NO — and the reason is instructive. Yomesan's 2 g chewable tablet is
   engineered for a single-dose, purely luminal, contact-killing effect
   on a tapeworm scolex. Poor dissolution is a FEATURE of that product.
   For CDI the drug must dissolve, cross mucus, and enter a colonocyte.
   Niclosamide's intrinsic aqueous solubility is ~1.6 µM (≈0.5 µg/mL)
   at neutral pH — at or below the concentration range where TcdB entry
   blockade is reported. The marketed formulation delivers mass without
   delivering free drug. Multiple modern solubility-enabling programs
   (COVID-era) attempted this and struggled. ⚠verify

THE GAP TO A CDI INDICATION — four separate problems, any one fatal:
  1. SOLUBILITY. Requires an enabling formulation: amorphous solid
     dispersion, nanocrystal, salt/co-crystal, or a soluble prodrug.
     That is a NEW DOSAGE FORM 505(b)(2): full CMC + bridging study,
     24–36 months and $10–20M BEFORE Phase 2 opens.
  2. RLD UNCERTAINTY. US marketing was discontinued (Niclocide). A
     discontinued listing can serve as an RLD only if withdrawal was not
     for safety or effectiveness reasons. This needs a formal listed-drug
     determination from FDA — a concrete, cheap, and necessary first
     action that nobody has taken. ⚠verify
  3. NITRO REDUCTION. §6.2: reducible groups are reduced at Eh ≈ −200 mV.
     Reduction of the 5-nitro to the amine plausibly destroys the
     pharmacophore. Settleable by one anaerobic stability assay.
  4. WRONG COMPARTMENT + WRONG SELECTIVITY. The target is intracellular
     (C2), requiring three serial low-efficiency steps. And niclosamide's
     actual primary pharmacology is PROTONOPHORE / mitochondrial
     uncoupling — a non-selective mechanism that will uncouple commensal
     bacteria and colonocytes alongside anything else. Against §6.4's
     central constraint (selectivity for C. difficile over the commensal
     guild), a protonophore is close to the worst possible profile.

  Note the shape of this: three of the four are answerable by cheap
  benchtop experiments (anaerobic stability, dissolution in fecal water,
  colonocyte uptake) and one by a letter to FDA. Total cost well under
  $500k. Niclosamide does not need a development decision; it needs
  a de-risking package that will probably kill it.

SCORES: compartment 2 · mechanism 4 · safety-transfer 6 (single-dose
        anthelmintic history does not cover 10-day repeat dosing at
        the exposures needed) · formulation 2 · regulatory 5 ·
        trial design 7 · commercial 3

═══════════════════════════════════════════════════════════
VERDICT: WEAK — the "poor absorption is a CDI advantage" argument is
         backwards for this molecule
KEY ADVANTAGE: Cheap, approved somewhere, and the failure modes are
               all cheaply testable
KEY RISK: Its low solubility, which the tasking frames as an asset, is
          the primary obstacle — the target is inside the cell
NEXT STEP: Spend $200–400k on the three benchtop experiments and the
          FDA listed-drug letter before spending anything else. Expect
          a negative. (Concurs with ADMET; adds the RLD determination
          and the protonophore-selectivity objection.)
═══════════════════════════════════════════════════════════
```

### 4.6 APREPITANT — `CHEMBL1471`

**Score 5.10/10. VETO FLAG: DDI in the target population.**

Compartment 7 (systemic; reaches the host NK1R target adequately) · Mechanism 3 (preclinical only in CDI; #51 is not Tier 1) · Safety-transfer 4 · Formulation 8 (oral capsule + IV fosaprepitant both marketed) · Regulatory 7 (clean 505(b)(2), RLD Emend; QIDP **ineligible** — host-directed) · Trial design 3 · Commercial 3.

Two things sink it, and neither is fixable by better development:

1. **The DDI profile is disqualifying in this specific population.** Aprepitant is a CYP3A4 substrate *and* a moderate CYP3A4 inhibitor. §3.3's DDI checklist for CDI patients leads with **tacrolimus, cyclosporine, warfarin, digoxin, DOACs** — and the population is elderly, renally impaired, and heavily polypharmaceutical. Aprepitant's DDI profile is thoroughly characterised precisely *because* it is clinically consequential. The disease model spends §6.4 explaining that CDI's great pharmacological advantage is that luminal drugs have near-zero DDI risk; aprepitant discards that advantage for a preclinical-only target.
2. **There is no endpoint.** The Clinical Landscape agent classes host-directed adjuncts with no endpoint precedent as "**unbounded** — endpoint risk dominates." Aprepitant's plausible effect (reduced secretion and neurogenic inflammation) would manifest as symptom improvement, which is not what CDI approvals are granted on.

Additionally the approved exposure is a **3-day antiemetic course**; CDI needs 10+ days, so even the safety package only partially transfers.

**Verdict: NOT RECOMMENDED.** Its 5.10 score reflects an easy regulatory pathway to a destination nobody can define — exactly the artefact §1.3 warns the Candidate Ranker about. **Do not read 5.10 as "middling but viable."**

### 4.7 ANAKINRA and USTEKINUMAB — the host-directed biologics

Neither has a 505(b)(2) path: **biologics are licensed under the PHS Act, and 505(b)(2) does not exist for them.** The route is a BLA supplement (sponsor-controlled) or an investigator-initiated trial under an IND. That alone removes both from the "fastest 505(b)(2)" question.

**ANAKINRA — score 4.95/10.** Target #45 (IL-1β/IL-1R), Tier 2.

Anakinra has one genuine and underappreciated advantage for an *infection* indication: a **4–6 hour half-life**. Unlike every other biologic immunomodulator, its effect can be switched off within a day if the infection worsens. In a disease where TNF blockade is itself a CDI risk factor (#49, *Clinical negative*), reversibility is not a minor convenience — it is the property that makes cytokine blockade thinkable at all here. On drug-property grounds anakinra is clearly the better of the two biologics.

But the positioning is the worst available: the plausible indication is **fulminant CDI**, which §4.6 lists as unmet need #6 and which the Clinical Landscape agent scores as having **no endpoint precedent, 8–15 year timelines, and consent-impaired, slow-accruing enrolment**. Daily subcutaneous injection in frail elderly patients adds an administration burden. Evidence is preclinical only.

*Recommendation:* not a development candidate for this pipeline. If host-directed therapy is pursued at all, anakinra in fulminant CDI with **colectomy-free survival** as the endpoint is the most defensible version — as an academic investigator-initiated trial, framed honestly as a decade-long, high-risk effort to open an empty category (§4.6 #8).

**USTEKINUMAB — score 4.30/10. VETO FLAG: mechanism points the wrong way.**

Q5 asks whether there is clinical signal for anti-recurrence benefit in CDI+IBD patients. **I am aware of no powered analysis, and I will not manufacture one.** What can be said:

- The consistent IBD-literature signal is that ustekinumab carries a **lower serious-infection rate than anti-TNF**. That is a statement about infections in general, not evidence of an anti-CDI-recurrence effect.
- Any observational signal in this population would be dominated by **confounding by indication** — patients on ustekinumab differ systematically in disease control, steroid exposure, and prior biologic failure from those who are not.
- **The mechanistic problem is worse than the evidentiary one.** See §7.1: IL-23 is the principal driver of ILC3-derived IL-22, and target #47 instructs us to **AGONIZE** IL-22 as a protective epithelial axis. Ustekinumab (anti-p40, blocking IL-12 *and* IL-23) would **suppress IL-22**. The disease model asks for opposite interventions at #46 and #47 and does not notice.
- **PK does not match the disease timescale.** Ustekinumab dosing is IV induction then SC every 8–12 weeks. The rCDI recurrence window is 8 weeks. A drug you cannot titrate within the event window is a poor tool for modifying events inside it.
- Commercially: biosimilars have entered ⚠️verify, which improves COGS and simultaneously removes any sponsor's incentive to fund a new indication.

*Recommendation:* **Not a development candidate.** The right action is a **retrospective cohort analysis in IBD biologic registries** — is CDI recurrence lower on ustekinumab than on anti-TNF or vedolizumab, adjusted for disease activity and steroid exposure? Cost **$100–300k, 6–9 months**. It either produces a signal worth a prospective look or closes the question permanently. That is the correct disposition for a hypothesis this cheap to test and this expensive to develop.

### 4.8 HYDROXYCHLOROQUINE — **new candidate, Q6**

**Score 6.35/10. VETO FLAGS: none. Status: hypothesis, one experiment from a verdict.**

Target **#41 — v-ATPase / endosomal acidification**, required for TcdB translocation. The disease model names "Bafilomycin A1, **chloroquine/hydroxychloroquine**, ammonium chloride" in that row (§5.3) with *Preclinical* validation. #41 sits outside Tier 1, so no Round 1 agent picked it up — but as a *repurposing* target it is unusually attractive, because unlike most Module A targets it has an approved, generic, oral drug pointing at it.

**Why it deserves a look — it solves the compartment problem that killed ebselen and niclosamide.** The ADMET agent's most important structural finding was that ebselen and niclosamide are **C2 candidates** (target inside the colonocyte) being scored on **C1 criteria** (luminal retention), and that both fail because they cannot get from lumen to cytosol. HCQ inverts this entirely:

- It is **well absorbed and reaches the colonocyte basolaterally** — no mucus layer, no dissolution step, no luminal thiol sink.
- It has an enormous volume of distribution and, as a lipophilic weak base, **concentrates specifically in acidic organelles** — it accumulates in the exact compartment it must act on. Very few drugs have a distribution profile that matches their target organelle this well.
- The marketed tablet is usable as-is; it is generic and cheap.

**Why it might not work:** the endosomal pH shift required to block TcdB translocation may exceed what is achievable at clinically tolerated plasma concentrations. This is the whole question, and it is answerable in vitro for a few tens of thousands of dollars.

**Safety in this specific population:** the vast HCQ safety database is reassuring in general but has one sharp edge here. HCQ prolongs QT; CDI patients are elderly and, from profuse diarrhoea, frequently **hypokalaemic** — and hypokalaemia potentiates QT prolongation. Retinopathy is a cumulative-dose toxicity and irrelevant for a 10-week course. So: ECG and potassium monitoring, and exclusion of patients on other QT-prolonging agents. Manageable, but real.

Scores: compartment 7 · mechanism 4 · safety-transfer 7 · formulation 10 · regulatory 8 (505(b)(2), RLD Plaquenil; QIDP ineligible — host-directed) · trial design 7 (add-on; bezlotoxumab establishes the anti-toxin add-on principle, though not for a host-directed agent) · commercial 2.

**Next step:** a single in vitro experiment — does HCQ, at concentrations achievable in colonic mucosa at standard oral doses, block TcdB-induced cell rounding in a colonocyte line? Cost ~$30–60k, 2–3 months. If yes, HCQ becomes a genuinely fast add-on candidate. If no, it is closed. **This is the cheapest high-information experiment in the entire Phase 2 analysis** and I recommend it regardless of what else the pipeline pursues.

### 4.9 RIBAXAMASE (in-licensing reference) — Tier 1 target #70

**Score 7.4/10 — highest in this analysis. Not a repurpose: an acquisition.**

I include it because §6.4 below concludes that **no approved drug addresses Tier 1 target #70**, and because the honest answer to "fastest path to patients" has to consider transactions other than repurposing.

Ribaxamase (SYN-004, Theriva) is an **orally delivered β-lactamase** that degrades residual IV β-lactam antibiotic in the intestinal lumen before it can destroy the microbiota — primary prevention of the dysbiosis that permits CDI. Status: **Phase 2b positive, stalled for funding** (Clinical Landscape §2.3).

Scores: compartment 9 (delayed-release oral capsule, acts in the lumen, delivery already demonstrated clinically) · mechanism 8 (**positive human Phase 2b** — the strongest evidence in this entire report) · safety-transfer 7 · formulation 8 (already developed) · regulatory 6 (BLA, enzyme biologic; addresses §4.6 unmet need #7, primary prevention, for which no approved option exists) · trial design 8 (prevention trial in patients receiving IV β-lactams; endpoint is new-onset CDI — clean, and not competing against an 80–90%-effective generic) · commercial 5 (large prevention market, difficult payer logic, **but the asset is cheap precisely because its sponsor ran out of money**).

**The strategic point:** the Clinical Landscape agent identified that 6 of 12 CDI failures were financial. Read from a repurposing seat, an unusually high density of *clinically de-risked, financially orphaned* assets is a market inefficiency — the same information that reads as "this field is a graveyard" to a clinician reads as "positive Phase 2 data is available below replacement cost" to a business developer. Ribaxamase, NTCD-M3, and CP101 all fall in this category. **A serious CDI strategy should evaluate acquiring one of these alongside — probably ahead of — repurposing a generic bile acid.**

---

## 5. Consolidated scoring

### 5.1 Dimension scores

| Candidate | Compart. (20%) | Mech (15%) | Safety-xfer (15%) | Formul. (15%) | Reg (10%) | Trial (10%) | Comm. (15%) | **Weighted** | Veto |
|---|---|---|---|---|---|---|---|---|---|
| **Ribaxamase** *(in-license, ref.)* | 9 | 8 | 7 | 8 | 6 | 8 | 5 | **7.40** | — |
| **UDCA (ursodiol)** | 5 | 6 | 9 | 10 | 8 | 9 | 3 | **6.90** | — |
| **Nitazoxanide** | 7 | 8 | 8 | 9 | 8 | 5 | 2 | **6.75** | — |
| **Chenodiol (CDCA)** | 6 | 7 | 5 | 9 | 8 | 9 | 3 | **6.50** | — |
| **Hydroxychloroquine** | 7 | 4 | 7 | 10 | 8 | 7 | 2 | **6.35** | — |
| **UDCA + IBAT inhibitor** | 9 | 3 | 6 | 6 | 5 | 7 | 4 | **5.85** | ⚑ **YES** |
| **Aprepitant** | 7 | 3 | 4 | 8 | 7 | 3 | 3 | **5.10** | ⚑ **YES** (DDI) |
| **Anakinra** | 7 | 4 | 6 | 6 | 5 | 2 | 3 | **4.95** | — |
| **Ustekinumab** | 6 | 2 | 6 | 6 | 4 | 3 | 2 | **4.30** | ⚑ **YES** (IL-22) |
| **Ebselen** | 2 | 7 | 4 | 3 | 2 | 7 | 4 | **4.00** | — |
| **Niclosamide** | 2 | 4 | 6 | 2 | 5 | 7 | 3 | **3.85** | — |

### 5.2 Landscape summary

| Rank | Drug | Strategy | Score | Tier 1 target | Key advantage | Key risk | Disposition |
|---|---|---|---|---|---|---|---|
| 1 | **Ribaxamase** | In-license | 7.4 | #70 | Positive human Phase 2b; only asset at #70 | Not a repurpose; BLA; payer logic | **Evaluate acquisition** |
| 2 | **UDCA** | Target-based | 6.9 | #11, #66 | Every non-biological barrier cleared | Colonic conc. may be sub-IC₅₀; dose ceiling | **Pursue — Stage 0 first** |
| 3 | **Nitazoxanide** | Phenotypic | 6.75 | — (Phase 2) | Only candidate with human CDI efficacy data | Me-too antibacterial = 0-for-3 profile | **Conditional — reposition or drop** |
| 4 | **Chenodiol** | Target-based | 6.5 | #11 | Higher potency; no bai-guild dependence | Hepatotoxicity in a hepatically-impaired population | **Pursue as Stage 0 parallel arm** |
| 5 | **Hydroxychloroquine** | Target-based | 6.35 | — (#41) | Solves the C2 compartment problem | Achievable endosomal pH shift unproven | **One in vitro experiment** |
| 6 | **UDCA + IBAT** | Combination | 5.85 | #11 delivery | Definitively solves colonic delivery | ⚑ Shunts taurocholate (the germinant) too | **Preclinical question only** |
| 7 | **Aprepitant** | Target-based | 5.10 | — (#51) | Easy pathway | ⚑ DDI disqualifying; no endpoint | **Do not pursue** |
| 8 | **Anakinra** | Mechanism | 4.95 | — (#45) | Short t½ = reversible during infection | No endpoint in fulminant CDI | **IIT only, if at all** |
| 9 | **Ustekinumab** | Mechanism | 4.30 | — (#46) | Already used in CDI+IBD | ⚑ Suppresses protective IL-22; PK too slow | **Registry analysis only** |
| 10 | **Ebselen** | Target-based | 4.00 | #26 | Validates the best anti-toxin target | No RLD → full NDA; warhead destroyed in colon | **Tool compound, not candidate** |
| 11 | **Niclosamide** | Target-based | 3.85 | — (#30) | Cheap failure modes to test | Solubility, nitro reduction, protonophore | **$300k kill-or-cure package** |

---

## 6. Question 6 — approved drugs NOT on the list, by Tier 1 target

### 6.1 #7/#11 — CspC / taurocholate-competitive germination inhibition

| Drug | Status | Assessment |
|---|---|---|
| **Chenodiol (CDCA)** | ✅ Approved 1983 | **The find.** Named in the #11 target row with *Preclinical (strong)* validation; omitted from A.2. Full report §4.2 |
| **Obeticholic acid** | ✅ Approved 2016 | **Reject.** Semi-synthetic CDCA analog and potent FXR agonist, but carries a hepatotoxicity warning and use restrictions in cirrhosis ⚠️verify. §3.2 flags hepatic impairment as overrepresented in CDI. Wrong toxicity, wrong population |
| **Taurursodiol** | ✅ Approved 2022 (`CHEMBL272427`) | **Marginal.** Tauro-conjugated UDCA. Conjugation improves solubility but the taurine conjugate is *more efficiently recaptured* by ileal ASBT, plausibly worsening colonic delivery. Worth including as a Stage 0 analytical comparator, not as a candidate |
| **Cholic acid, deoxycholic acid** | ✅ Approved | **Reject.** Cholic acid is the germinant precursor — wrong direction. DCA is growth-inhibitory but is a colonic carcinogen risk on chronic exposure and has no oral formulation for this purpose (approved as an injectable for submental fat) |
| **LCA or non-convertible LCA analog** | ❌ Not approved | The ADMET agent's suggestion, and mechanistically the cleanest answer if LCA proves to be the effector. **No approved product exists** — this would be a discovery program, not a repurpose |

**Net:** the germination space contains exactly **two** viable approved drugs — ursodiol and chenodiol — and they are stereoisomers of each other. That is a thin bench, and it is why Stage 0 should test both.

### 6.2 #26 — TcdB CPD covalent inhibition

**No approved drug hits this target.** I checked the obvious adjacent chemotypes:

- **Auranofin** (approved 1985, `CHEMBL1366`) — a gold(I) thiol-reactive compound named alongside ebselen at target #21 (Stickland selenoproteins). It fails for **exactly the same reason as ebselen**: it is a soft metal electrophile whose mechanism is thiol exchange, deployed into a millimolar-thiol, H₂S-rich, −200 mV lumen. Same quenching, same non-selectivity, and gold adds nephrotoxicity and blood dyscrasias. **Reject** — and note that the failure of *two* independent thiol-reactive chemotypes for the same reason strengthens the ADMET agent's argument from an inference about one molecule to a **class-level rule: soft-electrophile covalent chemistry is not viable in the CDI colonic lumen.** That rule should be recorded for the SAR Analyst, because it constrains the warhead-replacement search: the replacement warhead must be one that resists exchange with abundant small-molecule thiols, which rules out most of the standard covalent toolkit and points toward reversible-covalent or non-covalent designs.
- **Disulfiram** (approved 1951, `CHEMBL964`) — thiol-reactive disulfide. Same objection, plus §6.2 explicitly flags disulfides as unstable in this environment, plus a disulfiram–alcohol reaction. **Reject.**

**Net: #26 has no approved-drug repurposing option.** It is a medicinal chemistry program.

### 6.3 #70 — luminal antibiotic inactivation

**No approved drug hits this target.** Options considered:

- **Activated charcoal** — approved/OTC adsorbent, and the mechanistic ancestor of DAV132. But non-selective: it would adsorb the CDI-treatment antibiotic (fidaxomicin, vancomycin) alongside the inciting one. DAV132's entire engineering effort is a colon-targeted release designed to avoid precisely this. Off-the-shelf charcoal is not a shortcut to DAV132; it is the thing DAV132 exists to improve on. **Reject.**
- **β-lactamase inhibitors** (clavulanate, `CHEMBL777`, present in project data) — **wrong direction.** These *preserve* β-lactam activity; #70 requires *destroying* it in the lumen. A textbook mechanism-direction error of the kind my skill file's guardrails warn about, and worth recording as the clean example.
- **Oral β-lactamase enzyme** — no approved product. Ribaxamase is the asset, and it is investigational.

**Net: #70 is the clearest white space in the disease. It has clinical proof-of-concept (Phase 2b positive), no approved drug, and no active sponsor.** That combination is unusual and is the basis of the §4.9 in-licensing recommendation.

### 6.4 #64/#66 — secondary bile acid restoration, and the IBAT inhibitor idea

The ADMET agent asked (its line 431): *"Would UDCA + an ASBT inhibitor (odevixibat/elobixibat class) deliberately deliver therapeutic bile acid concentrations to the colon? Both components are approved."*

The premise checks out — **odevixibat** (`CHEMBL4297588`, 2021) and **maralixibat** (`CHEMBL363392`, 2021) are both in the project's approved-drug data. And the delivery logic is sound: IBAT/ASBT inhibitors block ileal bile acid recapture, which by design shunts bile acids into the colon. It is a *pharmacological* colon-targeting mechanism, which means it does not depend on a pH-sensitive coating (defeated by the PPIs this population is universally on) or on microbiota-triggered release (defeated by the dysbiosis itself). On delivery grounds it scores 9/10 — the best in this report.

**⚑ VETO — and it is the reason this attractive idea should not advance:**

1. **It shunts the germinant along with the anti-germinant.** ASBT is not selective for UDCA. Blocking it delivers the *entire* bile acid pool to the colon — including **taurocholate, the primary germinant and the ligand at target #11 that UDCA is meant to competitively displace**. You would be raising the concentration of both the inhibitor and the substrate it competes with, and the net effect on germination depends on a ratio nobody has measured. It could plausibly be *worse* than baseline.
2. **The dose-limiting toxicity of IBAT inhibitors is diarrhoea.** In a disease defined by diarrhoea, with diarrhoea as the endpoint. This is the third time in this report that a candidate's principal adverse effect collides with the primary endpoint (UDCA, chenodiol, now IBAT inhibitors) — a pattern worth naming: **bile acid pharmacology and CDI share an adverse-event axis, and every bile-acid-directed CDI program will have to defend against it.**
3. **Commercial arithmetic.** Odevixibat and maralixibat are on-patent, orphan-priced products. Combining a pennies-per-dose generic with an orphan-priced biologic-adjacent drug destroys the one advantage the UDCA thesis has (cost), while roughly doubling the 505(b)(2) burden (two RLDs, combination rule, DDI studies, dose-finding for the pair).

**Disposition: surfaced, evaluated, rejected as a development path.** Retained as a **preclinical question** for the Pathway Analyst: in a colonic model, does IBAT inhibition raise the UDCA:taurocholate ratio or lower it? That is a cheap in silico/ex vivo question and it fully determines whether the idea is salvageable. Recording a rejected-with-reasons candidate is more useful to the pipeline than silently dropping it — the ADMET agent will otherwise re-raise it.

### 6.5 Other approved drugs considered and rejected

| Drug | Target | Why rejected |
|---|---|---|
| **Cholestyramine, colesevelam, sevelamer** | #34 sequestration | Doubly disqualified: §4.5 shows tolevamer **failed Phase 3** at luminal sequestration, and §6.2 forbids co-administration (they bind vancomycin — and would bind any bile-acid candidate, i.e. they are the direct antagonist of the #66 strategy) |
| **Colchicine** | #44 NLRP3 | Approved, cheap, with a large chronic-dosing safety base from cardiovascular trials. But: dose-limiting toxicity is **diarrhoea**; narrow therapeutic index; severe toxicity in **renal impairment**; CYP3A4/P-gp DDIs against the §3.3 list. Every one of those lands on a §3.4 population vulnerability. **Reject on safety** |
| **Pioglitazone** | #53 PPARγ | Approved; but preclinical-only in CDI, carries heart-failure warnings, and §3.2 flags CHF as prevalent (the same issue that constrains bezlotoxumab). **Reject** |
| **Calcitriol / vitamin D3** | #54 VDR | Approved, trivially cheap, induces cathelicidin; #54 is the only host target with **any** clinical (observational) CDI data. Effect size is almost certainly too small to be a therapy. **Disposition: not a candidate, but a near-free adjunct arm or a stratification covariate** in whatever trial does run. Worth one line in a protocol, not a program |
| **Teduglutide** | #60 GLP-2 | Approved, intestinotrophic; but injectable, expensive, carries a neoplasia warning, and is "computational/untested in CDI" per §5.3. Wrong risk profile for an acute infection. **Reject** |
| **Hsp90 inhibitors** | #40 | The ethnobotany agent's gedunin/celastrol hypothesis is interesting, but **no Hsp90 inhibitor has ever been approved** — the oncology programs all failed. Cyclosporine hits the same pathway and is DDI-prohibitive. **No repurposing option exists** |
| **Rifaximin** | Phase 2 | Already in §4.3 as a "chaser" with limited evidence and ready rifamycin resistance. Not a new finding, and the evidence is [UNCERTAIN] in the model. **No change** |
| **Paromomycin, aminoglycosides** | Phase 2 | Top of my luminal physicochemical screen (§2.3), and exactly the wrong answer — broad-spectrum destruction of the commensal guild. Included here as the worked example of why that screen must not be used alone |

---

## 7. Cross-cutting findings and challenges to Round 1

### 7.1 ⚑ Targets #46 and #47 are mutually incompatible

**This is the most consequential finding in this report after the RLD correction.**

- Target **#46** instructs: **INHIBIT** IL-23 / IL-23R. Named drugs: ustekinumab, risankizumab, guselkumab.
- Target **#47** instructs: **AGONIZE** IL-22 / IL-22R / STAT3, described as a "protective epithelial axis, AMP induction."

IL-23 is the principal driver of IL-22 production by ILC3s. **Blocking IL-23 suppresses IL-22.** These targets cannot both be pursued; a drug that satisfies #46 actively defeats #47. The disease model lists both as legitimate Tier 2 targets without noting the conflict, and the Round 1 scoring exercise — which scored candidates independently against a target list — had no mechanism for detecting it.

This matters directly for Q5: **ustekinumab is not merely unsupported in CDI, it is pointed at the wrong end of an axis the model itself says is protective.**

> **To the Pathway Analyst (Phase 2):** please adjudicate. The IL-23/IL-22 relationship in CDI is likely dose- and compartment-dependent — pathogenic IL-23-driven Th17 inflammation and protective ILC3-derived IL-22 may be separable by timing, cell type, or magnitude. But until someone resolves the direction, **no IL-23-directed candidate should be scored positively**, and the disease model's §5.3 should carry an explicit cross-reference between rows #46 and #47.

### 7.2 Soft-electrophile covalent chemistry is a class-level failure in the CDI lumen

The ADMET agent argued this for ebselen from selenium chemistry. Finding **auranofin** (gold, thiol-reactive) at target #21 and **disulfiram** (disulfide) in the approved set — both failing for the identical reason — upgrades a molecule-specific objection to a **class rule**:

> Any warhead whose mechanism is exchange with a cysteine thiol will be consumed by the millimolar free cysteine, glutathione, and bacterially-generated H₂S in the colonic lumen (Eh ≈ −200 mV) before reaching a target, and will have no selectivity if it does.

**Consequence for the SAR Analyst's warhead-replacement task at #26:** the replacement cannot simply be "a different covalent warhead." It must resist exchange with abundant small-molecule thiols — which rules out most of the standard covalent toolkit and points toward **reversible-covalent** chemistry with fast off-rates against small thiols but slow off-rates against the target, or a **non-covalent** CPD inhibitor, or a **mucosally-activated prodrug** that only unmasks the warhead after epithelial uptake. This narrows the search usefully and should be handed over as a constraint, not a suggestion.

### 7.3 Bile acid pharmacology and CDI share an adverse-event axis

Three of the strongest candidates in this report — UDCA, chenodiol, and the IBAT inhibitors — have **diarrhoea** as their principal or dose-limiting adverse effect. So does colchicine. CDI's primary endpoint is diarrhoea recurrence.

This is not a coincidence to be noted and moved past; it is a **structural feature of the therapeutic area**, and it has three consequences that belong in every bile-acid CDI protocol:

1. **Endpoint must be toxin-confirmed and adjudicated**, never symptom-based. (Standard in CDI trials, which fortunately mitigates most of this.)
2. **Functional unblinding risk** — a patient whose stool frequency rises after starting "study drug" may correctly infer their allocation. Blinded independent endpoint committee is mandatory, not optional.
3. **Dose escalation is doubly constrained** — by the adverse effect *and*, for UDCA specifically, by the high-dose PSC harm signal (§4.1). The intuitive response to "colonic concentration may be sub-therapeutic" — give more — is closed off from both directions. This is the tightest constraint on the pipeline's leading candidate and, as far as I can tell, it has not been stated anywhere in Round 1.

### 7.4 Where I disagree with Round 1

| Round 1 position | My position | Basis |
|---|---|---|
| Ebselen scored 6.4 mean (Target Profiler 8.5); framed as a repurposing candidate with a fast path | **Repurposing feasibility 4.0.** No RLD → full 505(b)(1) NDA, 9–12 yrs, $125–225M | Regulatory: prior human exposure ≠ reference-able safety data. The Target Profiler's 8.5 is right *about the target* and should be preserved as such |
| Niclosamide's poor absorption is "a CDI advantage" (disease model, tasking) | **It is the primary obstacle.** The target is intracellular; solubility ~1.6 µM caps free drug below the active range | ADMET's three-compartment model; niclosamide is C2, not C1 |
| Ustekinumab worth investigating for anti-recurrence benefit | **Mechanistically contraindicated** (⚑ §7.1) plus PK too slow for an 8-week window | Disease model's own #47 |
| Aprepitant mean 4.9, "moderate" | **Do not pursue.** DDI profile is disqualifying in this population and there is no endpoint | §3.3 DDI checklist + Clinical Landscape "unbounded" |
| Repurposing is the fastest route to patients (implicit in my own skill file) | **Partly false in CDI.** In-licensing a de-risked, financially orphaned Phase 2 asset is faster and better-evidenced — ribaxamase scores highest here | Clinical Landscape's 6-of-12-financial-failures finding, read as a market signal |

### 7.5 Where I agree with and extend Round 1

- **ADMET's three-compartment model is the single most useful analytical contribution of Round 1** and I have adopted it as dimension 1 of my rubric. It is what correctly demotes ebselen and niclosamide and what correctly promotes hydroxychloroquine.
- **Clinical Landscape's add-on-vs-replacement finding** is the correct organising principle for positioning and I have weighted it explicitly.
- **Ethnobotany's inversion** ("compounds abandoned for poor bioavailability elsewhere should be positively screened for CDI") is right for **C1 luminal** candidates and **wrong for C2 candidates** — niclosamide is the counterexample that shows the inversion has a boundary. The refined rule: *invert bioavailability scoring only after establishing which compartment the target sits in.*

---

## 8. Recommended actions, in cost order

| # | Action | Cost | Duration | Decides |
|---|---|---|---|---|
| 1 | **HCQ in vitro TcdB entry-blockade assay** | $30–60k | 2–3 mo | Whether a cheap approved drug hits Module A |
| 2 | **Niclosamide kill-or-cure package** — anaerobic stability, fecal-water dissolution, colonocyte uptake, FDA listed-drug determination | $200–400k | 4–6 mo | Closes niclosamide (expected) |
| 3 | **Ustekinumab/anti-TNF CDI-recurrence registry analysis** in IBD cohorts | $100–300k | 6–9 mo | Answers Q5 definitively |
| 4 | **Stage 0: fecal bile acid PK in CDI patients** — UDCA + chenodiol + taurocholate arms, free concentration in fecal water vs germination IC₅₀ | **$1–3M** | **9–12 mo** | **Go/no-go on the pipeline's leading candidate** |
| 5 | **Ribaxamase asset evaluation** — diligence on the Phase 2b data package and acquisition cost | $150–300k | 3–4 mo | Whether the fastest path is a transaction, not a repurpose |
| 6 | Pre-IND / Type B meeting on 505(b)(2) reliance, endpoint, and fecal-concentration bridging | $200k | 4–6 mo (parallel with 4) | De-risks the regulatory assumptions in §3.1 |

**Total to a fully informed go/no-go on the entire repurposing thesis: under $4.5M and about 12 months.** That is roughly 5% of the cheapest development program in this report, and it resolves every one of Round 1's gaps #5, #6, #7 and most of #2.

---

## 9. Items requiring verification before external use

Per the skill file guardrails and disease model §A.3:

| # | Claim | Why it matters |
|---|---|---|
| 1 | **Niclosamide US listed-drug/RLD status** (discontinued-but-referenceable?) | Determines whether niclosamide has any 505(b)(2) path at all |
| 2 | **Chenodiol current US marketing status and label** (Chenodal; Ctexli for CTX) | RLD availability and the hepatotoxicity/diarrhoea rates quoted in §4.2 |
| 3 | **High-dose UDCA PSC harm signal** (28–30 mg/kg/d, increased death/transplant) | This is the dose ceiling on the leading candidate — the most load-bearing single fact in §4.1 |
| 4 | **UDCA and CDCA anti-germination IC₅₀ values** in *C. difficile* | Stage 0's entire go/no-go criterion. Round 1 already routed this to the Literature Reviewer |
| 5 | **Fecal bile acid concentrations in UDCA-treated patients** | Whether Stage 0 is likely to succeed; may be partly answerable from existing literature before spending $2M |
| 6 | **Ebselen clinical development status and sponsor** (Daiichi, Sound Pharmaceuticals/SPI-1005) | Confirms the no-RLD finding |
| 7 | **Ustekinumab biosimilar availability** | Affects the (already low) commercial score |
| 8 | **Obeticholic acid current market/regulatory restrictions** | Basis for rejecting it at §6.1 |
| 9 | **Nitazoxanide CDI trial data** — size, comparator, outcomes; and any sporulation/toxin-suppression data | Nitazoxanide's whole case rests on this; it is the one candidate whose rank would move most |
| 10 | **Ribaxamase asset status and Theriva's disposition** | Whether recommendation §4.9 is actionable |
| 11 | **Orphan designation precedent for recurrent CDI** | Worth 7 years, stacks with QIDP |

---

## 10. Research disclaimer

All repurposing hypotheses in this report are **computational and knowledge-based**. No new experimental data was generated. Target–drug assignments derive from the disease model's hand-curated §5 master list, which — per §2.1 above — **has no database backing in this project's current data**. Feasibility scores measure development-path tractability, not probability of clinical benefit. Every candidate here requires experimental and clinical validation before any claim of efficacy, and the §9 verification list must be cleared before any external-facing use.

---

*End of Phase 2 Drug Repurposing Strategist report.*
