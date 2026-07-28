# Retriever Comparison

BM25, TF-IDF, Dense Ollama retriever의 검색 결과를 같은 query 기준으로 비교한 리포트입니다.

## Top-1 Summary

| Query | BM25 | TFIDF | DENSE | Agreement |
| --- | --- | --- | --- | --- |
| Where is Chatou located? | wiki_Chatou_c1<br>p.1 c.1<br>8.1243 | wiki_Chatou_c0<br>p.1 c.0<br>0.2283 | wiki_Chatou_c0<br>p.1 c.0<br>0.8170 | different |
| Chatou commune Yvelines France | wiki_Chatou_c0<br>p.1 c.0<br>18.2136 | wiki_Chatou_c0<br>p.1 c.0<br>0.3199 | wiki_Chatou_c0<br>p.1 c.0<br>0.8039 | same |
| What is Yangju Citizen Football Club? | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>23.3841 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.5771 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8971 | same |
| Yangju Citizen football club K3 League | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>31.2388 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.7018 | wiki_Yangju_Citizen_FC_c0<br>p.3 c.0<br>0.8674 | same |
| What country is France located in Western Europe? | wiki_France_c0<br>p.2 c.0<br>16.5925 | wiki_France_c18<br>p.2 c.18<br>0.1988 | wiki_France_c8<br>p.2 c.8<br>0.7483 | different |
| France French Republic Western Europe | wiki_France_c0<br>p.2 c.0<br>14.4176 | wiki_France_c2<br>p.2 c.2<br>0.3046 | wiki_France_c0<br>p.2 c.0<br>0.6934 | different |
| Who was Albrecht Durer? | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>9.4935 | wiki_Albrecht_Dürer_c6<br>p.8 c.6<br>0.2661 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8515 | different |
| Albrecht Durer Renaissance artist | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>10.6979 | wiki_Albrecht_Dürer_c6<br>p.8 c.6<br>0.2045 | wiki_Albrecht_Dürer_c0<br>p.8 c.0<br>0.8396 | different |
| What is Helsingin Jalkapalloklubi? | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>14.7273 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.2272 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8037 | same |
| HJK Helsinki Finnish football club | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>19.2174 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.6283 | wiki_Helsingin_Jalkapalloklubi_c0<br>p.5 c.0<br>0.8533 | same |
| Where is Nuremberg located? | wiki_Nuremberg_c11<br>p.9 c.11<br>8.5381 | wiki_Nuremberg_c11<br>p.9 c.11<br>0.2690 | wiki_Nuremberg_c11<br>p.9 c.11<br>0.7983 | same |
| Nuremberg Bavaria Germany city | wiki_Nuremberg_c0<br>p.9 c.0<br>12.0352 | wiki_Nuremberg_c1<br>p.9 c.1<br>0.2848 | wiki_Nuremberg_c0<br>p.9 c.0<br>0.8245 | different |

## Detailed Results

### Where is Chatou located?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 8.1243 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Îl... |
| 2 | 8.0717 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2283 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |
| 2 | 0.2070 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the N... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8170 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |
| 2 | 0.7052 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the N... |

### Chatou commune Yvelines France

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 18.2136 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |
| 2 | 8.7537 | wiki_Chatou_c1 | 1 | to create the commune of Le Vésinet. It boasts many bourgeois mansions of every kind of architecture and owned by private individuals.  Chatou is home to Maison Fournaise on the Îl... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3199 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |
| 2 | 0.1798 | wiki_France_c18 | 2 | percent per year; since 2011, annual growth has been between 0.4 and 0.5 percent annually, and France is projected to continue growing until 2044. Immigrants are major contributors... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8039 | wiki_Chatou_c0 | 1 | Entity: Chatou  Summary: Chatou (French pronunciation: [ʃatu] ) is a commune in the Yvelines department in the Île-de-France region in northern France. Chatou is a part of the affl... |
| 2 | 0.6884 | wiki_Chatou_c2 | 1 | festive atmosphere inspired Impressionist painters such as Claude Monet, Edgar Degas, Alfred Sisley, Gustave Caillebotte and especially Renoir.  On 25 August 1944, in Chatou, the N... |

