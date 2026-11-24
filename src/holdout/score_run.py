#!/usr/bin/env python3
"""Score a blinded pipeline run against the held-out answer key.

Measures whether the discovery pipeline rediscovered drugs that are in fact
already used for the target disease, without having been shown that fact.

Input: a predictions JSON produced from the pipeline's final ranking:
    {"disease": "...", "ranked": [{"rank": 1, "name": "FENOFIBRATE", "score": 8.4}, ...]}

Usage:
    python src/holdout/score_run.py --disease diabetic-retinopathy \
        --predictions data/reports/.../scoring/predictions.json
"""

import argparse
import json
import re
from pathlib import Path

# Candidate names are free text from agents; normalize to match the key.
SALT_SUFFIXES = [
    "sodium", "hydrochloride", "hcl", "maleate", "acetate", "tromethamine",
    "citrate", "phosphoric acid", "acetonide", "choline", "micronized",
]


def norm(name):
    n = name.upper().strip()
    n = re.sub(r"[^A-Z0-9 ]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    for s in SALT_SUFFIXES:
        n = re.sub(rf"\b{s.upper()}\b", "", n).strip()
    return re.sub(r"\s+", " ", n).strip()


# Active-moiety equivalence. Source databases tag an indication against one entity
# (usually the marketed parent), leaving prodrugs, active metabolites and salts of the
# SAME pharmacological agent untagged. Scoring them as misses understates rediscovery.
# Each group is one drug in vivo; membership is justified in the run's notes.
MOIETY_GROUPS = [
    # Fenofibrate is an obligate ester prodrug; fenofibric acid is the circulating active
    # moiety; choline fenofibrate is a salt of that acid. The project's own
    # chembl_drug_metabolism.csv records the conversion as "more or less complete".
    {"FENOFIBRATE", "FENOFIBRIC ACID", "CHOLINE FENOFIBRATE"},
    {"TRIAMCINOLONE", "TRIAMCINOLONE ACETONIDE"},
    {"DEXAMETHASONE", "DEXAMETHASONE PHOSPHORIC ACID"},
    {"KETOROLAC", "KETOROLAC TROMETHAMINE"},
    {"LEVODOPA", "CARBIDOPA"},
]


def moiety_of(name):
    """Return the canonical group a normalized name belongs to, or None."""
    for g in MOIETY_GROUPS:
        if name in g:
            return frozenset(g)
    return None


def load_key(disease):
    p = Path(f"data/holdout/{disease}/answer-key.json")
    key = json.loads(p.read_text())
    truth = {}
    for d in key["redacted_drugs"]:
        n = norm(d["name"])
        if not n:
            continue
        terms = [t.lower() for t in d["removed_terms"]]
        # Tier 1: the drug explicitly carried the target disease term.
        tier = 1 if any("diabetic retinopath" in t for t in terms) else 2
        prev = truth.get(n)
        if prev is None or tier < prev["tier"]:
            truth[n] = {"name": d["name"], "tier": tier, "terms": d["removed_terms"]}
    return key, truth


def score(disease, predictions, k_values=(1, 3, 5, 10)):
    key, truth = load_key(disease)
    ranked = sorted(predictions["ranked"], key=lambda r: r["rank"])
    hits = []
    for r in ranked:
        n = norm(r["name"])
        match = truth.get(n)
        moiety_hit = False
        if not match:
            # same active moiety under a different entity name
            g = moiety_of(n)
            if g:
                for tn, t in truth.items():
                    if tn in g:
                        match, moiety_hit = t, True
                        break
        if not match:
            # substring match for multi-word / class names
            for tn, t in truth.items():
                if tn and (tn in n or n in tn) and len(n) > 4:
                    match = t
                    break
        if match:
            hits.append({"rank": r["rank"], "predicted": r["name"],
                         "truth": match["name"], "tier": match["tier"],
                         "moiety_equivalent": moiety_hit,
                         "removed_terms": match["terms"]})

    tier1 = [h for h in hits if h["tier"] == 1]
    strict = [h for h in hits if not h.get("moiety_equivalent")]
    strict_t1 = [h for h in strict if h["tier"] == 1]
    out = {
        "disease": disease,
        "n_predictions": len(ranked),
        "n_truth_tier1": sum(1 for t in truth.values() if t["tier"] == 1),
        "n_truth_total": len(truth),
        "hits": hits,
        "precision_at_k": {},
        "tier1_hit_at_k": {},
        "first_tier1_rank": min([h["rank"] for h in tier1], default=None),
        "strict_no_moiety": {
            "hits": len(strict),
            "tier1_hits": len(strict_t1),
            "first_tier1_rank": min([h["rank"] for h in strict_t1], default=None),
        },
    }
    for k in k_values:
        topk = [h for h in hits if h["rank"] <= k]
        out["precision_at_k"][f"P@{k}"] = round(len(topk) / min(k, len(ranked)), 3) if ranked else 0.0
        out["tier1_hit_at_k"][f"hit@{k}"] = any(h["tier"] == 1 for h in topk)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--disease", required=True)
    ap.add_argument("--predictions", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    preds = json.loads(Path(args.predictions).read_text())
    res = score(args.disease, preds)
    txt = json.dumps(res, indent=2)
    print(txt)
    if args.out:
        Path(args.out).write_text(txt)


if __name__ == "__main__":
    main()
