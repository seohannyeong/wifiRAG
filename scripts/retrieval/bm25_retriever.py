from pathlib import Path
import argparse
import json
import re

from rank_bm25 import BM25Okapi


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "survey_on_rag2_chunks.jsonl"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", text.lower())


def load_chunks(path: Path) -> list[dict]:
    chunks = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))

    return chunks


def build_bm25(chunks: list[dict]) -> BM25Okapi:
    tokenized_corpus = [tokenize(chunk["text"]) for chunk in chunks]
    return BM25Okapi(tokenized_corpus)


def search(query: str, chunks: list[dict], bm25: BM25Okapi, top_k: int) -> list[dict]:
    tokenized_query = tokenize(query)
    scores = bm25.get_scores(tokenized_query)
    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    results = []
    for index in ranked_indices[:top_k]:
        chunk = chunks[index]
        results.append(
            {
                "score": float(scores[index]),
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"],
                "text": chunk["text"],
            }
        )

    return results


def print_results(query: str, results: list[dict]) -> None:
    print(f"Query: {query}")
    print()

    for rank, result in enumerate(results, start=1):
        preview = result["text"].replace("\n", " ")
        if len(preview) > 450:
            preview = preview[:450].rstrip() + "..."

        print(f"[{rank}] score={result['score']:.4f}")
        print(
            f"    chunk_id={result['chunk_id']} "
            f"page={result['page']} chunk_index={result['chunk_index']}"
        )
        print(f"    {preview}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Search RAG survey chunks with BM25.")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to show")
    parser.add_argument("--chunks", type=Path, default=CHUNKS_PATH, help="Path to chunks JSONL")
    args = parser.parse_args()

    chunks = load_chunks(args.chunks)
    bm25 = build_bm25(chunks)

    if args.query:
        results = search(args.query, chunks, bm25, args.top_k)
        print_results(args.query, results)
        return

    print("BM25 retriever is ready. Type a query, or type 'exit' to quit.")
    while True:
        query = input("\nQuery> ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            continue

        results = search(query, chunks, bm25, args.top_k)
        print_results(query, results)


if __name__ == "__main__":
    main()
