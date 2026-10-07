# q03 rev 0 - blind solver A (fresh blind-solver subagent, packet solver-1), 2026-10-07

Raw return as received:

answer: 5, 6, 7, 11, 17, 22, 23

confidence: high

path:
1. Which guide: D10 (text/D10.txt L13) "a short guide to the unfair commercial practices guidance to help businesses" — the only document with a "Misleading promotional claims" heading (searched every text/ file for "promotional", "bait", "special offer", "cease trading", "statutory rights"; D06 is also a short guide but covers consumer reviews only).
2. What it lists (D10 L77–79; docs/ L75–77 identical): "Misleading promotional claims — You must not use bait advertising or bait and switch or pretend that a special offer will finish soon, or that you are about to cease trading or move premises, when this is not true. You mustn't say a product is free when in fact it isn't, or tell someone they have won a prize if that's not true. You mustn't pretend that consumers' statutory rights are a distinctive part of your offer." → 7 practices.
3. CMA207 numbers = Schedule 20 paragraph numbers: D09 L573 "The full text of the banned practice can be found in paragraph 13 of Schedule 20… banned practice 13"; D09 fn39 and L1885 non-criminal "paragraphs 12, 13 and 30 of Schedule 20" match BP12 (paid editorial), BP13 (fake reviews), BP30 (children); D08 L63 "paragraph 27 of Schedule 20" (refusing to leave = BP27); D08 L159 "paragraph 22 of Schedule 20… false impression the consumer has won a prize" (= BP22); D09 fn38 the old CPUTR list "has been rearranged and therefore the numbers of the banned practices differ".
4. Mapping (D09 chapter 3, L437–675): bait advertising → BP5 (L439, invitation at a specified price where supply "in reasonable quantities" is not possible and the trader "does not disclose that fact"; example headphones at £9, only 10 sets); bait and switch → BP6 (L455, refusing to show or supply, or a defective sample, "with the intention of promoting a different product"); special offer ending soon → BP7 (L477); statutory rights as distinctive → BP11 (L511); cease trading or move premises → BP17 (L601); won a prize → BP22 (L655; D08 L159 supports); free → BP23 (L671).
5. Ascending: 5, 6, 7, 11, 17, 22, 23 (7 paragraphs for 7 items; the other themes — trust marks, reviews, illegal products, pressure selling, after-sales care — map to separate practices, so none of the 7 is reused).

minimal_documents: D10 + D09 (D09 the only full numbered list — D08, D04, D11 confirm only a few numbers: D08 22 and 27; D04 13; D11 12, 13, 25; D10 the only source of the theme's members; D08 helpful backup for "banned practice N" = "paragraph N").

readings:
- Broader prize reading: "won a prize" also covering BP21 ("Claiming to offer a competition or prize promotion without awarding the prizes described") → 5, 6, 7, 11, 17, 21, 22, 23; weak (the guide's wording "tell someone they have won a prize" matches BP22; nothing about failing to award prizes).
- "All themes cover all 32" reading: BP15, BP20, BP21 (and one of BP24/BP31) are matched by no theme's wording; one could guess they belong here, but the question asks what the guide lists → excluded.
- Old CPUTR numbering: does not apply (fn38).

gaps: CMA207 does not use the labels "bait advertising" or "bait and switch" (mapped by ordinary meaning and D09's descriptions/examples); the Act's text is not in the packet (numbering link from D09 and D08); D01–D07, D11 and most of D09 searched by keyword only (D09 read L1–60, L380–788, fn L1587–1613, L1813, L1885); question.txt not read; plain text, no extraction problems.

contaminated: no
