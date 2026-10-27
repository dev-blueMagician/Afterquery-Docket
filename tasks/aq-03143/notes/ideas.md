# aq-03143 - lean candidate sketches

Current target: medium (Hard welcome); measured platform success pending. User, 2026-10-11: "there is no slot for
Easy Tier for this bundle, we should target medium and high. do your best." Origin of every sketch: claude.

Round 1 (2026-10-11). Sketch-only until a quick test survives (no question file, prepare or hand-over yet). The
mechanical screen (`docket_agent.py screen`) passed for all six: quotes found, two documents each, no failures.
Its warnings are the deep-number ones listed per sketch. No model was run.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md): outside London, 10 hours each on a housing and a non-asylum immigration legal help matter plus 3 hours attending county court with counsel -> £1,032.50 | h1 | Wrong routes £1,463.00, £696.00, £980.45, £1,023.50 each fail a stated rule. Doc 1 is the only source of the two escape multiples; Doc 3 the only printed final £52.00 (Doc 4 states the 75% rule only) | quick test 2026-10-12: did not survive; closed |
| i02 | [sketches/i02.md](sketches/i02.md): i01 with "whether by fixed fee or at hourly rates" -> £1,032.50 | h1 | As i01; the phrase adds no rule or figure | quick test 2026-10-12: survived; promoted unchanged to questions/q01.md rev 0 |
| i03 | [sketches/i03.md](sketches/i03.md): London, 17 hours asylum legal help, 9 hours housing legal help, 3 hours attendance -> £1,557.10 | h1 | Both thresholds printed (£1,118, £669); wrong routes £1,957.80, £938.00, £1,505.05. Doc 1; Doc 3 or Doc 4 | quick test 2026-10-12: did not survive; closed |
| i04 | [sketches/i04.md](sketches/i04.md): Q11 counts for areas with a 50% remote limit and a full-time office -> 106 | h2 | 152 without the immigration exclusion; 80 for the part-time side. Doc 1 holds both rules, Doc 3 the counts | quick test 2026-10-12: did not survive; closed |
| i05 | [sketches/i05.md](sketches/i05.md): barristers' share of the interim response's £115m -> 34% | h4 | 27% mixes volume bases, 33% is the 2019-20 share. Doc 5; Doc 6 or Doc 7 | quick test 2026-10-12: did not survive; closed |
| i06 | [sketches/i06.md](sketches/i06.md): rise in the yearly cost of fee simplification -> £0.1 million | h3 | £0 and £0.3m fail the wording. Doc 2 and Doc 4 | spare, not in batch 1 |

Quick test, batch 1 (user chat 2026-10-12, verbatim: "only i02 survived"; no panel pasted; 5 of 10 quick tests
used, by the batch size). What it shows about h1: the bare case (i01) and the London case with both thresholds
printed (i03) did not survive, while the same non-London case with the phrase naming the kind of payment (i02)
did. The reason i01 failed is not shown (too easy is the quick test's only failing verdict the user has reported
before, but the words were not given). i02 is the only wording carried forward.

Set notes: i01, i02 and i03 share one answer path (submit at most one). i04, i05 and i06 use different document
pairs and mechanisms and give no hint toward h1. Question lengths 29-48 words: above the 12-20 words the user
prefers, because the h1 case needs three stated items; say so at hand-over.

Not sketched: h5, h8, h9, h10 (closed in hooks.md for necessity or two-reading faults); h6 and h7 held.

## Round 2 (2026-10-12), built from Run 1 on q01 rev 0

Run 1: "In band — Easy tier", Low 2/5 (capture verdicts/AQ-03143_difficulty_2026-10-12_1221.txt; routes in
hooks.md, "Measured results"). No Easy slot (user, 2026-10-12), so q01 rev 0 is not submitted. All five low attempts
cleared both escape thresholds; the three misses were all in the attendance cell (£49.00 twice, £34.65 once).
Sketch-only again; mechanical screen passed for i07-i09 (no failures); no model run.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i07 | [sketches/i07.md](sketches/i07.md): 2024 housing legal help matter + new immigration legal help matter + county court attendance in a new housing and a new discrimination case -> £1,054.25 | h1 + h11 + h12 | Wrong routes £1,120.25, £1,550.75, £1,122.50, £1,052.90, £1,045.25, £1,002.20 each fail a stated rule or printed rate. Doc 1 for the escape multiples, Doc 3 for £52.00 (both "Needed" on Run 1) | quick test 2026-10-12: survived; promoted unchanged to questions/q01.md rev 1 (12f43234...) |
| i08 | [sketches/i08.md](sketches/i08.md): i07 without the discrimination case -> £966.50 | h1 + h11 | q01's gold £1,032.50 becomes the wrong route for a new-fee reading | not quick-tested; held as a fallback if rev 1 proves too hard |
| i09 | [sketches/i09.md](sketches/i09.md): i07 without the 2024 matter -> £897.25 | h1 + h12 | £965.50 if the increase is applied to the discrimination case | not quick-tested; held as a fallback if rev 1 proves too hard |

Set notes: i07, i08 and i09 share one answer path with each other and with q01; at most one is ever submitted.
Lengths 48-57 words. Two quick tests stay in reserve (i06 untested).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

Round 2 outcome (2026-10-12): i07, promoted as q01 rev 1, measured "Too easy", Low 5/5 (Run 2; routes in hooks.md).
q01 is dropped and hooks h1, h11 and h12 are retired; i08 and i09 are subsets of i07 and are closed untested. Two
rounds used and two difficulty runs spent: Easy (no slot), then Too easy. No third round is proposed, because no
remaining idea rests on a miss this solver actually made (hooks.md, "Decision"). Release recommended.
