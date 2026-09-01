# Molecular Target Analyst — Phase 1 Assessment
## *Clostridioides difficile* Infection (CDI)

**Agent:** Molecular Target Analyst (target-profiler)
**Date:** 2026-08-17
**Question addressed:** How druggable and validated are the targets these candidates hit, in the context of CDI?
**Reference disease model:** `data/reports/disease-explorer/clostridioides-difficile/2026-08-17/disease-model.md` §5 (72-target master list), §5.5 (prioritization tiers), §2.3 (germination), §2.6 (toxin biology), §4.5 (failed approaches), §4.6 (unmet needs), Appendix A.2

---

## 0. DATA AVAILABILITY STATEMENT — read this before weighting any claim below

I ran the assigned discovery commands plus supplementary coverage checks. The result materially constrains what can be called data-backed.

### 0.1 What the project data actually contains

| File | Rows | Verdict for CDI |
|---|---|---|
| `chembl_drug_targets.csv` | **44** | **Test-mode stub.** Contains adrenergic receptors, DNA gyrase, acetylcholinesterase. Organism breakdown: 11× *Rattus norvegicus*, 3× *E. coli*, 1× *Homo sapiens*, plus Gram-negative enterics. **Zero *C. difficile* entries.** All three assigned target greps (`RNA polymerase`, `peptidoglycan`, `cysteine protease`, `bile acid`, `NK1R`, `TACR1`) returned **no hits.** |
| `chembl_drug_mechanisms.csv` | **11** | **Test-mode stub.** Contains only nicotine, four fluoroquinolones, indomethacin, amphetamine. The assigned mechanism grep (`vancomycin\|fidaxomicin\|metronidazole\|ebselen\|niclosamide\|aprepitant`) returned **no hits.** |
| `chembl_drug_indications.csv` | 80 | Stub — no candidate rows |
| `chembl_bioactivities.csv` | 24 | Stub |
| `chembl_toxicity.csv` | 2 | Stub (header + 1 row) |
| `drugbank_drug_targets.csv` | 19 | Chlorhexidine-centric; not CDI-relevant |
| `ttd_drug_target_genes.csv` | 4 | Oral Mucositis only (palifermin/FGFR2) |
| `chembl_approved_drugs.csv` | **3,277** | **Substantive.** Contains 7 of 10 candidates with physchem/approval metadata |
| `pubchem_phytochem_target_interactions.csv` | **60,522** | **Substantive but host-only.** 312 unique phytochemicals × 15,762 unique human genes, CTD/TTD-derived. `grep -ic "difficile\|clostrid"` → **0 rows.** No bacterial or toxin targets whatsoever. |

### 0.2 Consequence for this analysis

