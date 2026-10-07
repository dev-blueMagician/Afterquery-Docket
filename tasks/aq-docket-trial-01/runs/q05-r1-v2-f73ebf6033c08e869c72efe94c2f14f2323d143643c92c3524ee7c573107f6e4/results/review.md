# q05 rev 1 bound review (question-review agent, fresh context), 2026-10-06

Input: frozen fields (questions/q05.md rev 1), prepared run, tested_sha256 f73ebf60..., target easy,
rev 1 and rev 0 raw returns, q04's review, comparison files aq-docket-trial-02 q01 and
aq-docket-trial-06 q02. Return copied verbatim from the task notification.

I found no blocking issue. q05 is fair and its gold is supported, but it is only marginally Easy: a Too easy result is about as likely as an Easy one. The pass/fail rows count FAIL/WARN results from the floor checker (`check_questions.py`).

**q05 (rev 1; tested_sha256: f73ebf6033c08e869c72efe94c2f14f2323d143643c92c3524ee7c573107f6e4)**

**gold_verified: yes.** I recomputed it in Python with exact fractions and Decimal.
- Brain share: 33,538 − 14,638 = 18,900, and 18,900 / 33,538 = 0.5635399 (D05 l.783).
- Autoimmune share: 3000 − 979 = 2,021, and 2,021 / 9,671 = 0.2089753 (D02 l.431 and Appendix A l.723–725).
- Ratio: 182,781,900 / 67,780,298 = 2.696682, which gives 2.7.

Rounding paths:
- Every reasonable path gives 2.7: percentage shares rounded to 0–4 decimals (half-up or half-even), fractions rounded to 2–4 decimals, truncation at one decimal or finer, and 2.70 then 2.7.
- Only two unreasonable paths break it: one-significant-figure fractions (0.6 / 0.2 = 3.0) and whole-percent truncation (56 / 20 = 2.8).
- Table 2's module sizes add up to 979, and the smallest module has exactly 20 genes.

Premises and other readings:
- **Sec. 5.1 "Small or weakly defined clusters are removed":** no count or second rule exists anywhere, and Appendix A credits the result to the size rule ("This resulted in 979"). No alternative number can be computed.
- **Sec. 5.5 "19 gene modules from 979 genes":** read as the starting count, no genes are removed and the ratio is undefined. WGCNA did start from those 979 genes.
- **WGCNA (4 grey-module genes):** gives 1,362.5, but it is not the selected model (l.447, l.725). 3000 − 975 gives 2.6914, the same 2.7, so it does no harm.
- **HVG analysis:** gives 4.4. **Brain kept share:** gives 2.1. **MAD step:** 0.8. **3000 base:** 0.8. **All 8,692 removals:** 0.6.
- **Other bases:** a bundle-wide search of "N genes" totals finds only 9,671 and 33,538. D01's 2,194 genes are a leukemia dataset, and D05's 12-section study prints no gene count.
- **Table 2 "mapped genes" (939):** would give 2.6, but that column is gene mapping for the enrichment analysis, not a removal step, so it is not a defensible reading.
- "For its selected model" is true: the 19 modules are the input to the K = 9, q = 8 model.

**outcome: A: match; B: match.**
- Both solvers returned 2.7 with high confidence from separate packets (solver-1 and solver-2). Both packets are byte-identical to the snapshot corpus.
- Both solvers rejected 0.6, 0.8 and the WGCNA route. Neither reported contamination.
- This agrees with the two rev 0 matches (2.70).

**closed-book: misses.** It answered "unknown" and could not identify either study.

**necessity:**
- **D02** is the only source of 9,671, of 3000 (the autoimmune MAD count, printed once) and of 979.
- **D05** is the only source of 33,538 and 14,638 (l.783; the repeat at l.1055 is in the same document).
- No smaller set of documents works.
- One decimal widens the window a forced guess has to hit:
  - Without D05, a guess must put the brain discard share in [55.38%, 57.47%), which is 14,265–14,965 genes retained. At two decimals that window was only 0.21 percentage points wide.
  - The probe without D05 guessed 3.0 (about 63% discarded) and the rev 0 probe guessed 2.39 (about 50%). A natural "about 15,000 retained" guess gives 2.6 and also misses. Risk about 5%.
  - Without D02, the window is (20.49%, 21.27%], and that probe guessed 11.3. Risk about 1–2%.

**shortcut: clear.**
- My shortest route is the same as the auditor's: D05 l.783, D02 l.431, then Appendix A l.723–725, two subtractions, two divisions and the ratio.
- No passage prints 18,900, 2,021, 8,692, either share or the ratio. "2021" appears only as citation years, including on D02 l.431 itself.
- Searching the question's words ("low-expression", "selected model") finds the input sentences, not the answer.
- The Doc 2 overview prints "top 3000 genes ranked by MAD · 979 genes grouped into 19 modules". That is navigation and inputs, not the answer, but if the platform's solver sees it, the trap gets weaker.

