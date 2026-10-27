# aq-01540 - lean candidate sketches

Current target: medium (hard optional; the task page says only Medium can still be submitted); measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (caller, 2026-10-08), after the caller's full read and the mapper's doc-map. Ids vs page: D01 = Doc 6,
D02 = Doc 8, D03 = Doc 7, D04 = Doc 5, D05 = Doc 2, D06 = Doc 4, D07 = Doc 1, D08 = Doc 3.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1: contract-based forum relief; one item is a background transfer in an Anti-Injunction Act opinion | Defendants of the eight decided lawsuits that got a federal court to dismiss or transfer the suit in favor of another court by relying on a contract's terms -> Royal Caribbean; Steven Johnson and his law firm | D04 l.15, l.121-123; D08 l.21, l.42 | Bury one list item late; Mentions it vs does it. Decoys DUAL et al. (D06 denied), OEC (D07 denied), Ofcom (D03 not reached), JLF arbitration request (D08 denied) | single trap; late-item family measured Easy before; cited precedents excluded by the universe phrase; first wording ("relied on ... to have") read as an attempt, fixed to state success; the consent judgment (D05) excluded by "in favor of another court" | screen passed; promoted q02 |
| i02 | new: two-condition filter, both gold items non-salient | Defendants a court said were within its personal jurisdiction even as it dismissed every claim against them -> Lorenzo Vidino; Lewis Machining & Engineering | D02 l.515, l.551; D05 l.80, l.118, l.156 | Match then exclude; Bury one list item late. Decoys OEC India (D07, Part vs total), Shenzhen plaintiffs (D05, plaintiffs; two counterclaims adjudged), jurisdictional dismissals (D02, D03, D07) | two hidden items may make it Too hard; Vidino's jurisdiction is stated, not litigated; Lewis Machining's is a stipulated finding | screen passed; promoted q01 |
| h2/h3 | law applied (breach claim; forum-clause question) | two parallel asks: maritime/Ohio; New York/maritime | D06 l.86, l.188, l.191; D07 l.60, l.344-352; D04 l.58, l.106 | Who belongs where | each gold explicit in its own section (tied); parallel lookups | parked (fallback) |

Rejected hooks and reasons: notes/hooks.md (h4-h16).

Round 1b (independent question-author subagent, Claude Code Opus 5.5, this session, 2026-10-08; returned sketches only, wrote no files;
it read all eight texts in full before the doc-map existed). Bottom line in its words: "I found no design I can defend as likely to
reach Medium." Its estimates are binomial guesses, not measurements.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| a01 | FNC movants dismissed on another ground; OEC India / OEC USA joint-motion mix-up | Wording C: "which defendants that had asked the court to dismiss on forum non conveniens grounds were dismissed on a different ground instead?" -> Ofcom and OEC USA. Wording A (fairer): "whose motions to dismiss included a forum non conveniens request" | D03 l.97, l.250; D07 l.25, l.83, l.204, l.210, l.278, l.449-455 | Match then exclude; Mentions it vs does it. Decoys: Royal Caribbean (dismissed on FNC itself), OEC India (FNC denied; only Count IX dismissed) | wording C: the court calls the FNC request "OEC India's" (l.451, fn 10), so "Ofcom" alone is arguably defensible and both form solvers could take it; wording A names the joint motion's request and is easier. Author: C Medium ~10-15%, A ~3-6% | caller: park; offer for the form's free check plus a quick test only (wording A for fairness) |
| a02 | = caller's i01 / q02 | contract-based forum relief -> Royal Caribbean, JLF Defendants | as q02 | Bury one list item late | author: low model ~60-70% right per attempt, Medium <=5%; critique (Lewis Machining settlement dismissal; "written"; scope to the decided lawsuit) already met by q02 rev 1 | promoted earlier as q02 |
| a03 | = caller's h3 | law each court used for its forum clause -> federal maritime (cruise ticket), New York (cargo policy) | D04 l.58, l.106; D06 l.84-88, l.191 | Who belongs where | tied: each gold opens its own section; Medium <=3% | reject (Easy) |
| a04 | ground on which each ruling rejected a fraudulent-inducement claim | lack of justifiable reliance (5th Cir.), Rule 9(b) particularity (Ohio) | D01 l.168-179; D07 l.418-444 | Does the hedge apply; Mentions it vs does it (concurrence "forfeiture grounds alone"; district court's two findings) | free-text grading; "fraudulent inducement" finds both; Medium <=2% | reject (Easy) |
| a05 | litigants who agreed to give up a defense so a particular court could hear the dispute | Royal Caribbean; the four Shenzhen sellers | D04 l.113; D05 l.165 | Mentions it vs does it (Badal and Besson waived service but kept defenses) | keyword "waive"; Too easy ~55% | reject |

Author's rejected-hook list (28 items) agrees with notes/hooks.md and adds: Exxon v. CIMEX citation link (needs outside knowledge),
D02 Ariaf (named defendant in no count, never ruled on), D05 Motion to Enforce (disposed of only as moot), D01 coverage-part mismatch,
foreign proceedings between the parties (India appeal; Ofcom UK enforcement), D02 + D03 same-day pairing lookups.


For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
