# q01 rev 0 - independent review (question-review, fresh context)

Date: 2026-10-05. Input: frozen snapshot, live question file, results/returns.md, results/gap-index.md,
corpus. Return below as delivered, unedited.

q01 (rev 0; tested_sha256: fbb841e51c467054da11e1f34541ebeada5fffc88b5df62b62403e261f51f3ff)

**gold_verified: yes.** I recomputed it from the passages with exact fractions.
- **January range:** D07 (dated Jan. 22, 2026, l.19) gives $5.55–$5.80 (l.31/283), midpoint 5.675.
- **July range:** D10 (dated July 16, 2026, l.21) gives $5.45–$5.60 (l.29/289), midpoint 5.525.
- **Result:** 5.525 − 5.675 = −0.150 exactly, so −$0.15 under any rounding rule.
- **Selection:** the deal closed March 23, 2026 (D08 l.27; also D08 l.47/127/137/403 and D10 l.49/183/593/629). The next range, $5.38–$5.58 (D08 l.19/31/203), carries D08's April 16, 2026 dateline (l.21), 24 days after closing. So the January range was in force at closing.
- **One stated figure per input:** each range is printed the same way everywhere it appears.
- **Alternatives, none allowed by the wording:**
  - April range as the base: +0.045 (+$0.05 or +$0.04).
  - April minus January: −0.195.
  - April range plus the $0.20 dilution, as a stand-in for the pre-deal range: −0.155. No document states that range.
  - Reversed sign: +0.15.

**outcome: A: match; B: match.** Both solvers worked inside their packets, reported no contamination, and answered −$0.15 by the same route. Both raised the April-range reading and rejected it using D08's dateline, which the wording "in force when it completed" requires. That reading is a wrong lever, not an ambiguity. Two distinct fresh matches validate the gold.

**closed-book: misses.** It answered "−$0.20" as a low-confidence guess: the January range it remembered, minus an assumed $0.20 dilution. That is not equivalent to −$0.15 at the cent precision asked. Exposure is moderate, because the sign and rough size can be guessed. The exact cent depends on the July 2026 range.

**necessity:**
- **D07:** the only source of $5.55–$5.80 ("5.55" and "5.80" appear only at l.17/31/283).
  - Without it, nothing else works: D08 never names the range it replaced, and D10's "previous range" is the April one.
  - The add-back stand-in (5.58–5.78) is stated nowhere.
- **D10:** the only source of the July range ("5.45" and "5.60" appear only at l.19/29/289). D11 (Aug 20) has no guidance.
- **D08:** the only document that dates $5.38–$5.58 to after the closing (l.21 with l.19/31/203; headline l.15).
  - Without it, D10 gives that range only as an undated "previous range" (l.19/29).
  - D07 l.33 and D05 l.49 give only an expected close in Q2 2026. D09 and D11 have no guidance. No document states how often guidance is updated.
  - So the answer could be −$0.15 or +$0.045.
  - The closing date is repeated in D10, so it is not what makes D08 necessary.
- **No smaller valid set:**
  - {D07, D10} leaves the April range undated.
  - {D08, D10} lacks the January range.
  - {D07, D08} lacks the July range.

**shortcut: clear.** The verified shortest route matches the gold: D08 l.27 → D08 l.21 against l.19 → D07 l.19/31 → D10 l.21/29 → two midpoints and a difference.
- Searches for 0.15, .150, 5.675, 5.525, 5.48, 0.045, 0.195 and "midpoint" found only growth-at-the-midpoint wording.
- No passage pairs the January range with either the closing or the July range.
- Reading D10 alone leads to the +$0.045 decoy, which is a trap, not a shortcut.

**source_assessment:** All 128 gaps are irrelevant on all six dimensions (gap hash 40c0cca7…4189); details are in the gap grouping below. The corpus stays incomplete.

