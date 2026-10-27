# q01 rev 0 narrow confirmation review (fresh question-review subagent, 2026-10-08)

Scope given: floor and fingerprint; truth of every Targeted failure mode sentence; hand-over against the question
file. Verbatim hand-back (harness indentation removed).

q01 (rev 0; tested_sha256: 8766f4397a13e8f501b617e8fd6b1e7c809ca1bc67f170b29c9df0dfa0a22af1)

**Verdict: ready (local).** All three checks pass. The question is locally supported and both failure modes are true. Keep the status at checked: there is no platform result, and Medium is still unmeasured. Nothing blocks submission. Three optional wording points are under findings.

gold_verified: yes. I recomputed it myself using exact decimal arithmetic:
- Japan: (11,658 × 14.719 + 12,130 × 13.480) / 23,788 = 14.087208, which is 56.34883% of 25 questions.
- China: 1.414 / 3 = 47.13333%.
- Difference: 9.21550, so 9.2.
- Using the Chinese distribution instead (0×11.67% + 1×46.01% + 2×31.55% + 3×10.77% = 1.4142) gives 9.2088, also 9.2.
- The counts add up: 25,000 − 1,212 = 23,788 = 11,658 + 12,130, and 37 + 614 + 4,204 + 3,705 = 8,560 = 23,788 − 15,228.

outcome: A: match; B: match. I did not re-judge these; two earlier reviews did. The raw returns.md at this fingerprint shows A at L8 and B at L63, both 9.2. The report lists both match records under 8766f439.

closed-book: misses. It answered "about 30.0" (returns.md L54).

necessity: taken from the earlier reviews and probes; I did not re-probe.
- D01 (Doc 5) is the only source for the 2016 Japanese survey, the 23,788 non-students and Table 5's means.
- D03 (Doc 2) is the only source for the 2015 Chinese survey's 1.414.
- Both removal probes answered "cannot be determined".

shortcut: clear, taken from the audit. My grep supports it: D01 prints no overall literacy mean for the 23,788 non-students.
- The only overall literacy mean is Table 2's 15.2 for the 15,228 complete cases (L216).
- Table 5 gives only the means for men and women (L365).
- Tables 8 and 9 print behaviour means (15.343 / 15.580) and attitude means (9.410 / 9.947), not literacy.
- L631 says "may have a lower mean" but gives no figure.

source_assessment: the report shows no source gaps (gap hash 4f53cda1...). Supplements the papers cite are not in the bundle (Doc 5's S1/S2 tables, Doc 2's Supplementary Table 1). Neither the gold nor the failure modes use them, and the earlier review assessed their impact. The warning that the bundle is complete as captured, not that the articles are complete, still stands.

difficulty: medium (marginal), as local suitability only, not a measured tier.
- For Medium: the gold is printed nowhere. It needs Table 5's means weighted by group size and both tests put on a share basis (25 vs 3 questions). The 15.2 decoy is the paper's only overall literacy mean, and weighting the two sexes equally changes the first decimal.
- Against: the decoy's N (15,228) and the "complete cases" title sit right beside it, and weighting by group size is routine. Easy is at least as likely as Medium.

verdict: ready (local).

failure_modes:
- **FM1 (Part vs total / Picks the wrong entity or section): the trap is real.** My recomputation: 15.2 / 25 = 60.8%, and 60.8 − 47.1333 = 13.667, so 13.7. Every sentence checks out:
  - Both quotes from D01 L208 are exact.
  - The Table 2 title (L212) and row (L216: 15,228 | 15.2 | 6.6) sit directly after L208.
  - "Only overall financial literacy mean in the paper" holds.
  - 8,560 adds up.
  - "Use all 23,788 non-students (11,658 men and 12,130 women) and impute the missing items" is true:
    - Tables 3, 6 and 7: L293, L444, L488.
    - Table 4: L340, where the two sex models (11,658 + 12,130) together cover everyone.
    - Tables 5, 8 and 9: L397, L546, L592.
    - Every table lists 20 imputations, and L251 describes the imputation.
  - The old "all report N 23,788" claim is gone. It survives only in the review record (q01.md L121), not in the mode or the hand-over.
  - "Asked measure's own label" is true. It is the same 25-question score for a smaller group, not a look-alike label.
  - 288 words. Both labels are the best fit: the solver's first wrong step is taking a different table that covers a narrower group (form value wrong_entity_or_scope). The wording does not rule the trap out, because the complete cases are also non-students.
- **FM2 (Figure that must be computed / Calculation slip): the trap is real.** My recomputation: (14.719 + 13.480) / 2 = 14.0995, which is 56.398%, giving 9.2647, so 9.3. Every claim checks out:
  - It now declares only this unweighted route. The 9.4 and 14.1 routes appear only in Lever checks (L96–97).
  - The two quotes (L365 and L397) are exact.
  - "Only place" and "no overall non-student mean printed anywhere" are true.
  - 56.349 − 47.133 = 9.216, and the 1.4142 route gives 9.209.
  - 207 words. Both labels fit, and no trap is used twice.
- The Answer component role for both documents matches how each is used.

findings:
1. **Check 1 passes.** `check_questions --q q01` gives 0 FAIL and 1 WARN; the WARN is about origin and is explained. `report` recomputes the fingerprint as 8766f439..., with no mechanical failures and no source gaps.
2. **Check 2 passes.** Details are under failure_modes.
3. **Check 3 passes.** A script compared every hand-over field with the question file:
   - The question, 1 ask, answer, reasoning and component are identical.
   - All 7 evidence items match on Doc number, location note, quote and component, and every quote appears word for word in D01/D03.
   - Doc 5 and Doc 2 are both marked Answer component. The unticked Doc 1, 3, 4, 6 and 7 match the numbering in notes/intake.json.
   - The tags match.
   - Both modes' trap, cause and three boxes are identical, apart from line wrapping.
4. **Housekeeping, not blocking.** q01.md (03:56:26) was saved 23 seconds after the hand-over (03:56:03). Every form field still matches and the fingerprint has not changed, so the later edit touched only sections outside the form. Regenerate the hand-over when you change the status: its header still says "DRAFT: not locally checked".
5. **Optional, no re-test needed (the modes are outside the fingerprint):**
   - (a) FM1's "Why" box (q01.md L72–73) writes 56.349 − 47.133 "= 9.2". The literal result is 9.216, so show the rounding step the way FM2 does.
   - (b) FM1 L70–71, "means are the scores of all 23,788": they are averages of those scores. This is loose but not false.
   - (c) FM2 says "Kept unrounded" and then gives three-decimal figures. The unrounded difference is 9.2155. This is harmless.
6. **Carried forward:** run the form's free "One defensible answer" check before any difficulty run.

This is a local review only. It does not establish a platform pass or measured difficulty.

## Caller actions (2026-10-08)

- Optional 5(a) and 5(b) applied in FM1; 5(c) applied in FM2 ("Without rounding it first"). Status set to checked; hand-over regenerated after these edits.
