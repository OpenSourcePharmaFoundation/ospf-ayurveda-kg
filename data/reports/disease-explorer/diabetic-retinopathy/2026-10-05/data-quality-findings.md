# Data Quality Findings (incidental to the DR run)

Surfaced by the Phase 0 PPARα scout and verified independently by the orchestrator.
These are defects in project data, not findings about diabetic retinopathy.

## 1. `chembl_drug_metabolism.csv` — `drug_name` column is meaningless; file is 10x duplicated

**Severity: high** (silently corrupt data, 3.0 MB file, git-tracked)

Evidence:
- 10,000 rows contain only **1,000 unique records** once `drug_name` is ignored — a clean 10.0x inflation.
- Only **10 distinct `drug_name` values** appear, and every one of the 152 `drug_chembl_id`
  values is paired with every one of them.
- Concretely: `drug_chembl_id=CHEMBL672`, `substrate_name=FENOFIBRATE`,
  `metabolite_name=FENOFIBRIC ACID`, `enzyme_name=Esterases` — a correct record — is
  written ten times, labelled `drug_name` = PRAZOSIN, NICOTINE, OFLOXACIN, NALIDIXIC ACID,
  INDOMETHACIN, SULBACTAM, TAZOBACTAM, CIPROFLOXACIN, NORFLOXACIN, AMPHETAMINE in turn.

Root cause — `src/scrapers/chembl/chembl_scraper.py`:

- Line 261: `url = f"{BASE_URL}/metabolism?molecule_chembl_id={chembl_id}&limit=1000"`.
  `molecule_chembl_id` is not a valid filter field on the ChEMBL `/metabolism` endpoint.
  ChEMBL ignores the unrecognised parameter and returns the **first 1,000 records of the
  whole table** on every call, identically, for every drug queried.
- Line 889: `"drug_name": drug_name` takes the name from the **loop variable** (the drug
  being queried) while line 888 takes `drug_chembl_id` from the **API response**. The two
  columns therefore describe different drugs in every row.

The run that produced this file was in test mode (`test_limit = 10`), which is why there
are exactly 10 queried drugs. A full run would have produced the same 1,000 records
duplicated ~3,276 times.

Suggested fix:
1. Filter on a field the endpoint supports (`drug_chembl_id` or `substrate_chembl_id`),
   and assert the returned `drug_chembl_id` matches the requested id before writing.
2. Drop the `drug_name` column, or populate it by looking up the **response's**
   `drug_chembl_id`, never the loop variable.
3. Add a post-write uniqueness check — identical record counts across distinct queries is
   the signature of an ignored filter and is cheap to assert.

Not fixed in this run: out of scope for the DR analysis, and re-scraping requires network
access and a full ChEMBL pass.

## 2. ChEMBL mechanism and target tables are near-empty test extracts

`chembl_drug_mechanisms.csv` has 11 rows, `chembl_drug_targets.csv` 44,
`chembl_drug_indications.csv` 80, against 3,276 drugs in `chembl_approved_drugs.csv`.
Zero PPAR content in any of them. Any analysis needing drug-target or mechanism edges
cannot be data-backed from this project today. These files are labelled
`⚠️ Test Data` in `src/analysis/chembl_statistics.py`, so this is known, but the gap is
large enough to change what the pipeline can honestly claim.

## 3. Legacy Oral Mucositis scoping

`disgenet__OM_*.csv`, `ttd_drug_target_genes.csv` and `drugbank_drug_targets.csv` are all
scoped to the earlier Oral Mucositis project. There are no gene-disease associations for
diabetic retinopathy anywhere in the project.

## 4. PubChem interaction data is predominantly expression-level, not binding

Of 143 PPARA rows, the large majority are Comparative Toxicogenomics Database statements
of the form "X results in increased expression of PPARA mRNA" or "X inhibits the reaction
[insult results in decreased expression of PPARA]". These are not target-engagement
evidence. The best-controlled activation record in the file (antagonist-reversal with
GW 6471) belongs to dibutyl phthalate, a plasticiser. Downstream scoring must not treat
row counts as evidence weight.

