"""
CDI Candidate Ranker - Phase 3 final scoring.
Aggregation: LEXICOGRAPHIC-WITH-BOUNDED-MODIFIERS (not a weighted sum).

  Composite = EfficacyAnchor + clamp(sum(modifiers), -1.5, +1.5)

EfficacyAnchor = evidence-tier ceiling (Literature Reviewer p2-literature.md L415-424,
extended upward for human tiers) MINUS named, itemised efficacy deductions.
Modifiers = axis position, compartment/chemistry, safety, regulatory/capital,
traditional use. Bounded so no modifier set can outvote a refutation.
"""
MOD_CAP = 1.5

TIER = {
    "human_ph2b_hard_endpoint": 8.0,
    "human_ph2_small_endpoint_untested": 6.5,
    "mouse_recurrence_replicated": 7.0,
    "mouse_recurrence_single_lab": 6.5,
    "mouse_prophylactic_lab_strain": 4.0,
    "hamster_survival_only": 3.5,
    "purified_toxin_instillation": 2.5,
    "in_vitro_only": 2.0,
}

# Flat, mechanism-independent penalties (debate-advocate.md L112): these survive
# base-rate conditioning and apply to EVERY preclinical-only candidate.
ENDPOINT_PEN = -0.50   # sustained-response endpoint; SRC -0.20, p=1.5e-54
YOUNG_ANIMAL_PEN = -0.25

C = []
def cand(name, tier, deds, mods, gate, coupled, note):
    anchor = TIER[tier] + sum(d[1] for d in deds)
    raw = sum(m[1] for m in mods)
    applied = max(-MOD_CAP, min(MOD_CAP, raw))
    C.append(dict(name=name, ceiling=TIER[tier], deds=deds, anchor=round(anchor,2),
                  mods=mods, raw=round(raw,2), applied=round(applied,2),
                  comp=round(anchor+applied,2), gate=gate, coupled=coupled, note=note))

cand("Ribaxamase", "human_ph2b_hard_endpoint",
 [("Phase 2b package unverified by any agent in this pipeline", -1.00),
  ("Addressable-population ceiling: beta-lactam-driven CDI only; FQ/clindamycin untouched, unquantified", -0.50)],
 [("Axis #70/C7 sole occupant; ONLY loop-ENTRY-preventing asset; zero competition", +1.00),
  ("Compartment K1 luminal; target IS luminal beta-lactam - exact match; no redox-fragile pharmacophore", +0.30),
  ("Zero systemic exposure -> near-zero DDI in polypharmacy population", +0.50),
  ("BLA/enzyme CMC; no RLD; large prevention Ph3; prophylaxis payer logic", -0.60)],
 "PASS", "NO", "Only asset in the set with positive HUMAN data on a hard clinical endpoint.")

cand("Ibezapolstat", "human_ph2_small_endpoint_untested",
 [("Initial-cure non-inferiority vs 85-92% comparator UNDEMONSTRATED; axis base rate 0-for-8", -1.50),
  ("Recurrence claim rests on the untested sustained-response endpoint", -0.25)],
 [("C2 saturation, adds no axis -0.4; under-credited C7 bile-acid/microbiome touch +0.5", +0.10),
  ("LSAS 9/10; purpose-designed K1 luminal delivery; redox-clean", +0.80),
  ("ONLY candidate in the entire set with measured commensal-spectrum data", +0.40),
  ("FDA open to a single Phase 3; QIDP/GAIN eligible", +0.40)],
 "PASS", "NO", "#2 on evidence maturity, NOT on strategic differentiation.")

