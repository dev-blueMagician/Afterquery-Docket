# q05 rev 1 independent review (question-review, fresh context), completed 2026-10-06

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns, the rev 0 review and the
platform context only. Pasted unabridged.

q05 is ready on local evidence. All three rev 0 findings are resolved; the gold recomputes to 10.87% by every route. Status should stay `checked` until the platform measures this exact content. Local suitability for Easy is marginal, with a high risk of a "too easy" result.

q05 (rev 1; tested_sha256: cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306)

**gold_verified: yes.** I recalculated by script from the passages, not from the author's sums.
- **ROCE earnings for the twelve months: 22,247 by five routes.**
  - 13,581 (D10 l.405) − 6,469 + 15,135 (D12 l.389).
  - Adding the four quarters: 3,942 + 3,170 + 2,603 + 12,532.
  - Adding the components: 20,591 + 374 + 1,282.
  - Full-year 2025 minus 1Q25 and 2Q25, plus 1Q26 and 2Q26.
  - Nine months minus six months, plus Q4 and the 2026 first half.
- **Capital employed at June 30, 2025:** 176,725 (D08 l.358-360). Working back from three printed averages gives 176,725 to 176,727 (2×177,212−177,698; 2×206,935−237,144; 2×178,243−179,761).
- **Capital employed at June 30, 2026:** 232,633 (D12 l.352-354). Working back from printed averages gives 232,633 to 232,635.
- **Result:** the average is 204,679 to 204,681, so ROCE is 10.86911% to 10.86925%. That rounds to 10.87% in all 24 combinations.
- **Method is pinned.**
  - The two-point average reproduces D10's 205,316 exactly, and D05's 180,232 (180,231.5).
  - The five-point average (200,852) and the mean of the quarterly averages (199,737) do not.
  - The year column is not annualized (D10 l.406).
- **Margin:** the answer flips only if earnings move by −8.6/+11.9 or average capital by +79/−109.

**outcome: A: match; B: match.**
- Both ran fresh in separate packets (solver-1, solver-2), and the packet question equals the frozen text.
- Both gave supported paths and rejected the same alternatives using the footnote.
- Neither is contaminated, so the two matches validate the gold.

**closed-book: misses.** It answered "about 9%" (range 6.5–10%) with low confidence. That is not equivalent to 10.87%.

**necessity:**
- **D12 is indispensable.** It is the only source of 2Q26 and first-half 2026 ROCE earnings (12,532 / 15,135) and the June 30, 2026 balances. No later release exists.
- **D10 is indispensable at two decimals.**
  - Q4 and full-year 2025 ROCE earnings (3,170 / 13,581) appear only in D10, checked by grep over D01–D12.
  - The same holds for Q4 noncontrolling interest (75), Q4 after-tax interest (325), Q4 pre-tax interest (361) and Q4 distributions to noncontrolling interests.
  - Replacement test: D11 repeats 4Q25 total earnings of 2,770 (l.25) and 4Q25 ROCE of 5.4% (l.60). With Q4 average capital of (237,144 + 232,934)/2 = 235,039, the 5.4% bounds Q4 ROCE earnings to 3,143.65–3,202.41. That gives 10.8563–10.8850%, which could be 10.86, 10.87 or 10.88.
  - Residual: guessing Q4's add-backs from 3Q25 (403) or 1Q26 (393) happens to give 10.87, but a three-quarter mean (419) gives 10.88. That is a guess, not a route.
- **D08, D09, D11, D05 and D06 are replaceable.**
  - D08: June 30, 2025 capital employed can be worked back from D12's first-half 2025 average and D10's December 31, 2024 comparative.
  - D09: the full-year-minus-half-year route does not need Q3.
  - D11: D12's first-half 2026 figures replace its Q1.
  - D05, D06: the December 2024 balances also appear in D10.
- **Smallest valid set: {D10, D12}.** This equals the documents field, so rev 0 finding 1 is resolved.

**shortcut: clear.**
- No passage prints a twelve-month ROCE; the only trailing-12-month figures are for CFFO (D11 l.368, D12 l.376).
- "10.87", "22,247", "204,679", "176,725", "176,726" and "232,633" do not appear anywhere in text/.
- The overview gives only 8.3% (1Q25), 4.5% (1Q26) and 21% (2Q26). D07's "double-digit ROCE" is a target.
- The auditor's shortest route (D10 + D12, working back the June 2025 figure) matches mine. Search finds the inputs, not the answer.

