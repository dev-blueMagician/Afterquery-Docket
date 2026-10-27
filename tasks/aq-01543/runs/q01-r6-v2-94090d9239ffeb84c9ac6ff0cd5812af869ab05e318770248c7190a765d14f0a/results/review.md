# q01 rev 6 - independent review (fresh question-review subagent), 2026-10-08

Input: root, slug, question id, revision, fingerprint, target, source-gap hash, paths to the frozen snapshot, the
question file, the six raw returns of this fingerprint, the rev 5 review, the rev 5 form screenshot and the v4
emulator; three adjudication requests (v4 against every form message and accepted step and rev 6's likely form
result, the shortfall route against the gold, failure-mode and lever-check truth). No writer conversation. The agent
stopped at its 60-turn limit without reporting; the caller asked it (one message) to deliver its report from what it
had established and to mark unfinished items "not checked". Agent id af253fc0a6356f5d5 (79 tool calls in all).
Raw return below, unchanged except for this header.

q01 (rev 6; tested_sha256: 94090d9239ffeb84c9ac6ff0cd5812af869ab05e318770248c7190a765d14f0a)

**Verdict: ready.** Every local check holds on this exact content, and the platform form's reaction to the reasoning is still pending. I expect rev 6 to clear the form's number check (about 75%), but not certainly. Two numbers could still be flagged: 21,335.206 in Step 6 and 8,667.806 in Step 7 (finding 2).

**gold_verified: yes.** I recomputed it with Decimal from the docs/ originals:
- 0.416 × 37,963 = 15,792.608
- 28,460 − 15,792.608 = 12,667.392
- 12,667.392 / 37,963 = 33.36773%
- 56.2 − 33.36773 = 22.83227, which is 22.8 under both half-up and half-even rounding.

The rev 6 route checks out:
- 0.562 × 37,963 = 21,335.206
- 21,335.206 − 12,667.4 = 8,667.806
- 8,667.806 / 37,963 = 22.832247%, written as 22.83%, which rounds to 22.8.

The shortfall divided by production equals Poland's share minus Bulgaria's share. Bulgaria's coal is coal = baseload − nuclear, and S/P = 0.562 − C/P. So the route is identical to 56.2 − 12,667.4/37,963×100, and the unrounded coal figure gives 22.832268.

Other checks:
- All four quotes are verbatim and occur once each in docs/ and text/.
- All 41 corpus hashes match the snapshot, and the packets are byte-identical copies.
- Every packet's question.txt matches the question.
- The answer flips to 22.9 only if the nuclear share is 41.6177% or higher; the document prints 41.6%.
- Early rounding moves the answer: 15.8 TWh gives 22.9, 12.7 TWh gives 22.7, and 38.0 TWh gives 22.9. This keeps the State-the-rounding lever active.

**outcome: A: match; B: match.** I re-ran audit_transcript.py on both: 15 calls each, all inside their packets. The launch prompts held only the root, the packet path and the verbatim question, and the hand-backs equal the saved returns. Each solver has a wrong side remark on the rounding threshold (finding 4). Neither affects the match.

**closed-book: misses.** It answered about 29.0 (Poland about 57%, Bulgaria about 28%), low confidence. Its "partial" contamination note refers only to git-status file names, with no answer content. It made one call, the hand-back.

**necessity:**
- **Doc 1 / D02** is the only source of Bulgaria's 2024 inputs: 37,963 GWh (L10), 28,46 TWh baseload (L11) and 41.6% nuclear (L13). D13 mentions Bulgaria only as a trading neighbour (L23) and in the BRUA pipeline name (L40). The probe without it said not answerable; forced guess 26.7 (p 0.04).
- **Doc 2 / D11** is the only source for Poland: 56.2% (L13). The probe without it said not answerable; forced guess 23.7 (p 0.15) from a recalled 57.1%.
- Both probe packets were verified: 19 documents each, the right one absent, text bodies equal to the originals.
- No smaller set exists. The residual risk is a model that recalls exactly 56.2%; state it at hand-over.

**shortcut: clear.** The shortest route is the D11 L13 lookup plus the three D02 inputs and a subtraction. No document prints 22.8, 22.83, 33.37, 33.4, 21,335, 8,667, 12,667, 15,792 or 74.9.

**source_assessment:** no recorded gaps. source_gaps is empty and its sha 4f53cda1… matches the report. The D02 L44 monthly chart is unrendered in both the original and the capture, and holds totals only. It is irrelevant to the premises, gold, exclusions, uniqueness, necessity and shortcut.

**difficulty: medium (marginal).** Rev 6 does not change it, because solvers never see the reasoning. Easy is still the likeliest single tier, and this bundle has no Easy slot.

