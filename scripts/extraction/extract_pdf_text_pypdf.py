from pathlib import Path
import json
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parents[2]
pdf_path = PROJECT_ROOT / "data" / "raw" / "survey on RAG2.pdf"
output_path = PROJECT_ROOT / "data" / "interim" / "survey_on_rag2_pages_pypdf.jsonl"

reader = PdfReader(str(pdf_path))

with output_path.open("w", encoding="utf-8") as f:
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        record = {
            "source": pdf_path.name,
            "page": page_num,
            "text": text
        }

        f.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Saved to: {output_path}")
