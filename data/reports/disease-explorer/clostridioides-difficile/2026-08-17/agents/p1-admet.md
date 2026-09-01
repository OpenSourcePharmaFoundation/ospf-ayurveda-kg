# Pharmacokinetics / ADMET Analysis — *Clostridioides difficile* Infection

**Agent:** Pharmacokinetics Specialist (ADMET Predictor)
**Phase:** 1 — Parallel domain analysis
**Date:** 2026-08-17
**Skill applied:** `.claude/skills/admet-predictor/SKILL.md`, with the **CDI ADMET inversion** from disease-model.md §6.2 overriding the standard absorption rubric
**Disease model sections used:** §1.5 (subtypes), §2.2 (Phase 0), §2.5 (sub-MIC toxin induction), §2.6 A.2–A.3 (toxin entry), §3.2–3.4 (population), §4.5 (failed approaches), §6.1–6.4 (route), Appendix A.1–A.2

**Central question for this agent:** *Can these compounds reach the relevant tissue, and what are the pharmacokinetic deal-breakers?*

---

## 0. EXECUTIVE SUMMARY

| # | Candidate | Score /10 | Compartment | Verdict | Binding PK constraint |
|---|---|---|---|---|---|
| 1 | **Fidaxomicin** | **10** | C1 luminal | **A** — benchmark | None. Reference standard for inverted ADMET |
| 2 | **Ibezapolstat** | **9** | C1 luminal | **A** | PK designed-in and demonstrated; but PK is not the differentiator (§4.5) |
| 3 | **Vancomycin PO** | **9** | C1 luminal | **A** | Prolonged fecal persistence sustains dysbiosis; systemic accumulation in severe colitis + renal failure |
| 4 | **Berberine** | **8** | C1 luminal | **B** | Fecal binding (cationic) → free conc. may land in the **sub-MIC toxin-induction window** (§2.5) |
| 5 | **UDCA (ursodiol)** | **6** | C1 luminal (via bile) | **C** | Colonic delivery is enterohepatic spillover only; likely sub-therapeutic without colon-targeting |
| 6 | **Bezlotoxumab** | **6** | C3 systemic → C2 | **B** | Delivery to site of action is inflammation-gated; IV route + CHF fluid-load signal |
| 7 | **Aprepitant** | **5** | C3 systemic | **C** | Reaches target fine; **CYP3A4/2C9 DDI** in the §3.3 polypharmacy population is the deal-breaker |
| 8 | **Ebselen** | **4** | **C2 mucosal** | **D** | Selenium electrophile **quenched by luminal thiols** before reaching the mucosa |
| 9 | **Niclosamide** | **3** | **C2 mucosal** | **D** | **Nitro group reduced anaerobically** → destroys the protonophore pharmacophore; plus solubility-capped free conc. |
| 10 | **Conessine** | **2** | — | **F** | Absorbed *and* fecal-bound *and* CNS-active in a population §3.4 says to avoid CNS agents in |

**Scoring axis:** this score answers *"can it get to where it needs to act, in active form, at adequate free concentration, in this patient population?"* It is **not** an efficacy or potency score. A candidate can score 10 here and still be commercially worthless (see §4.5 and Cross-Cutting Observation 6).

---

## 1. FRAMEWORK — THREE COMPARTMENTS, NOT TWO

The task brief and §6.2 both frame CDI ADMET as a binary: **luminal** (inverted scoring) vs **systemic** (conventional scoring). That binary is correct for eight of the ten candidates but **misfiles the two most mechanistically interesting ones**, and I want to flag this before scoring.

| Compartment | Definition | What governs exposure | Candidates |
|---|---|---|---|
| **C1 — Luminal free** | Dissolved, unbound drug in colonic lumen/mucus | Dose delivered to colon, aqueous solubility at pH 5.5–7.5, fecal/mucin binding, transit time, chemical stability at Eh ≈ −200 mV | Fidaxomicin, vancomycin, ibezapolstat, berberine, UDCA |
| **C2 — Mucosal intracellular** | Cytosol / endosomes of colonocytes | Dissolution → mucus penetration → cellular uptake (three serial low-efficiency steps), *or* basolateral delivery from plasma | **Ebselen, niclosamide**, (bezlotoxumab acts on the serosal face of this compartment) |
| **C3 — Systemic** | Plasma + interstitium | Conventional ADMET; §3.3 DDI environment is binding | Aprepitant, bezlotoxumab |

**Why this matters.** Per §2.6 A.2, the TcdB entry cascade steps 3–6 — endosomal acidification, delivery-domain pore formation, InsP6-triggered CPD autoproteolysis, and GTD glucosylation of RhoA — **all occur inside the host colonocyte**. Therefore:

- **Ebselen's** target (TcdB cysteine protease domain, §2.6 target table) is **cytosolic**. Low absorption is *not* an asset for ebselen; it needs mucosal uptake.
- **Niclosamide's** proposed mechanism (endosomal deacidification / protonophore, §2.6 target table: *"niclosamide-like protonophores"*) is **endosomal**. Same conclusion.

Scoring these two on luminal-retention criteria would reward them for the wrong property. Both are scored below against a **mucosal-uptake** requirement instead — and both fail it, for chemical rather than pharmacokinetic reasons.

---

## 2. CANDIDATE-BY-CANDIDATE ASSESSMENT

---

### 2.1 FIDAXOMICIN — Score 10/10 | Verdict A | Confidence HIGH | Evidence: mixed

```
═══════════════════════════════════════════════════════════
ADMET ASSESSMENT: FIDAXOMICIN (CHEMBL1255800)
COMPARTMENT: C1 — luminal          VERDICT: A (benchmark)
═══════════════════════════════════════════════════════════
PROJECT DATA (data/processed/chembl_approved_drugs.csv):
  molecular_weight = 1058.05   first_approval = 2011   max_phase = 4
  natural_product = 1          withdrawn_flag = False
  alogp, hba, hbd, psa, rtb, ro5_violations, qed_weighted = ALL BLANK
```

**Note the blank descriptors — they are themselves the finding.** The descriptor calculator skipped fidaxomicin entirely, presumably as out-of-range. §6.2 states plainly: *"Fidaxomicin (MW ~1058) and vancomycin (MW ~1449) both grossly violate Rule of Five and are the two best drugs for this disease."* The project's own descriptor pipeline cannot represent the gold standard for this indication. Any automated Ro5 filter run over `chembl_approved_drugs.csv` would drop the best CDI drug in the file.

**Absorption (inverted):** 18-membered macrolactone with two sugars, two chlorines, and a resorcylate ester. Systemic Cmax after 200 mg BID is single-digit ng/mL — effectively unmeasurable; <1% absorbed. **This is the target profile, achieved by intrinsic physicochemistry rather than by a delivery system** (see Cross-Cutting Observation 8).

**Colonic exposure:** Fecal concentrations ~1000–1400 µg/g against *C. difficile* MIC₉₀ ≈ 0.25 µg/mL → **>4000× headroom**. This is the concrete instance of §6.4's *"fecal vancomycin concentrations routinely exceed MIC by 100–1000×, which relaxes potency requirements substantially."*

**Metabolism — a worked example of the inversion:** the standard ADMET rubric (skill file, *Metabolic Liability Red Flags*) lists **ester groups → rapid hydrolysis by esterases → very short half-life** as a liability. Fidaxomicin has exactly that: its isobutyryl ester is hydrolyzed by intestinal esterases to **OP-1118**. In conventional ADMET this is a red flag. In CDI it is **benign-to-favorable**: the hydrolysis is *gut* not *hepatic*, OP-1118 is itself active (~8× less potent), and OP-1118 is present at **higher** fecal concentration than parent. Net antibacterial exposure is increased, not lost.

