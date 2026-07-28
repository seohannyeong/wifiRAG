# Dense Metric Comparison

Ollama embedding 결과를 같은 조건에서 cosine similarity와 Euclidean similarity로 비교한 결과입니다.

## Top-1 Summary

| Query | Cosine Top-1 | Euclidean Top-1 | Top-1 Same | Top-k Overlap |
| --- | --- | --- | --- | ---: |
| Which French town near western Paris was associated with Impressionist painters? | wiki_Chatou_c1<br>p.1 c.1<br>0.7211 | wiki_Chatou_c1<br>p.1 c.1<br>0.5725 | same | 3 |
| Which riverside suburb was described by Renoir as a pretty spot near Paris? | wiki_Chatou_c1<br>p.1 c.1<br>0.7134 | wiki_Chatou_c1<br>p.1 c.1<br>0.5691 | same | 3 |
| Where did painters gather around Maison Fournaise and the Seine? | wiki_Chatou_c1<br>p.1 c.1<br>0.7807 | wiki_Chatou_c1<br>p.1 c.1<br>0.6016 | same | 3 |
| Which place opened a museum dedicated to Sufism in 2024? | wiki_Chatou_c2<br>p.1 c.2<br>0.5928 | wiki_Chatou_c2<br>p.1 c.2<br>0.5256 | same | 3 |
| Which South Korean football club played in the K3 League? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.7414 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.5817 | same | 3 |
| Find the article about a semi-professional football team from Gyeonggi Province. | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.7483 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.5850 | same | 3 |
| Which club name is connected to Yangju and Korean football? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8296 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.6314 | same | 3 |
| Which European republic has overseas regions in South America and the Caribbean? | wiki_France_c0<br>p.2 c.0<br>0.7036 | wiki_France_c0<br>p.2 c.0<br>0.5650 | same | 3 |
| Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain? | wiki_France_c7<br>p.2 c.7<br>0.7356 | wiki_France_c7<br>p.2 c.7<br>0.5790 | same | 3 |
| Which nation has Paris as its largest city and cultural center? | wiki_France_c1<br>p.2 c.1<br>0.8021 | wiki_France_c1<br>p.2 c.1<br>0.6138 | same | 3 |
| Find the article about the country whose history includes Gauls, Franks, and Napoleon. | wiki_France_c0<br>p.2 c.0<br>0.7456 | wiki_France_c0<br>p.2 c.0<br>0.5837 | same | 3 |
| Which Renaissance artist was known as a German painter and printmaker? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.7439 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.5829 | same | 3 |
| Who created works during the Northern Renaissance and was linked to Nuremberg? | wiki_Nuremberg_c6<br>p.9 c.6<br>0.7733 | wiki_Nuremberg_c6<br>p.9 c.6<br>0.5976 | same | 3 |
| Find the article about an artist known for engravings and self-portraits. | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.7135 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.5692 | same | 3 |
| Which Finnish football team is commonly abbreviated as HJK? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8382 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6374 | same | 3 |
| Find the Helsinki football club article without using its full Finnish name. | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.7446 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.5832 | same | 3 |
| Which sports club is described as a major Finnish football club from Helsinki? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8284 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6306 | same | 3 |
| Which Bavarian city is associated with imperial history and Renaissance art? | wiki_Nuremberg_c1<br>p.9 c.1<br>0.7344 | wiki_Nuremberg_c1<br>p.9 c.1<br>0.5784 | same | 3 |
| Find the German city connected to Franconia and medieval history. | wiki_Nuremberg_c0<br>p.9 c.0<br>0.7771 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.5996 | same | 3 |
| Which city in Germany is linked to Albrecht Durer? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8001 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.6126 | same | 3 |
| Find the article about a European city in Bavaria without naming the city directly. | wiki_Nuremberg_c0<br>p.9 c.0<br>0.7542 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.5879 | same | 3 |

## Detailed Results

### Which French town near western Paris was associated with Impressionist painters?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7211 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6327 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5988 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5725 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.5385 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5275 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

### Which riverside suburb was described by Renoir as a pretty spot near Paris?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7134 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6433 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6224 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5691 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.5421 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5350 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

### Where did painters gather around Maison Fournaise and the Seine?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7807 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.6494 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.6313 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6016 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.5443 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 3 | 0.5380 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

