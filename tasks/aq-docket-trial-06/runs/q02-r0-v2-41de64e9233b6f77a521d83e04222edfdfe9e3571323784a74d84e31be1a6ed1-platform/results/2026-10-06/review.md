# q01 rev 0 independent review (2026-10-06)

Fresh question-review agent; input: frozen snapshot, corpus, raw returns, removal probes, target.
Return copied verbatim.

q01 (rev 0; tested_sha256: 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1)

**Binding checks**
- `report` recomputes the same fingerprint from the current file and corpus.
- The D02/D05 copies in the solver-1, solver-2 and shortcut packets have the same hashes as the snapshot.
- All four raw returns and the q01.md records are for rev 0 on this fingerprint.
- Floor: 0 FAIL, 1 WARN (origin). There is no platform record.

**gold_verified: yes.** I recomputed it with a script:
- Credit unions: 9,688 (D02 line 231) + 214 (line 1179) = 9,902. The other route gives the same total: 9,688 + 212 (line 233) + 2 (footnote 8, line 239) = 9,902.
- Banks: 1,846 + 5,695 (D05 line 191) = 7,541.
- Answer: 9,902 − 7,541 = 2,361.

The two credit-union groups cover everything without overlap. Line 231 says federally chartered credit unions "must be federally insured", and line 1179 counts the 214 that "lacked federal deposit insurance". The shares fit the text: 9,688 / 9,902 = 97.8%, matching "98 percent". No text file and no overview prints 9,902, 9,900, 7,541 or 2,361.

**outcome: A: match; B: match.**
- Solver A's main answer is the gold. Its alternative, 2,359, assumes footnote 8 has no date, but A never read line 1179, which places the 214 (and so the two uninsured) "As of December 2002". That is a gap in A's evidence, not a defensible reading.
- Solver B read line 1179 and answered with high confidence.
- Both ran from separate fresh packets with no contamination.

**closed-book: misses.** It answered 2,148 (recalled 9,688 minus "about 7,540"). That is not equivalent to the gold; it lands next to the 2,147 decoy. The 214 / two-uninsured remainder exists only in the bundle.

**necessity:**
- **D02** is the only source of credit-union counts. D03 mentions credit unions only in NCUA's name (lines 107, 111, 171). Without D02, memory gives 9,688 and so 2,147; the removal probe guessed 2,147 (p 0.35).
- **D05** is the only bank count and the only place "September 30, 2005" appears. Line 393's "about 1,900 national banks" is rounded, sits in December 2004 context and covers one charter type; it gives 8,002. Memory gives about 7,540 to 7,550, so 2,352 to 2,362; the probe guessed about 2,350 (p 0.01).
- To bypass D05, one attempt would need exactly 7,541 from memory and 9,902 from D02. I rate that risk low to moderate: the closed-book run also recalled 8,859 FDIC institutions, so approximate Q3 2005 counts are in memory.
- D01, D04 and D06 are off-topic. No smaller document set works.

**shortcut: clear (my own check).**
- Shortest route: add the two bank counts in D05 line 191, add D02 lines 231 and 1179, then subtract once.
- The question's exact "September 30, 2005" only finds an input, not the answer.
- The overview (capture lines 47 and 77) leads to the 2,147 decoy.
- The auditor found no shortcut. Its "ambiguous" verdict is a uniqueness claim, which I refute in finding 1.

**source_assessment:**
- prepare/report list no gaps (source_gaps [], gap hash 4f53cda1…).
- intake.json shows all six captured hashes equal to the source hashes, with 0 gap characters.
- Some content is missing from the original text format itself, identically in the platform text:
  - **D05 footnote bodies, including footnote 6 on line 191:**
    - Premises: the question uses D05's own word, "banks".
    - Gold: both counts are printed in the body text.
    - Exclusions: none claimed.
    - Uniqueness: no solver can see a competing definition.
    - Necessity: D05 is still the only bank count.
    - Shortcut: there is no hidden total to find.
  - **D02 Appendix III/IV letter pages (pages 59–71):** only the headers survive, and no input comes from them. None of the six dimensions is affected.
  - **D02 Figure 1:** the graphic is garbled, but its values sum to 212, matching line 233 and Table 3 (line 469).

