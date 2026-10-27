# q01 rev 2 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-11. Packet: the prepared corpus, D01-D07.
Prompt: workspace root, packet path and the exact question only, launched from the workspace root. Optional
diagnostic for one concrete issue: whether a fresh reader identifies the event of the new anchor ("the day
DOE published its proposal to create TE2") and still finds the minimum that applied then.
tested_sha256 235a31a7963fdb900fe7a5efd923cfbf2fe64e9911a941ebf04b30d934118609. Not a platform result.

answer: 76.0 percent (TE2)

confidence: high

path:
1. Date of the TE2 proposal. D02 (87 FR 78824, section III.A): "On February 25, 2022, DOE published a NOPR in the Federal Register that proposed to update the CWAF test procedure ... and to establish a new metric--Thermal Efficiency Two (``TE2'')." D03 and D04 Background sections give the same date.
2. Federal minimum on that day. D02 (87 FR 78823): "for gas-fired CWAFs manufactured starting on January 1, 1994, until January 1, 2023, TE at the maximum rated capacity ... must be not less than 80 percent. For gas-fired CWAFs manufactured starting on January 1, 2023, the TE ... must be not less than 81 percent." February 25, 2022 falls before January 1, 2023, so the base TE is 80 percent, not 81.
3. NEEA's largest part-load share. D04 (90 FR 5565, section II.C): NEEA modeling "showed a range of times for CWAF operation at full and part loads, from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)." Largest part-load share is 75 percent.
4. DOE's jacket-loss estimate. D03 (89 FR 104863, II.C.1): "a jacket loss factor of 3.3 ... a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses." (0.75 x 3.3 = 2.475.)
5. DOE's part-load estimate. D03 (89 FR 104863-104864, II.C.2): "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate ... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate."
6. The differences are percentage points, and DOE's own combined low case is 3.5 below TE. D03: "between 3.5 percent lower (in a model with high jacket loss and poor part-load performance) to 1 percent higher"; "a CWAF with a TE of 81 percent ... could ... have an actual range of efficiencies from 77.5 to 82 percent." Check: 81 - 2.5 - (0.50 x 2) = 77.5.
7. Calculation at 75 percent part-load weighting, base 80:
   - Part-load penalty: 0.75 x 2 = 1.5 points (versus 1.0 at 50 percent).
   - Jacket penalty: 2.5 points.
   - TE2 low = 80 - 2.5 - 1.5 = 76.0.
   - With the unrounded jacket figure: 80 - 2.475 - 1.5 = 76.025, which also rounds to 76.0.

minimal_documents: D02, D03, D04.
- D02 supplies the proposal date and the 80/81 percent changeover on January 1, 2023. D03 and D04 mention "from 80 to 81 percent" but not the changeover date, so D02 is needed.
- D04 is the only document with the NEEA 25/75 split.
- D03 is the only document stating the 2-point part-load efficiency swing and 50 percent weighting explicitly.
- Possible replacement: D02 + D04 alone, by inference. D04 gives jacket loss "as much as a 2.5 percent difference" and 81 to 77.5 (3.5 lower), implying 1.0 point from part load at "the 50 percent weighting at full load and part load", hence 2 points unweighted. This is less direct than D03.

readings:
- Base of 81 percent (ignoring that the 81 percent standard only applied from January 1, 2023): 81 - 4.0 = 77.0.
- Keeping DOE's adopted 50 percent weighting with base 80: 80 - 3.5 = 76.5.
- DOE's printed figure with neither adjustment (81 base, 50 percent weighting): 77.5.
- I consider 76.0 the only reading that honours both conditions in the question.

gaps:
- The packet does not contain the actual appendix B TE2 formula. The answer relies on DOE's simplified estimates and assumes the jacket-loss deduction is unaffected by the full/part-load weighting; DOE presents it as a separate deduction.
- "Nearly 2.5 percent" is a rounded figure, but this does not change the answer at one decimal place.
- Coverage: D01 through D05 were read in full. D01 concerns consumer furnaces and is irrelevant. D06 (certification rule rescission) and D07 (analytic methods RFI) were only keyword-searched and header-checked; D06 has only incidental CWAF mentions (certification dates) and D07 has no CWAF, TE2, part-load or jacket-loss hits beyond a NEEA commenter listing.
- No PDFs are in the packet; all documents are text extractions and no extraction problems affected the decisive passages.
- I did not read the question.txt file in the packet folder.

contaminated: no

Caller's note: this solver took the proposal date from Doc 2's own TE2 paragraph (III.A), not from Doc 3 or
Doc 4, so for it the anchor still led into Doc 2, one section away from the date rule. The anchor is less
tied than rev 1's, not untied.
