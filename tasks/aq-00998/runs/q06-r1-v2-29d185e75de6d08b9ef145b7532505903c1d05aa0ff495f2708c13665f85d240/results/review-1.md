# q06 rev 1 independent review (question-review, fresh context), completed 2026-10-06 (agent ad875a46dd9025578)

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns, the rev 0 review and the
platform context only. Pasted unabridged.

q06 is locally ready for the Easy target. My own recompute confirms the gold, both blind solves match, the closed-book run misses, and the shortcut audit's "clear" holds. Two records need correcting: they understate how cheaply an approximate cash-flow route reaches the answer, and the closed-book run shows that half the answer can be recalled from memory. Neither is blocking. No platform result exists, so status stays checked.

**q06 (rev 1; tested_sha256: 29d185e75de6d08b9ef145b7532505903c1d05aa0ff495f2708c13665f85d240)**

**gold_verified:** yes. My own script parsed all eleven balance-sheet tables (D01–D06, D08–D12).
- Every net/adjusted debt figure equals total debt minus cash, time deposits and marketable securities.
- The December 31 values are identical in every release that prints them.
- Quarter-on-quarter changes, total debt / net debt ($M):

| Quarters | Changes | Result |
|---|---|---|
| 1Q24, 2Q24, 3Q24, 1Q25, 3Q25, 1Q26 | +999/+2,944; +1,349/+3,619; +2,657/+1,962; +5,140/+7,282; +12,077/+8,416; +4,670/+5,640 | out: total debt rose |
| 4Q24, 2Q26 | −1,300/−3,382; −8,353/−11,556 | out: both fell |
| **2Q25, 4Q25** | **−214/+363; −786/+644** | **qualify** |

- The set {2Q 2025, 4Q 2025} holds at $0.1B rounding and without time deposits.
- Other readings: comparing each release's two columns (quarter-end vs prior December) gives none; the debt and net-debt ratio rows give 4Q 2025 only; the debt-to-CFFO ratios (D10–D12) give none. The question's "previous quarter-end" and its amount definitions rule all three out. The cash-flow lines give the same set.
- No narrative states a competing balance. D12's "record $8.4 billion" matches the 8,353 drop.

**outcome:** A: match; B: match.
- Each ran in its own packet: question identical to the snapshot, 25 corpus files at snapshot hashes, no extra files.
- Both rebuilt net debt from its parts and gave equivalent forms. Agent IDs are distinct and neither was contaminated.

**closed-book:** misses.
- The committed answer is "2Q 2025" alone, which is not the two-item gold. It names 4Q 2025 only as "possible" and says it has no figures from 4Q 2025 on.
- The rev 0 run on the identical question text answered "1Q 2024 and 2Q 2025" (wrong).
- Exposure is moderate. Accurate recall of end-2024 debt and cash and of 2Q25 cash ($4.6B to $4.1B) put 2Q 2025 in both runs. Protection rests on the January–July 2026 releases: including 4Q 2025 and excluding 1Q and 2Q 2026.

**necessity:** Each non-December quarter-end balance appears only in its own release, in both text/ and docs/.
- **D02** (Mar 31, 2024: 21,835 / 15,557), for 1Q24 and 2Q24. **D03** (Jun 30, 2024: 23,184 / 19,176), for 2Q24 and 3Q24. **D04** (Sep 30, 2024: 25,841 / 21,138), for 3Q24 and 4Q24. For all three, the rest of the bundle offers only ratios (no equity for that date) and cash flows.
- **D06** (Mar 31, 2025: 29,681 / 25,038), for 1Q25 and 2Q25. The substitute ratio rises in 2Q25 even though debt fell.
- **D08** (Jun 30, 2025: 29,467 / 25,401), for 2Q25 and 3Q25. D12's year-ago average capital employed (178,243) plus D06 rebuilds only the equity + debt + noncontrolling-interest sum (176,725). Isolating total debt needs D08's noncontrolling interest and an unrounded ratio.
- **D09** (Sep 30, 2025: 41,544 / 33,817), for 3Q25 and 4Q25. Elsewhere only one-decimal debt-to-CFFO multiples (1.3x/1.1x), far too coarse.
- **D11** (Mar 31, 2026: 45,428 / 40,101), for 1Q26 and 2Q26. Without D11, D12's bullet alone shows debt was at least 37,075 + 8,350 = 45,425 > 40,758, so 1Q26 still drops out. D11's indispensable fact narrows to the March 31, 2026 net debt that decides 2Q26.
- **D12** (Jun 30, 2026: 37,075 / 28,545). No other document covers 2Q26.
- D01, D05 and D10 only repeat December balances, and D07 has none. No smaller set works on the defined balances.
- A smaller approximate set does exist: cash flows from just four releases, D08, D09, D10 and D12 (finding 1).

