# q01 rev 0 independent review (fresh question-review agent, 2026-10-08)

tested_sha256: 6f8f40e33cf2ab101a45954cb6df514b0091b51a1fe45140e8a4d6b1ecdd34f7
Inputs: question file, snapshot, corpus, all raw returns (A, B, audit, closed-book, two removal probes), floor; caller's five adjudication points.

Raw return:

q01 (rev 0; tested_sha256: 6f8f40e33cf2ab101a45954cb6df514b0091b51a1fe45140e8a4d6b1ecdd34f7)

**Verdict: revise.** The fix is limited to the Failure mode 1 boxes, which sit outside the fingerprint, so no re-test is needed. **Difficulty: easy** for the Medium target; I put Medium at about 10%.

gold_verified: yes. I read D02–D08 in full and D01 by search plus its disposition and separate-opinion passages. Under the question's literal words exactly two defendants qualify:
- **Vidino:** D02 l.515 says "over whom the Court has personal jurisdiction". Count Three is his only claim, and it is dismissed (l.551, l.564).
- **Lewis Machining:** D05 l.80 is the court's own finding ("the Court finds as follows") of "personal jurisdiction over the Parties". The Parties include the sole defendant (l.31, l.118). All of the plaintiffs' Counts I–III are dismissed with prejudice (l.68, l.156), with final judgment for the defendant (l.108).

Exclusions all hold:
- OEC India: Counts I–VIII survive (D07 l.455).
- OEC USA, the Alp defendants, Besson, the UAE and Ofcom: dismissed for want of jurisdiction.
- Royal Caribbean: D04 l.25 is only a statement of doctrine.
- The Shenzhen plaintiffs: Counterclaim Counts I–II were adjudged against them (l.128–130, l.158).
- Ariaf and the John Does: no ruling on them.
- Philadelphia, DUAL/Chaucer/Houston, the JLF Defendants and Norvell: no dismissal in the ruling and no personal-jurisdiction statement.
- No cited precedent supplies a qualifying defendant.

All eight rulings are dated or filed September 11–15, 2026.

outcome: A: match; B: match. Both committed to Vidino and Lewis Machining (an equivalent name form), each at medium confidence. A's "contested only → Vidino alone" is a reading it noted, not its answer. The packets were distinct and carried only the verbatim question; the git-status harness listing is not contamination.

closed-book: misses. It answered "unknown", with a forced guess of "none" at p 0.10.

