# q03 rev 0 independent review (2026-10-06)

Fresh question-review agent; input: frozen snapshot, corpus, raw returns, removal probes, q01's
review, target. Return copied verbatim.

q03 (rev 0; tested_sha256: f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf)

**Binding.** `report` recomputes this fingerprint and lists no source gaps. All 13 corpus files in the solver-1, solver-2 and shortcut packets match the snapshot hashes. All four question.txt files equal the frozen question. Every record is rev 0 on this hash. The floor shows 0 FAIL and 1 WARN (origin). There is no platform record.

**gold_verified: yes.** I recomputed it with a Decimal script:
- Credit unions: 9,688 (D02 line 231) + 214 (D02 line 1179) = 9,902. The other route agrees: 9,688 + 212 (line 233) + 2 (footnote 8, line 239).
- Banks: 1,846 + 5,695 (D05 line 191) = 7,541.
- 2,361 / 7,541 = 31.30884%, which is 31.31% under both half-up and half-even rounding.
- The credit-union groups cover everything. Line 231 says federally chartered credit unions "must be federally insured", and line 1179 counts the 214 that "lacked federal deposit insurance".
- No document and no overview prints 9,902, 7,541, 2,361 or any comparison of credit unions with banks.

**outcome: A: match; B: match.**
- Both solvers read line 1179. Both ran in fresh packets and neither was contaminated.
- Both listed 31.28% only as a reading for "insured credit unions". That is a narrower group than the question asks about, so it does not make either solve ambiguous.

**closed-book: misses.** It answered 28.49% from a recalled 9,688 and about 7,540 banks. That is not equivalent to 31.31%; it sits beside the 28.47% decoy. No run without D02 recalled the 214 or the two uninsured credit unions.

**necessity:**
- **D02** is the only source of credit-union counts. D03 names NCUA only (lines 107, 111, 171). Without D02, memory routes give 28.47% (9,688) or 31.28% (9,900), and the probe's forced guess was 28.47% (p about 0.25).
- **D05** is the only bank count. Its own "about 1,900 national banks" (line 393) is in December 2004 context, so it leaves with D05 and is no substitute anyway. Without D05, a recalled 7,540 gives 31.33%, and the probe guessed 11.95%.
- No smaller set of documents works.

**shortcut: clear (my own check).**
- Shortest complete route: lines 231 + 1179 give 9,902, line 191 gives 7,541, then one ratio.
- Searching the question's dates finds the inputs, not the answer. The overview leads only to the 28.47% decoy.
- The recorded audit verdict, "ambiguous", is a claim about uniqueness, not a shortcut. Finding 1 refutes it.

**source_assessment:** No gaps are registered, and intake shows all 6 documents captured equal to their sources. The omissions below are part of the original text and appear identically on the platform.
- **D05 footnote bodies, including footnote 6 on line 191:**
  - Premises: "banks" is the word D05's body text uses.
  - Gold: both bank counts are printed in the body text.
  - Exclusions: none are claimed for banks.
  - Uniqueness: no reader can see a competing figure.
  - Necessity: D05 is still the only bank count.
  - Shortcut: there is no hidden total anyone could use.
- **D02 Appendix III/IV letters (lines 1261–1309, headers only):** no input, premise or exclusion comes from them, and they can show no competing count. None of the six dimensions is affected.
- **D02 Figure 1 (garbled):** its values add up to 212, matching line 233 and Table 3 (lines 467–469). No effect.

**difficulty: medium (marginal).** This is local suitability only. It uses the recommended Medium mechanism: a total that looks complete inside one document, ruled out by a footnote and appendix fact. Easy remains the larger risk (finding 4).

**verdict: revise.** Procedural only: no field or wording change is needed.

**findings:**

1. **Uniqueness (focus 1; D02 lines 233, 239, 243, 1179, 1207, Table 3).** 31.31% is the single defensible answer.
   - Line 1179 dates the two uninsured credit unions to December 2002.
   - They sit outside the 212. New Hampshire is not among the eight private-insurance states (line 243, line 1207, and Table 3, which totals 212 without it).
   - The "98 percent" and "about 2 percent" shares are rounded. They fit 9,902 (97.84% and 2.14%) as well as 9,900, so they cannot decide the total.
   - The scope note limits GAO's assessment, not which institutions count as credit unions.
   - The auditor read D02 lines 1180–1220 but not line 1179. That is an ordinary incomplete reading.
   - Required: one replacement fresh audit on the unchanged fingerprint, as for q01. Keep the original record. `check_questions.py` (lines 799–800) needs `verdict: clear`.
   - Do not change the wording. "In December 2002" would steer readers to the deciding sentences, and naming the uninsured credit unions would give the trap away. If the replacement still says ambiguous after reading line 1179, take it to the user.

