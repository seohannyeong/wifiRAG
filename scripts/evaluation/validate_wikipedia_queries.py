from collections import Counter, defaultdict
from pathlib import Path
import argparse
import json
import re
import sys
import unicodedata


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHUNKS = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks_full.jsonl"
DEFAULT_QUERIES = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_queries_test.jsonl"
)
DEFAULT_DEV_QUERIES = (
    PROJECT_ROOT / "data" / "evaluation" / "wikipedia_retrieval_queries.jsonl"
)
DEFAULT_REPORT = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_queries_test_validation.md"
)

QUERY_TYPES = ("exact_name", "keyword", "natural", "paraphrase", "hard")
REQUIRED_FIELDS = {
    "query_id",
    "query",
    "query_type",
    "difficulty",
    "expected_entity",
    "relevant_chunk_ids",
}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on {path}:{line_number}") from exc
    return rows


def normalize_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(re.findall(r"[a-z0-9]+", without_accents.casefold()))


def display_entity(entity: str) -> str:
    return entity.replace("_", " ").strip()


def contains_entity_title(query: str, entity: str) -> bool:
    title = display_entity(entity)
    variants = {
        normalize_text(title),
        normalize_text(re.sub(r"\s*\([^)]*\)\s*$", "", title)),
    }
    normalized_query = f" {normalize_text(query)} "
    return any(
        len(variant) >= 4 and f" {variant} " in normalized_query
        for variant in variants
    )


def validate_rows(
    queries: list[dict],
    chunks: list[dict],
    dev_queries: list[dict],
) -> tuple[list[str], list[str], dict, set[str]]:
    errors = []
    warnings = []
    chunk_by_id = {chunk["chunk_id"]: chunk for chunk in chunks}
    seen_ids = set()
    seen_queries = set()
    queries_by_entity = defaultdict(list)
    row_errors_by_entity = defaultdict(list)

    for row_number, query in enumerate(queries, start=1):
        location = f"row {row_number}"
        missing = REQUIRED_FIELDS - set(query)
        if missing:
            errors.append(f"{location}: missing fields {sorted(missing)}")
            continue

        query_id = query["query_id"]
        normalized_query = normalize_text(query["query"])
        query_type = query["query_type"]
        entity = query["expected_entity"]

        if query_id in seen_ids:
            errors.append(f"{location}: duplicate query_id {query_id}")
        seen_ids.add(query_id)

        if normalized_query in seen_queries:
            errors.append(f"{location}: duplicate query text {query['query']}")
        seen_queries.add(normalized_query)

        if query_type not in QUERY_TYPES:
            errors.append(f"{location}: unknown query type {query_type}")
        if not normalized_query:
            errors.append(f"{location}: empty query")

        relevant_ids = query["relevant_chunk_ids"]
        if not relevant_ids:
            errors.append(f"{location}: no relevant chunk IDs")
            row_errors_by_entity[entity].append(location)
        evidence_texts = []
        for chunk_id in relevant_ids:
            chunk = chunk_by_id.get(chunk_id)
            if chunk is None:
                errors.append(f"{location}: unknown chunk ID {chunk_id}")
                row_errors_by_entity[entity].append(location)
            elif chunk["entity"] != entity:
                errors.append(
                    f"{location}: {chunk_id} belongs to {chunk['entity']}, not {entity}"
                )
                row_errors_by_entity[entity].append(location)
            else:
                evidence_texts.append(chunk["text"])

        if query_type == "exact_name":
            if normalized_query != normalize_text(display_entity(entity)):
                warnings.append(
                    f"{location}: exact-name query differs from entity title"
                )
        elif contains_entity_title(query["query"], entity):
            errors.append(f"{location}: query reveals the entity title")
            row_errors_by_entity[entity].append(location)

        evidence_numbers = set(
            re.findall(r"\d+", " ".join(evidence_texts))
        )
        query_numbers = set(re.findall(r"\d+", query["query"]))
        unsupported_numbers = query_numbers - evidence_numbers
        if unsupported_numbers:
            errors.append(
                f"{location}: unsupported numbers {sorted(unsupported_numbers)}"
            )
            row_errors_by_entity[entity].append(location)
        if re.search(
            r"\d:\d|\b\d{1,2}\.\d{3}\b|-\s*:\s*\d",
            query["query"],
        ):
            errors.append(f"{location}: malformed numeric punctuation")
            row_errors_by_entity[entity].append(location)

        queries_by_entity[entity].append(query)

    expected_types = set(QUERY_TYPES)
    for entity, entity_queries in queries_by_entity.items():
        type_counts = Counter(row["query_type"] for row in entity_queries)
        missing_types = expected_types - set(type_counts)
        duplicate_types = {
            query_type: count
            for query_type, count in type_counts.items()
            if count > 1
        }
        if missing_types:
            errors.append(f"{entity}: missing query types {sorted(missing_types)}")
        if duplicate_types:
            errors.append(f"{entity}: duplicate query types {duplicate_types}")

    dev_entities = {row["expected_entity"] for row in dev_queries}
    test_entities = set(queries_by_entity)
    overlap = sorted(dev_entities & test_entities)
    if overlap:
        errors.append(
            f"Dev/test entity overlap ({len(overlap)}): {overlap[:10]}"
        )

    type_counts = Counter(row.get("query_type") for row in queries)
    metrics = {
        "query_count": len(queries),
        "entity_count": len(test_entities),
        "type_counts": dict(sorted(type_counts.items())),
        "dev_entity_overlap": len(overlap),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "invalid_entity_count": len(row_errors_by_entity),
    }
    invalid_entities = set(row_errors_by_entity)
    return errors, warnings, metrics, invalid_entities


