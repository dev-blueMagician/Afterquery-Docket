# aq-06903 - document map

Navigation only, like the form's bundle overview; questions quote the documents, never this map.

## Bundle

- What it is: the same four documents as aq-01189 (user confirmed a fresh Hard design, 2026-10-18):
  BHP Group operational reviews for the nine months to 31 March 2026 (D01 = Doc 3, 22 April 2026)
  and the year to 30 June 2026 (D02 = Doc 4, 16 July 2026); Freeport (NYSE: FCX) results releases
  for Q1 2026 (D03 = Doc 1, April 23, 2026) and Q2 / six months 2026 (D04 = Doc 2, July 23, 2026).
- Reuse binding: text content equals aq-01189's text/ after removing that capture's ```text fence
  lines and one escaped rule line per document (diff checked 2026-10-19, all four documents), so
  [aq-01189's map](../../aq-01189/notes/doc-map.md) applies as navigation. Its line numbers are
  aq-01189 text lines; here lines shift up by the number of fence lines above (about 2 per table).
  Source sha256 (this capture): D01 17b6e303..., D02 049ae9f6..., D03 ddaee19d..., D04 b7d6083a...
  (notes/intake.json); corpus 08cf7d356a5a9d94 (notes/mine.md).
- Gaps: none in the capture (4 of 4 read in full; gap_characters 0). Italics flagged by BHP as
  meaningful are not visible in text (D01 89/170/218, D02 231/279); the overlapping Appendix 2
  quarters (900 cells, Jun 2025-Mar 2026) and FY25 comparatives match across editions, so no
  restated figure exists to be hidden by lost italics (scratchpad cmp_bhp2.py / cmp_fy25b.py).
- Read coverage this session: D03 and D04 main text and all tables read in full (D04 product
  schedules by grep of headers, totals, unit lines and notes); D01 and D02 read in full to D02
  line 522 (Appendix 3, Ministers North JORC tables, skimmed via aq-01189's map only).

## Locations used by the sketches (this capture's line numbers)

- FCX full-year 2026 estimates and price decks: D03 29-43, 118-132, 185-189, 219-223, 300-306,
  320-326; D04 25-37, 118-132, 179-185, 213-221, 290-296, 310-316. Operating cash flow estimate
  with working capital and sensitivities: D03 322, D04 312.
- FCX cash flow statements: D03 602-654 (three months), D04 655-711 (six months only).
- FCX silver: product-schedule notes only; D04 six months 2026 at 1181 (U.S.), 1393 (South
  America), 1614 (Indonesia); Q2 2026 at 1075, 1287, 1497; D03 Q1 at 1009, 1116 (the U.S. Q1 note,
  903, gives no volume).
- LME / COMEX averages: D03 737 (Q1), D04 835 (Q2); LME spot D03 753 (April 22), D04 871 (July 22).
- BHP realised prices: D01 145-157 (Q3 FY26, YTD Mar FY26), D02 198-218 (Q4, H2, FY26).
- BHP Appendix 2 silver: D01 242-249, D02 303-310; quarter headers D01 210-214, D02 271-275.
- BHP exploration: D01 202 (YTD March FY26), D02 263 (FY26).
