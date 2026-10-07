# q01 rev 0 - shortcut auditor (fresh shortcut-auditor context, packet shortcut)

Date: 2026-10-05. tested_sha256: 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16
Task message: workspace root, packet path shortcut, exact question text only.

Raw return (verbatim):

answer: **47.0%**. In the first half of 2026, South America sold 493 million lb of copper. When FCX raised its Cerro Verde stake in May 2026, its full-year projection for South America was about 1.05 billion lb. 493 / 1,050 = 46.95%, which rounds to 47.0%.

verdict: clear

shortest_path:
1. **When the stake was raised (D04, the 2Q 2026 release filed 2026-07-23).** Line 921: "In May 2026, FCX increased its ownership interest in Cerro Verde from 55.08% to 55.66%." The footnote at line 511 agrees: "prior to May 2026 it was 55.08%." Line 39 says FCX bought 2.0 million Cerro Verde shares on the open market for $107 million in 2Q 2026.
2. **Which projection was current then.** May 2026 falls between the 1Q release (2026-04-23) and the 2Q release (2026-07-23), so the April projection applies. D03 line 227: "Copper sales from South America operations are expected to approximate 1.05 billion pounds for the year 2026." This is D03's only full-year South America sales projection.
3. **First-half 2026 sales (D04).** The six-month table, under the "Sales" 2026 column (lines 467–469, 485), reads "|Total South America|507|539|493||540||". So sales were 493 million lb. As a cross-check, D03's 1Q figure of 248 (line 209) plus D04's 2Q figure of 245 (line 205) also gives 493.
4. **Calculation.** 493 / 1,050 = 0.469524, or 46.952%, which rounds to 47.0%.

sufficient_documents: D03 and D04 are both needed, and neither works alone.
- D04 has the first-half sales and the May timing, but only the July projection ("expected to approximate 1.0 billion pounds", line 221). It never restates the April 1.05 billion figure; searches for "1.05" and "1,050" in D04 found nothing.
- D03 has the 1.05 billion projection but no first-half data and no Cerro Verde purchase. It shows only the 55.08% stake, and searches for "ownership interest", "purchased" and "55.66" turned up no Cerro Verde transaction.
- No alternative set works. D01 and D02 (the BHP reviews) have nothing on Freeport or Cerro Verde. Their only matches were "Cerro Colorado" and Antamina in Peru.

searches:
- Literal terms: "Cerro Verde", "ownership interest", "purchased", "open market", "55.66", "South America", "expected to approximate", "billion pounds", "1.05", "1,050", "April 2026", "January 2026", and "Freeport|FCX|Cerro|Peru|McMoRan" across D01 and D02.
- Sources inspected: the manifest; D03 lines 1–240; D04 lines 1–240, 300–319, 458–513 and 905–944; and the long lines the search tool had cut short, checked by reading them or matching terms only.
- Shortcut attempts: I looked for a statement that hands over the whole answer, such as a percentage or "first-half vs April estimate" comparison, and found none. D04's own references to April estimates are limited to consolidated 2Q sales, gold, molybdenum and costs. There is nothing for South America's full year.

readings/gaps:
- **Alternative (rejected): 49.3%.** This uses D04's July projection: 493 / 1,000 = 49.3%. That projection came out on July 23, after the May stake increase, so it was not the one in force "at the time it raised" the stake. Because D04 alone leads straight to this wrong answer, it acts as a trap rather than a shortcut.
- **Second reading checked: "during 2Q 2026" broadly.** If any purchase had happened before April 23, the January 2026 South America projection would apply, and that projection is not in the packet. D04 explicitly dates the increase to May 2026, so this reading does not hold.
- **Rounding.** 46.952% is above the 46.95 midpoint, so it rounds cleanly to 47.0%.
- **Difficulty risk.** The valid route is simple: find the timing, find the April projection, find the first-half sales, then divide once. It is still genuinely cross-document, so it does not count as a shortcut.
- **Gaps.** I did not read every line of D03 and D04 in full, but targeted searches covered all South America, Cerro Verde and projection references. All packet text came from the source text files, so there were no extraction gaps.
- **Contamination.** None. I did not open question.txt, notes, snapshots or other packets. My inputs were only the workspace root, the packet path and the question.

Files used (as reported): shortcut\text\D03.txt, shortcut\text\D04.txt, shortcut\text\manifest.json
