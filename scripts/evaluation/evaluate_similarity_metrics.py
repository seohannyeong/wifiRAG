from collections import defaultdict
from pathlib import Path
from time import perf_counter
import argparse
import json
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks_full.jsonl"
QUERIES_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_queries_test.jsonl"
)
DENSE_CACHE_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wikipedia_ollama_embeddings_full.json"
)
QUERY_CACHE_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wikipedia_ollama_query_embeddings_test.json"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_similarity_metric_evaluation_980.json"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_similarity_metric_evaluation_980.md"
)

if str(RETRIEVAL_DIR) not in sys.path:
    sys.path.append(str(RETRIEVAL_DIR))

import dense_ollama_retriever
import evaluate_retrievers as common
import tfidf_retriever


METHODS = (
    "dense_cosine",
    "dense_euclidean",
    "tfidf_cosine_l2",
    "tfidf_euclidean_l2",
    "tfidf_euclidean_no_norm",
)
METHOD_LABELS = {
    "dense_cosine": "Dense Cosine",
    "dense_euclidean": "Dense Euclidean",
    "tfidf_cosine_l2": "TF-IDF Cosine L2",
    "tfidf_euclidean_l2": "TF-IDF Euclidean L2",
    "tfidf_euclidean_no_norm": "TF-IDF Euclidean No Norm",
}


def load_dense_matrices(
    path: Path,
    chunks: list[dict],
    model: str,
) -> tuple[np.ndarray, np.ndarray, dict]:
    with path.open("r", encoding="utf-8") as file:
        cache = json.load(file)
    if not dense_ollama_retriever.cache_matches(cache, chunks, model):
        raise ValueError(
            "Dense cache does not match the selected chunks or embedding model."
        )

    raw_matrix = np.asarray(
        [item["embedding"] for item in cache["embeddings"]],
        dtype=np.float32,
    )
    norms = np.linalg.norm(raw_matrix, axis=1)
    safe_norms = np.where(norms == 0, 1.0, norms)
    normalized_matrix = raw_matrix / safe_norms[:, np.newaxis]
    norm_summary = {
        "minimum": float(norms.min()),
        "maximum": float(norms.max()),
        "mean": float(norms.mean()),
        "standard_deviation": float(norms.std()),
    }
    return raw_matrix, normalized_matrix, norm_summary


def dense_scores(
    query_embedding: list[float],
    raw_matrix: np.ndarray,
    normalized_matrix: np.ndarray,
    metric: str,
) -> np.ndarray:
    query_vector = np.asarray(query_embedding, dtype=np.float32)

    if metric == "cosine":
        query_norm = float(np.linalg.norm(query_vector))
        if query_norm == 0:
            return np.zeros(len(raw_matrix), dtype=np.float32)
        return normalized_matrix @ (query_vector / query_norm)

    if metric == "euclidean":
        query_squared_norm = float(query_vector @ query_vector)
        document_squared_norms = np.einsum(
            "ij,ij->i",
            raw_matrix,
            raw_matrix,
        )
        squared_distances = (
            document_squared_norms
            + query_squared_norm
            - 2 * (raw_matrix @ query_vector)
        )
        distances = np.sqrt(np.maximum(squared_distances, 0.0))
        return 1 / (1 + distances)

    raise ValueError(f"Unknown dense metric: {metric}")


def results_from_scores(
    scores: np.ndarray | list[float],
    chunks: list[dict],
    top_k: int,
) -> list[dict]:
    score_array = np.asarray(scores)
    ranked_indices = np.argsort(-score_array, kind="stable")[:top_k]
    return [
        {
            "score": float(score_array[index]),
            "chunk_id": chunks[index]["chunk_id"],
            "source": chunks[index]["source"],
            "page": chunks[index]["page"],
            "chunk_index": chunks[index]["chunk_index"],
            "text": chunks[index]["text"],
        }
        for index in ranked_indices
    ]


