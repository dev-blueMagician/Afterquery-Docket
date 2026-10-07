# q05 rev 0 independent review (question-review, fresh context), completed 2026-10-06

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns and the platform context only.
Pasted unabridged.

q05 (rev 0; tested_sha256: 5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72)

**gold_verified: yes.** I recalculated by script from text/. D08 to D12 and their originals match the snapshot hashes.
- ROCE earnings for the twelve months: 13,581 (D10 l.405) − 6,469 + 15,135 (D12 l.389) = 22,247. Two cross-checks agree:
  - adding the quarters: 3,942 (D09 l.372) + 3,170 + 2,603 (D11 l.379) + 12,532
  - adding the components: 20,591 + 374 + 1,282
- Capital employed:
  - June 30, 2025 = 29,467 + 146,417 + 841 = 176,725 (D08 l.358-360)
  - June 30, 2026 = 37,075 + 189,883 + 5,675 = 232,633 (D12 l.352-354)
  - average 204,679
- Result: 22,247 / 204,679 = 10.8692%, so 10.9%. The answer only flips if earnings move by 39 or capital by 362.
- Consistency: all ten printed averages from 1Q25 to 2Q26 reproduce to within 0.5. Every figure is in $ millions at one precision, and no release restates the June 2025 balances.

**Your point 1 (method): exactly one answer.**
- The D10 l.412 footnote fixes the start and end points.
- D10's FY2025 average of 205,316 equals the two-point December 2024 / December 2025 average exactly. Neither alternative matches it:
  - five-point 2025 average: 200,852
  - mean of the 2025 quarterly averages: 199,737
- D10 l.406 shows the year column is not annualized.
- So the five-point (10.0%), quarterly-average (9.8%) and mean-of-quarterly-ROCE (9.7%) readings are ruled out by the method the question names, not just less likely.

**outcome:** A: match; B: match. Both worked only from their packets (question.txt is identical to the frozen text) and are uncontaminated. Both gave supported paths and rejected the alternatives using the footnote. Two fresh matches validate the gold.

**closed-book: misses.** It answered "unknown, roughly 7–10%" with low confidence. 10.9% is outside that range, and the 2026 inputs come after its knowledge.

