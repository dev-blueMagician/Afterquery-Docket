# aq-02483 - lean candidate sketches

Current target: medium (user 2026-10-09: "there is no slot for Easy Tier for this bundle, we should
target medium and high. do your best."); measured platform success pending. Sources: caller (hooks
h1-h12) and two independent question-author agents (A: numeric focus; B: regulatory-scope focus),
all origin claude. No local model checks were run on any candidate.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i02 | [sketches/i02.md](sketches/i02.md) | B's i02: newest federal CCR amendments reflected in Wyoming's (cutoff Dec 14, 2020 -> Nov 12, 2020 amendment) and Wisconsin's (Aug 28, 2020) rules: 76 days | Decoy 108 (cutoff taken as an amendment date; disproved by the dated list in another section); D02 and D06 each sole source; analogy risk via Virginia/Alabama cutoffs | q01 rev 0 quick test "too easy" (user 2026-10-09); q01 dropped, hook closed |
| i03 | [sketches/i03.md](sketches/i03.md) | B's i01 family: definitions the 2024 Legacy Rule added that stay federal, Wyoming 10 minus Virginia 7 = 3 | Decoy 0 ("neither adopted 2024 changes"); D02 and D03 each sole source; small-integer gold | quick test "too easy" (user 2026-10-09); dropped |
| i04 | [sketches/i04.md](sketches/i04.md) | A i13 = B i03: Wisconsin landfill deadline Feb 1, 2023 vs Wyoming impoundment deadline (12 months after Aug 19, 2022): 28 weeks | Decoy 24 weeks (effective date as deadline); "to the nearest week" absorbs the 198/199-day convention; shares D02 L278 with q01 | quick test "survived"; q02 rev 0 difficulty Run 1 (Version 7ed75f) Too easy, Low 5/5; no fair repair, dropped (feedback-index P4) |
| i01 | [sketches/i01.md](sketches/i01.md) | Caller h1: Legacy amendments approved as Alabama's version but not Wisconsin's: 8 | Decoy 6 (17 - 11), 9 (template list); two printed numbered lists: same family as aq-02447 q01, which scored Too easy (Low 5/5) once a search reached both lists | handed over; no quick-test result reported |
| i05 | [sketches/i05.md](sketches/i05.md) | A's i11: landfills in states whose version of the 2024 "Infiltration" definition EPA approves: 16 | Decoy 19 (Alabama's identical entry under "not being approved"); keyword search lands on all entries | handed over; no quick-test result reported |

Rejected (reasons in hooks.md and author returns): A i12 (1,884 days; February 10, 2026 date printed in
four documents, so no second indispensable source); B's sum form "Wyoming + Alabama = 20" (sum vs
union reading; identification only via twin Docs 3/4); funding, unit-per-facility, penalty, tribe,
comment-period, application-gap, North Dakota and internal-mismatch hooks (h2-h12).
Set rule: submit at most one of i01/i03/i05 (shared approval lists) and at most one of q01/i04 (shared
Doc 2 sentence).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