## 5. Coverage gaps in the approved-drugs table

Bezafibrate, ruboxistaurin and calcium dobesilate are absent from the 3,276-row table
despite being relevant to the mechanism classes under study. Aflibercept, ranibizumab and
bevacizumab are absent as biologics. The table is small-molecule-biased and incomplete.

## 6. `medicinal_plants_with_uses.csv` is 99.6% empty — and disconfirms, not corroborates

**Severity: high** (315 KB file whose name promises therapeutic uses; it has almost none)

Found by the Phase 1 Traditional Medicine agent, verified independently by the orchestrator:

- 1,907 of 1,915 rows carry the literal string `"UNKNOWN USE"` in the `Uses` column — **99.6%**.
- Only **8 rows** contain a real use description.
- **Zero** of those 8 mention eye, vision, ocular, retinal or diabetes.
- The 8 real rows describe plants already present in the IMPPAT data, so the file adds
  no coverage at all.

The file's name invites exactly the mistake of treating it as a therapeutic-use corpus.
It is not one. Any analysis that greps it for a disease keyword will get hits only from
plant names, families, or bibliographic strings in other columns.

## 7. Keyword hits on bibliographic metadata produced a false finding *inside* this run

The Phase 0 disease model reported "8 of 13 IMPPAT plants carry relevant eye/diabetes
uses". The correct figure is **6 of 13**. *Alstonia scholaris* and *Santalum album* were
admitted on a "vision" keyword match whose hits are **100% the bibliographic string
"Forest Divisions (Maharashtra)"**. A further 4 of 13 plants have zero use records, so
the honest denominator is 9, not 13.

This is notable because the disease model had itself warned about this artifact class in
a *different* file, then fell into it. **Substring matching across a whole record, rather
than against the specific field that carries the claim, is the recurring defect in this
project's data handling.** It has now produced three separate false findings: the
original DR-indication miss, the plant "vision" hits, and the `statin` / `somatostatin`
false positive flagged during blinding QC.

Recommendation: field-scoped matching with explicit column selection, never whole-record
grep, in any analysis code under `src/`.

## 8. Target-coverage counts are not evidence — they measure study effort

**This invalidates a framing the orchestrator used in `data-inventory.md`.**

The Traditional Medicine agent ran the null model that should have been run first:

- A **random** set of 20 compounds covers ≥26 of the 27 DR-panel genes with probability
  **0.58**; at 40 compounds, 0.95. Broad coverage is the default outcome, not a signal.
- Correlation between a plant's catalogue size and its DR-matrix hits: **r = 0.911**.
- **Ascorbic acid alone covers 23 of 27.** *Trichosanthes dioica* covers 27 of 27 from
  7 compounds. Sandalwood, which has no recorded eye use, covers 26 of 27.
- The panel's high-count genes are a generic rodent stress block — TNF appears for 84%
  of compounds, CASP3 78%, IL6 69%. The DR-specific genes are nearly empty: ANGPT2 1,
  PRKCB 11, KDR 15. Even AKR1B1's 22 hits include sugars that are *substrates* of aldose
  reductase, not inhibitors.

**Consequence:** the "compounds hitting PPARA plus the widest DR-target set" table in
`data-inventory.md` ranks compounds by how heavily they have been studied in the
Comparative Toxicogenomics Database. It must not be read as polypharmacology. The
`evidence/compound-dr-target-matrix.tsv` file carries a header warning to this effect.

## 9. The traditional DR pharmacopoeia is absent from the project

Not present anywhere in the data: curcumin, berberine, piperine, puerarin, tanshinone IIA,
salvianolic acid B, astragaloside IV, crocin, anthocyanins, resveratrol. Nor the source
plants: Danshen, *Panax notoginseng*, *Astragalus*, bilberry, *Pinus pinaster*, saffron,
*Ginkgo*, *Curcuma*. Triphala is 1 of 3 present; *Tinospora cordifolia* has zero chemistry.

So the project's phytochemical data cannot speak to the traditional DR corpus at all. Any
apparent ethnobotanical convergence in this dataset is convergence with what IMPPAT
happens to catalogue, not with what the traditions actually use.

