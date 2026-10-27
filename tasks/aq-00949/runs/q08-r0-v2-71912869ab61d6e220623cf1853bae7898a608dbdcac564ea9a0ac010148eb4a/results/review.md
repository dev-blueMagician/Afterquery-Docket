role: question-review (fresh Agent subagent, question-review role)
received: 2026-10-08
input: workspace root, slug, question id, revision 0, tested_sha256, target medium (with the user's no-Easy-slot instruction), frozen question file, snapshot, corpus paths and the six raw returns in this folder; no writer conversation
tested_sha256: 71912869ab61d6e220623cf1853bae7898a608dbdcac564ea9a0ac010148eb4a
agent: abd5399608e1707d6 | tool_uses: 69 | duration_ms: 1515607

--- raw return (verbatim as received; harness indent removed) ---

q08 (rev 0; tested_sha256: 71912869ab61d6e220623cf1853bae7898a608dbdcac564ea9a0ac010148eb4a)

**Verdict: revise.** The question is fair and correct: the gold checks out, both blind solves match, the closed-book run misses and no shortcut exists. The open problem is the target. My local estimate is Easy, and this bundle has no Easy slot.

gold_verified: yes. I recomputed it with exact fractions from the originals.
- D01 (L155-189), December 31, 2019: equity 21,641; net debt 3,147 (= 5,175 - 2,028); total capitalization 24,788. That gives r = 12.69566%.
- D07 (L829-838; equity also on the balance sheet at L231), June 30, 2026: equity 31,864; net debt 3,019 (= 7,926 - 4,907).
- Required net debt N = 31,864 × 3,147 / 21,641 = 4,633.6125. The addition is 1,614.6125, which rounds to 1,615. It sits 0.11 above the 1,614.5 rounding boundary. Check: 4,633.61 / 36,497.61 = r.
- The answer holds under other readings. Matching the 2019 net-debt-to-equity proportion gives the same N. Whether the extra net debt comes from borrowing or from spending cash makes no difference.
- Every alternative gives a different number:
  - printed 13% → 1,742
  - ratio rounded early to 12.7% → 1,616
  - proportion rounded early to 0.1454 → 1,614
  - total capitalization held fixed → 1,410
  - 13% × printed total capitalization → 1,516
  - GAAP total capitalization → 2,033
  - March 31, 2026 column → 413
  - June 30, 2025 column → 5,232
  - total instead of the addition → 4,634
  - measuring "additional" from 2019's net debt → 1,487 (not a natural reading)

outcome: A: match; B: match.
- Both were fresh runs with distinct agent ids.
- Their packets hash-match the snapshot corpus and question.txt.
- Both computed 31,864 × 3,147 / 21,641 - 3,019 from D01 and D07, and both rejected the 13%, 12.7% and total readings using the question's wording.
- The git status they could see showed file names only, so neither is contaminated. Two matches validate the gold.

closed-book: misses. It answered "unknown". It recalled the 2019 inputs exactly (3,147; 21,641; 0.14542) and stated the formula, but it had no June 30, 2026 figures, which come after its cutoff. Its "contaminated: yes" refers to git-status file names, which cannot supply those inputs, so the miss stands.

necessity: the smallest valid set is {D01, D07}, and nothing smaller works.
- D01 is the only source of the December 31, 2019 net debt and equity. "2019" occurs only in D01. The D02-D06 tables start at March 31, 2024, and D03 has no balance figures.
- D07 is the only source of the June 30, 2026 figures. D06 ends at March 31, 2026.
- Substitution search: I tried all 34 percentages printed in D02-D07 and 9 equity/net-debt column pairs, each with both the correct algebra and the fixed-total-capitalization algebra. None gives 1,615. The nearest is 12.7% (D07's June 2025 GAAP ratio), which gives 1,616.
- Probe without D01: unforced "not answerable"; forced guess 1,615 at p 0.5 (p 0.6 at the sketch stage), from recall. This is a stated risk.
- Probe without D07: unforced "not answerable"; forced guess 5,232 at p 0.03. A miss.

shortcut: clear.
- I confirmed the shortest route: D01's net debt table plus D07's June 30, 2026 column, then N = equity 2026 × net debt 2019 / equity 2019, minus 3,019.
- 1,615, 1,614, 4,633 and 4,634 appear in no document. 1,410 appears only as 1,410.4 MBoed.
- The capture overview shows only Doc 1's rounded ratios and Doc 7's cash.
- Searching finds the inputs, not the answer. That is a difficulty risk, not a Guide violation.

source_assessment: no gaps (source_gaps [], 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945). intake.json shows 7 of 7 documents complete and matching the capture. D02 and D04-D07 are supplemental-table exhibits with no narrative pages. That is the platform's own document content (0 gap characters), and no premise, input, exclusion or alternative depends on narrative text.

difficulty: easy. This is local suitability for the Medium target, not an observed tier.
- The wording closes every wrong route it could open. "Computed from ... net debt and stockholders' equity" rules out 13%. "Rounding only the final result" rules out 12.7%. "Additional" rules out the total.
- That leaves only the fixed-total-capitalization slip, and no local reader made it. That covers solvers A and B, the audit, the sketch fairness solve, both closed-book formula statements and the probes.
- One "Net Debt" search reaches both tables, and the algebra is textbook.
- Bundle calibration: q04 rev 5 used the same D01/D07 tables and measured Low 5/5, Too easy, even with a 0.0036 rounding margin. Nothing in this bundle has reached Medium.
- Rough local guess: Too easy about 45%, Easy about 40%, Medium 10% or less. A Low 0/5 result would most likely become "Between levels" rather than a Medium pass.
- The risk that the platform flags Doc 1 as not needed is separate and moderate.

failure_modes: one mode declared, Figure that must be computed / Misapplies a rule or premise.
- The trap is real. D07 L838 prints 34,883. I recomputed 34,883 × 3,147 / 24,788 = 4,428.63, minus 3,019 = 1,409.63, giving $1,410 million. The shortcut leaves the ratio at 4,428.6 / 36,292.6 = 12.20%.
- Every arithmetic claim and row position in the boxes is true. 34,883 is two rows below net debt.
- The label fits acceptably; "Unit or basis" is the alternative. The cause fits. No trap repeats. The boxes total 247 words (177 containing a letter).
- Weaknesses:
  - No local check took this route.
  - It is borderline under "nothing the wording already rules out": the question names equity as the held quantity, and the auditor called this route "contradicts 'holding equity'".
  - "Sits beside the ratio" is loose. The row is two rows above the 8.7% row, with the GAAP ratio row in between.
- Correctly not declared: the 13%, 12.7% and total routes, which the wording excludes.

findings:
1. Target suitability (gate Q13 and final readiness). This is Easy for a Medium target, per the evidence above. An Easy result has no slot, and the archive README records 4 of 8 runs left. Required next step: a quick test against the platform's easier solver before any difficulty run (the 2026-10-06 capture shows 2 of 10 quick tests used). If the low model solves it, retire this design for the Medium slot. Do not loosen the fairness pins to manufacture difficulty.
2. Q2, recall of Doc 1. The local model recalled 21,641 and 3,147 in every run, and the platform's high model filled gaps from memory on q07. Every D01 fact is public and from before the cutoff, so no fair fix exists. State this risk at hand-over. The only precedent without a flag is q04 rev 2, which the user reported as a pass.
3. Records. The Lever checks Necessity bullet still says "Final probes at the prepared fingerprint: pending", but both probes are recorded under Blind solve. Update it; it sits outside the fingerprint.
4. Form, platform-only and unknown.
   - Steps 4-5 carry derived operands (0.1454184; 4,633.61) in steps citing Doc 1 and Doc 7. The q05 rev 0 precedent accepted this pattern.
   - Step 5 writes "= 1,615" for 1,614.61. That is consistent with the no-restatement rule.
   - The evidence quotes join D01's blank-line-separated cells and use pipe-free D07 rows. Both forms passed the platform's verbatim check on q04 rev 2.
   - The thousands comma in the answer has precedent (aq-00964 q01).
5. There is no "## Necessary documents" section, so both documents default to Answer component. That matches how each is used.
6. Set. q09 reuses D07's 3,019 cell and the closing phrase "Answer in millions of dollars" (similarity 0.29, longest shared run 5 tokens). Neither question gives the other's answer away. Both pair a recallable pre-cutoff document with D07's net-debt table, and both had their gold forced from memory in a removal probe, so the set concentrates one risk. Archived q04/q05 used the same D01 table, so a sibling advisory is possible if either is still on the form.
7. Low risks:
   - "Additional" has an implicit baseline, but every local reader took June 30, 2026's 3,019.
   - The stated-figure matcher may produce a false-positive advisory on "net debt".
   - The question runs 53 words (advisory only).
   - The floor's points-or-percent WARN is a false positive.

Not verified: platform-only checks (restricted names, original-question check, token window), subagent isolation beyond what the records show, and any platform tier.

Files:
- d:\Agents\Docket\tasks\aq-00949\questions\q08.md
- d:\Agents\Docket\tasks\aq-00949\runs\q08-r0-v2-71912869ab61d6e220623cf1853bae7898a608dbdcac564ea9a0ac010148eb4a\snapshot.json
- d:\Agents\Docket\tasks\aq-00949\runs\q08-r0-v2-71912869ab61d6e220623cf1853bae7898a608dbdcac564ea9a0ac010148eb4a\results\
- d:\Agents\Docket\tasks\aq-00949\text\D01.txt
- d:\Agents\Docket\tasks\aq-00949\text\D07.txt
