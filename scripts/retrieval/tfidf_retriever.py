from pathlib import Path
import argparse
import json
import re
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 1. 문서(Chunk) 로드
# 2. Token으로 분리
# 3. TF-IDF 벡터 생성
# 4. Query 입력
# 5. Query도 Token으로 분리
# 6. Query와 각 문서의 TF-IDF 유사도 계산
# 7. 가장 높은 점수의 Top-k 문서 반환

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_PATH = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"


def tokenize(text: str) -> list[str]:
    # 대소문자 차이를 줄이고 영문/숫자 중심으로 토큰을 나눈다.
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", text.lower())
#대소문자 차이 없앰
#findall() 함수는 정규표현식에 매칭되는 모든 문자열을 찾아 리스트로 반환


def load_chunks(path: Path) -> list[dict]:
    chunks = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))

    return chunks


def build_tfidf(
    chunks: list[dict],
    normalize: bool = True,
) -> tuple[TfidfVectorizer, object]:
    documents = [chunk["text"] for chunk in chunks]
    # norm="l2"는 각 chunk 벡터 길이를 1에 가깝게 맞춘다.
    # normalize=False이면 벡터 크기 차이가 살아나서 euclidean 실험에 유용하다.
    vectorizer = TfidfVectorizer(
        tokenizer=tokenize,
        lowercase=False,
        token_pattern=None,
        norm="l2" if normalize else None,
    )
    matrix = vectorizer.fit_transform(documents)
    return vectorizer, matrix


def score_tfidf(query_vector: object, matrix: object, metric: str) -> list[float]:
    if metric == "cosine":
        return cosine_similarity(query_vector, matrix).flatten().tolist()

    if metric == "euclidean":
        # 거리는 작을수록 좋으므로 0~1 범위의 similarity 점수로 바꾼다.
        distances = euclidean_distances(query_vector, matrix).flatten()
        return (1 / (1 + distances)).tolist()

    raise ValueError(f"Unknown metric: {metric}")


def search(
    query: str,
    chunks: list[dict],
    vectorizer: TfidfVectorizer,
    matrix: object,
    top_k: int,
    metric: str = "cosine",
) -> list[dict]:
    # query도 같은 TF-IDF 단어 공간의 벡터로 변환한 뒤 chunk matrix와 비교한다.
    query_vector = vectorizer.transform([query])
    scores = score_tfidf(query_vector, matrix, metric)
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
    parser = argparse.ArgumentParser(
        description="Search Wikipedia chunks with TF-IDF retrieval."
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to show")
    parser.add_argument(
        "--metric",
        choices=["cosine", "euclidean"],
        default="cosine",
        help="Similarity metric for TF-IDF vectors",
    )
    parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Disable TF-IDF L2 normalization to show length/norm effects more clearly",
    )
    args = parser.parse_args()

    chunks = load_chunks(CHUNKS_PATH)
    vectorizer, matrix = build_tfidf(chunks, normalize=not args.no_normalize)

    if args.query:
        results = search(
            args.query,
            chunks,
            vectorizer,
            matrix,
            args.top_k,
            metric=args.metric,
        )
        print_results(args.query, results)
        return

    print("TF-IDF retriever is ready. Type a query, or type 'exit' to quit.")
    while True:
        query = input("\nQuery> ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            continue

        results = search(
            query,
            chunks,
            vectorizer,
            matrix,
            args.top_k,
            metric=args.metric,
        )
        print_results(query, results)


if __name__ == "__main__":
    main()
