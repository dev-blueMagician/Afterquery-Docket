# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-08 "let's work on AQ-02157_2026-10-08_1559. there is no slot for
  Easy Tier for this bundle, we should target medium and high. do your best."
- Verification target / measured platform tier: medium / q04 rev 3 PASSED "In band — Medium tier" (Run 3, Low 0/5,
  Medium 2/5); q01 unmeasured.
- Page state at intake: Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions left; 0 of 10 quick tests;
  8 of 8 difficulty runs.
- Bundle: five UK tobacco/vaping policy documents; D02=Doc 1 smokefree consultation, D01=Doc 2 its response,
  D05=Doc 3 pack-insert consultation, D03=Doc 4 its impact assessment, D04=Doc 5 its response. Full corpus.
- Phase: q04 ready (difficulty passed; submission is the user's); q01 handed over, platform pending.
- Questions:
  - q01 rev 5 checked, 31ee6be207fec2e31b9554f6ffb88468957934a8e4da7ea61902e30faad720c6: 2030 gap between the
    highest and lowest UK nation repeating each 2021-22 point change (Doc 3 + Doc 1) = 8.9 points. Form history:
    rev 1 "Say the rounding"; rev 2 six number flags; rev 3 only Step 13 (15.6); user's rev 4 wording still 15.6
    (labelled "Step 5"); rev 5 drops the subtraction of percentage-typed 2030 rates (0.1 + 8.8 = 8.9 in points).
    Probes: no Doc 3 misses (7.4); no Doc 1 forced the gold at p 0.1 (stated residual risk).
  - q04 rev 3 READY, 7790f824581b6cbee3fc9b98c51688851c9be1ebb33fc803cdb71472d6961f49 (origin user+claude):
    "What is the increase in the minimum excise duty on a pack of 20 cigarettes, to one decimal place, from the pack
    insert impact assessment to the government's response to the smoke-free consultation?" gold £1.5. Run 3 In band
    — Medium tier (Low 0/5: £0.6 x4, £0.5 x1; Medium 2/5: £0.5 x3). Runs 1-2 Too hard on paraphrases (f7, f8).
  - q01 rev 0 superseded (2032; probes guess-reached via remembered Scotland rates).
  - q02 dropped (Netherlands/Finland flavour mapping recalled, p 0.65); q03 dropped (directions recalled).
- Handovers: notes/handover-q01.md, notes/handover-q04.md (whole form, Doc N numbering).
- Optional diagnostics used (concrete recall concern): removal probes, runs q01-r0-alt-h7, q02-r0-alt-m3,
  q01-r1-alt-c4, q03-r0-alt-p9, q04-r0-alt-f2 (bound in .claude/solver-scope.json; raw returns in results/).
- Five-candidate trial: not enrolled (slots full); efficiency timer not started (aq-02147's timer active).
- Form rules: notes/helpers/form_check_v10.py (lists read; deep text unread; identical-string reuse; a result
  typed as a percentage, by "per cent"/"%" after it or "in %" before its expression, is not reusable as plain r).
  Feedback: notes/feedback-index.md f1-f9. Expected remaining flags: q01 none; q04 Steps 1-2 (deep text).
- Next action: user submits q04 (record any acceptance/Checks words). q01 rev 5: form reaction pending; before its
  difficulty run get the user's final question wording and align the record/gold to it; quick test first.
  7 of 10 difficulty runs left (8 of 50 in 24 h across tasks).
- Reserve: h4 (vape profit, fairness doubt). Bundle lesson: answers must depend on exact document values of
  the least-remembered items; direction-only filters on public statistics are recalled.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5), max effort, Claude Code VS Code extension.
