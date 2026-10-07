# q01 rev 1 independent review (fresh question-review agent), 2026-10-06

tested_sha256: a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba
Input: frozen fields (snapshot), corpus, raw rev 1 A/B/audit/closed-book returns, rev 0 review; target medium. Return copied verbatim.

---

**q01 review: ready (fair, supported and fully checked locally), but difficulty is easy, below the Medium target**

The gold of $309.0 million holds and every fairness check passes. On my estimate it lands at Easy or Too easy, so it does not meet the gate's "target-suitable difficulty" condition for Medium. I would quick-test it before spending a difficulty run.

q01 (rev 1; tested_sha256: a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba)

**Binding:** the snapshot, all four raw rev 1 returns and the four rev 1 records in q01.md carry rev 1 and this hash. `docket_agent.py report` recomputes the same hash from the current q01.md and corpus. The solver-1, solver-2 and shortcut packets hold the verbatim question and a corpus byte-identical to text/ and docs/. The closed-book packet holds only the question. Floor: 0 FAIL, 1 WARN (origin). There is no platform record, so Q13 is unknown.

**gold_verified: yes.** Recomputed with Decimal from the originals.
- D06 L46 (docs L44): "From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million."
- March 31, 2026 inventories are 1,035.4 (D06 L229, and identical in D04 L203). Peak = 1,035.4 + 320.9 = 1,356.3.
- June 30, 2026 inventories are 1,047.3 (D04 L203). The first quarter of fiscal 2027 is the three months ended June 30, 2026 (D04 L6/L20).
- Gold = 1,356.3 − 1,047.3 = 309.0. Cross-check: 320.9 − 11.9 = 309.0.
- "Now" means March 31: the same paragraph's $22.3 million equals D05's 1,057.7 − 1,035.4.
- Each input is printed once at one decimal, with no rounded prose version, so only one value exists at the asked precision.
- Wrong routes: 320.9 (stale), 332.8 (sign flip), 246.2 (March 2025 as the base), 376.9 (scaling by days).

**outcome:** A: match; B: match. Both answered $309.0 million with high confidence from D04 and D06, and both rejected 320.9 as the wrong date. Neither run was contaminated: B saw question.txt only in a file listing, and it holds just the question.

**closed-book: misses.** It answered "About $340 million" at low confidence (recalled peak about $1.32 billion, June 2026 extrapolated). That is not equivalent to the gold.

**necessity:**
- **D06 (Doc 5)** is the only fact tying the December 2024 level to a dated balance. Without it, Microchip inventories appear only for March 2025 (1,293.5), December 2025 (1,057.7), March 2026 and June 2026. There is no December 2024 balance and no inventory cash-flow line. D05's "substantial progress on inventory reduction" and D04's days figures carry no dollar amounts. The answer becomes undetermined, or 246.2.
- **D04 (Doc 6)** is the only June 30, 2026 balance, and it postdates model cutoffs. Without it the answer is 320.9 or undetermined.
- **D05** only corroborates. No other document mentions Microchip, so {D04, D06} is the minimal set.

**shortcut: clear.** The shortest route is D06 L46 plus D04 L203, which prints both balances: 320.9 − (1,047.3 − 1,035.4).
- A word-boundary search finds no "peak" anywhere; the only hits are inside "speak".
- "High point" and "December 2024" occur only at D06 L46.
- No passage, table or overview summary prints 309.0 or 1,356.3. The overview's Doc 4 summary says "progress on inventory reduction" and Doc 6's says "inventory days", with no figures.

**source_assessment: no gaps.**
- The report and snapshot both show source_gaps [] with gap hash 4f53cda1….
- The intake marks D04–D06 complete, with 0 gap characters and matching the capture. The capture hash a6eab79e… is verified.
- The quoted lines match the docs/ originals, so no assessment record is needed.

**difficulty: easy.** It is below the Medium target. The decoy (320.9) is answer-shaped, uses the asked measure, sits in the solver's path and is a required input. But it predates the asked date, which is the profile measured as crossed (aq-00998 q03, Low 5/5). It is not the later, current-looking decoy that reached Medium (aq-00964 q01). Several things also date the decoy for the solver:
- The asked quarter is D04's title.
- D04 L36's "185 days on March 31" dates D06's "185 days in March".
- D06's own "First Quarter Fiscal Year 2027 Outlook" shows that quarter was still ahead when 320.9 was written.

