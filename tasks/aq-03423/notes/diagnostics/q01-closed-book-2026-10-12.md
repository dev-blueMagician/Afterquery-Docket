# q01 closed-book probe, 2026-10-12 (optional diagnostic, one run)

Reason: a concrete issue on q01. Its gold is a public statistic (fixed broadband shares in the Commerce
Commission's 2017 monitoring report), so the platform's one closed-book attempt and its Document check could
reach it without the documents.

Not bound to a snapshot: it ran before `prepare`, on the wording without "to the nearest percent". The frozen
rev 0 (tested_sha256 5f25fda0ea48e13730bd649900b696638691b6e3c36adbbca5c1f49f0961e64b) adds only that phrase.
It is not a platform result and says nothing about a tier.

Role: closed-book-solver (claude-opus-5-5, role file .claude/agents/closed-book-solver.md). Input: the
question text only.

Question sent: "On the Commerce Commission's December 2017 monitoring figures, what share of the fixed
broadband market did New Zealand's two largest mobile network operators hold together?"

Return, verbatim:

    answer: About 70% (Spark roughly 44% plus Vodafone roughly 26%)
    confidence: low
    basis: Memory of the Commerce Commission's Annual Telecommunications Monitoring Report 2017 (published December 2017); the two largest mobile operators were Vodafone and Spark. The individual shares are recalled approximately and could each be off by a point or two, so the sum could be 69-71%. No tools were called.
    contaminated: yes - the session was not question-only. Auto-attached context included a git status snapshot (branch, Docket workspace file paths, task ID aq-00949, agent/memory file names, recent commit messages), the working directory path, and the user's email. None of it contained document excerpts, an answer key, hints, or anything bearing on this question, and it was not used.

Reading (author's, not the probe's):
- The return is contaminated by the harness's auto-attached workspace context, so by the role's own rule it does
  not establish the check. The attached context held nothing about this bundle.
- It answered 70%, not the gold 71%, and named its own range as 69-71%. The statistic is recalled to within a
  point. A solver that recalls 44% and 27% would reach 71% without the documents.
- Stated risk for q01: the platform's "Needs the documents" check and its Document check may be reached by
  recall. q02 has no such exposure (plan prices and a three-month offer from the submissions).
