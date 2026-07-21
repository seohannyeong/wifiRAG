# Retriever Evaluation

This report compares retrievers using expected pages and expected terms for each query.

Note: This is an automatic helper score. Read the previews before making the final judgment.

## Summary

| Query | Expected Pages | BM25 | TFIDF | DENSE | Best Guess |
| --- | --- | --- | --- | --- | --- |
| What is sparse retrieval? | 4, 11 | 4/4<br>survey_on_rag2_p4_c2<br>p.4 c.2<br>page:OK term:OK | 4/4<br>survey_on_rag2_p4_c2<br>p.4 c.2<br>page:OK term:OK | 4/4<br>survey_on_rag2_p4_c3<br>p.4 c.3<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is dense retrieval? | 4 | 3/4<br>survey_on_rag2_p5_c1<br>p.5 c.1<br>page:NO term:OK | 4/4<br>survey_on_rag2_p4_c2<br>p.4 c.2<br>page:OK term:OK | 3/4<br>survey_on_rag2_p4_c8<br>p.4 c.8<br>page:OK term:NO | TFIDF |
| What is retrieval granularity in RAG? | 4, 5 | 4/4<br>survey_on_rag2_p4_c8<br>p.4 c.8<br>page:OK term:OK | 4/4<br>survey_on_rag2_p4_c8<br>p.4 c.8<br>page:OK term:OK | 4/4<br>survey_on_rag2_p4_c8<br>p.4 c.8<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is query rewriting in RAG? | 6 | 4/4<br>survey_on_rag2_p6_c1<br>p.6 c.1<br>page:OK term:OK | 4/4<br>survey_on_rag2_p6_c1<br>p.6 c.1<br>page:OK term:OK | 2/4<br>survey_on_rag2_p1_c5<br>p.1 c.5<br>page:NO term:NO | BM25, TFIDF |
| What is Query2doc? | 5 | 4/4<br>survey_on_rag2_p5_c5<br>p.5 c.5<br>page:OK term:OK | 4/4<br>survey_on_rag2_p5_c5<br>p.5 c.5<br>page:OK term:OK | 4/4<br>survey_on_rag2_p5_c5<br>p.5 c.5<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is HyDE? | 6 | 4/4<br>survey_on_rag2_p6_c0<br>p.6 c.0<br>page:OK term:OK | 4/4<br>survey_on_rag2_p6_c0<br>p.6 c.0<br>page:OK term:OK | 4/4<br>survey_on_rag2_p6_c0<br>p.6 c.0<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is input-layer integration? | 8 | 4/4<br>survey_on_rag2_p8_c2<br>p.8 c.2<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c2<br>p.8 c.2<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c5<br>p.8 c.5<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is output-layer integration? | 8 | 4/4<br>survey_on_rag2_p8_c5<br>p.8 c.5<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c5<br>p.8 c.5<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c5<br>p.8 c.5<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What is intermediate-layer integration? | 8 | 4/4<br>survey_on_rag2_p8_c6<br>p.8 c.6<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c6<br>p.8 c.6<br>page:OK term:OK | 4/4<br>survey_on_rag2_p8_c6<br>p.8 c.6<br>page:OK term:OK | BM25, TFIDF, DENSE |
| Why can irrelevant retrieved passages hurt generation? | 9 | 4/4<br>survey_on_rag2_p9_c0<br>p.9 c.0<br>page:OK term:OK | 4/4<br>survey_on_rag2_p9_c0<br>p.9 c.0<br>page:OK term:OK | 1/4<br>survey_on_rag2_p6_c6<br>p.6 c.6<br>page:NO term:NO | BM25, TFIDF |
| What are training-free RAG methods? | 9, 10 | 4/4<br>survey_on_rag2_p10_c1<br>p.10 c.1<br>page:OK term:OK | 4/4<br>survey_on_rag2_p9_c7<br>p.9 c.7<br>page:OK term:OK | 4/4<br>survey_on_rag2_p9_c5<br>p.9 c.5<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What are independent training, sequential training, and joint training? | 9, 10, 11 | 4/4<br>survey_on_rag2_p9_c6<br>p.9 c.6<br>page:OK term:OK | 4/4<br>survey_on_rag2_p9_c6<br>p.9 c.6<br>page:OK term:OK | 4/4<br>survey_on_rag2_p9_c7<br>p.9 c.7<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What applications use RA-LLMs? | 12, 13 | 4/4<br>survey_on_rag2_p12_c1<br>p.12 c.1<br>page:OK term:OK | 4/4<br>survey_on_rag2_p12_c1<br>p.12 c.1<br>page:OK term:OK | 2/4<br>survey_on_rag2_p2_c5<br>p.2 c.5<br>page:NO term:NO | BM25, TFIDF |
| How is Wikipedia used as an external database in RAG? | 6, 7, 14 | 4/4<br>survey_on_rag2_p6_c7<br>p.6 c.7<br>page:OK term:OK | 4/4<br>survey_on_rag2_p6_c7<br>p.6 c.7<br>page:OK term:OK | 4/4<br>survey_on_rag2_p14_c0<br>p.14 c.0<br>page:OK term:OK | BM25, TFIDF, DENSE |
| What are future challenges of RA-LLMs? | 13, 14 | 4/4<br>survey_on_rag2_p13_c3<br>p.13 c.3<br>page:OK term:OK | 4/4<br>survey_on_rag2_p13_c3<br>p.13 c.3<br>page:OK term:OK | 2/4<br>survey_on_rag2_p1_c2<br>p.1 c.2<br>page:NO term:NO | BM25, TFIDF |