### Which place opened a museum dedicated to Sufism in 2024?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5928 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 2 | 0.5914 | wiki_Trinity_University_(Texas)_c5 | 7 | for its large Hofmann-Ballard pipe organ, the largest pipe organ in South Texas, comprising 5 divisions, 102 stops, 112 ranks, and over 6,000 pipes. A state-of-the-art four-manual console was installed in summer 2007, with the aid of the university's Calvert Trust Fund. Non-denom... |
| 3 | 0.5886 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5256 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the Nazis shot 27 people, civilians and members of the French Resistance. This event is today known as th... |
| 2 | 0.5252 | wiki_Trinity_University_(Texas)_c5 | 7 | for its large Hofmann-Ballard pipe organ, the largest pipe organ in South Texas, comprising 5 divisions, 102 stops, 112 ranks, and over 6,000 pipes. A state-of-the-art four-manual console was installed in summer 2007, with the aid of the university's Calvert Trust Fund. Non-denom... |
| 3 | 0.5244 | wiki_Nuremberg_c10 | 9 | is integrated into the building of the Germanisches Nationalmuseum and the choir of the former Franziskanerkirche is part of a modern building. Other churches located inside the city walls are: St. Laurence's, Saint Clare's, Saint Martha's, Saint James the Greater's, Saint Giles'... |

### Which South Korean football club played in the K3 League?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7414 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6630 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.6471 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5817 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5492 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.5434 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

### Find the article about a semi-professional football team from Gyeonggi Province.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7483 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6928 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.6889 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5850 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5606 | wiki_Aris_Thessaloniki_F.C._c0 | 37 | Entity: Aris_Thessaloniki_F.C.  Summary: Aris FC (Greek: ΠΑΕ Άρης) ['aris], commonly known as Aris Thessaloniki or simply Aris, is a Greek professional football club from the city of Thessaloniki, Macedonia, Greece. The team competes in the top-tier Super League Greece and their... |
| 3 | 0.5590 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |

### Which club name is connected to Yangju and Korean football?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8296 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.6680 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |
| 3 | 0.6645 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6314 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.5510 | wiki_Hereford_United_F.C._c0 | 29 | Entity: Hereford_United_F.C.  Summary: Hereford United Football Club was an association football club based in Hereford, England. They played at Edgar Street for their entire history. They were nicknamed 'The Whites' or 'The Lilywhites', after their predominantly white kit, or 'T... |
| 3 | 0.5497 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

### Which European republic has overseas regions in South America and the Caribbean?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7036 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.6862 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.6848 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5650 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.5580 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.5574 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

### Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7356 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.7212 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.6806 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5790 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.5725 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.5558 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

### Which nation has Paris as its largest city and cultural center?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8021 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.7212 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 3 | 0.7125 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6138 | wiki_France_c1 | 2 | of which are overseas—span a combined area of 632,702 km2 (244,288 sq mi), with a total population estimated at over 69.1 million in 2026. Its capital, largest city and main cultural and economic centre is Paris, with a metropolitan population of over 13 million. Metropolitan Fra... |
| 2 | 0.5725 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 3 | 0.5687 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mostly between latitudes 41° and 51° N, and longitudes 6° W and 10° E, on the western edge of Europe,... |

### Find the article about the country whose history includes Gauls, Franks, and Napoleon.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7456 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.7310 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.7181 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5837 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.5769 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.5711 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |

### Which Renaissance artist was known as a German painter and printmaker?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7439 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7025 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 3 | 0.6936 | wiki_Albrecht_Dürer_c3 | 8 | his German successors; the "Little Masters" who attempted few large engravings but continued Dürer's themes in small, rather cramped compositions. Lucas van Leyden was the only Northern European engraver to successfully continue to produce large engravings in the first third of t... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5829 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5645 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 3 | 0.5609 | wiki_Albrecht_Dürer_c3 | 8 | his German successors; the "Little Masters" who attempted few large engravings but continued Dürer's themes in small, rather cramped compositions. Lucas van Leyden was the only Northern European engraver to successfully continue to produce large engravings in the first third of t... |

