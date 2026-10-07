# q01 rev 1 independent review (question-review, fresh context, 2026-10-05)

Verbatim return from the task notification.

q01 (rev 1; tested_sha256: dbae27b24ec253977887e482e7d1f02ff0b886d77e4042e0ca23494c8cf9fda5)

**gold_verified: yes.** I recomputed the gold from the original documents using exact fractions.
- **Closing date:** D08 l.27, "On March 23, 2026, Abbott completed its acquisition of Exact Sciences". D10 repeats it at l.49, 203, 685 and 722.
- **April range is too late:** D08 is dated April 16, 2026 (l.21). Its $5.38–$5.58 range (l.19/31/223) was issued after the closing.
- **Range in force at closing:** D07, dated Jan. 22, 2026, gives $5.55–$5.80 (l.17/31/335). It is the latest range issued before March 23.
- **July range:** D10, dated July 16, 2026, gives $5.45–$5.60 (l.19/29/329).
- **Calculation:** 5.525 − 5.675 = −0.150 exactly, so the answer is -$0.15 under any rounding convention. Units are dollars per share.
- **Alternatives checked:**
  - Using the April range as the base gives +0.045 (+$0.05 rounding half up, +$0.04 half to even).
  - Subtracting the $0.20 dilution from the January midpoint gives +0.05.
  - Comparing range endpoints instead of midpoints gives −0.10 or −0.20.
  - The wording ("in force when it completed", "midpoint of … guidance") rules all of these out.
- **Uniqueness of inputs:** each of the six range endpoints appears only at the lines cited above (searched all 11 texts).
- **Other checks:** all 8 evidence quotes appear word for word in the docs/ originals. The question is 45 words.

**outcome: A: match; B: match.**
- Both answered -$0.15 with high confidence. They used separate packets (solver-1, solver-2), with the frozen wording and corpus bytes confirmed identical.
- Their citations differ (A: D10 l.203/685; B: D10 l.49), which fits independent runs.
- Both rejected the April range because it was issued April 16, after the closing. Both declared themselves uncontaminated.
- Independence rests on your attestation; I cannot inspect the agents' contexts.

**closed-book: misses.** The answer was "about −$0.20", low confidence, stated as a guess. It recalled the January range; the July range is after its cutoff.
- −$0.20 is not equivalent to -$0.15 at cent precision.
- Residual exposure: the sign and rough size can be guessed from the recalled January range plus the deal's dilution. The July raise is the fact only the bundle holds.

**necessity:**
- **D07:** the only source of $5.55–$5.80.
  - Without it, D08 states no earlier range and D10 names only the April range as "previous".
  - Working back from D08's "$0.20 of dilution" gives 5.58–5.78 (−0.155), which no document supports.
- **D10:** the only source of $5.45–$5.60. D11 (Aug 20, 2026) has no guidance.
- **D08:** the only document that dates $5.38–$5.58 to after the closing. Its closing date is repeated in D10, so the date alone is not what makes D08 necessary.
  - Without D08, D10's "previous range" has no date. D05 l.49 and D07 l.33 give only an expected second-quarter close, and D09 and D11 have no guidance.
  - The answer could then be −0.15 or +0.045, and the documents cannot decide. Only an outside assumption about when guidance usually changes picks the gold.
- **No smaller set works:**
  - D07 + D10: the base is ambiguous.
  - D08 + D10: no January range.
  - D07 + D08: no July range.
- **Newly visible tables:** I read D07, D08 and D10 in full. Their tables (earnings statements, tax notes, reconciliations, specified items) contain no range, midpoint or release date.

**shortcut: clear.** I verified the shortest route:
1. Closing date from D08 l.27 (or D10 l.49).
2. D08's April 16 date line (l.21) rules out D08's own range.
3. January range from D07 l.335.
4. July range from D10 l.329.
5. Two midpoints and one difference.

No passage prints the answer or both ranges together, and a search finds inputs only. This matches the auditor's route. Reaching the gold from D07 + D10 plus a cadence assumption is a difficulty risk, not a Guide violation; it still needs two documents.

**source_assessment: not required.**
- The snapshot lists no source gaps; its gap hash is the hash of an empty list.
- intake.json records all 11 documents as complete, with zero gap characters, matching the capture. The capture hash (49dc4016…) matches.
- All 23 corpus hashes match the snapshot. Each original equals its capture section apart from a title and token-count line.
- The rev 0 Source assessment is history only.

