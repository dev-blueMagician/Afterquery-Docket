# q01 rev 1 independent review (fresh question-review)

Date: 2026-10-06. tested_sha256: bf62461660d05af3ce536190b5582a74aa318ec7e36c1eb2d2531287c4ea414b

Raw return:

q01 (rev 1; tested_sha256: bf62461660d05af3ce536190b5582a74aa318ec7e36c1eb2d2531287c4ea414b)

gold_verified: yes. I parsed D04 myself.
- Exactly 20 rows contain both "Brochure" and "Counted": Wave 2 rows 29-47 (l.612-632, 19 rows, 4,735,573) and the Wave 3 row at l.734 ("How People Area Counted Thai 85,850").
- A script adds them to 4,821,423. These are exact integers with no rounding.
- Cross-checks:
  - Wave 2's 121 rows add up to exactly the printed 26,230,373.
  - Wave 3's 28 rows add up to 7,697,271, against a printed total of 7,652,496. The 44,775 gap equals one confidentiality-flyer row (Khmer or Thai), not the brochure row.
  - The ARRA wave adds up to its printed 14,385,004 and has no brochure rows. The Reprint and Reorder lists have none either.
- D06 Appendix F is numbered 1-55 with no gaps and ends "TOTAL AWARDS WON 55". The brochure is items 24, 26 and 27. The Poster Series (22), Fotonovela (23) and Toolkit for Latinos (25) have one award each.
- Neither 4,821,423, 4,735,573 nor "4.8 million" appears in the documents or the capture.

outcome: A: match; B: match. Both answered 4,821,423 with high confidence. Each packet held only the question plus byte-identical documents (3 copies of each of the 6 hashes). Both raised the Wave-2-only and English-only readings. B also raised a loose "printed" reading that points to the Mural ads, and dismissed it because they aren't a partnership piece and have no listed copies. The git-status file list B mentions came from the harness and carries no answer, so it is not contamination.

closed-book: misses. It answered "unknown" with low confidence and recalled nothing.

necessity:
- Doc 1 (D06) is the only per-piece award list. D03 l.92, D05 l.512, D02 l.407 and D06 l.465 give only award programs or totals.
  - The rev 1 probe (byte copy minus D06, ids renumbered without a gap) found the question unanswerable. Its forced guess was the Action Poster, 6,528,160, at p 0.03.
- Doc 4 (D04) is the only source of per-item quantities. "How People" appears nowhere else, and D06 l.246 and D02 l.400 mention brochures only in general.
- No smaller set of documents works.

shortcut: clear. The shortest route is:
1. Count awards per piece in App F (3 against 1).
2. Find the brochure's App B rows. A search for "How People", "Counted" or "Brochure" catches the Thai row; only the exact full title misses it.
3. Add 20 numbers.
No passage or overview gives the piece or the total. The overview shows only "55 total awards won" and "288 different promotional materials". This is a difficulty risk, not a Guide violation.

source_assessment: The snapshot lists no source gaps (hash 4f53cda1...). The intake shows gap_characters 0 and matches_capture true for all six documents, and the corpus hashes I recomputed match the snapshot. The doc map's visual-only items don't touch any input:
- Premises and gold: the App F text and App B rows are complete. The "**" marker sits on the ARRA timeframe, a section with no brochure rows whose total reconciles. The "*" marker is on the calendar row, inside a Wave 2 total that reconciles exactly.
- Exclusions: no excluded piece depends on those ranges.
- Uniqueness: App F runs 1-55 without a break under a printed total.
- Necessity and shortcut: no gap range holds per-piece awards or item quantities.
The missing-images warning still stands.

difficulty: easy. This is below the Medium target. Estimates for rev 1 (rev 0 review in brackets): Too easy ~10% (~8%); Easy ~65% (~65%); Medium ~17% (~20%); High ~5% (~5%); Too hard ~3% (~2%).
- Basis: a Monte Carlo on my own assumptions, not a calibrated model. I assumed the low model picks the right piece 0.82-0.95 of the time, finds the Thai row 0.35-0.75, and sums correctly 0.70-0.92. That puts Low 0/5 at about 10%. I then shifted toward harder, because local reviews have underestimated trap questions before (aq-00964 q01, aq-00745 q09).
- What rev 1 changed: "printed" removes the four-award wrong-piece routes (the website, the Mural ads), which makes it easier. "In total" drops the explicit "all versions" cue, which makes it slightly harder. The net change is within about +/-3 points.
- Why Easy is still most likely: the only wrong route is leaving a row out; no printed figure in the documents looks like an answer; a model reading the full text in context is barely slowed by the "Area" typo; picking the piece is a clean 3-against-1 count; on the D-checks, D3, D4 and D7 are only partial, the same pattern as earlier questions that came back Easy or Too easy.

