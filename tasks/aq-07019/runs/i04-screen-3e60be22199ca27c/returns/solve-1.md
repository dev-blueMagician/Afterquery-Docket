# i04 strong-solver screen, solve 1 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: 37.4% (Q4 FY26 US$117.74/t vs a derived Q4 FY25 price of about US$85.70/t)

confidence: medium-high. The method is checked against three printed figures, but the answer depends on deriving the Q4 FY25 price, because no document prints it.

path:
1. Q4 FY26 price. D02 (FY26 operational review), Appendix 1, line 206: "|Energy coal (US$/t)vi|117.74|11%|37%|112.15|17%|23%|104.28|(3%)|". The columns (line 202) are Q4 FY26 | v Q3 FY26 | v Q4 FY25 | H2 FY26 | v H1 FY26 | v H2 FY25 | FY26 | v FY25. The comparison with Q4 FY25 is printed only as a rounded "37%"; the Q4 FY25 price itself does not appear anywhere in the packet.
2. Price basis. D02 footnote vi (line 218): "Export sales only. Includes energy coal sales from steelmaking coal mines." D01's version (line 157) says "thermal coal", which is the same thing as energy coal.
3. FY25 full-year price. D02 line 176: "Average realised price US$104.28/t ê3% FY25 US$107.80/t".
4. Price for the nine months to March 2025. D01 (nine-month review) line 129: "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t".
5. Sales volumes in kt, BHP share. The price is weighted by NSWEC export sales plus BMA energy coal sales.
   - D02 line 489, "Energy coal - Export": Jun 2025 quarter 3,554; Jun 2026 quarter 4,224; FY26 15,898; FY25 13,569.
   - D02 line 484, BMA "Energy coal": Jun 2025 quarter 199; Jun 2026 quarter 383; FY26 548; FY25 313.
   - D01 lines 424 and 419, nine months to March 2025: export 10,015 and BMA 114. These equal FY25 minus Q4 FY25, so the figures are consistent.
   - Combined volumes: FY25 13,882; nine months to March 2025 10,129; Q4 FY25 3,753.
6. Q4 FY25 price = (107.80 × 13,882 − 115.99 × 10,129) / 3,753 = (1,496,479.60 − 1,174,862.71) / 3,753 = 321,616.89 / 3,753 = US$85.696/t.
7. Increase = 117.74 / 85.696 − 1 = 0.37393, which is 37.4%.
8. Checks on the weighting method:
   - FY26 rebuilt from the nine months to March 2026 and Q4 FY26: (99.04 × 11,839 + 117.74 × 4,607) / 16,446 = 104.278. D02 prints 104.28. Using NSWEC exports only gives 104.01, which does not match.
   - H2 FY26: (105.61 × 3,945 + 117.74 × 4,607) / 8,552 = 112.144. D02 prints 112.15, a difference within rounding.
   - H2 FY26 against H1 FY26 (derived at 95.76) gives 17%, as printed.
   - 37.4% is consistent with the printed "37%".
9. Rounding sensitivity: the 107.80 and 115.99 inputs are rounded to the cent (±0.005 each), so Q4 FY25 falls between 85.664 and 85.728. That gives a range of 37.34% to 37.44%. The central value of 37.39% rounds to 37.4%; only the extreme edge of the range would round to 37.3%.

minimal_documents: D01 + D02.
- D02 supplies 117.74, 107.80 and all the volumes. D01 supplies only the 115.99 price for the nine months to March 2025.
- Neither document is enough alone. D02 gives only rounded comparisons for H2 FY25 and Q4 FY25 (23% and 37%), which are not precise enough for one decimal place. D01 lacks both Q4 FY26 and FY25.
- D03 and D04 (Freeport) contain no coal data, so they cannot replace either document.

readings:
- NSWEC export volumes only, leaving out the BMA energy coal: Q4 FY25 = 301,098.35 / 3,554 = 84.72, giving 39.0%. This is weak: it contradicts footnote vi, does not reproduce FY26 (104.01 against 104.28), and does not match the printed 37%.
- All NSWEC sales including domestic, plus BMA: Q4 FY25 = 85.21, giving 38.2%. This contradicts "Export sales only".
- Taking the printed 37% (37.0%) is circular, because it does not calculate from the two prices as the question asks.
- Mistakenly using the FY25 full-year price of 107.80 as the Q4 FY25 price gives 9.2%. That is not a valid reading.

gaps:
- No document states the Q4 FY25 price directly, so it has to be derived. The derivation assumes BHP's average is weighted by sales volume over NSWEC exports plus BMA energy coal sales. This is inferred from footnote vi and confirmed by the three checks, not stated outright.
- The comparative prices may include later provisional-pricing adjustments, which are not disclosed.
- The source's sales column header reads "Dec 2026" (D02 line 473), a typo for Dec 2025; it does not affect the calculation.
- I did not read D03 and D04 in full; a search of both for "coal" returned nothing.
- I read only the relevant parts of D01 and D02, and searched all text for "energy coal", "realised", "thermal coal" and US$/t figures.
- There are no layout files or PDFs. The sources are plain text, and the decisive numbers match the docs\ originals: the D01 source at lines 136, 164, 446 and 451, and the D02 source at lines 185, 219, 513 and 518.

contaminated: no

Packet: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\ (D01.txt, D02.txt)
