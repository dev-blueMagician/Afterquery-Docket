# q01 rev 0 independent review (fresh question-review agent), 2026-10-06

tested_sha256: 562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87
Input: frozen fields (snapshot), corpus, raw A/B/audit/closed-book returns; target medium. Return copied verbatim.

---

**q01 review: verdict revise (one wording fix). The gold of $309 million holds, and the design looks like Easy at best, not Medium.**

q01 (rev 0; tested_sha256: 562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87)

**Binding.** The snapshot, all four raw returns and all four q01.md records carry rev 0 and this hash. `docket_agent.py report` recomputes the same hash from the current q01.md and corpus. The floor gives 0 FAIL and 1 WARN (origin, expected). There is no platform record, so Q13 is unknown.

gold_verified: yes. I recomputed it with a Decimal script from the originals.
- D06 L46: "we have now reduced the inventory by $320.9 million" from the December 2024 high point.
- March 31, 2026 inventories are 1,035.4 (D06 L229, repeated in D04 L203). June 30, 2026 inventories are 1,047.3 (D04 L203).
- Peak = 1,035.4 + 320.9 = 1,356.3. Gold = 1,356.3 − 1,047.3 = 309.0. Cross-check: 320.9 − 11.9 = 309.0.
- "Now" means March 31. The same paragraph says "185 days in March" and "reduced inventory by $22.3 million", and D05's 1,057.7 − 1,035.4 = 22.3.
- Units are $ millions, the result is exact and no rounding step is involved. Q1 FY2027 is the three months ended June 30, 2026 (D04 L20).
- Wrong routes are 320.9 (stale), 332.8 (sign flip), 246.2 (March 2025 base) and 376.9 (scaling by days). The wording or the balance sheets rule each one out.

outcome: A: match; B: match. Both answered $309.0M with high confidence from D04 and D06 and named the decoys. B's "About $309.0 million" is an equivalent form. I confirmed each packet holds only question.txt plus all 12 documents, with hashes identical to text/. Neither run was contaminated.

closed-book: misses. It answered "About $330 million" at low confidence, recalling the peak only as roughly $1.34B.

necessity:
- **D06 (Doc 5)** is the only source of the reduction from the December 2024 high point. Without it, the remaining releases print balances only for Mar 2025, Dec 2025, Mar 2026 and Jun 2026, and have no inventory cash-flow line. D05's "substantial progress on inventory reduction" gives no number, so the answer becomes undetermined or 246.2.
- **D04 (Doc 6)** is the only June 30, 2026 balance, and that figure postdates model cutoffs. Without it the answer becomes 320.9 or undetermined.
- **D05** is corroboration only and is correctly unlisted. No smaller set works.

shortcut: clear. The shortest route is D06 L46 plus D04 L203: one sentence, one table row and two operations. No passage, table or overview prints 1,356.3 or 309. Every "peak" hit is "speak" or "speaking", and "high point" / "December 2024" appear only at D06 L46. The question's wording leads a search to the decoy sentence, which is an input, not the answer.

source_assessment: no recorded gaps. The report shows source_gaps [], with a gap hash equal to the snapshot's. The capture read all 12 documents in full with zero gap characters. text/ differs from docs/ only by a header line and blank lines around tables, which I checked on every quoted row.

difficulty: easy. It is locally suited at most to Easy and sits below the Medium target. The design has an answer-shaped, undated decoy ("now") in the solver's path. Against that, the asked quarter is named, D04 carries it as its title, and D04 L36's "185 days on March 31" dates D06's "185 days in March". Past results point the same way. A decoy that predates the asked date was crossed (aq-00998 q03, Low 5/5). The two Medium-or-higher passes used a decoy that looked current (aq-00964 q01, aq-00745 q09). The auditor also noted the anchor is found quickly.

verdict: revise