## Total Simple Scores

| Method | Total |
| --- | ---: |
| BM25 | 59 |
| TFIDF | 60 |
| DENSE | 50 |

## Details

### What is sparse retrieval?

- Note: Sparse retrieval definition and examples
- Expected pages: 4, 11
- Expected terms: sparse retrieval, bm25, tf-idf, inverted index

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 6.3115 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 2 | 5.7760 | survey_on_rag2_p5_c1 | 5 | first symptom sign of a heart attack is sudden cardiac arrest. Angina pectoris is caused by a decrease in myocardial blood flow.  Figure 3: Illustration of the basic Retrieval-Augm... |
| 3 | 5.7102 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1917 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 2 | 0.1484 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |
| 3 | 0.1473 | survey_on_rag2_p5_c1 | 5 | first symptom sign of a heart attack is sudden cardiac arrest. Angina pectoris is caused by a decrease in myocardial blood flow.  Figure 3: Illustration of the basic Retrieval-Augm... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7516 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |
| 2 | 0.7246 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 3 | 0.6701 | survey_on_rag2_p11_c1 | 11 | given input. Regarding the retriever, it can be categorized into two types: 1) Sparse retriever [120, 125], and 2) Dense retriever [61, 69, 197]. The sparse retrievers usually expl... |

### What is dense retrieval?

- Note: Dense retrieval definition
- Expected pages: 4
- Expected terms: dense retrieval, vector space, semantic similarity, embedding

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 5.1418 | survey_on_rag2_p5_c1 | 5 | first symptom sign of a heart attack is sudden cardiac arrest. Angina pectoris is caused by a decrease in myocardial blood flow.  Figure 3: Illustration of the basic Retrieval-Augm... |
| 2 | 5.1169 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 3 | 5.1040 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1381 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 2 | 0.1358 | survey_on_rag2_p4_c4 | 4 | and docu- ments into continuous vector space with certain criteria, for exam- ple, semantic similarity [61]. Dense retrieval methods are usually trainable, therefore holding more f... |
| 3 | 0.1354 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7086 | survey_on_rag2_p4_c8 | 4 | and data. 3.1.2 Retrieval Granularity. Retrieval granularity denotes the re- trieval unit in which the corpus is indexed, e.g., document, passage, token, or other levels like entit... |
| 2 | 0.7071 | survey_on_rag2_p4_c4 | 4 | and docu- ments into continuous vector space with certain criteria, for exam- ple, semantic similarity [61]. Dense retrieval methods are usually trainable, therefore holding more f... |
| 3 | 0.7064 | survey_on_rag2_p4_c3 | 4 | 117, 168, 196, 197], where passages are specifically represented as a bag of words and ranked based on term and inverse docu- ment frequencies [ 54]. On top of offering supplementa... |

