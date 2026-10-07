# q04 rev 0 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, scope hook), given only the
  workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00

## Return

answer: **20.33%.** North America made $739M of operating profit on $3,635M of net sales over those twelve months, using the segment as recast from 2026.

verdict: clear

shortest_path:
1. **D10** (the 2026-03-17 "Segment Information (Recast)" exhibit), 2025 figures under the 2026 definition:
   - Full year 2025 (line 25): "North America | $ 3,679 | … | $ 790"
   - First half 2025 (line 245): "$ 1,823 | … | $ 384"
2. **D12** (Q2 2026 release), Table 5:
   - Net sales, first half 2026 (line 428): "North America(1) | $ 891 | $ 919 | $ 1,779 | $ 1,823"
   - Operating profit, first half 2026 (line 444): "$ 192 | $ 187 | $ 333 | $ 384"
   - Note (1) says the history was recast to the structure effective for the quarter ended March 31, 2026. D12's first-half 2025 figures match D10's.
3. Twelve-month totals:
   - Net sales = 3,679 + 1,779 − 1,823 = 3,635
   - Operating profit = 790 + 333 − 384 = 739
   - Margin = 739 / 3,635 = 20.330%, which rounds to **20.33%**
4. Cross-check by adding the four quarters gives the same result:
   - Q3 2025 (D10 line 312): 922 / 199
   - Q4 2025 (D10, full year minus nine months): 3,679 − 2,745 = 934 and 790 − 583 = 207
   - Q1 2026 (D11 lines 369/385): 888 / 141
   - Q2 2026 (D12): 891 / 192
   - Totals: 3,635 / 739
5. What changed in the segment (D11 line 85): the skin health business was moved out of North America into the new Europe, Middle East &amp; Africa segment.

sufficient_documents:
- Minimal set: **D10 + D12**. No single document is enough. D10 has no 2026 data, and D12 has no second-half 2025 data. Nothing in the packet holds Q3 or Q4 2025 under the new definition together with 2026 results.
- Alternative: D10 + D11 + D12, adding up the quarters.
- Difficulty risk: this is a simple two-document calculation (full year + this year's first half − last year's first half). It is ordinary cross-document arithmetic, not a whole-answer lookup.

searches:
- "North America" across all of text/ (D02–D12 hits reviewed).
- Direct-figure terms: twelve, trailing, last 12, 12 months, LTM, TTM, rolling (with word boundaries), annualized, "20.3%" and "fourth quarter 2025". These found only full-year tables that end December 31 under the old structure, plus an unrelated Europe "20.3%" in D02.
- The candidate result values (3,635, 739, 934, 207): none appears as a North America figure, so no reported total gives the answer away.
- Read in full: D10 and D12.
- Read in part: D11 (lines 1–130 and 340–459) and D09 (lines 90–149 and 440–509).
- Checked the original files for D10 and D12 against their text versions. They match, and D10 has no standalone Q4 2025 table.
- I did not open question.txt or anything outside the packet.

readings/gaps:
- **Old-definition trap.** D09 reports full-year 2025 North America under the old structure as $4,045M / $784M.
  - Old full year + new 2026 − new first half 2025 gives 733 / 4,001 = 18.32%.
  - Old Q3 2025 from D08 (999 / 190) and old Q4 2025 from D09 (1,021 / 203), plus new 2026 quarters, give 726 / 3,799 = 19.11%.
  - Old full year + new 2026 − old first half 2025 from D07 (2,025 / 390) gives 727 / 3,799 = 19.14%.
  - All three mix definitions and are wrong.
- **Averaging the quarters' margins** instead of dividing total profit by total sales gives 20.29%. The question asks for a percentage of the segment's net sales, which means total over total.
- **Underlying unrounded figures.** The company's own percentages are calculated before rounding: D11 states 15.8% for Q1 2026, while 141 / 888 = 15.88%. From the unrounded data the true margin could fall anywhere in about 20.28–20.38%. Calculated from the reported millions, it is 20.33%.
- **Base Business (non-GAAP) view.** This gives the same answer. Restructuring (productivity program) and other special charges sit in Corporate, not in the segment figures.
- **Not read:** D01–D08 beyond the search hits. They are 2019–2025 releases using older segment definitions, including the July 2024 recast that moved skin health from Europe into North America, so they cannot supply figures under the 2026 definition.

Files:
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r0-v2-4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00\shortcut\text\D10.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r0-v2-4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r0-v2-4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00\shortcut\text\D11.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r0-v2-4fda6f2ac451ec3f1115bbe1b100a2b2bf2662eba2f5ed198ffcb10decdc3a00\shortcut\text\D09.txt
