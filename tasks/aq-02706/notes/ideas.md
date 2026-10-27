# aq-02706 - lean candidate sketches

Current target: medium (hard welcome; no Easy slot per the user, 2026-10-10); measured platform success pending.
Round 1 (2026-10-10): caller hooks h1-h10 plus two question-author runs (lane A rule-application scenarios,
lane B derived world facts and qualitative levers). All sketches origin claude. No local model checks run and
no tier predicted.
Round 1 result (user chat 2026-10-10, "both are too easy to pass quick test"): i01 / q01 and i02 too easy.
Round 2 (2026-10-10): one new mechanism, an untied edition trap (i04 -> q02).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [questions/q01.md](../questions/q01.md) (lane A sketch, caller-edited wording) | h4: one bank profile run through the OCC's covered-community-bank rule (D07) and the FDIC's proposed branch processing (D04); four cells, total 14 moves | Competing totals 26, 13, 1, 0, 2 each fail a stated condition through a document rule (relocation definition D04 L544; "regardless" D04 L244; financial-condition qualifier D07 L286). D07 only source of the covered-community-bank definition and its extension to branch and main-office filings; D04 only source of test (5), the composite-rating track and the relocation definition. One implausible double error also totals 14 (q01 Lever checks). | promoted to q01 rev 0 (258ac5e3...); quick test "too easy" (user chat 2026-10-10, no panel); q01 dropped, family h4 closed |
| i02 | [sketches/i02.md](sketches/i02.md) (lane B sketch) | h11: merger applications per small entity, 2022 to 2023, with each year's count from the edition sized at that year-end: 48.03% | 50.00 (one count for both years), 47.78, 45.73, 49.18 fail "sized on December 31 of each year" or "small entity". D01 only source of the yearly counts and the end-2022 count; D02 only source of the end-2023 count (interpolation gives 47.95). Constructed measure; the question names the tie. Sketch screen: quotes found, 13 deep-number warnings (expected form false alarms if written up). | quick test "too easy" (user chat 2026-10-10, no panel); dropped, a tie named in the question points at the right footnote |
| i03 | lane A fallback, not saved as a sketch file | h4 variant: a covered community savings association and a State nonmember affiliate each open 12 branches (one in the District of Columbia) and shift 5 onto adjoining lots; applications or filings required = 13 | Unit "applications or filings" arguable (FDIC advance notices, the association's published notice): 18 defensible. "District of Columbia" and "adjoining lots" point at the two exceptions. Same frame and document pair as i01. | held; do not use beside i01 |
| i04 | [questions/q02.md](../questions/q02.md) (caller, round 2) | h12: the Office of Advocacy's comment is reported only in the final rule (D02), which restates it with its own August 2024 count (636); the count current at the comment is the proposal's (D01, 661); less the final rule's 78 = 583 | 558 (D02's count) fails "then counted": D02 fn 49 dates 636 to August 18, 2024, after comments closed April 15, 2024 (D01 L40). 623 (proposal's 38) fails "final rule's estimate of small institutions". D01 only source of 661 and the deadline; D02 only source of the comment, 78 and the data date. Stated risk: D02's own sentence applies 636 to "the proposed rule", so a solver or reviewer may hold 558 defensible. | q02 rev 0 (1fabf5a4...): difficulty Run 1 "Answer not supported", Low 1/5, high model 558 x3 (index P3). Rev 1 (f6fbc210...) asks for "the count the OCC had published by then": difficulty Run 2 "In band - Easy tier", Low 3/5 (index P4). Below target; no fair route to Medium on this hook |

Not sketched (reasons in hooks.md): h1, h2, h8, h10 are labelled figures plus one operation; h3 and h9 have two
defensible answers; h5 rests on D07 presupposing paragraphs D02 removed; h6 states its exception in the question's
own concept; h7 gives the same number under either agency. Lane B also examined and dropped: three-edition decline
rates, estimates as a share of small entities, the reputation-risk category lists, D06's ten-year sums (single
document), OCC/FDIC 2024 policy asymmetries (binary or agency-name answers).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
