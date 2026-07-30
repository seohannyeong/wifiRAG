# Retriever Comparison

BM25, TF-IDF, Dense Ollama retriever의 검색 결과를 같은 query 기준으로 비교한 리포트입니다.

## Top-1 Summary

| Query | BM25 | DENSE | HYBRID | Agreement |
| --- | --- | --- | --- | --- |
| Which French town near western Paris was associated with Impressionist painters? | wiki_Chatou_c0<br>p.1 c.0<br>15.7227 | wiki_Chatou_c1<br>p.1 c.1<br>0.7211 | wiki_Chatou_c1<br>p.1 c.1<br>0.0325 | different |
| Which riverside suburb was described by Renoir as a pretty spot near Paris? | wiki_Chatou_c0<br>p.1 c.0<br>24.6641 | wiki_Chatou_c1<br>p.1 c.1<br>0.7134 | wiki_Chatou_c1<br>p.1 c.1<br>0.0325 | different |
| Where did painters gather around Maison Fournaise and the Seine? | wiki_Chatou_c1<br>p.1 c.1<br>26.7015 | wiki_Chatou_c1<br>p.1 c.1<br>0.7807 | wiki_Chatou_c1<br>p.1 c.1<br>0.0328 | same |
| Which place opened a museum dedicated to Sufism in 2024? | wiki_Chatou_c2<br>p.1 c.2<br>22.7761 | wiki_Chatou_c2<br>p.1 c.2<br>0.5928 | wiki_Chatou_c2<br>p.1 c.2<br>0.0328 | same |
| Which South Korean football club played in the K3 League? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>28.3047 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.7414 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.0328 | same |
| Find the article about a semi-professional football team from Gyeonggi Province. | wiki_Hereford_United_F.C._c4<br>p.29 c.4<br>10.1958 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.7483 | wiki_Aris_Thessaloniki_F.C._c0<br>p.37 c.0<br>0.0311 | different |
| Which club name is connected to Yangju and Korean football? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>21.7911 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8296 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.0328 | same |
| Which European republic has overseas regions in South America and the Caribbean? | wiki_France_c0<br>p.2 c.0<br>28.6123 | wiki_France_c0<br>p.2 c.0<br>0.7036 | wiki_France_c0<br>p.2 c.0<br>0.0328 | same |
| Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain? | wiki_France_c0<br>p.2 c.0<br>35.0096 | wiki_France_c7<br>p.2 c.7<br>0.7356 | wiki_France_c7<br>p.2 c.7<br>0.0325 | different |
| Which nation has Paris as its largest city and cultural center? | wiki_France_c1<br>p.2 c.1<br>13.5152 | wiki_France_c1<br>p.2 c.1<br>0.8021 | wiki_France_c1<br>p.2 c.1<br>0.0328 | same |
| Find the article about the country whose history includes Gauls, Franks, and Napoleon. | wiki_France_c4<br>p.2 c.4<br>14.1689 | wiki_France_c0<br>p.2 c.0<br>0.7456 | wiki_France_c4<br>p.2 c.4<br>0.0320 | different |
| Which Renaissance artist was known as a German painter and printmaker? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>21.7731 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.7439 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.0328 | same |
| Who created works during the Northern Renaissance and was linked to Nuremberg? | wiki_Nuremberg_c5<br>p.9 c.5<br>19.5348 | wiki_Nuremberg_c6<br>p.9 c.6<br>0.7733 | wiki_Nuremberg_c5<br>p.9 c.5<br>0.0320 | different |
| Find the article about an artist known for engravings and self-portraits. | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>12.7434 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.7135 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.0328 | same |
| Which Finnish football team is commonly abbreviated as HJK? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>20.6605 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8382 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.0328 | same |
| Find the Helsinki football club article without using its full Finnish name. | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>17.0989 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.7446 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.0328 | same |
| Which sports club is described as a major Finnish football club from Helsinki? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>20.3136 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8284 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.0328 | same |
| Which Bavarian city is associated with imperial history and Renaissance art? | wiki_Nuremberg_c1<br>p.9 c.1<br>19.2519 | wiki_Nuremberg_c1<br>p.9 c.1<br>0.7344 | wiki_Nuremberg_c1<br>p.9 c.1<br>0.0328 | same |
| Find the German city connected to Franconia and medieval history. | wiki_Nuremberg_c0<br>p.9 c.0<br>14.9533 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.7771 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.0328 | same |
| Which city in Germany is linked to Albrecht Durer? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>10.7654 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8001 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.0328 | same |
| Find the article about a European city in Bavaria without naming the city directly. | wiki_Nuremberg_c0<br>p.9 c.0<br>16.7515 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.7542 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.0328 | same |

