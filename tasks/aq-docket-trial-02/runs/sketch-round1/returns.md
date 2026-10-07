# Sketch round 1: preliminary screen returns (2026-10-06)

Sketch-stage evidence only, not final check records. Each blind solve is a fresh blind-solver agent
given only the workspace root, a packet path from q01 rev 0's prepared run (same corpus bytes; the
scope guard allows only that packet's text/ and docs/) and the sketch question verbatim. Closed-book
agents received only the question. Returns copied verbatim from the task notifications.

## i03 closed-book (closed-book-solver, question only)

Question: By what percentage did Colgate's combined net sales in Russia and Belarus change from 2024 to 2025? Give the sign, to one decimal place.

Return (verbatim):

I couldn't recall this figure, so the answer below is an estimate rather than a number from the filing.

answer: +14.5% (estimate)
confidence: low
basis: I don't remember the dollar amounts Colgate reported for Russia and Belarus in its 2025 10-K, so I worked the figure out from exchange rates. The ruble averaged about 83.5 per US dollar in 2025, against about 92.5 in 2024, so it gained roughly 11%. I added a few percent of sales growth in local currency, mostly from price increases, partly offset by lower volumes. The actual 2024 and 2025 amounts from the 10-K are what's missing.
contaminated: no. The session held only standard environment and account details, nothing about the question. I used no tools.

Screen result: misses (gold +3.7%).

## i02 closed-book (closed-book-solver, question only)

Question: In the year Colgate took a charge to write down goodwill and intangible assets tied to its skin health business, what were that business's net sales, in millions of dollars?

Return (verbatim):

answer: unknown. My best guess is about $500 million in 2022, the year of the impairment.
confidence: low
basis: I recall that Colgate took a non-cash impairment of about $721 million in 2022. It wrote down goodwill and intangible assets for its skin health business, mainly the Filorga brand. That business also includes EltaMD and PCA Skin. I don't remember Colgate reporting an exact net sales figure for skin health. The roughly $500 million is my own estimate from rough brand sizes: Filorga about $150–200M, EltaMD about $200–250M and PCA Skin about $50–70M. I may be missing a later skin health impairment, possibly in 2025, which would change the year.
contaminated: no

Screen result: misses (gold $366 million). Caller note: the solver recalls an earlier (2022) skin
health impairment that the bundle never mentions; "the year Colgate took a charge" would need the
year pinned (2025) or the anchor changed before any write-up (description-fits-one-thing risk).

## i02 blind solve (blind-solver, q01 rev 0 solver-1 packet)

Return (verbatim):

**answer:** About **$366 million** in net sales for fiscal 2025. No document states this figure directly; it is the difference between two segment tables.

**confidence:** high

**path:**
1. The charge was taken in 2025. D09 (Q4/FY2025 release, dated Jan 30, 2026), line 71: "During the fourth quarter, the Company took a non-cash, after-tax charge of $794 million to adjust the carrying values of goodwill and intangible assets related to the skin health business." Line 17: "GAAP EPS declined 25% to $2.63, driven by goodwill and intangible assets impairment charges related to the skin health business." Line 495 gives the pre-tax figure for the twelve months ended Dec 31, 2025: "goodwill and intangible assets impairment charges of $919". No other document mentions an impairment or write-down.
2. All of the skin health business sat in North America until 2026. D04 line 88 (same text in D05 and D06): skin health results formerly in Europe "are reported with the other skin health businesses in the North America reportable operating segment." D11 line 85 describes the 2026 change: Europe, Africa/Eurasia (excluding Russia and Belarus) "and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East &amp; Africa reportable operating segment." Russia and Belarus moved to Asia Pacific. Nothing else changed in North America.
3. North America FY2025 under the old structure: D09 Table 5, line 460: "| North America | $ 1,021 | $ 1,036 | $ 4,045 | $ 4,113 |". The columns are Q4 2025, Q4 2024, FY2025, FY2024. FY2025 = 4,045.
4. North America FY2025 after the recast: D10 (Segment Information (Recast)), line 25: "| North America | $ 3,679 | $ 1,510 | $ 1,375 | $ 4 | $ 790 |". The row checks: 3,679 − 1,510 − 1,375 − 4 = 790. Both figures also appear in the original docs/ files.
5. Skin health 2025 net sales = 4,045 − 3,679 = **366**.
6. Quarterly check, old structure (D06/D07/D08/D09) minus recast (D10):
   - Q1: 998 − 904 = 94
   - Q2: 1,027 − 919 = 108
   - Q3: 999 − 922 = 77
   - Q4: 1,021 − (3,679 − 2,745 = 934) = 87
   - Sum: 94 + 108 + 77 + 87 = 366
   
   D11 (904) and D12 (919; six months 1,823) repeat the recast Q1 and Q2 figures.
