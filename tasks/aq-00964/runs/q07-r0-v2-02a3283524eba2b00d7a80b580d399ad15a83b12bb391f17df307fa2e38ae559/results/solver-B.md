# q07 rev 0 - blind solver B (packet solver-2)

- Date: 2026-10-05
- tested_sha256: 02a3283524eba2b00d7a80b580d399ad15a83b12bb391f17df307fa2e38ae559
- Role: blind-solver, fresh non-fork context; input = root, solver-2 packet path, question text.
- Usage: 77,337 subagent tokens, 16 tool uses, 191 s.

## Raw return (verbatim)

answer: **-$167 million.** In its July 2026 outlook, American Tower expected 2026 straight-line revenue of -$66 million (midpoint). It recognized about +$101.0 million of straight-line revenue in 2025, so the expected 2026 figure is about $167 million lower.

confidence: high

path:
1. The July 2026 outlook is D07 (docs/amt_ex991_2026-07-28.txt), the Q2 2026 release. Line 153 says the estimates "reflect the Company's expectations as of July 28, 2026."
2. D07 line 183 is the table "2026 Outlook for Total Property revenue, at the midpoint, includes the following components ($ in millions)". Its row at line 191 reads "Straight-line revenue (124) 3 33 3 19 (66)". The columns are U.S. & Canada, Latin America, Africa & APAC, Europe, Data Centers and Total. Check: -124 + 3 + 33 + 3 + 19 = -66.
3. The sign is confirmed in D07's AFFO reconciliations. Lines 261 and 293 show "Straight-line revenue 66 – 66", which is an add-back, so the revenue item is -66. The 2025 outlook used the opposite pattern: D04 line 219 shows "Straight-line revenue 48 32 7 87", and the AFFO reconciliation deducted "(87)" (D04 lines 293 and 323). Footnotes in D07 also call this a decrease: line 179 says "negative impact of approximately 2% associated with a decrease in straight-line revenue recognition."
4. The 2025 recognized amount comes from D05 (Q4/FY2025 release, Feb 24, 2026), line 111: "FY 2025 growth rates impacted by a decrease in non-cash straight-line revenue, which represented approximately $28.0 million and $101.0 million, respectively, in the current periods".
5. The quarterly figures add up to the same total: Q1 2025 $17.1 million (D02 line 103); Q2 2025 $28.2 million (D03 line 107); Q3 2025 $27.7 million (D04 line 111); Q4 2025 $28.0 million (D05 line 111); sum 101.0.
6. Calculation: -66 - 101.0 = **-167.0**, so -$167 million.
7. Plausibility check: FY2025 total property revenue was $10,305 million (D05 line 33), and 167 / 10,305 = 1.6%. That matches the stated "approximately 2%" negative impact. Also, the 2026 midpoint of 10,770 / 10,305 gives the stated 4.5% growth.

minimal_documents: D07 and D05. D05 can't be replaced, because it is the only document with Q4 or full-year 2025. D02–D04 only corroborate the total. D05 and D06 contain the February and April 2026 outlooks, not the July one.

readings:
- **Main reading (adopted):** July 2026 outlook total minus actual 2025 → **-167**.
- **Ignoring the sign:** treating the AFFO add-back "66" as positive straight-line revenue gives 66 - 101.0 = -35. This contradicts the "(66)" in the components table and the footnotes describing a decrease, so I rejected it.
- **Comparing with the 2025 outlook instead of the actual:** -66 - 87 = -153. The question asks about revenue "recognized in 2025", so the actual figure applies.
- **Using an earlier 2026 outlook (not what the question asks):** February (D05 line 211, (70)) gives -171; April (D06 line 187, (27)) gives -128.
- **Using straight-line revenue net of straight-line expense:** 2026 would be -66 - 34 = -100 against 2025's $64.8 million (D05 line 115), giving -164.8. The question asks about straight-line revenue alone, so this doesn't apply.

gaps:
- The 2025 figure is printed as "approximately $101.0 million". Its exact GAAP value from the 10-K is not in the packet.
- In every document, the extracted tables cut off rows, marked "[... N characters not shown on the page ...]". This hides the straight-line rows in the reported-period segment and AFFO reconciliation tables, including FY2025 in D05. The docs/ source files have the same markers, and the packet has no PDF or layout file to check against.
- Coverage: read in full D07 and D05; read in part D04 lines 196–225; searched only D02, D03 and D06 (straight-line terms and prior-period/restatement wording); D01 (2021) had no straight-line matches and was otherwise not read.
- The packet contains question.txt, which I did not open.

contaminated: no
