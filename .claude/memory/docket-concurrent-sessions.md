---
name: docket-concurrent-sessions
description: "Several Claude sessions work in this workspace at the same time (one per bundle); shared state such as .claude/solver-scope.json, tools/ and memory can change under you, so never assume a single active run."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-05
  originSessionId: fcb2d2e3-acb3-4f5d-88ad-83093c59d52d
  modified: 2026-10-06T18:04:42.127Z
---

## Current rule

- Expect another session to be running checks on a different bundle while you work. Shared
  files are live: `.claude/solver-scope.json` (blind-solver read guard), `tools/`, memory notes,
  WORKFLOW.md and the command/agent files.
- `docket_agent.py prepare` now merges its run into a schema 2 binding (a list of runs, 12-hour
  expiry, lock file plus atomic replace) instead of overwriting one binding, and
  `agent_scope.py` accepts both the old single-run form and the list. Do not reintroduce a
  single-run overwrite.
- Before changing a shared tool, check the binding and the newest `tasks/*/runs/` timestamps
  for in-flight work; keep changes backward compatible, write the new file beside the old one
  and swap it with an atomic replace, then run both test suites.

**Why:** on 2026-10-05 (aq-00998) prepare failed with WinError 5 on the staging rename while
another session's aq-00745 q02 solvers were mid-run under the single binding. Re-running the old
prepare would have evicted that binding and denied their solvers' reads. The fix (multi-run
binding, rename retry) passed 19 agent tests and 24 tool tests; three new tests cover concurrent
runs, legacy merge and pruning.

**How to apply:** at every prepare, read the returned `bound_runs`; if a scope denial appears
in a blind return, check the binding before treating the run as a solver error. See also
[[docket-windows-text-io]].

- A whole bundle folder can vanish while you work. If it does, check `ListAgents`, the other
  bundles and the Recycle Bin. Then rebuild from the template and the capture. Restore only
  provenance you actually read (intake history), never check records, and re-run every check.
- The binding holds at most MAX_BINDINGS = 16 runs (newest first). With four or more sessions
  each binding prepare runs and removal-probe runs, every new bind drops the oldest entry, which
  may be another session's run. Re-run prepare (it re-binds an existing run) right before
  launching blind solvers, treat a scope denial as an eviction, and tell the peers via
  SendMessage when your binds push out their recent runs. Raising the cap is a one-line change in
  tools/docket_agent.py that peers agreed not to make unilaterally.
- Peers coordinate shared-tool edits by message: on 2026-10-06 docket-e1 (AQ-01321) announced and
  made the plain-text (.txt) capture support in tools/split_capture.py while other sessions held
  off; ask before editing a tool another session has claimed.

## Evidence and history

- 2026-10-06 (aq-01278 session, docket-d0): two removal-probe binds evicted runs bound 30-40
  minutes earlier by aq-01322, aq-01320 and aq-docket-trial-04; the peers (docket-e1, -e9, -ba)
  replied that those runs had finished, so no solver was denied.

- 2026-10-05 12:36:31 -0700: `tasks/aq-00998` was deleted programmatically a few minutes after a
  new session had read its notes. No peer session was named for that bundle, the folder was not in
  the Recycle Bin, and no git history existed. The deleted folder held the clipped-capture work (q01
  dropped; q02/q03 locally checked; runs and raw returns). The session rebuilt the folder from the
  template and the user's complete capture. It copied the old intake record, which it had read
  verbatim, into `intake.json` history (D07's unchanged hash confirmed the copy) and checked all
  new questions from scratch. The cause was never found.
