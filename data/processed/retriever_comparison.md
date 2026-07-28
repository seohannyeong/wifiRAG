# Retriever Comparison

BM25, TF-IDF, Dense Ollama retriever의 검색 결과를 같은 query 기준으로 비교한 리포트입니다.

## Top-1 Summary

| Query | DENSE | DENSE_EUCLIDEAN | Agreement |
| --- | --- | --- | --- |
| Where is Chatou located? | wiki_Chatou_c0<br>p.1 c.0<br>0.8170 | wiki_Chatou_c0<br>p.1 c.0<br>0.6231 | same |
| Chatou commune Yvelines France | wiki_Chatou_c0<br>p.1 c.0<br>0.8039 | wiki_Chatou_c0<br>p.1 c.0<br>0.6149 | same |
| Which river is Chatou located near? | wiki_Chatou_c0<br>p.1 c.0<br>0.7848 | wiki_Chatou_c0<br>p.1 c.0<br>0.6039 | same |
| What place in Chatou was connected to Impressionist painters? | wiki_Chatou_c1<br>p.1 c.1<br>0.8438 | wiki_Chatou_c1<br>p.1 c.1<br>0.6414 | same |
| What is Yangju Citizen Football Club? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8971 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.6879 | same |
| Yangju Citizen football club K3 League | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8674 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.6601 | same |
| Which league does Yangju Citizen FC play in? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8692 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.6616 | same |
| What country is France located in Western Europe? | wiki_France_c8<br>p.2 c.8<br>0.7483 | wiki_France_c8<br>p.2 c.8<br>0.5850 | same |
| France French Republic Western Europe | wiki_France_c0<br>p.2 c.0<br>0.6934 | wiki_France_c0<br>p.2 c.0<br>0.5608 | same |
| What is the capital and largest city of France? | wiki_France_c1<br>p.2 c.1<br>0.7853 | wiki_France_c1<br>p.2 c.1<br>0.6041 | same |
| Which countries border metropolitan France? | wiki_France_c8<br>p.2 c.8<br>0.7747 | wiki_France_c8<br>p.2 c.8<br>0.5984 | same |
| Who was Albrecht Durer? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8515 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.6473 | same |
| Albrecht Durer Renaissance artist | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8396 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.6384 | same |
| What kind of artist was Albrecht Durer? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8174 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.6233 | same |
| What is Helsingin Jalkapalloklubi? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8037 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6148 | same |
| HJK Helsinki Finnish football club | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8533 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6487 | same |
| What does HJK refer to in Finnish football? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8370 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6365 | same |
| Where is Nuremberg located? | wiki_Nuremberg_c11<br>p.9 c.11<br>0.7983 | wiki_Nuremberg_c11<br>p.9 c.11<br>0.6116 | same |
| Nuremberg Bavaria Germany city | wiki_Nuremberg_c0<br>p.9 c.0<br>0.8245 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.6280 | same |
| What German state is Nuremberg in? | wiki_Nuremberg_c0<br>p.9 c.0<br>0.7939 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.6090 | same |
| Which city is associated with Albrecht Durer and Bavaria? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.7904 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.6070 | same |

## Detailed Results

### Where is Chatou located?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8170 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.7052 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6810 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6231 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.5657 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5559 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

### Chatou commune Yvelines France

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8039 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.6884 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6643 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6149 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.5588 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5496 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

### Which river is Chatou located near?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7848 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.6847 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6690 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6039 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 0.5574 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5514 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |

### What place in Chatou was connected to Impressionist painters?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8438 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.7547 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.7543 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6414 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.5881 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5879 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

### What is Yangju Citizen Football Club?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8971 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6474 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.6199 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6879 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5435 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.5342 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

### Yangju Citizen football club K3 League

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8674 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6250 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.6014 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6601 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5359 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.5283 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |

### Which league does Yangju Citizen FC play in?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8692 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6479 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.6367 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6616 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5437 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.5398 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

### What country is France located in Western Europe?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7483 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 2 | 0.7347 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.7328 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5850 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 2 | 0.5786 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.5777 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |

### France French Republic Western Europe

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6934 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.6827 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |
| 3 | 0.6630 | wiki_France_c3 | 2 | Bourbon Restoration until the founding of the French Second Republic, which was succeeded by the Second French Empire upon Napoleon III's takeover. His empire collapsed during the Franco-Prussian War in 1870. This led to the establishment of the French Third Republic, as well as... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5608 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.5566 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |
| 3 | 0.5492 | wiki_France_c3 | 2 | Bourbon Restoration until the founding of the French Second Republic, which was succeeded by the Second French Empire upon Napoleon III's takeover. His empire collapsed during the Franco-Prussian War in 1870. This led to the establishment of the French Third Republic, as well as... |

### What is the capital and largest city of France?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7853 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.7443 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 3 | 0.6972 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6041 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.5831 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 3 | 0.5624 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |

### Which countries border metropolitan France?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7747 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 2 | 0.7639 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.7257 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5984 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |
| 2 | 0.5927 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.5745 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |

### Who was Albrecht Durer?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8515 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7045 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.7036 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, Dover Publications, New York 1963 (2nd ed. 2000), ISBN 0-486-21097-9.  Section: External links  Colvi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6473 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5654 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.5650 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, Dover Publications, New York 1963 (2nd ed. 2000), ISBN 0-486-21097-9.  Section: External links  Colvi... |

### Albrecht Durer Renaissance artist

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8396 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7498 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.7483 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6384 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5857 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.5850 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

### What kind of artist was Albrecht Durer?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8174 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.6938 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |
| 3 | 0.6881 | wiki_Albrecht_Dürer_c3 | 8 | his German successors; the "Little Masters" who attempted few large engravings but continued Dürer's themes in small, rather cramped compositions. Lucas van Leyden was the only Northern European engraver to successfully continue to produce large engravings in the first third of t... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6233 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5610 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |
| 3 | 0.5587 | wiki_Albrecht_Dürer_c3 | 8 | his German successors; the "Little Masters" who attempted few large engravings but continued Dürer's themes in small, rather cramped compositions. Lucas van Leyden was the only Northern European engraver to successfully continue to produce large engravings in the first third of t... |

### What is Helsingin Jalkapalloklubi?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8037 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6741 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.6667 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6148 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.5533 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.5505 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

### HJK Helsinki Finnish football club

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8533 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.7961 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.7771 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6487 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6103 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.5997 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

### What does HJK refer to in Finnish football?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8370 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.8110 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.7839 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6365 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6193 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.6033 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

### Where is Nuremberg located?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7983 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |
| 2 | 0.7915 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 3 | 0.7902 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6116 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |
| 2 | 0.6076 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 3 | 0.6069 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |

### Nuremberg Bavaria Germany city

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8245 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.8121 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.7791 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6280 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.6200 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.6007 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

### What German state is Nuremberg in?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7939 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.7820 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.7670 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6090 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.6023 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.5943 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

### Which city is associated with Albrecht Durer and Bavaria?

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7904 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7640 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.7489 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |

#### DENSE_EUCLIDEAN

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6070 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5928 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.5853 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |

