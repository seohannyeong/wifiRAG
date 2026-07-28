# TF-IDF Metric Comparison

같은 TF-IDF 검색에서 cosine, euclidean, euclidean without normalization을 비교한 결과입니다.

## Top-1 Summary

| Query | TF-IDF Cosine L2 | TF-IDF Euclidean L2 | TF-IDF Euclidean No Norm | Top-1 Same | Shared Top-k |
| --- | --- | --- | --- | --- | ---: |
| Which European republic has overseas regions in South America and the Caribbean? | wiki_France_c0<br>p.2 c.0<br>0.3047 | wiki_France_c0<br>p.2 c.0<br>0.4589 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0367 | different | 0 |
| Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain? | wiki_France_c7<br>p.2 c.7<br>0.2934 | wiki_France_c7<br>p.2 c.7<br>0.4569 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0355 | different | 0 |
| Find the article about the country whose history includes Gauls, Franks, and Napoleon. | wiki_France_c4<br>p.2 c.4<br>0.1304 | wiki_France_c4<br>p.2 c.4<br>0.4313 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0358 | different | 0 |
| Which French town near western Paris was associated with Impressionist painters? | wiki_Chatou_c1<br>p.1 c.1<br>0.1581 | wiki_Chatou_c1<br>p.1 c.1<br>0.4352 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0365 | different | 0 |
| Where did painters gather around Maison Fournaise and the Seine? | wiki_Chatou_c1<br>p.1 c.1<br>0.2963 | wiki_Chatou_c1<br>p.1 c.1<br>0.4574 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0368 | different | 0 |
| Which South Korean football club played in the K3 League? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.4543 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.4891 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0378 | different | 0 |
| Find the article about a semi-professional football team from Gyeonggi Province. | wiki_Hereford_United_F.C._c4<br>p.29 c.4<br>0.1279 | wiki_Hereford_United_F.C._c4<br>p.29 c.4<br>0.4309 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0380 | different | 0 |
| Which Renaissance artist was known as a German painter and printmaker? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.1963 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.4409 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0370 | different | 0 |
| Find the article about an artist known for engravings and self-portraits. | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.1169 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.4294 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0370 | different | 0 |
| Which Finnish football team is commonly abbreviated as HJK? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.4699 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.4927 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0385 | different | 0 |
| Find the Helsinki football club article without using its full Finnish name. | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.3042 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.4588 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0364 | different | 0 |
| Which Bavarian city is associated with imperial history and Renaissance art? | wiki_Nuremberg_c0<br>p.9 c.0<br>0.2466 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.4489 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0380 | different | 0 |
| Find the German city connected to Franconia and medieval history. | wiki_Nuremberg_c0<br>p.9 c.0<br>0.1904 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.4401 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0377 | different | 0 |
| Find a very short external links section about a football club. | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.1788 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.4383 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0397 | different | 1 |
| Find a chunk that mostly contains references or external links. | wiki_France_c6<br>p.2 c.6<br>0.1125 | wiki_France_c6<br>p.2 c.6<br>0.4288 | wiki_Héctor_Cúper_c2<br>p.36 c.2<br>0.0384 | different | 0 |

## Detailed Results

