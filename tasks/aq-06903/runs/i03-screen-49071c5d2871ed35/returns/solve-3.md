# i03 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i03 blind solve 3")

Judged by the author against gold 40%: RIGHT.

answer: 40%

confidence: high

path:
The question asks for Q2 2026 (three months ended June 30, 2026), in US$ millions: (common dividends paid + stock buybacks) ÷ (operating cash flow − capex − distributions to noncontrolling interests (NCI)), rounded to the nearest whole percent. D04's cash flow statement only covers six months, so the Q2 dividend and NCI figures come from subtracting D03's Q1 statement.

1. Q2 operating cash flow = 2,048. D04 Summary Financial Data, three months 2026 column: "|Operating cash flowse|$2,048|$2,195|$3,543|$3,253|". Cross-check against the cash flow statements: D04 six months "Net cash provided by operating activities|3,543" minus D03 Q1 "Net cash provided by operating activities|1,495|1,058|" = 2,048.
2. Q2 capex = 1,104. D04 summary: "|Capital expenditures|$1,104|$1,261|$2,077|$2,433|". Cross-check: the D04 six-month capex lines (496+285+972+49+275 = 2,077) minus the D03 Q1 lines (244+114+456+29+130 = 973) = 1,104.
3. Q2 NCI distributions = 134. Under "Cash dividends and distributions paid", D04 six months has "|Noncontrolling interests|(359)|(625)|" and D03 Q1 has "|Noncontrolling interests|(225)|—|". 359 − 225 = 134. D04 gives no direct Q2 figure; its "Noncontrolling Interests" section covers only income attributable to NCI.
4. Q2 common dividends paid = 216. D04 six months "|Common stock|(434)|(433)|" minus D03 Q1 "|Common stock|(218)|(218)|" = 216. This is the March 25 declaration "which will be paid on May 1, 2026" (D03, Common Stock Dividends), so it was paid in Q2.
5. Q2 buybacks = 110. D04: "During second-quarter 2026, FCX purchased 1.7 million shares of its common stock for a total cost of $110 million". Cross-check: treasury stock purchases of 203 (D04, six months) − 93 (D03, Q1) = 110.
6. Cash left over = 2,048 − 1,104 − 134 = 810. Returns to common stockholders = 216 + 110 = 326. 326 / 810 = 0.40247, which rounds to 40%.

The question's wording follows the financial policy text in D04: "up to 50% of available cash flows generated after planned capital spending and distributions to noncontrolling interests would be allocated to common stockholder returns". I checked the key cash flow rows against the docs/ source files and they match (D04 source lines 723–725, D03 source lines 665–667).

minimal_documents: D03 + D04. D04 alone is not enough: it has no Q2 split for NCI distributions or dividends paid, so the Q1 subtraction needs D03. There is no substitute: D01 and D02 are BHP operational reviews, and a search for "freeport|FCX" in both found 0 matches.

readings:
- Declared-dividend basis (D04 June 30 "Dividends payable - common stock|218", or $0.15 × about 1,443M shares ≈ 216): (218 + 110)/810 = 40.5%, so still 40%.
- Counting the Q2 "Acquisition of additional ownership interest in Cerro Verde (107)" as an NCI-related deduction: 326/703 = 46.4%, giving 46%. The question names only capex and NCI distributions, so this reading isn't supported.
- Using six-month figures by mistake: (434 + 203)/(3,543 − 2,077 − 359) = 637/1,107 = 57.5%, giving 58%. Wrong period.
- Using the rounded headline figures ($2.0B operating cash flow, $1.1B capex): 326/766 ≈ 42.6%, giving 43%. This loses precision and isn't preferred.
- Adding the Q2 "payments for withholding of employee taxes" (44 − 43 = 1) to returns: 327/810 = 40.4%, still 40%. These payments aren't buybacks anyway.

gaps: I did not read D01 or D02 beyond confirming they have no Freeport/FCX mentions. The extraction method is text with no PDF pages, and the tables extracted cleanly, so there was nothing to check against an original page. I did not read question.txt. No other gaps.

contaminated: no
