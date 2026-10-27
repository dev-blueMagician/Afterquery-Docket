# aq-02780 - lean candidate sketches

Current target: medium (hard welcome; no Easy slot per the user, 2026-10-10); measured platform success pending.
Same seven files as tasks/aq-02706, where three designs were measured on the platform earlier the same day
(two quick-test "too easy", one "In band - Easy tier"); see [hooks.md](hooks.md). Round 1 here (2026-10-10):
caller only, full second read of the sources, hooks h13-h20. All sketches origin claude. No local model checks
run and no tier predicted.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h13: one plan for three institutions run through the OCC's 2026 rule (D07) and the FDIC's 2025 proposal (D04); how many of 16 changes need approval, 9 | Wrong routes 8, 8, 7, 12, 13, 16 each fail a limit stated in a document, not in the question: association's rule covers branches only (D07 L112-113), banks apply (D07 L108), de minimis covers a branch only (D04 L547). D07 only source of the OCC rules, D04 only source of the FDIC exemption. Mechanical screen 2026-10-10: eligible, no failure, one warning (a CFR section number quoted from past character 20,000 of D07; keep section numbers out of the reasoning). 57 words. | promoted to [q01](../questions/q01.md). Rev 0 (f6541c05..., 9 changes): Run 1 "Answerable without the documents", the gold being the sum of the question's opening counts (index P1). Rev 1 (1c342b41..., 4 by the OCC and 6 by the FDIC): Run 2 "In band — Easy tier", Low 1/5, below target; four low attempts OCC 12, all attempts right on the FDIC side (index P2). Rev 2 (8d0a0160..., 3 by the OCC and 7 by the FDIC of 27 changes; the bank's branches replaced by qualifying operating subsidiaries, one added for the association): no run, the form flagged its question text as AI-generated (index P3). Rev 3 (3d92ec69...), rev 4 (2dbe139a...) and rev 5 (9a1c7f69..., origin user+claude): the same content with the question in the user's own wording, rev 5 current at 59 words; checked 2026-10-11, floor 0 FAIL, 2 WARN (origin; revision count); platform pending. A second Easy result closes the hook at Easy |
| i02 | [sketches/i02.md](sketches/i02.md) | h14: of the filings one FDIC-supervised bank's plan needs, how many stand approved if the FDIC never acts, 3 (D03 x D04) | Wrong routes 4, 6, 7, 2. D03 only source of "does not constitute an automatic or default approval" (one hit); D04 only source of the three-business-day rule. Weak point: a solver may assume the merger rule without D03. Mechanical screen 2026-10-10: eligible, no failure, one warning (a CFR section number quoted from past character 30,000 of D03). 51 words. | active: quick test only, second choice; do not use beside i01 as a question |

Not sketched (reasons in hooks.md): h15 and h20 rest on D03 thresholds a model can recall and on a guessable
carve-out; h16 is two public dates and a gap; h17 has no noun that fits all three counts; h18 has an arguable
definition and a printed answer; h19 is single-document. The families closed on aq-02706 (h4 count of
expedited moves, h11 edition-aligned ratio, h12 edition trap) are not reopened: h13 changes h4's dependency
from eligibility tests the question names to the reach of three exemptions, which is the one focused repair
that family gets.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
