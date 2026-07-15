from pathlib import Path
import json
import pdfplumber


base_dir = Path(__file__).parent
pdf_path = base_dir / "survey on RAG2.pdf"
output_path = base_dir / "survey_on_rag2_pages_pdfplumber.jsonl"

with pdfplumber.open(pdf_path) as pdf:
    with output_path.open("w", encoding="utf-8") as f:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""

            record = {
                "source": pdf_path.name,
                "page": page_num,
                "text": text,
            }

            f.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Saved to: {output_path}")
