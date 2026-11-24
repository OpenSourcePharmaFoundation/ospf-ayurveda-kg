# Diabetic Retinopathy — Blinded Drug Discovery Run
**2026-10-05 · 16 agents · 5 phases · ~17,000 lines of analysis**

Two questions were asked of this run:

1. **Evaluate possible treatments for diabetic retinopathy, focusing on PPARα.**
2. **Do it blind** — with every DR indication redacted from the dataset — so the pipeline's
   rediscovery ability could be measured afterwards.

---

## Start here

### → **`REPORT.md`** — the single consolidated report, self-contained.

Everything below is supporting material. Read `REPORT.md` unless you need provenance or depth
on a specific phase.

| If you want… | Read |
|---|---|
| **Everything, in one document** | **`REPORT.md`** |
| The ranking and mechanism in pipeline format | `consensus-report.md` |
| **What to actually run in the lab** | **`research-program.md`** — the experimental agenda, sequenced and costed by what each experiment decides |
| **Did the blinded pipeline get it right?** | **`BENCHMARK-RESULT.md`** — scored against the held-out answer key |
| **What went wrong in the analysis** | **`data-quality-findings.md`** — 22 defects, 5 of them orchestrator errors |

---

## The short version

**Fenofibric acid ranks first** for early-to-moderate disease. The pipeline derived the
fibrate class from receptor pharmacology alone, with every retinopathy indication stripped
from its data.

**It also corrected its own brief on staging** — arguing from mechanism that the treatable
window is mild-to-moderate non-proliferative disease, not the preclinical window it was told
was the top unmet need, because an intact blood-retinal barrier means there is no lipoprotein
extravasation to prevent.

**The mechanism is unresolved, and that is the real finding.** Four candidate limbs imply
different molecules, stages and experiments:

| Limb | Engagement | Status |
|---|---|---|
| Hepatic → plasma lipoprotein composition → retina | **Certain** | Live |
| Hepatic → FGF21 → retinal endothelium, luminal side | Certain upstream | Live, **unquantified** |
| Retinal endothelium / RPE transrepression | Marginal | Live |
| Neural retina gene transactivation | **Absent** | Excluded on arithmetic |

**One measurement stands between this target and a decision**, and it has never been made in
any species: **free fibrate concentration in retinal tissue.** Every quantitative claim in
this analysis rests on estimated partition ratios, not measurement.

---

## Benchmark result

**Right drug, right stage, wrong mechanism.**

```
Round 1 (cleanly blinded):   P@1 = 1.00,  first tier-1 hit at rank 1
Phase 3 (NOT cleanly blinded — see below)
```

Fenofibrate is an approved DR therapy in Australia and appears in current ADA guidance. The
pipeline found it blind, and independently matched the label's stage restriction.

It converged on **systemic lipid lowering** as the mechanism. The clinical evidence most
clearly excludes exactly that — benefit does not track lipid change, appears on top of a
statin, and in one trial's renal subgroup appeared with *no lipid change at all*.

**The diagnosis generalises:** evidence grading rewards whichever mechanism has measurable
intermediate steps. Plasma markers are measurable; retinal drug concentration is not, so the
retinal chain can only ever accumulate weak citations *no matter how true it is*. This will
recur for any target behind a barrier.

⚠ **Blinding degraded across phases.** Phase 0 and Round 1 are the clean measurement. The
debate round had one partially contaminated agent, which disclosed and quarantined itself.
**Phase 3 was not cleanly blinded** — three successive leaks of the same class, each created
by the fix for the last. Full accounting in `data-quality-findings.md` §17b, §19.

---

## All files

**Primary output**
- `consensus-report.md` — final ranking, mechanism ranking, combination verdict, next experiments
- `research-program.md` — the experimental agenda
- `BENCHMARK-RESULT.md` — rediscovery scoring and the mechanism post-mortem

**Method and provenance**
- `blinding-protocol.md` — what was redacted and how it was verified
- `data-inventory.md` — what data existed, and what it could not support
- `data-quality-findings.md` — 22 defects, including the orchestrator's own
- `disease-model.md` — the DR pathobiology model all agents worked from (1,555 lines)
- `disease-brief.md` — the brief every agent received

**Phase syntheses**
- `round1-synthesis.md` · `round2-synthesis.md` · `debate-summary.md`
- `round1-score-matrix.txt` · `round2-score-matrix.txt`

**Raw agent reports** — `agents/` (18 files)
⚠ `agents/UNBLINDING-part-b.md` **contains the held-out answer.** Do not read it, or expose
it to any agent, if re-running this benchmark.

**Evidence and scoring**
- `evidence/` — pre-computed interaction tables (note the header warning on the target matrix:
  coverage counts measure study effort, not polypharmacology)
- `scoring/` — predictions and scores for both rounds

---

## Reproducing

```bash
# Rebuild the blinded dataset (regenerable; not committed — 31MB)
python src/holdout/blind_dataset.py --disease diabetic-retinopathy

# Score a ranking against the held-out key
python src/holdout/score_run.py --disease diabetic-retinopathy \
    --predictions <run>/scoring/predictions-final.json
```

Tooling and its caveats: `src/holdout/README.md`.
