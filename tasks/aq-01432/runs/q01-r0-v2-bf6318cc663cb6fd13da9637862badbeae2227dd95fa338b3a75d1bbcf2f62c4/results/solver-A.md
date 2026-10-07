# q01 rev 0 - blind solver A (fresh blind-solver subagent, packet solver-1), 2026-10-06

Raw return as received:

answer: 6 — Of the 7 banned pressure-selling behaviours the short guide names, breaching the banned practice is a criminal offence for 6; the exception is asking children to buy products (Schedule 20 paragraph 30).

confidence: high

path:
1. D10 (short guide; L13 "This is a short guide to the unfair commercial practices guidance to help businesses understand what they need to do"; L71 "The banned practices fall into the following themes.") Under "Pressure selling" (L89–L91): "You must not put unfair pressure on consumers to buy products for example by exaggerating the risks they face, pretending they have ordered something when they haven't, refusing to leave their home, hassling them by repeatedly contacting them, or making them feel they can't leave your shop without buying something. You mustn't ask children to buy products, or tell customers that if they don't buy your product then your livelihood will be at risk." → 7 behaviours.
2. D09 (CMA207, L575–L763) maps each behaviour to a numbered banned practice (= Schedule 20 paragraph; L573 ties "Banned practice 13" to "paragraph 13 of Schedule 20"; D08 L63 ties refusing to leave to "paragraph 27 of Schedule 20"):
   - exaggerating risks → BP14 "materially inaccurate claim concerning the nature and extent of the risk to the personal security or safety…"
   - pretending ordered → BP24 "…gives the consumer the impression that the consumer has already ordered the marketed product when the consumer has not" (BP31 unrequested supply would give the same result)
   - refusing to leave home → BP27 "Ignoring a request from a consumer to leave or not return to the consumer's home"
   - repeated contact → BP28 "Making persistent and unwanted solicitations by any means"
   - can't leave shop → BP26 "Creating the impression that the consumer cannot leave the premises until a contract is formed."
   - children → BP30 "Including in an advertisement a direct appeal to children to buy advertised products…"
   - livelihood → BP32 "…the trader's job or livelihood will be at risk."
3. D09 L1391: offence to engage in "banned practices listed in Schedule 20 to the DMCC Act [footnote 112]"; fn112 (L1885): "It is not a criminal offence to infringe paragraphs 12, 13 or 30 of Schedule 20." Corroborated by fn39 (L1593): "Most banned practices (except those listed in paragraphs 12, 13 and 30 of Schedule 20 to the DMCC Act) amount to criminal offences, which can lead to fines and/or imprisonment."
4. Calculation: 7 behaviours → paragraphs {14, 24, 27, 28, 26, 30, 32}; only 30 is in the excluded set {12, 13, 30}; 7 − 1 = 6. (12 = undisclosed paid editorial content, 13 = fake reviews — both in D10's reviews/hidden-advertising theme, not pressure selling.)
5. Numbering check: fn38 (L1589) says the old CPUTRs list "has been rearranged and therefore the numbers of the banned practices differ", so the DMCC numbering in D09 governs.

minimal_documents: D10 + D09. D08 corroborates numbering but cannot replace D09 (no offence exceptions). No other document lists pressure selling or the offence exclusions.

readings:
- "Pretending they have ordered something" read as BP31 (inertia selling) instead of BP24: answer unchanged (6).
- "Prosecuted" read as under any offence: the children practice might still be prosecutable as an aggressive practice or misleading action if the effect test is met (D09 L1399–L1407), giving 7; but the question specifies "for breaching the banned practice involved", so 6 is the better reading.
- Using old CPUTRs numbering (where paragraph 12 was the personal-security risk practice) would give 5; rejected by fn38.

gaps:
- Coverage: D10 and D08 read fully; D09 read L1–L60, L385–L784, L1165–L1168, L1360–L1449, L1589–L1594, L1860–L1929.
- D01–D07 and D11 not read in full; searched all packet texts for "prosecut|offence|criminal" and "pressur|short guide" — no matches in those eight.
- D09 footnote markers slightly misaligned around 116–119, but fn39 and fn112 (decisive) are mutually consistent.
- docs/ originals are .txt (manifest method "text", no pages); no PDF to inspect, no extraction issues.

contaminated: no