**difficulty: medium (marginal).** This is local suitability only; nothing has been measured. See finding 3.

**verdict: revise. Procedural only:** the content is supported locally, and I am asking for no change to fields, wording or evidence.

**findings:**

1. **Uniqueness (focus 1; D02 lines 231, 233, 239, 1179, 1207).** 2,361 is the single defensible answer as written.
   - "Credit unions" with no qualifier means all of them. Line 231 itself calls 9,688 the federally insured 98 percent, so 2,147 is a misreading. The auditor supported it only by guessing that the writer used the headline figure.
   - 2,359 drops two credit unions that line 1179 places in the December 2002 count. Also, New Hampshire is not one of the eight private-insurance states (line 1207), so footnote 8's pair cannot already be inside the 212.
   - "At the end of 2002" is the ordinary reading of an as-of-December count. D02 has no competing 2002 date for any input, and no run questioned the period.
   - No wording change is needed. Changing to "in December 2002" would repeat the "As of December 2002" phrase used in lines 231, 233 and 1179, the deciding sentence. That steers search and attention to the remainder and raises the Easy-tier risk. It also does nothing about A's actual doubt, which was footnote 8's missing date. Wording that names the uninsured credit unions would give the trap away.

2. **Audit record (`results/shortcut-audit.md`; the `## Shortcut audit` section of q01.md).** The recorded verdict is "ambiguous". The gate, and `check_questions.py` (lines 799–800), require `verdict: clear` on this fingerprint, and this review cannot supply that.
   - The auditor searched widely, read line 1179, and preferred 2,361.
   - Required: one replacement fresh audit on the unchanged fingerprint, treated as a replacement for an ordinary error. Keep the original record.
   - If the new audit repeats this argument, take the disagreement to the user rather than re-running again.

3. **Difficulty (focus 2).** The trap sits inside D02 and the cross-document step is plain arithmetic, as the trial-01 lesson advises.
   - There are two coherent decoys:
     - 9,688 is the figure the overview shows.
     - 9,900 looks complete because the "98 percent" and "about 2 percent of all credit unions" sentences add to 100%.
   - The gold does not need line 1179: footnote 8, in the same Background block, is enough (that is how A got there).
   - "Too hard" would need every tier to drop the two uninsured credit unions. The Opus runs that read D02 (A, B, the auditor and the D05-removal probe) kept them in 3 of 4 runs, so this is the smaller risk.
   - The larger risk is an Easy result: one low-model attempt in five that adds footnote 8's "two uninsured" is enough. I put the chance of Low 0/5 near even.
   - An optional quick test (0 of 10 used) would screen for this, but it does not set a tier.

4. **Reviewer and document check (focus 3).**
   - The question is not trivia: it aggregates a total that is never printed, and the Guide allows "calculate across documents".
   - A difference between end-2002 credit unions and September 2005 banks has no real-world meaning, and the cross-document step is one subtraction. A reviewer could call it contrived or thin reasoning.
   - Wording cannot fix this, because D05 has no 2002 bank count and D02 has no 2005 credit-union count.
   - The document-check risk for D05 is as stated under necessity.

5. **Evidence label.** "Appendix I footnote 2" is wrong: the 214 sentence is Appendix I body text that follows the footnote marker. Footnote 2's actual text (line 1185) defines credit unions. The quote itself is verbatim. Evidence is part of the fingerprint, so fix the label only if a revision happens for another reason.

6. **Lever checks (not part of the fingerprint).** The Necessity line still says "removal probes pending". Add the sketch-round1 results and note that the probes' folder names revealed which document had been removed.

7. **Question set.** Sketch i02 reuses the same D02–D05 subtraction path; if it is promoted, vary the document pair or mechanism.

8. **Authorship and platform-only checks.**
   - Origin "claude" is accurate. The export tool accepts only "user", so report that rather than changing the origin.
   - Unknown locally: restricted names, originality/duplicate, token window, and the AI-use terms.
   - Status must stay below ready until the platform passes this fingerprint at Medium or above.

