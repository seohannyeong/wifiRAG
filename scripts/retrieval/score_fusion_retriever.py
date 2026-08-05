from pathlib import Path
import argparse
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"

RETRIEVAL_DIR = Path(__file__).resolve().parent
if str(RETRIEVAL_DIR) not in sys.path:
    sys.path.append(str(RETRIEVAL_DIR))

import bm25_retriever
import dense_ollama_retriever
import hybrid_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_CANDIDATE_K = 20 # bm25, dense가 top20을 뽑음
DEFAULT_BM25_WEIGHT = 1.0 #기본 가중치
DEFAULT_DENSE_WEIGHT = 1.0


def min_max_normalize(results: list[dict]) -> dict[str, float]:
    # Min-max normalization을 통해 점수를 0~1 범위로 변환
    if not results:
        return {}

    scores = [float(result["score"]) for result in results]
    minimum = min(scores)
    maximum = max(scores)

    if maximum == minimum:
        return {result["chunk_id"]: 0.0 for result in results}

    score_range = maximum - minimum
    return {
        result["chunk_id"]: (float(result["score"]) - minimum) / score_range
        for result in results
    }


def prepare_candidates(results: list[dict]) -> dict[str, dict]:
    # 후보 chunk들을 chunk_id를 key로 하는 dict로 변환
    normalized_scores = min_max_normalize(results)
    return {
        result["chunk_id"]: {
            "rank": rank,
            "raw_score": float(result["score"]),
            "normalized_score": normalized_scores[result["chunk_id"]],
        }
        for rank, result in enumerate(results, start=1)
    }


def weighted_score( # BM25와 Dense 점수를 가중합하여 최종 점수 계산
    bm25_score: float,
    dense_score: float,
    bm25_weight: float,
    dense_weight: float,
) -> float:
    weight_sum = bm25_weight + dense_weight
    return (
        bm25_weight * bm25_score
        + dense_weight * dense_score
    ) / weight_sum # fusion_score = (bm25_score + dense_score) / 2


def build_fused_result(
    chunk: dict,
    bm25_candidate: dict | None,
    dense_candidate: dict | None,
    bm25_weight: float,
    dense_weight: float,
) -> dict:
    """Combine one chunk's BM25 and dense candidate information."""
    bm25_score = (
        bm25_candidate["normalized_score"]
        if bm25_candidate
        else 0.0
    )
    dense_score = (
        dense_candidate["normalized_score"]
        if dense_candidate
        else 0.0
    )
    fusion_score = weighted_score(
        bm25_score=bm25_score,
        dense_score=dense_score,
        bm25_weight=bm25_weight,
        dense_weight=dense_weight,
    )

    return {
        "score": float(fusion_score),
        "chunk_id": chunk["chunk_id"],
        "source": chunk["source"],
        "page": chunk["page"],
        "chunk_index": chunk["chunk_index"],
        "bm25_rank": bm25_candidate["rank"] if bm25_candidate else None,
        "bm25_score": (
            bm25_candidate["raw_score"]
            if bm25_candidate
            else None
        ),
        "bm25_normalized": float(bm25_score),
        "bm25_contribution": float(bm25_weight * bm25_score),
        "dense_rank": dense_candidate["rank"] if dense_candidate else None,
        "dense_score": (
            dense_candidate["raw_score"]
            if dense_candidate
            else None
        ),
        "dense_normalized": float(dense_score),
        "dense_contribution": float(dense_weight * dense_score),
        "text": chunk["text"],
    }


def score_fusion(
    chunks: list[dict],
    bm25_results: list[dict],
    dense_results: list[dict],
    top_k: int,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
) -> list[dict]:
    hybrid_retriever.validate_weights(bm25_weight, dense_weight)
    chunk_by_id = {chunk["chunk_id"]: chunk for chunk in chunks}
    bm25_candidates = prepare_candidates(bm25_results)
    dense_candidates = prepare_candidates(dense_results)
    candidate_ids = bm25_candidates.keys() | dense_candidates.keys()

    fused_results = []
    for chunk_id in candidate_ids:
        fused_result = build_fused_result(
            chunk=chunk_by_id[chunk_id],
            bm25_candidate=bm25_candidates.get(chunk_id),
            dense_candidate=dense_candidates.get(chunk_id),
            bm25_weight=bm25_weight,
            dense_weight=dense_weight,
        )
        fused_results.append(fused_result)

    return sorted(
        fused_results,
        key=lambda item: (
            -item["score"],
            item["chunk_id"],
        ),
    )[:top_k]