**source_assessment: not applicable.**
- source_gaps is [], and 4f53cda1… is the recomputed sha256 of "[]".
- No "not shown" markers appear in D01–D12.
- All 25 corpus hashes match the snapshot.
- The docs/ originals carry the same table rows.

**difficulty: easy (marginal, high too-easy risk).** This is local suitability only, not a tier.
- **Design:** no passage states the answer. It is built from about 10 labelled cells in two releases, using two standard constructions (rolling twelve months, two-point average), plus either working back a figure or a third lookup.
- **Wrong routes, all different from 10.87 at two decimals:**
  - Reusing D10's printed full-year average of 205,316, which the "full-year" wording invites: 10.84.
  - December 2024 and June 2026 as endpoints: 10.84.
  - Midpoint of D12's two printed six-month averages: 10.85.
  - June 2025 and December 2025 as endpoints: 10.86.
  - Leaving noncontrolling interest out of both earnings and capital: 10.86. Using the printed "Total debt plus total stockholders' equity" line as capital: 11.05.
  - Pre-tax interest: 10.94.
  - Reported earnings only: 10.06.
  - Five quarter-ends: 9.98. Mean of the quarterly averages: 9.78. Mean of the quarterly ROCEs: 9.73.
  - D12's six-month 2026 average, or December 2025 as the start: 9.56.
  - Printed 13.0% or 21.4%.
- **Against misses:**
  - The method footnote sits under every ROCE table.
  - The dated balance sheets sit directly above those tables.
  - Both standard ways of building the twelve months give 22,247.
  - Labelled cells plus a standard transformation were measured too easy on this bundle (q03 Low 5/5; q01, q02 and q04 failed the quick test).
- Unlike q01–q04, the answer is not a single cell, and the two-decimal precision turns near-miss methods into wrong answers. Whether that produces two or more low-model misses in five is unmeasured.

**verdict: ready.** This is local only: the caller keeps `checked`, and Q13 is pending.

**findings:**
1. **Rev 0 findings resolved.**
   - (1) Every route through D10 gives 10.87, and no route without D10 fixes the second decimal: D11's 5.4% leaves 10.86–10.88, and no other printed ratio narrows it.
   - (2) D10 and D12 are each indispensable; D08 and D09 are correctly unlisted.
   - (3) There is no "answered inconsistently" exposure. Each input has one stated value, comparatives are identical across editions with no restatement, and rounding when working back moves the result by at most 0.0001 percentage points.
2. **Q1–Q12 and rule 10 pass.**
   - 32 words, one ask, precision stated, exact period, no hint or set reference.
   - The tags reflect work actually done. The levers are active, and no which-items decoy is needed.
3. **Q14, platform-only, unknown.** The evidence quotes replace tabs with single spaces (D10 l.370-372, 394, 408; D12 l.341, 352-354, 378, 392), and the docs/ originals contain the same tabs. The local floor accepts this; whether the platform's verbatim check does is unseen.
4. **Reasoning, a possible form flag (advisory, unconfirmed).**
   - The second "Decoy check" holds two "=" results (10.84%, 9.56%). On aq-00949 q03 the form flagged the second result in a multi-result step.
   - If the form flags it here, split the step. Reasoning is part of the fingerprint (submission_sha256), so any edit needs a new revision, prepare and full re-check.
   - The form's reaction to steps citing two documents (Steps 2, 4, 6, 7) is also unseen.
5. **Lever checks, record accuracy (not part of the fingerprint).** The Necessity line should also note that D11 repeats 4Q25 total earnings of 2,770, plus the guessed add-backs residual. The conclusion does not change.
6. **Records.**
   - The A, B, closed-book and audit lines carry rev 1 and cfbb7e….
   - The report recomputes the same fingerprint from the current file, so it is current.
   - The report only reads the Blind solve section, so it does not list the audit line.
   - The floor shows 0 FAIL and 1 WARN: origin is truthfully "claude", but the export tool only accepts "user". That authorship issue is outside this review.
7. **Q13 and the set.** There is no platform record. q01–q04 are dropped, so there are no live sibling overlaps.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q05.md
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r1-v2-cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r1-v2-cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D10.txt, D11.txt and D12.txt (D08.txt and D09.txt for the replacement tests)
