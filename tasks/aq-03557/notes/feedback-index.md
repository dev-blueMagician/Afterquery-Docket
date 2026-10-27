# Feedback index

Keep concise rows linking raw returns, current fixes and status. Raw platform words stay in
the linked artifacts/feedback notes; this index does not replace exact-content records.
Never edit submitted/accepted question files to maintain it.

## Active issues

Triage each exact tested version once. Key by bundle/question + platform version + issue;
record revision/fingerprint when established. Distinguish platform observations from the
author's inference. Categories: ambiguity, necessity, unsupported gold, form, difficulty,
identity. One mechanism per row is enough; use short phrases and links, not essays.

| Issue id / bundle / question | Tested platform version / rev / fingerprint | Category / mechanism | Raw feedback links / platform observation | Current version / author comparison or fix link | Status / next action |
| --- | --- | --- | --- | --- | --- |
| aq-03557-q01-F1 / aq-03557 / q01 | Form Checks, "4 min ago", no version id shown. The Question box shows rev 0's wording word for word (21 words); answer, reasoning and footer are not in the screenshots, so rev 0 (8e203179...) is bound for the question only and presumed for the rest | form (authorship), blocking / "Question in your own words" Failed: the question text is Claude's (origin: claude), pasted as handed over. Nothing in the check concerns the content | [question box](platform-feedback/q01-rev0-question-box-2026-10-12.png), [checks](platform-feedback/q01-rev0-checks-2026-10-12.png), [transcription](platform-feedback/q01-rev0-checks-2026-10-12.txt): "Your question reads as AI-generated. Rewrite it in your own words. Re-running the same text gives the same result." Only an admin can clear this check | questions/q01.md rev 2 (114f324f...), 2026-10-12, origin user+claude: "With the number of stores Woolworths provides, how many supermarkets trade under banners that any retailer's submission says have no loyalty programme?" (the opening is the user's; the second half is rev 0's). Two other wordings from the user were checked and not adopted because "the retailer’s" drops the any-submission rule (Feedback log). Earlier: rev 1 (c31b1263...), the user's first rewording, recorded verbatim ("Using Woolworths’ store counts, how many supermarkets operate under banners that any retailer’s submission says have no loyalty programme?"). Not restyled by Claude (docket-opus-ownership). Author's comparison: every listed element is kept; "Woolworths’ store counts" for "the store counts Woolworths gives" opens a reading as Woolworths' own stores (71), reported to the user | user reports rev 2 "submitted as medium tier" (2026-10-12), so Submit was not blocked; the check's own result on rev 2 was not sent. Earlier note: rev 2 shares its second half with rev 0's sentence. The admin report route applies only to text the user wrote |
| aq-03557-q01-F2 / aq-03557 / q01 | Same screenshots, same binding | form, advisory / "Each description fits one thing" Warning: the description is a set by design and the four matches listed (PAK'nSAVE, Four Square, Raeward Fresh, FreshChoice) are banners the gold counts; SuperValue, the fifth, is not listed. The same advisory has warned on every list or set question recorded here (aq-03170, aq-02750, aq-02743) | Same artifacts: "4 matches ... Narrow the description." "A warning, never a block" | No change: narrowing the description to one banner would remove the question | open as an observed advisory; no repair. Re-read after the reworded question is checked |
| aq-03557-q01-P1 / aq-03557 / q01 | Same screenshots, same binding | platform observation, not an issue / on rev 0's wording the blocking "One defensible answer", "Needs two or more documents" and "Reasoning reaches the answer" Passed, as did "Reasoning in your own words" and five advisories (Evidence supports its component, Question does not hint the answer, No single passage gives the answer, Left-out items do not qualify, Answer matches a stated figure) | Same artifacts. Rows outside the screenshots are unknown | These results belong to rev 0's wording. Rev 2 is new content and needs them again | historical since rev 1 (2026-10-12); Checks not recorded with `record-checks` (partial screenshots, no text capture, identity presumed beyond the question) |
| aq-03557-q01-D1 / aq-03557 / q01 | Difficulty Run 1, Oct 12, 2026, 10:51 PM, Version d8243a (current) / rev 2 / 114f324f... (question quoted word for word, "Your answer: 376 supermarkets", Document check on documents 7 and 3; reasoning and evidence as submitted not shown) | difficulty / observed result only: "In band — Medium tier", Low 0/5 · Medium 1/5 · High —; closed-book needed the documents; every-document attempt 376; both documents needed. Wrong answers: 301 four times (low), 71 three times (one low, two medium: the opening phrase read as Woolworths' own stores), 372 once (medium, route unread), no answer once (medium, output loop) | [capture](../verdicts/AQ-03557_difficulty_2026-10-12_2319.txt); per-attempt read-out in [feedback-q01.md](feedback-q01.md). Three Reasoning blocks were saved unloaded (Medium 2, Medium 3, one removal attempt) | questions/q01.md rev 2, status submitted, accepted_tier: Medium Tier (frozen 2026-10-12) | resolved by observed platform result at the target tier; submitted by the user; review outcome pending. Declared mode 2 (392) caught no attempt; not aligned before Submit |

Statuses may be unresolved identity, open, repaired/platform pending, resolved by observed
platform result, historical, or redesign. A local repair is not a platform pass. Preserve
prior raw feedback and fixes through links when updating a row.

- Re-sent screenshots of the same version/issue link to the same row, with no new failure or
  return count. Compare the tested content with the current draft before changing it.
- Unknown versions get distinct receipt ids and stay unresolved. Do not group unrelated
  returns under a shared `unknown` key; merge only with evidence of the same tested version
  and issue, or an identical re-sent artifact. Never infer a current fingerprint from a qNN.
- Make one focused repair for a mechanism. If the same failure is demonstrated on that
  repaired exact version, redesign the hook; stale/duplicate/unknown feedback does not show
  recurrence. No automatic local model validation follows intake or repair.

## Next five newly promoted candidates

Use one owner index for the five-candidate trial, including if it spans bundles; link it from
other bundle sessions. Add each newly promoted candidate once. Resume/revision keeps its row;
a genuinely new hook promoted as a new candidate gets a new row. Do not enroll old candidates
retrospectively or reset the count when changing bundles. Stop enrolling after five.

- Trial owner index / start: [workspace owner](../../../notes/feedback-index.md); start recorded in the shared ledger
- Candidate rows used: 0 / 5

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |

Record actual active candidate authoring/revision minutes as work happens, including any
already timed sketch work; exclude idle/platform waiting. Keep brief dated increments in the
minutes cell or a linked session note and mark coverage complete or partial/unknown. Never
estimate missed time afterward. A promotion does not make unrecorded earlier work known.
Revision rounds count distinct edits after first promotion, not duplicate screenshots or
resumptions. Count each distinct platform return once per applicable ambiguity/necessity
category, linked to its issue row; unknown identity stays uncounted/pending until resolved.
Acceptance records the actual platform observation (accepted, rejected or pending) with its
raw link; a difficulty pass or local repair is not acceptance. A candidate retired before any
submission is recorded as not submitted/retired: zero acceptances, no platform verdict claimed.
Retirement after submission does not settle a pending platform outcome.

- Summary: this bundle's candidate (i01 -> q01) is not enrolled in the trial; the owner index is the workspace
  notes/feedback-index.md. Short timers ran for i01 on 2026-10-12 (shared ledger); the reading of the nine
  documents was not timed, so timing coverage is partial. One difficulty run (Run 1, Medium, rev 2); two
  revisions after promotion, both the user's rewordings of the question; no ambiguity or necessity return;
  submitted 2026-10-12, acceptance pending.
- Accepted questions per known authoring hour: pending. Once all five have complete timing
  and settled outcomes (including retired before submission), compute accepted count / (total recorded minutes / 60), including
  time spent on unsuccessful candidates. No rate claim while either is incomplete or the
  denominator is zero; report known counts/minutes without treating partial time as a total.

## Measured events

Use the single workspace `notes/efficiency.json` ledger; this table links its report, rather than
maintaining a second set of totals. Start/stop timers and promote candidates through
`python tools/docket_agent.py efficiency` (WORKFLOW section 11). Keep stable candidate IDs across
work sessions and revisions. Do not enroll pre-existing questions or reconstruct their history.

For `record --event PATH`, save a JSON object with `kind`, a stable `event_id`, the bundle slug in
`bundle`, the tracked `candidate`, and `source` pointing to the actual trace/return/session evidence.
Add the fields below. Illustrative field names are a contract, not recorded measurements.

| Kind | Additional fields |
| --- | --- |
| `usage` | `total_tokens`: nonnegative integer reported by the runtime/API |
| `platform_attempt` | `attempt_id`: identified platform run; `stage`: `quality`, `difficulty` or `review`; `revision`: nonnegative integer; `tested_sha256`: verified prepared fingerprint |
| `revision` | `revision`: actual post-promotion revision number; `tested_sha256`: content fingerprint |
| `outcome` | `outcome`: `accepted`, `rejected`, `pending` or `retired_before_submission` |
| `coverage` | `timing` and `tokens`: each `complete`, `partial` or `unknown`; source explains coverage |

One usage event represents one non-overlapping reported usage interval/request; use its stable
receipt ID and do not record overlapping session and request totals. Missing usage stays unknown;
zero requires a reported zero. Do not substitute document-token counts or estimates. Repeated event
IDs with the same data are harmless; conflicting reuse is rejected. Duplicate identified runs or
revision snapshots do not increase counts. Keep unresolved run identity in feedback notes until known.

The `source` records provenance, not an independent verification of the supplied value. Acceptance
must be an observed platform outcome, not inferred from a difficulty pass. Confirm timing/token
coverage only when the measured records cover the relevant work; future work needs reconfirmation.
Stop timers before waits and turn end; discard an interrupted interval whose active time is unknown.
Unpromoted work and incomplete coverage remain visible. No metric triggers new model validation.
