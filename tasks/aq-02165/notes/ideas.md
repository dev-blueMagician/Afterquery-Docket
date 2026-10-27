# aq-02165 - lean candidate sketches

Current target: medium (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."; page: Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests); hard where a design
supports it. Measured platform success pending. Origin of all sketches: claude (Opus 5.5).

Sources are byte-identical to tasks/aq-02102, where a response-share question and a union match-then-exclude list were
both quick-test "too easy". Families closed here: response statistics, union membership lists.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | n1: years between the earliest employer-funded top-up age under the 2017 proposals (SPA - 10, Doc 5) and the MOD-funded MDP pension age (SPA - 3, Doc 2): 7 | Decoys 5 (Home Office police NPA 60, same Doc 2 extract), 9/8/10 (age 55 held fixed against an assumed SPA), 10 (alpha NPA). Each rule has one source (greps). Risks: reading of "State Pension Age" as the member's own; constructed comparison; small integer | q01 rev 0 quick test "too easy" (user, 2026-10-08); dropped, family n1 closed |
| i02 | [sketches/i02.md](sketches/i02.md) | n2: classic WPS 1.5% (Doc 4) as a share of the 2021/22 rate on £60,000 (7.35%, Doc 1's rolled-over table): 20.4% | Decoys 16.9% (WPS on top), 27.5% / 18.6% (wrong band). One source each. Risks: recallable rates; two lookups plus one division | round 2 quick test "too easy" (user message 2026-10-08, verbatim: "i03 and i02 are all easy to pass quick test" (no screenshot)); dropped |
| i03 | [sketches/i03.md](sketches/i03.md) | n7: the 2023 papers' missed-election rule (only taper-protected mixed benefits change, Doc 3 4.8 / Doc 4 4.45) applied to the 2016 counts in Doc 1/2 Table 1: 54,807 | Decoys 222,424 (deemed election for all-alpha service read as a change), 105,875, 277,231. Groups "Doc 1 or Doc 2" and "Doc 3 or Doc 4". Risk: plain rule sentence (lookup profile) | round 2 quick test "too easy" (user message 2026-10-08, verbatim: "i03 and i02 are all easy to pass quick test" (no screenshot)); dropped |
| n3-n5 | [hooks.md](../notes/hooks.md) | consultation-length range 27 days; 2010 disability bridge 7.6%; £80,000 contribution £5,880 | plainly dated or single-bridge lookups, or contrived bridges | parked |
| n6, c1 | [hooks.md](../notes/hooks.md) | draft vs final 2023 rules; aq-02102 families | one-document final rule; measured too easy | rejected / closed |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
