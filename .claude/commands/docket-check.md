---
description: Run one Docket mechanical preflight and full handover for platform validation; optional diagnostics only for a stated issue
argument-hint: <slug> [iNN | qNN ...]
model: claude-opus-5-5
effort: max
---

Check $ARGUMENTS within one active bundle. No ids means draft/checked questions. Read the guide
and gate; honor difficulty_target easy|medium|hard (new default hard since 2026-10-14, legacy
default hard). For a Hard target read .claude/memory/reference/hard-playbook.md first.
Never edit submitted/accepted content. The caller owns fixes and accurate authorship.

Default path:

1. For a sketch, verify essential source inputs, the author calculation, necessary dependencies,
   obvious alternate readings and the selected levers before full write-up. Decoys are required
   for which-items questions; ordinary cross-document arithmetic/date/ID joins are eligible.
   Check the sketch's competing answer -> wording condition and per-source unique input ->
   substitute search. Recheck necessity after clarification; do not promote a cosmetic second
   document. Reuse source-bound passages and calculations; these are author checks, not extra jobs.
   `python tools/docket_agent.py screen tasks/<slug> --idea iNN` is an optional mechanical screen.
   It warns when a period word in the question is also printed as a reporting label ("half-year
   results"); act on that warning before any platform test, and make the same search by hand for
   every phrase naming the asked period or population (WORKFLOW section 4).
   For a Hard target `screen` also checks the sketch's `## Lever stack` (two or more levers with
   found quotes and different wrong answers, three steps, a decoy, no rare question word in a settling
   passage; playbook section 4): settle its warnings before the strong-solver screen.
   For a Hard target, run the strong-solver screen before anything is offered (WORKFLOW section 4:
   `docket_agent.py packet`, three fresh blind solves, `record-screen`); the floor FAILs a live Hard
   question with no screen record and WARNs when the screen was right three times. The screen ranks;
   the user decides what runs.
   File viable sketches through /docket-add; launch no other local validators to screen them.
2. For a final question, verify arithmetic/date results with a script or calculator, including
   input choice, units, signs, rounding and counting convention. Complete every form field,
   necessary-document role and Targeted failure mode. Assess actual source gaps for this candidate.
3. Run `python tools/docket_agent.py prepare tasks/<slug> --q qNN` to freeze fields and one corpus
   copy. Save the revision, tested_sha256 and run path. Default preparation creates no solver
   packets, binds no diagnostic scope and runs no models. An editable legacy question needs its
   existing hard target made explicit through /docket-add before preparation; never lower it silently.
4. Known gaps need a substantive author assessment or supplied platform evidence covering every
   exact gap's effect on premises, gold, exclusions, uniqueness, necessity and shortcut coverage.
   Record it in Source assessment using the snapshot/gap hashes and the schema in WORKFLOW.md.
   Necessary/cited missing material and unknown provenance cannot be waived. An irrelevant-gap
   assessment preserves the incomplete-corpus warning; no independent model review is mandatory.
5. Run `python tools/check_questions.py tasks/<slug> --handover --q qNN` once at the phase boundary.
   Fix FAILs and fix/explain WARNs; repeat only after a relevant change or unresolved failure.
   Set checked when mechanical preflight is done and platform validation is pending. Hand over
   notes/handover-qNN.md whole, every form field and failure mode included, with platform Doc N
   numbers. State the target and pending platform result. No local difficulty guesses, odds or
   "likelier" tiers. For a gold that has to be derived, ask the user to look at the form's
   "One defensible answer" check before spending a difficulty run.
   Also provide questions/qNN.json containing only the form input values when generated. For a
   JSON-only request, use `check_questions.py tasks/<slug> --json --q qNN` without repeating validation.
6. Record genuine platform output supplied by the user or from an already authorized test under
   `## Platform validation` (legacy platform records in `## Blind solve` remain readable):

   - DATE | rev: N | platform difficulty check | tested_sha256: HASH | platform_verdict: pass|fail|unknown | passed_tier: easy|medium|hard | tiers: EXACT PLATFORM LINE | feedback: EXACT PLATFORM WORDS

   Use passed_tier only for an explicit pass. Preserve the raw output and exact tested identity;
   counts/reached tiers alone never prove a pass. Set ready only with a clean floor and an
   exact-content recorded platform pass at/above target. Preparation is not external authorization.
   Revise editable content as a new revision/snapshot; leave old records historical.
7. Track all 39 platform Checks separately. After verifying that a supplied capture tested the
   prepared content, record it with `python tools/docket_agent.py record-checks tasks/<slug> --q qNN
   --capture <capture.txt> --revision N --tested-sha256 HASH`. This appends raw outcomes without
   running models. Never infer binding from title/time; unbound captures leave Checks pending.
   Report/handover separates Checks clearance from difficulty `ready`. Missing/stale blocking
   results or an explicit footer blocker prevent clearance; advisory warning/retry stays advisory.
   Own-words checks belong to the admin, including explicit nonblocking reasoning review; preserve
   actual origin. A recorded clearance is not acceptance.

Optional diagnostics:

- The strong-solver screen above is not one of these. Run the others only on explicit user
  request or for a concrete unresolved issue, choosing the smallest
  useful check. Missing/stale local records are not a reason to launch new solves. No mandatory
  pair of solves, audit, closed-book check, removal probes, independent reviewer or tier prediction.
- If needed, run `python tools/docket_agent.py prepare tasks/<slug> --q qNN --local-checks` to
  prepare sealed packets and scope binding. Read the applicable role prompt explicitly. Use fresh
  workers without inherited chat (`fork_turns: none` on Codex; supported omitClaudeMd on Claude).
- A blind solver/auditor gets only the exact question and its own prepared document packet,
  never gold, notes, selected evidence/tags or writer history. A closed-book worker gets only the
  question and no usable tools/files. An optional removal probe gets a renumbered packet without
  the tested document in a neutral folder. An independent reviewer gets frozen fields and raw returns.
- Preserve authentic returns outside packets with their revision/fingerprint. Contaminated,
  cut-off or failed executions are not misses. Resolve demonstrated defects without treating
  optional diagnostic completion as a readiness gate or simulating platform difficulty.
- Repair denied scope through preparation/explicit packet paths; never widen access or leak the
  answer to make a check work. Keep scope security hooks in place.

Keep notes/session.md under 4,000 characters with target, run, mechanical/platform status,
concrete open findings and next action. Do not create extra prose reports for routine checks.
