# wikiRAG

Wikipedia 기반 RAG System PART 2 실험 코드입니다.

이 프로젝트는 논문 PDF를 RAG에서 검색할 수 있는 형태로 변환하고, 같은 chunk 데이터에 대해 BM25, TF-IDF, Dense Ollama retriever를 실행 및 비교하는 것을 목표로 합니다.

## 담당 범위

- PDF 텍스트 추출
- page 단위 JSONL 생성
- chunk 생성
- BM25 sparse retriever 구현
- TF-IDF sparse retriever 구현
- Ollama embedding 기반 dense retriever 구현
- retriever별 검색 결과 비교 리포트 생성

## 폴더 구조

```text
data/
  raw/          원본 PDF
  interim/      PDF 텍스트 추출 결과(JSONL)
  processed/    chunk, embedding cache, retriever 비교 결과
scripts/
  extraction/   PDF 텍스트 추출 스크립트
  preprocessing/chunk 생성 스크립트
  retrieval/    BM25, TF-IDF, Dense retriever
  evaluation/   retriever 비교/평가 스크립트
experiments/    실험용 파일
notebooks/      단계별 실행 확인용 notebook
```

## 실행 환경

Python 3.10 이상을 권장합니다.

Windows에서는 보통 `python`을 사용합니다.

```powershell
python --version
```

Mac에서는 보통 `python3`을 사용합니다.

```bash
python3 --version
```

아래 명령어는 프로젝트 루트 폴더에서 실행해야 합니다.

```text
wikiRAG/
```

즉, 터미널 위치가 다음과 비슷해야 합니다.

```powershell
C:\학부연구생\wikiRAG>
```

또는 Mac/Linux에서는:

```bash
.../wikiRAG$
```

## 패키지 설치

Windows:

```powershell
pip install pypdf pdfplumber pdfreader rank_bm25 scikit-learn
```

Mac:

```bash
pip3 install pypdf pdfplumber pdfreader rank_bm25 scikit-learn
```

각 패키지 역할은 다음과 같습니다.

| 패키지 | 용도 |
| --- | --- |
| `pypdf` | 최종 PDF 텍스트 추출 |
| `pdfplumber` | PDF 추출 방식 비교용 |
| `pdfreader` | PDF 추출 방식 비교용 |
| `rank_bm25` | BM25 retriever 구현 |
| `scikit-learn` | TF-IDF vectorizer 및 cosine similarity |

## 전체 실행 순서

### 1. PDF 텍스트 추출

최종 실험에서는 `pypdf` 결과를 사용했습니다.

Windows:

```powershell
python .\scripts\extraction\extract_pdf_text_pypdf.py
```

Mac:

```bash
python3 scripts/extraction/extract_pdf_text_pypdf.py
```

출력 파일:

```text
data/interim/survey_on_rag2_pages_pypdf.jsonl
```

비교용으로 `pdfplumber`, `pdfreader`도 실행할 수 있습니다.

Windows:

```powershell
python .\scripts\extraction\extract_pdf_text_pdfplumber.py
python .\scripts\extraction\extract_pdf_text_pdfreader.py
```

Mac:

```bash
python3 scripts/extraction/extract_pdf_text_pdfplumber.py
python3 scripts/extraction/extract_pdf_text_pdfreader.py
```

### 2. Chunk 생성

`pypdf`로 추출한 page JSONL을 chunk JSONL로 변환합니다.

Windows:

```powershell
python .\scripts\preprocessing\chunk_text.py
```

Mac:

```bash
python3 scripts/preprocessing/chunk_text.py
```

출력 파일:

```text
data/processed/survey_on_rag2_chunks.jsonl
```

현재 chunk 설정:

```text
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
```

각 chunk에는 다음 정보가 저장됩니다.

```json
{
  "chunk_id": "survey_on_rag2_p4_c2",
  "source": "survey on RAG2.pdf",
  "page": 4,
  "chunk_index": 2,
  "text": "..."
}
```

## Retriever 개별 실행

### BM25 Retriever

BM25는 단어 기반 sparse retrieval입니다.

Windows:

```powershell
python .\scripts\retrieval\bm25_retriever.py "What is RAG?" --top-k 3
```

Mac:

```bash
python3 scripts/retrieval/bm25_retriever.py "What is RAG?" --top-k 3
```

출력 예시는 다음 정보를 포함합니다.

```text
score
chunk_id
page
chunk_index
text preview
```

### TF-IDF Retriever

TF-IDF는 chunk를 TF-IDF 벡터로 변환한 뒤, query 벡터와 cosine similarity를 계산하는 sparse retrieval입니다.

Windows:

```powershell
python .\scripts\retrieval\tfidf_retriever.py "What is RAG?" --top-k 3
```

Mac:

```bash
python3 scripts/retrieval/tfidf_retriever.py "What is RAG?" --top-k 3
```

### Dense Ollama Retriever

Dense retriever는 Ollama embedding model을 사용해 query와 chunk를 embedding vector로 변환한 뒤 cosine similarity를 계산합니다.

먼저 Ollama가 설치되어 있고 실행 중이어야 합니다.