*This is the clearest demonstration in the candidate set that the standard rubric must be re-derived, not merely sign-flipped.*

**Stability at Eh ≈ −200 mV:** no nitro, azo, disulfide, quinone, or N-oxide. Nothing to reduce. Passes the §6.2 anaerobic-stability filter cleanly.

**Fecal binding:** neutral, no permanent charge → the §6.2 cationic-adsorption flag does not apply.

**DDI:** essentially zero by non-absorption — scored as a **safety asset** per §6.2 and §3.3.

**Residual concerns (none are PK deal-breakers):**
- **No non-oral route.** §1.5(c)/§6.1: ileus in fulminant CDI makes oral delivery pharmacokinetically unavailable. Fidaxomicin has no IV or rectal option.
- Capsule size — §6.3 flags fidaxomicin/vancomycin capsules as a swallowing problem in frail elderly.
- Extended-pulsed regimen runs 25 days, extending the adherence burden (§6.3).
- Cost/payer denial (§6.3) — not a PK matter, flagged for Clinical Feasibility.

---

### 2.2 IBEZAPOLSTAT — Score 9/10 | Verdict A | Confidence MODERATE | Evidence: **knowledge-based, not data-backed**

**Absent from project data.** Not in `chembl_approved_drugs.csv` (all 3276 rows checked), not in the natural-products file. Investigational (DNA polymerase IIIC / PolC inhibitor, Gram-positive-selective; §2.4 target table).

**Absorption (inverted):** purpose-designed for luminal delivery. Reported Phase 2 PK shows minimal systemic exposure with fecal concentrations well above MIC throughout dosing. **This is what the inverted ADMET logic looks like when applied prospectively rather than discovered retrospectively** — fidaxomicin and vancomycin arrived at non-absorption by accident of chemotype; ibezapolstat was designed to it.

**The genuinely distinctive PK-adjacent finding:** reported Phase 2 microbiome data describe *increases* in Actinobacteria/Firmicutes — including bile-acid-converting Clostridia — and rising secondary bile acids **during** therapy. If that holds, the drug's colonic exposure profile is not merely non-destructive but **restorative to the Phase 0 mechanism** (§2.2: secondary bile acid production is the best-characterized colonization-resistance mechanism). Per §1.5(b) and §4.6 that is the single most valuable property available in this disease, and no other candidate here claims it.

**Concerns:**
1. **PK excellence does not protect against the §4.5 failure pattern.** Ridinilazole, surotomycin, and cadazolid all had adequate luminal PK and adequate narrowness, and all failed to differentiate on sustained response. §A.3 warns that *"preclinical efficacy in CDI has an unusually poor record of predicting Phase 3 success."* **I am scoring PK; the Candidate Ranker should not read a 9 here as a 9 overall.**
2. **Small-N microbiome findings.** The bile-acid-restoration signal is from limited Phase 2 cohorts and should be treated as [EMERGING].
3. **Under-examined stability class.** The chemotype is uracil-based (6-anilinouracil family). Colonic bacteria are rich in pyrimidine-salvage enzymes and nucleoside phosphorylases. **Stability of a uracil scaffold to colonic bacterial pyrimidine metabolism is a liability class §6.2 does not enumerate**, and I would want it measured. It is not a reducible group, so the §6.2 checklist would pass it by default — that checklist is incomplete for nucleobase-like scaffolds.
4. Development/commercial status is uncertain and should be verified by the Clinical Landscape agent.

---

### 2.3 VANCOMYCIN (ORAL) — Score 9/10 | Verdict A | Confidence HIGH | Evidence: mixed

```
PROJECT DATA (CHEMBL262777): molecular_weight = 1449.27 | first_approval = 1964
  natural_product = 1 | max_phase = 4 | all computed descriptors BLANK
  (duplicate salt record: CHEMBL1200628 VANCOMYCIN HYDROCHLORIDE, same MW)
```

**Absorption (inverted):** glycopeptide, MW 1449, densely H-bonded, permanently zwitterionic, far beyond any passive-permeability window. ~0% absorbed from an intact gut. Fecal concentrations routinely >1000 µg/g against MIC₉₀ ≈ 1–2 µg/mL. **Textbook-ideal luminal PK.**

**Three real PK caveats — the score is 9, not 10, on PK grounds specifically:**

1. **"Non-absorbed" fails in the sickest patients.** §3.4 states directly: *"vancomycin can accumulate systemically even after oral dosing when the colon is severely inflamed"* in renal failure. Severe colitis breaches the barrier; renal impairment (present in ~20–30% per §3.2) removes the clearance route. Systemic vancomycin is nephrotoxic and ototoxic. **The non-absorption safety asset evaporates exactly where the disease is most dangerous** — this is a conditional, not absolute, property, and §6.2's blanket "score non-absorption as a safety asset" instruction should be read with that caveat.

2. **Prolonged fecal persistence is a PK property that directly drives the recurrence loop.** Vancomycin remains detectable in stool for weeks after a 10-day course. The dysbiotic pressure therefore **outlasts the treatment window**, which is precisely the self-defeating loop described in §1.5(b)/§2.2 (*"the treating antibiotic itself perpetuates the dysbiosis that permitted infection"*). This is worth stating as a **pharmacokinetic** finding, not just an ecological one: colonic residence time — the very parameter §6.2 says to optimize *upward* for luminal drugs — is the parameter that makes vancomycin harmful. **For a broad-spectrum luminal agent, long colonic residence is a liability, not an asset.** §6.2's framing ("colonic residence time is what matters") is directionally under-specified: it matters, but the optimal value depends on spectrum. A selective agent wants long residence; a broad one wants exposure that stops when dosing stops.

3. **Formulation incompatibility.** §6.2: *"Do not co-administer with bile acid sequestrants (cholestyramine, colestipol) — they bind vancomycin."* Relevant because cholestyramine is sometimes used empirically for diarrhea in this population.

**Stability:** no reducible groups; stable in the anaerobic colon. **DDI:** none systemically. **Cost:** generic — §6.3 notes this is a real advantage.

---

### 2.4 BERBERINE — Score 8/10 | Verdict B | Confidence MODERATE | Evidence: mixed

```
═══════════════════════════════════════════════════════════
ADMET ASSESSMENT: BERBERINE (CHEMBL295124)
COMPARTMENT: C1 — luminal          VERDICT: B
═══════════════════════════════════════════════════════════
PROJECT DATA (data/processed/chembl_approved_drugs.csv):
  molecular_formula = C20H18NO4+   ← PERMANENT QUATERNARY CATION
  molecular_weight = 336.37   alogp = 3.10   hba = 4   hbd = 0
  psa = 40.80   rtb = 2      ro5_violations = 0   aromatic_rings = 3
  heavy_atoms = 25           qed_weighted = 0.67
  oral_bioavailability = False   natural_product = 1   max_phase = 4
  withdrawn_flag = True (UNVERIFIED — see Data Gaps)
  SMILES: COc1ccc2cc3[n+](cc2c1OC)CCc1cc2c(cc1-3)OCO2
═══════════════════════════════════════════════════════════
```

**This is the most interesting ADMET profile in the candidate set**, because by conventional scoring it looks like a *good oral drug* — MW 336, logP 3.10, PSA 40.8, HBD 0, RTB 2, **zero Ro5 violations, QED 0.67** — and it is in fact <1% bioavailable. The Lipinski block completely fails to predict this. The reason is in the molecular formula, not the descriptors: **`C20H18NO4+` — a permanently charged isoquinolinium quaternary ammonium.** No pH exists at which it is neutral, so there is no passive transcellular absorption; the small absorbed fraction is P-gp effluxed and heavily first-pass metabolized.

