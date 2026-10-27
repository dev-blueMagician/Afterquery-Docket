---
name: docket-user-counts-non-green-check-rows-as-failed
description: "Docket form Checks: when the user says 'N checks failed', the count covers every non-green row (Failed, advisory Warning, Couldn't check); read each row's own label before changing a question"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f3353b91-2901-4de2-9337-705e930c531a
  modified: 2026-10-12T22:29:57.380Z
---

When the user sends a Docket Checks screenshot with "N checks failed", N counts every row that is not green: a real
Failed, an orange advisory Warning, and a "Couldn't check ... retry" row alike. Read each row's label and text first,
then answer row by row: what it is, whether it blocks, and what to do.

**Why:** aq-03170, 2026-10-12, twice in one session. "2 checks failed" was one Failed (Reasoning tags: ticks not set
on the page) plus one advisory Warning (Answer format stated). Later "two checks failed" was one advisory Warning (Each
description fits one thing, listing the gold's own three names) plus "Needs the documents — Couldn't check — Could not
run this check — retry", which is the platform failing to run a check. Neither message contained a second real
failure. My interpretation, not the user's words: they want every non-green row gone or explained, so an advisory I
knowingly leave in place will come back to me as a failure.

**How to apply:** before a hand-over, clear every advisory the local preflight predicts where that costs nothing (for a
list answer, state the order in the check's own words: "alphabetically", "in date order", "in any order"). Name in the
hand-over any row that will stay orange and why (any list question draws "Each description fits one thing"; it did not
stop a difficulty run or the "You can submit now" line). For "Couldn't check", tell the user to retry, reloading the
page if it asked for a reload; do not revise content for it. Related: [[docket-user-states-open-tier]] (take the user's
reports at face value), [[docket-read-the-trace-before-naming-a-route]].

Tool note, 2026-10-12: the local floor had accepted "Earliest second letter first." as an order while the form still warned, and the form flagged "second letter" as a pointer. `tools/check_questions.py` now WARNs on a bare order word (code `format`) and on an ordinal before a document part (code `pointer`); treat both as must-fix before a hand-over.