def build_tfidf_state(chunks: list[dict]) -> dict:
    l2_vectorizer, l2_matrix = tfidf_retriever.build_tfidf(
        chunks,
        normalize=True,
    )
    raw_vectorizer, raw_matrix = tfidf_retriever.build_tfidf(
        chunks,
        normalize=False,
    )
    raw_norms = np.sqrt(raw_matrix.multiply(raw_matrix).sum(axis=1)).A1
    return {
        "l2_vectorizer": l2_vectorizer,
        "l2_matrix": l2_matrix,
        "raw_vectorizer": raw_vectorizer,
        "raw_matrix": raw_matrix,
        "raw_norm_summary": {
            "minimum": float(raw_norms.min()),
            "maximum": float(raw_norms.max()),
            "mean": float(raw_norms.mean()),
            "standard_deviation": float(raw_norms.std()),
        },
    }


def retrieve_all_metrics(
    query_text: str,
    query_embedding: list[float],
    chunks: list[dict],
    raw_dense_matrix: np.ndarray,
    normalized_dense_matrix: np.ndarray,
    tfidf_state: dict,
    top_k: int,
) -> dict[str, tuple[list[dict], float]]:
    retrieved = {}

    for method, metric in (
        ("dense_cosine", "cosine"),
        ("dense_euclidean", "euclidean"),
    ):
        started = perf_counter()
        scores = dense_scores(
            query_embedding,
            raw_dense_matrix,
            normalized_dense_matrix,
            metric,
        )
        results = results_from_scores(scores, chunks, top_k)
        retrieved[method] = (
            results,
            (perf_counter() - started) * 1000,
        )

    tfidf_settings = (
        (
            "tfidf_cosine_l2",
            tfidf_state["l2_vectorizer"],
            tfidf_state["l2_matrix"],
            "cosine",
        ),
        (
            "tfidf_euclidean_l2",
            tfidf_state["l2_vectorizer"],
            tfidf_state["l2_matrix"],
            "euclidean",
        ),
        (
            "tfidf_euclidean_no_norm",
            tfidf_state["raw_vectorizer"],
            tfidf_state["raw_matrix"],
            "euclidean",
        ),
    )
    for method, vectorizer, matrix, metric in tfidf_settings:
        started = perf_counter()
        results = tfidf_retriever.search(
            query=query_text,
            chunks=chunks,
            vectorizer=vectorizer,
            matrix=matrix,
            top_k=top_k,
            metric=metric,
        )
        retrieved[method] = (
            results,
            (perf_counter() - started) * 1000,
        )

    return retrieved


def evaluate(
    queries: list[dict],
    chunks: list[dict],
    query_embeddings: dict[str, list[float]],
    raw_dense_matrix: np.ndarray,
    normalized_dense_matrix: np.ndarray,
    tfidf_state: dict,
    top_k: int,
) -> tuple[dict[str, list[dict]], dict[str, dict]]:
    chunk_entity_by_id = {
        chunk["chunk_id"]: chunk["entity"]
        for chunk in chunks
    }
    records = {method: [] for method in METHODS}

    for index, query in enumerate(queries, start=1):
        retrieved = retrieve_all_metrics(
            query_text=query["query"],
            query_embedding=query_embeddings[query["query"]],
            chunks=chunks,
            raw_dense_matrix=raw_dense_matrix,
            normalized_dense_matrix=normalized_dense_matrix,
            tfidf_state=tfidf_state,
            top_k=top_k,
        )
        for method in METHODS:
            results, elapsed_ms = retrieved[method]
            records[method].append(
                common.evaluate_query(
                    query=query,
                    results=results,
                    chunk_entity_by_id=chunk_entity_by_id,
                    top_k=top_k,
                    elapsed_ms=elapsed_ms,
                )
            )
        if index % 50 == 0 or index == len(queries):
            print(f"Queries: {index}/{len(queries)}")

    summaries = {
        method: {
            "overall": common.aggregate_records(method_records, top_k),
            "by_query_type": common.aggregate_by_field(
                method_records,
                "query_type",
                top_k,
            ),
        }
        for method, method_records in records.items()
    }
    return records, summaries


