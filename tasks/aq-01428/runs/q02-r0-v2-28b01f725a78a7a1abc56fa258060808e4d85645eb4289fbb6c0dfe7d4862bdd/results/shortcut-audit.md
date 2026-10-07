# q02 rev 0 - shortcut audit (raw return)

- Date: 2026-10-06 (user's local date)
- Role: fresh shortcut-auditor subagent (Claude Code, Opus 5.5, omitClaudeMd role file, scope hook), packet shortcut
- Run: q02-r0-v2-28b01f725a78a7a1abc56fa258060808e4d85645eb4289fbb6c0dfe7d4862bdd
- tested_sha256: 28b01f725a78a7a1abc56fa258060808e4d85645eb4289fbb6c0dfe7d4862bdd
- Prompt: workspace root, packet path shortcut, and the question verbatim

## Return (verbatim)

answer: €6.45 billion (13.80 − 7.347 = 6.453)

verdict: clear

shortest_path:
1. Guidance in place at 30 June 2026 comes from D01, Eni's Q1 2026 release dated 24 April 2026.
   - text/D01.txt line 70: "FY CFFO guidance is raised by 20% to €13.8 bln."
   - Line 178: "At a revised Brent scenario of 83 $/bbl, SERM refining margin at 8 $/bbl … adjusted CFFO to amount to €13.8 bln".
   - The next change came in D02, dated "July 29, 2026" (line 110), at line 253: "adjusted CFFO is expected to amount to €15 bln". That was after the end of June.
2. The H1 2026 actual comes from D02 (6-K filed 4 Aug 2026).
   - Line 133: "|2,878|Cash flow from operations before changes in working capital at replacement cost (a)||4,469|2,775|61|7,347|…". The columns are Q1'26 | Q2'26 | Q2'25 | % | H1'26.
   - The same row appears at line 785. The original file also says "€7,347 mln in IH ’26 (€4,469 mln in the Q2 ’26)".
   - Cross-check: D01 Q1 is 2,878 (line 97), and 2,878 + 4,469 = 7,347.
3. The calculation is 13,800 − 7,347 = 6,453 million, so €6.45 bln. The rounded narrative figures give the same result: 13.8 − (2.88 + 4.47) = 6.45.
4. Both figures measure the same thing. D01 line 159 says "adjusted CFFO before working capital movements was €2.88 bln", and the guidance at line 178 is also "adjusted CFFO". The definition is at D02 lines 1009–1011.

sufficient_documents: D01 + D02. Both are needed, and no other pair works.
- D01 alone has the guidance and Q1, but no Q2.
- D02 alone has H1 but only the 29 July €15 bln guidance. "13.8" does not appear anywhere in D02, in either the text or the original.
- D03 and D04 are Occidental releases in USD and are not relevant.

searches:
- Terms searched across text/D01–D04: CFFO, "cash flow from operations", "before working capital", guidance/raised/revised/previous/prior/last quarter, 13.8/13,8, 7,347, 2,878, 4,469, €15 bln, second half/2H/remaining/rest of the year/June 30, 6.45/7.65.
- Read D01 lines 1–200, 600–629 and 760–771.
- Read D02 lines 1–300, 750–789, 866–945 and 1000–1019, including the lines the search display had cut short.
- Checked the key values against the docs/ originals with sha256-matched sources.
- I did not open the packet's question.txt, because it is a question file.

Shortcut attempts (none worked):
- **Whole-answer lookup:** neither Eni release states a second-half requirement or remaining amount.
- **D02 alone, via the buyback policy:** using "60% of upside vs. the budgeted CFFO (€11.5 bln)", 2.8 = 1.5 + 0.6 × (X − 11.5) gives X ≈ 13.67, and an answer of 6.32. That is wrong. The same formula gives 14.67 for July instead of the stated 15, so this back-calculation is unreliable.
- **D02 alone, via sensitivities:** backing out the old guidance needs the prior scenario (Brent 83, SERM 8), which only D01 has.
- **Wording:** the question does not give away any number.
- **Difficulty risk:** once the right guidance is picked, this is a single subtraction across two documents. The real test is the timing: telling the April guidance apart from the July guidance.

readings/gaps:
- €7.65 bln (15 − 7.347): uses the 29 July upgrade. Rejected because it was announced after 30 June, and this is the most likely trap.
- €4.15 bln (11.5 − 7.347): uses the original budget. Rejected because it was replaced on 24 April.
- 10.92 (13.8 − 2.878): this is what was needed for Q2–Q4, not for the second half.
- Gaps: none material. The packet has no Eni statements between 24 April and 29 July, so an interim update can't be ruled out completely. However, D02 line 264 refers to "last quarter already revised guidance of €2.8 bln" (the buyback), which suggests the Q1 update was the last one before July.

Files: shortcut\text\D01.txt, shortcut\text\D02.txt, shortcut\docs\eni-spa-q2-2026-results-announcement-form-6-k-filed-2026-08-04.txt

## Caller classification

verdict: clear; route D01 April 24 guidance €13.8 bln (l.70/l.178) and D02 H1 7,347 (l.133/l.802), 13.8 - 7.347 = 6.45; D01 + D02 both required; D02-only buyback back-calculation 6.32 (wrong).
