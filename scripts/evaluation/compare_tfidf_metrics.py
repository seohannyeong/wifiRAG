from pathlib import Path
import argparse
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "tfidf_metric_comparison.json"
REPORT_PATH = PROJECT_ROOT / "data" / "processed" / "tfidf_metric_comparison.md"

sys.path.append(str(RETRIEVAL_DIR))

import tfidf_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_QUERIES = [
    "Which European republic has overseas regions in South America and the Caribbean?",
    "Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain?",
    "Find the article about the country whose history includes Gauls, Franks, and Napoleon.",
    "Which French town near western Paris was associated with Impressionist painters?",
    "Where did painters gather around Maison Fournaise and the Seine?",
    "Which South Korean football club played in the K3 League?",
    "Find the article about a semi-professional football team from Gyeonggi Province.",
    "Which Renaissance artist was known as a German painter and printmaker?",
    "Find the article about an artist known for engravings and self-portraits.",
    "Which Finnish football team is commonly abbreviated as HJK?",
    "Find the Helsinki football club article without using its full Finnish name.",
    "Which Bavarian city is associated with imperial history and Renaissance art?",
    "Find the German city connected to Franconia and medieval history.",
    "Find a very short external links section about a football club.",
    "Find a chunk that mostly contains references or external links.",
]


METHODS = [
    {
        "name": "tfidf_cosine_l2",
        "label": "TF-IDF Cosine L2",
        "metric": "cosine",
        "normalize": True,
    },
    {
        "name": "tfidf_euclidean_l2",
        "label": "TF-IDF Euclidean L2",
        "metric": "euclidean",
        "normalize": True,
    },
    {
        "name": "tfidf_euclidean_no_norm",
        "label": "TF-IDF Euclidean No Norm",
        "metric": "euclidean",
        "normalize": False,
    },
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


def build_runners(chunks: list[dict]) -> dict:
    runners = {}

    for method in METHODS:
        vectorizer, matrix = tfidf_retriever.build_tfidf(
            chunks,
            normalize=method["normalize"],
        )

        def run(
            query: str,
            top_k: int,
            current_vectorizer=vectorizer,
            current_matrix=matrix,
            current_metric=method["metric"],
        ) -> list[dict]:
            return tfidf_retriever.search(
                query=query,
                chunks=chunks,
                vectorizer=current_vectorizer,
                matrix=current_matrix,
                top_k=top_k,
                metric=current_metric,
            )

        runners[method["name"]] = run

    return runners


def compare_query(
    query: str,
    runners: dict,
    top_k: int,
    preview_chars: int,
) -> dict:
    results = {}
    top_ids = []
    top_k_sets = []

    for method in METHODS:
        method_results = runners[method["name"]](query, top_k)
        trimmed = [trim_result(result, preview_chars) for result in method_results]
        results[method["name"]] = trimmed
        top_ids.append(trimmed[0]["chunk_id"])
        top_k_sets.append({result["chunk_id"] for result in trimmed})

    shared_top_k = set.intersection(*top_k_sets) if top_k_sets else set()

    return {
        "query": query,
        "top1_same": len(set(top_ids)) == 1,
        "shared_top_k_count": len(shared_top_k),
        "results": results,
    }


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def format_score(score: float) -> str:
    return f"{score:.4f}"


def format_top_result(result: dict) -> str:
    return (
        f"{result['chunk_id']}<br>"
        f"p.{result['page']} c.{result['chunk_index']}<br>"
        f"{format_score(result['score'])}"
    )


def write_markdown_report(comparison: list[dict], output_path: Path) -> None:
    lines = [
        "# TF-IDF Metric Comparison",
        "",
        "같은 TF-IDF 검색에서 cosine, euclidean, euclidean without normalization을 비교한 결과입니다.",
        "",
        "## Top-1 Summary",
        "",
        "| Query | "
        + " | ".join(method["label"] for method in METHODS)
        + " | Top-1 Same | Shared Top-k |",
        "| --- | " + " | ".join("---" for _ in METHODS) + " | --- | ---: |",
    ]

    for item in comparison:
        cells = [markdown_escape(item["query"])]
        for method in METHODS:
            cells.append(format_top_result(item["results"][method["name"]][0]))
        cells.append("same" if item["top1_same"] else "different")
        cells.append(str(item["shared_top_k_count"]))
        lines.append("| " + " | ".join(cells) + " |")

    lines.extend(["", "## Detailed Results", ""])

    for item in comparison:
        lines.extend([f"### {markdown_escape(item['query'])}", ""])

        for method in METHODS:
            lines.extend([f"#### {method['label']}", ""])
            lines.append("| Rank | Score | Chunk | Page | Preview |")
            lines.append("| --- | ---: | --- | ---: | --- |")

            for rank, result in enumerate(item["results"][method["name"]], start=1):
                lines.append(
                    f"| {rank} | {format_score(result['score'])} | "
                    f"{result['chunk_id']} | {result['page']} | "
                    f"{markdown_escape(result['preview'])} |"
                )

            lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_comparison(comparison: list[dict], preview_chars: int) -> None:
    for item in comparison:
        print("=" * 88)
        print(f"Query: {item['query']}")
        print(
            f"Top-1: {'same' if item['top1_same'] else 'different'} | "
            f"Shared top-k: {item['shared_top_k_count']}"
        )
        print("=" * 88)

        for method in METHODS:
            print(f"\n[{method['label']}]")
            for rank, result in enumerate(item["results"][method["name"]], start=1):
                print(
                    f"{rank}. score={result['score']:.4f} "
                    f"{result['chunk_id']} page={result['page']} "
                    f"chunk={result['chunk_index']}"
                )
                print(f"   {result['preview'][:preview_chars]}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare TF-IDF cosine, Euclidean, and no-normalization Euclidean."
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of results per method")
    parser.add_argument(
        "--query",
        action="append",
        dest="queries",
        help="Query to evaluate. Can be used multiple times.",
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH, help="JSON output path")
    parser.add_argument(
        "--report",
        type=Path,
        default=REPORT_PATH,
        help="Markdown report output path",
    )
    parser.add_argument("--preview-chars", type=int, default=280, help="Preview length")
    args = parser.parse_args()

    queries = args.queries or DEFAULT_QUERIES
    chunks = tfidf_retriever.load_chunks(CHUNKS_PATH)
    runners = build_runners(chunks)

    comparison = [
        compare_query(
            query=query,
            runners=runners,
            top_k=args.top_k,
            preview_chars=args.preview_chars,
        )
        for query in queries
    ]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        json.dump(comparison, f, ensure_ascii=False, indent=2)

    write_markdown_report(comparison, args.report)
    print_comparison(comparison, args.preview_chars)
    print(f"Saved comparison to: {args.output}")
    print(f"Saved markdown report to: {args.report}")


if __name__ == "__main__":
    main()
