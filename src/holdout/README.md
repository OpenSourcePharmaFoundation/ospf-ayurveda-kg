# holdout — held-out benchmark tooling

Supports blinded evaluation runs of the discovery pipeline: remove the answer
from the dataset, run the pipeline, then score what it rediscovered.

## Modules

- `blind_dataset.py` — builds `data/processed-blinded-<disease>/`, a full copy of
  `data/processed/` with disease-revealing indication terms redacted, plus an
  answer key at `data/holdout/<disease>/answer-key.json`. Verifies zero residual
  matches before returning. The source tree is never mutated.
- `score_run.py` — compares a pipeline's final ranking against the answer key and
  reports precision@k and the rank at which the first known therapy appears.

## Adding a disease

Add a pattern list to `HOLDOUT_PATTERNS` in `blind_dataset.py`. Patterns should
cover the disease, its synonyms, and closely-related conditions whose drug classes
would give the answer away — but NOT upstream/background conditions, which are
legitimate context rather than leakage.

## Caveat

Blinding removes the dataset signal only. It does not remove what a language model
already knows from pretraining. Pair it with a behavioral instruction to agents and
report both layers honestly.

## Writing patterns: beware naive substrings

Patterns are matched case-insensitively against semicolon-delimited indication terms.
Anchor them on distinctive stems. A bare drug-class substring will false-positive on
unrelated words — `statin` matches both `somatostatin` and `stating`. The current
diabetic-retinopathy set anchors on `retinopath`, `macular edema` and similar, which
are not susceptible. If a future disease needs a short or common stem, use a word
boundary (`\bstatin\b`) and adjudicate the verifier's hits by hand before trusting a
zero-leak result.

## Keep held-out content in its own file

Do not place an answer key, an unblinding section, or any held-out material after a marker
inside a file that blinded agents are instructed to read. Content hidden behind an in-file
boundary is still exposed by every structural operation: heading grep, table of contents,
outline view, editor symbol list, or a summariser's first pass. A blinded agent in this
project's diabetic-retinopathy run received two substantive section headings this way while
legitimately trying to find where its permitted reading ended.

Put held-out content in a separate file with a do-not-read banner, and let the filesystem
enforce the boundary rather than an instruction.

## Never describe held-out content in an incident report

If a blinding breach occurs, the write-up records *that* it happened, its mechanism, and its
scope — never what was disclosed. In this project's diabetic-retinopathy run, documenting a
leaked section heading reproduced its content inside the defect log, and the defect log was a
required read for the agent producing the final ranking. The record of the leak reached more
agents than the leak did.

Three leaks of this class occurred in one run: a redaction marker, an in-file section
boundary, and the incident report itself. Each fix created the next. The invariant to hold is
that **no file a blinded agent is required to read may contain held-out content, a description
of it, or a pointer precise enough to reconstruct it.**
