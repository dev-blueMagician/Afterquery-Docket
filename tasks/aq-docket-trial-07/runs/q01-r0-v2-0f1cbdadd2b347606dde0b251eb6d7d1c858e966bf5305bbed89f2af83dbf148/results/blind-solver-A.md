# q01 rev 0 - blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

tested_sha256: 0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148
Input given: workspace root, packet path, verbatim question only.

## Raw return (verbatim)

answer: +10.4%, -8.6%

The first figure is Midwest nondurable goods manufacturing employment and the second is U.S. rail transportation employment, both measured from March 2010 to December 2019.

confidence: high

path:
1. **Midwest nondurable series (D05, Chart 5).** The chart is titled "Durable and nondurable goods employment in the Midwest region of the United States, seasonally adjusted, 1990–2019 (in thousands)". Each row lists durable goods first, then nondurable goods.
2. **Finding the lowest month (D05, text lines 2757–2767).** The values around the low are:
   - Jan 2010: "2,258.3 1,319.3"
   - Feb 2010: "2,259.7 1,319.3"
   - **Mar 2010: "2,265.8 1,318.5"**
   - Apr 2010: "1,322.1"

   A regex scan of every row for nondurable values below 1,320 found only these three months. March 2010 is lower than the other two, so it is the only lowest month. All other rows are higher, from Dec 2009 at 1,320.6 back to the 1990s at about 1,700 or more, and forward to Dec 2019. The same figures appear in the docs/ source file.
3. **December 2019 nondurable value (D05, line 3233).** "Dec 2019 … 2,674.5 1,456.0". As a cross-check, the article text says "Between January 1990 and December 2019, nondurable goods employment in the Midwest fell by 247,300 jobs (–14.5 percent)". That matches 1,703.3 − 1,456.0 = 247.3.
4. **Rail series (D04, Chart 1).** The chart is titled "Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)", and note 1 says the CES data are national and seasonally adjusted. The values are:
   - Mar 2010: 178.8 (line 1467)
   - Dec 2019: 163.4 (line 1935)

   D04's Chart 5 shows the same Dec 2019 value, "163.4 1,034.3". Both values match the docs/ source.
5. **Calculations:**
   - Nondurable: (1,456.0 − 1,318.5) / 1,318.5 = 137.5 / 1,318.5 = +10.43%, which rounds to **+10.4%**.
   - Rail: (163.4 − 178.8) / 178.8 = −15.4 / 178.8 = −8.61%, which rounds to **−8.6%**.

   Neither result is close to a rounding boundary.

minimal_documents: D05 and D04 are both required. D05 supplies the low month and the nondurable values; D04 Chart 1 is the only source for rail employment in March 2010, since Chart 5 starts in January 2018. No other document can stand in for either: D01, D02, D03, D06 and D07 have no matches for "nondurable", "non-durable" or "rail".

readings:
- **Using the recession trough the article discusses (June 2009) instead of the actual series low.** D05 says manufacturers "recovered 125,000 between June 2009 and December 2019. This 9.3-percent growth rate…". The nondurable change from that month is 125.0 / 1,331.0 = +9.4% (the article prints 9.3%). The rail change is (163.4 − 181.9) / 181.9 = −10.2%. This does not answer the question as worded, because June 2009 is not the lowest level.
- **Using total Midwest manufacturing (Chart 1) by mistake.** Its chart low is Dec 2009 at 3,528.4, while the text says it "bottomed out in February 2010". The rail change would be −8.6% from Dec 2009 or −8.3% from Feb 2010. This reading is wrong because the question asks about nondurable goods.

gaps:
- I read D04 and D05 in full. D01, D02, D03, D06 and D07 I only searched by keyword; the only hits were incidental mentions of "manufacturing" in D01 and D06.
- Both documents are text extractions with no PDF pages to check. The short header portions marked "not captured" and the missing formula in D05 note 8 don't affect the answer.
- Chart 5's durable and nondurable values don't add up to Chart 1's totals; for example, in Jan 1990 they sum to 5,266.0 against 5,184.3. That doesn't affect this question.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\solver-1\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\solver-1\text\D04.txt
- The matching docs/ sources: mlr_exploring_midwest_manufacturing_employment_from_1990_to_2019.txt and mlr_employment_in_rail_transportation_heads_downhill_between_nov.txt

Run metadata: 12 tool uses, about 102 s.
