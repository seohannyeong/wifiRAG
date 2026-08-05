from pathlib import Path
import argparse
import json
import math
import random
import re
import socket
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from collections import Counter


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHUNKS = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks_full.jsonl"
DEFAULT_DEV_QUERIES = (
    PROJECT_ROOT / "data" / "evaluation" / "wikipedia_retrieval_queries.jsonl"
)
DEFAULT_OUTPUT = (
    PROJECT_ROOT
    / "data"
    / "evaluation"
    / "wikipedia_retrieval_queries_test_draft.jsonl"
)

DEFAULT_MODEL = "qwen3:4b"
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434"
QUERY_TYPES = ("exact_name", "keyword", "natural", "paraphrase", "hard")
GENERATED_TYPES = ("natural", "paraphrase", "hard")
DIFFICULTY_BY_TYPE = {
    "exact_name": "easy",
    "keyword": "easy",
    "natural": "medium",
    "paraphrase": "medium",
    "hard": "hard",
}
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "concerning",
    "entity",
    "external",
    "for",
    "from",
    "has",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "section",
    "summary",
    "that",
    "the",
    "this",
    "to",
    "was",
    "what",
    "which",
    "who",
    "with",
}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


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


def normalize_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    words = re.findall(r"[a-z0-9]+", without_accents.casefold())
    return " ".join(words)


def content_words(text: str) -> set[str]:
    return {
        word
        for word in normalize_text(text).split()
        if len(word) > 2 and word not in STOPWORDS
    }


def display_entity(entity: str) -> str:
    return entity.replace("_", " ").strip()


def entity_title_variants(entity: str) -> list[str]:
    title = display_entity(entity)
    variants = {normalize_text(title)}
    without_parenthetical = re.sub(r"\s*\([^)]*\)\s*$", "", title)
    variants.add(normalize_text(without_parenthetical))
    return sorted(variant for variant in variants if len(variant) >= 4)


def contains_entity_title(query: str, entity: str) -> bool:
    normalized_query = f" {normalize_text(query)} "
    return any(
        f" {variant} " in normalized_query
        for variant in entity_title_variants(entity)
    )


def post_json(url: str, payload: dict, timeout: int) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise RuntimeError(f"Could not connect to Ollama at {url}.") from exc


def check_ollama(ollama_url: str, timeout: int) -> None:
    url = f"{ollama_url.rstrip('/')}/api/tags"
    try:
        with urllib.request.urlopen(url, timeout=timeout):
            return
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise RuntimeError(f"Could not connect to Ollama at {ollama_url}.") from exc


def output_schema() -> dict:
    properties = {
        query_type: {"type": "string"}
        for query_type in GENERATED_TYPES
    }
    return {
        "type": "object",
        "properties": properties,
        "required": list(GENERATED_TYPES),
    }


def build_prompt(entity: str, evidence: str, previous_errors: list[str]) -> str:
    error_text = ""
    if previous_errors:
        error_text = (
            "\nThe previous attempt failed these checks. Correct every issue:\n- "
            + "\n- ".join(previous_errors)
        )

    return f"""You are creating a retrieval benchmark from one Wikipedia chunk.

Target entity: {display_entity(entity)}

Evidence chunk:
{evidence}

Create exactly three English retrieval queries. Every query must be answerable from
the evidence, and the intended answer/entity must be the target entity.

Requirements:
- Never reveal the exact target entity title in any generated query.
- natural: a direct who/what/which question.
- paraphrase: an indirect question using different wording from the evidence.
- hard: a question combining at least two independent clues from the evidence.
- Do not ask for an attribute whose answer is not the target entity.
- Copy every year, count, score, age, and other number exactly from the evidence.
- Do not insert unusual punctuation inside names or numbers.
- Do not include answers, explanations, citations, or placeholders.
- Return only a JSON object with natural, paraphrase, and hard.
{error_text}
"""


def generate_with_ollama(
    entity: str,
    evidence: str,
    model: str,
    ollama_url: str,
    timeout: int,
    previous_errors: list[str],
) -> dict:
    payload = {
        "model": model,
        "prompt": build_prompt(entity, evidence, previous_errors),
        "stream": False,
        "format": output_schema(),
        "think": False,
        "options": {
            "temperature": 0.25,
            "num_predict": 500,
        },
    }
    response = post_json(
        f"{ollama_url.rstrip('/')}/api/generate",
        payload,
        timeout,
    )
    generated_text = response.get("response", "")
    try:
        return json.loads(generated_text)
    except json.JSONDecodeError as exc:
        raise ValueError("Ollama returned invalid JSON.") from exc