**difficulty: easy.** This is local suitability for the Easy target only.
- **For it:** it uses the same mechanism as the aq-00964 q01 pass. The event is reported in a release that prints its own post-event range (D08 l.19 beside l.27), and D10 l.29 points straight at that decoy.
- **D7 risk:** the right edition is also the first 2026 guidance, so a "use the original guidance" habit skips the date check.
- **D4 risk:** the decoy's refutation is on the same D08 page as the closing date.
- **D2 risk:** the capture overview lists all three ranges, April 16, and an unlabelled March 23.
- **D3 risk:** searching "Exact Sciences" leads straight to D08.
- **D1 risk:** moderate (see closed-book).

**verdict: ready.** This is local only: the platform measurement is pending and status stays `checked`.

**findings:**
1. **Interim guidance update (Q4/Q9, low risk).** No bundle document falls between Jan 22 and Apr 16, and D08 doesn't name the range it replaced. Three things support the gold:
   - D08 l.15 says it "Updates Guidance to Reflect Acquisition".
   - D08's dated Q1 bullets (l.33–37, January to March) mention no guidance change.
   - D10 l.29 links the July range back to April.

   Both solvers and the auditor flagged this and concurred with the gold. No change needed.
2. **Form number rule (unknown; can only be checked on the platform).** In my emulation, Steps 1–3, the conclusion and the decoy line pass; every decoy input appears in Doc 10. Step 4 cites "Doc 7 and Doc 10", and each of its inputs appears in only one of the two. How the form treats a step citing two documents has not been observed yet. Check the form after pasting.
3. **Evidence quote (advisory).** The D10 l.29 quote tagged [c1] supports ruling out the decoy, not an input to the answer. The form may flag it.
4. **Records.** Verified matches:
   - Snapshot and report fingerprint: fbb841e5…, recomputed live by the report.
   - All 23 corpus files and the 3 document packets match by hash.
   - The 4 question copies and 4 records match.

   The Source assessment and Review sections are empty; record this review against rev 0, fbb841e5… and gap hash 40c0cca7…. There is no platform record yet.

   The memory note about "aq-00745 q01 rev 1" being "Too easy" refers to an earlier, different tax-footnote question. Don't attribute that verdict to this content.
5. **Set check.** q02 asks about quarterly forecasts against actual results. It shares no answer path with q01 and neither gives the other away.

---

## Gap grouping

Every marker sits between two rows of the same table, on pages 2–21. None is on page 1 (headline, bullets, dateline) or in the guidance section (page 7) of any release. I checked this by script and confirmed it by reading D07, D08 and D10 in full.

**G1: sales-growth "% Change" rows, pages 2–6 (57 gaps).** Each hides the International, total-reported, currency-excluded and organic/comparable rows. D08's uncut Diagnostics table (l.111–125) shows the same rows: 176 characters across four columns. That fits D08 l.65's 196 hidden characters across five columns.
- **Premises:** the premise passages (D08 l.27; D10 l.21/29/289) are on pages 1 and 7, where there are no gaps.
- **Gold:** the hidden cells are growth percentages, not guidance, so the 5.675 and 5.525 inputs are untouched.
- **Exclusions:** the April range (D08 l.19/31/203) and the quarterly ranges (D07 l.283, D08 l.205, D10 l.291) are visible. A growth row cannot add or remove a full-year 2026 EPS range.
- **Uniqueness:** no row can restate a range differently; all three ranges are printed only in visible bullets and guidance sections.
- **Necessity:** these rows cannot print the January range or date the April range. D01–D04 rows are 2024–25 data from before the 2026 outlook (D07 l.15). Even if a row repeated the closing date, it would only duplicate the visible March 23 mentions.
- **Shortcut:** one-decimal percentage cells cannot state a midpoint or a change.

**G2: D01 footnote-3 COVID-test sales tables, page 8, l.363–397 (4 gaps).** These hold 2023–24 dollar sales in a release dated Jan. 22, 2025. The line "-- more --" after them is the original's page marker, which appears 19 times in the source before each footer; it is not a truncation.
- **Premises:** nothing about the closing or any 2026 range.
- **Gold:** D01 supplies no input.
- **Exclusions:** a release from a year before the 2026 outlook cannot hold a 2026 range.
- **Uniqueness:** no alternative input figure.
- **Necessity:** D01 is unlisted and replaces nothing.
- **Shortcut:** none.

