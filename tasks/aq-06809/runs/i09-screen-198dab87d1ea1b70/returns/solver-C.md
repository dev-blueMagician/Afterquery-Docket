# i09 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-19

Raw return, verbatim. Judged: right (gold 1.5). Readings raised: 3.0 (printed quarters only), 2.5 / 2.1
(Huntington's own-definition ratio, against the stated formula), 1.2 (GAAP revenue, not asked).

answer: 1.5 percentage points. The narrowest gap was in 1Q25: Fifth Third ≈61.0% vs Huntington ≈59.5%. In that quarter Fifth Third's ratio was the higher one; in 2Q25–4Q25 Huntington's was higher.

confidence: high on the data and arithmetic. The answer depends on including 1Q25, which has to be derived as six-month 2025 YTD minus 2Q25 (see readings).

path:
1. Fifth Third's reported ratio uses the question's definition. D01 p.29 Non-GAAP Reconciliation: "Efficiency ratio (FTE) (w) / [(a) + (u)]", i.e. noninterest expense / (NII FTE + noninterest income). D02 slide 42 has the same: "Efficiency ratio (FTE) (g) / [(c) + (e)]".
2. Huntington's reported ratio does not. D04 p.3 note (4) and p.18 note (2): "Noninterest expense less amortization of intangibles divided by the sum of FTE net interest income and noninterest income excluding … securities gains (losses)". So I recomputed Huntington from the raw lines.
3. Fifth Third quarters, D01 p.15 five-quarter Financial Highlights (columns Jun26, Mar26, Dec25, Sep25, Jun25):
   - "Total revenue (FTE)(a) 3,279|2,834|2,344|2,306|2,250"
   - "Noninterest expense|2,109|2,395|1,309|1,267|1,264"
   - Reported "Efficiency (FTE)" is 55.8 / 54.9 / 56.2 for 4Q25 / 3Q25 / 2Q25.
   Fifth Third YTD, D01 p.14 (June 2025 year-to-date column): "Total revenue (FTE)(a) …6,113|4,386"; "Noninterest expense…4,504|2,568"; NII FTE 2,942; noninterest income 1,444.
   Derived 1Q25: revenue 4,386−2,250 = 2,136 (1,442 + 694); noninterest expense 2,568−1,264 = 1,304.
4. Huntington quarters, D04 p.10 (same figures in D03 Tables 3 and 8): "Total revenue FTE (1)|$|2,857 $|2,592 $|2,191 $|2,151 $|1,954"; "Total noninterest expense|1,809 1,774 1,420 1,246 1,197".
   Huntington YTD, D04 p.22: "Total revenue (1)|$|5,449 $|3,889"; "Total noninterest expense|3,583 2,349"; NII FTE 2,924; noninterest income 965.
   Derived 1Q25: revenue 3,889−1,954 = 1,935 (1,441 + 494); noninterest expense 2,349−1,197 = 1,152.
5. Ratios (noninterest expense / FTE revenue) and gaps:
   | Quarter | Fifth Third | Huntington | Gap (pp) |
   |---|---|---|---|
   | 1Q25 | 1,304/2,136 = 61.049% | 1,152/1,935 = 59.535% | 1.514 |
   | 2Q25 | 1,264/2,250 = 56.178% | 1,197/1,954 = 61.259% | 5.081 |
   | 3Q25 | 1,267/2,306 = 54.944% | 1,246/2,151 = 57.927% | 2.983 |
   | 4Q25 | 1,309/2,344 = 55.845% | 1,420/2,191 = 64.811% | 8.966 |
   The minimum is 1Q25 at 1.514, which rounds to 1.5. Rounding each ratio first (61.0 − 59.5) also gives 1.5.
6. Cross-checks:
   - My Fifth Third ratios reproduce the printed 56.2 / 54.9 / 55.8, and the YTD 58.6% (2,568/4,386 = 58.55%).
   - Huntington's printed 59.0 / 57.4 / 64.2 are reproduced under its own definition, e.g. 2Q25: (1,197−11)/(1,954+58) = 1,186/2,012 = 58.95%. This confirms the line items.
   - The decisive YTD rows are identical in the original docs/ files (fitb_ex991 lines 624–633; hban_ex992 lines 309, 315, 1719, 1721).

minimal_documents: D01 + D04.
- D02 can stand in for D01 only for 2Q25–4Q25; it has no 2025 YTD figures, so it cannot give 1Q25.
- D03 can stand in for D04 only for 2Q25–4Q25; it has no 2025 YTD income figures.
- For the reading limited to 2Q25–4Q25, any pairing of {D01 or D02} with {D03 or D04} is enough.
- D05 (KeyCorp) is not needed.

readings:
- Only the quarters printed in the five-quarter tables (2Q25–4Q25): the narrowest is 3Q25, 2.983, so 3.0 pp.
- Using Huntington's reported adjusted efficiency ratio, which goes against the question's stated definition:
  - Printed quarters only: 3Q25, 57.4 − 54.9 = 2.5 pp.
  - Including derived 1Q25: Huntington (2,327−1,186)/(3,947−2,012) = 1,141/1,935 = 58.97% vs Fifth Third 61.05%, so 2.1 pp.
- GAAP (non-FTE) revenue, which was not asked for: 1Q25 would be 1,304/2,131 = 61.19% vs 1,152/1,920 = 60.00%, so 1.2 pp. 1Q25 is still the narrowest.

gaps:
- No document prints 1Q25 directly. It is derived as six-month YTD minus 2Q25, both as presented in the 2026 filings; nothing in the packet mentions a restatement.
- D05 (KeyCorp) was checked by search only ("Fifth Third", "Huntington", "FITB", "HBAN", "peer"), not read in full. Its only "peer" mentions are generic boilerplate.
- In D02 I read the narrative, expense and reconciliation slides; the credit and portfolio slides were only skimmed.
- All documents are text-method sources with no PDF pages, so no page-image check was possible or needed.

contaminated: no. The packet folder contains a question.txt, which I did not open.
