# q01 rev 2 - final independent review (raw, verbatim)

- Date: 2026-10-06. Fresh question-review agent (claude-opus-5-5), given the frozen fields, corpus,
  raw returns and target, without the writer's conversation; asked for a thorough, adversarial final
  check before a single submission attempt. Copied verbatim from the task notification.
- tested_sha256: 4a2aae5ab7ba14e5789c823ef80800a3eb6e9e94d265593a9ae00f6d43581ac3

## Return

q01 (rev 2; tested_sha256: 4a2aae5ab7ba14e5789c823ef80800a3eb6e9e94d265593a9ae00f6d43581ac3)

**gold_verified: yes.** I recomputed the gold by script from the docs/ originals, using Decimal arithmetic and half-up rounding.
- **Old structure:** D09 Table 5 (text l.463-464) gives full-year Africa/Eurasia net sales of 1,172 (2025) and 1,095 (2024), and Asia Pacific 2,814 and 2,858.
- **Recast:** D10 (l.28, l.59) gives recast Asia Pacific of 3,038 and 3,074.
- **Calculation:** Russia and Belarus = 224 and 216. Moved operations = 948 and 879. Change = +69. 69 / 879 = 7.849829%, so **+7.85%**. The result sits 0.0048 points above the lower rounding boundary and 0.0052 below the upper one.
- **Other full-year routes agree.** The EMEA route, nine months (D08) plus Q4 (D09), and H1 + Q3 + Q4 all give 948 and 879.
- **Caveat:** the EMEA route is the same equation as the Africa/Eurasia route once the totals (15,769 / 15,618) and Latin America match. It checks the arithmetic, not the composition. The composition rests only on D11 l.85, which is explicit: all of skin health went from North America to EMEA, and only Russia and Belarus went to Asia Pacific.

**outcome: A: match; B: match.** The two solvers worked from separate packets with byte-identical question text (sha d45e807a…). Both went D11 → D09 → D10 and rejected +7.03% because of D11's exclusion. Their input-rounding remarks are about the true underlying value, not about a different route using printed figures.

**closed-book: misses.** It answered "unknown" with low confidence.

**necessity:**
- **D11** is the only statement of what moved and the only place Russia and Belarus are named. Every other hit is Ukraine boilerplate. D10 has no notes, and D12's footnotes (l.81/115/455) give no content. The unforced probe without D11 answered +7.03% (65%), with the gold as a 15% alternative.
- **D09** is the only source of full-year 2025 and Q4 2025 old-structure rows. D05 repeats only the 2024 column, and D11/D12 hold no full-year tables. Without it the inputs must be estimated (rev 1 probe: +50, or 5.69%).
- **D10** is the only source of full-year recast figures and the only source of any 2024 recast. Without it the probe gave +41 or +63 (4.66% or 7.17%). A constant-share estimate from D11/D12 gives 7.03%.
- No smaller valid set exists.

**shortcut: clear.** The shortest route is the auditor's. No passage prints 7.85%, or 224, 216, 948 or 879 as these quantities. The only hits are unrelated: 948 is 2023 net income in D03, 879 is dividends in D12, and 216 is a tax line in D05/D09. The overview summaries say nothing about the realignment.

**source_assessment:** No known gaps. The capture holds 12 of 12 documents in full, and the docs/ and text/ hashes equal the snapshot. The gap hash is sha256 of an empty list.

**difficulty: easy.** This is local suitability for the Medium target only, and it is weak (finding 5).

**verdict: revise**

**findings:**

1. **Q4, precision (ask 1).** Two decimals are defensible. The printed full-year rows give 7.85% on every full-year route. Only routes that mix in quarter sums differ:
   - 2025 rebuilt from quarters gives 947, or 7.74%.
   - 2024 Africa/Eurasia from quarters (827 + 269 = 1,096) gives 7.73% or 7.61%.
   
   "Full-year" plus the full-year figures printed in D05, D09 and D10 makes those solver errors. There is no second stated figure for any input, so the "answered inconsistently" pattern does not apply. The alternatives are worse:
   - **One decimal:** 7.8 sits beside a 7.9 double-rounding trap and the 7.7 quarter route.
   - **Whole percent:** all routes give 8%, but that shrinks the gap to the printed 7.0% and to removal estimates, invites a closed-book "about 8%" guess, and widens the target for sloppy work.
   
   Keep two decimals. The risk that a reviewer treats derived precision as a defect is low; aq-00998 q05 passed at three decimals on derived inputs.

