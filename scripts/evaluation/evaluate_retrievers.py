from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter
import argparse
import json
import math
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = (
    PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks_full.jsonl"
)
QUERIES_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_queries_test.jsonl"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_evaluation_test.json"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_evaluation_test.md"
)
DENSE_EMBEDDINGS_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wikipedia_ollama_embeddings_full.json"
)
QUERY_EMBEDDINGS_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wikipedia_ollama_query_embeddings_test.json"
)

if str(RETRIEVAL_DIR) not in sys.path:
    sys.path.append(str(RETRIEVAL_DIR))

import bm25_retriever
import dense_ollama_retriever
import hybrid_retriever
import score_fusion_retriever
import tfidf_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_METHODS = [
    "bm25",
    "tfidf",
    "dense",
    "hybrid",
    "score_fusion",
]
METRIC_K_VALUES = (1, 3, 5)


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


def validate_queries(queries: list[dict], chunks: list[dict]) -> None:
    required_fields = {
        "query_id",
        "query",
        "query_type",
        "difficulty",
        "expected_entity",
        "relevant_chunk_ids",
    }
    known_chunk_ids = {chunk["chunk_id"] for chunk in chunks}
    query_ids = set()

    for query in queries:
        missing_fields = required_fields - set(query)
        if missing_fields:
            raise ValueError(
                f"{query.get('query_id', '<unknown>')} is missing fields: "
                f"{sorted(missing_fields)}"
            )
        if query["query_id"] in query_ids:
            raise ValueError(f"Duplicate query_id: {query['query_id']}")
        query_ids.add(query["query_id"])

        if not query["relevant_chunk_ids"]:
            raise ValueError(f"{query['query_id']} has no relevant chunks")
        unknown_ids = set(query["relevant_chunk_ids"]) - known_chunk_ids
        if unknown_ids:
            raise ValueError(
                f"{query['query_id']} references unknown chunks: {sorted(unknown_ids)}"
            )


def limit_queries_per_type(queries: list[dict], limit: int) -> list[dict]:
    counts = Counter()
    selected = []
    for query in queries:
        query_type = query["query_type"]
        if counts[query_type] >= limit:
            continue
        selected.append(query)
        counts[query_type] += 1
    return selected


def build_retrieval_state(args, chunks: list[dict]) -> dict:
    state = {}
    needs_bm25 = any(
        method in args.methods
        for method in ("bm25", "hybrid", "score_fusion")
    )
    needs_dense = any(
        method in args.methods
        for method in ("dense", "hybrid", "score_fusion")
    )

    if needs_bm25:
        state["bm25"] = bm25_retriever.build_bm25(chunks)

    if "tfidf" in args.methods:
        vectorizer, matrix = tfidf_retriever.build_tfidf(chunks)
        state["tfidf_vectorizer"] = vectorizer
        state["tfidf_matrix"] = matrix

    if needs_dense:
        dense_ollama_retriever.check_ollama(args.ollama_url, args.timeout)
        embeddings = dense_ollama_retriever.build_or_load_embeddings(
            chunks=chunks,
            model=args.embedding_model,
            ollama_url=args.ollama_url,
            cache_path=args.dense_cache,
            rebuild_cache=args.rebuild_dense_cache,
            timeout=args.timeout,
        )
        matrix = np.asarray(
            [item["embedding"] for item in embeddings],
            dtype=np.float32,
        )
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        state["dense_matrix"] = matrix / norms

    return state


def load_query_embedding_cache(path: Path, model: str) -> dict[str, list[float]]:
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as file:
        cache = json.load(file)
    if cache.get("model") != model:
        return {}
    return cache.get("embeddings", {})


