# q07 rev 0 - shortcut auditor (packet shortcut)

- Date: 2026-10-05
- tested_sha256: 02a3283524eba2b00d7a80b580d399ad15a83b12bb391f17df307fa2e38ae559
- Role: shortcut-auditor, fresh non-fork context; input = root, shortcut packet path, question text.
- Usage: 78,096 subagent tokens, 22 tool uses, 206 s.

## Raw return (verbatim)

answer: **−$167 million.** In the July 28, 2026 outlook, American Tower expected 2026 straight-line revenue of about −$66M, against about $101.0M recognized in 2025: −66 − 101.0 = −167.

verdict: clear

shortest_path:
1. **D07** (`docs/amt_ex991_2026-07-28.txt`, the Q2 2026 release, outlook "as of July 28, 2026"), text line 191, total property revenue components at midpoint: "Straight-line revenue (124) 3 33 3 19 (66)". So the total is −66. The segment figures add up: −124 + 3 + 33 + 3 + 19 = −66.
   - The sign is confirmed in the same document. The AFFO reconciliation adds back "Straight-line revenue 66 – 66" (lines 261, 293), and footnote (2) refers to "a decrease in straight-line revenue recognition". The 2025 editions use the same convention in reverse: the components table shows 87 and the reconciliation shows (87).
2. **D05** (`docs/amt_ex991_2026-02-24.txt`, the Q4 and full-year 2025 results), text line 111, footnote (3): "Q4 2025 and FY 2025 growth rates impacted by a decrease in non-cash straight-line revenue, which represented approximately $28.0 million and $101.0 million, respectively, in the current periods…"
3. Calculation: −66 − 101.0 = **−167**.
4. Cross-check from the quarterly footnotes: Q1 17.1 (D02, line 103) + Q2 28.2 (D03, line 107) + Q3 27.7 (D04, line 111) + Q4 28.0 (D05) = 101.0.

sufficient_documents: D07 + D05 is the minimal pair. An alternative route is D07 + D02 + D03 + D04 + D05 using the quarterly sum, which still needs D05 for Q4. No single document is enough:
- D07 has no visible full-year 2025 straight-line figure. Its "approximately 2%" growth-impact footnote implies roughly −206 against about $10.3B of 2025 property revenue, so it can't produce the exact figure.
- D05 has the 2025 actual but only the February outlook (−70), which gives the wrong-edition answer of −171.

The route is an ordinary two-document subtraction. That is a difficulty risk, not a shortcut.

searches:
- **Terms:** a regex for straight-line, straight line and straightline across text/ and docs/ (78 hits each, in D02–D07; none in D01). I also searched for "167/166/168" (no answer-shaped hit), "101", and "prior-year/2025" near "straight".
- **Read in full or in large part:** D07 lines 1–716, D05 lines 1–340 and 420–919, D06 lines 1–200, D01's opening (an unrelated 2021 CoreSite acquisition release).
- **Checked:** the 2025 outlook tables in D02–D04, and that the docs/ originals match the text/ extraction for the key lines.
- **Not opened:** question.txt, per the rules.

readings/gaps:
- **Wrong edition:** February 2026 outlook (−70, D05): −171; April 2026 outlook (−27, D06): −128.
- **Wrong 2025 base (outlook instead of actual):** April 2025 outlook (61, D02): −127; July or October 2025 outlook (87, D03/D04): −153.
- **Net straight-line instead of revenue:** 2025 net of expense was 64.8 and the July 2026 figure would be −66 − 34 = −100, giving −164.8. The question asks for revenue, so this is not the right reading.
- **Sign misread:** treating the AFFO add-back of +66 as the 2026 value gives 66 − 101 = −35. This is wrong.
- **Rounding:** the 2026 figure is rounded to whole millions, so −167 is the precise figure that can be supported.
- **Extraction gaps:** "[... N characters not shown on the page ...]" placeholders appear in both docs/ and text/ across the financial-statement, segment and reconciliation tables of D02–D07. These include D05's full-year 2025 revenue-components and AFFO-reconciliation rows, which probably contain a straight-line line. That content is unresolved. However, it sits in D05, and D07's gaps cover only quarterly and six-month tables, so they don't open a single-document route.
- No contamination: no notes, question files, author reasoning or prior outputs were seen.
