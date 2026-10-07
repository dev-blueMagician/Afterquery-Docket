role: question-review (fresh Agent subagent, question-review role; frozen fields, corpus and raw returns; no writer conversation)
received: 2026-10-05
input: workspace root, slug aq-00949, q05, rev 0, tested_sha256, target medium, snapshot path, raw return paths, and two context notes (sibling q04 status; no source gaps)
tested_sha256: 6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d
tool_uses: 55 | duration_ms: 779132

--- raw return (verbatim as received) ---

q05 (rev 0; tested_sha256: 6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d)

**Binding.** `docket_agent.py report` recomputes this same fingerprint from the live question file and corpus. All snapshot corpus hashes match the live bundle and the solver-1, solver-2 and shortcut packets. The question text is byte-identical in all four packets, and all four raw returns carry this fingerprint. The floor shows 0 FAIL and 1 WARN (origin). Status is draft. No platform difficulty-check result exists for this content; the round-4 quick-test "Survived — worth writing up" (I checked the transcript against the PNG) is a screen, not a tier.

**gold_verified: yes**
- **Doc 1 (end-2019).** D01 L155-171 gives debt of 5,175 and "Less: Cash" of (2,028). Two printed figures confirm the reading: 5,175 − 2,028 = 3,147, the printed net debt, and 5,175 / 26,816 = 19%, the debt ratio the prose gives for "total debt".
- **Doc 7 (June 30, 2026).** D07 L829-835, first column, gives 7,926 and (4,907); 7,926 − 4,907 = 3,019 is printed. The balance sheet agrees: L186 cash 4,907, and L212 + L216 = 27 + 7,899 = 7,926. L320 defines the measure as "Long-Term Debt (including Current Portion…)".
- **Calculation (Decimal script).** 39.18841% → 61.91017%, a difference of 22.72176, which rounds to 22.7. That is 0.028 below the 22.75 boundary. Rounding the two ratios first to 1 or 2 decimals also gives 22.7.
- **Alternatives at one decimal.**

| Route | Result |
| --- | --- |
| Prose cash only | 23.3 |
| Prose debt only | 22.9 |
| Both prose figures | 23.4 |
| 2026 long-term debt only | 22.9 |
| Both prose figures plus long-term debt only | 23.7 |
| Doc 7 figures in billions | 22.8 / 23.6 |
| March 31, 2026 column | 9.3 |
| June 30, 2025 column | 83.9 |
| Relative change (ruled out by "percentage points") | 58.0% |
| Inverted ratio (contradicts "rise") | −93.7 |

- Both prose figures ("$5.2 billion", "$2.0 billion") are visibly rounded versions of figures the same release prints exactly. The exact route is therefore the one defensible answer.

**outcome: A: match; B: match.** Both were fresh, packet-only solves that reported they were not contaminated. Both read the same four cells, cross-checked them against the balance sheet, and rejected the prose (23.4), long-term-debt-only and relative-change readings for reasons the documents support. That gives two uncontaminated matches.

**closed-book: misses.** It answered "unknown" at low confidence, which is not equivalent to 22.7. It did recall the 2019 inputs exactly (2,028; 5,175; 39.2%), but no June 2026 cash figure.

**necessity:**
- **D01** holds the only 2019 values. "2019" occurs only in D01. The other tables start in 2021-2024, and D03 has only deal funding. Removing D01 leaves no printed or rounded substitute.
- **D07** is the only source for June 30, 2026. D06 ends at March 31, 2026, which gives 9.3. These figures are after the model cutoff and were not recalled.
- No smaller set and no alternative pair exist.
- **Recall caveat for D01.** Without D01, the gold needs a recalled 2019 ratio in (39.160, 39.260]. That means cash of about 2,027-2,031 if debt is 5,175, or debt of about 5,166-5,178 if cash is 2,028. The closed-book recall (39.2%) lands inside: 61.91 − 39.2 = 22.71. Recall at the "$2.0B/$5.2B" level gives 23.4 and misses.

**shortcut: clear.** I confirmed the auditor's route: two tables, two divisions and one subtraction.
- No document prints a cash-to-debt ratio or a 2019-2026 comparison.
- 39.19, 61.91 and 22.72 appear nowhere. "22.7" appears only inside unrelated NGL prices of 22.70.
- 5,175 also appears in D04-D07 as June 30, 2025 total current liabilities, which is unrelated.
- The capture overview (`D:\Dev\Docket\AQ-00949_2026-10-06_0251.md` L33, L93) shows only the decoy "$5.2 billion" and one input ($4,907M), not the answer.
- This is a difficulty risk, not a Guide violation.

**source_assessment:** No gaps. `source_gaps` is [] (hash 4f53cda1…), the intake records 7 of 7 documents complete, and the capture hash c0774ce9… matches. No impact mapping is needed.

