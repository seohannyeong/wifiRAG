from pathlib import Path
import json
from pdfreader import SimplePDFViewer


base_dir = Path(__file__).parent
pdf_path = base_dir / "survey on RAG2.pdf"
output_path = base_dir / "survey_on_rag2_pages_pdfreader.jsonl"

with pdf_path.open("rb") as pdf_file:
    viewer = SimplePDFViewer(pdf_file)

    with output_path.open("w", encoding="utf-8") as f:
        for page_num, _ in enumerate(viewer, start=1):
            viewer.render()
            text = "\n".join(viewer.canvas.strings)

            record = {
                "source": pdf_path.name,
                "page": page_num,
                "text": text,
            }

            f.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Saved to: {output_path}")
