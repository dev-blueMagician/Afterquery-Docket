# q01 rev 0 - removal probe, packet solver-2 (Doc 4 left out, documents renumbered D01-D06)

Raw return of the blind-solver agent, 2026-10-10. Packet: a copy of the prepared corpus without
docs/fr_2024_08913.txt (Doc 4), ids renumbered contiguously (packet D04 = Doc 5, D05 = Doc 6, D06 = Doc 7).
Prompt: workspace root, packet path, the exact question, and a request for a forced guess with probability.
tested_sha256 711d7c9dca349cb3240f2cced5b227170e9675437428c74000a564ce7690c933.

answer: $45,602 in total: one large-business SNUN at $45,496 plus one export notification at $106 (only the Korean subsidiary is a non-FEOC prospect, so one destination country).

forced_guess: $45,602 — probability about 0.85

confidence: high on the two cost figures and the SNUN trigger; medium-high on the one-country count.

path:
1. The rule and substance (D06, 91 FR 22075, Apr 24 2026, proposed SNURs 26-2). The covered substances are "Cobalt lithium manganese nickel oxide, metals-doped (generic)" at proposed 40 CFR 721.12219 and 721.12220. "A covered oxide" is one substance, so one SNUN.
2. The SNUN trigger (D06 Sec. 721.12219(a)(2)(iii), identical in 721.12220): "It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%."
   - Reclaiming at 90% is below 99%, so it is a significant new use.
   - D06 Unit II.A: "A SNUN is required prior to any significant new use."
   - The article exemption does not help: "The article exemption applies unless/until the article has been shredded or processed such that dust is generated."
3. SNUN cost (D06 Unit I.D.1): "costs are an estimated $45,496 per SNUN submission for large business submitters and $14,976 for small business submitters. These estimates include the cost to prepare and submit the SNUN ... and the payment of a user fee." A large recycler pays $45,496.
4. Export notification cost (D06 Unit I.D.2): "a one-time notice to EPA must be provided for the first export or intended export to a particular country ... the estimated cost of the export notification requirement on a per unit basis is approximately $106." The cost is therefore $106 per destination country.
5. FEOC test (D02, 88 FR 84082, DOE proposed interpretive rule, Dec 4 2023):
   - Covered nations include the PRC (Sec. A).
   - "Government of a foreign country" includes "A national or subnational government" (B.II), so a Chinese city or province qualifies.
   - Control exists if "25% or more of the entity's board seats, voting rights, or equity interest are cumulatively held by that other entity" (B.IV(i)); the three measures are alternatives.
   - "Subject to the jurisdiction" covers an entity "incorporated or domiciled in, or has its principal place of business in, a covered nation" (B.III).
   - C.III: "subsidiaries of the FEOC are not automatically considered to also be FEOCs solely based on their parent being a covered nation jurisdictional entity."
   - C.IV.a: "DOE's interpretation would not factor in any voting share, equity interest, or board seats held by an entity that is a FEOC solely by virtue of being subject to the covered nation's jurisdiction."
6. Classification of the three prospects:
   - Polish firm, 50% owned by a Chinese city: a subnational PRC government holds 50% equity, which is at least 25%. FEOC, excluded.
   - Korean subsidiary of a private Shanghai company: the parent is a FEOC only through jurisdiction (private, incorporated in China). That status does not pass to the subsidiary, and the parent's holdings are not counted as government control. Not a FEOC, so this is an export destination.
   - Japanese firm where a Chinese province picks two of five directors: board seats are 2/5 = 40%, which is at least 25%, even though voting rights are only 20%. FEOC, excluded.
7. Calculation: one destination country (Korea) gives 1 x $106 = $106. Total = $45,496 + $106 = $45,602.

minimal_documents: D06 and D02. No substitute exists in the packet: D04 only cross-references the statutory FEOC definition (42 U.S.C. 18741(a)(5)) with no tests, and D01, D03 and D05 are irrelevant to this question.

readings:
- Japanese firm judged on the 20% voting figure alone (ignoring the 40% of board seats): two destination countries, $45,496 + $212 = $45,708. I reject this because the D02 test is disjunctive.
- "Notifying EPA" read as the SNUN only: $45,496. Read as export notices only: $106. "Altogether" favours the sum.
- "Korean" read as North Korean (a covered nation in D02): the subsidiary would be a FEOC by jurisdiction, leaving no eligible prospects and a total of $45,496. Ordinary usage points to South Korea.
- Two SNUNs because there are two CFR sections: $91,098. I reject this because the question says "a covered oxide".

gaps:
- D02 is DOE's proposed interpretation; the final FEOC guidance is not in the packet, so the classification rests on the proposed text.
- The question does not say where the Korean subsidiary is incorporated or operates, or who ultimately owns the Shanghai parent. I assumed Korean incorporation, no production in China, and no government or senior-political-figure ownership.
- D06 prints the small-business SNUN cost inconsistently ($14,976 in Unit I.D versus "about $14,967" in Unit IV.D). This does not affect the large-business figure.
- All six documents were read in full from the text/ extraction (D01-D06). The docs/ originals were not opened separately, since they are the same text-method sources.

contaminated: no
