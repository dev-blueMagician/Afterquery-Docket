# aq-03120 - lean candidate sketches

Current target: medium (user, 2026-10-11: no Easy slot on this bundle, "target medium and high"); measured platform
success pending. Origin of every sketch: claude. Round 2 of 3. Round 1: i06 became q01, dropped after four versions (Easy, two
form blocks, quick-test too easy). Round 2: i07 became q02; its third wording (i08) passed at Medium and was submitted 2026-10-12.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i06 | [sketches/i06.md](sketches/i06.md): Kiwibank home lending growth in the half of its financial year when ANZ piloted Simple Switch; $0.5 billion; Docs 2, 3, 4 | h1 | 0.6 fails the period (its half ended 31 December 2022); 1.1 is twelve months. Doc 2 = only date of the pilot; Doc 4 = only first-half figure and its dates; Doc 3 = only full-year figure. Doc 2 is "Used to identify" | quick test survived (user chat 2026-10-11: "i06 survived"; nothing said about the others). Promoted unchanged to [q01](../questions/q01.md) rev 0 (ec5f8e4c...): difficulty Run 1 "In band — Easy tier", Low 1/5, below target. q01 rev 1 (8ea00ff3...) replaced the ANZ pilot with Kiwibank's own first-half announcement as the dating event (Docs 3, 4) and was stopped by the form's "One defensible answer" check (no run). q01 rev 2 (4e4615e2...) asked the same thing as a percentage of the year's growth and was blocked again (both form solvers 55%). q01 rev 3 (4bfe9546...) names the half by ANZ's pilot again and keeps the percentage form (45%, Docs 2, 3, 4); quick test too easy (user chat 2026-10-12). q01 dropped |
| i07 | [sketches/i07.md](sketches/i07.md): Kiwibank home lending growth "in its last completed financial half-year before its owner announced a $225 million capital injection"; $0.5 billion; Docs 3, 4 | h1 | 0.6 belongs to the half completed 31 December 2022; a later half was completed 30 June 2023, before the 1 August 2023 announcement (Doc 4 fn 4). Doc 4 = injection date, first-half figure and its dates; Doc 3 = full-year figure | quick test survived (user chat 2026-10-12: "survived"). Promoted unchanged to [q02](../questions/q02.md) rev 0 (a4f09e88...): difficulty Run 2 "Answer not supported", Low 0/5 · Medium 2/5, high model 0 of 3 with every document. q02 rev 1 (64ce77d2...) added "stated or implied": quick test too easy (user chat 2026-10-12) |
| i08 | [sketches/i08.md](sketches/i08.md): the same growth "in the half of its financial year that last ended before its owner announced a $225 million capital injection"; $0.5 billion; Docs 3, 4 | h1 | one reading (a July-to-June year has two halves; the one that last ended before 1 August 2023 is January-June 2023); no call for a calculation. Necessity as q02 | quick test survived (user chat 2026-10-12: "survived"). Written into [q02](../questions/q02.md) rev 2 (e0d20bd4...): difficulty Run 3 "In band — Medium tier", Low 0/5 · Medium 2/5; submitted at Medium 2026-10-12 (user report). My note that Easy was likelier was wrong |
| i01 | [sketches/i01.md](sketches/i01.md): the same growth "in the first half of calendar 2023"; $0.5 billion; Docs 3, 4 | h1 | "calendar" excludes the fiscal first half (0.6). Both documents supply their own figure | offered for quick test (middle wording). Mechanical screen clean |
| i02 | [sketches/i02.md](sketches/i02.md): the same growth "in the six months to 30 June 2023"; $0.5 billion; Docs 3, 4 | h1 | as i01, no "first half" keyword | offered for quick test (most explicit wording; control) |
| i04 | [sketches/i04.md](sketches/i04.md): BNZ vs ASB share of active personal customers doing no digital banking; 8.1 percentage points; Docs 3, 4 | h7 | 87.9 is "enabled" over all customers; 71 is over-65s. Each bank's figure only in its own document | offered for quick test, lower prior (two lookups and a subtraction) |
| i05 | [sketches/i05.md](sketches/i05.md): named farm lenders that reach the switching arrangements only through an agent; Rabobank and Heartland Bank; Docs 6, 2 | h2 | TSB unstarred; SBS and NBS starred but not farm lenders. Lists exist only in their own documents | offered for quick test, lower prior (two-list intersection) |
| i03 | [sketches/i03.md](sketches/i03.md): which fintech Consumer NZ called absent had launched, and how many days earlier; Revolut, 66 days; Docs 5, 3 | h3 | Doc 5 is replaceable by a guess (shared 7 September date; one fintech with a launch date) | held, not offered |

Set decisions: i06, i01 and i02 are one answer path with one gold; they are a wording ladder (least to most explicit)
for the quick test, and at most one is written up. Rule from aq-02673 q05: write up the most explicit wording that
survives the quick test. i04 and i05 use different relationships and document pairs.

Ambiguity: competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes searched
-> what is lost without it. Details per sketch are in the linked files.

One focused repair per distinct observed failure; a repeated failure means change the hook. The Kiwibank hook is the
only cross-document period relationship with unambiguous inputs in this bundle (hooks.md h8-h11 record the others
and why each is closed).
