# Wikipedia TF-IDF Similarity Evaluation

## 1. 실험 목적

전체 Wikipedia corpus에서 다음 세 가지 TF-IDF 검색 방식을 비교한다.

1. TF-IDF + Cosine Similarity + L2 정규화
2. TF-IDF + Euclidean Similarity + L2 정규화
3. TF-IDF + Euclidean Similarity + 정규화 없음

기존 20개 엔티티 파일럿 결과를 최종 결과로 사용하지 않고, 현재 수집된 전체 corpus에서 정규화와 유사도 계산 방식이 검색 성능에 어떤 영향을 주는지 확인하는 것이 목적이다.

## 2. 실험 조건

| 항목 | 값 |
| --- | ---: |
| Wikipedia 엔티티 | 980개 |
| 전체 chunk | 6,488개 |
| 평가 대상 엔티티 | 200개 |
| 평가 질문 | 1,000개 |
| 엔티티당 질문 | 5개 |
| 평가 깊이 | Top-5 |

질문 유형은 Exact name, Keyword, Natural, Paraphrase, Hard로 구성되며 각 유형은 200개이다.

## 3. 전체 결과

| 방법 | Chunk Hit@1 | Chunk Hit@3 | Chunk Hit@5 | Chunk MRR | Article Hit@5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| TF-IDF Cosine L2 | 74.6% | 93.3% | 96.2% | 0.8387 | 97.5% |
| TF-IDF Euclidean L2 | 74.6% | 93.3% | 96.2% | 0.8387 | 97.5% |
| TF-IDF Euclidean No Norm | 0.2% | 0.3% | 0.3% | 0.0023 | 1.3% |

Cosine L2와 Euclidean L2의 성능은 모든 평가 지표에서 동일했다. 반면 정규화를 적용하지 않은 Euclidean 방식은 거의 모든 질문에서 검색에 실패했다.

## 4. 질문 유형별 결과

| 질문 유형 | 방법 | Hit@1 | Hit@5 | MRR |
| --- | --- | ---: | ---: | ---: |
| Exact name | Cosine L2 | 54.5% | 96.5% | 0.7275 |
| Exact name | Euclidean L2 | 54.5% | 96.5% | 0.7275 |
| Exact name | Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| Keyword | Cosine L2 | 88.5% | 99.5% | 0.9321 |
| Keyword | Euclidean L2 | 88.5% | 99.5% | 0.9321 |
| Keyword | Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| Natural | Cosine L2 | 70.0% | 92.0% | 0.7952 |
| Natural | Euclidean L2 | 70.0% | 92.0% | 0.7952 |
| Natural | Euclidean No Norm | 0.0% | 0.0% | 0.0000 |
| Paraphrase | Cosine L2 | 74.5% | 94.5% | 0.8273 |
| Paraphrase | Euclidean L2 | 74.5% | 94.5% | 0.8273 |
| Paraphrase | Euclidean No Norm | 0.5% | 0.5% | 0.0050 |
| Hard | Cosine L2 | 85.5% | 98.5% | 0.9112 |
| Hard | Euclidean L2 | 85.5% | 98.5% | 0.9112 |
| Hard | Euclidean No Norm | 0.5% | 1.0% | 0.0067 |

Keyword와 Hard 질문에서 L2 기반 TF-IDF가 특히 높은 성능을 보였다. 자동 생성 질문이 source chunk의 단어와 사실을 많이 유지하므로, 단어 일치 기반 검색에 유리한 결과로 해석해야 한다.

## 5. 검색 순위 일치도

| 비교 | Top-1 일치 | Top-5 순서 전체 일치 | 평균 Top-5 공통 chunk |
| --- | ---: | ---: | ---: |
| Cosine L2 vs Euclidean L2 | 100.0% | 98.4% | 4.96 / 5 |
| Cosine L2 vs Euclidean No Norm | 0.3% | 0.0% | 0.02 / 5 |