**For CDI this is close to fidaxomicin-grade luminal delivery obtained for free from physicochemistry, in a cheap, orally-dosed, widely-available natural product.** Among the non-benchmark candidates it has the best intrinsic luminal profile.

Supporting properties:
- **Acid-stable** — aromatic isoquinolinium, no hydrolyzable ester/amide/glycoside. Survives gastric transit without enteric coating. Per §6.1, must *"survive gastric acid and small-intestinal enzymes"* — it does.
- **No reducible groups** in the §6.2 sense (methylenedioxy and methoxy aryl ethers are not bioreduced at Eh −200 mV). Passes the anaerobic-stability filter.
- `oral_bioavailability = False` in project data — notably the one record in this candidate set where that flag agrees with reality (see Data Gaps).

**Concern 1 — fecal binding. §6.2 explicitly instructs: *"Flag any strongly cationic candidate."*** Berberine is the archetype: a **planar, fully aromatic, permanently cationic** species. Mucin is heavily anionic (sialylated and sulfated), fecal solids and bacterial surfaces likewise. Berberine will adsorb extensively. **Total colonic concentration will substantially overstate free concentration**, and §6.2 warns that *"measured fecal MIC ≫ broth MIC for many compounds."* Planar aromatic cations additionally stack onto nucleic acids and particulates. Of everything in this report, **this is the single measurement I would most want run.**

**Concern 2 — the sub-MIC toxin-induction trap. This is the specific deal-breaker risk for berberine, and §2.5 instructs me to flag it by name:**

> *"Sub-inhibitory concentrations of some antibiotics… **increase** toxin production in vitro. Any candidate with marginal colonic exposure must be checked for toxin induction — this is a real failure mode, not a theoretical one, and the Chemist/ADMET agents should flag candidates whose predicted colonic concentration sits near the MIC."*

Berberine's reported MIC against *C. difficile* is high (tens to >100 µg/mL). A plausible total colonic concentration at conventional dosing (~500 mg TID) lands in the low hundreds of µg/g — apparently adequate. **But after cationic fecal binding, the free concentration plausibly falls to at-or-just-below MIC.** That is precisely the window §2.5 describes. Berberine is the candidate in this set that most exactly matches the warning's description.

Critically, this risk is **invisible to any total-concentration analysis** and would be missed by the §6.4 "100–1000× headroom" reasoning, which is a *total*-concentration argument.