**shortcut:** clear.
- Shortest route: read the total-debt and net/adjusted-debt rows from the eight listed balance-sheet tables (December values from comparative columns), take ten consecutive differences, apply both conditions. This matches the auditor's route and my gold.
- No passage, highlights row or overview line states the pattern. The overview mentions only 2Q26's debt reduction, which is a decoy.
- The four-release cash-flow route approximates a different measure and still needs ten comparisons. It is a difficulty risk, not a Guide violation.

**source_assessment:** no gaps.
- The capture hash matches intake (9f6eab4d…), and all 12 documents are complete with zero gap characters.
- The empty gap list hashes to sha256("[]") = 4f53cda1….
- Live corpus, snapshot and all packets agree, and the report recomputes the same fingerprint from the live fields. No gap mapping is needed.

**difficulty:** easy (local suitability only, not measured).
- Where a solver can go wrong:
  - the 10-quarter, two-condition filter needs the previous quarter-end from the previous release; for seven quarters the printed column is the prior December, and that reading gives "none";
  - the label changes from "Adjusted debt" to "Net debt";
  - the ratio rows give 4Q 2025 only or none;
  - 2Q26's widely highlighted debt cut is a decoy;
  - the 2Q25 margins are thin (−214 / +363).
- Too-easy risk is moderate: every input is a labelled cell, both solvers matched with high confidence, and the cash-flow route also lands on the gold.
- This is a different design from q03, a one-sentence bridge into adjacent cells that the platform scored Too easy (Low 5/5).

**verdict:** ready

**findings:**
1. **Necessity record (Lever checks; rev 1 audit; rev 0 review).** The records say the cash-flow route "needs many documents", that "D12 alone covers only 2Q25 and 2Q26", or that it needs "six releases". In fact four releases reproduce the list using year-ago and year-to-date columns:
   - D08: 1Q24 = 2.4 − 1.3; 2Q24 = 1.3
   - D09: 3Q24 = 2.6; 3Q25 = 2.1
   - D10: 4Q24 −1.4 debt / +2.5 cash; 4Q25 −0.9 / −1.5
   - D12: 1Q25 = 4,731 + 299; 2Q25 −299 / −791; 1Q26 = −3,764 + 8,406; 2Q26 −8,406 / +3,266

   It is not a valid replacement. It tracks financing flows and cash including restricted cash, not balances: 3Q25 flow +2.1B vs balance change +12,077; 2Q25 −299 vs −214. Consequence: the eight-document listing stands for the defined measure, but the cheap route is a real too-easy risk. Correct the Lever checks and hand-over wording; that section is outside the fingerprint, so no re-test is needed.
2. **Closed-book exposure (Q1).** As above. Note it at hand-over; the platform's "Needs the documents" check decides.
3. **Verbatim evidence (platform-only, blocking check).** 14 of the 22 quotes use spaces where the source and the capture have tabs (for example, D02 line 334 is `Total debt $\t21,835 $\t20,836`). The 8 header quotes are exact. Check the form's verbatim panel after pasting; re-copying any quote changes the evidence and the fingerprint.
4. **Reasoning number rule.** My emulation flags nothing.
   - Steps 2–9 each cite one document, and every number appears in it.
   - Whole dates are printed in the shares-outstanding notes: D02 line 290, D06 line 288, D11 line 300.
   - Steps 10–12 cite no document and reuse only earlier balances and printed quarter labels, with no computed values.
   - Step 1, the only multi-document step, holds just "December 31" (printed in all six cited releases) and verbatim labels.
   - The rev 0 Step 1 wording slip and the weak tag are fixed. The form's handling of a multi-document step is still unseen.
5. **Format advisory.** "If any" does not say what to answer when nothing qualifies. Advisory only, since the answer is not empty.
6. **Records.** Rev 1 and this fingerprint appear on A, B, the closed-book run and the audit; the report shows no platform record. Status stays checked until an exact-content platform pass at Easy or above. The authorship tick ("I wrote this question myself") is reported separately.
7. **Set review.** q05 (trailing-twelve-month ROCE to June 30, 2026) shares the June 30, 2026 inputs but no answer path or hint. The dropped q01's 2Q26 net-debt change appears here only as a decoy.

Files reviewed:
- D:\Dev\Docket\tasks\aq-00998\questions\q06.md
- D:\Dev\Docket\tasks\aq-00998\runs\q06-r1-v2-29d185e75de6d08b9ef145b7532505903c1d05aa0ff495f2708c13665f85d240\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q06-r1-v2-29d185e75de6d08b9ef145b7532505903c1d05aa0ff495f2708c13665f85d240\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D01.txt – D12.txt
- D:\Dev\Docket\AQ-00998_2026-10-06_0256.md
