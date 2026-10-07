---
name: docket-opus-ownership
description: Claude Opus 5.5/max owns drafting and revision as well as checks; preserve accurate authorship and independent validation.
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 073c2539-55b7-44ff-bcf1-7fe822f487fc
  modified: 2026-10-05T02:47:42.136Z
---

## Current rule

Use `claude-opus-5-5` at max effort for all local work, commands and agents. The caller drafts
topics, sketches, questions, gold answers, reasoning and revisions, and handles evidence,
checks, export preparation and feedback without handing routine work back to the user.
The mapper writes navigation only; the blind solver sees only the workspace root, bundle
path and question; the reviewer returns findings without editing. After revisions, use a
fresh independent blind solve and review. Preserve explicitly requested verbatim content.

Record `origin: claude`, `user` or `user+claude` accurately. The current export tool accepts
only `user`; report this restriction rather than changing authorship to bypass it. Keep
submitted and accepted content fixed; preparing an export does not establish submission.
The platform form's "Before you submit" list includes "I wrote this question myself."; at
hand-off, say plainly that it cannot be ticked truthfully for `origin: claude` content and
leave that decision, and the platform's AI-use terms, to the user. The form's own-words checks
are not part of this workspace's quality check (user, 2026-10-04); do not report them at
hand-off, and never restyle Claude's text to get past them.

Read the newer-guide note alongside the local guide and gate. Local solver results do not
guarantee a platform result. Keep checkpoints under 4,000 characters and compact only on
the user's explicit request.

## Evidence and history

- 2026-10-04: the user confirmed that Claude Opus 5.5 should handle all tasks and requested
  updates to agents, commands, workflow, CLAUDE.md and memory. Removed stale instructions
  that limited Claude to transcription or required the user to perform routine revisions.
- 2026-10-04 (aq-docket-trial-05): all seven trial captures list "I wrote this question
  myself." among the 11 "Before you submit" items. Trial-05's q01-q02 are origin: claude, so
  the hand-off flagged that item instead of treating local readiness as permission to submit.
