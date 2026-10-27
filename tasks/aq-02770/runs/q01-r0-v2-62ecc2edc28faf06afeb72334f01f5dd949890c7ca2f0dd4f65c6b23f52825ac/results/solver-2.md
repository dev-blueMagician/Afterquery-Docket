# q01 rev 0 - removal probe, packet solver-2 (Doc 2 left out, documents renumbered D01-D06)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-10. Packet: a copy of the prepared corpus
without docs/fr_2022_27878.txt (Doc 2), ids renumbered contiguously (packet D02 = Doc 3, D03 = Doc 4,
D04 = Doc 5, D05 = Doc 6, D06 = Doc 7). Prompt: workspace root, packet path, the exact question, and a
request for a forced guess with probability and source. Optional diagnostic for one concrete issue: whether
Doc 2's input (the compliance date of the 81 percent standard) is recalled when the document is absent.
tested_sha256 62ecc2edc28faf06afeb72334f01f5dd949890c7ca2f0dd4f65c6b23f52825ac. Not a platform result.

answer: Not answerable from the packet as worded. One input is not settled: the federal minimum thermal efficiency that applied to a gas-fired CWAF built in 2022. The packet says the standard "went from 80 to 81 percent" under the January 15, 2016 direct final rule, but never gives the date compliance with 81 percent began. Everything else is settled and gives a 4.0-point reduction from TE, so the answer is 76.0 if the 2022 minimum was 80 percent, or 77.0 if it was 81 percent.

confidence: high on the 4.0-point reduction; low on which base applies, because the documents do not say.

path:
1. NEEA's largest part-load share is 75 percent. D03 (final determination, 90 FR 5565, text line 187): "modeling submitted by NEEA that showed a range of times for CWAF operation at full and part loads, from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)."
2. DOE's part-load estimate is 2 points at the reduced rate, which becomes 1 point at the adopted 50 percent weighting. D02 (December 2024 NOTD, 89 FR 104863-64, lines 164-168): "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit... when accounting for the weighting of 50 percent of time operating at the reduced input rate."
3. DOE's jacket-loss estimate is about 2.5 points. D02 (line 158): "jacket loss factor of 3.3... a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses." (0.75 x 3.3 = 2.475.)
4. DOE's low case combines both, in percentage points. D02 (line 144): "between 3.5 percent lower (in a model with high jacket loss and poor part-load performance) to 1 percent higher"; D02 (line 176) and D03 (line 143): "a CWAF with a TE of 81 percent... actual range of efficiencies from 77.5 to 82 percent." So 81 - 2.5 - 1.0 = 77.5.
5. Reweighting part load at 75 percent: 0.75 x 2 = 1.5 points. Total low-case reduction = 2.5 + 1.5 = 4.0 points (4.0 to one decimal even using 2.475).
6. Federal minimum: D02 (line 144) and D03 (line 184): "when DOE last amended the standards for gas-fired CWAFs, the minimum required efficiency went from 80 to 81 percent... 81 FR 2420, 2430." D02 footnote 3 dates that rule: "On January 15, 2016, DOE published a direct final rule amending energy conservation standards for... CWAFs."
7. Result: 80 - 4.0 = 76.0, or 81 - 4.0 = 77.0. With unrounded jacket loss these are 76.025 and 77.025, the same at one decimal.

minimal_documents: D02 + D03 give the 4.0-point reduction and the 80/81 pair. D03 alone nearly suffices, since it has NEEA's 75 percent, the 50 percent weighting, the 2.5 jacket figure, 77.5 to 82 for an 81 percent unit, and 80 to 81; the 2-point part-load figure can be back-calculated from it. No document in the packet supplies the 2022 minimum.

readings:
- 81 percent base (treating the 2016 amendment as in force by 2022, or reading "federal minimum" as the current standard DOE uses in its example): 77.0.
- 80 percent base (the amended standard not yet requiring compliance in 2022): 76.0.
- Relative-percent reading (80 x 0.96 = 76.8; 81 x 0.96 = 77.8): rejected, because DOE's own 81 to 77.5 example uses percentage points.

gaps:
- Missing fact: the compliance date of the 81 percent gas-fired CWAF standard. I searched all six text files for "January 1, 20", "2023", "compliance date", "manufactured on", "80 percent", "81 percent" and "thermal efficiency"; none ties a date to the 81 percent standard.
- D01's long compliance lags for consumer furnaces (a 2007 rule with 2015 compliance) show that a 2016 publication date does not imply 2022 applicability.
- D01 covers consumer furnaces only (weatherized gas furnaces at 81 percent AFUE); it is not a CWAF standard.
- D05 mentions CWAFs only in certification lists; D06 has no CWAF or TE2 content, and NEEA appears there only as a commenter on another docket.
- Coverage: D02, D03 and D04 read in full; D01 read to line 359; D05 and D06 covered by targeted searches only.
- I did not open question.txt in the packet root, or anything outside text/ and docs/.

contaminated: no

Files used:
- ...\solver-2\text\D02.txt
- ...\solver-2\text\D03.txt

forced_guess: 76.0, p=0.65, source: memory (only for the unsettled input — my recollection is that 81 percent applies to units manufactured from January 1, 2023, so a 2022 unit was held to 80 percent; the 4.0-point reduction is from the documents)

Caller's reading: unforced answer misses (not answerable; 76.0 or 77.0). The forced guess reaches the gold by
recall of the January 1, 2023 compliance date at p 0.65: a stated risk under the removal-probe rule, and high
enough that a fair change was sought. Rev 1 replaces "built in 2022" with a document-only anchor (the day
DOE published its final determination not to amend the standards), so that the manufacture date as well as
the compliance date must come from Doc 2.