cand("Niclosamide", "mouse_recurrence_single_lab",
 [("Sustained-response endpoint penalty (flat, mechanism-independent)", ENDPOINT_PEN),
  ("Young-animal penalty (flat, mechanism-independent)", YOUNG_ANIMAL_PEN)],
 [("C4 white space (bezlotoxumab withdrawn Jan-2025); strain-agnostic, covers CDT; but downstream of the receptor-binding branch (misses NOX1 arm)", +0.70),
  ("Compartment K2 coherent - metabolic-clearance spec; 'insolubility paradox' retired", +0.20),
  ("REDOX GATE CONDITIONAL: nitro reducible at Eh -200mV, never measured; only in vivo counter-evidence", -0.30),
  ("COUPLED FILTER TRIGGERED: protonophore = intrinsic uncoupler; unfixable by des-nitro or formulation; TI narrows as the patient worsens", -1.00),
  ("Contingent RLD; full CMC; 7-10 yrs; $75-140M", -0.40),
  ("Nitroso/hydroxylamine genotoxicity alert at 10-14x anthelmintic cumulative dose; 15-25% of CDI pts on DNA-damaging chemo", -0.20)],
 "CONDITIONAL", "YES (serious, structural)", "Best preclinical package in the set; structurally defective mechanism.")

cand("CamSA", "mouse_prophylactic_lab_strain",
 [("Sustained-response endpoint penalty (flat)", ENDPOINT_PEN),
  ("Young-animal penalty (flat)", YOUNG_ANIMAL_PEN),
  ("Anti-germinant CLASS validity unresolved: can any anti-germinant hold vs a replenished reservoir?", -0.25)],
 [("Axis C1 Tier-1, near-empty; serves unmet need #2 (spore reservoir) and #1 (non-live)", +1.00),
  ("REDOX GATE PASS: zero reducible groups; sulfonate guarantees non-absorption", +0.50),
  ("COUPLED FILTER INVERTED: the sulfonate sets potency AND non-absorption - same atom, same direction", +0.50),
  ("No systemic exposure; no DDI; cholic-acid derivative", +0.30),
  ("NCE, zero human exposure, full 505(b)(1), 9-12 yrs; partly offset by one amide coupling from a commodity API", -0.60)],
 "PASS", "NO (inverted - favourable)", "Best-designed molecule; thinnest efficacy evidence. Largest sensitivity in the ranking.")

cand("Berberine", "mouse_recurrence_replicated",
 [("Group sizes unverified, abstracts only; natural-product publication bias", -0.75),
  ("spo0A upregulation at sub-MIC contradicts the very endpoint it is proposed for", -0.50),
  ("Sustained-response endpoint penalty (flat)", ENDPOINT_PEN),
  ("Young-animal penalty (flat)", YOUNG_ANIMAL_PEN)],
 [("Exits C2 graveyard into C5+C7+#72 cross-feed +0.5; DIRECTIONAL CONFLICT on C6 (Wnt/anti-proliferative), the zero-coverage axis -0.4", +0.10),
  ("K1 luminal confinement real (A=4, equals fidaxomicin); redox CONDITIONAL (reduction to absorbable dihydroberberine); cationic fecal binding largely moot under host/microbiota reclassification", -0.45),
  ("LSAS 6: real human DDI (cyclosporine +35% AUC) excludes CNI-transplant, digoxin, P-gp DOACs - over-represented in this cohort", -0.50),
  ("No drug RLD; zero human CDI data; comparator is now approved LBPs with FMT-class efficacy", -0.40),
  ("Traditional use genuinely ON-indication (Ayurvedic/TCM infectious diarrhoea, dysentery)", +0.40)],
 "CONDITIONAL", "NO", "Best-replicated preclinical package; worst comparator set after reclassification.")

cand("UDCA", "in_vitro_only",
 [("Measured colonic delivery in the DISEASE-RELEVANT state (43.5% of fecal BA pool under antibiotics)", +0.50)],
 [("Axis C1 sole clinical-stage occupant; unmet need #1 (non-live, immunocompromised) and #2", +1.00),
  ("Redox-clean; delivery measured; but 43.5% of the POOL is not free monomer - fecal-water conc never measured", +0.20),
  ("COUPLED FILTER: NO - efficacy and safety levers cleanly separated", +0.20),
  ("Approved generic, RLD exists, fastest/cheapest 505(b)(2) in the set +0.6; negative-NPV for a commercial sponsor -0.3", +0.30),
  ("Well tolerated at PBC dose; ORANGE at 28-30 mg/kg (PSC trial harm)", +0.20)],
 "PASS", "NO", "Low anchor + capped-out modifiers = an OPTION, not a programme.")