## 10. The DR gene panel is blind to the pathway this run is about — orchestrator error

**Severity: high. This is a defect in the orchestrator's own evidence pack, not in source data.**

Found by the Phase 1 Molecular Target Analyst, verified by the orchestrator:

The 27-gene DR panel used to build `evidence/compound-dr-target-matrix.tsv` contains
**all three PPAR receptors** (PPARA, PPARD, PPARG) and **zero PPAR effector genes**.
Absent: ANGPTL4, CPT1A, ACOX1, HMGCS2, FABP1/4/5, LPL, APOA1, APOA5, ABCA1, FGF21,
PDK4, ACADM, EHHADH.

Consequence: **the pathway this entire run is about is structurally invisible to the
run's own data.** Every directional claim about what PPARα agonism does downstream —
including the ANGPTL4 argument that became the pipeline's central controversy — is
necessarily knowledge-based. The data cannot confirm or refute any of it.

I chose that panel. It was assembled from DR pathobiology genes before the PPARα
mechanism was characterised, and it was never revised once the focus narrowed. The
correct panel for this question would have included the receptor's transcriptional
programme alongside the disease genes.

## 11. SCORING HAZARD — the target matrix structurally favours polyphenols over drugs

**Verified: only 5 of the 15 candidates appear anywhere in
`evidence/compound-dr-target-matrix.tsv`** — linoleic acid, alpha-linolenic acid,
linalool, quercetin and melatonin. All five are natural products. **Every approved drug
in the candidate set is absent**, because the underlying PubChem/CTD file is a
phytochemical and environmental-chemical corpus, not a drug corpus.

Combined with finding §8 (coverage counts measure study effort, not polypharmacology),
this produces a specific and severe hazard:

> **Any ranking that weights "number of DR-panel targets hit" will rank polyphenols above
> approved drugs as a pure database artifact — and will do so while appearing data-backed.**

**Instruction carried forward to the Candidate Ranker:** do not use target-count as a
scoring dimension. Absence from the matrix is not evidence of inactivity; presence in it
is not evidence of relevance. Score on evidence quality (binding > activation >
expression association), stage fit, compartment fit and exposure, and treat the matrix as
a lookup for specific claims only.

## 12. SCORING HAZARD — `alogp` is not a permeability proxy, and `logd` is empty

Found by the Phase 1 Medicinal Chemist; the empty-column fact verified independently by
the ADMET agent (`logd` populated **0 / 3276**, `cx_logd` 0/3276, `permeability` 0/3276).

Fenofibric acid carries `alogp = 3.81` in the blinded dataset. Its actual distribution
coefficient at physiological pH is approximately **-0.5**, because its pKa near 3.1 leaves
it >99.99% anionic at pH 7.4. **A ranker reading `alogp` as a permeability proxy is wrong
by roughly four orders of magnitude for every acid in the candidate set** — which is every
Group A compound and both Group B fatty acids.

The dataset contains no `logd` value to correct this with. The column exists and is empty
for all 3,276 rows.

**Instruction carried forward to the Candidate Ranker and all Phase 2 agents:** do not use
`alogp` to rank tissue penetration for ionisable compounds. Use the explicit ionisation
state and the agents' logD estimates, which are knowledge-based and must be labelled as
such.

## 13. ~~The structural reason the retinal PPARα hypothesis may be untestable with fibrates~~ — RETRACTED, see §18

Not a data defect — a finding recorded here because it governs how the final ranking must
be read.

Retinal receptor occupancy is governed by `fu x C_plasma x Kp,uu / EC50`. The fibrate
series improved the denominator (potency) by 4-5 logs from fenofibric acid to pemafibrate
while degrading **every term in the numerator**: free fraction, achievable plasma
concentration, and tissue partitioning all move the wrong way. The cause is structural
rather than coincidental — the lipophilic bulk that fills the receptor's arms II/III is
the same recognition element that albumin site II and the hepatic OATP1B uptake
transporters bind.

