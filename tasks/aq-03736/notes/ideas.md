# aq-03736 - lean candidate sketches

Current target: medium (hard welcome); the user states there is no Easy slot, and the page of 2026-10-13
reads "Hard 0/3 · Medium 0/2 · Easy 1/0". Sketch files are in notes/sketches/; facts and checks live there or
in the question files, not here. Round 3 of 3 (three difficulty runs used; the page reads "13 of 16 runs left" after an extra run for "Too easy"). Rounds 1 and 2 are spent: q01 Easy, q02 gate failed,
i07 and i09 quick-test failures, i06, i02 and i03 withdrawn on necessity.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i07 | [sketches/i07.md](sketches/i07.md) | h17 | Gold: financial holding companies. Wrong routes: "none" (entry-for-entry matching), mixed financial holding company, management company, crypto-asset service providers. Delete-and-guess: holds on both sides. One unpointed step. | dropped: quick test failed (user chat 2026-10-13: "i07, i09 failed"; no panel pasted, so the tested wording is taken to be the sketch as handed over or the user's own-words version; identity unbound, routes unread) |
| i09 | [sketches/i09.md](sketches/i09.md) | h20 | Gold: Minamata Convention, Montreal Protocol. Decoy: the Rotterdam Convention (import ban in both texts, unnamed in the proposal). Delete-and-guess: holds on both sides. Every step pointed at by "imports". | dropped: quick test failed (user chat 2026-10-13: "i07, i09 failed"; no panel pasted, so the tested wording is taken to be the sketch as handed over or the user's own-words version; identity unbound, routes unread) |
| i10 | [sketches/i10.md](sketches/i10.md), written up as [q01](../questions/q01.md) rev 1 | h15 | q01 with the documents' phrase "financial year" taken out of the question; gold 38 months. Quick test survived, then Run 3 (Version 6bde93): "Too easy", Low not run, Medium 5/6; the one miss took the proposal's first deadline as 30 April 2028. | q01 dropped, hook closed |
| i05 | [sketches/i05.md](sketches/i05.md), written up as [q01](../questions/q01.md) | h15 | Run 1 (Version 420741): "In band — Easy tier", Low 1/5; four low attempts 26 months by one route; both documents "Needed ✓". | q01 rev 0 held: Easy is closed |
| i01 | [sketches/i01.md](sketches/i01.md), written up as [q02](../questions/q02.md) | h1 | Run 2 (2:31 PM, screenshots only): Low 2/5; gate failed, "Your answer can still be reached without document 3". The gold is every guidance item the proposal calls optional, so the adopted text only confirms it. | q02 dropped, hook closed |
| i06 | wording in hooks.md h16 | h16 | Both bounds are headline thresholds; fails delete-and-guess on both sides. | withdrawn 2026-10-13, untested |
| i02 | [sketches/i02.md](sketches/i02.md) | h2 | Doc 3 supplies only recalled dates. | dropped 2026-10-13, untested |
| i03 | [sketches/i03.md](sketches/i03.md) | h3 | D02 alone names all three dropped kinds. | dropped before any test |
| i04 | [sketches/i04.md](sketches/i04.md) | h4 | Gold 18 points and 12 points. The defined term in the question leads to each definition (a pointed step). Delete-and-guess holds on both sides. | the last fair untested sketch; offered 2026-10-13 for a quick test |

Sketch wordings (author: claude; the user rewrites every question in their own words):

- i04: "On how many numbered annex points can an adverse environmental impact rest under the adopted due
  diligence directive, and on how many under the Commission's proposal?" Answer: 18 points under the adopted
  directive and 12 under the proposal.
- i07: "Which kind of regulated financial undertaking, if any, counts as a company under the adopted due
  diligence directive but did not under the Commission's proposal?" Answer: financial holding companies.
- i09: "Under which treaties does the annex to the adopted due diligence directive ban imports where the annex
  to the Commission's proposal banned none under the same treaty? List them alphabetically." Answer: Minamata
  Convention, Montreal Protocol.
- i10: "An EU company that must publish its due diligence statement always has 6,000 employees, EUR 1.2
  billion worldwide turnover and accounts closed each 30 June. Had the Commission's proposal entered into
  force when the adopted directive did, how many months after its first statement deadline under the proposal
  does the first accounting year its directive statement must cover end?" Answer: 38 months.

Tests every sketch must pass before it is offered (both added after a run was spent on a failure):

| Candidate | Unpointed steps (WORKFLOW section 6, item 6) | Delete each document and guess (WORKFLOW section 4) |
| --- | --- | --- |
| q01 / i10 | one: the Article 16 exception closing D02 Article 37(1)(b) | measured: both documents needed |
| q02 | counted as two | FAILED on D02, found only by the run: with D02 deleted the proposal's two optional guidance items are the natural answer |
| i06 | two, in one sentence | fails on both: EUR 150 million and EUR 80 million are headline thresholds |
| i07 | one: an entry gained a kind inside a 590-word sentence | holds: no natural guess on either side |
| i09 | none: "imports" points at every step | holds: no natural guess on either side |

Independent author runs (question-author, fresh context, 2026-10-13; both returned): run 1 proposed h15 and
h16; run 2 proposed the financial-undertakings list (kept as i07), the worker-kinds list (h18, held) and the
export form of h20, and found D02 recital (18).

What the bundle has shown (three results; the third at the Medium level, where a six-step chain was solved
5 of 6): the easier solver clears every step a word in the question points
at and recalls the adopted directive's headline dates and thresholds; the Document check reached a two-item
gold without the adopted text. A design here has to rest on non-headline wording of both texts and on a
partition that cannot be guessed from one of them.

Keep facts/checks in the linked sketch or question file. One focused repair per distinct observed failure; a
repeated failure means change the hook.
