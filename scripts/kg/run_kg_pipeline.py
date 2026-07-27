from pathlib import Path
import argparse
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def run_step(args: list[str]) -> None:
    print("\nRunning:", " ".join(args))
    subprocess.run(args, cwd=PROJECT_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Wikipedia KG pipeline.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--provider", default="openai", choices=["openai", "gemini", "deepseek"])
    parser.add_argument("--skip-collection", action="store_true")
    parser.add_argument("--skip-generation", action="store_true")
    parser.add_argument("--skip-neo4j", action="store_true")
    parser.add_argument("--clear-neo4j-first", action="store_true")
    args = parser.parse_args()

    if not args.skip_collection:
        run_step(
            [
                sys.executable,
                "scripts/collection/collect_wikipedia.py",
                "--limit",
                str(args.limit),
            ]
        )

    if not args.skip_generation:
        run_step(
            [
                sys.executable,
                "scripts/kg/generate_kg.py",
                "--provider",
                args.provider,
                "--limit",
                str(args.limit),
            ]
        )

    if not args.skip_neo4j:
        neo4j_args = [
            sys.executable,
            "scripts/kg/import_to_neo4j.py",
            "--kg-dir",
            f"data/kg/{args.provider}",
        ]
        if args.clear_neo4j_first:
            neo4j_args.append("--clear-first")
        run_step(neo4j_args)

    print("\nKG pipeline completed.")


if __name__ == "__main__":
    main()
