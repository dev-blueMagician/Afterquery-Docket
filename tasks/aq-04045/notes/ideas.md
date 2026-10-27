# aq-04045 - lean candidate sketches

Current target: medium or hard (user, 2026-10-13: "there is no slot for Easy Tier for this bundle, we should
target medium and high"). Measured platform success pending.
Page state at intake: Hard 0/3 · Medium 0/2 · Easy 0/0; quick tests used 0 of 15; 8 submissions left.
Round 1 (2026-10-13): five sketches, all author-screened and script-screened (0 failures each). Quick tests
the same day (user chat, verbatim, no panels): "1, 3 too easy, 2 survived. others not tested". Quick tests
used: 3 of 15 by this count. Difficulty Run 1 on q02 (2026-10-13 15:37): "Too easy", Low 5/5 (2 not scored);
the page then read "15 of 16 runs left". Hook h1 is closed after three forms.
Round 2 (2026-10-13): i04 and i05 still untested; i06 added (author- and script-screened, 0 failures).
Round 2 result (user chat, verbatim): "4 survived". Sketches 5 and 6 were not mentioned.
Difficulty Run 2 on q03 (2026-10-13 17:46): "Too easy", Low — · Medium 5/8; the page then read "15 of 17 runs left".
Round 3 (2026-10-13): i07, the one repair of q03, offered as a sketch.
Round 3 result: i07 "survived"; applied as q03 rev 1; Difficulty Run 3 (2026-10-13 19:59): "Too easy", Low — · Medium 4/8.
Round 4 (2026-10-14): hook h2 closed; i08 (new hook h3c) offered; i05 and i06 given ", if any," and kept as siblings.
Round 4 result (user chat, verbatim): "too easy for quick test" (i08). i05 and i06 are untested; each needs a
subset of the steps the easier solver did on i08 (i06 names the collective in its own section; i05 is the plain
intersection), so by the workspace rule a family the easier solver has solved stays closed. No other fair design.
Round 4 close (user chat, verbatim): "both failed" (i05, i06). Every fair sketch now has a result: no fair Medium
or Hard design on this bundle; release recommended 2026-10-14. Nothing was submitted.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md), written up as [q01](../questions/q01.md) | h1: share of all FY 2024 space station fees on NGSO-Other, from D05's units and D06's per-unit fees through the 40% NGSO share. Gold 31.5%. | Still-possible reading: 32.0% as "the allocation" (40% x 80%); only the documents reject it (D06 para 40). D05 and D06 each hold a figure nothing else prints. Three steps the question does not point at, in two documents. | Quick test: too easy (the easier solver answered it). q01 dropped. |
| i02 | [sketches/i02.md](sketches/i02.md) | h1b: GSO stations' FY 2024 fees as a group. Gold $20.2 million. | No printed look-alike; wrong route $19.9 million (small-satellite fees left out). A cautious solver may answer "cannot be determined". | Quick test: survived. Written up as [q02](../questions/q02.md), fingerprint d823b968.... Difficulty Run 1: Too easy, Low 5/5. q02 dropped. |
| i03 | [sketches/i03.md](sketches/i03.md) | h1c: share on NGSO payors charged per system. Gold 39.4%. | The printed 40% fits a loose reading of "NGSO payors charged per system"; a "too vague" block is possible. | Quick test: too easy. Dropped. |
| i04 | [sketches/i04.md](sketches/i04.md) | h2: change in the small-provider share between the FCC's earliest (D03, 2020) and latest (D07, 2023) year-end counts. Gold 2.6 percentage points. | Publication-order route gives 5.6. D03 and D07 each the only source of their year. | Quick test: survived. Written up as [q03](../questions/q03.md), fingerprint 4e9dbb9f.... Difficulty Run 2 (Version 84ce0b): "Too easy", Medium 5/8, check started at the Medium level. All three wrong answers were 5.6 (Doc 3's count missed). Repair is sketch i07. |
| i07 | [sketches/i07.md](sketches/i07.md) | h2, q03's one repair: the same question with "change ... Give the sign" instead of "rise". Gold +2.6 percentage points. | In Run 2 one right attempt had missed the latest count and re-read only because the question said "rise". Wrong routes now +5.6 and -3.0, each a plain answer. Still-possible reading: "earliest" as the first rule published (+5.6). | Quick test: survived. Applied as [q03](../questions/q03.md) rev 1 (4b266045...). Difficulty Run 3 (Version 790376): "Too easy", Medium 4/8. Same failure on the repaired version: hook h2 closed, q03 dropped. |
| i05 | [sketches/i05.md](sketches/i05.md) | h3: petitioners against the 2020 debris rules named with a fee proposal in the 2025 notice. Gold Kuiper, SpaceX, Telesat. | Decoys Maxar and Kepler fail "petitioned". D01 and D05 each the only source of its list. | Quick test (user chat 2026-10-14, "both failed" for i05 and i06): failed. Dropped. |
| i08 | [sketches/i08.md](sketches/i08.md) | h3c: the company named in the 2025 fee notice, if any, that had joined a petition asking reconsideration of the deployment-device disclosure. Gold Telesat. | The deployment section names five arguers and leaves Telesat out; only D01 para 1 says the petition of all six asked about deployment devices. Still-possible reading: only the five named arguers petitioned on this rule ("none"). | Quick test (user chat, verbatim): "too easy for quick test". Dropped. |
| i06 | [sketches/i06.md](sketches/i06.md) | h3b: the one company named in the 2025 fee notice that had sought reconsideration of the persistent-liquids rule. Gold Telesat. | The order attributes that objection only to "The Combined Petition", a label its first paragraph defines; SpaceX and Kuiper petitioned on other rules, Maxar and Kepler only commented. Still-possible reading: the objection came from some of the six only. | Quick test (user chat 2026-10-14, "both failed"): failed. Dropped. |

Rejected or held, with reasons in hooks.md: h4 (old small-satellite formula: two defensible answers), h5
(what-if on FY 2024's pool: mixes bases, every step named), h6 (1,600-day gap: date gaps test too easy),
h7 (fees while awaiting re-entry: unstated assumptions), h8 (BIS category against the FCC fee category:
guessable).

What the difficulty run showed (routes in questions/q02.md, Feedback log): every scored low attempt found the
units and the fees in different rules, put the small-satellite fees inside the NGSO share and scaled through the
60/40 split; one multiplied the unit count by a per-station fee it remembered. The quick-test survival was noise.
A survivor whose sibling wordings failed on the same steps gets a second quick test before any write-up.

What round 1 showed: the easier solver did the two share forms, which need the total through the 40% share
and the small-satellite fees inside it, so those steps do not hold it. The dollar form survived although it
needs the same steps; the one difference is that nothing about the asked category (GSO) is priced in the
documents. Its wrong answer is unknown (no panel): route unread. One survival beside two failed siblings is a
screen result, not a measured difficulty.

Superseded (q01 dropped): reserve wording for q01 if "One defensible answer" fails on 32.0%: "What percentage of all regulatory fees the
FCC assessed across its four space station fee categories for fiscal year 2024 fell on NGSO-Other, to one
decimal place?" It names the base by its structure and adds no instruction to calculate. Untested.

Set review: i01, i02 and i03 share one answer path (D05 units x D06 fees); at most one of them is
submitted. i04 (D03, D07) and i05 (D01, D05) share no input with them or with each other.

A survival at the quick test sets no tier. For a derived gold the form's "One defensible answer" check
comes before any difficulty run (aq-03120, aq-03711).
