# q01 rev 1 - removal probe without D10 (short business guide, platform Doc 11), 2026-10-06

Packet: runs/q01-r1-probe-m2/solver-1 (copy of the rev 1 solver-1 packet minus D10, ids and header lines
renumbered D01-D10; neutral run name; question.txt = rev 1 wording, not read). Fresh blind-solver; question
verbatim plus the forced-guess instruction.

Raw return as received:

Not answerable from the packet — the short UCP guide is missing, so its pressure-selling list cannot be checked. Forced best guess: **6** (probability ≈ 0.25).

    answer: not answerable from this packet. Forced best guess: 6 (probability ~0.25)
    confidence: low
    path:
    1. The short guide is not here: searched text/ and docs/ (identical match counts) for pressur, theme(s), short guide, explainer, summary, "banned practices". The only "short guide" is D06 (consumer reviews; L11 URL ".../fake-reviews/short-guide-for-businesses-publishing-consumer-reviews-and-complying-with-consumer-protection-law"), no themes, nothing on pressure selling. Only D08 and D09 contain "pressur"; D08 L25 points to "our explainer on what businesses need to do to comply with the law", not in the packet. D09 lists banned practices one by one (L397–763), never grouped into themes.
    2. D09 L95: "There are 32 commercial practices listed in the DMCC Act… These include fake reviews, misuse of trust marks, pressure selling and sales of illegal products."
    3. Prosecutable (D09): L1387–1391 "It is an offence to engage in a commercial practice which involves: banned practices listed in Schedule 20 to the DMCC Act [footnote 112]"; fn112 L1885 "It is not a criminal offence to infringe paragraphs 12, 13 or 30 of Schedule 20."; fn39 L1593 the same.
    4. Banned practice N = Schedule 20 paragraph N (D08 L63 paragraph 27 = D09 BP27 L703; D08 L159 paragraph 22 = D09 BP22 L655).
    5. Possible pressure-selling practices: 7 (L477, limited time "to elicit an immediate decision"; example L481 "to pressure them"), 14 (L577), 26 (L695), 27 (L703), 28 (L711), 29 (L719), 30 (L729, the only non-criminal candidate), 31 (L739), 32 (L759).
    6. Answer = number named under pressure selling minus any mapping to 12, 13 or 30. Guess: the theme covers the aggressive block 26–32 (7 behaviours) → 7 − 1 = 6; chosen because "the question only makes sense if one listed behaviour can't be prosecuted, and in a pressure-selling theme that can only be paragraph 30."
    minimal_documents: D09 plus the missing short guide; D08 optional (numbering).
    readings: theme {26, 27, 28, 30, 31, 32} or {7, 26, 27, 28, 30, 32} → 5 (~0.2); {26, 27, 28, 30, 32} or {26, 27, 28, 32} → 4; 7 plus 26–32 → 7; children practice under another theme → the full count; only a few examples per theme → smaller.
    gaps: the short business guide (the "explainer") is absent — the deciding fact. Unread: D09 L777–1210, L1311–1369, L1445–1582, L1603–1804, L1820–1869 (searched; no theme grouping found); D04 only L243–245; D01, D02, D03, D05 searched only. question.txt not read. Text only, no extraction problems.
    contaminated: no

Caller adjudication: not answerable; the forced guess equals the gold (p 0.25) through the coincidence the
rev 0 review flagged (practices 26-32 are seven items including 30) plus an inference from the question's
form. Rev 0's probe without D10 guessed 5 (p 0.25). Platform document-check risk for Doc 11: low to
moderate (the high model, not forced to guess, would most likely answer "cannot be determined").
