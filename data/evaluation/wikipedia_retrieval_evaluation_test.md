# Wikipedia Retriever Evaluation

## Evaluation Setup

- Queries: 1000
- Wikipedia entities: 200
- Final retrieval depth: Top-5
- Methods: bm25, tfidf, dense, hybrid, score_fusion
- Primary metric: chunk-level MRR
- Article metrics count any chunk from the expected Wikipedia entity as relevant.

## Overall Result

**Best method by chunk_mrr_at_5: bm25**

| Method | Chunk Hit@1 | Chunk Hit@3 | Chunk Hit@5 | Chunk MRR | Chunk nDCG | Article Hit@1 | Article Hit@5 | Article MRR | Avg search ms/query |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bm25 | 88.0% | 97.2% | 98.9% | 0.9264 | 0.9423 | 97.0% | 99.7% | 0.9817 | 19.7 |
| tfidf | 74.6% | 93.3% | 96.2% | 0.8387 | 0.8701 | 86.6% | 97.5% | 0.9126 | 8.6 |
| dense | 61.2% | 82.8% | 87.6% | 0.7212 | 0.7604 | 76.9% | 91.6% | 0.8287 | 1.1 |
| hybrid | 79.8% | 93.4% | 96.6% | 0.8663 | 0.8915 | 88.3% | 98.4% | 0.9238 | 21.4 |
| score_fusion | 85.8% | 98.7% | 99.3% | 0.9200 | 0.9388 | 93.8% | 99.5% | 0.9637 | 21.2 |

## Query-Type Result

| Query type | Method | Queries | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR | Article Hit@1 | Article Hit@5 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| exact_name | bm25 | 200 | 57.5% | 96.0% | 0.7383 | 99.0% | 100.0% |
| exact_name | tfidf | 200 | 54.5% | 96.5% | 0.7275 | 96.0% | 100.0% |
| exact_name | dense | 200 | 92.0% | 100.0% | 0.9546 | 99.5% | 100.0% |
| exact_name | hybrid | 200 | 87.5% | 100.0% | 0.9287 | 100.0% | 100.0% |
| exact_name | score_fusion | 200 | 84.5% | 100.0% | 0.9158 | 100.0% | 100.0% |
| hard | bm25 | 200 | 98.5% | 100.0% | 0.9917 | 99.0% | 100.0% |
| hard | tfidf | 200 | 85.5% | 98.5% | 0.9112 | 89.5% | 98.5% |
| hard | dense | 200 | 55.0% | 91.5% | 0.7067 | 78.5% | 94.5% |
| hard | hybrid | 200 | 85.0% | 97.0% | 0.9035 | 91.0% | 99.5% |
| hard | score_fusion | 200 | 92.5% | 99.5% | 0.9563 | 97.0% | 99.5% |
| keyword | bm25 | 200 | 99.0% | 100.0% | 0.9950 | 99.0% | 100.0% |
| keyword | tfidf | 200 | 88.5% | 99.5% | 0.9321 | 92.0% | 99.5% |
| keyword | dense | 200 | 29.5% | 63.0% | 0.4348 | 51.0% | 76.5% |
| keyword | hybrid | 200 | 57.5% | 91.0% | 0.7027 | 70.5% | 96.5% |
| keyword | score_fusion | 200 | 74.0% | 100.0% | 0.8596 | 84.5% | 100.0% |
| natural | bm25 | 200 | 91.0% | 100.0% | 0.9502 | 93.5% | 100.0% |
| natural | tfidf | 200 | 70.0% | 92.0% | 0.7952 | 77.0% | 94.0% |
| natural | dense | 200 | 71.5% | 95.5% | 0.8128 | 82.5% | 96.5% |
| natural | hybrid | 200 | 88.0% | 98.0% | 0.9214 | 93.0% | 98.5% |
| natural | score_fusion | 200 | 88.5% | 99.0% | 0.9333 | 94.5% | 99.5% |
| paraphrase | bm25 | 200 | 94.0% | 98.5% | 0.9568 | 94.5% | 98.5% |
| paraphrase | tfidf | 200 | 74.5% | 94.5% | 0.8273 | 78.5% | 95.5% |
| paraphrase | dense | 200 | 58.0% | 88.0% | 0.6971 | 73.0% | 90.5% |
| paraphrase | hybrid | 200 | 81.0% | 97.0% | 0.8752 | 87.0% | 97.5% |
| paraphrase | score_fusion | 200 | 89.5% | 98.0% | 0.9350 | 93.0% | 98.5% |

## Difficulty Result

| Difficulty | Method | Queries | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR | Article Hit@1 | Article Hit@5 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| easy | bm25 | 400 | 78.2% | 98.0% | 0.8667 | 99.0% | 100.0% |
| easy | tfidf | 400 | 71.5% | 98.0% | 0.8298 | 94.0% | 99.8% |
| easy | dense | 400 | 60.8% | 81.5% | 0.6947 | 75.2% | 88.2% |
| easy | hybrid | 400 | 72.5% | 95.5% | 0.8157 | 85.2% | 98.2% |
| easy | score_fusion | 400 | 79.2% | 100.0% | 0.8877 | 92.2% | 100.0% |
| hard | bm25 | 200 | 98.5% | 100.0% | 0.9917 | 99.0% | 100.0% |
| hard | tfidf | 200 | 85.5% | 98.5% | 0.9112 | 89.5% | 98.5% |
| hard | dense | 200 | 55.0% | 91.5% | 0.7067 | 78.5% | 94.5% |
| hard | hybrid | 200 | 85.0% | 97.0% | 0.9035 | 91.0% | 99.5% |
| hard | score_fusion | 200 | 92.5% | 99.5% | 0.9563 | 97.0% | 99.5% |
| medium | bm25 | 400 | 92.5% | 99.2% | 0.9535 | 94.0% | 99.2% |
| medium | tfidf | 400 | 72.2% | 93.2% | 0.8113 | 77.8% | 94.8% |
| medium | dense | 400 | 64.8% | 91.8% | 0.7549 | 77.8% | 93.5% |
| medium | hybrid | 400 | 84.5% | 97.5% | 0.8983 | 90.0% | 98.0% |
| medium | score_fusion | 400 | 89.0% | 98.5% | 0.9342 | 93.8% | 99.0% |

## Best-Rank Counts

Ties give one win to every method sharing the best rank.

| Method | Best chunk rank | Best article rank |
| --- | ---: | ---: |
| bm25 | 905 | 981 |
| tfidf | 757 | 867 |
| dense | 623 | 769 |
| hybrid | 811 | 885 |
| score_fusion | 877 | 943 |

## All-Method Failures

| ID | Type | Expected entity | Query |
| --- | --- | --- | --- |
| test_q0234 | paraphrase | John_Benson_(footballer) | What is the name of the footballer who was active from 1942 to 2010 and is Scottish? |
| test_q0954 | paraphrase | Adam_Miller_(footballer) | Which individual is identified as an English footballer with a birth year of 1982? |

## Interpretation Notes

- Chunk-level metrics are stricter: only the labeled answer chunk is correct.
- Article-level metrics are more forgiving: another chunk from the correct Wikipedia page is accepted.
- Scores from different retrievers are not directly comparable because their score scales differ.
- Search latency excludes query embedding time because query embeddings are batched and cached for evaluation.
- Automatically generated queries should be human-reviewed before reporting final benchmark results.
