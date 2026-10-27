# aq-06994 - document map

Maintained by the caller from `text/` (plain-text capture, so `docs/` and `text/` carry the same words).
Navigation only, like the form's bundle overview. Questions quote the documents, never this map.

## Bundle

- What it is: repeat of aq-06801 (same seven documents, byte-identical). Two unrelated companies' quarterly
  filings: Iridium Communications (calendar year) Q3 2025, Q4/FY 2025 and Q1 2026 earnings releases; Comtech
  Telecommunications (fiscal year ends July 31) Q1, Q2 and Q3 fiscal 2026 earnings releases plus the Q1 fiscal
  2026 Form 10-Q.
- Documents: 7. Local id -> task-page Doc number (by source sha256 in notes/intake.json):
  D01 = Doc 6 (Comtech Q1 FY26 release, Dec 11 2025); D02 = Doc 7 (Comtech Q1 FY26 10-Q, quarter ended
  Oct 31 2025); D03 = Doc 5 (Comtech Q2 FY26 release, Mar 16 2026); D04 = Doc 4 (Comtech Q3 FY26 release,
  Jun 15 2026); D05 = Doc 1 (Iridium Q1 2026 release, Apr 23 2026); D06 = Doc 3 (Iridium Q3 2025 release,
  Oct 23 2025); D07 = Doc 2 (Iridium Q4 and full-year 2025 release, Feb 12 2026).
- Gaps: none. Capture AQ-06994_2026-10-19_0421.txt says "7 of 7 read in full (406,589 characters)"; splitter
  marked every document complete, no gap characters. All seven read in full by the caller on 2026-10-19
  (D02 lines 1-2153), independently of the aq-06801 read of 2026-10-18.
- Reuse binding (2026-10-19): every docs/ source sha256 and every text/Dnn.txt sha256 equals aq-06801's
  (D01 a96a03b3, D02 02fd6f93, D03 6021c02f, D04 73a35b89, D05 61b06e5e, D06 05020897, D07 f19980e1;
  manifest.json identical). The capture's own sha256 differs (c6e9aaeb... against 1a90f739...) only in its
  page header and work section; the document sections are byte-identical (sha256 98a98fcd... both). The
  corpus sha256 in notes/mine.md (7342478d...) differs from aq-06801's (c2f757e1...) because it also hashes
  notes/intake.json, which records the capture hash. aq-06801's map, hooks and screens therefore apply as
  history; its sketch sentences and platform result (q01 High 3/3 Too easy) bind to the same documents.
- Extraction spot-checks (carried from aq-06801, re-confirmed by the full read): text capture, no pages. Tables
  checked by footing: Iridium 9M + Q4 = FY on every OEBITDA reconciliation line; Comtech Q1 + Q2 = 6M and
  6M + Q3 = 9M on sales, operating loss, Adjusted EBITDA and restructuring. One defect: D02's segment table
  (l.1117-1143) shifts the prior-year cells left (rows read S&S FY26, Allerium FY26, S&S FY25, Allerium FY25 with
  totals missing); footed by hand. D07 prints Q4 2025 engineering and support 37,061 / total revenue 212,940 in
  the statement (l.151-152) and 37,062 / 212,941 in the summary table (l.223-224): a $1K source difference.
- Provenance: notes/intake.json, capture sha256 c6e9aaeb...; corpus sha256 7342478df8269ba3 (notes/mine.md).

## Iridium (D05, D06, D07) - calendar quarters, $ thousands in tables

- Each release prints its own quarter and the prior-year quarter; D06 adds nine months 2025/2024, D07 adds
  full year 2025/2024; D05's OEBITDA reconciliation adds a FY2025 column (l.116-125).
- Q2 2025 is printed nowhere: only June 30 subscriber totals in D06 prose (l.39 total 2,483,000; l.57
  commercial 2,355,000; l.69 government 128,000). Q2 = 9M (D06) - Q3 (D06) - Q1 2025 (D05 prior-year column).
- OEBITDA definition: D06 l.108 "acquisition and related costs" (fn l.137 narrow); D07 l.108 / D05 l.98
  "transaction related expenses" (fn broader). No numeric effect in 2025 (9M line "—"; Q4 479; Q1 2026 699).
- 2026 practice change: incentive comp all cash; D07 l.99 / D05 l.89 "$17 million impact ... $480 million to
  $490 million ... Without this change ... $497 million to $507 million"; D05 l.31 Q1 2026 "$4.2 million".
- Net debt definition: D06 l.250 and D05 l.208 include the revolver; D07 l.249 term loan only. Revolver drawn
  $20,000 at Mar 31 2025 (D05 l.189), $50,000 at Sep 30 2025 (D06 l.231, l.85), repaid in Q4 2025 (D07 l.85),
  nil at Mar 31 2026. Net leverage: D06 l.85 3.5x TTM (1,736,188 / 497,125 = 3.49); D07 l.85 3.4x on 2025
  OEBITDA; D05 l.79 3.4x TTM. D06 l.99 also prints FY2024 OEBITDA ($470.6 million), so D06 alone rebuilds TTM.
- ARPU footnote (4): revenue / average of beginning and ending billable subscribers / months (D05 l.258,
  D06 l.300, D07 l.299). Subscriber tables: D05 l.210-250, D06 l.252-292, D07 l.251-291.
