# q01 rev 0 second careful check (2026-10-06)

Fresh question-review agent, independent of the first reviewer, run at the user's request ("once
after reach result, you need to check carefully again"). Input: question file, snapshot, raw
returns, removal probes, corpus, hand-over block (notes/handover-q01.md), task-page capture, guide
and memory notes. Return copied verbatim.

**q01 (rev 0; tested_sha256: 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1)**

**gold_verified: yes.** I recomputed it by script from the source passages:
- Credit unions: 9,688 (D02 231) + 214 (D02 1179) = 9,902. The other route gives the same total: 212 (D02 233) + 2 (fn 8, D02 239).
- Banks: 1,846 + 5,695 (D05 191) = 7,541.
- Answer: 9,902 − 7,541 = 2,361. Shares of 97.84% and 2.14% match the text's "98 percent" and "about 2 percent".
- No text file or capture line prints 9,902, 9,900, 7,541, 2,361, 2,359 or 2,147.

**outcome: A: match; B: match.**
- A's main answer is 2,361. Its 2,359 alternative treats fn 8 as undated, but A never read D02 1179, which dates the 214 (including the two uninsured) to "As of December 2002".
- B read 1179 and answered with high confidence.
- The packets are separate. All 39 packet files (13 per packet) hash-match the snapshot, and each question.txt is the verbatim question.

**closed-book: misses.** It answered 2,148, not equivalent to the gold. It recalled 9,688 exactly and banks as "about 7,540".

**necessity:**
- **Doc 2** is the only source of credit-union counts. D03 has three mentions, all the NCUA's name; D05 has none. Memory can supply 9,688 (the closed-book run did) or 9,688 + 212 (the q02 probe recalled 212), giving 2,147 or 2,359. The two uninsured credit unions are GAO-only. Robust.
- **Doc 5** is the only bank count and the only "September 30, 2005" in the bundle. D05 has no thrift counts, and its "about 1,900 national banks" (393) sits inside Doc 5 anyway. Memory gives about 7,540 to 7,550 (closed-book and probe), so 2,352 to 2,362.
- The platform's document check fails only if the high model, without Doc 5, recalls exactly 7,541 and also keeps the remainder. I estimate roughly 10–20% across its two attempts. That is a real but not blocking risk.
- No smaller source set works.

**shortcut: clear.**
- Shortest route: D02 231 + 1179 (or 233 + 239), then D05 191, then one subtraction.
- The overview (capture lines 47 and 77) shows only 9,688, 1,846 and 5,695, which leads to the 2,147 decoy.
- Audit 1's "ambiguous" rested on a guess about the writer's intent (2,147), not on the text. Audit 2 was clear, and its search covered all six documents.

**source_assessment:**
- `prepare`/`report` register no gaps (gap hash 4f53cda1…).
- The capture's Doc 2 and Doc 5 bodies equal the local text after whitespace normalization, so what is missing from the originals is also missing on the platform. This does not make the corpus complete.
- **D05 footnote bodies, including fn 6 on the bank-count sentence:**
  - premises: the question uses D05's own word "banks" and its date.
  - gold: both counts are printed in the body text.
  - exclusions: none used.
  - uniqueness: no solver can see a competing definition.
  - necessity: D05 is still the only bank count.
  - shortcut: no hidden total is visible.
- **D02 Appendix III/IV letters (1261–1315):** only headers survive and no input comes from them.
- **D02 Figure 1:** garbled, but its values sum to 212, matching Table 3 (469).

**difficulty: medium (marginal).** This is local suitability only. The trap sits inside D02: a same-label wrong value (9,688) and an implied 98% + 2% total (9,900), both ruled out only by fn 8 or 1179. The cross-document step is plain arithmetic.

**verdict: ready (local).** Status stays `checked` until a platform pass at Medium or above on this fingerprint.

**findings:**

1. **Hand-over fidelity (check 1).**
   - The question, gold, all four reasoning steps, component, tags, documents and all six quotes are identical to the snapshot. The q01.md tested fields equal the snapshot, and `report` recomputes 41de64e9….
   - Doc titles match the capture (lines 19 and 22). Local Dnn equals platform Doc N.
   - Each quote is 38–128 characters and occurs exactly once in the capture: Doc 2 at lines 619, 619, 621, 627 and 1567; Doc 5 at 3021. None sits in a pipe table, and "state- chartered" matches the platform text.

