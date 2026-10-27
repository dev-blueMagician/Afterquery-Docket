# aq-02770 - lean candidate sketches

Current target: medium (user, 2026-10-10: "there is no slot for Easy Tier for this bundle, we should target
medium and high"); measured platform success pending. The capture saved at 20:21 still printed "Hard 0/2 ·
Medium 0/3 · Easy 0/1"; the user's statement is newer and governs.

Hooks are in notes/hooks.md. Origin of every sketch below: claude (i03 was proposed by an independent
question-author run and re-derived by the caller).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md): lowest TE2 for a gas-fired CWAF built at the federal minimum on the day DOE held its public webinar on the proposal to create TE2 (March 29, 2022), part load weighted at NEEA's largest modeled share. Gold 76.0 percent | h1 | Ambiguity: 77.0 (81 base: the documents' example, or a later TE2 event such as the June 2023 final rule or the May 2025 rescission webinar) fails "built ... on the day DOE held its public webinar on the proposal to create TE2", which D02 l.135-136 places under the 80 percent level; 76.5 fails the stated re-weighting. Necessity: only D02 dates the 81 level; only D04 has NEEA's shares (both measured as needed on rev 1); D03 unticked | questions/q01.md dropped 2026-10-11. Measured twice: rev 1 (tied anchor) "In band - Easy tier", Low 3/5; rev 3 (untied anchor) "Too easy", Low 4/5. Hook h1 retired |
| i01 (alternate) | Same hook on DOE's own weighting, gold 76.5 | h1 | Second source "D03 or D04": not individually necessary (aq-02147) | questions/q03.md dropped 2026-10-11, never platform-tested |
| i02 | "If DOE's national impact analysis for oil, electric and weatherized gas consumer furnaces had covered sales over the timeframe DOE says mirrors its rulemaking cycle, from the same first year, what would the last sales year be?" Gold 2038 | h3 | Ambiguity: 2039 (2030 + 9) fails an inclusive count, which D01's own "2030 through 2059" confirms for 30 years; 2027 uses D02's CWAF window. Necessity: D01 gives 2030; D07 gives the nine-year frame, but DOE's nine-year sensitivity is long-standing public practice, so D07 may be recalled; its figure sits at character 89,738 (form number-check flag) | not written up; a spare quick-test sketch at most |
| i03 | Organizations that commented on the April 2022 CWAF proposed determination (D02) and on analytic methods in the April 2025 Process Rule RFI (D07) but not on the December 2024 tentative determination (D04). Gold: American Gas Association, American Public Gas Association, American Council for an Energy-Efficient Economy, Lennox International | h4 | Ambiguity: unit fixed at the member ("filing alone or jointly"); D07's table covers analytic-methods submissions only, so the question says so. Decoys: ASAP (in both lists inside same-named groups, removed by D04), NYSERDA and NRDC (D02's Joint Advocates only), AHRI and NEEA (removed by D04). Necessity: all three documents change the answer when left out (seven names without D04; a different seven without D07) | questions/q02.md dropped 2026-10-11: user's quick test "too easy" (chat report, one draw, no panel) |
| i04 | "In any order, which organizations, if any, that commented on DOE's April 2022 proposal to leave commercial warm air furnace standards unchanged, alone or jointly, did not comment on analytic methods in response to its April 2025 Process Rule request for information?" Gold: New York State Energy Research and Development Authority, Natural Resources Defense Council, California Investor-Owned Utilities | h4 | Ambiguity: unit fixed at the member ("alone or jointly"); D07's table is the analytic-methods list. Decoys: ASAP and ACEEE (in D07's Joint Advocates, so out although their 2022 co-filers stay), AGA and APGA (in D07's Joint Gas Associations under another label), AHRI, Lennox, NEEA. Label-level matching drops the whole 2022 Joint Advocates and keeps AGA and APGA. Necessity: D02 and D07; D04 plays no part | quick-test sketch, the two-document mirror of q02 (three names, so no list-contract advisory). An alternate of q02, never submitted beside it: q02's reasoning states this answer |

Not sketched: h2 (both compliance dates are codified public regulation), h5, h6 (two lookups and one
operation), h7 (rests on a physical identity no document states). The author run also weighed a 683-day gap
(TE2 effective date in D04 to the rescission proposal in D05): fair, two labelled lookups, not promoted.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

## Rounds

- Round 1 (2026-10-10): caller read all seven documents; hooks h1-h7; i01 promoted as q01 rev 0. One
  independent question-author run, given no hypothesis, converged on h1 (oil-fired built in 2024, 78.0, same
  two documents) and named the what-if on weighting as that design's open defect; it also proposed i03. Its
  map correction (D07 Table 1 has 27 rows) is applied.
- Round 1 repair (one focused repair for one observed failure): q01 rev 0's removal probe without Doc 2 was
  "not answerable" unforced but reached 76.0 on a forced guess from memory at p 0.65. Rev 1 anchors the
  manufacture date on an event only Doc 2 reports. q03 added as the no-what-if alternate; q02 written up
  from i03.
- Round 2 (2026-10-11, platform feedback): q01 rev 1 difficulty Run 1 = "In band - Easy tier", Low 3/5, both
  documents needed (feedback-index F1). The re-weighting step separated no low attempt; the tied date anchor
  caught two of five. One focused repair, the anchor: rev 2 (proposal date) still led a blind solver into Doc 2, so rev 3 uses the
  webinar on that proposal, dated only in the TE2 documents. q03 dropped. If rev 3 measures Easy again or
  fails the Document check on Doc 2, the hook is exhausted; do not try a third wording.
- Round 2 result (2026-10-11): q01 rev 3 difficulty Run 2 = "Too easy", Low 4/5 (feedback-index F2). Every low
  attempt dated the webinar and applied the dated rule. h1 retired, q01 dropped.
- Round 3 (2026-10-11): no new numeric hook. Re-examined with the two runs' evidence (the low model resolves
  dated rules and stated what-ifs; it lost attempts only on same-titled look-alike documents): every remaining
  numeric pairing is either a labelled date gap, a recallable codified standard, or needs a Doc 3/Doc 4 twin
  as its second source. The live candidate is q02 (h4), with i04 as its two-document mirror for a quick test.
  Three rounds used: if q02 and i04 both fail, report the bundle as having no Medium design.
- Round 3 result (2026-10-11): q02 quick test "too easy" (user chat, feedback-index F3). q02 dropped. i04 not known
  to have been tested; it is the same mechanism on two tables. Three rounds used. Supported options: (1) release
  the bundle, no fair Medium design found; (2) q01 rev 1 measured "In band - Easy tier" (Low 3/5, both documents
  needed), usable only if an Easy slot counts. Unresolved avenues, none promising: labelled date gaps (683 days,
  TE2 effective date to the rescission proposal), codified standards (recalled), Doc 3/Doc 4 twins as a second source.
