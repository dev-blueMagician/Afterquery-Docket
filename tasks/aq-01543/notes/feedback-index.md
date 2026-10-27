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
| F1 / aq-01543 / q01 | Unbound form state, received 2026-10-08: question, gold component and documents of revs 1-8; reasoning box not shown; evidence had 5 rows (no local revision has 5); no fingerprint | Unsupported gold, possibly ambiguity. Platform: the form's solvers, working the question with the documents, did not reach 22.8; no solver answer shown. Inference: built Bulgarian share beside Doc 1's printed 27.6% for Sep 2024-Aug 2025, a window "In 2024" did not visibly exclude | [screenshots + transcription](../runs/q01-platform-unbound-2026-10-08/README.md); red, Question box: "Working the question from the documents does not give this answer. ..." | Rev 9, tested_sha256 8671bcad...: "In calendar year 2024" (one focused repair); reasoning relabelled, arithmetic unchanged ([q01 Feedback log](../questions/q01.md)) | Superseded: rev 9's quick-test solver reached the gold (F3), then q01 was dropped |
| F2 / aq-01543 / q01 | Same unbound form state as F1 | Form, Evidence field: a fifth quote from Doc 1's Sep 2024-Aug 2025 paragraph (40.38% nuclear, 27.6% coal), in no local revision; most likely an earlier "Derive the rest" proposal from revs 0-5's Decoy line, kept by the page | Same folder; orange, panel: "The quote from document 1 for component 1 (...) does not seem to support that component. ..." | Rev 9 hand-over keeps the four rows; the stray row must be deleted on the form | Superseded: q01 dropped |
| F3 / aq-01543 / q01 | Rev 9 presumed (user's reply to the rev 9 hand-over; no screenshot); tested_sha256 unconfirmed (rev 9 = 8671bcad...) | Difficulty: Quick test "Too easy. Solver got it". Inference: "calendar year 2024" visibly excludes the 27.6% decoy, so the derivation is the only route and the low model took it; unpinned wording (rev 8) had failed the form's solver check | User message, 2026-10-08 (verbatim in q01's Feedback log) | No fair wording between rev 8 and rev 9; q01 dropped; replacement q04 (sketch i05, different hook), rev 0 addb7a41..., checked | Closed for q01 (redesign done). Next: platform result for q04 |
| F4 / aq-01543 / q04 | Rev 0, tested_sha256 addb7a41... (user's reply to the rev 0 hand-over; the screenshot shows q04's failure-mode picks) | Form: the Targeted failure modes section changed (trap and cause per mode, then one shared "Why these are traps" reason of at most 50 words); the empty reason box blocked Submit | [screenshot](../runs/q04-r0-v2-addb7a41e30a3b93fdb5f019e31590520c91c44a5de49e352a5dc1f6918593e0-platform/results/platform-form-failure-modes-2026-10-08.png); q04 Feedback log | q04 section rewritten (46-word reason; outside the fingerprint); hand-over regenerated | Repaired; user fills the reason box |
| F5 / aq-01543 / q04 | Rev 0 = platform version a39f39, Run 1 (bound by the saved page: rev 0's question restated in every attempt, gold 7.79%, Docs 4 and 12, "first run") | Difficulty: "In band — Easy tier", "Low 1/5 · Medium — · High —", "You can submit now." | User message, then [saved difficulty page](../verdicts/AQ-01543_difficulty_2026-10-08_1236.txt) (same run) | q04 Platform validation: user-report record plus the verbatim record; below the medium target, status stays checked | Submitting at Easy is the user's call (bundle set up with no Easy slot, 2026-10-07) |
| F6 / aq-01543 / q04 | Same as F5 | Ambiguity advisory (not blocking): "This question may be too vague: several solvers agreed on an answer that is not your gold "7.79%"" (7.20% x3, 7.04% x1). Inference: FM3's merged Kori status cell; the solvers saw the conflict with the printed count of 23 but could not resolve it | Same saved page | No change: the 7.20% reading contradicts the printed count and Table 2's "in operation" marks; Step 3 states the exclusion; any question edit needs a new run | Open risk: a reviewer may return it as ambiguous (aq-01278 q02 precedent); if returned, name the scope in the question and re-measure |
| H1 / aq-01543 / q01 | Revs 2, 3, 4, 5 and 7 (fingerprints in q01's Feedback log) | Form, reasoning number check (Step 6 flags) | runs/q01-r{2,3,4,5,7}-v2-.../results/platform-form-reasoning-check*.png | Rev 8 notation; rev 9 keeps every rev 8 expression | Historical. Rev 8's reasoning-box result was never reported (not shown in the F1 screenshots); check rev 9's box after pasting |
| H2 / aq-01543 / q02 | Rev 1 (1430e5d3) form; rev 2 (1f8c30ef) quick test | Form (Step 5 flag); difficulty: "Too easy — solver got it" | q02 Feedback log; runs/q02-r{1,2}-v2-.../results/ | q02 dropped (no fair harder variant) | Historical; slot reassigned to a future q04 |
| H3 / aq-01543 / q03 | Revs 1 (c686ab34) and 3 (716aef39) | Form, reasoning number check (Steps 2-3, then Step 6) | q03 Feedback log; runs/q03-r{1,3}-v2-.../results/ | Rev 4 (808fc8ec) "*" notation | Repaired, platform pending (user paste of rev 4) |

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

The trial is owned by the [workspace index](../../../notes/feedback-index.md) and its ledger.
No aq-01543 candidate is enrolled: q01-q03 were promoted on 2026-10-07/08 before the trial
started, and pre-existing questions are not enrolled or backfilled. A genuinely new hook
promoted here later (for example a future q04) would take a slot through
`docket_agent.py efficiency promote`.
