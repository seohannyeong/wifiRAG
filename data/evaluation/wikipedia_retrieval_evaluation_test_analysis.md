# Wikipedia Retriever Evaluation Analysis

## Evaluation Status

- Corpus: 6,488 chunks from 980 Wikipedia entities
- Test set: 1,000 queries from 200 held-out entities
- Query types: exact name, keyword, natural, paraphrase, hard
- Methods: BM25, TF-IDF, Dense, Rank Fusion, Score Fusion
- Retrieval depth: Top-5
- Query validation: 0 errors, 0 warnings, and no entity overlap with the development set

## Overall Results

| Method | Chunk Hit@1 | Chunk Hit@5 | Chunk MRR | Article Hit@5 |
| --- | ---: | ---: | ---: | ---: |
| BM25 | 88.0% | 98.9% | 0.9264 | 99.7% |
| TF-IDF | 74.6% | 96.2% | 0.8387 | 97.5% |
| Dense | 61.2% | 87.6% | 0.7212 | 91.6% |
| Rank Fusion | 79.8% | 96.6% | 0.8663 | 98.4% |
| Score Fusion | 85.8% | 99.3% | 0.9200 | 99.5% |

BM25 has the highest Chunk Hit@1 and MRR. Score Fusion has the highest Chunk Hit@3 and Hit@5, so it is slightly more likely to include the answer within a wider candidate set.

## Statistical Caution

The test set contains five queries for each of 200 entities, so the 1,000 rows are not fully independent. An entity-level bootstrap was therefore used to compare BM25 and Score Fusion.

| Difference | Observed | Entity-bootstrap 95% interval |
| --- | ---: | ---: |
| BM25 minus Score Fusion, Chunk MRR | +0.0064 | -0.0077 to +0.0208 |
| BM25 minus Score Fusion, Chunk Hit@1 | +0.0220 | -0.0020 to +0.0470 |
| Score Fusion minus BM25, Chunk Hit@5 | +0.0040 | -0.0030 to +0.0110 |

All intervals include zero. This evaluation does not provide strong evidence that either BM25 or Score Fusion is universally better.

## Results By Query Type

| Query type | Best Chunk MRR | Main observation |
| --- | --- | --- |
| Exact name | Dense, 0.9546 | Dense places the title's article chunk first more consistently. |
| Keyword | BM25, 0.9950 | Keyword queries use terms drawn directly from the source chunk. |
| Natural | BM25, 0.9502 | Natural questions still retain many source words and named facts. |
| Paraphrase | BM25, 0.9568 | Paraphrases change sentence structure but retain identifying facts. |
| Hard | BM25, 0.9917 | Hard questions are longer and contain more exact evidence, making them easy for sparse matching. |

Rank Fusion is weaker than BM25 because equal RRF weights allow the relatively weak Dense ranking to pull strong BM25 candidates downward. Score Fusion preserves BM25's strength better, but its fixed 1:1 weights are not yet tuned.

## Lexical Overlap

The proportion below is the share of unique query terms also found in the labeled source chunk.

| Query type | Average query tokens | Source-term coverage |
| --- | ---: | ---: |
| Exact name | 2.9 | 100.0% |
| Keyword | 8.0 | 97.8% |
| Natural | 17.0 | 92.2% |
| Paraphrase | 24.8 | 77.9% |
| Hard | 29.7 | 84.0% |

This high overlap explains why BM25 performs exceptionally well. In particular, the generated hard questions are longer and contain more evidence than the natural questions. Their label describes generation style, not measured retrieval difficulty.

## All-Method Failures

Only two queries failed to retrieve the expected article in Top-5 with every method:

1. `test_q0234`, John Benson: the wording only provides a broad nationality and a very wide year range.
2. `test_q0954`, Adam Miller: the wording only identifies an English footballer and a birth year.

Both questions are underspecified and can match many footballers, so they should be revised or marked ambiguous before using the benchmark for a final claim.

## Limitations

- The questions were automatically generated from the same chunks used as evidence.
- High lexical overlap favors sparse retrieval, especially BM25.
- The 1,000 queries represent 200 independent entities rather than 1,000 unrelated topics.
- Only a stratified sample was manually inspected; the full set has not been human-labeled.
- Chunk size, overlap, candidate count, RRF constant, and fusion weights were not jointly tuned.
- Query embedding time is excluded from reported search latency because embeddings were batched and cached.
- The benchmark contains synthetic questions rather than real user queries.

## Recommended Conclusion

BM25 is the strongest simple baseline for this corpus, while Score Fusion gives the best Top-5 chunk recall. Dense retrieval is particularly effective for exact-name queries but underperforms on generated keyword-heavy questions. The present benchmark is useful for implementation comparison, but a manually reviewed and more lexically diverse query set is needed before making a general performance claim.
