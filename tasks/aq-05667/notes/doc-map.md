# aq-05667 - document map

Navigation only (like the form's bundle overview). Questions quote the documents, never this map.
Line numbers are `text/Dnn.txt` lines (two header lines above the document's own first line).

## Bundle

- What it is: nine Sherwin-Williams (SHW) MD&A sections, Q2 2024 10-Q through Q2 2026 10-Q, two 10-Ks.
- Documents (platform Doc N = local id): Doc 1 = D03 (10-Q Q2 2024), Doc 2 = D04 (10-Q Q3 2024),
  Doc 3 = D01 (10-K 2024), Doc 4 = D05 (10-Q Q1 2025), Doc 5 = D06 (10-Q Q2 2025), Doc 6 = D07
  (10-Q Q3 2025), Doc 7 = D02 (10-K 2025), Doc 8 = D08 (10-Q Q1 2026), Doc 9 = D09 (10-Q Q2 2026).
  Local ids sort by file name, so D01 is Doc 3; always convert before writing Doc N.
- Gaps: none. Capture 2026-10-15 12:57 says "9 of 9 read in full (476,677 characters)"; split total
  476,637 (whitespace normalisation). The page asked for a reload (stale-checks warning only).
- Extraction spot-checks: plain-text originals; text/ equals docs/ plus a header. Checked one table
  per document (net sales by segment) and the 10-K footnotes (D01 L205-207, D02 L196-197) against docs/.
- Provenance: notes/intake.json (capture sha 1491919c...); source hashes in text/manifest.json.
- Coverage: all nine read in full by the caller on 2026-10-15 (sketch round 1).

## Per document (common layout)

Every MD&A has: Background, Summary bullets, Outlook, net sales tables by segment (with currency and
"Acquisition and Divestiture Impact" columns), income statement % table, segment income table,
tax, EPS (with per-share amortization/restructuring items), liquidity (net working capital, PP&E,
real estate financing, goodwill/intangibles, debt table, pensions, equity, buybacks, dividends,
cash flow, TTM cash flows), market risk, Financial Covenant, Non-GAAP (EBITDA/Adjusted EBITDA).
Fiscal year = calendar year. Units: $ millions unless "billion".

- Doc 1 (D03, Q2 2024): covenant cites credit agreement of Aug 30, 2022 (L191). HQ financing expected
  $800-850M (L141). Buyback authorization 36.5M shares (L179).
- Doc 2 (D04, Q3 2024): New Credit Agreement July 31, 2024 (L187); deposit for acquisition that
  closed October 2024 (L147).
- Doc 3 (D01, 10-K 2024): 2025 outlook (L21-23): interest expense +~$40M (refinancing), "In addition"
  HQ transition ~$100M = ~$80M SG&A + ~$20M interest; 80-100 new stores; leverage 2-2.5x.
  Store counts (L44-46). 2023 sale-leaseback of the current HQ and R&D center, $47.2M (L120).
  HQ real estate financing table: proceeds 2022 210.0, 2023 305.0, 2024 244.2 (L128-139).
  Contractual obligations table, real estate financing 148.1 with footnote (1) excluding the new HQ
  (L188-207); BASF Brazil decorative paints deal excluded (L208). Net debt target definition (L158).
  Dividend payout on prior-year EPS (L234). Pension 2025 outlook (L173). FCF table capex 1,070.0 vs
  PP&E capex 1,014 (L120, L279). Non-GAAP tables (L254-366).
- Doc 4 (D05, Q1 2025): HQ final proceeds, total $800M (L114-118); "Core capital expenditures, which
  exclude" HQ (L112); first restructuring add-back 19.3 (L190).
- Doc 5 (D06, Q2 2025): restructuring 59.0 / H1 78.3 (L229); R&D Center in service Q2 2025, 60 yrs
  (L143); $300M rate locks (L169); OBBBA (L126).
- Doc 6 (D07, Q3 2025): HQ in service Q3 2025, 60/45 yrs (L148); HQ lease ~$1.938B over 30 yrs (L155);
  Suvinil deposit $1.150B in Other assets (L162); July 2025 notes $1.5B, repaid $400M + $400M due
  Aug 2025 (L174); DDTL $750M + EUR250M (L176); restructuring 14.4 / 9M 92.7 (L235).
- Doc 7 (D02, 10-K 2025): interest expense +$49.3M (L76; 465.0 vs 415.7, L61); 2026 outlook interest
  +~$85M with HQ interest folded in (L21); Suvinil closed Oct 2025, $164.5M / 5.3% of CBG (L42);
  store counts (L41-43); HQ table 2025 proceeds 40.9 (L125-135); contractual obligations real estate
  financing 2,058.1, no exclusion footnote (L190); treasury retirement 29.5M shares (L221);
  dividend raised Jan 26, 2026 (L223); Adjusted EBITDA adds restructuring 111.0 + trademark
  impairment 17.8 (L257-258); impairment "related to restructuring activities" (L71), "primarily
  related" (L358).
- Doc 8 (D08, Q1 2026): "technology center" wording (L66, L110); dividend raise "In February 2026"
  (L159, conflicts with Doc 7's January 26, 2026); interest +27.8 (L72).
- Doc 9 (D09, Q2 2026): interest +23.5 / H1 +51.3 (L88, L101); restructuring 23.8 (L221).

## Shared ground (navigation only)

- Repeated every filing: covenant text, HQ real estate financing paragraph, debt table (three dates),
  buyback authorization, dividend paragraph, EBITDA table with prior-year comparatives.
- Forecast/actual pairs: 2025 interest outlook (Doc 3) vs 2025 actual (Doc 7); 2026 interest outlook
  (Doc 7) vs H1 2026 (Doc 9); HQ proceeds $800-850M (Docs 1-3) vs $800M (Docs 4-9); 80-100 stores
  (Doc 3) vs 83 opened (Doc 7); 2025 dividend $3.16 if approved (Docs 3-5) vs approved (Docs 6-7).
- Changed tables/definitions: contractual obligations real estate row excludes the new HQ in 2024
  (Doc 3) but not in 2025 (Doc 7); OPEB scope "other postretirement" (Doc 3) vs "domestic" (Doc 7);
  "R&D center" (2025) vs "technology center" (2026).
- Same-fact conflicts: dividend raise date (Doc 7 vs Docs 8-9); 2024 capex 1,014 (PP&E) vs 1,070.0
  (FCF table); HQ proceeds table sum 800.1 vs "total of $800 million".
- Q4 figures printed nowhere: FY (Docs 3, 7) minus nine months (Docs 2, 6).