cand("TUDCA", "in_vitro_only",
 [("Anti-germination potency NEVER measured against UDCA", -0.50)],
 [("Axis C1, but shared with UDCA - a formulation contingency, not a separate asset", +0.60),
  ("TGR5 (#62) agonism adds C5/C6 tone UDCA lacks - on the zero-coverage axis", +0.40),
  ("Better colonic-delivery physics (TPSA 123.9 vs 77.8); BSH depletion keeps it conjugated; redox-clean", +0.40),
  ("Regulatory premise likely VOID: FDC withdrawn 2024, no marketed US RLD; the supplement form is not an RLD", -0.60)],
 "PASS", "NO", "Mechanism defended over SAR; regulatory advantage inverted.")

cand("Aprepitant", "purified_toxin_instillation",
 [("All efficacy evidence anchored on TcdA - the clinically DISPROVEN toxin", -1.00)],
 [("Unique C5/NK1R arm; only candidate touching fulminant CDI (unmet need #6)", +0.40),
  ("Triple CYP liability, LSAS 3 - 'aprepitant IS the DDI' in a polypharmacy cohort", -0.80),
  ("K3 systemic compartment; viable only in the ICU/fulminant niche", -0.10)],
 "PASS", "NO", "Right axis, wrong evidence anchor.")

cand("Ebselen", "mouse_prophylactic_lab_strain",
 [("Activity ABOLISHED by 5% blood; RT078 intrinsically resistant; Stickland ENHANCED not inhibited; mechanism contested in print", -1.50),
  ("Sustained-response endpoint penalty (flat)", ENDPOINT_PEN),
  ("Young-animal penalty (flat)", YOUNG_ANIMAL_PEN)],
 [("Target #26 valid, Tier 1", +0.50),
  ("REDOX GATE FAIL - soft electrophile consumed by mM thiols at Eh -200mV; abolition by 5% blood is the confirming measurement", -1.00),
  ("COUPLED FILTER FATAL: thiol quenching destroys efficacy AND liberates Se (290-575x UL)", -1.00),
  ("No RLD anywhere -> full 505(b)(1), 9-12 yrs, $125-225M", -0.50)],
 "FAIL", "YES (fatal)", "DISQUALIFIED on the redox gate. Target survives; molecule does not.")

cand("Conessine", "in_vitro_only",
 [("CspC pharmacophore hypothesis structurally FALSIFIED (0/3 elements)", -1.00)],
 [("No coherent network position", -0.30),
  ("RED safety dealbreaker: H3/CNS-active + hERG/QT in a torsades-primed cohort + antimotility (megacolon) + absorbed cationic", -1.50)],
 "n/a", "n/a", "DISQUALIFIED on safety. Efficacy hypothesis independently falsified.")

C.sort(key=lambda x: -x["comp"])
w = max(len(c["name"]) for c in C)
print(f"{'CANDIDATE':<{w}} | CEIL | ANCHOR | MOD raw | MOD appl | COMPOSITE | REDOX GATE  | COUPLED FILTER")
print("-"*118)
for c in C:
    print(f"{c['name']:<{w}} | {c['ceiling']:>4.1f} | {c['anchor']:>6.2f} | {c['raw']:>7.2f} | "
          f"{c['applied']:>8.2f} | {c['comp']:>9.2f} | {c['gate']:<11} | {c['coupled']}")
print()
print("Modifier cap BINDING for:", ", ".join(c["name"] for c in C if abs(c["raw"]) > MOD_CAP+1e-9) or "none")
