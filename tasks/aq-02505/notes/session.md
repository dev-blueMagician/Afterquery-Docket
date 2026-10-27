# aq-02505 checkpoint (2026-10-10)

- Goal and user constraints: user 2026-10-09 "let's work on AQ-02505_2026-10-09_1045. there is no slot for Easy
  Tier for this bundle, we should target medium and high. do your best." Page: Hard 0/2 · Medium 0/3 · Easy 0/1,
  9 submissions, 0 of 10 quick tests; capture warned "Docket has been updated. Reload this page".
- Verification target / measured platform tier: medium (hard welcome). Five runs, none usable: q01 rev 0 Easy
  (Low 1/5), rev 1 "Too hard" (0/15), rev 2 Easy (Low 1/5); q02 Easy (Low 1/5); q03 "Between levels" (Low 0/5 ·
  Medium 0/5 · High 5/5, Run 5). Difficulty runs left: 5 of 10.
- Prepared run / tested_sha256: q04 rev 0, e5563dcdf1df206cd884939377863e39622733600c408b758c0ea441331a0874
  (runs/q04-r0-v2-e556...-platform). Earlier fingerprints are in each question's Platform validation.
- Bundle: seven FR texts D01-D07 = page Doc 1-7: DOL H-2B survey NPRM (Nov 2024), DHS UFLPA Entity List notices
  (Nov 25, 2024; Jan 15, 2025; Aug 3, 2026), NOAA seafood COA NPRM (Dec 2024), USTR Section 301 forced-labor
  determinations (Jun 2026), CBP supply-chain ANPRM (Sep 2026). Complete capture, no gaps; D05 Annex A omitted
  at source (graphics). Read in full by the caller (notes/doc-map.md).
- Phase: decision returned to the user after q04's quick test (user, 2026-10-10: "q04 too easy for quick test"; no panel).
  No live question: q01-q04 are dropped with their records.
- Last question q04 (dropped): "To one decimal place, what percentage of the entities first placed on the UFLPA Entity
  List from November 25, 2024 through August 3, 2026 mine or source copper or lithium?" = 4.6% (5 of 109). Set:
  q03's five names (Ashele excluded, already on Doc 2's (ii) list). Base: 187 - (107 - 29) = 109 (Daqo, one of
  Doc 2's thirty additions, first listed June 2022). Traps: 6/109 = 5.5% (Ashele), 5/110 = 4.5% (Daqo). Docs 2,
  4, 6. Floor 0 FAIL / 3 WARN (origin; 107 and 187 in words, expected false alarms). notes/handover-q04.md.
- Measured solver behaviour (verdicts f2-f6): an already-listed check is cleared by the low model in 3 of 20
  attempts (Runs 1, 3, 4, 5), by the medium model never (it takes each notice's "adds" sentence as first
  placement), by the high model every time measured. One such check lands Easy or Between levels. All levels read
  an unprinted bare date as a typo (Run 2). Low recalls 2024-25 totals closed-book; 2026 facts are not recalled.
- Decisions: only the UFLPA series gives cross-document structure (hooks.md rounds 1-4). q01-q03 dropped with
  their records. q04 is the one focused repair for Between levels: both checks in one figure. Rejected this
  round: h23 (iron ore widening), h24 (event-anchored window). The Coach's near-miss example (Xinjiang Zijin
  Nonferrous) smelts zinc, not copper or lithium; its full-legal-name point no longer applies (numeric gold).
- Standing conclusion (f7): with a hidden already-listed check the result is Easy or Between levels; without one
  the low and medium models read the notices alike. No hook in rounds 1-4 separates medium from low or stops high.
  Do not patch wording; a new attempt needs a mechanism not yet in hooks.md.
- Feedback index: notes/feedback-index.md f1-f7 (trial owner: workspace notes/feedback-index.md). Revision
  rounds: q01 2, others 0.
- Efficiency: five trial slots full (promote refused), unpromoted work. Sessions c8068b6d, 31a6542d, cb246dc7
  and 693f73b6 (i08 draft, 4 minutes; the Run 5 analysis before it was not timed) are stopped.
- Next action: the user's decision: release the bundle, or use an Easy result if that slot is usable (q02 rev 0,
  ae90f7cd..., Run 4, Version b94f39: "In band — Easy tier ... You can submit now"; the page calls a result final
  for its version, so restoring that exact content may restore it; not verified). 5 difficulty runs unspent.
- Runtime/model/effort: Claude Code, claude-opus-5-5, max effort (settings.json).
