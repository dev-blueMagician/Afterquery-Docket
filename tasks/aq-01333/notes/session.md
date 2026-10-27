# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06 "work on AQ-01333_2026-10-06_1150 ... difficulty_target to at least medium". Slots: the capture showed Hard 0/2 · Medium 0/3 · Easy 0/1. The standing page line "Still open on this set: Hard, Medium, Easy." was still shown on 2026-10-08, so the single Easy slot is unfilled. 9 submissions, 8 difficulty runs, 10 quick tests at capture; 4 of 8 runs left (assumed).
- Verification target / measured platform tier: medium. q01 rev 4 passed at the Easy tier (user report) and was submitted 2026-10-07. The platform reviewer returned it, "Revision requested": question and gold correct, Doc 5 not necessary. Earlier results: q02 Too easy; q01 rev 1 Answer not supported; rev 2 Too easy.
- Current runs: q01 rev 5 q01-r5-v2-f6b3318d49235652e301180a068020df2e8835966fcbc2df3c8dfaaa84710c1c (2026-10-07: A match, B match, audit clear, closed-book misses, review ready, local difficulty easy). Removal probes 2026-10-08 in q01-r5-alt-h3: without Doc 4, 61.7%; without Doc 6, not answerable (forced 41.7%). Both miss. Status checked.
- Bundle: six HPE earnings releases. Local id = platform Doc, quarter, date:
  - D01 = Doc 4 (Q1 FY26, 2026-03-09)
  - D02 = Doc 1 (Q2 FY25, 2025-06-03)
  - D03 = Doc 5 (Q2 FY26, 2026-06-01)
  - D04 = Doc 2 (Q3 FY25, 2025-09-03)
  - D05 = Doc 6 (Q3 FY26, 2026-09-02)
  - D06 = Doc 3 (Q4 FY25, 2025-12-04)
  Text = originals except NFKC; pipe tables only.
- Phase: 2026-10-08, the user re-sent the same Revision requested panel. Rev 5 already implements it (Doc 5 unticked and the note deleted, no Doc 5 evidence row, Step 2 the reviewer's sentence). Added outside the fingerprint: Targeted failure modes (one trap: Wrong year or edition / Uses the wrong period or date; Doc 5's June range gives 11.8%; the December 61.7% trap was withdrawn) and the two probes. Independent review of these additions, 2026-10-08: probes pass, hand-over matches, ready (local). Its one failure-mode overclaim and the record errors were fixed. Hand-over regenerated: notes/handover-q01.md.
- Platform: rev 5 unticks Doc 5, so a new difficulty result is needed before resubmitting ("any edit to the question, answer or necessary documents needs a new result"). Paste every field from the hand-over, tick Doc 4 and Doc 6 by hand, then run the check. If the form flags Step 2's numbers, use the contingency Steps 1-2 in q01 Lever checks (Revision 5); that would be rev 6, with re-run checks.
- Questions: q01 rev 5 checked (above). q03 checked rev 0: day cue "On the day", likely too easy. Do NOT mark its Doc 2 as exclusion source (reviewer ruling). q02 dropped.
- Families: h01 and h09 promoted (edition bridges); h02 promoted (recast); h03-h08 and h10 held. No third Medium design was found.
- Revision rounds: q01 5 (rev 5 = reviewer-requested); q03 0; q02 dropped.
- Next action: after the user's new difficulty run, record it under Blind solve (verbatim tier line, per-document lines and feedback). On resubmission, set status submitted and take accepted_tier from that rev 5 result, not from rev 4's. The form must hold exactly the 5 rev 5 evidence rows before any result is bound to f6b3318d.
- Runtime: Claude Code, Opus 5.5 max. Blind roles run as fresh non-fork subagents with omitClaudeMd and the scope hook. Project memory: D:\Agents\Docket\.claude\memory (D:\Dev\Docket\.claude\memory is an empty leftover).
