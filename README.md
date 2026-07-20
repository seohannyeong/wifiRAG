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
python .\scripts\retrieval\dense_ollama_retriever.py "dense retrieval embedding" --top-k 3
python .\scripts\evaluation\compare_retrievers.py --top-k 3
```

## Main Files

- `data/raw/survey on RAG2.pdf`
- `data/interim/survey_on_rag2_pages_pypdf.jsonl`
- `data/processed/survey_on_rag2_chunks.jsonl`
- `data/processed/survey_on_rag2_ollama_embeddings.json`
- `data/processed/retriever_comparison.json`
- `scripts/retrieval/bm25_retriever.py`
- `scripts/retrieval/tfidf_retriever.py`
- `scripts/retrieval/dense_ollama_retriever.py`
- `scripts/evaluation/compare_retrievers.py`

## Ollama Dense Retrieval

Ollama를 사용하려면 Ollama 앱/서버가 실행 중이어야 하고 embedding 모델이 필요합니다.

```powershell
ollama pull nomic-embed-text
python .\scripts\retrieval\dense_ollama_retriever.py "What is dense retrieval?" --top-k 3
```

첫 실행에서는 모든 chunk embedding을 생성하므로 시간이 걸립니다. 이후에는
`data/processed/survey_on_rag2_ollama_embeddings.json` 캐시를 재사용합니다.
