# Docket workspace instructions

Follow [CLAUDE.md](CLAUDE.md), [WORKFLOW.md](WORKFLOW.md), and the platform guide in
[instruction.md](instruction.md), with the latest user's Easy-minimum target taking precedence
over historical High-only notes. Runtime-specific model settings in `.claude/` describe the
Claude deployment; use the actual current Codex runtime and record its authorship accurately.

Do not alter bundle originals or submitted/accepted questions. Find cross-document hooks and screen lean sketches before full evidence/write-up. Apply attacks
to the chosen levers; decoys are required for which-items questions, not every possible ask.
Ordinary cross-document arithmetic/date/ID joins are eligible; reject demonstrated Guide violations. Local checks and test
counts do not prove a Docket tier pass. New questions carry `difficulty_target: easy|medium|hard`
and checks must match the prepared snapshot fingerprint.

When delegating a blind solve or shortcut audit, launch a fresh agent with no inherited chat
(`fork_turns: none` where available). Give only the exact question and one prepared document
packet; never pass this writer's conversation, gold answer, notes, selected evidence or tags.
Read the applicable role prompt explicitly. Give a closed-book worker only the question and
no tools/files, and an independent reviewer the frozen fields plus raw returns.

Hand over every form field, failure modes included, with
`python tools/check_questions.py tasks/<slug> --handover --q qNN` (notes/handover-qNN.md).

For tool changes run `python tools/test_docket_tools.py` and `python tools/test_docket_agent.py`.
Use [tools/docket_agent.py](tools/docket_agent.py) to screen sketches, prepare final checks,
report current evidence and replay historical rejections without modifying them. Known source
gaps receive candidate-specific review; unrelated gaps cannot waive missing necessary material.