## Detailed Results

### Which French town near western Paris was associated with Impressionist painters?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 15.7227 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 15.2940 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 3 | 10.6352 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7211 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6327 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5988 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0325 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.0323 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 0.0315 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |

### Which riverside suburb was described by Renoir as a pretty spot near Paris?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 24.6641 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 2 | 11.0525 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 3 | 8.8633 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7134 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6433 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6224 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0325 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.0323 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 0.0315 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |

### Where did painters gather around Maison Fournaise and the Seine?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 26.7015 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 11.3306 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 9.3300 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7807 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6494 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6313 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.0320 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 0.0308 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |

### Which place opened a museum dedicated to Sufism in 2024?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 22.7761 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 2 | 8.8663 | wiki_Trinity_University_(Texas)_c5 | 7 | for its large Hofmann-Ballard pipe organ, the largest pipe organ in South Texas, comprising 5 divisions, 102 stops, 112 ranks, and over 6,000 pipes. A state-of-the-art four-manual console was installed in summer 2007, with the aid of the university's Calvert Trust Fund. Non-denom... |
| 3 | 8.7947 | wiki_Malta_national_football_team_c9 | 35 | by a 1–0 home victory against San Marino on 12 June, anchoring a strong run in their Group D2 campaign and finishing second overall in the group. In September 2024, during the 2024–25 UEFA Nations League, Malta beat Moldova 2–0 away on 7 September and then overcame Andorra 1–0 aw... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5928 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 2 | 0.5914 | wiki_Trinity_University_(Texas)_c5 | 7 | for its large Hofmann-Ballard pipe organ, the largest pipe organ in South Texas, comprising 5 divisions, 102 stops, 112 ranks, and over 6,000 pipes. A state-of-the-art four-manual console was installed in summer 2007, with the aid of the university's Calvert Trust Fund. Non-denom... |
| 3 | 0.5886 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 2 | 0.0323 | wiki_Trinity_University_(Texas)_c5 | 7 | for its large Hofmann-Ballard pipe organ, the largest pipe organ in South Texas, comprising 5 divisions, 102 stops, 112 ranks, and over 6,000 pipes. A state-of-the-art four-manual console was installed in summer 2007, with the aid of the university's Calvert Trust Fund. Non-denom... |
| 3 | 0.0159 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |

### Which South Korean football club played in the K3 League?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 28.3047 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 11.9870 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 11.6147 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7414 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6630 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.6471 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.0320 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.0308 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |

### Find the article about a semi-professional football team from Gyeonggi Province.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 10.1958 | wiki_Hereford_United_F.C._c4 | 29 | He became manager a year later and set about building a team to challenge at the top of the Southern League and gain election to the Football League. With the club becoming one of the best-supported non-league clubs in the country Charles used his standing within the game to canv... |
| 2 | 9.9487 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |
| 3 | 9.8725 | wiki_Héctor_Cúper_c1 | 36 | Congo, taking the second of those countries to the 2017 Africa Cup of Nations final and a place at the 2018 FIFA World Cup.  Section: Personal life Cúper's great-grandfather was an Englishman whose surname was Cooper, who migrated to Santa Fe Province in Argentina and married an... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7483 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6928 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.6889 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0311 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 2 | 0.0164 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 3 | 0.0164 | wiki_Hereford_United_F.C._c4 | 29 | He became manager a year later and set about building a team to challenge at the top of the Southern League and gain election to the Football League. With the club becoming one of the best-supported non-league clubs in the country Charles used his standing within the game to canv... |

