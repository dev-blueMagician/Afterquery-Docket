# q01 rev 2 - removal probe, packet solver-2 (Doc 2 left out, documents renumbered D01-D06)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-11. Packet: a copy of the prepared corpus
without docs/fr_2022_27878.txt (Doc 2), ids renumbered contiguously (packet D02 = Doc 3, D03 = Doc 4,
D04 = Doc 5, D05 = Doc 6, D06 = Doc 7). Prompt: workspace root, packet path, the exact rev 2 question, a
request for the single answer it would submit if this were the whole document set, and a forced guess with
probability and source; launched from the workspace root. Optional diagnostic for one concrete issue: with
the manufacture date now available from the TE2 documents, does a solver without Doc 2 reach the gold by
recalling the compliance date. tested_sha256 235a31a7963fdb900fe7a5efd923cfbf2fe64e9911a941ebf04b30d934118609.
Not a platform result. Rev 3 differs only in the event (the March 29, 2022 webinar instead of the February
25, 2022 proposal); both give a solver a 2022 date without Doc 2, so this probe is read for both.

answer: 77.0 percent. This is the single answer I would submit from this document set; I would not decline. It rests on one input the documents do not settle (see gaps), and the other value that input allows is 76.0 percent.

confidence: medium

path:
1. Proposal date. D03 (90 FR 5562, I.C): "DOE subsequently published a notice of proposed rulemaking (``NOPR'') for the CWAFs test procedure in the Federal Register on February 25, 2022 ... and proposed a new metric, TE2". D02 (89 FR 104861) gives the same date. So the day is February 25, 2022.
2. Federal minimum, gas-fired. D02 (89 FR 104863) and D03 (90 FR 5565): "when DOE last amended the standards for gas-fired CWAFs, the minimum required efficiency went from 80 to 81 percent ... 81 FR 2420, 2430." D02 footnote 3: "On January 15, 2016, DOE published a direct final rule amending energy conservation standards for various types of commercial air conditioning equipment and CWAFs. 81 FR 2420." The amendment was published before February 25, 2022, so I take the minimum as 81 percent. Both notices' own example also uses "a CWAF with a TE of 81 percent".
3. Jacket loss, worst case. D02 II.C.1 (89 FR 104863): ASHRAE 90.1-2022 limits jacket losses to "0.75 percent of the input rating"; weatherized CWAFs "have a jacket loss factor of 3.3"; "a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent". Exact product: 0.75 x 3.3 = 2.475.
4. Part-load, worst case. D02 II.C.2 (89 FR 104863-104864): "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate"; "the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate." So the penalty is 2 x the part-load weight.
5. NEEA's largest part-load share. D03 II.C (90 FR 5565): NEEA modeling ran "from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)." The largest part-load share is 75 percent.
6. Method check. D02's printed range for TE 81 is "from 77.5 to 82 percent": 81 - 2.5 - (0.50 x 2) = 77.5 and 81 + 1 = 82, so the losses are additive in percentage points.
7. Calculation. Part-load penalty at 75 percent: 0.75 x 2 = 1.5. Lowest TE2 = 81 - 2.5 - 1.5 = 77.0. With the exact jacket product: 81 - 2.475 - 1.5 = 77.025, which also rounds to 77.0.

minimal_documents: D02 and D03.
- D03 is the only source of the NEEA 30/75 percent range.
- D02 is the only source of the 2 percent part-load figure, the 0.75 percent x 3.3 jacket derivation and the January 15, 2016 date.
- D03 alone nearly suffices, by backing 2.5 and 1 out of its "77.5 to 82" range and its "as much as a 2.5 percent difference" for jacket losses, but it never states the 2 percent part-load figure or the 50 percent to 1 percent link explicitly.
- D01 (consumer furnaces, AFUE), D04 (2025 proposal to rescind Appendix B), D05 and D06 add nothing needed.

readings:
- A: the minimum in force for a unit built February 25, 2022 was still 80 percent, because compliance with the 81 percent standard began later. Then 80 - 2.5 - 1.5 = 76.0 (exact 76.025, still 76.0). The documents neither support nor exclude this.
- B: "largest share" misread as the 70 percent full-load figure, giving 30 percent part load: 81 - 2.5 - 0.6 = 77.9. I reject this; the question asks for part load's largest share.
- C: DOE's own 50 percent weighting gives 77.5. I reject this; the question changes the weighting.

gaps:
- The unsettled input is the compliance date of the 81 percent gas-fired CWAF standard. The packet gives only the amending rule's publication date (January 15, 2016) and that the minimum "went from 80 to 81 percent". It never says from what manufacture date 81 percent applied, so it does not strictly establish whether a furnace built on February 25, 2022 faced 81 or 80.
- The packet itself shows compliance can lag publication by years: D01 describes a 2007 consumer-furnace rule with compliance in November 2015.
- From memory only, not from the documents: I believe the 2016 rule's CWAF compliance date was January 1, 2023. If so, the real-world minimum on February 25, 2022 was 80 percent and the answer would be 76.0. If the gold is 77.0, the question's premise may be factually vulnerable; if the gold is 76.0, it is not derivable from this packet.
- Coverage: D01 to D04 read in full. D05 and D06 were only header-read and keyword-searched (CWAF, warm air furnace, furnace, thermal efficiency, part load, jacket, NEEA, weighting, 2023, compliance date, gas-fired); neither has CWAF standard content. The files in docs/ are plain text mirrored in text/; there were no PDF pages to inspect.

contaminated: no

forced_guess: 77.0, p=0.65, source: inference from the documents

Caller's reading: asked to commit, the solver without Doc 2 submitted 77.0, the wrong-year answer, by
inference from the remaining documents; a miss under the platform's rule ("the answer without it is wrong").
It knew the true compliance date from memory and named 76.0 as the alternative, so the recall route exists
and is a stated risk: a solver that prefers its memory to the documents' silence reaches the gold. Compare
rev 0 ("built in 2022"), where the same role, asked only for a forced guess, chose 76.0 from memory at p 0.65.
