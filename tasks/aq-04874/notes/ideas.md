# aq-04874 - lean candidate sketches

Current target: medium (user, 2026-10-14: "there is no slot for Easy Tier for this bundle, we should target medium and
high"). Page at capture 12:17: Hard 0/5 · Medium 0/1 · Easy 1/0, "Still open on this set: Hard, Medium"; quick tests
0 of 15 (up to 5 sketch slots); difficulty runs 15 of 15. Medium has one slot and every captured run on 2026-10-14
started at the High level on other bundles, so sketches are audited against the medium and the high solver.
Measured platform success pending. Origin of every sketch: claude.

Round 1, 2026-10-14. Sketch only: no question file, prepare or form until the user reports a quick-test survivor; a
survivor's sentence and short answer go into the question file word for word.

Search behind this round: the caller read all five texts in full; two independent question-author agents searched the
whole bundle (author A from the RDPs, Doc 1 and Doc 2; author B from Doc 3, Doc 4 and Doc 5). All three found no
fair design with a step that no word in the question points at, and all three named the same best fair design (h1).
Structural reason: no document cites, restates, forecasts or amends another; the only cross-document numbers are posed
cases (one paper's rule applied to another paper's figure), and the case's own premise names every step. The bundle's
genuine unpointed exceptions (Doc 1's 2003-04 exemption for bonuses/overtime, Doc 3's non-mortgagor note, Doc 2's
missing 2007/08 survey wave, Doc 1's age-dependent super shock) each live in one document or fail delete-and-guess
when tied to another.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: Doc 1's super rule (counted over 40, vested linearly to 60) at Doc 4's 2022/23 median investor age 51: 55% | Readings still possible: 85% (vesting read as age/60), 100% (vesting skipped), 25% (1999/2000 age), 0% (Doc 2's equity measure, rejected by "2020"). Delete-and-guess: Doc 1 rule not recallable; without Doc 4 a guessed age near 50 gives 50%. Screen clean, 24 words. Unpointed steps: 0 | QUICK-TEST FAILED (user, 2026-10-14: "both too easy", no panel); route unread; dropped |
| i02 | [sketches/i02.md](sketches/i02.md) | h1 sibling: 0.55 x Table 4's average super shock of 30 = 16.5 cents per dollar | Readings: 30 cents (vesting skipped), 55 cents (shock skipped), 25.5 (age/60), 7.5 (age 45). Delete-and-guess as i01. Screen clean, 37 words. Unpointed steps: 0 (one more pointed lookup than i01) | QUICK-TEST FAILED with i01 ("both too easy"); dropped |
| A-i02 | hooks.md h8 (author A) | Michigan US$140,000 home, 5% deposit, Doc 1's 40% fall and 10% foreclosure cost: US$62,300 | US survey case under the Australian stress test: numbers the documents never connect; 0 unpointed | dropped, not offered |
| A-i03 | hooks.md h3 (author A form) | SIH waves in Doc 3's rising-rate years: 2011/12 and 2017/18 | Doc 2 fails delete-and-guess (biennial schedule recallable; Doc 1 names 2017-18); asks about survey design | dropped, not offered |
| B-i02 | hooks.md h9 (author B) | Doc 3 trimming windows keeping a -30% rent year: 1 | Doc 1 fails delete-and-guess (any shock from -10 to -50 gives 1) | dropped, not offered |
| B-i03 | hooks.md h2 (author B form) | price fall before a 20%-deposit loan loses self-cure: just under 11.1% | Doc 2 fails delete-and-guess (20% deposit is the default guess) | dropped, not offered |

Round 1 result (user, 2026-10-14, no panel): i01 and i02 "both too easy". No fair untested sketch remains: every other
hook is single-document, fails delete-and-guess, or joins figures no document connects (hooks.md h2-h13). Release
recommended to the user 2026-10-14; 13 of 15 quick tests and 15 of 15 difficulty runs unspent.
