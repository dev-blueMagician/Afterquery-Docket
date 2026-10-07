# q01 rev 2 shortcut auditor (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

Prompt: workspace root, packet path shortcut, exact question text only.

**Verdict: clear.** Actual fiscal 2026 reported diluted EPS from continuing operations was $10.44. The outlook in force when Q4 began was $10.62 to $10.82, with a midpoint of $10.72. The difference is **−$0.28**.

answer: −$0.28. The actual $10.44 was 28 cents below the $10.72 midpoint of the December 18, 2025 range.

verdict: clear

shortest_path:
1. **When Q4 began:** D05 line 11 says "third quarter ended February 22, 2026", so Q4 began February 23, 2026. Two other documents give the same date: D04 line 11 says "second quarter ended November 23, 2025" (plus 13 weeks gives February 22, 2026); D06 line 13 says "fiscal year ended May 31, 2026, which included a 53rd week" (a 14-week Q4 starting February 23).
2. **Which outlook applies:** The March 19, 2026 update in D05 came about four weeks into Q4, so it doesn't count. The outlook in force on February 23 was the December 18, 2025 update (D04 line 76: "The Company updated its full year financial outlook for fiscal 2026").
3. **The range:** D04 line 139, in the reconciliation table, reads "Reported diluted net earnings per share from continuing operations | $10.62 | to | $10.82". The outlook bullets at line 90 show only the adjusted range of $10.50 to $10.70. Midpoint: (10.62 + 10.82) / 2 = 10.72.
4. **The actual:** D06 line 49 reads "Reported diluted net earnings per share from continuing operations were $10.44". The same $10.44 appears in the year-to-date reconciliation (line 173) and the 12-month income statement (line 271).
5. **Calculation:** 10.44 − 10.72 = −0.28.

sufficient_documents:
- Minimal set: D04 plus D06. The Q4 start date is stated outright in D05 and can also be worked out from the week counts in D04 or D06.
- No single document is enough: D04 has no full-year actual; D06 gives only the fiscal 2027 outlook and does not restate the fiscal 2026 range or compare results to guidance; D05 gives a later range and only nine-month results.
- No duplicated evidence gives a different route.

searches:
- Darden coverage: "Darden|DRI|Olive Garden" appears only in D04 to D06.
- Values searched: 10.62, 10.82, 10.72, 10.44, 10.40, 10.50, 10.45 and 0.28. The range values appear only in D04 (line 139) and D05 (line 139); $10.44 appears only in D06. The 0.28 hits are Wendy's and Chipotle dividend and EPS figures, not Darden. No precomputed midpoint or difference appears anywhere.
- Answer-shaped wording: "midpoint", "guidance", "prior outlook", "high end" and "low end" have no hits in the Darden files; the "guidance" hits are in Chipotle and Wendy's files.
- Outlook in D06 refers only to fiscal 2027.
- Dates: searched the docs/ originals for "quarter ended" and "fiscal year ended".
- Coverage: read the manifest and D04, D05 and D06 in full and checked the docs/ originals (match the text/ files). D01–D03 and D07–D12 only searched.

readings/gaps:
- Trap reading (rejected): the March 19, 2026 outlook in D05 (line 139: $10.40 to $10.50, midpoint $10.45) gives −$0.01; issued after Q4 began.
- Adjusted reading (rejected): December adjusted midpoint $10.60 gives −$0.16 against the reported actual, or +$0.04 against the adjusted actual of $10.64; the question asks for reported figures.
- Gap: no Darden statements in the packet between December 18, 2025 and March 19, 2026 (for example a mid-quarter investor conference update); no Q1 fiscal 2026 release. Nothing points to an interim update, but its absence is unresolved rather than proof.
- Difficulty risk: once the right outlook is chosen, a simple subtraction across two documents. The discriminating step is timing, choosing D04 over the more obvious "latest" outlook in D05. Allowed cross-document reasoning, not a shortcut.
