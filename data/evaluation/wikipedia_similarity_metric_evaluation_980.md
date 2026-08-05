# Wikipedia Similarity Metric Evaluation

## Setup

- Corpus: 980 entities, 6,488 chunks
- Queries: 1000
- Retrieval depth: Top-5
- Dense document and query embeddings are reused from the nomic-embed-text cache.

## Overall Result

| Method | Chunk Hit@1 | Chunk Hit@3 | Chunk Hit@5 | Chunk MRR | Article Hit@5 | Avg search ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dense Cosine | 61.2% | 82.8% | 87.6% | 0.7212 | 91.6% | 1.30 |
| Dense Euclidean | 61.2% | 82.8% | 87.6% | 0.7212 | 91.6% | 1.58 |
| TF-IDF Cosine L2 | 74.6% | 93.3% | 96.2% | 0.8387 | 97.5% | 9.35 |
| TF-IDF Euclidean L2 | 74.6% | 93.3% | 96.2% | 0.8387 | 97.5% | 6.34 |
| TF-IDF Euclidean No Norm | 0.2% | 0.3% | 0.3% | 0.0023 | 1.3% | 6.38 |

## Ranking Agreement

| Pair | Top-1 same | Ordered Top-5 same | Average Top-5 overlap |
| --- | ---: | ---: | ---: |
| Dense cosine vs Euclidean | 100.0% | 100.0% | 5.00 |
| TF-IDF cosine L2 vs Euclidean L2 | 100.0% | 98.4% | 4.96 |
| TF-IDF cosine L2 vs Euclidean without normalization | 0.3% | 0.0% | 0.02 |

## Query-Type Result

| Query type | Method | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR |
| --- | --- | ---: | ---: | ---: |
| exact_name | Dense Cosine | 92.0% | 100.0% | 0.9546 |
| exact_name | Dense Euclidean | 92.0% | 100.0% | 0.9546 |
| exact_name | TF-IDF Cosine L2 | 54.5% | 96.5% | 0.7275 |
| exact_name | TF-IDF Euclidean L2 | 54.5% | 96.5% | 0.7275 |
| exact_name | TF-IDF Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| hard | Dense Cosine | 55.0% | 91.5% | 0.7067 |
| hard | Dense Euclidean | 55.0% | 91.5% | 0.7067 |
| hard | TF-IDF Cosine L2 | 85.5% | 98.5% | 0.9112 |
| hard | TF-IDF Euclidean L2 | 85.5% | 98.5% | 0.9112 |
| hard | TF-IDF Euclidean No Norm | 0.5% | 1.0% | 0.0067 |
| keyword | Dense Cosine | 29.5% | 63.0% | 0.4348 |
| keyword | Dense Euclidean | 29.5% | 63.0% | 0.4348 |
| keyword | TF-IDF Cosine L2 | 88.5% | 99.5% | 0.9321 |
| keyword | TF-IDF Euclidean L2 | 88.5% | 99.5% | 0.9321 |
| keyword | TF-IDF Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| natural | Dense Cosine | 71.5% | 95.5% | 0.8128 |
| natural | Dense Euclidean | 71.5% | 95.5% | 0.8128 |
| natural | TF-IDF Cosine L2 | 70.0% | 92.0% | 0.7952 |
| natural | TF-IDF Euclidean L2 | 70.0% | 92.0% | 0.7952 |
| natural | TF-IDF Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| paraphrase | Dense Cosine | 58.0% | 88.0% | 0.6971 |
| paraphrase | Dense Euclidean | 58.0% | 88.0% | 0.6971 |
| paraphrase | TF-IDF Cosine L2 | 74.5% | 94.5% | 0.8273 |
| paraphrase | TF-IDF Euclidean L2 | 74.5% | 94.5% | 0.8273 |
| paraphrase | TF-IDF Euclidean No Norm | 0.5% | 0.5% | 0.0050 |

## Vector Norms

| Vector | Minimum | Maximum | Mean | Standard deviation |
| --- | ---: | ---: | ---: | ---: |
| Dense document embedding | 0.999999 | 1.000001 | 1.000000 | 0.000000 |
| TF-IDF document vector without normalization | 20.6824 | 187.8755 | 72.9072 | 14.7669 |

## Interpretation

- For L2-normalized vectors, Euclidean distance and cosine similarity are monotonic transformations, so they should produce the same ranking.
- Dense cosine and Euclidean can differ only when embedding norms differ enough to affect Euclidean distance.
- TF-IDF Euclidean without normalization retains vector magnitude, so document length and term-weight magnitude can dominate semantic direction.
- Search latency excludes the time needed to create a new query embedding.
