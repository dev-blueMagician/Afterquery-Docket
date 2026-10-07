# q02 rev 0 - independent review (raw, verbatim)

- Date: 2026-10-06. Fresh question-review agent (claude-opus-5-5), given the frozen fields, corpus,
  raw returns and target, without the writer's conversation; asked for a thorough, adversarial final
  check before a single submission attempt. Copied verbatim from the task notification.
- tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747

## Return

I recomputed q02 from the original passages, tried to replace each listed document using the rest of the bundle, and checked the records. The gold of $132 million holds and the question is fair. My verdict is still revise, because the only open item is the Medium target: Easy is the most likely platform result.

**q02 (rev 0; tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747)**

**gold_verified: yes.** I rebuilt it by script from text/ and checked the quotes against docs/ and the platform capture.
- **Estimate:** Doc 11 (D11) l.39 gives $350–$550 million, so the midpoint is 450.
- **2025:** D09 gives programme charges of 13 for Q4 (l.491) and 13 for the full year (l.495) in operating profit, and the same 13 before income taxes (l.703, l.865). D08 l.450 shows none through September 2025.
- **2026:** Q1 is 176 pretax (D11 l.548, which is 171 + 5). Q2 is 129 (D12 l.656). The first half is 305 (D12 l.800), which equals 300 + 5 (l.742, l.760) and also 176 + 129.
- **Cross-checks:** 1,842 + 305 = 2,147; 892 + 176 = 1,068; 950 + 129 = 1,079; 3,059 + 919 + 65 + 13 + 9 = 4,065. The cost-line splits also add up (2 + 13 + 285 = 300; 6 + 165 = 171; 2 + 7 + 120 = 129).
- **Result:** 450 − (13 + 305) = **132**.
- **Wrong routes:** 137 (operating-profit basis), 145 (2026 only), 150 (both errors), 261 (through Q1 only), −68 or −63 (original estimate).

**outcome: A: match; B: match.** Both were fresh, separate packets with byte-identical question text (question.txt sha e9e84a89…), and both packets hash-match the snapshot. Both used D09, D11 and D12 and rejected 137 because the question and the estimate say "pretax". Neither was contaminated.

**closed-book: misses.** It answered "about $100 million" at low confidence, worked out from the original $200–300 million range. That is not a near-equivalent, and it showed no memory of the expanded estimate.

**necessity:**
- **D11** is the only place the $350–550 million estimate appears. Only D07 and D11 contain any estimate wording, and D12 has none. Without D11 the result is −68 or not determinable.
- **D09** is the only source of the 2025 charge of 13. D11 and D12 compare only against Q1, Q2 and the first half of 2025, and D10's Corporate line is not split out. Without D09 the result is 145 or an estimate.
- **D12** is the only source of Q2 (129) and the first-half total (305). Without it the result is 261, as of March 31.
- No smaller set works. D07 and D08 are not needed, because D09's equal Q4 and full-year figures show nothing was charged before Q4.

**shortcut: clear.** The auditor's route (D11 l.39 → D09 l.495/865 → D12 l.800) checks out. No document prints a programme-to-date total, a remaining amount, 318 or 132 in this context (132 appears only at D09 l.420 and D10 l.142; 318 only at D10 l.223). The bundle overview prints only D07's original range and the word "expanded" for Doc 11. The 13 is found by searching the programme name, but that finds one input, not the whole answer.

**source_assessment:** No gaps. The source-gap list is empty (its hash is sha256 of "[]"), the capture holds all 12 documents in full, intake shows every document complete, and the live corpus and all three packets equal the snapshot hashes. The live question file recomputes to the same fingerprint (0a386408…) and form hash (7ddaa358…).

**difficulty: easy.** This is local suitability only, and Medium is not well supported (finding 8).

**verdict: revise.** There is no correctness or fairness defect. The open finding is target suitability, which matches how earlier Medium-target reviews in this workspace were recorded (trial-01 q03). No fair wording change would raise the difficulty: "pretax", "cumulative" and "latest" are each needed for a single answer.

**findings:**

