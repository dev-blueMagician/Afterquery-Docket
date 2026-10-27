# q01 rev 0 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-10. Packet: the prepared corpus, D01-D07.
Prompt: workspace root, packet path and the exact question only. Optional diagnostic for one concrete
issue: whether a fresh reader takes the question's what-if on part-load weighting the intended way.
tested_sha256 62ecc2edc28faf06afeb72334f01f5dd949890c7ca2f0dd4f65c6b23f52825ac. Not a platform result.

answer: 76.0 percent (TE2 lower bound = 80 - 2.5 - 1.5)

confidence: high (medium-high on the intended treatment of the jacket-loss figure, but both the rounded 2.5 and the unrounded 2.475 give 76.0 at one decimal)

path:
1. Federal minimum TE, gas-fired CWAF built in 2022 = 80 percent. D02 (87 FR 78821, Dec. 23, 2022 final determination), sec. II.B, text line 135-136: "for gas-fired CWAFs manufactured starting on January 1, 1994, until January 1, 2023, TE at the maximum rated capacity (i.e., rated maximum input) must be not less than 80 percent. For gas-fired CWAFs manufactured starting on January 1, 2023, the TE ... must be not less than 81 percent." So a 2022-built unit is at 80, not 81.
2. DOE's low-end estimate and its components. D03 (89 FR 104859, Dec. 26, 2024 NOTD), sec. II.C, line 144: "the test procedure for TE2 could produce a result that is between 3.5 percent lower (in a model with high jacket loss and poor part-load performance) to 1 percent higher ... than the industry test procedure". Line 176: "a CWAF with a TE of 81 percent ... could ... have an actual range of efficiencies from 77.5 to 82 percent" (so DOE's "percent" are percentage points, applied additively).
3. Jacket-loss component. D03 line 158: "a jacket loss factor of 3.3), a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses." (0.75 x 3.3 = 2.475, which DOE carries as 2.5: 3.5 = 2.5 + 1.0.) D04 line 189 repeats "as much as a 2.5 percent difference in efficiency."
4. Part-load component. D03 lines 164-168: "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate ... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate." So part-load penalty = 2 x part-load weight.
5. NEEA's largest part-load share = 75 percent. D04 (90 FR 5560, Jan. 17, 2025 final determination), sec. II.C, line 187: "DOE reviewed modeling submitted by NEEA that showed a range of times for CWAF operation at full and part loads, from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)."
6. Calculation: part-load penalty at 75 percent weighting = 2 x 0.75 = 1.5 points (check: 0.25 x 80 + 0.75 x 78 = 78.5). Jacket loss = 2.5 points. TE2 low = 80 - 2.5 - 1.5 = 76.0. With unrounded jacket loss 2.475: 76.025 -> 76.0. Sanity check against DOE's own figure: 81 - 2.5 - (2 x 0.50) = 77.5, matching the printed 77.5.

minimal_documents: D02, D03, D04.
- D02 is the only document tying the 80 percent level to units manufactured before January 1, 2023 (D03/D04 say only that the minimum "went from 80 to 81 percent" without the compliance date).
- D04 is the only document with NEEA's 30-75 percent part-load range.
- D03 gives the explicit 2-percent part-load delta, 50 percent weighting and 0.75 x 3.3 jacket derivation. Alternative: D02 + D04 alone is arguably sufficient by inference, since D04 prints 81 -> 77.5 (3.5 lower), "as much as a 2.5 percent difference" from jacket loss, and "the 50 percent weighting at full load and part load", which implies 1.0 point of part-load penalty at 50 percent, hence 1.5 at 75 percent.

readings:
- Keeping DOE's adopted 50 percent weighting (ignoring the NEEA condition): 80 - 3.5 = 76.5.
- Using the post-2023 standard of 81 (misreading the build year): 81 - 2.5 - 1.5 = 77.0.
- Treating the "2 percent" part-load drop as relative rather than percentage points: part-load efficiency 78.4, weighted 78.8, less 2.5 = 76.3 (less 2.475 = 76.3). Not preferred, because DOE's own arithmetic (2 -> 1 at 50 percent; 81 -> 77.5) is additive in points.
- Misusing the "4.5 percent difference" (D04 line 184, which is the high-to-low spread, not the drop below TE): 75.5. Not defensible.
- Using NEEA's smallest part-load share (30 percent): 80 - 2.5 - 0.6 = 76.9; the question asks for the largest share, so not applicable.

gaps:
- The packet does not contain the appendix B TE2 formula itself (June 2023 Final Rule, 88 FR 36217); the result rests on DOE's stated estimates in D03/D04, as the question's "by DOE's estimates" indicates. In particular, the packet gives no basis for treating jacket loss differently at part load, so I held it at 2.5.
- D05 (90 FR 20909, May 16, 2025 proposed rescission of appendix B), line 117, states a tentative view that DOE "overestimated the impacts of jacket losses and part-load operation on CWAF energy use" but supplies no replacement figures; it does not change the calculation.
- Coverage: D03 and D04 read in full; D02 read lines 60-239 (synopsis through sec. III.D.2) plus keyword hits elsewhere; D05 read lines 1-135; D01 (consumer furnaces NOPR), D06 (certification/enforcement CRA rescission) and D07 (analytic methods proposal) were only header-read and keyword-searched (TE2, NEEA, jacket loss, part load, warm air furnace, 75/80/81 percent, January 1, 2023) with no relevant hits beyond an unrelated 75 percent AFUE mention (D01), a 5 percent enforcement tolerance row (D06) and commenter-list entries (D07). No PDFs or layout files exist in this packet (all sources are text), so no page inspection was needed.
- Environment note: the session working directory was .../solver-2 while the packet path supplied was .../solver-1; I read only D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-02770\runs\q01-r0-v2-62ecc2edc28faf06afeb72334f01f5dd949890c7ca2f0dd4f65c6b23f52825ac\solver-1\text\ (manifest.json, D01-D07.txt). A question.txt exists at that packet root and was not opened.

contaminated: no (inputs were workspace root, packet path and question only; an auto-attached git-status listing of workspace file names was visible but contained no answer, reasoning or source hint for this question)

Caller's note: the working directory at launch was the solver-2 packet (the caller's shell had been left there
after rebuilding it). The agent reports reading solver-1 only, so the removed-document packet did not shape
this solve; recorded here because it departs from a clean launch.