necessity:
- **D02 (Doc 8)** is the only source of Vidino (all 29 mentions are in D02). The probe without it answered "cannot be determined"; its forced guess was Lewis Machining alone at p 0.40.
- **D05 (Doc 2)** is the only source of Lewis Machining (D01's "Lewis v. Walley" is an unrelated citation). The probe without it answered "cannot be determined"; its forced guess was Vidino alone at p 0.4.
- The probe packets are correct: renumbered, neutrally named, each missing the intended ruling. No smaller source set exists. D07 and D04 rule out only their own content, so they must stay unticked (the aq-01333 lesson).

shortcut: clear. The shortest route is a "personal jurisdiction" search (51 hits across D02, D04, D05, D07), then D02 l.515/551 and D05 l.80/118/156, then rejecting D07 via l.455 and D04's l.25. No single passage, document or capture overview holds the answer. The Doc 8 overview names Vidino's merits dismissal without jurisdiction; the Doc 2 overview is cut off at "The order dismisses all…". Two difficulty risks, not violations: the question's legal term is the search key, and l.515 is answer-shaped for one item.

source_assessment: no gaps. intake.json shows all eight documents with captured hash equal to source hash and 0 gap characters. The report lists no source gaps, and the capture file's hash equals intake's capture_sha256.

difficulty: easy. The main trap (Failure mode 2) is a single non-salient member. The decoy (OEC India) was rejected by every local run, and aq-01432 q03 showed such decoys don't trap the low model either. The closest measured analog, aq-01433 q01 (one hidden list member), came in at Low 2/5, Easy.
- Per low attempt I estimate exact gold at about 0.45–0.6: Vidino found about 0.9, Lewis Machining included about 0.6–0.7, decoys excluded about 0.85–0.9.
- Conditional on a run: Too easy 25%, Easy 50%, Medium 10%, Between levels 7%, High 3%, Too hard or Answer not supported 5%.
- Separately, about 15% chance the form blocks it before any run (point 2).
- The local Opus results show fairness, not tier.

failure_modes:
- **FM1 (Part vs total / Wrong members in a list).** The trap is real and needs D07's conclusion to defeat. Two problems in the boxes:
  - The recomputed single-trap wrong answer is "Lorenzo Vidino, Lewis Machining & Engineering and OEC India", which is what Lever checks' condition-removed counterfactual gives. The box instead lists "OEC India" and "Lorenzo Vidino and OEC India", which stack Failure mode 2's omission on top.
  - Two claims are false. "Longest jurisdiction analysis in the bundle": D07 Part II is 3,607 words, against 3,666 for D02's personal-jurisdiction part, 8,419 for D02's FSIA analysis and 4,763 for D03's. "Ends: 'Upon review…'": that sentence opens section II.B at l.127; the section ends at l.204.
  - No local run took OEC India.
- **FM2 (Document convention / Wrong members in a list).** The trap is real, the recomputed wrong answer is "Lorenzo Vidino", every claim in the boxes checks, and the label is the best fit available. A small nit: "the Parties" is defined at l.118, after the finding at l.80.

findings:
1. **Point 1, the narrow reading.** It adds conditions the question does not state.
   - "Say" is met by the court's numbered finding at l.80, and "dismissed" by the court's own l.68 plus ¶9 of the entered judgment.
   - The "contested holding" variant cannot yield Vidino alone. Nothing in D02 shows Vidino contested jurisdiction, and the probe without D05 found that variant gives "none".
   - Only a reading that excludes collective or stipulated findings, or agreed dismissals, gives Vidino alone, and neither is in the words.
   - So this is not a demonstrated ambiguity. I put a reviewer return for it at about 10%, and no fairness fix is required.
   - If the form blocks the question, the change must state the separating condition in the question: a court statement covering the defendant collectively counts, and the manner of dismissal (contested or agreed) is irrelevant. It must do this without naming a settlement or consent judgment, without pointing at Doc 2 and without an exclusion list. Expect that change to disarm Failure mode 2 and land Easy or Too easy, which is unusable on this bundle.
2. **Point 2, the form block.** A block needs both form solvers to answer "Lorenzo Vidino". All three local full-bundle runs named that reading and held only medium confidence, and local matches predicted none of the four recorded blocks. I estimate the risk at about 15% (range 10–25%). Screen it in the free form check before spending a difficulty run.
3. **Point 3, "List them in any order".** Not a fairness issue: the plural "which defendants" carries the same signal, and the form asks for an order statement. It slightly weakens Failure mode 2 and slightly lowers the block risk, and it made the removal probes decline to commit. It does not justify a re-test on its own; if you revise for another reason, match q02 rev 1's line.
4. **Point 5, evidence.** All six quotes are verbatim in text/ and in the docs/ originals, 83–117 characters each, ASCII only. The second ¶9 fragment also occurs in ¶10; paired with the first fragment it still supports c2.
5. **Lever metadata.** "Bury one list item late" is inactive and not recorded in Lever checks. D02 announces Vidino's dismissal in its opening lines (l.39, l.49), and the search reaches l.515 directly. Drop it or document it; this field is outside the fingerprint.
6. **Roles section.** "## Necessary documents" is empty, and the hand-over defaults both documents to Answer component, which is correct. Writing the section changes the fingerprint, so leave it empty or re-prepare.
7. **Set review.** q01 and q02 share the frame and a two-defendant list shape (a 6-word run, "15, 2026, which defendants, if any"), so the Sibling question and Question mix advisories may fire. There are no mutual giveaways. The closest match in other tasks is aq-docket-trial-05 q04 at ratio 0.44, on stock phrasing only.
8. **"In eight federal rulings".** This counts documents, a ground-rule-10 tension, but the floor passed it and the check is advisory. The count also makes removal solvers answer "cannot be determined", which helps the platform's document check.
9. **Records.** Rev 0, and all records carry 6f8f40e3…, matching the report; the report and the question file lack the audit-recorded probe kinds only. There is no platform record. The capture shows Medium as the only open slot, with 8 of 8 runs left. Local review does not establish a platform pass.

Files reviewed:
- D:\Agents\Docket\tasks\aq-01540\questions\q01.md
- D:\Agents\Docket\tasks\aq-01540\runs\q01-r0-v2-6f8f40e33cf2ab101a45954cb6df514b0091b51a1fe45140e8a4d6b1ecdd34f7\
- D:\Agents\Docket\tasks\aq-01540\runs\q01-r0-alt-n5\results\
- D:\Agents\Docket\AQ-01540_2026-10-07_1253.txt