2. **Alternatives (check 2).**
   - 2,147 is ruled out by D02 231: 9,688 is "Almost all (98 percent)".
   - 2,359 is ruled out by 1179, which dates the 214 ("all but two were privately insured"). Table 3 (467–469) gives 212 across eight states, none of them New Hampshire, and "uninsured" excludes private insurance.
   - 2,345 and 3,059 come from rounded shares when exact counts exist.
   - 8,056 or 4,207 count one charter type; D05 189 says banks "can be either federally or state-chartered".
   - 8,002 uses "about 1,900", which is approximate and in December 2004 context.
   - Including thrifts has no figure anywhere in the bundle.
   - Period: no document uses "end of 2002", and no competing end-2002 or 2005 count exists.
   - Exactly one answer is defensible: 2,361.

3. **Form checks (check 3).**
   - Length and shape: 23 words; no em or en dashes; one ask; answer is 4 words with units and no semicolon; one component. The question does not contain "2,361", asks about the world rather than the documents, and names both periods exactly. Since this is not a company, "fiscal or calendar" does not apply.
   - Reasoning-number check (emulated):
     - Step 1: 9,688, 214, 212 and "December 2002" are all in Doc 2; 9,902 follows "=".
     - Step 2: 1,846, 5,695 and "September 30, 2005" are all in Doc 5; 7,541 follows "=".
     - Step 3 uses derived values in a step naming both source documents. aq-00949 q05's step 3 had the same shape and passed. 2,361 follows "=".
     - Step 4 has no digits.
   - The comma in "2,361" is a thousands separator. aq-00964 q01's "$1,605 million" drew no recorded list-order warning. If the advisory appears here, it is a false positive and does not block.
   - Unknown locally: restricted names, originality/duplicate, token window, AI-use terms.

4. **Reviewer risks and wording (check 5).**
   - The 2002-vs-2005 pairing is inherently contrived. The Guide allows a cross-document difference, and wording cannot fix it because D05 has no 2002 bank count and D02 has no 2005 credit-union count.
   - Solver answers split across 2,147 and 2,359 may trigger the platform's non-failing "may be too vague" warning. The reasoning and the 1179 quote answer it.
   - Rewordings I considered and rejected:
     - "in December 2002": steers search toward the 1179 sentence and fixes nothing observed.
     - "in total" / "all credit unions": hints at the remainder.
     - Naming the uninsured credit unions: gives the trap away.
     - "state-chartered banks" (gold 4,207): slightly less recallable, but more contrived and needs a new revision.
     - A ratio: removes the trap (both totals give 1.313 at three decimals).
   - Recommendation: no change.

5. **Tier expectation (check 6).**
   - Roughly a coin flip: Easy about 45%, Medium about 40%, High about 10%, Too easy and Too hard each under 5%.
   - The low model only needs one attempt in five that adds fn 8's two to land Easy.
   - Local Opus readers kept the remainder in 4 of 5 runs. However, past local predictions have been too pessimistic on all four measured questions, which pushes toward Medium.

6. **Evidence label (local only).** "Appendix I footnote 2" should say Appendix I body text. The hand-over note already tells you to find it by its words. Fix it only in a later revision.

**blocking issues:** none.

**non-blocking notes:**
- **Run the difficulty check before submitting, and submit only on "In band — Medium tier" or higher.** A quick test screens only the low model and has not predicted tiers reliably here.
- **Doc 5 recall risk.** If the document check flags Doc 5, the form allows a 200-character note to the reviewer, but whether the gate then passes is unconfirmed. Otherwise it needs a revision and fresh checks.
- **Authorship.** Origin is "claude". The checklist item "I wrote this question myself" is a statement only you can decide about honestly; leave the origin record as it is.
- **Sibling question.** q02 is dropped and shares the deciding fact, so keep it off the form.
- **Form proposals.** The reasoning contains no quotation marks, so if the form's "Derive the rest" proposes fields, check them by hand.
- **Not verified here.** None of this is a platform result.
