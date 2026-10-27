# q01 rev 1 independent review (fresh question-review subagent, 2026-10-08)

Verbatim hand-back (harness indentation removed).

q01 (rev 1; tested_sha256: 4f003703a5866803c8eb8c390fb0a3d6018bb6af42f0fda2e748f53199319b40)

Summary: the gold checks out and every local check passes, so the verdict is ready (local only). Two things must happen before the hand-over: correct the stale record lines in Lever checks, then regenerate the stale hand-over file. After that, paste rev 1 verbatim into the form's free check before any quick test or difficulty run. I put the chance that the form blocks it again at about 25%.

gold_verified: yes
- I recomputed with a Decimal script: (11,658 × 14.719 + 12,130 × 13.480) / 23,788 = 14.087208. That is 56.34883% of 25 questions.
- China side: 1.414 / 3 = 47.13333%. Difference 9.21550, which gives 9.2.
- With the distribution mean 1.4142 instead, the difference is 9.2088, still 9.2. Carrying the printed precision of every input through gives a range of 9.197 to 9.234, all 9.2.
- The literacy score is never missing: 37 + 614 + 4,204 + 3,705 = 8,560 = 23,788 − 15,228 exactly. So Table 5's means by sex cover all 23,788 non-students.
- Wrong routes, recomputed:

| Route | Value |
|---|---|
| Complete-case mean 15.2 | 13.667, gives 13.7 |
| Unweighted average of the sex means | 9.265, gives 9.3 |
| Complete-case group sizes as weights | 9.408 |
| Pooled mean rounded early to 14.1 | 9.267, gives 9.3 |
| Men only / women only | 11.7 / 6.8 |
| Osaka survey 0.62 / 0.6185 (Docs 3 and 4) | 14.9 / 14.7 |

- Premises are true: Japan's share is higher; the 2016 survey used 25 questions (D01 L61, L69); the 2015 China survey measured households on three questions (D03 L90, L106, L108).

outcome: A: match; B: match
- Both are fresh, uncontaminated and high confidence.
- Both named and rejected 13.7 (15,228 complete cases is not all 23,788) and 9.3 (the two sexes differ in size).
- All four rev 1 packets hold the rev 1 question verbatim, and the packet text is byte-identical to text/.

closed-book: misses
- Answer "about 27.0", low confidence, not equivalent to 9.2.
- Its context held only unrelated workspace file names, so it is not contaminated.

necessity:
- Doc 5 (D01) is the only document with Japan's 2016 survey: the 25-question test (L69), 23,788 non-students (L208), the means by sex (L365) and the group sizes (L397). Docs 3 and 4 have only the Osaka survey's 2010 three-question score.
  - Probe without Doc 5: "cannot be determined"; forced guess 8.5 (p 0.3) from the recalled 55.6%. Reaching 9.2 needs 56.28–56.38%.
- Doc 2 (D03) is the only document with a 2015 China survey figure, 1.414 (L102, L106, L108). Doc 1 has only a 2017/2019 index (0.0436); Doc 6 pools 2011–2019 and prints no level.
  - Probe without Doc 2: "cannot be determined"; forced guess 26.3 (p 0.01).
- I hashed both probe packets: each is byte-identical to the rev 1 corpus minus the left-out document, renumbered contiguously.
- No smaller valid set exists.

shortcut: clear
- The auditor's shortest route matches mine: L69, L208, L365 and L397 give 56.349%; Table 1 gives 47.133%; the difference is 9.2155.
- No passage or summary states either share, a pooled non-student mean or the difference.
- The overview's "15,228 complete cases" exposes nothing; if anything it feeds the decoy.

source_assessment: no recorded gaps
- source_gaps is [] with gap hash 4f53cda1…, matching snapshot.json. The intake shows 7 of 7 documents complete, 0 gap characters, all matching the capture.
- Material missing from the originals themselves cannot change the gold, the decoys, uniqueness or necessity, because the platform shows the same text:
  - Doc 5's S1/S2 tables would bear only on the "Big 3" measure, which "each survey's own literacy test" excludes.
  - Doc 2's Supplementary Table 1 is absent for every reader, so no competing 2015 figure is visible.

difficulty: medium (marginal) — local suitability only
- The gold is built; no overall non-student mean is printed anywhere.
- An answer-shaped figure with the same label (15.2) is the first literacy mean a solver finds, and only the population scope separates it from the gold.
- On rev 0 that decoy caught both form solvers (2 of 2). Rev 1's "all" points at the check, which partly ties the trap.
- My odds if the form check clears: Too easy ~10%, Easy ~35%, Medium ~27%, Between levels ~15%, Hard ~6%, Answer not supported ~7%. That makes a usable Medium or Hard result about 1 in 3 if it clears, about 1 in 4 overall.
- The Between-levels risk follows the aq-01431 rev 0 pattern: the low model takes the printed figure and the medium model follows the cue.

verdict: ready (local only; status stays checked; no platform evidence for rev 1)