**failure_modes:**
- **FM1 is real.** D02 L18 gives 27.6%, and 56.2 − 27.6 = 28.6. It is the tenth paragraph, eight after L10, and its window runs eight months into 2025. "Out-of-range period / Uses the wrong period or date" fits.
- **FM2 is real.** 74.9677 − 40.38 = 34.5877, and 56.2 − 34.5877 = 21.6123, which is 21.6. "Two numeric shares" is true, and the fifth paragraph does open "To support its energy needs". "Figure that must be computed / Uses the wrong period or date" fits.
- Neither trap repeats, neither is ruled out by more than the "In 2024" anchor they test, and both boxes stay true for rev 6.
- Both documents are correctly "Answer component".
- Nit, outside the fingerprint: the boxes write the gap as "22.83%", not percentage points.

**findings:**

1. **Is v4 right?** I ran v4 in memory on every snapshot.
   - It reproduces all seven aq-01543 messages exactly. It is silent on rev 6, q02 rev 2, q03 rev 2 and aq-01320 q01.
   - It misses three recorded messages from other bundles: aq-00949 q05 rev 0 (5,175 and 7,926) and aq-01321 q02 Step 9 (3,941), both from their screenshots or records. It would also miss aq-00949 q03's second semicolon-joined sum by construction, though that pasted text isn't saved.
   - A simpler rule fits equally well: any expression with a "%" operand, other than "a% of b", is not evaluated. It gives the identical seven messages and silences, so the mathjs convention is not established.
   - A rule that allows rounding only up to two decimals also fits all seven without the spaced-% rule. It conflicts only with the memory's trial-01 "= 10.123%" pass, which can't be re-checked because that bundle was rebuilt.
   - Uniform rounding fails on 9.116, and the fraction rule fails on rev 5.
2. **Will rev 6 clear the form?** Probably, with two untested features in Steps 6 and 7:
   - **Layout.** They are the first calculations written mid-sentence after ordinary words. Every cleanly evaluated calculation on record starts right after a colon or at a sentence start. A parser that reads the expression from the last colon (which would also explain aq-00949 q03's flag) would flag both. The only counter-precedent is aq-00949 q04 rev 2's "…, and 7,926 / 5,175 = 153.2%", where "no flag" was recorded but the screen wasn't observed.
   - **Floating point.** Both results are inexact in standard float arithmetic: 21335.206000000002 in every evaluation order, and 8667.805999999999. A rule with naive equality above two decimals fits every record except trial-01.
   - Step 8 is low risk: it is the same shape as the accepted Step 5, and its operand is an earlier "=" result.
   - Two properties would clear every rule I tested:
     - each calculation sits right after a colon;
     - each new result is either exact in float arithmetic or written to two decimals or fewer as a %-result or percent-of.
   - That change would be a new revision needing fresh checks; your call.
3. **Is the shortfall route clear?** Yes. It is correct and traceable for a human reviewer. Step 5's 33.37% is unused downstream but lets a reader check the subtraction directly. The final rounding to 22.8 is implicit, as in revs 4 and 5; "Reasoning reaches the answer" is low risk. Removing the Decoy line loses nothing required: this is not a which-items question, and FM1 carries the exclusion. An optional number-free mention in the reasoning would keep the exclusion visible there.
4. **Records.** The rev 6 Blind solve lines repeat each solver's wrong threshold: A's claim that 41.55–41.65% still gives 22.8, and B's claim that 41.65% or more gives 22.9. The true threshold is 41.6177%. Annotate them.
5. **Memory note.** docket-form-automated-checks should record the non-mathjs rule from finding 1 as an equally fitting explanation. It should also say that v4's "all seven" claim covers aq-01543 only.
6. **Set.** q03 rev 2 also relies on a three-decimal percent-of result (33,271.553), so either first paste tests that shape for both.
7. **Hand-over.** notes/handover-q01.md matches rev 6. At hand-over, state the Poland recall risk, the form reaction pending with the two named numbers, and the Easy-tier risk.
8. **Not checked:**
   - the capture overview's per-document fact lines;
   - the exact pasted text behind aq-00949 q03's form message;
   - the form's "Answer matches a stated figure" advisory;
   - the platform-only checks: Original question, Not a duplicate, Restricted names, token window.
9. I wrote one temporary file to the session scratchpad (a print of the snapshot's fields), outside the workspace. I made no workspace writes.

Key paths:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\questions\q01.md
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\notes\helpers\form_check_v4.py
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r6-v2-94090d9239ffeb84c9ac6ff0cd5812af869ab05e318770248c7190a765d14f0a\snapshot.json
