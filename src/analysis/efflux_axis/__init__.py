"""Finding an agent for the uncovered reverse-cholesterol-transport arm.

Step 6 of ``docs/prompts/dr-solve-open-questions-prompt.md``.  Every one of the
29 compounds the diabetic-retinopathy analysis considered lowers what arrives
in the retina; none accelerates what leaves.  This package asks whether an
agent for the leaving side exists, and answers in four parts.

``axis``        The nine genes, split by what kind of evidence each can take:
                two ligandable nuclear receptors, four effectors that are
                readouts rather than pockets, three scavenger receptors.
``gnn_rank``    The repository's link-prediction model pointed at the axis,
                with the retrieval benchmark that says whether its answer can
                be believed.  It cannot; the benchmark is the deliverable.
``chembl_axis`` Measured affinity for the axis, which the knowledge graph does
                not hold.
``candidates``  Aggregation into per-molecule potency and isoform selectivity,
                tiered by what the assay could actually show.
``physchem``    The retinal-access filter, driven by Step 5's calibrated
                barrier model rather than by ``alogp``.
``steatosis``   The class-killing liability, expressed as the selectivity a
                molecule must carry rather than as a warning.
``acceptor``    Whether a direct extracellular acceptor beats a transporter
                inducer, solved as a two-compartment system.
``run``         Orchestration; writes the CSVs under ``data/processed/``.
"""
