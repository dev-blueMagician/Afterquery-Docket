# Independent review, q01 rev 0 (2026-10-08)

Role: question-review (fresh context; frozen fields, corpus, raw returns and floor output).
tested_sha256: b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea

Raw return (verbatim):

q01 (rev 0; tested_sha256: b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea)

**Verdict: revise.** The gold, both matches, the closed-book miss, the audit and the necessity checks all hold. The required fixes are claims in the failure-mode boxes. Those boxes sit outside the fingerprint, so the existing checks stay valid after the fix. Difficulty is Easy-leaning for a Medium target, and this set cannot use an Easy result.

**Record binding.** `docket_agent.py report` recomputes the same fingerprint from the current file. Source hashes match intake.json, and source_gaps is []. Solvers A and B, the closed-book run, the audit and both probes all carry this fingerprint. The probe packets in runs\q01-r0-alt-k3 are byte copies minus one document; only the renumbered header lines differ, and the question text is identical everywhere. There is no platform record yet.

**gold_verified: yes**
- Inputs:
  - Doc 7 l.63-64: the $100 automatic payment goes to the No Bankruptcy Group only.
  - Doc 7 l.66 and l.73: each payment is the member's points over all claimants' points, with 3 points against 1.
  - Doc 7 footnotes 2-3: both groups are defined by Jaffe's April 22, 2025 report.
  - Doc 6 l.47: the Thomson Reuters re-run eliminated 920 and left a list of 57,233.
  - Doc 6 l.49 gives 20,891 and l.61 gives 36,317.
- Exact-decimal script: 62,673 / 98,990 = 63.31246%, which is 63.3 under both half-up and half-even rounding.
- Every other stated-figure route also gives 63.3: 57,233 − 20,891 → 63.297; 57,233 − 36,317 → 63.340; the fund residual of 20,900 → 63.32.
- Wrong routes:

| Route | Result |
| --- | --- |
| March split | 64.962 (65.0) |
| 920 removed from the no-record group | 64.0 |
| 920 removed from the aged group | 65.5 |
| Reserve-derived 21,000 with 36,317 | 63.433 |
| Reserve-derived 21,000 with 57,233 − 21,000 | 63.487 |
| June 2022 sample | 72.3 |
| Head count | 36.5 |
| $1,000/$350 weights | 62.2 |
| Reversed points | 16.1 |

- Margin: the answer only changes if the no-record count moves by +34 or −57, or the aged count by +98 or −59. The 25-member gap (57,233 vs 57,208) and the two test records stay inside that margin in any allocation.

**outcome: A: match; B: match.** Both answered 63.3% with high confidence from D03 + D07. Both rejected the March split and the reserve readings on document grounds. Neither saw answer content (git-status file names only).

**closed-book: misses.** It answered 22.6% by recalling a different case (Ramirez). Its context held file names only.

**necessity**
- Doc 7 alone holds the payment terms: which group gets the automatic payment, the 3:1 points, the pro-rata formula and the April-report definitions. The bundle's only other settlement (Clark, Doc 4) has no money terms and no preliminary approval.
- Doc 6 alone holds 20,891 and 36,317. Doc 5 lists the April report as an exhibit with no counts. Doc 4 has only the June 2022 sample and projections built from it. Doc 7's reserve or fund residual gives only about 21,000 / 20,900 no-record members and no aged count.
- Removal probes: both unforced answers were "not answerable". Forced guesses were 36.5% and 72.3%, both off the gold.
- No smaller source set and no alternative pair exist.

**shortcut: clear.** The shortest route is Doc 7's terms and footnotes, then Doc 6 l.47/49/61, then one weighted share. No passage or overview states the share, a point total or the April split. Doc 6's overview (capture l.70) prints 57,233 beside the March split only, which exposes the decoy, not the answer.

**source_assessment:** not applicable. The capture is complete with no gaps.

**difficulty: easy, marginal toward medium** (local suitability only).

**failure_modes**
- **Mode 1 (Superseded date or version / Uses the wrong period or date):** real. Doc 6 l.47 sets it and the wording doesn't rule it out. 65.0% is recomputed correctly, the labels fit, and the boxes total 233 words. Two overclaims in "Where the trap sits":
  - "Nearly word for word": Doc 6 paraphrases footnotes 2-3, it does not repeat them.
  - "The first place in the bundle where both group sizes appear together": the March counts are not the group sizes, and Doc 4 prints a 270/311 pair for the same two categories earlier in bundle order.
- **Mode 2 (Linking across documents / Rounding, scale or sign):** the trap exists, it isn't ruled out by the wording, 63.4 and 63.5 are correct, and the boxes total 235 words. Three problems:
  - The story contradicts itself: a solver who "does not match" the groups to Doc 6 is then given Doc 6's 36,317, which needs exactly that matching. The consistent route is 57,233 − 21,000 → 63.5%.
  - "The figure the court rounds to $2.1 million" is unsupported. Doc 7 cites the settlement agreement for the reserve, so only consistency is shown.
  - No run gave it as an answer; it appeared only as a rejected reading.

