# q01 rev 2 independent review (fresh question-review subagent, 2026-10-08)

Verbatim hand-back (harness indentation removed).

q01 (rev 2; tested_sha256: 2091a4a4c23369f4674fad9c8aa4eb96ab436584b59913983f7050f693aad822)

The headline is a platform result nobody logged. The task folder holds a saved difficulty-check page: `D:\Agents\Docket\tasks\aq-01650\verdicts\AQ-01650_difficulty_2026-10-08_1000.txt`. It ran on a slightly stronger version of this question's wording and came back "Answer not supported". It changes the verdict.

gold_verified: yes. I recomputed the gold with a Decimal script.
- Japan: (11,658×14.719 + 12,130×13.480) / 23,788 = 14.087208, which is 56.348832% of 25 questions.
- China: 1.414 / 3 = 47.133333%.
- Difference: 9.215498, which is 9.2.
- Moving each printed input to the ends of its rounding range gives 9.197 to 9.234. Using the distribution's mean (1.4142) gives 9.2088. All of these round to 9.2.
- Inputs are verbatim in D01 L69, L208, L365 and L397, and in D03 L102, L106 and L108.
- The Table 5 values are observed means for all 23,788 non-students:
  - L196 says Ȳ "denote the sample means".
  - Literacy is not among the missing items listed at L208.
  - L251 uses knowledge as a predictor in the imputation, so the score itself is not imputed.
- The rev 2 descriptions are accurate:
  - D01 L11 and L61: the survey was "conducted by the Central Council for Financial Services Information (Bank of Japan)".
  - D03 L90: CHFS "of 2015 and 2017".
  - D02 L164: the CHFS "rounds" include 2015.
  - Japan's share is higher than China's, as the question assumes.

outcome: A: match; B: match. Each ran fresh on its own packet, answered with high confidence, and named and rejected both 13.7 and 9.3. Their context held only unrelated git-status file names, so both count as uncontaminated. That gives two valid matches.

closed-book: misses. It answered "about 30" from recall: Japan's published 55.6% plus a guess for China. The platform's own closed-book on the stronger wording also missed (13.1).

necessity:
- Doc 5 (D01) alone has the 2016 survey, its 25 questions, the 23,788 non-students and Table 5's means and counts. D04 and D05 are Osaka University's Preference Parameters Study (0.62 / 0.6185).
- Doc 2 (D03) alone has a 2015 CHFS literacy level. D02 prints no mean; D06 covers 2017/2019 with an index (0.0436).
- I re-hashed both removal-probe packets: each is byte-identical to the rev 2 corpus minus one document.
  - Without Doc 5: "cannot be determined"; forced guess 8.5 (p 0.35, from the recalled 55.6%).
  - Without Doc 2: "cannot be determined"; forced guess 26.3 (p 0.02).
- Hitting 9.2 without Doc 5 would need a Japanese share between 56.28% and 56.38%. No smaller valid document set exists.

shortcut: clear. The auditor's route matches mine. No passage states either share, the pooled mean or any cross-survey comparison, and "56.3" and "47.1" appear nowhere in the bundle.

source_assessment: source_gaps is [] and its hash 4f53cda1… matches. The corpus hashes equal the snapshot, and intake shows all seven documents match the capture. Some material is missing from the originals themselves (D01's S1/S2 tables, D03's Supplementary Table 1). It is missing on the platform as well, so it adds no input, no competing figure and no change to necessity.

difficulty: easy. It is not suitable for the Medium target as it stands.
- Chance the form's "One defensible answer" check blocks rev 2: about 30% (20–45%).
- If the form clears:

| Outcome | Estimate |
|---|---|
| Answer not supported | ~50% |
| Easy | ~22% |
| Too easy | ~12% |
| Between levels | ~8% |
| Medium | ~5% |
| Hard | ~2% |

- Overall chance of a usable Medium or Hard result: about 5%.

verdict: revise

failure_modes:
- FM1 (Part vs total / Picks the wrong entity or section) is real. Table 2's "Financial literacy|15,228|15.2|6.6" gives 15.2/25 = 60.8%, minus 47.133 = 13.667, which is 13.7. The platform has now measured it: rev 0's form check 2 of 2, and on the stronger wording low model 2 of 5 and high model 3 of 3. Every quote is verbatim, the claims are true, and "all" in the question does not rule it out.
- FM2 (Figure that must be computed / Calculation slip) is true and not ruled out by the wording. An unweighted average of the two means is 14.0995, which is 56.398% and gives 9.265, or 9.3. However, none of the 8 platform attempts or any local run produced it, so withdrawing it is optional.
- The labels are the best fit and neither repeats. Both documents are correctly ticked as Answer component.

