# q01 rev 2 - blind solver B (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-2 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 4a2aae5ab7ba14e5789c823ef80800a3eb6e9e94d265593a9ae00f6d43581ac3

## Return

**answer:** +7.85%

**confidence:** high

**path:**
1. **What was moved (D11, Q1 2026 release, line 85, footnote 1):** "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So the moved operations are Africa/Eurasia minus Russia and Belarus.
2. **Old-structure full-year net sales ($M, 2025 / 2024) (D09, Table 5, lines 460–465):** North America 4,045 / 4,113; Latin America 4,776 / 4,782; Europe 2,962 / 2,770; Asia Pacific 2,814 / 2,858; Africa/Eurasia 1,172 / 1,095; Total Oral, Personal and Home Care 15,769 / 15,618. These match the source file docs/cl_ex991_2026-01-30.txt (lines 458–463). The 2024 column also matches D05 lines 457–462 (4,113; 4,782; 2,770; 2,858; 1,095; 15,618).
3. **Recast full-year net sales (D10, "Segment Information (Recast)", lines 25–28 and 56–59):** North America 3,679 / 3,716; Latin America 4,776 / 4,782; "Europe, Middle East &amp; Africa | 4,276" / "4,046"; Asia Pacific 3,038 / 3,074. These match docs/cl_ex991_2026-03-17.txt (lines 23–26, 54–57).
4. **Totals check:** the recast segments add up to 15,769 (2025) and 15,618 (2024), the same as the old structure. Latin America is unchanged, as expected.
5. **Russia and Belarus** (new Asia Pacific minus old Asia Pacific): 2025: 3,038 − 2,814 = 224; 2024: 3,074 − 2,858 = 216.
6. **Moved operations** (Africa/Eurasia minus Russia and Belarus): 2025: 1,172 − 224 = **948**; 2024: 1,095 − 216 = **879**.
7. **Cross-check through EMEA:**
   - Skin health (old minus new North America): 2025: 4,045 − 3,679 = 366; 2024: 4,113 − 3,716 = 397.
   - EMEA minus Europe minus skin health: 2025: 4,276 − 2,962 − 366 = 948; 2024: 4,046 − 2,770 − 397 = 879. Both routes agree.
8. **Change:** (948 − 879) / 879 = 69 / 879 = 0.078498…, which is +7.8498% and rounds to **+7.85%**.

**minimal_documents:** D09, D10, D11.
- D05 can replace D09 for the 2024 figures only. No other document gives full-year 2025 figures in the old structure (D08 covers only nine months).
- D10 is the only source of full-year recast figures. D11 and D12 have recast figures only for Q1/Q2 2025.
- D11 is the only document that says what the realignment contained. D12's footnote just says the history was recast and doesn't describe the content.

**readings:**
- **Treating the whole Africa/Eurasia segment as moved** (ignoring the Russia/Belarus exclusion): (1,172 − 1,095) / 1,095 = 77 / 1,095 = **+7.03%**. This matches D09 Table 7's "Africa/Eurasia 7.0%" as-reported change. It conflicts with D11's explicit exclusion, so it is weaker.
- **Not defensible:** EMEA minus old Europe without removing skin health gives 1,314 vs 1,276, or +2.98%. That contradicts D11, which says skin health was also combined into EMEA.

**gaps:**
- No document states the moved operations' net sales directly; they are derived from rounded $-million figures.
- Each derived yearly value could be off by up to about ±1.5M from rounding, which could shift the result by about ±0.35 points. At the printed figures, the answer is +7.85%.
- The 2023 recast figures show a 1M rounding mismatch (824 vs 825). There is no such mismatch for 2024 or 2025.
- **Coverage:** I read D09 lines 1–165 and 440–609 and all of D10, D11 lines 1–160, and the D05 table rows. I searched all twelve text files for: segment names, EMEA, Russia, Belarus, skin health, and realign/recast/reportable segment.
- **Not read in full:** D01–D04, D06–D08 and D12. Their search hits were only old-structure quarterly data, the July 2024 skin-health recast note, and Q2 2026 recast footnotes with no description of the realignment.
- D01 (2019) had no segment-name hits. The documents are text, not PDFs, so there were no page images to check.
- I did not open question.txt in the packet root.

**contaminated:** no