### Which European republic has overseas regions in South America and the Caribbean?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3047 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.2278 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.1559 | wiki_France_c3 | 2 | Bourbon Restoration until the founding of the French Second Republic, which was succeeded by the Second French Empire upon Napoleon III's takeover. His empire collapsed during the Franco-Prussian War in 1870. This led to the establishment of the French Third Republic, as well as... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4589 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 2 | 0.4459 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 3 | 0.4349 | wiki_France_c3 | 2 | Bourbon Restoration until the founding of the French Second Republic, which was succeeded by the Second French Empire upon Napoleon III's takeover. His empire collapsed during the Franco-Prussian War in 1870. This led to the establishment of the French Third Republic, as well as... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0367 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0331 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0325 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Which country borders Belgium, Germany, Switzerland, Italy, Monaco, Andorra, and Spain?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2934 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.2761 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.0741 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified; services represent two-thirds of both the workforce and GDP, while the industrial sector accounts... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4569 | wiki_France_c7 | 2 | English.  Section: Geography The vast majority of France's territory and population is situated in Western Europe and is called Metropolitan France. It is bordered by the North Sea in the north, the English Channel in the northwest, the Atlantic Ocean in the west and the Mediterr... |
| 2 | 0.4539 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in South America, Saint Pierre and Miquelon in the North Atlantic, the French West Indies, and many island... |
| 3 | 0.4236 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified; services represent two-thirds of both the workforce and GDP, while the industrial sector accounts... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0355 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0322 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0317 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Find the article about the country whose history includes Gauls, Franks, and Napoleon.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1304 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 2 | 0.1236 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |
| 3 | 0.1236 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4313 | wiki_France_c4 | 2 | Gaulle. Algeria and most French colonies became independent in the 1960s, with the majority retaining close economic and military ties with France. France retains its centuries-long status as a global centre of art, science, cuisine and philosophy. It hosts the fourth-largest num... |
| 2 | 0.4303 | wiki_France_c5 | 2 | forums.  Section: Etymology Originally applied to the whole Frankish Empire, the name France comes from the Latin Francia, or 'realm of the Franks'. The name of the Franks is related to the English word frank ('free'): the latter stems from the Old French franc ('free, noble, sin... |
| 3 | 0.4303 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0358 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0324 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0320 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Which French town near western Paris was associated with Impressionist painters?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1581 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.1425 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |
| 3 | 0.1230 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4352 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.4330 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominated by the conflict with the House of Habsburg and the French Wars of Religion between Catholics and H... |
| 3 | 0.4302 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0365 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0330 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0324 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Where did painters gather around Maison Fournaise and the Seine?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2963 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.1656 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 0.0858 | wiki_Nuremberg_c9 | 9 | dominated by the front of the unique Gothic Frauenkirche (Our Lady's Church), provides a picturesque setting for the famous Christmas market. A main attraction on the square is the Gothic Schöner Brunnen (Beautiful Fountain) which was erected around 1385 but subsequently replaced... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4574 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Île des Impressionnistes, formerly a meeting place for Impressionist painters on the Seine. It was a p... |
| 2 | 0.4363 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affluent suburbs of western Paris and is on the northwest side of the Seine river about 14 km (9 mi) fro... |
| 3 | 0.4251 | wiki_Nuremberg_c9 | 9 | dominated by the front of the unique Gothic Frauenkirche (Our Lady's Church), provides a picturesque setting for the famous Christmas market. A main attraction on the square is the Gothic Schöner Brunnen (Beautiful Fountain) which was erected around 1385 but subsequently replaced... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0368 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0331 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0326 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Which South Korean football club played in the K3 League?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4543 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.1982 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |
| 3 | 0.1957 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4891 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.4412 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |
| 3 | 0.4409 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0378 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0340 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0338 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Find the article about a semi-professional football team from Gyeonggi Province.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1279 | wiki_Hereford_United_F.C._c4 | 29 | He became manager a year later and set about building a team to challenge at the top of the Southern League and gain election to the Football League. With the club becoming one of the best-supported non-league clubs in the country Charles used his standing within the game to canv... |
| 2 | 0.1244 | wiki_Malta_national_football_team_c0 | 35 | Entity: Malta_national_football_team  Summary: The Malta national football team (Maltese: Tim nazzjonali tal-futbol ta' Malta) represents Malta in men's international football and is controlled by the Malta Football Association, the governing body for football in Malta. The first... |
| 3 | 0.1134 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4309 | wiki_Hereford_United_F.C._c4 | 29 | He became manager a year later and set about building a team to challenge at the top of the Southern League and gain election to the Football League. With the club becoming one of the best-supported non-league clubs in the country Charles used his standing within the game to canv... |
| 2 | 0.4304 | wiki_Malta_national_football_team_c0 | 35 | Entity: Malta_national_football_team  Summary: The Malta national football team (Maltese: Tim nazzjonali tal-futbol ta' Malta) represents Malta in men's international football and is controlled by the Malta Football Association, the governing body for football in Malta. The first... |
| 3 | 0.4289 | wiki_Hereford_United_F.C._c3 | 29 | –  but played only a few games in this league before the outbreak of the Second World War. At the same time the club became a limited company. When football resumed after the war, Hereford finished 1st in their first full season in the league only to be demoted to 2nd behind Chel... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0380 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0345 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |
| 3 | 0.0341 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |

### Which Renaissance artist was known as a German painter and printmaker?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1963 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.1154 | wiki_Albrecht_Dürer_c1 | 8 | revolutionised the potential of that medium, while his extraordinary handling of the burin expanded especially the tonal range of his engravings. Dürer's introduction of classical motifs and of the nude into Northern art, through his knowledge of Italian artists and German humani... |
| 3 | 0.1059 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4409 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.4292 | wiki_Albrecht_Dürer_c1 | 8 | revolutionised the potential of that medium, while his extraordinary handling of the burin expanded especially the tonal range of his engravings. Dürer's introduction of classical motifs and of the nude into Northern art, through his knowledge of Italian artists and German humani... |
| 3 | 0.4279 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0370 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0332 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0327 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Find the article about an artist known for engravings and self-portraits.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1169 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.1079 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |
| 3 | 0.0966 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4294 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German painter, printmaker, and theorist of the German Renaissance. Born in Nuremberg, Dürer established his r... |
| 2 | 0.4281 | wiki_Albrecht_Dürer_c4 | 8 | in Italy, where probably only his altarpiece in Venice was seen, and his German successors were less effective in blending German and Italian styles. His intense and self-dramatizing self-portraits have continued to have a strong influence up to the present, especially on painter... |
| 3 | 0.4266 | wiki_Albrecht_Dürer_c2 | 8 | Thus, Dürer contributed to the expansion in German prose which Luther had begun with his translation of the Bible.  Section: Legacy and influence Dürer exerted a huge influence on the artists of succeeding generations, especially in printmaking, the medium through which his conte... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0370 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0333 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0329 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Which Finnish football team is commonly abbreviated as HJK?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4699 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.3445 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.2723 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4927 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.4662 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |
| 3 | 0.4532 | wiki_Helsingin_Jalkapalloklubi_c5 | 5 | kenttä, and in 1909–1914 at the Eläintarha Stadium. HJK's first official home ground was Töölön Pallokenttä where they played in 1915–1998. During the Veikkausliiga era, HJK played their home matches occasionally also at the Helsinki Olympic Stadium.  Section: Transfers HJK Helsi... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0385 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0347 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |
| 3 | 0.0343 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |

### Find the Helsinki football club article without using its full Finnish name.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3042 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.1667 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 0.1403 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4588 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 2 | 0.4365 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide support within Finnish speaking, prosperous middle class of Helsinki. The club's supporters were often... |
| 3 | 0.4327 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was established in 1997, when the club celebrated its 90th anniversary. Initially 16 people were named, after whi... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0364 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0329 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0328 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Which Bavarian city is associated with imperial history and Renaissance art?

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2466 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.2081 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.1354 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4489 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.4428 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the Renaissance, Nuremberg was also a centre of art, publishing, and scientific innovation, and was assoc... |
| 3 | 0.4320 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0380 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0340 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0334 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Find the German city connected to Franconia and medieval history.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1904 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.1445 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |
| 3 | 0.1312 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4401 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria and the largest city in the cultural region of Franconia. Its 546,397 (2024) inhabitants make it the... |
| 2 | 0.4333 | wiki_Nuremberg_c13 | 9 | Prize  Section: External links   Nuremberg travel guide from Wikivoyage Chisholm, Hugh, ed. (1911). "Nuremberg" . Encyclopædia Britannica. Vol. 19 (11th ed.). Cambridge University Press. English website of the city KUNSTNÜRNBERG – Online – Magazine for Contemporary Art and Histor... |
| 3 | 0.4314 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo stretching over more than 60 hectares (148 acres) in the Nuremberg Reichswald (or Nürnberger Reichsw... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0377 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0338 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |
| 3 | 0.0333 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

### Find a very short external links section about a football club.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1788 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.1500 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.1411 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4383 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of Uijeongbu not far from Seoul. The club is a member of the K3 League, the third tier of league footba... |
| 2 | 0.4341 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK (Finnish: ['hoː jiː koː]), is a Finnish football club based in Helsinki. The club competes in Veikk... |
| 3 | 0.4328 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0397 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0351 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |
| 3 | 0.0344 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |

### Find a chunk that mostly contains references or external links.

#### TF-IDF Cosine L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1125 | wiki_France_c6 | 2 | free of taxation or, more generally, because they had the status of freemen in contrast to servants or slaves. The etymology of *Frank is uncertain. It is traditionally derived from the Proto-Germanic word *frankōn, which translates to 'javelin' or 'lance' (the throwing axe of th... |
| 2 | 0.0825 | wiki_William_Hopper_c2 | 30 | and Gilbert had separated. They later divorced, and Hopper married Jeanette Juanita Ward. They remained together until his death.  Section: Death Hopper entered Desert Hospital in Palm Springs, California, on February 14, 1970, after suffering a stroke. He died of pneumonia three... |
| 3 | 0.0802 | wiki_Harvard_University_c4 | 33 | the country. Harvard and the other seven Ivy League universities are prohibited from offering athletic scholarships. The school color is crimson.  Section: In popular culture Harvard's reputation as a center of elite achievement or elitist privilege has made it a frequent literar... |

#### TF-IDF Euclidean L2

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.4288 | wiki_France_c6 | 2 | free of taxation or, more generally, because they had the status of freemen in contrast to servants or slaves. The etymology of *Frank is uncertain. It is traditionally derived from the Proto-Germanic word *frankōn, which translates to 'javelin' or 'lance' (the throwing axe of th... |
| 2 | 0.4247 | wiki_William_Hopper_c2 | 30 | and Gilbert had separated. They later divorced, and Hopper married Jeanette Juanita Ward. They remained together until his death.  Section: Death Hopper entered Desert Hospital in Palm Springs, California, on February 14, 1970, after suffering a stroke. He died of pneumonia three... |
| 3 | 0.4244 | wiki_Harvard_University_c4 | 33 | the country. Harvard and the other seven Ivy League universities are prohibited from offering athletic scholarships. The school color is crimson.  Section: In popular culture Harvard's reputation as a center of elite achievement or elitist privilege has made it a frequent literar... |

#### TF-IDF Euclidean No Norm

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.0384 | wiki_Héctor_Cúper_c2 | 36 | División in 1982 and 1984.  Section: Managerial statistics As of 18 July 2026  Section: External links  Héctor Cúper manager profile at BDFutbol Héctor Cúper at WorldFootball.net |
| 2 | 0.0337 | wiki_Malta_national_football_team_c11 | 35 | of 5 June 2026.   Positive record   Neutral record   Negative record  Section: FIFA rankings As of 10 February 2022  Section: External links  Official site of the Malta Football Association Malta at UEFA Malta at FIFA RSSSF archive of results from 1957 Reports for all matches of... |
| 3 | 0.0337 | wiki_Aris_Thessaloniki_F.C._c7 | 37 | (in Greek) Aris Thessaloniki on pressaris.gr (in Greek) Aris Thessaloniki on yellowradio.gr (in Greek) Current results of ARIS matches Media  Official Facebook page Official YouTube channel |