**Consequence:** pemafibrate's hepatoselectivity is not a separable design choice that a
medicinal chemist could engineer away while keeping the potency. It is the direct
consequence of the potency strategy itself. Therefore **no molecule in the fibrate
chemotype can test the retina-intrinsic PPARα hypothesis** — a negative result with any of
them is ambiguous between "retinal PPARα agonism does not help" and "the drug never
arrived."

This resolves the Round 1 conflict between the Phase 0 scout (hepatoselectivity is a bug)
and the Target Analyst (it is a feature) at a level beneath both: within this chemical
series the property is not optional, so the question they were arguing about cannot be
settled by choosing a different fibrate. Testing it requires the non-acidic chemotype the
chemist proposes in its scaffold-hopping section, which does not currently exist as a drug.

## 14. Orchestrator claim corrected in Phase 2 — the control was the wrong particle

The Round 1 synthesis (§5) asserted that "no non-PPAR remnant-lowering generic exists" when
justifying ezetimibe as the mechanism-discriminating control. The Drug Repurposing
Strategist corrected this.

**Why the original control choice was weak.** Ezetimibe lowers predominantly LDL
cholesterol. Fibrates lower triglyceride-rich **remnant** particles via APOC3 repression.
Diabetic dyslipidaemia is a remnant disorder in which LDL-C is frequently normal, and the
disease model's toxic species is the modified apoB particle retained in the outer
plexiform layer. **A null result with ezetimibe would therefore have been uninterpretable**
— it would not distinguish "the receptor is irrelevant" from "the wrong particle was
lowered."

**The matched control.** An apoC-III-directed agent (olezarsen, an antisense
oligonucleotide) suppresses the exact node through which PPARα lowers remnants, with no
receptor involvement. Same mechanism, receptor deleted.

**A second, uncomfortable prediction surfaced.** PCSK9 inhibitors lower apoB by 45-55%
against a fibrate's 5-15%. If the operative mechanism is apoB supply, they should work
substantially better — a clean falsifiable prediction that the pipeline should state rather
than avoid. The counter-argument is that apoB *mass* is the wrong metric and remnant /
apoC-III concentration is the right one, which keeps the hypothesis alive but **only as a
remnant hypothesis**, not an apoB hypothesis. Compounding this, statins are background
therapy in both arms at 35-45% apoB lowering, so whatever a fibrate adds is likely the
remnant component statins do not touch.

All of the above is `[knowledge-based]`; no project data bears on it.

## 15. Two orchestrator framing errors corrected by the Pathway Analyst

**(a) "Hub" was used as a single property, and it is two.** Round 1 debated whether PPARα
"escapes the single-node criticism by being a transcriptional hub." That debate was
unresolvable as posed, because the DR network has **two hubs of opposite topology**:
ROS/GAPDH is a **divergence** point (damage flux fans out from it) and NF-κB/RELA is a
**convergence** point (inflammatory signals fan in). Scoring a candidate requires naming
which hub and which side of it. PPARα fits neither — **no damage flux passes through the
receptor at all**; it is a modulator acting on the convergence hub from outside, which is a
different claim from being a hub.

**(b) CD36/LOX-1 blockade is not the complement to lipid efflux — it is a second uptake
intervention.** My Phase 2 prompt framed scavenger-receptor blockade as "the complementary
upstream option" to the efflux arm. That is wrong, and the error has a wrong-sign risk:
macrophage uptake is the **only catabolic route** for retained apoB lipoprotein in retina,
so blocking it converts "foam cells that die and re-release lipid" into "extracellular
modified lipoprotein that nothing removes at all." Its legitimate claim is CD36/TLR→NLRP3
signalling, which belongs to the **inflammation module (P6), not the lipid-efflux
sub-module (P8.3)**. The genuine complement to a transporter inducer is an **acceptor
donor**.

## 16. The fibrates do not cover the lipid efflux arm — settled by Round 1's own logic

ABCA1 is a PPARα-inducible gene, which raised the question of whether the fibrates already
cover the efflux gap. They do not, and the argument is internally consistent with the
ANGPTL4 resolution rather than an independent assertion:

