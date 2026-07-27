from pathlib import Path
import argparse
import json


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "wikipedia" / "wikipedia_rag_data.jsonl"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "wikipedia_chunks.jsonl"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def split_into_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be larger than overlap")

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            boundary = max(
                text.rfind(". ", start, end),
                text.rfind("? ", start, end),
                text.rfind("! ", start, end),
                text.rfind("\n\n", start, end),
                text.rfind("\n", start, end),
            )
            if boundary > start + chunk_size * 0.5:
                end = boundary + 1
            else:
                space = text.rfind(" ", start, end)
                if space > start:
                    end = space

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = max(0, end - overlap)
        while start < len(text) and text[start] != " ":
            start += 1
        while start < len(text) and text[start] == " ":
            start += 1

    return chunks


def build_entity_text(record: dict, include_sections: bool) -> str:
    parts = [
        f"Entity: {record.get('entity', '')}",
        f"Summary: {record.get('summary', '')}",
    ]

    if include_sections:
        for section in record.get("sections", []):
            title = section.get("section_title", "")
            text = section.get("text", "")
            if text.strip():
                parts.append(f"Section: {title}\n{text}")

    return "\n\n".join(parts).strip()


def chunk_wikipedia(
    input_path: Path,
    output_path: Path,
    chunk_size: int,
    overlap: int,
    limit: int | None,
    include_sections: bool,
    allow_duplicates: bool,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    total_chunks = 0
    total_entities = 0
    skipped_duplicates = 0
    seen_entities = set()

    with input_path.open("r", encoding="utf-8") as f_in, output_path.open(
        "w", encoding="utf-8"
    ) as f_out:
        for line_number, line in enumerate(f_in, start=1):
            if limit is not None and total_entities >= limit:
                break

            record = json.loads(line)
            entity = record.get("entity", f"entity_{line_number}")
            if not allow_duplicates and entity in seen_entities:
                skipped_duplicates += 1
                continue
            seen_entities.add(entity)

            text = build_entity_text(record, include_sections)
            chunks = split_into_chunks(text, chunk_size, overlap)

            for chunk_index, chunk_text in enumerate(chunks):
                chunk_record = {
                    "chunk_id": f"wiki_{entity.replace(' ', '_')}_c{chunk_index}",
                    "source": "wikipedia_rag_data.jsonl",
                    "entity": entity,
                    "page": line_number,
                    "chunk_index": chunk_index,
                    "text": chunk_text,
                }
                f_out.write(json.dumps(chunk_record, ensure_ascii=False) + "\n")
                total_chunks += 1

            total_entities += 1

    print(f"Saved {total_chunks} chunks from {total_entities} entities to: {output_path}")
    print(f"Skipped duplicate entities: {skipped_duplicates}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Chunk Wikipedia JSONL data for retrievers.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE)
    parser.add_argument("--overlap", type=int, default=CHUNK_OVERLAP)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--include-sections", action="store_true")
    parser.add_argument("--allow-duplicates", action="store_true")
    args = parser.parse_args()

    chunk_wikipedia(
        input_path=args.input,
        output_path=args.output,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        limit=args.limit,
        include_sections=args.include_sections,
        allow_duplicates=args.allow_duplicates,
    )


if __name__ == "__main__":
    main()
