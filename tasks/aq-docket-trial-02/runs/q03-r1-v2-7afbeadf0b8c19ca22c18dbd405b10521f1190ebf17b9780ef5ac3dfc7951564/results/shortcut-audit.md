# q03 rev 1 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 7afbeadf0b8c19ca22c18dbd405b10521f1190ebf17b9780ef5ac3dfc7951564

## Return

answer: 19.68%. In 2024 the Africa/Eurasia operations that moved into EMEA (Africa/Eurasia excluding Russia and Belarus) had about $879M of net sales and $173M of segment operating profit. 173 / 879 = 19.68%.

verdict: clear

shortest_path:
1. **What moved.** D11 (`docs/cl_ex991_2026-05-01.txt`), note (1), line 85: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment. In conjunction with this realignment, Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So only part of Africa/Eurasia went to EMEA.
2. **Recast 2024 figures.** D10 (`docs/cl_ex991_2026-03-17.txt`), lines 56–59, net sales / operating profit in $M:
   - North America: 3,716 / 856
   - EMEA: 4,046 / 814
   - Asia Pacific: 3,074 / 892
3. **Old-structure 2024 figures.** D05 Table 5 (lines 457–478), repeated in D09 (lines 460–481), net sales / operating profit in $M:
   - North America: 4,113 / 839
   - Europe: 2,770 / 658
   - Asia Pacific: 2,858 / 812
   - Africa/Eurasia: 1,095 / 253
   - Both structures total 15,618 net sales and 4,088 operating profit, so the bridge reconciles.
4. **Route A, through Asia Pacific.**
   - Russia and Belarus = recast Asia Pacific minus old Asia Pacific: net sales 3,074 − 2,858 = 216; operating profit 892 − 812 = 80.
   - Moved Africa/Eurasia: net sales 1,095 − 216 = 879; operating profit 253 − 80 = 173.
5. **Route B, a cross-check through EMEA.**
   - Skin health = old North America minus recast North America: net sales 4,113 − 3,716 = 397; operating profit 839 − 856 = −17.
   - Moved Africa/Eurasia: net sales 4,046 − 2,770 − 397 = 879; operating profit 814 − 658 + 17 = 173. Same result.
6. **Margin.** 173 / 879 = 0.196815, or 19.68%.

The same method works for other years: 2023 gives 143/824 (17.35%) and 2025 gives 195/948 (20.57%). Both reconcile within rounding, which supports the approach, but they are the wrong period.

sufficient_documents: D11 (what moved) + D10 (recast 2024) + either D05 or D09 (old 2024 figures; they report identical values). No single document is enough:
- D10 does not say what the new segment contains and has no old-structure figures.
- D05 and D09 have no recast figures.
- D11 and D12 contain no full-year 2024 data.

D01 (a 2019 performance stock unit award agreement) is irrelevant.

searches:
- Terms searched across all 12 text files: "Africa/Eurasia", "Europe, Middle East", "EMEA", "Middle East", "recast", "realign", "reorganiz", "reclassif", "new segment", "reportable segment", "Russia", "Belarus", "skin health", "excluding Russia".
- Answer-shaped values searched: 19.6, 19.7, 23.1%, 879, 173, 216, 397. Every hit was unrelated, e.g. dividends of (879) in D12 and Corporate (397) in D03/D07.
- Read in full: manifest, D10, D01. Read in part: D11 (1–140), D05 (440–599), D09 (60–149, 440–599), D12 (60–129).
- D02–D04 and D06–D08 were covered by searches. Only D11 explains what the new segment contains; only D10 has recast 2024 figures.
- I confirmed the D10 2024 figures and the D11 "excluding Russia and Belarus" wording in the original `docs/` text.
- I did not open `question.txt` or anything outside this packet's `docs/` and `text/`.

readings/gaps:
- **All of Africa/Eurasia (rejected):** 253 / 1,095 = 23.11%. This ignores D11's exclusion of Russia and Belarus. It is the obvious trap.
- **Recast EMEA minus Europe, ignoring skin health (wrong):** 156 / 1,276 = 12.23%.
- **Rounding:** D10's EMEA 2024 cost lines sum to 813, not the reported 814. Using 813 in Route B would give 172 / 879 = 19.57%. Route A has no rounding gap (Asia Pacific's lines sum exactly to 892) and matches the reported figures, so 19.68% stands.
- **Difficulty risk, not a shortcut:** the arithmetic is simple, and a solver who misses D11's note will probably answer 23.11%.
- No extraction gaps found; every file was extracted as plain text.