### What is Yangju Citizen Football Club?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 23.3841 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 5.8783 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.5771 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 0.1465 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8971 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 0.6474 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

### Yangju Citizen football club K3 League

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 31.2388 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 5.6595 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7018 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 0.1437 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8674 | wiki_Yangju_Citizen_FC_c0 | 3 | Entity: Yangju_Citizen_FC  Summary: Yangju Citizen Football Club (양주 시민 축구단) is a South Korean football club based in the city of Yangju, located south of Dongducheon and north of... |
| 2 | 0.6250 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |

### What country is France located in Western Europe?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 16.5925 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in Sou... |
| 2 | 12.6133 | wiki_France_c11 | 2 | countries, the Organisation for Economic Co-operation and Development (OECD), and the G20. France ranked 13th in the 2025 Global Innovation Index. The economy is highly diversified... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.1988 | wiki_France_c18 | 2 | percent per year; since 2011, annual growth has been between 0.4 and 0.5 percent annually, and France is projected to continue growing until 2044. Immigrants are major contributors... |
| 2 | 0.1816 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in Sou... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7483 | wiki_France_c8 | 2 | and the Netherlands through Saint Martin in the Caribbean. Metropolitan France includes various coastal islands, of which the largest is Corsica. Metropolitan France is situated mo... |
| 2 | 0.7347 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in Sou... |

### France French Republic Western Europe

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 14.4176 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in Sou... |
| 2 | 12.2734 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominate... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.3046 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominate... |
| 2 | 0.2838 | wiki_France_c3 | 2 | Bourbon Restoration until the founding of the French Second Republic, which was succeeded by the Second French Empire upon Napoleon III's takeover. His empire collapsed during the... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6934 | wiki_France_c0 | 2 | Entity: France  Summary: France, officially the French Republic, is a country primarily located in Western Europe. Its overseas regions and territories include French Guiana in Sou... |
| 2 | 0.6827 | wiki_France_c2 | 2 | known as the Hundred Years' War. In the 16th century, French culture flourished during the French Renaissance, and a French colonial empire emerged. Internally, France was dominate... |

### Who was Albrecht Durer?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 9.4935 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German pai... |
| 2 | 9.3454 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, D... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2661 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, D... |
| 2 | 0.2073 | wiki_Albrecht_Dürer_c5 | 8 | – along with other works of art were stolen from the National Art Museum of Azerbaijan. The drawings were later recovered.  Section: List of works List of paintings by Albrecht Dür... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8515 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German pai... |
| 2 | 0.7045 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhalt... |

### Albrecht Durer Renaissance artist

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 10.6979 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German pai... |
| 2 | 9.3454 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, D... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2045 | wiki_Albrecht_Dürer_c6 | 8 | and the Unconscious, eds. J. Hendrix and L. Holm, Farnham Surrey: Ashgate, 2016, pp. 27–44, ISBN 978-1-4724-5647-2. Kurth, Wilhelm (ed.). The Complete Woodcuts of Albrecht Durer, D... |
| 2 | 0.1593 | wiki_Albrecht_Dürer_c5 | 8 | – along with other works of art were stolen from the National Art Museum of Azerbaijan. The drawings were later recovered.  Section: List of works List of paintings by Albrecht Dür... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8396 | wiki_Albrecht_Dürer_c0 | 8 | Entity: Albrecht_Dürer  Summary: Albrecht Dürer ( DURE-ər, German: [ˈalbʁɛçt ˈdyːʁɐ]; 21 May 1471 – 6 April 1528), sometimes spelled in English as Durer or Duerer, was a German pai... |
| 2 | 0.7498 | wiki_Albrecht_Dürer_c8 | 8 | Schröder ISBN 978-3791352879 Albrecht Dürer, exhibition, Albertina, Vienna, 20 September 2019 – 6 January 2020. Ehrl, Franziska (28 February 2020). "Schlaglicht: Die einzige erhalt... |

