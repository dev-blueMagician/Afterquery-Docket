# aq-01322 - lean candidate sketches

Current target: medium (user, 2026-10-06: "you should do difficulty_target to at least medium").
Measured platform success pending. Task page: Hard 0/2 · Medium 0/3 · Easy 0/1 slots open,
quick tests 0 of 10 used, 8 of 8 difficulty runs, 9 submissions left.

Local ids: D01=Doc 4, D02=Doc 1, D03=Doc 5, D04=Doc 2, D05=Doc 6, D06=Doc 3.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1 untied edition trap (aq-00745 q09 / aq-00964 q01 family) | Other's FY26 adjusted OI growth in the guidance in force at the U.S. Consulting divestiture -> Flat | D05 L81 April 2026; D01 L17 Feb 4 + L114 Flat; decoys D03 L123, D05 L118, D06 L138 | right edition; decoys E3/E4 same label, post-event | pipe-row answer; plainly dated month | screen pass; promote as q01 (wording mirrors aq-00964 q01: group identified through the event) |
| i02 | h1 sibling (consolidated revenue row) | revenue growth range in force at the divestiture -> 7% to 9% | D05 L81; D01 L17, L107; decoys D03 L116, D05 L111 (4-6%), D06 L131 (5-7%) | right edition | sibling of i01 (one submission only) | screen pass; keep for quick test as i01's alternative |
| i03 | h4 restatement carve-out | margin of operations moved out of U.S. segment, Q3 FY25 -> 4.4% | D04 L423/L431; D05 L456/L465; decoy D05 L490 Other 4.13% | calculate across documents; printed answer-shaped decoy | question names the restatement (route signposted) | screen pass; promote as q03 (user-preferred derived-numeric shape) |
| i04 | h3 method applied to unreported period | calendar-2025 adjusted FCF -> $3.38 billion | D06 FY25 prose; D01 L200/L404/L406/L469 | method application, calendar alignment; near misses 3.36/3.39/3.41/5.82/2.97 | shares D01 Q1 FY26 input with i05; closed-book estimate risk | screen pass; quick-test alternative to i05 |
| i05 | h2 period identified by a fact + YTD | adjusted FCF in the quarter OneOncology closed -> $1.16 billion | D03 L639 Feb 2, 2026; D03 L686 6M; D01 L469 Q1 | period by fact; two printed same-label decoys (Q1 in the announcing release; six-month) | YTD transform known; date plain in D03 | screen pass; promote as q02 |

Closed-book sketch screens (fresh closed-book-solver, question text only), 2026-10-06:
- i02: "Revenue growth of 7% to 9%" (low confidence; believes the November 2025 initial guidance
  was 7-9%, which is actually E2's value). Reaches the gold: dropped (fails "Needs the documents").
- i04: "about $3.40 billion (a rough estimate)" (low confidence; built calendar 2025 correctly as
  FY25 - Q1 FY25 + Q1 FY26 but guessed every input). Gold $3.38 billion: near miss, exposure risk;
  stays a quick-test alternative only.
- i01: "Growth of roughly 3% to 7% in Other's adjusted operating income ... a guess" (low; recalls
  the November 2025 EPS range $17.45-$17.75 but not Other's row, the sale date or the edition).
  Misses the gold (Flat).
- i03: "About 3.5% ... a guess" (low; describes the original-minus-restated method, guesses an
  MWI-type margin). Misses the gold (4.4%).

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.

Promotion and check results (2026-10-06):
- q01 (i01): rev 0 checks passed and review ready/medium (Medium or better ~55%), but a no-Doc-6
  removal probe forced-guessed the gold (held-for-sale reading of "divested"); rev 1 says
  "completed the divestiture of" (aq-00964 q01 style). Rev 1: A/B match, closed-book miss, audit
  clear, no-Doc-6 probe best answer "High-single digit growth" (Flat only 0.25); review pending.
- q02 (i05): A/B match, closed-book miss, audit clear; review revise for target only, predicted Easy
  (Too easy ~20%, Easy ~60%, Medium ~12%): plain repeated closing date, routine year-to-date step.
  Kept as a fair Easy-slot fallback, not a Medium submission.
- q03 (i03): rev 0 (June quarter) failed necessity: D02 + D06 rebuild the original June quarter, so
  D04 was replaceable. Rev 1 asks January-June 2025 (only D02 has the original March quarter, only
  D05 the restated June quarter); A/B match 5.2%, closed-book miss, audit clear; review pending.
- No second untied edition event exists: OneOncology (D01 ties its update to the closing), MWI and
  EyeSouth agreements undated, Q3 FY26 events span the uncertain May-August EPS window, FY2025
  editions print their own previous ranges.
