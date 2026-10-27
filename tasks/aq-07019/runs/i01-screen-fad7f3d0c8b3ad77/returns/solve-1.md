# i01 strong-solver screen, solve 1 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: US$85.7 per tonne. This is BHP's average realised energy coal price for Q4 FY25 (April to June 2025). It is calculated as the FY25 full-year price minus the nine months to March 2025, weighted by export sales volumes, and it includes energy coal sold from BMA.

confidence: high

path:
1. Definition (D02 line 218, Appendix 1 footnote vi): "Export sales only. Includes energy coal sales from steelmaking coal mines." D01 line 157 (footnote ii) says the same: "Export sales only. Includes thermal coal sales from steelmaking coal mines." So the volume that goes with the price is NSWEC export sales plus BMA's energy coal sales. Domestic sales are excluded.
2. FY25 price (D02 line 176, Energy coal panel): "Average realised price US$104.28/t ê3% FY25 US$107.80/t".
3. Price for the nine months to March 2025 (D01 line 129): "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t".
4. FY25 volumes, from the D02 sales "Year to date Jun 2025" column:
   - NSWEC export (line 489): "Energy coal - Export|kt|...|3,554|3,549|4,190|3,935|4,224|15,898|13,569|17%", so 13,569 kt.
   - BMA energy coal, BHP 50% share (line 484): "Energy coal|kt|...|199|44|111|10|383|548|313|75%", so 313 kt. As a check, 4,831 + 199 = 5,030, which is the BMA "Total", not the "Total (100%)" row.
5. Volumes for the nine months to March 2025, from the D01 sales "Year to date Mar 2025" column:
   - NSWEC export (line 424): "...|3,128|3,554|3,549|4,190|3,935|11,674|10,015|17%", so 10,015 kt.
   - BMA energy coal (line 419): "...|83|199|44|111|10|165|114|45%", so 114 kt.
   - The June 2025 quarter columns in D01 (3,554 and 199) match D02. Also 10,015 + 3,554 = 13,569 and 114 + 199 = 313.
6. Calculation (kt × US$/t gives US$ thousands):
   - FY25: 107.80 × (13,569 + 313 = 13,882) = 1,496,479.60
   - Nine months to March 2025: 115.99 × (10,015 + 114 = 10,129) = 1,174,862.71
   - Q4 FY25: 321,616.89 / 3,753 = 85.69595, which rounds to **85.7**
   - The printed prices are rounded to the cent, which moves the result by at most ±0.03, so the one-decimal answer is safe.
7. Checks that the volume basis is right:
   - Applying the same basis to FY26 gives (99.04 × 11,839 + 117.74 × 4,607) / 16,446 = 104.278, which matches the printed FY26 price of 104.28. Using NSWEC exports alone gives 104.008, which does not match.
   - D02 line 206 shows the Q4 FY26 price of 117.74 as "37%" above Q4 FY25. 117.74 / 85.696 is +37.4%, which fits. The NSWEC-only figure of 84.72 would imply +39%.
   - H2 FY26 recomputed from the two quarterly prices is 112.144, against 112.15 printed. That is within rounding.

minimal_documents: D01 and D02, which are both necessary.
- D01 is the only source for the US$115.99/t price for the nine months to March 2025 and the matching volumes.
- D02 is the only source for the FY25 price of US$107.80/t and the FY25 volumes.
- D03 and D04 are Freeport-McMoRan releases. A search found no mentions of "coal" or "BHP" in either, so neither can stand in for D01 or D02.

readings:
- NSWEC export sales only, leaving out BMA energy coal against footnote vi: (1,462,738.2 − 1,161,639.85) / 3,554 = 84.72, giving **84.7**. This conflicts with the FY26 check and the printed 37% change.
- Including domestic sales: (107.80 × 15,502 − 115.99 × 11,377) / 4,125 = 85.21, giving **85.2**. This contradicts "Export sales only."
- Backing out from D02's rounded "v Q4 FY25" change: 117.74 / 1.37 = 85.94, giving **85.9**. This relies on a rounded percentage, which the question rules out.
- BMA energy coal on a 100% basis (double the BHP share): about 86.57, giving **86.6**. This reading isn't defensible because the price reflects BHP's 50% share.

gaps:
- None of the documents states the Q4 FY25 price directly, so it has to be derived.
- Read: D01 lines 1–200, 225–269 and 395–454; D02 lines 1–240 and 290–509. The rest of D01 and D02 was covered only by searches for "energy coal", "thermal coal", "NSWEC", "Mt Arthur", "Q4 FY25", "H2 FY25", "115.99" and "107.80". D03 and D04 were only searched, for "coal" and "BHP", with no matches.
- The packet's sources are text files: the manifest shows method "text" and pages null, and there are no layout files or PDFs, so no page images were inspected.
- I checked the key quotes against the docs/ sources and they match:
  - D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i01-screen-fad7f3d0c8b3ad77\solver-1\docs\bhp-group-limited-operational-review-for-the-nine-months-ended-31-march-2026-form-6-k-filed-2026-04-22.txt (lines 136, 169, 446, 451)
  - D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-07019\runs\i01-screen-fad7f3d0c8b3ad77\solver-1\docs\bhp-group-limited-operational-review-for-the-year-ended-30-june-2026-form-6-k-filed-2026-07-17.txt (lines 185, 232, 513, 518)
- One header in D02's coal table is misprinted ("Dec 2026" at line 473). The other D02 tables read Dec 2025, and it does not affect the figures used.
- I did not read question.txt.

contaminated: no. No answer, reasoning, proposed lever or source hint was in my context. I can't independently confirm how this session was launched (non-fork or omitClaudeMd), but no project instructions or memory content appeared in it. The only auto-attached context was git status and a user email, neither related to this question.
