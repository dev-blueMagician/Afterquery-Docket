# q01 rev 0 independent review (question-review, fresh context), completed 2026-10-05

Dispatched with the frozen fields, corpus, fingerprint, target and raw returns only. Pasted unabridged.

q01 (rev 0; tested_sha256: b04d65a733139e6116d70c4bfc23d8fd02db1c81e1a63d81d2fa9938d72e109b)

gold_verified: yes. I recomputed it from the original passages:
- **Start of quarter:** D11 Attachment 2 gives net debt of 40,101 at March 31, 2026 (45,428 − 5,323 − 4).
- **End of quarter:** D12 Attachment 2 gives 28,545 at June 30, 2026 (37,075 − 8,527 − 3).
- **Change:** 28,545 − 40,101 = −11,556 ($ millions, "Millions of Dollars").
- **Cross-check:** both releases print the same December 31, 2025 value, 34,461. Half-year change −5,916 minus first-quarter change +5,640 = −11,556.
- **Quarter:** D12 l.54 says "During the quarter, Chevron signed a 20-year power purchase agreement with Microsoft", in the Q2 2026 release.
- The original files hold the same rows (docs/cvx_ex991_2026-05-01.txt l.354; docs/cvx_ex991_2026-07-31.txt l.52 and l.362). No rounding is involved, and no restatement exists.

outcome: A: match; B: match. Both answered −11,556 from D11 and D12 with high confidence. All four packets hold byte-identical question text (sha256 a84257bf…). Both solvers report no contamination and list only packet files. Each rejected −5,916, −8,353/−8,406 and +5,640 for stated, correct reasons. That gives two fresh matches at the current fingerprint.

closed-book: misses. It answered "about +3,000", guessing Q1 2026, with low confidence. The sign and the quarter are both wrong, so it is not equivalent. Its only extra context was the attached email and environment details.

necessity:
- **D12** is the only source of the signing quarter (l.54) and of the June 30, 2026 balance (l.364).
  - "Microsoft" appears only at D11 l.105 and D12 l.19, l.54 and l.103.
  - The other data-center mentions (D05 l.109, D06 l.81, D10 l.91 and l.129, and boilerplate in D06–D08) involve no Microsoft agreement.
  - Without D12, both the premise and the end balance are gone.
- **D11** is the only source of the March 31, 2026 net debt (l.356). D10 holds only December 31, 2025.
  - I tried four D12-only rebuilds. None is exact, and none matches even at one decimal in billions (gold −11.6):

| D12-only route | Result | In $ billions |
| --- | --- | --- |
| Second-quarter cash flows: (8,406) + 3,266 | −11,672 | −11.7 |
| December 31 balances plus first-quarter flows derived from the six-month columns: March 31 ≈ 40,072 | −11,527 | −11.5 |
| 1.3x × trailing cash flow derived for March 31 (31,264): March 31 ≈ 40,643 | −12,098 | −12.1 |
| Average capital employed | gives 234,799, which is capital employed, not net debt | — |

- No smaller document set works.

shortcut: clear. The verified shortest route is: search "Microsoft" → D12 l.54 (Q2 2026) → D12 l.364 (28,545) → D11 l.356 (40,101) → subtract.
- "11,556" appears nowhere in text/, docs/ or the capture.
- The task-page overview places the 20-year Microsoft agreement in Doc 12. It prints "$8.4 billion total debt reduction, 2Q 2026" (a decoy) and no net debt figure.
- Search finds the inputs, not the answer. That is a difficulty risk, not a Guide violation.

source_assessment: no known gaps.
- The report shows `source_gaps: []`. The gap hash 4f53cda1… equals the SHA-256 of an empty canonical list.
- intake.json records all 12 documents as complete, matching the capture, with hashes equal to the snapshot's.
- The capture says "12 of 12 captured in full". Its 349,777-character total is lower than the 370,920 in docs/ because the capture adds table markup. D07, which has no tables, nearly matches (12,491 vs 12,508).
- No gap-impact mapping is needed.

