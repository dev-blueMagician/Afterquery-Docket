# aq-05015 - document map

Maintained by the caller from `text/` (2026-10-14). Navigation only; questions quote the documents.

## Bundle

- What it is: Valero Energy (VLO) exhibits 99.1: one November 2021 cash tender offer announcement
  and seven quarterly earnings releases, Q4 2024 (Jan 30, 2025) through Q2 2026 (Jul 30, 2026).
- Documents: 8; local D01-D08 = platform Doc 1-8 (alphabetical file names are chronological).
- Gaps: none. Capture "8 of 8 read in full"; intake.json: every document matches the capture,
  incomplete false, gap 0. All eight read in full by the caller (2026-10-14).
- Extraction spot-checks: plain-text capture; tables flattened to rows (column order stated per
  table header); one table and one footnote checked per release against the capture body.
- Provenance: notes/intake.json (capture_sha256 6c9d53f5...). Fiscal year = calendar year.

## D01 - Cash tender offers announcement (Nov 18, 2021)

- Any and All offer: 2.700% Senior Notes due 2023, $850,000,000 outstanding.
- Maximum offer (cap $1,000,000,000 aggregate purchase price), principal outstanding and priority:
  1.200% 2024 $925M (1, cap $400M); 3.650% 2025 $600M (2); 4.375% 2026 (issued by Valero Energy
  Partners LP) $500M (3, cap $400M for levels 2-4 together, note e); 2.850% 2025 $1,050M (4);
  10.500% 2039 $250M (5, cap $200M for levels 5-8, note f); 8.750% 2030 $200M (6); 7.500% 2032
  $750M (7); 6.625% 2037 $1,500M (8). Early tender payment $30 per $1,000; caps can be raised.
- About Valero (2021): 15 refineries ~3.2 million bpd; 12 ethanol plants ~1.6 billion gal/yr;
  DGD one renewable diesel plant (Norco); ~7,000 outlets. IR: Homer Bhullar.

## D02-D08 - quarterly earnings releases (common layout)

- Prose: headline net income/adjusted net income; segment operating income; throughput; G&A; cash
  flow; capital investments (total, sustaining part, attributable to Valero); stockholder returns
  (D02-D05 split dividends/buybacks and shares; D06-D08 give only totals and payout ratio); debt.
- Tables: Financial Highlights (income statement), by segment, non-GAAP reconciliations, Refining
  by region (USGC, Mid-Continent, North Atlantic, West Coast), operating statistics per barrel/
  gallon, market reference prices, Other financial data (balance sheet, CFO, capital investments).
- Columns: D02/D06 Q4 + full year (current, prior); D03/D07 Q1 (current, prior); D04/D08 Q2 + six
  months; D05 Q3 + nine months.
- Notes: per-unit = dollars / (per-day volume x days in period); DGD 50% joint venture; regions
  list (West Coast = Benicia, Wilmington).

### Release-specific facts

- D02 (Q4 2024): second-generation biofuel tax credit $79M recognized Dec 2024, split by period
  (9M 2024 21, Q4 2024 5, 2023 24, 2020-22 29); 2025 expected capital investments 2,060 (DGD other
  member (110), attributable 1,950); SAF at DGD Port Arthur (470 Mgal capacity, ~50% to SAF);
  St. Charles FCC $230M, 2026; dividend raised $1.07 -> $1.13 (Jan 16, 2025).
- D03 (Q1 2025): $650M 5.15% notes due 2030 issued; repaid $189M 3.65% (March) and $251M 2.85%
  (April); $1.131B impairment of Benicia and Wilmington; Benicia to cease refining by end of April
  2026; credit $7M attributable to Q1 2024.
- D04 (Q2 2025): Benicia incremental depreciation ~$100M; credit $7M/$14M (Q2/6M 2024).
- D05 (Q3 2025): Benicia retention/separation $50M (adjusted out); incremental depreciation ~100/200;
  "Polymer Grade Propylene less Brent" replaces "Propylene less Brent" (comparatives restated);
  returned "over $2.6 billion" year to date; utilization 97%.
- D06 (Q4 2025): NEW LINE "Taxes other than income taxes" (note b: excise taxes on sales by certain
  foreign operations); Q4/FY 2024 cost of materials restated (27,926 -> 26,409 + 1,517; 116,516 ->
  110,616 + 5,900); LIFO liquidation charge $37M (West Coast); incremental depreciation ~100/300;
  2026 expected capital investments 1,725 (attributable 1,700); dividend $1.13 -> $1.20; IR now
  Brian Donovan.
- D07 (Q1 2026): Q1 2025 cost of materials restated (27,548 -> 26,048 + 1,500); $850M 5.150% notes
  due 2036 (Mar 10, 2026); "operates 14 refineries ~3.0 million bpd"; Benicia idling begun;
  incremental depreciation ~100.
- D08 (Q2 2026): Q2 and six months 2025 restated (26,332 -> 24,678 + 1,654; 53,880 -> 50,726 +
  3,154); LIFO benefit $44M; Port Arthur Refinery fire repair $15M (adjusted out); Benicia fully
  idled April 2026; decommissioning moved to Corporate and Other from Q2 2026; incremental
  depreciation ~33/133 (2026) and ~100 (Q2/6M 2025).

## Shared ground (navigation only)

- Same-period figures printed twice: Q4/FY 2024 (D02, D06), Q1 2025 (D03, D07), Q2/H1 2025 (D04,
  D08). Checked line by line: identical except cost of materials (taxes split out) and the
  propylene reference series. Q3 2025, nine months 2025, Q1-Q3 2024 appear once only.
- Series repeated in every release: throughput, regional margins, per-unit statistics, prices.
- Forecast/actual: 2025 capital investment outlook (D02) vs actual (D06); 2026 outlook (D06) vs
  H1 2026 (D07, D08); St. Charles timing (2026 -> H2 2026 -> Q3 2026).
- Cross-document instruments: 3.650% and 2.850% notes due 2025 (D01 amounts, D03/D04 repayments);
  4.375% VEP notes due 2026 (D01) vs "debt maturing in 2026" (D07, amounts not stated).
