from pathlib import Path
import argparse
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "survey_on_rag2_chunks.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "retriever_comparison.json"

sys.path.append(str(RETRIEVAL_DIR))

import bm25_retriever
import dense_ollama_retriever
import tfidf_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_QUERIES = [
    "BM25 sparse retrieval",
    "dense retrieval embedding",
    "retrieval granularity chunk entity",
    "query rewriting",
    "Self-RAG",
    "How does RAG reduce hallucination?",
    "What are training-free RAG methods?",
]


def trim_result(result: dict, preview_chars: int) -> dict:
    preview = result["text"].replace("\n", " ")
    if len(preview) > preview_chars:
        preview = preview[:preview_chars].rstrip() + "..."

    return {
        "score": result["score"],
        "chunk_id": result["chunk_id"],
        "page": result["page"],
        "chunk_index": result["chunk_index"],
        "preview": preview,
    }


def build_bm25_runner(chunks: list[dict]):
    bm25 = bm25_retriever.build_bm25(chunks)

    def run(query: str, top_k: int) -> list[dict]:
        return bm25_retriever.search(query, chunks, bm25, top_k)

    return run


def build_tfidf_runner(chunks: list[dict]):
    vectorizer, matrix = tfidf_retriever.build_tfidf(chunks)

    def run(query: str, top_k: int) -> list[dict]:
        return tfidf_retriever.search(query, chunks, vectorizer, matrix, top_k)

    return run


def build_dense_runner(
    chunks: list[dict],
    model: str,
    ollama_url: str,
    timeout: int,
    rebuild_cache: bool,
):
    dense_ollama_retriever.check_ollama(ollama_url, timeout)
    embeddings = dense_ollama_retriever.build_or_load_embeddings(
        chunks=chunks,
        model=model,
        ollama_url=ollama_url,
        cache_path=dense_ollama_retriever.EMBEDDINGS_PATH,
        rebuild_cache=rebuild_cache,
        timeout=timeout,
    )

    def run(query: str, top_k: int) -> list[dict]:
        return dense_ollama_retriever.search(
            query=query,
            chunks=chunks,
            embeddings=embeddings,
            model=model,
            ollama_url=ollama_url,
            timeout=timeout,
            top_k=top_k,
        )

    return run


def print_comparison(comparison: list[dict], methods: list[str], preview_chars: int) -> None:
    for item in comparison:
        print("=" * 88)
        print(f"Query: {item['query']}")
        print("=" * 88)

        for method in methods:
            print(f"\n[{method.upper()}]")
            for rank, result in enumerate(item["results"][method], start=1):
                print(
                    f"{rank}. score={result['score']:.4f} "
                    f"{result['chunk_id']} page={result['page']} "
                    f"chunk={result['chunk_index']}"
                )
                print(f"   {result['preview'][:preview_chars]}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare BM25, TF-IDF, and Ollama dense retrieval results."
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of results per method")
    parser.add_argument(
        "--query",
        action="append",
        dest="queries",
        help="Query to evaluate. Can be used multiple times.",
    )
    parser.add_argument(
        "--methods",
        nargs="+",
        default=["bm25", "tfidf", "dense"],
        choices=["bm25", "tfidf", "dense"],
        help="Retrievers to compare",
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH, help="JSON output path")
    parser.add_argument("--preview-chars", type=int, default=280, help="Preview length")
    parser.add_argument("--model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-dense-cache", action="store_true")
    args = parser.parse_args()

    queries = args.queries or DEFAULT_QUERIES
    chunks = bm25_retriever.load_chunks(CHUNKS_PATH)

    runners = {}
    if "bm25" in args.methods:
        runners["bm25"] = build_bm25_runner(chunks)
    if "tfidf" in args.methods:
        runners["tfidf"] = build_tfidf_runner(chunks)
    if "dense" in args.methods:
        runners["dense"] = build_dense_runner(
            chunks=chunks,
            model=args.model,
            ollama_url=args.ollama_url,
            timeout=args.timeout,
            rebuild_cache=args.rebuild_dense_cache,
        )

    comparison = []
    for query in queries:
        method_results = {}
        for method in args.methods:
            results = runners[method](query, args.top_k)
            method_results[method] = [
                trim_result(result, args.preview_chars) for result in results
            ]

        comparison.append({"query": query, "results": method_results})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        json.dump(comparison, f, ensure_ascii=False, indent=2)

    print_comparison(comparison, args.methods, args.preview_chars)
    print(f"Saved comparison to: {args.output}")


if __name__ == "__main__":
    main()
