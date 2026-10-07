# q01 rev 0 independent review (fresh question-review)

Date: 2026-10-06. tested_sha256: 866f2ddd97642838aeb5ce32828c7229cd162a80174786f807cf02307d3322ca

Raw return:

The question is fair and its answer checks out locally, but I expect it to land in the Easy tier, below your Medium target. So "ready" below covers fairness and correctness only, and I'd quick-test it before spending the difficulty run on it.

q01 (rev 0; tested_sha256: 866f2ddd97642838aeb5ce32828c7229cd162a80174786f807cf02307d3322ca)

gold_verified: yes - I parsed D04 myself. The only rows in the bundle containing both "Brochure" and "Counted" are:
- Wave 2 items 29-47 (l.612-632): 19 rows, 4,735,573.
- Wave 3 row 3 (l.734): "How People Area Counted Thai 85,850".
My script sums them to 4,821,423 (exact integers, no rounding).
- Wave 2's 121 rows add up to its printed 26,230,373.
- Wave 3's rows add up to 7,697,271 against a printed 7,652,496. The 44,775 gap equals a confidentiality-flyer row, not the brochure's 85,850.
- In D06 App F (l.723-742) the brochure has items 24, 26 and 27. The Poster Series, Fotonovela and Toolkit have one award each.
- Neither 4,821,423 nor 4,735,573 is printed anywhere in the bundle.

outcome: A: match; B: match - both answered 4,821,423 with high confidence. Their packets were fresh, held only the question, and contained byte-identical copies of the documents. Both named the Wave-2-only route and ruled out the Mural ads. B also dealt with the brochures in the nine ARRA languages and the reading where items 25 and 26 count as one.

closed-book: misses - it answered "unknown" and recalled no piece or quantity.

necessity:
- Doc 1 (D06) is the only per-piece awards list. D03 l.92, D05 l.512, D02 l.407 and D06 l.465 give only totals. The removal probe without Doc 1 could not answer; its forced guess was 6,528,160 (the Action Poster) at p 0.03.
- Doc 4 (D04) is the only source of per-version quantities. No other document has brochure rows.
- No smaller set of documents works.

shortcut: clear - the shortest path is: count awards in App F, scan App B for "Brochure"/"Counted" (all 20 rows), then add. No passage, summary or task-page overview states the total or names the most-awarded piece. The overview (capture l.27-53) shows only "55 total awards won" and "288 different promotional materials". That makes it a difficulty risk, not a Guide violation.

source_assessment: no gaps are recorded. The intake shows all six documents complete (gap_characters 0, matches_capture true), and the snapshot's gap list is empty (hash 4f53cda1...). The doc map lists ranges that are captions or images only:
- D06 App B, a costs chart (l.562-566)
- D05 Table 1, Figures 1-5 and its appendix timeline
- D03's media-outlet appendix (l.427)
- D02 Figures 1-2
- D04's App A timeline, the App C/D review marks, and the "*"/"**" markers
None of these affects the question:
- Premises and gold: every fact comes from App F text and App B rows, and none of these ranges falls in either.
- Exclusions: none are claimed.
- Uniqueness: App F is numbered 1-55 without a break and ends with "TOTAL AWARDS WON 55", and the App B section totals add up. So no award or brochure row can sit in these ranges.
- Necessity and shortcut: none of these ranges prints item quantities or per-piece awards.
The platform shows the same text, so the missing-images warning still stands.

difficulty: easy - below the Medium target. My estimates:
- Too easy ~8%
- Easy ~65%
- Medium ~20% (includes Low 0/5 then Medium 4-5/5, whose platform label is not documented)
- High ~5%
- Too hard ~2%
- Basis: a binomial mixture with low-model success per attempt of 0.18-0.53 and medium about 0.59 put Low at 0/5 only about 17% of the time. I shifted the estimates toward harder because local reviews have underestimated traps before.
- Low model: most misses should be the Wave 3 Thai row (answer 4,735,573), then errors in the 20-number sum, then picking the wrong piece (Mural or 2010census.gov, four awards each).
- Medium model: misses the Thai row sometimes, the arithmetic rarely.
- Why Easy-leaning:
  - The only wrong route is leaving a row out; there is no printed decoy that looks like an answer.
  - "Across all of its language and audience versions" tells the solver to hunt for more versions.
  - A model reading the full text is barely slowed by the "Area" typo, because Brochure, How People, Counted and Thai all still match. The real obstacle is that the row sits in a separate table after Wave 2's printed total, and all three Opus runs found it.
  - Misses that come from arithmetic errors are misses for the wrong reason, so a Medium placement built on them would be fragile.
  - On the D1-D7 risk checks, D1, D2, D5 and D6 hold; D3, D4 and D7 are only partial. That is the same pattern as earlier questions that came back Easy or Too easy.

