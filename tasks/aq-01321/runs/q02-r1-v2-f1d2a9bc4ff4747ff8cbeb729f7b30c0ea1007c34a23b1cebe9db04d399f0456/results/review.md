# q02 rev 1 independent review (fresh question-review agent), 2026-10-06

tested_sha256: f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456
Input: frozen fields (snapshot), corpus, raw rev 1 A/B/audit/closed-book returns, rev 0 review; target medium. Return copied verbatim.

---

q02 (rev 1; tested_sha256: f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456)

**gold_verified: yes.** I recomputed the gold from the originals; the docs/ rows match text/.
- TTM R&D: 2,083 − 517 − 527 + 510 + 535 = 2,084. TTM SG&A: 1,860 − 472 − 485 + 464 + 490 = 1,857. Combined: 3,941.
- Revenue: Doc 9 prints 19,453, and rebuilding it gives the same figure (17,682 − 4,069 − 4,448 + 4,825 + 5,463).
- 3,941 / 19,453 = 20.25909%, which is 20.26 under both half-up and half-even rounding. Only numerators of 3,941 or 3,942 give 20.26.
- The quarter route agrees: derived Q3 2025 is 518 + 457 = 975, and 975 + 967 + 974 + 1,025 = 3,941. The derived Q3 2025 revenue of 4,742 fits Doc 7's "decreased 7% sequentially" (−6.7%).
- Rounding order doesn't change it. Two- or three-decimal shares give 20.26, and so do rounded quarterly headline revenues (19,452). Only mixed-precision slips (3.94 / 19.453 gives 20.25) differ, and those are solver errors.
- I reproduced every step value in the reasoning.
- Wrong routes at two decimals: 20.05 ($3.9B), 20.27 (2025 numerator), 21.30 (twelve months to March), 22.30 (calendar 2025), 20.43 (adding acquisition charges), 21.04 (adding acquisition and restructuring), 20.34 (mean of the quarterly ratios), 19.43, 18.76. None fits the wording.

**outcome: A: match; B: match.**
- Both answered 20.26% with high confidence, using separate packets that contain only the verbatim question.
- Both rejected 20.05% as too coarse, and also 21.04%. A also rejected 22.30%; B also rejected 18.76% and checked the rounding boundary.
- The memory note that leaked the gold in rev 0 no longer states it (docket-general-knowledge-check.md L53-61).
- That gives two supported matches on the current fingerprint.

**closed-book: misses.** It answered "About 22.2%" with low confidence, which is not equivalent to 20.26%. It recalled 2025 revenue (Q3 about $4.74B, Q4 about $4.42B) but no 2026 line items.

**necessity:** The smallest valid set is Doc 7, Doc 8 and Doc 9. TI appears only in D10-D12, and no TI release has six-month or twelve-month R&D/SG&A figures.
- **Doc 7** is the only source of the 2025 R&D and SG&A (2,083 / 1,860).
  - Without it, the "$3.9 billion" statements in Doc 8 and Doc 9 only bound the result to 19.86–20.30%. Face-value routes give 20.05 or 20.12; the probe answered 20.05.
  - Reaching the gold would need July–December 2025 to land on 1,942–1,943 out of a 100-value window.
  - Residual risk: a model that recalls the 2025 line items exactly.
- **Doc 8** is the only source of both Q1 columns.
  - Without it, the twelve-month total is 3,956 + (Q1 2026 − Q1 2025), which is unknown. Bound 19.79–20.30; face value 20.05; probe 20.05.
  - Residual coincidence: of my 25 natural guesses, one hits the gold (split 1,964 evenly and set Q1 2026 equal to Q4 2025). It is 1 of the 4 guesses that respect the $3.9B bound, and about 2.8% of all integer pairs that respect it.
- **Doc 9** is the only source of both Q2 columns and the twelve-month revenue. Without it, twelve months to March gives 21.30, and 18 guesses built on the Q2 outlook range 20.17–20.95, none of them 20.26.
- The removal-probe results are stored only as summaries in runs/sketch-round1/returns.md, not raw returns. My conclusions rest on my own computation.