### What is retrieval granularity in RAG?

- Note: Retrieval unit: document, passage, token, entity
- Expected pages: 4, 5
- Expected terms: retrieval granularity, document, passage, token, entity

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 10.8842 | survey_on_rag2_p4_c8 | 4 | and data. 3.1.2 Retrieval Granularity. Retrieval granularity denotes the re- trieval unit in which the corpus is indexed, e.g., document, passage, token, or other levels like entit... |
| 2 | 10.5717 | survey_on_rag2_p5_c3 | 5 | REALM [46], RAG [74] and Atlas [55]. A more fine-grained retrieval, i.e., token retrieval, instead can be done with faster searching but will bring more burden for the database sav... |
| 3 | 8.1076 | survey_on_rag2_p4_c7 | 4 | [ 122], which may therefore excel for their versatility, meaning that they can transfer and generalize better to new domains or tasks. Such general- purpose pre-trained retrievers,... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3599 | survey_on_rag2_p4_c8 | 4 | and data. 3.1.2 Retrieval Granularity. Retrieval granularity denotes the re- trieval unit in which the corpus is indexed, e.g., document, passage, token, or other levels like entit... |
| 2 | 0.2806 | survey_on_rag2_p5_c3 | 5 | REALM [46], RAG [74] and Atlas [55]. A more fine-grained retrieval, i.e., token retrieval, instead can be done with faster searching but will bring more burden for the database sav... |
| 3 | 0.1500 | survey_on_rag2_p4_c7 | 4 | [ 122], which may therefore excel for their versatility, meaning that they can transfer and generalize better to new domains or tasks. Such general- purpose pre-trained retrievers,... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8829 | survey_on_rag2_p4_c8 | 4 | and data. 3.1.2 Retrieval Granularity. Retrieval granularity denotes the re- trieval unit in which the corpus is indexed, e.g., document, passage, token, or other levels like entit... |
| 2 | 0.7569 | survey_on_rag2_p4_c2 | 4 | we will introduce the major techniques involved in the retrieval of tradi- tional and LLM-based RAGs, including the retriever type, retrieval granularity, pre- and post-retrieval e... |
| 3 | 0.7517 | survey_on_rag2_p5_c3 | 5 | REALM [46], RAG [74] and Atlas [55]. A more fine-grained retrieval, i.e., token retrieval, instead can be done with faster searching but will bring more burden for the database sav... |

### What is query rewriting in RAG?

- Note: Pre-retrieval query rewriting
- Expected pages: 6
- Expected terms: query rewrite, query rewriting, rewrite-retrieve-read, retrieval need

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 9.8576 | survey_on_rag2_p6_c1 | 6 | of the rewriting step is to clarify the retrieval need in the new query to ease the burden on the retrieval function to comprehend the input and enhance the output, i.e., retrieved... |
| 2 | 7.4823 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |
| 3 | 7.3730 | survey_on_rag2_p9_c2 | 9 | trainable models to offer self-knowledge as the reference for the adaptive calling of a retriever. In traditional RAGs, retrieval necessity judg- ment has also been explored and pr... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2497 | survey_on_rag2_p6_c1 | 6 | of the rewriting step is to clarify the retrieval need in the new query to ease the burden on the retrieval function to comprehend the input and enhance the output, i.e., retrieved... |
| 2 | 0.1414 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |
| 3 | 0.1213 | survey_on_rag2_p9_c2 | 9 | trainable models to offer self-knowledge as the reference for the adaptive calling of a retriever. In traditional RAGs, retrieval necessity judg- ment has also been explored and pr... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7379 | survey_on_rag2_p1_c5 | 1 | query or the generated output [62, 103]. Specifically, RAG first invokes the retriever to search and extract the relevant documents from external databases, which are then leverage... |
| 2 | 0.7156 | survey_on_rag2_p6_c1 | 6 | of the rewriting step is to clarify the retrieval need in the new query to ease the burden on the retrieval function to comprehend the input and enhance the output, i.e., retrieved... |
| 3 | 0.6684 | survey_on_rag2_p2_c3 | 2 | due to the substantial computational resources required for fine-tuning LLMs with domain-specific or the latest data. This, in turn, significantly hinders the widespread adoption o... |

