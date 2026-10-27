# aq-05821 - cross-document hooks

Bundle: ten 10-Q MD&A excerpts, Q1 and Q2 2026, for Marriott (D07, D08), Hilton (D05, D06), Hyatt
(D03, D04), Wyndham (D09, D10) and Choice Hotels (D01, D02). Local ids are alphabetical by file name;
platform Doc numbers are in `intake.json` (Marriott Doc 1/6, Hilton 2/7, Hyatt 3/8, Wyndham 4/9,
Choice 5/10). All five use calendar years. Each Q2 document prints six-month columns for every
income-statement item it shows, so a Q1 document is needed only for March 31 balances, Q1 cash
flows (Q2 documents print only six-month cash flows) and Q1-only narrative.

Target: hard (user, 2026-10-16: no Easy or Medium slot; page: Hard 0/5, Medium closed, Easy 0/0).
Playbook constraint: finding or rebuilding printed figures is cleared by the High model; design
from a judgment a default reading gets wrong.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D08 six-month columns of every income-statement table (fee revenues l.140, owned/leased l.153-157, cost reimbursements l.166-168, other operating expenses l.177-181, non-operating l.195-199, taxes l.207); D02 l.177; D06 l.159; D04 l.531; D10 l.187 | Marriott never prints net income in either MD&A (0 hits); its captions give H1 2026 1,414 vs H1 2025 1,428, a fall, although fees, operating income (2,293 vs 2,184) and pre-tax income (1,902 vs 1,818) rose. Cost reimbursements net (134) vs (9) and tax 488 vs 390 (prior-year reserve release) decide it. Which companies earned less H1 net income: Choice Hotels, Marriott | figure that must be computed; parallel rule (Hilton's Adjusted EBITDA and Marriott's own "not designed to impact our economics" leave reimbursed programs out; net income keeps them) | decoy Wyndham (net revenues fell 702 vs 713, net income rose 163 vs 149); counterfactual: reimbursements left out gives Marriott 1,548 vs 1,437 (rise), pre-tax gives a rise, so the answer becomes Choice Hotels | D08 tax prose says "higher pre-tax income ($42 million)", not the derived +84; table lines govern. Marriott quotes sit past 20,000 characters in D08 (form-number WARN) | sketch i01 |
| h2 | Q2 operating cash flow = six months (D02 l.240, D04 l.560, D06 l.320, D08 l.266, D10 l.337) minus Q1 (D01 l.166 "used ... $23.2 million", D03 l.380, D05 l.306, D07 l.215, D09 l.237); Q2 net income D02 l.73, D04 l.513, D06 l.159, D10 l.105, Marriott derived 766 | Q2 2026 cash from operations below net income: Hilton 472 vs 482, Hyatt 50 vs 110, Wyndham 91 vs 102; not Choice 90.6 vs 64.3, Marriott 948 vs 766. The six-month view reverses Hilton and Choice | a period no document reports on its own, across ten documents | lure from six-month figures: Choice, Wyndham; Choice's Q1 outflow read as an inflow gives 44.2 and adds Choice | breadth, not a single judgment; ten necessary documents | sketch i02 |
| h3 | D01 l.173 / D02 l.251: franchisee loan repayments $24.6 million for Q1 and for six months | Q2 2026 repayments were nil | period not reported alone; printed six-month lure 24.6 | not applicable | rebuild kind (playbook section 3) | held |
| h4 | D05 development table (Q1 openings 131, net additions 102) / D06 (H1 338, 288) | Q2 hotels removed 21 (lures 50, 29) | rebuild | not applicable | rebuild kind; "openings minus net additions" is an inference | held |
| h5 | D03 "approximately $543 million remaining"; D04 "$1,531 million remaining", Q2 buybacks $12 million | implied new authorization about $1.0 billion | reconciled observation not printed | not applicable | a question would assert an authorization no document states | rejected |
| h6 | D07/D08 Owned/Leased 51 → 50 properties, 14,406 → 13,333 rooms; D08 YoY column (873) | Q2 owned/leased rooms fell 1,073 (lure 873) | rebuild | not applicable | rebuild kind | held |

Rejected families: covenant headroom (definitions and step-up elections not in the bundle);
excise-tax-consistent buyback comparisons (tax amounts not given); Wyndham Q1/H1 2025 derivations
(the documents disagree by 1-2 on several 2025 lines); Hyatt comparable-hotel counts (1,218 less 8
removals ≠ 1,212); per-share buyback prices (share counts rounded).
