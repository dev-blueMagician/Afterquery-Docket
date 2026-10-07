# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06 "work on AQ-01333_2026-10-06_1150 ... difficulty_target to at least medium". Slots on capture: Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions, 8 difficulty runs, 10 quick tests left.
- Verification target / measured platform tier: medium. q01 rev 4 passed at the Easy tier (user report) and was submitted 2026-10-07. The platform reviewer then returned it as "Revision requested": question and gold correct, Doc 5 not necessary ("Without document 5 — 58.3%"). Earlier results: q02 Too easy; q01 rev 1 Answer not supported; rev 2 Too easy. 4 of 8 runs left (assumed one used).
- Current runs: q01 rev 5 q01-r5-v2-f6b3318d49235652e301180a068020df2e8835966fcbc2df3c8dfaaa84710c1c. Checks 2026-10-07: A match, B match, audit clear, closed-book misses; review ready (difficulty easy, local). Status checked. History: q01 r0-r4, probe q01-r3-probe-x4. q03 r0 cd238848; q02 r0 dropped.
- Bundle: six HPE earnings releases. Local id = platform Doc, quarter, date:
  - D01 = Doc 4 (Q1 FY26, 2026-03-09)
  - D02 = Doc 1 (Q2 FY25, 2025-06-03)
  - D03 = Doc 5 (Q2 FY26, 2026-06-01)
  - D04 = Doc 2 (Q3 FY25, 2025-09-03)
  - D05 = Doc 6 (Q3 FY26, 2026-09-02)
  - D06 = Doc 3 (Q4 FY25, 2025-12-04)
  Text = originals except NFKC; pipe tables only.
- Phase: q01 revision requested by the platform reviewer. The panel is logged verbatim in notes/feedback-q01.md; the screenshots are in runs/q01-r4-.../results/. Rev 5 is revised in place: status draft (checked after the checks); accepted_tier removed until resubmission.
- q01 rev 5 changes (exactly what the reviewer asked; question, answer, component and tags unchanged):
  - documents D01, D05;
  - Doc 5 unticked and the note deleted;
  - every Doc 5 evidence row dropped;
  - Step 2 is the reviewer's sentence;
  - Step 1's quote period moved outside the quotation marks;
  - decoy line uses Doc 5's own date only.
  The fields were handed to the user in labelled blocks after the user pasted step 2 into Evidence 2 ("NOT VERBATIM").
- Questions: q01 rev 5 draft (above). q03 checked rev 0: day cue "On the day", likely too easy. Do NOT mark its Doc 2 as exclusion source (reviewer ruling). q02 dropped.
- Families: h01 and h09 promoted (edition bridges); h02 promoted (recast); h03-h08 and h10 held. Author run 1 failed (output limit); run 2 found no third Medium design.
- Memory updated 2026-10-07 (exclusion-role lesson reversed; Revision requested panel; accepted-question rule). Files: platform-quality-checks, series-editions-necessity, calibration, redesign-v2, MEMORY.md, gpt-project playbook/lessons (user must re-upload).
- Revision rounds: q01 5 (rev 5 = reviewer-requested); q03 0; q02 dropped.
- Next action: wait for the user's resubmission. Then set status submitted, restore accepted_tier: Easy Tier and record any new difficulty result. If the form flags Step 2's numbers, use the contingency Steps 1-2 in q01 Lever checks (Revision 5); that change is a rev 6 with re-run checks. The form must hold exactly the 5 rev 5 evidence rows before any result is bound to f6b3318d.
- Runtime: Claude Code, Opus 5.5 max; blind roles run as fresh non-fork subagents with omitClaudeMd and the scope hook.