def write_report(
    path: Path,
    query_path: Path,
    chunk_path: Path,
    metrics: dict,
    errors: list[str],
    warnings: list[str],
) -> None:
    lines = [
        "# Wikipedia Retrieval Query Validation",
        "",
        f"- Queries: `{query_path}`",
        f"- Chunks: `{chunk_path}`",
        f"- Query count: {metrics['query_count']}",
        f"- Entity count: {metrics['entity_count']}",
        f"- Dev/test entity overlap: {metrics['dev_entity_overlap']}",
        f"- Errors: {metrics['error_count']}",
        f"- Warnings: {metrics['warning_count']}",
        f"- Invalid entities: {metrics['invalid_entity_count']}",
        "",
        "## Query Type Counts",
        "",
        "| Type | Count |",
        "| --- | ---: |",
    ]
    for query_type, count in metrics["type_counts"].items():
        lines.append(f"| {query_type} | {count} |")

    lines.extend(["", "## Errors", ""])
    lines.extend(f"- {error}" for error in errors)
    if not errors:
        lines.append("- None")

    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {warning}" for warning in warnings)
    if not warnings:
        lines.append("- None")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a generated Wikipedia retrieval query set."
    )
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNKS)
    parser.add_argument("--dev-queries", type=Path, default=DEFAULT_DEV_QUERIES)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument(
        "--clean-output",
        type=Path,
        help="Write only complete entities without row-level validation errors",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    queries = load_jsonl(args.queries)
    chunks = load_jsonl(args.chunks)
    dev_queries = load_jsonl(args.dev_queries) if args.dev_queries.exists() else []
    errors, warnings, metrics, invalid_entities = validate_rows(
        queries,
        chunks,
        dev_queries,
    )
    write_report(
        path=args.report,
        query_path=args.queries,
        chunk_path=args.chunks,
        metrics=metrics,
        errors=errors,
        warnings=warnings,
    )

    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print(f"Saved report: {args.report}")
    if args.clean_output:
        clean_rows = [
            row
            for row in queries
            if row["expected_entity"] not in invalid_entities
        ]
        args.clean_output.parent.mkdir(parents=True, exist_ok=True)
        with args.clean_output.open("w", encoding="utf-8") as file:
            for row in clean_rows:
                file.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"Saved {len(clean_rows)} clean queries: {args.clean_output}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
