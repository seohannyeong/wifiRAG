from pathlib import Path
import argparse
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RETRIEVAL_DIR = PROJECT_ROOT / "scripts" / "retrieval"
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "dense_metric_comparison.json"
REPORT_PATH = PROJECT_ROOT / "data" / "processed" / "dense_metric_comparison.md"

sys.path.append(str(RETRIEVAL_DIR))

import dense_ollama_retriever


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DEFAULT_QUERIES = [
    "Which French town near western Paris was associated with Impressionist painters?",
    "Which riverside suburb was described by Renoir as a pretty spot near Paris?",
    "Where did painters gather around Maison Fournaise and the Seine?",
    "Which place opened a museum dedicated to Sufism in 2024?",
    "Which South Korean football club played in the K3 League?",
    "Find the article about a semi-professional football team from Gyeonggi Province.",
    "Which club name is connected to Yangju and Korean football?",
    "Which European republic has overseas regions in South America and the Caribbean?",
    "Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain?",
    "Which nation has Paris as its largest city and cultural center?",
    "Find the article about the country whose history includes Gauls, Franks, and Napoleon.",
    "Which Renaissance artist was known as a German painter and printmaker?",
    "Who created works during the Northern Renaissance and was linked to Nuremberg?",
    "Find the article about an artist known for engravings and self-portraits.",
    "Which Finnish football team is commonly abbreviated as HJK?",
    "Find the Helsinki football club article without using its full Finnish name.",
    "Which sports club is described as a major Finnish football club from Helsinki?",
    "Which Bavarian city is associated with imperial history and Renaissance art?",
    "Find the German city connected to Franconia and medieval history.",
    "Which city in Germany is linked to Albrecht Durer?",
    "Find the article about a European city in Bavaria without naming the city directly.",
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


def compare_query(
    query: str,
    chunks: list[dict],
    embeddings: list[dict],
    model: str,
    ollama_url: str,
    timeout: int,
    top_k: int,
    preview_chars: int,
) -> dict:
    cosine_results = dense_ollama_retriever.search(
        query=query,
        chunks=chunks,
        embeddings=embeddings,
        model=model,
        ollama_url=ollama_url,
        timeout=timeout,
        top_k=top_k,
        metric="cosine",
    )
    euclidean_results = dense_ollama_retriever.search(
        query=query,
        chunks=chunks,
        embeddings=embeddings,
        model=model,
        ollama_url=ollama_url,
        timeout=timeout,
        top_k=top_k,
        metric="euclidean",
    )

    cosine_ids = [result["chunk_id"] for result in cosine_results]
    euclidean_ids = [result["chunk_id"] for result in euclidean_results]
    overlap = len(set(cosine_ids) & set(euclidean_ids))

    return {
        "query": query,
        "top1_same": cosine_ids[0] == euclidean_ids[0],
        "top_k_overlap": overlap,
        "results": {
            "cosine": [trim_result(result, preview_chars) for result in cosine_results],
            "euclidean": [
                trim_result(result, preview_chars) for result in euclidean_results
            ],
        },
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
        "# Dense Metric Comparison",
        "",
        "Ollama embedding 결과를 같은 조건에서 cosine similarity와 Euclidean similarity로 비교한 결과입니다.",
        "",
        "## Top-1 Summary",
        "",
        "| Query | Cosine Top-1 | Euclidean Top-1 | Top-1 Same | Top-k Overlap |",
        "| --- | --- | --- | --- | ---: |",
    ]

    for item in comparison:
        cosine_top = item["results"]["cosine"][0]
        euclidean_top = item["results"]["euclidean"][0]
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_escape(item["query"]),
                    format_top_result(cosine_top),
                    format_top_result(euclidean_top),
                    "same" if item["top1_same"] else "different",
                    str(item["top_k_overlap"]),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Detailed Results", ""])

    for item in comparison:
        lines.extend([f"### {markdown_escape(item['query'])}", ""])

        for metric in ["cosine", "euclidean"]:
            lines.extend([f"#### {metric.title()}", ""])
            lines.append("| Rank | Score | Chunk | Page | Preview |")
            lines.append("| --- | ---: | --- | ---: | --- |")

            for rank, result in enumerate(item["results"][metric], start=1):
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
            f"Top-k overlap: {item['top_k_overlap']}"
        )
        print("=" * 88)

        for metric in ["cosine", "euclidean"]:
            print(f"\n[{metric.upper()}]")
            for rank, result in enumerate(item["results"][metric], start=1):
                print(
                    f"{rank}. score={result['score']:.4f} "
                    f"{result['chunk_id']} page={result['page']} "
                    f"chunk={result['chunk_index']}"
                )
                print(f"   {result['preview'][:preview_chars]}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare cosine and Euclidean similarity for Ollama dense retrieval."
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of results per metric")
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
    parser.add_argument("--model", default=dense_ollama_retriever.DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=dense_ollama_retriever.DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=dense_ollama_retriever.DEFAULT_TIMEOUT)
    parser.add_argument("--rebuild-cache", action="store_true")
    args = parser.parse_args()

    queries = args.queries or DEFAULT_QUERIES
    dense_ollama_retriever.check_ollama(args.ollama_url, args.timeout)
    chunks = dense_ollama_retriever.load_chunks(CHUNKS_PATH)
    embeddings = dense_ollama_retriever.build_or_load_embeddings(
        chunks=chunks,
        model=args.model,
        ollama_url=args.ollama_url,
        cache_path=dense_ollama_retriever.EMBEDDINGS_PATH,
        rebuild_cache=args.rebuild_cache,
        timeout=args.timeout,
    )

    comparison = [
        compare_query(
            query=query,
            chunks=chunks,
            embeddings=embeddings,
            model=args.model,
            ollama_url=args.ollama_url,
            timeout=args.timeout,
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