**difficulty: easy.** This is local suitability only, and it is below the medium target.
- **Same lever already measured at Easy.** The only working trap is the same table-versus-rounded-prose check on the same D01 sentence. The platform measured that at Low 3/5 (Easy) in q04 rev 2.
- **The two traps are one decision.** Cash and debt sit in one prose sentence, so the errors are correlated. A solver that reaches the table for debt finds cash two rows below; one that stops at the prose uses both figures. That is one decision, not two traps.
- **No new obstacle on the Doc 7 side.** It has no prose, and its decoys (long-term debt only, the June 2025 column) were already present in q04.
- **The prose points to the exact figures.** D01's prose sends readers to "the attached tables".
- **Medium is unlikely.** Medium needs Low 0/5. If q04's two misses came from its now-fixed ratio-direction ambiguity rather than the prose, Low 4-5/5 ("Too easy") is also possible.
- **The quick test does not separate tiers.** "Survived" doesn't separate Easy from Medium; aq-00745 q01 survived and then placed Easy.
- **Past bias doesn't help here.** On numeric-lever questions, earlier local reviews were too pessimistic only about too-easy risk, not about the Easy/Medium boundary.

**verdict: revise**

**findings:**
1. **Gate summary.** Q1, Q3-Q10 and Q12 pass. Q2 passes locally, with the recall risk in finding 3. Q6 is supported: it is a cross-document join, and the Doc 7 tables carry both June 30, 2025 and June 30, 2026 columns. Q9 is supported: "as a percentage of its total debt" names the base, "rise" rules out the inverted ratio, the dates are exact and fiscal year equals calendar year. Q10: 29 words, one ask. Q13 is pending, with no platform pass. Q14 passes locally; its platform parts are unknown (findings 5-6).
2. **Q13 target fit (q05.md "Family and target").**
   - Evidence: the analysis under difficulty above.
   - Consequence: there is one Medium attempt, and an Easy placement would use it up without meeting the target.
   - Required: a design with an independent mechanism that a careless reader falls for. The workspace's only measured Medium pass used a later-dated decoy in the same document. Any redesign needs fresh solvers A and B, a closed-book run, an audit and a review on the new fingerprint.
3. **Q2 recall route (q05.md "Necessity").**
   - Evidence: `closed-book.md` and the ratio band above.
   - Consequence: the platform could show "A marked document may not be needed … document 1". q04's reported pass with the same D01 dependence is only indirect mitigation, because its document-check line was never seen.
   - Required: state this risk at hand-over. It cannot be removed while the 2019 endpoint is a public 10-K balance.
4. **Q11 lever record ("Selected-lever checks").** The table-versus-prose lever is active: every prose route differs at one decimal. "State the rounding" is not an independent lever. Rounding the ratios at 1-2 decimals gives 22.7. Only rounding the inputs (which is lever 1's route) or rounding to whole percents (62 − 39 = 23) changes the answer. At whole-number precision every prose route gives the gold 23. The record's "0.028 margin" note is not an early-rounding test. Correct the record; the levers field is outside the fingerprint, so no re-test is needed for that alone.
5. **Q14 reasoning step 3 (platform-only, unknown).**
   - Step 3 cites Doc 1 and Doc 7, but neither prints its inputs 61.91 or 39.19 (checked by search).
   - Under the recorded form rule, every number in a step that cites a document must appear in that document or come straight after "=". How the form treats derived inputs is unobserved, and an uncited step risks its own new result being flagged instead.
   - Check the reasoning box after pasting. Any change is a new revision.
6. **Verbatim evidence (platform-only).**
   - The D01 table quotes match only after joining line breaks. The D07 "… (b) 7,926" and "Less: Cash (4,907)" quotes match only with the table pipes removed.
   - They are likely to pass: the capture shows the platform renders table rows space-separated (capture L150), and q04 was submitted with the identical two debt quotes. The two "Less: Cash" quotes are unconfirmed.
   - Advisory: the D01 L41 quote supplies the decoy $5.2 billion, not a figure used in the answer. It is defensible because it ties "total debt" to the table line.
7. **Set review.** q05 repeats q04's documents, lever, D01 sentence, inputs 5,175 and 7,926, tags and phrasing. Neither answer gives the other away directly, but working q05 produces q04's inputs. Set diversity is low, and the sibling advisory may fire.
8. **Origin WARN.** `origin: claude` is accurate. The export restriction and the form's "I wrote this question myself" tick are the user's decision.

Files:
- `D:\Dev\Docket\tasks\aq-00949\questions\q05.md`
- `D:\Dev\Docket\tasks\aq-00949\runs\q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d\results\` (the four raw returns and the quick-test screen)
- `D:\Dev\Docket\tasks\aq-00949\text\D01.txt`
- `D:\Dev\Docket\tasks\aq-00949\text\D07.txt`
- `D:\Dev\Docket\tasks\aq-00949\questions\q04.md`
