# q01 rev 2 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 4a2aae5ab7ba14e5789c823ef80800a3eb6e9e94d265593a9ae00f6d43581ac3

## Return

answer: +7.85%. The operations moved from Africa/Eurasia into EMEA had net sales of $879M in 2024 and $948M in 2025. (948 − 879) / 879 = +7.8498%, which rounds to +7.85%.

verdict: clear

shortest_path:
1. D11 (Q1 2026 release, line 85) says which operations moved: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment… Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment." So the moved piece is Africa/Eurasia excluding Russia and Belarus.
2. D09 (Q4/FY2025 release, Table 5, lines 460–464) gives full-year net sales on the old segment basis, in $M:

   | Segment | FY2025 | FY2024 |
   | --- | --- | --- |
   | North America | 4,045 | 4,113 |
   | Europe | 2,962 | 2,770 |
   | Asia Pacific | 2,814 | 2,858 |
   | Africa/Eurasia | 1,172 | 1,095 |

3. D10 (2026-03-17 "Segment Information (Recast)", lines 25–28 and 56–59) gives the recast full-year figures, in $M:

   | Segment | FY2025 | FY2024 |
   | --- | --- | --- |
   | North America | 3,679 | 3,716 |
   | Europe, Middle East &amp; Africa | 4,276 | 4,046 |
   | Asia Pacific | 3,038 | 3,074 |

   Latin America is unchanged and the totals match: 15,769 for 2025 and 15,618 for 2024.
4. Russia and Belarus = recast Asia Pacific − old Asia Pacific: 3,038 − 2,814 = 224 (2025) and 3,074 − 2,858 = 216 (2024).
5. Moved operations = Africa/Eurasia − Russia/Belarus: 1,172 − 224 = 948 (2025) and 1,095 − 216 = 879 (2024).
6. A second route through EMEA gives the same result. Skin health = old North America − recast North America: 366 (2025) and 397 (2024). Then EMEA − Europe − skin health: 4,276 − 2,962 − 366 = 948, and 4,046 − 2,770 − 397 = 879.
7. Change = 69 / 879 = +7.85%.

sufficient_documents: D09 + D10 + D11, all three needed.
- **D09** is the only source of old-basis full-year 2025 figures, including the Q4 split.
- **D10** is the only source of recast full-year figures.
- **D11** is the only document saying Russia and Belarus went to Asia Pacific rather than EMEA.
- **D05** can replace D09 for the 2024 old-basis figures (identical values at lines 457–461), but D09 is still required for 2025.

searches:
- **Terms:** "Africa/Eurasia", "Middle East", "EMEA", "realign", "reorganiz", "recast", "moved", "transferred", "reclassif", "Russia", "Belarus", "skin health", "Ukraine", "Central Asia", the segment table rows, and possible answer values (7.8x%, 948, 879, 224, 216).
- **Read in full:** the manifest and D10.
- **Read in part:** D11 lines 1–140, D09 lines 1–150 and 440–600, and the D01 header (a 2019 stock award agreement, not relevant).
- **Grep only:** D02–D08 and D12. D12 has only Q2/H1 2025 recast comparatives and a footnote without the Russia/Belarus detail.
- **Coverage:** Only D11 mentions Russia or Belarus. No document states the moved operations' sales or a ready-made growth rate; the numeric hits were coincidental (dividends, net income, other periods' growth rates).
- **Cross-check:** Quarterly 2025 data reconciles. D06/D07/D08 old basis plus D10 recast quarters give Africa/Eurasia ex-Russia/Belarus of 223, 236, 236 and an implied Q4 of 252. That sums to 947 against 948 from the full-year tables, a rounding difference.

readings/gaps:
- **Main risk is a distractor.** D09 Table 7 prints "Africa/Eurasia 7.0%", and the whole old segment gives 1,095 → 1,172 = +7.03%. That includes Russia and Belarus, which went to Asia Pacific, so it doesn't answer the question.
- **Other readings don't fit the wording.** Including skin health gives 1,276 → 1,314 = +2.98%, but the question says "from its Africa/Eurasia segment." Russia and Belarus alone give +3.70%, which is the wrong piece.
- **Rounding.** Summing 2025 quarters instead of using the full-year figure gives 947, or +7.74%. The full-year tables are the direct route for "full-year." The derived figures inherit ±1–2 of rounding from the $M tables, so the second decimal depends on using the published full-year values.
- **Unread sections.** The narrative parts of D02–D08 and D12 were only searched, not read in full. D02–D04 predate FY2025 and can't hold its figures.
- **Contamination.** None observed: no notes, question files or other packets were accessed.
