# q05 rev 0 independent review (question-review, fresh context, 2026-10-05)

Verbatim return from the task notification.

q05 (rev 0; tested_sha256: b5701f231afc934da7f55929d882f4794383305f4cbf0cf9f6ec05e38d6aed29)

**gold_verified: yes.** I recomputed −0.3 from the original passages with an exact-fraction script.
- **Actual margin:** D07 12M25 reconciliation (l.563-565): 25,151 − 2,830 − 12,020 = 10,301. Divided by 44,328 (l.456) that is 23.2381%.
- **Difference:** 23.2381 − 23.5 = −0.2619, which rounds to −0.3. Rounding the margin first (to 23.2 or 23.24) gives the same result.
- **Other routes all give 10,301:**
  - GAAP operating earnings 8,053 + 1,824 + 112 + 312.
  - The four quarters: 2,178 + 2,551 + 2,610 + 2,962, with sales summing to 44,328.
  - D04's nine months (7,339) plus D07's Q4 (2,962).
  - Averaging the four quarterly margins also gives −0.3.
- **The unprinted margin is fair and well defined.** The documents link these lines: the statement of earnings defines Operating Earnings, and the reconciliation adjusts it line by line. The same method reproduces every adjusted margin Abbott printed (1Q25 21.0, 2Q25 22.9, 3Q25 23.0), every GAAP margin (16.3, 18.4, 18.1) and the stated +130, +100 and +40 bp changes. This is not "numbers the documents never connect."
- **"Approximately 23.5%" gives one clear answer.** It is a single figure, and the question asks for a signed difference, so the figure is 23.5.

**outcome: A: match; B: match.** Both answered −0.3 with high confidence.
- Both rejected the earlier range (midpoint −0.5, top −0.8), the GAAP margin, and including other income. B also rejected reversing the subtraction.
- The packet text files are byte-identical to the corpus, and the packets hold only the question and documents.

**closed-book: misses.** It answered "+0.1 percentage points" at low confidence: wrong sign, not equivalent. It did recall the January 2025 range, so the outlook half of the question is general knowledge.

**necessity:**
- **D07 cannot be replaced.** It is the only source of the full-year adjusted lines (l.563-565) and the Q4 lines (l.521-523). Without it, D04's nine months give −1.2, and D08/D10 repeat only full-year sales and 1Q25/2Q25/first-half figures.
- **D03 is needed for a single answer.** Only l.349 gives "approximately 23.5%"; "operating margin" appears nowhere outside D01-D04. Without D03, D02's 23.5%–24.0% range is the latest outlook (D04 l.339 says nothing on margin), so "the figure" is undefined: −0.5, −0.8 or −0.3.
- No smaller set works. D01, D02 and D04 are correctly left unlisted.

**shortcut: clear.** I verified the auditor's route: D03 l.349 + D07 l.563-565 and l.456. No passage, footnote, table or overview prints the full-year 2025 adjusted margin or the gap. Searching for 23.2 finds only D04's Diabetes Care growth-rate cells; 23.24 and 10,301 find nothing. The overview gives only "$44.3 billion" for Doc 7.

**source_assessment:** Not applicable; there are no gaps. Prepare reported `source_gaps []`, intake shows all 11 documents complete, and the capture hash (49dc4016…) matches intake.

**difficulty: easy (marginal).** This is local suitability only.
- **What makes it work:** the margin has no labelled line and must be built. Labelled lines invite wrong answers: GAAP "Operating Earnings" gives −5.3 and adjusted pre-tax earnings gives +0.8.
- **Risk of "too easy":** high. The path is two documents and standard arithmetic, "most recent" points straight at the edition check, and the low end of the old range coincides with the gold. Both local solvers and the auditor matched with high confidence.

**verdict: ready** (local only). The caller should keep status `checked` until a platform pass on this exact content.

**findings:**
1. **One clear answer – record error (Lever checks, "Precision/readings").**
   - "Every input to the actual has one printed value" is false. D07 l.25 (and the overview) print "$44.3 billion". With that denominator, 10,301 / 44,300 = 23.2528%, giving −0.2472, which rounds to −0.2.
   - The gold sits only 0.012 pp from the rounding boundary. Slack is $5.3M in the numerator or $22.6M in the denominator.
   - I resolved this for the gold: $44.3B is a headline rounding. The same sentence's footnote 2 (l.377) gives $44.328 billion, and l.456 gives 44,328 in the numerator's units. Under the precision note it is visibly approximate, so the exact route governs.
   - Add a "One clear answer" line listing this route. Lever checks is not part of the fingerprint, so no re-test is needed. If the platform returns "answered inconsistently," this is the likely cause.
2. **Edition lever is only partly active (Q11 and Q2).** The low end of the D01/D02 range equals D03's figure. A reader who uses the old range's low end, or reports the shortfall below the range, lands on the gold. The lever only catches readers who use the midpoint or top. The author already discloses this; keep the lever described as partial.
3. **Pipe-table quotes and the platform's verbatim check (D07 l.563-565).** Status: unknown, at risk.
   - On aq-00949, the platform's form quoted a row the capture shows as a pipe table as "Other International (C) - - - - - - - 4 1": no pipes, hyphens instead of em dashes. So the pipe-format quotes probably won't match the platform's text, and this check blocks submission.
   - **No other text gives these inputs:**
     - The adjusted gross margin, R&D and SG&A rows exist only as pipe tables.
     - The GAAP route needs 8,053 (l.462) and the specified items (l.563-565 or l.775-777), also pipe rows.
     - The l.572 prose ($614M) includes the $48M non-operating item, so it can't isolate the operating adjustments.
     - The non-pipe adjusted pre-tax figure (10,762, l.649) needs interest (185, l.463) and adjusted other income (596, l.566), both pipe rows.
   - D07 is still cited by non-pipe quotes (l.377, l.553, l.557), so the "necessary documents cited" check should still pass.
   - If the form rejects the three rows, re-copy them from the platform page. That changes the Evidence field, so prepare must be re-run and the records re-bound. The question, answer and documents would not change.
4. **Advisory: D01 and D04 quotes.** They support no input to −0.3 (one is the decoy, the other shows an absence). The "Evidence supports its component" check may flag them. Optional for a later revision.
5. **Record error (Lever checks, overview probe).** Doc 1's overview does mention "operating margin" in its guidance description (capture l.33), though with no figure. There is no exposure; correct the note.
6. **Wording: "differ from … Give the sign."** It reads as actual minus outlook, and both solvers agreed. Low risk. Tighten in a new revision only if the form flags the direction.
7. **General knowledge.** The outlook is public. The actual was not recalled: two closed-book runs gave +0.2 and +0.1, both wrong sign. The platform model may still know the figure; this can't be tested locally.
8. **Set review.** This is the third guidance-versus-actual question (with q01 and q02), and it uses the same lever pair as q01. There are no mutual giveaways, only mild wording reuse ("Abbott's full-year 202X adjusted", "Give the sign"). Vary the question families in further work.
9. **Records and fingerprint.** `report` recomputes b5701f23… from the current fields. Blind A/B, closed-book and the audit all record rev 0 with that hash. There is no platform record.

Files: D:\Dev\Docket\tasks\aq-00745\questions\q05.md, D:\Dev\Docket\tasks\aq-00745\text\D07.txt, D:\Dev\Docket\tasks\aq-00745\text\D03.txt, D:\Dev\Docket\tasks\aq-00949\runs\q01-r1-v2-f3e58066a5d923c72210b05827944b7fe6138f52c5c2915b053cf4d68c161056\results\platform-form-feedback.md
