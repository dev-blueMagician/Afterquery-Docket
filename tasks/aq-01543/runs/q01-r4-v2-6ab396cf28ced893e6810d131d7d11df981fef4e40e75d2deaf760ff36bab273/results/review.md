# q01 rev 4 - independent review (fresh question-review subagent), 2026-10-08

Input: root, slug, question id, revision, fingerprint, target, source-gap hash, paths to the frozen snapshot, the
question file, the six raw returns of this fingerprint, the rev 3 review, the form screenshot and the emulator;
three adjudication requests (reaching the gold with "= 22.83", failure-mode truth, rev 3 findings). No writer
conversation. Raw return below, unchanged except for this header.

q01 (rev 4; tested_sha256: 6ab396cf28ced893e6810d131d7d11df981fef4e40e75d2deaf760ff36bab273)

**Short version:** rev 4 holds up locally, and Step 6 should now clear the form's number check. One thing must happen first: `notes/handover-q01.md` still holds the rev 3 text, including the Step 6 line the form rejected. Regenerate it before the user pastes anything.

**gold_verified: yes.** I recomputed it with Decimal from the docs/ originals.
- Nuclear: 0.416 × 37,963 = 15,792.608 GWh.
- Coal: 28,460 − 15,792.608 = 12,667.392 GWh, which is 33.36773% of 37,963.
- Result: 56.2 − 33.36773 = 22.8323, so 22.8.
- All four quotes appear word for word, once each, in docs/ and in the platform capture (curly apostrophe included). The corpus hashes match the snapshot, and the capture hash (41394e0a…) matches intake.json.
- Edges: 22.9 needs a nuclear share of 41.6177% or more; the document prints 41.6%. A baseload total anywhere from 28.455 to 28.465 TWh gives 22.82–22.85.
- Every other route gives a different value:
  - Bulgaria side: 28.6, 29.2, 21.2, 21.6, −18.8.
  - Poland side: 37.3, 27.1, 22.6, 36.6.
  - Rebuilding Poland from its TWh figures: 22.48–22.66.
  - Rounding a TWh input early: 22.85 (so 22.9), 22.75 (so 22.7), 22.91 (so 22.9).
  - None of these comes from a stated figure that the question's wording allows.

**outcome: A: match; B: match.** Both reached 22.8 by the same derivation and rejected 28.6, 29.2 and 21.6.
- I re-ran the transcript audit helper myself. Solver A (agent-a385b100…) made 17 calls and solver B (agent-a5cefa28…) made 12, all inside their own packets.
- Each saved return contains every line of its handback.
- The packets hold all 20 documents, byte-identical to text/ and docs/, plus the verbatim question.

**closed-book: misses.** It answered "about 28 percentage points" (Poland about 57.1% minus Bulgaria about 29%), with low confidence. That is not equivalent to 22.8. Its transcript (agent-a4090f5c…) is a single handback.

**necessity:**
- **Doc 1 (D02):** the only source of Bulgaria's three 2024 inputs (L10, L11, L13). Elsewhere "Bulgar" appears only in Doc 20 (Romania): L21 as a trading partner and L38 in the BRUA pipeline name.
  - Probe without it (agent-aafd5e3f…, 14 calls; 19 documents, the D02 original and its manifest entry absent, bodies identical): "not answerable". Forced guess 28.2 (p 0.05).
- **Doc 2 (D11):** the only document that names Poland.
  - Probe without it (agent-a258c841…, 12 calls): "not answerable". Forced guess 23.7 (p 0.15), from a recalled 57.1%.
- No smaller document set exists.
- Remaining risk: a model that recalls Poland's share as 56.12–56.21% reaches the gold without Doc 2. Every local recall gave 57.0–57.1% (now four closed-book runs, four probes and one recall test). Without Doc 1, the gold needs a recalled Bulgaria share of 33.35–33.45%.

**shortcut: clear.** The verified route is a Doc 2 L13 lookup, plus the Doc 1 L10/L11/L13 derivation (decimal comma, GWh and TWh), plus one subtraction.
- The capture's overview cards print 56.2%, 37,963 GWh and 41.6%: inputs only, with no baseload total and no Bulgarian coal share.
- There is no ranking or summary sentence across countries.
- The auditor (agent-ab8a12da…, 16 calls, all inside its packet) also found the route clear.

**source_assessment:** no recorded gaps. The gap hash 4f53cda1… is the sha256 of "[]". There is one known unrendered item: Doc 1's "View Bulgaria's Electricity Production from Jan 2024 to Dec 2024 in the chart:" (docs L42 / text L44). The chart is missing from the original and the capture alike.
- Premises: none rest on it.
- Gold: it could show monthly totals at most; the annual 37,963 GWh is stated, and the derivation uses no monthly data.
- Exclusions: the question has none.
- Uniqueness: a production-total chart has no split by source, so it cannot give a rival coal share.
- Necessity: it sits inside Doc 1, so it cannot stand in for Doc 2 or for L11/L13.
- Shortcut: it is absent on the platform too.

L11's "3,3264 GWh" is malformed in the original and unused. None of this shows the corpus is complete.

**difficulty: medium (marginal), as local suitability only.** The question, answer and documents are unchanged since rev 1.
- **For Medium:** no Bulgarian 2024 coal share is printed, getting one takes three dependent 2024 inputs, and a precise, answer-shaped 27.6% (with 40.38% nuclear beside it) sits in an overlapping window. The exact result is 0.018 below a rounding edge.
- **Against:** the window's own opening words disarm it, the inputs are in paragraphs 2, 3 and 5, and Poland is a single lookup. Similar shapes measured Easy (aq-01320, aq-01430).
- Easy is still the likeliest single platform tier, and this bundle has no Easy slot.