**source_assessment:** there are no gaps.
- `source_gaps` is [] with hash 4f53cda1…, and the intake shows all six documents complete with 0 gap characters.
- The capture's hash (342b8839…) matches the intake.
- Figure images are not in the text, but every input is running text, so missing figures cannot affect the premises, gold, exclusions, uniqueness, necessity or shortcut coverage.

**difficulty: easy (marginal).**

Compared with q04, q05 is harder in three ways:
- It drops q04's pointer to the right base ("genes each step started from").
- The module step's discards are printed nowhere, and the base comes from a different section.
- One decoy is live: a reader who stays in Sec. 5.1 sees 9,671 and 979 but not 3000, and answers 0.6.

It stays Easy-leaning because:
- "Undersized modules" and "selected model" lead straight to the Appendix A paragraph, where 3000 sits one sentence before 979.
- Sec. 5.1 itself points readers to Appendix A.
- The overview prints 3000 and 979.
- The question's own words rule out every other wrong route.
- One decimal removes the rounding miss route, which is correct, because a miss there would have been unfair.

I estimate the Low model gets each attempt right about 60–75% of the time.

| Platform outcome | q05 | q04 (its review) |
| --- | --- | --- |
| Too easy (Low 4–5/5) | ~50% | ~65% |
| Easy (Low 1–3/5) | ~40% | ~30% |
| Low 0/5, moves on to Medium | ~10% | ~5% |
| Quick test survives | ~30–35% | ~20–25% |
| Document check flags a document | ~5% | ≤5% |
| Closed-book check reaches the gold | <1% | <1% |

If the Low model goes 0/5, Medium 1–3/5 would place it in the Medium tier, which is above the target. We have no local record of what the platform does with Low 0/5 followed by Medium 4–5/5.

**verdict: ready.** This is a local judgement only; the platform result is still pending.

**findings:**
1. **Gold and one answer (Q4, Q9):** reproduced as above. Every alternative either differs at one decimal or is ruled out by the question's words. Nothing further to verify.
2. **Form checks (Q5, Q14):**
   - The question is 44 words with no digits and one ask. "Divided by" fixes the direction, and "Give one decimal place." is in the question box.
   - The answer "2.7 times" is two words, has no semicolon, carries a unit and matches c1.
   - All 8 evidence quotes and all 8 quotes inside the reasoning appear exactly once, word for word, in `docs/`, `text/` and the capture's Doc 2 and Doc 5 text.
   - The Appendix A paragraph break is handled: one quote ends at "fewer than" and the next starts at "20 genes". The joined phrase has 0 hits and appears only as unquoted paraphrase in step 2. The quotes hold whether the platform keeps or removes the break.
   - My emulation of the reasoning-number rule flagged nothing. Steps 4, 7 and 10 reuse derived values (2,021, 18,900) in steps that cite their own document. The only precedent that passed, aq-00949 q05 rev 0, was a two-document step, so this is a low remaining risk. Check the form panel when pasting; any edit means re-preparing and re-running the checks.
3. **Wording (Q3, Q7, Q8, Q10, Q12):** it asks about the world, not the set. Each description fits one thing, there is no false premise and nothing is given away.
4. **Levers and tags (Q6, Q11):** "Match, then exclude" here is a numeric exclusion inside D02, and it is active: skipping it gives 0.6. All three tags are acceptable.
5. **Records:** the report recomputes f73ebf60…, and every rev 1 record (A, B, closed-book, audit, probes) carries it. The floor shows 0 FAIL and 2 WARN (origin claude, and sibling of q04), both explained. Status may become `checked`, not `ready`.
6. **Local notes (not fingerprint-bound, so fix without re-testing):**
   - Lever checks say "3000 is printed once in the bundle". "3000" also appears in D05 (l.767, 815–859, 1055, 1071) and "3,000" in D05 l.783 and D06. It should say the autoimmune MAD count is printed once.
   - The i17 row in `ideas.md` says the ratio is "stable at 2.70 on every rounding path". That is out of date: whole-percent rounding gave 2.67 at two decimals, which is why rev 1 moved to one decimal.
7. **Set:** q04, q05 and sketch i10 share the same answer path, so submit at most one. q05 is the better choice for the single attempt; quick-test it first.
8. **Not checkable locally:** restricted names, originality and duplicates, the token window, and Q13 (the measured platform tier) are unknown.
