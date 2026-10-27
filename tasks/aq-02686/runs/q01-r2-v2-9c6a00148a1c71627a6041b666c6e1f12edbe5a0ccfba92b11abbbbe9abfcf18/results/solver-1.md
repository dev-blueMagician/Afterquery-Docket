# q01 rev 2 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent, 2026-10-10. Prompt: workspace root, packet path and the exact
question only. tested_sha256 9c6a00148a1c71627a6041b666c6e1f12edbe5a0ccfba92b11abbbbe9abfcf18.
The tested wording said "notes convertible into 20% more"; rev 3 says "another 20%" (see readings).

answer: $45,602 in total — one large-business SNUN at $45,496 plus one export notification at $106 (Thailand only; the Polish and Japanese firms are FEOCs, so nothing is exported to them).

confidence: high

path:
1. D07 (EPA proposed SNUR, 91 FR 22075, Apr 24 2026), proposed 721.12219/721.12220 (a)(2)(iii): "It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%." Reclaiming at 90% is below 99%, so it is a significant new use. Unit II.A: "A SNUN is required prior to any significant new use."
2. D07 Unit I.D.1: "costs are an estimated $45,496 per SNUN submission for large business submitters and $14,976 for small business submitters. These estimates include the cost to prepare and submit the SNUN (including registration for EPA's Central Data Exchange (CDX)), and the payment of a user fee." The $37,000 user fee is already inside $45,496, so it is not added again. One covered substance means one SNUN.
3. D07 Unit I.D.2: "a one-time notice to EPA must be provided for the first export or intended export to a particular country ... the estimated cost of the export notification requirement on a per unit basis is approximately $106." So the export cost is $106 per destination country.
4. D04 (DOE final FEOC interpretive rule, 89 FR 37079, May 6 2024), sec. V.C: government of a foreign country includes "(i) A national or subnational government of a foreign country". Sec. I lists the PRC as a covered nation. A Chinese province or city therefore counts.
5. D04 sec. V.E(i): control exists if "25% or more of the entity's board seats, voting rights, or equity interest, with each metric evaluated independently, are cumulatively held".
6. Thai firm: 15% equity is below 25%, and it is not incorporated in a covered nation. It is not a FEOC, so there is one export destination (Thailand).
7. Polish firm: D04 sec. II.E response says equity interests "include capital or profit interests and contingent equity interests ... with the amount of contingent interest that can be reasonably determined included". Sec. III.E.i adds that it "should be included in the 25% control calculation, without consideration of whether conversion is imminent or within the control of the equity-owning entity". 10% + 20% = 30%, which is at least 25%, so it is a FEOC. It stays at or above 25% even with dilution: 30/120 = 25%.
8. Japanese firm: D04 sec. II.E response says "For 'board seats,' DOE intends for the value of a board seat to equal the value of its voting power on the board. So, if one board seat is held by a representative of the government of a covered nation and that seat holds 25% of the board voting power, then that entity would be considered a controlled FEOC." Six directors with one vote plus one with two gives 8 votes; 2/8 = 25%, which meets "25% or more", so it is a FEOC.
9. Calculation: $45,496 + 1 x $106 = $45,602.

minimal_documents: D07 and D04. D02 (the December 2023 proposed FEOC rule) cannot replace D04: it has the 25% test but neither the contingent-equity nor the board-voting-power clarification. No other document carries the SNUN or export-notice costs.

readings:
- Proposed-rule or face-value reading (10% equity; 1 of 7 seats = 14.3%): all three are non-FEOCs, giving $45,496 + 3 x $106 = $45,814. I reject this because the final rule (D04) governs.
- "20% more" read as 20% above the existing 10% stake (12% in total): the Polish firm is a non-FEOC, giving $45,496 + 2 x $106 = $45,708. This is a strained reading.
- SNUN only, treating export notices as outside "notifying EPA": $45,496. D07 calls the export notice a "notice to EPA", so I include it.
- Adding the $37,000 fee on top ($82,602) double-counts and is not defensible.

gaps:
- D07 and D04 were read in full; D02 was read only for its control section (lines 104-207).
- D01 (EPA battery-recycling RFI), D03 (TVA record of decision), D05 (Treasury regulatory agenda) and D06 (EPA lead wheel weights petition) were keyword-searched only. The searches covered SNUN, FEOC, export, board seat, contingent, convertible and dollar amounts, and found nothing relevant.
- The $106 figure is stated as "approximately" and per notification.
- I assumed the Thai, Polish and Japanese firms have no covered-nation incorporation or production for the exported material; the question does not say.
- D07 prints both $14,976 and $14,967 for small businesses; this does not affect a large submitter.

contaminated: no — I received only the workspace root, packet path and question. I did not open question.txt in the packet folder, or any notes or other runs.
