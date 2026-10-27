# i01 blind solve 1 (fresh blind-solver, 2026-10-18) - judged RIGHT

Raw return, verbatim:

answer: 3.7 (billion dollars): Katrina NFIP payments of over $15.7 billion minus about $12 billion paid since the program began, as stated in April 2005.

confidence: high

path:
1. Lifetime total to April 2005: D02, GAO-05-532T, testimony "Thursday, April 14, 2005" (text/D02.txt lines 13, 45: "DATE: 04/14/2005"). Line 96: "Since its inception, the program has paid about $12 billion in insurance claims, primarily from policyholder premiums..." (same sentence at line 94 of docs/gaoreports_gao_05_532t.txt). Line 82: established "Under the National Flood Insurance Act of 1968", so "since its inception" = entire history.
2. Katrina payments: D09, GAO-08-28, Dec. 28, 2007. Line 185: "FEMA estimated that NFIP had paid over $15.7 billion in flood insurance claims from Hurricane Katrina as of August 31, 2007, encompassing approximately 99 percent of all flood claims received." Footnote 21 (line 311) agrees: "FEMA estimates that Hurricane Katrina alone accounts for over $15.7 billion in flood insurance claims."
3. Not used: D09 line 304, combined Katrina and Rita: "For both Hurricanes Katrina and Rita, FEMA estimates that NFIP has paid approximately $16.2 billion in claims". The question asks about Katrina alone.
4. Calculation: 15.7 − 12.0 = 3.7 billion dollars, already one decimal. Inputs rounded ("over" $15.7B, "about" $12B), so 3.7 is a lower bound.
5. D02 line 101: the 2004 hurricanes produced "59,125 NFIP claims for more than $1.3 billion in payments as of March 2005." A single season, not a lifetime total; adding it to the $12B would probably double count, the $12B being a since-inception figure stated in April 2005.

minimal_documents: D02 + D09. No substitute for either: only D02 and D09 contain "flood" or "NFIP" at all (case-insensitive: 76 hits in D02, 100 in D09, none in D01 or D03–D08). D02 is the only source for the lifetime total and D09 the only source for Katrina payments.

readings:
- Main: Katrina alone (15.7) − since-inception total (12) = 3.7.
- Katrina plus Rita: 16.2 − 12 = 4.2. Does not match the question (Katrina only).
- Adding the 2004 hurricanes to the lifetime total: 15.7 − (12 + 1.3) = 2.4. Not supported (probable double count).
- Treating $15.7B as 99 percent of an eventual total: 15.7 / 0.99 ≈ 15.86, minus 12 ≈ 3.9. Not supported: the 99 percent is tied to "flood claims received", not dollars, and the question asks what was paid.
- No defensible reading changes the main answer.

gaps:
- D02 Appendix I, Figure 1 ("Total NFIP Payments to Claimants, 1972-2004", data "as of February 28, 2005") lost its bar values; text/ and docs/ .txt keep only axis labels, and the packet has no PDF. Could not total the yearly payments as a cross-check on the $12B. Not blocking: D02 states the since-inception total directly.
- Coverage: text/D02.txt and text/D09.txt read in full. D01, D03–D08 checked only by search: "flood/NFIP" (no hits), "Katrina" (3 unrelated hits in D05, lines 173, 203, 265, on insurer claim operations and NAIC), "April 2005" (D02 only), inception/history terms, and title lines. Not read in full.
- Packet question.txt not opened, per instructions.

contaminated: no

Packet: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i01-screen-7614748bfbc01ec2\solver-1 (decisive files: text\D02.txt, text\D09.txt)
