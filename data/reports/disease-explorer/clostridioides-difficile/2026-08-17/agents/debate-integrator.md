# Debate Round — Integration Specialist

## *Clostridioides difficile* Infection (CDI)

**Role:** Resolve cross-agent conflicts, weight evidence, and build the strongest surviving case for each candidate.
**Inputs read:** disease-model.md · round1-complete-scores.md · round2-synthesis.md · p2-literature.md · p2-pathway.md · p2-safety.md · p2-sar.md · p2-repurposing.md · p1-admet.md (targeted) · p1-clinical-landscape.md (targeted)
**Devil's Advocate report:** ⚠️ **NOT AVAILABLE at time of writing.** `agents/debate-advocate.md` does not exist. §9 below is a pre-committed response frame; the integration should be re-run against the Advocate's actual challenge when it lands. Every conclusion here is stated so that it can be attacked on the record.

---

## 0. EXECUTIVE SUMMARY

**Three data-integrity corrections must propagate before any Phase 3 scoring**, because two of them changed my rankings and one of them is in the Round 2 synthesis *and* in the tasking brief:

| # | Correction | Consequence |
|---|---|---|
| **A** | **"Berberine sub-MIC toxin induction at 6–12 h" does not exist in any Phase 2 report.** It was ADMET's Phase 1 *hypothesis* (p1-admet.md:428). The Literature Reviewer **refuted** it: TcdA −57%, TcdB −54% at ½ MIC, with *tcdA/tcdB/tcdE/tcdR* **down**-regulated at 24–48 h (p2-literature.md:118). Round 2 listed it as Unresolved Conflict #2 and the brief repeats it. | Remove from the unresolved list. **Replace** with the two liabilities that *are* real and new: ***spo0A* upregulation** and **biofilm enhancement specifically with vancomycin at ½ MIC**. |
| **B** | **TUDCA is a live head-to-head conflict, not a consensus candidate.** Pathway §2.5 recommends it (+0.5 to UDCA's score); **SAR §6.4 Proposal U-6 explicitly rejects it** — "on the agonist side of the C24 switch… flagged specifically because this is a trap a descriptor-driven pipeline would walk into." Round 2 credited it to "Pathway+SAR" at 7.5. | The pipeline's **top recommended combination** (`Fidaxomicin → UDCA/TUDCA maintenance`) contains a component one Phase 2 agent says is mechanistically backwards. Resolved in §2, Conflict 2 — **Pathway wins**, but the regulatory premise for TUDCA is separately weak. |
| **C** | **"U-1 Urso-CamSA (8.0)" conflates two different SAR proposals.** SAR **U-1 is CamSA** (cholate core, feasibility **8/10**). **U-3 is urso-CamSA** (UDCA core, feasibility **6/10**, described as "speculative"). | The 8.0 belongs to the *known, mouse-validated* molecule; the *novel* one scores 6.0. Do not fund the novel one on the known one's score. |

**The pipeline-level finding.** No single agent stated it, but it falls out of combining three of them:

> Six of ten candidates sit on **C2 (vegetative fitness)** — an axis where **eight** programmes have now failed (ridinilazole, surotomycin, cadazolid, LFF571, DS-2969b, OPS-2071, ramoplanin, Ramizol). Meanwhile **C6 has zero coverage, C1/C3/C7/C8 have one each, and bezlotoxumab's January 2025 withdrawal just emptied C4.** Separately, the Drug Repurposing Strategist found that the **highest-scoring asset in the entire analysis (ribaxamase, 7.4) targets an axis with no candidate in the set at all**, and that **6 of 12 CDI programme failures were financial, not scientific.**
>
> **The pipeline's binding constraint is not candidate quality. It is axis allocation and capital structure.** CDI reliably kills scientifically sound assets for want of a sponsor. That inverts the standard question: the highest-expected-value action is not "pick the best molecule," it is "acquire a clinically de-risked, financially orphaned asset on an unoccupied axis."

**Single-program recommendation: ribaxamase acquisition**, gated on a $150–300K diligence pass. It is the only asset in the analysis with **positive human Phase 2b data**; it is the only **primary-prevention** asset; and it structurally escapes all three of the failure modes that killed this field (the initial-cure non-inferiority bar, the sustained-response translation penalty, and the diarrhoea-endpoint confound). Full argument and honest counter-case in §5.

**Total cost to resolve every live conflict in this analysis before committing to any $45M+ programme: ~$700K–1.4M** (§6).

---

## 1. HOW I WEIGHTED THE EVIDENCE

Stated up front so the Devil's Advocate can attack the weighting rather than only the conclusions.

| Principle | Application here |
|---|---|
| **1. Measured beats inferred.** | Kills UDCA's delivery-rescue strategies (delivery was *measured* at 43.5% of the fecal pool). Kills the ebselen 8.5 target score as a *molecule* score. Rescues niclosamide from a purely chemical nitro-reduction prediction. |
| **2. A discount schedule must be applied symmetrically.** | The Literature Reviewer built an excellent preclinical discount schedule (§8) — hamster survival/prophylaxis caps at **3.5** — and then applied it **only to positive evidence**. The UDCA refutation rests on a **hamster prophylaxis survival study**. Under its own schedule that study is a 3.5-grade instrument *in either direction*. See §2, Conflict 1. |
| **3. Negative results at n=8 are weak evidence of absence.** | Palmieri's hamster arms were 5/8 vs 5/8. Detecting a 62.5%→25% mortality drop at 80% power needs ~n=27/arm. p=0.78 at n=8 means "we could not tell," not "it does not work." |
| **4. Coupled efficacy/safety invalidates therapeutic-index reasoning.** | The Safety Pharmacologist's Finding 5. I have applied it as a **hard structural filter**, and it is what demotes niclosamide below the Round 2 ranking despite its best-in-set preclinical package. |
| **5. Compartment before bioavailability.** | The Repurposing Strategist's refinement of the Ethnobotany inversion: *invert bioavailability scoring only after establishing which compartment the target sits in.* This single rule resolves three separate Round 1 conflicts. |
| **6. Positioning is scored as a property of the asset, not the trial.** | CDI replacement trials 0-for-3, add-on trials 3-for-3. An asset whose evidence base is in the replacement configuration carries that as a *defect*, not a fixable design choice. |

---

## 2. CONFLICT RESOLUTION TABLE

### Conflict 1 — UDCA: Pathway (7.5, mechanism sound) vs Literature (3.0, REFUTED)

**Framing check first: these two agents do not actually disagree about the mechanism.** The Literature Reviewer explicitly grants "strong, reproducible *in vitro* germination *and* growth inhibition." The disagreement is entirely about whether that translates.

**Which side has stronger evidence?** *Neither, and that is the finding.* Both instruments are weak:

| Literature's case | The weakness I am adding |
|---|---|
| Hamster mortality 62.5% vs 62.5%, p=0.78 (n=8/arm) | **Underpowered by ~3×.** Only an enormous effect was detectable. And under the Literature Reviewer's **own §8 schedule**, a hamster prophylaxis/survival study caps at **3.5/10** as an evidence instrument — which must apply to its *negative* result too. This is an underpowered null in a low-grade model, not a refutation. |
| Human observational: CDI 25% on UDCA vs 9.2% controls | **The comparator differs by PSC status, not by UDCA.** PSC-IBD is itself an established independent CDI risk factor. The design cannot separate drug from disease. This is uninformative, not wrong-direction. ⚠️ **Data-integrity flag:** the same report gives this denominator as both **4/12** (§3 body) and **4/16** (elsewhere); 25% is consistent only with 4/16. Verify before citing. |
| Delivery was achieved (43.5% of fecal BA pool) yet it still failed | **43.5% of the *pool* is not a free concentration.** Pathway §2.3 flags CMC ceiling and solids partitioning; competitive inhibition at CspC requires **free monomer**. The Repurposing Strategist's Stage 0 specifies "free UDCA in **fecal water**, not total fecal" — precisely because nobody has that number. The measurement that would close this has not been made. |
| **Cross-cutting** | The **36% CDI translation rate** was used to discount positive preclinical data. Consistency requires discounting the negative preclinical data by the same factor. |

**Resolved by route of administration?** **No — and this part of Literature's finding is decisive and should stand.** Colon-targeted UDCA, UDCA + ASBT/IBAT inhibitor, and dose escalation all solve a delivery problem that does not exist in the dysbiotic patient. **Stand those strategies down permanently.** (The IBAT combination carries an additional veto: it shunts *taurocholate*, the germinant, to the colon alongside the inhibitor.)

**Resolved by combination therapy?** **Yes — and this is the strongest surviving argument for UDCA.** Palmieri tested UDCA as **monotherapy prophylaxis against a 10⁴-spore bolus of VPI10463 in an animal that cannot recover**. The proposed clinical use is **adjunct maintenance against a static, non-replenishing reservoir after fidaxomicin has cleared vegetative cells and suppressed new sporulation (C8)**. Three specific mismatches:

1. **Inoculum structure.** Germination inhibition is competitive and probabilistic — it lowers per-spore germination probability. Against a large synchronised bolus, even a 2-log block leaves ample germinating cells to kill a hamster. Human recurrence proceeds from a *small, asynchronous* endogenous reservoir. Anti-germinants are inherently **inoculum-dependent**, and the model used the inoculum designed to overwhelm.
2. **Configuration.** Palmieri is a **replacement-configuration** study — the 0-for-3 path. The proposed use is **add-on** — the 3-for-3 path.
3. **Endpoint.** Hamsters cannot model recurrence at all. Literature's own §8 states a mouse recurrence study should outrank a hamster survival study; no mouse recurrence study of UDCA exists.

**Is the conflict a feature?** Partly. UDCA's millimolar potency is fatal for monotherapy but adequate for an 8–12-week hold against a static reservoir — and Pathway's **self-tapering handoff** (as the `bai` guild returns, UDCA is converted to LCA, itself a C1 *and* C2 inhibitor) is genuinely elegant: the bridging drug is consumed exactly as the endogenous mechanism it substitutes for comes back online.

**Does disease context change the weighting? Yes — and this is the reframe that justifies keeping UDCA alive.** §4.6 unmet need #1 is *recurrence prevention usable in **immunocompromised** patients* — the population that **cannot receive live biotherapeutics**. In immunocompetent patients UDCA competes against VOWST/REBYOTA/VE303, which have FMT-class efficacy, and it loses. In the immunocompromised, **the alternative is nothing.** UDCA's strategic value is not that it is the best anti-germinant; it is that it is a **non-live option in the only population with no option at all.** At that positioning, a moderate probability of success is worth a $1–3M option.

> **RESOLUTION: UDCA → 5.5.** Both the 7.5 promotion and the 3.0 refutation are over-claims. The disposition is **neither kill nor promote: buy the option.** Fund Stage 0 ($1–3M); do not fund the $45–85M programme. **Sequencing correction to the Repurposing plan: Stage 0 as specified compares fecal concentration to an anti-germination IC₅₀ that does not exist** (Literature Gap #4). Run the $50–100K dose-response assay **first** so Stage 0 has a threshold to compare against.
> **Residual uncertainty:** free monomeric fecal-water concentration; the UDCA:taurocholate ratio; whether any anti-germinant can hold against a replenished reservoir (a class question, not a UDCA question).

---

### Conflict 2 — TUDCA: Pathway (recommend) vs SAR (explicit REJECT) ⚑ *unflagged by Round 2*

**Which side has stronger evidence? Pathway, clearly.**

The germinant/inhibitor determinant at CspC is the **12α-hydroxyl**, not C24 conjugation. The bile-acid series settles it:

| | 12α-OH present | 12α-OH absent |
|---|---|---|
| **Conjugated** | taurocholate, glycocholate, taurodeoxycholate → **GERMINANT** | **taurochenodeoxycholate → INHIBITOR** |
| **Unconjugated** | cholate, deoxycholate → **GERMINANT** | CDCA, UDCA, LCA → **INHIBITOR** |

Conjugation state varies *within* both columns and does not flip the sign. **Taurochenodeoxycholate is the decisive counterexample**, and Pathway §2.1 cites it explicitly.

**SAR's C24 switch is a real finding that has been over-generalised.** CamSA is a **bulky aryl** amide on a **cholate (germinant) core** — it demonstrates that steric bulk at C24 blocks *productive triggering*. It does **not** demonstrate that a *small polar* C24 amide converts an *antagonist* core into an agonist. SAR inferred "taurine causes germination" from "taurine is on the germinant taurocholate," which is confounded by the core.

**SAR's practical caution survives, in reduced form:** TUDCA's anti-germination potency has never been measured against UDCA's. That is a $50–100K assay, not a rejection.

**Resolved by route?** This *is* the route question, and Pathway's physics is sound: TPSA 123.9 vs 77.8 and alogp 3.40 vs 4.48 predict lower jejunal absorption and higher colonic delivery; BSH depletion in CDI means TUDCA arrives *and stays* conjugated — a second dysbiosis-protects-the-drug effect. TGR5 (#62) agonism adds real C5/C6 tone that UDCA lacks, on the axis with zero coverage.

**⚠️ A regulatory issue neither agent surfaced.** Taurursodiol's 2022 US approval was as a **fixed-dose combination** (with sodium phenylbutyrate). To my knowledge that product was **withdrawn from the market in 2024 after its confirmatory Phase 3 failed** — which would leave **no marketed US RLD containing taurursodiol**, and the widely available supplement form is not an RLD. ⚠️**Requires formal listed-drug verification before any TUDCA claim of a 505(b)(2) advantage is made.** If confirmed, **TUDCA's regulatory story is worse than UDCA's, not better** — which inverts the Round 2 framing.

> **RESOLUTION: Pathway wins on mechanism; SAR's warning is downgraded to a measurement; TUDCA's *regulatory* advantage is likely illusory. TUDCA → 5.5 as a scientific backup to UDCA, NOT as a faster path, and NOT as a co-equal in the flagship combination.**
> **Practical consequence:** the combination should read **"Fidaxomicin → UDCA maintenance"** with TUDCA as a formulation contingency pending assay and RLD verification — not "UDCA/TUDCA" as if interchangeable.
> **The one construct both theories endorse: SAR's U-3 "urso-CamSA"** — 7β core (antagonist under Pathway's 12α rule) **plus** bulky C24 aryl sulfonamide (antagonist under SAR's C24 rule). It is the single molecule where the two conflicting frameworks agree, which is a real, non-obvious argument for making it. **But fund it at U-3's 6/10, not U-1's 8/10.**

---

### Conflict 3 — Niclosamide: the delivery paradox is built on a false premise

**The brief asks: does reduced nitroreduction (favourable) or increased barrier permeability (unfavourable) dominate?**

**Neither dominates, because they are not opposed.** Both push toward *more active drug at the target*: reduced nitroreduction preserves the pharmacophore; increased permeability increases colonocyte uptake. For **efficacy** they are additive positives. The problem is that the second is *also* the toxicity route. So the correct statement is not "which effect wins," it is:

> **In CDI, niclosamide's efficacy and its toxicity are driven by the same variable — mucosal uptake — and disease severity raises both together. The therapeutic index is not a constant; it narrows as the patient gets sicker.** (Safety Finding 4 × Finding 5, compounding.) That is an inverted risk structure and it is disqualifying for the severe stratum specifically.

**Is "insoluble enough to limit absorption but soluble enough to enter colonocytes" a feasible pharmaceutical window?**

**The question is mis-specified, and SAR §2.7 has the correct model.** The Literature Reviewer ("the safety margin rests on insolubility") and the Safety Pharmacologist (§5.4, "dissolution gates both") converged on the **same error**. SAR:

> *"The requirement is not 'low permeability', it is **'high cellular uptake, low systemic exposure'** — which is a **metabolic-clearance specification, not a permeability one**. Niclosamide already has that profile natively (absorbed but cleared by rapid glucuronidation/sulfation)."*

**This dissolves the paradox as posed.** The safety margin rests on **rapid presystemic UGT/SULT conjugation**, not on undissolved crystal. Two consequences:

1. **The decisive experiment changes.** It is not a dissolution study. It is **plasma parent-niclosamide and the glucuronide/sulfate ratio in a severe-colitis model, at a dose achieving colonocyte target engagement.** Measure the metabolic ratio, not the solubility.
2. **The des-nitro salvage becomes coherent rather than self-defeating.** SAR's own substituent scan (**–CN > –CF₃ ≫ –SO₂CH₃**) says –CN preserves the electron-withdrawal that sets the proton-shuttle pKa, so "the nitro is load-bearing" is a *pKa* constraint, not a *nitro* constraint. Des-nitro also removes the nitroso/hydroxylamine genotoxicity alert — which matters disproportionately here, because 15–25% of CDI patients have active malignancy on DNA-damaging chemotherapy, and the CDI exposure is **10–14× the anthelmintic cumulative dose** (20–28 g vs 2 g).

**Resolved by combination?** Partially — pairing with fidaxomicin lets niclosamide be dosed for the **C4** contribution only, at the lowest dose achieving toxin protection rather than at a dose chasing burden reduction.

**Is the conflict a feature? On pathway coverage, emphatically yes — and this is where Round 2 under-credited it.** Pathway scored niclosamide 4.0 partly for being *"redundant on C4 with bezlotoxumab."* **Bezlotoxumab was withdrawn in January 2025. That deduction is void.** Niclosamide is now the only small molecule with any claim on C4 at all. And its host-directed mechanism is **strain-agnostic** — it covers TcdA, TcdB **and CDT**, and is immune to the TcdB-subtype/receptor-switching variability (§A.3) that a CROPS-directed antibody is exposed to. That is coverage bezlotoxumab never had.

**The honest limit:** niclosamide blocks *endosomal escape*, which is **downstream of the receptor-binding branch** — so like ebselen, it misses the GTD-independent NOX1 necrosis arm. Its C4 coverage is real but **mechanistically incomplete**, and only receptor blockade sits upstream of that branch.

> **RESOLUTION: Niclosamide → 6.5** (down from Round 2's 7.0, up from Round 1's 5.1).
> **Upgrades:** C4 redundancy deduction void (bezlotoxumab withdrawn); best-designed preclinical package in the set on every axis that matters; strain-agnostic + CDT coverage; the "insolubility" objection is retired.
> **Downgrades:** the **uncoupling-vs-anti-TcdB selectivity ratio does not exist**, and mitochondrial uncoupling is **intrinsic to the protonophore mechanism** — it is not fixable by des-nitro or by formulation. Chemical coupling, not physical. Plus contingent RLD status, full CMC programme, 7–10 yrs, $75–140M.
> **Disposition: best *second* programme, contingent on two cheap experiments** (§6 items 2 and 5). Not the lead — too many unresolved unknowns to absorb the whole budget.
> **Residual uncertainty:** the selectivity ratio; anaerobic stability (never measured); whether human colonic uptake reproduces the mouse result in an aged, inflamed gut.

---

### Conflict 4 — Berberine: does the DDI end the development path?

**First, correct the record (Correction A above).** The sub-MIC toxin-induction fear that ADMET nominated as its highest-value experiment and proposed as a **hard stop** was **tested and refuted** — toxin *falls* at ½ MIC, comparably to vancomycin. **The hard stop does not trigger.** That is a genuine upgrade the Round 2 synthesis inverted into a downgrade.

**The real new liabilities are two, and they are worse than the one they replace:**

| Liability | Why it is specifically damaging |
|---|---|
| ***spo0A* upregulation at sub-MIC** | Berberine's entire proposed value is **recurrence prevention**, and recurrence is driven by the **spore reservoir**. A sporulation-promoting adjunct works against the exact endpoint it is proposed for. This is a mechanistic contradiction, not a generic safety flag. |
| **Biofilm enhancement with vancomycin at ½ MIC (p=0.02)** | It occurred in **precisely the combination** the mouse data supports and the pipeline routes to Combination Design. Not a hypothetical pairing — the proposed one. |

**Counterweight, and it is substantial:** **two independent laboratories, ten years apart, both positive, both in the recurrence configuration** (Lv 2015; IJAA 2025) — the best-replicated preclinical package in the set, generated in the *add-on* configuration that is 3-for-3 clinically. Either the *spo0A* effect is too modest to matter in vivo, or net benefit outweighs it. **The in vitro flags are hypotheses about the in vivo results, and the in vivo results are already in and positive.** They justify a cheap disconfirming experiment, not a kill.

**Does the DDI exclude the broader CDI population? No — and the Round 2 framing overstates it.**

The cyclosporine interaction is **L2 (gut wall)**, real, human, ~35% AUC increase. Precisely who is excluded:

- **Excluded:** solid-organ transplant on calcineurin inhibitors (cyclosporine, tacrolimus, sirolimus); **digoxin**; P-gp-dependent DOACs (dabigatran); ritonavir/cobicistat-boosted regimens.
- **NOT excluded:** most chemotherapy patients (few cytotoxics are P-gp-sensitive narrow-TI *oral* drugs); haematologic malignancy not on CNI; steroid-treated IBD; modern INSTI-based HIV regimens; and the large majority of the elderly, antibiotic-exposed population.

So it is a **labelling-and-screening problem covering an identifiable subgroup**, not a market exclusion — the same structure as amiodarone or clarithromycin in geriatrics. **But** digoxin and DOACs are over-represented in exactly this cohort, so the screening burden is real and it lands on the highest-need slice.

**Does the mechanism reclassification (host + microbiota, not antibacterial) make berberine more or less valuable? Both, and the direction that matters is "less."**

- **More valuable strategically:** it **exits the C2 graveyard** (8 failed programmes) and enters near-empty C5/C7. The fecal-matrix MIC question — Round 1's decisive experiment — becomes largely **moot**, because you are no longer asking it to kill. The 400×-worse-than-vancomycin MIC stops being the disqualifier it looked like.
- **Less valuable competitively, and this dominates:** as a host/microbiota modulator its comparator is no longer vancomycin — it is **live biotherapeutics with FMT-class efficacy and approved products**. Berberine has **zero human CDI data**. It moved out of a bad neighbourhood into one where it is outclassed by incumbents.

> **RESOLUTION: Berberine → 5.5** (down from 6.0). Net of a real upgrade (toxin-induction refuted; potency objection defanged by reclassification) and two real, endpoint-specific downgrades (*spo0A*, vancomycin-biofilm), plus a comparator set that got much stronger under reclassification.
> **Disposition: keep, do not lead.** Fund the **$150–300K *spo0A* in vivo disconfirming experiment** (§6 item 6) before anything larger. Literature §9 correctly calls this "the highest-value *disconfirming* experiment for the candidate currently best supported."
> **If pairing, pair with fidaxomicin, not vancomycin** — the biofilm signal is vancomycin-specific and fidaxomicin already spares C7.
> **Residual uncertainty:** publication bias (negative natural-product results are systematically under-published, so two positive studies with no published negatives is weaker than it reads); no FIC indices, so "synergy" is asserted not demonstrated; group sizes for both rodent studies unverified (Literature §14).

---

### Conflict 5 — Ibezapolstat and the ridinilazole rehabilitation

**The correction is real; the strategic inference drawn from it is backwards.**

Ridinilazole *did* deliver the recurrence advantage (8.1% vs 17.3%, P=.0002) and failed on **initial clinical response** (86.5% vs 92.3%). Round 2 read this as rehabilitating narrow-spectrum agents and nudged ibezapolstat **up**.

But follow the corrected lesson through: **if the binding constraint is initial cure, then a narrow-spectrum agent must first clear a non-inferiority margin on initial cure against an 85–92%-effective comparator — the exact bar ridinilazole missed by 6.2 points — before its recurrence advantage is even evaluable.** The correction does not lower ibezapolstat's bar; it **identifies precisely which bar killed the last eight entrants**, and ibezapolstat has not shown it clears it. Total human exposure is ~50–60 subjects.

**Genuine assets that the correction does not touch, and that I am crediting:**
- **LSAS 9/10** — second only to fidaxomicin. DNA pol IIIC has no *Bacteroidetes* and no human homolog.
- **The only candidate in the entire set with measured commensal-spectrum data.** That is the field's largest blind spot (Round 1 Gap #8, Literature Gap #2, Safety §8.6). Being the only asset that has already answered it is worth real points.
- FDA openness to a single Phase 3 is a material cost advantage.

> **RESOLUTION: Ibezapolstat → 6.2** (down from Round 2's 6.8, up from Literature's evidence-only 5.0). The category rehabilitation is genuine; **it does not transfer to this specific asset**, because it re-specifies the failure mode as one ibezapolstat has yet to demonstrate it survives.
> **Is the conflict a feature?** One way: its commensal data is exactly the evidence every other candidate lacks, so its *evidence* profile is unusually mature even where its *strategy* is crowded.
> **Residual uncertainty:** whether initial-cure non-inferiority is achievable — answerable only in Phase 3, which is why this is an expensive candidate to be wrong about.

---

### Conflict 6 — Ebselen: fully resolved, and the durable output is not the compound

Every Phase 2 lens converged: Pathway 5.0 (single-turnover in an anaerobic colon; CPD sits downstream of the injury branch; plausible *tcdR* de-repression), Safety ORANGE→RED (115–230 mg elemental Se/day = **290–575× the UL**), SAR 4.5 (no recognition element, therefore no SAR series), Literature 4.0 (activity abolished by 5% blood; RT078 intrinsically resistant; mechanism formally contested in print; Stickland metabolism *enhanced*, not inhibited), Repurposing 4.0 (**no RLD anywhere → full 505(b)(1), 9–12 yrs, $125–225M**).

**Ebselen exhibits the purest form of Safety Finding 5:** the thiol-quenching reaction that destroys efficacy is the same reaction that liberates the selenium. **Dose escalation buys no efficacy and all of the toxicity.** Therapeutic-index reasoning is formally invalid here.

> **RESOLUTION: Ebselen → 4.0.** Target #26 valid; molecule undevelopable; not salvageable by dosing or formulation.
> **The durable output is the class rule** (Repurposing §7.2), which generalises from ebselen to auranofin (#21) and disulfiram: *any warhead whose mechanism is exchange with a cysteine thiol will be consumed by millimolar free cysteine, glutathione and bacterial H₂S at Eh ≈ −200 mV before reaching target, and will have no selectivity if it does.* This constrains the replacement programme to **reversible-covalent chemistry with fast off-rates against small thiols and slow off-rates against target**, a **non-covalent** CPD inhibitor, or a **mucosally-activated prodrug**. That is a real, reusable design constraint and it outlives the compound that generated it.

---

### Conflict 7 — UDCA absorption: Safety (~90% absorbed) vs Pathway (30–60%) vs Literature (measured)

Small but it propagates into the LSAS score. Safety §7.3 scores UDCA **A=1** on "~90% absorbed in jejunum/ileum," calling it "not a luminal drug." Pathway §2.3 estimates 30–60% absorption and derives 4–15 mM colonic. Literature reports the **measured** value: **43.5% of the fecal bile acid pool** in the antibiotic-treated state.

> **RESOLUTION: the measured value governs (Principle 1).** UDCA reaches the colon in the dysbiotic patient. Safety's LSAS **A=1 should be A=2**, raising UDCA's LSAS from 5 to 6. This does not change the ranking but it should be corrected before Phase 3 re-scores off the LSAS table. **Caveat that survives:** pool *fraction* is not free *concentration* — see Conflict 1.

---

## 3. INTEGRATED CANDIDATE RANKING (POST-DEBATE)

Weighted across evidence quality (Literature), network position and uniqueness (Pathway), safety structure (Safety), chemical tractability (SAR), developability (Repurposing), plus the resolutions in §2.

| Rank | Candidate | R2 | **Integrated** | Δ | Decisive reason for the change |
|---|---|---|---|---|---|
| — | **Fidaxomicin** *(SOC benchmark, not a fundable programme)* | 9.0 | **9.0** | — | LSAS 10/10 on all four axes independently; 3.5 axes; GREEN; the only C2 agent with no toxin-induction hazard. Unchallenged. |
| **1** | **Ribaxamase** *(in-license)* | 7.4 | **7.5** | ⬆ | Only asset with **positive human Phase 2b**. Sole occupant of #70/C7 — the only **loop-entry-preventing** axis, and one with *no* candidate in the set. Structurally escapes all three field-wide failure modes (§5). |
| **2** | **Niclosamide** | 7.0 | **6.5** | ⬇ | C4-redundancy deduction **void** (bezlotoxumab withdrawn) and the insolubility objection retired — but **uncoupling selectivity ratio unmeasured**, and uncoupling is intrinsic to the mechanism. Round 2 priced the upside and not the coupling. |
| **3** | **CamSA (U-1)** *(NCE)* | — | **6.3** | new | Mouse-validated, ~1000× CDCA potency, structurally guaranteed luminal confinement, **zero reducible groups**, one amide coupling from a commodity API. Occupies the emptiest Tier 1 axis. Heavy NCE/time penalty. **Not to be confused with U-3 urso-CamSA (6.0).** |
| **4** | **Ibezapolstat** | 6.8 | **6.2** | ⬇ | Corrected ridinilazole lesson **raises** the bar it must clear, on an axis with 8 failures. Offset by LSAS 9 and being the only candidate with commensal-spectrum data. |
| **5** | **UDCA** | 6.5 | **5.5** | ⬇ | Both the promotion and the refutation are over-claims. **Buy the option, not the programme.** Its real value is as a **non-live** agent for the population that cannot receive live biotherapeutics. |
| **5=** | **Berberine** | 6.0 | **5.5** | ⬇ | Toxin-induction fear **refuted** (+); ***spo0A* and vancomycin-biofilm** added (−); reclassification moves it into a niche where LBPs outclass it. |
| **5=** | **TUDCA** | 7.5 | **5.5** | ⬇⬇ | Mechanism **defended** against SAR's rejection — but its regulatory premise is likely void (⚠️ verify RLD). Scientific backup to UDCA, **not** a faster path, and not a co-equal in the flagship combination. |
| **8** | **U-3 urso-CamSA** *(NCE, novel)* | 8.0* | **6.0** | ⬇ | *The 8.0 was U-1's score.* The only construct **both** bile-acid theories endorse — genuinely novel and cheap to make — but entirely untested, two variables changed at once. SAR's own feasibility: 6/10. |
| **9** | **Nitazoxanide** | — | **5.0** | new | Only candidate with **existing human CDI efficacy data** and the cleanest QIDP claim — but that data is in the **replacement** configuration (0-for-3), i.e. strong evidence on the endpoint that no longer matters. |
| **10** | **Ebselen** | 5.0 | **4.0** | ⬇ | Target valid, molecule dead, not salvageable by dose or formulation. Durable output is the class rule, not the compound. |
| **10=** | **Colostrum / IgY** *(TcdB-directed)* | 6.0 | **4.0** | ⬇ | Modality validated by bezlotoxumab; evidence base does not exist (one n=38 trial terminated for sponsor bankruptcy, numerically inferior to metronidazole). Must be **re-specified as TcdB-directed** — all existing work is anti-TcdA, the failed arm. |
| **12** | **Chenodiol (CDCA)** | — | **4.5** | new | Better C1 potency than UDCA, no `bai`-guild dependence — but hepatotoxicity in a hepatically-impaired cohort. **Best used as a Stage 0 parallel arm, not a programme.** |
| **13** | **Aprepitant** | 4.5 | **3.0** | ⬇ | Entire NK1R evidence base is **TcdA**-anchored — the toxin whose targeting failed clinically. Triple CYP liability. No endpoint. |
| **14** | **Conessine** | 2.5 | **2.0** | ⬇ | Structurally falsified; RED safety dealbreaker. Closed. |
| — | **Bezlotoxumab** | WD | **WITHDRAWN** | — | Mechanism validation **retained**; its withdrawal is what converts C4 into white space and voids niclosamide's redundancy penalty. |
| — | **Vancomycin** | 6.6 | **4.5** | — | Retained as comparator only. Safety §8.6's argument that its ecological harm should be scored as **toxicity, not efficacy failure**, is correct and should be adopted: *vancomycin causes the condition it treats.* |

**Note on the shape of this table:** fidaxomicin is standard of care, not a fundable programme. **The real ranking of investable assets starts at ribaxamase**, and the gap between #1 and #2 is wider than the numbers suggest, because it is a gap in *evidence tier* (human Phase 2b vs rodent), not in score.

---

## 4. COMBINATION STRATEGY — REVISED

**The Round 2 flagship (`Fidaxomicin → UDCA/TUDCA → live biotherapeutic`) has two structural problems neither round caught:**

1. It contains **TUDCA**, which one Phase 2 agent says is mechanistically backwards (resolved in Pathway's favour in §2, but it should not be presented as consensus), and whose regulatory premise is likely void.
2. **The live-biotherapeutic arm excludes the immunocompromised** — and §4.6 unmet need **#1** is explicitly *recurrence prevention **usable in immunocompromised patients***. **The flagship combination fails the flagship unmet need.**

**Recommended replacement: two combinations for two populations.**

### Combination A — Immunocompetent (the served population)
```
 DAY 0 ────────── DAY 10 ─────────────────────────────── WEEK 12
 │◄─ FIDAXOMICIN ─►│
                   │◄──── VOWST / REBYOTA / VE303 ───────────►│   ← C7 does the work
                   │◄──── UDCA (OPTIONAL add) ───────────────►│
```
**C1 + C2 + C3 + C7(strong) + C8 = 5 axes.** The LBP is the primary agent; **UDCA is optional, not load-bearing.** This matters, because it means Combination A does not fail if Stage 0 kills UDCA.
**Key risk (Pathway):** does luminal UDCA suppress consortium engraftment? Test before adding.
**Formulation risk:** bile salts solubilise poorly-soluble lipophiles; UDCA could micellise fidaxomicin (MW 1058) and raise its absorption, cutting luminal exposure. **Sequential, never concurrent** — which the phase logic independently prefers.

### Combination B — Immunocompromised (the white space) ⭐ **the strategically important one**
```
 DAY 0 ────────── DAY 10 ─────────────────────────────── WEEK 12
 │◄─ FIDAXOMICIN ─►│
                   │◄─ UDCA / CamSA  ── OR ── oral TcdB-IgY ─►│   ← no live organisms
```
**C1 + C2 + C3 + C8 (+ C4 on the antibody arm) = 4–5 axes, with zero live-organism exposure.**

Three reasons this is the better flagship:
1. It is the **only construction that serves §4.6 unmet need #1.**
2. **Pathway's key risk for Combination A disappears here** — there is no consortium to suppress, so the UDCA-antagonism question is moot in the population where UDCA matters most.
3. It creates a **coherent development thesis for two otherwise-marginal assets** (UDCA and TcdB-directed IgY) by placing them where they have no competition rather than where they lose to incumbents.

### Combination C — Primary prevention (upstream of both)
`Ribaxamase during IV β-lactam therapy` — **prevents loop entry entirely.** Not a combination in the usual sense; it is the only intervention that operates *before* the disease. Orthogonal to A and B and compatible with both.

### Combinations to AVOID (carried forward and extended)
| Combination | Reason |
|---|---|
| **Berberine + vancomycin** | ⚑ **The specific pair with the biofilm signal** (½ MIC, p=0.02) — and it is the pair the mouse data supports. If berberine is combined at all, **pair with fidaxomicin.** |
| Ebselen + anything | Selenium; no recognition element; shared redox-fragile failure mode with niclosamide (correlated risk, the opposite of diversification). |
| Vancomycin + any C7 agent | Direct directional conflict; it sterilises the consortium it is co-dosed with. |
| Berberine in **active Phase 4** disease | Wnt/anti-proliferative risk on C6 — the axis with zero coverage, which cannot absorb a negative contributor. |
| Any **second C2 agent** on fidaxomicin | Zero added axes on the most over-served axis in the disease. |
| **UDCA + IBAT inhibitor** | ⚑ Veto: shunts **taurocholate — the germinant** — to the colon alongside the inhibitor. |

---

## 5. THE SINGLE STRONGEST DEVELOPMENT PROGRAMME

### Recommendation: **acquire and develop ribaxamase**, gated on a $150–300K diligence pass.

**Why it wins, stated as the things that kill CDI programmes and what ribaxamase does about each:**

| Field-wide failure mode | Ribaxamase's exposure |
|---|---|
| **The initial-cure non-inferiority bar** killed ridinilazole and 7 others. | **Escapes entirely.** It never competes against an 80–90%-effective generic on cure. Its endpoint is **new-onset CDI incidence** in patients on IV β-lactams. |
| **The sustained-response endpoint** is the strongest negative correlate of preclinical→clinical translation (SRC −0.20, p=1.5×10⁻⁵⁴). | **Escapes.** Its endpoint is incidence, not sustained response at day 14+. |
| **The diarrhoea-endpoint confound** afflicts every bile acid (UDCA, chenodiol, IBAT inhibitors all have diarrhoea as the dose-limiting AE, in a disease whose endpoint is diarrhoea). | **Escapes.** An orally-delivered luminal enzyme has no such axis. |
| **The 36% preclinical translation rate.** | **Largely escapes** — its evidence is already **human Phase 2b positive**, not rodent. Every other non-approved candidate's best evidence is a rodent study. |
| **Financial failure (6 of 12 programmes).** | **This is why it is available.** Its defect is correctable with capital; a pharmacodynamic defect is not. |
| **Empty axes.** | It is the **only asset touching #70/C7**, the only axis whose repair *exits* the recurrence loop rather than suppressing within it. The candidate set contains **no** primary-prevention asset at all. |

**The honest counter-case, stated in full:**

1. **It is not a repurpose — it is an acquisition** of unknown cost, and a **BLA for an enzyme biologic** with harder CMC than any small molecule here.
2. **Prevention indications need large, expensive Phase 3s** — you must enrol many at-risk patients to accrue enough CDI events. The $80–150M estimate excludes acquisition and is probably optimistic.
3. **It only prevents β-lactam-driven CDI.** Fluoroquinolone- and clindamycin-driven CDI are untouched. That is a real ceiling on the addressable population and nobody in this pipeline quantified it.
4. **Payer logic for prophylaxis is genuinely difficult** — you are asking someone to pay for an event that does not happen.
5. ⚠️ **Most important: the Phase 2b design and results have not been verified by anyone in this pipeline.** The Repurposing Strategist flagged it "⚠verify." **My top recommendation rests on an unverified claim.** That is precisely why the recommendation is *gated on diligence rather than committed to* — and why item 1 in §6 is the diligence itself, at 0.2% of programme cost.

**If diligence fails**, the fallback is **the C1 germination programme** — CamSA as the molecule, UDCA as the fast-path clinical probe, positioned for **Combination B (immunocompromised)** where there is no competing modality. That is the second-best allocation and it is a genuinely different bet, not a consolation prize.

**Not chosen, and why:**
- **Niclosamide** — best preclinical package, but the uncoupling selectivity ratio is unmeasured, uncoupling is unfixable by chemistry or formulation, RLD status is contingent, and the therapeutic index *narrows with disease severity*. Too many live unknowns to absorb the whole budget. **Best second programme, after §6 items 2 and 5.**
- **UDCA** — fastest and cheapest, but the biology is the weakest link and Stage 0 may kill it. **Buy the $1–3M option; do not buy the $45–85M programme.** That is the correct instrument for an asset with this uncertainty profile.
- **Ibezapolstat** — a seventh entrant on an eight-programme graveyard axis, facing the exact bar that killed the last one.

---

## 6. DE-RISKING EXPERIMENTS, RANKED BY INFORMATION VALUE PER DOLLAR

Ranked by *(probability the result changes a funding decision) ÷ cost*.

| # | Experiment | Cost | Time | What it decides |
|---|---|---|---|---|
| **1** | **Ribaxamase Phase 2b diligence** — full data package, endpoint definitions, acquisition cost | **$150–300K** | 3–4 mo | **Confirms or destroys the top recommendation** and could redirect the entire strategy. Highest ratio in the analysis by an order of magnitude: 0.2% of programme cost. |
| **2** | **Anaerobic fecal-slurry stability panel** — niclosamide, berberine, ebselen, CamSA, UDCA; strict anaerobiosis, Eh ≈ −200 mV, LC-MS 0–24 h | **$80–150K** | 2–3 mo | The single most-cited unresolved question in the whole pipeline — **four agents independently nominated it** (Chemist, ADMET, Literature §11, SAR §2.8) and **it has never been done for any candidate.** Multi-candidate, so cost amortises. |
| **3** | **Commensal-spectrum MIC panel** — *Lachnospiraceae*, *Ruminococcaceae*, *C. scindens/hiranonis/hylemonae*, *Bacteroides*, for every candidate | **$100–200K** | 3–4 mo | Round 1 Gap #8 + Literature Gap #2, entirely unfilled. **Safety §8.6 establishes it is the primary *toxicology* experiment for every antibacterial here, not merely an efficacy one.** Only ibezapolstat has any of this data. |
| **4** | **Bile-acid germination dose-response** — UDCA vs **TUDCA** vs CDCA vs CamSA vs urso-CamSA against taurocholate, full curves | **$50–100K** | 1–2 mo | Three questions on one plate: resolves the **Pathway-vs-SAR TUDCA conflict**; generates the **first-ever UDCA IC₅₀** (Literature Gap #4); tests the urso-CamSA rationale. **Must precede Stage 0**, which currently compares a concentration to a threshold that does not exist. |
| **5** | **Niclosamide selectivity ratio** — mitochondrial uncoupling (OCR) vs anti-TcdB protection, matched cells, plus parent/glucuronide/sulfate ratio in severe-colitis model | **$60–120K** | 2–3 mo | Safety §5.5: *"the number that determines whether the scaffold is salvageable."* **It does not exist.** Gates the #2-ranked candidate. |
| **6** | **Berberine *spo0A* in vivo** — sporulation, CFU, spore counts in the mouse recurrence model ± berberine | **$150–300K** | 4–6 mo | Literature §9 item 8: *"the highest-value disconfirming experiment for the candidate currently best supported."* Could kill berberine cheaply, or clear it decisively. |
| **7** | **HCQ TcdB entry-blockade in vitro** | **$30–60K** | 2–3 mo | Lottery ticket on the **now-empty C4 axis** with a cheap approved drug. Asymmetric payoff. |
| **8** | **Fidaxomicin–UDCA micellisation** — in vitro solubilisation/dissolution interaction | **$30–60K** | 1–2 mo | Decides concurrent vs sequential dosing in the flagship combination. Cheap and specific. |
| **9** | **Plasma PK stratified by CDI severity** for any luminal candidate, embedded in an existing trial | **$50–100K** marginal | within trial | Safety §8.4: *"the single most valuable safety measurement the whole programme could add"* — it validates or invalidates the premise **every** luminal candidate's safety case rests on. Near-zero marginal cost. |
| **10** | **Stage 0 — free UDCA in fecal water** in CDI patients, ± chenodiol and taurocholate arms | **$1–3M** | 9–12 mo | Go/no-go on the C1 clinical programme. **10× the cost of anything above — run it *after* #4, never before.** |

**Items 1–9 total ≈ $700K–1.4M and resolve essentially every live conflict in this analysis.** That is under 2% of the cheapest development programme in the report. **Item 10 should not be commissioned until #4 has produced an IC₅₀ to compare against** — otherwise you spend $1–3M measuring a concentration with no threshold.

---

## 7. WHAT REMAINS GENUINELY UNRESOLVED

Distinguished from conflicts I resolved above — these are open questions where I do not think the evidence supports a call.

1. **Can *any* anti-germinant hold against a spore reservoir?** This is a **class question**, not a UDCA question, and the disease model itself raises it (§2.3). CamSA, UDCA, chenodiol and urso-CamSA all die together if the answer is no. **Nothing in the analysis addresses it.** It is the largest single uncertainty behind the fallback programme, and it deserves a dedicated experimental design that nobody has proposed.
2. **Is C4 white space or a graveyard?** Bezlotoxumab worked mechanistically and was withdrawn **commercially**. Whether that means "the mechanism is proven and available cheaply" or "even a working anti-toxin cannot survive this market" is the difference between niclosamide being ranked #2 and being unfundable. This is a business-model question that the pipeline has been treating as a science question.
3. **Does UDCA suppress live-biotherapeutic engraftment?** Determines whether Combination A is synergistic or antagonistic. Untested, and cheap to test.
4. **Niclosamide's human colonic uptake in an aged, inflamed gut.** The mouse result is real; the mouse was young, healthy-barriered and short-gutted.
5. **The addressable fraction of CDI that is β-lactam-driven** — the ceiling on the top recommendation, unquantified by anyone.
6. **⚠️ TUDCA's listed-drug status** (§2, Conflict 2). Verify before any 505(b)(2) claim.
7. **⚠️ The UDCA human-observational denominator** — 4/12 or 4/16 (§2, Conflict 1). Verify before citing.

---

## 8. CONFIDENCE ASSESSMENT

**Overall: MODERATE.** Disaggregated, because a single number would hide the useful part:

| Claim | Confidence | Why |
|---|---|---|
| The three data-integrity corrections (A, B, C) | **HIGH** | Directly verifiable against the source files; each is a traceable propagation error. |
| Strategic diagnosis — axis mis-allocation, capital structure as the binding constraint, C4 emptied, C6 at zero | **HIGH** | Structural, derivable from evidence already in hand, and independently supported by three agents reasoning from different starting points. |
| Ebselen undevelopable; conessine dead; aprepitant not viable | **HIGH** | Five independent lenses converged with no dissent. |
| The niclosamide safety margin rests on metabolic clearance, not insolubility | **MODERATE–HIGH** | SAR's argument is sound and specific; two agents converged on the opposite error, which is itself informative. Not experimentally confirmed. |
| TUDCA mechanism resolution (Pathway over SAR) | **MODERATE–HIGH** on the 12α-OH biology; **LOW** on the regulatory status, which needs verification. |
| Berberine at 5.5 | **MODERATE** | Rests partly on two rodent studies whose group sizes Literature could not verify, in a literature with known negative-result publication bias. |
| **UDCA at 5.5** | **LOW–MODERATE** | **Genuinely unresolved.** Both the positive and the negative evidence are weak instruments. My contribution is to say so, not to have settled it. |
| **Ribaxamase as the #1 programme** | **LOW–MODERATE on the specifics; HIGH on the strategic logic.** | The strategic argument is strong and multiply-supported. **The underlying Phase 2b data was verified by nobody in this pipeline.** Hence the diligence gate — which is the honest form of this recommendation. |

**The single experiment that would most increase overall confidence: item 1, the ribaxamase diligence pass** ($150–300K, 3–4 months). It is the only experiment that can either confirm or destroy the top recommendation, and it costs 0.2% of the programme it gates.
**Runner-up: item 2, the anaerobic stability panel** — it is the only experiment that moves **five** candidates at once, and four independent agents nominated it without coordination.

---

## 9. RESPONSE FRAME FOR THE DEVIL'S ADVOCATE ⚠️ *pre-committed, report not yet available*

`agents/debate-advocate.md` did not exist at time of writing. I am pre-committing to how I will treat the likely challenges, so that my responses cannot be reverse-engineered from the Advocate's actual arguments.

| Anticipated challenge | Pre-committed response |
|---|---|
| *"You rescued UDCA from a clean negative result."* | **I did not rescue it — I downgraded it, from 6.5 to 5.5, and recommended against funding the programme.** What I rejected is the *refutation*, on the grounds that a 5/8-vs-5/8 hamster prophylaxis study is a 3.5-grade instrument by the Literature Reviewer's own schedule. **Concede immediately if the Advocate shows the study was adequately powered or that fecal-water free concentration was measured.** |
| *"Ribaxamase is outside the candidate set — you changed the question."* | **Correct, and deliberate.** The Repurposing Strategist scored it highest of anything examined, and it occupies the one axis with zero candidates. A pipeline that can only rank what it was handed cannot detect that it was handed the wrong set. **The counter I would accept: evidence that the Phase 2b endpoint does not support a Phase 3, or that the β-lactam-only ceiling makes the market non-viable.** |
| *"Niclosamide at 6.5 is still too high given an unmeasured selectivity ratio."* | **Plausibly right, and I will move it on evidence.** I ranked it on the strength of the preclinical package and the vacated C4 axis, while gating it behind two experiments. If the Advocate argues that an unmeasured, mechanism-intrinsic toxicity should floor a candidate rather than gate it, **that is a defensible position and I would move niclosamide to ~5.5.** |
| *"Your combination reframe is a strategy invention, not an integration."* | **Partly fair.** The two-population split is my construction. Its justification is that the Round 2 flagship **fails §4.6 unmet need #1** — the pipeline's own top-ranked unmet need — which is a defect in the existing recommendation, not a preference of mine. |
| *"You are trusting SAR over Literature on niclosamide and Pathway over SAR on TUDCA — that is convenient."* | **Both calls are made on the same stated principle (Principle 1, measured/mechanistic specificity beats inference), and both are falsifiable by named experiments (§6 items 4 and 5).** If the Advocate can show I applied the principle inconsistently, the ranking should change, not the principle. |

**On the Safety Pharmacologist's suggested screen** — *"for each candidate, is there a single property that sets both the efficacy ceiling and the safety floor?"* — I applied it and it is the most productive filter in the analysis. Results: **Ebselen — yes, chemical** (thiol quenching destroys efficacy *and* liberates selenium) → **fatal, unfixable.** **Niclosamide — yes, chemical** (the protonophore that deacidifies endosomes uncouples mitochondria) → **serious, unfixable by des-nitro or formulation; NOT the physical dissolution coupling that Literature and Safety both assumed.** **Berberine — no** (the DDI is independent of the anti-inflammatory effect). **UDCA — no.** **CamSA — no, and notably the reverse:** the sulfonate that drives its potency is the same group that guarantees non-absorption, so its efficacy and safety levers are the same atom pointing the *same* way. **That inversion is the strongest single argument for CamSA in this analysis**, and it is why I ranked an unadvanced NCE at #3.

---

## 10. RECOMMENDED PROPAGATIONS BEFORE PHASE 3

1. **round2-synthesis.md** — remove "berberine sub-MIC toxin induction at 6–12 h" from Unresolved Conflicts; replace with ***spo0A* upregulation** and **vancomycin-specific biofilm enhancement**. Record that ADMET's proposed hard stop was tested and **did not trigger**.
2. **round2-synthesis.md** — reattribute TUDCA: **Pathway recommends, SAR rejects (U-6)**. Not a consensus candidate.
3. **round2-synthesis.md** — split "U-1 Urso-CamSA (8.0)" into **U-1 CamSA (8/10)** and **U-3 urso-CamSA (6/10)**.
4. **round2-synthesis.md** — replace the flagship combination with the **two-population construction** (§4), on the grounds that the current one fails §4.6 unmet need #1.
5. **p2-safety.md §7.3** — correct UDCA LSAS **A=1 → A=2** (measured fecal delivery), total 5 → 6.
6. **disease-model.md** — adopt Literature §13's eight edits, **plus**: mark **C4 as vacated** following bezlotoxumab's withdrawal (this voids niclosamide's redundancy penalty), and add the **soft-electrophile class rule** (Repurposing §7.2) as a screening filter.
7. **Phase 3 agents** — carry **Principle 2** forward explicitly: *the preclinical discount schedule applies symmetrically to negative results.* This is the methodological error most likely to recur.
8. **Verify before external use:** TUDCA listed-drug status; the UDCA observational denominator (4/12 vs 4/16); the ribaxamase Phase 2b data package.

---

*Integration Specialist — Debate Round. Prepared without the Devil's Advocate report; §9 is a pre-committed response frame and this analysis should be re-run against the Advocate's actual challenge. Research analysis only — not clinical or investment advice. All ⚠️-flagged items require independent verification before external use.*
