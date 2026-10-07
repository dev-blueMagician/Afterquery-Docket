# q05 rev 3 independent review (question-review, fresh context), completed 2026-10-06 (agent a23093fe9cc9b30af)

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns, the rev 2 review and the
platform context only. Pasted unabridged.

q05 (rev 3; tested_sha256: 6259dd6661f380230636bc2b2669179ad9f54a20ceeee5c046f3750787f255bc)

**gold_verified: yes.** I recomputed it by script from the source passages, not from the author's sums.
- **Twelve-month ROCE earnings = 22,247 by four independent routes:**
  - 13,581 (D10 l.405) − 6,469 + 15,135 (D12 l.389).
  - The four quarters: 3,942 (D09 l.372) + 3,170 (D10) + 2,603 (D11 l.379) + 12,532 (D12).
  - The components: 20,591 + 374 + 1,282.
  - D09's nine-month 10,411 − 6,469 + 3,170 + 15,135.
- **Capital employed at June 30, 2025:** 176,725 from D08 l.358-360. Working back from printed averages gives 176,725 or 176,726 (via D12's 177,212 with D10's December 2024 balance, D09's 206,935, or D08's 178,243 with D06's March 2025 balance).
- **Capital employed at June 30, 2026:** 232,633 from D12 l.352-354. Working back gives 232,633 or 232,634.
- **Result:** all combinations give 10.86916–10.86922%, so 10.87% every time.
- **The method is pinned.** The start-and-end average exactly reproduces the printed full-year averages for FY2025 (205,316), FY2024 (180,232, from 180,231.5) and FY2023 (183,173). A five-quarter-end average (200,852) and a mean of quarterly averages (199,737) do not.
- **Margin:** the answer flips only if earnings move by −8.6/+11.9 or capital by +79/−109.

**outcome: A: match; B: match.**
- Both solvers reproduce 22,247, 176,725 and 232,633, and both reject the 9.98 and 9.78 readings using the footnote.
- Each packet's question and all 25 corpus hashes match the snapshot.
- The read guard is bound to this run.
- Neither the answer nor the construction appears in auto-loaded memory or CLAUDE.md.
- That gives two uncontaminated matches.

**closed-book: misses.** It answered "unknown … mid-to-high single digits", with low confidence. That is not equivalent to 10.87%.

**necessity:**
- **D12 is indispensable.** It is the only source of Q2 and first-half 2026 ROCE earnings (12,532 / 15,135) and the June 30, 2026 balances. It is the latest release, so nothing later repeats them.
- **D10 is indispensable at two decimals.** A grep of all 12 documents finds 13,581, 3,170, Q4's noncontrolling interest (75) and Q4's after-tax interest (325) only in D10.
  - D11 repeats only Q4 2025 total earnings (2,770) and the Q4 ROCE (5.4%).
  - With Q4 average capital of 235,039 (D09 plus D11), the 5.4% bounds the result to 10.856–10.885%. That could be 10.86, 10.87 or 10.88.
- **D08, D09, D05, D06 and D11 can all be replaced.** The smallest valid set is {D10, D12}, which equals the documents field.
- **Caveat:** natural estimates without D10 still land on 10.87. Taking 5.4% at face value gives 10.8707%, and borrowing Q3's or Q1's add-backs gives 10.87. This route needs three or more other documents, so it is not a shortcut. It is not an ambiguity either, because D10's exact figures settle the answer.

**shortcut: clear.** I confirmed the auditor's shortest route (D10 + D12):
- 22,247 earnings.
- 2 × 177,212 − 177,698 = 176,726.
- (176,726 + 232,633) / 2 = 204,679.5.
- 10.8689%, which is 10.87%.

No passage prints a twelve-month ROCE; the only "trailing 12 months" figures are for CFFO (D11 l.368, D12 l.376). None of 10.87, 22,247, 204,679, 176,72x or 232,633 appears in the text. The overview gives only 8.3%, 4.5% and 21%. D07's "double-digit ROCE" is a target, not this figure. Search finds the inputs, not the answer.

**source_assessment: no gaps.**
- source_gaps is [], and its stored hash 4f53cda1… is sha256("[]"), which I recomputed.
- The capture says "12 of 12 captured in full".
- The bundle's corpus bytes match the snapshot.

**difficulty: easy (marginal, high risk of "Too easy").** This is local suitability only, not a measured tier.
- **For:**
  - No passage states the answer.
  - It applies a definition to a period no release reports.
  - At two decimals, about ten near-miss methods give wrong answers. Several use labelled figures in the documents:
    - D10's full-year average: 10.84.
    - D12's six-month average: 9.56.
    - The "Total debt plus total stockholders' equity" line, which leaves out noncontrolling interest: 11.05.
  - The figures are from 2026.
- **Against:**
  - The question points to the method, and its one-sentence footnote sits under every ROCE table. This matches aq-00949 q03 (a stated rule applied to labelled rows), which measured Low 5/5.
  - The rolling twelve months is a standard transformation.
  - There is no trap like the one in aq-00964 that a quick reader falls into.

**verdict: ready.** This is local only. Keep status `checked`; the platform result is pending.

**findings:**
1. **Gold and alternatives (Q4, Q9, Q11):** verified as above. Every wrong route listed in Lever checks recomputes as stated: 10.84, 9.56, 9.52, 9.78, 9.98, 10.06, 11.05, 10.85, 10.86 and 9.73. No choice between stated figures changes the answer.
2. **Per-step number rule (rev 3 change):**
   - Steps 2–7 and both calculation decoy lines now carry exactly one "=", with the result straight after it. This resolves the rev 2 advisory.
   - Under the documented rule (each number in a cited document or after "="), my emulation flags nothing in any of the 10 paragraphs.
   - Whole dates are printed in the cited documents: "December 31, 2024" in D10 l.322/535/539 and "June 30, 2026" in D12 l.304/341/515.
   - Steps 4, 6 and 7 re-expand earlier results from raw inputs instead of restating them. That avoids the restated-number flag.
   - **Platform-only, unknown:** if the form checks a step that names two documents against the first one only, it would flag inputs such as 6,469, 15,135 and 177,212. That behaviour has not been seen yet, and a cross-document calculation has no single-document home.
3. **Q14, platform-only, unknown:**
   - All 15 quotes match locally: 5 exactly, 10 only after tabs become spaces.
   - Two quotes (D10 l.405 and D12 l.389) are Markdown pipe rows. The ROCE-earnings inputs exist only in pipe rows, and the platform's blocking verbatim check on such rows has not been seen.
   - `notes/handover.md` l.5-10 already tells the user to re-copy them via Save passage.
   - Each necessary document still has quotes that are not pipe rows.
4. **Records:**
   - The report recomputes 6259dd… from the current file and corpus.
   - The A, B, closed-book and audit lines all carry rev 3 and this fingerprint, and they match the raw returns.
   - The rev 2 → rev 3 snapshot diff changes only Steps 2–7, the revision number and record sections. Question, answer, components, evidence, documents, tags, target and corpus are identical.
   - The front matter still says `draft`; the caller should set it to `checked`.
5. **Records note (outside the fingerprint):** the Necessity line in Lever checks says guesses from adjacent quarters give "10.87 or 10.88". Borrowing Q2 2026's add-backs actually gives 10.90, and the 5.4% bound spans 10.86–10.88. This is minor.
6. **Floor WARNs are explained:**
   - The origin "claude" is truthful; the export tool's user-only rule is an authorship matter outside this review.
   - Revisions 2 and 3 were form-safety edits made at review advisories, not retries of a failed question family.
7. **Q1–Q12 and rule 10 pass:**
   - 32 words, one ask, with the period and precision stated.
   - It asks about the world, not the document set.
   - The tags match work actually done, and the levers are active. No which-items decoy is needed.
8. **Q13:** there is no platform record, so the measurement is pending.
9. **Set:** q06 uses the same "Total debt" rows but asks for a list of quarters, so neither question gives the other away. q01–q04 are dropped.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q05.md
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r3-v2-6259dd6661f380230636bc2b2669179ad9f54a20ceeee5c046f3750787f255bc\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r3-v2-6259dd6661f380230636bc2b2669179ad9f54a20ceeee5c046f3750787f255bc\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\notes\handover.md
- D:\Dev\Docket\tasks\aq-00998\text\D10.txt, D12.txt (plus D08, D09 and D11 for the replacement tests)
- D:\Dev\Docket\AQ-00998_2026-10-06_0256.md
