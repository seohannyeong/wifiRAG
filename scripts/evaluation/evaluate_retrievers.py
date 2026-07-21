from pathlib import Path
import argparse
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "survey_on_rag2_chunks.jsonl"
QUERY_PATH = PROJECT_ROOT / "data" / "evaluation" / "retrieval_eval_queries.jsonl"
REPORT_PATH = PROJECT_ROOT / "data" / "processed" / "retriever_evaluation.md"

sys.path.append(str(RETRIEVAL_DIR))

import bm25_retriever
import dense_ollama_retriever
import tfidf_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def load_eval_queries(path: Path) -> list[dict]:
    queries = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                queries.append(json.loads(line))
    return queries


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


def contains_expected_term(text: str, terms: list[str]) -> bool:
    lower_text = text.lower()
    return any(term.lower() in lower_text for term in terms)


def evaluate_result(results: list[dict], expected_pages: list[int], expected_terms: list[str]) -> dict:
    top1 = results[0]
    topk_text = " ".join(result["text"] for result in results)
    topk_pages = [result["page"] for result in results]

    top1_page_hit = top1["page"] in expected_pages
    topk_page_hit = any(page in expected_pages for page in topk_pages)
    top1_term_hit = contains_expected_term(top1["text"], expected_terms)
    topk_term_hit = contains_expected_term(topk_text, expected_terms)

    simple_score = sum([top1_page_hit, topk_page_hit, top1_term_hit, topk_term_hit])
    return {
        "top1_page_hit": top1_page_hit,
        "topk_page_hit": topk_page_hit,
        "top1_term_hit": top1_term_hit,
        "topk_term_hit": topk_term_hit,
        "simple_score": simple_score,
    }


def mark(value: bool) -> str:
    return "OK" if value else "NO"


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def trim(text: str, limit: int) -> str:
    preview = text.replace("\n", " ")
    if len(preview) > limit:
        return preview[:limit].rstrip() + "..."
    return preview


def write_report(evaluations: list[dict], methods: list[str], output_path: Path, preview_chars: int) -> None:
    lines = [
        "# Retriever Evaluation",
        "",
        "This report compares retrievers using expected pages and expected terms for each query.",
        "",
        "Note: This is an automatic helper score. Read the previews before making the final judgment.",
        "",
        "## Summary",
        "",
        "| Query | Expected Pages | " + " | ".join(method.upper() for method in methods) + " | Best Guess |",
        "| --- | --- | " + " | ".join("---" for _ in methods) + " | --- |",
    ]

    totals = {method: 0 for method in methods}
    for item in evaluations:
        method_cells = []
        best_score = -1
        best_methods = []

        for method in methods:
            evaluation = item["methods"][method]["evaluation"]
            score = evaluation["simple_score"]
            totals[method] += score
            if score > best_score:
                best_score = score
                best_methods = [method]
            elif score == best_score:
                best_methods.append(method)

            result = item["methods"][method]["results"][0]
            cell = (
                f"{score}/4<br>"
                f"{result['chunk_id']}<br>"
                f"p.{result['page']} c.{result['chunk_index']}<br>"
                f"page:{mark(evaluation['top1_page_hit'])} "
                f"term:{mark(evaluation['top1_term_hit'])}"
            )
            method_cells.append(cell)

        best_guess = ", ".join(method.upper() for method in best_methods)
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_escape(item["query"]),
                    ", ".join(str(page) for page in item["expected_pages"]),
                    *method_cells,
                    best_guess,
                ]
            )
            + " |"
        )

    lines.extend(["", "## Total Simple Scores", ""])
    lines.append("| Method | Total |")
    lines.append("| --- | ---: |")
    for method in methods:
        lines.append(f"| {method.upper()} | {totals[method]} |")

    lines.extend(["", "## Details", ""])
    for item in evaluations:
        lines.extend(
            [
                f"### {markdown_escape(item['query'])}",
                "",
                f"- Note: {markdown_escape(item['note'])}",
                f"- Expected pages: {', '.join(str(page) for page in item['expected_pages'])}",
                f"- Expected terms: {', '.join(item['expected_terms'])}",
                "",
            ]
        )

        for method in methods:
            lines.extend([f"#### {method.upper()}", ""])
            lines.append("| Rank | Score | Chunk | Page | Preview |")
            lines.append("| --- | ---: | --- | ---: | --- |")
            for rank, result in enumerate(item["methods"][method]["results"], start=1):
                lines.append(
                    f"| {rank} | {result['score']:.4f} | {result['chunk_id']} | "
                    f"{result['page']} | {markdown_escape(trim(result['text'], preview_chars))} |"
                )
            lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate retrievers with expected pages and expected terms."
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of results per method")
    parser.add_argument(
        "--methods",
        nargs="+",
        default=["bm25", "tfidf", "dense"],
        choices=["bm25", "tfidf", "dense"],
        help="Retrievers to evaluate",
    )
    parser.add_argument("--queries", type=Path, default=QUERY_PATH, help="Evaluation query JSONL")
    parser.add_argument("--output", type=Path, default=REPORT_PATH, help="Markdown report path")
    parser.add_argument("--preview-chars", type=int, default=220, help="Preview length")
    parser.add_argument("--model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-dense-cache", action="store_true")
    args = parser.parse_args()

    chunks = bm25_retriever.load_chunks(CHUNKS_PATH)
    eval_queries = load_eval_queries(args.queries)

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

    evaluations = []
    for eval_query in eval_queries:
        item = {
            "query": eval_query["query"],
            "expected_pages": eval_query["expected_pages"],
            "expected_terms": eval_query["expected_terms"],
            "note": eval_query.get("note", ""),
            "methods": {},
        }

        for method in args.methods:
            results = runners[method](eval_query["query"], args.top_k)
            item["methods"][method] = {
                "results": results,
                "evaluation": evaluate_result(
                    results=results,
                    expected_pages=eval_query["expected_pages"],
                    expected_terms=eval_query["expected_terms"],
                ),
            }

        evaluations.append(item)

    write_report(evaluations, args.methods, args.output, args.preview_chars)
    print(f"Saved evaluation report to: {args.output}")


if __name__ == "__main__":
    main()