Cosine L2와 Euclidean L2는 모든 질문에서 같은 Top-1을 선택했다. 16개 질문에서 Top-5 후순위 순서가 달랐지만, 대부분 관련 단어가 없어 동점에 가까운 문서의 순서 차이였다. 따라서 Hit와 MRR에는 영향을 주지 않았다.

## 6. L2에서 결과가 같은 이유

L2 정규화를 적용하면 쿼리 벡터와 문서 벡터의 길이가 1이 된다.

```text
||q|| = 1
||d|| = 1
```

단위 벡터 사이에서는 Euclidean distance와 cosine similarity 사이에 다음 관계가 성립한다.

```text
Euclidean distance² = 2 - 2 × cosine similarity
```

Cosine similarity가 커질수록 Euclidean distance는 작아진다. 두 값의 숫자 자체는 다르지만 문서를 정렬하는 순서는 같아진다.

예를 들어:

```text
문서 A cosine = 0.8 → Euclidean distance = sqrt(0.4)
문서 B cosine = 0.5 → Euclidean distance = sqrt(1.0)
```

Cosine에서는 A의 점수가 더 크고, Euclidean에서는 A의 거리가 더 작으므로 두 방식 모두 A를 더 유사한 문서로 판단한다.

## 7. 정규화를 끄면 실패하는 이유

정규화하지 않은 TF-IDF 벡터의 길이는 다음과 같았다.

| 벡터 | 최소 norm | 최대 norm | 평균 norm | 표준편차 |
| --- | ---: | ---: | ---: | ---: |
| Query | 4.3980 | 46.4017 | 17.5458 | 5.8305 |
| Document chunk | 20.6824 | 187.8755 | 72.9072 | 14.7669 |

문서 벡터가 쿼리 벡터보다 훨씬 크고 문서마다 크기 차이도 크다. 따라서 Euclidean distance는 단어 방향보다 벡터 크기에 더 큰 영향을 받는다.

그 결과 정규화를 끈 Euclidean의 Top-1은 단 6개 chunk에만 집중되었다.

| Top-1 chunk | 선택 횟수 | 문자 수 |
| --- | ---: | ---: |
| `wiki_Charlotte_Eagles_c2` | 526회 | 158자 |
| `wiki_Poland_women's_national_football_team_c4` | 452회 | 168자 |
| `wiki_HC_CSKA_Moscow_c2` | 16회 | 164자 |
| `wiki_University_of_Illinois_at_Urbana–Champaign_c20` | 3회 | 154자 |
| `wiki_Richard_McKinney_(footballer)_c0` | 2회 | 428자 |
| `wiki_Cosmin_Matei_c1` | 1회 | 321자 |

1,000개 질문 중 978개가 길이 158자와 168자인 두 chunk 중 하나를 Top-1으로 선택했다. 즉, 질문과 의미가 비슷한 문서가 아니라 벡터 크기가 작은 짧은 문서를 반복해서 선택했다.

## 8. 결론

1. L2 정규화를 적용한 TF-IDF에서는 Cosine과 Euclidean의 검색 성능이 동일했다.
2. 두 방법은 Top-1에서 100% 동일한 결과를 만들었다.
3. 정규화를 끈 Euclidean은 문서 길이와 벡터 크기의 영향을 크게 받아 검색에 실패했다.
4. 현재 TF-IDF Retriever에서는 기본값인 `norm="l2"`와 Cosine Similarity를 유지하는 것이 가장 이해하기 쉽고 안정적이다.
5. Euclidean L2도 성능은 동일하지만, 정보 검색에서 널리 사용하는 Cosine을 기본 방식으로 유지하는 편이 발표와 코드 설명에 적합하다.

## 9. 실험 한계

- 평가 질문은 source chunk를 바탕으로 자동 생성되어 단어 중복률이 높다.
- 1,000개 질문은 200개 엔티티에서 각각 5개씩 생성되었으므로 완전히 독립적인 질문 1,000개는 아니다.
- 현재 결과는 chunk size 1,000자와 overlap 150자 조건에 한정된다.
- 실제 사용자 질문이나 사람이 작성한 의미 중심 질문에서는 유형별 성능이 달라질 수 있다.
