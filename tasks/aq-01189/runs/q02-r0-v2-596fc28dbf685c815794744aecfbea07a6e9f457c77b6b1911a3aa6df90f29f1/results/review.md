# q02 rev 0 - independent question-review (fresh context, no writer conversation)

Date: 2026-10-05. tested_sha256: 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1
Inputs: snapshot.json, q02.md, q01.md (set check), text/ and docs/, doc-map (navigation), results/solver-A.md, solver-B.md, shortcut-audit.md, closed-book.md, floor output.

Raw return (verbatim):

q02 (rev 0; tested_sha256: 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1)

**gold_verified:** yes. I recomputed it by script from the passages.
- **Sources:** D01's guidance table (L78-90) gives the Previous and Current ranges. D02's table (L80-92) gives FY26 actuals, and its FY26e column equals D01 Current on all 13 rows.
- **Actuals:** I re-added every actual from D02 Appendix 2's four quarters (Sep-25 to Jun-26). Each sum equals the printed full-year figure.
- **Classification** (ranges in force before the 22 April review, BHP-operated only, strictly below or above the range):
  - Spence 212.6 kt is below 230 (17.4 short).
  - NSWEC 16.361 Mt is above 16 (0.361 over).
  - Inside on every basis: Escondida 1,261.2; Copper SA 320.7 net and 330.6 gross; WAIO 256.9 and 291.2; BMA 18.6 and 37.3.
  - No value sits on a boundary.
- **Excluded:**
  - Antamina (copper 151.5 outside, zinc 96.1 inside) and Samarco (7.84 outside) are named non-operated (D01 L480, D02 L943).
  - Carajás and WA Nickel have no range.
  - Group copper and iron ore totals are not assets and are inside anyway.
- **Robustness:** prose-rounded actuals give the same set. "BHP-operated" only decides Antamina and Samarco. Every other guided asset is inside, so the non-exhaustive "include" list cannot change the answer.
- **Anchor:** one date, 2 April 2026 (D01 L123; D02 L95/L348/L477).
- **Names:** "Pampa Norte (Spence)" is the row label; NSWEC is "NSW Energy Coal (NSWEC)" (D01 L280).

**outcome:** A: match; B: match.
- Both answered with high confidence from D01 and D02, picked the Previous column because 2 April comes before 22 April, and named and rejected the decoys.
- Packets held only the question and the corpus, with byte hashes equal to the snapshot. Both reported no contamination, and the solver IDs are distinct.
- The report recomputes 596fc28d... from the live fields, so the tested content is current.

**closed-book:** misses. It answered "Escondida (best guess)" with low confidence. That is not equivalent: Escondida is inside its range and neither gold item is named. The sketch-stage run said "none". Its recalled Escondida range (about 1,150-1,250) differs from D01's 1,200-1,275, so a memory route would mislead rather than replace D01.

**necessity:**
- **D01 (Doc 3):** its indispensable facts are the ranges before 22 April (Spence 230-250, L80/L107) and its 22 April date.
  - D02 has no production "Previous" column; its only one is unit costs (L241). Neither "230 – 250" nor "between 230 and 250" appears in it (script check).
  - Without D01, FY26e gives {NSWEC}; misreading FY27e gives {Escondida, CuSA, NSWEC}.
  - The Carajás date and the non-operated list repeat in D02, so they are not why D01 is needed.
- **D02 (Doc 4):** its indispensable facts are the FY26 actuals. Without it, D01's routes give:
  - {Spence} from D01's own stated expectations;
  - {Spence, BMA, NSWEC} from nine months plus the Q3 run rate;
  - {Spence, CuSA, BMA, NSWEC} from nine months times 4/3;
  - {Escondida, NSWEC} from nine months plus the prior-year June quarter.
  - Only an inconsistent mix lands on the gold, so the platform removal-test risk is low.
- **D03/D04:** Freeport releases with no BHP text (searched every asset name, CoreX, Carajás). There is no smaller or alternative source set.

**shortcut:** clear.
- The verified route is: 2 April (D01 L123 or D02 L95) -> D01's 22 April date (L17/L45) and Previous column (L77-90, L107) -> the operated filter (L480) -> D02 actuals (L80-92). The auditor's route and answer match mine.
- No passage states Spence's result against the earlier range. D02 L70/L187 states only NSWEC's, which is a difficulty risk, not a whole-answer lookup.

