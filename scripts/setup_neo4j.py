#!/usr/bin/env python3
"""
Neo4j Database Setup Script

Connects to a Neo4j instance and runs all Cypher scripts in order to set up
the OSPF Ayurveda Knowledge Graph database.

Usage:
    python scripts/setup_neo4j.py                    # Uses defaults (localhost:7687)
    python scripts/setup_neo4j.py --uri bolt://localhost:7687 --password mypassword
    python scripts/setup_neo4j.py --test             # Use test subset (100 drugs)
    python scripts/setup_neo4j.py --chembl-only      # Only run ChemBL import scripts
    python scripts/setup_neo4j.py --clear            # Clear existing data first

Environment variables (alternative to CLI args):
    NEO4J_URI=bolt://localhost:7687
    NEO4J_USER=neo4j
    NEO4J_PASSWORD=your_password
"""

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Optional

try:
    from neo4j import GraphDatabase
    from neo4j.exceptions import ServiceUnavailable, AuthError
except ImportError:
    print("❌ neo4j driver not installed. Run:")
    print("   pip install neo4j")
    sys.exit(1)


# Script execution order
SCRIPT_ORDER = [
    # Original scripts (for full database setup)
    ("1_uniqueness_constraints.txt", "Original constraints", False),
    ("2_formulation_plant_compound_target.txt", "IMPPAT plant data", False),
    ("3_disease_drug_target.txt", "DrugBank/TTD/DisGeNET data", False),
    # ChemBL scripts
    ("4_chembl_constraints.txt", "ChemBL constraints", True),
    ("5_chembl_approved_drugs.txt", "ChemBL approved drugs", True),
    ("6_chembl_mechanisms_targets.txt", "ChemBL mechanisms & targets", True),
    ("7_chembl_indications.txt", "ChemBL indications", True),
    ("8_chembl_warnings.txt", "ChemBL warnings", True),
]

VALIDATION_SCRIPT = ("9_chembl_test_import.txt", "Validation queries", True)