def clean_generated_queries(generated: dict) -> dict[str, str]:
    cleaned = {}
    for query_type in GENERATED_TYPES:
        value = generated.get(query_type)
        if not isinstance(value, str):
            continue
        query = " ".join(value.split()).strip()
        if query and not query.endswith("?"):
            query += "?"
        cleaned[query_type] = query
    return cleaned


def validate_generated_queries(
    queries: dict[str, str],
    entity: str,
    evidence: str,
) -> list[str]:
    errors = []
    missing_types = set(GENERATED_TYPES) - set(queries)
    if missing_types:
        errors.append(f"Missing query types: {sorted(missing_types)}")
        return errors

    normalized_queries = [normalize_text(queries[key]) for key in GENERATED_TYPES]
    if len(set(normalized_queries)) != len(normalized_queries):
        errors.append("Generated queries must be different from one another.")

    evidence_words = content_words(evidence)
    evidence_numbers = set(re.findall(r"\d+", evidence))
    for query_type in GENERATED_TYPES:
        query = queries[query_type]
        word_count = len(normalize_text(query).split())
        if contains_entity_title(query, entity):
            errors.append(f"{query_type} reveals the entity title.")
        if not 6 <= word_count <= 45:
            errors.append(
                f"{query_type} has {word_count} words; expected 6-45."
            )

        overlap = content_words(query) & evidence_words
        minimum_overlap = 1 if query_type == "paraphrase" else 2
        if len(overlap) < minimum_overlap:
            errors.append(
                f"{query_type} is weakly grounded in the evidence."
            )

        query_numbers = set(re.findall(r"\d+", query))
        unsupported_numbers = query_numbers - evidence_numbers
        if unsupported_numbers:
            errors.append(
                f"{query_type} contains unsupported numbers: "
                f"{sorted(unsupported_numbers)}."
            )
        if re.search(r"\d:\d|\b\d{1,2}\.\d{3}\b|-\s*:\s*\d", query):
            errors.append(f"{query_type} contains malformed numeric punctuation.")

    return errors


def generate_queries_for_entity(
    source_chunk: dict,
    model: str,
    ollama_url: str,
    timeout: int,
    max_retries: int,
) -> dict[str, str]:
    previous_errors = []
    for _ in range(max_retries):
        try:
            generated = generate_with_ollama(
                entity=source_chunk["entity"],
                evidence=source_chunk["text"],
                model=model,
                ollama_url=ollama_url,
                timeout=timeout,
                previous_errors=previous_errors,
            )
            queries = clean_generated_queries(generated)
            previous_errors = validate_generated_queries(
                queries,
                source_chunk["entity"],
                source_chunk["text"],
            )
            if not previous_errors:
                return queries
        except (RuntimeError, ValueError) as exc:
            previous_errors = [str(exc)]

    raise RuntimeError(
        f"Failed to generate valid queries for {source_chunk['entity']}: "
        + "; ".join(previous_errors)
    )


def build_idf(source_chunks: list[dict]) -> dict[str, float]:
    document_frequency = Counter()
    for chunk in source_chunks:
        document_frequency.update(content_words(chunk["text"]))

    document_count = len(source_chunks)
    return {
        word: math.log((1 + document_count) / (1 + frequency)) + 1
        for word, frequency in document_frequency.items()
    }


def make_keyword_query(source_chunk: dict, idf: dict[str, float]) -> str:
    entity_words = set(normalize_text(display_entity(source_chunk["entity"])).split())
    frequencies = Counter(
        word
        for word in normalize_text(source_chunk["text"]).split()
        if len(word) > 2
        and word.isalpha()
        and word not in STOPWORDS
        and word not in entity_words
    )
    ranked_words = sorted(
        frequencies,
        key=lambda word: (
            -(1 + math.log(frequencies[word])) * math.sqrt(idf.get(word, 1.0)),
            word,
        ),
    )
    keywords = ranked_words[:8]
    if len(keywords) < 4:
        raise ValueError(
            f"Could not extract enough keywords for {source_chunk['entity']}."
        )
    return " ".join(keywords)


def select_source_candidates(
    chunks: list[dict],
    excluded_entities: set[str],
    minimum_chars: int,
    seed: int,
) -> list[dict]:
    candidates = [
        chunk
        for chunk in chunks
        if chunk["chunk_index"] == 0
        and chunk["entity"] not in excluded_entities
        and len(chunk["text"]) >= minimum_chars
    ]
    random.Random(seed).shuffle(candidates)
    return candidates