- **All bacterial-target (#1–#25) and toxin-target (#26–#34) assessments are knowledge-based, not data-backed.** The knowledge graph has no pathogen-target layer. This is not a gap I can close with better queries — the data does not exist in this repository.
- **Host targets (#35–#63) are partially data-backed** via the PubChem/CTD phytochemical file, but *for compound classes, not for the specific candidates*. Coverage counts I pulled:

| CDI host target | Gene | Interaction rows | CDI direction (§5.3) |
|---|---|---|---|
| NF-κB p65 | `RELA` | **326** | INHIBIT |
| IL-1β | `IL1B` | **425** | INHIBIT (#45) |
| PPARγ | `PPARG` | **196** | AGONIZE (#53) |
| AhR | `AHR` | **105** | AGONIZE (#52) |
| HIF-1α | `HIF1A` | **85** | STABILIZE (#55) |
| NF-κB1 | `NFKB1` | 85 | INHIBIT |
| EGFR | `EGFR` | 68 | AGONIZE (#58) |
| β-catenin | `CTNNB1` | 55 | RESTORE (#59) |
| Caspase-1 | `CASP1` | **45** | INHIBIT (#44) |
| FXR | `NR1H4` | 37 | MODULATE — direction UNCERTAIN (#61) |
| ZO-1 | `TJP1` | 36 | STABILIZE (#56) |
| NLRP3 | `NLRP3` | **33** | INHIBIT (#44) |
| Occludin | `OCLN` | 27 | STABILIZE (#56) |
| Hsp90 | `HSP90AA1` | 24 | INHIBIT (#40) |
| VDR | `VDR` | 20 | AGONIZE (#54) |
| NOX1 | `NOX1` | 13 | INHIBIT (#43) |
| Claudin-1 | `CLDN1` | 13 | STABILIZE (#56) |
| TGR5 | `GPBAR1` | 6 | AGONIZE (#62) |
| IL-23 | `IL23A` | 6 | INHIBIT (#46) |
| CSPG4 | `CSPG4` | **5** | BLOCK (#35) |
| NK1R | `TACR1` | **5** | ANTAGONIZE (#51) |
| CXCR2 | `CXCR2` | 5 | MODULATE (#48) |
| IL-22 | `IL22` | **3** | **AGONIZE** (#47) |
| FZD1 | `FZD1` | 2 | BLOCK carefully (#36) |
| TLR5 | `TLR5` | **1** | **AGONIZE** (#50) |
| MLCK | — | **0** | INHIBIT (#57) |

- **Candidate-specific coverage in the phytochemical file is near-zero.** `berberine` appears in 20 rows but **never as the primary compound** — only as a named co-treatment inside CTD evidence strings for fructose/rutin experiments. `conessine`: **0 rows.** The compounds that dominate the NLRP3/inflammasome rows are quercetin (7), palmitic acid (5), cholesterol (5), melatonin (2), luteolin, galangin, emodin, celastrol, rhein. TACR1 rows are genistein, β-amyrin, α-amyrin — not aprepitant.
- **Physchem/approval status for 7 of 10 candidates IS data-backed** (see §3.1 below).

**Net:** this assessment is ~85% knowledge-based, ~15% mixed. I mark each candidate explicitly.

---

## 1. TARGET PROFILES — the targets these candidates hit

Profiles follow the skill's format, adapted to CDI. Validation levels use the disease model's own scale (Clinical / Genetic / Preclinical / Computational) rather than the OM-specific 1–6 hierarchy, since the OM scale's "Level 1 = approved for OM" anchor does not transfer.

### TARGET #1 — RNA polymerase switch region (*C. difficile* RpoB/RpoC)

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #1 — Bacterial RNA polymerase, switch region
═══════════════════════════════════════════════════════════
CLASS:            BACT (bacterial)   |  Phase/Module: 2 (vegetative outgrowth)
PROTEIN CLASS:    Multi-subunit nucleotidyltransferase — enzyme
DIRECTION:        INHIBIT ✓
VALIDATION:       CLINICAL (highest available) — fidaxomicin approved 2011
DRUGGABILITY:     KNOWN DRUGGABLE — High

STRUCTURAL NOTES:
  The switch region is a hinge controlling clamp opening for DNA loading.
  It is an ALLOSTERIC pocket distinct from the rifamycin site — which is why
  fidaxomicin retains activity against rifampicin-resistant strains. Deep,
  well-defined, and has no human ortholog: the selectivity ceiling is high.

CDI RELEVANCE:
  Blocks transcription initiation → bactericidal against vegetative cells.
  SECONDARY EFFECTS THAT MATTER MORE THAN THE PRIMARY ONE (§2.3, §2.5):
    • Suppresses sporulation at sub-MIC — partially addresses Phase 1 /
      the spore reservoir, which no approved agent otherwise touches
    • Suppresses toxin production (Phase 3)
    • Narrow spectrum → spares Bacteroidetes/Firmicutes, preserving #64–#67

COMPETITIVE LANDSCAPE:
  Fully occupied. Fidaxomicin is the guideline-preferred first-line agent.
  Target-level novelty is zero.

RESISTANCE:  rpoB/rpoC switch-region substitutions reported; MIC creep
             documented in ribotype 027 isolates.

ASSESSMENT:  The best-validated target on the list — and the least available.
CONFIDENCE:  High (knowledge-based)
═══════════════════════════════════════════════════════════
```

### TARGET #2 — Peptidoglycan D-Ala-D-Ala terminus

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #2 — Peptidoglycan D-Ala-D-Ala
═══════════════════════════════════════════════════════════
CLASS:            BACT   |  Phase/Module: 2
TARGET TYPE:      NOT A PROTEIN — a cell-wall precursor SUBSTRATE.
                  Vancomycin binds the ligand, not an enzyme. This inverts
                  the usual druggability logic: no active site to mutate,
                  which is why glycopeptide resistance in C. difficile
                  requires wholesale vanG-type pathway acquisition and
                  remains rare.
DIRECTION:        INHIBIT ✓
VALIDATION:       CLINICAL (highest) — standard of care since the 1970s
DRUGGABILITY:     KNOWN DRUGGABLE — but only by large glycopeptides/
                  lipoglycopeptides. The chemical space is narrow and mature.

⚠ SYSTEM-LEVEL DIRECTION CONFLICT — the key finding of this profile:
  Target #2 is conserved across ALL Gram-positive organisms, including the
  7α-dehydroxylating Clostridia (C. scindens and relatives) that constitute
  target #64 — a RESTORE/AUGMENT target. Engaging #2 therefore
  simultaneously DEPLETES #64, #65 (BSH), #66 (secondary bile acids), and
  #67 (butyrate/SCFA producers).

  Vancomycin does not violate the Direction column at the level of its own
  target. It violates it at the level of the SYSTEM. This is the
  mechanistic explanation for the ~25% recurrence rate: the drug that
  clears the infection is also the drug that maintains the dysbiotic state
  permitting germination (§2.2, §2.8).

ASSESSMENT:  Maximal validation, minimal headroom, and an intrinsic
             pro-recurrence liability that is a property of the target
             itself, not of the molecule.
CONFIDENCE:  High (knowledge-based)
═══════════════════════════════════════════════════════════
```

### TARGET #26 — TcdB cysteine protease domain (CPD) · TARGET #21 — Proline reductase PrdB

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #26 — TcdB CPD  (Tier 1 per §5.5)
═══════════════════════════════════════════════════════════
CLASS:            TOXIN  |  Module A  |  TcdB residues ~544–767
PROTEIN CLASS:    Cysteine protease (papain-like fold) — catalytic Cys698
DIRECTION:        INHIBIT ✓
VALIDATION:       PRECLINICAL (STRONG) — ebselen shows in vivo murine efficacy
DRUGGABILITY:     KNOWN DRUGGABLE — HIGH. A catalytic cysteine in a defined
                  pocket is among the most tractable chemotypes available;
                  covalent warhead design is a mature discipline.

MECHANISM CONTEXT (§2.6):
  Cytosolic InsP6 binds the allosteric site (#29) → activates CPD →
  autoproteolysis releases the GTD into the cytosol → Rho glucosylation.
  Blocking CPD leaves the GTD tethered to the delivery domain, non-catalytic
  against Rho.

WHY THIS TARGET IS TIER 1:
  • Downstream of receptor binding → strain/receptor-variant agnostic, which
    matters given the TcdB subtype diversity flagged in §A.3
  • TcdB-specific — sidesteps the actoxumab/TcdA failure (#31)
  • Small molecule → oral, unlike bezlotoxumab (unmet need #4, §4.6)
  • Anti-virulence, not antibacterial → does not deplete #64–#67

⚠ RISKS:
  • CPD-INDEPENDENT TOXICITY. Autoprocessing-deficient TcdB retains partial
    cytotoxicity in some systems; and #43 (NOX1-mediated, GTD-independent
    necrosis) is a documented escape route at high toxin concentration.
    CPD blockade may therefore be partial rather than complete protection.
  • Human cysteine-protease off-targets (cathepsins, caspases) — selectivity
    must be demonstrated, not assumed.

───────────────────────────────────────────────────────────
TARGET PROFILE: #21 — Proline reductase PrdB (selenoprotein)
───────────────────────────────────────────────────────────
CLASS:            BACT  |  Phase 2  |  Stickland fermentation
DIRECTION:        INHIBIT ✓
VALIDATION:       GENETIC + PRECLINICAL
DRUGGABILITY:     THEORETICALLY DRUGGABLE — the selenocysteine residue is
                  markedly more nucleophilic than cysteine, giving a genuine
                  covalent-selectivity handle over host cysteine enzymes.

RELEVANCE: Stickland proline reduction is C. difficile's principal energy
           route and a validated fitness factor. Human selenoproteome
           (TrxR, GPx) is the obvious off-target liability.

⚠ NOTE: proline reductase activity intersects Stickland donor availability,
  which is itself modulated by Enterococcus cross-feeding (#72). Inhibiting
  #21 and suppressing #72 are mechanistically convergent.
═══════════════════════════════════════════════════════════
```

### TARGET #11 — Taurocholate-competitive germination block · TARGET #66 — Secondary bile acid supply/mimicry

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #11 + #66 — Bile acid axis  (both Tier 1 per §5.5)
═══════════════════════════════════════════════════════════
#11 CLASS:  BACT  | Phase 1 | DIRECTION: COMPETITIVELY BLOCK ✓
#66 CLASS:  MICROBIOME | Phase 0/1/C | DIRECTION: SUPPLY / MIMIC ✓
VALIDATION: PRECLINICAL (STRONG) for both
DRUGGABILITY: KNOWN DRUGGABLE — bile acid chemistry is mature; the
              steroid nucleus is synthetically accessible and semi-synthetic
              analogs are routine.

⚠⚠ DIRECTION AUDIT — THE TRAP THE TEAM LEAD FLAGGED:
  #66 is SUPPLY/MIMIC and #64 (baiCD/baiE/baiA2/baiH) is RESTORE/AUGMENT.
  A candidate that INHIBITED 7α-dehydroxylation would remove the source of
  DCA/LCA and WORSEN disease.
  UDCA does NOT do this. UDCA is a bile acid that is SUPPLIED, engaging #66
  in the correct direction and competing at #11 in the correct direction.
  ✓ NO DIRECTION VIOLATION. This is the correct read.

MECHANISTIC LOGIC (§2.3, §2.8):
  Taurocholate + glycine → CspC (#7) → CspB → SleC → germination.
  CDCA is an ESTABLISHED competitive inhibitor of TA-mediated germination.
  DCA/LCA additionally inhibit vegetative growth. Restoring the secondary
  bile acid pool therefore hits germination AND outgrowth.

⚠ RISKS SPECIFIC TO UDCA AS THE #66 AGENT:
  • UDCA is a 7β-epimer of CDCA — it is NOT DCA or LCA. Whether it
    reproduces the growth-inhibitory activity of true secondary bile acids
    at colonically achievable concentrations is genuinely unresolved.
  • UDCA is efficiently absorbed in the ileum and enterohepatically
    recycled. Colonic delivery of the parent compound is the weak link —
    the opposite of berberine's situation.
  • Conjugation: host and microbial conjugation of UDCA yields TUDCA/GUDCA.
    Whether any conjugate can act as a germinant rather than an antagonist
    at CspC is not established and should be treated as an open risk.
  • FXR (#61) direction is marked UNCERTAIN in the model. UDCA is a weak
    FXR modulator; the net effect on the endogenous bile acid pool could
    theoretically run either way.
═══════════════════════════════════════════════════════════
```

### TARGET #7 — CspC bile acid germinant receptor

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #7 — CspC  (Tier 1 per §5.5, highest-value open target)
═══════════════════════════════════════════════════════════
CLASS:            BACT  |  Phase 1  |  DIRECTION: INHIBIT / ANTAGONIZE ✓
PROTEIN CLASS:    Subtilisin-like PSEUDOprotease — catalytically dead,
                  functions purely as a steroid ligand sensor
VALIDATION:       GENETIC + PRECLINICAL. cspC mutants are germination-
                  deficient; CamSA protects in a mouse model.
DRUGGABILITY:     THEORETICALLY DRUGGABLE — a defined small-molecule ligand
                  site with a known natural ligand (taurocholate) and a known
                  competitive antagonist chemotype (CDCA). Those two facts
                  alone put it well above most "theoretical" targets.

WHY THIS IS THE HIGHEST-VALUE OPEN TARGET IN CDI (§2.3):
  1. Germination is OBLIGATORY and IRREVERSIBLE — a true committed step
  2. It is CHEMICALLY triggered by a defined ligand-receptor interaction
  3. It targets the SPORE RESERVOIR — the actual driver of recurrence,
     and unmet need #2 in §4.6
  4. NO clinical competition whatsoever

⚠ THE DRUGGABILITY CAVEAT THAT MATTERS:
  §2.3 states the CspC ligand-binding structural details "remain
  incompletely resolved." Without a liganded structure there is no
  structure-based design handle — a campaign here is a phenotypic
  germination-assay screen, not rational design. That is slower and
  higher-variance, and it is the reason this target has stayed open.

⚠ OPEN BIOLOGICAL QUESTION (§2.3, flagged UNCERTAIN):
  Blocking germination does not KILL the spore. Whether an anti-germinant
  prevents disease or merely defers it against a continuously replenished
  spore load is unanswered — this is an existential question for the whole
  target class, not a candidate-specific one.
═══════════════════════════════════════════════════════════
```

### TARGET #27 — TcdB CROPS domain · TARGET #30 — TcdB delivery/pore domain

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: #27 — TcdB CROPS  (residues ~1833–2366)
═══════════════════════════════════════════════════════════
DIRECTION:        NEUTRALIZE ✓   |  VALIDATION: CLINICAL (bezlotoxumab)
DRUGGABILITY:     KNOWN DRUGGABLE (BIOLOGIC ONLY). CROPS is a repetitive
                  β-solenoid carbohydrate-binding array — a large, flat,
                  extended surface. This is a textbook small-molecule-
                  hostile PPI epitope. Antibodies and VHH multimers work
                  here; small molecules essentially cannot.
                  ⚠ Druggability is therefore HIGH-but-modality-locked, and
                    the locked modality is IV — which conflicts directly
                    with unmet need #4 ("an ORAL small-molecule toxin
                    inhibitor").

⚠ TARGET-BIOLOGY RISK (§2.6):
  CSPG4 — the high-affinity TcdB receptor — binds a region within the
  DELIVERY domain (~res 1500–1800), NOT CROPS. CROPS-truncated TcdB retains
  substantial cytotoxicity. So #27 is a strong ANTIBODY EPITOPE but is
  arguably NOT the functionally critical receptor-binding determinant.
  Bezlotoxumab's ~10-point absolute recurrence reduction — real but partial
  — is consistent with neutralizing a non-essential domain.
  Strain-level TcdB subtype variation (§A.3) compounds this.

───────────────────────────────────────────────────────────
TARGET PROFILE: #30 — TcdB delivery / pore-forming domain
───────────────────────────────────────────────────────────
DIRECTION:        INHIBIT ✓   |  VALIDATION: PRECLINICAL [EMERGING]
DRUGGABILITY:     THEORETICALLY DRUGGABLE. pH-dependent membrane insertion
                  is a conformational transition, not a binding pocket.
                  Amantadine-class precedent exists for viral pore blockade,
                  but this class has a poor record of yielding selective,
                  potent, non-membrane-disruptive leads.

⚠ MECHANISM-ATTRIBUTION PROBLEM — important for the niclosamide read:
  Niclosamide is a protonophore/mitochondrial uncoupler. Its documented
  ability to block TcdB entry is at least as consistent with COLLAPSE OF
  THE ENDOSOMAL pH GRADIENT — i.e. functionally target #41 (v-ATPase /
  endosomal acidification) — as with a specific interaction with the TcdB
  delivery domain. The model assigns niclosamide to #30; I flag that the
  assignment may be an epiphenomenon of a general protonophore effect.
  This is testable: a specific #30 binder should be inactive against
  unrelated pH-dependent toxins (diphtheria, anthrax LF); a protonophore
  will block all of them.
═══════════════════════════════════════════════════════════
```

### TARGET #3 — DNA polymerase IIIC · TARGET #51 — NK1R · TARGET #44/#56 — host inflammatory & barrier

```
═══════════════════════════════════════════════════════════
#3  DNA POLYMERASE IIIC (PolC)
    DIRECTION: INHIBIT ✓  |  VALIDATION: CLINICAL (early, Phase 2)
    DRUGGABILITY: KNOWN DRUGGABLE — HIGH. PolC is the Gram-positive-
    specific replicative polymerase with NO human ortholog and no
    Gram-negative counterpart. The dGTP-competitive site is well
    characterized. On pure target-quality metrics this is arguably the
    cleanest bacterial target on the list after #1.
    ⚠ STRATEGIC PROBLEM, NOT A TARGET PROBLEM: this is another
      narrow-spectrum antibacterial. §4.5 names ridinilazole "the single
      most important cautionary tale" — narrow-spectrum microbiome-sparing
      activity met non-inferiority but FAILED SUPERIORITY on sustained
      response. Target excellence does not rescue a disproven strategy.

───────────────────────────────────────────────────────────
#51 NK1R (TACR1) / substance P
    DIRECTION: ANTAGONIZE ✓  |  VALIDATION: PRECLINICAL only
    DRUGGABILITY: KNOWN DRUGGABLE — HIGH. Class A GPCR, ~34% of approved
    drugs are GPCR-directed; aprepitant/fosaprepitant approved elsewhere.
    Target-class druggability is the highest of any target in this set.
    ⚠ THREE STRUCTURAL PROBLEMS FOR CDI:
      1. It is a HOST SYMPTOM/INFLAMMATION target. §4.6 ranks host-directed
         anti-inflammatory therapy DEAD LAST (#8 of 8 unmet needs). It
         touches neither the bacterium, the toxin, nor the microbiome —
         so it cannot address recurrence, the actual bottleneck.
      2. ROUTE INVERSION: NK1R sits on enteric neurons, lamina propria
         immune cells and colonocytes — SUBEPITHELIAL. Engagement requires
         systemic absorption, forfeiting the luminal-confinement advantage
         that §6.2 says should be the scoring asset in this disease.
      3. Anti-secretory/antimotility pharmacology in a disease where §3.3
         and §7.2 both flag antimotility → TOXIC MEGACOLON risk.
    ⚠ DATA NOTE: TACR1 has only 5 rows in the phytochemical file
      (genistein ×2, β-amyrin, α-amyrin, sucrose) — no aprepitant, and
      no CDI context anywhere.

───────────────────────────────────────────────────────────
#44 NLRP3 INFLAMMASOME / CASPASE-1   — INHIBIT ✓ | Preclinical
    DRUGGABILITY: KNOWN DRUGGABLE. MCC950, VX-765, dapansutrile are all
    clinical-stage elsewhere. NACHT-domain ATPase pocket is tractable.
    Data-backed at the CLASS level: 33 NLRP3 + 45 CASP1 + 425 IL1B rows,
    dominated by quercetin, luteolin, galangin, emodin, celastrol, rhein.
    ⚠ BIDIRECTIONAL RISK: IL-1β/neutrophil recruitment is partly
      PROTECTIVE in CDI. This is the same bidirectional trap the model
      flags explicitly for #48 (CXCR2) and #49 (TNF-α — where blockade is
      itself a CDI RISK FACTOR, a Clinical NEGATIVE signal). Immunosuppress
      the wrong axis in this population and you worsen outcomes.

───────────────────────────────────────────────────────────
#56 TIGHT JUNCTION PROTEINS (ZO-1, occludin, claudins) — STABILIZE ✓
    DRUGGABILITY: **DIFFICULT (structural)** — explicitly so in §5.3.
    These are scaffold/adaptor proteins with no enzymatic activity and no
    binding pocket; per the skill's own druggability table, scaffold
    proteins sit at the BOTTOM of the tractability hierarchy. "Upregulates
    ZO-1 and occludin" in a colitis model is a DOWNSTREAM PHENOTYPIC
    READOUT, not target engagement — it names an effect, not a target.
    Data present (TJP1 36 / OCLN 27 / CLDN1 13 rows) but all
    expression-level CTD associations, consistent with that reading.
═══════════════════════════════════════════════════════════
```

---

## 2. CANDIDATE → TARGET MAPPING AND SCORES

Scoring dimension: **target quality** = druggability × validation level × direction alignment × centrality to the CDI bottleneck (recurrence, per §4.6). This is *not* a scoring of the molecule's overall developability — ADMET, safety, and clinical feasibility are other agents' remits.

### 2.1 Summary table

| # | Candidate | Targets hit | Tier (§5.5) | Druggability | Validation | Direction | Score |
|---|---|---|---|---|---|---|---|
| 3 | **Ebselen** | #26 CPD + #21 PrdB | **Tier 1 + Tier 2** | Known (covalent Cys) + Theoretical (Sec) | Preclinical (strong) + Genetic | ✓ INHIBIT / ✓ INHIBIT | **8.5** |
| 1 | **Fidaxomicin** | #1 RNAP switch (+ partial Phase 1) | Incumbent | Known | **Clinical** | ✓ INHIBIT | **8.0** |
| 10 | **Bezlotoxumab** | #27 CROPS | Approved | Known (biologic only) | **Clinical** | ✓ NEUTRALIZE | **8.0** |
| 4 | **UDCA** | #11 + #66 | **Tier 1 + Tier 1** | Known (bile acid chem) | Preclinical (strong) | ✓ BLOCK / ✓ SUPPLY | **7.5** |
| 2 | **Vancomycin** | #2 D-Ala-D-Ala | Incumbent | Known | **Clinical** | ✓ target / ⚠ system | **7.0** |
| 7 | **Ibezapolstat** | #3 PolIIIC | — | Known (high) | Clinical (early) | ✓ INHIBIT | **7.0** |
| 5 | **Berberine** | #44, RELA, #56, #52, #53, #64–67 (indirect) | Tier 2 + non-tiered | Mixed (#56 Difficult) | Preclinical | ✓ all | **6.0** |
| 6 | **Niclosamide** | #30 (possibly #41) | — | Theoretical | Preclinical [EMERGING] | ✓ INHIBIT | **5.5** |
| 8 | **Conessine** | #7 (hypothesis only) | **Tier 1 target** | Theoretical, no structure | **Computational** (pairing) | ✓ INHIBIT | **5.0** |
| 9 | **Aprepitant** | #51 NK1R | — | **Known (high)** | Preclinical | ✓ ANTAGONIZE | **5.0** |

### 2.2 Candidate detail

**1. Fidaxomicin — 8.0 | Confidence: High | Knowledge-based**
Hits the single best-validated target in CDI: #1 is Clinical-validated, known druggable, correct direction, allosteric, and has no human ortholog. It also partially reaches Phase 1 via sub-MIC sporulation suppression — the only approved agent that touches the spore reservoir at all — and spares the microbiome, meaning it does not antagonize #64–#67 the way vancomycin does. The score is capped below 9 because target-level headroom is nil: the target is fully occupied by the incumbent, and §4.5's synthesis is explicit that killing *C. difficile* better is not the bottleneck. Resistance via *rpoB/rpoC* switch-region substitution is documented.
*Key data points:* `chembl_approved_drugs.csv` CHEMBL1255800, MW 1058.05, first approval 2011, `indication_class` includes "clostridium difficile infection" — the only candidate whose recorded indication is CDI. No mechanism/target row exists (stub files).

**2. Vancomycin — 7.0 | Confidence: High | Knowledge-based**
Target #2 carries maximal validation and near-zero resistance risk (a substrate target, not a mutable enzyme active site), and the direction is correct. It scores a full point below fidaxomicin for a target-intrinsic reason rather than a formulation one: D-Ala-D-Ala is conserved across all Gram-positives *including the 7α-dehydroxylating Clostridia of target #64*. Engaging #2 therefore degrades #64, #65, #66 and #67 — four RESTORE-direction targets — which is the mechanistic account of the ~25% recurrence rate. Of the ten candidates this is the closest thing to a direction violation in the set, and it belongs to the incumbent.
*Key data points:* CHEMBL262777 / CHEMBL1200628, MW 1449.27, first approval 1964, physchem fields blank (beyond ChEMBL's descriptor range — consistent with a non-absorbed macromolecule).

**3. Ebselen — 8.5 | Confidence: Moderate-High | Knowledge-based**
The strongest target portfolio on the list. #26 is Tier 1 with strong preclinical validation and, uniquely here, an *ideal chemotype*: a catalytic cysteine in a defined pocket is the most tractable thing a covalent program can be handed. #21 adds a second, mechanistically independent hit whose selenocysteine gives real covalent-selectivity leverage over host cysteine enzymes. Both directions are INHIBIT — correct. The dual-mechanism profile is exactly what §4.5's failure synthesis calls for, and both targets are anti-virulence/fitness rather than bactericidal, so neither antagonises #64–#67. The half-point of caution: ebselen is a promiscuous selenoelectrophile, and the model's own critique of allicin (§7.2 — "a promiscuous thiol-reactive electrophile") applies with reduced but non-zero force; CPD-independent TcdB toxicity and the #43 NOX1 escape route mean CPD blockade may be partial; and §A.3 warns that CDI preclinical efficacy predicts Phase 3 unusually poorly.

**4. UDCA — 7.5 | Confidence: Moderate | Knowledge-based (physchem data-backed)**
Two Tier 1 targets, both correctly directed, both in mature bile acid chemistry — the highest Tier-1 density of any candidate. It passes the direction audit cleanly: UDCA *supplies* a bile acid (#66 SUPPLY/MIMIC ✓) and *competes* at the germinant site (#11 COMPETITIVELY BLOCK ✓); it does not inhibit bai-operon 7α-dehydroxylation, so no RESTORE target is harmed. The reservations are target-biology reservations, not chemistry ones: UDCA is a 7β-epimer of CDCA, not DCA or LCA, and whether it reproduces true secondary-bile-acid growth inhibition at colonic concentrations is unresolved; ileal absorption and enterohepatic recycling make colonic delivery of the parent compound the weak link; and #61 FXR is flagged direction-UNCERTAIN in the model, so pool-level effects could run either way.
*Key data points:* CHEMBL1551 (URSODIOL), MW 392.58, aLogP 4.48, PSA 77.76, RO5 violations 0, first approval 1987, `oral_bioavailability=True` — the last is the concern, not the asset, under §6.2's inverted logic. Related: CHEMBL272427 (TAURURSODIOL), MW 499.71, approved 2022.

**5. Berberine — 6.0 | Confidence: Moderate | Mixed (class-level data-backed)**
The breadth is real and the directions are all correct — NLRP3/caspase-1 (#44) INHIBIT, NF-κB INHIBIT, AhR (#52) AGONIZE, PPARγ (#53) AGONIZE, tight junctions (#56) STABILIZE, plus indirect microbiome effects that at minimum do not antagonize #64–#67 the way vancomycin does. From a *target-profiling* standpoint that is also the problem: this is a polypharmacology profile, not a target. #56 is explicitly "Difficult (structural)" — scaffold proteins with no binding pocket, and "upregulates ZO-1/occludin" is a downstream phenotypic readout rather than demonstrated target engagement. #44 carries the same bidirectional risk the model flags for #48 and #49, where IL-1β/neutrophil signalling is partly protective. No single target here is both well-validated in CDI and cleanly engaged.
*Key data points:* CHEMBL295124, MW 336.37, aLogP 3.10, RO5 violations 0, QED 0.67, `natural_product=1`, `oral_bioavailability=False` (the CDI-favourable direction per §6.2), `withdrawn_flag=True` — worth flagging to the Safety Pharmacologist. **Berberine appears in the phytochemical interaction file only as a co-treatment mention inside CTD evidence strings (20 rows), never as a primary compound** — its NLRP3/NF-κB/tight-junction activity is *not* data-backed in this repository. The relevant target rows are populated by quercetin, luteolin, galangin, emodin, celastrol and rhein instead.

**6. Niclosamide — 5.5 | Confidence: Low-Moderate | Knowledge-based**
Direction is correct and #30 sits inside the highest-value module in the model, but the target itself is the weakest link: a pH-dependent conformational transition rather than a binding pocket, validation is Preclinical [EMERGING], and the amantadine-class precedent has a poor record of yielding selective leads. The larger issue is mechanism attribution — niclosamide is a protonophore, and its block of TcdB entry is at least as consistent with collapsing the endosomal pH gradient (functionally #41, v-ATPase/acidification) as with a specific TcdB delivery-domain interaction. If it is really a #41 agent, the target is a *host* organelle function with obvious selectivity concerns rather than a pathogen-specific site. This is directly testable against unrelated pH-dependent toxins.
*Key data points:* CHEMBL1448, MW 327.12, aLogP 3.86, RO5 violations 0, first approval 1982, `natural_product=1`.

**7. Ibezapolstat — 7.0 | Confidence: Moderate-High | Knowledge-based**
On pure target metrics this is close to the cleanest bacterial target in the set after #1: PolC is the Gram-positive-specific replicative polymerase with no human ortholog and no Gram-negative counterpart, the dGTP-competitive site is characterized, druggability is high, direction is correct, and validation has reached Clinical (early, Phase 2). The score is held at 7.0 by strategy, not by target quality: this is another narrow-spectrum antibacterial, and §4.5 identifies ridinilazole — same value proposition, better-resourced — as "the single most important cautionary tale," having met non-inferiority but failed superiority on sustained response. Target excellence does not rescue a strategy the disease has already disproven twice (surotomycin, cadazolid) and stalled once more.

**8. Conessine — 5.0 | Confidence: Low | Knowledge-based (hypothesis-level)**
This score splits sharply between target and pairing. **Target #7 is arguably the single most valuable target in the entire model** — Tier 1, obligatory committed step, genetically validated, chemically triggered, addresses the recurrence reservoir directly, zero clinical competition. **The conessine→CspC pairing has no evidence at all.** §7.2 marks it explicitly as a hypothesis the disease model itself generated, not a literature finding; §7.4 records CDI-specific experimental evidence as "None." The scaffold logic is genuinely attractive — germination is triggered by a steroid (taurocholate) and competitively inhibited by a steroid (CDCA), and conessine is a steroidal alkaloid — but attractive scaffold logic is Computational-level validation. Two further target-side problems: §2.3 states CspC's ligand-binding structural details remain incompletely resolved, so there is no structure-based design handle and any campaign is a phenotypic screen; and conessine is CNS-penetrant (H3 antagonist), meaning it is *absorbed* and forfeits the luminal confinement this target requires.
*Key data points:* absent from `chembl_approved_drugs.csv`; **0 rows** in `pubchem_phytochem_target_interactions.csv`. No project data exists for this compound.

**9. Aprepitant — 5.0 | Confidence: Moderate | Mixed (physchem data-backed)**
The paradox of this candidate is that it has the *best target-class druggability on the list* — NK1R is a Class A GPCR with an approved antagonist in hand — and the *worst target-strategy fit*. Validation in CDI is Preclinical only. It touches neither bacterium, toxin, nor microbiome, so it cannot address recurrence; §4.6 ranks host-directed anti-inflammatory therapy last of eight unmet needs. NK1R is subepithelial, so engagement requires systemic absorption, inverting §6.2's scoring asset. And its anti-secretory/antimotility pharmacology intersects the toxic megacolon risk flagged in §3.3.
*Key data points:* CHEMBL1471, MW 534.43, aLogP 4.95, PSA 83.24, RO5 violations 1, QED 0.44, approved 2003; CHEMBL1199324 (FOSAPREPITANT). `indication_class` is CINV/oncology-dominated — no GI infection indication. TACR1 has 5 phytochemical rows, none involving aprepitant.

**10. Bezlotoxumab — 8.0 | Confidence: High | Knowledge-based**
The only candidate whose target is Clinically validated *for the actual endpoint that matters* — recurrence reduction as an add-on to standard of care — and the direction (NEUTRALIZE) is correct. It is also the strategy that survived while its TcdA-directed partner failed, confirming the model's TcdB-over-TcdA prioritization at #31. Two target-intrinsic ceilings keep it from scoring higher. First, druggability at #27 is high but **modality-locked**: a repetitive β-solenoid glycan-binding array is a flat, extended PPI surface that admits antibodies and VHH multimers and essentially excludes small molecules — and the locked modality is IV, which is precisely what unmet need #4 asks to escape. Second, and more interesting biologically: CSPG4, the high-affinity receptor, binds the *delivery* domain around residues 1500–1800, not CROPS, and CROPS-truncated TcdB retains substantial cytotoxicity. #27 may be an excellent epitope that is not the functionally critical determinant — which fits the partial (~10-point absolute) recurrence benefit observed, and is compounded by the TcdB subtype variation flagged in §A.3.
*Key data points:* absent from `chembl_approved_drugs.csv` (biologic — the file is small-molecule dominated).

---

## 3. CROSS-CUTTING TARGET-LEVEL OBSERVATIONS

### 3.1 Direction-alignment audit (the team lead's explicit instruction)

I checked all ten candidates against the Direction column of §5. **No candidate directly inhibits a RESTORE/AUGMENT target** — no one proposes blocking baiCD, BSH, or SCFA production. The set is clean on the literal trap.

Two subtler direction findings are worth escalating:

1. **Vancomycin's system-level conflict.** Target #2 is INHIBIT-correct in isolation, but D-Ala-D-Ala is conserved in the 7α-dehydroxylating Clostridia that *are* target #64. Engaging #2 depletes #64, #65, #66 and #67 — four RESTORE targets — simultaneously. The direction violation is not at the target, it is at the system. This deserves to be named explicitly because it is the incumbent standard of care and because it is the mechanistic root of the recurrence problem the whole exercise is trying to solve.

2. **UDCA passes the audit that superficially looks like it should fail.** A bile-acid-directed agent is exactly where one expects a RESTORE-direction error. UDCA does not make it: it *supplies* rather than *inhibits*, engaging #66 (SUPPLY/MIMIC) and #11 (COMPETITIVELY BLOCK) both correctly. Any downstream agent that penalizes UDCA for "interfering with bile acid metabolism" has read the direction backwards.

A third, softer note: berberine and ibezapolstat both carry antibacterial activity and therefore carry a diluted version of vancomycin's problem. Berberine's rodent data reportedly shows better diversity preservation than vancomycin, which if it holds is a target-system advantage, not merely a potency claim — but it is animal-only.

### 3.2 The two target classes behave completely differently

The disease model's insistence on separating INHIBIT from RESTORE targets has a consequence that shows up sharply once all ten candidates are mapped: **every high-validation target in this set is an INHIBIT target, and every RESTORE target has low-or-no small-molecule validation.** #64, #65, #67, #69 are not small-molecule targets at all — the model states this outright ("not a small-molecule target — deliver the organism or the product"). The single exception is **#66, secondary bile acids themselves**, which is both RESTORE-direction *and* "Known druggable (mature bile acid chemistry)."

That makes #66 structurally unique in the target list: it is the only place where a conventional small molecule can act in the RESTORE direction. UDCA's score rests substantially on occupying that slot, and any future candidate that can engage #66 more faithfully than UDCA (a genuine DCA/LCA mimetic with colonic delivery) would inherit an unusually uncontested position.

### 3.3 Validation stratifies almost perfectly into "validated but occupied" vs. "open but preclinical"

| | Occupied | Open |
|---|---|---|
| **Clinical validation** | #1 fidaxomicin, #2 vancomycin, #27 bezlotoxumab | — |
| **Preclinical / genetic only** | — | #7, #11, #21, #26, #30, #66 |

There is no target in this set that is both clinically validated and commercially available. Every candidate is therefore either a me-too against a validated target or a first-mover against a preclinical one. Ibezapolstat (#3, Clinical-early) is the only entry that partially straddles this, and it straddles into the category §4.5 explicitly warns against.

### 3.4 Target-class druggability inverts strategic value

Ranking the ten purely by target-class tractability gives roughly: NK1R (GPCR) > TcdB CPD (Cys protease) ≈ PolC (polymerase) > RNAP (allosteric enzyme) > bile acid sites > CROPS (PPI) > tight junctions (scaffold) > CspC (pseudoprotease, unresolved structure).

Ranking them by value against §4.6's unmet needs gives almost the reverse: CspC/#11/#66 (recurrence + spore reservoir) > TcdB CPD (oral anti-toxin) > RNAP/PolC (initial cure, solved) > NK1R (host anti-inflammatory, ranked last).

**The most valuable targets in CDI are the least tractable ones, and the most tractable are the least valuable.** This is the structural reason the field has produced three failed narrow-spectrum antibiotics — those programs optimized for the tractable axis. Any candidate proposing a highly druggable target should be asked which axis it is optimizing.

### 3.5 A note on preclinical discounting

§A.3 instructs downstream agents to discount preclinical-only evidence *more steeply* in CDI than in most indications, because the hamster model is hyperacute and the mouse antibiotic-cocktail model is artificial. I have applied this: it is the reason ebselen (#26, Preclinical-strong) scores 8.5 rather than 9+, why UDCA sits at 7.5 despite two Tier 1 targets, and why niclosamide's [EMERGING] designation costs it more than it would elsewhere.

---

## 4. DATA GAPS

1. **No pathogen-target layer exists in this knowledge graph.** Zero *C. difficile* rows across every processed file. Targets #1–#34 — bacterial and toxin, i.e. the majority of the CDI target space — cannot be interrogated with project data at all.
2. **The ChEMBL derivative tables are test-mode artifacts.** `chembl_drug_targets.csv` (44 rows), `chembl_drug_mechanisms.csv` (11), `chembl_drug_indications.csv` (80), `chembl_bioactivities.csv` (24), `chembl_toxicity.csv` (2). All three assigned discovery greps against the first two returned nothing. Per CLAUDE.md the scraper supports a full run (`python src/scrapers/chembl/chembl_scraper.py`, hours) — that is the fix, and it would make the mechanism/target claims for at least vancomycin, metronidazole, niclosamide, aprepitant and fidaxomicin data-backed.
3. **The phytochemical file cannot support the natural-product candidates.** Berberine appears only as an incidental co-treatment mention; conessine is entirely absent. Neither *Berberis*, *Coptis*, nor *Holarrhena* chemistry is represented among the 312 compounds.
4. **DisGeNET coverage is Oral Mucositis only** (`disgenet__OM_altexps.csv`, `_biomarkers`, `_genvars`). No CDI gene-disease associations. Host-susceptibility targets cannot be validated against project data.
5. **No structural data source in the repository.** Druggability calls (pocket depth, catalytic cysteine accessibility, CROPS surface topology, CspC ligand site) are made from domain knowledge with no PDB/AlphaFold layer available to check them.
6. **No microbiome or metagenomic data.** Targets #64–#72 — the entire RESTORE class, and per §5.5 the tier containing the clearest path to breaking the recurrence loop — have no representation in the knowledge graph in any form.

---

## 5. CONCLUSIONS

**Strongest target portfolio: Ebselen (8.5).** Tier 1 target #26 with an ideal covalent-cysteine chemotype and strong preclinical validation, plus an independent second hit at #21 whose selenocysteine confers genuine selectivity leverage. Both directions correct, both anti-virulence rather than bactericidal, and the dual-mechanism profile answers §4.5's central lesson that single-mechanism approaches fail in CDI. Fidaxomicin (#1) hits the better-validated target but into a fully occupied space.

**Most valuable target, worst-evidenced pairing: CspC (#7) via conessine.** The target may be the best in the entire model; the compound-target link is a hypothesis the disease model generated about itself. The right downstream action is to treat #7 as a screening campaign target and conessine as one scaffold entry in it — not to advance conessine as a candidate.

**Biggest target-level concern:** the inversion in §3.4 — CDI's most valuable targets are its least tractable, and its most tractable are its least valuable. Three Phase 3 failures came from programs that optimized tractability.

---

*Computational target analysis. All druggability and validation assessments require experimental verification. Bacterial and toxin target assessments are knowledge-based — the project knowledge graph contains no* C. difficile *data.*
