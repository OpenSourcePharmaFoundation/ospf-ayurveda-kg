#!/usr/bin/env python3
"""Tabulate a disease-explorer round's agent scores into a comparison matrix.

Agents append a `## SCOREBLOCK` section to their report containing lines of:
    SCORE|<name>|<score>|<confidence>|<evidence_basis>|<reason>

This reads every report in a round, builds the candidate x agent matrix, and
reports spread — the disagreements are the point, so they are surfaced, not averaged away.

Usage:
    python src/holdout/tabulate_round.py --dir <run>/agents --pattern 'p1-*.md'
"""

import argparse
import glob
import os
import re
import statistics


def parse(path):
    txt = open(path).read()
    m = re.search(r"^## SCOREBLOCK\s*$(.*)", txt, re.M | re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        line = line.strip().strip("`")
        if not line.startswith("SCORE|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        _, name, score, conf, basis = parts[:5]
        reason = parts[5] if len(parts) > 5 else ""
        val = None if score.upper() in ("NA", "N/A", "") else float(score)
        out[name] = {"score": val, "conf": conf, "basis": basis, "reason": reason}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--pattern", default="p1-*.md")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.dir, args.pattern)))
    data = {}
    for f in files:
        agent = os.path.basename(f).replace(".md", "")
        d = parse(f)
        if d:
            data[agent] = d

    agents = list(data.keys())
    names = []
    for d in data.values():
        for n in d:
            if n not in names:
                names.append(n)

    rows = []
    for n in names:
        vals = [data[a][n]["score"] for a in agents if n in data[a] and data[a][n]["score"] is not None]
        nas = [a for a in agents if n in data[a] and data[a][n]["score"] is None]
        rows.append({
            "name": n,
            "scores": {a: (data[a][n]["score"] if n in data[a] else None) for a in agents},
            "mean": round(statistics.mean(vals), 2) if vals else None,
            "min": min(vals) if vals else None,
            "max": max(vals) if vals else None,
            "spread": round(max(vals) - min(vals), 1) if len(vals) > 1 else 0,
            "n": len(vals),
            "na_agents": nas,
        })
    rows.sort(key=lambda r: (r["mean"] is None, -(r["mean"] or 0)))

    short = {a: a.split("-", 1)[1][:8] for a in agents}
    w = max(len(r["name"]) for r in rows) + 1
    hdr = f"{'candidate':<{w}} " + " ".join(f"{short[a]:>8}" for a in agents) + f" {'mean':>6} {'spread':>7} {'n':>3}"
    lines = [hdr, "-" * len(hdr)]
    for r in rows:
        cells = " ".join(
            (f"{r['scores'][a]:>8.1f}" if r["scores"][a] is not None else f"{('NA' if a in r['na_agents'] else '-'):>8}")
            for a in agents
        )
        lines.append(f"{r['name']:<{w}} {cells} {(r['mean'] if r['mean'] is not None else 0):>6.2f} {r['spread']:>7.1f} {r['n']:>3}")

    lines.append("")
    lines.append("LARGEST DISAGREEMENTS (spread >= 3.0) — these drive the debate round:")
    for r in sorted(rows, key=lambda x: -x["spread"]):
        if r["spread"] >= 3.0:
            hi = max((a for a in agents if r["scores"][a] is not None), key=lambda a: r["scores"][a])
            lo = min((a for a in agents if r["scores"][a] is not None), key=lambda a: r["scores"][a])
            lines.append(f"  {r['name']:<24} spread {r['spread']:>4.1f}  {short[hi]} {r['scores'][hi]:.1f} vs {short[lo]} {r['scores'][lo]:.1f}")

    txt = "\n".join(lines)
    print(txt)
    if args.out:
        open(args.out, "w").write(txt + "\n")


if __name__ == "__main__":
    main()