verdict: ready (fairness and correctness only; not suitable for the Medium target)

findings:
1. One piece fits the description (Q4; App F l.664-827; D02 l.405-407).
   - Across App F, Mural (items 1, 2, 6, 10) and 2010census.gov (47, 49, 50, 54) have four awards each. The Greg Biffle PSA (28, 29, 39), Issues Management (33, 38, 45) and Social Media (43, 44, 46) tie the brochure at three.
   - "Partnership promotional piece" plus "copies listed" rules all of these out, and only the brochure has App B rows, so the answer is unique.
   - Remaining risk: D02 calls the PSAs coordinated by the National Partnership office "award-winning". A broad reading therefore gives a 3-3 tie with the Biffle PSA, and the platform's advisory check "Each description fits one thing" could flag it.
   - Limiting the description to printed materials would remove the tie. The Mural would then be excluded only by "partnership", because item 10 covers its "Print and OOH Ads".
   - Reasoning step 1 rules out Puerto Rico Doors, which has only two awards, but not the Biffle PSA or the website. Add those on any future revision.
2. "Listed for distribution" fixes a single total (D04 l.212, l.786-864, l.944-994).
   - App E is a surplus table by language, with no item rows.
   - The ARRA, Reprint and Reorder lists have no brochure rows.
   - The brochures said to exist in the nine ARRA languages (l.212) have no listed quantity, so "listed" leaves them out.
   - "Language and audience versions" covers the Spanish (PR), NHPI and AIAN rows.
   - The Wave 3 total discrepancy does not involve the brochure row.
3. Form number rule (Q14): passes as written.
   - I checked it step by step: the numbers in step 1 all occur in Doc 1, every operand in steps 2-4 occurs in Doc 4, 4,821,423 comes straight after "=", and the decoy line contains only "2" and "3".
   - All 29 evidence quotes and the phrases quoted in the reasoning match the documents word for word, with straight quotes.
   - A 20-number sum in one step has not yet been seen on the form. None of the known failure causes applies: parentheses, a restated result, several "=" in one step, or a label naming a period the document gives as a rounded figure.
   - If the form flags it, split it into a Wave 2 subtotal step and a final two-number step. q02's 27-number sum will test the same thing.
4. Measurement plan. None of the 10 quick tests has been used yet (capture l.79). Quick-test this first. If the low model solves it, don't spend the difficulty run hoping for Medium. If it survives, that still does not establish Medium.
5. Wording changes (described only).
   - The one fair way to strengthen it is to soften the completeness hint: ask for the piece's total listed copies without spelling out "language and audience versions".
   - Keep a sense of "total", so that counting only the English original (920,100) stays excluded.
   - Expected gain is a few points at most, and the change would need fresh solves, a new audit and a new closed-book run.
   - Adding a language-subset filter from Doc 2 would copy q02's mechanism and drift toward a rulebook. Share or ratio versions run into the question of what language the NHPI and AIAN rows are in.
   - The planner frame makes no difference to difficulty; the task page asks for practitioner scenarios.
6. Set overlap. q02 also sums D04 App B rows and answers in copies, so the two share a document and a shape. Neither gives the other away. Vary the design if you write a replacement.
7. Records and platform-only checks.
   - The report recomputes the same fingerprint (866f2ddd...). The removal probe removed only D06 and kept the document ids contiguous. The report leaves out audit records by design.
   - The floor's one warning (origin claude; the export takes origin user only) remains an authorship and export blocker to resolve separately.
   - Restricted names, "Original question" and "Not a duplicate" can't be checked locally. The closest match among 73 workspace questions has a token-overlap ratio of 0.26 and a longest shared run of 3 tokens.
8. Form model-check risk. If two of the form's solvers both stop at Wave 2, the form may block the question as "too vague", as happened with aq-01321 q02. The defence is that Wave 3 has its own distribution timeframe and the row carries the same title. Locally, 4,735,573 is not a defensible reading.