**source_assessment:** no recorded gaps. source_gaps is empty, and source_gaps_sha256 equals sha256("[]"). The capture is 4 of 4 complete and the packet bytes match the snapshot. Two observations that are not gaps:
- Italics are invisible in the text (D01 L93/L186/L239). The Previous/Current columns, the "Lowered"/"Increased" labels and the prose carry every production change. D02's quarters re-add to the printed full-year figures, so no hidden restatement affects the actuals.
- The HY26 announcement date is absent from the bundle (finding 1).

**difficulty:** medium, as local suitability only (marginal).
- The question has one untied edition trap plus one exclusion, and each changes the answer: {NSWEC} if the later ranges are used, {Spence, NSWEC, Antamina, Samarco} if the exclusion is skipped, {NSWEC, Samarco} if both go wrong.
- **Strong on the D02 side:** the 2 April footnote sits directly under the FY26e column, and D02's summary names only NSWEC as exceeding guidance, so the {NSWEC} decoy looks coherent.
- **Weaker on the D01 side:** the correct ranges sit in a column labelled "Previous" in the event's own release, and the Carajás sentence (L123) directly follows Antamina's "from 140 to 150 kt previously" (L122).
- **Analogues:** it sits between aq-00964 q01 (Medium; the correct value was in another edition) and aq-00745 q01 (Easy; the headline tied the event to the guidance change). Like aq-00745 q09 (High), the event is untied.
- **Main risk:** an Easy placement (Low 1-3/5). A High result would still qualify. "Too hard" looks unlikely: the exclusion list is explicit, and the uncertain operated cases (Escondida, WAIO, BMA) cannot change the answer. The local matches show fairness, not tier.

**verdict:** ready

**findings:**
1. **Premise (Q1/Q9; D01 L93/L107; HY26 date absent).** The reading needs only that the 22 April review made the change: "has been lowered ... (from between 230 and 250 kt previously)". D02 L249 measures updates from the prior periodic report, which supports guidance changing at reports. Nothing shows another change between 2 and 22 April, so I see one defensible reading. The bundle alone cannot rule out an unpublished change in between; all three document readers flagged this and none found an alternative. No change required.
2. **Overview exposure (Q8/D2).** The Doc 3 overview prints "2 April 2026" and "US$240 m Carajás divestment completion" (capture L49/L51). The author's overview probe left this out. The bridge date is cheap anyway (D02 L95), and the edition choice is not exposed. Record it in Lever checks.
3. **Stale record line.** Lever checks still says "Warnings answered: pending floor run." The floor now shows 0 FAIL and 1 WARN (origin: claude is accurate; the export tool takes user only). Record that explanation. Lever checks is outside submission_sha256 (check_questions.py L182-186), so no retest is needed.
4. **Set overlap with q01.** Both questions use the same mechanism: a company transaction date selects the guidance edition, and the later release's own range is the decoy. Both list "Same series, right edition", so the q02 note "different ... lever from q01" is wrong. There are no shared facts, shared wording or mutual giveaways, but the platform risk is correlated. Use a different source relationship for the remaining slots.
5. **Reasoning step 2.** Its "therefore" treats "Our non-operated assets include ..." as a complete list. This is harmless because the unlisted assets outside the gold are inside their ranges. Any edit to the reasoning changes the fingerprint and needs fresh checks.
6. **Form checks emulated (pass).** Every number and date in reasoning steps 1-4 and 6 is printed in the Doc it cites; uncited step 5 only reuses earlier values. All eight quotes are verbatim in the docs/ originals and sit inside one cell or prose line; the shortest is "16 July 2026" at exactly 12 characters. The question is 37 words, and its "in any order, or answer none" covers order and the empty case. The answer is 5 words, separated by a comma, with no semicolon.
7. **Report tool.** It does not list the shortcut-audit record type (a known limitation). The audit line in q02.md carries the current fingerprint.
8. **Platform-only, unknown:** restricted names, originality/duplicate, the "One defensible answer" and "Needs two or more documents" model checks, whether "in any order" clears the format advisory, and the difficulty check with its removal test. Status stays checked until an exact-content platform pass at Medium or higher.
