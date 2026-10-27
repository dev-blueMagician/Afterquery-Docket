# Closed-book solve (q01 rev 0)

- Date: 2026-10-08
- Role: fresh closed-book-solver (non-fork, omitClaudeMd; the hook denies every tool call), question text only.
- Result: misses (answered "unknown").
- Self-reported context: the harness auto-attaches a git-status snapshot (file names of other tasks and memory files, commit messages, working directory, the user's email) to every session. The solver listed it under "contaminated" while stating none of it related to the question; no file contents, documents, notes or key were present. The blind solvers saw the same snapshot and reported "contaminated: no". It cannot carry this question's answer.

## Raw return (verbatim)

answer: unknown
confidence: low
basis: The question covers federal court rulings from July to September 2026. My knowledge ends in June 2026, so I don't know which whistleblower cases were decided in that window. I also don't know the key facts, such as whether a plaintiff reported to the SEC, OSHA, FAA or FDA while still employed. Any surnames I named would be guesses, so I'm not offering any. Answering would need the documents that identify those rulings and when each plaintiff reported.
contaminated: Yes, from context attached automatically. None of it related to the answer. It included a git status snapshot listing workspace and bundle file paths: tasks/aq-00949 run files (closed-book, solver, review and shortcut-audit results, plus shortcut/docs/eog_ex991_2020-03-16.txt) and the names of .claude/memory and gpt-project files. It also included recent commit messages, the working directory and the user's email. I saw no file contents and did not use any of it. Two tools were declared (Read and SubagentHandback), not one; I used only this handback.
