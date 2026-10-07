# q01 rev 1 - shortcut auditor (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: 4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22
Input given: workspace root, packet path, verbatim question only.

## Raw return (verbatim)

answer: **+10.4% (Midwest nondurable goods manufacturing), −8.6% (U.S. rail transportation)**, both measured from March 2010 to December 2019.

verdict: clear

shortest_path:
1. In D05, Chart 5 ("Durable and nondurable goods employment in the Midwest region… seasonally adjusted, 1990–2019 (in thousands)"), the lowest nondurable value is **Mar 2010 = 1,318.5**. It is the only month at that level: Dec 2009 is 1,320.6, Jan 2010 and Feb 2010 are both 1,319.3, and Apr 2010 is 1,322.1. Every value before mid-2009 is above 1,331, and every value from April 2010 on is at least 1,322.1. **Dec 2019 = 1,456.0** (text/D05.txt line 3235). The article's own text backs up that December value: "fell by 247,300 jobs (–14.5 percent)", and 1,703.3 − 1,456.0 = 247.3.
2. The nondurable change is (1,456.0 − 1,318.5) / 1,318.5 = 137.5 / 1,318.5 = **+10.43%, so +10.4%**.
3. In D04, Chart 1 ("Employment in rail transportation, January 1980–December 2020, seasonally adjusted (in thousands)"), **Mar 2010 = 178.8** (text/D04.txt line 1469) and **Dec 2019 = 163.4** (line 1937). Chart 5 of the same document repeats 163.4 for December 2019.
4. The rail change is (163.4 − 178.8) / 178.8 = −15.4 / 178.8 = **−8.61%, so −8.6%**.

Neither result is close to a rounding boundary.

sufficient_documents: D05 and D04 together; no single document is enough. D05 gives the month and the nondurable change, but has no rail data. D04 gives the rail series, but nothing in it points to March 2010. The two are linked only by the month, followed by ordinary percentage arithmetic. That is an allowed cross-document join. It is a difficulty risk, because the route is simple (find one minimum, look up one month, compute two percentages), but it is not a shortcut. There are no alternative document sets: only D04 and D05 mention rail or nondurable.

searches:
- Search terms: nondurable, rail, Midwest, manufactur, "transportation employment", "Mar(ch) 2010", lowest, trough, bottom(ed) out, "Dec 2019", and "percent increase/change since".
- What I inspected: the manifest, all of docs/ D04 and D05, and the matching text/ copies. The text/ copies have identical values with a 2-line header offset.
- The other documents: D01 (Indian country), D02 (Consumer Expenditure Surveys), D03 (business employment dynamics by wage class), D06 (employment projections and O*NET) and D07 (European work schedules) only touch "manufacturing" in passing or have unrelated "lowest/Dec 2019" hits. None has competing data.
- No passage states the answer or the March 2010 minimum, and the question's wording doesn't reveal the month.

readings/gaps:
- **Wrong month taken from D05's narrative about total manufacturing.** The text says "Postrecession manufacturing employment bottomed out in February 2010… a 17.1-percent increase since the trough of the recession in February 2010." Using February 2010 gives +10.4% and −8.3% (178.2 base). This applies to total manufacturing, not nondurables. It also conflicts with D05's own Chart 1, where the total-manufacturing low is Dec 2009 at 3,528.4.
- **Recession trough of June 2009.** The text says nondurables "recovered 125,000 between June 2009 and December 2019. This 9.3-percent growth rate…" Using June 2009 gives +9.4% (the text says 9.3%) and −10.2% (181.9 base). This is wrong because June 2009 is not the nondurable minimum.
- **Other months.** Dec 2009 gives +10.3% and −8.6%. Jan 2010 gives +10.4% and −8.2%. Both are wrong under the question's wording.
- **Source inconsistency (not load-bearing).** In D05, Chart 1's total does not equal durable plus nondurable (for January 1990, 5,184.3 vs. 5,266.0), and the narrative's 17.1% does not match its own chart (about 15.7%). Neither affects this answer.
- **Extraction gaps.** About 1,408 characters at the start of D05 and about 970 at the start of D04 were not captured. They appear to be page headers, sit before the article text, and are unresolved but unlikely to matter.

Files:
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\shortcut\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\shortcut\text\D04.txt
- D:\Dev\Docket\tasks\aq-docket-trial-07\runs\q01-r1-v2-4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22\shortcut\text\manifest.json

No contamination: only the question, the packet path and the packet's docs/ and text/ files were used.

Run metadata: 16 tool uses, about 108 s.
