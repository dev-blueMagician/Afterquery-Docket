# aq-06801 - document map

Maintained by the caller from `text/` (plain-text capture, so `docs/` and `text/` carry the same words).
Navigation only, like the form's bundle overview. Questions quote the documents, never this map.

## Bundle

- What it is: two unrelated companies' quarterly filings: Iridium Communications (calendar year) Q3 2025,
  Q4/FY 2025 and Q1 2026 earnings releases; Comtech Telecommunications (fiscal year ends July 31) Q1, Q2 and
  Q3 fiscal 2026 earnings releases plus the Q1 fiscal 2026 Form 10-Q.
- Documents: 7. Local id -> task-page Doc number (by source sha256 in notes/intake.json):
  D01 = Doc 6 (Comtech Q1 FY26 release, Dec 11 2025); D02 = Doc 7 (Comtech Q1 FY26 10-Q, quarter ended
  Oct 31 2025); D03 = Doc 5 (Comtech Q2 FY26 release, Mar 16 2026); D04 = Doc 4 (Comtech Q3 FY26 release,
  Jun 15 2026); D05 = Doc 1 (Iridium Q1 2026 release, Apr 23 2026); D06 = Doc 3 (Iridium Q3 2025 release,
  Oct 23 2025); D07 = Doc 2 (Iridium Q4 and full-year 2025 release, Feb 12 2026).
- Gaps: none. Capture says "7 of 7 read in full (406,589 characters)"; splitter marked every document
  complete, no gap characters. All seven read in full by the caller on 2026-10-18 (D02 lines 1-2153).
- Extraction spot-checks: text capture, no pages. Tables checked by footing: Iridium 9M + Q4 = FY on every
  OEBITDA reconciliation line; Comtech Q1 + Q2 = 6M and 6M + Q3 = 9M on sales, operating loss, Adjusted
  EBITDA and restructuring. One defect: D02's segment table (l.1117-1143) shifts the prior-year cells left
  (rows read S&S FY26, Allerium FY26, S&S FY25, Allerium FY25 with totals missing); footed by hand. D07 prints
  Q4 2025 engineering and support 37,061 / total revenue 212,940 in the statement (l.151-152) and 37,062 /
  212,941 in the summary table (l.223-224): a $1K source difference, not extraction.
- Provenance: notes/intake.json, capture sha256 1a90f739...; corpus sha256 c2f757e1435594d3 (notes/mine.md).

## Iridium (D05, D06, D07) - calendar quarters, $ thousands in tables

- Each release prints its own quarter and the prior-year quarter; D06 adds nine months 2025/2024, D07 adds
  full year 2025/2024; D05's OEBITDA reconciliation adds a FY2025 column (l.116-125).
- Q2 2025 is printed nowhere: only June 30 subscriber totals in D06 prose (l.39 total 2,483,000; l.57
  commercial 2,355,000; l.69 government 128,000). Q2 = 9M (D06) - Q3 (D06) - Q1 2025 (D05 prior-year column).
- OEBITDA definition: D06 l.108 "acquisition and related costs" (fn l.137 narrow); D07 l.108 / D05 l.98
  "transaction related expenses" (fn broader). No numeric effect in 2025 (9M line "—"; Q4 479; Q1 2026 699).
- 2026 practice change: incentive comp all cash; D07 l.99 / D05 l.89 "$17 million impact ... $480 million to
  $490 million ... Without this change ... $497 million to $507 million"; D05 l.31 Q1 2026 "$4.2 million".
- Net debt definition: D06 l.250 and D05 l.208 include the revolver; D07 l.249 term loan only (revolver nil).
  Net leverage: D06 l.85 3.5x TTM; D07 l.85 3.4x on 2025 OEBITDA; D05 l.79 3.4x TTM.
- ARPU footnote (4): revenue / average of beginning and ending billable subscribers / months (D05 l.258,
  D06 l.300, D07 l.299). Subscriber tables: D05 l.210-250, D06 l.252-292, D07 l.251-291.