7. Totals check:
   - Old FY2025 segments: 4,045 + 4,776 + 2,962 + 2,814 + 1,172 = 15,769.
   - Recast FY2025 segments: 3,679 + 4,776 + 4,276 + 3,038 = 15,769.
   - Europe, Middle East &amp; Africa: Asia Pacific rose by 3,038 − 2,814 = 224 (Russia and Belarus). Europe + Africa/Eurasia − 224 + 366 = 2,962 + 1,172 − 224 + 366 = 4,276. This matches, though it follows from the totals rather than being an independent check.

**minimal_documents:** D09, D10, D11.
- D09 gives the charge year and the old-structure figure.
- D10 gives the recast figure.
- D11 is the only document that says the recast moved the skin health business out of North America. D12's recast footnotes don't name skin health, so D12 can't replace it.
- D06 + D07 + D08 + D09 would give the same old-structure total quarter by quarter, but D09 is needed anyway.

**readings:**
- Fourth quarter only (the quarter of the charge): 1,021 − 934 = 87.
- 2024 instead of 2025: 4,113 − 3,716 = 397. This doesn't fit the question, because D09 places the charge in Q4 2025.
- 2026 (the year the charge was announced): not answerable, since the packet only goes up to Q2 2026. The documents clearly treat this as a 2025 charge.

**gaps:**
- No document states skin health net sales directly; the figure is a derived difference. It assumes, as D11's footnote says, that skin health was the only thing taken out of North America.
- Segment figures are rounded to the nearest million, and the tables note they "may not sum due to rounding", so the true figure could be off by about $1 million.
- Coverage:
  - Fully read: D01 (a 2019 stock unit award agreement, not relevant) and D10.
  - D09: read lines 1–180 and 440–600.
  - D02–D08, D11 and D12: covered only by targeted searches ("skin", "Filorga", "EltaMD", "PCA SKIN", "derm", "goodwill", "impairment", "write-down", "North America", "recast"); not read in full.
  - All documents are text-only; there are no PDFs or layout files, and the extraction showed no problems.

**contaminated:** no

Screen result: match (gold $366 million), high confidence; readings 87 (Q4 only), 397 (2024).

## i04 closed-book (closed-book-solver, question only)

Question: Measured as Colgate measures segment operating profit, what was its skin health business's result in the quarter in which it took the goodwill and intangible assets impairment charge on that business, in millions of dollars?

Return (verbatim):

answer: unknown. As far as I know, Colgate has never published a separate operating profit figure for skin health. The $721M goodwill and intangible assets impairment, which I believe was taken in Q3 2022, was booked in Corporate. On Colgate's segment basis it was therefore left out of segment operating profit, with $0 effect.

confidence: low

basis: From memory, Colgate took a $721M impairment on its skin health business (mainly Filorga) in Q3 2022 and reports such charges under Corporate, not in segment operating profit. Skin health (EltaMD, PCA Skin, Filorga) is split across the North America and Europe segments. I don't recall any disclosure of its own segment-basis profit, so the specific number likely depends on a document I don't have. I also have a faint, unconfirmed memory of a later skin health impairment, around Q4 2025, which could change which quarter is meant.

contaminated: no

Screen result: misses (gold -$4 million). Same real-world 2022 impairment ambiguity as i02.

## i04 blind solve (blind-solver, q01 rev 0 solver-2 packet)

