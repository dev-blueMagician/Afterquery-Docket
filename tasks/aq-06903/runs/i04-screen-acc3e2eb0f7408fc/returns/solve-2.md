# i04 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i04 blind solve 2")

Judged by the author against gold 27: RIGHT.

answer: 27 US cents per pound. BHP's H2 FY26 average realised copper price was US$6.21/lb. The six-month LME average, worked out from Freeport's two quarterly averages, is US$5.94/lb.

confidence: high

path:
1. The period maps to BHP's H2 FY26. D02 line 47 says "Operational review for the year ended 30 June 2026", and line 97 says "the second half of FY26 (H2 FY26)". D01 covers the "nine months ended 31 March 2026" ("YTD Mar FY26"), so FY26 started on 1 July 2025. H2 FY26 is therefore 1 January to 30 June 2026.
2. BHP figure: D02 Appendix 1, "Average realised prices", line 203: "|Copper (US$/lb)ii, iii|6.53|11%|47%|6.21|18%|38%|5.74|35%|". The columns (line 202) are Q4 FY26, v Q3 FY26, v Q4 FY25, H2 FY26, v H1 FY26, v H2 FY25, FY26, v FY25. So H2 FY26 = US$6.21/lb. Footnote i says this is a "weighted average of various sales terms" and "Includes the impact of provisional pricing and finalisation adjustments."
3. LME for Q1 2026: D03 line 737 says sales are "generally based on quoted LME monthly average settlement copper prices, which averaged $5.83 per pound in first-quarter 2026".
4. LME for Q2 2026: D04 line 835 says "...LME monthly average settlement copper prices, which averaged $6.05 per pound in second-quarter 2026".
5. Neither Freeport release gives a six-month LME average. D04 mentions LME on only three lines: 833 (no figure), 835 (Q2 $6.05) and 871 (the 22 July spot price of $6.30 and the provisional price of $6.07). D04 does not repeat the Q1 figure.
6. Six-month average: (5.83 + 6.05) / 2 = 11.88 / 2 = 5.94 $/lb. Weighting each quarter by its three months gives the same result.
7. Difference: 6.21 − 5.94 = 0.27 $/lb = 27 US cents/lb.
8. Rounding check: every input is printed to the cent, so the true value lies roughly between 26.5 and 27.5 cents. That still rounds to 27.
9. Consistency check: D01 line 150 gives Q3 FY26 copper at 5.86. Then 6.53 / 5.86 = 1.114, which matches D02's "v Q3 FY26 11%".

minimal_documents: D02 + D03 + D04. D02 alone has BHP's H2 FY26 figure, D03 alone has the Q1 2026 LME average and D04 alone has the Q2 2026 LME average. D01 is not needed for the main answer; it only supports the alternative reading below. I found no document that could replace any of the three.

readings:
- Building BHP's Jan–Jun figure from its two quarters instead of using the printed H2 figure. Q3 FY26 is 5.86 (D01 line 150) and Q4 FY26 is 6.53 (D02 line 203). Their simple average is (5.86 + 6.53) / 2 = 6.195, and 6.195 − 5.94 = 25.5 cents (about 25–26). This reading is weaker: BHP prints the H2 FY26 figure directly, and it is volume-weighted.
- Comparing quarter by quarter and averaging the gaps. Q3: 5.86 − 5.83 = 3 cents. Q4: 6.53 − 6.05 = 48 cents. The average is 25.5 cents. This has the same weakness.
- Using the wrong period or index (FY26 at 5.74, Q4 alone, or COMEX at $5.79 and $6.16) does not answer the question as asked.

gaps:
- The six-month LME average is worked out, not printed. No document gives a trading-day-weighted or reported half-year LME average.
- The packet has no PDFs (manifest method "text", pages null) and no layout files, so I could not check against original pages. Nothing appeared to be lost in extraction for the rows used.
- I did not read the documents in full. I searched all four for LME, London, settlement, averaged, copper price, realised/realized, H2/half/six months and US$/lb. I read D01 lines 140–164; D02 lines 1–60 and 190–229; D03 lines 150–194, 713–716 and 725–759; and D04 lines 120–131, 150–191, 376–385, 750–761 and 820–879.

contaminated: no
