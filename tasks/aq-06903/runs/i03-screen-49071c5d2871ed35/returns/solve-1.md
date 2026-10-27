# i03 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i03 blind solve 1")

Judged by the author against gold 40%: RIGHT.

answer: 40%

confidence: high

path:
1. Q2 2026 operating cash flow is $2,048M. D04 (the FCX 2Q26 release), Summary Financial Data table, "Three Months Ended June 30" 2026 column: "|Operating cash flowse|$2,048|$2,195|$3,543|$3,253|" (text/D04.txt line 62). Cross-check: 3,543 for six months (D04 cash flow statement, line 684) minus 1,495 for Q1 (D03 line 629) = 2,048.
2. Q2 2026 capital expenditures are $1,104M. D04 line 63: "|Capital expenditures|$1,104|$1,261|$2,077|$2,433|". Cross-check: 2,077 minus 973 for Q1 (D03 line 63, and the Q1 segment lines 244+114+456+29+130=973) = 1,104.
3. Q2 distributions to noncontrolling interests are $134M. The D04 cash flow statement covers six months only ("Six Months Ended June 30"). Under "Cash dividends and distributions paid", it shows "|Noncontrolling interests|(359)|(625)|" (line 701). The D03 cash flow statement covers the three months ended March 31, 2026, and shows "|Noncontrolling interests|(225)|—|" (line 645). Q2 = 359 − 225 = 134.
4. Q2 cash dividends paid on common stock are $216M. D04 line 700 shows "|Common stock|(434)|(433)|" and D03 line 644 shows "|Common stock|(218)|(218)|". Q2 = 434 − 218 = 216.
5. Q2 buybacks are $110M. D04 line 363 says: "During second-quarter 2026, FCX purchased 1.7 million shares of its common stock for a total cost of $110 million". This matches treasury stock purchases of (203) for six months (D04 line 702) minus (93) for Q1 (D03 line 646) = 110.
6. Cash flow left after capex and NCI distributions = 2,048 − 1,104 − 134 = 810.
7. Returns to common stockholders = 216 + 110 = 326.
8. 326 / 810 = 0.40247, which rounds to 40%.
The measure matches FCX's own policy wording in D04 line 353: "up to 50% of available cash flows generated after planned capital spending and distributions to noncontrolling interests would be allocated to common stockholder returns".
I checked the six-month and Q1 rows against the original files in docs/ (2Q file lines 723–725, 1Q file lines 665–667), and the figures are the same.

minimal_documents: D03 + D04. D04 alone is not enough because it gives only six-month figures for NCI distributions and dividends paid. D01 and D02 (BHP operational reviews) are irrelevant and cannot stand in for either one.

readings:
- Using dividends declared in Q2 instead of dividends paid: the $0.15/share declared June 24 gives $218M payable at June 30 (D04 line 633). (218+110)/810 = 40.49%, still 40%. This is close to the rounding boundary: the 41% cutoff is 40.5% × 810 = 328.05.
- Also counting Q2 "Payments for withholding of employee taxes related to stock-based awards" (44 − 43 = 1) as buybacks: dividends paid give 327/810 = 40.4% (40%), but dividends declared give 329/810 = 40.6% (41%). This is a weak reading, since tax withholding is not a stock buyback.
- Also subtracting the Q2 "Acquisition of additional ownership interest in Cerro Verde" (107, D04 line 692): 326/703 = 46%. Not supported, because this was an open-market purchase recorded in investing activities, not a distribution to NCI.
- Using the rounded narrative figures ($2.0B OCF, $1.1B capex): 326/766 = 43%. Less precise, so inferior.
- Wrong-period or wrong-concept errors: six-month figures give 637/1,107 = 58%; Q2 figures with the six-month NCI total (359) give 56%; using NCI net income ($407M) instead of distributions gives 326/537 = 61%.

gaps:
- No Q2-only cash flow statement exists, so the Q2 NCI distributions and dividends paid are derived as six months minus Q1.
- The manifest lists every document as "method: text", with no PDF pages or layout files, so there was no page image to inspect.
- I read D04 and D03 in part: the summaries, the liquidity, financial policy and noncontrolling-interest sections, and the income statement, balance sheet and cash flow statement. I did not read the segment and product-cost schedules in full.
- I did not read D01 or D02 in full. A search for "Freeport|FCX|noncontrolling|non-controlling" in them found only a BHP line ("Dividends paid to non-controlling interests|~1,400").
- I did not read question.txt.

contaminated: no
