# q01 rev 0 - local removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a packet that is a byte copy of the prepared q01 corpus
minus one necessary document (its text/Dnn.txt, its docs/ original and its manifest entry), with a
neutral folder name, bound to the read guard as its own run. Input: workspace root, packet path, the
verbatim q01 question, and an instruction to answer if the packet settles it, otherwise commit to one
forced guess with a probability. This approximates the platform's document check (high model, each
marked document left out); it is not that check.

## Probe m9: packet without D05 (Midwest manufacturing article, platform Doc 4)

Raw return (verbatim):

I could not answer this from the packet: it has no Midwest nondurable goods manufacturing series. D04 settles the rail figure once the starting month is known. The answer below is a forced guess.

answer: Not answerable from the packet. Forced best guess: **+6.0%, −8.2%** (Midwest nondurable goods manufacturing first, then U.S. rail transportation). This assumes the Midwest low point was January 2010.

confidence: low. I put the chance that this guess is exactly right at one decimal place at about 1% or less.

path:
1. **Rail series.** D04 (`D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-probe-m9\solver-1\text\D04.txt`) has this chart at line 15: "Chart 1. Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)". Note 1 adds: "The CES data used in this article are seasonally adjusted unless otherwise noted."
   - December 2019 is **163.4** (lines 1935–1937). Chart 5 repeats the same value (lines 3272–3274).
   - December 2019 is the lowest rail value from 1980 to 2019, so the rail change from any earlier month is negative.
2. **Midwest series is missing.** I searched every text/ file for "nondurable", "non-durable", "Midwest", "manufactur", "region", "goods" and "durable". I also searched for Midwest state names, nondurable industries (food, paper, chemicals, plastics, printing, petroleum, textile, apparel) and "1990" / "seasonally adjusted". I repeated the key terms on docs/.
   - "Midwest" appears only in D04's coal note: "March and April 2019 data probably reflect the impacts of historic flooding in the Midwest."
   - The other documents cover unrelated topics: D01 Indian Country, D02 Consumer Expenditure survey quality, D03 national job gains and losses by wage class, D06 employment projections and O*NET, D07 European work schedules.
   - The manifest has no D05. Going by the alphabetical file order, D05 would fall between the rail article and "mapping" (for example, a title starting "manufacturing…"). It is probably the missing source.
3. **Guess for the low month (general knowledge, not from the packet).** I expect Midwest nondurable employment bottomed soon after the 2008–09 recession, around late 2009 to early 2010. By then the auto-linked plastics and rubber rebound would offset falling printing and paper jobs, while food manufacturing kept growing. I picked **January 2010**.
4. **Guess for the Midwest change (general knowledge).** My rough industry-by-industry estimate from 2010 to 2019:
   - food about +15%, beverages and plastics/rubber up, chemicals about +5%
   - printing about −18%, paper about −9%
   - This gives about 1.24 million rising to 1.31 million, roughly **+6.0%**.
5. **Rail from January 2010.** January 2010 is 177.9 (lines 1459–1461). (163.4 − 177.9) / 177.9 = −8.15%, which rounds to **−8.2%**.

minimal_documents: D04 is needed for the rail figure but is not enough on its own. No packet document supplies the Midwest series, and I found no substitute.

readings: The rail figure depends only on which month is the Midwest low. These values come straight from D04, always ending at December 2019 = 163.4:

| Low month | Rail level | Rail change |
|---|---|---|
| Jun 2009 | 181.9 | −10.2% |
| Jul 2009 | 182.0 | −10.2% |
| Aug 2009 | 181.8 | −10.1% |
| Sep 2009 | 181.0 | −9.7% |
| Oct 2009 | 179.6 | −9.0% |
| Nov 2009 | 178.6 | −8.5% |
| Dec 2009 | 178.7 | −8.6% |
| Jan 2010 | 177.9 | −8.2% |
| Feb 2010 | 178.2 | −8.3% |
| Mar 2010 | 178.8 | −8.6% |
| Apr 2010 | 179.4 | −8.9% |
| May 2010 | 180.5 | −9.5% |
| Jun 2010 | 182.3 | −10.4% |
| Jul 2010 | 184.1 | −11.2% |
| Aug 2010 | 184.6 | −11.5% |
| Sep 2010 | 186.0 | −12.2% |
| Oct 2010 | 187.1 | −12.7% |
| Nov 2010 | 188.4 | −13.3% |
| Dec 2010 | 188.6 | −13.4% |

- If the low was during 2011 (188.6–194.9), rail is about −13.4% to −16.2%.
- If the low was in late 2017 or early 2018 (about 179.3), rail is about −8.9%.
- The Midwest percentage itself cannot be worked out from the packet. My plausible range is about +3% to +10%.

