# q04 rev 1 - delta review (the rev 0 question-review agent, resumed), 2026-10-08

Raw return as received (harness indent removed). Usage reported: 13 tool uses, about 246 s. The reviewer has
reviewed q04 since rev 0; it is independent of the writer, and this pass covered only the rev 1 changes and records.

q04 rev 1 should be dropped. The gold still stands, but by the workspace's own probe rule Doc 2 is not reliably necessary, and I found no fair fix.

q04 rev 1 delta review (tested_sha256: 53beb8cb78b2c686fa3066d7d4fdf169505819f2254271d3277028bdb144a537)

**(1) Findings 1, 2 and 4 are closed. The changed reasoning, evidence and failure-mode text are accurate.**
- **Finding 1:** the four [c2] rows are gone.
  - What remains is Doc 5 L418, L424, L428, L430, L432 and Doc 2 L33, L35 (first sentence), L63.
  - Every component has support, both ticked documents are quoted, and the floor shows 0 FAIL with the origin WARN only.
- **Finding 2:**
  - Step 3's added sentence on the fake-review branch matches Doc 5 L428 and Doc 2 L63.
  - Step 4 now describes the platform example correctly (Doc 5 L452, "on other sites"). It cites L71 as a hosting answer, not as the platform's own rule.
  - The Decoy line ("staff report that the rule defines") matches L297.
- **Finding 4:**
  - The cause is now "Misapplies a rule or premise".
  - Every quoted fragment in the boxes is verbatim ("the rule defines", L297's list, "enable accounts to be set up", "the business model of acting as a broker procuring banned reviews").
  - The boxes total 325 words. "Helping banned reviews get published" is a fair paraphrase of chapter 7's title.
- **Minor, pre-existing, optional:** three reasoning quotes use straight marks where the source has curly ones: Step 2 "465.2(a)'s", Step 4 "'distribution'", Step 4 "didn't". The q02 rev 1 precedent fixed the same kind of mismatch.
- **Stale lines in Lever checks (outside the fingerprint):**
  - "The second probe shows that D01 does not replace D03" is now contradicted by the rev 1 probe.
  - "gate Q2 holds locally" and "about 30-40%" need updating, per (3).

**(2) Every rev 1 record is accurate to its raw return and bound to 53beb8cb.**
- The current file recomputes to 53beb8cb, and the form hash 51150d27 equals the snapshot's.
- The question, components, reasoning, evidence, metadata and corpus all equal the snapshot. Question and corpus are byte-identical to rev 0.
- Both probe packets in q04-r0-alt-k8 match rev 1's solver-1 packet minus one document. I checked every docs/ file byte for byte and every text body; the question bytes are identical too.
- Each summary matches its raw return:
  - A: high.
  - B: medium, high for items 2 and 3.
  - Audit: clear, eight documents read in full.
  - Closed-book: misses. It gives two generic classes, cites a reserved §465.3 and names none of the examples.
  - Without Doc 5: misses; forced guess p 0.25.
  - Without Doc 2: "guess-reaches", the gold at p 0.5.

**(3) The Doc 2 probe should not be treated as a stated risk. Under the workspace's own probe rule it is a Q2 FAIL for Doc 2.**
- The removal-probe memory says: "A gold reached by inference from the remaining documents is a FAIL even when forced." It also says to "state the higher reading" when probes disagree.
- This probe reached the gold by reasoning from the rule text, not from recall.
- Even its unforced text-only answer lists the gold: the bot and SEO services "clearly fall under it", and the recruiting-group service "probably does too".
- The platform's high model is not told to hold back the way our probes are. It can also use recall: both closed-book returns drew on memory of Part 465, and the rev 0 one cited the staff Q&A.
- I now put the risk that the platform flags "A marked document may not be needed" for Doc 2 at about 50-60%.

I see no fair fix worth a new version:
- Doc 2's only fact that decides membership is L63 (brokers count as selling). It can be inferred from Doc 1's "sell" and §465.4, and it can be recalled. No other staff-only answer decides any of Doc 5's services.
- **Grouping "Doc 2 or Doc 1":** this contradicts "as FTC staff interpret it" and requires ticking and quoting Doc 1, whose text is scrambled. It also leaves the recall route open.
- **"Exclusion / condition source" with a note:** this does not fit. Doc 2's deciding fact adds an item rather than excluding one, and Doc 2 names no excluded item. The aq-01333 reviewer rejected a similar note.
- **Set note:** q02 rev 1 rests on a staff exclusion (L161-163) that the rule's literal text contradicts. Its Doc 2 probe forced a non-gold four-item answer at p 0.6, so q02 is the family's stronger Doc 2 dependency. Never submit both.

**(4) Verdict: drop. Difficulty: easy, below the medium target.**
- Fairness and the gold hold: two matches, a closed-book miss and a clear audit. The drop is for Q2 on Doc 2 with no allowed fix.
- The answer is the whole chapter 6 list, joined to Doc 2 by the shared word "broker". That is the same labelled-group pattern that measured Too easy on q03.
- Odds for one run (local estimates, not platform evidence):

| Outcome | Estimate |
|---|---|
| Too easy | 55-65% |
| In band at Easy, before the gates | ~33% |
| Usable Easy pass, after the Doc 2 risk | ~10-15% |
| Usable Medium pass | about 1-2% |

If the user still wants one Easy-slot attempt from this family, q02 rev 1 is the better candidate.

I wrote no files and ran no solves.

---

Caller's response, 2026-10-08: accepted. q04 is set to dropped. The rev 1 Review record is drop. The stale Lever
checks lines are corrected: the caller had first logged the Doc 2 forced reach as a stated risk, and the review
showed that was wrong under the probe rule. The optional curly-mark fix is moot. The next candidate is q02 rev 1.