2. **Q2, D11 document check (ask 2).** Risk is low to moderate. The two probes are single samples with different framing (forced dollar answer vs unforced percentage), so their rates can't be compared. The rev 1 route of inferring the split from operating margins is still open to the high model. The percentage form helps, because the printed 7.0% backs the whole-segment default. The platform's own rule counts a document as needed when it is "the only document naming an item you marked it as excluding", which fits D11 exactly. Before the run, check whether the form lets you mark that, and keep the 200-character note ready; any edit clears the note. Unknown: how split attempts are scored.

3. **Q8/Q9/Q12, wording (ask 3).** "Moved … into" is a fair paraphrase of "combined", and the description fits one thing given D11. The fiscal year is the calendar year, and the direction and line item are pinned. The question is 36 words. The "Answer matches a stated figure" advisory may fire, because D09 Table 7 (l.583) prints "Africa/Eurasia 7.0%" with the same label and period. It is advisory only, and the Decoy line answers it. A Coach may remark that the description signposts the carve-out; that breaks no rule.

4. **Form number check (ask 4).** My emulation is clean apart from four operands: 224 (Step 6), 948 and 879 (Step 8), and 69 and 879 (Step 9). None is printed in Doc 9 or 10, but each is an earlier "=" result. That pattern passed once (aq-00949 q05 Step 3). Step 9's "69 / 879 = 7.85% (to two decimal places)" follows the accepted shape. The Decoy line's 7.0% is printed in Doc 9, and "March 31, 2026" is printed in Doc 11. Risk is low.

5. **Difficulty (ask 5).** A Medium placement needs Low 0/5, meaning the default reading has to fail.
   - The question's own description sends every reader to D11 l.85, the only 2026 passage that names Africa/Eurasia. The exclusion sits in the defining parenthesis there, so the printed 7.0% only catches attempts that never read the definition. That is the tied profile (aq-00745 q01, Low 1/5), not the untied one (aq-00964 q01, aq-00745 q09).
   - The remaining step (Russia and Belarus = recast Asia Pacific minus original) is a method applied to a quantity no document reports, like aq-00998 q05 (Low 2-3/5). Here it is done twice.
   - Compared with rev 1, the printed decoy mostly turns would-be Too-easy outcomes into Easy ones. It does not make the low model fail systematically.
   - Estimate: Easy about 55%, Too easy about 20%, Medium or higher about 20%, Too hard under 5%. The platform's label for "Low 0/5 then Medium 4-5/5" is unknown.
   - A quick test is still unused (0 of 10, capture l.161). A "Too easy" there would settle the question; a survival is not a Medium placement.

6. **Q14, verbatim evidence (blocking).** The quotes at D09 l.463-464 and D10 l.28/59 exist only as pipe rows, and there is no prose substitute. The platform shows these rows without pipes. Settling the exact text through Save passage changes the evidence, and WORKFLOW §8 then requires a new revision with fresh, re-bound checks. Do this before the difficulty check, because rev 2's exact content cannot be the content submitted.

7. **Records.** The report tool recomputes the live fingerprint as 4a2aae5a…, matching the snapshot. Corpus hashes match. A, B, the closed-book solve, the audit and the D11 probe are all bound to this fingerprint. The rev 0 and rev 1 records belong to earlier wordings.

8. **Platform-only and authorship.** The question is origin: claude, but the form's checklist includes "I wrote this question myself" (capture l.212); that is the user's call. Restricted names, originality, the token window (the page shows 93,722 prompt tokens), Coach reaction and the target tier (Q13) are all unknown. I am not claiming any platform pass.

I advise against submitting this exact content. Its correctness and fairness hold up, but the evidence text has to change first, and Easy is the most likely tier against a Medium target with one attempt.
