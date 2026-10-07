# q05 rev 4 independent review (question-review, fresh context), completed 2026-10-06 (agent a5f897bcf9e575d0d)

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns, the rev 3 review, the platform
Run 2 transcription and the memory notes named in the prompt only. Pasted unabridged.

q05 (rev 4; tested_sha256: 17565b4d96691eac335d58c8b7083ad35a62698ea133c0f56e0da7701a3ad0bc)

**gold_verified: yes.** I recomputed it by script from the source passages.
- **Earnings:** the twelve-month ROCE earnings come to 22,247 by four separate routes:
  - 13,581 (D10 l.405) − 6,469 + 15,135 (D12 l.389)
  - the four quarters 3,942 (D09 l.372) + 3,170 + 2,603 (D11 l.379) + 12,532
  - the components 20,591 + 374 + 1,282
  - D09's nine months 10,411 − 6,469 + 3,170 + 15,135
- **June 30, 2025 capital employed:** 176,725 printed directly (D08 l.358-360). Working back from printed averages gives 176,726 or 176,725 (D12's 177,212 with the December 2024 balance; D09's 206,935; D08's 178,243 with D06).
- **June 30, 2026 capital employed:** 232,633 (D12 l.352-354), or 232,634 worked back.
- **Result:** every combination, including rounding extremes up to 176,727 and 232,635, gives 10.86911-10.86922%. That is 10.869 and nothing else.
- **Method is pinned:** the start-and-end average reproduces the printed full-year averages exactly for FY2025 (205,316) and FY2023 (183,173), and to rounding for FY2024 (180,231.5 vs 180,232). A five-point average (200,852) or a mean of quarterly averages (199,737) does not.

**outcome: A: match; B: match.**
- Both returned 10.869% by the exact route (22,247 / 176,725 / 232,633).
- They were distinct fresh agents. Each packet's question and all 25 corpus hashes match the snapshot.
- The answer does not appear in CLAUDE.md, MEMORY.md or the role files.

**closed-book: misses.** It answered "unknown", with a rough guess of 6–7% and low confidence. That is not equivalent to 10.869%.

**necessity:**
- **D12 is indispensable.** It is the only source of 2Q 2026 and first-half 2026 ROCE earnings and of the June 30, 2026 balances, and no later release repeats them.
- **D10 is indispensable at three decimals.** Searching all 12 documents finds Q4 noncontrolling interest (75), Q4 after-tax interest (325), 3,170, 13,581 and the FY2025 ROCE of 6.6% only in D10.
- **Every natural route without D10 misses 10.869:**
  - D11's rounded 5.4% taken at face value, with the Q4 average of 235,039 rebuilt from D09 and D11: **10.871**.
  - The same 5.4% with other Q4 averages: 10.856–10.885.
  - D11's Q4 earnings of 2,770 plus add-backs borrowed from other quarters: 10.866 (1Q26), 10.868 (mean of 3Q25 and 1Q26), 10.871 (3Q25), 10.878 (three-quarter mean), 10.899 (2Q26).
  - Every quarter at its printed ROCE: 10.866.
- **What hitting the gold would take:** a Q4 ROCE of 5.3925–5.3959%, or add-backs of 399–400. Only one contrived mix lands there: 2Q26 noncontrolling interest (142) plus a nine-month average interest (257) = 399.
- **Smallest valid set:** D08, D09, D05, D06 and D11 can all be replaced. {D10, D12} is the smallest valid set and equals the documents field.

**shortcut: clear.**
- I confirmed the auditor's route. No passage states a twelve-month ROCE; the only "trailing 12 months" figures are CFFO (D11 l.368, D12 l.376).
- None of 22,247, 204,679, 176,726, 10.86x or 10.869 is printed anywhere.
- The overview gives only 8.3%, 4.5% and 21%.

**source_assessment: no gaps.**
- source_gaps is [], and its hash 4f53cda1… equals sha256("[]").
- The capture says 12 of 12 documents captured in full.
- D10–D12 text differs from the originals only in trailing tabs and hyphen characters, never in a figure.

**difficulty: easy.** This is local suitability only, not an observed tier.
- **Measured evidence:** rev 3, with near-identical content, scored Low 2/5 (inside the 1–3 window) before failing the removal gate.
- **Expected effect of rev 4:** any answer correct at three decimals is also correct at two, so the set of right routes can only shrink. Expect Low at or below 2/5.
- **Risk:** Low 0/5 moves the check to Medium. What the platform does with Low 0/5 and Medium 4/5 or better is not documented.
- **For:** it applies a stated method to a period no release reports, and about a dozen near-miss methods go wrong at three decimals.
- **Against:** the method footnote sits under every ROCE table, and the rolling twelve months is a standard step.

**verdict: ready.** This is local only. Keep status `checked`; the platform result is pending.

**findings:**
1. **Removal test (Q2; the rest depends on the platform).**
   - If the platform grades strictly at the asked precision, Doc 10 is now needed.
   - But the face-value route (10.871) and the averaged add-backs (10.868) sit only 0.002 and 0.001 points from the gold. A grader with any absolute tolerance of 0.002 points or more would still count the answer as reached.
   - aq-docket-trial-04 q03 (−2.2 vs −2.3, "answered inconsistently") suggests strict grading, but tolerance at three decimals has not been observed.
   - **Required:** a new difficulty run on this fingerprint. If the flag persists, more decimals cannot fix it because the gap is absolute, so the quantity itself would have to change.
2. **One clear answer (Q4).** The rounded 5.4% creates no "answered inconsistently" risk while D10 is available.
   - D10 prints the exact input (3,170; 13,581) beside it.
   - 5.4% is a one-decimal ratio of a different quantity, not a second printed value of the same input.
   - The natural route (full year minus first half plus first half) never touches Q4.
   - Only rounding to billions part-way through (22.247 / 204.7 = 10.868) leaves the gold, and the stated precision makes that a solver error.
3. **Lever (Q11).**
   - "Exact table vs rounded prose" passes the guide's redo test: 5.4% gives 10.871, and FY 6.6% × 205,316 gives 10.854. In practice it mainly protects the removal test, and both blind solvers ignored the rounded figure. The 5.4% is a rounded table cell, not prose; that affects only the label.
   - All ten wrong routes listed in Lever checks reproduce at three decimals.
4. **Per-step number rule (form; unknown).**
   - My emulation flags nothing in any of the 11 paragraphs.
   - In the new decoy line, 3,942, 189,843, 41,544, 5,757, 152,318, 24,541 and 839 are in D09 (l.343-345, 372). The figures 5.4, 2,603 and 186,450 / 40,758 / 5,726 are in D11, and the rest are in D12.
   - **Unknown:** if the form checks only the first document a step names, Steps 2, 4, 6 and 7 and the new line (which names Doc 9 first) would be flagged.
   - **Unknown:** the nested-parenthesis question from aq-00949 q04 is still open, and the new line is the most complex expression in the reasoning (18 operands). Watch the form's reaction.
5. **Evidence (Q14; unknown).**
   - All 15 quotes pass the floor.
   - The two pipe-row quotes (D10 l.405, D12 l.389) are the only place the ROCE earnings rows appear. The handover tells the user to re-copy them with Save passage on the platform page.
   - Docs 9 and 11 rightly have no quotes because they are not marked necessary. The handover warns against Derive the rest marking them.
6. **Records.**
   - The report recomputes this fingerprint.
   - The A, B, closed-book and audit lines all carry rev 4 and this fingerprint, and they match the raw returns.
   - The report reads only the Blind solve section, so the audit's absence from it is by design.
   - **To fix:** set status to `checked`.
   - **To fix:** the Feedback log still says "none chosen yet" although rev 4 exists. Record whether the user chose option (b). Saving rev 4 on the form clears the reviewer-note option on version 35d6a9 and replaces its Low 2/5 result (6 of 8 runs left).
7. **Wording in Lever checks (outside the fingerprint):** "every route without D10 misses" holds for natural routes; the contrived 399 mix above is the one exception.
8. **Coverage:** the auditor and both solvers called D10 required without testing rounded-figure approximations. Finding 1 supplies that test.
9. **Q1–Q12 and rule 10 pass.**
   - 32 words, one ask, with the period and precision stated.
   - It asks about the world, not the document set, and the tags match the work.
   - Floor: 0 FAIL. Both WARNs are explained: the origin is truthful, and rev 4 answers platform evidence. Sibling q06 shares no answer path or hint.
10. **Q13:** there is no rev 4 platform record, so the measurement is pending.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q05.md
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r4-v2-17565b4d96691eac335d58c8b7083ad35a62698ea133c0f56e0da7701a3ad0bc\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r4-v2-17565b4d96691eac335d58c8b7083ad35a62698ea133c0f56e0da7701a3ad0bc\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r3-v2-6259dd6661f380230636bc2b2669179ad9f54a20ceeee5c046f3750787f255bc\results\platform-difficulty-check-run2.md
- D:\Dev\Docket\tasks\aq-00998\notes\handover.md
- D:\Dev\Docket\tasks\aq-00998\text\D10.txt, D11.txt, D12.txt (plus D08 and D09 for the replacement tests)