→ **Recommended experiment (cheap, decisive):** measure *C. difficile* toxin output (TcdA/TcdB ELISA) across a berberine concentration gradient **in fecal-slurry-supplemented medium**, not broth. Two possible outcomes, both actionable: clean inhibition supports advancement; a toxin-induction hump below MIC is a hard stop for berberine monotherapy and would reframe it as combination-only (with vancomycin or fidaxomicin providing the kill, per §A.2's suggested pair *"vancomycin + berberine"*).

**Concern 3 (favorable, and it corrects a model assumption) — dysbiosis-dependence runs the *right* way here.** Berberine is reductively metabolized by **gut bacterial nitroreductases** to dihydroberberine, which is the actually-absorbable species (~5× higher uptake), then re-oxidized systemically. §6.1/§6.2 warn that *"microbiota-triggered release depends on colonic bacterial enzymes that are depleted in CDI dysbiosis"* — presented purely as a failure mode. **For berberine the same dependence is protective:** in a dysbiotic colon the reductase capacity is depleted, so *less* berberine is converted to the absorbable form, so *more* stays luminal. The direction of microbiota-dependence must be evaluated per candidate, not assumed harmful.

**Concern 4 — systemic DDI of the small absorbed fraction.** The skill file lists berberine as a **CYP2D6 inhibitor**; it also inhibits CYP3A4 and P-gp. Even at <1% absorption this deserves a check against §3.3's tacrolimus/cyclosporine/digoxin/DOAC list. Likely minor, but not automatically zero — non-absorption gives a *near*-empty DDI profile, not an empty one.

**Data-quality note:** `withdrawn_flag = True` for berberine, but there is **no corresponding row** in `chembl_drug_warnings.csv` (9 rows total). Unverifiable; **not relied upon** in this assessment. Flagged to the Safety Pharmacologist.

---

### 2.5 UDCA / URSODIOL — Score 6/10 | Verdict C | Confidence MODERATE | Evidence: mixed

```
PROJECT DATA (CHEMBL1551): molecular_weight = 392.58 | alogp = 4.48
  hba = 3 | hbd = 3 | psa = 77.76 | rtb = 4 | ro5_violations = 0
  aromatic_rings = 0 | heavy_atoms = 28 | qed_weighted = 0.66 | first_approval = 1987
  Comparators in same file: DEOXYCHOLIC ACID (CHEMBL406393, identical descriptors —
  MW 392.58, alogp 4.48, psa 77.76); CHOLIC ACID (CHEMBL205596, MW 408.58);
  TAURURSODIOL (CHEMBL272427, MW 499.71, psa 123.93); OBETICHOLIC ACID (CHEMBL566315, MW 420.63)
```

**Ro5-compliant — and that is misleading.** Bile acids are handled by **active transport** (ASBT/NTCP), not passive permeability, so the Lipinski block has essentially no predictive value here. This is a case where the standard rubric is not merely inverted but *inapplicable*.

**Route to the colon is real but leaky and modest.** UDCA is absorbed proximally (passive, protonated form) and by ileal ASBT → conjugated in liver to glyco-/tauro-UDCA → secreted in bile → **~50–80% reabsorbed at the terminal ileum per enterohepatic cycle**. Only the **spillover fraction** reaches the colon. The task brief frames UDCA's ~50% bioavailability as "BUT enters enterohepatic circulation → reaches colon via bile" — correct in direction, but the quantitative reality is that efficient ileal recapture is *designed* to prevent colonic delivery. At cholestatic doses (13–15 mg/kg/d), colonic concentrations are likely **well short** of the high-µM-to-mM range at which anti-germination and cytoprotective effects are reported in vitro.

**→ Colonic concentration, not absorption, is the binding constraint. This is a formulation problem with two rational solutions:**
- **Colon-targeted delayed-release UDCA** — but see Cross-Cutting Observation 8: pH-dependent coatings are defeated by the PPIs that §3.3 calls *"extremely common, often unnecessarily continued"* in this population.
- **Co-administration with an ASBT inhibitor** (odevixibat/elobixibat class), which deliberately dumps bile acids into the colon. Mechanistically elegant and uses approved agents — **worth flagging to the Combination Designer**, alongside §A.2's suggested *"SOC + bile acid restoration"* pairing.

Note also that simply escalating the oral dose disproportionately increases *hepatic and systemic* exposure rather than colonic — the enterohepatic loop buffers it. Dose escalation is not a route to colonic exposure.

**Two CDI-specific twists, one favorable and one genuinely uncertain:**

**(a) Favorable — diarrhea helps here.** §6.2 lists *"diarrhea shortens transit time → reduced colonic residence"* as a general liability. **For UDCA it inverts:** accelerated transit and diarrhea impair ileal ASBT reabsorption, so **more bile acid spills into the colon exactly when the patient is symptomatic.** Delivery is self-amplifying during active disease. This is the one candidate where §6.2's transit-time warning points the wrong way, and it is worth recording as a counterexample.

**(b) [UNCERTAIN] — which species is the active one?** In a healthy colon, bacteria epimerize UDCA (7β-OH) → CDCA (7α-OH), and the `bai` guild 7α-dehydroxylates CDCA → **LCA** (§2.2). In dysbiotic CDI that guild is **depleted**, so UDCA persists largely unconverted. Whether that helps or hurts depends on the active species:
- If **UDCA itself** is the effector (it inhibits taurocholate-mediated germination and is epithelium-cytoprotective), dysbiosis is neutral-to-favorable.
- If **LCA** is the effector (§2.2: *"LCA also inhibits germination"*; §2.3 lists lithocholate as a germination inhibitor [CURRENT CONSENSUS]), then **UDCA cannot be converted in the patients who need it** — the drug depends on the very enzymatic capacity the disease destroys, which is the §6.1 microbiota-dependent-failure pattern in a new guise.

**This is a real fork and I cannot resolve it from PK reasoning alone — it is a question for the Target Profiler and Pathway Analyst** (posed formally below). Note the alternative it implies: if LCA is the effector, **deliver LCA or a non-convertible LCA analog directly** rather than UDCA, bypassing the missing enzymology entirely.

**Other:** §6.2 — do not co-administer with bile acid sequestrants (they would bind UDCA as they bind vancomycin). Chronic high colonic secondary-bile-acid exposure (DCA/LCA) carries genotoxic/tumor-promoting concerns — acceptable for a 10–12 week course, a constraint on indefinite prophylaxis. §3.2 notes hepatic impairment/cirrhosis is overrepresented and *"alters the bile acid pool — mechanistically relevant"*: UDCA PK will differ substantially in these patients.

---

### 2.6 BEZLOTOXUMAB — Score 6/10 | Verdict B | Confidence HIGH | Evidence: knowledge-based

**Absent from project data** — `chembl_approved_drugs.csv` is small-molecule-centric; no biologic records.

**Standard biologic PK.** Human IgG1 mAb, ~148 kDa. IV only. Vd ≈ 7.3 L (plasma volume + modest interstitial — i.e. **plasma-restricted**), clearance ≈ 0.3 L/day, **t½ ≈ 19 days**. Eliminated by proteolytic catabolism with FcRn recycling — **no CYP, no renal, no hepatic clearance → essentially zero DDI**.

That last point deserves emphasis against §3.3: bezlotoxumab is the **only candidate here that achieves a clean DDI profile without relying on non-absorption.** In a population on tacrolimus, warfarin, DOACs, amiodarone, digoxin, and statins, a drug with no metabolic clearance pathway at all is genuinely valuable — and unlike the luminal agents, it retains that property in fulminant disease where barrier breach compromises the "non-absorbed" assumption (cf. vancomycin, §2.3 caveat 1).

**The central PK question — and the answer is more favorable than it first appears.** How does a plasma-restricted IgG reach a toxin produced in the lumen? Largely it does not — **and it does not need to.** Per §2.6 A.2, TcdB's high-affinity receptor **CSPG4 is subepithelial/stromal** (*"low on mature colonocytes"*), and **FZD1/2/7 are on colonic crypt stem cells**. Both are **basolateral/serosal**. Plasma IgG extravasates into inflamed lamina propria (vascular permeability is markedly increased in colitis), so bezlotoxumab intercepts toxin **after it breaches the epithelium** — which is exactly where the FZD-mediated Wnt/stem-cell repair failure (§2.6 A.3: *"the epithelium cannot repair itself even as toxin is cleared"*) and the systemic manifestations arise. **The apparent compartment mismatch is not a real one.**

**But this creates a genuine and specific limitation: delivery is inflammation-gated.**
- Exposure at the site of action is **highest when the mucosa is inflamed and lowest when it is intact.** The drug therefore does little against *luminal* toxin in mild disease or during the asymptomatic inter-episode interval.
- Its **recurrence-prevention** action across the 8-week window (§1.5b) depends entirely on the long t½ maintaining a plasma titer sufficient to meet a *re-emergent* toxin challenge. Eight weeks is ~3 half-lives; titer at the tail of that window is a fraction of peak. **This is a plausible partial PK explanation for incomplete recurrence prevention**, and it argues that the failure mode is exposure-limited rather than mechanism-limited — a testable distinction.

**Population-specific PK liabilities from §3.2/§3.4:**
- **CHF exacerbation signal, attributed to infusion fluid volume** (§3.2 states this explicitly, and notes CHF is common in this cohort). **This is a formulation/delivery problem, not a mechanism problem** — the constraint is the volume, not the antibody. A higher-concentration or subcutaneous formulation would plausibly retire the signal. Worth flagging to Clinical Feasibility as a fixable defect.
- **Hypoalbuminemia is "very common"** (§3.2). Low albumin is associated with increased IgG catabolic clearance and capillary leak — plausibly a **shorter effective half-life in exactly the frail patients at highest recurrence risk.** I have not seen this raised for bezlotoxumab and it is directly testable in existing PK datasets; if real, it argues for weight- or albumin-adjusted dosing in frail patients.
- **60-minute IV infusion in a clinic** — a real burden (§6.3), partly offset by §6.3's observation that rCDI patients are *"counterintuitively highly motivated"* and accept invasive procedures for durable cure. One-and-done dosing is a genuine adherence advantage over 6–12 week tapers.

**Modality asset:** non-live, so usable in the transplant/HSCT/immunocompromised group that §3.4 calls *"arguably the most underserved sub-group in CDI"* — the population for which live biotherapeutics (Rebyota, Vowst) are relatively contraindicated. This is a PK/modality advantage, not merely a safety one.

---

### 2.7 APREPITANT — Score 5/10 | Verdict C | Confidence MODERATE | Evidence: mixed

```
PROJECT DATA (CHEMBL1471): molecular_weight = 534.43 | alogp = 4.95
  hba = 5 | hbd = 2 | psa = 83.24 | rtb = 6 | ro5_violations = 1
  aromatic_rings = 3 | heavy_atoms = 37 | qed_weighted = 0.44 | first_approval = 2003
IV PRODRUG ALSO IN PROJECT DATA:
  FOSAPREPITANT (CHEMBL1199324): MW 614.41 | alogp 4.37 | psa 129.91 | ro5_violations 1
  FOSAPREPITANT DIMEGLUMINE (CHEMBL1201782): same parent, MW 614.41
```

**Host-directed → conventional ADMET applies** (§6.2 final paragraph; §2.6 A.3 rationale: substance P / **NK1R (TACR1)** neurogenic inflammation and secretory diarrhea; §A.2 lists aprepitant as target #51).

**Absorption and distribution are not the problem.** Oral bioavailability ~60–65%, food-independent, >95% protein bound, t½ ~9–13 h, Vd ~70 L. It reaches enteric neurons and colonic mucosal NK1R adequately. **Aprepitant is the one candidate here with no meaningful tissue-access question.**

**Pfizer 3/75 toxicity rule:** alogp 4.95 (>3) but PSA 83.24 (>75) → **PASSES**, narrowly. Not flagged.

**The deal-breaker is DDI, and §3.3 makes it severe in this specific population.** Aprepitant is a **CYP3A4 substrate, a moderate CYP3A4 inhibitor, and a CYP2C9 inducer** — a triple liability against §3.3's checklist:

| §3.3 concurrent medication | Interaction | Severity in CDI population |
|---|---|---|
| **Tacrolimus, cyclosporine** | CYP3A4/P-gp narrow-TI substrates; aprepitant inhibits CYP3A4 → levels rise | §3.3 names these *"highest-priority DDI risk."* Transplant/IBD patients are over-represented (§3.2, §3.4) |
| **Warfarin** | CYP2C9 substrate; aprepitant **induces** CYP2C9 → INR falls | **Compounding risk.** §3.3 separately notes *"warfarin INR is destabilized by antibiotics and by microbiome disruption (vitamin K₂ production)."* **Two independent, same-direction destabilizing pressures act on warfarin simultaneously** in a heavily anticoagulated elderly cohort |
| **DOACs (apixaban, rivaroxaban)** | P-gp / CYP3A4 substrates | Bleeding risk in the elderly |
| **Statins, amiodarone, digoxin, quetiapine** | CYP3A4 / narrow-TI / QT | §3.3 flags all; QT stacking with concurrent fluoroquinolones |

The structural signature is visible in the project descriptors: **QED 0.44** (lowest of the small molecules assessed here) with **Ro5 violation = 1**, alogp 4.95, 3 aromatic rings, MW 534 — the profile of a large, lipophilic, CYP3A4-centric molecule. §6.2 is explicit that for systemic candidates *"the polypharmacy/organ-impairment profile in Section 3.3 becomes the binding constraint."* It does.

**The genuine and underrated upside — route flexibility for the fulminant subtype.** §1.5(c) states that in fulminant CDI *"ileus prevents oral drug from reaching the colon,"* and §6.1 confirms IV is required. **Aprepitant is the only oral candidate in this set with a ready-made, already-approved IV route** — fosaprepitant, present in the project data at CHEMBL1199324/CHEMBL1201782. §1.5(c) also notes fulminant CDI is *"the one CDI subtype where systemic exposure is desirable."*

So aprepitant's systemic profile — a liability everywhere else in this disease — is **exactly right for the one subtype nothing else can reach**, with a solved formulation and an approved IV product already on the shelf. For fulminant CDI (3–8% of hospitalized cases, 30–50% mortality, §1.3) this is a short and cheap development path. **I would not have predicted this from the compound; it comes out of cross-referencing §1.5(c) against the fosaprepitant record in the project data, and I think it is the most actionable single finding in this report.** Flagged to the Drug Repurposing Strategist and Clinical Feasibility Assessor.

Secondary point: aprepitant is already used as an antiemetic in the oncology comorbidity group (§3.2, ~15–25% of CDI patients), so tolerability in frail, comorbid patients is well characterized — an unusually low-risk repurposing profile *if* the DDI burden can be managed by patient selection (i.e. exclude transplant and warfarin patients).

---

### 2.8 EBSELEN — Score 4/10 | Verdict D | Confidence MODERATE | Evidence: knowledge-based

**Absent from project data** (not approved; not in the 3276-row approved-drugs file nor the 25-row natural-products stub).

**Structure:** 2-phenyl-1,2-benzisoselenazol-3(2H)-one. C₁₃H₉NOSe, **MW 274.2**, logP ~2.3, PSA ~35 Å², Ro5-compliant. **By conventional rules: good oral absorption.**

**Re-filing the compartment.** The task brief asks whether a molecule this small "will be absorbed" — implying that absorption would be a CDI disadvantage. **I think that framing is wrong for ebselen, and it matters.** Ebselen's validated target is the **TcdB cysteine protease domain** (§2.6 target table: *"ebselen is a validated covalent CPD inhibitor with in vivo efficacy [EMERGING]"*). Per §2.6 A.2 step 5, CPD autoproteolysis is triggered by **cytosolic InsP6** and occurs **inside the host cell**. Ebselen must therefore reach the **colonocyte cytosol (C2)** — moderate absorption is appropriate for it, not disqualifying. Scoring ebselen on luminal-retention criteria would reward the wrong property.

**The actual deal-breaker is chemical, and it is severe.**

**(1) Thiol quenching in the lumen.** Ebselen's entire mechanism is **Se–S exchange with cysteine thiols** — it is a soft selenium electrophile. The colonic lumen is a **thiol-saturated, strongly reducing sink**: §6.2 specifies Eh ≈ −200 mV, and the compartment contains millimolar free cysteine and glutathione plus **H₂S generated by sulfate-reducing bacteria** (*Desulfovibrio* spp.). Ebselen will be converted to ebselen–selenol and mixed selenosulfide conjugates **before it crosses the mucus layer.** §6.2 warns specifically about *"compounds with reducible groups… will be reduced"* — the selenium electrophile is exactly such a group, and unlike metronidazole (where reduction *is* the mechanism), here reduction is **pure inactivation**.

**(2) The same chemistry destroys selectivity.** Ebselen is a well-documented promiscuous covalent cysteine reactant (thioredoxin reductase, glutathione peroxidase mimicry, and a long list of others) — a frequent-hitter profile. The skill file's **PAINS** alert applies. In a thiol-rich lumen there is no selectivity to be had: the compound reacts with whatever thiol it meets first, and *C. difficile* CPD is a vanishingly small fraction of available thiol.

**(3) The plausible rescue also fails — and this is the interesting part.** If luminal thiol is the problem, the logical fix is to deliver ebselen **systemically**, reaching the colonocyte from the **basolateral** side and bypassing the luminal thiol sink entirely — i.e. **inverting the inversion** for this compound. But plasma is also thiol-rich: ebselen binds **albumin Cys34** essentially quantitatively (>99%), and free fraction is minimal. This is consistent with the persistent low-exposure problems across ebselen's clinical development history (SPI-1005 programs). **Both routes are blocked by the same chemistry.**

**(4) Secondary mechanism, same problem.** §2.4 notes *C. difficile* Stickland fermentation depends on the **selenoproteins PrdB and GrdA**, and flags ebselen as intersecting there. But those are **intracellular bacterial** targets — ebselen would have to survive the lumen and then enter the bacterium. Same sink, one more membrane.

**Verdict D — the target is excellent, the chemotype is wrong for this compartment.** The productive recommendation is not to reformulate ebselen but to **retain the CPD target and replace the warhead**: a non-selenium, non-thiol-reactive CPD inhibitor (reversible, or a covalent warhead with lower promiscuity such as a tuned acrylamide) would inherit the validated mechanism without the luminal quenching. Alternatively, a **mucosally-cleaved prodrug** that liberates ebselen only after epithelial uptake. **Flagged to the SAR Analyst and Chemist as a warhead-replacement problem, not a formulation problem.**

---

### 2.9 NICLOSAMIDE — Score 3/10 | Verdict D | Confidence MODERATE | Evidence: mixed

```
═══════════════════════════════════════════════════════════
ADMET ASSESSMENT: NICLOSAMIDE (CHEMBL1448)
COMPARTMENT: C2 — mucosal/endosomal   VERDICT: D
═══════════════════════════════════════════════════════════
PROJECT DATA: molecular_weight = 327.12 | alogp = 3.86 | hba = 4 | hbd = 2
  psa = 92.47 | rtb = 3 | ro5_violations = 0 | aromatic_rings = 2
  heavy_atoms = 21 | qed_weighted = 0.66 | first_approval = 1982 | natural_product = 1
  SMILES: O=C(Nc1ccc([N+](=O)[O-])cc1Cl)c1cc(Cl)ccc1O
                        ^^^^^^^^^^^^^^ AROMATIC NITRO GROUP
═══════════════════════════════════════════════════════════
```

The task brief asks directly: *"BUT stability in anaerobic fecal environment?"* **The answer is no, and the reason is specific rather than general.**

**Deal-breaker 1 — anaerobic nitroreduction destroys the pharmacophore.** The SMILES carries an **aromatic nitro group**. §6.2 names nitro first among reducible groups that *"will be reduced"* at Eh ≈ −200 mV, and the colon is additionally rich in bacterial nitroreductases. Reduction (nitro → nitroso → hydroxylamine → **aryl amine**) is essentially certain.

Why that is fatal rather than merely inconvenient: niclosamide's proposed anti-TcdB mechanism is **protonophore-mediated endosomal deacidification**, blocking the pH-dependent delivery-domain insertion at §2.6 A.2 step 3 (the §2.6 target table lists *"niclosamide-like protonophores, endosomal acidification blockers"*). Protonophore activity requires an **acidic phenol** that can shuttle protons across the endosomal membrane — and that phenol's pKa (~5.6, unusually low for a phenol) is set by the **strongly electron-withdrawing para-nitro group**. Reduce nitro → amine and you replace a powerful σ/π electron-withdrawing group with an electron-**donating** one. **The phenol pKa rises by several units, the compound is no longer appreciably ionized at endosomal pH, and protonophore activity is lost.**

**The anaerobic colon selectively destroys the exact functionality the mechanism depends on.** This is a sharper failure than generic instability: the metabolite is not merely less potent, it is mechanistically inert.

**Deal-breaker 2 — solubility caps the free concentration, and §6.4's headroom argument does not rescue it.** Niclosamide is famously insoluble: **~0.5–2 µg/mL (≈1.5–6 µM)** in aqueous media near neutral pH. Reported anti-TcdB entry-blocking activity is in the **low-µM** range. So the maximum achievable **free, dissolved** luminal concentration sits at roughly the same order as the concentration required — **with no headroom at all.**

§6.4's reassurance that *"fecal concentrations routinely exceed MIC by 100–1000×, which relaxes potency requirements substantially"* is a **total**-concentration argument that tacitly assumes dissolution. Undissolved crystalline drug is pharmacologically absent. **Niclosamide is the candidate that most clearly exposes the limits of that reasoning**, and the reason it must be checked compound-by-compound rather than assumed (see Cross-Cutting Observation 2).

**Deal-breaker 3 — wrong compartment, three serial low-efficiency steps.** Like ebselen, niclosamide's site of action is intracellular (C2 — host endosome). It must (i) dissolve, (ii) cross the mucus layer, (iii) enter the colonocyte. Step (i) is already limiting.

**Toxicity alert (relevant here, not theoretical).** Nitroaromatic → nitroreduction → **hydroxylamine intermediate** is a classic mutagenicity structural alert (skill file: *"Nitro group → nitroreduction to amines → mutagenicity risk"*). In most tissues this is a modest concern; **in a lumen with high bacterial nitroreductase activity it is the dominant metabolic fate**, making genotoxicity a live concern for any extended course. Note the contrast with metronidazole (§2.4), where the identical chemistry *is* the mechanism — the difference is that metronidazole's radical is generated **inside the target organism** by ferredoxin-mediated reduction, whereas niclosamide's would be generated **in the lumen at large**.

**On rescue paths — an important distinction:** reformulation (niclosamide ethanolamine salt, nanocrystal, amorphous solid dispersion) addresses **only deal-breaker 2**. It does nothing for nitroreduction. **The two problems need different solutions and reformulation alone is not sufficient** — a point I would expect a formulation-first analysis to miss.

**→ SAR recommendation (flagged to the SAR Analyst):** synthesise a **des-nitro analog** replacing the nitro with a strongly electron-withdrawing but **non-bioreducible** group — **–CF₃** or **–CN** — preserving the low phenol pKa and hence protonophore activity while removing both the anaerobic-inactivation and the mutagenicity liabilities. Such analogs typically also have improved solubility relative to the nitro parent. **This single modification addresses all three deal-breakers, and whether it preserves anti-TcdB activity is the question that determines whether niclosamide is salvageable at all.**

---

### 2.10 CONESSINE — Score 2/10 | Verdict F | Confidence MODERATE | Evidence: knowledge-based

**Absent from project data** (not in approved drugs; not in the 25-row natural-products stub). Steroidal alkaloid from *Holarrhena antidysenterica* (Kutaja) — the disease model discusses this plant at §7.2.

**Structure:** C₂₄H₄₀N₂, MW 356.6. Conanine steroidal skeleton with **two basic nitrogens** (3-dimethylamino + pyrrolidine ring N), essentially no polar functionality, cLogP ~4.5–5.

**Documented CNS activity (histamine H₃ receptor antagonist) is simultaneously proof of systemic absorption and proof of BBB penetration.** For a compound intended to act in the colonic lumen, that is a pharmacokinetic disqualification derived from the compound's own best-characterized pharmacology.

**Triple PK failure — and the failures compound rather than merely coexist:**

1. **Absorbed** → luminal concentration falls while systemic exposure rises. This is the exact inverse of §6.2's requirement (*"LOW oral bioavailability, ideally <5%"*). Compare metronidazole (§2.4), *"systemically absorbed (a liability here — absorption means less drug reaches the colon)"* — the disease model has already demoted a drug for precisely this property.

2. **Dicationic at colonic pH** → both amines (pKa ~8–9) are >99% protonated at pH 6–7, triggering §6.2's *"flag any strongly cationic candidate"* fecal-binding warning. **Conessine gets the worst of both worlds simultaneously: absorbed enough to lose the lumen, and cationic enough that what remains luminal is adsorbed to fecal solids and mucin.** Berberine at least converts its permanent charge into excellent luminal retention; conessine's basic amines are neutral enough at intestinal pH to permit absorption, yet protonated enough at colonic pH to be bound. **It occupies the worst point on that axis.**

3. **CNS-active in the one population §3.4 explicitly says to avoid CNS-active agents in.** §3.4: *"Elderly (≥65)… Favor non-absorbed agents; **avoid CNS-active**, QT-prolonging, or nephrotoxic candidates."* The CDI cohort is median age 65–75 with high dementia, delirium, and falls prevalence and frequent LTCF residence (§3.1, §3.2). H₃ antagonism is wake-promoting and psychoactive. **This is a population-level disqualifier independent of any efficacy consideration.**

**Additional structural alerts (skill file rubric):**
- **hERG:** basic nitrogen + lipophilic scaffold + logP >3 → hERG/QT alert, in a population already stacked with QT-prolonging fluoroquinolones, amiodarone, haloperidol, and quetiapine (§3.3). QT stacking here is additive and clinically material.
- **Cationic amphiphilic drug (CAD) profile** → phospholipidosis risk on extended dosing.

**A warning for the Ethnobotany Expert — the traditional-use evidence may point at an actively harmful mechanism.** Kutaja's traditional antidiarrheal use is genuine, but the likely mechanism is **antimotility/antisecretory**, and §3.3 states: *"**Antimotility agents are relatively contraindicated in CDI** — risk of toxic megacolon by prolonging toxin contact time."* §7.1 separately instructs that traditional candidates be scored on microbiome modulation, host-directed anti-inflammation, and anti-virulence — **not** on symptomatic antidiarrheal effect. **A candidate whose traditional evidence base rests on slowing transit is not neutral in CDI; it is pointed the wrong way**, and symptomatic improvement could mask progression toward toxic megacolon. This is the clearest reject in the set, and the reason is not weak activity but active hazard.

---

## 3. CROSS-CUTTING OBSERVATIONS

**1. Three compartments, not two.** The luminal/systemic binary misfiles ebselen and niclosamide, whose targets (TcdB CPD autoprocessing; endosomal acidification) are **inside host colonocytes** per §2.6 A.2. For C2 candidates, low absorption is not automatically a virtue — they need *mucosal uptake without systemic distribution*, a narrow and rarely-achieved window. §6.2 should be read as having three columns.

**2. Free vs total luminal concentration is the real currency, and nothing in this project measures it.** §6.4's *"100–1000× fecal MIC headroom"* is a **total**-concentration argument. Two distinct mechanisms attack the **free** fraction: **cationic fecal/mucin binding** (berberine, conessine) and **dissolution limits** (niclosamide). Both are invisible to total-concentration reasoning, and §6.2 does flag the first (*"measured fecal MIC ≫ broth MIC for many compounds"*) without integrating it into §6.4's headroom argument.

> **Highest-value single experiment across the whole candidate set: measure MIC in 10–20% fecal-slurry-supplemented medium alongside broth MIC for every luminal candidate.** It is cheap, it is one assay, and it resolves the largest single uncertainty in this analysis — including the berberine toxin-induction question below.

**3. The anaerobic reducing environment is the dominant chemical-stability filter, and it sorts this set cleanly.** Applying §6.2's reducible-group test:

| Candidate | Reducible group | Consequence |
|---|---|---|
| Niclosamide | **Aromatic nitro** | Reduced → phenol pKa rises → protonophore pharmacophore destroyed + mutagenic hydroxylamine intermediate |
| Ebselen | **Se electrophile** (thiol-reactive) | Quenched by luminal cysteine/GSH/H₂S before reaching mucosa |
| Fidaxomicin, vancomycin, berberine, UDCA, ibezapolstat | None | Pass |

**The two candidates that fail on chemistry are the same two that are misfiled on compartment** — a striking convergence, and it means these are chemotype problems, not delivery problems. Metronidazole (§2.4) shows the same chemistry can be *exploited*, but only when reduction occurs inside the target organism rather than in the lumen at large.

**4. Microbiota-dependence has a direction, and §6.2 only documents one of them.** §6.1/§6.2 warn that microbiota-triggered *release* fails in dysbiosis. But **berberine's** microbiota-dependent *activation* to the absorbable dihydroberberine also fails in dysbiosis — which **increases** luminal drug. Meanwhile **UDCA's** dependence on the depleted `bai` guild may run the harmful way *if* LCA is the effector species. **Direction must be determined per candidate; dysbiosis-dependence is not uniformly a liability.**

**5. Diarrhea-shortened transit also cuts both ways.** §6.2 lists it as a general liability (reduced colonic residence). **For UDCA it inverts:** accelerated transit defeats ileal ASBT reabsorption and *increases* colonic bile acid delivery precisely during active disease.

**6. PK excellence is a gate in CDI, not a discriminator — and the Candidate Ranker should treat it that way.** §4.5 records that ridinilazole, surotomycin, and cadazolid all had adequate luminal PK and adequate narrowness and all still failed to differentiate on sustained response. **Ibezapolstat's near-ideal PK (9/10) therefore should not be read as a strong overall signal.** PK eliminates candidates; it does not select them. The actual discriminator per §1.5(b)/§4.6 is microbiome sparing and restoration — a **spectrum** question, which belongs to the Chemist and Target Profiler, not to me. I want this stated plainly because a PK score of 9 next to a benchmark score of 10 invites exactly the wrong inference.

**7. The fulminant subtype is a route orphan — and one candidate quietly solves it.** §1.5(c)/§6.1: ileus makes oral delivery pharmacokinetically unavailable in fulminant CDI (3–8% of hospitalized cases, 30–50% mortality). Only **three of ten** candidates have any non-oral route:

| Candidate | Non-oral route | Status |
|---|---|---|
| Bezlotoxumab | IV (native) | Approved |
| **Aprepitant** | **IV via fosaprepitant** | **Approved prodrug, in project data (CHEMBL1199324)** |
| Vancomycin | Rectal (off-label salvage) | §6.1 |
| Fidaxomicin, ibezapolstat, berberine, UDCA, niclosamide, ebselen, conessine | **None** | — |

Aprepitant's systemic profile — a liability in every other CDI context — is **exactly right for the one subtype where §1.5(c) says systemic exposure is desirable**, with the IV formulation already approved and on the shelf.

**8. Both major colon-targeting delivery technologies are compromised in this specific population — which favors intrinsic physicochemistry over formulation.**
- **pH-responsive coatings** (Eudragit S/L) are defeated by PPIs, which §3.3 calls *"extremely common, often unnecessarily continued"* in CDI patients.
- **Microbiota-triggered release** (azo-bond, polysaccharide matrices) *"may fail in exactly the patients it targets"* (§6.1).

**Therefore candidates that reach the colon by intrinsic physicochemistry — berberine's permanent quaternary cation, fidaxomicin's and vancomycin's size and polarity — are structurally more robust than any candidate requiring a delivery system.** This is a design principle, and it materially strengthens berberine's position relative to UDCA (which needs colon-targeting to work). **Flagged to the Chemist and Combination Designer.**

**9. Non-absorption is a conditional safety asset, not an absolute one.** §6.2 and §3.3 both instruct scoring non-absorption as a safety asset. True — **but §3.4 notes vancomycin accumulates systemically in severe colitis with renal impairment.** Barrier breach plus impaired clearance is common in exactly the sickest patients. The luminal candidates' clean-DDI advantage is weakest where the disease is most dangerous. Bezlotoxumab, whose clean profile derives from having no metabolic clearance pathway at all, retains the advantage unconditionally.

---

## 4. RANKED SUMMARY

| Rank | Candidate | Score | Verdict | One-line PK judgement |
|---|---|---|---|---|
| 1 | Fidaxomicin | 10 | A | Benchmark. <1% absorbed, >4000× fecal MIC headroom, active gut metabolite, no reducible groups |
| 2 | Ibezapolstat | 9 | A | Designed-in luminal PK, demonstrated in humans; but PK is not the differentiator (§4.5) |
| 3 | Vancomycin PO | 9 | A | Ideal luminal PK; deductions for fecal persistence driving dysbiosis and systemic accumulation in severe colitis |
| 4 | Berberine | 8 | B | Best intrinsic luminal profile among repurposables (permanent cation, <1% F); **flagged for sub-MIC toxin induction** |
| 5 | UDCA | 6 | C | Reaches colon only as enterohepatic spillover; needs colon-targeting or ASBT inhibition; active species [UNCERTAIN] |
| 6 | Bezlotoxumab | 6 | B | Clean PK, no metabolic clearance; delivery inflammation-gated; IV + CHF fluid-load signal |
| 7 | Aprepitant | 5 | C | No tissue-access problem; CYP3A4/2C9 DDI is the deal-breaker — **except in fulminant CDI, where fosaprepitant IV is a real opportunity** |
| 8 | Ebselen | 4 | D | Right target, wrong warhead — Se electrophile quenched by luminal thiols; both luminal and systemic routes blocked by the same chemistry |
| 9 | Niclosamide | 3 | D | Nitro reduced anaerobically → pharmacophore destroyed; free conc. solubility-capped at the required concentration; reformulation is insufficient |
| 10 | Conessine | 2 | F | Absorbed **and** fecal-bound **and** CNS-active in an elderly cohort; traditional antimotility mechanism is contraindicated (§3.3) |

---

## 5. QUESTIONS FOR OTHER AGENTS

**→ Target Profiler / Chemist / SAR Analyst — the compartment question (highest priority):**
For **ebselen** and **niclosamide**, is the intended site of action the colonic *lumen* or the host colonocyte *cytosol/endosome*? Per §2.6 A.2, CPD autoprocessing (InsP6-triggered) and endosomal acidification are both **intracellular**. If so, low absorption is a **liability** for these two, not an asset, and they must be re-scored against a mucosal-uptake requirement rather than luminal retention. This changes their optimisation direction entirely.

**→ SAR Analyst — the niclosamide salvage question:**
Does a **des-nitro analog** bearing a non-bioreducible electron-withdrawing group (**–CF₃** or **–CN**) retain the low phenol pKa required for protonophore activity, and does it retain anti-TcdB activity? This single question determines whether niclosamide is salvageable. Reformulation addresses solubility only and cannot address nitroreduction.

**→ Target Profiler / Pathway Analyst — the UDCA effector question:**
Is the active anti-germination species **UDCA itself**, or **LCA** produced downstream by 7α-dehydroxylation? §2.2/§2.3 credit LCA with germination inhibition, but the `bai` guild that produces it is depleted in CDI (§2.2). If LCA is the effector, UDCA depends on the exact enzymology the disease destroys, and the rational move is to **deliver LCA or a non-convertible LCA analog directly**, bypassing the missing conversion.

**→ Chemist / Combination Designer — the berberine free-fraction question:**
What is berberine's **fecal-matrix MIC** versus its broth MIC, and does toxin output rise at sub-MIC concentrations? §6.2 flags cationic compounds for fecal binding and §2.5 warns explicitly about sub-MIC toxin induction. **Berberine is the candidate that most exactly matches that warning's description.** If a toxin-induction hump exists below MIC, berberine monotherapy is disqualified and it becomes combination-only (per §A.2's *"vancomycin + berberine"*).

**→ Combination Designer — bile acid delivery:**
Would **UDCA + an ASBT inhibitor** (odevixibat/elobixibat class) deliberately deliver therapeutic bile acid concentrations to the colon, bypassing the enterohepatic recapture that currently limits UDCA? Both components are approved.

**→ Clinical Feasibility / Drug Repurposing Strategist — the fulminant opportunity:**
**Fosaprepitant** (approved IV prodrug, in project data at CHEMBL1199324) offers a route into **fulminant CDI**, where §1.5(c) says oral delivery is pharmacokinetically unavailable and systemic exposure is desirable — the only subtype with that logic, 30–50% mortality, and no adequate therapy. Is this worth a dedicated candidate line separate from oral aprepitant?

**→ Safety Pharmacologist:**
(a) Berberine carries `withdrawn_flag = True` in `chembl_approved_drugs.csv` with **no** corresponding row in `chembl_drug_warnings.csv` — please verify or discard; I have not relied on it.
(b) Aprepitant's **CYP2C9 induction** compounds with §3.3's separate note that warfarin INR is already destabilised by antibiotics and microbiome disruption — **two independent, same-direction pressures on anticoagulation** in a heavily anticoagulated cohort. Worth assessing as a compound risk rather than two separate ones.

---

## 6. DATA GAPS AND DATA-QUALITY FINDINGS

**Coverage of this candidate set in project data: 6 of 10** (fidaxomicin, vancomycin, berberine, niclosamide, aprepitant, UDCA — plus useful comparators: metronidazole, fosaprepitant, cholic acid, deoxycholic acid, taurursodiol, obeticholic acid). **Absent: ebselen, ibezapolstat, conessine, bezlotoxumab** — all four assessed knowledge-based.

### Findings that affect this analysis

**1. `oral_bioavailability` is unusable for this task — and using it would have inverted the answer.**
The column is 3276/3276 populated, but it is a **boolean**, not a percentage, and it disagrees with reality on the key cases:

| Drug | `oral_bioavailability` | Actual | |
|---|---|---|---|
| Vancomycin | `True` | ~0% absorbed | ✗ |
| Niclosamide | `True` | ~10% | ✗ |
| Berberine | `False` | <1% | ✓ |
| Metronidazole (base) | `True` | ~100% | ✓ |
| Metronidazole **HCl** | `False` | same molecule | ✗ inconsistent |
| Deoxycholic acid | `False` | — | ✗ (identical descriptors to ursodiol, which is `True`) |

It appears to encode a ChEMBL **administration-route** flag ("is an oral product marketed"), not absorption. Given that CDI candidate scoring turns *entirely* on bioavailability, **this column must not be used for ADMET work.** *Recommendation:* rename to `oral_route_flag`, and source measured %F separately (DrugBank, FDA labels, or ChEMBL's `oral`/`parenteral`/`topical` flags scraped explicitly).

**2. All distribution-relevant descriptor columns are empty — 0/3276.**
`molecular_species`, `bioavailability_score`, `permeability`, `logd`, `cx_logp`, `cx_logd` are **entirely unpopulated**. These are exactly the columns the ADMET skill's **Distribution** section is built on (skill file lines 157, 190–194). Only the Lipinski/Veber block is usable (`psa`, `qed_weighted` at 2973/3276 ≈ 91%; MW/alogp/hba/hbd/rtb/ro5 similar).

Practical consequence: **berberine's permanent cationic charge — the single most important PK fact about it — had to be read off the `molecular_formula` field (`C20H18NO4+`) because `molecular_species` is blank.** Populating `molecular_species` would make the §6.2 cationic-fecal-binding flag automatable across the whole file.

**3. The two gold-standard CDI drugs have no computed descriptors at all.**
Fidaxomicin (MW 1058.05) and vancomycin (MW 1449.27) have **every** computed field blank except molecular weight — the descriptor calculator evidently skipped out-of-range molecules. Given §6.2's instruction that bRo5 character is *desirable* here, **any automated Ro5 filter over `chembl_approved_drugs.csv` would silently discard the two best drugs for this indication.** Worth an explicit guard in any downstream filtering code.

**4. Four supporting files are stub/test scrapes — no DDI or warning cross-referencing was possible.**

| File | Rows | Status |
|---|---|---|
| `chembl_drug_mechanisms.csv` | **10** | Stub. **None** of the 10 candidates present (checked by ChEMBL ID) |
| `chembl_drug_warnings.csv` | **9** | Stub. No candidate rows — berberine's `withdrawn_flag` is unverifiable |
| `chembl_toxicity.csv` | **1** | Effectively empty |
| `chembl_natural_products.csv` | **25** | Stub **and mislabeled** — contains prazosin, nicotine, α-bungarotoxin. Not a curated natural-product set |

The skill file's *"Cross-Reference for DDI Risk"* workflow (lines 165–169) depends on `chembl_drug_mechanisms.csv` and **could not be executed**. All DDI analysis in §2.7 was substituted from disease-model §3.3 plus training knowledge.

**5. Probable column-alignment bug in `chembl_drug_metabolism.csv` (10,000 rows).**
The `drug_name` field is mismatched against `drug_chembl_id`. Example: `CHEMBL1200869` (metronidazole HCl) appears on separate rows with `drug_name` = PRAZOSIN, NICOTINE, OFLOXACIN, NALIDIXIC ACID, INDOMETHACIN, SULBACTAM, TAZOBACTAM, CIPROFLOXACIN, NORFLOXACIN, AMPHETAMINE — while `substrate_chembl_id`/`substrate_name`/`metabolite_name` on those same rows are internally consistent and correct (metronidazole → hydroxy/acetic-acid metabolites). The `drug_chembl_id`↔`drug_name` pairing looks like a cartesian join or an off-by-one in the scraper's field mapping. **Recommend re-checking `src/scrapers/chembl/chembl_scraper.py` field alignment for the metabolism endpoint** — 10,000 rows are affected and the file is currently unsafe for automated DDI inference.

### Domain data absent from the project entirely

None of the measurements that actually govern CDI pharmacokinetics exist locally:
- **Fecal / colonic drug concentrations** — the primary PK endpoint for this disease
- **Fecal-matrix MICs** (vs broth MIC) — the free-fraction question of Cross-Cutting Observation 2
- **Aqueous solubility** — decisive for niclosamide, absent for all compounds
- **Colonic transit / residence-time modeling**, including the diarrhea case
- **Commensal spectrum data** (Lachnospiraceae, Ruminococcaceae, Bacteroidetes) — §A.1 question 2 and, per Cross-Cutting Observation 6, the actual discriminator in this disease
- **Anaerobic / reducing-condition stability assays** — would have settled niclosamide and ebselen empirically rather than by inference

Every luminal-exposure statement in this report is therefore **predicted, not measured** — consistent with the skill file's guardrail to *distinguish prediction from measurement*, and with §A.3's warning that preclinical CDI data predict Phase 3 outcomes unusually poorly.

---

*End of ADMET analysis. Prepared by the Pharmacokinetics Specialist for Phase 1 of the CDI disease-explorer pipeline.*
