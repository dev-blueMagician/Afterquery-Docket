# q01 rev 0 - blind solve, packet solver-1 (all seven documents)

Raw return of the blind-solver agent, 2026-10-10. Prompt: workspace root, packet path and the exact
question only. tested_sha256 711d7c9dca349cb3240f2cced5b227170e9675437428c74000a564ce7690c933.

answer: About $45,708 in total. That is one significant new use notice (SNUN) at the large-business estimate of $45,496, plus two one-time export notifications at about $106 each ($212), for the two non-FEOC destinations, Korea and Japan. The Polish firm is a FEOC, so there is no export to it and no notice for Poland.

confidence: high (medium on the Japanese firm, which turns on one clarification in the final DOE guidance)

path:
1. D07 (EPA proposed SNURs, 91 FR 22075, Apr 24 2026), proposed 721.12219(a)(2)(iii) and 721.12220(a)(2)(iii): "It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%." Controls at 90% are below 99%, so reclaiming is a significant new use. Unit II.A: "A SNUN is required prior to any significant new use."
2. D07 Unit I.D.1: "costs are an estimated $45,496 per SNUN submission for large business submitters and $14,976 for small business submitters. These estimates include the cost to prepare and submit the SNUN (including registration for EPA's Central Data Exchange (CDX)), and the payment of a user fee." A large recycler handling one covered oxide files one SNUN: $45,496, with the $37,000 fee already inside that figure.
3. D07 Unit I.D.2: "For persons exporting a substance that is the subject of a SNUR, a one-time notice to EPA must be provided for the first export or intended export to a particular country... the estimated cost of the export notification requirement on a per unit basis is approximately $106." So the cost is $106 per destination country.
4. The FEOC test comes from D04 (DOE final interpretive rule, 89 FR 37079, effective May 6 2024). Section V.A: an entity is a FEOC if it is a "foreign entity" and is either "subject to the jurisdiction" of a covered nation government or "owned by, controlled by, or subject to the direction" of one. The PRC is a covered nation (Section I). Section V.C(i): government includes "A national or subnational government of a foreign country". Section V.E(i): control exists where "25% or more of the entity's board seats, voting rights, or equity interest, with each metric evaluated independently, are cumulatively held by that other entity".
5. Polish firm, 50% owned by a Chinese city: a subnational government holds 50% of the equity, which is at least 25%. It is a FEOC and is excluded.
6. Korean subsidiary of a private Shanghai company: the parent is a FEOC only by jurisdiction. D04 III.D: "subsidiaries of the FEOC are not automatically considered to be FEOCs themselves based solely on their parent being a covered nation jurisdictional entity." D04 III.E.i: DOE "would not factor in any voting share, equity interest, or board seats held by an entity that is a FEOC solely by virtue of being subject to the covered nation's jurisdiction." The subsidiary is in Korea and has no government stake, so it is not a FEOC. Export notice for Korea: $106.
7. Japanese firm, province names two of five directors holding 20% of board votes: D04 II.E response: "For ``board seats,'' DOE intends for the value of a board seat to equal the value of its voting power on the board. So, if one board seat is held by a representative of the government of a covered nation and that seat holds 25% of the board voting power, then that entity would be considered a controlled FEOC." The measure is therefore 20% voting power, not 40% of seats. That is under 25%, with no other metric given, so it is not a FEOC. Export notice for Japan: $106.
8. Calculation: $45,496 + $106 + $106 = $45,708.

minimal_documents: D07 and D04. D02 (the December 2023 proposed DOE interpretation) cannot replace D04. It has the 25% test, subnational governments and the jurisdiction-only-holder exclusion, but not the board-seat voting-power clarification; its only "voting power" hits are statutory citations about stock. On D02 alone a seat count would make the Japanese firm 40% and a FEOC.

readings:
- Counting seats rather than voting power (the D02 or naive reading) makes the Japanese firm a FEOC, leaving one notice: $45,496 + $106 = $45,602.
- Treating "notifying EPA" as export notices only gives $212; I rejected this because the SNUN is itself the required notice to EPA.
- Notifying all three countries regardless of FEOC status gives $45,814; this contradicts the question's "non-FEOC" limit.
- D07's Regulatory Flexibility section prints the small-business total as "$14,967" against "$14,976" in Unit I.D.1. This does not matter for a large recycler.

gaps:
- The $106 is described as "approximately" and the SNUN figure as an estimate "as they are known at the time of this rulemaking"; a final rule could restate them.
- The FEOC classifications assume "no other relevant circumstances": no production inside China, no effective-control licence or contract with a FEOC, and no senior-political-figure holdings in the private Shanghai parent.
- Coverage: D07 and D04 were read in full. D02 was keyword-searched only (board seats, voting power, subnational). D01 (EPA 2022 battery-recycling request for information), D03 (TVA Kingston record of decision), D05 (Treasury regulatory agenda) and D06 (EPA lead wheel weights petition decision) were keyword-searched only. They returned no hits for SNUN, export notification or the cost figures; D05 mentions FEOC only in a Section 30D agenda entry.
- I read the packet at the solver-1 path given in the task, although the session's working directory was solver-2.

contaminated: no
