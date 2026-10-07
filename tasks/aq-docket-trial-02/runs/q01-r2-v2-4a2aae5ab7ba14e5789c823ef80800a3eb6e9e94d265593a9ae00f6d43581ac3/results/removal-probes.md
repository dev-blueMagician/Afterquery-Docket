# q01 rev 2 - removal probe without D11 (2026-10-06)

Fresh blind-solver agent given the shortcut packet of this run, the verbatim question and an
instruction to treat D11 as absent and answer "as you normally would" (best answer plus probability;
not a forced guess). Approximates the platform's document check for D11. Not an official blind solve.
tested_sha256: 4a2aae5ab7ba14e5789c823ef80800a3eb6e9e94d265593a9ae00f6d43581ac3. Gold: +7.85%.
Rev 1's probes (same inputs; forced guesses) are in runs/q01-r1-v2-3fabaea5.../results/removal-probes.md:
without D09 +50, without D10 +41, without D11 +69 at about 50%.

## Return (verbatim)

I couldn't answer this exactly without D11. My best answer is **+7.03%**, with about a 65% chance it is right. None of the other eleven documents says which Africa/Eurasia operations went into Europe, Middle East &amp; Africa. The 7.03% assumes the whole Africa/Eurasia segment moved there.

answer: Not answerable exactly without D11. Best answer: **+7.03%**, at about 65% probability.

confidence: low (that the figure matches the gold); high (that the figure follows from the stated assumption)

path:
1. The Africa/Eurasia full-year net sales come from D09, Table 5 (Twelve Months 2025 / 2024), line 464: "| Africa/Eurasia | 309 | 269 | 1,172 | 1,095 |". D05 line 461 shows the same 2024 figure of 1,095. The four 2025 quarters add up to 1,172: 271 (D06), 295 (D07), 297 (D08) and 309 (D09).
2. The calculation is (1,172 − 1,095) / 1,095 = 77 / 1,095 = 7.032%, which gives **+7.03%**. D09 Table 7, line 583, rounds the same change to "Africa/Eurasia 7.0%".
3. The restated figures are in D10, "Segment Information (Recast)". Europe, Middle East &amp; Africa is $4,276M (2025) and $4,046M (2024). North America is 3,679 / 3,716 and Asia Pacific is 3,038 / 3,074. Latin America and the total for Oral, Personal and Home Care are unchanged (15,769 / 15,618). Africa/Eurasia no longer appears as a segment.
4. D12 footnote (1), line 83, only says: "The Company has recast its historical geographic segment information to conform to the reporting structure effective for the quarter ended March 31, 2026." It is attached to North America, Europe, Middle East &amp; Africa, and Asia Pacific, and does not say what moved. The source files for D10 and D12 also contain no description.
5. I compared the D09 segments with the D10 restated segments to see where sales moved:
   - 2025: Europe, Middle East &amp; Africa minus (Europe + Africa/Eurasia) = 4,276 − (2,962 + 1,172) = +142. North America fell 366 (4,045 → 3,679) and Asia Pacific rose 224 (2,814 → 3,038), and 142 + 224 = 366.
   - 2024: 4,046 − (2,770 + 1,095) = +181. North America fell 397 and Asia Pacific rose 216, and 181 + 216 = 397.
   - So North America operations also moved into Europe, Middle East &amp; Africa and/or Asia Pacific. The figures balance either way, so they cannot show whether part of Africa/Eurasia went to Asia Pacific instead. The 2025 quarters and operating profit don't settle it either: the alternative split also gives positive flows every quarter.
6. Reasons for the full-segment assumption:
   - The new segment's name covers Africa and the Middle East.
   - Africa/Eurasia disappears from the restated tables.
   - D12 now defines emerging markets (line 517) as "Africa, the Middle East and Eastern and Central Europe", which fits Eurasia being counted as Eastern Europe.
   - Only whole-segment Africa/Eurasia totals give full-year figures for the moved operations.
   - The main risk is that D11 describes only part of Africa/Eurasia moving, with the rest going to Asia Pacific.

minimal_documents: D09 alone holds both figures for the best answer; D10 (and D12) only show the restructuring. D05 can replace D09 for the 2024 figure, but nothing replaces D09 for 2025. The full answer needs D11 to say what moved.

readings:
- Part of Africa/Eurasia moved to Asia Pacific, and all of North America's moved operations went to Europe, Middle East &amp; Africa: 1,314 − 366 = 948 (2025) versus 1,276 − 397 = 879 (2024), which is **+7.85%** (about 15%).
- Simply taking the restated Europe, Middle East &amp; Africa figure minus the old Europe figure: 1,314 versus 1,276, which is **+2.98%**. This is not valid, because 1,314 is more than the whole Africa/Eurasia segment (1,172). I'd give it about 10%, as a possible error by whoever set the question.
- Any other split of the flows can't be determined from these documents.

gaps:
- The description of what moved (presumably the D11 footnote) is missing.
- Full-year figures for a partial Africa/Eurasia carve-out are not in any remaining document.
- Not read (by instruction): D11 / docs/cl_ex991_2026-05-01.txt.
- Partly read:
  - D02–D08: segment tables and footnotes found by search only.
  - D09: lines 55–170 and 440–610.
  - D12: lines 1–170 and 405–580.
- D01 is an unrelated 2019 stock-award agreement.
- All documents are text-only, so there were no PDFs or extraction problems.

contaminated: no

## Caller note

Result: best answer +7.03% (the decoy), gold +7.85% only as a 15% alternative. In an unforced
answer D11 behaves as needed. Together with rev 1's forced probe (+69 at about 50%), the platform's
document check on D11 is a moderate-to-low risk; the excluded-item clause and the reviewer note
remain the fallback.
