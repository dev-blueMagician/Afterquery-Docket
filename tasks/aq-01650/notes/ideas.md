# aq-01650 - lean candidate sketches

Current target: medium (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should
target medium and high"; page then: Hard 0/2, Medium 0/3, Easy 0/1 with "In review: Easy 1");
measured platform success pending.

Round 2 (2026-10-08, restart under gate v3; user: "first clear work history on AQ-01650 and start
again by new updated gate"). Round 1 (q01, S1-S3, i01-i04, quick-test batch) is archived unchanged in
`archive/round1-q01/`; new sketch ids start at i05 and questions at q02 so old ids stay unambiguous.
Origin claude for both sketches. Hooks: notes/hooks.md. No local model checks were run (gate v3);
golds recomputed by the author's script.

Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, ambiguity and necessity checks, mechanism, risk and decision. Keep at
most two active sketches. Full components, submission reasoning and mechanical preflight follow
promotion; complete relevant membership/exclusion proof before promoting a list/count. The platform
validates the completed question; do not predict its tier or run local models by default.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i05 | notes/sketches/i05.md | h1: women's share of participants, Doc 3 (D04) Table 4 check-up row vs Doc 4 (D05) Table 4 zero and total rows; gold 14.5 pp (59.629 - 45.152) | competing: -9.3 / -16.7 (within-sex column percentages) fail "women's share of [those who had ...]"; 12.2 (Doc 4's "1" row = exactly one examination) fails "a ... cancer examination"; 4.5 (unscreened) and 1.2 (whole samples) fail "who had". Necessity: check-up counts only in D04, screening counts only in D05 (grep across D01-D07). Screen passed (0 failures) | PROMOTED to q02 rev 0 (checked: floor 0 FAIL, 1 WARN origin; tested_sha256 29e79690...; platform pending) |
| i06 | notes/sketches/i06.md | h2: group with the highest non-mandatory check-up rate (Doc 3 Table 4: unemployed 21/52 = 40.38%) -> its mean counted cancer examinations (Doc 4 Table 4: 39/55); gold 0.71 | competing: 1.01 (women, 36.99%) fails "highest"; 1.15 overall and 1.16 not-unemployed fail the group; 0.36 (any examination) fails "mean". Widening to age or risky-behaviour groups keeps the unemployed on top. Necessity: group from D04, distribution from D05. Screen passed | alternate, not promoted: the bridge is printed in D04 prose (L243) and flagged in its discussion (L403) |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
Allow one focused repair per distinct observed failure; a repeated failure means change the hook.