**shortcut: clear.** The auditor's route is right: Doc 7's 2025 column rolled forward with the Doc 8 and Doc 9 quarter columns, over Doc 9's twelve-month revenue.
- A search of the whole bundle finds no 3,941, 20.26 or twelve-month R&D/SG&A figure. The only hits are unrelated substrings: D12 L177 "(2,001)" and D10 L132 "(42,084)".
- The overview for Docs 7–9 lists no R&D or SG&A.
- The one-document $3.9B route gives a wrong answer, so it is a lever, not a shortcut.

**source_assessment:** No gaps are recorded, so there is nothing to map.
- intake.json shows 12 of 12 documents complete, with zero gap characters and every file matching the capture.
- The snapshot lists no source gaps (hash 4f53cda1…). The capture reports all 12 documents read in full.

**difficulty: easy.** This is local suitability for the Medium target.
- The lever is stronger than aq-00949 q04's: the exact numerator is printed nowhere, while "$3.9 billion in R&D and SG&A" covers exactly the asked window in the document the solver lands on first.
- Against that, twelve-month builds are routine for the low model (trial-02 q04 was Too easy), and aq-00998 q05 reached only Easy.
- **Tier odds:** Too easy ~30%, Easy ~43%, Medium ~12%, High ~3%, Low 0/5 followed by Medium 4–5/5 (an outcome we have not seen) ~10%, Too hard ≤2%.
- Attempts tend to share one path, so the $3.9B pull will mostly act as all-or-nothing at Low.
- Earlier local reviews underestimated four platform results, so treat these numbers loosely.
- This is unchanged from rev 0, because the question and documents are identical.

**verdict: ready.** This covers local correctness and fairness only. The gate's "target-suitable difficulty" for Medium is not supported by this review. I found no fix that raises difficulty without a hint, so whether to measure at Medium or retarget is your call.

**findings:**
1. **Rev 0 finding 1 is resolved (reasoning-number check).**
   - The diff of the two snapshots shows only Step 10 split into Steps 10 and 11, and the D11 L17 evidence line removed. Question, answer, components and corpus are byte-identical.
   - Steps 1–5: every operand is printed in the cited document, including "December 31, 2025" at Doc 7 L241. Each result follows "=".
   - Steps 6–9 and 11 use derived operands, but each names every document they came from. That matches the one observed acceptance (aq-00949 q05 Step 3).
   - Step 10 uses printed values only (12, June 30, 2026, 19,453).
   - The closing paragraph's 12 and 3.9 are printed in Docs 7–9, and it restates no result.
   - Each step holds one "=", with no parenthesised expressions. The form's behaviour here is still inferred from a few observations, so it remains unknown.
2. **Pipe-free quotes are still a platform risk (blocking check, unknown locally).** 7 of the 11 quotes match only after the pipes are removed (L62/63 in all three releases, and D11 L220). The L220 quote spans an empty cell, which makes it the riskiest. Use Save passage on these rows before the full checks; any mismatch means a new revision and new checks.
3. **The advisory risk is reduced.** The decoy quote is gone. The title quotes remain but establish each release's period. "Derive the rest" may re-propose the $3.9B sentence from the reasoning, so decline it by hand.
4. **Removal residuals:** the Doc 8 coincidence and recall of the 2025 line items for Doc 7. Both are low risk. Disclose them; a precision change won't help.
5. **Platform-only checks are unknown:** Restricted names, Original question (the frame differs from aq-00998 q05 and trial-02 q04), and "Answer matches a stated figure" (the $3.9B is the numerator, not the asked ratio). Origin is claude, so expect the export WARN; the self-authorship tick is your decision.
6. **Records match.** The report recomputes f1d2a9bc… from the current files, and it equals the snapshot and all four rev 1 records. There is no platform record (the capture shows 0 runs; slots Hard 0/2, Medium 0/3, Easy 0/1), so status must not move to ready.
7. **Q-checks and set.** Q1–Q12 and Q14 pass locally; the question is 29 words with one ask and passes rule 10. q01 (Microchip inventory, D04/D06) shares no path or giveaway with q02.

Files:
- D:\Dev\Docket\tasks\aq-01321\questions\q02.md
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\results\
- D:\Dev\Docket\tasks\aq-01321\runs\sketch-round1\returns.md

I changed no files.