Summary of the verbatim return (full text in the task notification of 2026-10-06; key lines):
answer: About -$4 million (an operating loss of roughly $4 million in Q4 2025), medium confidence.
Path: D09 l.71 (fourth quarter), l.491 (impairment in Corporate), l.477 (Q4 North America OP 203);
D11 l.85 (only skin health left North America); D10 l.25/l.333 (790 - 583 = 207); 203 - 207 = -4;
EMEA/AP cross-check 432 - 436 = -4.
readings: "Full year minus nine months (-3): ... Full year = 784 - 790 = -6; nine months = 580 - 583
(D08, line 436) = -3; Q4 = -3. It differs from -4 only through rounding ... The EMEA/Asia Pacific
version of this route gives -2." Including the impairment: about -$923 million.

Screen result: match on -4, but defensible rounding routes give -3 and -2 at the asked precision.
Decision: drop i04 (one-clear-answer risk; the platform returns such questions as "answered
inconsistently").

## i07 closed-book (closed-book-solver, question only)

Question: By what percentage did full-year net sales of the operations Colgate moved from its Africa/Eurasia segment into its Europe, Middle East & Africa segment change from 2024 to 2025? Give the sign, to two decimal places.

Return (verbatim):

answer: About +3%. This is a guess; I don't recall the exact two-decimal figure.
confidence: low
basis: This is inference, not recall. I'm assuming the operations moved into Europe, Middle East &amp; Africa are most or all of Colgate's former Africa/Eurasia segment (Middle East, Africa, Turkey and Eurasia). In 2025 that business probably grew organically by mid-single digits while currency headwinds eased, which would point to a small rise in net sales. I don't remember the restated 2024 and 2025 net sales for the moved operations, which a two-decimal answer would need. Those figures would likely be in Colgate's 2026 filing of restated segment results or its Q1 2026 10-Q.
contaminated: no

Screen result: misses (gold +7.85%).

## i06 closed-book (closed-book-solver, question only)

Question: By how much did full-year net sales of the operations Colgate moved from its Africa/Eurasia segment into its Europe, Middle East & Africa segment change from 2024 to 2025, in millions of dollars? Give the sign.

Return (verbatim):

answer: About +$40 million (an increase). This is an estimate, not a recalled figure.
confidence: low
basis: I don't remember the recast segment figures that would show these operations' 2024 and 2025 net sales. From memory, Africa/Eurasia had about $1.1B in yearly sales. In 2025, organic growth was mid-single digits. Weaker Turkish, Egyptian and Nigerian currencies were partly offset by a stronger ruble and rand. If most of the segment moved to EMEA, that points to a modest increase of roughly $20–50M. The missing information is Colgate's disclosure of the moved operations' net sales for both years.
contaminated: no

Screen result: misses (gold +$69 million).

## i07 blind solve (blind-solver, q01 rev 0 solver-2 packet)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
answer: +7.85% ; confidence: high.
path: D11 l.85 composition and Russia/Belarus move; D09 Table 5 FY 2025/2024 (A/E 1,172/1,095; AP
2,814/2,858); D10 l.25-28 and l.56-59 (AP 3,038/3,074; EMEA 4,276/4,046; NA 3,679/3,716); Russia and
Belarus 224/216; moved operations 948/879; cross-check via EMEA - Europe - skin health (948/879);
"(948 - 879) / 879 = 69 / 879 = 0.0784983, which rounds to +7.85%".
minimal_documents: D09, D10 and D11 (D05 can replace D09 for 2024 only).
readings: whole Africa/Eurasia +7.03% (D09 Table 7 prints 7.0%); Russia and Belarus only +3.70%.
gaps (quoted): "Inputs are rounded to $M ... and the result (7.8498%) sits close to the 7.84/7.85
boundary. So the second decimal is exact only for the reported figures."

Screen result: match (gold +7.85%). Caller note: the two-decimal percentage invites a precision
objection; the integer dollar form (i06, +69) carries the same dependency without it.

## i06 blind solve (blind-solver, q01 rev 0 solver-1 packet)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
answer: "+69 million dollars. Net sales of the Africa/Eurasia operations that moved into Europe,
Middle East & Africa rose from about $879 million in 2024 to about $948 million in 2025." ;
confidence: high.
path: D11 l.85 composition; D09 Table 5 FY 2025/2024 (NA 4,045/4,113; Europe 2,962/2,770; AP
2,814/2,858; A/E 1,172/1,095); D10 l.25-28/56-59 (NA 3,679/3,716; EMEA 4,276/4,046; AP 3,038/3,074);
Russia and Belarus 224/216; moved operations 948/879; change +69; cross-check EMEA - Europe - skin
health 948/879; bridge of EMEA's +230 = Europe +192, skin health -31, moved operations +69.
minimal_documents: D09, D10, D11 (D05 can replace D09 for 2024 only; nothing replaces D11).
readings: whole Africa/Eurasia +77 (ruled out by D11); new segment minus old Europe only +38;
whole new segment +230 (different question).
gaps: derived not disclosed; rounding to nearest million could move the true change by 1-2.

Screen result: match (gold +$69 million), high confidence.

## i08 closed-book (closed-book-solver, question only)

Question: As of June 30, 2026, how much of the midpoint of Colgate's latest estimate of cumulative pretax charges for its Strategic Growth and Productivity Program had not yet been recorded, in millions of dollars?

Return (verbatim):

answer: about $100 million (a guess)
confidence: low
basis: I remember only roughly that Colgate started its Strategic Growth and Productivity Program in late 2025 or early 2026. I don't remember the filing for the period ending June 30, 2026. My answer guesses a pretax charge range of $200 million to $300 million, which has a midpoint of $250 million. It also guesses that about $150 million had been recorded by June 30, 2026. Both numbers are inferences from Colgate's past restructuring programs, not recalled figures. To answer properly I would need the latest charge range and the total charges recorded to date, both from that filing.
contaminated: no. The only extra context was an automatically attached user email and the working-directory path, and neither says anything about the answer.

Screen result: misses (gold $132 million); it recalls the original $200-300 million range (public,
August 2025) but not the April 2026 expansion.

## i08 blind solve 1 (blind-solver, q01 rev 2 solver-1 packet)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
answer: "$132 million. The midpoint of the latest estimate is $450M, and $318M of SGPP pretax charges
had been recorded by June 30, 2026, so $132M had not yet been recorded." ; confidence: high.
path: D11 l.39 ($350-550M, midpoint 450; the "$200 million to $300 million, annually" figure is
savings); estimate not revised by June 30 (D12 has no estimate); no SGPP charges before Q4 2025 (D08
l.450); 2025 pretax 13 (D09 l.865 with note l.903; l.495); Q1 2026 pretax 176 (D11 l.548 = 171
operating + 5 non-service); 1H 2026 pretax 305 (D12 l.800 = 300 operating + 5 non-service; Q2 129);
13 + 305 = 318; 450 - 318 = 132. Rows checked against docs/ originals.
minimal_documents: D09, D11, D12.
readings: operating-profit charges only 450 - 313 = 137 ("leaves out the $5M SGPP charge in
non-service postretirement costs, even though it is pretax, so it is weaker"); 2026 only 145 (weaker);
original estimate (rejected).

Screen result: match (gold $132 million), high confidence.

## i08 blind solve 2 (blind-solver, q01 rev 2 solver-2 packet)

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
answer: "$132 million. The midpoint of the latest estimate is $450M, and $318M of pretax charges had
been recorded through June 30, 2026." ; confidence: high.
path: D11 l.39 (350-550, midpoint 450; D12 gives no new estimate; only D07 and D11 contain charge
ranges); D07 l.41 / D08 l.37 alias; no charges through Q3 2025 (D08 l.450, l.135); FY2025 13 (D09
l.865, note l.903, Q4 l.703, l.495); Q1 2026 176 (D11 l.548 = 171 + 5); H1 2026 305 (D12 l.800 = 300
+ 5; Q2 129, 176 + 129 = 305); 13 + 305 = 318; 450 - 318 = 132.
minimal_documents: D09, D11, D12.
readings: operating-profit charges only 137 ("weaker for a question about cumulative pretax
charges"); 2026 only 145; original estimate -68 (rejected).

Screen result: match (gold $132 million), high confidence. Both strong solvers converge on 132 and
class 137 as weaker; promoted to q02 for full checks.
