# q01 rev 1 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent (claude-opus-5-5), 2026-10-10. Packet: the prepared corpus, D01-D07.
Prompt: workspace root, packet path and the exact question only, launched from the workspace root. Optional
diagnostic for one concrete issue: whether a fresh reader dates "that day" by the publication date and not
by the effective date or by Doc 4's final determination.
tested_sha256 7df56a5808a063c37449b13f37f397ba1f653c787e02ba4d8958ff137d8db930. Not a platform result.

answer: 76.0 percent (TE2)

confidence: high

path:
1. The determination is D02 (87 FR 78821), published Friday, December 23, 2022. Header: "Federal Register Volume 87, Number 246 (Friday, December 23, 2022)"; ACTION: "Final determination."; "DOE has determined not to amend the energy conservation standards for CWAFs." Its effective date is different: "effective January 23, 2023."
2. Federal minimum for a gas-fired unit built on December 23, 2022 is 80 percent. D02, p. 78823: "for gas-fired CWAFs manufactured starting on January 1, 1994, until January 1, 2023, TE at the maximum rated capacity (i.e., rated maximum input) must be not less than 80 percent. For gas-fired CWAFs manufactured starting on January 1, 2023, the TE at the maximum rated capacity must be not less than 81 percent."
3. DOE's jacket-loss estimate is about 2.5 points. D03 (89 FR 104859), p. 104863: "which have a jacket loss factor of 3.3), a jacket loss of 0.75 percent could result in a difference of nearly 2.5 percent as compared to a unit with negligible jacket losses." (0.75 x 3.3 = 2.475.)
4. DOE's part-load estimate is up to 2 points at the reduced rate, which gives 1 point at 50 percent weighting. D03, pp. 104863-104864: "the efficiency when operating at the reduced input rate can be as much as 2 percent higher or lower than the efficiency when operating at the maximum input rate ... the resulting difference in TE2 would be 1 percent higher or lower than the TE of that unit ... when accounting for the weighting of 50 percent of time operating at the reduced input rate."
5. DOE treats these as additive percentage points. D03, p. 104863: "between 3.5 percent lower (in a model with high jacket loss and poor part-load performance) to 1 percent higher"; D03, p. 104864: "a CWAF with a TE of 81 percent ... could ... have an actual range of efficiencies from 77.5 to 82 percent" (81 - 2.5 - 1.0 = 77.5).
6. NEEA's largest part-load share is 75 percent. D04 (90 FR 5560), p. 5565: "modeling submitted by NEEA that showed a range of times for CWAF operation at full and part loads, from operating as much as 70 percent of the time at full load (and 30 percent of the time at part load) to operating as little as 25 percent of the time at full load (and 75 percent at part load)."
7. Calculation:
   - Part-load penalty at 75 percent weighting: 2 x 0.75 = 1.5 points (versus 2 x 0.50 = 1.0 in DOE's base case).
   - Jacket penalty: 2.5 points (2.475 unrounded).
   - Lowest TE2: 80 - 2.5 - 1.5 = 76.0. With the unrounded jacket figure, 80 - 2.475 - 1.5 = 76.025, which also rounds to 76.0.

minimal_documents: D02 + D03 + D04.
- D02 is irreplaceable: only it gives the publication date and the January 1, 2023 switch from 80 to 81 percent.
- D04 is irreplaceable: only it gives NEEA's 30 to 75 percent part-load range.
- D03 could arguably be dropped. D04 repeats the "77.5 to 82" range, the 4.5-point spread, the 2.5-point jacket figure and the 50 percent weighting, so the 2-point part-load swing can be backed out (3.5 - 2.5 = 1.0 at 50 percent). D03 is the only place the 2-point figure and the 3.3 jacket factor are stated outright.

readings:
- "That day" taken as the effective date (January 23, 2023), or the 81 percent standard applied: 81 - 4.0 = 77.0. I rejected this because the question says "published".
- "Final determination" taken as D04 (January 17, 2025): 77.0. I rejected this because D04 concerns the test procedure, not a decision not to amend standards.
- Percentages applied as relative rather than points: 80 x 0.96 = 76.8. This is inconsistent with DOE's own 81 to 77.5.
- DOE's 50 percent weighting left unchanged: 76.5. This ignores the question's condition.

gaps:
- The 75 percent weighting is my extrapolation of DOE's stated 2-point part-load difference; DOE itself only publishes the 50 percent case.
- D02, D03 and D05 were read in full. D04 was read through line 215; only the signature block remains.
- D01 (consumer furnaces preliminary TSD notice), D06 (certification rule revocation under the Congressional Review Act) and D07 (2026 request for information on analytic methods) were checked by header plus targeted searches for CWAF, TE2, NEEA, jacket loss, part load and thermal efficiency. Nothing relevant turned up. In D07, NEEA appears only in the commenter table and a footnote citation.
- No PDFs are in the packet; all sources are plain text and no extraction problems appeared.
- D05 (May 2025 proposed rule) tentatively says DOE "overestimated the impacts of jacket losses and part-load operation" and proposes removing TE2. It gives no replacement figures, so the estimates used are those in D03 and D04.

contaminated: no