### Which club name is connected to Yangju and Korean football?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 21.7911 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 9.8057 | wiki_The_Bad_Seed_(1956_film)_c0 | 31 | Entity: The_Bad_Seed_(1956_film)  Summary: The Bad Seed is a 1956 American psychological horror thriller film directed by Mervyn LeRoy and starring Nancy Kelly, Patty McCormack, Henry Jones and Eileen Heckart, about an eight-year-old girl whose mother begins to suspect that she m... |
| 3 | 9.1996 | wiki_Hereford_United_F.C._c15 | 29 | Herefordshire bull was introduced for the 1971–72 season with H.U.F.C. lettering underneath. A supporters' club crest was also used during the 1970s. The shirt crest design changed several times over the years, with the full club name being added above and below the bull, which r... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8296 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6680 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |
| 3 | 0.6645 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.0161 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |
| 3 | 0.0161 | wiki_The_Bad_Seed_(1956_film)_c0 | 31 | Entity: The_Bad_Seed_(1956_film)  Summary: The Bad Seed is a 1956 American psychological horror thriller film directed by Mervyn LeRoy and starring Nancy Kelly, Patty McCormack, Henry Jones and Eileen Heckart, about an eight-year-old girl whose mother begins to suspect that she m... |

### Which European republic has overseas regions in South America and the Caribbean?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 28.6123 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 22.5370 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 18.5625 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7036 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.6862 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.6848 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.0323 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.0317 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

### Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 35.0096 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 34.0129 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 10.7663 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified; services represent two-thirds of both the workforce and GDP, while the industrial sector accounts... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7356 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.7212 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.6806 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0325 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.0325 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.0315 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified; services represent two-thirds of both the workforce and GDP, while the industrial sector accounts... |

### Which nation has Paris as its largest city and cultural center?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 13.5152 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 11.6454 | wiki_Nuremberg_c2 | 9 | and the newly founded University of Technology Nuremberg. Nürnberg Messe ranks among Germany's largest trade-fair and convention organisers. Nuremberg is known for its well-preserved medieval heritage, including Nuremberg Castle, the Old Town, and the city walls. It is an importa... |
| 3 | 11.1441 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8021 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.7212 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 3 | 0.7125 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.0294 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified; services represent two-thirds of both the workforce and GDP, while the industrial sector accounts... |
| 3 | 0.0290 | wiki_France_c13 | 2 | are manufacturing, real estate, finance and insurance. The Paris Region has the highest concentration of multinational firms in mainland Europe. Under the doctrine of dirigisme, the government historically played a major role in the economy; policies such as indicative planning a... |

### Find the article about the country whose history includes Gauls, Franks, and Napoleon.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 14.1689 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 2 | 13.6961 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 3 | 12.6110 | wiki_The_Bad_Seed_(1956_film)_c0 | 31 | Entity: The_Bad_Seed_(1956_film)  Summary: The Bad Seed is a 1956 American psychological horror thriller film directed by Mervyn LeRoy and starring Nancy Kelly, Patty McCormack, Henry Jones and Eileen Heckart, about an eight-year-old girl whose mother begins to suspect that she m... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7456 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.7310 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.7181 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0320 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 2 | 0.0315 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 3 | 0.0308 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |

### Which Renaissance artist was known as a German painter and printmaker?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 21.7731 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 13.4869 | wiki_Albrecht_Dürer_c1 | 8 | revolutionised the potential of that medium, while his extraordinary handling of the burin expanded especially the tonal range of his engravings. Dürer's introduction of classical motifs and of the nude into Northern art, through his knowledge of Italian artists and German humani... |
| 3 | 13.0358 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7439 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7025 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 3 | 0.6936 | wiki_Albrecht_Dürer_c3 | 8 | his German successors; the "Little Masters" who attempted few large engravings but continued Dürer's themes in small, rather cramped compositions. Lucas van Leyden was the only Northern European engraver to successfully continue to produce large engravings in the first third of t... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.0315 | wiki_Albrecht_Dürer_c1 | 8 | revolutionised the potential of that medium, while his extraordinary handling of the burin expanded especially the tonal range of his engravings. Dürer's introduction of classical motifs and of the nude into Northern art, through his knowledge of Italian artists and German humani... |
| 3 | 0.0306 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |

