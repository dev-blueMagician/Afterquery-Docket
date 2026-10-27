# q01 rev 3 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-11. Packet: the prepared corpus, D01-D07.
Prompt: workspace root, packet path and the exact question only, launched from the workspace root. Optional
diagnostic for one concrete issue: whether a fresh reader identifies the webinar of the new anchor among the
three webinars in the documents and still finds the minimum that applied on its date.
tested_sha256 df6c090d374a0de4121b2022c569cdb6effd1b6904c242a8d76ab3ae47d0956d. Not a platform result.

answer: 76.0 percent (TE2 of about 76.0%)

confidence: high

path:
1. Webinar date. The proposal to create TE2 was the February 25, 2022 test-procedure NOPR. D03 (89 FR 104861, text line 104-106): DOE "proposed a new test procedure ... appendix B ... to measure energy efficiency under the TE2 metric" and "The February 2022 NOPR had a 60-day comment period and DOE held a webinar public meeting on March 29, 2022." Same statement in D04 (90 FR 5562, lines 103 and 141). The other webinars in the packet are not on this proposal: D01 is December 19, 2022 (consumer furnaces preliminary TSD); D05 is May 29, 2025 (proposal to rescind TE2/Appendix B).
2. Federal minimum on that day. D02 (87 FR 78823, lines 135-136): "for gas-fired CWAFs manufactured starting on January 1, 1994, until January 1, 2023, TE at the maximum rated capacity ... must be not less than 80 percent. For gas-fired CWAFs manufactured starting on January 1, 2023, the TE ... must be not less than 81 percent." A unit built March 29, 2022 therefore has minimum TE = 80 percent (not the 81 percent DOE uses in its worked example).
3. DOE's jacket-loss estimate. D03 (89 FR 104863, line 158): with the weatherized jacket loss factor of 3.3, "a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses." (0.75 x 3.3 = 2.475.) D04 line 189 repeats "as much as a 2.5 percent difference."
4. DOE's part-load estimate. D03 (89 FR 104863-104864, lines 164-168): "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate ... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate." So the part-load effect scales as (part-load weight) x 2 points.
5. DOE's combined method is additive in percentage points. D03 line 144: "between 3.5 percent lower ... to 1 percent higher"; D03 line 176 / D04 lines 143, 193: "a CWAF with a TE of 81 percent ... could ... have an actual range of efficiencies from 77.5 to 82 percent" (81 - 2.5 - 1.0 = 77.5).
6. NEEA's largest part-load share. D04 (90 FR 5565, line 187): DOE "reviewed modeling submitted by NEEA that showed a range of times for CWAF operation at full and part loads, from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)." Largest part-load share = 75 percent.
7. Calculation. Part-load penalty at 75 percent weight = 0.75 x 2 = 1.5 points. Low-end TE2 = 80 - 2.5 (jacket) - 1.5 (part load) = 76.0. Equivalent weighted form: 0.25 x (80 - 2.5) + 0.75 x (80 - 2 - 2.5) = 19.375 + 56.625 = 76.0. Using the unrounded jacket figure 2.475 gives 76.025, which still rounds to 76.0.

minimal_documents: D02 + D03 + D04.
- D02 is the only document that gives the January 1, 2023 compliance date separating 80 from 81 percent (D03/D04 only say the minimum "went from 80 to 81 percent" without the date).
- D04 is the only document with the NEEA modeling range (75 percent part load); it also carries the webinar date.
- D03 gives the explicit "2 percent higher or lower" part-load figure and the 50 percent weighting arithmetic. Alternative: D02 + D04 alone suffices if the solver infers the part-load term from D04 (81 to 77.5 is 3.5 lower; jacket up to 2.5; remainder 1.0 at the "50 percent weighting" implies 2 points at reduced rate). That is an inference, not a printed figure.

readings:
- Using the standard in force after January 1, 2023 (81 percent) instead of the one applying on the manufacture date: 81 - 2.5 - 1.5 = 77.0. I reject this because the question fixes the build date at March 29, 2022.
- Keeping DOE's adopted 50 percent weighting: 80 - 2.5 - 1.0 = 76.5. Rejected because the question explicitly reweights part load.
- Taking NEEA's other endpoint (30 percent part load): 80 - 2.5 - 0.6 = 76.9. Rejected; "largest share" for part load is 75 percent.
- Treating "percent lower" as relative rather than percentage points: 80 x (1 - 0.04) = 76.8. Rejected because DOE's own example (81 to 77.5) is additive in points.
- Treating the wrong webinar (May 29, 2025 in D05, or December 19, 2022 in D01) does not match "the proposal to create TE2"; the May 2025 date would give 81 percent and 77.0; the December 2022 date still gives 80 percent and 76.0.

gaps:
- The packet does not contain the February 2022 NOPR or the June 2023 Final Rule themselves, so the actual appendix B TE2 formula is not available; the answer relies on DOE's stated estimates and additive arithmetic in D03/D04, which is what the question asks for ("by DOE's estimates").
- Whether jacket loss percentage would differ at reduced input rate is not addressed in the packet; DOE's estimate treats it as a flat ~2.5-point effect.
- Coverage: D03 and D04 read in full. D02 read lines 78-227 (background, standards, test procedure, NEEA discussion); remainder covered by keyword search only. D05 read lines 1-36 and 80-204. D01, D06, D07 read headers only plus keyword searches (webinar, NEEA, TE2, jacket, part-load, 75 percent, thermal efficiency, warm air furnace, 80/81 percent, January 1, 2023); they are a consumer-furnace preliminary TSD notice, a CRA certification-rule rescission, and an analytic-methods RFI, with no relevant CWAF figures found. One D01 line containing "75 percent" (line 211) was an omitted long line that I did not view; D01 concerns consumer furnaces, so it should not affect the answer.
- Docs folder originals were not opened separately; the text/ files are plain-text Federal Register extractions with no charts or tables at issue.

contaminated: no
