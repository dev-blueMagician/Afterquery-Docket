# q02 rev 0 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent, 2026-10-10. Prompt: workspace root, packet path and the exact
question only. tested_sha256 1f910fbd56b1e0fa3cbb689936856d5edc1c4dc4fa8784c0222074b16449ca1c.

answer: $45,920 — one large-business SNUN at $45,496 plus four export notifications at about $106 each ($424).

confidence: medium-high. The arithmetic and the EPA facts are firm. The one judgement call is treating the Chinese city's convertible notes as a "contingent equity interest", which makes the Thai buyer a FEOC.

path:
1. D07 (EPA proposed SNUR 26-2, 91 FR 22075, Apr 24 2026) covers two substances, 40 CFR 721.12219 and 721.12220, both "Cobalt lithium manganese nickel oxide, metals-doped (generic)". These are the two "covered oxides".
2. D07 reg text (a)(2)(iii), identical for both sections: "It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%."
   - The oxide reclaimed at 90% is a significant new use, so a SNUN is required.
   - The oxide reclaimed at 99% meets the minimum, so no SNUN.
3. D07 Unit I.D.1: "costs are an estimated $45,496 per SNUN submission for large business submitters and $14,976 for small business submitters. These estimates include the cost to prepare and submit the SNUN ... and the payment of a user fee." A large recycler filing one SNUN pays $45,496.
4. D07 Unit I.D.2: "a one-time notice to EPA must be provided for the first export or intended export to a particular country. The total costs of export notification will vary by chemical, depending on the number of required notifications (i.e., the number of countries to which the chemical is exported) ... the estimated cost of the export notification requirement on a per unit basis is approximately $106."
   - Notices are counted per chemical per country, so the two Japanese buyers count as one country.
5. FEOC test for the Thai buyer, from D04 (DOE final interpretive rule, 89 FR 37079, May 6 2024):
   - Covered nations include "the People's Republic of China (PRC)" (Sec. I).
   - "Government of a foreign country" means "(i) A national or subnational government of a foreign country" (Sec. V.C), so a Chinese city qualifies.
   - Control exists if "25% or more of the entity's board seats, voting rights, or equity interest, with each metric evaluated independently, are cumulatively held" (Sec. V.E(i)).
   - Sec. II.E response: "For 'equity interests,' DOE intends to refer to percent value of the ownership interest, to include capital or profit interests and contingent equity interests ... with the amount of contingent interest that can be reasonably determined included for the purpose of determining FEOC compliance."
   - Sec. III.E.i: "the amount of the contingent interest that can be reasonably determined ... should be included in the 25% control calculation, without consideration of whether conversion is imminent or within the control of the equity-owning entity."
   - Equity interest is therefore 10% held + 20% convertible = 30%, which is at or above 25%. The Thai buyer is a FEOC and, "barring FEOCs", receives no export and triggers no notice.
6. Export notices: 2 oxides x 2 countries (Japan, Chile) = 4. 4 x $106 = $424.
7. Total: $45,496 + $424 = $45,920.

minimal_documents: D07 and D04.
- D07 alone supplies every EPA cost and the 99% trigger.
- D04 is needed for the FEOC call. D02 (the Dec 2023 proposed interpretive rule) cannot replace it: it has the 25% threshold but no mention of "contingent" or "convertible" interests, so it would lead to the 10% / not-FEOC result.

readings:
- Convertible notes not counted (D02-only, or notes treated as plain debt): Thai buyer at 10% is not a FEOC, giving 5 notices ($530) and a total of $46,026. Rejected because the final D04 guidance includes contingent equity "without consideration of whether conversion is imminent."
- Notices per buyer rather than per country: 6 notices ($636), total $46,132. Rejected by "to a particular country."
- Notices per country regardless of chemical: 2 notices ($212), total $45,708. Rejected by "will vary by chemical."
- SNUN for both oxides: $90,992 + $424 = $91,416. Rejected because 99% satisfies the "minimum ... 99%" condition.
- User fee only ($37,000) instead of the full submission cost: $37,424. Weaker, because the question asks what notifying would cost and D07 gives $45,496 as the per-submission cost.

gaps:
- D04 says "contingent equity interests" is a defined term in 31 CFR 800.207, but the packet does not reproduce that definition. Classing convertible notes as contingent equity rests on ordinary meaning and on D04's own word "conversion".
- D04's FEOC interpretation is written for BIL 40207 / IRC 30D, not TSCA. I applied it only to decide which buyers the recycler excludes.
- The $106 figure is stated as "approximately".
- D07 states the small-business SNUN cost inconsistently ($14,976 in Unit I.D vs $14,967 in Unit IV.D); this does not affect a large business.
- Coverage: D07 and D04 were read in full. D01 (EPA battery-recycling RFI), D02, D03 (TVA Kingston record of decision), D05 (Treasury regulatory agenda) and D06 (EPA lead wheel weights petition) were checked by targeted searches only (SNUN, export notification, $106, FEOC, contingent/convertible, Japan/Chile/Thai, cobalt). None returned competing cost figures or definitions. No original PDFs were needed; the sources are plain text.
- The packet's question.txt and everything outside text/ and docs/ were not read.

contaminated: no. Input was only the workspace root, packet path and question; no answer, reasoning, lever or source hint was supplied.