class Neo4jSetup:
    def __init__(self, uri: str, user: str, password: str):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None
        self.scripts_dir = Path(__file__).parent / "cypher_scripts"

    def connect(self) -> bool:
        """Establish connection to Neo4j."""
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            # Test connection
            with self.driver.session() as session:
                result = session.run("RETURN 1 AS test")
                result.single()
            print(f"✅ Connected to Neo4j at {self.uri}")
            return True
        except ServiceUnavailable:
            print(f"❌ Cannot connect to Neo4j at {self.uri}")
            print("   Make sure Neo4j is running and the URI is correct.")
            return False
        except AuthError:
            print(f"❌ Authentication failed for user '{self.user}'")
            print("   Check your username and password.")
            return False

    def close(self):
        """Close the Neo4j connection."""
        if self.driver:
            self.driver.close()

    def clear_database(self):
        """Clear all nodes and relationships."""
        print("\n🗑️  Clearing existing data...")
        with self.driver.session() as session:
            # Count before
            result = session.run("MATCH (n) RETURN count(n) AS count")
            count = result.single()["count"]

            if count == 0:
                print("   Database is already empty.")
                return

            print(f"   Found {count:,} nodes to delete...")

            # Delete in batches to avoid memory issues
            deleted = 0
            while True:
                result = session.run("""
                    MATCH (n)
                    WITH n LIMIT 10000
                    DETACH DELETE n
                    RETURN count(*) AS deleted
                """)
                batch_deleted = result.single()["deleted"]
                if batch_deleted == 0:
                    break
                deleted += batch_deleted
                print(f"   Deleted {deleted:,} nodes...")

            print(f"✅ Cleared {deleted:,} nodes")

    def run_script(self, script_name: str, description: str) -> bool:
        """Run a single Cypher script file."""
        script_path = self.scripts_dir / script_name

        if not script_path.exists():
            print(f"   ⚠️  Script not found: {script_name}")
            return False

        print(f"\n📄 Running: {description}")
        print(f"   File: {script_name}")

        # Read script content
        with open(script_path, 'r') as f:
            content = f.read()

        # Split into individual statements
        # Remove comments and split on semicolons
        statements = self._parse_cypher_statements(content)

        if not statements:
            print("   ⚠️  No executable statements found")
            return True

        print(f"   Statements: {len(statements)}")

        # Execute each statement
        success_count = 0
        error_count = 0

        with self.driver.session() as session:
            for i, stmt in enumerate(statements, 1):
                try:
                    result = session.run(stmt)
                    summary = result.consume()

                    # Report what was done
                    counters = summary.counters
                    changes = []
                    if counters.nodes_created:
                        changes.append(f"+{counters.nodes_created} nodes")
                    if counters.relationships_created:
                        changes.append(f"+{counters.relationships_created} rels")
                    if counters.properties_set:
                        changes.append(f"{counters.properties_set} props")
                    if counters.constraints_added:
                        changes.append(f"+{counters.constraints_added} constraints")
                    if counters.indexes_added:
                        changes.append(f"+{counters.indexes_added} indexes")

                    if changes:
                        print(f"   [{i}/{len(statements)}] {', '.join(changes)}")

                    success_count += 1

                except Exception as e:
                    error_msg = str(e)
                    # Ignore "already exists" errors for constraints/indexes
                    if "already exists" in error_msg.lower():
                        print(f"   [{i}/{len(statements)}] (already exists, skipping)")
                        success_count += 1
                    else:
                        print(f"   [{i}/{len(statements)}] ❌ Error: {error_msg[:100]}")
                        error_count += 1

        if error_count == 0:
            print(f"   ✅ Completed ({success_count} statements)")
        else:
            print(f"   ⚠️  Completed with {error_count} errors")

        return error_count == 0

    def _parse_cypher_statements(self, content: str) -> list:
        """Parse Cypher script into individual statements."""
        statements = []
        current_stmt = []

        for line in content.split('\n'):
            # Skip empty lines and comments
            stripped = line.strip()
            if not stripped or stripped.startswith('//'):
                continue

            current_stmt.append(line)

            # Statement ends with semicolon
            if stripped.endswith(';'):
                stmt = '\n'.join(current_stmt).strip()
                # Remove trailing semicolon for neo4j driver
                stmt = stmt.rstrip(';').strip()
                if stmt:
                    statements.append(stmt)
                current_stmt = []

        # Handle statement without trailing semicolon
        if current_stmt:
            stmt = '\n'.join(current_stmt).strip().rstrip(';').strip()
            if stmt:
                statements.append(stmt)

        return statements

    def run_validation(self) -> dict:
        """Run validation queries and return results."""
        print("\n🔍 Running validation queries...")

        results = {}

        with self.driver.session() as session:
            # Count ChemBL drugs
            result = session.run("""
                MATCH (d:Drug) WHERE d.chembl_id IS NOT NULL
                RETURN count(d) AS count
            """)
            results['chembl_drugs'] = result.single()["count"]

            # Count all nodes by type
            result = session.run("""
                MATCH (n)
                RETURN labels(n)[0] AS type, count(n) AS count
                ORDER BY count DESC
            """)
            results['node_counts'] = {r["type"]: r["count"] for r in result}

            # Count relationships
            result = session.run("""
                MATCH ()-[r]->()
                RETURN type(r) AS type, count(r) AS count
                ORDER BY count DESC
            """)
            results['rel_counts'] = {r["type"]: r["count"] for r in result}

        return results

    def setup_database(self, chembl_only: bool = False, clear_first: bool = False):
        """Run all setup scripts."""
        if clear_first:
            self.clear_database()

        print("\n" + "=" * 60)
        print("Starting database setup...")
        print("=" * 60)

        start_time = time.time()
        scripts_run = 0
        errors = 0

        for script_name, description, is_chembl in SCRIPT_ORDER:
            if chembl_only and not is_chembl:
                print(f"\n⏭️  Skipping: {description} (not ChemBL)")
                continue

            success = self.run_script(script_name, description)
            scripts_run += 1
            if not success:
                errors += 1

        elapsed = time.time() - start_time

        print("\n" + "=" * 60)
        print(f"Setup complete in {elapsed:.1f} seconds")
        print(f"Scripts run: {scripts_run}, Errors: {errors}")
        print("=" * 60)

        # Run validation
        results = self.run_validation()

        print("\n📊 Database Summary:")
        print(f"   ChemBL Drugs: {results['chembl_drugs']:,}")
        print(f"\n   Node counts:")
        for node_type, count in list(results['node_counts'].items())[:10]:
            print(f"      {node_type}: {count:,}")
        print(f"\n   Relationship counts:")
        for rel_type, count in list(results['rel_counts'].items())[:10]:
            print(f"      {rel_type}: {count:,}")

        return errors == 0


def main():
    parser = argparse.ArgumentParser(
        description="Set up Neo4j database for OSPF Ayurveda Knowledge Graph"
    )
    parser.add_argument(
        "--uri",
        default=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
        help="Neo4j URI (default: bolt://localhost:7687)"
    )
    parser.add_argument(
        "--user",
        default=os.environ.get("NEO4J_USER", "neo4j"),
        help="Neo4j username (default: neo4j)"
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("NEO4J_PASSWORD"),
        help="Neo4j password (or set NEO4J_PASSWORD env var)"
    )
    parser.add_argument(
        "--chembl-only",
        action="store_true",
        help="Only run ChemBL import scripts (scripts 4-8)"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all existing data before import"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use test subset data (100 drugs) - copy test_import/*.csv to Neo4j import folder first"
    )

    args = parser.parse_args()

    # Check for password
    if not args.password:
        print("❌ No password provided.")
        print("   Use --password or set NEO4J_PASSWORD environment variable")
        sys.exit(1)

    if args.test:
        print("📋 Test mode: Make sure you copied data/test_import/*.csv to Neo4j import folder")

    # Create setup instance
    setup = Neo4jSetup(args.uri, args.user, args.password)

    # Connect
    if not setup.connect():
        sys.exit(1)

    try:
        # Run setup
        success = setup.setup_database(
            chembl_only=args.chembl_only,
            clear_first=args.clear
        )
        sys.exit(0 if success else 1)
    finally:
        setup.close()


if __name__ == "__main__":
    main()
