# q01 rev 1 - blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

tested_sha256: 4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22
Input given: workspace root, packet path, verbatim question only.

## Raw return (verbatim)

**answer:** +10.4% (Midwest nondurable goods manufacturing employment), −8.6% (U.S. rail transportation employment). Both are measured from March 2010 to December 2019.

**confidence:** high

**path:**
1. **Base month.** The Midwest nondurable series is in D05, Chart 5: "Durable and nondurable goods employment in the Midwest region of the United States, seasonally adjusted, 1990–2019 (in thousands)". Each row lists durable goods first, then nondurable goods (header "Period Durable goods Nondurable goods").
   - I checked all 360 months. Nondurable employment fell from about 1,700 in the 1990s to the 1,300s in 2009, then rose steadily to about 1,456 in 2019.
   - Rows around the bottom: Dec 2009 "2,256.8 1,320.6"; Jan 2010 "2,258.3 1,319.3"; Feb 2010 "2,259.7 1,319.3"; **Mar 2010 "2,265.8 1,318.5"**; Apr 2010 "2,283.1 1,322.1".
   - Every month after March 2010 is at least 1,322.1. So the single lowest month is **March 2010, at 1,318.5 thousand**.
   - December 2019 is "2,674.5 1,456.0", so nondurable employment was 1,456.0 thousand.
   - Cross-check from the D05 text: "Between January 1990 and December 2019, nondurable goods employment in the Midwest fell by 247,300 jobs (–14.5 percent)". January 1990 was 1,703.3, and 1,703.3 − 247.3 = 1,456.0, which matches.
2. **Rail series.** This is in D04, Chart 1: "Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)". The data are national CES figures (note 1).
   - March 2010 is "178.8". December 2019 is "163.4".
   - December 2019 is also 163.4 in Chart 5, and Chart 2 shows the December 2019 monthly change as "-1,500" (164.9 to 163.4), which is consistent.
   - The docs/ source files show the same values (rail lines 1465–1467; D05 lines 2763–2765).
3. **Calculations.**
   - Nondurable: (1,456.0 − 1,318.5) / 1,318.5 = 137.5 / 1,318.5 = 10.43%, so **+10.4%**.
   - Rail: (163.4 − 178.8) / 178.8 = −15.4 / 178.8 = −8.61%, so **−8.6%**.
   - Neither result is close to a rounding boundary.

**minimal_documents:** D05 and D04. Both are needed. No other document has either series (searches for "nondurable" and "rail" matched only D05 and D04 respectively), so there are no substitutes.

**readings:**
- **February 2010 as the base month.** The D05 text says "Postrecession manufacturing employment bottomed out in February 2010 at 3.5 million". That refers to total manufacturing, not nondurable goods. Using it gives nondurable (1,456.0 − 1,319.3) / 1,319.3 = +10.4% and rail (163.4 − 178.2) / 178.2 = **−8.3%**. I rejected this because the question asks for the nondurable low point, and February 2010 (1,319.3) is above March 2010 (1,318.5).
- **June 2009 as the base month.** The D05 text measures the nondurable recovery from there: "recovered 125,000 between June 2009 and December 2019. This 9.3-percent growth rate…". June 2009 was 1,331.0, which is not the lowest month. This would give nondurable +9.4% by calculation (the article prints 9.3) and rail (163.4 − 181.9) / 181.9 = −10.2%. Rejected.
- **December 2009 as the base month.** This is the lowest month in D05's Chart 1 for total manufacturing (3,528.4), which differs from the text's "February 2010". Using it gives nondurable +10.3% and rail (163.4 − 178.7) / 178.7 = −8.6%. Rejected, because it is the wrong series.

**gaps:**
- The first 1,408 characters of D05 and the first 970 characters of D04 are not captured in either text/ or docs/. They appear to be page headers placed before the date and title.
- The packet has no PDF or layout files (method "text"). The charts are given as data rows, so no images needed reading, and the docs/ rows match text/.
- I did not read D01, D02, D03, D06 or D07 in full. Searches for "nondurable", "rail", "railroad", "Midwest", "NAICS 482" and "transportation and warehousing" found nothing in them. "transportation" and "manufacturing" appear only as scattered words in D01, D02 and D06, and not at all in D03 or D07.

**contaminated:** no

Relevant files:
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\solver-2\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\solver-2\text\D04.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\solver-2\docs\mlr_exploring_midwest_manufacturing_employment_from_1990_to_2019.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\solver-2\docs\mlr_employment_in_rail_transportation_heads_downhill_between_nov.txt

Run metadata: 13 tool uses, about 107 s.
