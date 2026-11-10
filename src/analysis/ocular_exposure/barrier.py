"""The compartment model.

Three compartments, and the first point of the model is that they are not
three draws from one range -- they sit behind structurally different numbers
of barriers, and two of them sit behind none.

**Retinal vascular endothelium.**  This cell *is* the inner blood-retinal
barrier.  Its luminal membrane faces plasma directly; there is no barrier
between plasma and that membrane.  So its free exposure is the free plasma
concentration, reduced only by whatever its own ATP-driven pumps push back
into the lumen.  The DR analysis assigned it a partition ratio of 0.2-0.7 as
though it were behind the barrier.  The ceiling is 1.0, not 0.7, and the
reason the number is below 1 is efflux, not partition.

**Retinal pigment epithelium.**  Faces the choriocapillaris, which is
fenestrated: choroidal interstitial free concentration is plasma free
concentration.  The RPE is likewise one membrane from the blood side.  It is
also the one compartment here that can *exceed* plasma free concentration,
because human RPE expresses the concentrative organic-anion uptake
transporters OAT3 (SLC22A8, 465 nCPM) and OAT1 (SLC22A6, 64 nCPM) alongside
the efflux pump ABCC5 (823 nCPM) -- all measured, in
``data/processed/retina_hpa_celltype_ncpm.tsv``.  An anionic drug facing a
tissue with OAT uptake can be concentrated, not excluded.  Net direction is
unmeasured, so the prior spans both sides of unity.

**Neural retina.**  The only compartment genuinely behind a tight junction,
on both sides: the endothelial junctions of the inner BRB and the RPE
junctions of the outer BRB.  Its steady-state free ratio is a competition
between clearances,

    Kp,uu = PS_passive / (PS_passive + CL_efflux + CL_bulk)

which is the form that matters, because it says low permeability on its own
does not lower the plateau -- it only lowers it in competition with a route
out that is not the way in.  For these compounds that route exists: the human
retinal endothelium expresses ABCB1 at 507 nCPM, ABCC4 at 178 and ABCG2 at
142, each above its hepatocyte value.

Calibration.  ``Kp,uu`` for the neural retina is not asserted.  It is solved
from the one measurement of any fibrate in ocular tissue after systemic
dosing in any species -- Huang 2021, mouse, fenofibrate 2 mg/kg/day IP --
and then transferred to the other compounds on relative passive permeability
and relative efflux liability.
"""

from __future__ import annotations

import numpy as np

from . import ionisation


def kpuu_neural_retina_reference(a: dict) -> np.ndarray:
    """Solve Kp,uu for the mouse neural retina from the Huang 2021 anchor.

    The measured sample is **pooled vitreous + retina**, reported per mg of
    total protein.  Vitreous carries drug but essentially no protein, so it
    adds to the numerator and not the denominator: treating the pooled figure
    as a retinal tissue concentration overstates retinal exposure.  The
    inversion below keeps the two phases separate.

    For a pooled sample of retinal protein mass ``P`` holding retinal volume
    ``V_ret`` and vitreous volume ``V_vit``, with free concentration ``Cu``
    common to both at equilibrium and retinal tissue binding ``fu_ret``:

        M [ng/mg protein] = (Cu * V_vit + (Cu / fu_ret) * V_ret) / P

    so

        Cu,retina = M * P / (V_vit + V_ret / fu_ret)

    and on the plasma side, where the same per-protein convention applies,

        Cu,plasma = M_plasma * [plasma protein] * fu_plasma

    ``a`` holds one sampled array per anchor parameter.
    """
    cu_retina = (a["retina_ffa"] * a["retina_protein_mg"]) / (
        a["vitreous_vol_ul"] + a["retina_vol_ul"] / a["fu_tissue_retina"]
    )  # ng/µL == µg/mL
    cu_plasma = (
        a["plasma_ffa"] * a["plasma_protein_mouse"] * a["fu_plasma_mouse_ffa"]
    ) / 1000.0  # ng/mg * mg/mL = ng/mL -> µg/mL

    kpuu = cu_retina / cu_plasma
    # A single late time point on a falling plasma curve is not a steady-state
    # ratio; for a slowly-equilibrating tissue it reads high.
    return np.clip(kpuu / a["late_sample_bias"], 1e-6, 1.0)


def relative_permeability(
    cmp_logp, cmp_pka, cmp_mw, ref_logp, ref_pka, ref_mw, logd_slope, mw_slope
) -> np.ndarray:
    """Passive permeability of a compound relative to the reference.

    Only the neutral species crosses, so the driver is logD(7.4), not logP.
    The slope of log permeability on logD is below 1 in this lipophilicity
    range and is carried as an uncertainty, as is the size penalty.
    """
    d_cmp = ionisation.log_d(cmp_logp, cmp_pka, 7.4)
    d_ref = ionisation.log_d(ref_logp, ref_pka, 7.4)
    log_r = logd_slope * (d_cmp - d_ref) - mw_slope * (cmp_mw - ref_mw)
    return np.power(10.0, log_r)


def kpuu_transfer(kpuu_ref, r_perm, r_efflux, efflux_share) -> np.ndarray:
    """Move the calibrated Kp,uu from the reference compound to another.

    Write the reference as a clearance ratio

        theta_ref = (CL_efflux + CL_bulk) / PS  =  1/Kp,uu_ref - 1

    Only the efflux part of that is compound-specific; bulk flow out of the
    retina is a property of the eye.  ``efflux_share`` is the fraction of
    ``theta_ref`` that is active efflux, so

        theta = theta_ref * [(1 - share) + share * r_efflux] / r_perm
    """
    theta_ref = 1.0 / np.clip(kpuu_ref, 1e-6, 0.999999) - 1.0
    theta = theta_ref * ((1.0 - efflux_share) + efflux_share * r_efflux) / r_perm
    return 1.0 / (1.0 + theta)


def compartment_ratios(kpuu_nr, endo_retention, rpe_net) -> dict[str, np.ndarray]:
    """Free concentration in each compartment, as a multiple of free plasma."""
    return {
        "endothelium": endo_retention,
        "rpe": rpe_net,
        "neural_retina": kpuu_nr,
    }
