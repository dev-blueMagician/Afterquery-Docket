# q01 rev 0 - removal probe without D10 (short business guide, platform Doc 11), 2026-10-06

Packet: runs/q01-r0-probe-t5/solver-1 (byte copy of solver-1 minus D10, ids renumbered D01-D10; neutral
run name). Fresh blind-solver; question verbatim plus the forced-guess instruction.

Raw return as received:

answer: Not answerable from this packet — the short business guide to unfair commercial practices is not in it. Forced best guess: **5** (probability ≈ 0.25 that it is correct).

confidence: low

path:
1. The short guide is missing. The manifest lists D01–D10; the only UK "short guide" is D06, which covers publishing consumer reviews. D08 L25 points to "our explainer on what businesses need to do to comply with the law", but it is not included. Searches of text/ and docs/ for "short guide", "explainer" and "pressure" found no list of pressure-selling behaviours.
2. D09 mentions pressure selling but does not define it: L95 "There are 32 commercial practices ... unfair in all circumstances. These include fake reviews, misuse of trust marks, pressure selling and sales of illegal products." It never says which numbered banned practices count as pressure selling.
3. Offences (D09): L1387–1391 "It is an offence to engage in a commercial practice which involves: banned practices listed in Schedule 20 ... [footnote 112]"; fn112 (L1885) "It is not a criminal offence to infringe paragraphs 12, 13 or 30 of Schedule 20."; fn39 (L1593) agrees.
4. The three exceptions: practice 12 (L519) unlabelled paid editorial content; 13 (L527–571) fake reviews; 30 (L729) "a direct appeal to children to buy advertised products or persuade their parents or other adults to buy" — only this one could reasonably be called pressure selling.
5. Likely pressure-selling candidates by ordinary meaning: core five — practice 7 (L477, false "limited time" claims; example L481 "in order to pressure them into making an immediate decision to buy"), 26 (L695), 27 (L703), 28 (L711), 32 (L759); borderline 14 (L577), 20 (L639), 30 (L729), 31 (L739).
6. Rule: every named pressure-selling behaviour is prosecutable except one matching paragraph 30, so the answer is the number named, minus 1 if the guide includes the children's appeal.
7. Guess: the core five are all prosecutable → 5 (if the guide also listed the children's appeal, 6 named, still 5). The guide's actual list cannot be checked.

minimal_documents: D09 for the offence rule and the list of banned practices; the missing short guide is needed for which behaviours it names. Nothing in the packet stands in for it (D08 names only paragraphs 27, L63, and 22, L159).

readings: 4 (26, 27, 28, 32 with or without 30, or without 7); 6 (all of 26–32 named, 6 prosecutable); 3 (a short list such as 7, 27, 28); D08 treated as "the short guide": 1 (paragraph 27 only) or 2 (with the paragraph 22 prize case), both prosecutable.

gaps: the decisive document (the guide's own list) is absent and was not filled in from memory. D09 read in part (L1–140, L380–779, L1210–1334, L1365–1444, L1584–1613, L1870–1930) and searched in full; D06, D08 read in full; D04, D07, D10 and the US FTC documents (D01, D02, D03, D05) searched only. docs/ matches text/; plain text, no PDF pages. question.txt not read by design. Some D09 in-text footnote markers misnumbered (due-diligence references); fn112 unaffected.

contaminated: no — automatic context included a git status of workspace file names only; no CLAUDE.md, memory or notes read.

Caller adjudication: not answerable; forced guess 5 (p 0.25) differs from the gold 6 → D10 needed.