def search(
    query: str,
    chunks: list[dict],
    bm25,
    embeddings: list[dict],
    model: str,
    ollama_url: str,
    timeout: int,
    top_k: int,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
) -> list[dict]:
    hybrid_retriever.validate_weights(bm25_weight, dense_weight)
    candidate_k = max(candidate_k, top_k)

    bm25_results = bm25_retriever.search(query, chunks, bm25, candidate_k)
    dense_results = dense_ollama_retriever.search(
        query=query,
        chunks=chunks,
        embeddings=embeddings,
        model=model,
        ollama_url=ollama_url,
        timeout=timeout,
        top_k=candidate_k,
        metric="cosine",
    )
    return score_fusion(
        chunks=chunks,
        bm25_results=bm25_results,
        dense_results=dense_results,
        top_k=top_k,
        bm25_weight=bm25_weight,
        dense_weight=dense_weight,
    )


def format_optional(value: float | int | None, digits: int = 4) -> str:
    if value is None:
        return "-"
    if isinstance(value, int):
        return str(value)
    return f"{value:.{digits}f}"


def print_results(query: str, results: list[dict]) -> None:
    print(f"Query: {query}")
    print()

    for rank, result in enumerate(results, start=1):
        preview = result["text"].replace("\n", " ")
        if len(preview) > 450:
            preview = preview[:450].rstrip() + "..."

        print(f"[{rank}] score_fusion={result['score']:.4f}")
        print(
            f"    chunk_id={result['chunk_id']} "
            f"page={result['page']} chunk_index={result['chunk_index']}"
        )
        print(
            f"    bm25_rank={format_optional(result['bm25_rank'])} "
            f"raw={format_optional(result['bm25_score'])} "
            f"normalized={result['bm25_normalized']:.4f} "
            f"contribution={result['bm25_contribution']:.4f}"
        )
        print(
            f"    dense_rank={format_optional(result['dense_rank'])} "
            f"raw={format_optional(result['dense_score'])} "
            f"normalized={result['dense_normalized']:.4f} "
            f"contribution={result['dense_contribution']:.4f}"
        )
        print(f"    {preview}")
        print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Search Wikipedia chunks with BM25 + dense min-max score fusion."
        )
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--candidate-k", type=int, default=DEFAULT_CANDIDATE_K)
    parser.add_argument("--bm25-weight", type=float, default=DEFAULT_BM25_WEIGHT)
    parser.add_argument("--dense-weight", type=float, default=DEFAULT_DENSE_WEIGHT)
    parser.add_argument("--model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-dense-cache", action="store_true")
    return parser


def validate_args(args, parser: argparse.ArgumentParser) -> None:
    for option, value in {
        "--top-k": args.top_k,
        "--candidate-k": args.candidate_k,
        "--timeout": args.timeout,
    }.items():
        if value <= 0:
            parser.error(f"{option} must be greater than zero")

    try:
        hybrid_retriever.validate_weights(args.bm25_weight, args.dense_weight)
    except ValueError as exc:
        parser.error(str(exc))


def prepare_retrievers(args) -> tuple[list[dict], object, list[dict]]:
    chunks = bm25_retriever.load_chunks(CHUNKS_PATH)
    bm25 = bm25_retriever.build_bm25(chunks)
    dense_ollama_retriever.check_ollama(args.ollama_url, args.timeout)
    embeddings = dense_ollama_retriever.build_or_load_embeddings(
        chunks=chunks,
        model=args.model,
        ollama_url=args.ollama_url,
        cache_path=dense_ollama_retriever.EMBEDDINGS_PATH,
        rebuild_cache=args.rebuild_dense_cache,
        timeout=args.timeout,
    )
    return chunks, bm25, embeddings


def search_and_print(
    query: str,
    args,
    chunks: list[dict],
    bm25,
    embeddings: list[dict],
) -> None:
    results = search(
        query=query,
        chunks=chunks,
        bm25=bm25,
        embeddings=embeddings,
        model=args.model,
        ollama_url=args.ollama_url,
        timeout=args.timeout,
        top_k=args.top_k,
        candidate_k=args.candidate_k,
        bm25_weight=args.bm25_weight,
        dense_weight=args.dense_weight,
    )
    print_results(query, results)


def interactive_search(args, chunks, bm25, embeddings) -> None:
    print("Score-fusion retriever is ready. Type a query, or type 'exit' to quit.")
    while True:
        query = input("\nQuery> ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            continue
        search_and_print(query, args, chunks, bm25, embeddings)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)
    chunks, bm25, embeddings = prepare_retrievers(args)

    if args.query:
        search_and_print(args.query, args, chunks, bm25, embeddings)
        return

    interactive_search(args, chunks, bm25, embeddings)


if __name__ == "__main__":
    main()
