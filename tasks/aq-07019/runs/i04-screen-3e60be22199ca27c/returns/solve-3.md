# i04 strong-solver screen, solve 3 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

I found the answer: 37.4%. BHP doesn't print a Q4 FY25 energy coal price, so I worked it out from the two BHP reports. The derivation checks out against figures the reports do print.

answer: 37.4%

confidence: high

path:
1. **Quarter ended 30 June 2026 (Q4 FY26) price.** D02, Appendix 1 (line 206): "|Energy coal (US$/t)vi|117.74|11%|37%|112.15|17%|23%|104.28|(3%)|". The column headers (line 202) are "Q4 FY26|v Q3 FY26|v Q4 FY25|H2 FY26|v H1 FY26|v H2 FY25|FY26|v FY25". Footnote vi (line 218): "Export sales only. Includes energy coal sales from steelmaking coal mines." So Q4 FY26 = US$117.74/t. The 37% is only a rounded comparison.
2. **Full-year FY25 price.** D02 line 176: "Average realised price US$104.28/t ê3% FY25 US$107.80/t".
3. **Nine months to March FY25 (YTD Mar FY25) price.** D01 line 129: "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t". D01 footnote ii (line 157): "Export sales only. Includes thermal coal sales from steelmaking coal mines."
4. **Sales volumes in kt, BHP share.** The price weighting uses NSWEC export sales plus the BMA "Energy coal" sales row:
   - D01 line 424, NSWEC "Energy coal - Export": Jun 2025 quarter 3,554; YTD Mar 2025 10,015.
   - D01 line 419, BMA "Energy coal": Jun 2025 quarter 199; YTD Mar 2025 114.
   - D02 line 489, NSWEC export: Jun 2025 quarter 3,554; FY25 13,569.
   - D02 line 484, BMA energy coal: Jun 2025 quarter 199; FY25 313.
   - The figures tie together: 10,015 + 3,554 = 13,569 and 114 + 199 = 313.
   - Volume basis: YTD Mar FY25 = 10,129; Q4 FY25 = 3,753; FY25 = 13,882.
5. **Q4 FY25 price.**
   - 107.80 × 13,882 = 1,496,479.6
   - 115.99 × 10,129 = 1,174,862.71
   - Difference = 321,616.89; divided by 3,753 = US$85.696/t (about 85.70).
6. **Percentage.** 117.74 / 85.696 − 1 = 37.39%, which is 37.4%. Rounding Q4 FY25 to 85.70 first gives the same result. This agrees with the printed rounded "37%".
7. **Checks that the volume basis is right (NSWEC export plus BMA at BHP share):**
   - FY26: (99.04 × 11,839 + 117.74 × 4,607) / 16,446 = 104.278, against 104.28 printed.
   - H2 FY26: (105.61 × 3,945 + 117.74 × 4,607) / 8,552 = 112.14, against 112.15 printed. The 0.01 gap is consistent with rounding.
   - With NSWEC volumes only, the same checks give FY26 = 104.01 and H2 = 111.89, so that basis fails.
   - With BMA at 100%, H2 = 112.38, which also fails.
   - Q3 FY25 is about 97.79 (105.61 / 1.08). That gives H2 FY25 of about 91.27, and 112.15 / 91.27 is about 23%, matching D02.
8. **Rounding sensitivity.** Prices are rounded to the cent and volumes to the kt. That puts Q4 FY25 between about 85.66 and 85.73, so the result is 37.3–37.5% at the extremes and 37.4% in the centre.

minimal_documents: D01 and D02, with no alternatives.
- D01 is the only source of the exact YTD Mar FY25 price (115.99).
- D02 is the only source of Q4 FY26 (117.74) and FY25 (107.80).
- D03 and D04 (Freeport-McMoRan) contain no coal data; a search for "coal" found nothing in them.

readings:
- Using only NSWEC export volumes, which ignores footnote vi, gives Q4 FY25 ≈ 84.72 and **39.0%**. This fails the internal checks.
- Weighting by all NSWEC sales including domestic, which contradicts "Export sales only", gives Q4 FY25 ≈ 85.21 and **38.2%**.
- Counting BMA energy coal at 100% gives Q4 FY25 ≈ 86.57 and **36.0%**. This fails the H2 FY26 check.
- Quoting D02's printed comparison gives **37%**. That is a rounded figure, not a calculation from the two prices.
- Only 37.4% fits the footnote and every check.

gaps:
- No Q4 FY25 energy coal price is printed anywhere in the packet, so it has to be derived as above. The result assumes the FY25 and YTD Mar FY25 prices are consistent prior-year figures and that the volume basis is the one the checks confirmed.
- Prices are described as "provisional, unaudited estimates".
- The documents are text sources ("method": "text"), with no PDF page markers or layout files. Locations are therefore line numbers.
- In "é"/"ê", the letter stands for an up or down arrow.
- What I read:
  - D02: lines 1–110, 160–234 and 466–505.
  - D01: lines 115–174 and 402–441.
  - Searches across the whole packet for "energy coal", "thermal coal", NSWEC, "realised"/"realized", "Q4 FY25", "June 2025" and "US$…/t" prices.
  - D03 and D04 were only searched; they have no coal mentions.

contaminated: no. I received only the workspace path, the packet path and the question. The environment's git-status snapshot listed unrelated workspace filenames but nothing about this question.

Files: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\D01.txt and D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\D02.txt
