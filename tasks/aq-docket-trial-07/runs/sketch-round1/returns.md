# Sketch round 1 - local screens (preliminary, not final records), 2026-10-06

Packets reused from prepared run q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148
(corpus-only text/ and docs/; the read guard blocks the packet's question.txt). Each solver was a fresh
blind-solver agent given only the workspace root, the packet path and the sketch question.

## i02 - blind screen (packet solver-1)

Question as tested: "From the month in which seasonally adjusted Midwest manufacturing employment reached its highest level after the Great Recession, through December 2019, what percentage of the net decline in Class I railroad employment came from train-and-engine jobs? Give one decimal place."

Raw return (verbatim):

**Answer: 53.9%**

Midwest manufacturing employment peaked after the Great Recession in February 2019. From February 2019 through December 2019, Class I railroads lost a net 14,314 jobs. Train-and-engine jobs made up 7,715 of them, which is 53.9%.

answer: 53.9%

confidence: high

path:
1. **When the Great Recession ended.** D05 (text\D05.txt, line 1465) says: "From the business cycle peak of December 2007 to the trough of June 2009." D07 note 12 gives the same dates, but D05 alone is enough.
2. **The peak month.** D05 Chart 1 (lines 19–1461) is titled "Manufacturing employment in the Midwest region of the United States, seasonally adjusted, 1990–2019" and is in thousands. I checked every month after June 2009. The series rises to Dec 2018 at 4,123.9 and Jan 2019 at 4,122.3. It peaks in **Feb 2019 at 4,128.8** (line 1419). After that it falls: Mar 2019 is 4,127.3, Apr 4,121.5, and so on down to Dec 2019 at 4,083.7. No other month after the recession is higher. The same rows appear in the docs/ source file (lines 1417–1419).
   - Robustness check: D05 Chart 5's durable plus nondurable figures do not add up to the Chart 1 totals. Their sum still peaks in Feb 2019: 2,719.6 + 1,456.7 = 4,176.3. Dec 2018 sums to 4,171.2 and Mar 2019 to 4,174.7.
3. **Class I employment by type of job.** D04 Chart 4 is titled "Employment in North American Class I rail transportation, by occupational group" and comes from the Surface Transportation Board. Its six columns, in order, are executives; professional and administrative; maintenance of way and structures; maintenance of equipment and stores; transportation (other than train and engine); and transportation (train and engine).
   - Feb 2019 (text line 3074; docs line 3072): 8,127 11,696 31,579 26,981 5,569 61,848. **Total 145,800.**
   - Dec 2019 (text line 3114; docs line 3112): 7,622 10,811 30,780 22,745 5,395 54,133. **Total 131,486.**
4. **Check that the columns are read correctly.** I used Nov 2018 (total 148,981) and Dec 2020 (total 117,770). Total jobs lost come to 31,211. The article says "Out of the 31,000 jobs lost estimated by the STB."
   - Train-and-engine losses are 14,211, which is 45.5% of the total. The article says that group "accounted for 46 percent."
   - Train-and-engine jobs were 63,280/148,981 = 42.5% of jobs in Nov 2018. The article says "less than 43 percent."
5. **Calculation.**
   - Net decline: 145,800 − 131,486 = **14,314**.
   - Decline by group: 505 + 885 + 799 + 4,236 + 174 + 7,715 = 14,314, which matches.
   - Train-and-engine decline: 61,848 − 54,133 = **7,715**.
   - Share: 7,715 / 14,314 = 0.53898, or **53.9%**. This is well away from the rounding edges of 53.85 and 53.95.

minimal_documents: D05 and D04. D05 is needed to find the peak month and D04 for the Class I job data. No other document in the packet has either the Midwest monthly series or the Class I data, so neither can be replaced.

readings:
- **Counting the change during February itself.** If the window starts from the January 2019 level, the January total is 146,556, so the net decline is 15,070. The train-and-engine decline is 62,545 − 54,133 = 8,412, giving **55.8%**. I treat this as the weaker reading, because "from [month] through December" normally means the level in that month to the December level.
- **Using a different employment series.** Dividing by the drop in total rail transportation employment from the D04 Chart 1 survey series (182.5 to 163.4 thousand, a 19.1 thousand drop) would give about 40.4%. This is not defensible: that series is not limited to Class I railroads, and the article says it is "not broken down by the specific type of job."

gaps:
- I read D04 and D05 in full and checked their decisive rows against the docs/ originals.
- I did not read D01, D02, D03, D06 or D07 in full. I only searched them for key terms (Class I, train and engine, railroad, Surface Transportation Board, Midwest, Great Recession, manufacturing employment). D01, D02 and D06 had no hits. The D03 hits were irrelevant ("wage class", one mention of the Great Recession). D07 had only the recession dates in its note 12.
- The sources are web-page text with no PDF page images, so there was nothing to check visually. Each file has a short "[... characters not captured ...]" note at the top, which does not affect the charts I used.
- One small inconsistency inside D05 does not change the answer. The text says employment "bottomed out in February 2010," but Chart 1 shows Dec 2009 (3,528.4) slightly lower than Feb 2010 (3,530.2).

contaminated: no. I received only the workspace root, the packet path and the question, with no answer, hints or prior work. I saw no project instructions or memory, but I cannot verify the invocation mode myself.

(Files used: solver-1 text\D05.txt, text\D04.txt and the two matching docs/ sources. 13 tool uses, about 117 s.)

## i06 - blind screen (packet solver-2)

Question as tested: "In the month in which seasonally adjusted Midwest manufacturing employment reached its lowest level of January 1990 to December 2019, how many people, in thousands, were employed in U.S. rail transportation (seasonally adjusted)?"

Raw return (verbatim):

answer: 178.7 thousand (December 2009)

confidence: high. The data gives December 2009. But D05's own text names February 2010 as the bottom, which would give 178.2 thousand (see readings).

path:
1. **Midwest series:** D05, Chart 1, "Manufacturing employment in the Midwest region of the United States, seasonally adjusted, 1990–2019", in thousands. It has 360 monthly rows (text/D05.txt lines 19–1461). I listed every row below 3,600; all fall between May 2009 and Aug 2010:
   - Jul 2009: 3,530.7
   - Oct 2009: 3,537.3
   - Nov 2009: 3,528.7
   - **Dec 2009: 3,528.4** (line 981)
   - Jan 2010: 3,528.7
   - Feb 2010: 3,530.2
   - Mar 2010: 3,535.5

   All rows before 2009 are above 3,800, and all rows after Mar 2010 are higher. So the lowest month is December 2009, by 0.3 thousand at the printed precision. The source file in docs/ shows the same values.
2. **Cross-check:** adding D05 Chart 5's durable and nondurable series also puts the minimum in December 2009 (2,256.8 + 1,320.6 = 3,577.4). Nov 2009 sums to 3,577.8, Jan 2010 to 3,577.6 and Feb 2010 to 3,579.0.
3. **Rail series:** D04, Chart 1, "Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)". The Dec 2009 row reads 178.7 (text/D04.txt line 1455; docs source line 1455). Neighbouring months: Nov 2009 178.6, Jan 2010 177.9, Feb 2010 178.2. D04 note 1 says the industry covers "transportation of passengers and cargo using railroad rolling stock" and excludes commuter rail and rapid transit.
4. **Conflict in D05's text** (line 1467): "Postrecession manufacturing employment bottomed out in February 2010 at 3.5 million… adding 554,000 jobs through the end of 2019… a 17.1-percent increase since the trough of the recession in February 2010."
   - The chart's own Nov 2009, Dec 2009 and Jan 2010 values are all lower than Feb 2010, so the chart contradicts this.
   - The 554,000 figure fits a Feb 2010 base: 4,083.7 − 3,530.2 = 553.5. A Dec 2009 base gives 4,083.7 − 3,528.4 = 555.3.
   - The 17.1% fits neither month: 553.5/3,530.2 and 555.3/3,528.4 both round to 15.7%.
   - Other month labels in the text also stray from the chart. It calls January 2000 the "employment peak", yet Feb 2000 (5,468.1) is higher than Jan 2000 (5,467.1).

   The question asks for the lowest level over January 1990 to December 2019, which matches the chart's title and range. I therefore used the chart values over the text's statement.

minimal_documents: D05 + D04. There are no alternatives: rail employment data appears only in D04, and Midwest manufacturing data only in D05.

readings:
- **Following D05's text:** if you trust "bottomed out in February 2010" over the chart, the answer is 178.2 thousand. The chart contradicts that statement.
- **Postrecession only:** taking just the months after the June 2009 trough still gives December 2009, so 178.7.

gaps:
- The first 1,408 characters of D05 and 970 characters of D04 are marked "not captured" in both text/ and docs/. They come before the article date line and look like page headers.
- The manifest lists all documents as text extractions with no pages, so there was no PDF or layout file to check.
- I read D04 and D05 in full. D01, D02, D03, D06 and D07 were only searched for "rail", "Midwest" and "bottom/trough/lowest/minimum"; none had relevant data.

contaminated: no

(Files used: solver-2 text\D05.txt, text\D04.txt and the two matching docs/ sources. 13 tool uses, about 128 s.)

## i06 - closed-book probe (fresh closed-book-solver agent, question only, no tools)

Raw return (verbatim):

answer: About 214 thousand. The month is probably January or February 2010.
confidence: low
basis: This comes from memory only, with no tools. National manufacturing employment bottomed around February 2010. For the Midwest, Michigan and Indiana bottomed in mid-2009 as auto production recovered, but Ohio, Illinois, Wisconsin, Minnesota and the other states kept losing jobs until early 2010. So the Midwest low was most likely between December 2009 and February 2010. My recollection is that seasonally adjusted BLS rail transportation employment (series CES4348200001) was near its low then, roughly 213–216 thousand. That is down from about 230 thousand in 2008, before rising to about 228 thousand in 2011. I can't recall the exact Midwest series, its trough month or the exact rail figure for that month.
contaminated: no

Caller note: misses (gold 178.7; 0 tool uses).

## i02 - closed-book probe (fresh closed-book-solver agent, question only, no tools)

Raw return (verbatim):

answer: about 51% (rough estimate; the exact one-decimal figure is unknown)
confidence: low
basis: This is from memory only, with no data lookup. I placed the Midwest manufacturing peak around late 2018 (roughly December 2018), but I don't have the exact month from the series. For Class I railroad employment, I recalled Surface Transportation Board (STB) figures: a total of about 150–151k in late 2018, falling to about 136–137k by December 2019, a drop of about 14k. I estimated that train-and-engine jobs fell from about 62–64k to about 55–57k, a drop of about 7k, so they made up roughly half of the net decline. The exact percentage depends on the precise peak month and the exact monthly STB category counts, which I can't recall.
contaminated: no (only generic environment and account metadata was attached; none of it relates to the question)

Caller note: misses at the asked precision (gold 53.9; "roughly half" is directionally close, so a D05-removal probe would be informative if i02 were promoted).
