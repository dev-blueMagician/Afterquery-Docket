# aq-01650 round 1 archive (archived 2026-10-08)

The user asked on 2026-10-08: "first clear work history on AQ-01650 and start again by new updated
gate". Round 1's question file, every run, the platform captures and the round's working notes were
moved here unchanged, out of `questions/`, `runs/`, `verdicts/` and `notes/`, so the tools no longer
see them. Nothing was edited. Memory notes that cite aq-01650 q01 refer to these files under their
old paths (`questions/q01.md`, `runs/<run>/...`, `verdicts/...` now sit below this folder).

Kept in the active bundle: `docs/`, `text/`, `notes/intake.json` and `notes/doc-map.md` (source
navigation bound to the unchanged source hashes). New questions start at q02, so q01 stays
unambiguous in records and memory.

| id | final status | what happened |
| --- | --- | --- |
| q01 | dropped (rev 2) | Japan 2016 non-student mean share correct (rebuilt from the sex-specific means in Doc 5's decomposition table) minus the CHFS 2015 mean share, gold 9.2 points; the printed complete-case mean gave 13.7 |

Platform record for the q01 family (all "Earlier version" except Run 4; pages saved in `verdicts/`):

| run | version | result | tier line |
| --- | --- | --- | --- |
| form check | rev 0 | "One defensible answer" blocked: too vague (both form solvers 13.7) | - |
| 1 | 1923ac | Answer not supported | Low 3/5 · Medium — · High — |
| 2 | 288215 | Did not finish | Low 0/5 · Medium 0/5 · High 0/4 |
| 3 | 288215 | Too hard | Low 0/5 · Medium 0/5 · High 0/5 |
| 4 | 61debd (current on the page at 16:09) | Answer not supported | Low 1/5 · Medium — · High — |

Run 4's page: "2 of 5 gave the same wrong answer ... 13.7", "2 wrong attempts quoted the same passage:
Doc 5 ("Descriptive statistics for complete cases.")", "4 of 8 runs left". The 16:57 Checks capture
(37 of 39 passed) flagged "Each description fits one thing" and still listed "The difficulty check could
not reach your answer even with every document" under "Still needed before you can submit".

Round-1 sketches never written up (notes/ideas.md, notes/quicktest-batch.md): S2 (+14.5), S3 (1.36),
i01 (24.7), i02 (graduates, the unemployed, drinkers), i03 and i04 held. Their old-workflow tier
estimates are superseded by gate v3 (no local tier predictions).

Page state seen on 2026-10-08: "Hard 0/2, Medium 0/3, Easy 0/1" with "In review: Easy 1", 8 submissions.
Runs `q01-r0-probe-m5` and the q01 snapshots were bound to the read guard; moving them makes the guard
drop those entries at its next bind.