findings:
1. **Critical: an unlogged platform run.** The saved page shows:
   - "Run 1 · Answer not supported · Result the gate uses … Version 1923ac (current) · Low 3/5 · Medium — · High —" at 09:39 on 2026-10-08, with "7 of 8 runs left".
   - The tested wording was rev 1 plus ", including those with missing background information,". That is exactly the fallback rung Lever checks still offers as "likely Easy".
   - "In the final check, the high model was given every document and still did not reach your answer."
   - All three every-document attempts answered 13.7 (file L1125, L1446, L1677), reasoning "we don't have the mean for all 23,788".
   - None of the high model's attempts mentions Table 5, 14.719 or "decomposition". The low model's three correct attempts found Table 5 by themselves.
   - The run is missing from q01's Feedback log, from Lever checks ("No quick test or difficulty run yet"), from session.md ("8 difficulty runs") and from both earlier reviews.
   - Consequence: the failure is that the high model never reads Table 5's unlabelled header-cell values as the 23,788 means. The population wording is not the problem. Rev 2 changes only the survey names, and its "all" is weaker than the wording that was measured.
   - Required:
     - Log the page verbatim as a different version (it is not bound to rev 2).
     - Correct Lever checks, the run count and the fallback plan.
     - Do not spend a difficulty run on rev 2.
   - A pointer to the gender means would let the high model through, but the low model already found them 3 of 5 times unaided, so the result would be Easy or Too easy, and the Easy slot is full. If no wording avoids that, drop this question family for the Medium target.
2. **Gate Q4 holds in form but fails in practice.** Every printed figure the wording fits fails a stated condition:
   - 15.2: N is 15,228, not all 23,788.
   - Table 5's men-only and women-only means: each covers one sex.
   - 0.62 / 0.6185: wrong organiser, title and year.
   - Table 8/9 means: behaviour and attitude scores, not questions answered correctly.
   - 10.77%: a share of households, not of questions.
   - 0.0436: wrong wave and measure.

   Even so, finding 1 shows that stating the condition does not stop the high model falling back to the printed decoy when it cannot find the gold's input. On the block risk: rev 0 was blocked with both solvers at 13.7, the stronger wording cleared the form (its difficulty run executed), and rev 2 sits in between.
3. **Rev 2's new survey descriptions are clean.**
   - The longest run of words shared with any document is 7 ("the central council for financial services information"), and it is a proper name.
   - Against the other 80 workspace questions, the highest similarity ratio is 0.248 and the longest shared run is 4 words.
   - No new reading, false premise or giveaway. At 52 words it is over the guide's 20–45 aim but under the 60-word warning.
   - The "Narrow the description" advisories may persist, because L11 and L61 both name the survey. They are warnings, not blocks.
4. **Number rule and quotes pass.** In every step that cites a document, each number is in that document or comes straight after "=". Steps 4, 5 and 8 use derived operands, a pattern the form has accepted before but not confirmed here. All 7 evidence quotes and all failure-mode quotes appear verbatim in the docs/ originals. Step 9's decoy note may again make "Derive the rest" propose the Table 2 row; it needs unticking.
5. **Stale notes.** `notes/handover-q01.md` is still rev 1 (fingerprint 4f003703…). session.md's run count and quicktest-batch.md's odds are also stale.
6. **Optional:** evidence row 7 (the 10.77% sentence) supports only the 3-question denominator, so the form may flag it as "does not seem to support that component".
7. **For memory:** a condition stated in the question can clear the form check and still end in "Answer not supported" when the gold's input sits in a cell the high model never consults. Four local matches and two reviews (which put Answer not supported at 5–7%) missed this.

Files:
- `D:\Agents\Docket\tasks\aq-01650\questions\q01.md`
- `D:\Agents\Docket\tasks\aq-01650\verdicts\AQ-01650_difficulty_2026-10-08_1000.txt`
- `D:\Agents\Docket\tasks\aq-01650\runs\q01-r2-v2-2091a4a4c23369f4674fad9c8aa4eb96ab436584b59913983f7050f693aad822\results\returns.md`
- `D:\Agents\Docket\tasks\aq-01650\runs\q01-r0-probe-m5\results\probe-returns.md`
- `D:\Agents\Docket\tasks\aq-01650\notes\handover-q01.md`

## Caller actions (2026-10-08)

- Finding 1 applied: the page is logged verbatim in q01's Feedback log and as a Blind solve platform record bound to no local revision (rev: none, tested_sha256: unknown); I verified the review's claims against the page (high-model section: 0 mentions of 14.719, 13.480, Table 5 or decomposition; low-model section: 22 mentions of 14.719).
- Decision: q01 dropped for the Medium target (status dropped). No wording found gives Low 0/5 with a gold the high model reaches: a pointer to the sex-specific means helps both models (the low model already reached 9.2 in 3 of 5 without it), and without one the high model ends at 15.2.
- Session, run count, quick-test batch and memory updated; the hand-over is withdrawn rather than regenerated.
