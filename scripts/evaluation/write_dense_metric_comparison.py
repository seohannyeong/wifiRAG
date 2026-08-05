from collections import Counter, defaultdict
from pathlib import Path
import argparse
import json


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_similarity_metric_evaluation_980.json"
)
DEFAULT_OUTPUT = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_dense_cosine_euclidean_comparison.md"
)


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def format_ranked_chunks(results: list[dict]) -> str:
    return "<br>".join(
        f"{result['rank']}. `{result['chunk_id']}` ({result['score']:.4f})"
        for result in results
    )


def compare_records(
    cosine_records: list[dict],
    euclidean_records: list[dict],
) -> list[dict]:
    if len(cosine_records) != len(euclidean_records):
        raise ValueError("Dense result counts do not match.")

    comparisons = []
    for cosine, euclidean in zip(cosine_records, euclidean_records):
        if cosine["query_id"] != euclidean["query_id"]:
            raise ValueError(
                f"Query mismatch: {cosine['query_id']} != {euclidean['query_id']}"
            )

        cosine_ids = [result["chunk_id"] for result in cosine["results"]]
        euclidean_ids = [result["chunk_id"] for result in euclidean["results"]]
        ordered_same = cosine_ids == euclidean_ids
        top1_same = cosine_ids[0] == euclidean_ids[0]
        overlap = len(set(cosine_ids) & set(euclidean_ids))

        comparisons.append(
            {
                "query_id": cosine["query_id"],
                "query": cosine["query"],
                "query_type": cosine["query_type"],
                "status": "same" if ordered_same else "different",
                "top1_same": top1_same,
                "top_k_overlap": overlap,
                "cosine_results": cosine["results"],
                "euclidean_results": euclidean["results"],
            }
        )
    return comparisons


def write_report(path: Path, data: dict, comparisons: list[dict]) -> None:
    configuration = data["configuration"]
    status_counts = Counter(item["status"] for item in comparisons)
    comparisons_by_type = defaultdict(list)
    for item in comparisons:
        comparisons_by_type[item["query_type"]].append(item)

    lines = [
        "# Dense Cosine vs Euclidean Chunk Comparison",
        "",
        "## Evaluation Setup",
        "",
        f"- Wikipedia entities: {configuration['entity_count']}",
        f"- Chunks: {configuration['chunk_count']}",
        f"- Queries: {configuration['query_count']}",
        f"- Retrieval depth: Top-{configuration['top_k']}",
        f"- Embedding model: `{configuration['embedding_model']}`",
        "- `same`: the ordered Top-5 chunk IDs are identical.",
        "- `different`: at least one Top-5 rank or chunk ID differs.",
        "",
        "## Summary",
        "",
        "| Result | Queries | Rate |",
        "| --- | ---: | ---: |",
        f"| same | {status_counts['same']} | "
        f"{status_counts['same'] / len(comparisons) * 100:.1f}% |",
        f"| different | {status_counts['different']} | "
        f"{status_counts['different'] / len(comparisons) * 100:.1f}% |",
        "",
        "| Query type | Same | Different |",
        "| --- | ---: | ---: |",
    ]

    for query_type, items in sorted(comparisons_by_type.items()):
        counts = Counter(item["status"] for item in items)
        lines.append(
            f"| {query_type} | {counts['same']} | {counts['different']} |"
        )

    lines.extend(["", "## Different Results", ""])
    different_items = [
        item
        for item in comparisons
        if item["status"] == "different"
    ]
    if not different_items:
        lines.append(
            "No different results were found. Cosine and Euclidean returned "
            "the same ordered Top-5 chunks for all queries."
        )
    else:
        lines.extend(
            [
                "| ID | Type | Query | Cosine Top-5 | Euclidean Top-5 | Overlap |",
                "| --- | --- | --- | --- | --- | ---: |",
            ]
        )
        for item in different_items:
            lines.append(
                f"| {item['query_id']} | {item['query_type']} | "
                f"{markdown_escape(item['query'])} | "
                f"{format_ranked_chunks(item['cosine_results'])} | "
                f"{format_ranked_chunks(item['euclidean_results'])} | "
                f"{item['top_k_overlap']} |"
            )

    lines.extend(
        [
            "",
            "## All Query Results",
            "",
            "The score scales differ: cosine uses cosine similarity, while "
            "Euclidean uses `1 / (1 + distance)`.",
        ]
    )

    for query_type, items in sorted(comparisons_by_type.items()):
        lines.extend(
            [
                "",
                f"### {query_type}",
                "",
                "| ID | Query | Status | Cosine Top-5 | Euclidean Top-5 | Overlap |",
                "| --- | --- | --- | --- | --- | ---: |",
            ]
        )
        for item in items:
            lines.append(
                f"| {item['query_id']} | "
                f"{markdown_escape(item['query'])} | "
                f"**{item['status']}** | "
                f"{format_ranked_chunks(item['cosine_results'])} | "
                f"{format_ranked_chunks(item['euclidean_results'])} | "
                f"{item['top_k_overlap']} |"
            )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The nomic-embed-text document and query embedding norms are approximately 1.",
            "- For unit vectors, Euclidean distance squared equals "
            "`2 - 2 * cosine_similarity`.",
            "- Therefore, larger cosine similarity always corresponds to smaller Euclidean distance.",
            "- The numerical scores differ, but the document ranking is identical in this experiment.",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write a per-query Dense cosine vs Euclidean chunk report."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    records = data["records"]
    comparisons = compare_records(
        records["dense_cosine"],
        records["dense_euclidean"],
    )
    write_report(args.output, data, comparisons)

    counts = Counter(item["status"] for item in comparisons)
    print(f"same: {counts['same']}")
    print(f"different: {counts['different']}")
    print(f"Saved report: {args.output}")


if __name__ == "__main__":
    main()