Files:
- D:\Dev\Docket\tasks\aq-docket-trial-06\questions\q01.md
- D:\Dev\Docket\tasks\aq-docket-trial-06\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q01-r0-v2-41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1\results\shortcut-audit.md


# Final verdict after the replacement audit (same reviewer context, 2026-10-06)

Return copied verbatim.

q01 (rev 0; tested_sha256: 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1)

The replacement audit came back clear and the binding is unchanged, so my final verdict for rev 0 is **ready** locally, at **medium (marginal)** difficulty. Nothing local still blocks it; the only thing between this and status ready is a platform pass on this fingerprint.

**Binding re-checked:**
- `report` recomputes the same fingerprint, so no tested field or source byte has changed. The only edit since my last review was to the Lever checks, which are not part of the fingerprint.
- The floor shows 0 FAIL and 1 WARN (origin).
- All three check packets hold only question.txt and the corpus files. All 13 files match the snapshot hashes and the question text matches, so the second auditor used an intact, unmodified packet.
- The saved review.md is my earlier report word for word. The q01.md record of audit 2 matches its raw return.

**gold_verified: yes.** Unchanged: 9,688 + 214 = 9,902; 1,846 + 5,695 = 7,541; 9,902 − 7,541 = 2,361.

**outcome: A: match; B: match.** Unchanged. A's 2,359 alternative depends on not having read D02 line 1179.

**closed-book: misses.** It answered 2,148, which sits on the 2,147 decoy.

**necessity:** D02 and D05 are both needed. The risk that the platform's high model recalls exactly 7,541 and so skips D05 stays low to moderate; it is now recorded in the Lever checks.

**shortcut: clear.** `shortcut-audit-2.md` (a fresh context, same intact packet) answered 2,361 with verdict clear:
- Its shortest path is the same as mine: D02 lines 231 + 1179 (or 233 plus footnote 8) give 9,902; D05 line 191 gives 7,541; then one subtraction.
- It searched dates, counts, insurance terms, candidate totals and bank-count wordings across all six documents.
- It rejected 2,359 using line 1179 and 2,147 because the question asks for all credit unions.
- This is the one replacement I asked for, for an ordinary error. The first "ambiguous" record stays in the file. No defensible alternative was thrown away: both are disproved by the documents.

**source_assessment:** No gaps are registered (gap hash 4f53cda1…). My earlier notes on content missing from the original documents still hold: D05's footnote bodies, D02's comment-letter pages and the garbled Figure 1. None of it affects this question.

**difficulty: medium (marginal).** This is local suitability for the Medium target, not a measured tier. An Easy result is the larger risk: one low-model attempt in five that adds footnote 8's two uninsured credit unions puts it there. "Too hard" is the smaller risk.

**verdict: ready.** This is a local result only. Status should stay `checked` until a platform pass at Medium or above on this fingerprint is recorded.

**Remaining findings (none block local readiness):**
1. **Platform result (gate Q13).** Pending. Status `ready` needs a recorded platform pass at Medium or above with the exact tier line. Local checks say nothing about which tier it will land in.
2. **Difficulty risk.** An Easy-tier result is more likely than "Too hard". An optional quick test (0 of 10 used) would screen the low model, but it does not set a tier.
3. **Reviewer judgement.** A reviewer may find the end-2002 credit unions versus September 2005 banks comparison contrived. It breaks no Guide rule, and rewording can't fix it.
4. **Evidence label.** "Appendix I footnote 2" should say Appendix I body text; the quote itself is word for word. Evidence is part of the fingerprint, so fix it only if a revision happens for another reason. When transcribing, find the passage by its quote.
5. **Question set.** Sketch i02 reuses the same D02–D05 subtraction; vary the documents or mechanism if it is promoted.
6. **Authorship and platform-only checks.** Origin "claude" is accurate, but the export tool accepts only "user"; report this, don't change the origin. Restricted names, originality/duplicates, the token window and the AI-use terms can't be checked locally.
