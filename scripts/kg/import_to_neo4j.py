from pathlib import Path
import argparse
import json
import os
import re

from dotenv import load_dotenv
from neo4j import GraphDatabase


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KG_DIR = PROJECT_ROOT / "data" / "kg" / "openai"


def sanitize_relationship_type(label: str) -> str:
    rel_type = re.sub(r"[^0-9a-zA-Z_]", "_", str(label).strip())
    rel_type = re.sub(r"_+", "_", rel_type).strip("_").upper()
    if not rel_type:
        rel_type = "RELATED_TO"
    if rel_type[0].isdigit():
        rel_type = f"REL_{rel_type}"
    return rel_type


def insert_relation(tx, source: str, label: str, target: str) -> None:
    rel_type = sanitize_relationship_type(label)
    query = (
        "MERGE (a:Entity {id: $source}) "
        "MERGE (b:Entity {id: $target}) "
        f"MERGE (a)-[r:`{rel_type}`]->(b) "
        "SET r.original_label = $label"
    )
    tx.run(query, source=source, target=target, label=label)


def insert_entity(tx, entity: str) -> None:
    tx.run("MERGE (:Entity {id: $entity})", entity=entity)


def iter_kg_files(kg_dir: Path, recursive: bool) -> list[Path]:
    pattern = "**/*.json" if recursive else "*.json"
    return sorted(path for path in kg_dir.glob(pattern) if path.is_file())


def import_to_neo4j(kg_dir: Path, recursive: bool, clear_first: bool) -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    username = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD")
    if not password:
        raise RuntimeError("Missing NEO4J_PASSWORD. Create .env from .env.example first.")

    kg_files = iter_kg_files(kg_dir, recursive)
    if not kg_files:
        raise FileNotFoundError(f"No KG JSON files found in: {kg_dir}")

    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            if clear_first:
                session.run("MATCH (n) DETACH DELETE n")
                print("Cleared existing Neo4j graph.")

            for index, path in enumerate(kg_files, start=1):
                with path.open("r", encoding="utf-8") as f:
                    data = json.load(f)

                entities = data.get("entities", [])
                relations = data.get("relations", [])

                for entity in entities:
                    if isinstance(entity, str):
                        session.execute_write(insert_entity, entity)

                relation_count = 0
                for relation in relations:
                    if isinstance(relation, list) and len(relation) == 3:
                        source, label, target = relation
                        session.execute_write(insert_relation, source, label, target)
                        relation_count += 1

                print(
                    f"[{index}/{len(kg_files)}] Imported {path.name}: "
                    f"{len(entities)} entities, {relation_count} relations"
                )

    print("Neo4j import completed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Import KG JSON files into Neo4j.")
    parser.add_argument("--kg-dir", type=Path, default=DEFAULT_KG_DIR)
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--clear-first", action="store_true")
    args = parser.parse_args()

    import_to_neo4j(
        kg_dir=args.kg_dir,
        recursive=args.recursive,
        clear_first=args.clear_first,
    )


if __name__ == "__main__":
    main()
