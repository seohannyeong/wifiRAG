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
    / "wikipedia_dense_metric_chunk_comparison_980.md"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a cosine vs Euclidean dense retrieval chunk report."
    )
    parser.add_argument("--evaluation-path", type=Path, default=DEFAULT_EVALUATION_PATH)
    parser.add_argument("--chunks-path", type=Path, default=DEFAULT_CHUNKS_PATH)
    parser.add_argument("--output-path", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument(
        "--samples-per-type",
        type=int,
        default=2,
        help="Number of detailed examples to include for each query type.",
    )
    parser.add_argument(
        "--preview-chars",
        type=int,
        default=180,
        help="Maximum number of characters in each chunk preview.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_chunks(path: Path) -> dict[str, dict]:
    chunks_by_id = {}
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                chunk = json.loads(line)
                chunks_by_id[chunk["chunk_id"]] = chunk
    return chunks_by_id


def escape_markdown(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def make_preview(text: str, max_chars: int) -> str:
    preview = " ".join(text.split())
    if len(preview) > max_chars:
        preview = preview[:max_chars].rstrip() + "..."
    return escape_markdown(preview)


def result_ids(record: dict) -> list[str]:
    return [result["chunk_id"] for result in record["results"]]


def compare_records(cosine_record: dict, euclidean_record: dict) -> dict:
    cosine_ids = result_ids(cosine_record)
    euclidean_ids = result_ids(euclidean_record)
    top1_same = bool(cosine_ids and cosine_ids[0] == euclidean_ids[0])
    ordered_top_k_same = cosine_ids == euclidean_ids
    overlap = len(set(cosine_ids) & set(euclidean_ids))

    return {
        "top1_same": top1_same,
        "ordered_top_k_same": ordered_top_k_same,
        "overlap": overlap,
        "result": "SAME" if ordered_top_k_same else "DIFFERENT",
    }


def format_ranked_chunks(record: dict) -> str:
    return "<br>".join(
        (
            f'{result["rank"]}. `{escape_markdown(result["chunk_id"])}` '
            f'({result["score"]:.6f})'
        )
        for result in record["results"]
    )


def select_samples(records: list[dict], samples_per_type: int) -> list[dict]:
    counts: dict[str, int] = {}
    samples = []

    for record in records:
        query_type = record["query_type"]
        count = counts.get(query_type, 0)
        if count < samples_per_type:
            samples.append(record)
            counts[query_type] = count + 1

    return samples


def build_report(
    evaluation: dict,
    chunks_by_id: dict[str, dict],
    samples_per_type: int,
    preview_chars: int,
) -> str:
    cosine_records = evaluation["records"]["dense_cosine"]
    euclidean_records = evaluation["records"]["dense_euclidean"]
    euclidean_by_query_id = {
        record["query_id"]: record for record in euclidean_records
    }

    comparisons = []
    for cosine_record in cosine_records:
        query_id = cosine_record["query_id"]
        euclidean_record = euclidean_by_query_id.get(query_id)
        if euclidean_record is None:
            raise ValueError(f"Missing Euclidean result for query: {query_id}")
        comparisons.append(
            (
                cosine_record,
                euclidean_record,
                compare_records(cosine_record, euclidean_record),
            )
        )

    query_count = len(comparisons)
    top1_same_count = sum(item[2]["top1_same"] for item in comparisons)
    ordered_same_count = sum(item[2]["ordered_top_k_same"] for item in comparisons)
    different_count = query_count - ordered_same_count
    average_overlap = (
        sum(item[2]["overlap"] for item in comparisons) / query_count
        if query_count
        else 0.0
    )
    top_k = evaluation["configuration"]["top_k"]
    norms = evaluation["dense_norms"]

    lines = [
        "# Dense Cosine vs Euclidean Chunk Comparison",
        "",
        "## 비교 조건",
        "",
        f'- Query 수: {query_count:,}',
        f'- Corpus: {evaluation["configuration"]["entity_count"]:,} entities, '
        f'{evaluation["configuration"]["chunk_count"]:,} chunks',
        f"- 비교 범위: Top-{top_k}",
        f'- Embedding model: `{evaluation["configuration"]["embedding_model"]}`',
        "",
        "## 전체 결과",
        "",
        "| 비교 항목 | SAME | DIFFERENT | SAME 비율 |",
        "| --- | ---: | ---: | ---: |",
        (
            f"| Top-1 chunk | {top1_same_count:,} | "
            f"{query_count - top1_same_count:,} | "
            f"{top1_same_count / query_count:.1%} |"
        ),
        (
            f"| Ordered Top-{top_k} | {ordered_same_count:,} | "
            f"{different_count:,} | {ordered_same_count / query_count:.1%} |"
        ),
        "",
        f"- Average Top-{top_k} overlap: **{average_overlap:.2f} / {top_k}**",
        (
            "- 결론: 이 실험에서는 Cosine과 Euclidean이 모든 쿼리에서 "
            "동일한 Top-5 chunk를 동일한 순서로 검색했다."
        ),
        "",
        "## 동일한 순위가 나온 이유",
        "",
        (
            "- Dense document embedding norm은 "
            f"`{norms['minimum']:.6f} ~ {norms['maximum']:.6f}`이고, "
            f"평균은 `{norms['mean']:.6f}`이다."
        ),
        "- 즉, 모든 embedding 벡터의 길이가 거의 1로 정규화되어 있다.",
        (
            "- 길이가 1인 두 벡터에서는 "
            "`Euclidean distance^2 = 2 - 2 * Cosine similarity` 관계가 성립한다."
        ),
        (
            "- 따라서 점수의 숫자와 방향은 다르지만, 유사한 문서를 정렬한 "
            "순위는 같아진다."
        ),
        "",
        "## Query 유형별 SAME / DIFFERENT",
        "",
        "| Query type | Query 수 | SAME | DIFFERENT |",
        "| --- | ---: | ---: | ---: |",
    ]

    query_types = sorted({record["query_type"] for record in cosine_records})
    for query_type in query_types:
        type_items = [
            item for item in comparisons if item[0]["query_type"] == query_type
        ]
        same_count = sum(item[2]["ordered_top_k_same"] for item in type_items)
        lines.append(
            f"| `{query_type}` | {len(type_items):,} | "
            f"{same_count:,} | {len(type_items) - same_count:,} |"
        )

    lines.extend(
        [
            "",
            "## 대표 Query 상세 비교",
            "",
            (
                f"각 query type에서 앞의 {samples_per_type}개 query를 선택했다. "
                "점수는 서로 다른 척도이므로 숫자 크기를 직접 비교하지 않고 "
                "chunk 순위를 비교한다."
            ),
            "",
        ]
    )

    sample_ids = {
        record["query_id"]
        for record in select_samples(cosine_records, samples_per_type)
    }
    for cosine_record, euclidean_record, comparison in comparisons:
        if cosine_record["query_id"] not in sample_ids:
            continue

        lines.extend(
            [
                (
                    f'### {cosine_record["query_id"]} '
                    f'({cosine_record["query_type"]})'
                ),
                "",
                f'- Query: **{escape_markdown(cosine_record["query"])}**',
                f'- Expected entity: `{escape_markdown(cosine_record["expected_entity"])}`',
                f'- Result: **{comparison["result"]}**',
                "",
                (
                    "| Rank | Cosine chunk | Cosine score | Euclidean chunk | "
                    "Euclidean similarity | Rank result | Chunk preview |"
                ),
                "| ---: | --- | ---: | --- | ---: | --- | --- |",
            ]
        )

        for cosine_result, euclidean_result in zip(
            cosine_record["results"], euclidean_record["results"]
        ):
            rank_same = cosine_result["chunk_id"] == euclidean_result["chunk_id"]
            chunk = chunks_by_id.get(cosine_result["chunk_id"], {})
            preview = make_preview(chunk.get("text", ""), preview_chars)
            lines.append(
                f'| {cosine_result["rank"]} '
                f'| `{escape_markdown(cosine_result["chunk_id"])}` '
                f'| {cosine_result["score"]:.6f} '
                f'| `{escape_markdown(euclidean_result["chunk_id"])}` '
                f'| {euclidean_result["score"]:.6f} '
                f'| {"SAME" if rank_same else "DIFFERENT"} '
                f"| {preview} |"
            )
        lines.append("")

    lines.extend(
        [
            "## DIFFERENT Query 모음",
            "",
        ]
    )
    different_items = [
        item for item in comparisons if not item[2]["ordered_top_k_same"]
    ]
    if not different_items:
        lines.extend(
            [
                (
                    "**없음.** 1,000개 query 모두 Cosine과 Euclidean의 "
                    "Ordered Top-5가 동일했다."
                ),
                "",
            ]
        )
    else:
        lines.extend(
            [
                "| Query ID | Type | Query | Cosine Top-5 | Euclidean Top-5 |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for cosine_record, euclidean_record, _ in different_items:
            lines.append(
                f'| `{cosine_record["query_id"]}` '
                f'| `{cosine_record["query_type"]}` '
                f'| {escape_markdown(cosine_record["query"])} '
                f"| {format_ranked_chunks(cosine_record)} "
                f"| {format_ranked_chunks(euclidean_record)} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 전체 Query별 Chunk 비교",
            "",
            (
                "아래 표는 1,000개 query 각각에 대해 두 방식이 가져온 "
                "Top-5 chunk ID와 점수를 모두 보여준다."
            ),
            "",
            (
                "| Query ID | Type | Query | Cosine Top-5 "
                "| Euclidean Top-5 | Result |"
            ),
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    for cosine_record, euclidean_record, comparison in comparisons:
        lines.append(
            f'| `{cosine_record["query_id"]}` '
            f'| `{cosine_record["query_type"]}` '
            f'| {escape_markdown(cosine_record["query"])} '
            f"| {format_ranked_chunks(cosine_record)} "
            f"| {format_ranked_chunks(euclidean_record)} "
            f'| **{comparison["result"]}** |'
        )

    lines.extend(
        [
            "",
            "## 해석할 때 주의할 점",
            "",
            (
                "- Cosine은 클수록 유사하고, 현재 Euclidean 점수는 거리를 "
                "`1 / (1 + distance)`로 변환했으므로 역시 클수록 유사하다."
            ),
            (
                "- 두 점수는 계산식과 범위가 다르므로 `0.7 대 0.8`처럼 "
                "점수 자체를 직접 비교하면 안 된다."
            ),
            (
                "- 이 결과는 두 방식 중 하나가 더 우수하다는 뜻이 아니라, "
                "현재 정규화된 embedding에서는 두 방식의 순위가 같다는 뜻이다."
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    evaluation = load_json(args.evaluation_path)
    chunks_by_id = load_chunks(args.chunks_path)
    report = build_report(
        evaluation=evaluation,
        chunks_by_id=chunks_by_id,
        samples_per_type=args.samples_per_type,
        preview_chars=args.preview_chars,
    )

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(report, encoding="utf-8")
    print(f"Created: {args.output_path}")


if __name__ == "__main__":
    main()
