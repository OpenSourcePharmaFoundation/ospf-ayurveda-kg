"""Quantitative ocular exposure model for the fibrate chemotype.

Step 5 of ``docs/prompts/dr-solve-open-questions-prompt.md``.  The DR analysis
assigned retinal partition ratios by argument (0.2-0.7 for endothelium and RPE,
0.01-0.15 for neural retina) and three mutually exclusive programmes depended on
which end was right.  This package replaces the assertion with a model that is
calibrated against measured data and carries its uncertainty end to end.

Modules
-------
``parameters``  Every input as a distribution with a provenance tag.  Nothing in
                this package may use a bare float that is not declared here.
``ionisation``  Henderson-Hasselbalch: logD(7.4) from logP and pKa, and the
                pH-partition ratio between two compartments.
``barrier``     The compartment model.  Calibrates ``Kp,uu`` for the neural
                retina against the one measured systemic-dosing ocular
                concentration that exists (Huang 2021) and transfers it between
                compounds on relative passive permeability and efflux.
``binding``     Free-fraction arithmetic, including the serum correction that
                makes a cell-assay EC50 comparable with a free concentration.
``potency``     EC50 distributions read from the repository's own ChEMBL pull.
``model``       Monte-Carlo over every declared input; margins per compartment.
``sensitivity`` Saltelli first-order and total Sobol indices on log10(margin).
``report``      Renders the tables that go into
                ``docs/notes/retinal-exposure-model.md``.
"""