gaps:
- **Missing facts:** the Midwest series' low month, its level that month, and its December 2019 level. The source looks like it was dropped during preparation (no D05), so the caller should check the preparation step.
- **Unread material:** I read D04 in full. For D03 I read the first 30 lines and searched the rest. D01, D02, D06 and D07 were only keyword-searched, not read in full.
- **Format:** the packet holds only .txt files, so there were no PDF pages to inspect.

contaminated: no

Caller note: forced guess +6.0%, -8.2% misses the gold (+10.4%, -8.6%); the nondurable half is not
recoverable without D05. D05 needed in practice. Residual: a guessed Dec 2009 or Mar 2010 start would
land the rail half on -8.6, but the nondurable half (+10.4) still needs D05's levels. 16 tool uses, about 280 s.

## Probe k4: packet without D04 (rail article, platform Doc 5)

Raw return (verbatim):

**answer:** The packet only settles the first figure, the Midwest nondurable change of **+10.4%**. None of the documents has U.S. rail transportation employment data, so the second figure is a forced guess: **+10.4%, −5.5%**.

**confidence:** high for +10.4%; low for the rail figure. I put the chance that the full pair is exactly right at about 1.5% (about 97% for +10.4%, about 1.5% for −5.5%).

**path:**
1. D05 (`text\D05.txt`, which matches `docs\mlr_exploring_midwest_manufacturing_employment_from_1990_to_2019.txt`) has "Chart 5. Durable and nondurable goods employment in the Midwest region of the United States, seasonally adjusted, 1990–2019 (in thousands)". The second column is nondurable goods.
2. Lowest nondurable value:
   - The values just before and after the low are Dec 2009 "1,320.6", Jan 2010 "1,319.3" and Feb 2010 "1,319.3". The lowest is **Mar 2010 "2,265.8 1,318.5"** (text line 2767), and values rise from Apr 2010 (1,322.1).
   - Searches confirmed that only Jan, Feb and Mar 2010 fall in the 1,300.0–1,319.9 range, and no value is below 1,300. Every month from 1990 to 2008 is at least 1,405.7. So March 2010 is the single lowest month.
3. Dec 2019: "2,674.5 1,456.0".
4. Calculation: (1,456.0 − 1,318.5) / 1,318.5 = 137.5 / 1,318.5 = 10.43%, which gives **+10.4%**.
5. The chart matches the article's own figures:
   - "fell by 247,300 jobs (–14.5 percent)": 1,703.3 − 1,456.0 = 247.3, and 247.3 / 1,703.3 = 14.52%.
   - "lost 134,700 jobs between December 2007 and June 2009": 1,465.7 − 1,331.0 = 134.7.
6. Rail: no document has a rail series, so nothing in the packet gives March 2010 or December 2019 values.
   - "rail" (case-insensitive) has zero matches in `text\` and `docs\`.
   - Matches for transportation, freight, train and NAICS 482 are all unrelated: occupation names in D06, consumer spending categories in D02, and the "Trade, transportation, and utilities" supersector in D01.
   - The manifest has no D04.
7. How I made the rail guess, from memory and unverified:
   - Class I railroad jobs (STB/AAR figures) fell roughly 9–10% from early 2010 (about 148–150 thousand) to December 2019 (about 135–137 thousand), as railroads cut staff in 2019.
   - The BLS rail series (CES NAICS 482) is larger, at about 200–220 thousand. It also counts Amtrak and short-line railroads, which changed less, so the overall drop would be smaller.
   - That points to roughly −4% to −7%. I picked the middle, −5.5%.

**minimal_documents:** D05 is enough for +10.4%. No document in the packet covers the rail figure, and none of the others could replace it.

**readings:**
- The article says total manufacturing "bottomed out in February 2010". Measuring nondurables from Feb 2010 gives 136.7 / 1,319.3 = 10.36%, still **+10.4%**, so the first figure holds either way.
- Measuring from the official recession end (June 2009) gives 125.0 / 1,331.0 = 9.39%. The article prints "9.3-percent", which suggests it truncates rather than rounds. But June 2009 isn't the lowest month, so this reading doesn't fit the question. 10.43 gives 10.4 whether rounded or truncated.
- I can't offer any other answer for rail.

**gaps:**
- The packet has no rail transportation employment data, either seasonally adjusted or not, and the D04 slot is missing. The rail number is general-knowledge guesswork.
- Coverage: I read D05 in full. For D01, D02, D03, D06 and D07 I only read the titles and searched them for rail and transportation terms (plus "seasonally adjusted", nondurable and Midwest); I didn't read them in full.
- All documents are text extractions with no PDF pages to check. The chart rows I used came through intact in both `text\` and `docs\`.

**contaminated:** no

Caller note: forced rail guess -5.5% misses the gold -8.6% (the model's remembered CES rail levels,
about 200-220 thousand, differ from the article's chart, 178.8 and 163.4). D04 needed in practice.
19 tool uses, about 287 s.

## Summary

Both necessary documents changed the answer when left out (D05 out: +6.0%, -8.2%; D04 out: +10.4%,
-5.5%). Local probes, not the platform's document check.