> ABCA1 induction is **PPRE-driven transactivation — the identical limb that the ANGPTL4
> resolution declared absent at achievable retinal occupancy.** If retinal occupancy is too
> low to induce CPT1A, it is too low to induce ABCA1. The induction is additionally a
> **two-step relay** (PPARα → NR1H3/LXRα → ABCA1), which is *more* occupancy-sensitive, not
> less. And the transrepression discount does not apply, because a PPRE is transactivation
> by definition.

The one reachable limb — hepatic APOA1 induction raising circulating acceptor — aims at the
**acceptor** half while the diabetic lesion sits on the **transporter** half, and it raises
mature HDL when ABCA1's actual substrate is lipid-poor pre-β ApoA1. Worth roughly half a
point, not coverage.

**The structural statement worth carrying to the final report:**

> PPARα has an engagement-certain compartment that is not the diseased one. The efflux
> arm's only useful compartment **is** the diseased one. **You cannot perform retinal
> reverse cholesterol transport from the liver.**

## 17a. One encouraging asymmetry — the LXR pocket is not charge-locked

The chemist established that the PPARα pocket **mandates** a lipophilic acid, which is what
couples potency to hepatoselectivity and makes a retina-penetrant agonist structurally
self-defeating. **The LXR pocket does not** — LXR ligands are neutral. Ionisation is not
structurally locked in for that target.

**Consequence:** an orally retina-penetrant LXRβ-biased modulator is chemically conceivable
in a way that a retina-penetrant PPARα agonist is not. This is the most actionable
medicinal-chemistry opening the run has produced, and it points at the efflux arm — the
gap — rather than at the supply arm, which is already covered. It should be routed to the
SAR Analyst and carried into the final report's forward-look.

Caveat to carry with it: systemic LXR agonism has repeatedly failed on hepatic steatosis
and hypertriglyceridaemia, so isoform selectivity or tissue restriction is the whole
problem, not a detail.

## 17b. BLINDING DEFECT — an in-file boundary does not survive structural inspection

**Severity: high (benchmark integrity). Found and self-disclosed by the Devil's Advocate.**

The Literature Reviewer's report was structured as Part A (blinded) followed by a section
headed `## POST-HOC UNBLINDING (EXCLUDED FROM SCORING)`. Blinded agents were instructed to
read Part A and stop at that heading.

The Devil's Advocate, trying to locate where Part A ended, ran a heading-level grep across
the file. **That returned the Part B headings, two of which carried substantive content.**
[The content of those headings is deliberately NOT described here — see §19. Describing it
is what turned this record into a second leak.] The agent stopped immediately, read no Part B
body text, and disclosed the leak in full — including a
section-by-section assessment of which of its own arguments were contaminated and which were
not, and the observation that its bet-against pick was the *other* leader.

**This is the same class of defect as the `[REDACTED-HOLDOUT]` markers found in Phase 0: the
content was protected and the structure was not.** Any structural listing operation defeats
an in-file boundary — heading grep, table of contents, outline view, editor symbol list,
a summariser's first pass.

**Fix applied.** Part B moved to a separate sibling file, `agents/UNBLINDING-part-b.md`,
carrying a do-not-read banner. `p2-literature.md` retains Part A and its SCOREBLOCK plus a
stub recording the move. Verified afterwards: no trial name, regulatory body or approval
status appears anywhere in the remaining Part A text.

**Rule adopted for future blinded runs:** held-out content lives in a separate file, never
behind a marker inside a file that blinded agents are told to read. Boundaries must be
enforced by the filesystem, not by instruction.

**Honest accounting of the contamination.** The advocate's mechanism attack (its §6) was the
section most affected, because it had been assigned to argue that the mechanism may be
intraocular, and a Part B heading pointed that way. Its arguments are constructed from Part A
and general pharmacology and can be checked line by line, but **its confidence in that
section should be discounted, and the benchmark must record that one of eleven agents had
partial structural knowledge of the answer before writing.** The other five sections are
arithmetic and consistency checks against files in the run tree and are uncontaminated.

## 18. ORCHESTRATOR ERROR — a term reported as a product, and §13 retracted