**difficulty: easy (marginal).** This is local suitability only, not a measured tier.
- **For:** it uses the same mechanism as the aq-00964 q01 platform pass. D08 reports the closing and prints its own post-closing range, and D10 calls that range "previous". So the April decoy is reachable from both documents that state the closing date.
- **Against:**
  - The correct base is the first 2026 range, so comparing "initial guidance" with July reaches the gold without the date bridge (D7 partial).
  - "In force when" points the reader at the date check, and both bridge facts are plain highlight or date-line sentences (D4 weak).
  - The overview prints every input (finding 1, D2 weak).
  - The January range can be recalled without the documents (D1 partial).
- D3, D5 and D6 hold.

**verdict: ready.** This is local readiness only. Status stays `checked` until an exact-content platform pass at Easy or above.

**findings:**
0. **Gate:** Q1–Q12 and Q14 pass locally.
   - Q2: three necessary documents.
   - Q10: 45 words, one ask.
   - Q11: the edition lever changes the answer only against the April range; the calculation lever is active; no "which items" decoy is needed.
   - Q14: one component, quoted from all three necessary documents.
   - Rule 10 (ask about the world, not the set) is met. Doc 7, 8 and 10 match D07, D08 and D10.
   - Q13 (platform pass) is pending.
1. **Overview exposure (D2).** The capture's overview prints everything needed (AQ-00745_2026-10-06_0256.md l.95–97, 103–107, 125–127):
   - Doc 7: "$5.55 to $5.80" and "Jan. 22, 2026".
   - Doc 8: "updates guidance to reflect the acquisition of Exact Sciences", "March 23, 2026 · April 16, 2026", and "$5.38 to $5.58".
   - Doc 10: "$5.45–$5.60".

   The Lever checks claim of "no edition-to-event link" is wrong. This lowers difficulty but breaks no rule, since the overview is for navigation and prints no answer. Correct the note and disclose the exposure at hand-over.
2. **Stale line numbers.** The Lever checks "Precision/readings" line cites "D08 l.…203" and "D10 l.…289". Those are numbers from the clipped capture (line-remap.md maps old D08 203 to new 223 and old D10 289 to new 329). The current l.203 is a table row and l.289 is blank. Lever checks is outside the fingerprinted fields (check_questions.py l.155–167), so fixing it should not change the fingerprint; run `report` to confirm it stays dbae27b2….
3. **Missing rev 1 records.** `report` shows no rev 1 records yet. Enter A, B, the closed-book solve, the shortcut audit and this review as rev 1 with this fingerprint.
4. **Earliest-edition coincidence (D7).** The correct range is also the first 2026 range. No fix is needed for Easy; only the platform can measure the effect.
5. **No documents between Jan 22 and Apr 16, 2026.** All three document readers noted this gap. The bundle still settles the answer: D08 l.15 says "Updates Guidance to Reflect Acquisition of Exact Sciences" on April 16. Acceptable as is.
6. **Platform-only, unknown locally:**
   - restricted names;
   - originality and duplicate checks;
   - token window (the overview counts total about 98,400 tokens);
   - how the form's number check treats Step 4 and the Decoy line, which each cite two documents;
   - whether the platform's model already knows the July 2026 guidance.
7. **Authorship.** Origin is `claude`, but the export tool accepts `user` only, and "I wrote this question myself" cannot be ticked truthfully. Report this to the user separately.
8. **Set review.** q01–q04 all list D07 and D10. q01 and q02 both read the guidance sections (full-year ranges here, quarterly ranges in q02), but neither gives the other's answer away. Vary the document pairs in any further work.

Files:
- D:\Dev\Docket\tasks\aq-00745\questions\q01.md
- D:\Dev\Docket\tasks\aq-00745\runs\q01-r1-v2-dbae27b24ec253977887e482e7d1f02ff0b886d77e4042e0ca23494c8cf9fda5\results\returns.md
- D:\Dev\Docket\tasks\aq-00745\runs\q01-r1-v2-dbae27b24ec253977887e482e7d1f02ff0b886d77e4042e0ca23494c8cf9fda5\snapshot.json
- D:\Dev\Docket\AQ-00745_2026-10-06_0256.md
- D:\Dev\Docket\tasks\aq-00745\notes\line-remap.md
