# q01 rev 0 - blind solver B (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-2 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 61ba023040204aa9fed82b996bd73e101e327afa4c6a97a7741ec4bf96a62cce

## Return

answer: About $948 million. That is Africa/Eurasia's full-year 2025 net sales of $1,172M minus $224M for Russia and Belarus, which moved to Asia Pacific. It is the Africa/Eurasia part of the recast 2025 Europe, Middle East &amp; Africa (EMEA) net sales of $4,276M.

confidence: high

path:
1. **How the segments were rebuilt.** D11 (text/D11.txt line 85, Q1 2026 release; same wording in docs/cl_ex991_2026-05-01.txt line 83) says: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment."
   - So EMEA = Europe + (Africa/Eurasia minus Russia and Belarus) + skin health.
   - Background: D04, D05 and D06 say skin health had been moved from Europe into North America in July 2024.
2. **Full-year 2025 under the old segments.** D09, Table 5, lines 460–464, twelve months 2025:
   - "North America | … | $ 4,045"
   - "Europe | … | 2,962"
   - "Asia Pacific | … | 2,814"
   - "Africa/Eurasia | … | 1,172"
   - These sum to the 15,769 Oral, Personal and Home Care total.
3. **Full-year 2025 under the new segments.** D10, "Segment Information (Recast)", lines 25–28 (checked against the docs/ source):
   - "North America | $ 3,679"
   - "Europe, Middle East &amp; Africa | 4,276"
   - "Asia Pacific | 3,038"
   - These also sum to 15,769, and Latin America is unchanged at 4,776.
4. **Calculation.**
   - Russia and Belarus = Asia Pacific's increase, 3,038 − 2,814 = 224.
   - Africa/Eurasia portion of EMEA = 1,172 − 224 = **948**.
   - Cross-check: skin health = North America's decrease, 4,045 − 3,679 = 366. Then 4,276 − 2,962 − 366 = **948**, and 2,962 + 948 + 366 = 4,276.
5. **Quarterly cross-check.** This uses the old-segment releases (D06 for Q1, D07 for Q2, D08 for Q3, D09 for Q4) and D10's recast quarters.
   - Russia and Belarus by quarter: 738−690 = 48, 746−687 = 59, 775−714 = 61, and 779−722 = 57 (Q4 recast taken as full year minus nine months).
   - Africa/Eurasia remaining in EMEA by quarter: 223, 236, 236, 252, which sum to 947.
   - Each quarter's EMEA rebuild lands within 1 of the recast figure, so the 947 versus 948 gap is rounding. The full-year rows give 948 directly.

minimal_documents: D09, D10 and D11.
- D11 is the only document that says what was combined. D12 only says history was recast ("Recast historical geographic segment information can be found on the Company's website"), so it cannot replace D11.
- D10 is the only document with recast full-year 2025 figures. D11 and D12 only carry recast Q1 and Q2 2025.
- D09 is the only document with old-segment full-year and Q4 2025 figures. D06–D08 cover only the first nine months.

readings:
- Counting all of Africa/Eurasia gives $1,172M. That is wrong, because the definition excludes Russia and Belarus.
- Treating EMEA minus Europe as the Africa/Eurasia piece gives 4,276 − 2,962 = $1,314M. That is wrong, because it leaves skin health's $366M inside.
- Summing the quarters gives $947M, a rounding difference only.
- The headline totals alone can't separate the moves, because any split of skin health into Asia Pacific would also reconcile. D11's text settles it: all of skin health went to EMEA and only Russia and Belarus went to Asia Pacific.

gaps:
- The documents give no direct dollar figure for Russia and Belarus or for skin health. Both are worked out from the old and recast totals, assuming no other operations moved, which is what D11's text implies.
- All figures are rounded to millions, so ±1 is possible.
- There are no PDFs or layout files in the packet; the docs/ originals are text, and the decisive rows match them.
- Read in full: D09, D10, the first 160 lines of D11, and D12 lines 55–124. The segment tables in D06–D08 were read in part. D01–D05 were searched by term only.

contaminated: no
