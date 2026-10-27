# q01 rev 0 independent review (question-review subagent, fresh context, 2026-10-08)

Verbatim hand-back (harness indentation removed).

q01 (rev 0; tested_sha256: 8766f4397a13e8f501b617e8fd6b1e7c809ca1bc67f170b29c9df0dfa0a22af1)

**Verdict: revise.** Only the Targeted failure modes text needs fixing. The tested fields can stay as they are and keep their checks. Expected tier: Easy is the most likely result, which this document set cannot use.

gold_verified: yes. I recomputed it with exact decimals from Doc 5 (D01 L69, L208, L365, L397) and Doc 2 (D03 L102, L106, L108).
- Japan: (11,658 × 14.719 + 12,130 × 13.480) / 23,788 = 335,106.502 / 23,788 = 14.08721. Divided by 25, that is 56.3488%.
- China: 1.414 / 3 = 47.1333%.
- Difference: 9.2155, which is 9.2 under both half-up and half-even rounding. Using the distribution's mean (1.4142) gives 9.2088, also 9.2.
- Rounding of the printed means (±0.0005) keeps the result between 9.197 and 9.234, so it stays 9.2.
- Rounding-order grid (each share rounded to 0–3 dp): every route that rounds both shares to 1–3 decimals gives 9.2. The only routes that differ are whole-percent shares (giving 9.0, 8.9, 9.3 or 9.4) and the mixed 56.35 − 47.1 = 9.25 (9.3 half-up). These are early-rounding errors, not a second stated figure.
- The counts all reconcile: 25,000 − 1,212 = 23,788 = 11,658 + 12,130. 37 + 614 + 4,204 + 3,705 = 8,560 = 23,788 − 15,228. 8,054 + 7,174 = 15,228.

Are the Table 5 means observed for all 23,788? Yes, by a tight inference, though the paper never says it in words:
- The missing-data list names only education, self-rating, income and assets, and those counts add up exactly to the 8,560 dropped.
- L251 imputes "missing variables" using "financial attitudes, behaviours, and knowledge" as predictors.
- In the decomposition, the group means of an outcome that is not imputed equal its observed means in every imputation. The printed difference of 1.240 against 1.239 is rounding.

Is the complete-case reading (13.7) defensible? Not under this wording.
- L208 calls the group left after excluding students "the remaining 23,788 respondents". The 15,228 is a further subset with complete data.
- Table 2 is titled "Descriptive statistics for complete cases", and its row shows N 15,228.
- Every analysis table uses N 23,788.
- 15.2 is rounded, so that route cannot even fix the first decimal (13.47–13.87).
- It is still a strong pull. It is the only overall mean printed, the question's own "non-student" wording leads to it, and the overview advertises "15,228 complete cases".

outcome: A: match; B: match. Both reached 9.2 by the weighted Table 5 route, and each named and refuted 13.7 and 9.3 with evidence. Neither saw anything beyond auto-attached file names, so neither is contaminated. The auditor and the sketch solver also reached 9.2. That gives two fresh, uncontaminated matches.

closed-book: misses. It answered "about 30.0". It recalled Japan's published overall rate (about 55.6%) and nothing for the CHFS. Its context held file names only, so it is a valid miss.

necessity: no smaller valid set exists.
- **Doc 5 (D01)** is the only source of the 2016 survey: the 25-question measure, the student exclusion and the Table 5 means and counts.
  - Without it, the only Japanese figures left are D04/D05's Osaka 2010 panel (0.6185 or 0.62, giving 14.7 or 14.9 from the wrong survey).
  - Probe solver-1 answered "cannot be determined"; its forced guess was 8.9 (p 0.07).
  - Landing on the gold needs a Japan share of 56.28–56.38%. Recall misses it: 55.6% gives 8.5 and 56% gives 8.9.
- **Doc 2 (D03)** is the only source of a 2015 CHFS literacy level (1.414).
  - D02 pools 2011–2019 and prints coefficients only. D06 covers 2017/2019 with a factor index (0.0436). D07 is a Saudi study.
  - Probe solver-2 answered "cannot be determined"; its forced guess was 26.3 (p 0.02).
- The probe packets were clean. Ids are renumbered contiguously, the removed original is gone from both text/ and docs/, and the manifests are neutral. The folder name "probe-m5" was visible to the probes but reveals nothing.

shortcut: clear. Shortest route: D01 L69 → L208 → L365 + L397 (weighting) → D03 L108 → subtraction. No passage states either share, the pooled mean or the difference. "Non-student" matches no text verbatim. The overview exposes only 15,228 and 10.77%. The route is simple once found, which is a difficulty risk, not a Guide violation.

source_assessment: prepare reported no gaps (gap hash 4f53cda1...). Intake shows all seven documents complete (gap_characters 0, matching the capture), so there is no exact gap label to map. Some material is cited by the papers but absent from both the bundle and the platform text: Doc 2's Supplementary Table 1, Doc 5's S1/S2, Doc 4's Tables 1–3 and 7–9, Doc 3's Appendix. Their effect on each dimension:
- Premises: survey names, the 25 and 3 items and both populations are stated in body text.
- Gold: uses only body Tables 1 and 5.
- Exclusions: the Big 3 subset is ruled out by "each survey's own literacy test" and has no values in the bundle.
- Uniqueness: Supplementary Table 1 may hold a regression-sample mean, but no solver can see it, so 1.414 remains the only 2015 figure.
- Necessity and shortcut: unaffected.

The corpus is complete as captured; this does not certify the articles themselves as complete.