**Severity: high. This is the most consequential error in the run, and it is mine.**
Found by the Devil's Advocate, verified by the orchestrator line-by-line against
`agents/p1-admet.md` §3.2.

### What I got wrong

**(a) I conflated the Kp,uu term with the occupancy product.** Round 1 §2 asserted that the
ADMET agent "independently produced the same result from the other direction — potency rank is
the exact reverse of retinal-access rank," and used it to support the claim that potency and
engagement are anti-correlated.

The *Kp,uu term alone* is reversed against potency — that is ADMET's Table 1, explicitly headed
"Rank by retinal access (Kp,uu)." The *occupancy product* is not. From ADMET §3.2:

| Compound | Endothelial margin vs free EC50 |
|---|---|
| **Elafibranor** | **−0.7 to +0.4 log** |
| Pemafibrate | −1.6 to −0.2 log |
| Fenofibric acid | −3.0 to −1.1 log |

**Same order as potency.** ADMET's own wording is that potency is "nearly **orthogonal** to
engagement," which I rendered as inversely correlated.

**(b) I reported a favourable range end as the central estimate.** I described the
endothelial compartment as "ALIVE, marginal" and quoted Kp,uu 0.2–0.7 — the partitioning
figure — rather than the margin, which is −3.0 to −1.1 log. The ADMET agent's own reading was
*"Not robust engagement anywhere; a small, chronic, partial transcriptional nudge in the
endothelium and RPE is arguable."* My framing was more favourable than its source.

**(c) I reported the scout's correction as a correction to the conclusion.** Fixing the
scout's inconsistent free-versus-nominal comparison closes ~1 log *of the comparison method*.
It does not move fenofibric acid's endothelial position, which remains ~2 logs short at
midpoint — essentially where the scout left it.

### What it cost

**§13 of this document is retracted.** It asserted that "no molecule in the fibrate chemotype
can test the retina-intrinsic PPARα hypothesis." **The run had a probe in its own candidate
set:** ADMET names elafibranor "the only Group A compound that plausibly reaches or exceeds its
free EC50 at the retinal endothelium… the cleanest pharmacological probe."

That retracted finding propagated:
- It framed the SAR Analyst's entire 1,029-line assignment around escaping a constraint that
  was overstated.
- It fed a non-clinical-entity cost model for a molecule that may not be needed.
- It appeared in the benchmark result as a headline structural conclusion.

**The retraction is partial.** Elafibranor is genuinely confounded — PPARδ co-agonism muddies
the isoform question, a Michael-acceptor enone at 120 mg/day is a real chronic liability, and
ADMET flags its Cmax as the lowest-confidence number in that report. **But "confounded and
uncertain" is a different claim from "structurally impossible," and I asserted the latter.**

### The generalisable lesson

The Devil's Advocate's own framing, which I endorse:

> **The highest-yield attack surface in a multi-agent pipeline is not any agent's reasoning —
> it is the synthesis layer, where ranges get collapsed to point estimates and contradictions
> get averaged away.** Both of its top findings are orchestrator transcription errors, not
> agent errors.

Every agent in this run reported ranges with explicit uncertainty bounds and labelled
provenance. The synthesis stripped the bounds. **Rule adopted: when a synthesis carries a
quantitative claim forward, it carries the range and the provenance tag, or it does not carry
the claim.**

### Action taken

- Round 1 synthesis §1 table and §2 corrected in place, with the retraction shown rather than
  silently edited.
- §13 above marked retracted.
- Benchmark result updated.
- **Elafibranor reinstated as a short-duration (~12-week) mechanistic probe candidate** — not
  as a chronic therapeutic, where its safety profile remains poor.

## 19. ORCHESTRATOR ERROR — the defect log itself became the leak, and it reached the final ranker

**Severity: high (benchmark integrity). Self-disclosed by the Candidate Ranker.**

When I documented the §17b blinding defect, I described **what the leaked headings said** —
that one named a candidate as an established approved therapy for this indication and another
announced the mechanism analysis was wrong.