def make_query_records(
    source_chunk: dict,
    keyword_query: str,
    generated_queries: dict[str, str],
    start_index: int,
    model: str,
) -> list[dict]:
    entity = source_chunk["entity"]
    queries = {
        "exact_name": display_entity(entity),
        "keyword": keyword_query,
        **generated_queries,
    }
    records = []
    for offset, query_type in enumerate(QUERY_TYPES):
        records.append(
            {
                "query_id": f"test_q{start_index + offset:04d}",
                "query": queries[query_type],
                "query_type": query_type,
                "difficulty": DIFFICULTY_BY_TYPE[query_type],
                "expected_entity": entity,
                "relevant_chunk_ids": [source_chunk["chunk_id"]],
                "source_chunk_id": source_chunk["chunk_id"],
                "split": "test",
                "generation_model": model,
                "review_status": "auto_generated",
            }
        )
    return records


def append_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def next_query_index(rows: list[dict]) -> int:
    indices = []
    for row in rows:
        match = re.fullmatch(r"test_q(\d+)", row.get("query_id", ""))
        if match:
            indices.append(int(match.group(1)))
    return max(indices, default=0) + 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a balanced Wikipedia retrieval test set with Ollama."
    )
    parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNKS)
    parser.add_argument("--dev-queries", type=Path, default=DEFAULT_DEV_QUERIES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--entities", type=int, default=200)
    parser.add_argument("--minimum-chars", type=int, default=300)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--resume", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    for name, value in {
        "--entities": args.entities,
        "--minimum-chars": args.minimum_chars,
        "--timeout": args.timeout,
        "--max-retries": args.max_retries,
    }.items():
        if value <= 0:
            raise SystemExit(f"{name} must be greater than zero.")

    check_ollama(args.ollama_url, args.timeout)
    chunks = load_jsonl(args.chunks)
    dev_queries = load_jsonl(args.dev_queries) if args.dev_queries.exists() else []
    excluded_entities = {query["expected_entity"] for query in dev_queries}

    existing_rows = []
    if args.resume and args.output.exists():
        existing_rows = load_jsonl(args.output)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text("", encoding="utf-8")

    completed_entities = {row["expected_entity"] for row in existing_rows}
    excluded_entities |= completed_entities
    remaining_count = args.entities - len(completed_entities)
    if remaining_count <= 0:
        print(f"Output already contains {len(existing_rows)} queries.")
        return

    source_candidates = select_source_candidates(
        chunks=chunks,
        excluded_entities=excluded_entities,
        minimum_chars=args.minimum_chars,
        seed=args.seed,
    )
    if len(source_candidates) < remaining_count:
        raise SystemExit(
            f"Requested {remaining_count} entities but only "
            f"{len(source_candidates)} qualify."
        )
    idf = build_idf(source_candidates)

    query_index = next_query_index(existing_rows)
    failures = []
    completed_count = 0
    for candidate_index, source_chunk in enumerate(source_candidates, start=1):
        if completed_count >= remaining_count:
            break
        entity = source_chunk["entity"]
        print(
            f"[{completed_count + 1}/{remaining_count}] "
            f"Generating queries for {entity}"
        )
        try:
            keyword_query = make_keyword_query(source_chunk, idf)
            generated_queries = generate_queries_for_entity(
                source_chunk=source_chunk,
                model=args.model,
                ollama_url=args.ollama_url,
                timeout=args.timeout,
                max_retries=args.max_retries,
            )
        except RuntimeError as exc:
            failures.append(str(exc))
            print(f"  skipped: {exc}", file=sys.stderr)
            continue

        records = make_query_records(
            source_chunk=source_chunk,
            keyword_query=keyword_query,
            generated_queries=generated_queries,
            start_index=query_index,
            model=args.model,
        )
        append_jsonl(args.output, records)
        query_index += len(records)
        completed_count += 1
        if args.sleep > 0:
            time.sleep(args.sleep)

    generated_rows = load_jsonl(args.output)
    print(f"Saved {len(generated_rows)} queries to: {args.output}")
    if completed_count < remaining_count:
        print(
            f"Generated only {completed_count}/{remaining_count} requested entities.",
            file=sys.stderr,
        )
    if failures:
        print(f"Skipped {len(failures)} entities.", file=sys.stderr)


if __name__ == "__main__":
    main()
