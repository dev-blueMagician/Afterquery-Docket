# q01 rev 0 - independent question-review (fresh context, no writer conversation)

Date: 2026-10-05. tested_sha256: 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16
Inputs: snapshot.json, q01.md, text/ and docs/, results/solver-A.md, solver-B.md, shortcut-audit.md, closed-book.md, floor output.

Raw return (verbatim):

q01 (rev 0; tested_sha256: 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16)

**gold_verified: yes.** I recomputed it with a script. D04 shows 1H 2026 South America sales of 493 in three places (L205, L485, L1423). That equals D03 Q1 248 (L209/L227/L431/L1021) plus D04 Q2 245 (L205/L221/L431/L1313), and the mine split agrees (Cerro Verde 205+193=398, El Abra 43+52=95). The projection in force is D03 L227, "expected to approximate 1.05 billion pounds for the year 2026", dated April 23 (L47). 493 / 1,050 = 46.952%, which is 47.0% under both half-up and half-even rounding. Each input has only one stated value. The 311/312 mismatch exists only in the U.S. rows. To round to 47.0, 1H sales would have to be exactly 493 or 494.

Wrong routes:
- July projection (decoy): 49.3%
- Production instead of sales: 48.3%
- Consolidated instead of South America: 44.1%
- Cerro Verde only: 37.9%
- Q2 only: 23.3%

The two possible readings of the timing phrase:
- **Transaction month.** "In May 2026" (L921) and "prior to May 2026 it was 55.08%" (L457/L511). D03 still shows "55.08%-owned" (L197/L429), so the increase came after April 23. Any date from April 23 to July 22 gives 1.05, so the answer is 47.0%.
- **Disclosure date** (July 23, giving 1.0 and 49.3%). The words "at the time it raised" refer to the act itself, so this reading isn't defensible.

The highlight's "During second-quarter 2026" (L39) is settled by the dated sentence. The idea that the April projection stayed in force is supported by D04: it measures Q2 against "April 2026 estimate(s)" (L9, L11, L112, L130).

**outcome: A: match; B: match.** Both answered 47.0% with high confidence, citing D03+D04 at the right lines. Both named 49.3% and rejected it for the right reason. Both report being uncontaminated, and their packet texts match the corpus by hash.

**closed-book: misses.** It answered "About 49% (best guess 49.1%)" at low confidence from assumed figures. That is not equivalent to 47.0% at one decimal.

**necessity:**
- **D03 (Doc 1)** is the only source of the 1.05 billion projection. D04 never repeats it: no "1.05" or "1,050" anywhere, and its only April estimates are consolidated (690 lb, 140 koz, molybdenum, $2.24). Without D03, the result is 49.3%. Rebuilding the figure from consolidated 3.1 − U.S. 1.4 − PTFI 0.7 also gives 1.0, so 49.3% again.
- **D04 (Doc 2)** holds the event month and the Q2 and 1H sales. Without it, a solver could only guess: Q2=Q1 gives 47.2%, Q2=Q1 production 48.2%, a share of the consolidated Q2 estimate 48.4%, an even spread of the rest of the year 49.1%, half the year 50.0%. None lands on 47.0%.
- **D01/D02 (BHP)** contain no Freeport, FCX or Cerro Verde text. The only near-matches are "Cerro Colorado", Antamina and a "South America" job title.
- No smaller valid set exists.

**shortcut: clear.** The verified shortest route is the D04 May sentence, then a date comparison (April 23 against July 23), then D03 L227, then D04's 493, then one division. No passage states the ratio. The capture overview (D:\Dev\Docket\AQ-01189_2026-10-06_1257.md L23-41) omits May 2026, the South America projections and the 1H South America sales.

**source_assessment:** No gaps.
- The snapshot's source_gaps list is empty, and its hash (4f53cda1...) matches an empty list.
- Intake shows 4 of 4 documents complete, 0 gap characters, matches_capture true.
- The visual features the map flags are all in BHP documents, none of which hold Freeport content: italics at D01 93/186/239 and D02 249/302, D02 Figures 1-3 at L736-738, and arrow glyphs. They have no effect on the premises, gold, exclusions, uniqueness, necessity or shortcut.
- All evidence quotes are prose, so the pipe-table quoting risk doesn't apply.

**difficulty: medium (marginal).** This is local suitability for the Medium target, not an observed tier.
- *For:* it reproduces aq-00964 q01, the measured Medium analogue (Low 0/5, Medium 1/5, every wrong attempt took the event release's own later outlook). Like aq-00745 q09 (passed High), D04 never connects its 1.05→1.0 change to the stake purchase. The decoy can be built entirely from D04: the event, "55.66%-owned" next to the 1.0 projection (L193-221), and the 493 total.
- *Against:*
  - There are only two editions, so it is a binary choice.
  - The event month is plainly dated.
  - The question copies "ownership interest in Cerro Verde" and flags the timing ("was projecting ... at the time"). A solver could take the earlier edition from the past tense alone.
  - The six-month total is printed, so the arithmetic is trivial.

The main risk is landing in the Easy tier, which does not meet the target. "Too hard" is unlikely.

**verdict: ready.** This means locally supported only. Status should stay checked until an exact-content platform pass at Medium or above is recorded.

**findings:**
1. **Floor WARN (origin).** q01.md Lever checks still say "Warnings answered: pending floor run". Record the explanation: the origin is accurately claude, and the user-only export rule is a separate matter. Lever checks are not fingerprinted (submission_sha256 binds documents, tags, target, asks, answer_type, question, answer, components, reasoning and evidence), so this edit doesn't require retesting. Do not change the origin.
2. **Form number rule.** My emulation found every number either printed in a cited document or placed straight after "=". Steps 5-6 cite both documents with the operands split between them. How the form handles that is unconfirmed. Check the form's output after pasting.
3. **Removal tolerance.** The closest guess without D04 is 47.2%, 0.2 points off. Whether the platform grades with a tolerance is unobserved. Low risk.
4. **Guessable range.** 1H-to-full-year ratios cluster around 45-50%. The local closed-book guesses were 49.1% and 49.5%. A lucky "47%" from another model can't be ruled out, but asking for one decimal limits the exposure. Note it at hand-over.
5. **Tier risk (finding 6 in Difficulty).** The binary edition choice, the dated anchor and the timing cue make Easy tier the main risk. Only platform measurement can settle it.
6. **Report bookkeeping.** `docket_agent.py report` lists A, B and the closed-book run but not the shortcut audit, because it doesn't parse that record type. The q01.md audit line and the raw header both carry rev 0 and the same sha. This is a tool gap, not a question defect.
7. **Wording nit.** The Lever checks say Q1 "survives only inside D04's six-month table", but Q1 can be derived as 493 − 245. Immaterial: D03's indispensable fact is the 1.05 projection.
