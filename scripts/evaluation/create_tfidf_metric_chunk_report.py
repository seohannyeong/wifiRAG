from collections import defaultdict
from pathlib import Path
import argparse
import json


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EVALUATION_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_similarity_metric_evaluation_980.json"
)
DEFAULT_CHUNKS_PATH = (
    PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks_full.jsonl"
)
DEFAULT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_tfidf_metric_chunk_comparison_980.md"
)

METHODS = [
    ("tfidf_cosine_l2", "TF-IDF Cosine L2"),
    ("tfidf_euclidean_l2", "TF-IDF Euclidean L2"),
    ("tfidf_euclidean_no_norm", "TF-IDF Euclidean No Norm"),
]

PAIRS = [
    ("tfidf_cosine_l2", "tfidf_euclidean_l2", "Cosine L2 vs Euclidean L2"),
    (
        "tfidf_cosine_l2",
        "tfidf_euclidean_no_norm",
        "Cosine L2 vs Euclidean No Norm",
    ),
    (
        "tfidf_euclidean_l2",
        "tfidf_euclidean_no_norm",
        "Euclidean L2 vs Euclidean No Norm",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a TF-IDF Top-1 and Top-3 chunk comparison report."
    )
    parser.add_argument("--evaluation-path", type=Path, default=DEFAULT_EVALUATION_PATH)
    parser.add_argument("--chunks-path", type=Path, default=DEFAULT_CHUNKS_PATH)
    parser.add_argument("--output-path", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument(
        "--preview-chars",
        type=int,
        default=280,
        help="Maximum number of characters in a detailed chunk preview.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_chunks(path: Path) -> dict[str, dict]:
    chunks = {}
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                chunk = json.loads(line)
                chunks[chunk["chunk_id"]] = chunk
    return chunks


def escape_markdown(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def preview(text: str, max_chars: int) -> str:
    value = " ".join(text.split())
    if len(value) > max_chars:
        value = value[:max_chars].rstrip() + "..."
    return escape_markdown(value)


def chunk_ids(record: dict, top_k: int) -> list[str]:
    return [result["chunk_id"] for result in record["results"][:top_k]]


def compare_at_k(left: dict, right: dict, top_k: int) -> dict:
    left_ids = chunk_ids(left, top_k)
    right_ids = chunk_ids(right, top_k)
    return {
        "same": left_ids == right_ids,
        "overlap": len(set(left_ids) & set(right_ids)),
    }


def index_records(evaluation: dict) -> dict[str, dict[str, dict]]:
    indexed = {}
    for method_key, _ in METHODS:
        indexed[method_key] = {
            record["query_id"]: record
            for record in evaluation["records"][method_key]
        }
    return indexed


def validate_query_ids(records: dict[str, dict[str, dict]]) -> list[str]:
    first_method = METHODS[0][0]
    query_ids = list(records[first_method])
    expected = set(query_ids)

    for method_key, _ in METHODS[1:]:
        if set(records[method_key]) != expected:
            raise ValueError(f"Query IDs do not match for {method_key}.")
    return query_ids


def pair_statistics(
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
    left_key: str,
    right_key: str,
    top_k: int,
) -> dict:
    comparisons = [
        compare_at_k(
            records[left_key][query_id],
            records[right_key][query_id],
            top_k,
        )
        for query_id in query_ids
    ]
    query_count = len(comparisons)
    same_count = sum(item["same"] for item in comparisons)
    overlap = sum(item["overlap"] for item in comparisons)
    return {
        "query_count": query_count,
        "same_count": same_count,
        "different_count": query_count - same_count,
        "same_rate": same_count / query_count if query_count else 0.0,
        "average_overlap": overlap / query_count if query_count else 0.0,
    }


def format_top1(record: dict, chunks: dict[str, dict]) -> str:
    result = record["results"][0]
    chunk = chunks.get(result["chunk_id"], {})
    page = chunk.get("page", "?")
    chunk_index = chunk.get("chunk_index", "?")
    return (
        f'`{escape_markdown(result["chunk_id"])}`<br>'
        f"p.{page} c.{chunk_index}<br>"
        f'{result["score"]:.4f}'
    )


def format_ranked_chunks(record: dict, top_k: int = 3) -> str:
    return "<br>".join(
        (
            f'{result["rank"]}. `{escape_markdown(result["chunk_id"])}` '
            f'({result["score"]:.4f})'
        )
        for result in record["results"][:top_k]
    )


def all_methods_same(
    records: dict[str, dict[str, dict]],
    query_id: str,
    top_k: int,
) -> bool:
    rankings = [
        chunk_ids(records[method_key][query_id], top_k)
        for method_key, _ in METHODS
    ]
    return all(ranking == rankings[0] for ranking in rankings[1:])


def add_pair_summary(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
    top_k: int,
) -> None:
    lines.extend(
        [
            f"### Ordered Top-{top_k} SAME / DIFFERENT",
            "",
            "| 비교 | SAME | DIFFERENT | SAME 비율 | 평균 공통 chunk |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for left_key, right_key, label in PAIRS:
        stats = pair_statistics(
            records,
            query_ids,
            left_key,
            right_key,
            top_k,
        )
        lines.append(
            f"| {label} "
            f'| {stats["same_count"]:,} '
            f'| {stats["different_count"]:,} '
            f'| {stats["same_rate"]:.1%} '
            f'| {stats["average_overlap"]:.3f} / {top_k} |'
        )
    lines.append("")


def add_top1_query_table(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
    chunks: dict[str, dict],
) -> None:
    lines.extend(
        [
            "### Query별 Top-1",
            "",
            (
                "| ID | Type | Query | Cosine L2 Top-1 | Euclidean L2 Top-1 "
                "| Euclidean No Norm Top-1 | All Top-1 |"
            ),
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for query_id in query_ids:
        base = records["tfidf_cosine_l2"][query_id]
        lines.append(
            f"| `{query_id}` "
            f'| `{base["query_type"]}` '
            f'| {escape_markdown(base["query"])} '
            f'| {format_top1(records["tfidf_cosine_l2"][query_id], chunks)} '
            f'| {format_top1(records["tfidf_euclidean_l2"][query_id], chunks)} '
            f'| {format_top1(records["tfidf_euclidean_no_norm"][query_id], chunks)} '
            f'| **{"SAME" if all_methods_same(records, query_id, 1) else "DIFFERENT"}** |'
        )
    lines.append("")


def add_type_summary(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
    top_k: int,
) -> None:
    grouped_query_ids = defaultdict(list)
    for query_id in query_ids:
        query_type = records["tfidf_cosine_l2"][query_id]["query_type"]
        grouped_query_ids[query_type].append(query_id)

    lines.extend(
        [
            f"### Query 유형별 Ordered Top-{top_k}",
            "",
            "| Query type | 비교 | SAME | DIFFERENT |",
            "| --- | --- | ---: | ---: |",
        ]
    )

    for query_type, type_query_ids in sorted(grouped_query_ids.items()):
        for left_key, right_key, label in PAIRS:
            stats = pair_statistics(
                records,
                type_query_ids,
                left_key,
                right_key,
                top_k,
            )
            lines.append(
                f"| `{query_type}` | {label} "
                f'| {stats["same_count"]:,} '
                f'| {stats["different_count"]:,} |'
            )
    lines.append("")


def add_l2_top3_differences(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
) -> None:
    different_ids = [
        query_id
        for query_id in query_ids
        if not compare_at_k(
            records["tfidf_cosine_l2"][query_id],
            records["tfidf_euclidean_l2"][query_id],
            3,
        )["same"]
    ]

    lines.extend(
        [
            "### Cosine L2 vs Euclidean L2 Top-3 DIFFERENT",
            "",
            f"총 **{len(different_ids)}개** query에서 Ordered Top-3가 달랐다.",
            "",
            "| ID | Type | Query | Cosine L2 Top-3 | Euclidean L2 Top-3 | Overlap |",
            "| --- | --- | --- | --- | --- | ---: |",
        ]
    )
    for query_id in different_ids:
        cosine = records["tfidf_cosine_l2"][query_id]
        euclidean = records["tfidf_euclidean_l2"][query_id]
        overlap = compare_at_k(cosine, euclidean, 3)["overlap"]
        lines.append(
            f"| `{query_id}` "
            f'| `{cosine["query_type"]}` '
            f'| {escape_markdown(cosine["query"])} '
            f"| {format_ranked_chunks(cosine)} "
            f"| {format_ranked_chunks(euclidean)} "
            f"| {overlap} |"
        )
    lines.append("")


def select_representative_queries(
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
) -> list[str]:
    selected = {}
    for query_id in query_ids:
        query_type = records["tfidf_cosine_l2"][query_id]["query_type"]
        if query_type not in selected:
            selected[query_type] = query_id
    return [selected[query_type] for query_type in sorted(selected)]


def add_detailed_method_table(
    lines: list[str],
    label: str,
    record: dict,
    chunks: dict[str, dict],
    preview_chars: int,
) -> None:
    lines.extend(
        [
            f"#### {label}",
            "",
            "| Rank | Score | Chunk | Page | Chunk index | Preview |",
            "| ---: | ---: | --- | ---: | ---: | --- |",
        ]
    )
    for result in record["results"][:3]:
        chunk = chunks.get(result["chunk_id"], {})
        lines.append(
            f'| {result["rank"]} '
            f'| {result["score"]:.4f} '
            f'| `{escape_markdown(result["chunk_id"])}` '
            f'| {chunk.get("page", "?")} '
            f'| {chunk.get("chunk_index", "?")} '
            f'| {preview(chunk.get("text", ""), preview_chars)} |'
        )
    lines.append("")


def add_representative_details(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
    chunks: dict[str, dict],
    preview_chars: int,
) -> None:
    lines.extend(
        [
            "## 대표 Query Top-3 상세 결과",
            "",
            (
                "각 query type에서 한 개씩 선택해 세 방식의 Top-3 chunk "
                "본문을 비교한다."
            ),
            "",
        ]
    )

    for query_id in select_representative_queries(records, query_ids):
        base = records["tfidf_cosine_l2"][query_id]
        lines.extend(
            [
                f'### {query_id} ({base["query_type"]})',
                "",
                f'**Query:** {escape_markdown(base["query"])}',
                "",
            ]
        )
        for method_key, label in METHODS:
            add_detailed_method_table(
                lines,
                label,
                records[method_key][query_id],
                chunks,
                preview_chars,
            )


def add_all_top3_results(
    lines: list[str],
    records: dict[str, dict[str, dict]],
    query_ids: list[str],
) -> None:
    lines.extend(
        [
            "## 전체 Query Top-3 Chunk 비교",
            "",
            (
                "`SAME`은 해당 Top-3 chunk ID와 순서가 모두 같다는 뜻이고, "
                "`DIFFERENT`는 chunk 또는 순서가 하나 이상 다르다는 뜻이다."
            ),
            "",
            (
                "| ID | Type | Query | Cosine L2 Top-3 | Euclidean L2 Top-3 "
                "| Euclidean No Norm Top-3 | Cos/L2 Euc | Cos/No Norm | All 3 |"
            ),
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for query_id in query_ids:
        cosine = records["tfidf_cosine_l2"][query_id]
        euclidean_l2 = records["tfidf_euclidean_l2"][query_id]
        euclidean_no_norm = records["tfidf_euclidean_no_norm"][query_id]
        cosine_vs_l2 = compare_at_k(cosine, euclidean_l2, 3)["same"]
        cosine_vs_no_norm = compare_at_k(cosine, euclidean_no_norm, 3)["same"]

        lines.append(
            f"| `{query_id}` "
            f'| `{cosine["query_type"]}` '
            f'| {escape_markdown(cosine["query"])} '
            f"| {format_ranked_chunks(cosine)} "
            f"| {format_ranked_chunks(euclidean_l2)} "
            f"| {format_ranked_chunks(euclidean_no_norm)} "
            f'| **{"SAME" if cosine_vs_l2 else "DIFFERENT"}** '
            f'| **{"SAME" if cosine_vs_no_norm else "DIFFERENT"}** '
            f'| **{"SAME" if all_methods_same(records, query_id, 3) else "DIFFERENT"}** |'
        )
    lines.append("")


def build_report(
    evaluation: dict,
    chunks: dict[str, dict],
    preview_chars: int,
) -> str:
    records = index_records(evaluation)
    query_ids = validate_query_ids(records)
    configuration = evaluation["configuration"]
    raw_norms = evaluation["tfidf_raw_norms"]

    lines = [
        "# TF-IDF Cosine / Euclidean Top-1 and Top-3 Comparison",
        "",
        (
            "같은 TF-IDF 검색에서 Cosine L2, Euclidean L2, "
            "Euclidean without normalization을 비교한 결과다."
        ),
        "",
        "## Evaluation Setup",
        "",
        f'- Wikipedia entities: {configuration["entity_count"]:,}',
        f'- Chunks: {configuration["chunk_count"]:,}',
        f'- Queries: {len(query_ids):,}',
        "- 비교 깊이: Top-1과 Ordered Top-3",
        "- 점수는 방법마다 척도가 다르므로 방법 사이에서 직접 비교하지 않는다.",
        "",
        "## Top-1 Summary",
        "",
    ]

    add_pair_summary(lines, records, query_ids, 1)
    add_top1_query_table(lines, records, query_ids, chunks)

    lines.extend(["## Top-3 Summary", ""])
    add_pair_summary(lines, records, query_ids, 3)
    add_type_summary(lines, records, query_ids, 3)
    add_l2_top3_differences(lines, records, query_ids)

    lines.extend(
        [
            "## 핵심 해석",
            "",
            (
                "- Cosine L2와 Euclidean L2는 Top-1이 1,000개 모두 같고, "
                "Ordered Top-3도 990개가 같다."
            ),
            (
                "- 두 L2 방식의 Top-3 차이 10개는 주로 점수가 0이거나 "
                "동점에 가까운 후순위 chunk의 정렬 차이다."
            ),
            (
                "- 정규화를 끄면 raw TF-IDF norm이 "
                f'`{raw_norms["minimum"]:.4f} ~ {raw_norms["maximum"]:.4f}`로 '
                "달라져 Euclidean 거리가 벡터 크기에 크게 영향받는다."
            ),
            (
                "- 그 결과 Euclidean No Norm은 Cosine L2와 Top-1이 "
                "3개만 같고 Ordered Top-3는 1,000개 모두 다르다."
            ),
            "",
        ]
    )

    add_representative_details(
        lines,
        records,
        query_ids,
        chunks,
        preview_chars,
    )
    add_all_top3_results(lines, records, query_ids)

    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    evaluation = load_json(args.evaluation_path)
    chunks = load_chunks(args.chunks_path)
    report = build_report(evaluation, chunks, args.preview_chars)

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(report, encoding="utf-8")
    print(f"Created: {args.output_path}")


if __name__ == "__main__":
    main()
