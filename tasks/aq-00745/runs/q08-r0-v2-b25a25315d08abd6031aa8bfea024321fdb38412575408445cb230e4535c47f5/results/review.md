# q08 rev 0 independent review (question-review, fresh context, 2026-10-06)

Verbatim return from the task notification.

**q08 (rev 0; tested_sha256: b25a25315d08abd6031aa8bfea024321fdb38412575408445cb230e4535c47f5)**

**gold_verified: yes.** I recomputed it from the original passages using exact fractions.
- **Closing date:** March 23, 2026 (D08 l.27, and D10 l.49 and l.203).
- **Full-year 2026 ranges:** only three exist in D01–D11. I searched every $5.xx figure plus the terms "full-year 2026", raise, reaffirm and previous range. D05, D09 and D11 contain none.
  - D07, Jan. 22: $5.55–$5.80 (l.19 and l.335)
  - D08, Apr. 16: $5.38–$5.58 (l.21 and l.223)
  - D10, Jul. 16: $5.45–$5.60 (l.21 and l.329)
- **Dividend:** D10 l.337 is the only declaration made in June 2026. It was declared June 12, has a record date of July 15, and is payable Aug. 17 (a Monday).
- **Range in force on each day:** Mar 23 is D07's, low end 5.55. Aug 17 is D10's, low end 5.45.
- **Result:** 5.45 − 5.55 = −0.10 exactly.
- **Alternatives:**
  - D08's range taken at the closing gives +0.07.
  - Anchoring on the June 12 or July 15 date gives −0.17.
  - Both errors together give 0.00.
  - "Low end" rules out the midpoint (−0.15) and the high end (−0.20).
  - "Give the sign" rules out an unsigned path length (0.24).

**outcome: A: match; B: match.** Both answered −$0.10 (the Unicode minus is equivalent) by the correct path, and both rejected +$0.07 on the dates. B also set aside the Feb. 20 dividend. Each packet held only question.txt plus the 11 originals and texts, with hashes identical to the bundle. Both reported themselves uncontaminated. A's "D07+D10 minimal" is a necessity misjudgment, not a gold error.

**closed-book: misses.** It answered −$0.17 at low confidence: it recalled the January range and faintly the April one, but not the July range. That is not equivalent to the gold. Its packet held the question only.

**necessity:** all three documents are needed; no smaller set works.
- **D07** is the only source of 5.55. D08 and D10 never print the January range. Without D07, nothing gives the closing-day range.
- **D08** is the only document that dates the $5.38–$5.58 range to April 16, after the closing. D10 l.19 and l.29 leave "previous range" undated, and D07 l.33 only *expected* a second-quarter close. Without D08, the closing-day low end could be 5.55 or 5.38 (giving −0.10 or +0.07). Its closing date can be replaced by D10.
- **D10** is the only source of the June declaration, the Aug. 17 payable date and 5.45. D08 l.231's Feb. 20 dividend is a different one.

**shortcut: clear.** The auditor's route matches my gold: closing date, then D07's range with D08 dating the April range, then D10's dividend and July range, then one subtraction. 5.55 appears only in D07 and 5.45 only in D10. No passage pairs them or states a low-end change. The capture overview lists each document's range and Doc 10's two dividend dates separately, with no answer. D10's "compared to previous range" sentence is an answer-shaped trap (+0.07), not a shortcut.

**source_assessment: not required.** source_gaps is [] (4f53cda1… is the hash of an empty list), and the capture reports "11 of 11 captured in full".

**difficulty: medium (marginal).** This is local suitability only.
- **For:**
  - **Measured trap:** the main trap is the one measured on q01. There, 4 of 5 low attempts took D08's post-closing range, and the platform's all-document check split 1 right, 1 wrong.
  - **Signpost removed:** q08 drops q01's "in force" signpost.
  - **Trap in the solver's path:** every solver has to open D10 for the dividend, and D10 prints the trap pair in one sentence.
  - **Added filter:** the payment date versus the declaration or record date is an independent second filter.
  - **Same mechanism passed at Medium:** aq-00964 q01 used the same mechanism and was placed Medium.
- **Against:**
  - **Weak second filter:** the payable date is one plainly dated sentence next to the declaration date. That kind of bridge was crossed easily in aq-00949 q02 and on aq-00998.
  - **First/latest coincidence:** the correct editions are the bundle's first and latest 2026 ranges. A solver who ignores the anchors, or who misreads the anchor as June but defaults to the latest range, still lands on the gold.
  - **Correlated errors:** careful date readers will avoid both traps, so the two filters are not fully independent.
  - **Net:** expect Low at the 0/5–1/5 border. An Easy placement, for which this bundle has no slot, is a material risk.

