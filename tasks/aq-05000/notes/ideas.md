# aq-05000 - lean candidate sketches

Current target: hard (page: "Still open on this set: Hard", "Hard 0/5 · Medium closed · Easy 0/0"); measured platform
success pending. Expect the check to start at the High level: two solvers, up to 3 tries each; ready only when both
miss at least once and not every attempt misses.

Rules applied (workspace files changed mid-session, 2026-10-14 ~20:36Z, user-approved per CLAUDE.md):
.claude/memory/reference/hard-playbook.md is the design rulebook; a Hard sketch is offered for a quick test only after
the strong-solver screen (packet, three fresh blind-solver solves, record-screen; three right = replace the hook, never
reword or re-screen). Release is recommended only when every fair sketch has a screen result.

Sources of sketches: caller (all seven texts read in full) and two independent question-author agents (A and B, both
returned 2026-10-14). Origin of any promoted sketch: claude.

| ID | Sketch | Hook | Ambiguity / necessity findings | Playbook kind | Strong-solver screen | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | sketches/i01.md (caller): share of responding firms using AI, Atlanta Fed SBU Nov 2025 minus Dallas Fed Apr 2024 = 69.4 - 38.30 = 31.1 points | h2 | look-alike 39.7 (78 employment-weighted); arbitrary pairing of two Fed surveys | number rebuilt from printed figures, basis signposted | 3/3 right (24517437) | rejected |
| i02 | sketches/i02.md (caller; A and B sent the same family in points, 12.7): RPS growth from first reading to Nov 2025 = 40.7 / 28 - 1 = 45.4% | h1 | look-alikes 31.3% (printed YoY), 46.4% (prose 41); recall risk on Doc 6's 28% | number rebuilt from printed figures | 3/3 right (e9adaf3c) | rejected |
| i03 | sketches/i03.md (author B; A sent the one-number variant 2.6): employment weighting alone, Census Sep 2023 - Feb 2024 (20 - 8.8 = 11.2) and Atlanta Fed Nov 2025 (78 - 69.4 = 8.6) | h2/h3 | lure 15.0 (the body's 5-to-20 gap); settlement Doc 6 L53-60 + fn 2, Doc 5 fn 9 | two footnote judgments in different documents | 3/3 right (9d3cca50) | rejected |
| i04 | sketches/i04.md (author A): business surveys run by ONS, the Census Bureau or a regional Fed that reported AI adoption weighted by employment -> BTOS, MES, SBU | h12 | MES only in Doc 1 L72 against eleven firm-weighting chart notes; Fed surveys only "tentatively" approximately employment-weighted | incidental fact vs own account + mentions vs does | 3/3 right (3b0ff763) | rejected |
| B-i02 | author B: DCMS 2022 vs DSIT 2025 "counting AI users as DSIT does" = -1 point | h4 | needs a "Counting" cue clause for one reading; DCMS adopted/piloting overlap unstated; "around 2%"; populations differ | cue clause = signpost | not screened (not fair) | rejected |

Every route the solvers took went straight to the deciding passage: footnote markers on the very sentence (i03), a sweep
of "employment" (i04), the basis words of the question (i01), an RPS sweep from "first reading" (i02). No solver talked
itself out of a deciding fact; 12 of 12 solves were right. Round 1 closed 2026-10-14: every fair sketch has a screen
result, none survived, so nothing goes to a quick test. Release recommended to the user (the user decides).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