- Capital allocation prose: D06 l.85-91 (Q3 capex 21.5 incl. 1.1 capitalized interest; Q3 buyback 1.9M
  shares $50.0M; $245.3M remaining); D07 l.85-91 (Q4 capex 33.5 incl. 1.4; FY capex 100.3 incl. 4.6 l.43;
  FY buybacks ~6.8M shares ~$185.0M, none in Q4; FY dividends $62.9M); D05 l.79-81.
- Guidance: D06 l.95-103 (FY2025 updated, with previous ranges); D07 l.95-103 and D05 l.85-93 (FY2026).
- EMSS contract: $738.5M seven-year from Sept 2019; $110.5M for contract year from Sept 15 2025 (D06 l.61-67).

## Comtech (D01-D04) - fiscal year ends July 31; tables in whole dollars

- D01: Q1 FY26 (ended Oct 31 2025) and Q1 FY25; prose on Q4 FY25 ("immediately preceding quarter": op income
  $1.9M l.47, Adj EBITDA $13.3M l.54, NLA $11.6M l.52, gross profit $40.7M / 31.2% l.43, op cash flow $11.4M
  l.60, S&S and Allerium l.70-72, l.102-106); FY2025 column in the Adjusted EBITDA reconciliation (l.294-308)
  and the non-GAAP reconciliation (l.331-347). Balance sheets Oct 31 / Jul 31 2025. Liquidity at Dec 10 2025.
- D02 (10-Q): same Q1 statements; notes on debt (Note 9 l.688-800: amendments, covenant thresholds l.716,
  sale-proceeds 65/35 rule l.702), subordinated facility (Note 10 l.802-881: make-whole schedule l.844-846,
  priority $35M tranche PIK l.818-825), preferred (Note 17 l.1255-1379: 9.00% PIK compounding quarterly
  l.1304, conversion price $7.99 l.1311, puts l.1315-1317), segments (Note 14 l.1091-1171), MD&A (Q4 FY25 net
  sales $130.4M l.1588; FY25 Adjusted EBITDA reconciliation in $M l.1831-1846; Adjusted EBITDA definition
  l.1883). Equity statement l.193-214 (retained earnings nil at Oct 31 2024; preferred adjustments to APIC).
- D03: Q2 FY26 (ended Jan 31 2026), Q2 FY25, six months both years; FY2025 columns as in D01; prior-year Q2
  "(Dividends) deemed contributions" +26,383 (l.197).
- D04: Q3 FY26 (ended Apr 30 2026), Q3 FY25, nine months both years; FY2025 columns; S&S sale to Gilat
  ($157.5M, signed Jun 14 2026, not held for sale at Apr 30; l.17, l.121, l.128-129); covenant suspension
  extended to the period ending Jul 31 2027 (l.131).
- No FY2025 income statement anywhere: FY2025 net loss and Q4 FY25 GAAP net income are printed nowhere
  (searched 2026-10-18); FY2025 net loss only through the reconciliation (NLA, preferred adjustments, gain).
- Covenant passage re-quoted: D01 l.120 and D03 l.137 name two covenants; D02 l.702 and D04 l.131 name three
  (Minimum EBITDA added). D02 l.696-699: the first two amendments suspended only until Jan 31 2025 / Oct 31 2025.
- Preferred redemption value / liquidation preference: Jul 31 2025 204,153; Oct 31 208,746; Jan 31 2026
  213,443; Apr 30 218,245 (2.25% a quarter); income-statement "net dividends" also carry the embedded
  derivative remeasurement (3,903 / 6,525 / 10,810).

## Shared ground (navigation only)

- No entity, period or document links the two companies; quarter ends never coincide (Iridium Mar/Jun/Sep/Dec,
  Comtech Jan/Apr/Jul/Oct).
- Periods printed only cumulatively: Iridium Q2 2025 (D05 + D06); Comtech Q4 FY2025 (FY column in D01/D03/D04
  less nine months in D04; partly in D01/D02 prose).
- Comtech FY2025 column repeats identically in D01, D03, D04 (and in $M in D02): one fact in several documents.