### Who created works during the Northern Renaissance and was linked to Nuremberg?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 19.5348 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 2 | 17.2264 | wiki_Albrecht_Dürer_c1 | 8 | revolutionised the potential of that medium, while his extraordinary handling of the burin expanded especially the tonal range of his engravings. Dürer's introduction of classical motifs and of the nude into Northern art, through his knowledge of Italian artists and German humani... |
| 3 | 17.1335 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7733 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 2 | 0.7642 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.7342 | wiki_Nuremberg_c7 | 9 | Adam Kraft and Peter Vischer are also associated with Nuremberg. Composed of prosperous artisans, the guilds of the Meistersingers flourished here. Richard Wagner made their most famous member, Hans Sachs, the hero of his opera Die Meistersinger von Nürnberg. Baroque composer Joh... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0320 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 2 | 0.0320 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.0318 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |

### Find the article about an artist known for engravings and self-portraits.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 12.7434 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 11.4437 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |
| 3 | 10.5401 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7135 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.6387 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |
| 3 | 0.6359 | wiki_Albrecht_Dürer_c5 | 8 | – along with other works of art were stolen from the National Art Museum of Azerbaijan. The drawings were later recovered.  Section: List of works List of paintings by Albrecht Dürer List of engravings by Albrecht Dürer List of woodcuts by Albrecht Dürer  Section: Further reading... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.0320 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |
| 3 | 0.0315 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

### Which Finnish football team is commonly abbreviated as HJK?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 20.6605 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 14.6492 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 13.8359 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8382 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.7983 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.7836 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.0320 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.0313 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

### Find the Helsinki football club article without using its full Finnish name.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 17.0989 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 12.7893 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 10.9666 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7446 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6807 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.6755 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.0320 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 0.0315 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

### Which sports club is described as a major Finnish football club from Helsinki?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 20.3136 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 19.3485 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 12.9811 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8284 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.7819 | wiki_Helsingin_Jalkapalloklubi_c4 | 5 | as well. Before the 1970s HJK came to be known especially as a Töölöan club due to most of their activity taking place in this particular district. During recent decades the club's old image as a prosperous, middle class group from Töölö has largely disappeared due to social chan... |
| 3 | 0.7746 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.0320 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 0.0315 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

### Which Bavarian city is associated with imperial history and Renaissance art?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 19.2519 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 2 | 13.3416 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 3 | 12.4265 | wiki_Nuremberg_c7 | 9 | Adam Kraft and Peter Vischer are also associated with Nuremberg. Composed of prosperous artisans, the guilds of the Meistersingers flourished here. Richard Wagner made their most famous member, Hans Sachs, the hero of his opera Die Meistersinger von Nürnberg. Baroque composer Joh... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7344 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 2 | 0.7142 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.7138 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 2 | 0.0320 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 3 | 0.0310 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |

### Find the German city connected to Franconia and medieval history.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 14.9533 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 13.9661 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |
| 3 | 13.1452 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7771 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.7325 | wiki_Nuremberg_c4 | 9 | a strong base in the city. Nuremberg is still an important industrial centre with a strong standing in the markets of Central and Eastern Europe. Items manufactured in the area include electrical equipment, mechanical and optical products, motor vehicles, writing and drawing para... |
| 3 | 0.7281 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.0312 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |
| 3 | 0.0308 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

### Which city in Germany is linked to Albrecht Durer?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 10.7654 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 10.7620 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, Dover Publications, New York 1963 (2nd ed. 2000), ISBN 0-486-21097-9.  Section: External links  Colvi... |
| 3 | 9.3071 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8001 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7664 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.7602 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.0313 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.0311 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, Dover Publications, New York 1963 (2nd ed. 2000), ISBN 0-486-21097-9.  Section: External links  Colvi... |

### Find the article about a European city in Bavaria without naming the city directly.

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 16.7515 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 16.3970 | wiki_Aris_Thessaloniki_F.C._c1 | 37 | in the Ludovisi Ares sculpture. It is considered as one of the biggest teams in Greece and is part of the multi-sports club Aris Thessaloniki. Aris was also one of the strongest and most popular teams in Greece during the interwar period. They have won the Greek championship thre... |
| 3 | 15.1448 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7542 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.7204 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.7007 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |

#### HYBRID

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0328 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.0305 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.0303 | wiki_Nuremberg_c3 | 9 | has been a destination for immigrants. 19.2% of the residents had an immigrant background in 2022 (counted with MigraPro).  Section: Economy Nuremberg for many people is still associated with its traditional gingerbread (Lebkuchen) products, sausages, and handmade toys. Pocket wa... |