**necessity:**
- **D12: indispensable.** It is the only source of 2026 ROCE earnings and the June 30, 2026 balance sheet.
- **D08: not necessary (your point 2).** Without it, 2 × 177,212 (D12 l.392, 6M 2025 average) − 177,698 (D10 l.370-372, December 31, 2024 comparative) = 176,726, or 176,725–176,727 allowing for rounding. That still gives 10.869%, so 10.9%. D09 also works (2 × 206,935 − 237,144). The Lever checks say any back-solve "still needs another release"; that misses this route. D08 should be quoted but unlisted (or its route dropped), not listed as necessary.
- **D10: replaceable at one decimal place.** Nobody flagged this route:
  - D11 l.60 prints 4Q 2025 ROCE as 5.4%.
  - 4Q average capital = (237,144 from D09 + 232,934 from D11) / 2 = 235,039.
  - So 4Q earnings fall between 3,144 and 3,202 for any ROCE from 5.35% to 5.45%.
  - 3,942 (D09) + that + 2,603 (D11) + 12,532 (D12), divided by 204,679, gives 10.856–10.885%. That is 10.9% across the whole range.
  - D11's own table prints the ×4 annualization and two-point average (2,603 × 4 = 10,412; / 233,867 = 4.5%), so nothing is assumed.
  - The q04 review counted a rebuild as a replacement only if it pinned the answer (its rebuild spread 7.9–8.1 and didn't). This one does pin it.
- **Smallest valid set:** {D10, D12}. A set without D10 also works: {D09, D11, D12}.
  - Only D12 is strictly indispensable.
  - Every route needs at least two releases, so guide rule 2 and the platform's "Needs two or more documents" check pass.
  - WORKFLOW l.98 and gate Q2 ("two indispensable sources") are not met as written.
  - At two decimals the D11 rebuild spans 10.86–10.88, while every D10 + D12 variant gives 10.87.

**shortcut: clear.**
- "10.9" appears nowhere in text/.
- No twelve-month ROCE is printed; the only trailing-12-month basis is for CFFO (D11 l.368, D12 l.376).
- The overview gives only 21% (2Q26), 4.5% (1Q26) and 8.3% (1Q25).
- D07's "double-digit ROCE" is a target, not a figure for this period.
- The shortest verified route is D10 + D12 with the back-solve: an ordinary two-document calculation. The auditor's "D10 needed in every route" is incomplete, but that affects necessity, not shortcut.

**source_assessment: not applicable.** source_gaps is [] (4f53cda1… is the sha256 of "[]"). D08 to D12 have no "characters not shown" markers, and the originals carry the same figures.

**difficulty: easy, marginal, with high too-easy risk.** This is local suitability only, not a tier.

Your point 3, routes the low model could get wrong:
- (a) Reusing D10's printed full-year average of 205,316, which the question's "full-year" wording points at: 10.8%.
- (b) Starting from a comparative column:
  - December 31, 2024: 10.8%
  - December 31, 2025 or the 6M 2026 average: 9.6%
  - 2Q 2026 average: 9.5%
- (c) Building the denominator from quarters:
  - mean of the quarterly averages: 9.8%
  - five quarter-ends: 10.0%
  - mean of the quarterly ROCEs: 9.7%
- (d) Taking a printed figure: 13.0% (1H26, next to "Annualized ROCE earnings") or the 21% headline.
- (e) Using reported earnings (10.1%) or leaving noncontrolling interest out of capital (11.0%).

Three wrong methods still land on 10.9%:
- pre-tax interest: 10.94%
- midpoint of the two six-month averages: 10.85%
- June 2025 and December 2025 as the two points: 10.86%

Working against misses:
- The question names the method, and the deciding footnote sits under every ROCE table.
- D08's balance sheet is labelled June 30, 2025.
- Both standard ways of building the twelve months give 22,247.

aq-00964 q01 and aq-00745 q01 passed because each left a same-label decoy open. This wording leaves none open, so misses would have to come from slips across about ten labelled cells. That profile was measured too easy on this bundle (q03 Low 5/5; q01, q02 and q04 failed the quick test). Two or more misses in five is possible through (a)–(c), but I judge it less likely than not.

**verdict: revise**

**findings:**
1. **Q2, documents field and Lever checks.**
   - Problem: D08 is listed but replaceable (D10 + D12, or D09), and D10 is replaceable at one decimal place (D09 + D11). The listing is inaccurate and the two-indispensable-source rule is unmet as written. The Necessity line's "D10 is needed in every route" and its back-solve claim are both false.
   - Required:
     - Fix D10's status: either re-pin so the D11 rebuild no longer decides the answer, then recheck every combination of stated figures; or record an explicit decision that discloses both alternative routes.
     - Remove D08 from the documents field and correct the Necessity line.
2. **Re-verification.** The documents field (and the precision, if changed) is part of the fingerprint. The change needs a new revision, prepare, two fresh blind solves, a closed-book solve, an audit and a review. No platform run exists for q05, so nothing measured is lost.
3. **Q14, platform-only, unknown.** The evidence quotes replace the originals' tabs with spaces ("Total debt $\t37,075 $\t40,758"). The floor accepts this; whether the platform's verbatim check does is unseen.
4. **Reasoning apostrophe.** The reasoning quotes "Total debt plus total stockholders' equity" with a straight apostrophe, but the documents print ’. Keep quoted phrases verbatim so Derive the rest picks them up.
5. **Q11, levers.** "Calculate across documents" and "Scatter the pieces" both work: no single passage holds the answer. No which-items decoy is needed. The three wrong methods that still give 10.9% weaken the method lever but are not a fairness defect.
6. **Other checks.**
   - Q1, Q3–Q10 and Q12 pass: premises are supported, the period is exact, there is one ask in 32 words, precision is stated, and there is no giveaway, hint, set reference or rulebook.
   - Q13 is pending (no platform record).
7. **Records.** The A, B, closed-book and audit lines carry rev 0 and the matching fingerprint, and the report shows no mechanical failures. The floor shows 0 FAIL and 1 WARN: origin is truthfully "claude", but the export tool only accepts "user". That authorship issue is outside this review.

Files: D:\Dev\Docket\tasks\aq-00998\questions\q05.md; D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\results\returns.md; D:\Dev\Docket\tasks\aq-00998\text\D08.txt through D12.txt.
