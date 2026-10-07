# q01 rev 1 - blind solver B (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-2 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7

## Return

answer: +69 million dollars. Net sales of the moved operations rose from $879 million in 2024 to $948 million in 2025.

confidence: high

path:
1. **What moved (D11 line 85):** "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So the operations in question are Africa/Eurasia minus Russia and Belarus. Latin America is not affected.
2. **Old-structure full-year net sales (D09 Table 5, lines 460–465, "Twelve Months Ended December 31, 2025 2024", $ millions):**
   - North America: 4,045 (2025), 4,113 (2024)
   - Latin America: 4,776, 4,782
   - Europe: 2,962, 2,770
   - Asia Pacific: 2,814, 2,858
   - Africa/Eurasia: "1,172 | 1,095"
   - Total Oral, Personal and Home Care: 15,769, 15,618
   - D05 lines 457–462 show the same 2024 figures.
3. **Recast full-year net sales (D10, "Segment Information (Recast)"):**
   - 2025 (lines 25–28): North America 3,679; Latin America 4,776; Europe, Middle East &amp; Africa 4,276; Asia Pacific 3,038; total 15,769
   - 2024 (lines 56–59): North America 3,716; Latin America 4,782; Europe, Middle East &amp; Africa 4,046; Asia Pacific 3,074; total 15,618
   - D10's Q1 2025 recast (904 / 1,143 / 1,007 / 738) matches D11 Table 4, which confirms D10 uses the structure D11 describes.
4. **Russia and Belarus** = recast Asia Pacific minus old Asia Pacific: 2025 = 3,038 − 2,814 = 224; 2024 = 3,074 − 2,858 = 216.
5. **Moved operations** = old Africa/Eurasia minus Russia and Belarus: 2025 = 1,172 − 224 = 948; 2024 = 1,095 − 216 = 879.
6. **Cross-check through the new segment.** Skin health = old North America minus recast North America: 366 in 2025 (4,045 − 3,679) and 397 in 2024 (4,113 − 3,716). Then the new segment minus old Europe minus skin health gives 4,276 − 2,962 − 366 = 948 for 2025 and 4,046 − 2,770 − 397 = 879 for 2024. Both match step 5.
7. **Totals check.** The old and recast segment totals are equal in both years: 15,769 for 2025 and 15,618 for 2024.
8. **Change:** 948 − 879 = **+69**.

minimal_documents: D09, D10, D11.
- D09 is the only source of old-structure full-year 2025 figures.
- D10 is the only source of the recast figures.
- D11 is the only document that says Russia and Belarus were excluded and skin health was added. D12's footnote (line 83) gives no breakdown, and D10 has no explanatory text.
- D05 can replace D09 for 2024 only, not for 2025.

readings:
- **Whole Africa/Eurasia segment treated as moved** (ignoring the Russia/Belarus exclusion): 1,172 − 1,095 = **+77**. D11 explicitly excludes Russia and Belarus, so this reading is weaker.
- **Change in the whole new segment:** 4,276 − 4,046 = **+230**. This is a different quantity, because it includes Europe and skin health.
- **New segment minus old Europe, without removing skin health:** 1,314 − 1,276 = **+38**. This is wrong because skin health came from North America, not Africa/Eurasia.

gaps:
- No document reports net sales for "Africa/Eurasia excluding Russia and Belarus" directly, so the figures are derived from rounded segment numbers. The true change could differ from 69 by about ±1–2. Both derivation paths give exactly 948 and 879 because the 2024 and 2025 totals reconcile exactly. For 2023 the recast table is off by 1 from its stated total, but that year isn't needed.
- **Not read in full:** D01 (a 2019 stock award agreement; my searches found no segment content), D02–D04, D06–D08 and D12. I searched all of text/ for the segment names, "Russia", "Belarus", "skin health" and recast/segment terms. I did not read docs/ separately; the manifest marks every document as plain text with no PDF pages, so there are no layout files or page images.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\solver-2\text\D09.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\solver-2\text\D10.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\solver-2\text\D11.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\solver-2\text\D05.txt (corroborates 2024)
