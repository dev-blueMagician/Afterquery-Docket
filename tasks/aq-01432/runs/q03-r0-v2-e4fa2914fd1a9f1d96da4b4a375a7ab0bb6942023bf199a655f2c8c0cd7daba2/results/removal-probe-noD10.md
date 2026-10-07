# q03 rev 0 - removal probe without D10 (short business guide, platform Doc 11), 2026-10-07

Packet: runs/q03-r0-probe-w4/solver-1 (copy of the q03 solver-1 packet minus D10, ids and header lines
renumbered D01-D10; neutral run name). Fresh blind-solver; question verbatim plus the forced-guess instruction.

Raw return as received:

answer: Not answerable from this packet — no document is a brief business guide on unfair trading with a "misleading promotional claims" heading, so there is no list to map. Forced best guess: paragraphs 21, 22, 23 (probability ≈ 0.12).

confidence: low for the guess; high that the packet does not settle the question.

path:
1. The guide is not in the packet: D08 (probe numbering) is only an examples page from the CMA207 collection and points at L25 to "our explainer on what businesses need to do to comply with the law", which is not among D01–D10 (manifest); docs/ search found only the same mention.
2. Other short guides do not match: D06 L13 "This summary is for businesses who publish consumer reviews" (reviews only, no grouping of banned practices); D10 (probe numbering = Who regulates hidden advertising) L70 lists Banned Practice 12, 13, 25 under hidden advertising; D07 L75 "Avoid misleading your audience" (influencer advice, no numbers).
3. Searches across text/ for "promotion", "promotional claim", "short guide|brief guide|explainer", "unfair trading", "at a glance", "misleading (promotion|marketing|advert|offer|sales|claim|price|pricing)" found no such heading; nearest summary D09 L95 "These include fake reviews, misuse of trust marks, pressure selling and sales of illegal products."
4. Banned practice N = Schedule 20 paragraph N (D09 L393, L573, fn39 L1593; D08 L159 paragraph 22 = D09 BP22 L655; D08 L63 paragraph 27 = D09 BP27 L703).
5. Forced guess from the D09 practices most clearly about sales promotions: BP21 (L647), BP22 (L655), BP23 (L671) → 21, 22, 23 (not based on any guide wording).

minimal_documents: the missing brief guide plus D09; D08 backs up the mapping but cannot replace the guide.

readings: broader "offers/marketing claims" heading → 7, 17, 21, 22, 23 (~0.08) or 5, 6, 7, 17, 21, 22, 23 (~0.07); hidden-advertising reading (D10 probe numbering as the guide) → 12, 13, 25 (unlikely).

gaps: the brief guide and its list are absent (deciding fact); US FTC documents seen through search hits only; D04 L1–120 plus hits; D09 L1–170, L380–780, L1580–1620 plus searches; no PDFs.

contaminated: no (git-status file names only).

Caller adjudication: not answerable; forced guess 21, 22, 23 (p 0.12) differs from the gold → D10 needed.
Note: the probe's best alternative reading (5, 6, 7, 17, 21, 22, 23) also differs (adds 21, drops 11).