def save_query_embedding_cache(
    path: Path,
    model: str,
    embeddings: dict[str, list[float]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    payload = {
        "model": model,
        "embeddings": embeddings,
    }
    temporary_path.write_text(
        json.dumps(payload, ensure_ascii=False),
        encoding="utf-8",
    )
    temporary_path.replace(path)


def prepare_query_embeddings(
    queries: list[dict],
    args,
) -> dict[str, list[float]]:
    needs_dense = any(
        method in args.methods
        for method in ("dense", "hybrid", "score_fusion")
    )
    if not needs_dense:
        return {}

    cache = load_query_embedding_cache(
        args.query_embedding_cache,
        args.embedding_model,
    )
    query_texts = list(dict.fromkeys(query["query"] for query in queries))
    missing_texts = [text for text in query_texts if text not in cache]

    if not missing_texts:
        print(f"Loaded {len(query_texts)} query embeddings from cache.")
        return {text: cache[text] for text in query_texts}

    print(
        f"Embedding {len(missing_texts)} uncached queries "
        f"in batches of {args.query_batch_size}..."
    )
    for start in range(0, len(missing_texts), args.query_batch_size):
        batch = missing_texts[start : start + args.query_batch_size]
        batch_embeddings = dense_ollama_retriever.embed_texts(
            texts=batch,
            model=args.embedding_model,
            ollama_url=args.ollama_url,
            timeout=args.timeout,
        )
        cache.update(zip(batch, batch_embeddings))
        save_query_embedding_cache(
            args.query_embedding_cache,
            args.embedding_model,
            cache,
        )
        completed = min(start + len(batch), len(missing_texts))
        print(f"  Query embeddings: {completed}/{len(missing_texts)}")

    return {text: cache[text] for text in query_texts}


def dense_search_from_embedding(
    query_embedding: list[float],
    chunks: list[dict],
    normalized_matrix: np.ndarray,
    top_k: int,
) -> list[dict]:
    query_vector = np.asarray(query_embedding, dtype=np.float32)
    query_norm = float(np.linalg.norm(query_vector))
    if query_norm == 0:
        scores = np.zeros(len(chunks), dtype=np.float32)
    else:
        scores = normalized_matrix @ (query_vector / query_norm)

    ranked_indices = np.argsort(-scores, kind="stable")[:top_k]
    return [
        {
            "score": float(scores[index]),
            "chunk_id": chunks[index]["chunk_id"],
            "source": chunks[index]["source"],
            "page": chunks[index]["page"],
            "chunk_index": chunks[index]["chunk_index"],
            "text": chunks[index]["text"],
        }
        for index in ranked_indices
    ]


def retrieve_once(
    query_text: str,
    query_embedding: list[float] | None,
    args,
    chunks: list[dict],
    state: dict,
    top_k: int,
) -> dict[str, tuple[list[dict], float]]:
    candidate_k = max(args.candidate_k, top_k)
    bm25_results = None
    dense_results = None
    bm25_ms = 0.0
    dense_ms = 0.0
    retrieved = {}

    if "bm25" in state:
        started = perf_counter()
        bm25_results = bm25_retriever.search(
            query_text,
            chunks,
            state["bm25"],
            candidate_k,
        )
        bm25_ms = (perf_counter() - started) * 1000

    if "tfidf_vectorizer" in state:
        started = perf_counter()
        tfidf_results = tfidf_retriever.search(
            query_text,
            chunks,
            state["tfidf_vectorizer"],
            state["tfidf_matrix"],
            top_k,
            metric="cosine",
        )
        retrieved["tfidf"] = (
            tfidf_results,
            (perf_counter() - started) * 1000,
        )

    if "dense_matrix" in state:
        if query_embedding is None:
            raise ValueError("Dense retrieval requires a query embedding")
        started = perf_counter()
        dense_results = dense_search_from_embedding(
            query_embedding,
            chunks,
            state["dense_matrix"],
            candidate_k,
        )
        dense_ms = (perf_counter() - started) * 1000

    if "bm25" in args.methods:
        retrieved["bm25"] = (bm25_results[:top_k], bm25_ms)
    if "dense" in args.methods:
        retrieved["dense"] = (dense_results[:top_k], dense_ms)

    if "hybrid" in args.methods:
        started = perf_counter()
        results = hybrid_retriever.rrf_fusion(
            chunks=chunks,
            bm25_results=bm25_results,
            dense_results=dense_results,
            top_k=top_k,
            rrf_k=args.rrf_k,
            bm25_weight=args.bm25_weight,
            dense_weight=args.dense_weight,
        )
        fusion_ms = (perf_counter() - started) * 1000
        retrieved["hybrid"] = (results, bm25_ms + dense_ms + fusion_ms)

    if "score_fusion" in args.methods:
        started = perf_counter()
        results = score_fusion_retriever.score_fusion(
            chunks=chunks,
            bm25_results=bm25_results,
            dense_results=dense_results,
            top_k=top_k,
            bm25_weight=args.bm25_weight,
            dense_weight=args.dense_weight,
        )
        fusion_ms = (perf_counter() - started) * 1000
        retrieved["score_fusion"] = (
            results,
            bm25_ms + dense_ms + fusion_ms,
        )

    return retrieved


def first_rank(values: list[str], relevant_values: set[str], top_k: int) -> int | None:
    for rank, value in enumerate(values[:top_k], start=1):
        if value in relevant_values:
            return rank
    return None


def reciprocal_rank(rank: int | None) -> float:
    return 0.0 if rank is None else 1.0 / rank


def discounted_gain(rank: int | None) -> float:
    return 0.0 if rank is None else 1.0 / math.log2(rank + 1)


def evaluate_query(
    query: dict,
    results: list[dict],
    chunk_entity_by_id: dict[str, str],
    top_k: int,
    elapsed_ms: float,
) -> dict:
    result_ids = [result["chunk_id"] for result in results]
    result_entities = [chunk_entity_by_id[chunk_id] for chunk_id in result_ids]
    relevant_ids = set(query["relevant_chunk_ids"])
    expected_entities = {query["expected_entity"]}

    chunk_rank = first_rank(result_ids, relevant_ids, top_k)
    entity_rank = first_rank(result_entities, expected_entities, top_k)

    return {
        "query_id": query["query_id"],
        "query": query["query"],
        "query_type": query["query_type"],
        "difficulty": query["difficulty"],
        "expected_entity": query["expected_entity"],
        "relevant_chunk_ids": query["relevant_chunk_ids"],
        "chunk_rank": chunk_rank,
        "entity_rank": entity_rank,
        "elapsed_ms": elapsed_ms,
        "results": [
            {
                "rank": rank,
                "chunk_id": result["chunk_id"],
                "entity": chunk_entity_by_id[result["chunk_id"]],
                "score": float(result["score"]),
            }
            for rank, result in enumerate(results, start=1)
        ],
    }


def aggregate_records(records: list[dict], max_k: int) -> dict:
    count = len(records)
    if count == 0:
        return {"query_count": 0}

    metrics = {"query_count": count}
    for k in METRIC_K_VALUES:
        if k > max_k:
            continue
        metrics[f"chunk_hit_at_{k}"] = sum(
            record["chunk_rank"] is not None and record["chunk_rank"] <= k
            for record in records
        ) / count
        metrics[f"entity_hit_at_{k}"] = sum(
            record["entity_rank"] is not None and record["entity_rank"] <= k
            for record in records
        ) / count

    metrics[f"chunk_mrr_at_{max_k}"] = sum(
        reciprocal_rank(record["chunk_rank"]) for record in records
    ) / count
    metrics[f"entity_mrr_at_{max_k}"] = sum(
        reciprocal_rank(record["entity_rank"]) for record in records
    ) / count
    metrics[f"chunk_ndcg_at_{max_k}"] = sum(
        discounted_gain(record["chunk_rank"]) for record in records
    ) / count
    metrics["avg_latency_ms"] = sum(record["elapsed_ms"] for record in records) / count
    return metrics


def aggregate_by_field(
    records: list[dict],
    field: str,
    max_k: int,
) -> dict[str, dict]:
    grouped = defaultdict(list)
    for record in records:
        grouped[record[field]].append(record)
    return {
        key: aggregate_records(group, max_k)
        for key, group in sorted(grouped.items())
    }


def evaluate_all(
    queries: list[dict],
    query_embeddings: dict[str, list[float]],
    args,
    chunks: list[dict],
    state: dict,
    top_k: int,
) -> tuple[dict[str, list[dict]], dict[str, dict]]:
    chunk_entity_by_id = {
        chunk["chunk_id"]: chunk["entity"]
        for chunk in chunks
    }
    records_by_method = {method: [] for method in args.methods}

    print(
        f"\nEvaluating {len(args.methods)} methods "
        f"on {len(queries)} queries with shared retrieval..."
    )
    for index, query in enumerate(queries, start=1):
        query_embedding = query_embeddings.get(query["query"])
        retrieved = retrieve_once(
            query_text=query["query"],
            query_embedding=query_embedding,
            args=args,
            chunks=chunks,
            state=state,
            top_k=top_k,
        )
        for method in args.methods:
            results, elapsed_ms = retrieved[method]
            records_by_method[method].append(
                evaluate_query(
                    query=query,
                    results=results,
                    chunk_entity_by_id=chunk_entity_by_id,
                    top_k=top_k,
                    elapsed_ms=elapsed_ms,
                )
            )
        if index % 10 == 0 or index == len(queries):
            print(f"  Queries: {index}/{len(queries)}")

    summaries = {}
    for method, records in records_by_method.items():
        summaries[method] = {
            "overall": aggregate_records(records, top_k),
            "by_query_type": aggregate_by_field(records, "query_type", top_k),
            "by_difficulty": aggregate_by_field(records, "difficulty", top_k),
        }

    return records_by_method, summaries


def best_method(summaries: dict[str, dict], top_k: int) -> str:
    metric = f"chunk_mrr_at_{top_k}"
    return max(
        summaries,
        key=lambda method: (
            summaries[method]["overall"][metric],
            summaries[method]["overall"][f"entity_mrr_at_{top_k}"],
            -summaries[method]["overall"]["avg_latency_ms"],
        ),
    )


def query_win_counts(
    records_by_method: dict[str, list[dict]],
    rank_field: str,
) -> Counter:
    wins = Counter()
    methods = list(records_by_method)
    for record_index in range(len(next(iter(records_by_method.values())))):
        ranks = {
            method: records_by_method[method][record_index][rank_field]
            for method in methods
        }
        valid_ranks = [rank for rank in ranks.values() if rank is not None]
        if not valid_ranks:
            continue
        best_rank = min(valid_ranks)
        for method, rank in ranks.items():
            if rank == best_rank:
                wins[method] += 1
    return wins


def format_percent(value: float) -> str:
    return f"{value * 100:.1f}%"


def format_float(value: float) -> str:
    return f"{value:.4f}"


def write_report(
    path: Path,
    queries: list[dict],
    methods: list[str],
    records_by_method: dict[str, list[dict]],
    summaries: dict[str, dict],
    top_k: int,
) -> None:
    primary_metric = f"chunk_mrr_at_{top_k}"
    winning_method = best_method(summaries, top_k)
    chunk_wins = query_win_counts(records_by_method, "chunk_rank")
    entity_wins = query_win_counts(records_by_method, "entity_rank")
    query_types = sorted({query["query_type"] for query in queries})
    difficulties = sorted({query["difficulty"] for query in queries})

    lines = [
        "# Wikipedia Retriever Evaluation",
        "",
        "## Evaluation Setup",
        "",
        f"- Queries: {len(queries)}",
        f"- Wikipedia entities: {len({query['expected_entity'] for query in queries})}",
        f"- Final retrieval depth: Top-{top_k}",
        f"- Methods: {', '.join(methods)}",
        "- Primary metric: chunk-level MRR",
        "- Article metrics count any chunk from the expected Wikipedia entity as relevant.",
        "",
        "## Overall Result",
        "",
        f"**Best method by {primary_metric}: {winning_method}**",
        "",
        "| Method | Chunk Hit@1 | Chunk Hit@3 | Chunk Hit@5 | Chunk MRR | Chunk nDCG | Article Hit@1 | Article Hit@5 | Article MRR | Avg search ms/query |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for method in methods:
        metrics = summaries[method]["overall"]
        lines.append(
            f"| {method} | "
            f"{format_percent(metrics.get('chunk_hit_at_1', 0.0))} | "
            f"{format_percent(metrics.get('chunk_hit_at_3', 0.0))} | "
            f"{format_percent(metrics.get('chunk_hit_at_5', 0.0))} | "
            f"{format_float(metrics[primary_metric])} | "
            f"{format_float(metrics[f'chunk_ndcg_at_{top_k}'])} | "
            f"{format_percent(metrics.get('entity_hit_at_1', 0.0))} | "
            f"{format_percent(metrics.get('entity_hit_at_5', 0.0))} | "
            f"{format_float(metrics[f'entity_mrr_at_{top_k}'])} | "
            f"{metrics['avg_latency_ms']:.1f} |"
        )

    lines.extend(
        [
            "",
            "## Query-Type Result",
            "",
            "| Query type | Method | Queries | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR | Article Hit@1 | Article Hit@5 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for query_type in query_types:
        for method in methods:
            metrics = summaries[method]["by_query_type"][query_type]
            lines.append(
                f"| {query_type} | {method} | {metrics['query_count']} | "
                f"{format_percent(metrics.get('chunk_hit_at_1', 0.0))} | "
                f"{format_percent(metrics.get('chunk_hit_at_5', 0.0))} | "
                f"{format_float(metrics[primary_metric])} | "
                f"{format_percent(metrics.get('entity_hit_at_1', 0.0))} | "
                f"{format_percent(metrics.get('entity_hit_at_5', 0.0))} |"
            )

    lines.extend(
        [
            "",
            "## Difficulty Result",
            "",
            "| Difficulty | Method | Queries | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR | Article Hit@1 | Article Hit@5 |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for difficulty in difficulties:
        for method in methods:
            metrics = summaries[method]["by_difficulty"][difficulty]
            lines.append(
                f"| {difficulty} | {method} | {metrics['query_count']} | "
                f"{format_percent(metrics.get('chunk_hit_at_1', 0.0))} | "
                f"{format_percent(metrics.get('chunk_hit_at_5', 0.0))} | "
                f"{format_float(metrics[primary_metric])} | "
                f"{format_percent(metrics.get('entity_hit_at_1', 0.0))} | "
                f"{format_percent(metrics.get('entity_hit_at_5', 0.0))} |"
            )

    lines.extend(
        [
            "",
            "## Best-Rank Counts",
            "",
            "Ties give one win to every method sharing the best rank.",
            "",
            "| Method | Best chunk rank | Best article rank |",
            "| --- | ---: | ---: |",
        ]
    )
    for method in methods:
        lines.append(
            f"| {method} | {chunk_wins[method]} | {entity_wins[method]} |"
        )

    lines.extend(["", "## All-Method Failures", ""])
    all_failed = []
    for query_index, query in enumerate(queries):
        if all(
            records_by_method[method][query_index]["entity_rank"] is None
            for method in methods
        ):
            all_failed.append(query)

    if all_failed:
        lines.append("| ID | Type | Expected entity | Query |")
        lines.append("| --- | --- | --- | --- |")
        for query in all_failed:
            safe_query = query["query"].replace("|", "\\|")
            lines.append(
                f"| {query['query_id']} | {query['query_type']} | "
                f"{query['expected_entity']} | {safe_query} |"
            )
    else:
        lines.append("Every query retrieved the expected article in Top-k with at least one method.")

    lines.extend(
        [
            "",
            "## Interpretation Notes",
            "",
            "- Chunk-level metrics are stricter: only the labeled answer chunk is correct.",
            "- Article-level metrics are more forgiving: another chunk from the correct Wikipedia page is accepted.",
            "- Scores from different retrievers are not directly comparable because their score scales differ.",
            "- Search latency excludes query embedding time because query embeddings are batched and cached for evaluation.",
            "- Automatically generated queries should be human-reviewed before reporting final benchmark results.",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate Wikipedia retrievers with labeled queries."
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        choices=DEFAULT_METHODS,
        default=DEFAULT_METHODS,
        help="Retrieval methods to evaluate",
    )
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--limit", type=int, help="Evaluate only the first N queries")
    parser.add_argument(
        "--per-type-limit",
        type=int,
        help="Evaluate the first N queries from every query type",
    )
    parser.add_argument("--chunks", type=Path, default=CHUNKS_PATH)
    parser.add_argument("--queries", type=Path, default=QUERIES_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument(
        "--dense-cache",
        type=Path,
        default=DENSE_EMBEDDINGS_PATH,
    )
    parser.add_argument(
        "--query-embedding-cache",
        type=Path,
        default=QUERY_EMBEDDINGS_PATH,
    )
    parser.add_argument(
        "--query-batch-size",
        type=int,
        default=32,
        help="Number of query texts sent to Ollama per embedding request",
    )
    parser.add_argument("--embedding-model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-dense-cache", action="store_true")
    parser.add_argument("--candidate-k", type=int, default=20)
    parser.add_argument("--rrf-k", type=int, default=hybrid_retriever.DEFAULT_RRF_K)
    parser.add_argument(
        "--bm25-weight",
        type=float,
        default=hybrid_retriever.DEFAULT_BM25_WEIGHT,
    )
    parser.add_argument(
        "--dense-weight",
        type=float,
        default=hybrid_retriever.DEFAULT_DENSE_WEIGHT,
    )
    return parser


def validate_args(args, parser: argparse.ArgumentParser) -> None:
    positive_values = {
        "--top-k": args.top_k,
        "--candidate-k": args.candidate_k,
        "--rrf-k": args.rrf_k,
        "--timeout": args.timeout,
        "--query-batch-size": args.query_batch_size,
    }
    if args.limit is not None:
        positive_values["--limit"] = args.limit
    if args.per_type_limit is not None:
        positive_values["--per-type-limit"] = args.per_type_limit

    for option, value in positive_values.items():
        if value <= 0:
            parser.error(f"{option} must be greater than zero")

    if args.limit is not None and args.per_type_limit is not None:
        parser.error("--limit and --per-type-limit cannot be used together")

    if args.top_k < max(METRIC_K_VALUES):
        parser.error(f"--top-k must be at least {max(METRIC_K_VALUES)}")

    try:
        hybrid_retriever.validate_weights(args.bm25_weight, args.dense_weight)
    except ValueError as exc:
        parser.error(str(exc))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)

    chunks = bm25_retriever.load_chunks(args.chunks)
    queries = load_jsonl(args.queries)
    validate_queries(queries, chunks)
    if args.limit:
        queries = queries[: args.limit]
    elif args.per_type_limit:
        queries = limit_queries_per_type(queries, args.per_type_limit)

    try:
        state = build_retrieval_state(args, chunks)
        query_embeddings = prepare_query_embeddings(queries, args)
    except RuntimeError as exc:
        parser.error(str(exc))

    records_by_method, summaries = evaluate_all(
        queries=queries,
        query_embeddings=query_embeddings,
        args=args,
        chunks=chunks,
        state=state,
        top_k=args.top_k,
    )

    result = {
        "configuration": {
            "query_count": len(queries),
            "top_k": args.top_k,
            "methods": args.methods,
            "embedding_model": args.embedding_model,
            "candidate_k": args.candidate_k,
            "chunks": str(args.chunks),
            "queries": str(args.queries),
            "dense_cache": str(args.dense_cache),
            "query_embedding_cache": str(args.query_embedding_cache),
            "query_batch_size": args.query_batch_size,
        },
        "best_method": best_method(summaries, args.top_k),
        "summaries": summaries,
        "records": records_by_method,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_report(
        path=args.report,
        queries=queries,
        methods=args.methods,
        records_by_method=records_by_method,
        summaries=summaries,
        top_k=args.top_k,
    )

    print(f"\nBest method: {result['best_method']}")
    print(f"Saved JSON: {args.output}")
    print(f"Saved report: {args.report}")


if __name__ == "__main__":
    main()
