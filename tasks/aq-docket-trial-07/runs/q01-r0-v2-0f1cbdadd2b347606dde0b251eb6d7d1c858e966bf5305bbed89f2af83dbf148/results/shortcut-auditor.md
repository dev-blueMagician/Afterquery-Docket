# q01 rev 0 - shortcut auditor (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: 0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148
Input given: workspace root, packet path, verbatim question only.

## Raw return (verbatim)

answer: **+10.4%, −8.6%**. Midwest nondurable goods manufacturing employment hit its low in March 2010, at 1,318.5 thousand. From that month to December 2019, Midwest nondurable employment rose 10.4% and U.S. rail transportation employment fell 8.6%.

verdict: clear

shortest_path:
1. In D05, Chart 5 ("Durable and nondurable goods employment in the Midwest region…, seasonally adjusted, 1990–2019 (in thousands)") has all 360 monthly rows. A grep for every value below 1,325.0 returns only Oct 2009 to Jun 2010:
   - Dec 2009: 1,320.6
   - Jan 2010: 1,319.3
   - Feb 2010: 1,319.3
   - **Mar 2010: 1,318.5** (the single lowest value; `text\D05.txt` line 2767)
   - Apr 2010: 1,322.1
   - Dec 2019: **1,456.0** (line 3235)
2. Join on the month in D04, Chart 1 ("Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)"):
   - **Mar 2010: 178.8** (`text\D04.txt` line 1469)
   - **Dec 2019: 163.4** (line 1937; Chart 5 repeats 163.4)
3. Arithmetic:
   - Nondurable: (1,456.0 − 1,318.5) / 1,318.5 = 137.5 / 1,318.5 = +10.43%, so **+10.4%**
   - Rail: (163.4 − 178.8) / 178.8 = −15.4 / 178.8 = −8.61%, so **−8.6%**
   - Neither result is near a rounding boundary.

sufficient_documents: D05 and D04 together, and both are needed. D05 has no rail data, and D04 has no Midwest data. The rail half depends on the month found in D05. D04 Chart 5 starts in Jan 2018, so only D04 Chart 1 has the March 2010 rail figure. The docs/ originals of both articles give the same values.

searches:
- Terms searched across text/ and docs/: rail, nondurable/non-durable, Midwest, manufactur, "transportation and warehousing", 482, bottom/trough/lowest/low point, Mar 2010/March 2010, and the answer strings 10.4 and 8.6.
- Read in full: the manifest, D04 and D05.
- D01, D02, D03, D06 and D07 (Indian country, Consumer Expenditure Survey quality, business employment dynamics by wage class, projections/O*NET, European work schedules) were checked by keyword only. Their hits were unrelated mentions or coincidental numbers such as "48.6" and "110.4".
- No passage states the nondurable low month or either percentage change from March 2010, so there is no whole-answer lookup and no single-document answer.
- Difficulty risk: this is a simple, valid cross-document route (scan for a minimum, join on the month, two percentage changes). That is a difficulty concern, not a shortcut.

readings/gaps:
- **Distractor 1:** D05 line 1467 says "Postrecession manufacturing employment bottomed out in February 2010 at 3.5 million." That refers to total manufacturing, not nondurable goods. Starting from Feb 2010 gives nondurable +10.4% (136.7/1,319.3) but rail **−8.3%** (−14.8/178.2), so the rail figure would be wrong. The statement also conflicts with D05's own Chart 1, where total manufacturing is lowest in Dec 2009 (3,528.4), not Feb 2010 (3,530.2).
- **Distractor 2:** D05 also cites the "trough of June 2009" and a nondurable recovery of 125,000 / "9.3-percent" from Jun 2009 to Dec 2019. Starting from Jun 2009 gives +9.4% (125.0/1,331.0) and −10.2% (−18.5/181.9). The question asks for the lowest level, not the business-cycle trough.
- Jan and Feb 2010 tie at 1,319.3, but neither is the minimum, so the month is unambiguous.
- **Extraction gaps:**
  - Uncaptured header text: 1,408 characters in D05 and 970 in D04, plus 34-character endings in both. These gaps are in the docs/ originals too and look like site boilerplate. They remain unresolved.
  - D05 footnote 8's location-quotient formula is missing, which doesn't affect this question.
  - D01, D02, D03, D06 and D07 were not fully read.
- **Contamination:** none. No project instructions, memory, answer key or prior solve outputs appeared in context. The packet root contains a `question.txt`, which I saw only in the file listing and did not open.

Files used:
- `D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\shortcut\text\D05.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\shortcut\text\D04.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\shortcut\docs\mlr_exploring_midwest_manufacturing_employment_from_1990_to_2019.txt`
- `D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r0-v2-0f1cbdadd2b347606dde0b251eb6d7d1c858e966bf5305bbed89f2af83dbf148\shortcut\docs\mlr_employment_in_rail_transportation_heads_downhill_between_nov.txt`

Run metadata: 17 tool uses, about 138 s.
