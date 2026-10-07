# aq-00949 - lean candidate sketches

Current target: medium for new work (user, 2026-10-05, after q04's Easy pass: "at least Medium");
q04 keeps its easy target. Measured: Easy met by q04 (Low 3/5, user report); Medium not met.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (2026-10-05): question-author (origin: claude) returned three sketches; the caller
verified every input line in text/D05-D07 and D01/D03 and ran the mechanical screen.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1: classification inferred across two editions | First calendar quarter with Bahrain crude output, then first with UAE crude output -> "4Q 2025, then 2Q 2026" | D06 79 (Other International crude row), D06 125 (note B: Bahrain); D07 79, 123 (note B: UAE and Bahrain), 923 (2025 Bahrain) | Same series, right edition: D07-only reading of note B over 2026 gives "4Q 2025, 1Q 2026". Mentions vs does: D05 123 names Bahrain in 3Q25 for gas only, giving "3Q 2025, 2Q 2026" | Gaps near rows are numeric volume tables; "—" also prints for FY25; latest-edition heuristic reaches the UAE part without D06 | screen pass; promoted to q01. Rev 0 checked, then the platform form warned the two-part answer had no stated order; rev 1 ("Give the two quarters in that order.") checked: A/B match, closed-book miss (each half guessed once across two runs), audit clear, review ready/easy (marginal), 200 gaps assessed irrelevant. Then dropped at the user's request: the platform's document check judged Doc 7 alone sufficient (jump guess); quarter-pair answer parsed as a list |
| i02 | h2: date bridge into an edition-unique EPS walk | Volume effect on diluted EPS in the quarter after the payable quarter of the $1.02 dividend declared with the Encino agreement -> -$0.11 per diluted share | D03 47 (payable October 31, 2025); D06 479-487 (4Q25 to 1Q26 walk, volume step (0.11)) | Scatter the pieces: declaration-date route gives +0.32/+0.33 (3Q25 walk); 2Q26 walk +0.14 | Overview prints October 31, 2025; lookup chain; D07 MTM step also prints (0.11) | screen pass; promoted to q02 (2026-10-05) after q01 was dropped: wording "In the calendar quarter after the one in which that dividend was payable ...", same-label decoy walk in D07 (+0.14). q02 checked rev 0 (A/B match, closed-book miss, audit clear, review easy marginal), then platform quick test: solved too easily, "answer from only Doc 6" (user report). Dropped |
| i03 | h3: threshold bridge into an edition-unique EPS walk | Volume effect on GAAP diluted EPS in the first quarter (Mar 2024-Jun 2026) whose quarter-end GAAP debt ratio exceeded the end-2019 level -> +$0.32 per diluted share | D01 41 (19%), D05 675 (20.3% at Sep 30, 2025), D05 473-481 (walk volume step 0.32) | Scatter the pieces: net-debt route points to Dec 31, 2025 (no walk); adjusted walk 0.33 | Overview prints Doc 1's 19%; same family as i02 | screen pass; held as fallback; do not spend a platform test on both i02 and i03 if one fails |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.

Rejected in round 1 (author and caller; reasons in hooks.md h4-h10): Encino announcement date
into the 2Q25 walk (public date; Encino first appears in D04), Goldman/Bapco entity bridges (one
source plus public knowledge), Encino cost treatment by measure (one document), old vs new free
cash flow definition (D04-D07 restate it), Rocky Mountain write-down quarter (duplicated,
"primarily"), D01 vs mid-2026 comparisons (lookups; 13% vs 12.70% flips one-decimal answers),
recomputing the missing 3Q25-to-4Q25 walk (method would need stating), effective tax rate vs the
walks' 22% (no individually necessary document), walk rankings/sums and platform idea 1
(exhaustive lookups), platform idea 2 (D07 repeats the 2026 note), MMBoe sums (hidden tables print
them), WTI method change and China dropped (duplicated or guessable).

Round 3 (2026-10-05, complete capture; caller origin: claude). Hooks h12-h18 in notes/hooks.md.
The full statements repeat every 2025 quarter in D06 and D07, so sketches anchor on facts only
D01, D03 or D07 (2Q 2026) hold.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i04 | h12: D01 funding test applied to D07 quarters | Quarter 1Q25-2Q26 where the cash measure named in the March 2020 plan fell short of capital spending plus dividends -> 2Q 2025 | D01 35 (CFO to fund capex and dividends; capital plan excludes acquisitions); D07 278, 285-286, 297, 744 | Definition applied; exclusion of acquisitions. FCF route or capex-only -> none; Encino-inclusive spending -> 2Q25 and 3Q25; with buybacks -> 1Q25, 2Q25, 4Q25 | 2Q25 is also the lowest-CFO quarter (lazy heuristic lands on gold); funding test guessable without D01 | mechanical screen pass; overview mentions CFO funding of the plan only (decoy direction); closed-book screen (singular-wording draft) missed: "4Q 2025 (best guess)", low confidence, recalled the measure as discretionary cash flow and took a free-cash-flow route. Promoted to q03 rev 0 with "quarters ..., if any" wording; prepared 106680fc. Rev 0: A/B match, closed-book miss (named 2Q25 conditionally), audit clear, review ready / easy marginal / high too-easy risk (wording named the measure and scope). Rev 1 (29 words, cues removed), 9a58bd16: A/B match, closed-book miss ("None", did not name 2Q25), audit clear, review ready / easy marginal / too-easy risk moderate to high. Rev 2 (user-reworded reasoning, one sum per step) 1e66a974 checked. Platform difficulty check Run 1: "Too easy", Low 5/5 (all quoted the Doc 1 rule sentence). Dropped |
| i05 | h14: investor contact at both events | Neel Panchal | D01 51-59; D03 65-75 | Who belongs where; Ehmer decoy (media only in 2025) | Trivia risk | mechanical screen pass; closed-book screen recalled the gold from memory ("Neel Panchal", medium confidence, Ehmer set aside as media): general-knowledge exposure. Dropped |
| i06 | Exact table vs rounded prose: D01 end-2019 debt (table 5,175; prose "$5.2 billion") to D07 June 30, 2026 debt (7,926) | Growth to one decimal -> 53.2% | D01 41, 165-167; D07 834 | Prose route 52.4%; net-debt reading -4.1% | Answered-inconsistently risk if a grader accepts the prose input; labelled lookups (too-easy risk) | mechanical screen pass; backup for q03; closed-book screen missed: "About 35.3%" (low confidence; recalled end-2019 debt 5,175 exactly, estimated June 2026 debt at about 7.0B; alternative 45-50%), so the end-2019 input is public but the answer is not. Promoted to q04 rev 0 (prepared 9c195ffc) after q03 failed; q04 rev 2 (ratio form, 153.2%) passed the platform difficulty check in the Easy tier, low model 3/5 (user report, 2026-10-05) |

Round 4 (2026-10-05, target medium, fresh re-read; caller origin: claude). Structural limit: no
outlook/guidance editions, no restated figures except the 2026 PRM fold-in, every 2025 value in both
D06 and D07, walks rebuildable from later per-Boe tables. Unique anchors: D01, D03, D07 (2Q26, H1
2026, June 30, 2026), D05 (Sep 30, 2025 PRM split). Golds below recomputed by script. None promoted.

| ID | Mechanism | Question and provisional gold | Inputs | Decoys / wrong routes | Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| i07 | Exact table vs rounded prose, two inputs plus a scope trap | Percentage-point rise in cash as a share of total debt, Dec 31, 2019 to June 30, 2026, one decimal -> 22.7 | D01 41 ("$2.0 billion", "$5.2 billion"), 165-171 (5,175; 2,028); D07 186/834 (4,907; 7,926) | prose cash 23.3; prose debt 22.9; both prose 23.4; long-term debt only 22.9; both prose + LTD 23.7 | q04's lever (Low 3/5); prose cash and debt sit in one sentence, so the errors are correlated; shares 5,175 with q04 | platform quick test (user screenshot, 2026-10-05): "Survived — worth writing up"; promoted to q05 rev 0 (only sketch whose two documents both survive a removal test); rev 0: A/B match, closed-book miss, audit clear, review revise / easy (one prose decision, same lever and sentence as q04) |
| i08 | Unprinted gearing ratio vs the printed net-debt ratio | Percentage-point fall in net debt as a share of stockholders' equity, Dec 31, 2019 to June 30, 2026, one decimal -> 5.1 | D01 163/177 (21,641; 3,147); D07 833/836 (31,864; 3,019) | printed net debt-to-total-cap 4.3; computed net-debt ratio 4.0; prose net debt 3.2B -> 5.3 | Four labelled lookups; the decoy only catches a misread of the asked ratio | quick test: "Survived — worth writing up"; held (weaker trap for careful models) |
| i09 | Bridge method applied to an unbridged pair (YoY) | Volume effect on GAAP diluted EPS from the Encino-agreement quarter to a year later, EOG's bridge method -> $0.94 | D03 13/47 (May 30, 2025); D07 162 (103.2, 128.3), 612 (25.51), 645 (529) | D07's sequential walk 0.14; basic shares 0.95; margin excl. exploration 0.97; 2Q25 margin 0.55; no tax 1.21 | D07's walk is a copyable template; 2Q25 is guessable from the series' 2Q25 Encino costs, so D03 may fail the removal test | quick test: "Survived — worth writing up"; promoted to q06 rev 0 after q05's review (user choice); rev 0: A/B match, closed-book miss (recalled the date), audit clear, review revise / easy (Doc 3 inferable and recalled; $0.95 daily-rate split; q02 family) |
| i10 | Event-document forward value as decoy (aq-00964 shape) | Dividends per share declared in the four calendar quarters after the quarter of the $4.08 indicated-rate announcement -> $3.06 | D03 47 ($1.02, $4.08); D07 85 (3Q25 dash; 1.0200 x3) | indicated rate 4.08 (4 x 1.02); dash misread | Decoy is a different concept from "declared"; the 2Q25 anchor is inferable from 2Q25's 1.9950 | quick test: "Survived — worth writing up"; held: 2Q26's 1.0200 is guessable without D07 and the anchor is inferable without D03 |

Round 5 (2026-10-06, target medium, after q04 rev 5 "Too easy" Low 5/5; caller origin: claude).
A search for material earlier rounds had not used found no sketch worth promoting:
- Forward-looking series data: none. No hedge-position tables (only mark-to-market gains and
  settlements), no guidance, no outlook, no ROCE/EBITDA method in D07.
- D03 claims (275,000 Boe/d pro forma Utica output, 9-10% accretion, $150 million synergies, the
  "less than one times debt-to-EBITDA at $45 WTI" target) have no measurable actual counterpart.
- The "5%" dividend headline vs (1.02 - 0.975) / 0.975 = 4.62%: 0.975 sits beside 1.02 in D07's
  dividends-declared row, and the May 2025 raise is public (closed-book).
- The 2026 PRM recast ("Other" 452 vs 469 at Sep 30, 2025): asking for the line gives two
  presentations of one item, so two defensible answers; the PRM split alone is a one-document lookup.
- Dividends payable / $1.02 implying a share count: a figure the documents never connect.
- Walk sums across the D06 and D07 bridges: two labelled lookups plus a sum.
- Net-ratio threshold (only Dec 31, 2025 exceeds end-2019's 13%) into the D06 walk: the i03/q02
  family, and the end-2019 ratio is recallable.
q04 rev 5's result also removes the rounded-prose lever (q05's lever, held by the other session).
Structural conclusion unchanged from round 4: every individually necessary input outside D06/D07
is a pre-cutoff fact that models recall (5,175; the Encino funding; May 30, 2025), and the
editions carry no forward values, so the edition trap behind this workspace's Medium/High passes
has no material here.

Round 5 write-up (2026-10-06, user: "stay here"; caller origin: claude). The best remaining long
shot, chosen for its decoy: i10's mechanism re-anchored on a fact only D03 states.

| ID | Mechanism | Question and provisional gold | Inputs | Decoys / wrong routes | Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| i11 | i10 re-anchored: declaration quarter of the dividend with the October 17, 2025 record date (D03 only), then the four following quarters' declarations (D07) | Dividends declared per share over the four calendar quarters after that declaration's quarter -> $3.06 | D03 13/47 (May 30, 2025; $1.02 "today declared"; record October 17, payable October 31, 2025); D07 85 (3Q25 dash; 1.0200 x3; 2026 YTD 2.0400) | $4.08 indicated annual rate printed beside the anchor; $4.035 (counts the declaration quarter); $3.99 (calendar 2025); $5.055; record/payable-quarter anchor runs past the bundle | Removal: D03 inferable from 2Q25's 1.9950 and the Jun 30, 2025 dividends payable 1,081; D07's 2Q26 1.02 assumable from D06 | mechanical screen pass (sketch_sha256 22b2efab...); promoted to q07 rev 0 (target medium), prepared d366d025...; A/B match ($3.06), audit clear (difficulty risk: the window equals D07's last four quarters), closed-book REACHED $3.06 (recalled the deal-day declaration, assumed $1.02 thereafter). q07 dropped before review |
