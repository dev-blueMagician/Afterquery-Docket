# aq-02743 - lean candidate sketches

Current target: medium (hard welcome), by the user's instruction of 2026-10-10 ("there is no slot for Easy Tier for
this bundle, we should target medium and high"). Measured platform success pending; nothing here is a tier estimate.
Hooks are in notes/hooks.md. Sketch files hold the quotes and checks; this table holds the decisions.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md): most days HHS's deadline can fall after DOJ's for one public entity, 380 | h1 | Competing 15, 14, 351, 381 fail "at most" / "after" / "extended". Both documents needed. Author finding: earliest-with-latest reaches the gold without the tier insight | Held, not offered |
| i02 | [sketches/i02.md](sketches/i02.md): small town's deadlines just before HHS's rule took effect, 716 | h2 | D03's April 26, 2028 is the public 2024 date plus one year, and D04 says "by one year": D03 not indispensable | Dropped 2026-10-10; replaced by i06 |
| i03 | [sketches/i03.md](sketches/i03.md): DOJ's annualized benefits minus costs on the delayed schedule divided by HHS's, 524% | h3 | Competing 381% (HHS original-schedule pair), 540% (DOJ's rounded $1.3 billion), 1,397% ($90.2 million), 423% (3% tables) each fail a stated condition. D03 alone prints 4,509.5 and 3,249; D04 alone prints 820.3 and 1,061.0. All legitimate HHS routes give 524% | Promoted to [q01](../questions/q01.md) rev 0, checked (0 FAIL, 5 WARN). Quick test 2026-10-10 "too easy" (user chat, no trace): q01 dropped, h3 closed. Caller and both independent authors had reached this design separately |
| i04 | [sketches/i04.md](sketches/i04.md): days from HHS's rule taking effect to a large HHS-funded county's first deadline, 354 | h4 | Competing 369, 350, 352, 371 fail "first" / "took effect" / D03's exact date. Both documents clearly needed. Every tier fact is in the question | Quick test 2026-10-10 "survived" (user chat, one draw, no trace). Promoted word for word to [q02](../questions/q02.md) rev 0. Form Checks on rev 0: "One defensible answer" Failed (the choice of DOJ's date over HHS's read as an assumption). Rev 1 states it ("does any federal rule first require it"), checked; not quick-tested |
| i05 | [sketches/i05.md](sketches/i05.md): two special districts, one with an HHS grant, one paid only under a direct procurement contract, 351 | h5 | Both wrong routes give 0. D04 needed for the date and the definition; D03's date rebuildable from public memory plus "one year" (stated risk) | Quick test 2026-10-10 "too easy" (user chat, no trace): dropped, h5 closed |
| i06 | [sketches/i06.md](sketches/i06.md): a large HHS-funded county's two deadlines just before HHS's rule took effect, 350 | h2 | Competing 17 and 15 fail the timing phrase; 348 fails D03's exact date. D04's operand is the public 2024 date (stated risk) | Not tested (user, 2026-10-10). Superseded by i08 / q03 |
| i07 | [sketches/i07.md](sketches/i07.md): two HHS-funded towns under 50,000 people, one with 15 or more employees and one with fewer, days between their first deadlines, 351 | h14 | Competing 365 (HHS only), 0 (DOJ only), 14 (later date each), 350 (2024 dates) each fail a stated condition. D03's April 26, 2028 is rebuildable from the public 2024 date plus "one year" (stated risk) | Held, not offered: same earlier-of mechanism as q03, which the easier solver tabulates (q03 rev 0 Low 3/5; rev 1 quick test too easy) |
| i08 | [q03](../questions/q03.md): days HHS's rule gained the county before any federal rule required WCAG 2.1, 350 | h15 | Competing 365 (HHS's own extension), 367 (DOJ's superseded date as the start), 15, 17, 348 each fail a stated condition. D03 alone prints April 26, 2027; D04 alone prints HHS's dates and May 7, 2026; the start date is the public 2024 HHS date (stated risk) | Promoted straight to q03 rev 0 (2026-10-10). Difficulty Run 1, Version 90fd80: "In band — Easy tier", Low 3/5, below the open tiers (both wrong low attempts answered 0, "DOJ's date controls"). Rev 1 (2026-10-11): one county in each of the four tier combinations, total gain 1,067 days: quick test "too easy" (user chat, one draw, no trace). Repair retired, h15/h4 closed for the Medium target; q03 restored to rev 0's measured content (Easy pass, usable only in an Easy slot) |

Independent authors' other proposals, not adopted as written:

- Author B's lead sketch: a city of 80,000 and a special district, each with 200 employees and HHS grants, days
  between their first deadlines = 15. Fair, with wrong routes 366 (DOJ only), 0 (HHS only), 351, 17. Not offered: 15 is
  also the plain difference between the two rules' headline dates, as B itself noted.
- Author A's and B's wording of h3 as DOJ divided by HHS at a whole percentage (524%) was adopted over the caller's
  HHS-over-DOJ form; B held the design for its deep operands, the dollar-year caveat and D03 L381.

Quick tests, user chat 2026-10-10, verbatim: "q01 i05 too easy, i04 survived, i06 not tested" (no panels, no traces; wordings
taken as the handed-over ones). Sketch rounds used: 2 of 3 (round 2: q02 rev 1 and i08 after the form block; q03 rev 1 is the one focused repair of i08, not a new round). One focused repair per distinct observed failure; a repeated failure means another hook.
