"""Put achievable and active FGF21 concentrations on one axis.

Everything here is driven by the values extracted in
``docs/notes/fgf21-concentration-bridge.md``.  Each input value carries a
provenance tag, because the failure this whole chain is correcting is the
conflation of measured, converted and assumed numbers:

    MEASURED   - read directly from a published result
    CONVERTED  - a measured value transformed by stated arithmetic (unit or
                 molar conversion); no new assumption introduced
    ASSUMED    - a distribution chosen to span the published spread; this is the
                 only class that encodes judgement, and every one is justified
                 in the note

Usage:  python -m src.analysis.fgf21_bridge.bridge
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20261103)
N = 200_000

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------
# UniProt Q9NSA1: 209 aa precursor, signal peptide 1-28, mature chain 29-209.
MW_FGF21_DA = 19_500.0  # MEASURED (sequence-derived), mature human FGF21
# PF-05231023: two [dHis/Ala129Cys]FGF21 molecules conjugated to the CovX-2000
# humanised IgG1k scaffold; 2:1 stoichiometry, ~190 kDa total.
MW_PF05231023_DA = 190_000.0  # MEASURED (Pfizer/CovX characterisation)
FGF21_ARMS_PER_CONJUGATE = 2  # MEASURED


def pf_to_fgf21_equiv_ng_ml(pf_ng_ml: float) -> float:
    """ng/mL PF-05231023 -> ng/mL native-FGF21-equivalent.  CONVERTED.

    A ng/mL of a 190 kDa conjugate is NOT a ng/mL of a 19.5 kDa hormone: on a
    mass basis the conjugate is ~90% scaffold.  Comparing the two directly - as
    any reader would who sees "100 ng/mL FGF21" in the retinal papers and
    "600 pg/mL FGF21" in the clinical ones - overstates the retinal dose by
    about 5-fold.  Converting through moles is the only defensible bridge.
    """
    mol_conjugate = pf_ng_ml / MW_PF05231023_DA  # nmol/L
    mol_fgf21 = mol_conjugate * FGF21_ARMS_PER_CONJUGATE
    return mol_fgf21 * MW_FGF21_DA


def nm_to_ng_ml(nm: float) -> float:
    """nM native FGF21 -> ng/mL.  CONVERTED."""
    return nm * MW_FGF21_DA / 1000.0


def _lognormal(median: float, lo95: float, hi95: float, n: int = N) -> np.ndarray:
    """Lognormal pinned to a median and an approximate 95% interval.

    Uses the wider of the two half-intervals on the log scale, so the stated
    uncertainty is never understated by an asymmetric input.
    """
    mu = np.log(median)
    sigma = max(np.log(hi95 / median), np.log(median / lo95)) / 1.96
    return RNG.lognormal(mu, sigma, n)


def run() -> dict:
    # ---- numerator: achievable human plasma FGF21 on a fibrate -----------
    # Baseline in type 2 diabetes with retinopathy.  MEASURED anchors:
    #   Lin 2014 (via PMC5735335): NDR 326.8, NPDR 631.9, PDR 669.4 pg/mL
    #   PMC8016097 (n=654, Abcam ab222506): NDR 326.8+-81.6, NSTDR 572.7+-79.5,
    #                                       STDR 625.8+-83.7 pg/mL
    #   Yokote 2021 (n=1253 hypertriglyceridaemic, 35.8% T2D): baseline ~610
    # ASSUMED distribution: median 550, 95% CI 250-1200 pg/mL.  The interval is
    # deliberately wide enough to absorb the cross-study/cross-kit spread in
    # healthy-control medians (85-232 pg/mL across the kits surveyed) rather
    # than pretending any single cohort is the population.
    baseline = _lognormal(550.0, 250.0, 1200.0)

    # Fibrate-induced fold change.  MEASURED anchors:
    #   Galman 2008   fenofibrate 200 mg, 2 wk          +28%
    #   Christodoulides 2009 GW590735 20 ug/d, 2 wk     +39%
    #   Yokote 2021   pemafibrate 0.4 mg, 12 wk         +369.5 pg/mL on ~610 => +61%
    # ASSUMED: median 1.40, 95% CI 1.25-1.70.
    fold = _lognormal(1.40, 1.25, 1.70)

    # Intact fraction.  MEASURED (Zhen 2016, Biochem J): 10-34% of circulating
    # FGF21 is cleaved after Pro-171 by FAP, and the C-terminus is the
    # beta-Klotho-binding determinant.  ASSUMED uniform over the reported range.
    intact = 1.0 - RNG.uniform(0.10, 0.34, N)

    achievable_total = baseline * fold  # pg/mL
    achievable_intact = achievable_total * intact  # pg/mL

    # ---- denominator: active concentration -------------------------------
    # Anchor A (retinal, the readout the relay actually needs).  MEASURED:
    # Tomita 2020 - HRMEC permeability/TEER protected at 50 and 100 ng/mL
    # PF-05231023.  CONVERTED to FGF21-equivalent below.  No lower
    # concentration was tested, so this is an upper bound on the true
    # threshold, not the threshold itself.
    a_lo = pf_to_fgf21_equiv_ng_ml(50.0) * 1000.0  # pg/mL
    a_hi = pf_to_fgf21_equiv_ng_ml(100.0) * 1000.0  # pg/mL

    # Anchor B (receptor-level, independent of the retina).  MEASURED:
    # EC50 1.16 nM for FGF21-stimulated glucose uptake in human adipocytes -
    # a KLB-rich, maximally FGF21-responsive tissue, so if anything a
    # lower bound on what a KLB-poor tissue needs.
    b = nm_to_ng_ml(1.16) * 1000.0  # pg/mL

    # ASSUMED active-concentration distribution spanning both anchors, with the
    # lower tail extended to 5 ng/mL to allow for the untested sub-50 ng/mL
    # region of the HRMEC dose-response.
    active = _lognormal(15_000.0, 5_000.0, 45_000.0)  # pg/mL

    ratio_total = achievable_total / active
    ratio_intact = achievable_intact / active

    def pct(x):
        return np.percentile(x, [2.5, 50, 97.5])

    return {
        "anchor_A_50ng_pf_as_fgf21_pg_ml": a_lo,
        "anchor_A_100ng_pf_as_fgf21_pg_ml": a_hi,
        "anchor_B_ec50_pg_ml": b,
        "baseline_pg_ml": pct(baseline),
        "achievable_total_pg_ml": pct(achievable_total),
        "achievable_intact_pg_ml": pct(achievable_intact),
        "active_pg_ml": pct(active),
        "ratio_total": pct(ratio_total),
        "ratio_intact": pct(ratio_intact),
        "shortfall_fold_total": pct(1.0 / ratio_total),
        "shortfall_fold_intact": pct(1.0 / ratio_intact),
        "p_ratio_ge_1": float((ratio_intact >= 1).mean()),
        "p_ratio_ge_0.1": float((ratio_intact >= 0.1).mean()),
        "log10_shortfall_intact": pct(np.log10(1.0 / ratio_intact)),
    }


def main() -> int:
    r = run()
    print("FGF21 CONCENTRATION BRIDGE")
    print("=" * 64)
    print(
        f"Anchor A  50 ng/mL PF-05231023 = {r['anchor_A_50ng_pf_as_fgf21_pg_ml']:10,.0f} pg/mL FGF21-eq"
    )
    print(
        f"Anchor A 100 ng/mL PF-05231023 = {r['anchor_A_100ng_pf_as_fgf21_pg_ml']:10,.0f} pg/mL FGF21-eq"
    )
    print(f"Anchor B EC50 1.16 nM FGF21    = {r['anchor_B_ec50_pg_ml']:10,.0f} pg/mL")
    print()
    for k in (
        "baseline_pg_ml",
        "achievable_total_pg_ml",
        "achievable_intact_pg_ml",
        "active_pg_ml",
    ):
        lo, md, hi = r[k]
        print(f"{k:28s} {md:10,.0f}  [{lo:,.0f} - {hi:,.0f}] pg/mL")
    print()
    for k in ("ratio_total", "ratio_intact"):
        lo, md, hi = r[k]
        print(f"{k:28s} {md:10.4f}  [{lo:.4f} - {hi:.4f}]")
    for k in ("shortfall_fold_total", "shortfall_fold_intact"):
        lo, md, hi = r[k]
        print(f"{k:28s} {md:10.1f}x [{lo:.1f}x - {hi:.1f}x]")
    lo, md, hi = r["log10_shortfall_intact"]
    print(f"{'log10 shortfall (intact)':28s} {md:10.2f}  [{lo:.2f} - {hi:.2f}]")
    print()
    print(f"P(achievable >= active)        = {r['p_ratio_ge_1']:.4f}")
    print(f"P(achievable >= 10% of active) = {r['p_ratio_ge_0.1']:.4f}")
    print()
    print("CALIBRATION")
    print("=" * 64)
    calibration()
    return 0


# --------------------------------------------------------------------------
# Calibration and sensitivity, appended for the note
# --------------------------------------------------------------------------
def calibration() -> None:
    """Three checks that the denominator is not an artefact of my arithmetic."""
    r = run()
    lo, md, hi = r["active_pg_ml"]
    # 1. Clinically achieved FGF21-analog exposures (Yokote 2021 citing the
    #    analog trials): 17.5-150 ng/mL = 17,500-150,000 pg/mL.  A drug is
    #    normally dosed just above its active concentration, so the modelled
    #    active range should sit at or just below the bottom of that band.
    print(f"modelled active        : {md:,.0f} pg/mL [{lo:,.0f} - {hi:,.0f}]")
    print(f"analog trial exposures : 17,500 - 150,000 pg/mL")
    print(
        f"  -> modelled active is {17_500/md:.1f}x below the bottom of the "
        f"clinically dosed band (expected: slightly below)"
    )

    # 2. What fold-rise over a T2D baseline would a fibrate need?
    base = 550.0
    need = md / base
    print(
        f"\nfold-rise needed over {base:.0f} pg/mL baseline to reach active: "
        f"{need:.0f}x"
    )
    print(
        f"fold-rise a fibrate delivers                                : "
        f"1.28 - 1.61x"
    )
    print(f"  -> gap in required fold-rise: {need/1.61:.0f}x to {need/1.28:.0f}x")

    # 3. Endogenous FGF21 relative to its own EC50 - the context that stops
    #    the shortfall being read as "FGF21 does nothing at 550 pg/mL".
    ec50 = nm_to_ng_ml(1.16) * 1000.0
    print(
        f"\nendogenous T2D plasma / adipocyte EC50 = {base/ec50:.4f} "
        f"({ec50/base:.0f}x below EC50)"
    )
    print("  -> endogenous FGF21 already sits ~40x below its own in-vitro EC50,")
    print("     so the in-vitro EC50 is an imperfect yardstick; this is why the")
    print("     retinal anchor (PF-05231023 in HRMECs) carries the argument.")


if __name__ == "__main__":
    raise SystemExit(main())
