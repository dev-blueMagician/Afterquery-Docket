# q01 rev 0 - blind solver B (fresh blind-solver subagent, packet solver-2), 2026-10-06

Raw return as received:

answer: 6 — the guide names 7 pressure-selling behaviours; a trader could be prosecuted for 6 of them (all except asking children to buy products).

confidence: high

path:
1. D10 (text/D10.txt L13 identifies itself: "a short guide to the unfair commercial practices guidance to help businesses understand what they need to do"). Its "Pressure selling" theme (L91): "You must not put unfair pressure on consumers to buy products for example by exaggerating the risks they face, pretending they have ordered something when they haven't, refusing to leave their home, hassling them by repeatedly contacting them, or making them feel they can't leave your shop without buying something. You mustn't ask children to buy products, or tell customers that if they don't buy your product then your livelihood will be at risk." → 7 behaviours.
2. Map each to the full guidance's numbered banned practices (D09 L397–L763):
   (a) exaggerating risks → BP14 "materially inaccurate claim concerning the nature and extent of the risk to the personal security or safety of the consumer" (example L581 "exaggerated statements of the risk of doorstep mugging");
   (b) pretending they have ordered something → BP24 "invoice or similar document ... gives the consumer the impression that the consumer has already ordered the marketed product when the consumer has not" (BP31, unsolicited products with payment demand, also arguable);
   (c) refusing to leave their home → BP27 "Ignoring a request from a consumer to leave or not return to the consumer's home" (D08 L63 confirms "breach of paragraph 27 of Schedule 20");
   (d) repeated contact → BP28 "Making persistent and unwanted solicitations by any means";
   (e) can't leave shop → BP26 "Creating the impression that the consumer cannot leave the premises until a contract is formed.";
   (f) asking children → BP30 "a direct appeal to children to buy advertised products";
   (g) livelihood at risk → BP32 "if the consumer does not buy the product, the trader's job or livelihood will be at risk."
3. BP numbering equals Schedule 20 paragraph numbering: fn38 (L1589) notes the old CPUTRs list "has been rearranged and therefore the numbers of the banned practices differ"; L573 says BP13's full text is "in paragraph 13 of Schedule 20"; D08 maps BP27→para 27 and BP22→para 22.
4. Criminal status: D09 L1387 "It is an offence to engage in a commercial practice which involves: banned practices listed in Schedule 20 to the DMCC Act [footnote 112]", and fn112 (L1885): "It is not a criminal offence to infringe paragraphs 12, 13 or 30 of Schedule 20." Also fn39 (L1593): "Most banned practices (except those listed in paragraphs 12, 13 and 30 of Schedule 20 to the DMCC Act) amount to criminal offences, which can lead to fines and/or imprisonment." "Time limits apply to the prosecution of offences" (L1437).
5. Of BP14, 24 (or 31), 27, 28, 26, 30, 32 — only BP30 is in {12, 13, 30}. So 7 − 1 = 6.

minimal_documents: D10 (the guide's own list; D09 only names "pressure selling" as a theme at L95 without enumerating which practices belong to it) and D09 (mapping and the criminal-offence exceptions). D08 cannot substitute (it maps only paras 27 and 22 and has no criminal-exception text). No other document provides an alternative source.

readings:
- Counting only the first sentence's "for example" list (5 behaviours): all 5 criminal → 5. Weaker, because the second sentence is under the same "Pressure selling" heading.
- Reading "prosecuted" as under any offence (e.g. the children appeal might still be an aggressive or misleading practice, which D09 L1387 lists as offences) → could be 7; excluded by the question's "for breaching the banned practice involved".
- "Pretending they have ordered" as BP31 rather than BP24: both are criminal → still 6.

gaps:
- D01–D07 and D11 not read in full; searches for offence/prosecut/criminal/pressure/children showed nothing relevant (FTC materials and CMA reviews/hidden-ad guides).
- D09 read in parts (L380–L779, L1365–L1444, L1583–L1622, L1870–L1929) plus search hits.
- Text-only documents (manifest pages null), no PDF to check.
- D09 footnote markers 116–119 in the body do not quite line up with the numbered notes; this does not affect fn39 or fn112, which agree.

contaminated: no — session context showed workspace file names in git status but no file contents, answers or hints; nothing outside this packet's text/ was read.
