# q03 rev 0 - blind solver A (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-1 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 40a1754e52b63814906853c94e992a3af44260ee1af1768c123c67b161b1771c

## Return

**answer:** 37.04% (Russia and Belarus, full-year 2024: operating profit of about $80M on net sales of about $216M)

**confidence:** medium-high. No document states this figure directly. I derived it as the difference between two reconciled sets of segment tables, using numbers rounded to the nearest million.

**path:**
1. **What moved where (D11, the Q1 2026 release, text/D11.txt line 85).** "Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." The same note says the rest of Africa/Eurasia and Europe, plus "the skin health business (previously within the North America reportable operating segment)", were combined into a new "Europe, Middle East &amp; Africa" segment.
2. **2024 under the new structure (D10, "Segment Information (Recast)", "Year Ended December 31, 2024", line 59).** "Asia Pacific | 3,074 | 1,144 | 1,061 | (23) | 892". The columns are net sales, cost of sales, SG&amp;A, other, and operating profit. The row is internally consistent: 3,074 − 1,144 − 1,061 + 23 = 892. I confirmed the same row in the raw file docs/cl_ex991_2026-03-17.txt (line 57).
3. **2024 under the old structure.** D05 (Q4 2024 release, Table 5, lines 460 and 477) shows Asia Pacific twelve-month 2024 net sales of 2,858 and operating profit of 812. D09 (Q4 2025 release, lines 463 and 480) prints the same 2024 figures. I confirmed both in the raw docs.
4. **Only the four affected segments changed.** Latin America (4,782 / 1,526), total Oral, Personal and Home Care (15,618 / 4,088) and Corporate (784) are identical in the old and recast tables.
5. **Calculation.**
   - Russia and Belarus net sales = 3,074 − 2,858 = 216
   - Russia and Belarus operating profit = 892 − 812 = 80
   - Margin = 80 / 216 = 0.370370…, which rounds to **37.04%**
6. **Cross-check through the other segments** (same totals, so this is a consistency check rather than independent proof):
   - Skin health = old North America minus recast North America: net sales 4,113 − 3,716 = 397; operating profit 839 − 856 = −17.
   - Old Europe + old Africa/Eurasia + skin health = 2,770 + 1,095 + 397 = 4,262 net sales, and 658 + 253 − 17 = 894 operating profit.
   - Subtracting the new EMEA segment (4,046 / 814) leaves 216 / 80. This matches.
7. **Plausibility check on other periods, using the same method:**
   - 2023: 3,041 − 2,782 = 259 net sales, 878 − 767 = 111 profit, about 42.9%
   - 2025: 3,038 − 2,814 = 224 net sales, 820 − 760 = 60 profit, about 26.8%
   - Q1 2025 (D10 versus D06): 738 − 690 = 48 net sales, 204 − 198 = 6 profit, 12.5%
   
   The margin declines over time, so the 2024 figure is not an outlier. D11's own Q1 2025 comparatives (Asia Pacific 738 / 204, EMEA 1,007 / 222) match D10, which supports D10 as the official recast.

**minimal_documents:** D10 + D11 + D05. D09 can replace D05; both give identical 2024 old-structure figures. D11 cannot be replaced: it is the only document that mentions Russia or Belarus. D12's recast note does not name them, and a search of the raw docs/ found no other mention.

**readings:**
- **Recomputed EMEA profit:** Adding up D10's EMEA 2024 cost lines gives 813 rather than the printed 814 (the table notes it "may not sum due to rounding"). Using 813 in the cross-check route gives 81 / 216 = 37.50%. The direct Asia Pacific route gives 37.04% either way, and I prefer the printed figures.
- **Rounding range:** Each difference could be off by up to $1M, so the true margin lies between roughly 36.4% (79/217) and 37.7% (81/215). Two decimal places is finer than the source data supports, but 37.04% is the result from the printed figures.
- **Whole-segment margins:** Reading the question as asking about the segment that contains Russia and Belarus gives recast Asia Pacific at 892 / 3,074 = 29.02%, or old Africa/Eurasia at 253 / 1,095 = 23.11%. These don't fit "operations in Russia and Belarus", so I rejected them.

**gaps:**
- No document gives Russia and Belarus figures directly. The full recast is "on the Company's website" and not in the packet. The answer assumes the recast changed nothing in Asia Pacific except adding Russia and Belarus, which the D11 note and the unchanged totals support.
- Coverage: I read D10 in full; the segment tables in D05, D09 and D11; the D11 note; and the D06 segment rows. I searched all text/ and docs/ files for Russia, Belarus, recast, skin health and Middle East. I did not read D01–D04, D07, D08 or D12 in full.
- All files are text-only (the manifest says method "text"), so there were no PDF pages or layout files to check.

**contaminated:** no