failure_modes:
- FM1 (Part vs total / Picks the wrong entity or section) is real. Table 2 (L212–216) gives 15.2 / 25 = 60.8%, and 60.8 − 47.133 = 13.667, so 13.7.
  - The labels are the best fit: the form value wrong_entity_or_scope matches a population-scope error, with "Misapplies a rule or premise" a close second.
  - The wording does not rule it out on its own: "all" names the condition, but only Table 2's title and N show that 15.2 fails it.
  - I checked every claim:
    - Both quotes are contiguous and verbatim (L208).
    - 15.2 is the only overall mean in the paper.
    - 8,560 is correct.
    - The regressions and decomposition use 23,788 with imputation (L251, L293, L397).
    - Literacy is not among the missing items.
    - 9.216 is correct.
  - Caveat in finding 5.
- FM2 (Figure that must be computed / Calculation slip) is real: 14.0995, 56.398%, 9.265, so 9.3. No run produced it.
  - The labels fit and it does not repeat FM1's trap. The wording implies weighting but does not state it.
  - Claims true: Table 5 is the only source of literacy means for all non-students, no pooled mean is printed, and 9.209 with 1.4142 is correct.
- Roles: both documents are Answer component, which matches how each is used.

findings:
1. Q4, chance of another form block (the question; D01 L208 and L212–216).
   - Rev 1 states a condition, "all", and 15.2 fails it: N 15,228 under "Descriptive statistics for complete cases", against "remaining 23,788".
   - Every other printed figure the wording could loosely fit fails a stated condition: the means by sex fail "all", the Osaka 0.62 fails the survey name, Doc 1's 0.0436 fails "2015", and 10.77% fails "average share of questions". So updated Q4 holds in form.
   - Residual block risk is about 25% (range 15–35%), mostly from both form solvers taking 13.7, plus about 5% from both taking 9.3. Reasons:
     - 15.2 is still the only printed overall mean and the first one a solver hits.
     - The phrase the advisory matched to 15.2 on rev 0 is unchanged in rev 1.
     - On aq-01431 rev 1, one stated word ("single") did not stop both form solvers.
   - Local Opus solves cannot measure this risk.
   - Required: paste rev 1 verbatim into the form's free check before any quick test or difficulty run, and log the panel.
2. Q1–Q3 and Q5–Q12 pass.
   - 43 words, one ask, periods and survey names pinned, "percentage points" and one decimal stated.
   - No answer part or hint in the question; asks about the world, not the set.
   - Tags fit (join, scale normalisation, weighted aggregation).
   - No answer-shaped decoy or rulebook is needed for a single numeric answer.
3. Q14, number rule and quotes (Reasoning and Evidence).
   - Emulated pass: every number in a step citing a document is printed in it or follows "=". Steps 4–6 and 8 reuse earlier results, which the form has accepted before (aq-00949 q05).
   - All seven quotes are contiguous and verbatim in both text/ and the docs/ originals (Doc 5 L67, L206, L370, L402; Doc 2 L106, L108).
4. Stale records in q01.md Lever checks (outside the fingerprint; fix before hand-over, no re-test needed).
   - Line 96 says "Removal probes at this fingerprint" but reports rev 0's results (8.9 at p 0.07; 26.3 at p 0.02). Rev 1's results are 8.5 at p 0.3 and 26.3 at p 0.01, as the Blind solve section records (lines 117–118).
   - Line 100 cites closed-book "about 26 and about 30" and omits rev 1's 27.0.
5. FM1's closing sentence about the form result.
   - It states as fact that the earlier wording drew 13.7 from both form solvers. The Feedback log calls the link between that screenshot and the rev 0 wording "probable, not established".
   - It is very likely true. It also tells the platform reviewer that an earlier wording had two answers. Whether to qualify or drop it is your choice; it is not a correctness defect.
6. The hand-over file is stale (notes/handover-q01.md).
   - It still holds rev 0: the question without "all", revision 0, tested_sha256 8766f439…, and rev 0's FM1 boxes. Pasting it would resubmit the blocked wording.
   - Regenerate it with --handover after finding 4. Also update notes/quicktest-batch.md, which still has rev 0's wording.
7. Record check.
   - The report's current fingerprint and snapshot.json both read 4f003703…, revision 1. The floor shows 0 FAIL and 1 WARN (origin, already explained).
   - Platform-only checks are unknown: restricted names (list not captured), Original question / Not a duplicate, and the token window.

## Caller actions (2026-10-08)

- Finding 4 applied: the Necessity bullet now gives rev 1's probe results (8.5, p 0.3; 26.3, p 0.01) with rev 0's as history; the overview bullet lists all three closed-book misses (26, 30, 27.0).
- Finding 5: the FM1 sentence citing the rev 0 form result was removed from the box; the fact stays in Lever checks with its "probable" binding.
- Finding 6: hand-over regenerated after these edits; notes/quicktest-batch.md had already been updated to rev 1's wording before this review returned (its q01 entry carries "all").
