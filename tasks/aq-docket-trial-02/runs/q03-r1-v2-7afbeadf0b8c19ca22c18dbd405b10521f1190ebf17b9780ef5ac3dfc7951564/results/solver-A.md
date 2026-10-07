# q03 rev 1 - blind solver A (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-1 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 7afbeadf0b8c19ca22c18dbd405b10521f1190ebf17b9780ef5ac3dfc7951564

## Return

**answer:** 19.68%. In 2024 the Africa/Eurasia operations moved into EMEA (the old segment minus Russia and Belarus) had about $173M of operating profit on $879M of net sales.

**confidence:** high

**path:**
1. **What moved (D11, 1Q26 release, line 85):** "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So the operations in question are Africa/Eurasia without Russia and Belarus.
2. **2024 under the old structure (D05, Q4 2024 release, lines 457–478, twelve months 2024, $M):**
   - North America: net sales 4,113, operating profit 839
   - Latin America: 4,782 / 1,526
   - Europe: 2,770 / 658
   - Asia Pacific: 2,858 / 812
   - Africa/Eurasia: "1,095" / "253"
   - Total Oral, Personal and Home Care: 15,618 / 4,088
   
   D09 (Q4 2025 release, lines 460–481) prints the same 2024 figures.
3. **2024 under the new structure (D10, "Segment Information (Recast)", lines 56–59, $M):**
   - North America: 3,716 / 856
   - Latin America: 4,782 / 1,526
   - Europe, Middle East &amp; Africa: "4,046" / "814"
   - Asia Pacific: 3,074 / 892
   
   These rows match the original source docs\cl_ex991_2026-03-17.txt, lines 54–57. Both structures add up to the same totals (15,618 / 4,088), and Latin America is unchanged.
4. **Calculation, route A (old Africa/Eurasia minus Russia and Belarus):**
   - Russia and Belarus = new Asia Pacific minus old Asia Pacific: 3,074 − 2,858 = 216 net sales; 892 − 812 = 80 operating profit.
   - Operations moved to EMEA: 1,095 − 216 = 879 net sales; 253 − 80 = 173 operating profit.
5. **Calculation, route B (check through EMEA):**
   - Skin health = old North America minus new North America: 4,113 − 3,716 = 397 net sales; 839 − 856 = −17 operating profit.
   - Operations moved to EMEA = EMEA − Europe − skin health: 4,046 − 2,770 − 397 = 879; 814 − 658 + 17 = 173. This matches route A.
6. **Margin:** 173 / 879 = 0.196815, which rounds to **19.68%**.
7. **Same method on other years:** it reproduces the recast EMEA within normal rounding. For 2025 (D09 vs D10): 2,962 + 1,172 − 224 + 366 = 4,276, as printed; operating profit comes to 937 against 938 printed. For 2023: 3,821 against 3,822, and 753 against 754.

**minimal_documents:** D11 + D10 + D05. D09 can replace D05, since it has the same old-structure 2024 figures. Only D11 says that Russia and Belarus were excluded; no other document can replace it, and D12's note gives no detail.

**readings:**
- If you take the whole old Africa/Eurasia segment, including Russia and Belarus: 253 / 1,095 = **23.11%**. The question asks about the operations that moved into EMEA, and D11 says Russia and Belarus did not move there, so this reading is weaker.
- Subtracting Europe from EMEA without removing skin health gives 156 / 1,276 = 12.23%. That conflicts with D11's explicit statement that skin health was combined into EMEA, so it isn't defensible.

**gaps:**
- No document gives Africa/Eurasia-without-Russia-and-Belarus figures directly; they are derived from rounded $M figures. Each input is rounded, so the true margin could be roughly ±0.2 points off. 19.68% is exact from the printed figures.
- The derivation assumes the realignment involved only the three changes D11 lists. The fact that the totals tie and Latin America is unchanged supports this.
- There are no PDFs or layout files (the manifest shows method "text", pages null), so there were no extraction issues to check against originals.
- Coverage: I read D10 in full, D11 lines 1–160, and D05 lines 440–499. D02–D04, D06–D08, D09 and D12 were only searched for segment, Africa/Eurasia, Russia/Belarus, skin health and recast terms, not read in full. D01 (2019) has no segment or Africa matches.

**contaminated:** no
