# q04 rev 1 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, scope hook), given only the
  workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: c199d813c5fd35ac6b473e5fd6f893b5718e5eca410e0066b2d8dad87e8fb1ce

## Return

**North America (recast basis) operating profit margin, twelve months ended June 30, 2026: 20.33%.** Net sales were $3,635M and operating profit $739M, giving 739 / 3,635 = 20.330%. Two documents are needed, D10 and D12, and no single-document or ready-made shortcut exists.

answer: 20.33% (TTM net sales $3,635M, TTM operating profit $739M)

verdict: clear

shortest_path:
1. **D10** (`docs/cl_ex991_2026-03-17.txt`, "Segment Information (Recast)"):
   - Year ended December 31, 2025: `| North America | $ 3,679 | $ 1,510 | $ 1,375 | $ 4 | $ 790 |`
   - Six months ended June 30, 2025: `| North America | $ 1,823 | $ 737 | $ 700 | $ 3 | $ 384 |`
2. **D12** (`docs/cl_ex991_2026-07-31.txt`, Table 5):
   - Net sales row: `| North America(1) | $ 891 | $ 919 | $ 1,779 | $ 1,823 |`
   - Operating profit row: `| North America(1) | $ 192 | $ 187 | $ 333 | $ 384 |`
   - D12's recast H1 2025 figures (1,823 / 384) match D10 exactly.
3. **Calculation:**
   - Net sales: 3,679 − 1,823 + 1,779 = 3,635
   - Operating profit: 790 − 384 + 333 = 739
   - Margin: 739 / 3,635 = 0.203301, so 20.33%
4. **Cross-check by summing quarters:**
   - Q3 2025 (D10): 922 / 199
   - Q4 2025 (D10, full year minus nine months of 2,745 / 583): 934 / 207
   - Q1 2026 (D11 Table 4): 888 / 141
   - Q2 2026 (D12): 891 / 192
   - Total: 3,635 / 739. Same result.
5. **The segment definition:** D11 note (1) says "the skin health business (previously within the North America reportable operating segment)" moved into the new Europe, Middle East &amp; Africa segment, effective for the quarter ended March 31, 2026.

sufficient_documents:
- Minimum: {D10, D12}. Alternative: {D10, D11, D12}.
- D10 is required for the recast second-half 2025 (or full-year 2025) figures; no other document has them on the new basis.
- D12 is required for Q2 2026.
- No single document is enough: D10 has no 2026 data, D12 has no recast second-half 2025, and D11 covers only Q1.
- This is a simple route across two documents (a recast exhibit plus a quarterly release, then subtraction and a ratio). That is a difficulty risk, not a shortcut. D12's footnote ("Recast historical geographic segment information can be found on the Company's website") and D10's title make the join easy to find.

searches:
- **Concept terms (all of text/):** twelve, trailing, LTM, TTM, rolling, annualized, last 12 months. The only "Twelve Months" hits are the old-basis full-year tables in D05 and D09. No trailing-twelve-month figure appears for any segment.
- **Answer-shaped values (all of text/):** 3,635, 739, 20.3%, 20.33. The only hits are unrelated: 739 is company net income in D05/D09, and 20.3% is Europe in 1Q 2024 (D02).
- **Structure terms:** recast, skin health, reporting structure, realign. These hits come from D04–D07 and D09–D12. The 2026 structure appears only in D10–D12; D04–D07 refer to the earlier July 2024 recast. D09 mentions skin health only for the impairment, which is booked in Corporate.
- **Coverage:**
  - Read in full: D10, D12, manifest.json.
  - Read in part: D11 (lines 1–130 and 340–429).
  - Searched for "North America" only: D07, D08, D09.
  - Checked against originals: the docs/ sources for D10 and D12 match the extracted text.
- I saw `question.txt` in the packet root and deliberately did not read it.

readings/gaps:
- **Mixed-basis trap 1:** D09's old full-year 2025 North America (4,045 / 784, includes skin health), plus D12 H1 2026, minus D12 recast H1 2025, gives 4,001 / 733 = **18.32%**. This is wrong.
- **Mixed-basis trap 2:** old second-half 2025 plus new H1 2026.
  - Using D09 full year minus D07 H1 (2,020 / 394): 3,799 / 727 = **19.14%**.
  - Using D08 Q3 (999 / 190) plus D09 Q4 (1,021 / 203): 3,799 / 726 = **19.11%**.
  - Both are wrong, because the question asks for the 2026 definition.
- **Simple average of the four quarterly margins** (21.58%, 22.16%, 15.88%, 21.55%) gives about 20.29%. That is not the standard method; the margin should be built from the summed dollars.
- **GAAP vs Base Business:** no difference here. Segment operating profit sits outside the adjustments, which are in Corporate.
- **Rounding:** all inputs are rounded to $ millions, and the company calculates its percentages from unrounded figures. For example, Q1 2026 is 141/888 = 15.88% but reported as 15.8%; Q2 2026 is 192/891 = 21.55% but reported as 21.6%. The exact underlying margin could therefore differ by a few hundredths. Moving operating profit by ±1 gives 20.30% to 20.36%. The figure computable from the reported numbers is 20.33%.
- **Unread:** D01–D06 were not read in full (they cover periods before the window). D07–D09 were only searched, and D11 was read in part. None of the unread parts could hold recast second-half 2025 data, since the recast exhibit is dated March 2026.