### What is Query2doc?

- Note: Query expansion method
- Expected pages: 5
- Expected terms: query2doc, query expansion, pseudo-documents

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 4.6670 | survey_on_rag2_p5_c5 | 5 | output of the retriever. Wang et al. [156] propose a query expansion approach Query2doc, which generates pseudo-documents by few-shot prompting LLMs and expands the query with the... |
| 2 | 3.5802 | survey_on_rag2_p16_c7 | 16 | learning for text classification with many labels. In Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP . 173–184. [102] Sewon Min, Xinxi Lyu, Ari Ho... |
| 3 | 3.4746 | survey_on_rag2_p15_c7 | 15 | Zhengbao Jiang, Frank F Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi- Yu, Yiming Yang, Jamie Callan, and Graham Neubig. 2023. Active Retrieval Augmented Generation. In Proceed... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1143 | survey_on_rag2_p5_c5 | 5 | output of the retriever. Wang et al. [156] propose a query expansion approach Query2doc, which generates pseudo-documents by few-shot prompting LLMs and expands the query with the... |
| 2 | 0.0631 | survey_on_rag2_p5_c4 | 5 | (E AE) model, which divides the parameter space of language models according to the entity identity. The proposed EAE model aims to learn entity representations from the text along... |
| 3 | 0.0585 | survey_on_rag2_p16_c3 | 16 | Gender Matter? Towards Fairness in Dialogue Systems. In Proceedings of the 28th International Conference on Computational Linguistics . 4403–4416. [88] Haochen Liu, Yiqi Wang, Wenq... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5870 | survey_on_rag2_p5_c5 | 5 | output of the retriever. Wang et al. [156] propose a query expansion approach Query2doc, which generates pseudo-documents by few-shot prompting LLMs and expands the query with the... |
| 2 | 0.5117 | survey_on_rag2_p1_c3 | 1 | Fine-tuning, In-context Learning, Prompting. ∗Corresponding author: Yujuan Ding 1This is the long version of the survey to appear at KDD 2024 [33] 1 INTRODUCTION As one of the most... |
| 3 | 0.4995 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |

### What is HyDE?

- Note: Hypothetical Document Embedding
- Expected pages: 6
- Expected terms: hyde, hypothetical document embedding, hypothetical documents

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 4.5494 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |
| 2 | 3.5802 | survey_on_rag2_p16_c7 | 16 | learning for text classification with many labels. In Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP . 173–184. [102] Sewon Min, Xinxi Lyu, Ari Ho... |
| 3 | 3.4746 | survey_on_rag2_p15_c7 | 15 | Zhengbao Jiang, Frank F Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi- Yu, Yiming Yang, Jamie Callan, and Graham Neubig. 2023. Active Retrieval Augmented Generation. In Proceed... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0867 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |
| 2 | 0.0532 | survey_on_rag2_p16_c3 | 16 | Gender Matter? Towards Fairness in Dialogue Systems. In Proceedings of the 28th International Conference on Computational Linguistics . 4403–4416. [88] Haochen Liu, Yiqi Wang, Wenq... |
| 3 | 0.0530 | survey_on_rag2_p15_c7 | 15 | Zhengbao Jiang, Frank F Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi- Yu, Yiming Yang, Jamie Callan, and Graham Neubig. 2023. Active Retrieval Augmented Generation. In Proceed... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4350 | survey_on_rag2_p6_c0 | 6 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li on ad-hoc information retrieval d... |
| 2 | 0.4291 | survey_on_rag2_p14_c10 | 14 | system: Enhancing recommender systems with large language models. In Proceedings of the 17th ACM Conference on Recommender Systems . 1369–1373. [27] Yujuan Ding, Yunshan Ma, Wenqi... |
| 3 | 0.4260 | survey_on_rag2_p5_c4 | 5 | (E AE) model, which divides the parameter space of language models according to the entity identity. The proposed EAE model aims to learn entity representations from the text along... |

### What is input-layer integration?

