# q04 rev 2 - blind solver A (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, scope hook), given only the
  workspace root, the solver-1 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8

## Return

**answer:** 20.33%

**confidence:** high

**path:**
1. **How the segment was defined from 2026.** D11 (Q1 2026 release, note (1), line 85) says: "The Company has recast its historical geographic segment information to conform to the reporting structure effective for the quarter ended March 31, 2026. The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment." D12 repeats that North America(1) is recast "to conform to the reporting structure effective for the quarter ended March 31, 2026." So from 2026, North America no longer includes skin health.
2. **2025 figures on the new basis.** D10 is titled "Segment Information (Recast)" (segmentrecast.htm, 2026-03-17). Its prior-year rows match the comparatives that D11 and D12 label as recast:
   - Q1 2025 North America: $904 / $197
   - Q2 2025: $919 / $187
   - H1 2025: $1,823 / $384

   This confirms D10 uses the 2026 structure. North America rows in D10 (net sales / operating profit, $ millions), checked against docs/cl_ex991_2026-03-17.txt:
   - Year ended December 31, 2025: "North America | $ 3,679 | … | $ 790"
   - Six months ended June 30, 2025: "$ 1,823 | … | $ 384"
   - Three months ended September 30, 2025: "$ 922 | … | $ 199"
   - Nine months ended September 30, 2025: "$ 2,745 | … | $ 583"
   - Derived Q4 2025: net sales 3,679 − 2,745 = 934; operating profit 790 − 583 = 207
3. **2026 figures.** D12 Table 5, checked against docs/cl_ex991_2026-07-31.txt lines 426 and 442:
   - Net sales: "North America(1) | $ 891 | $ 919 | $ 1,779 | $ 1,823" (Q2 2026, Q2 2025, H1 2026, H1 2025)
   - Operating profit: "North America(1) | $ 192 | $ 187 | $ 333 | $ 384"

   This matches D11 Table 4 for Q1 2026: net sales $888, operating profit $141 (888 + 891 = 1,779; 141 + 192 = 333).
4. **Twelve months ended June 30, 2026** (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026):
   - Net sales: 922 + 934 + 888 + 891 = 3,635. Cross-check: 3,679 − 1,823 + 1,779 = 3,635.
   - Operating profit: 199 + 207 + 141 + 192 = 739. Cross-check: 790 − 384 + 333 = 739.
   - Margin: 739 / 3,635 = 0.203301, which is **20.33%**.
5. **Consistency check.** The restated D10 totals match the original D09 totals for 2025: total Oral, Personal and Home Care net sales are 15,769 in both, total company net sales are 20,382, and Corporate is (1,717). Charges such as the Strategic Growth and Productivity Program sit in Corporate, so North America operating profit is the same on GAAP and Base Business bases.

**minimal_documents:** D10 + D12. D10 is the only source of the recast second half of 2025, and D12 is the only source of Q2 2026 and the first half of 2026. D11 can replace nothing that is needed; it adds the wording of the segment change and the Q1 2026 cross-check.

**readings:**
- **Simple average of the four quarterly margins** (21.58%, 22.16%, 15.88%, 21.55%): 20.29%. This is not a proper twelve-month margin.
- **Mixed definitions** (contrary to the question's wording): old-basis Q3 2025 from D08 ($999 / $190) and Q4 2025 from D09 ($1,021 / $203), plus first-half 2026 on the new basis, give 726 / 3,799 = 19.11%.
- **Old basis throughout:** not answerable, because 2026 quarters are reported only on the new basis.

**gaps:**
- The source figures are rounded to whole millions. Rounding alone means the true margin could fall roughly between 20.28% and 20.38%; 20.33% is the result from the printed figures. The company's own quarterly percentages, calculated from unrounded data (15.8% for Q1 2026 and 21.6% for Q2 2026), differ slightly from ratios of the printed figures (15.9% and 21.5%).
- D10 does not describe the segment change itself. I linked it to the 2026 structure through the matching recast comparatives in D11 and D12.
- Coverage: I read D10, D11 and D12 in full and D09's segment table (lines 440–504). For D08 and D09 I only saw search hits. D01–D07 I only searched (for "recast", "skin health" and "twelve months"). They cover 2019–2025 periods before the 2026 recast.
- No layout files or PDFs exist in this packet; the originals are text files.

**contaminated:** no

Files used:
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\solver-1\text\D10.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\solver-1\text\D11.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\solver-1\text\D12.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\solver-1\docs\cl_ex991_2026-03-17.txt
- D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\solver-1\docs\cl_ex991_2026-07-31.txt
