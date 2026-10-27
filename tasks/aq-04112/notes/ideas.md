# aq-04112 - lean candidate sketches

Current target: medium, hard open too (user, 2026-10-13: "no slot for Easy Tier ... target medium and
high"). Page at intake: quick tests 0 of 15, difficulty runs 15 of 15, Hard 0/3 · Medium 0/2 · Easy 0/0.
Measured so far: quick tests 2026-10-13 (user chat, verbatim "i02, i01 survived. others not tested"; no
panels); difficulty Run 1 on q02 (= i02), Version 402a46: "Too easy", Low 4/5, run returned ("15 of 16 runs
left"); quick tests of round 2 (user chat, verbatim "i06 survived, i07 failed"; no panels); difficulty Run 2 on q03
(= i06), Version baa047: "Too easy", Medium 4/6, the check starting at the medium level.

Doc numbers are the task page's (Doc 1 = D03 report, Doc 2 = D01 hearing of 26 October 2021, Doc 3 = D02
hearing of 9 November 2021). Sketch round 3 of 3 (i10).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: Association of Labour Providers' unit costs (Doc 1 Table 3) applied to the 150 staff Nick Allen's example plant lacks (Doc 2 Q70). Gold £1,273,150. | Other readings: three times the 50-worker total (£1,275,150), the application charged per worker (£1,422,150). "Unit costs" keeps the Association's rounded £2,834 rate out. Doc 1 alone has the costs, Doc 2 alone the head count. One unpointed step: the sponsor application does not scale. | Quick test survived (rev 0 sentence). Written up as [q01](../questions/q01.md); rev 1 drops "one company" (checked, 0 FAIL, 5 WARN, fingerprint e21fa8ca...). Rev 1's sentence then survived its own quick test ("i06, q01 survived, i03 failed"). Difficulty Run 4 on rev 1 (Version cfc84c): "Too easy", High 3/3, the check going straight to the high model. Dropped; hook h1 closed. |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: a butcher's starting salary against the threshold the Migration Advisory Committee's advice would have produced. Gold £6,020. | Run showed no step holding: all five low attempts found both figures and the 20% rule from the named advice. | Dropped. [q02](../questions/q02.md) Run 1 "Too easy", Low 4/5; one wrong answer, £900. Hook closed. |
| i03 | [sketches/i03.md](sketches/i03.md) | h3: one skills scheme said at both hearings to leave a sector out. Gold "The lifetime skills guarantee, poultry and hospitality". | Decoys T-levels, apprenticeship levy, plan for jobs. Each transcript holds one half. Delete-and-guess: either transcript gone, one sector is missing. | Quick test failed (user: "i03 failed"). Dropped; hook h3 closed. |
| i04 | [sketches/i04.md](sketches/i04.md) | h4: the NFU witness's two forecasts against visas issued. Gold 15.4. | Delete-and-guess, Doc 2 gone: Doc 1 para 30 points to butchers and the other scheme is a one-in-two guess. Every step pointed. | Withdrawn 2026-10-13. |
| i05 | [sketches/i05.md](sketches/i05.md) | h5: most seasonal visas signalled for 2022 against the NFU's own top figure. Gold 66.7%. | Delete-and-guess, Doc 1 gone: the 2022 allocation is a published headline figure and Doc 2 names the 30,000 pilot, so the gold can be reached. | Withdrawn 2026-10-13. |
| i06 | [sketches/i06.md](sketches/i06.md) | h14: witnesses who put a figure on training time (Doc 2 Q7, Q73; Doc 3 Q137). Gold Charlie Dewhirst, Nick Allen, Tom Southall. | Other lists: Allen left out (awkward sentence), Wright or Nicholls added (their "18 months" and "two-year" are not training times). Either transcript gone, a member is lost. | Sketch sentence survived one quick test. [q03](../questions/q03.md) rev 0 changed the opening and the order phrase at write-up; the user quick-tested that sentence and it failed ("q3 failed to pass quick test"). Rev 1 (draft) restores the sketch sentence word for word. The exact sentence survived a second quick test ("i06, q01 survived, i03 failed"). Difficulty Run 2 on q03 rev 1 (Version baa047): "Too easy", Medium 4/6, check started at the medium level. Dropped; hook h14 closed. |
| i10 | [sketches/i10.md](sketches/i10.md) | h16: organisations that sent written evidence but no witness (Doc 1's two lists) and were named at either hearing. Gold Association of Labour Providers, Kernock Park Plants, Royal College of Veterinary Surgeons. | Other lists: Defra added ("no witness" read as no witness at the two hearings; its witnesses came on 16 November), Kernock left out (the hearing says "Kernock Plants"), RCVS alone (only witnesses' words counted). Universe of 56 non-witness names checked twice by script. Each document holds a member or the filter. | Screened 2026-10-14, clean (sketch sha 87b722fe...). Quick test survived (user chat, verbatim "survived"). Written up as [q04](../questions/q04.md), sentence and answer word for word: rev 0 checked, 0 FAIL, 1 WARN (origin), fingerprint ca843e5c.... Difficulty Run 3 (Version daf97b): "Too easy", High 3/3, the check going straight to the high model. Dropped; hook h16 closed. |
| i07 | [sketches/i07.md](sketches/i07.md) | h15: witnesses who put a figure in weeks on visa or sponsor processing (Doc 2 Q48, Q52, Q73; Doc 3 Q138). Gold Tom Bradshaw, Nick Allen, Kate Nicholls. | Other lists: Dear added (his "six weeks" is the visa's length), Nicholls left out (a licence, not a visa). Either transcript gone, a member is lost. | Quick test failed (the easier solver answered). Dropped. Its question named the paperwork, which pointed at the member in the second hearing. |

What the run changed (details in q02.md Feedback log): on this bundle the easier solver finds any figure the
question names, follows a named body's advice to the rule it triggers, and reads the question's premise as
the instruction for the method. Designs whose every step is reached from a word in the question are closed
(h2, h4, h5). Left: q01, whose one unnamed step sits inside a table, and lists whose members have to be
searched for without a name (i06, i07, i03).

What Run 2 changed (details in q03.md Feedback log): the check started at the medium level, and every
recorded medium attempt went through both transcripts for training times and found all three members. A
list whose members each carry the asked word beside a number is a scan, however the members are spread.
Left: q01 (unrun) and i10, a match of two lists where the asked property ("named") has no keyword and one
member is named only by a short form in an MP's aside.

What Run 3 changed (details in q04.md Feedback log): the check went straight to the high model, as every run
in the workspace did on 2026-10-14, and the high model found i10's three members three times in three; the
page's note: the lists "pre-compute the set difference, leaving only a literal string match". Three sketch
rounds are used. Left: q01 rev 1, unrun.

What Run 4 changed (details in q01.md Feedback log): q01 went straight to the high model too and was right three
times in three; the notes say it included the one-off sponsor fee and could check itself against the table's
printed 50-worker total. Every candidate on this bundle is now measured below target: q02 (Low 4/5), q03 (Medium
4/6), q04 and q01 (High 3/3). No sketch is left untested; h9 is an unsketched spare.

Rejected with reasons in hooks.md: h6, h7, h8, h10, h11, h12, h13. i08 (the British Meat Processors
Association's share of a total; every step pointed) and i09 were rejected before files were written; i09's
reason was not kept. h9 (MPs who agreed the report and
questioned a named witness) is held as a spare.

Set review: q01 shares nothing with the sketches. i06 and i07 are the same shape on different facts. i10
shares Doc 1's witness list with nothing else live, and names the Association of Labour Providers, whose
Table 3 q01 uses: a solver of both meets the Association twice, but neither answer gives the other.

A survival at the quick test sets no tier: q02 survived and then measured too easy. On a derived answer
"One defensible answer" comes before any run.
