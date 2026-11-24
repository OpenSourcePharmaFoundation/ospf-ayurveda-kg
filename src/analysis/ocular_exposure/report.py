"""Run the model and print every table that goes into the note.

    venv/bin/python -m src.analysis.ocular_exposure.report
    venv/bin/python -m src.analysis.ocular_exposure.report --quick

Nothing in ``docs/notes/retinal-exposure-model.md`` is typed by hand: the
numbers there are this script's output, so a disagreement between the note and
the model is a reproducible failure rather than a transcription argument.
"""

from __future__ import annotations

import argparse
import textwrap

import numpy as np

from . import model, parameters, potency, sensitivity
from .compounds import COMPOUNDS, FENOFIBRIC_ACID, SELADELPAR


def _fmt(x: float) -> str:
    if x == 0 or not np.isfinite(x):
        return "-"
    a = abs(x)
    if a >= 1000 or a < 0.01:
        return f"{x:.2e}"
    if a >= 10:
        return f"{x:.1f}"
    return f"{x:.3g}"


def _table(rows, headers):
    w = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    line = "| " + " | ".join(str(headers[i]).ljust(w[i]) for i in range(len(w))) + " |"
    sep = "|" + "|".join("-" * (w[i] + 2) for i in range(len(w))) + "|"
    body = [
        "| " + " | ".join(str(r[i]).ljust(w[i]) for i in range(len(w))) + " |"
        for r in rows
    ]
    return "\n".join([line, sep] + body)


