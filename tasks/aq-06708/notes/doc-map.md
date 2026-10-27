# aq-06708 - document map

Maintained by the caller from `text/` (navigation only; questions quote the documents, never this map).

## Bundle

- What it is: Pinterest (4) and Snap (3) filings, Q4 2025 to Q2 2026; both calendar fiscal years.
- Documents: 7; local ids from `text/manifest.json` (alphabetical), platform Doc numbers in brackets:
  D01 [Doc 2] Pinterest Q1 2026 release (May 4, 2026); D02 [Doc 4] Pinterest Q1 2026 10-Q (265K chars);
  D03 [Doc 1] Pinterest Q2 2026 release (Aug 4, 2026); D04 [Doc 3] Pinterest Q4/FY2025 release (Feb 12, 2026);
  D05 [Doc 6] Snap Q1 2026 release (May 6, 2026); D06 [Doc 5] Snap Q2 2026 release (Aug 3, 2026);
  D07 [Doc 7] Snap Q4/FY2025 release (Feb 4, 2026).
- Gaps: none. Capture complete, 7 of 7 in full, no gap markers (notes/intake.json). The Pinterest releases
  refer to an "About non-GAAP financial measures" section that the documents do not contain (D01 l.46,
  D03 l.48, D04 l.42); the 10-Q MD&A defines Adjusted EBITDA (D02 l.1039).
- Extraction: plain-text capture split unchanged; text/ = docs/ plus a header line. Tables are pipe
  tables; spot-checked D04 statements, D06 supplemental table, D02 Note 7 and Part II table: intact.
- Coverage: all six releases read in full; D02 read in full l.1-1340 (statements, notes, MD&A, Items 3-4)
  and l.2155-2394 (dual class risk factors, Part II Items 2, 5, 6); risk factors l.1340-2155 searched
  for figures and dated statements only.

## Pinterest

- D04: Q4 and FY2025 tables (l.27-38), CC revenue Q4 $1,305.9M / FY $4,205.3M with FX $13.5M / $16.5M
  (fn 1, l.40), user-geography table (l.48-62), Q1 2026 guidance (l.66), statements l.88-200,
  non-GAAP l.204-300 (payroll-tax exclusion began Q4 2024, fn 1 l.275; FY2025 non-cash charitable 13,495).
- D01: Q1 2026 vs Q1 2025 (l.29-40), CC $984.3M (fn 1 l.44), geography l.52-66, Q2 guidance l.70,
  statements l.92-211, non-GAAP l.217-290 (restructuring excluded from Adjusted EBITDA, fn 2 l.294).
- D03: Q2 2026 vs Q2 2025, three and six months (statements l.145-215: six-month columns give H1 2025);
  Q2 Adjusted EBITDA 2025 250,776 (l.39, l.279); CC $1,169.3M (fn 1 l.46); Q3 2026 guidance (l.72);
  buyback headline "over $2 billion ... average price of $18.17" (l.13); capped calls (99,187) l.209.
- D02 10-Q: ASR $1.0B, 41,279,670 shares in March, +13,516,943 at April settlement (Note 7 l.766-776,
  Note 13 l.902-904); Nov 2024 and Mar 2026 programs (l.743-764; Part II table l.2322-2328);
  tvScientific (Note 3 l.559-569); Notes (Note 5 l.620-662); restructuring plan and range
  (Note 11 l.872-890); revenue by billing address (Note 10 l.843-857) vs user geography (MD&A l.1110);
  Class B 20 votes, 76.3% voting power at Mar 31 (l.2163-2166); Canada DST benefit $15.4M (l.1154).
- Q3 2025 is printed in no document (FY less Q4 less H1). Q1-Q3 2025 FX is printed only as FY less Q4.

## Snap

- D07: Q4/FY2025 tables; $500M program (l.19); supplemental quarterly table Q3 2024-Q4 2025 (l.358-456);
  2024 restructuring $72.0M (fn 1 l.61, l.317-320); no constant-currency figures.
- D05: Q1 2026; supplemental Q4 2024-Q1 2026; geographic footnote reworded (l.352); no CC figures.
- D06: Q2 2026, three and six months; restructuring $128.5M (fn 1 l.43, l.237), SBC and D&A tables
  "include restructuring charges" (l.254, l.274); first CC Revenue definition (l.59) and reconciliation
  (l.279-284); supplemental Q1 2025-Q2 2026 with a backfilled Constant Currency Revenue row (l.314).
- Overlapping supplemental rows agree across D05-D07 (only the share-count YoY row changes precision).

## Shared ground (navigation only)

- Both: Adjusted EBITDA, free cash flow, restructuring in 2026, buybacks, convertible notes, capped calls.
- Constant currency: Pinterest in every release; Snap only from D06 (2025 quarters backfilled there).
