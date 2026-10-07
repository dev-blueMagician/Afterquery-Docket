# q03 rev 0 - blind solver B (fresh blind-solver subagent, packet solver-2), 2026-10-07

Raw return as received:

answer: 5, 6, 7, 11, 17, 22, 23

confidence: high

path:
1. The guide: D10, GOV.UK "What businesses need to know about unfair commercial practices" (L13 "This is a short guide to the unfair commercial practices guidance"); under "Misleading promotional claims" (L77), L79: "You must not use bait advertising or bait and switch or pretend that a special offer will finish soon, or that you are about to cease trading or move premises, when this is not true. You mustn't say a product is free when in fact it isn't, or tell someone they have won a prize if that's not true. You mustn't pretend that consumers' statutory rights are a distinctive part of your offer." → 7 items (docs/ L77 same); no other document uses this heading.
2. D09 numbers = Schedule 20 paragraph numbers: L393 "Schedule 20 to the DMCC Act lists 32 banned commercial practices."; fn38 (L1589) old CPUTRs Schedule 1 "has been rearranged and therefore the numbers of the banned practices differ."; L573 "paragraph 13 of Schedule 20 … banned practice 13."; D08 L63 "paragraph 27 of Schedule 20" = refusing to leave = D09 BP27; D09 fn39 (L1593) paragraphs "12, 13 and 30 of Schedule 20" not criminal = D09 12 (paid editorial), 13 (reviews), 30 (children).
3. Mapping (D09): bait advertising → 5 (L439); bait and switch → 6 (L455–469, "with the intention of promoting a different product"); special offer ending soon → 7 (L477); statutory rights as a feature → 11 (L511); closing down or moving → 17 (L601); prize claim → 22 (L655; D08 L159 "paragraph 22 of Schedule 20 … creating the false impression the consumer has won a prize"); "free" → 23 (L671).
4. Exclusions: 20 (market conditions/availability), 21 (competition not awarding prizes), 15 and 31 — not named, none fits.
5. Ascending: 5, 6, 7, 11, 17, 22, 23 (7 paragraphs for 7 items).

minimal_documents: D10 + D09 (D08 backs up paragraph 22 and the numbering but cannot replace D09).

readings: broader — "tell someone they have won a prize" also covering 21 → 5, 6, 7, 11, 17, 21, 22, 23 (weaker: D10 describes a false claim of winning, not a failure to award); weaker still — "special offer will finish soon" mapped to 20 as well as 7 (no textual basis).

gaps: the Act's text is not in the packet (paragraphs 5, 6, 7, 11, 17, 23 from D09's numbering, tied to Schedule 20 by the cross-references); "bait advertising"/"bait and switch" undefined in the packet, matched by ordinary meaning (only other "bait" mention an FTC citation, D02 L178); read D10, D08 in full, D09 L380–799 and fn10, fn38–44; D01–D07, D11 key-term searches only; text sources, no PDFs.

contaminated: no — question.txt not opened; git status listed only other task paths.
