# Prospective efficiency trial

This is the shared owner index for the next five newly promoted candidates across bundles.
The measurement ledger is [efficiency.json](efficiency.json). Candidate enrollment starts with
new work; historical questions, agent maintenance, and unmeasured past usage are not backfilled.

Read the current measurements with:

```powershell
python tools/docket_agent.py efficiency report
```

The report is the source of numeric totals and coverage. It includes measured authoring time by
phase, reported tokens, distinct identified platform attempts, revision rounds, and observed
outcomes. Missing measurements stay unknown. Accepted questions per authoring hour remains pending
until five candidates have complete timing, settled outcomes and a positive denominator.

Use [WORKFLOW section 11](../WORKFLOW.md#11-measure-the-next-five-candidates) and the
[event contract](../tasks/template-task/notes/feedback-index.md#measured-events). Stop active
timers before platform/idle waits or yielding the turn. An interrupted interval with unknown
active time is discarded, retaining incomplete coverage. Record actual runtime usage only.

Bundle-specific ambiguity/necessity issues and raw platform returns remain in each bundle's
`notes/feedback-index.md` and linked artifacts. Link that index in each candidate's source-backed
events; do not duplicate its prose or infer a platform pass from these measurements. This ledger
does not modify question Markdown, form-input JSON, source documents or validation records.