I then instructed the Candidate Ranker to read `data-quality-findings.md` as **binding scoring
instructions**.

**So the record of the leak became a larger leak than the leak.** The original exposure
reached one agent, which disclosed it and quarantined its own contaminated section. My
description of it reached every agent afterwards that was told to read this file — including
the agent producing the pipeline's final ranking.

**This is the same error class for the third time in one run:**
1. `[REDACTED-HOLDOUT]` markers — content protected, structure not (Phase 0)
2. Part B behind an in-file boundary — content protected, structure not (Debate)
3. **This entry — the incident report describing the content the incident exposed**

Each fix introduced the next instance. The pattern is that I kept protecting the payload and
leaving its description, location or shape in a place blinded agents were required to look.

**Consequence for the benchmark — stated plainly, not minimised:**

> **The final Phase 3 ranking cannot be claimed as a clean blinded result.** The agent that
> produced it knew, before ranking, that some candidate in the set was an established approved
> therapy and that the pipeline's mechanism conclusion was wrong. Its P@1 = 1.00 and
> P@3 = 1.00 must be reported with that qualification attached.
>
> **The Round 1 consensus ranking is unaffected** — it was produced and scored before this
> entry existed, and its metrics (P@1 = 1.00, first tier-1 hit at rank 1) stand as the clean
> measurement.

**Mitigating facts, recorded without using them as an excuse.** The ranker disclosed the
contamination unprompted rather than exploiting it silently. Its two leader-affecting moves
are independently checkable and do not depend on the leak: the pemafibrate demotion is argued
from that drug's own cardiovascular outcome record in a near-identical population (non-DR
evidence, permitted under protocol), and the elafibranor reinstatement is re-derived
arithmetic from `p1-admet.md` §3.2 that I verified separately. Knowing *that* an approved
therapy exists in the set is also weaker information than knowing *which* — and the ranker
states it did not know which.

**Rule adopted, replacing the §17b rule which was insufficient:** an incident report about a
blinding breach records *that* a breach occurred, its mechanism, and its scope — **never the
content disclosed.** Content goes in the quarantined file with the rest of the held-out
material. And no file that blinded agents are required to read may ever contain a description
of held-out content, including a description written to protect it.

## 20. Round 2's combination argument was right for a mis-stated reason

Found by the Combination Designer (run after the pipeline initially shipped without it).

Round 2 §4 and the consensus report carried the claim that a supply-lowering agent and an
efflux-promoting agent are **multiplicative** while two supply-side agents are "additive at
best." The first half is right; **the contrast is wrong.**

Two supply agents are *also* multiplicative on burden — scaling influx by 0.85 and 0.60 gives
0.51, a product. The real distinction is **parameter independence and headroom**, not
algebraic form.

**The correct argument is stronger than the one stated.** Solving the self-renewing
foam-cell cycle as a two-compartment system gives burden = influx ÷ clearance **exactly**
(the recycling rate cancels). But as clearance approaches zero, **the system has no steady
state — it integrates.** A supply agent alone then buys *delay*, not a bounded burden. That
is a change of dynamical regime, not a multiplier.

**Two consequences the run had backwards:**

1. **The right second component is an extracellular acceptor or scavenger, not primarily a
   transporter inducer.** A direct removal term keeps burden finite even at zero transporter
   activity; a transporter inducer multiplies a term that may already be near zero. The run
   had carried LXR modulation as the primary opening (findings §17a) and acceptor donation as
   secondary. **The arithmetic reverses that**, and the acceptor route additionally dissolves
   the barrier-penetration problem because it can be delivered locally.

2. **If the integrating regime applies, monotherapy benefit is time-limited by construction.**
   That bears directly on the durability question the Phase 3 withdrawal extension was
   designed to answer, and it was not considered when that extension was designed.

**Both are cheap to settle** — the Combination Designer costs the two measurements at roughly
$100–130k inside the existing Gate 1, against a $5–9M trial.

