# q01 rev 1 - blind solver A (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-1 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7

## Return

**answer:** +69. Net sales of the moved operations rose by $69 million, from $879 million in FY2024 to $948 million in FY2025.

**confidence:** high

**path:**
1. **What moved (D11, line 85, footnote (1)):** "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So the operations moved are Africa/Eurasia excluding Russia and Belarus. Nothing in the packet reports their sales directly, so I worked them out from the two segment bases.
2. **Old-basis full-year net sales (D09, lines 452–467, Twelve Months Ended Dec 31, 2025 / 2024):**
   - North America: 4,045 / 4,113
   - Latin America: 4,776 / 4,782
   - Europe: 2,962 / 2,770
   - Asia Pacific: 2,814 / 2,858
   - Africa/Eurasia: 1,172 / 1,095
   - Total Oral, Personal and Home Care: 15,769 / 15,618
   
   D05 (lines 457–462) prints the same 2024 values (4,113, 2,770, 2,858, 1,095).
3. **Recast full-year net sales (D10, "Segment Information (Recast)", lines 25–30 and 56–61), 2025 / 2024:**
   - North America: 3,679 / 3,716
   - Latin America: 4,776 / 4,782
   - Europe, Middle East &amp; Africa: 4,276 / 4,046
   - Asia Pacific: 3,038 / 3,074
   - Totals: 15,769 / 15,618, the same as the old basis.
4. **Method B (Africa/Eurasia minus Russia and Belarus).** Russia and Belarus equal recast Asia Pacific minus old Asia Pacific.
   - 2025: 3,038 − 2,814 = 224, so 1,172 − 224 = **948**
   - 2024: 3,074 − 2,858 = 216, so 1,095 − 216 = **879**
5. **Method A, a cross-check (EMEA minus Europe minus skin health).** Skin health equals old North America minus recast North America.
   - 2025: 4,045 − 3,679 = 366, so 4,276 − 2,962 − 366 = **948**
   - 2024: 4,113 − 3,716 = 397, so 4,046 − 2,770 − 397 = **879**
6. **Change:** 948 − 879 = **+69** ($ millions). Both methods agree because Latin America is unchanged and the segment totals match exactly on both bases.

**minimal_documents:** D09, D10 and D11.
- D10 is the only document with full-year recast figures.
- D11 is the only document that says which operations moved. D12's footnote only says the data was recast, without the breakdown.
- D09 is the only source of old-basis 2025 full-year figures. D05 can replace it for the 2024 values only.

**readings:**
- Treating all of Africa/Eurasia as moved, ignoring the Russia/Belarus exclusion: 1,172 − 1,095 = +77. D11's explicit carve-out contradicts this.
- Taking EMEA minus old Europe without removing skin health: 1,314 − 1,276 = +38. This wrongly includes the skin health business moved from North America.
- I consider +69 the only reading that matches the question's wording.

**gaps:**
- All inputs are rounded to whole millions, so the derived 948 and 879 (and the +69) could each be off by about ±1–2 from unrounded values. The packet has no unrounded figures.
- The method assumes Asia Pacific's only recast change was adding Russia and Belarus, and North America's was only losing skin health. That is how D11 describes it, and the matching totals are consistent with it.
- The full-year 2024 figures in D05 and D09 already reflect the earlier July 1, 2024 recast that moved skin health from Europe to North America (D05 line 113; D06 line 85), so they are on the same basis as the 2025 figures.
- Coverage:
  - Read in full: D10.
  - Read in part: D11 (lines 1–140 plus search hits), D09 (lines 1–120 and 444–493), D05 (search hits).
  - Search hits only: D02–D04, D06–D08 and D12.
  - Not opened: D01 (2019).
  
  All documents are text; there were no PDFs or page images, and the D10 tables add up to their printed totals.

**contaminated:** no

Files used: D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\solver-1\text\D09.txt, D10.txt, D11.txt and D05.txt (same directory).
