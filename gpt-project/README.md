# Docket agent v2.1

This package replaces the previous maximum-only question writer with evidence-driven generation
and independent shortcut checks. Its default target is Easy. Actual Docket measurement is still
required; local tests and a review cannot guarantee a platform pass.

## Local workspace

[WORKFLOW.md](../WORKFLOW.md) is the canonical procedure; local agent roles live under
`.claude/agents/` and commands under `.claude/commands/`. Codex reads [AGENTS.md](../AGENTS.md).
New candidates carry `difficulty_target: easy|medium|hard`.

```powershell
python tools/docket_agent.py screen tasks/<slug> --idea iNN
python tools/check_questions.py tasks/<slug> --q qNN
python tools/check_questions.py tasks/<slug> --handover --q qNN
python tools/docket_agent.py prepare tasks/<slug> --q qNN
python tools/docket_agent.py report tasks/<slug> --q qNN
python tools/docket_agent.py replay
python tools/test_docket_tools.py
python tools/test_docket_agent.py
```

Prepare produces immutable-by-convention snapshots and separate document-only check packets,
validates bytes before reusing a run, and binds the solver guard to the active bundle/run.
It does not launch models, enforce OS isolation or authenticate a platform response.

Claude's blind roles set `omitClaudeMd: true`; that option requires Claude Code v2.1.271+.
The closed-book role exposes a tool declaration but its hook denies every tool call, avoiding
zero-tool launch issues. See [official subagent configuration](https://code.claude.com/docs/en/sub-agents).
Check runtime support before counting blind checks. If unavailable, use isolated chats instead.

## Portable Writer, Solver, Shortcut Auditor and Reviewer

The prompt files describe roles, not an API service or automatic platform connection:

| File | Purpose |
| --- | --- |
| instructions.md | Writer instructions |
| playbook.md | Portable complete workflow and acceptance gate |
| lessons.md | Historical verdicts and v2 calibration policy |
| solver-instructions.md | Document-only blind solver |
| shortcut-instructions.md | Question-only shortest-route auditor |
| reviewer-instructions.md | Independent evidence and fairness reviewer |
| ../instruction.md | Local platform guide |
| ../tools/check_questions.py | Mechanical floor |
| ../tools/docket_agent.py | Lightweight sketch screen, packets and readiness report |
| ../tools/split_capture.py | Capture parsing/provenance dependency |
| ../tools/agent_scope.py | Local Claude path guard |

Use separate fresh contexts for the two solver runs, shortcut audit, no-files closed-book check
and review. Supply full document packets only to solvers/auditor, and no writer history or gold.
A reviewer gets frozen fields and actual raw returns. Existing project memory or shared chat
history defeats independence; do not claim isolated verification if it cannot be established.

The writer records genuine returns with the prepared hash. It hands back changed files if it
cannot persist them. Authorship remains accurate and the current export accepts user-origin
questions only. Platform-restricted names, originality and token-window checks remain external.

## What changed

Historical failed questions often had a short semantic retrieval route despite being labelled
maximum locally. The redesign adds a dedicated shortcut auditor, all-bundle necessity checks,
two matching gold solves, source-gap provenance, exact-content fingerprints, configurable
targets and explicit platform verdicts. It preserves originals and historical questions.

The v2.1 workflow adopts hook discovery, lean sketch screening, note-based original phrasing,
independent calculation/date checks and set-level review from D:\Docket_new. It scopes decoy
attacks to the selected levers, permits ordinary valid cross-document reasoning, and uses
candidate-specific source-gap assessments. Older trial quotas/word limits/style-kit claims
were not adopted as current platform facts.

Historical lessons remain evidence. No stored result yet positively calibrates the redesigned
agent or demonstrates its Easy pass.