### What is Helsingin Jalkapalloklubi?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 14.7273 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 3.7219 | wiki_The_Bad_Seed_(1956_film)_c8 | 31 | only produce the film for Warner Bros. Pictures upon approval by the PCA. Adler contacted Shurlock demanding to know why approval had been given. Shurlock responded that director M... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2272 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 0.0459 | wiki_Trinity_University_(Texas)_c7 | 7 | and The Center for the Sciences and Innovation have been registered with the Green Building Council's LEED program and are awaiting certification. Trinity is a member of the Presid... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8037 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 0.6741 | wiki_Helsingin_Jalkapalloklubi_c6 | 5 | clubs from HJK.  Section: Reserve team HJK's reserve team Klubi 04 currently plays in the Ykkösliiga, Finnish second tier.  Section: Hall of Fame The HJK Hall of Fame was establish... |

### HJK Helsinki Finnish football club

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 19.2174 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 15.3272 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide sup... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.6283 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 0.3792 | wiki_Helsingin_Jalkapalloklubi_c3 | 5 | seasons in Veikkausliiga/Mestaruussarja/SM-Sarja 6 seasons in Ykkönen/Suomisarja Sources:  Section: Supporters and rivalries HJK Helsinki supporters Historically HJK had a wide sup... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8533 | wiki_Helsingin_Jalkapalloklubi_c0 | 5 | Entity: Helsingin_Jalkapalloklubi  Summary: Helsingin Jalkapalloklubi (lit. 'Helsinki's Football Club'), commonly known as HJK Helsinki (Swedish: HJK Helsingfors), or simply as HJK... |
| 2 | 0.7961 | wiki_Helsingin_Jalkapalloklubi_c1 | 5 | of Finland's most successful players have played for HJK before moving abroad. The club has also similar success with women's Kansallinen Liiga. HJK is the only Finnish club that h... |

### Where is Nuremberg located?

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 8.5381 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo... |
| 2 | 8.1749 | wiki_Nuremberg_c4 | 9 | a strong base in the city. Nuremberg is still an important industrial centre with a strong standing in the markets of Central and Eastern Europe. Items manufactured in the area inc... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2690 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo... |
| 2 | 0.2329 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg ha... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.7983 | wiki_Nuremberg_c11 | 9 | The Rochusfriedhof or the Wöhrder Kirchhof are near the Old Town. The Chain Bridge (Kettensteg), the first chain bridge on the European continent. The Tiergarten Nürnberg is a zoo... |
| 2 | 0.7915 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria a... |

### Nuremberg Bavaria Germany city

#### BM25

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 12.0352 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria a... |
| 2 | 9.9674 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the R... |

#### TFIDF

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.2848 | wiki_Nuremberg_c1 | 9 | significance, imperial diets were frequently held there, and the Imperial Regalia were kept in the city from 1424 until the end of the empire. During the Late Middle Ages and the R... |
| 2 | 0.2774 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria a... |

#### DENSE

| Rank | Score | Chunk | Page | Preview |
| --- | ---: | --- | ---: | --- |
| 1 | 0.8245 | wiki_Nuremberg_c0 | 9 | Entity: Nuremberg  Summary: Nuremberg ( NURE-əm-burg; German: Nürnberg [ˈnʏʁnbɛʁk] ; Mainfränkisch: Nämberch [ˈnɛmbɛrç]) is the second-largest city in the German state of Bavaria a... |
| 2 | 0.8121 | wiki_Nuremberg_c12 | 9 | represented in the Bundestag by two constituencies; Nuremberg North and Nuremberg South. Since 2002, both constituencies have been held by the CSU. At the local level, Nuremberg ha... |

