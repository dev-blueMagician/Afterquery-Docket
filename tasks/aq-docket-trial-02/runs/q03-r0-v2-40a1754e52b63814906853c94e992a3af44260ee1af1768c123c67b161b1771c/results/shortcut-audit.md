# q03 rev 0 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 40a1754e52b63814906853c94e992a3af44260ee1af1768c123c67b161b1771c

## Return

answer: **37.04%.** In 2024, Russia and Belarus had net sales of $216M and operating profit of $80M, and 80 / 216 = 37.04%.

verdict: **clear.** No document states this number directly, and no single document is enough. You need the recast segment table, an old-structure 2024 table, and the realignment note. The arithmetic is a simple difference and ratio, so there is some risk the question is too easy, but it is not a shortcut.

shortest_path:
1. **D11** (`docs/cl_ex991_2026-05-01.txt`, text line 85) explains the move: "Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." Skin health moved from North America into the new Europe, Middle East &amp; Africa segment. Nothing else moved into or out of Asia Pacific.
2. **D10** (`docs/cl_ex991_2026-03-17.txt`, "Segment Information (Recast)", year ended Dec 31, 2024) shows the new Asia Pacific, which includes Russia and Belarus: "Asia Pacific | 3,074 | 1,144 | 1,061 | (23) | 892". That is net sales $3,074M and operating profit $892M.
3. **D05** (`docs/cl_ex991_2025-01-31.txt`, Segment Information) shows the old Asia Pacific for FY2024: net sales "2,858" and operating profit "812". **D09** (`docs/cl_ex991_2026-01-30.txt`) repeats the same 2024 figures, 2,858 and 812.
4. Russia and Belarus = recast minus old: net sales 3,074 − 2,858 = **216**; operating profit 892 − 812 = **80**. Margin = 80/216 = 0.370370, or **37.04%**.

Cross-check by a second route, using the other segments (old structure: North America, Europe, Africa/Eurasia; new: Europe, Middle East &amp; Africa):
- Skin health = old North America minus recast North America: 4,113 − 3,716 = 397 net sales; 839 − 856 = −17 operating profit.
- Russia and Belarus = old Europe + old Africa/Eurasia + skin health − recast EMEA.
  - Net sales: 2,770 + 1,095 + 397 − 4,046 = 216.
  - Operating profit: 658 + 253 − 17 − 814 = 80.
- Both routes give the same result. Oral/Personal/Home Care totals (15,618 / 4,088) and Corporate (−784) are the same before and after the recast, so the recast only moved amounts between segments.

sufficient_documents:
- Minimal set: **D10 + D11 + D05**, with **D09** able to replace D05.
- D11 is needed to tie the Asia Pacific change to Russia and Belarus. D12's recast notes are generic and don't name them.
- D10 alone gives only recast figures; D05 and D09 give only old-structure figures.

searches:
- Search terms: "Russia|Belarus" across both text/ and docs/. The only hit is the D11 note, with no Russia or Belarus amounts or margins anywhere.
- Also searched: "Ukrain|CIS|sanction|hyperinflation|exit" (only private-label pet food hits); "margin|% to Net Sales" in D10 (none); "2024|Eurasia|recast" in D11 and D12 (no 2024 data, only generic recast notes); and Asia Pacific rows in D05, D09, D10 and D11.
- Read the manifest, D10 in full, D11 lines 1–120, the D05 and D09 segment tables, the D09 operating-profit-by-division table, and the D01 header (an unrelated 2019 stock award agreement).
- Checked the key figures against the original docs/ files: 3,074 and 892 in the 2026-03-17 file; 2,858 and 812 in the 2025-01-31 and 2026-01-30 files; and the D11 note wording.
- Did not read D02–D04, D06–D08 or D12 in full. Their segment rows weren't needed because D05 and D09 agree.

readings/gaps:
- Other years, if someone misreads the period:
  - 2025: (820 − 760) / (3,038 − 2,814) = 60/224 = 26.79%
  - 2023: (878 − 767) / (3,041 − 2,782) = 111/259 = 42.86%
- Rounding: all segment figures are rounded to $1M, so the underlying margin could fall anywhere from about 36.4% to 37.7%. 37.04% is the exact result from the reported figures.
- No extraction problems were found in the inputs used.
- Contamination: none. The packet root holds a `question.txt`, which I did not open, and I read no notes, snapshots or other packets.
