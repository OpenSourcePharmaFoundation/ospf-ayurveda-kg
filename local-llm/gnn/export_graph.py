"""Export the knowledge graph to a PyG ``HeteroData`` file.

Two sources produce the same :class:`~gnn.schema.GraphTables`:

* ``neo4j``  – live database. Schema-agnostic: every label and relationship type
               is exported; numeric features are pulled per
               :data:`~gnn.schema.NUMERIC_FEATURES`.
* ``csv``    – rebuilds the graph from ``data/processed`` (and the formulation
               CSV in ``data/raw``) by mirroring the Cypher import scripts
               ``2_…``, ``3_…``, ``0_master_import.cypher`` and §1-2 of ``10_…``.
               Use it when Neo4j is not running; the result should match a
               fresh Neo4j import of the same files.

Usage
-----
    python local-llm/gnn/export_graph.py                     # auto: neo4j if NEO4J_PASSWORD set, else csv
    python local-llm/gnn/export_graph.py --source neo4j --password ...
    python local-llm/gnn/export_graph.py --source csv
    python local-llm/gnn/export_graph.py --validate            # reload the saved file and print counts

Outputs ``local-llm/data/graph/graph_heterodata.pt`` and ``graph_node_index.csv``.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd

if __package__ in (None, ""):  # allow `python src/gnn/export_graph.py`
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gnn.schema import (  # noqa: E402
    GraphTables,
    NUMERIC_FEATURES,
    build_hetero_data,
    describe_hetero,
    load_graph,
    save_graph,
)

log = logging.getLogger("gnn.export")

SUBPROJECT = Path(__file__).resolve().parents[1]  # local-llm/
REPO_ROOT = SUBPROJECT.parent
DATA_PROCESSED = REPO_ROOT / "data" / "processed"
DATA_RAW = REPO_ROOT / "data" / "raw"
DEFAULT_OUT = SUBPROJECT / "data" / "graph" / "graph_heterodata.pt"

OM = "Oral mucositis"


# --------------------------------------------------------------------------- #
# Table accumulator shared by both sources
# --------------------------------------------------------------------------- #
class _Tables:
    def __init__(self, source: str):
        self.source = source
        self._nodes: dict[tuple[str, str], dict] = {}
        self._edges: set[tuple[str, str, str, str, str]] = set()
        self.notes: list[str] = []

    def node(self, label: str, key, name=None, external_id=None, **attrs) -> None:
        if key is None:
            return
        key = str(key).strip()
        if not key:
            return
        row = self._nodes.setdefault((label, key), {"label": label, "key": key})
        if name and not row.get("name"):
            row["name"] = str(name)
        if external_id and not row.get("external_id"):
            row["external_id"] = str(external_id)
        for k, v in attrs.items():
            if v is not None and row.get(k) is None:
                row[k] = v

    def edge(self, s: str, r: str, d: str, sk, dk) -> None:
        if sk is None or dk is None:
            return
        sk, dk = str(sk).strip(), str(dk).strip()
        if not sk or not dk:
            return
        self._edges.add((s, r, d, sk, dk))

    def has(self, label: str, key) -> bool:
        return (label, str(key).strip()) in self._nodes

    def build(self) -> GraphTables:
        nodes = pd.DataFrame(list(self._nodes.values()))
        if "name" in nodes.columns:
            nodes["name"] = nodes["name"].fillna(nodes["key"])
        else:
            nodes["name"] = nodes["key"]
        edges = pd.DataFrame(
            sorted(self._edges),
            columns=["src_label", "rel", "dst_label", "src_key", "dst_key"],
        )
        return GraphTables(
            nodes=nodes, edges=edges, source=self.source, notes=self.notes
        )


# --------------------------------------------------------------------------- #
# CSV mirror of the Cypher import scripts
# --------------------------------------------------------------------------- #
def _read_csv(path: Path, **kw) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False, **kw)


def _clean(v) -> str | None:
    """LOAD CSV semantics: empty string (or a bare pair of quotes) is null."""
    if v is None:
        return None
    v = str(v).strip()
    if v in ("", '""', "nan", "NaN"):
        return None
    return v


def _split_list(v: str | None, seps=(";", ",")) -> list[str]:
    if not v:
        return []
    v = v.replace('"', "")
    parts = re.split("|".join(map(re.escape, seps)), v)
    return [p.strip() for p in parts if p.strip()]


def _to_float(v) -> float | None:
    v = _clean(v)
    if v is None:
        return None
    try:
        return float(v)
    except ValueError:
        return None


class CsvSource:
    """Rebuild the graph from the processed CSV/JSON files the Cypher scripts load."""

    def __init__(self, processed: Path = DATA_PROCESSED, raw: Path = DATA_RAW):
        self.processed = Path(processed)
        self.raw = Path(raw)

    def _path(self, name: str) -> Path | None:
        for base in (self.processed, self.raw):
            p = base / name
            if p.exists():
                return p
        return None

    def load(self) -> GraphTables:
        t = _Tables("csv")
        self._script_2_plants_compounds_targets(t)
        self._script_3_disease_drug_target(t)
        self._chembl_master(t)
        self._script_10_extracted_types(t)
        tables = t.build()
        log.info(
            "csv mirror built: %d nodes, %d edges", len(tables.nodes), len(tables.edges)
        )
        return tables

    # -- 2_formulation_plant_compound_target.txt ------------------------------
    def _script_2_plants_compounds_targets(self, t: _Tables) -> None:
        form = self._path("ayurvedic_formulation.csv") or self._path(
            "ayurvedic_formulation_good_candidates_oral_mucositis.csv"
        )
        if form:
            for _, r in _read_csv(form).iterrows():
                plant = _clean(r.get("Scientific name of the ingredient"))
                f = _clean(r.get("Formulation"))
                t.node("Plant", plant, name=plant)
                t.node("Formulation", f, name=f)
                t.edge("Formulation", "CONTAINS", "Plant", f, plant)
        else:
            t.notes.append("formulation CSV not found; no Formulation nodes")

        p = self._path("imppat_plant_part_phytochemicals.json")
        if p:
            for entry in json.loads(p.read_text()):
                plant = _clean(entry.get("plant"))
                t.node("Plant", plant, name=plant)
                for part_name in entry.get("phytochemicals", []):
                    cname = _clean(part_name[1]) if len(part_name) > 1 else None
                    t.node("Compound", cname, name=cname)
                    t.edge("Plant", "PRODUCES", "Compound", plant, cname)

        p = self._path("imppat_plant_therapeutic_uses.json")
        if p:
            for entry in json.loads(p.read_text()):
                plant = _clean(entry.get("plant"))
                t.node("Plant", plant, name=plant)
                for use in entry.get("therapeutic_use", []):
                    area = _clean(use[0]) if use else None
                    t.node("Therapeutic_Area", area, name=area)
                    t.edge("Plant", "TREATS", "Therapeutic_Area", plant, area)

        # phytochem name → imppatId → pubchemId
        pubchem_to_compounds: dict[str, list[str]] = defaultdict(list)
        p = self._path("phytochem_imppatid_pubchem_id_url.csv")
        if p:
            for _, r in _read_csv(p).iterrows():
                cname = _clean(r.get("Name"))
                url = _clean(r.get("PubChem URL")) or ""
                cid = _clean(r.get("PubChem ID")) if url.startswith("https") else None
                t.node("Compound", cname, name=cname, external_id=cid)
                if cid:
                    pubchem_to_compounds[cid].append(cname)

        p = self._path("pubchem_phytochem_target_interactions.csv")
        if p:
            df = _read_csv(p)
            for r in df.itertuples(index=False):
                cid = _clean(r.cid)
                compounds = pubchem_to_compounds.get(
                    cid, []
                )  # MATCH (c {pubchemId}) semantics
                if not compounds:
                    continue
                gene = _clean(r.gene_name)
                prot = _clean(r.protein_name)
                if prot is None and gene is not None:
                    t.node("Gene", gene, name=gene)
                    for c in compounds:
                        t.edge("Compound", "TARGETS", "Gene", c, gene)
                elif prot is not None:
                    t.node("Protein", prot, name=prot, external_id=_clean(r.protein_id))
                    for c in compounds:
                        t.edge("Compound", "TARGETS", "Protein", c, prot)
                    if gene is not None:
                        t.node("Gene", gene, name=gene)
                        t.edge("Gene", "TRANSLATION", "Protein", gene, prot)

    # -- 3_disease_drug_target.txt --------------------------------------------
    def _script_3_disease_drug_target(self, t: _Tables) -> None:
        t.node("Disease", OM, name=OM)

        p = self._path("drugbank_drug_targets.csv")
        if p:
            for _, r in _read_csv(p).iterrows():
                drug = _clean(r.get("Drug_name"))
                dkey = f"name:{drug}" if drug else None
                t.node("Drug", dkey, name=drug, external_id=_clean(r.get("Drug_ID")))
                t.edge("Drug", "TREATS", "Disease", dkey, OM)
                prot = _clean(r.get("Target_name"))
                uniprot = _clean(r.get("Target_uniprot"))
                t.node("Protein", prot, name=prot, external_id=uniprot)
                t.edge("Drug", "TARGETS", "Protein", dkey, prot)
                gene = _clean(r.get("Gene"))
                if uniprot and gene:
                    t.node("Gene", gene, name=gene)
                    t.edge("Gene", "TRANSLATION", "Protein", gene, prot)

        p = self._path("ttd_drug_target_genes.csv")
        if p:
            for _, r in _read_csv(p).iterrows():
                disease = _clean(r.get("Disease"))
                drug = _clean(r.get("Drug"))
                dkey = f"name:{drug}" if drug else None
                t.node("Disease", disease, name=disease)
                t.node("Drug", dkey, name=drug)
                t.edge("Drug", "TREATS", "Disease", dkey, disease)
                prot = _clean(r.get("Target"))
                gene = _clean(r.get("Gene"))
                if prot:
                    t.node("Protein", prot, name=prot)
                    t.edge("Drug", "TARGETS", "Protein", dkey, prot)
                    if gene:
                        t.node("Gene", gene, name=gene)
                        t.edge("Gene", "TRANSLATION", "Protein", gene, prot)

        gda_max: dict[str, float] = {}
        for fname, rel in (
            ("disgenet__OM_altexps.csv", "EXPRESSION_ASSOCIATION"),
            ("disgenet__OM_biomarkers.csv", "BIOMARKER"),
            ("disgenet__OM_genvars.csv", "VARIANT_ASSOCIATION"),
        ):
            p = self._path(fname)
            if not p:
                continue
            for _, r in _read_csv(p).iterrows():
                gene = _clean(r.get("Gene"))
                if not gene:
                    continue
                t.node("Gene", gene, name=gene, external_id=_clean(r.get("Gene_id")))
                t.edge("Gene", rel, "Disease", gene, OM)
                s = _to_float(r.get("Score_gda"))
                if s is not None:
                    gda_max[gene] = max(s, gda_max.get(gene, float("-inf")))
        for gene, s in gda_max.items():
            t.node("Gene", gene, gda_score_max=s)

    # -- 0_master_import.cypher (ChemBL) --------------------------------------
    def _chembl_master(self, t: _Tables) -> None:
        p = self._path("chembl_approved_drugs.csv")
        drugs_present: set[str] = set()
        if p:
            df = _read_csv(p)
            for r in df.itertuples(index=False):
                cid = _clean(r.chembl_id)
                if not cid:
                    continue
                drugs_present.add(cid)
                feats = {
                    f: _to_float(getattr(r, f, None))
                    for f in NUMERIC_FEATURES["Drug"]
                    if f != "natural_product"
                }
                np_flag = _clean(getattr(r, "natural_product", None))
                feats["natural_product"] = (
                    1.0 if np_flag in ("1", "True", "true") else 0.0
                )
                t.node("Drug", cid, name=_clean(r.pref_name), external_id=cid, **feats)
                for area in _split_list(
                    _clean(getattr(r, "therapeutic_areas", None)), seps=(";",)
                ):
                    t.node("Therapeutic_Area", area, name=area)
                    t.edge("Drug", "INDICATED_FOR", "Therapeutic_Area", cid, area)

        p = self._path("chembl_drug_mechanisms.csv")
        if p:
            for r in _read_csv(p).itertuples(index=False):
                cid = _clean(r.chembl_id)
                if cid not in drugs_present:
                    continue  # MATCH (d:Drug {chembl_id}) semantics
                target = _clean(r.target_chembl_id)
                action = _clean(r.action_type)
                mech_id = f"{cid}_{target or 'unknown'}_{action or 'unknown'}"
                t.node(
                    "Mechanism", mech_id, name=_clean(r.mechanism_of_action) or mech_id
                )
                t.edge("Drug", "HAS_MECHANISM", "Mechanism", cid, mech_id)
                if target:
                    t.node(
                        "Target", target, name=_clean(r.target_name), external_id=target
                    )
                    t.edge("Mechanism", "ACTS_ON", "Target", mech_id, target)

        target_genes: dict[str, list[str]] = {}
        target_uniprots: dict[str, list[str]] = {}
        p = self._path("chembl_drug_targets.csv")
        if p:
            for r in _read_csv(p).itertuples(index=False):
                tid = _clean(r.target_chembl_id)
                if not tid:
                    continue
                t.node("Target", tid, name=_clean(r.pref_name), external_id=tid)
                target_genes[tid] = _split_list(_clean(r.gene_names))
                target_uniprots[tid] = _split_list(_clean(r.uniprot_accessions))

        p = self._path("chembl_drug_indications.csv")
        indication_names: dict[str, str] = {}
        if p:
            for r in _read_csv(p).itertuples(index=False):
                cid = _clean(r.chembl_id)
                if cid not in drugs_present:
                    continue
                mesh, efo = _clean(r.mesh_id), _clean(r.efo_id)
                heading, term = _clean(r.mesh_heading), _clean(r.efo_term)
                name = heading or term
                ind_id = mesh or efo or (f"{cid}_{name}" if name else None)
                if not ind_id:
                    continue
                t.node("Indication", ind_id, name=name, external_id=mesh or efo)
                indication_names[ind_id] = (name or "").lower()
                t.edge("Drug", "TREATS_INDICATION", "Indication", cid, ind_id)

        p = self._path("chembl_drug_warnings.csv")
        if p:
            for r in _read_csv(p).itertuples(index=False):
                cid = _clean(r.chembl_id)
                if cid not in drugs_present:
                    continue
                wtype, wclass = _clean(r.warning_type), _clean(r.warning_class)
                wid = f"{cid}_{wtype or 'unknown'}_{wclass or 'unknown'}"
                t.node("Warning", wid, name=_clean(r.warning_description) or wid)
                t.edge("Drug", "HAS_WARNING", "Warning", cid, wid)
                if wclass:
                    t.node("ToxicityCategory", wclass, name=wclass)
                    t.edge("Warning", "CATEGORY", "ToxicityCategory", wid, wclass)

        # Section 9: cross-database links.
        # NOTE: the Cypher splits uniprot_accessions on ', ' although the CSV uses
        # '; '. We split on both, so multi-accession targets link here even though
        # they silently don't in Neo4j today.
        protein_by_uniprot: dict[str, list[str]] = defaultdict(list)
        for (label, key), row in t._nodes.items():
            if label == "Protein" and row.get("external_id"):
                protein_by_uniprot[row["external_id"]].append(key)
        for tid, accs in target_uniprots.items():
            for acc in accs:
                for prot in protein_by_uniprot.get(acc, []):
                    t.edge("Target", "SAME_AS", "Protein", tid, prot)
        for tid, genes in target_genes.items():
            for g in genes:
                if t.has("Gene", g):
                    t.edge("Target", "ENCODED_BY", "Gene", tid, g)

        diseases = [
            (k, row.get("name", k).lower())
            for (lbl, k), row in t._nodes.items()
            if lbl == "Disease"
        ]
        for ind_id, iname in indication_names.items():
            if not iname:
                continue
            for dkey, dname in diseases:
                if dname == iname or dname in iname or iname in dname:
                    t.edge("Indication", "SAME_AS", "Disease", ind_id, dkey)
            if "mucositis" in iname or "stomatitis" in iname:
                t.edge("Indication", "RELATED_TO", "Disease", ind_id, OM)

        t.notes.append(
            "csv mirror skips metabolism (Enzyme/Metabolite) import; run Neo4j export for those"
        )

    # -- 10_extract_new_node_types.txt §1-2 -----------------------------------
    def _script_10_extracted_types(self, t: _Tables) -> None:
        p = self._path("chembl_approved_drugs.csv")
        if not p:
            return
        for r in _read_csv(p).itertuples(index=False):
            cid = _clean(r.chembl_id)
            if not cid:
                continue
            for ind in _split_list(
                _clean(getattr(r, "indication_class", None)), seps=(";",)
            ):
                key = f"name:{ind}"  # MERGE on name, distinct from the id-keyed ChemBL indications
                t.node("Indication", key, name=ind)
                t.edge("Drug", "TREATS_INDICATION", "Indication", cid, key)
            mt = _clean(getattr(r, "molecule_type", None))
            if mt:
                t.node("MoleculeType", mt, name=mt)
                t.edge("Drug", "IS_TYPE", "MoleculeType", cid, mt)
        t.notes.append(
            "csv mirror covers 10_extract §1-2 (Indication from indication_class, MoleculeType) only"
        )


# --------------------------------------------------------------------------- #
# Live Neo4j
# --------------------------------------------------------------------------- #
LABEL_PRIORITY = [
    "Drug",
    "Compound",
    "Gene",
    "Protein",
    "Disease",
    "Plant",
    "Formulation",
    "Therapeutic_Area",
    "Target",
    "Indication",
    "Mechanism",
    "Warning",
]
NAME_PROPS = [
    "name",
    "pref_name",
    "chembl_name",
    "scientificName",
    "mesh_heading",
    "efo_term",
    "id",
    "chembl_id",
]
EXTERNAL_ID_PROPS = [
    "pubchemId",
    "chembl_id",
    "uniprotId",
    "ncbiId",
    "imppatId",
    "drugbankId",
    "mesh_id",
    "efo_id",
]


class Neo4jSource:
    def __init__(self, uri: str, user: str, password: str, database: str | None = None):
        self.uri, self.user, self.password, self.database = (
            uri,
            user,
            password,
            database,
        )

    @staticmethod
    def _primary_label(labels: list[str]) -> str:
        for lbl in LABEL_PRIORITY:
            if lbl in labels:
                return lbl
        return sorted(labels)[0]

    def load(self) -> GraphTables:
        from neo4j import GraphDatabase
        from neo4j.exceptions import ClientError

        t = _Tables(f"neo4j:{self.uri}")
        driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
        try:
            driver.verify_connectivity()
            with driver.session(database=self.database) as s:
                try:
                    s.run("MATCH (n) RETURN elementId(n) LIMIT 1").consume()
                    idf = "elementId"
                except ClientError:
                    idf = "toString(id"  # Neo4j 4.x fallback; closed below
                idfn = (
                    (lambda v: f"{idf}({v})")
                    if idf == "elementId"
                    else (lambda v: f"toString(id({v}))")
                )

                log.info("exporting nodes…")
                for rec in s.run(
                    f"MATCH (n) RETURN {idfn('n')} AS id, labels(n) AS labels, properties(n) AS props"
                ):
                    labels = rec["labels"] or ["Unlabeled"]
                    label = self._primary_label(labels)
                    props = rec["props"] or {}
                    name = next(
                        (
                            props[k]
                            for k in NAME_PROPS
                            if props.get(k) not in (None, "")
                        ),
                        rec["id"],
                    )
                    ext = next(
                        (
                            props[k]
                            for k in EXTERNAL_ID_PROPS
                            if props.get(k) not in (None, "")
                        ),
                        None,
                    )
                    feats = {}
                    for f in NUMERIC_FEATURES.get(label, []):
                        v = props.get(f)
                        if isinstance(v, bool):
                            v = 1.0 if v else 0.0
                        feats[f] = _to_float(v) if v is not None else None
                    t.node(label, rec["id"], name=str(name), external_id=ext, **feats)

                log.info("exporting relationships…")
                label_of = {k[1]: k[0] for k in t._nodes}
                for rec in s.run(
                    f"MATCH (a)-[r]->(b) RETURN {idfn('a')} AS src, type(r) AS rel, {idfn('b')} AS dst"
                ):
                    s_lbl, d_lbl = label_of.get(rec["src"]), label_of.get(rec["dst"])
                    if s_lbl and d_lbl:
                        t.edge(s_lbl, rec["rel"], d_lbl, rec["src"], rec["dst"])

                log.info("aggregating gene gdaScore…")
                q = (
                    f"MATCH (g:Gene)-[r]->(:Disease) WHERE r.gdaScore IS NOT NULL "
                    f"RETURN {idfn('g')} AS id, max(toFloat(r.gdaScore)) AS s"
                )
                for rec in s.run(q):
                    if rec["s"] is not None:
                        t.node("Gene", rec["id"], gda_score_max=float(rec["s"]))
        finally:
            driver.close()
        return t.build()


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def export(source: str, out: Path, neo4j_kwargs: dict) -> Path:
    if source == "neo4j":
        tables = Neo4jSource(**neo4j_kwargs).load()
    else:
        tables = CsvSource().load()

    print(tables.summary())
    data, node_index = build_hetero_data(tables)
    print("\nHeteroData:")
    print(describe_hetero(data))
    idx_csv = save_graph(data, node_index, out)
    for n in tables.notes:
        print(f"note: {n}")
    print(f"\nsaved {out}\nsaved {idx_csv}")
    return out


def validate(pt_path: Path) -> None:
    data, node_index = load_graph(pt_path)
    print(describe_hetero(data))
    counts = node_index.groupby("label").size()
    ok = all(counts.get(nt, 0) == data[nt].num_nodes for nt in data.node_types)
    print(f"\nnode index rows: {len(node_index):,}  matches tensor sizes: {ok}")
    total_edges = sum(data[et].edge_index.size(1) for et in data.edge_types)
    print(
        f"total nodes: {sum(data[nt].num_nodes for nt in data.node_types):,}  total edges: {total_edges:,}"
    )
    if not ok:
        sys.exit(1)


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--source", choices=["auto", "neo4j", "csv"], default="auto")
    ap.add_argument(
        "--uri", default=os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    )
    ap.add_argument("--user", default=os.environ.get("NEO4J_USER", "neo4j"))
    ap.add_argument("--password", default=os.environ.get("NEO4J_PASSWORD"))
    ap.add_argument("--database", default=os.environ.get("NEO4J_DATABASE"))
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument(
        "--validate", action="store_true", help="only reload --out and print counts"
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )

    if args.validate:
        validate(args.out)
        return

    source = args.source
    if source == "auto":
        source = "neo4j" if args.password else "csv"
        print(
            f"source=auto → {source}"
            + ("" if args.password else " (set NEO4J_PASSWORD to export from Neo4j)")
        )
    if source == "neo4j" and not args.password:
        sys.exit("Neo4j export needs --password or NEO4J_PASSWORD")

    export(
        source,
        args.out,
        dict(
            uri=args.uri, user=args.user, password=args.password, database=args.database
        ),
    )


if __name__ == "__main__":
    main()