**verdict: ready.** It is locally ready, but not target-suitable for Medium.

**findings:**

1. **Rev 0 findings.**
   - Calendar pin: resolved ("end of calendar 2024").
   - "Now" support: resolved. The reasoning quotes D06's verbatim "lowered days of inventory from 201 days in December to 185 days in March", and the 22.3 cross-check holds.
   - Overview note: resolved (checked against capture L59 and L73).
   - Removal check: narrowed, but it still depends on recall; see item 4.
   - Pipe-free quotes: partly resolved. The redundant D06 row was dropped. The D04 L203 quote "Inventories 1,047.3 1,035.4" is still not verbatim locally (originals print "|Inventories|1,047.3|1,035.4|"). No prose prints 1,047.3, so the row stays. This is a blocking form check that runs before submission and does not burn an attempt. If it fails, use Save passage on the platform; that changes the evidence and needs a new revision.
   - Below Medium: unresolved by design.

2. **The "reduced … by the close of" reading.** I find no defensible second reading.
   - "Had reduced X from its peak by date T" is the net position at T. The CFO uses the same construction: 320.9 equals exactly 1,356.3 − 1,035.4, a level difference at the quarter's close.
   - The auditor's "most reduction achieved by then" (320.9) needs words like "at most" or "at any point", which the question does not contain.
   - A gross-reductions reading cannot be computed: no June or September 2025 balances exist, and it would match 320.9 only by assuming every quarter fell.
   - Residual risk: the action verb gives careless readers a slightly bigger opening than rev 0's state wording ("How far below … was … inventory balance at the close"). If several low-model attempts answer 320.9, the platform may add a "may be too vague" warning, as on aq-00745 q01. I put that at about 5%.

3. **Tier odds:** Too easy about 52%, Easy about 36%, Medium about 9%, Hard or higher about 3%.
   - **Low model's most likely route:** search "inventory" and land on D06 L46. Note that D06 is the March-quarter release. Open D04, whose title is the asked quarter, read 1,047.3 against 1,035.4, and compute 320.9 − 11.9 = 309.0.
   - **Likely misses:** first, 320.9, taken at face value. The mirrored verb and D06's fiscal 2027 outlook heading both pull toward it. Second, 332.8, from D04's falling days and "continued inventory normalization".
   - Medium needs Low 0/5, meaning every attempt stops at 320.9. D04's dating cues make that unlikely.

4. **Can the platform's document check reach $309.0 million without D06?** Not through any document route.
   - The high model would need an exact one-decimal recall: either the December 31, 2024 balance in the window [1,356.25, 1,356.35), or the $62.8 million March 2025-quarter reduction added to D05's 1,293.5.
   - Rounded recalls miss: "$1.356B" gives 308.7, $1.36B gives 312.7, $1.35B gives 302.7. The local closed-book recalls ($1.32–1.34B) give 272.7–292.7.
   - Risk is about 3–5%, down from about 10% at whole-dollar precision.
   - Without D04 the risk is effectively nil.

5. **Advisory risk.** The model check "Answer matches a stated figure" could misread D06's 320.9 as the asked figure. That is the trap itself; it is a warning, never a block.

6. **Set.** Sibling i04, the percentage form at 22.8%, shares the whole path and gives the answer away. Do not submit it alongside q01. i05 shares D04 but asks about a different quantity, with no hint.

7. **Authorship.** The origin WARN stands. The export accepts user origin only, and the form's self-authorship tick must reflect the real author.

8. **Platform-only checks are unknown:** restricted names, originality/duplicate check, token window, and the form's verbatim and reasoning-number checks. My local emulation of the reasoning-number check passes.

Relevant paths:
- D:\Dev\Docket\tasks\aq-01321\questions\q01.md
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\snapshot.json
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\results\
- D:\Dev\Docket\tasks\aq-01321\text\D04.txt, D05.txt, D06.txt
- D:\Dev\Docket\AQ-01321_2026-10-06_1139.txt (overview lines 59 and 73)
- D:\Dev\Docket\tasks\aq-01321\notes\sketches\i04.md