difficulty: easy (marginal). This is local suitability only, not a measured tier.
- **The path:** one plain bridge sentence, two labelled "Net debt" cells in adjacent releases, one subtraction.
- **Against the platform evidence in the calibration note:**
  - The low model solved labelled cells plus one standard step across two documents (trial-02 q01, trial-07 q05). This question has the same skeleton.
  - A one-sentence bridge "costs nothing to cross" (aq-00949 q02). "During the quarter" is one sentence, and the overview already names Doc 12.
  - An edition choice equal to the latest edition tests nothing (trial-03 q01). The signing quarter is the bundle's latest quarter, so guessing the most recent quarter reaches it without the bridge.
- **What resembles the one pass (aq-00964 q01):** the event is in the latest release, the start value sits in the previous edition, and the latest release prints tempting figures of its own.
- **Where it falls short of that pass:** aq-00964's decoy was a same-label figure for the asked quantity. D12's alternatives are a December 31 column that is plainly labelled, or a different measure.
- **Most likely wrong routes for a quick reader:**
  1. −5,916: subtracting D12's two Attachment 2 columns. This is the likeliest, because the bridge lands the reader in D12, which has no March 31 column.
  2. −8,400, −8,406 or −8,353: D12 l.93, "Total debt was reduced by a record $8.4 billion in the quarter". It is the only debt-change sentence tied to the quarter, and the overview repeats it.
  3. About −11,672 or −11,527: rebuilding from D12's flows alone.
  4. +5,640: taking D11's exclusivity agreement as the signing. This is weak.
- Overall the risk of a "too easy" verdict is high. The scatter/alignment trap is the only real defence.

verdict: ready. This is local readiness only. Status stays checked until a platform pass is recorded on this fingerprint.

findings:
1. **Q14, platform verbatim check (unknown).** The two quotes that carry the values, D12 l.364 and D11 l.356, use spaces where the source has tabs ("$\t28,545 $\t34,461"), and the capture shows the same tabs. They match only after whitespace is collapsed, which the floor does (check_questions.py l.70). The other four quotes match exactly. If the form's blocking "Verbatim evidence" check is whitespace-exact, those two quotes fail. Before submission, check them with Save passage on the platform page. Changing evidence means a new revision and fresh checks.
2. **Q11 lever "Mentions it vs does it".** It is active (D11 l.105 gives +5,640) but weak: the question's own "signed" and "20-year" rule it out on a plain read, and all three document-reading agents called it weak. Don't credit it as difficulty. The working lever is scatter (D12 alone gives −5,916).
3. **Difficulty risk (finding 3 of 7).** The path is three labelled lookups and one subtraction, and the bridge lands on the latest quarter. This is not a Guide violation; the platform has to measure it.
4. **Set review, q01 vs q02.** They share a shape: a dated-event bridge, then one subtraction across two releases, both ending on D12's Q2 2026 figures, with identical tags. Neither gives the other away (q02 names "second quarter of 2026" but not the Microsoft event). Where possible, vary the lever for other questions. The bundle supports, for example:
   - the definition changing between editions (D01–D03 leave out time deposits; D04–D06 include them; D08 onward renames the measure "Net debt");
   - D12's rounded "$8.4 billion" against the exact tables.
5. **Records.** The report recomputes the fingerprint as b04d65a7…, and all records are rev 0. However, docket-general-knowledge-check.md logs an "aq-00998 q01 rev 1" (a total-assets question, dropped) from the deleted workspace. That is different content under the same id; disambiguate it in the notes.
6. **Floor WARN on origin.** It is explained. `origin: claude` is accurate and must not be changed to get through the export tool.
7. **Platform-only checks, unknown.** No platform difficulty check has been run yet. Also unchecked:
   - the platform's "Needs the documents" check, run by models that may have later knowledge cutoffs;
   - restricted names and originality;
   - how the form reacts to Step 5 citing two documents.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q01.md
- D:\Dev\Docket\tasks\aq-00998\runs\q01-r0-v2-b04d65a733139e6116d70c4bfc23d8fd02db1c81e1a63d81d2fa9938d72e109b\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q01-r0-v2-b04d65a733139e6116d70c4bfc23d8fd02db1c81e1a63d81d2fa9938d72e109b\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D11.txt
- D:\Dev\Docket\tasks\aq-00998\text\D12.txt
- D:\Dev\Docket\tasks\aq-00998\notes\intake.json
- D:\Dev\Docket\.claude\memory\docket-general-knowledge-check.md