**G3: statement-of-earnings top rows, pages 9 and 11 (12 gaps).** Each sits between the column header and the first visible line item (currency, interest or other income): net sales and cost lines.
- **Premises:** these are reported results, not guidance.
- **Gold:** the EPS rows below each gap are visible (D07 l.355/357, D08 l.275/277, D10 l.363/365) and are actual results, not ranges.
- **Exclusions:** an income statement cannot hold a 2026 range candidate.
- **Uniqueness:** no second figure for any input.
- **Necessity:** cannot print the January range or date the April range.
- **Shortcut:** none.

**G4: EPS reconciliation rows after "Intangible Amortization", pages 11–14 (24 gaps).** These are reported-to-adjusted rows for the period. Their totals repeat in visible prose and tax-rate tables (D08 l.319/345–349, D10 l.445/499–503).
- **Premises:** reported results only.
- **Gold:** actual adjusted EPS (e.g., $1.15 at D08 l.277) is not a guidance input.
- **Exclusions:** no 2026 range candidate.
- **Uniqueness:** no alternative figure.
- **Necessity:** cannot print the January range or date the April range.
- **Shortcut:** cannot state a midpoint change.

**G5: specified-items detail rows, pages 14–21 (24 gaps).** Each sits between the category header and the visible "Taxes on Earnings (d)" row: cost lines by category for the period. All six findings are the same as G4: actual results only, with no guidance, dates or closing statements, and no route to the answer.

**G6: document-level "incomplete capture" notes (7 gaps).** Each note's total equals the sum of that document's in-text gaps (5,198; 2,192; 4,344; 4,227; 4,355; 2,060; 4,073). They describe exactly G1–G5, not any extra missing text. Final page footers are present (D07 l.705, D08 l.469, D10 l.761), and D05, D06, D09 and D11 are complete.
- **Premises:** every premise passage is present.
- **Gold, exclusions, uniqueness, necessity, shortcut:** no effect beyond G1–G5.

**Assignment of all 128 labels** (checked by script: each assigned exactly once, and it agrees with a classification by the visible line above each gap):
- **G1 (57):**
  - D01 l.69, 91, 123, 149, 171, 201, 227, 251, 273, 301
  - D02 l.61, 91, 123, 155, 179
  - D03 l.65, 89, 123, 145, 165, 193, 213, 237, 257, 285
  - D04 l.63, 87, 121, 143, 163, 189, 209, 233, 253, 277
  - D07 l.65, 87, 119, 139, 159, 185, 205, 229, 249, 271
  - D08 l.65, 87, 157, 181
  - D10 l.67, 83, 105, 127, 203, 227, 247, 273
- **G2 (4):** D01 l.371, 379, 387, 395
- **G3 (12):**
  - D01 l.405, 447
  - D02 l.257
  - D03 l.357, 401
  - D04 l.345, 381
  - D07 l.341, 393
  - D08 l.261
  - D10 l.347, 401
- **G4 (24):**
  - D01 l.497, 509, 527, 539
  - D02 l.303, 315
  - D03 l.445, 457, 473, 485
  - D04 l.425, 437, 453, 465
  - D07 l.449, 459, 473, 483
  - D08 l.317, 327
  - D10 l.443, 453, 469, 481
- **G5 (24):**
  - D01 l.685, 715, 745, 775
  - D02 l.389, 417
  - D03 l.597, 625, 653, 681
  - D04 l.575, 603, 639, 667
  - D07 l.591, 623, 655, 687
  - D08 l.419, 451
  - D10 l.647, 679, 711, 743
- **G6 (7):** the docs/ notes for 2025-01-22, 2025-04-16, 2025-07-17, 2025-10-15, 2026-01-22, 2026-04-16 and 2026-07-16.

**Verdict on gaps:** all 128 are irrelevant to all six dimensions. No gap could hold a guidance statement, a dated range or a closing-date statement that would change this question:
- guidance is printed only on page 1 and page 7 of each release, and neither page has a gap;
- the hidden sizes fit numeric table rows;
- the per-document totals leave no unaccounted text.

The most a hidden row could add is a repeat of the March 23 date, which is already printed several times. The incomplete-corpus warning stays, and this does not establish complete coverage. This review does not verify any platform result.