findings:
1. **Period not pinned (Q9, Rule 9b).** The question says "end-of-2024", but Microchip's fiscal year ends March 31 (D06 L28), and the guide requires "fiscal" or "calendar" for such companies. The fiscal reading (March 31, 2024) has no data in the bundle, so the gold and uniqueness are unaffected, but the platform's period check or a reviewer can return it. Fix: mark 2024 as calendar. This needs rev 1, a new prepare run, fresh A/B solves, a closed-book run and an audit.
2. **Two evidence quotes are not verbatim (Q14).** The two "Inventories …" row quotes match neither the originals nor the capture (docs D06 L234 and D04 L208; capture L2210 and L2682, all "|Inventories|…|…|"). They pass only the floor's pipe-stripping rule. See (3) below. Because evidence is part of the fingerprint, fold any evidence change into the same revision.
3. **Below the Medium target (Q11/D7).** The lever is real (320.9 ≠ 309) but the question's required period label defuses it. Run a quick test before spending a difficulty run.
4. **Removal check for D06 depends on recall.** See (2) below.
5. **One lever-check note in q01.md is wrong.** It says the overview mentions only "inventory days". The Doc 4 summary also says "progress on inventory reduction" (capture L59). It prints no figure, so there is no exposure.
6. **Optional reasoning fix.** The reasoning asserts the "now" date without support. D06's own "201 days in December to 185 days in March" supports it without adding a document.
7. **Sibling overlap.** i04, the percentage form, reuses q01's whole path, so submit only one of them.

**(1) Tier odds.** Too easy about 55%, Easy about 35%, Medium about 7%, Hard or higher about 3%.
- **Most likely low-model miss:** answering $320.9M from D06's "we have now reduced" sentence. D06's own "First Quarter Fiscal Year 2027 Outlook" heading (L115) puts the asked quarter's name in the decoy's release.
- **Less likely:** $332.8M, adding the June change because D04 talks about inventory days declining; or $246.2M, using the March 2025 balance as the peak.
- **Medium needs Low 0/5,** which requires a systematic "now" capture, and D04's dating makes that unlikely.

**(2) Document check without D06 or D04.**
- **Without D06:** no document route exists. The high model reaches 309 only if it recalls a December 31, 2024 balance between 1,355.8 and 1,356.8 ($M), i.e. "$1.356 billion" or "$1,356.x million". A recall of $1.36B gives 313, $1.35B gives 303, and the local closed-book's $1.34B gives 293. I put the risk at about 10%. Asking for one decimal ($309.0M) would shrink the window to an exact 1,356.3 recall, since "$1.356B" would then give 308.7. All inputs are printed at one decimal, so this adds no answer ambiguity.
- **Without D04:** the risk is negligible, because the June 2026 balance is post-cutoff and printed nowhere else.

**(3) Pipe-free row quotes.** Yes, this is a form risk, though unconfirmed. The only platform evidence, from aq-00949, showed a row in space-separated form, but that bundle used spaced pipes. It is a blocking pre-submit check, so it would not burn an attempt. Both necessary documents are already cited by prose quotes that are verbatim in the originals and the capture, so the cited-document and component-coverage checks survive dropping the rows. The D06 row quote is redundant because D04 L203 also prints 1,035.4. No prose prints 1,047.3, so that row must stay. Check the form's verbatim result first, and use Save passage if it fails.

**(4) Strengthening the trap.** I found no change that strengthens it within the rules, because the decoy is ruled out by the period label that Rule 9 requires. I describe options here rather than drafting replacement wording.
- **Pin 2024 as calendar:** neutral for difficulty.
- **Mirror the CFO's verb** (ask how much inventory had been "reduced" by the quarter's close): a marginal salience gain, with no new ambiguity.
- **One-decimal precision:** hardens the removal check, not the trap.
- **Anchor through D06's June-quarter outlook:** it prints "June 30, 2026" plainly, adds parsing load, and is likely crossed.

I wrote no files. Relevant paths:
- D:\Dev\Docket\tasks\aq-01321\questions\q01.md
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\
- D:\Dev\Docket\AQ-01321_2026-10-06_1139.txt
- D:\Dev\Docket\tasks\aq-01321\notes\sketches\i04.md