- Note: Augmentation at input layer
- Expected pages: 8
- Expected terms: input-layer integration, concatenating, retrieved documents, original input

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 9.2643 | survey_on_rag2_p8_c2 | 8 | which can reduce the computational costs and also relieve the burden of LMs to identify relevant information in long retrieved documents. 3.3 Retrieval Integration for Generation A... |
| 2 | 8.5036 | survey_on_rag2_p8_c4 | 8 | at a time. In general, most black-box generation-based RAG methods apply input-layer integration since neither the intermediate layer of the generation model or the output distribu... |
| 3 | 8.2370 | survey_on_rag2_p8_c8 | 8 | alternative to incorporate a large number of text chunks frequently retrieved, which are challenging to process with input-layer integration due to the input length limit of LMs [6... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3003 | survey_on_rag2_p8_c2 | 8 | which can reduce the computational costs and also relieve the burden of LMs to identify relevant information in long retrieved documents. 3.3 Retrieval Integration for Generation A... |
| 2 | 0.2475 | survey_on_rag2_p8_c4 | 8 | at a time. In general, most black-box generation-based RAG methods apply input-layer integration since neither the intermediate layer of the generation model or the output distribu... |
| 3 | 0.2233 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6490 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |
| 2 | 0.6270 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 3 | 0.6183 | survey_on_rag2_p8_c3 | 8 | the origi- nal input and all retrieved documents into a single sequence as the new input for the generation model. Despite the effectiveness, such integration is limited to the num... |

### What is output-layer integration?

- Note: Augmentation at output layer
- Expected pages: 8
- Expected terms: output-layer integration, post-hoc, knn-lm, next-token distributions

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 11.5751 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |
| 2 | 9.4220 | survey_on_rag2_p8_c4 | 8 | at a time. In general, most black-box generation-based RAG methods apply input-layer integration since neither the intermediate layer of the generation model or the output distribu... |
| 3 | 7.8466 | survey_on_rag2_p6_c8 | 6 | sets in previous RAG work, which stores factual structured 1Retrievers: [BE: Bi-Encoder (also referred as dual encoder), OE: One-Encoder, BT: BERT-style Transformer, GP: Partial Ge... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4287 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |
| 2 | 0.2639 | survey_on_rag2_p8_c4 | 8 | at a time. In general, most black-box generation-based RAG methods apply input-layer integration since neither the intermediate layer of the generation model or the output distribu... |
| 3 | 0.1599 | survey_on_rag2_p8_c2 | 8 | which can reduce the computational costs and also relieve the burden of LMs to identify relevant information in long retrieved documents. 3.3 Retrieval Integration for Generation A... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6998 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |
| 2 | 0.6190 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 3 | 0.5840 | survey_on_rag2_p8_c4 | 8 | at a time. In general, most black-box generation-based RAG methods apply input-layer integration since neither the intermediate layer of the generation model or the output distribu... |

### What is intermediate-layer integration?

- Note: Augmentation inside model layers
- Expected pages: 8
- Expected terms: intermediate-layer integration, transformer module, cross attention, retrieved chunks

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 9.7364 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 2 | 9.1206 | survey_on_rag2_p8_c8 | 8 | alternative to incorporate a large number of text chunks frequently retrieved, which are challenging to process with input-layer integration due to the input length limit of LMs [6... |
| 3 | 7.8466 | survey_on_rag2_p6_c8 | 6 | sets in previous RAG work, which stores factual structured 1Retrievers: [BE: Bi-Encoder (also referred as dual encoder), OE: One-Encoder, BT: BERT-style Transformer, GP: Partial Ge... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2713 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 2 | 0.2273 | survey_on_rag2_p8_c8 | 8 | alternative to incorporate a large number of text chunks frequently retrieved, which are challenging to process with input-layer integration due to the input length limit of LMs [6... |
| 3 | 0.1749 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6375 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 2 | 0.6062 | survey_on_rag2_p8_c5 | 8 | Output-Layer Integration. Another kind of augmentation is post-hoc, i.e., output-layer integration, which joints retrieval and generation results. For example, kNN-LM [ 62] interpo... |
| 3 | 0.5821 | survey_on_rag2_p8_c8 | 8 | alternative to incorporate a large number of text chunks frequently retrieved, which are challenging to process with input-layer integration due to the input length limit of LMs [6... |

### Why can irrelevant retrieved passages hurt generation?

- Note: Risk of unnecessary or noisy retrieval
- Expected pages: 9
- Expected terms: irrelevant passages, incorrect responses, hallucination, retrieval necessity

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 11.0445 | survey_on_rag2_p9_c0 | 9 | A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models Conference’17, July 2017, Washington, DC, USA 3.4 Retrieval Augmentation Necessity and Frequency The... |
| 2 | 6.0027 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |
| 3 | 5.0342 | survey_on_rag2_p18_c3 | 18 | Laverde, and Leah Li. 2024. Financial Report Chunking for Effective Retrieval Augmented Generation. arXiv preprint arXiv:2402.05131 (2024). [179] Dawei Yin, Yuening Hu, Jiliang Tan... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2119 | survey_on_rag2_p9_c0 | 9 | A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models Conference’17, July 2017, Washington, DC, USA 3.4 Retrieval Augmentation Necessity and Frequency The... |
| 2 | 0.1167 | survey_on_rag2_p6_c6 | 6 | which adds an intermediate step to process the retrieved documents into a textual summary before in-context augmentation in the generation process. From another perspective, long r... |
| 3 | 0.1043 | survey_on_rag2_p8_c6 | 8 | integration. REFEED [183] proposes an answer refining mechanism that applies an LLM to evaluate the retrieved information and adjust the initial answer accordingly to enhance the a... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6584 | survey_on_rag2_p6_c6 | 6 | which adds an intermediate step to process the retrieved documents into a textual summary before in-context augmentation in the generation process. From another perspective, long r... |
| 2 | 0.6205 | survey_on_rag2_p8_c3 | 8 | the origi- nal input and all retrieved documents into a single sequence as the new input for the generation model. Despite the effectiveness, such integration is limited to the num... |
| 3 | 0.6187 | survey_on_rag2_p9_c4 | 9 | the generation models along with the original input, as applied in REALM [ 46]. One-time retrieval is more suitable for the cases that the informa- tion needs in external databases... |

### What are training-free RAG methods?

- Note: Training-free RA-LLM methods
- Expected pages: 9, 10
- Expected terms: training-free, prompt engineering, retrieval-guided token generation

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 7.3679 | survey_on_rag2_p10_c1 | 10 | Existing RA- LLMs approaches can be categorized into two classes: training-free approaches usually directly leverage retrieved information during the inference time by integrating... |
| 2 | 6.8100 | survey_on_rag2_p9_c7 | 9 | train retriever and generator simultaneously. In the following section, we will comprehensively review the training-free, independent training, sequential training, and joint train... |
| 3 | 6.7588 | survey_on_rag2_p9_c6 | 9 | However, one potential challenge is that the retriever and generator components are not specifically optimized for downstream tasks, which could easily lead to sub-optimal utilizat... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1854 | survey_on_rag2_p9_c7 | 9 | train retriever and generator simultaneously. In the following section, we will comprehensively review the training-free, independent training, sequential training, and joint train... |
| 2 | 0.1547 | survey_on_rag2_p10_c1 | 10 | Existing RA- LLMs approaches can be categorized into two classes: training-free approaches usually directly leverage retrieved information during the inference time by integrating... |
| 3 | 0.1458 | survey_on_rag2_p9_c8 | 9 | [54, 57, 63], instead of relying solely on the implicit knowledge encoded in the model’s parameters. These approaches have shown significant performance improvement for various kno... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6831 | survey_on_rag2_p9_c5 | 9 | strat- egy, which retrieves information for the prediction of every token during the generation. Overall, applying different frequencies of re- trieval can impact both the effectiv... |
| 2 | 0.6656 | survey_on_rag2_p10_c1 | 10 | Existing RA- LLMs approaches can be categorized into two classes: training-free approaches usually directly leverage retrieved information during the inference time by integrating... |
| 3 | 0.6527 | survey_on_rag2_p11_c0 | 11 | A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models Conference’17, July 2017, Washington, DC, USA 4.2 Independent Training Independent training refers t... |

### What are independent training, sequential training, and joint training?

- Note: Training strategy categories
- Expected pages: 9, 10, 11
- Expected terms: independent training, sequential training, joint training

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 21.4215 | survey_on_rag2_p9_c6 | 9 | However, one potential challenge is that the retriever and generator components are not specifically optimized for downstream tasks, which could easily lead to sub-optimal utilizat... |
| 2 | 20.2136 | survey_on_rag2_p10_c1 | 10 | Existing RA- LLMs approaches can be categorized into two classes: training-free approaches usually directly leverage retrieved information during the inference time by integrating... |
| 3 | 20.0321 | survey_on_rag2_p10_c0 | 10 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Retriever  Datastore  Input Outpu... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3571 | survey_on_rag2_p9_c6 | 9 | However, one potential challenge is that the retriever and generator components are not specifically optimized for downstream tasks, which could easily lead to sub-optimal utilizat... |
| 2 | 0.3343 | survey_on_rag2_p11_c2 | 11 | retrieval and reformulate the text generation as multiple copy-and-paste operations from existing source text collection. 4.3 Sequential Training Independent training is an efficie... |
| 3 | 0.3314 | survey_on_rag2_p11_c0 | 11 | A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models Conference’17, July 2017, Washington, DC, USA 4.2 Independent Training Independent training refers t... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7061 | survey_on_rag2_p9_c7 | 9 | train retriever and generator simultaneously. In the following section, we will comprehensively review the training-free, independent training, sequential training, and joint train... |
| 2 | 0.6937 | survey_on_rag2_p11_c2 | 11 | retrieval and reformulate the text generation as multiple copy-and-paste operations from existing source text collection. 4.3 Sequential Training Independent training is an efficie... |
| 3 | 0.6802 | survey_on_rag2_p11_c3 | 11 | can be directly employed as the fixed retriever and generator, thereby bypassing the first pertaining process. Compared to independent training, sequential training involves coordi... |

### What applications use RA-LLMs?

- Note: Application section
- Expected pages: 12, 13
- Expected terms: qa systems, chatbot, fact verification, recommendations, software engineering, finance

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 6.3088 | survey_on_rag2_p12_c1 | 12 | et al. [178], etc. Figure 6: A summary of applications of RA-LLMs categorized by NLP applications, downstream tasks, and domain-specific application. Specifically, NLP applications... |
| 2 | 6.0030 | survey_on_rag2_p11_c7 | 11 | paradigm to that of RAG [74], and Maximum Inner Product Search (MIPS) [15, 29, 119, 131] technique is used to locate the most relevant documents. To employ MIPS, all external docum... |
| 3 | 5.3896 | survey_on_rag2_p12_c0 | 12 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Applications NLP Applications QA... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2155 | survey_on_rag2_p12_c1 | 12 | et al. [178], etc. Figure 6: A summary of applications of RA-LLMs categorized by NLP applications, downstream tasks, and domain-specific application. Specifically, NLP applications... |
| 2 | 0.1922 | survey_on_rag2_p11_c7 | 11 | paradigm to that of RAG [74], and Maximum Inner Product Search (MIPS) [15, 29, 119, 131] technique is used to locate the most relevant documents. To employ MIPS, all external docum... |
| 3 | 0.1445 | survey_on_rag2_p12_c0 | 12 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Applications NLP Applications QA... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7397 | survey_on_rag2_p2_c5 | 2 | research from several primary perspectives of RA-LLMs in terms of retrieval, generation, and augmentation in Section 3, as well as the necessity and application frequency of retrie... |
| 2 | 0.7220 | survey_on_rag2_p13_c1 | 13 | Applications RA-LLMs have been widely adopted for various domain-specific tasks, such as AI for Science and Finance. 5.3.1 AI for Science. RA-LLMs have proven to be beneficial for... |
| 3 | 0.7144 | survey_on_rag2_p1_c2 | 1 | existing research studies in RA-LLMs, covering three pri- mary technical perspectives: architectures, training strategies, and applications. As the preliminary knowledge, we briefl... |

### How is Wikipedia used as an external database in RAG?

- Note: Wikipedia/external database discussion
- Expected pages: 6, 7, 14
- Expected terms: wikipedia, external knowledge, database, datastore

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 11.8128 | survey_on_rag2_p6_c7 | 6 | stores key-value pairs for knowledge, which can be constructed in various ways. The keys are primarily used for similarity matching, being as sparse vectors such as in BM25 or dens... |
| 2 | 11.4575 | survey_on_rag2_p14_c0 | 14 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Quality of External Knowledge . A... |
| 3 | 10.6781 | survey_on_rag2_p6_c6 | 6 | which adds an intermediate step to process the retrieved documents into a textual summary before in-context augmentation in the generation process. From another perspective, long r... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2185 | survey_on_rag2_p6_c7 | 6 | stores key-value pairs for knowledge, which can be constructed in various ways. The keys are primarily used for similarity matching, being as sparse vectors such as in BM25 or dens... |
| 2 | 0.2172 | survey_on_rag2_p14_c0 | 14 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Quality of External Knowledge . A... |
| 3 | 0.1631 | survey_on_rag2_p2_c4 | 2 | in conversational tasks [137, 171]. As illustrated in Figure 1, an LLM-based dialog system will not be able to answer well for out-of-scope queries. With the help of RAG to retriev... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6892 | survey_on_rag2_p14_c0 | 14 | Conference’17, July 2017, Washington, DC, USA Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li Quality of External Knowledge . A... |
| 2 | 0.6759 | survey_on_rag2_p1_c5 | 1 | query or the generated output [62, 103]. Specifically, RAG first invokes the retriever to search and extract the relevant documents from external databases, which are then leverage... |
| 3 | 0.6742 | survey_on_rag2_p1_c4 | 1 | in external databases, can provide faithful and timely external knowledge, thereby serving vital functions in various knowledge-intensive tasks. Due to their powerful capaci- ties,... |

### What are future challenges of RA-LLMs?

- Note: Future challenges and opportunities
- Expected pages: 13, 14
- Expected terms: trustworthy, multi-lingual, multi-modal, quality of external knowledge

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 13.9587 | survey_on_rag2_p13_c3 | 13 | analysis. In addition, financial QA is another primary task of financial analysis, which usually extracts relevant knowledge from financial docu- ments. As professional documents a... |
| 2 | 10.8881 | survey_on_rag2_p2_c5 | 2 | research from several primary perspectives of RA-LLMs in terms of retrieval, generation, and augmentation in Section 3, as well as the necessity and application frequency of retrie... |
| 3 | 10.7807 | survey_on_rag2_p1_c2 | 1 | existing research studies in RA-LLMs, covering three pri- mary technical perspectives: architectures, training strategies, and applications. As the preliminary knowledge, we briefl... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2540 | survey_on_rag2_p13_c3 | 13 | analysis. In addition, financial QA is another primary task of financial analysis, which usually extracts relevant knowledge from financial docu- ments. As professional documents a... |
| 2 | 0.1627 | survey_on_rag2_p2_c5 | 2 | research from several primary perspectives of RA-LLMs in terms of retrieval, generation, and augmentation in Section 3, as well as the necessity and application frequency of retrie... |
| 3 | 0.1509 | survey_on_rag2_p1_c2 | 1 | existing research studies in RA-LLMs, covering three pri- mary technical perspectives: architectures, training strategies, and applications. As the preliminary knowledge, we briefl... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7361 | survey_on_rag2_p1_c2 | 1 | existing research studies in RA-LLMs, covering three pri- mary technical perspectives: architectures, training strategies, and applications. As the preliminary knowledge, we briefl... |
| 2 | 0.7091 | survey_on_rag2_p2_c5 | 2 | research from several primary perspectives of RA-LLMs in terms of retrieval, generation, and augmentation in Section 3, as well as the necessity and application frequency of retrie... |
| 3 | 0.6826 | survey_on_rag2_p13_c1 | 13 | Applications RA-LLMs have been widely adopted for various domain-specific tasks, such as AI for Science and Finance. 5.3.1 AI for Science. RA-LLMs have proven to be beneficial for... |

