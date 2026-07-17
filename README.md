# wikiRAG

Wikipedia 기반 RAG System PART 2 실험 폴더입니다.

## Folder Structure

```text
data/
  raw/          원본 PDF
  interim/      PDF 텍스트 추출 결과
  processed/    chunking 결과
scripts/
  extraction/   PDF 텍스트 추출 스크립트
  preprocessing/chunk 생성 스크립트
  retrieval/    BM25 등 검색 스크립트
experiments/    사용하지 않는 실험/비교 파일
```

## Main Pipeline

```powershell
python .\scripts\extraction\extract_pdf_text_pypdf.py
python .\scripts\preprocessing\chunk_text.py
python .\scripts\retrieval\bm25_retriever.py "BM25 sparse retrieval" --top-k 3
python .\scripts\retrieval\tfidf_retriever.py "BM25 sparse retrieval" --top-k 3
```

## Main Files

- `data/raw/survey on RAG2.pdf`
- `data/interim/survey_on_rag2_pages_pypdf.jsonl`
- `data/processed/survey_on_rag2_chunks.jsonl`
- `scripts/retrieval/bm25_retriever.py`
- `scripts/retrieval/tfidf_retriever.py`
