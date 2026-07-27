from pathlib import Path
import argparse
import json
import os

from dotenv import load_dotenv
from kg_gen import KGGen


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "wikipedia" / "wikipedia_rag_data.jsonl"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "data" / "kg"

API_CONFIGS = {
    "openai": {
        "model_name": "gpt-4o-mini",
        "env_key": "OPENAI_API_KEY",
    },
    "gemini": {
        "model_name": "gemini/gemini-2.5-flash",
        "env_key": "GEMINI_API_KEY",
    },
    "deepseek": {
        "model_name": "deepseek/deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
    },
}


def safe_filename(name: str) -> str:
    return name.replace("/", "_").replace("\\", "_")


def build_input_text(data: dict, include_sections: bool) -> str:
    parts = [
        f"Entity: {data.get('entity', '')}",
        f"Summary: {data.get('summary', '')}",
    ]

    if include_sections:
        for section in data.get("sections", []):
            title = section.get("section_title", "")
            text = section.get("text", "")
            if text.strip():
                parts.append(f"Section: {title}\n{text}")

    return "\n\n".join(parts)


def generate_kg(
    input_path: Path,
    output_root: Path,
    provider: str,
    limit: int | None,
    include_sections: bool,
    overwrite: bool,
) -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    config = API_CONFIGS[provider]
    api_key = os.getenv(config["env_key"])
    if not api_key:
        raise RuntimeError(
            f"Missing {config['env_key']}. Create .env from .env.example first."
        )

    kg = KGGen(
        model=config["model_name"],
        temperature=0.0,
        api_key=api_key,
    )

    output_dir = output_root / provider
    output_dir.mkdir(parents=True, exist_ok=True)

    generated_count = 0
    skipped_count = 0

    with input_path.open("r", encoding="utf-8") as f:
        for index, line in enumerate(f, start=1):
            if limit is not None and index > limit:
                break

            data = json.loads(line)
            entity_name = data.get("entity", f"unknown_{index}")
            output_path = output_dir / f"{safe_filename(entity_name)}.json"

            if output_path.exists() and not overwrite:
                print(f"[{index}] Skipping existing KG: {entity_name}")
                skipped_count += 1
                continue

            text = build_input_text(data, include_sections)
            print(f"[{index}] Generating KG with {provider}: {entity_name}", end="")

            try:
                graph = kg.generate(input_data=text, context=entity_name)
                result = {
                    "source_entity": entity_name,
                    "provider": provider,
                    "model": config["model_name"],
                    "entities": list(graph.entities),
                    "edges": list(graph.edges),
                    "relations": [list(relation) for relation in graph.relations],
                }

                with output_path.open("w", encoding="utf-8") as out:
                    json.dump(result, out, ensure_ascii=False, indent=2)

                print(" -> saved")
                generated_count += 1
            except Exception as exc:
                print(f" -> failed: {exc}")

    print(f"Generated KG files: {generated_count}")
    print(f"Skipped KG files: {skipped_count}")
    print(f"Output directory: {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate KG JSON from Wikipedia data.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--provider", choices=sorted(API_CONFIGS), default="openai")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--include-sections", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    generate_kg(
        input_path=args.input,
        output_root=args.output_root,
        provider=args.provider,
        limit=args.limit,
        include_sections=args.include_sections,
        overwrite=args.overwrite,
    )


if __name__ == "__main__":
    main()
