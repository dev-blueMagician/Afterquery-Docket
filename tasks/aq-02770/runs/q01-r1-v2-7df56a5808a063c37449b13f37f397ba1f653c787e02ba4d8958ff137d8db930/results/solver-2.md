# q01 rev 1 - removal probe, packet solver-2 (Doc 2 left out, documents renumbered D01-D06)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-10. Packet: a copy of the prepared corpus
without docs/fr_2022_27878.txt (Doc 2), ids renumbered contiguously (packet D02 = Doc 3, D03 = Doc 4,
D04 = Doc 5, D05 = Doc 6, D06 = Doc 7). Prompt: workspace root, packet path, the exact question, and a
request for a forced guess with probability and source; launched from the workspace root. Optional
diagnostic for one concrete issue: whether the rev 1 date anchor removes the recall route that rev 0's
probe found. tested_sha256 7df56a5808a063c37449b13f37f397ba1f653c787e02ba4d8958ff137d8db930. Not a platform result.

answer: Not answerable from this packet as posed. Two inputs are not settled by any document here: (a) the publication date of a DOE final determination not to amend commercial warm air furnace (CWAF) energy conservation standards, and (b) the federal minimum thermal efficiency for a gas-fired CWAF manufactured on that date. Everything else is settled: TE2 could be 4.0 percentage points below TE. That gives 77.0 percent if the 81 percent minimum applied that day, or 76.0 percent if the 80 percent minimum applied.

confidence: high on the 4.0-point reduction; low on which base applies, since the packet cannot settle it.

path:
1. Jacket loss (D02, II.C.1, FR p. 104863): "a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses" (jacket loss factor 3.3; 0.75 x 3.3 = 2.475). D03 II.C repeats "as much as a 2.5 percent difference in efficiency."
2. Part-load swing (D02, II.C.2, pp. 104863-104864): "efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate ... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate."
3. DOE's combined estimate (D02 p. 104863): "between 3.5 percent lower (in a model with high jacket loss and poor part-load performance) to 1 percent higher." D02 III and D03 III: "a CWAF with a TE of 81 percent ... could ... have an actual range of efficiencies from 77.5 to 82 percent." So DOE treats these as percentage points: 81 - 2.5 - 1.0 = 77.5.
4. NEEA modeling (D03, II.C, FR p. 5565): "from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)." The largest part-load share is 75 percent.
5. Calculation: the part-load penalty at 75 percent weighting is 0.75 x 2 = 1.5. Adding the 2.5 jacket loss gives 4.0 below TE (3.975 with the unrounded 2.475; same result at one decimal).
6. Base TE: the packet says only "when DOE last amended the standards for gas-fired CWAFs, the minimum required efficiency went from 80 to 81 percent ... 81 FR 2420" (D02 p. 104863; D03 p. 5565). D02 footnote 3 dates that direct final rule to January 15, 2016. No document gives the compliance date of the 81 percent level.
7. Result: 81 - 4.0 = 77.0, or 80 - 4.0 = 76.0.

minimal_documents: For the 4.0-point reduction, D03 alone is enough (77.5 to 82 range on 81, 2.5 jacket, 50 percent weighting, NEEA 25/75; the part-load swing of 1.0 at 50 percent follows from 3.5 - 2.5). D02 plus D03 gives the plus or minus 2 percent figure explicitly. A complete answer also needs a document not in this packet: the CWAF standards final determination, or another source giving its publication date and the dated gas-fired standard levels.

readings:
- If "final determination" is taken loosely to mean D03 ("Commercial Warm Air Furnaces; Final Determination", published January 17, 2025), the date is settled. D02 and D03 treat 81 percent as the level set by the last amendment and use it as their example, which gives 77.0. But D03 is a test-procedure determination (the industry test procedure fails EPCA; TE2 effective date confirmed), not a determination not to amend standards, so this conflicts with the question's premise.
- If the determination predates compliance with the 81 percent level, the base is 80 and the answer is 76.0.
- Using unrounded jacket loss gives 77.025 or 76.025, which round to the same values.

gaps:
- No document in the packet is a final determination not to amend CWAF standards. The phrase "final determination not to amend standards" appears only as generic statutory text in D01 (consumer furnaces, 42 U.S.C. 6295(m)(3)(B)). D04 mentions only a "determination not to amend the test procedures."
- No CWAF standards table (10 CFR 431.77 levels with manufacture dates) appears anywhere. D05 mentions CWAFs only in certification deadline and AEDM tolerance tables.
- Coverage: D01 to D04 were read in full. D05 was read to line 140 and lines 355-394; D06 to line 120. The rest of D05 and D06 was searched by keyword only (warm air furnace, CWAF, furnace, thermal efficiency, determination, part-load, full-load, jacket, NEEA, 2022, 2023, direct final rule). The only CWAF or NEEA hits there were the D05 certification tables and NEEA as a commenter in D06.
- The directory listing showed a `question.txt` in the packet root; I did not open it.

contaminated: no

forced_guess: 77.0, p=0.75, source: inference from the documents (the 4.0-point reduction is from the documents; the 81 percent base rests on D02/D03 calling 80 to 81 the last amendment, since the packet has neither the determination date nor the 81 percent compliance date)

Caller's reading: misses unforced (not answerable) and misses forced (77.0, the declared wrong-year answer,
reached by inference from the remaining documents). The recall route of rev 0 (forced 76.0 at p 0.65 from
memory) did not reappear: without Doc 2 the solver could not date the determination. One probe by a
cautious role, not the platform's Document check.