1. **One defensible answer (ask 1).** 137 does not hold up.
   - D12 l.461's $300 is only the charges inside Corporate operating profit. The question and D11 both say "cumulative pretax charges", and the pretax total in D12's Income Before Income Taxes column (l.800) includes the 5 shown at l.760.
   - The documents never give two figures for the same thing, which was the cause in trial-04 q03. So the risk of "answered inconsistently" is low, about 10%. It would come only from a reviewer reading the $300 sentence as "the charges".

2. **The 2025 figure (ask 1).** 13 is the only 2025 programme amount, and it is the same on both bases. Q4 equal to the full year (D09 l.491, l.495), D08 l.450, and the "—" comparatives in D11 and D12 together rule out anything before Q4 2025.

3. **Wording (ask 2).** "Latest" picks out D11 no matter when it is judged: D12 (July 31) does not update the estimate. "Had not yet been recorded" plainly means the midpoint minus the cumulative charges.

4. **Platform document check (ask 3).** I expect it to pass.
   - The three probes missed the gold (−68, about $50M or 145, and 261).
   - It still passes if the high model takes the operating-profit reading: removal then gives 150, −63 or 266, all different from 137.
   - Remaining risk is low: a model that remembers the May 1, 2026 expansion could manage without D11.
   - Record gap: the D09 probe is kept only as a summary, not verbatim. My own search confirms D09 is indispensable anyway.

5. **Form number check (ask 4).**
   - Every printed number sits in the document its step cites: "April 30, 2026", 350 and 550 in Doc 11; 13 and 2025 in Doc 9; 305, 300, 5 and "June 30, 2026" in Doc 12.
   - Step 3 uses 900, and Step 7 uses 450 and 318. None is printed in the cited documents, but each is an earlier "=" result. That pattern passed once (aq-00949 q05). The three-document citation in Step 7 has not been seen on the form yet.
   - Each calculation is a simple a-op-b, and the decoy line's 300 and 305 are in Doc 12.
   - The reasoning contains no quoted span from Doc 12. If "Derive the rest" is used, mark Doc 12 and attach its passage by hand.

6. **Evidence rows (ask 4).** All four quotes appear word for word in the text files, the originals and the capture. They are prose or tab rows, not pipe rows. The D09 row quote matches both the Q4 and full-year rows, which carry the same value. Save the passages from the page so the tabs are kept.

7. **Lever records (gate check Q11).**
   - "Same series, right edition" does nothing. The word "latest", D11's own "increased from" in the same sentence, and the negative −68 all rule out the old estimate.
   - The claim that 2025 is tied to the programme "only by a note" is wrong: D09 l.491, l.495 and l.172 name the programme directly.
   - These overstate the difficulty. Levers and lever checks are not part of the fingerprint, so correcting them needs no re-run.

8. **Difficulty (ask 5).**
   - The only live trap is the $300 operating-profit figure, with leaving out 2025 as a weaker second. The question's own words ("pretax", "cumulative") point straight at both.
   - The shape matches aq-00998 q05: a quantity no document reports, built from labelled pieces with near-miss values, which landed in Easy.
   - My estimate:
     - Easy about 50%.
     - Too easy about 25%.
     - Low 0/5 then Medium 4–5/5 (platform label unknown) 5–10%.
     - Medium about 10%.
     - High 5% or less.
     - Too hard under 3%.
     - That puts Medium or higher at roughly 15%.
   - q01 rev 2's review put Medium or higher at about 20%, but rev 2 cannot be submitted as is, because its pipe-row evidence needs a new revision and fresh checks.
   - **Which I would submit:** q02, if one has to go without further work. It is the only one of the two whose exact content is complete, its answer is a whole number with no rounding edge, and its evidence is clean. The 5-point Medium gap is smaller than the uncertainty in either estimate.
   - Before deciding, use the quick tests (0 of 10 used). Medium needs the low model to miss all five, so a quick-test solve rules a candidate out. A survival proves nothing.

9. **Anything else (ask 6).** I would not submit this as a Medium bet without a measurement.
   - The form's "I wrote this question myself" box (capture l.212) is the user's call, and must be answered truthfully for a question written by Claude.
   - Restricted names, originality and the platform result (gate check Q13) are unknown. I am not claiming any platform pass.