- Capital allocation prose: D06 l.85-91 (Q3 capex 21.5 incl. 1.1 capitalized interest; Q3 buyback 1.9M
  shares $50.0M; $245.3M remaining; program paused); D07 l.85-91 (Q4 capex 33.5 incl. 1.4; FY capex 100.3 incl.
  4.6 l.43; FY buybacks ~6.8M shares ~$185.0M, none in Q4; FY dividends $62.9M); D05 l.79-81 (Q1 2026 dividend
  $0.15, $16.5M; buybacks not mentioned).
- Guidance: D06 l.95-103 (FY2025 updated, with previous ranges); D07 l.95-103 and D05 l.85-93 (FY2026).
- EMSS contract: $738.5M seven-year from Sept 2019; $110.5M for contract year from Sept 15 2025 (D06 l.61-67);
  government service revenue 27,625 in Q4 2025 and Q1 2026 (= 110.5M / 4).
- 2024 net income includes a $19.8M one-time gain on the Satelles acquisition (D07 l.41); Q3 2024 broadband
  included $1.4M non-recurring revenue (D06 l.53).

## Comtech (D01-D04) - fiscal year ends July 31; tables in whole dollars

- D01: Q1 FY26 (ended Oct 31 2025) and Q1 FY25; prose on Q4 FY25 ("immediately preceding quarter": op income
  $1.9M l.47, Adj EBITDA $13.3M l.54, NLA $11.6M l.52, gross profit $40.7M / 31.2% l.43, op cash flow $11.4M
  l.60, net sales -14.8% sequential l.40, S&S and Allerium l.68-72, l.100-106 incl. S&S restructuring $0.7M);
  FY2025 column in the Adjusted EBITDA reconciliation (l.294-308) and the non-GAAP reconciliation (l.331-347).
- D02 (10-Q): same Q1 statements; Liquidity (l.323-331, exact borrowings at Oct 31 and Dec 10); notes on debt
  (Note 9 l.688-800: amendments, covenant thresholds l.716, sale-proceeds 65/35 rule l.702, Jul 31 / Oct 31
  principal table l.765-777: Term Loan 116,260 / 117,354, Revolving Loan 17,641 both dates; unused-line fee and
  consent cap l.793), subordinated facility (Note 10 l.802-881: lenders are the preferred holders l.804;
  make-whole schedule 33% / 50% / 75%+16% l.844-846; tranches closed Oct 17 2024 ($25M), Mar 3 2025 ($40M),
  Jul 21 2025 ($35M priority, PIK, no make-whole); Jul 31 / Oct 31 table l.859-869: 100,144 / 101,471),
  preferred (Note 17 l.1255-1379), segments (Note 14 l.1091-1171), MD&A (Q4 FY25 net sales $130.4M l.1588;
  FY25 Adjusted EBITDA reconciliation in $M l.1831-1846; Adjusted EBITDA definition l.1883). Supplemental
  cash flow l.286-299: term loan amendment fee paid-in-kind $2,107,000 and accrued $702,000 (the term loan rose
  in Q1 despite the $1,013,000 repayment; D03's $124.7M at Jan 31 implies the $702,000 was added in Q2).
- D03: Q2 FY26 (ended Jan 31 2026), Q2 FY25, six months both years; FY2025 columns as in D01; prior-year Q2
  "(Dividends) deemed contributions" +26,383 (l.197); borrowings at Jan 31 / Mar 13 (l.141-147).
- D04: Q3 FY26 (ended Apr 30 2026), Q3 FY25, nine months both years; FY2025 columns (so D04 alone gives Q4 FY25
  operating income 1,861 and restructuring 1,363 as FY less nine months); S&S sale to Gilat ($157.5M, signed
  Jun 14 2026, not held for sale at Apr 30; l.17, l.121, l.128-129); borrowings at Apr 30 / Jun 12 (l.133-141:
  senior $119.7M incl. $3.6M revolver, subordinated $104.1M excl. $32.5M make-whole); covenant suspension
  extended to the period ending Jul 31 2027 (l.131).
- No FY2025 income statement anywhere: FY2025 net sales, net loss and Q4 FY25 GAAP net income are printed
  nowhere; Q4 FY25 net sales only in D02 MD&A ($130.4M) or as D01's 14.8% sequential decline.
- Covenant passage re-quoted: D01 l.120 and D03 l.137 name two covenants; D02 l.702 and D04 l.131 three.
- Preferred redemption value / liquidation preference: Jul 31 2025 204,153; Oct 31 208,746; Jan 31 2026
  213,443; Apr 30 218,245 (2.25% a quarter); income-statement "net dividends" also carry the embedded
  derivative remeasurement (3,903 / 6,525 / 10,810).
- Revolver availability = $27.25M consent cap (54,750,000 commitment less the 27,500,000 consent portion) less
  the amount drawn: 9.6 / 14.6 / 19.6 / 23.6 / 27.3 at Oct 31, Dec 10, Jan 31, Apr 30, Jun 12.

## Shared ground (navigation only)

- No entity, period or document links the two companies; quarter ends never coincide (Iridium Mar/Jun/Sep/Dec,
  Comtech Jan/Apr/Jul/Oct).
- Periods printed only cumulatively: Iridium Q2 2025 (D05 + D06); Comtech Q4 FY2025 (FY column in D01/D03/D04
  less nine months in D04; partly in D01/D02 prose, rounded).
- Comtech FY2025 column repeats identically in D01, D03, D04 (and in $M in D02): one fact in several documents.