verdict: ready. This covers fairness and correctness only; the question is not suited to the Medium target.

findings:
1. The description fits one piece (Q4).
   - Pieces with several awards: Mural 4 (paid ads; item 10 includes "Print" ads, but "partnership" rules it out). 2010census.gov 4: items 47, 49, 50, 54, and possibly 48 and 51-53 (not printed).
   - Three awards each, none printed: Biffle PSA, Issues Management, Social Media.
   - Two each, all paid ads or PR: Puerto Rico Doors, "Believe", "A New Portrait of America".
   - The Biffle tie from rev 0 is gone.
   - Items 26 and 27 print no award level. They count as won only because of App F's title and its "TOTAL AWARDS WON 55". A reading that counted only labelled awards would contradict that printed total, so it is not defensible.
2. "In total ... listed for distribution" fixes one total.
   - Wave 2 only (4,735,573) is an omission, not a reading: the Thai row has its own distribution timeframe and the same title.
   - English only (920,100) is weak. App B's DESCRIPTION/LANGUAGE columns and D04 l.89 ("transcreated") treat the language versions as one material, and under that reading "In total" has nothing to add.
   - An English-audience subset (1,687,480) isn't prompted by anything in the question.
   - App E gives surplus by language, with no item rows.
   - D04 l.212 says brochures were developed in the nine added ARRA languages, but App B lists no brochure copies in them, so "listed" leaves them out.
   - The wording is slightly more open than rev 0's, but the risk of a "too vague" flag is low.
3. Form number rule (Q14): passes in my emulation.
   - Step 1's 34 numbers all occur in Doc 1.
   - Steps 2-4 use only numbers that occur in Doc 4, and 4,821,423 comes straight after "=".
   - The decoy line contains only 2 and 3.
   - The only spelled-out count is "one award", and Doc 1 contains "one".
   - A 20-number sum in a single step hasn't been seen on the form yet. If it gets flagged, split it into a Wave 2 subtotal step and a two-number final step, both citing Doc 4.
4. Minor accuracy point.
   - Step 1's list "Other multi-award entries..." leaves out "Believe" (items 4-5), "A New Portrait of America" (32, 40), the podcasts (30, 31, 35-37) and the possible website awards (48, 51-53).
   - The lever-check note's claim that step 1 "rules out every other multi-award App F entry" overstates this.
   - None of these pieces qualifies, so the answer is unaffected. Correct the note now, and change the field only if some other change forces a new revision.
5. Evidence advisory.
   - The five decoy quotes are tagged [c1]. "Evidence supports its component" accepts "a fact used to work it out", so they should pass; if they get flagged, they can be dropped without hurting necessity.
   - The item 10 quote stops before "Mural TV, Print and OOH Ads", so on its own it doesn't show the Mural link.
6. Measurement plan.
   - Quick tests used: 0 of 10. Quick-test this before spending one of the 8 difficulty runs.
   - If the low model solves it, it is Easy-class and below your target.
   - If it survives, that still isn't a Medium placement (aq-00949 round 4).
7. No fair change is likely to reach Medium reliably.
   - Getting there would need a printed figure that looks like an answer, or a second dependent step. This bundle doesn't print one for this piece.
   - The available extra filters (NHPI/AIAN audience versus language, the unlisted ARRA-language brochures) would add ambiguity or a rulebook.
   - Wording tweaks would gain a few points at most.
8. Overlap with q02.
   - q02 also adds up D04 App B rows and answers in "copies ... listed". Different rows, different bridge, no giveaway.
   - Token overlap is 0.277 with a longest shared run of 2 tokens. That is the highest of 75 questions compared, and below the near-copy limits.
   - The answer path is shared, so vary the design on any replacement.
9. Records.
   - The report recomputes bf6246..., with A, B and closed-book returns recorded at rev 1. The audit and probe are bound to the same question bytes.
   - The floor shows 0 FAIL and 1 WARN: origin is claude, but the export accepts only user. That is an authorship and export issue to resolve separately.
   - Not checkable locally: restricted names, Original question, Not a duplicate, the stated-figure matcher, and whether the form reads the commas in "4,821,423" as list separators.
   - There is no platform evidence yet. Status should stay at most checked.