**verdict: ready.** This is local readiness only, conditional on finding 1. Status stays `checked` until there is an exact-content platform pass at Medium.

**findings:**
1. **Q2/Q14 and records: the planned document marking conflicts with the frozen field.**
   - **Evidence:** the frozen field is `documents: D07, D08, D10`, and it is fingerprinted (check_questions.py l.172–176). But the Lever checks "Necessity" bullet and the "Next" line in session.md say to mark only Doc 7 and Doc 10 on the form.
   - **Consequence:** that marking changes tested content. WORKFLOW l.187 then requires a revision bump and fresh checks, so these records would not bind to what is submitted. My removal test shows D08 is necessary.
   - **Required:** hand over with Doc 7, Doc 8 and Doc 10 marked, and correct the Lever-checks recommendation (that field is not fingerprinted). Otherwise re-prepare as rev 1 and rerun.
   - **Unknown (platform-only):** whether the platform's document check run without Doc 8 still reaches −$0.10 and calls Doc 8 "not needed".
2. **Set review: q01 must not be submitted alongside q08.**
   - **Evidence:** q01.md still says `checked`, and q01 is already saved and difficulty-checked on the platform (version 3438f6). It shares q08's closing-day anchor, the July endpoint and the six-word span. Its phrase "the range in force when it completed" signposts q08's trap.
   - **Required:** record q01 as superseded, and replace it on the platform rather than submitting both. The Sibling and Not-a-duplicate checks are unknown (platform-only).
3. **Q9/Q12: "paid" versus the printed "payable".**
   - **Evidence:** D10 prints only "is payable Aug. 17, 2026". Aug. 17, 2026 is a Monday, so there is no weekend roll-over. The guide's worked example 2 uses the same convention: a stated effective date is the day rules "took effect".
   - **Consequence:** acceptable. Neither the declaration date nor the record date is a defensible payment day. Disclose this at hand-over.
4. **Q4: the answer rests on no guidance change in two windows.**
   - **Windows:** Jan 22–Mar 23 and Jul 16–Aug 17. No document can prove a non-event.
   - **Support:** D08 l.15 dates the acquisition update with "Updates Guidance to Reflect Acquisition"; D10 l.29 links the April and July editions; D11 (Aug 20) postdates Aug 17 and has no guidance.
   - **Consequence:** reading "the range in force" as "the latest one issued" is the ordinary meaning. The platform raised no not-answerable verdict on q01, which made the same assumption. No action needed.
5. **Q4 (platform-only): expect a "may be too vague" advisory.**
   - **Evidence:** q01 drew "This question may be too vague: several solvers agreed on an answer that is not your gold".
   - **Why +$0.07 is not a second answer:** D08's April 16 date line, 24 days after the closing, rules it out.
   - **Unknown:** the result of the "One defensible answer" model check.
6. **Q11/D7: the lever is active but the risk is real.** The three wrong-edition answers are all distinct, but the first/latest coincidence and the weak second filter (see the difficulty rating) make an Easy placement plausible. Only the platform can measure this.
7. **Records:**
   - **Fingerprints:** all four records (A, B, closed-book, audit) carry rev 0 and b25a2531…. The report and my own recomputation give the same fingerprint, and the audit record parses as `verdict: clear`.
   - **Floor:** no FAIL. The origin WARN is accurate and authorship is the user's decision. The sibling WARN is covered by finding 2.
   - **Quotes and length:** all nine quotes appear verbatim in both the local text and the platform capture. The question is 50 words: over the guide's 20–45 aim, under the form's 60-word warning.
   - **Unknown (platform-only):** Q13 (no platform result yet), restricted names, originality, duplicates and the token window.

**Files:**
- D:\Dev\Docket\tasks\aq-00745\questions\q08.md
- D:\Dev\Docket\tasks\aq-00745\runs\q08-r0-v2-b25a25315d08abd6031aa8bfea024321fdb38412575408445cb230e4535c47f5\results\returns.md
- D:\Dev\Docket\tasks\aq-00745\runs\q01-r1-v2-dbae27b24ec253977887e482e7d1f02ff0b886d77e4042e0ca23494c8cf9fda5\results\platform-difficulty-check-run2.md
- D:\Dev\Docket\tasks\aq-00745\notes\session.md
