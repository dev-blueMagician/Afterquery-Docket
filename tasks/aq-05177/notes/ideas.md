# aq-05177 - lean candidate sketches

Current target: hard (user 2026-10-14: no Easy or Medium slot; page "Hard 0/5 · Medium closed · Easy
0/0"). The check starts at the High model. Measured platform success: none yet.
Design: .claude/memory/reference/hard-playbook.md. Every fair sketch gets a three-solve strong-solver
screen and goes to the user with its result; the screen ranks, never withholds.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: Q4 2023 net cash interest = FY 38.3 (D04) - 9M 41.7 (D03) = -3.4 -> -$3M; lure the Q4 "cash paid" 5.6 (D04) | readings: gross 5.6 fails "after swap settlements and interest earned"; one-decimal routes split -3.4/-3.3, so nearest million. Necessity: D04 sole FY source; D03 replaceable by D05+D06+D07 comparatives | screen 3/3 right; quick test survived with my long answer text, failed with the bare answer (user 10-15, item C); q05 dropped; ledger row 24 |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: first 2024 IC revenue range 1,650-1,700 (D06 less Aug +10 and May +25, D05); same-business 2023 base 1,604 - 37.1 (D04); bottom implies 5.3%; lures 8.0% (analyst "8% to 8.5%"), 2.9%, 6.9%, 7.5% | readings named in the sketch, each failing "first", "bottom" or "businesses that made up that segment in 2024". Necessity: D04 sole base source; D06 range; D05 supporting (width route) | screen 3/3 right; quick test survived (user 10-15, item A); q03 Run 2 High 3/3 Too easy; dropped; ledger row 25 |
| i03 | [sketches/i03.md](sketches/i03.md) | h3: besides revenue, ranges increased at all three 2024 updates = 3 (IC EBITDA, capex, FCF); lure 2 (the CEO's "revenue, Adjusted EBITDA, and free cash flow") | decoys cash interest (lowered), DH R&D (not August), DH EBITDA (May only). Asked as a count: an alphabetical list flips with item naming | screen 3/3 right; quick test survived with my long answer text, failed with the bare answer (user 10-15, item B); q04 dropped; ledger row 26 |
| i04 | [sketches/i04.md](sketches/i04.md) | h11: updates that changed a Digital Health range = May and November; lure May only (November "substantially the same") | decoy August ("all remain the same"); D05 frames R&D as a guidance range | screen 3/3 right; quick test survived (user 10-14, item 2); written up as q02 rev 0, checked; ledger row 27 |
| i05 | [sketches/i05.md](sketches/i05.md) | h12: partners in the seven-center venture formed at the Q1 2024 close: Cedars-Sinai, Providence; lure Providence only (D05's formation sentence) | Cedars appears only in D07's passing "three-way" mention; formation-time reading named as a risk | screen 3/3 right (one solve medium confidence); quick test survived (user 10-14, item 1); written up as q01 rev 0, checked; ledger row 28 |
| i06 | [sketches/i06.md](sketches/i06.md) | h4: 2024 de novo shortfall vs the May plan (2 opened + 12 to open) = 14 - 9 = 5; lure 3 (12 - 9, or March's dozen) | D05 sole source of the May plan; D08 sole source of nine | screen 3/3 right; quick test not among the survivors (user 10-15, item D); ledger row 29 |
| i07 | [sketches/i07.md](sketches/i07.md) | h12 repair of q01 rev 0 after the form's "One defensible answer" block (both form solvers: Providence only): adds the structural scope "Judging by RadNet's 2024 earnings calls together" | single reading; no cue to a passage or member (precedent aq-03170 rev 4) | screen 3/3 right (all high confidence); q01 rev 1; quick test too easy (user 10-15); hook h12 dropped, q01 dropped; ledger row 30 |
| i08 | [sketches/i08.md](sketches/i08.md) | h11 form repair of q02 rev 0 after its Checks: "change any guidance range" (Partial answers), answer "May, November" (stated-figure row read year digits) | One defensible answer passed on rev 0; meaning unchanged | screen 3/3 right; written up as q02 rev 1, checked; ledger row 31 |

Round 1 (i01, i02): both 3/3. Round 2 (i03, i04: condition over every item; hedge): both 3/3. Round 3
(i05 incidental attribution, i06 plainest reading): both 3/3. Three unproductive rounds: all six handed
over ranked. User quick test (10-14): i05 and i04 survived; i01, i02, i03, i06 not tested. Still held: h5 (2024 quarters with a
sequential AI-revenue fall), h9 (2023 AI revenue vs the guidance reaffirmed in May). Dropped: h6-h8, h10 (weak lure or
two defensible answers from transcript inconsistencies).

Keep facts/checks in the linked sketch. Ambiguity: competing answer -> wording condition it fails.
Necessity: source -> unique input -> substitutes searched -> what is lost without it.
