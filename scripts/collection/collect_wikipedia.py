from pathlib import Path
import argparse
import json
import time

import pandas as pd
import wikipediaapi


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "entities" / "entity_ids.del"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "wikipedia" / "wikipedia_rag_data.jsonl"
DEFAULT_USER_AGENT = "wikiRAG/1.0 (student-project)"


def load_entities(path: Path, limit: int | None) -> list[str]:
    df = pd.read_csv(path, sep="\t", header=None, names=["id", "entity"])
    entities = df["entity"].dropna().astype(str).tolist()
    if limit is not None:
        return entities[:limit]
    return entities


def fetch_wiki_data(wiki: wikipediaapi.Wikipedia, entity_name: str) -> dict | None:
    page = wiki.page(entity_name)
    if not page.exists():
        return None

    return {
        "entity": entity_name,
        "summary": page.summary,
        "sections": [
            {"section_title": section.title, "text": section.text}
            for section in page.sections
            if section.text.strip()
        ],
    }


def collect_wikipedia(
    input_path: Path,
    output_path: Path,
    limit: int | None,
    language: str,
    user_agent: str,
    sleep_seconds: float,
    append: bool,
) -> None:
    entities = load_entities(input_path, limit)
    wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language=language)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if append else "w"

    success_count = 0
    missing_count = 0

    with output_path.open(mode, encoding="utf-8") as f:
        for index, entity in enumerate(entities, start=1):
            print(f"[{index}/{len(entities)}] Fetching: {entity}", end="")

            try:
                wiki_data = fetch_wiki_data(wiki, entity)
            except Exception as exc:
                print(f" -> error: {exc}")
                missing_count += 1
                continue

            if wiki_data is None:
                print(" -> missing")
                missing_count += 1
            else:
                f.write(json.dumps(wiki_data, ensure_ascii=False) + "\n")
                print(" -> saved")
                success_count += 1

            if sleep_seconds > 0:
                time.sleep(sleep_seconds)

    print(f"Saved {success_count} pages to: {output_path}")
    print(f"Missing or failed pages: {missing_count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect Wikipedia pages for wikiRAG.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--language", default="en")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--append", action="store_true")
    args = parser.parse_args()

    collect_wikipedia(
        input_path=args.input,
        output_path=args.output,
        limit=args.limit,
        language=args.language,
        user_agent=args.user_agent,
        sleep_seconds=args.sleep,
        append=args.append,
    )


if __name__ == "__main__":
    main()
