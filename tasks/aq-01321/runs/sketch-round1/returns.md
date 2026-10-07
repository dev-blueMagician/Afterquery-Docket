# Sketch round 1: preliminary screen returns (2026-10-06)

Sketch-stage evidence only, not final check records. Blind solves are fresh blind-solver agents
given the workspace root, a packet path from q01 rev 0's prepared run (same corpus bytes; told not to
open that packet's question.txt, which belongs to q01) and the sketch question verbatim. Closed-book
agents received only the question. Returns copied verbatim from the task notifications.

## i03 blind solve (blind-solver, q01-r0 solver-2 packet)

Question: Of the ranges onsemi forecast for its second quarter of 2026, which ones did its actual results for that quarter fall below the midpoint of? List them in any order.

Return (verbatim):

answer: Two ranges: **GAAP gross margin** (forecast 37.9%–39.9%, midpoint 38.9%, actual 38.4%) and **GAAP diluted earnings per share** (forecast $0.60–$0.72, midpoint $0.66, actual $0.56). Every other range came in at or above its midpoint.

confidence: high

path:
1. **The forecast.** D07 (onsemi's Q1 2026 release, filed 2026-05-04), "SECOND QUARTER 2026 OUTLOOK" table, lines 62–73. The same rows appear in the original docs/ file at lines 71–76. The ranges are:
   - Revenue: "$1,535 to $1,635 million" for both GAAP and non-GAAP.
   - Gross margin: GAAP "37.9% to 39.9%", non-GAAP "38.0% to 40.0%".
   - Operating expenses: GAAP "$302 to $317 million", non-GAAP "$287 to $302 million".
   - Diluted EPS: GAAP "$0.60 to $0.72", non-GAAP "$0.65 to $0.77".
   - These rows are single figures, not ranges, so I left them out: other income and expense "($6 million)", diluted shares "401 million" / "394 million", and the special-items column ($15 million, 0.1%, $0.05, 7 million).
2. **The actuals.** D08 (onsemi's Q2 2026 release, filed 2026-08-03; quarter ended July 3, 2026):
   - Line 44: revenue "$1,603.5".
   - Line 45: gross margin "38.4%" GAAP and "39.3%" non-GAAP.
   - Line 48: diluted EPS "$0.56" GAAP and "$0.74" non-GAAP.
   - Line 132: GAAP total operating expenses "357.7".
   - Line 280: non-GAAP operating expenses "$296.8".
3. **Comparison with each midpoint:**

| Range | Midpoint | Actual | Result |
|---|---|---|---|
| Revenue | (1,535+1,635)/2 = 1,585 | 1,603.5 | above |
| GAAP gross margin | (37.9+39.9)/2 = 38.9% | 38.4% | **below** |
| Non-GAAP gross margin | (38.0+40.0)/2 = 39.0% | 39.3% | above |
| GAAP operating expenses | (302+317)/2 = 309.5 | 357.7 | above (also above the top of the range) |
| Non-GAAP operating expenses | (287+302)/2 = 294.5 | 296.8 | above |
| GAAP diluted EPS | (0.60+0.72)/2 = 0.66 | 0.56 | **below** (also below the bottom of the range) |
| Non-GAAP diluted EPS | (0.65+0.77)/2 = 0.71 | 0.74 | above |

4. **Precision check.** I recomputed the close ones from D08's statements. GAAP gross margin is 616.3/1,603.5 = 38.43%. Non-GAAP gross margin is 630.9/1,603.5 = 39.35%. GAAP EPS is 226.8/404.4 = $0.561. Non-GAAP EPS is 293.8/397.0 = $0.740. Rounding does not change any result.
5. **Corroboration.** The CEO says in D08 (line 23): "We delivered revenue, gross margin and earnings per share above the midpoint of guidance." That matches the non-GAAP and revenue figures. The GAAP versions of gross margin and EPS were below their midpoints.

minimal_documents: D07 and D08. Both are needed and nothing else can replace either one. D09 (onsemi Q4 2025) only gives Q1 2026 guidance ("FIRST QUARTER 2026 OUTLOOK", line 85). D08's outlook covers Q3 2026, not Q2. No other document mentions onsemi.

readings:
- **"Below" meaning "worse than the midpoint":** higher spending is unfavorable, so both operating-expense ranges would count too. The answer would then be GAAP gross margin, GAAP operating expenses, non-GAAP operating expenses and GAAP diluted EPS. This is not the ordinary meaning of "fall below," so I don't adopt it.
- **Counting only non-GAAP or headline guidance,** which is how management framed its results: none of the ranges fell below the midpoint. But the question asks about all the ranges onsemi forecast, and the GAAP ranges are in the same table.
- **Counting revenue as two ranges (GAAP and non-GAAP):** no change, since revenue was above the midpoint either way.

gaps:
- No extraction problems. The sources are plain text (manifest method "text", pages null), and no PDFs or layout files exist.
- I read D07 and D08 in full. I searched D09 only for its outlook section. I did not read D01–D06 or D10–D12 (Analog Devices, Microchip, Texas Instruments); a search found no onsemi mentions in them. Their only "second quarter 2026" hits are the companies' own results.

contaminated: no

Screen result: match (gold GAAP gross margin, GAAP diluted EPS), high confidence. Readings to settle at
write-up: "below" as "worse than" (adds both opex ranges); management's non-GAAP framing (none).

## i03 closed-book (closed-book-solver, question only)

Return (verbatim):

answer: GAAP and non-GAAP operating expenses (a guess)
confidence: low
basis: This is an inference, not a memory of the results. onsemi likely reported its Q2 2026 results in early August 2026, which is after my training data ends. I can't reliably recall either its Q2 2026 guidance ranges or the actual results. The guess comes from onsemi's 2025 pattern, where revenue, gross margin and EPS usually came in at or above the guidance midpoint while operating expenses tended to come in below it. The missing information is the Q2 2026 guidance table and the actual Q2 2026 figures.
contaminated: no

Screen result: misses.

## i02 blind solve (blind-solver, q01-r0 solver-1 packet)

Question: What was the combined revenue of Analog Devices, Microchip, Texas Instruments and onsemi for each company's fiscal quarter that ended in the second calendar quarter of 2026? Give billions of dollars to one decimal place.

Return (verbatim):

**Answer: $12.1 billion.** For onsemi, the quarter that ended in April–June 2026 is its Q1 2026, which ended April 3, 2026. Its labeled "second quarter 2026" ended July 3, 2026, which falls in the third calendar quarter.

answer: $12.1 billion

confidence: high

path:
1. The second calendar quarter of 2026 runs April 1 to June 30, 2026. I picked each company's quarter by its printed end date.
2. **Analog Devices**, fiscal Q2 2026. D02 line 13 says the quarter "ended May 2, 2026". Line 126 (in thousands): "|Revenue|$3,623,465|$2,640,068|…" = $3,623.465M. D03 (lines 336–337) repeats $3,623,465 for May 2, 2026, so there is no restatement.
   - Excluded: fiscal Q1 "ended January 31, 2026" (D01 line 15) and fiscal Q3 "ended August 1, 2026" (D03 line 13).
3. **Microchip**, fiscal Q1 FY2027. D04 line 20: "results for the three months ended June 30, 2026". Line 167: "|Net sales|$1,484.7|$1,075.5|" = $1,484.7M.
   - Excluded: fiscal Q4 FY2026, "Three Months Ended March 31, 2026", $1,311.2M (D06 line 64/66).
4. **Texas Instruments**, Q2 2026. D11 line 56: "For Three Months Ended June 30," 2026. Line 59: "|Revenue|$5,463|$4,448|" = $5,463M.
   - Excluded: Q1 2026, "For Three Months Ended March 31", $4,825M (D10 lines 56/59).
5. **onsemi**, Q1 2026. D08 lines 121–122: "|July 3, 2026|April 3, 2026|July 4, 2025|…" and "|Revenue|$1,603.5|$1,513.3|$1,468.7|…". D07 lines 119–120 also show "April 3, 2026" with "$1,513.3".
   - April 3, 2026 falls in April–June, so the qualifying revenue is $1,513.3M.
   - Excluded: the labeled "Q2 2026" ended July 3, 2026 (third calendar quarter), and Q4 2025 ended December 31, 2025.
   - Because these quarters are about 13 weeks long, only one onsemi quarter-end can fall in the 91-day window.
6. Calculation: 3,623.465 + 1,484.7 + 5,463.0 + 1,513.3 = $12,084.465M, which rounds to **$12.1B**.
   - Cross-check with the headline figures: 3.62 + 1.485 + 5.46 + 1.513 = 12.078, also $12.1B.
   - Rounding each company first gives the same result: 3.6 + 1.5 + 5.5 + 1.5 = 12.1.

minimal_documents:
- D02, D04, D11, D08.
- D08 alone gives onsemi's April 3, 2026 revenue and shows that Q2 ended July 3.
- Alternatives: D03 can replace D02 for ADI. D07 can replace D08 for the onsemi revenue, but D07 alone does not show the July 3 end date. TI and Microchip have no substitutes in the packet.

readings:
- If "second calendar quarter" is read loosely as each company's labeled Q2-type period, onsemi's "second quarter 2026" (ended July 3, 2026) would be used instead. That gives 10,571.165 + 1,603.5 = $12,174.665M, or **$12.2B**. This conflicts with the printed July 3 end date.
- Choosing other quarters for ADI or Microchip is ruled out by their printed end dates.

gaps:
- None material.
- I read D02, D04, D07, D08 and D11 in full.
- I only searched D01, D03, D05, D06, D09, D10 and D12 for period-end dates and revenue rows.
- The documents are text-method extractions with no PDFs or layout files, so there were no original pages to inspect. The extracted tables were consistent.

contaminated: no

Screen result: match ($12.1 billion), high confidence; the labeled-Q2 onsemi route ($12.2 billion) named
and rejected on the printed July 3 end date.

## i02 closed-book (closed-book-solver, question only)

Return (verbatim):

answer: About $11.7 billion. This is an estimate, not a recalled reported figure.

confidence: low

basis: These are the quarters I used:
- Analog Devices: fiscal Q2 FY2026, ended about May 2, 2026
- Microchip: fiscal Q1 FY2027, ended June 30, 2026
- Texas Instruments: Q2 2026, ended June 30, 2026
- onsemi: Q2 2026, which probably ended July 3, 2026, just outside the calendar quarter. Using its Q1 instead would lower the total slightly.

Most of these results were reported after my June 2026 knowledge cutoff, so I don't know the real numbers. I projected each from late-2025 and early-2026 results and guidance: TI about $5.15B, ADI about $3.6B, onsemi about $1.57B and Microchip about $1.36B.

contaminated: no. The only extra context was the user's account email, which has nothing to do with the question. I called no tools.

Screen result: misses (gold $12.1 billion); the estimate band (11.7) sits 0.4 below the gold, so the
closed-book exposure is moderate rather than nil (run-rate projection of known companies).

## i06 closed-book (closed-book-solver, question only)

Question: What was the combined revenue of all the quarters that Analog Devices, Microchip, Texas Instruments and onsemi ended between January 1 and March 31, 2026? Give billions of dollars to one decimal place.

Return (verbatim):

answer: About $9.3 billion. This is ADI's fiscal Q1, which ended Jan 31, 2026 (about $3.16B), plus Microchip's fiscal Q4, which ended Mar 31, 2026 (about $1.3B), plus TI's Q1, which ended Mar 31, 2026 (about $4.83B). onsemi is left out because its Q1 2026 ended Apr 3, 2026, so it ended no quarter in the window.

confidence: low

basis: The quarter end dates come from memory of each company's fiscal calendar. onsemi's quarters end on the Friday nearest the calendar quarter end. ADI's year ends on the Saturday nearest Oct 31. TI and Microchip use calendar month ends. The revenue figures are recalled, not checked. Microchip's and TI's numbers are the least certain.

contaminated: no (the only added context was unrelated account and environment details)

Screen result: REACHES the gold ($9.3 billion) at low confidence, with the onsemi exclusion. i06
dropped: quarters reported February-April 2026 (ADI FQ1 $3.16B, TI Q1 $4.83B) and onsemi's 52/53-week
calendar are within the local model's recall. Lesson: anchor on quarters reported from about May 2026.

## i06 blind solve (blind-solver, q01-r1 solver-1 packet)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted): "answer: $9.3 billion"
"confidence: high". Path: ADI fiscal Q1 "ended January 31, 2026" (D01 L15), revenue 3,160,263K (L128;
TTM tables in D02/D03 print 3,160,063, immaterial); Microchip quarter ended March 31, 2026, 1,311.2
(D06 L8, L193); TI three months ended March 31, 2026, 4,825 (D10 L56-59); onsemi "Quarters Ended ...
April 3, 2026|December 31, 2025" (D07 L117-120; D08 L370), so no onsemi quarter in the window;
9,296.463 -> $9.3 billion. minimal_documents: D01, D06, D07, D10 (D02/D03 can replace D01; D08 can
replace D07). Readings: onsemi Q1 counted as March 10.8 (ruled out by the dates); "between" exclusive
3.2 (not ordinary meaning). contaminated: no.

Screen result: match, high confidence; sketch already dropped on the closed-book reach.

## i05 blind solve (blind-solver, q01-r1 solver-2 packet)

Question: What was the combined revenue of Analog Devices, Microchip, Texas Instruments and onsemi for the quarter each company ended between April 1 and June 30, 2026? Give billions of dollars to one decimal place.

Summary of the verbatim return (task notification 2026-10-06; key lines quoted): "answer: $12.1 billion"
"confidence: high". Path: ADI "fiscal second quarter 2026, which ended May 2, 2026", 3,623,465K (D02;
D03 FCF table repeats); Microchip "three months ended June 30, 2026", 1,484.7 (D04); TI three months
ended June 30, 5,463 (D11); onsemi "Quarters Ended ... April 3, 2026", 1,513.3 (D07; D08 repeats);
others outside the window (ADI Q1 Jan 31 and Q3 Aug 1; Microchip Mar 31; TI Mar 31; onsemi Q2 "July 3,
2026"); 12,084.465 -> $12.1 billion; headline figures also give 12.1. minimal_documents: D02, D04,
D07, D11 (D03 can replace D02; D08 can replace D07). Readings: onsemi "second quarter 2026" (ended
July 3) gives $12.2 billion, ruled out by the window; ADI Q3 / Microchip Q4 outside the window.
contaminated: no.

Screen result: match ($12.1 billion), high confidence; same trap named and rejected as in i02.

## i05 closed-book (closed-book-solver, question only)

Return (verbatim):

answer: about $11.6 billion (estimate)

confidence: low

basis: This comes from memory and inference. I made no tool calls. Each company's quarter in the window is:
- ADI fiscal Q2 2026, ended May 2: about $3.6B. I recall guidance of $3.5B ± $0.1B, and ADI usually lands near the top of its range.
- Microchip fiscal Q1 2027, ended June 30: about $1.35–1.4B, projected from its recovery trend. The actual result came out after my training cutoff.
- TI Q2 2026, ended June 30: about $5.0–5.2B, also projected. The actual came out after my cutoff.
- onsemi Q1 2026: about $1.5B. Its quarters end on the Friday closest to quarter-end, so Q1 likely ended April 3 and Q2 on July 3. That makes Q1 the quarter in the window. If you meant onsemi's Q2, add about $0.1B.

The total is roughly 11.4–11.8 in billions of dollars.

contaminated: no. Only automatic account and environment metadata was present, with nothing about this question.

Screen result: misses (gold $12.1 billion; band 11.4-11.8). Note: the model knows onsemi's
Friday-nearest calendar, so the onsemi alignment trap is weaker for models with that recall.

## i07 closed-book (closed-book-solver, question only)

Question: For the twelve months ended June 30, 2026, what was Texas Instruments' combined R&D and SG&A expense divided by its revenue, expressed as a percentage to two decimal places?

Return (verbatim):

answer: About 22% (a rough estimate; I don't know the exact two-decimal figure)
confidence: low
basis: TI reported its Q2 2026 results around July 2026, which is after my training data ends, so I can't give the exact figure. The estimate uses figures I only partly remember:
- Q3 2025 revenue was about $4.74B and Q4 2025 about $4.42B.
- I assumed about $4.7B for Q1 2026 and about $5.0B for Q2 2026, giving roughly $18.9B in trailing-twelve-month revenue.
- R&D plus SG&A ran about $1.0–1.05B a quarter, or roughly $4.15B over the twelve months.
- $4.15B ÷ $18.9B ≈ 22%.

The exact answer would come from the Q2 2026 earnings release, which states the past 12 months' R&D and SG&A spending, divided by twelve-month revenue.
contaminated: no. The only extra context was an automatically attached user email address, which has nothing to do with the question.

Screen result: misses (gold 20.26%). Note: the model expects the release's twelve-month R&D and SG&A
statement to supply the numerator, i.e. the rounded "$3.9 billion" route.

## i07 blind solve (blind-solver, q01-r1 solver-2 packet, re-bound)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted): "answer: **20.26%**"
"confidence: high". Path: TTM revenue D11 "|Revenue||$19,453|$16,675||" (recomputed 17,682 - 4,069 -
4,448 + 4,825 + 5,463 = 19,453); "TI doesn't print a 12-month R&D or SG&A figure. D11 line 17 only gives
a rounded total"; FY2025 R&D 2,083 and SG&A 1,860 (D12), Q1 2026/2025 510/517 and 464/472 (D10), Q2
2026/2025 535/527 and 490/485 (D11); R&D 2,084 + SG&A 1,857 = 3,941; 3,941 / 19,453 = 20.26%;
implied Q3 2025 R&D 518, SG&A 457, revenue 4,742 with checks (D12's "decreased 7% sequentially",
D10 TTM revenue 18,438, operating-profit identities). minimal_documents: D10, D11, D12, all required.
Readings: rounded "$3.9 billion" 20.05% ("less precise than two decimals warrant"); adding
restructuring and acquisition charges 21.04%; Q2 only 18.76%. contaminated: no.

Screen result: match (20.26%), high confidence; the decoy route named and rejected on precision.

## i07 removal probe without D12 = Doc 7 (blind-solver, packet runs/i07-alt-x4: byte copy of q01-r1 solver-1 minus TI Q4 2025; D01-D11 unchanged; bound with bind_scope)

Prompt: root, packet, forced-estimate instruction (best single estimate, method, probability), question verbatim.

Summary of the verbatim return (key lines quoted): "**answer:** 20.05%" "**confidence:** medium". Path:
D11 page 1 "Over the past 12 months we invested $3.9 billion in R&D and SG&A" and D11 twelve-month revenue
"$19,453"; 3,900 / 19,453 = 20.05%. Range from the rounded statements in D10 and D11 plus the printed
quarters: Q3 + Q4 2025 combined between 1,864 and 1,951, so the ratio lies between 19.86% and 20.30%.
"I can't reliably recall TI's Q3 or Q4 2025 figures, so I have not supplied them." Probability that
20.05% "equals the true unrounded ratio is only about 5–10%". Wrong window (twelve months to March)
21.15%; Q2 only 18.76%. contaminated: no.

Probe result: without Doc 7 the forced answer is 20.05%, not the gold; the documents only bound the
gold (19.86-20.30), which the platform's check does not count as reaching it. Doc 7 necessary.

## i07 removal probe without D10 = Doc 8 (blind-solver, packet runs/i07-alt-j8: byte copy minus TI Q1 2026; former D11/D12 renumbered D10/D11; bound with bind_scope)

Prompt: root, packet, forced-estimate instruction, question verbatim.

Summary of the verbatim return (key lines quoted; probe ids are renumbered, its "D10" = TI Q2 2026 and
its "D11" = TI Q4 2025): "**answer:** 20.05%". Twelve-month revenue "$19,453" and "Over the past 12 months
we invested $3.9 billion in R&D and SG&A"; 3,900 / 19,453 = 20.05%; rounding range 19.79%-20.30%; exact
total = 3,956 + (Q1 2026 - Q1 2025) with "Neither first-quarter figure is in the packet" and "I did not
fill in Q3 2025 or Q1 2026 from memory." It recalled only TI revenue figures for a consistency check
(Q1 2025 $4,069M, Q3 2025 $4,742M, Q3 2024 $4,151M), not used in the answer. Probability ~60% that
20.05% matches a packet-built key, ~5% if the key uses unrounded quarters. contaminated: no.

Probe result: without Doc 8 the forced answer is 20.05%, not the gold. Doc 8 necessary. Note: public
2025 TI revenue figures are recallable; Q1 2026 R&D/SG&A were not recalled.

## i08 blind solve (blind-solver, q02-r1 solver-1 packet)

Question: Over onsemi's four fiscal quarters ended July 3, 2026, what was the cash it paid to repurchase common stock divided by its free cash flow, expressed as a percentage to one decimal place?

Summary of the verbatim return (key lines quoted): "**answer:** 97.7%" "**confidence:** high". Quarters
ended Oct 3, 2025, Dec 31, 2025, Apr 3, 2026, Jul 3, 2026 (D08 LTM table); "Repurchase of common stock"
325.0 and 450.2 (D09 L253), 345.7 and 344.8 (D08 L232); 1,465.7 (cross-check 1,377.6 - 602.4 + 690.5);
LTM free cash flow 1,500.4 (D08; quarters add; also 1,672.0 - 171.6; also 1,418.6 - 560.8 + 642.6);
1,465.7 / 1,500.4 = 97.7%. minimal_documents: D08, D09 (D07 adds nothing). Readings: headline
buybacks for 2026 quarters ($346M, $332M) with cash for 2025 -> 96.9% (mixed bases; "cash it paid"
points to the cash-flow line); adding RSU tax withholding 101.0%; FCF net of asset-sale proceeds 95.5%;
bond-hedge payment excluded. contaminated: no.

Screen result: match (97.7%), high confidence.

## i08 closed-book (closed-book-solver, question only)

Return (verbatim):

answer: about 100% (a guess; I don't know the exact figure)
confidence: low
basis: From memory, onsemi said it would return about 100% of its 2025 free cash flow through share buybacks. As I recall, Q3 2025 free cash flow was about $372M, with buybacks of a similar size. Results for the quarter ended July 3, 2026 (Q2 2026) came out after my training cutoff. I also can't reliably recall the Q4 2025 and Q1 2026 buyback and free cash flow figures. Without those, I can't add up the four quarters, so this estimate comes only from the stated policy.
contaminated: no (the session included only automatic account and environment details, none related to the question)

Screen result: misses at the asked precision (gold 97.7%), but near (policy anchor 100%); it recalled
Q3 2025 free cash flow ($372M) exactly, so D09's removal-test risk is real for i08.