### Who created works during the Northern Renaissance and was linked to Nuremberg?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7733 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 2 | 0.7642 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.7342 | wiki_Nuremberg_c7 | 9 | Adam Kraft and Peter Vischer are also associated with Nuremberg. Composed of prosperous artisans, the guilds of the Meistersingers flourished here. Richard Wagner made their most famous member, Hans Sachs, the hero of his opera Die Meistersinger von Nürnberg. Baroque composer Joh... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5976 | wiki_Nuremberg_c6 | 9 | history in Nuremberg. Many of these publishers worked with well-known artists of the day to produce books that could also be considered works of art. In 1470 Anton Koberger opened Europe's first print shop in Nuremberg. In 1493, he published the Nuremberg Chronicles, also known a... |
| 2 | 0.5929 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.5783 | wiki_Nuremberg_c7 | 9 | Adam Kraft and Peter Vischer are also associated with Nuremberg. Composed of prosperous artisans, the guilds of the Meistersingers flourished here. Richard Wagner made their most famous member, Hans Sachs, the hero of his opera Die Meistersinger von Nürnberg. Baroque composer Joh... |

### Find the article about an artist known for engravings and self-portraits.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7135 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.6387 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |
| 3 | 0.6359 | wiki_Albrecht_Dürer_c5 | 8 | – along with other works of art were stolen from the National Art Museum of Azerbaijan. The drawings were later recovered.  Section: List of works List of paintings by Albrecht Dürer List of engravings by Albrecht Dürer List of woodcuts by Albrecht Dürer  Section: Further reading... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5692 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5405 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |
| 3 | 0.5396 | wiki_Albrecht_Dürer_c5 | 8 | – along with other works of art were stolen from the National Art Museum of Azerbaijan. The drawings were later recovered.  Section: List of works List of paintings by Albrecht Dürer List of engravings by Albrecht Dürer List of woodcuts by Albrecht Dürer  Section: Further reading... |

### Which Finnish football team is commonly abbreviated as HJK?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8382 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.7983 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.7836 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6374 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6115 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that has participated in the UEFA Champions League group stage. In 1998, they beat Metz in the play-off ro... |
| 3 | 0.6032 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

### Find the Helsinki football club article without using its full Finnish name.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7446 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6807 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.6755 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5832 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.5558 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.5538 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

### Which sports club is described as a major Finnish football club from Helsinki?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8284 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.7819 | wiki_Helsingin_Jalkapalloklubi_c4 | 5 | as well. Before the 1970s HJK came to be known especially as a Töölöan club due to most of their activity taking place in this particular district. During recent decades the club's old image as a prosperous, middle class group from Töölö has largely disappeared due to social chan... |
| 3 | 0.7746 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6306 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.6022 | wiki_Helsingin_Jalkapalloklubi_c4 | 5 | as well. Before the 1970s HJK came to be known especially as a Töölöan club due to most of their activity taking place in this particular district. During recent decades the club's old image as a prosperous, middle class group from Töölö has largely disappeared due to social chan... |
| 3 | 0.5983 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |

### Which Bavarian city is associated with imperial history and Renaissance art?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7344 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 2 | 0.7142 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.7138 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5784 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 2 | 0.5694 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |
| 3 | 0.5693 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |

### Find the German city connected to Franconia and medieval history.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7771 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.7325 | wiki_Nuremberg_c4 | 9 | a strong base in the city. Nuremberg is still an important industrial centre with a strong standing in the markets of Central and Eastern Europe. Items manufactured in the area include electrical equipment, mechanical and optical products, motor vehicles, writing and drawing para... |
| 3 | 0.7281 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5996 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.5776 | wiki_Nuremberg_c4 | 9 | a strong base in the city. Nuremberg is still an important industrial centre with a strong standing in the markets of Central and Eastern Europe. Items manufactured in the area include electrical equipment, mechanical and optical products, motor vehicles, writing and drawing para... |
| 3 | 0.5755 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

### Which city in Germany is linked to Albrecht Durer?

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8001 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.7664 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.7602 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6126 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.5940 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhaltene Radierplatte Albrecht Dürers". blog.arthistoricum.net (in German). Saxon State and University Li... |
| 3 | 0.5908 | wiki_Nuremberg_c5 | 9 | tourist destination for foreigners and Germans alike. After World War II, many medieval-style areas of the town were rebuilt.  Section: Culture Nuremberg was an early centre of humanism, science, printing, and mechanical invention. The city contributed much to the science of astr... |

### Find the article about a European city in Bavaria without naming the city directly.

#### Cosine

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7542 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.7204 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.7007 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |

#### Euclidean

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5879 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.5721 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg has historically been left-leaning in the conservative state of Bavaria – since the end of World War I... |
| 3 | 0.5638 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |

