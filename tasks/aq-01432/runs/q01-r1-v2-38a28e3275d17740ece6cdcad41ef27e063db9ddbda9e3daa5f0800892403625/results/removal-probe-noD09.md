# q01 rev 1 - removal probe without D09 (CMA207, platform Doc 9), 2026-10-06

Packet: runs/q01-r1-probe-m2/solver-2 (copy of the rev 1 solver-1 packet minus D09, ids and header lines
renumbered D01-D10, so the short guide is D09 inside the probe; neutral run name; question.txt = rev 1
wording, not read by the probe). Fresh blind-solver; question verbatim plus the forced-guess instruction.

Raw return as received:

answer: The packet doesn't settle this. Forced best guess: **6** of the 7 named behaviours (probability ≈ 0.6).

confidence: low

path:
1. D09 (probe numbering) is the short guide: L13 "This is a short guide to the unfair commercial practices guidance to help businesses understand what they need to do."; L71 "The banned practices fall into the following themes."; L89 heading "Pressure selling".
2. D09 L91 gives 7 behaviours: (a) exaggerating the risks they face, (b) pretending they have ordered something, (c) refusing to leave their home, (d) hassling them by repeatedly contacting them, (e) making them feel they can't leave your shop without buying, (f) asking children to buy products, (g) saying your livelihood is at risk. "Put unfair pressure" not counted (the heading idea, not a separate banned practice).
3. Only one behaviour linked to a specific banned practice in the packet: D08 L63 refusal to leave = "paragraph 27 of Schedule 20 to the DMCC Act" (nothing on prosecution).
4. No packet document says which banned practices are criminal offences: D09 L57 fines and compensation only; UK offence/prosecution hits not about banned practices (D08 L91 offence under the 2013 regulations; D08 L111/121 debt-example threats of "criminal proceedings"); other hits US FTC material (D03, D05) or unrelated words; D04 and D10 enforcement by CMA/TSS/ASA, no criminal liability.
5. Forced guess from memory, not the packet: under the CPUTRs 2008 (regulation 12) every banned practice was an offence except advertorials and urging children to buy; believed the DMCC Act keeps a similar exception list (recalled as advertorials 12, fake reviews 13, children 29). Only (f) falls in it → 7 − 1 = 6.

minimal_documents: D09 (probe numbering) for the behaviours; no packet document supplies prosecution facts; D08 only backs up paragraph 27.

readings: every Schedule 20 practice an offence → 7; one more pressure-selling practice excluded → 5 (unlikely); counting "unfair pressure" as a behaviour leaves the prosecutable count at 6.

gaps: the full guidance and the DMCC Act's offence sections and Schedule 20 are absent, so paragraph numbers for six of the seven behaviours and their prosecutability are missing. Read in full D08, D09, D10, manifest, D04 L95–124; others keyword-searched across text/ and docs/ (prosecut, offence/offense, criminal, penal, convict, indictment, liable, guilty, imprison, sentence, magistrate, Crown Court, sanction, civil, CPRs, regulation, section 23x, Schedule 20, banned, pressure, children, livelihood, exhort, turnover); docs/ matches text/; question.txt not read.

contaminated: no — git-status file names only; no project instructions or memory content present.

Caller adjudication: not answerable from the packet; forced guess equals the gold (p 0.6) through recalled
CPUTRs law. Same risk as rev 0 (p 0.55). Platform document-check risk for Doc 9: moderate; fallback is the
one-line reviewer note.
