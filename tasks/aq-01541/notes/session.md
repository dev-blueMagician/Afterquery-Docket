# Current bundle checkpoint

- Goal and user constraints: user 2026-10-08: "work on AQ-01541 ... there is no slot for Easy Tier for this bundle, we should target medium and high. do you best." Slots: Hard 1/2 · Medium 0/3 · Easy 1/1 (Easy full); 7 submissions left; 8 of 8 difficulty runs left; quick tests 0 of 10.
- Verification target / measured platform tier: medium (hard optional) / pending for all. An Easy-tier result is unusable here.
- Runs: q01 rev 1 6fa78753...; q02 rev 0 d365e12c...; q03 rev 0 50960993...; probe runs q01-r0-alt-k3, q02-r0-alt-m6.
- Bundle: aq-01541, seven Brooks v. Trans Union rulings, complete capture, no gaps. Ids vs page: D01 = Doc 1, D02 = Doc 2, D03 = Doc 7, D04 = Doc 3, D05 = Doc 4, D06 = Doc 5, D07 = Doc 6.
- Phase: handed over (2026-10-08). notes/handover-q01.md, -q02.md, -q03.md generated from checked files.
- Questions (all checked; floor 0 FAIL; origin WARN; q01/q02 sibling WARN intended):
  - q01 rev 1 (63.3%; Doc 6 + Doc 7): A/B match, closed-book miss, audit clear, probes off the gold; review ready, easy (marginal toward medium), usable ~15-20%.
  - q02 rev 0 ($29.1; Doc 6 + Doc 7; alternative to q01, never both): A/B match, closed-book miss, audit clear, probes off the gold; review revise (one failure-mode attribution, fixed, outside the fingerprint), easy, usable ~18%; preferred narrowly over q01.
  - q03 rev 0 (-10.0 pp; Doc 4 + Doc 6): A/B match, two closed-book misses (one forced: +20.0 p .01), audit clear, probes off the gold; review ready, easy, usable ~20%. Fallback precision whole points if the 0.1 split is raised.
- Set: submit at most one of q01/q02; q03 shares the March/April trap and 20,891 with them (one reviewer: avoid q02+q03; another: q03 with one of q01/q02 is fine).
- Decisions: h1 and h12 are the only Medium-type mechanisms; others rejected (hooks.md). Source errors avoided (Doc 4 March 2021 projections; Doc 7 "30 percent", June 24/25, January 2025; Doc 2 "2021"; 57,233 vs 57,208).
- Revision rounds: q01 one (form fix). Open platform feedback: none.
- Next action: user quick-tests (form's free "One defensible answer" check first); then a difficulty run only on a quick-test survivor; record any platform result verbatim against the tested fingerprint.
- Runtime/model/effort and independent-context method: Claude Code, Opus 5.5 max; blind roles via agents with omitClaudeMd and the read guard.