Ollama 모델 다운로드:

```bash
ollama pull nomic-embed-text
```

Windows:

```powershell
python .\scripts\retrieval\dense_ollama_retriever.py "What is dense retrieval?" --top-k 3
```

Mac:

```bash
python3 scripts/retrieval/dense_ollama_retriever.py "What is dense retrieval?" --top-k 3
```

첫 실행에서는 모든 chunk embedding을 생성하므로 시간이 걸립니다. 이후에는 아래 cache 파일을 재사용합니다.

```text
data/processed/survey_on_rag2_ollama_embeddings.json
```

embedding cache를 새로 만들고 싶으면:

Windows:

```powershell
python .\scripts\retrieval\dense_ollama_retriever.py "What is dense retrieval?" --top-k 3 --rebuild-cache
```

Mac:

```bash
python3 scripts/retrieval/dense_ollama_retriever.py "What is dense retrieval?" --top-k 3 --rebuild-cache
```

cache 없는 단순 버전도 있습니다.

Windows:

```powershell
python .\scripts\retrieval\dense_ollama_simple.py "What is dense retrieval?" --top-k 3
```

Mac:

```bash
python3 scripts/retrieval/dense_ollama_simple.py "What is dense retrieval?" --top-k 3
```

단순 버전은 코드 이해가 쉽지만, 실행할 때마다 모든 chunk embedding을 다시 계산하므로 느릴 수 있습니다.

## Retriever 비교 실행

BM25, TF-IDF, Dense Ollama retriever를 같은 query 목록으로 비교합니다.

Windows:

```powershell
python .\scripts\evaluation\compare_retrievers.py --top-k 3
```

Mac:

```bash
python3 scripts/evaluation/compare_retrievers.py --top-k 3
```

출력 파일:

```text
data/processed/retriever_comparison.json
data/processed/retriever_comparison.md
```

`retriever_comparison.md`는 발표나 결과 확인용으로 보기 좋게 정리된 markdown 리포트입니다.

## 평가 쿼리 기반 분석

평가용 query 파일:

```text
data/evaluation/retrieval_eval_queries.jsonl
```

평가 실행:

Windows:

```powershell
python .\scripts\evaluation\evaluate_retrievers.py
```

Mac:

```bash
python3 scripts/evaluation/evaluate_retrievers.py
```

출력 파일:

```text
data/processed/retriever_evaluation.md
```

## 자주 발생하는 문제

### `command not found: python`

Mac에서는 `python` 대신 `python3`을 사용해야 하는 경우가 많습니다.

```bash
python3 --version
python3 scripts/retrieval/bm25_retriever.py "What is RAG?" --top-k 3
```

### `.py` 파일을 직접 실행했을 때 이상한 경고가 나오는 경우

Windows에서 다음처럼 실행하면 Python이 아니라 다른 앱으로 연결될 수 있습니다.

```powershell
.\scripts\retrieval\bm25_retriever.py "What is RAG?" --top-k 3
```

반드시 앞에 `python`을 붙여 실행합니다.

```powershell
python .\scripts\retrieval\bm25_retriever.py "What is RAG?" --top-k 3
```

### `ModuleNotFoundError`

필요한 패키지가 설치되지 않은 상태입니다.

Windows:

```powershell
pip install pypdf pdfplumber pdfreader rank_bm25 scikit-learn
```

Mac:

```bash
pip3 install pypdf pdfplumber pdfreader rank_bm25 scikit-learn
```

### Dense retriever에서 Ollama 연결 오류가 나는 경우

Ollama 앱 또는 서버가 실행 중인지 확인합니다.

```bash
ollama list
```

모델이 없으면 다운로드합니다.

```bash
ollama pull nomic-embed-text
```

## 주요 파일

| 파일 | 설명 |
| --- | --- |
| `data/raw/survey on RAG2.pdf` | 원본 논문 PDF |
| `data/interim/survey_on_rag2_pages_pypdf.jsonl` | pypdf로 추출한 page 단위 텍스트 |
| `data/processed/survey_on_rag2_chunks.jsonl` | RAG 검색용 chunk 데이터 |
| `data/processed/survey_on_rag2_ollama_embeddings.json` | Ollama dense embedding cache |
| `data/processed/retriever_comparison.md` | retriever 비교 결과 markdown |
| `scripts/extraction/extract_pdf_text_pypdf.py` | 최종 PDF 텍스트 추출 |
| `scripts/preprocessing/chunk_text.py` | chunk 생성 |
| `scripts/retrieval/bm25_retriever.py` | BM25 검색 |
| `scripts/retrieval/tfidf_retriever.py` | TF-IDF 검색 |
| `scripts/retrieval/dense_ollama_retriever.py` | Ollama dense 검색 |
| `scripts/evaluation/compare_retrievers.py` | 세 retriever 결과 비교 |

## 실행 흐름 요약

```text
PDF
  -> pypdf text extraction
  -> page-level JSONL
  -> chunking
  -> chunk-level JSONL
  -> BM25 / TF-IDF / Dense Retrieval
  -> retriever comparison report
```
