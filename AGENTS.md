# Docket workspace instructions

Follow [CLAUDE.md](CLAUDE.md), [WORKFLOW.md](WORKFLOW.md), and the platform guide in
[instruction.md](instruction.md). Since 2026-10-14 the user's bundles have Easy and Medium full, so the
objective is a Hard pass and the check starts at the High model; design by
[hard-playbook.md](.claude/memory/reference/hard-playbook.md), which supersedes older notes. Runtime-specific model settings in `.claude/` describe the
Claude deployment; use the actual current Codex runtime and record its authorship accurately.

The guide's sections 4-7 of 2026-10-15/16 are saved verbatim in
[platform-guide-2026-10-16.md](.claude/memory/reference/platform-guide-2026-10-16.md). For a Hard target
run `docket_agent.py mine tasks/<slug>` first (it writes notes/mine.md), then stack two or three levers
on the path to one answer, each with its own wrong answer, in the sketch's `## Lever stack`
(playbook section 4), which `docket_agent.py screen` checks.

Do not alter bundle originals or submitted/accepted questions. Find cross-document hooks and
screen lean sketches before full evidence/write-up. Apply author checks to the chosen levers;
decoys are required for which-items questions, not every possible ask. Ordinary cross-document
arithmetic/date/ID joins are eligible; reject demonstrated Guide violations.
Prefer a precise numerical gold derived from indispensable cross-document inputs. In reasoning,
separate cited source values from labelled calculations; show the equation and units for each
derived result. Follow WORKFLOW section 5; calculated outputs need not occur verbatim in sources.

Before full write-up, keep at most two active sketches and record competing answer -> wording
condition plus each necessary document -> unique input -> substitute search. Recheck necessity
after clarifying wording. Reuse source-bound maps; make one focused repair per observed failure,
then change the hook if it recurs. Deduplicate version-bound feedback before repeating work.
For new candidate work, use `docket_agent.py efficiency` (WORKFLOW section 11) at phase boundaries.
Time actual work, stop before idle/platform waits, record only reported usage and observed outcomes,
and enroll the next five promotions in the shared workspace ledger. Never backfill estimates.

Default to platform validation: verify arithmetic/date results, freeze the final content with
`docket_agent.py prepare`, then run one mechanical preflight with the full handover. For a Hard
target, first run the strong-solver screen (WORKFLOW section 4): `docket_agent.py packet`, three
fresh blind solves of the exact sentence, `record-screen`. The result ranks sketches; every fair
sketch still reaches the user with it, and the user decides. Do not
otherwise dispatch local solvers, audits, closed-book/removal probes or reviewers, or predict
platform tiers. Optional diagnostics need an explicit request or a concrete unresolved issue;
stale local records do not create that need. `prepare --local-checks` creates isolated packets
only for those diagnostics. New questions carry `difficulty_target: hard` unless the user names
a lower open tier. After each verdict add one row to `notes/hard-runs.md`; change the playbook
only in the batch review every five new platform results, never for one run.
`checked` means mechanical preflight done, platform pending; `ready` requires a clean floor and
a recorded exact-content platform pass at/above target. Records bind to the prepared fingerprint.
Track all 39 platform Checks separately from difficulty readiness. Record supplied captures with
`docket_agent.py record-checks` only after verifying their match to the prepared revision/hash;
never infer identity from a title or save time. Missing/stale blocking results or an explicit
footer blocker leave submission clearance pending/blocked; advisories remain advisories.
Own-words checks remain admin-controlled, and recorded clearance never certifies authorship or acceptance.

For optional blind diagnostics, read the applicable role prompt and launch a fresh agent with
no inherited chat (`fork_turns: none`). Give only the exact question and one prepared document
packet, never writer history, gold, notes, selected evidence or tags. A closed-book worker gets
only the question and no tools/files; an independent reviewer gets frozen fields and raw returns.
An optional removal probe uses a fresh solver on a renumbered packet without the tested document.

Hand over every form field, failure modes included, with
`python tools/check_questions.py tasks/<slug> --handover --q qNN` (notes/handover-qNN.md).
It also writes questions/qNN.json when inputs can be encoded. For JSON input values alone use
`--json --q qNN`; this serializes existing fields without rerunning validation or changing Markdown.

For tool changes run `python tools/test_docket_tools.py` and `python tools/test_docket_agent.py`
(the second also runs tools/test_lever_mine.py).
Use [tools/docket_agent.py](tools/docket_agent.py) to screen sketches, freeze final content,
report current evidence and replay historical rejections without modifying them. Known source
gaps need substantive candidate-specific assessment by the author or supplied platform evidence;
no independent model is mandatory, and unrelated gaps cannot waive missing necessary material.
