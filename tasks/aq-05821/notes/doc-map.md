# aq-05821 - document map

Navigation only; questions quote the documents, never this map.

## Bundle

- What it is: ten 10-Q MD&A excerpts (Item 2 only), quarters ended March 31 and June 30, 2026, for
  five lodging companies. Calendar fiscal years throughout.
- Documents: 10; local ids alphabetical by file (`text/manifest.json`); platform Doc numbers in
  `notes/intake.json`: Marriott Doc 1 (D07) / Doc 6 (D08), Hilton Doc 2 (D05) / Doc 7 (D06), Hyatt
  Doc 3 (D03) / Doc 8 (D04), Wyndham Doc 4 (D09) / Doc 9 (D10), Choice Doc 5 (D01) / Doc 10 (D02).
- Gaps: none. Capture `AQ-05821_2026-10-16_0844.txt` says "10 of 10 read in full (423,879
  characters)"; it carries the page's "Docket has been updated. Reload this page" notice (stale-page
  warning, not a document gap). The 2026-10-15 21:45 capture is byte-identical in the documents.
- Extraction spot-checks: plain-text sources; extracted text matches the capture apart from a
  header line (character counts within 6 per document). Tables are pipe-flattened rows; each
  checked table (Marriott fee revenues, Hilton reconciliation, Choice income statement) reads
  correctly row by row.
- Coverage: all ten documents read in full by the author on 2026-10-16.

## Per document (key locations)

- D07 Marriott Q1 (21,886 chars): comparable-property definition l.22; system and pipeline l.33-35;
  properties by ownership l.47-56; RevPAR tables l.64-89; fee, owned/leased, cost-reimbursement,
  other-expense, non-operating and tax tables l.97-160 (no net income line anywhere); segments
  l.165-202; credit facility and covenant l.208-209; cash summary l.215; capex outlook l.221;
  buybacks to April 29 l.224; dividend l.226.
- D08 Marriott Q2 (27,303): same layout with three- and six-month columns; impairment $68M and
  litigation accrual $27M l.159, 183, 253; tax prose l.208; cash summary l.266; capex outlook l.273;
  buybacks to July 29 l.276; dividends l.278.
- D05 Hilton Q1 (37,092): system l.15; development table l.33-52; comparable-hotel counts l.60;
  RevPAR l.108-143; net income to Adjusted EBITDA l.147-168; revenue/expense tables l.170-264;
  segments l.268; revolver amendment l.284; buybacks l.286; cash flows l.300-320; debt and April
  borrowing l.324-326.
- D06 Hilton Q2 (42,702): as D05 with six-month columns; interest drivers incl. swap expiry l.272;
  segments l.284; revolver activity and May 2026 notes l.298; buybacks l.300; cash flows l.314-336;
  debt l.340-342.
- D03 Hyatt Q1 (50,875): portfolio table l.14-37; Adjusted EBITDA definition change l.43; RevPAR
  tables l.54-99; fee and other tables l.118-227; segments l.229-277; reconciliation l.346-365;
  liquidity, cash flows, debt, capital return l.367-395.
- D04 Hyatt Q2 (60,852): as D03 with six-month tables; comparable removals l.70, 86, 105, 119;
  reconciliations l.509-545; cash flows l.556-566; capex l.571-576; capital return l.588.
- D09 Wyndham Q1 (33,753): Super 8 China recast l.25, 63-79; P&L l.90-126; reconciliation l.131-148;
  restructuring l.181-200; Revo l.214; debt and swaps l.221-226; cash flow l.229-250; buybacks
  l.257-258; covenant l.268.
- D10 Wyndham Q2 (41,324): Revo exclusion from net room growth l.26; rooms ex Revo l.43; Q2 and H1
  P&L l.90-209; reconciliations l.130-146, 214-232; restructuring l.260-295; Revo cash l.312-314;
  cash flow l.329-348; buybacks l.358-360. Several 2025 lines differ by 1-2 from D09 (H1 less Q2).
- D01 Choice Q1 (50,543): system and pipeline l.7-8; reimbursable deficit l.32; income statement
  (thousands) l.44-73; chain-scale and U.S. brand tables l.85-136; international l.137; SG&A l.139;
  investments l.158; cash flows l.165-173; revolver and covenants l.177-190; notes l.191-203;
  dividends and buybacks l.211-216.
- D02 Choice Q2 (57,523): as D01 with Q2 and six-month statements l.44-73, 148-177; SG&A l.136,
  216; cash flows l.240-251; revolver l.256-266; dividends and buybacks l.286-294.

## Shared ground (navigation only)

- Every company: system size, RevPAR, net income (Marriott only as captions), cash flows (Q2
  documents six months only), buybacks, debt.
- Q1/Q2 pairs: each Q2 document's six-month columns equal Q1 + Q2 for Marriott, Hilton, Hyatt and
  Choice; Wyndham's 2025 lines do not always reconcile.