def targets():
    """(compound, gene) pairs to evaluate.

    Seladelpar appears twice: the DR analysis cares about PPARalpha, but
    seladelpar is a PPARdelta agonist and reporting only its PPARalpha margin
    would judge it on a receptor it was not built for.
    """
    out = [(c, c.ec50_gene) for c in COMPOUNDS]
    out.append((SELADELPAR, "PPARA"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200_000)
    ap.add_argument("--sobol-n", type=int, default=32_768)
    ap.add_argument("--quick", action="store_true", help="small n, for a smoke test")
    args = ap.parse_args()
    n = 20_000 if args.quick else args.n
    sn = 4_096 if args.quick else args.sobol_n

    print("=" * 78)
    print("PARAMETER TABLE")
    print("=" * 78)
    for label, group in (
        ("anchor", parameters.ANCHOR),
        ("barrier", parameters.BARRIER),
        ("assay", parameters.ASSAY),
    ):
        print(f"\n--- {label} ---")
        print(
            _table(
                [list(r) for r in parameters.table(group)],
                ["parameter", "value [95% CI]", "units", "provenance", "source"],
            )
        )

    print("\n--- compound PK and physicochemistry ---")
    rows = []
    for c in COMPOUNDS:
        rows.append(
            [
                c.name,
                c.chembl,
                f"{c.mw:.2f}",
                f"{c.logp:.2f}",
                c.pka.summary(),
                f"{c.dose_mg:g}",
                c.c_avg.summary(),
                c.fu_plasma.summary(),
                c.fu_plasma.provenance,
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "chembl",
                "MW",
                "logP",
                "pKa",
                "mg/day",
                "Cavg,ss ng/mL [95% CI]",
                "fu",
                "fu source",
            ],
        )
    )

    # ---- ionisation -------------------------------------------------------
    from . import ionisation

    print("\n--- ionisation at pH 7.4 (median pKa) ---")
    rows = []
    for c in COMPOUNDS:
        pka = (c.pka.a + c.pka.b) / 2.0
        fn = float(ionisation.fraction_neutral(pka, 7.4))
        rows.append(
            [
                c.name,
                f"{pka:.2f}",
                f"{c.logp:.2f}",
                f"{float(ionisation.log_d(c.logp, pka, 7.4)):+.2f}",
                f"{fn:.2e}",
                f"{float(ionisation.ph_partition(pka, 7.1, 7.4)):.2f}",
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "pKa",
                "logP",
                "logD(7.4)",
                "neutral fraction",
                "cytosol/plasma free (pH 7.1 vs 7.4)",
            ],
        )
    )

    # ---- potency ----------------------------------------------------------
    print(
        "\n--- measured EC50 (ChEMBL, data/processed/chembl_panel_bioactivities.csv) ---"
    )
    pots = {}
    rows = []
    for c, gene in targets():
        p = potency.load(c.chembl, gene)
        pots[(c.key, gene)] = p
        lo, hi = p.ci95()
        rows.append(
            [
                c.name,
                gene,
                p.n_determinations,
                _fmt(p.median_nM),
                f"{_fmt(lo)} - {_fmt(hi)}",
                f"{p.gsd:.2f}",
                ", ".join(_fmt(v) for v in p.censored_nM) or "-",
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "receptor",
                "n(=)",
                "median EC50 nM",
                "95% CI",
                "GSD",
                "censored (>) nM",
            ],
        )
    )

    # ---- the calibrated anchor -------------------------------------------
    rng = np.random.default_rng(20261109)
    u = rng.random((n, model.N_INPUTS))
    from . import barrier

    kp = barrier.kpuu_neural_retina_reference(model._anchor_draws(u))
    q = model.quantiles(kp)
    print("\n--- calibrated neural-retina Kp,uu (fenofibric acid, mouse anchor) ---")
    print(f"  Kp,uu = {q[1]:.4f}  [95% CI {q[0]:.4f} - {q[2]:.4f}]")
    print(
        f"  exclusion factor 1/Kp,uu = {1/q[1]:.1f}x  [{1/q[2]:.1f}x - {1/q[0]:.1f}x]"
    )
    print("  (DR analysis asserted 0.01-0.15 for neural retina, by argument)")

    # ---- independent calibration against measured ocular partition --------
    from . import anchors

    print(
        "\n--- external anchor: measured human aqueous-humour partition after oral dosing ---"
    )
    print(
        _table(
            anchors.table(),
            [
                "drug",
                "charge",
                "aqueous/plasma (total)",
                "fu plasma",
                "Kp,uu (free/free)",
                "source",
            ],
        )
    )
    print("\n  " + "\n  ".join(textwrap.wrap(anchors.EFFLUX_ANCHOR, 100)))

    # ---- margins ----------------------------------------------------------
    for exposure in ("c_avg", "c_max"):
        print("\n" + "=" * 78)
        print(f"FREE-DRUG MARGINS  (exposure = {exposure})")
        print("=" * 78)
        rows = []
        for c, gene in targets():
            p = pots[(c.key, gene)]
            r = model.evaluate(u, c, p, exposure)
            cu = model.quantiles(r.cu_plasma_nM)
            ec = model.quantiles(r.ec50_free_nM)
            row = [c.name, gene, f"{_fmt(cu[1])}", f"{_fmt(ec[1])}"]
            for k in model.COMPARTMENTS:
                m = model.quantiles(r.margins[k])
                row.append(f"{_fmt(m[1])} [{_fmt(m[0])}-{_fmt(m[2])}]")
            for k in model.COMPARTMENTS:
                row.append(f"{float(np.mean(r.margins[k] >= 1.0)):.3f}")
            rows.append(row)
        print(
            _table(
                rows,
                [
                    "compound",
                    "receptor",
                    "Cu plasma nM",
                    "free EC50 nM",
                    "margin endothelium",
                    "margin RPE",
                    "margin neural retina",
                    "P(endo>=1)",
                    "P(RPE>=1)",
                    "P(NR>=1)",
                ],
            )
        )

    # ---- the double-counting correction ----------------------------------
    print("\n--- size of the serum correction on EC50 (the double-counted log) ---")
    rows = []
    for c, gene in targets():
        p = pots[(c.key, gene)]
        r = model.evaluate(u, c, p, "c_avg")
        ratio = r.ec50_nominal_nM / r.ec50_free_nM
        q2 = model.quantiles(ratio)
        rows.append(
            [
                c.name,
                gene,
                f"{q2[1]:.1f}x",
                f"{q2[0]:.1f}x - {q2[2]:.1f}x",
                f"{np.log10(q2[1]):.2f} log",
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "receptor",
                "median overstatement",
                "95% CI",
                "median in logs",
            ],
        )
    )

    # ---- why the unmeasured free fraction turns out not to matter ---------
    #
    # Once the EC50 is corrected for the protein binding that was present in
    # its own assay, fu appears on both sides of the comparison and nearly
    # cancels: margin is proportional to fu / fu_assay, and for small fu that
    # is approximately (fu + s) where s is the assay's albumin fraction.  So
    # the parameter with no published measurement -- pemafibrate's plasma
    # protein binding -- barely moves the answer.  The converse is the real
    # warning: comparing free drug against an UNCORRECTED nominal EC50 makes
    # the margin scale directly with fu, so that analysis is dominated by the
    # parameter that should be nearly irrelevant.
    print("\n--- robustness: margin vs the free fraction, all else at its median ---")
    rows = []
    for c, gene in targets():
        p = pots[(c.key, gene)]
        vals = []
        for q in (0.001, 0.999):
            uu = np.full((1, model.N_INPUTS), 0.5)
            uu[0, model.IDX["compound.fu_plasma"]] = q
            vals.append(
                float(model.evaluate(uu, c, p, "c_avg").margins["endothelium"][0])
            )
        fu_lo = float(c.fu_plasma.ppf(np.array([0.001]))[0])
        fu_hi = float(c.fu_plasma.ppf(np.array([0.999]))[0])
        rows.append(
            [
                c.name,
                gene,
                f"{fu_lo:.5f} - {fu_hi:.5f}",
                f"{fu_hi/fu_lo:.1f}x",
                f"{_fmt(vals[0])} - {_fmt(vals[1])}",
                f"{vals[1]/vals[0]:.1f}x",
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "receptor",
                "fu range spanned",
                "fu fold-range",
                "margin range",
                "margin fold-range",
            ],
        )
    )
    print("  A 9-20x swing in fu moves the margin by 2-3x, because the corrected")
    print("  EC50 carries the same binding term.  Without the correction the")
    print("  margin would move by the full fu fold-range.")

    # ---- what dose would be needed ---------------------------------------
    print("\n--- dose multiple required for margin = 1 at the endothelium ---")
    rows = []
    for c, gene in targets():
        p = pots[(c.key, gene)]
        r = model.evaluate(u, c, p, "c_avg")
        need = 1.0 / r.margins["endothelium"]
        q3 = model.quantiles(need)
        rows.append(
            [
                c.name,
                gene,
                f"{c.dose_mg:g} mg/d",
                f"{_fmt(q3[1])}x",
                f"{_fmt(q3[0])}x - {_fmt(q3[2])}x",
            ]
        )
    print(
        _table(
            rows,
            [
                "compound",
                "receptor",
                "labelled dose",
                "median fold increase needed",
                "95% CI",
            ],
        )
    )

    # ---- the calibration that decides whether the model is trustworthy ----
    #
    # Fenofibrate at 200 mg/day demonstrably activates hepatic PPARalpha:
    # triglycerides fall 30-50%.  So a model that says free plasma drug sits
    # far below the free EC50 has to explain how the liver manages it.  Run
    # backwards, the model states the hepatic concentration factor the
    # observed effect REQUIRES.  If that number is implausible, the model is
    # wrong; if it lands in the measured range for OATP1B substrates and
    # orders the four compounds by their known hepatoselectivity, it is not.
    print("\n" + "=" * 78)
    print(
        "CALIBRATION: hepatic concentration factor the known clinical effect requires"
    )
    print("=" * 78)
    rows = []
    for c, gene in targets():
        p = pots[(c.key, gene)]
        r = model.evaluate(u, c, p, "c_avg")
        need = r.ec50_free_nM / r.cu_plasma_nM
        q4 = model.quantiles(need)
        rows.append(
            [c.name, gene, f"{_fmt(q4[1])}x", f"{_fmt(q4[0])}x - {_fmt(q4[2])}x"]
        )
    print(_table(rows, ["compound", "receptor", "required liver Kp,uu", "95% CI"]))
    print("  Measured Kp,uu(liver) for OATP1B substrate acids is ~10-100x.")
    print("  SLCO1B1: liver 502.3 nTPM, retina 0.0 nTPM (9th pctile).")
    print("  SLCO1B3: liver 247.7 nTPM, retina 0.0 nTPM (9th pctile).")
    print("  (data/processed/retina_hpa_bulk_ntpm.tsv, regenerated this step)")

    # ---- elafibranor + its active metabolite, combined --------------------
    print("\n--- elafibranor: parent + GFT1007 combined PPARalpha drive ---")
    from .compounds import ELAFIBRANOR, GFT1007

    pe = pots[(ELAFIBRANOR.key, "PPARA")]
    pg = pots[(GFT1007.key, "PPARA")]
    rows = []
    for exposure in ("c_avg", "c_max"):
        re_ = model.evaluate(u, ELAFIBRANOR, pe, exposure)
        rg = model.evaluate(u, GFT1007, pg, exposure)
        for k in model.COMPARTMENTS:
            tot = re_.margins[k] + rg.margins[k]  # equipotent: additive in margin units
            q5 = model.quantiles(tot)
            rows.append(
                [
                    exposure,
                    k,
                    f"{_fmt(q5[1])}",
                    f"{_fmt(q5[0])} - {_fmt(q5[2])}",
                    f"{float(np.mean(tot >= 1.0)):.3f}",
                ]
            )
    print(
        _table(rows, ["exposure", "compartment", "combined margin", "95% CI", "P(>=1)"])
    )
    print("  (GFT1007 assumed equipotent with the parent: its own EC50 is not")
    print("   separately determined in the ChEMBL record, so this is an upper")
    print("   bound on the combined drive if the metabolite is weaker.)")

    # ---- sensitivity ------------------------------------------------------
    print("\n" + "=" * 78)
    print(f"SENSITIVITY: Sobol indices on log10(margin), n = {sn}")
    print("=" * 78)
    for compartment in ("neural_retina", "endothelium"):
        print(f"\n--- compartment: {compartment} ---")
        per = {}
        for c, gene in targets():
            per[f"{c.key}/{gene}"] = sensitivity.sobol(
                c, pots[(c.key, gene)], compartment, n=sn
            )
        pooled = sensitivity.pooled(per)
        rows = []
        for name, st in sorted(pooled.items(), key=lambda kv: -kv[1]):
            if st < 0.005:
                continue
            s1s = [per[kk][name][0] for kk in per]
            rows.append([name, f"{float(np.mean(s1s)):.3f}", f"{st:.3f}"])
        print(_table(rows, ["input", "mean S1", "mean ST"]))
        print(
            f"  (inputs with mean ST < 0.005 omitted; "
            f"sum of mean ST = {sum(pooled.values()):.2f})"
        )

    # ---- grouped sensitivity: the decision-relevant decomposition ---------
    #
    # A per-input ranking makes the barrier look unimportant purely because
    # its uncertainty is spread over eighteen parameters while potency sits in
    # one.  The question being asked -- where should measurement effort go --
    # is a question about blocks, so the blocks are indexed as units.
    print("\n" + "=" * 78)
    print(f"SENSITIVITY, GROUPED: Sobol indices on log10(margin), n = {sn}")
    print("=" * 78)
    for compartment in ("neural_retina", "endothelium"):
        print(f"\n--- compartment: {compartment} ---")
        rows = []
        acc: dict[str, list[float]] = {}
        for c, gene in targets():
            g = sensitivity.sobol_groups(c, pots[(c.key, gene)], compartment, n=sn)
            for label, (s1, st) in g.items():
                acc.setdefault(label, []).append(st)
        for label, sts in sorted(acc.items(), key=lambda kv: -float(np.mean(kv[1]))):
            rows.append(
                [
                    label,
                    f"{float(np.mean(sts)):.3f}",
                    f"{min(sts):.3f} - {max(sts):.3f}",
                ]
            )
        print(_table(rows, ["input block", "mean ST", "range across compounds"]))

    # ---- machine-readable output for the next step ------------------------
    import csv
    import pathlib

    out = pathlib.Path(__file__).resolve().parents[3] / "data" / "processed"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "ocular_exposure_margins.tsv"
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "compound",
                "chembl_id",
                "receptor",
                "exposure",
                "compartment",
                "cu_plasma_nM_median",
                "ec50_free_nM_median",
                "margin_median",
                "margin_lo95",
                "margin_hi95",
                "p_margin_ge_1",
                "kpuu_median",
            ]
        )
        for exposure in ("c_avg", "c_max"):
            for c, gene in targets():
                r = model.evaluate(u, c, pots[(c.key, gene)], exposure)
                cu = model.quantiles(r.cu_plasma_nM)[1]
                ec = model.quantiles(r.ec50_free_nM)[1]
                kp = model.quantiles(r.kpuu_neural_retina)[1]
                for k in model.COMPARTMENTS:
                    m = model.quantiles(r.margins[k])
                    w.writerow(
                        [
                            c.name,
                            c.chembl,
                            gene,
                            exposure,
                            k,
                            f"{cu:.6g}",
                            f"{ec:.6g}",
                            f"{m[1]:.6g}",
                            f"{m[0]:.6g}",
                            f"{m[2]:.6g}",
                            f"{float(np.mean(r.margins[k] >= 1.0)):.4f}",
                            f"{kp:.6g}",
                        ]
                    )
    print(f"\n[ok] {path}")

    # ---- a per-compound view of the top driver ----------------------------
    print("\n--- top driver per compound, neural retina ---")
    rows = []
    for c, gene in targets():
        idx = sensitivity.sobol(c, pots[(c.key, gene)], "neural_retina", n=sn)
        top = sensitivity.ranked(idx)[:3]
        rows.append([c.name, gene] + [f"{nm} ({v[1]:.2f})" for nm, v in top])
    print(_table(rows, ["compound", "receptor", "1st", "2nd", "3rd"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
