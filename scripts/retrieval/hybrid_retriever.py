from pathlib import Path
import argparse
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"

if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.append(str(Path(__file__).resolve().parent))

import bm25_retriever
import dense_ollama_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_RRF_K = 60
DEFAULT_CANDIDATE_K = 20
DEFAULT_BM25_WEIGHT = 1.0
DEFAULT_DENSE_WEIGHT = 1.0


def load_chunks(path: Path) -> list[dict]:
    return bm25_retriever.load_chunks(path)


def index_results(results: list[dict]) -> dict[str, dict]:
    indexed = {}
    for rank, result in enumerate(results, start=1):
        indexed[result["chunk_id"]] = {
            "rank": rank,
            "score": result["score"],
        }
    return indexed


def reciprocal_rank(rank: int | None, rrf_k: int) -> float:
    if rank is None:
        return 0.0
    return 1 / (rrf_k + rank)


def validate_weights(bm25_weight: float, dense_weight: float) -> None:
    if bm25_weight < 0 or dense_weight < 0:
        raise ValueError("Retriever weights must be zero or greater.")
    if bm25_weight == 0 and dense_weight == 0:
        raise ValueError("At least one retriever weight must be greater than zero.")


def rrf_fusion(
    chunks: list[dict],
    bm25_results: list[dict],
    dense_results: list[dict],
    top_k: int,
    rrf_k: int,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
) -> list[dict]:
    validate_weights(bm25_weight, dense_weight)

    chunk_by_id = {chunk["chunk_id"]: chunk for chunk in chunks}
    bm25_by_id = index_results(bm25_results)
    dense_by_id = index_results(dense_results)
    candidate_ids = set(bm25_by_id) | set(dense_by_id)

    fused_results = []
    for chunk_id in candidate_ids:
        bm25_rank = bm25_by_id.get(chunk_id, {}).get("rank")
        dense_rank = dense_by_id.get(chunk_id, {}).get("rank")
        bm25_score = bm25_by_id.get(chunk_id, {}).get("score")
        dense_score = dense_by_id.get(chunk_id, {}).get("score")

        bm25_rrf_score = bm25_weight * reciprocal_rank(bm25_rank, rrf_k)
        dense_rrf_score = dense_weight * reciprocal_rank(dense_rank, rrf_k)
        hybrid_score = bm25_rrf_score + dense_rrf_score

        chunk = chunk_by_id[chunk_id]
        fused_results.append(
            {
                "score": float(hybrid_score),
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"],
                "bm25_rank": bm25_rank,
                "bm25_score": bm25_score,
                "bm25_rrf_score": float(bm25_rrf_score),
                "dense_rank": dense_rank,
                "dense_score": dense_score,
                "dense_rrf_score": float(dense_rrf_score),
                "text": chunk["text"],
            }
        )

    return sorted(fused_results, key=lambda item: item["score"], reverse=True)[:top_k]


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
    rrf_k: int = DEFAULT_RRF_K,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
) -> list[dict]:
    validate_weights(bm25_weight, dense_weight)
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
    return rrf_fusion(
        chunks=chunks,
        bm25_results=bm25_results,
        dense_results=dense_results,
        top_k=top_k,
        rrf_k=rrf_k,
        bm25_weight=bm25_weight,
        dense_weight=dense_weight,
    )


def print_results(query: str, results: list[dict]) -> None:
    print(f"Query: {query}")
    print()

    for rank, result in enumerate(results, start=1):
        preview = result["text"].replace("\n", " ")
        if len(preview) > 450:
            preview = preview[:450].rstrip() + "..."

        print(f"[{rank}] hybrid_score={result['score']:.4f}")
        print(
            f"    chunk_id={result['chunk_id']} "
            f"page={result['page']} chunk_index={result['chunk_index']}"
        )
        print(
            f"    bm25_rank={result['bm25_rank']} "
            f"bm25_score={format_optional_score(result['bm25_score'])} "
            f"bm25_rrf={result['bm25_rrf_score']:.6f} "
            f"dense_rank={result['dense_rank']} "
            f"dense_score={format_optional_score(result['dense_score'])} "
            f"dense_rrf={result['dense_rrf_score']:.6f}"
        )
        print(f"    {preview}")
        print()


def format_optional_score(score: float | None) -> str:
    if score is None:
        return "-"
    return f"{score:.4f}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search Wikipedia chunks with BM25 + dense cosine RRF hybrid."
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to show")
    parser.add_argument(
        "--candidate-k",
        type=int,
        default=DEFAULT_CANDIDATE_K,
        help="Number of BM25 and dense candidates to fuse",
    )
    parser.add_argument(
        "--rrf-k",
        type=int,
        default=DEFAULT_RRF_K,
        help="RRF smoothing constant",
    )
    parser.add_argument(
        "--bm25-weight",
        type=float,
        default=DEFAULT_BM25_WEIGHT,
        help="Weight applied to the BM25 reciprocal-rank score",
    )
    parser.add_argument(
        "--dense-weight",
        type=float,
        default=DEFAULT_DENSE_WEIGHT,
        help="Weight applied to the dense reciprocal-rank score",
    )
    parser.add_argument("--model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-dense-cache", action="store_true")
    args = parser.parse_args()

    chunks = load_chunks(CHUNKS_PATH)
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

    if args.query:
        results = search(
            query=args.query,
            chunks=chunks,
            bm25=bm25,
            embeddings=embeddings,
            model=args.model,
            ollama_url=args.ollama_url,
            timeout=args.timeout,
            top_k=args.top_k,
            candidate_k=args.candidate_k,
            rrf_k=args.rrf_k,
            bm25_weight=args.bm25_weight,
            dense_weight=args.dense_weight,
        )
        print_results(args.query, results)
        return

    print("Hybrid retriever is ready. Type a query, or type 'exit' to quit.")
    while True:
        query = input("\nQuery> ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            continue

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
            rrf_k=args.rrf_k,
            bm25_weight=args.bm25_weight,
            dense_weight=args.dense_weight,
        )
        print_results(query, results)


if __name__ == "__main__":
    main()
