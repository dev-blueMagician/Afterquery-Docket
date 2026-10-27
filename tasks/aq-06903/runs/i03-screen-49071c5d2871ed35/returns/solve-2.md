# i03 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i03 blind solve 2")

Judged by the author against gold 40%: RIGHT.

answer: 40%

confidence: high

path:
1. Q2 2026 operating cash flow: $2,048M. D04 summary financial data table (line 62), three months ended June 30, 2026: "|Operating cash flowse|$2,048|". Check: D04 six-month cash flow statement line 684, "Net cash provided by operating activities|3,543", minus D03 Q1 line 629, "1,495", gives 2,048.
2. Q2 2026 capital expenditures: $1,104M. D04 line 63: "|Capital expenditures|$1,104|". The segment table (line 938) has the same total of 1,104. Check from the cash flow statements: six months 496+285+972+49+275 = 2,077 (D04 lines 687-691), minus Q1 244+114+456+29+130 = 973 (D03 lines 632-636), gives 1,104.
3. Distributions to noncontrolling interests: D04 only reports this for the six months. Line 701 under "Cash dividends and distributions paid:" reads "|Noncontrolling interests|(359)|". D03 line 645 (Q1) reads "|Noncontrolling interests|(225)|". Q2 = 359 − 225 = $134M.
4. Common stock dividends paid: D04 line 700, "|Common stock|(434)|", minus D03 line 644, "|Common stock|(218)|", gives Q2 = $216M.
5. Common stock buybacks: D04 line 702, "|Treasury stock purchases|(203)|", minus D03 line 646, "(93)", gives $110M. D04 states this directly at lines 43 and 363: "During second-quarter 2026, FCX purchased 1.7 million shares of its common stock for a total cost of $110 million".
6. Cash left after capex and NCI distributions: 2,048 − 1,104 − 134 = $810M.
7. Returns to common stockholders: 216 + 110 = $326M.
8. 326 / 810 = 0.40247, or 40.25%, which rounds to **40%**.

Exclusion: the Cerro Verde purchase is not a distribution to noncontrolling interests and not a buyback of Freeport stock. D04 line 39 says FCX "purchased 2.0 million shares of Cerro Verde common stock in the open market for $107 million", and line 692 books it under investing as "Acquisition of additional ownership interest in Cerro Verde|(107)". These are not Freeport's common shares, so the $107M is left out.

minimal_documents: D03 + D04. Both are needed because D04's cash flow statement covers six months only, so Q2 NCI distributions and Q2 dividends paid require subtracting D03's Q1 figures. No replacement was found: D01 and D02 (BHP) have zero matches for "Freeport" or "FCX". D04 alone cannot give the Q2 NCI distributions.

readings:
- Dividends declared instead of paid. D04 line 633 shows dividends payable of $218M at June 30, 2026, for $0.15/share. Then (218+110)/810 = 40.49%, still 40%.
- Small items that do not change the answer. Counting Q2 tax-withholding payments on stock awards (44−43 = 1) as buybacks gives 327/810 = 40.4%. Netting Q2 option-exercise proceeds (22−19 = 3) gives 323/810 = 39.9%. Both round to 40%.
- Readings I consider wrong, listed for the caller:
  - Treating the $107M Cerro Verde purchase as an NCI distribution: 326/703 = 46%.
  - Counting it as a buyback: 433/810 = 53%.
  - Using the rounded headline figures ($2.0B OCF, $1.1B capex): 326/766 = 43%. That is less precise than the exact figures available.
  - Using the six-month figures throughout: (434+203)/(3,543−2,077−359) = 637/1,107 = 58%.
  - Mixing six-month NCI and dividends with Q2 OCF and capex: (434+110)/(2,048−1,104−359) = 93%.
- Policy definition: the financial policy (D04 line 353) uses "available cash flows generated after planned capital spending and distributions to noncontrolling interests". The question says "capital expenditures", and no Q2 split between planned and discretionary capex is given, so I used total capex.

gaps: None that affect the answer. The documents are text extractions (manifest method "text", pages null), so there are no PDF pages or layout files to check. The tables read cleanly and cross-foot (OCF, capex and buybacks reconcile with directly stated Q2 figures). What I read:
- D04: lines 1-130, 290-382, 560-760 and 868-947.
- D03: lines 30-69, 355-386 and 598-659.
- Targeted greps across D03 and D04 (operating activities, capex, noncontrolling, distributions, dividends, treasury/repurchase).
- D01 and D02: only searched for "Freeport" and "FCX", with zero hits.

The rest of D03 and D04 (operating and segment detail, unit cost schedules) was not read in full.

contaminated: no. I received only the workspace root, packet path and question. The attached git-status context lists unrelated task files (aq-00949) and gave no answer or hint for this question.
