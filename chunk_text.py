from pathlib import Path
import json


BASE_DIR = Path(__file__).parent
INPUT_PATH = BASE_DIR / "survey_on_rag2_pages_pypdf.jsonl"
OUTPUT_PATH = BASE_DIR / "survey_on_rag2_chunks.jsonl"

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


def main() -> None:
    total_chunks = 0

    with INPUT_PATH.open("r", encoding="utf-8") as f_in, OUTPUT_PATH.open(
        "w", encoding="utf-8"
    ) as f_out:
        for line in f_in:
            page_record = json.loads(line)
            page = page_record["page"]
            text = page_record["text"].strip()
            chunks = split_into_chunks(text, CHUNK_SIZE, CHUNK_OVERLAP)

            for chunk_index, chunk_text in enumerate(chunks):
                chunk_record = {
                    "chunk_id": f"survey_on_rag2_p{page}_c{chunk_index}",
                    "source": page_record["source"],
                    "page": page,
                    "chunk_index": chunk_index,
                    "text": chunk_text,
                }
                f_out.write(json.dumps(chunk_record, ensure_ascii=False) + "\n")
                total_chunks += 1

    print(f"Saved {total_chunks} chunks to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
