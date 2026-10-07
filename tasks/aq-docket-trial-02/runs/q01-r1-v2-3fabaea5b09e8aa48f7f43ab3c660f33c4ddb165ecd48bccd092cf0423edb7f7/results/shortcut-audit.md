# q01 rev 1 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7

## Return

answer: **+$69 million.** Net sales of the operations moved from Africa/Eurasia into Europe, Middle East &amp; Africa (EMEA) rose from $879M in 2024 to $948M in 2025. Those operations are Africa/Eurasia excluding Russia and Belarus.

verdict: clear

shortest_path:
1. D11 (Q1 2026 release), footnote (1) at line 85, defines what moved: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment. In conjunction with this realignment, Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment."
2. D09 (Q4 2025 release), Table 5, gives the old-structure twelve-month net sales ($M), as 2025 / 2024:
   - Africa/Eurasia: 1,172 / 1,095
   - Asia Pacific: 2,814 / 2,858
   - Europe: 2,962 / 2,770
   - North America: 4,045 / 4,113
3. D10 (2026-03-17 "Segment Information (Recast)") gives the new-structure full-year figures, as 2025 / 2024:
   - Asia Pacific: 3,038 / 3,074
   - EMEA: 4,276 / 4,046
   - North America: 3,679 / 3,716
4. Russia and Belarus = recast Asia Pacific minus old Asia Pacific: 3,038 − 2,814 = 224 (2025) and 3,074 − 2,858 = 216 (2024).
5. Moved operations = Africa/Eurasia minus Russia and Belarus: 1,172 − 224 = 948 (2025) and 1,095 − 216 = 879 (2024). The change is 948 − 879 = **+69**.
6. A second route gives the same result. Skin health = old North America minus new North America: 366 (2025) and 397 (2024). Then EMEA − Europe − skin health is 4,276 − 2,962 − 366 = 948 and 4,046 − 2,770 − 397 = 879.
7. The structures reconcile: Oral, Personal and Home Care totals are 15,769 and 15,618 under both. Latin America and Pet Nutrition are unchanged.

sufficient_documents: D09 + D10 + D11, all three needed.
- D05 (Q4 2024 release) repeats the 2024 old-structure values (Asia Pacific 2,858; Africa/Eurasia 1,095). It can replace D09 for 2024 only; D09 is still needed for 2025.
- Only D10 has full-year recast figures. D11 and D12 have only quarterly or six-month recast data.
- Only D11 says what moved. Without it, D09 + D10 alone fit at least two allocations (+69 or +77). That ambiguity is why D11 is required, so this is not a shortcut.
- Footnotes in D04, D05 and D06 confirm the July 1, 2024 recast that put Europe's skin health business into North America. This is consistent with D11 but not required.

searches:
- Across all text files: Russia, Belarus, skin health, realign, recast, Middle East &amp; Africa, Eurasia, "excluding Russia", moved, transferr. Only D11 line 85 describes the realignment. No document reports Africa/Eurasia excluding Russia and Belarus, or the Russia and Belarus sales, directly.
- Fully read: manifest, D09, D10, D11.
- Partly read: D01 (a 2019 stock-unit award agreement, irrelevant; its only match for these terms is in that agreement's text), and D05's segment rows.
- Covered only by targeted searches: D02–D04, D06–D08, D12. Their matches are old-structure Africa/Eurasia rows or generic recast footnotes.
- `question.txt` in the packet root was deliberately not read. No notes, memory or project instructions appeared in context, so I'm reporting no contamination. I can't confirm the invocation mode from inside the session.

readings/gaps:
- Wrong readings to watch for:
  - **+77**: all of old Africa/Eurasia (1,172 − 1,095), which ignores that Russia and Belarus went to Asia Pacific.
  - **+38**: recast EMEA minus old Europe ((4,276 − 2,962) − (4,046 − 2,770) = 1,314 − 1,276), which wrongly counts skin health as moved Africa/Eurasia operations.
  - **+230**: the change in the whole recast EMEA segment.
- Rounding: every input is a separately rounded whole-million figure ("may not sum due to rounding"), so the derived 948 and 879, and the +69, could be off by about $1–2M.
- Difficulty risk: once D11's footnote is found, the rest is simple subtraction across three documents. That is allowed cross-document reasoning, not a shortcut.
- Gaps: D02–D04, D06–D08 and D12 were not read in full, only searched.

Relevant files (all under `D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q01-r1-v2-3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7\shortcut\text\`):
- `D09.txt`
- `D10.txt`
- `D11.txt`
- `D05.txt`
- `manifest.json`