difficulty: medium (marginal), as local suitability only.
- For Medium:
  - A printed decoy (15.2) carries the asked measure's label but covers a narrower, labelled scope.
  - The gold is printed nowhere and must be rebuilt from a decomposition table.
  - A second, independent weighting trap changes the first decimal.
  - This resembles measured families: aq-01278 q02 (hidden-scope figure, Medium) and aq-01431 q01 (printed figure, Low 0/5).
- Against Medium:
  - The facts that disarm the decoy (23,788 vs 15,228, "complete cases") sit in the very sentence the question's population term retrieves. That is a tied trap, the profile measured Easy or Too easy (aq-00745 q01, aq-01432 q01).
  - Weighting by group size is routine, so a Low 0/5 run could still end "Between levels".
- Tier odds: Too easy 15%, Easy 45%, Medium 22%, Between levels 10%, Hard/Too hard 3%, Answer not supported 5%.
- Separately, there is a 10–15% chance the form's free "One defensible answer" check blocks the question if both form solvers answer 13.7 or 9.3.

verdict: revise. The fix is to the Targeted failure modes text, which sits outside the fingerprint, so no re-testing is needed.

failure_modes:
- **FM1, Part vs total / Picks the wrong entity or section**
  - The trap is real: 15.2 / 25 = 60.8%, and 60.8 − 47.133 = 13.667, so 13.7. The label fits ("Misapplies a rule or premise" would also be tenable).
  - **False claim:** the box says the sample paragraph "ends 'Thus, ... 15,228 individuals. Table 2 shows the descriptive statistics by gender.'" L208 continues with two more sentences on occupation and education proportions.
  - **Overclaim:** Table 2 "sits right after the sentence about excluding students". It actually follows the whole paragraph.
  - "The literacy score itself is observed for everyone" is an inference stated as fact.
  - "Lacked a covariate" misdescribes the 614 who are missing the self-rating, which is Table 4's outcome, not a covariate.
  - The other claims are true: the 8,560, "only overall mean", and the Table 5 values.
- **FM2, Figure that must be computed / Calculation slip**
  - The trap is real. Recomputed:
    - unweighted 14.0995 → 56.398% → 9.265, so 9.3;
    - complete-case weights 14.1353 → 9.408, so 9.4;
    - rounding the mean to 14.1 → 9.267, so 9.3;
    - using 1.4142 → 9.209.
  - The label is acceptable and the wording does not rule the trap out.
  - "The only place that reports financial literacy for all non-student respondents" holds only for means. Tables 3 and 6–9 report literacy coefficients on N 23,788.
  - The 9.4 route was not produced by any run, so trimming it is optional.
- Neither trap repeats the other.

findings:
1. **Q15, FM1 boxes:** correct the "ends" and "right after" claims, state the observed-score point as an inference, then regenerate `notes/handover-q01.md`. No re-test needed.
2. **Q4 / form risk:** run the form's free "One defensible answer" check on the exact 42-word question before any difficulty run. If both form solvers agree on 13.7, tighten the population anchor by a half step, then re-prepare and re-run all checks.
3. **Q14 and the number rule:** an emulation passes. Every number is in its cited document or comes straight after "=". Derived operands appear in Steps 4–6 and 8, the shape that passed on aq-00949 q05 and aq-01320 q01. All seven quotes are verbatim and contiguous in both text/ and docs/. The three tags and both Answer-component roles fit.
4. **Q11:** "State the rounding" is active: 9.3 is separated from 9.2, and no second stated figure flips the gold. Both removal probes are recorded at this fingerprint.
5. **Platform-side checks:** the question is 42 words, one ask, and about the world rather than the documents. Two advisories may fire as false positives: "Answer matches a stated figure" (keying on 1.414) and "Each description fits one thing" (the complete cases). No platform result exists yet, so status should stay draft or checked, not ready.
6. **Set:** sketches i01 and i03 reuse Doc 2 Table 1. A sibling should not print the 2015 CHFS share.
7. **Records:** revision 0 and the fingerprint are verified. The snapshot sections equal the file, the corpus sha256 values I recomputed match, and the report shows no mechanical failures. The floor shows 0 FAIL and 1 WARN, which concerns the origin export, not the question.

Files:
- D:\Agents\Docket\tasks\aq-01650\questions\q01.md
- D:\Agents\Docket\tasks\aq-01650\notes\handover-q01.md
- D:\Agents\Docket\tasks\aq-01650\runs\q01-r0-v2-8766f4397a13e8f501b617e8fd6b1e7c809ca1bc67f170b29c9df0dfa0a22af1\snapshot.json
- D:\Agents\Docket\tasks\aq-01650\runs\q01-r0-v2-8766f4397a13e8f501b617e8fd6b1e7c809ca1bc67f170b29c9df0dfa0a22af1\results\returns.md
- D:\Agents\Docket\tasks\aq-01650\runs\q01-r0-probe-m5\results\probe-returns.md

## Caller actions (2026-10-08)

- Finding 1 applied: FM1 now says the paragraph "then states" the complete-case sentences (not "ends"), Table 2 "follows that paragraph", the missing items are "education, self-rating, income or asset information" (not "a covariate"), and the observed-score point is stated as an inference from the paper's list of missing items. FM2 now says "financial literacy means". The table row is described, not quoted with inserted pipes. Fields inside the fingerprint are unchanged (fingerprint re-verified by report).
- Finding 2 carried to the hand-over: run the form's free "One defensible answer" check (and a quick test) before any difficulty run.