**verdict: ready (local).** This holds only once the hand-over is regenerated (finding 1). After that, status can go to checked, with the platform pending.

**failure_modes:**
- **FM1 (Out-of-range period / Uses the wrong period or date): real.**
  - The passage is Doc 1 L18, the Energy chapter's tenth paragraph in both the text and the capture. 56.2 − 27.6 = 28.6, which is 5.77 above the exact gold, so "almost six points" is true.
  - The label is the best fit; "Trailing-period total" and "Fiscal vs calendar period" are weaker alternatives. The cause fits.
  - The new third box, "56.2% - 33.37% = 22.83, which rounds to 22.8", is exact and matches Step 6.
  - "Eight paragraphs after", "eight months into 2025" and "is framed as" are all true.
- **FM2 (Figure that must be computed / Uses the wrong period or date): real.**
  - 28,460 / 37,963 = 74.97%; 74.97 − 40.38 = 34.59; 56.2 − 34.59 = 21.61, so 21.6 (21.612 unrounded).
  - The label is acceptable ("Look-alike measure" is the alternative), and the cause fits.
  - "Fifth paragraph" and "two numeric shares" are true.
- The wording rules out neither trap, no trap repeats, and the boxes run 242 and 212 words. No run produced either wrong answer; solvers A and B and the auditor each named both as rejected readings.
- **Necessary documents:** the section is blank, so both default to "Answer component", which is correct.

**findings:**
1. **The hand-over is stale (fix before hand-over).** `notes/handover-q01.md` was written at 00:11, before rev 4's 01:12 snapshot. It says revision 3 and 50f506ff…, its line 44 is "= 22.8 percentage points (to one decimal place)" (the line the form rejected), and FM1's third box still ends "= 22.8.". Pasting it again would bring back the same flag. Regenerate it with `--handover --q q01` and confirm Step 6 reads "56.2% - 33.37% = 22.83 percentage points."
2. **Your item 1 (form number check): rev 4 is predicted to pass.**
   - How far each "=" result is from its exact value: Step 2 0%, Step 3 0.0001%, Step 4 0%, Step 5 0.0067%, Step 6 0% (0.0099% if the form uses the unrounded 33.3677), Decoy 0%. All are far below the 0.131% that was rejected.
   - Every other number is printed in the document its step cites or repeats an earlier result character for character (33.37%). In the Decoy line, 27.6%, 2024, 2025 and 27 are in Doc 1; 56.2 matches Doc 2's 56.2%; 28.6 is also printed in Doc 2 as "28.6 GW".
   - I ran form_check_v2 read-only on all three snapshots. It reproduces the rev 2 message (33.37) and the rev 3 message (22.8) exactly, and prints nothing for rev 4.
   - The memory note records a precedent: aq-docket-trial-01's "= 10.123%" passed with a 10.1% gold.
   - The rev 3 screenshot shows the Decoy line in the box with only Step 6 flagged. If the form treats that unnumbered line as part of Step 6, the Step 6 flag may have hidden a Decoy flag, so the Decoy line is confirmed only when rev 4's Step 6 clears.
   - Caveat: the ~0.1% threshold rests on a few observations, and the content of one trial-01 paste is no longer on file. This matters for q02's planned fix, not for rev 4, whose result is exact.
3. **Reaching the gold.** Step 6 ends at 22.83 with no rounding sentence; the question's "to one decimal place" carries the step to 22.8 (22.83 is 0.02 below the 22.85 edge). Restating the rounded figure would invite the number flag. The only residual risk is the platform's "Reasoning reaches the answer" model check, which I judge low; it cannot be checked locally.
4. **Your item 3 (rev 3 findings).**
   - Finding 1 recurs, now with rev 3 content (see finding 1 above).
   - Finding 2 is superseded: its prediction failed because its emulation had no closeness test, which v2 now adds.
   - Finding 3 is unchanged after the rev 4 probes: Doc 2 risk about 5–10%, Doc 1 under 3%.
   - Rev 2's finding 5 is still open: the hand-over still has no line on the Poland recall risk.
   - Records: every rev 4 record carries rev 4 and 6ab396cf… and matches its raw return. The report recomputes 6ab396cf…. Between the rev 3 and rev 4 snapshots, the only fingerprinted change is Step 6 (plus the revision number).
   - Finding 8 has been applied.
5. **Optional tidying (outside the fingerprint).** The Lever checks' recall tally ("three closed-book runs, three probes") is now four and four, and the necessity and failure-mode lines leave out the rev 4 runs.
6. **Set review.** q01–q03 share no inputs and give nothing away to each other. All three, though, are two-country, one-number derivations at a stated precision; q01 and q03 are both electricity-generation shares. The rev 3 advice to vary the shape was not taken up in q03.
7. **Unknown here (platform-only):** restricted names, Original question, Not a duplicate, the token window, the form's model checks, the difficulty check, and the form's reaction to rev 4's Step 6 (pending the user's re-paste). The floor shows 0 FAIL and 2 WARN (origin; revision rounds). The Lever checks explain the revision WARN: rev 4 answers new platform evidence, and the question, answer and documents are unchanged since rev 1.

Files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\notes\handover-q01.md (stale)
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\questions\q01.md
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-v2-50f506ffa773a20f026c1af48472b2d9ecdf23b879bd482205ccf3ed32c33219\results\platform-form-reasoning-check-rev3.png
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\notes\helpers\form_check_v2.py

I wrote no files. Nothing here is a platform pass.