**Process note.** This is the fourth instance in this run of a conclusion being correct while
its stated justification was not (cf. §15 the hub framing, §18 term-versus-product, and the
ranker's FGF21 concentration gap). In each case the error was found by the next agent to look
at it with a different method. **A pipeline of this kind should treat "right answer, wrong
reason" as the expected failure mode and schedule for it**, rather than treating agreement
between rounds as confirmation.

## 21. TRIAL-DESIGN DEFECT — a Gate 1 kill criterion that can terminate a working mechanism

Found by the Combination Designer. **This is the most immediately actionable finding in the
run, because it would have been acted on.**

The Phase 3 feasibility plan's Gate 1 kill criterion read: *"No change in microaneurysm
turnover or hyperreflective foci at 12 months despite confirmed ≥30% remnant lowering."* It
treats the two imaging readouts as interchangeable. **They measure different things on
different clocks:**

- **Microaneurysm turnover is a flux measure** — it responds on the timescale of new lesion
  formation, which a supply-lowering agent acts on directly.
- **Hyperreflective-foci burden is a stock measure** whose time constant is **1 ÷ clearance**
  — and clearance is precisely the parameter diabetes suppresses, and the parameter the entire
  efflux-gap analysis says is near zero in this disease.

**Consequence:** the stock measure can show no change at 12 months **while the mechanism is
working**, because the deposit is still draining on a longer clock. Reading that null as
mechanism failure would terminate a true positive at the $5–9M gate, before the $43–58M
pivotal programme it was meant to protect.

**Fix applied to the plan:** flux measure primary; stock measure secondary with an explicitly
weaker prior. **And a null Gate 1 result must be interpreted against the measured clearance
rate, not against calendar time alone** — which is one of the two cheap measurements §20
already recommends adding to that gate.

**Why this was missed.** The feasibility agent designed the gate before the combination
analysis derived the clearance time constant, and no later agent re-read the gate against it.
Same structural cause as findings §18 and §20: a quantity derived in one phase was not
propagated back to a decision made in an earlier one. **A pipeline of this kind needs an
explicit back-propagation pass over prior decisions whenever a later phase derives a new rate
constant, threshold or time constant.**

## 22. Reporting frame changed — research programme foregrounded over development economics

Not a defect; a reframing of the deliverables, recorded for provenance.

The run's forward-looking output was originally organised as a **staged, costed development
plan** — gates, trial designs, regulatory pathway, exclusivity, deployment economics. That
framing was inherited from the Clinical Feasibility role and from the pipeline's default
report format, not chosen deliberately.

**It inverted the actual state of the problem.** The programme is not limited by cost, trial
design or commercial structure. It is limited by **one unmeasured concentration** (free
fibrate in retinal tissue, never measured in any species) and **one unperformed necessity
experiment** (cell-type-restricted receptor deletion in retina, absent after ~15 years of
interest in the target). No amount of development planning substitutes for either.

**Change made:**
- New primary forward-looking deliverable: **`research-program.md`** — the experimental
  agenda, assembled from experiments specified by named agents during the run, sequenced and
  costed by what each decides.
- The consensus report's `PATH TO PATIENTS` section replaced by **`NEXT EXPERIMENTS — what the
  analysis cannot settle`**, organised by scientific question rather than development stage.
- Development economics retained in full in `agents/p3-feasibility.md` and referenced in one
  paragraph, explicitly marked as not the organising frame.
- Candidate ranking preamble now states that several high-ranked entries are **instruments
  rather than assets** — probes and control arms, scored for what they measure rather than for
  therapeutic merit. Elafibranor (probe), olezarsen and inclisiran (falsification arms) and
  seladelpar (isoform control) are all in the top eight on that basis.

**Content was reorganised, not invented.** Every experiment in `research-program.md` traces to
a named agent: the rodent transactivation/transrepression study (Round 1 §4, with two arms
added by the Literature Reviewer), the aqueous humour measurement and the conditional-deletion
necessity experiment (Literature Reviewer §A6), the lipid-change covariate analysis
(Literature Reviewer, flagged as the highest-value item because it requires no new study), the
FGF21 concentration bridge (Candidate Ranker), the transporter-silenced explant study
(Combination Designer §4.2), and the bench chemistry package (SAR Analyst §9.2).
