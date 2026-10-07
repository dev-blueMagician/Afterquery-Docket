# q07 rev 0 - blind solver A (packet solver-1)

- Date: 2026-10-05
- tested_sha256: 02a3283524eba2b00d7a80b580d399ad15a83b12bb391f17df307fa2e38ae559
- Role: blind-solver, fresh non-fork context; input = root, solver-1 packet path, question text.
- Usage: 83,410 subagent tokens, 14 tool uses, 191 s.

## Raw return (verbatim)

answer: **-$167 million.** In the July 28, 2026 outlook, American Tower expected 2026 straight-line revenue of about -$66 million at the midpoint. It recognized about $101.0 million in 2025. -66 - 101.0 = -167.

confidence: high

path:
1. **2026 expectation (D07, July 28, 2026 release).** The 2026 outlook section says the estimates "reflect the Company's expectations as of July 28, 2026" (line 153).
   - The table "2026 Outlook for Total Property revenue, at the midpoint, includes the following components" (line 183) shows "Straight-line revenue (124) 3 33 3 19 (66)" (line 191).
   - The columns are U.S. & Canada, Latin America, Africa & APAC, Europe, Data Centers and Total Property. They add up: -124 + 3 + 33 + 3 + 19 = -66.
   - Column order checks out against the row above it, "International pass-through revenue N/A $516 $478 $230 N/A $1,224" (516 + 478 + 230 = 1,224).
   - The sign is confirmed by the AFFO reconciliation. It shows "Straight-line revenue 66 – 66" as an add-back (line 261). The 2025 outlook used the same convention the other way: a positive +87 component appeared as "(87)" in the AFFO reconciliation (D03 lines 217 and 291).
2. **2025 recognized (D05, Feb 24, 2026 release, footnote 3, line 111).** "Q4 2025 and FY 2025 growth rates impacted by a decrease in non-cash straight-line revenue, which represented approximately $28.0 million and $101.0 million, respectively, in the current periods." This footnote is attached to total revenue and total property revenue.
3. **Cross-check of the 2025 figure.** The quarterly footnotes add up to the full-year number: Q1 (D02 line 103) "$17.1 million"; Q2 (D03 line 107) "approximately $28.2 million"; Q3 (D04 line 111) "approximately $27.7 million"; Q4 $28.0 million; 17.1 + 28.2 + 27.7 + 28.0 = 101.0.
4. **Calculation.** -66 - 101.0 = -167.0, so -$167 million. The outlook figure is only given to whole millions.
5. **Consistency with the company's own footnotes.** D07 says "Property revenue growth rate includes an estimated negative impact of approximately 2% associated with a decrease in straight-line revenue recognition" (line 179). The check: 167 / 10,305 (FY2025 total property revenue, D05 line 67) = 1.6%, which is about 2%. The same method fits the April outlook (D06). There, -27 vs. 101 gives a drop of 128, or 1.2% of 2025 property revenue, and the footnote says "approximately 1%" (D06 lines 175 and 187).

minimal_documents: D07 + D05. No other document gives the July outlook. D05 can't be fully replaced either, because the Q4 and full-year 2025 figures only appear there. D02, D03 and D04 only corroborate the first three quarters.

readings:
- **Sign misread (rejected):** Treating the AFFO add-back "66" as positive straight-line revenue gives 66 - 101 = -35. The component table shows "(66)", and -35 is only 0.3% of revenue, which contradicts the "approximately 2%" footnote.
- **Net of straight-line expense (not what was asked):** 2026 net would be -66 - 34 = -100. The 2025 net was "approximately ... $64.8 million" (D05 line 115). That gives -164.8 million, and 164.8 / 7,130 = 2.3% of Adjusted EBITDA, consistent with D07's "approximately 2%" footnote on Adjusted EBITDA.
- **Change versus earlier 2026 outlooks (a different question):** Compared with April's -27, July's figure is -39; compared with February's -70, it is +4.

gaps:
- The full-year 2025 reconciliation tables in D05, which would show the straight-line revenue line, are cut off in both text/ and docs/ ("[… 602/688/746 characters not shown on the page …]"). D07's revenue-component rows are cut off the same way. So the 2025 figure rests on the "approximately $101.0 million" footnote, which the quarterly sum backs up.
- The packet has no PDF or layout files to check against.
- Coverage: I read all of D07, essentially all of D05, and D06 lines 20–299. For D02, D03 and D04 I read only the search hits. D01 (2021) has no straight-line matches and wasn't read further. I did not open question.txt.

contaminated: no