**findings**
1. **Q15 (failure-mode boxes, outside the fingerprint):** fix the three overclaims and declare 63.5% as mode 2's wrong answer, or withdraw mode 2. No re-test is needed.
2. **Form numbers rule (Reasoning Steps 4-6):** these uncited steps produce values printed in no document (62,673, 98,990, 63.3%). The memory note on form checks records the form flagging this pattern ("Which document says…? Add 'Doc N'"), though the rule is unconfirmed. Naming the source documents in those steps is the recorded fix. That edit is inside the fingerprint, so it means rev 1 and fresh checks; otherwise accept the advisory risk.
3. **Evidence (minor, inside the fingerprint):** two facts the reasoning relies on are unquoted: Doc 7 l.64 ("Members of the Aged Bankruptcy Group will not receive these automatic payments.") and footnote 3.
4. **Lever checks (local notes only):**
   - "No second distribution or cy pres arises" isn't established, since unused fee/expense caps and the ~$10,900 automatic-reserve surplus could fund one. It doesn't affect the asked pool.
   - "D05's only split" overlooks Doc 4's projected 2020/2021 splits.
5. **Premise:** opt-outs after the May 2025 notice are reported nowhere. Because the groups are defined by the April 22, 2025 report, the April counts are the documents' only answer. Low risk, no action.
6. **Origin WARN:** the warning is accurate (origin claude). The user-only export and the form's "I wrote this myself" tick remain the user's decision.

**Platform risks**
- **"Too vague" block:** about 10% that both form solvers agree on 65.0%, higher if they see the overview. Under 3% for 63.4%, which needs 36,317 found without the earlier 20,891.
- **"Answer matches a stated figure":** no document states the share. A false positive keyed on "$2,882,000.00" or "30 percent of the total fund" is possible; it is advisory only.
- **Document check:** under 5% risk. Neither document can be replaced from the bundle or recalled.
- **"Answer not supported":** about 3-5%. Local solvers (3 of 3) cleared the March split.
- **Original question:** the closest of 80 workspace questions has a token ratio of 0.276 and a longest shared run of 5 tokens. The platform-wide comparison is unknown.
- **Restricted names:** unknown, as the list is not captured.

**Tier estimate** (my judgment, not a measurement)

| Outcome | Estimate |
| --- | --- |
| Too easy | ~20% |
| Easy | ~45-50% |
| Medium | ~15% |
| Between levels (Low 0/5, Medium 4-5/5; gate fails) | ~10% |
| High | ~2% |
| Too hard / Answer not supported | ~5% |

A usable result (Medium or High) is about 15-20% likely.

- **Mechanism family:** an older same-document input pair, worded like the group definitions, with the governing version named only in another document's footnotes. It sits between the tied same-document trap that measured Easy (aq-00745 q01, Low 1/5) and the current-looking decoys that reached Medium (aq-00964 q01, aq-01322 q01, aq-01278 q02). A decoy that visibly predates the governing version measured Too easy (aq-00998 q03).
- **What raises the odds of Low 0/5:**
  - The March pair comes first, both counts in one sentence.
  - The overview places it beside the April total.
  - The question names no report, vendor or group.
  - The deciding date sits in Doc 7's footnotes.
  - The April counts appear as Trans Union's expert samples, without group names.
  - Several other miss routes exist (72.3, 36.5, 62.2, 64.0, 65.5).
- **What lowers it (and pushes Medium toward 4-5/5):**
  - The supersession is stated in the very next sentences.
  - 20,891's own description says "PACER or Thomson Reuters".
  - 22,212 + 35,941 ≠ 57,233.
  - The $2.1M reserve fits 20,891, not 22,212.
  - After that, only one weighted share remains.

**Wording change:** I found none that raises the Medium odds without a fairness cost.
- Describing the group by its records matches both splits, which raises the vague-answer risk.
- Asking for the aged group's share follows the same path.
- A whole-percent answer lets the reserve routes land on the gold.
- A dollar answer rests on "Approximately" figures.
- Asking for total points drops a step.

Run a quick test (0 of 10 used) before spending a difficulty run (8 left). If the low model solves it, Easy is the best possible result, and this set cannot use it.

Files:
- D:\Agents\Docket\tasks\aq-01541\questions\q01.md
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-v2-b71780908eaf49fd31c0951ed3ff123922ded0fc3cd65eec45e8d4768993a9ea\results\
- D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\
- D:\Agents\Docket\AQ-01541_2026-10-07_0358.txt (overview, lines 65-77)
