# i04 strong-solver screen, solve 2 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: 37.4%

confidence: high. The Q4 FY25 price is never printed in the packet, so I derived it, and I checked the derivation against three printed figures (see path).

path:
1. Price for the quarter ended 30 June 2026 (Q4 FY26). D02 line 206, Appendix 1 "Average realised prices". Header: "Q4 FY26|v Q3 FY26|v Q4 FY25|H2 FY26|v H1 FY26|v H2 FY25|FY26|v FY25". Row: "Energy coal (US$/t)vi|117.74|11%|37%|112.15|17%|23%|104.28|(3%)". So Q4 FY26 = US$117.74/t. The packet gives the June 2025 quarter only as a rounded "37%", never as a dollar price. I searched for "Q4 FY25", "Jun 2025", "H2 FY25" and price values between 84 and 87.
2. Full-year FY25 price. D02 line 176: "Average realised price US$104.28/t ê3% FY25 US$107.80/t".
3. Nine-month price to March 2025. D01 line 129: "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t".
4. Which sales the price covers. D02 line 218, footnote vi: "Export sales only. Includes energy coal sales from steelmaking coal mines." D01 line 157 says the same, using "thermal coal".
5. Sales volumes in kt, BHP share:
   - NSWEC "Energy coal - Export": June 2025 quarter 3,554 and YTD Mar 2025 10,015 (D01 line 424); FY25 13,569 (D02 line 489).
   - BMA "Energy coal" sales: June 2025 quarter 199 and YTD Mar 2025 114 (D01 line 419); FY25 313 (D02 line 484).
   - Combined weights: nine months to March 2025 = 10,129; Q4 FY25 = 3,753; FY25 = 13,882. The two parts add up to the full year.
6. Q4 FY25 = (107.80×13,882 − 115.99×10,129)/3,753 = (1,496,479.60 − 1,174,862.71)/3,753 = 321,616.89/3,753 = US$85.696, which rounds to US$85.70/t.
7. 117.74/85.70 − 1 = 0.37386, so 37.4%. Using the unrounded 85.696 gives 37.393%, also 37.4%.

Checks that this weighting method is right:
- It reproduces the printed FY26 price: (99.04×11,839 + 117.74×4,607)/16,446 = 104.278, printed as 104.28. Using NSWEC export volumes only gives 104.01, which does not match.
- It reproduces the printed H2 FY26 price: (105.61×3,945 + 117.74×4,607)/8,552 = 112.14, printed as 112.15.
- The result agrees with the printed "37%" for Q4 FY26 against Q4 FY25. The implied H2 FY25 price (about 91.1–91.5) also agrees with the printed "23%".

Rounding range: if 107.80 and 115.99 each carry ±0.005 of rounding, Q4 FY25 falls between 85.664 and 85.728. That puts the answer between 37.34% and 37.44%. Only a small extreme corner of that range (about 1–2%) would round to 37.3%.

minimal_documents: D01 + D02. D01 is the only source of the nine-month FY25 price (115.99). D02 is the only source of 117.74 and 107.80. The volumes are in both documents: the YTD Mar 2025 volumes can be taken as D02's FY25 total minus its June 2025 quarter. D03 and D04 (Freeport-McMoRan) do not mention BHP or coal at all, so they cannot replace either document.

readings:
- Take the printed rounded comparative ("37%", D02 line 206), or back-solve Q4 FY25 = 117.74/1.37 = 85.94: answer 37.0%. This is circular rather than calculated from two separately established prices.
- Weight by NSWEC export sales only, ignoring footnote vi: Q4 FY25 = 107.80 − 8.19×(10,015/3,554) = 84.72, giving 39.0%. This contradicts the printed 37%.
- Include NSWEC domestic sales as well: Q4 FY25 = 85.21, giving 38.2%. This contradicts both "Export sales only" and the printed 37%.
- Ignore volumes and treat the quarters as equal: 4×107.80 − 3×115.99 = 83.23, giving 41.5%. This contradicts the printed 37%.

gaps:
- The Q4 FY25 price is not printed in the packet. It is derived on the assumption that the reported BHP-share volumes (NSWEC export plus BMA energy coal) are the price weights. The checks above support this.
- I read only the relevant sections of D01 and D02 (summaries, energy coal sections, Appendix 1 price tables, coal sales tables). I checked D03 and D04 only by search (no hits for "BHP" or "coal").
- The packet has no PDFs or Dnn.layout.txt files (the manifest lists method "text" and no page markers), so I could not check any original page.
- Files used:
  - D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\D01.txt
  - D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\D02.txt
  - D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i04-screen-3e60be22199ca27c\solver-1\text\manifest.json

contaminated: no
