# q03 rev 0 final review verdict after the replacement audit (2026-10-06)

Same question-review context as review.md, resumed with the replacement audit. Return copied verbatim.

q03 (rev 0; tested_sha256: f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf)

**Binding re-checked.** Nothing has changed since my first report:
- `report` recomputes the same fingerprint, with no source gaps (gap hash 4f53cda1…) and no platform record. The floor shows 0 FAIL and 1 WARN (origin).
- The shortcut packet audit 2 used still matches the canonical corpus file for file, and its question.txt is the frozen question.
- q03.md holds two rev 0 audit records on this fingerprint; the latest says `verdict: clear`.
- results/review.md is my first report word for word.

**gold_verified: yes.** 9,688 + 214 = 9,902 (or 9,688 + 212 + 2); 1,846 + 5,695 = 7,541; 2,361 / 7,541 = 31.3088%, so 31.31%.

**outcome: A: match; B: match.** Both read line 1179. They are distinct fresh solvers and neither was contaminated.

**closed-book: misses.** It answered 28.49%, which is not equivalent to the gold.

**necessity:** Unchanged.
- D02 (9,688 + 214) and D05 (1,846 + 5,695) are each indispensable; no other document counts credit unions or banks.
- Memory routes give 28.47% or 31.28% without D02, and 31.33% or 11.95% without D05.
- No smaller set of documents works.

**shortcut: clear.**
- Audit 2's searches cover the shortcut routes: the totals 9,900, 9,902 and 7,541, every 4–5 digit number in D01–D06, other bank counts and duplicate inputs.
- My own check agrees. There is no whole-answer lookup and no single-source route. The overview prints only 9,688, 1,846 and 5,695.
- The one passage audit 2 never read, line 1179, gives an input (214), not the answer.
- Verified shortest route to the gold: D02 lines 231 + 1179 (or 233 + footnote 8), D05 line 191, then one ratio.

**source_assessment:** Unchanged. No gaps are registered. D05's missing footnote bodies (including footnote 6), D02's Appendix III/IV letters and the garbled D02 Figure 1 are part of the original text and identical on the platform. None of them affects premises, gold, exclusions, uniqueness, necessity or shortcut coverage.

**difficulty: medium (marginal).** Local suitability only.

**verdict: ready.** This is local only: status `checked`, platform pending. Hold q03 as the unsubmitted alternative (finding 4).

**findings:**

1. **(a) Does the "clear" record count?** Yes, as a shortcut check, and only as that.
   - Its verdict rests on search coverage I could verify, and my independent check reached the same result.
   - Its own answer, 31.28%, is not evidence for or against the gold. Uniqueness rests on the documents and on solvers A and B.
   - It does repeat the first auditor's reading ("the footnote gives no date"), now rated a "minor risk".
   - It does not meet the condition I set for taking a fairness question to the user: a reader who reads line 1179 and still finds 9,900 defensible. Neither q03 auditor reached 1179. Audit 2's search for "uninsured credit union" finds footnote 8 (line 239) but not line 1179, which says "lacked federal deposit insurance, and all but two were privately insured" without the word "uninsured".
   - So: no third audit and no wording change. Do tell the user about the pattern when handing over, as difficulty evidence for the single attempt, not as an open fairness question.

2. **(b) Fairness or difficulty?** My fairness judgment is unchanged.
   - Across q01 and q03, all 6 runs that read line 1179 used 9,902: q01 B, both q01 audits, q03 A, q03 B and the q03 D05-removal probe (that probe may have been primed by q02's packet text).
   - The 3 runs that took 9,900 had not read line 1179: the q01 D05-removal probe and both q03 audits.
   - The fourth run that missed line 1179, q01 A, still reached the gold through footnote 8.
   - So the split comes from not finding the sentence, not from reading it differently. Once the dating sentence is seen, no run prefers 9,900.
   - Line 1179 is quoted in the evidence, and reasoning step 1 dates the 214 to December 2002. The platform's one-defensible-answer check and its reviewer will have it in front of them.
   - All four blind solvers found the two uninsured credit unions. That is the role closest to the platform's attempts. All three misses came from auditor or probe roles, so "3 of 10" overstates the miss rate for runs that just answer the question.
   - Remaining risk, not blocking: if several low-model attempts agree on 31.28%, the difficulty check may add its "may be too vague" warning. That warning appeared on aq-00745 q01, which still passed. A reviewer who reads only footnote 8 could raise the same point; the quoted line 1179 answers it.

3. **Tier estimate and Too hard risk.** The repeat confirms that the trap catches strong readers who discount footnote 8. Because that failure looks consistent, platform attempts could fail together, as in aq-00745 q08, where medium and high went 9 of 10 into one wrong anchor.
   - Updated estimate, not calibrated: Too easy under 5%, Easy about 40%, Medium about 35%, High about 10–15%, Too hard about 5–10%.
   - Too hard needs Low, Medium and High all at 0/5. The 4-of-4 blind-solver record argues against the high model missing every attempt.
   - Easy is still the largest single risk.
   - q03's arithmetic-only wrong routes (31.30% from truncating, or from rounding the fraction to three decimals) make every tier slightly harder, Too hard included. The effect is too small to matter for the choice.

4. **(c) Which single submission: q01.**
   - Both share the deciding fact, decoys, documents and removal risks, so their tier odds are essentially the same. The percentage adds arithmetic, not evidence.
   - In q01 the two uninsured credit unions matter at the answer's natural integer precision. q03 needs a stated two decimals to make them matter (both routes give 31.3% at one decimal). A reviewer could read that as engineered precision, and q03 adds wrong routes unrelated to the evidence ("hard to reason through, not hard to parse").
   - q01 is further along: its replacement audit is clear and reached the gold via line 1179, it has two ready reviews including a second careful check, and its hand-over block has been verified. q03's clear audit gave a decoy answer and confirms only the absence of shortcuts.
   - q01 is shorter (23 words against 35) and plainer.
   - The only reason to choose q03 is a wish for Trial 2 q01's percentage shape. q03 lacks that question's printed, answer-shaped decoy, so the shape alone buys nothing measured. Submit one, never both.

5. **Records.**
   - In q03's Review record, describe audit 2 as: clear for shortcuts; its own answer is the decoy because it did not read line 1179; not confirming evidence.
   - Keep both audit records.
   - Keep the earlier note that the q03 removal probes ran in packets prepared for q02.

6. **Still open, none blocking.**
   - The end-2002 versus September 2005 comparison may look contrived.
   - Keep the dropped q02 off the form.
   - Origin "claude" is accurate, but the export tool accepts only "user".
   - Restricted names, originality, the token window and the AI-use terms cannot be checked locally.
   - The platform result (gate Q13) is pending. Status stays `checked` until a pass at Medium or higher is recorded on this fingerprint.