def ranking_agreement(
    left_records: list[dict],
    right_records: list[dict],
    top_k: int,
) -> dict:
    top1_same = 0
    ordered_top_k_same = 0
    overlap_sum = 0

    for left, right in zip(left_records, right_records):
        left_ids = [result["chunk_id"] for result in left["results"][:top_k]]
        right_ids = [result["chunk_id"] for result in right["results"][:top_k]]
        top1_same += left_ids[0] == right_ids[0]
        ordered_top_k_same += left_ids == right_ids
        overlap_sum += len(set(left_ids) & set(right_ids))

    count = len(left_records)
    return {
        "query_count": count,
        "top1_same_rate": top1_same / count,
        "ordered_top_k_same_rate": ordered_top_k_same / count,
        "average_top_k_overlap": overlap_sum / count,
    }


def format_percent(value: float) -> str:
    return f"{value * 100:.1f}%"


def write_report(
    path: Path,
    queries: list[dict],
    summaries: dict[str, dict],
    agreements: dict[str, dict],
    dense_norms: dict,
    tfidf_raw_norms: dict,
    top_k: int,
) -> None:
    query_types = sorted({query["query_type"] for query in queries})
    lines = [
        "# Wikipedia Similarity Metric Evaluation",
        "",
        "## Setup",
        "",
        f"- Corpus: 980 entities, 6,488 chunks",
        f"- Queries: {len(queries)}",
        f"- Retrieval depth: Top-{top_k}",
        "- Dense document and query embeddings are reused from the nomic-embed-text cache.",
        "",
        "## Overall Result",
        "",
        "| Method | Chunk Hit@1 | Chunk Hit@3 | Chunk Hit@5 | Chunk MRR | Article Hit@5 | Avg search ms |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for method in METHODS:
        metrics = summaries[method]["overall"]
        lines.append(
            f"| {METHOD_LABELS[method]} | "
            f"{format_percent(metrics['chunk_hit_at_1'])} | "
            f"{format_percent(metrics['chunk_hit_at_3'])} | "
            f"{format_percent(metrics['chunk_hit_at_5'])} | "
            f"{metrics[f'chunk_mrr_at_{top_k}']:.4f} | "
            f"{format_percent(metrics['entity_hit_at_5'])} | "
            f"{metrics['avg_latency_ms']:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Ranking Agreement",
            "",
            "| Pair | Top-1 same | Ordered Top-5 same | Average Top-5 overlap |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    agreement_labels = {
        "dense_cosine_vs_euclidean": "Dense cosine vs Euclidean",
        "tfidf_cosine_vs_euclidean_l2": "TF-IDF cosine L2 vs Euclidean L2",
        "tfidf_cosine_vs_euclidean_no_norm": "TF-IDF cosine L2 vs Euclidean without normalization",
    }
    for name, agreement in agreements.items():
        lines.append(
            f"| {agreement_labels[name]} | "
            f"{format_percent(agreement['top1_same_rate'])} | "
            f"{format_percent(agreement['ordered_top_k_same_rate'])} | "
            f"{agreement['average_top_k_overlap']:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Query-Type Result",
            "",
            "| Query type | Method | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for query_type in query_types:
        for method in METHODS:
            metrics = summaries[method]["by_query_type"][query_type]
            lines.append(
                f"| {query_type} | {METHOD_LABELS[method]} | "
                f"{format_percent(metrics['chunk_hit_at_1'])} | "
                f"{format_percent(metrics['chunk_hit_at_5'])} | "
                f"{metrics[f'chunk_mrr_at_{top_k}']:.4f} |"
            )

    lines.extend(
        [
            "",
            "## Vector Norms",
            "",
            "| Vector | Minimum | Maximum | Mean | Standard deviation |",
            "| --- | ---: | ---: | ---: | ---: |",
            f"| Dense document embedding | {dense_norms['minimum']:.6f} | "
            f"{dense_norms['maximum']:.6f} | {dense_norms['mean']:.6f} | "
            f"{dense_norms['standard_deviation']:.6f} |",
            f"| TF-IDF document vector without normalization | "
            f"{tfidf_raw_norms['minimum']:.4f} | "
            f"{tfidf_raw_norms['maximum']:.4f} | "
            f"{tfidf_raw_norms['mean']:.4f} | "
            f"{tfidf_raw_norms['standard_deviation']:.4f} |",
            "",
            "## Interpretation",
            "",
            "- For L2-normalized vectors, Euclidean distance and cosine similarity are monotonic transformations, so they should produce the same ranking.",
            "- Dense cosine and Euclidean can differ only when embedding norms differ enough to affect Euclidean distance.",
            "- TF-IDF Euclidean without normalization retains vector magnitude, so document length and term-weight magnitude can dominate semantic direction.",
            "- Search latency excludes the time needed to create a new query embedding.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate cosine, Euclidean, and normalization effects."
    )
    parser.add_argument("--chunks", type=Path, default=CHUNKS_PATH)
    parser.add_argument("--queries", type=Path, default=QUERIES_PATH)
    parser.add_argument("--dense-cache", type=Path, default=DENSE_CACHE_PATH)
    parser.add_argument("--query-cache", type=Path, default=QUERY_CACHE_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--per-type-limit", type=int)
    parser.add_argument(
        "--embedding-model",
        default=dense_ollama_retriever.DEFAULT_MODEL,
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.top_k < 5:
        raise SystemExit("--top-k must be at least 5")
    if args.per_type_limit is not None and args.per_type_limit <= 0:
        raise SystemExit("--per-type-limit must be greater than zero")

    chunks = common.load_jsonl(args.chunks)
    queries = common.load_jsonl(args.queries)
    common.validate_queries(queries, chunks)
    if args.per_type_limit:
        queries = common.limit_queries_per_type(queries, args.per_type_limit)

    query_embeddings = common.load_query_embedding_cache(
        args.query_cache,
        args.embedding_model,
    )
    missing_queries = [
        query["query"]
        for query in queries
        if query["query"] not in query_embeddings
    ]
    if missing_queries:
        raise SystemExit(
            f"Query embedding cache is missing {len(missing_queries)} queries."
        )

    raw_dense_matrix, normalized_dense_matrix, dense_norms = (
        load_dense_matrices(
            args.dense_cache,
            chunks,
            args.embedding_model,
        )
    )
    tfidf_state = build_tfidf_state(chunks)
    records, summaries = evaluate(
        queries=queries,
        chunks=chunks,
        query_embeddings=query_embeddings,
        raw_dense_matrix=raw_dense_matrix,
        normalized_dense_matrix=normalized_dense_matrix,
        tfidf_state=tfidf_state,
        top_k=args.top_k,
    )
    agreements = {
        "dense_cosine_vs_euclidean": ranking_agreement(
            records["dense_cosine"],
            records["dense_euclidean"],
            args.top_k,
        ),
        "tfidf_cosine_vs_euclidean_l2": ranking_agreement(
            records["tfidf_cosine_l2"],
            records["tfidf_euclidean_l2"],
            args.top_k,
        ),
        "tfidf_cosine_vs_euclidean_no_norm": ranking_agreement(
            records["tfidf_cosine_l2"],
            records["tfidf_euclidean_no_norm"],
            args.top_k,
        ),
    }

    result = {
        "configuration": {
            "query_count": len(queries),
            "chunk_count": len(chunks),
            "entity_count": len({chunk["entity"] for chunk in chunks}),
            "top_k": args.top_k,
            "embedding_model": args.embedding_model,
        },
        "dense_norms": dense_norms,
        "tfidf_raw_norms": tfidf_state["raw_norm_summary"],
        "agreements": agreements,
        "summaries": summaries,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_report(
        path=args.report,
        queries=queries,
        summaries=summaries,
        agreements=agreements,
        dense_norms=dense_norms,
        tfidf_raw_norms=tfidf_state["raw_norm_summary"],
        top_k=args.top_k,
    )
    print(f"Saved JSON: {args.output}")
    print(f"Saved report: {args.report}")


if __name__ == "__main__":
    main()