2. **Trap and rounding safety (focus 2).** The percentage form keeps the trap but does not strengthen it.
   - The two uninsured credit unions move the answer by 0.0265 points: 31.31% against 31.28%. At one decimal both routes give 31.3%, so two decimals are required.
   - The deciding fact, where it sits and both decoys (9,900 and 9,688) are unchanged.
   - The extra division is ordinary arithmetic. The Coach's trial-01 note: "One lookup plus one operation is usually solved".
   - The new wrong routes are arithmetic or format slips, not evidence: 31.30% (the fraction rounded to 0.313, or truncated), 23.84% (credit-union base) and 131.31% (plain ratio).
   - There is no printed decoy shaped like the answer, which Trial 2's q01 had.
   - Rounding safety: the gold is 0.0038 above 31.305 and 0.0062 below 31.315. One credit union moves it 0.0133 points and one bank 0.0174 points:
     - 9,901 credit unions gives 31.30%; 9,903 gives 31.32%.
     - 7,540 banks gives 31.33%; 7,542 gives 31.29%.
     - So only the exact 9,902 / 7,541 pair gives 31.31%.
   - Each input has one exact stated figure. The rounded prose gives other answers: 31.09% from "98 percent", 40.56% from "about 2 percent" and 30.38% from "about 1,900".

3. **Lever record (Lever checks, not part of the fingerprint).** "State the rounding" is active only through early rounding (31.30%). The mechanism that decides the answer is the remainder inside D02, and the Lever checks should say so.

4. **Tier compared with q01 (focus 3).** For tier purposes this is the same candidate.
   - Opus readers kept the remainder in 6 of 8 runs on q01 and q03. That excludes the q03 D05-removal probe (see finding 6).
   - Footnote 8 sits six lines below the 212 sentence (line 239 vs 233). An Easy result needs only one low-model attempt in five to find it.
   - My estimate: Easy about 50%, Medium about 30–35%, High about 10%, and Too easy or Too hard each 10% or less.
   - Arithmetic slips may cost a few low-model attempts, but they cost the medium model too, so the net effect is small.
   - What a Low 0/5 followed by Medium 4–5/5 result means is not recorded in this workspace.
   - Local predictions have underestimated platform difficulty before (aq-00964 q01, aq-00745 q09, aq-00998 q05).
   - The tier odds give no reason to prefer q03. q01 is further along, with a clear replacement audit and two ready reviews.

5. **Document-check risks.**
   - The platform's high model could recall exactly 7,541 banks; I rate that low to moderate, as for q01.
   - The overview prints 1,846 and 5,695 (capture line 77). Whether the document check shows the overview when Doc 5 is left out is unknown, and q01 has the same exposure.

6. **Removal probes (`runs/q02-r0-probe-m3`, `runs/q02-r0-probe-k7`).**
   - Both q03 probes ran in packets prepared for q02, whose question.txt holds q02's wording ("credit unions without federal deposit insurance").
   - The corpus files match. That text can supply neither the bank count nor the 214, so the necessity results stand.
   - The D05-removal probe's use of 9,902 is not independent evidence about difficulty.
   - Record the deviation.

7. **Reviewer perception.**
   - A reviewer may find the end-2002 versus September 2005 comparison contrived, as with q01.
   - Asking for two decimals so that two of 9,902 credit unions matter could look engineered.
   - If low-model attempts agree on 31.28%, the platform may warn that the question "may be too vague". That is a warning only, and the reasoning cites line 1179.

8. **Form emulation.**
   - The question is 35 words with one ask and one component.
   - Every number in the reasoning is in its cited document or follows "=".
   - All six quotes are verbatim and unique in the capture (lines 619, 621, 627, 1567, 3021), and none sits in a pipe-table row.
   - The line 1179 label is now correct.

9. **Question set.** q01 and q03 share the same path, so submit only one. q04 uses the same document pair but different facts and gives nothing away. Make sure the dropped q02, whose wording hints at the remainder, is not on the form.

10. **Authorship and platform-only checks.**
    - Origin "claude" is accurate, but the export tool accepts only "user".
    - Restricted names, originality, the token window and the AI-use terms cannot be checked locally.
    - The platform result (gate Q13) is pending. Status stays below ready until a Medium-or-higher pass is recorded on this fingerprint.


# Final verdict after the replacement audit (same reviewer context, 2026-10-06), summary

Summary only; the full final return is copied verbatim in review-final.md:
verdict: ready (local only; status checked, platform pending; hold q03 as the unsubmitted alternative).
difficulty: medium (marginal).
(a) The clear record counts as a shortcut check only; its own 31.28% answer is not evidence for or
against the gold; neither q03 auditor reached line 1179, so this is not the case of a reader who reads
1179 and still finds 9,900 defensible; no third audit and no wording change.
(b) Fairness unchanged: all 6 runs that read line 1179 used 9,902; the 3 runs that took 9,900 had not
read it; all four blind solvers found the two uninsured credit unions.
Tier estimate (not calibrated): Too easy under 5%, Easy about 40%, Medium about 35%, High about 10-15%,
Too hard about 5-10%.
(c) Single submission: q01 (same tier odds; q01's remainder matters at integer precision, q03 needs a
stated two decimals; q01 further along and plainer). Submit one, never both.
