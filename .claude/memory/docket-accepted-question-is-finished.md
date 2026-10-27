---
name: docket-accepted-question-is-finished
description: "Never edit, re-export or resubmit a question once its status is submitted or accepted; log later findings instead."
metadata:
  node_type: memory
  type: feedback
  stage: export
  updated: 2026-10-01
  originSessionId: cce78281-5de7-4ebd-afb7-2132b5621e18
  modified: 2026-10-07T08:32:34.443Z
---

## Current rule

A question with status `submitted` or `accepted` is finished. Do not change its question,
answer, documents, tags or reasoning, and do not export it again with changes. A finding made
afterwards goes into its `## Feedback log` or the bundle's notes, and into a lesson here if it
generalises; the submitted text stays as it was. A `rejected` question is revised in place,
with the platform's words logged first.

**Why:** in the Kepler workspaces the user corrected exactly this on 2026-09-10. Asked to make
a bundle "pass all validations" after it already had, an edit changed the submission and put a
passed item back through review for no gain. A submitted question is the record the platform
judged, in the same way.

**How to apply:** read the front-matter status before any edit to a question file. For
`submitted` or `accepted`, record, don't change.

A platform "Revision requested" works the same way as a rejection: the platform has handed the question
back. Log the panel verbatim first (notes/feedback-qNN.md plus a Feedback log line). Then revise in place
as a new revision with fresh records. Status moves from draft to checked, and back to submitted when the
user resubmits. Remove `accepted_tier` while the revision is pending (aq-01278 q02 2026-10-06, aq-01333
q01 2026-10-07). Change only what the reviewer asked for. On resubmission, take `accepted_tier` from the new
revision's own difficulty result, not the returned version's. Any change to the question, answer or necessary
documents needs a new result; aq-01333 q01 rev 5 only unticked a document and still needed one (review,
2026-10-08).

When the user confirms a submission, set `status: submitted` and add the platform tier the
question passed at as `accepted_tier: <Easy|Medium|Hard> Tier` in the front matter (user,
2026-10-07, aq-01433 q01: "I mean accepted_tier", correcting a first "answer_tier"; aq-01320 q01
already carried `accepted_tier: Easy Tier`). Neither field is in the tested fingerprint.

## Evidence and history

- 2026-10-01: rule seeded when the workspace was set up, from Kepler's
  `kepler-a-passed-bundle-is-finished`. No Docket evidence yet.
