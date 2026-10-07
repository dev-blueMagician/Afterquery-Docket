# q04 rev 0 - question-review

- Date: 2026-10-05
- tested_sha256: aedaeb4bfdef37145e3c29a92bde1a268f91091544df22d6e1c7f41577e2dc1c
- source_gaps_sha256 (as stated by the reviewer): 482e178fa029ca11a664427aba78990c8f2206303c7508fdadd711d962234b19
- Role: question-review, fresh context; input = root, slug, q04, rev 0, fingerprint, target easy,
  the run's results/ files (solver-A, solver-B, shortcut-audit, closed-book), sibling note on q01.
- Usage: 250,118 subagent tokens, 61 tool uses, 711 s.

## Raw return (verbatim)

q04 (rev 0; tested_sha256: aedaeb4bfdef37145e3c29a92bde1a268f91091544df22d6e1c7f41577e2dc1c)

**gold_verified:** yes. I recalculated with a script from D05 l.195, D06 l.173 and D07 l.177. Each footnote is byte-identical in text/ and docs/.
- Midpoints (Feb / Apr / Jul, $M):
  - U.S. & Canada: 5,090 / 5,090 / 5,090
  - Latin America: 1,655 / 1,740 / 1,800 (+85, +60)
  - Africa & APAC: 1,545 / 1,605 / 1,630 (+60, +25)
  - Europe: 1,040 / 1,040 / 1,040
  - Data Centers: 1,185 / 1,185 / 1,210 (0, +25)
- Both ends of every range move by the same amount. Judging "raised" by the low end, the high end, the midpoint or the printed growth rates gives the same set: Latin America, Africa & APAC. Measuring both updates against February also gives the same set.
- The five segments are the whole universe:
  - Segment lows and highs add up exactly to the totals: 10,440–10,590 (D05 l.183), 10,585–10,735 (D06 l.161) and 10,695–10,845 (D07 l.165).
  - The midpoint changes of 145 and 110 match D06 l.155 and D07 l.159.
- The premises hold:
  - The updates are "as of April 28, 2026" (D06 l.149) and "as of July 28, 2026" (D07 l.153), each measured against the "prior 2026 outlook" (D06 l.153, D07 l.157).
  - There were exactly two updates: "second time this year" (D07 l.41).
  - The fiscal year is the calendar year, so "full-year 2026" is pinned.

**outcome:** A: match; B: match. Both answered "Latin America and Africa & APAC" (an equivalent form) with high confidence.
- Both runs are rev 0 on this fingerprint and used separate packets (solver-1, solver-2). Their returns cite only packet files, and the read guard was bound to this run.
- B raised "FX-driven increases might not count". That reading is not defensible: D06 l.155 and D07 l.159 call increases that include FX "raising".
- That gives two fresh, uncontaminated matches.

**closed-book:** misses. It answered "Data Centers" with low confidence, as an inference about a period after its cutoff. That is not equivalent to the gold, and it is the decoy.

**necessity:**
- **D05** is the only source of the pre-April segment ranges. D06 gives only consolidated FX (+$107M, l.153) and the total raise (+$145M, l.155), and its growth rates are "vs. Prior Year" (l.159). Without D05, no segment's April change can be determined.
- **D06** is the only source of the April ranges. Without it, February to July shows Latin America, Africa & APAC and Data Centers all higher. D07's l.157, l.159 and l.41 are consolidated only, so Data Centers cannot be excluded.
- **D07** is the only source of the July ranges.
- Bundle-wide search: all 15 range endpoints appear only in these three footnotes. Other hits are unrelated: an Argentinean peso rate (D05 l.175) and 2025 capex totals (D03 l.259, D04 l.261). D01–D04 contain no 2026 outlook; their only "2026" is "into 2026" at D04 l.55.
- No smaller valid set exists.

**shortcut:** clear. The verified shortest route matches the auditor's: D05 l.195, D06 l.173, D07 l.177, with five segments compared twice.
- No passage states segment-level changes. The outlook narratives (D06 l.155, D07 l.159) are consolidated only.
- The CEO quotes name no segment change (D06 l.43–45, D07 l.41).
- The capture overview's summaries for Docs 5–7 contain no outlook figures.
- One phrase search finds all three inputs. That is input retrieval, not a whole-answer lookup.

**source_assessment:** All 151 labels are irrelevant to all six dimensions (source_gaps_sha256 482e178fa029ca11a664427aba78990c8f2206303c7508fdadd711d962234b19).

Shared evidence:
- The 2026 outlook sections (D05 l.171–335, D06 l.147–313, D07 l.151–317) contain no markers. The first markers are at D05 l.439, D06 l.415 and D07 l.419.
- The docs/ originals carry the same markers at the same sizes.
- Each document's marker sizes add up exactly to its stated shortfall, so there is no unmarked omission.
- Every marker sits between visible row labels of a table of actual results.

Per group:
- **G1, balance sheets:** D02 449/455/461; D03 449/455/461; D04 451/457/463; D05 439/445/451; D06 415/421/427; D07 419/425/431.
  - Premises: these are quarter-end balances, while the premises sit at D06 l.149–155 and D07 l.41/153–159.
  - Gold: they hold no revenue outlook.
  - Exclusions: they cannot change the U.S. & Canada, Europe or Data Centers ranges.
  - Uniqueness: balance sheets are not split by segment.
  - Necessity: they cannot restate the February or April ranges.
  - Shortcut: numeric rows only.
- **G2, statements of operations:** D02 473/479/489; D03 473/479/489; D04 475/481/491; D05 463/469/479; D06 439/445/455; D07 443/449/453/457.
  - Premises: actual-period rows carry no update dates.
  - Gold: they report actual revenue for past periods, not an outlook.
  - Exclusions: they cannot alter the outlook footnote ranges.
  - Uniqueness: consolidated lines, no segment columns.
  - Necessity: the comparison columns are prior actual periods, not a prior outlook.
  - Shortcut: income-statement rows can hold no raise statement.
- **G3, cash flows:** D02 545/549/553/557/561; D03 541/545/549/553/557; D04 539/543/547/551/555; D05 527/531/535/539/543; D06 489/493/497/501; D07 487/491/495/499.
  - Premises: cash movements only.
  - Gold: no outlook figures.
  - Exclusions: they cannot change any outlook range.
  - Uniqueness: not split by segment.
  - Necessity: year-to-date actuals.
  - Shortcut: D07 l.491 may hold the Philippines/KTBL sale proceeds; that is actual cash, not an outlook raise.
- **G4, segment results tables:** D02 591/607/619/653/669/681; D03 587/603/615/649/665/677; D04 587/603/615/649/665/677; D05 573/589/601/629/645/657/685/701/713/743/759/771; D06 533/549/561/589/605/617; D07 535/551/563/593/609/621.
  - Premises: segment identities are confirmed by the visible headers (e.g. D06 l.531).
  - Gold: these are actual quarters and years.
  - Exclusions: actual Q1/Q2 2026 segment revenue cannot alter outlook ranges.
  - Uniqueness: the gaps are row blocks under visible column headers, so there is no hidden segment.
  - Necessity: comparison columns are prior-year actuals, not prior outlooks.
  - Shortcut: an outlook-change sentence would sit in the marker-free outlook section.
- **G5, reconciliations of actuals:** D02 711/737/741/787; D03 707/733/737/781; D04 707/733/737/783; D05 797/823/827/871; D06 643/663/667/691; D07 647/667/671/695.
  - Premises: they cover consolidated EBITDA/FFO/AFFO only.
  - Gold: no segment property revenue.
  - Exclusions: they cannot move segment ranges.
  - Uniqueness: not split by segment.
  - Necessity: the 2026 outlook reconciliations (D05 l.255–331, D06 l.233–309, D07 l.237–313) are fully visible and consolidated only.
  - Shortcut: numeric rows only.
- **G6, segment gross-margin reconciliations:** D02 801/815; D03 795/809; D04 797/811; D05 887/895/905/913; D06 701/709; D07 705/713.
  - Premises: headers are visible.
  - Gold: these are actual margins.
  - Exclusions: they cannot change the outlook.
  - Uniqueness: the same five property columns appear in the visible headers.
  - Necessity: actual-period rows cannot restate the outlook.
  - Shortcut: numeric rows only.
- **G7, document-level labels** for the six docs/ files (7,808; 8,081; 8,464; 11,021; 7,412; 8,075): each equals the sum of that document's markers above. D02–D04 were published before the first 2026 outlook (D05 l.173), so they cannot hold one.

Readiness consequence: the gaps do not block this question once the Source assessment is recorded (verdict unaffected, bound to both hashes, findings keyed by every exact label). The corpus stays labelled incomplete.

**difficulty:** easy. This is local suitability only.
- In favour:
  - The deciding facts exist only in this bundle and postdate the closed-book solver's cutoff.
  - No passage or overview gives the membership.
  - Data Centers is a plausible decoy: it is named in July's rationale and in the CEO's CoreSite remark (l.41), and it was raised in July. Only the February-to-April comparison removes it.
  - Africa & APAC was raised twice but is never named in any raise rationale.
  - The shape matches the Guide's worked example 1.
- Risks (D3, D4, D7):
  - The inputs are three identically worded footnotes that one search finds.
  - Whole ranges shift, so no arithmetic is needed.
  - The April comparison alone already yields the gold; the July condition excludes nothing.
  - A similar labelled-cell comparison was solved at the platform's lowest tier before (trial-07 q05).
- Too-easy risk is moderate to high. There is no platform evidence yet.

**verdict:** ready (local). Status should become checked, platform pending.

**findings:**
1. **Records (Q13).** The Blind solve, Shortcut audit and Review sections of q04.md are empty, and `report` shows no records for this revision. Enter the A, B, closed-book, audit, review and Source assessment lines at rev 0 with aedaeb4b…. These sections are outside the fingerprint, so entering them invalidates nothing. Status stays checked until an exact-content platform pass at Easy or above.
2. **Lever label (Q11).** "Mentions it vs does it" does not describe what happens here. Each segment named in a rationale was actually raised at that update (Latin America in April, Data Centers in July). The mechanisms that actually work are: the edition sequence (skipping or mis-baselining April adds Data Centers, script-verified); incomplete prose (reading only the rationales gives none, Latin America, or Latin America plus Data Centers). The levers and lever-checks fields are not in the fingerprint, so correcting them needs no retest.
3. **Reasoning wording.** The decoy note says Doc 6 "never mentions Africa & APAC". That is literally false: D06 l.173, 181, 197 and 531 name it. Only the rationale at l.155 omits it. The consequence is low. Fixing it changes a field the fingerprint covers, which means a new revision, a fresh prepare and fresh checks.
4. **Sibling q01.** It uses the same footnote evidence and the same phrase "full-year 2026 property revenue", but the asks differ: q01 wants one April midpoint reached through the sale date, q04 wants membership across both updates. Neither gives the other away. Across the set, q01, q02 and q04 are all outlook-revision questions. If more are added, vary the source relationship (e.g., the South Africa Fiber gain period D02 l.107 and D06 l.671 vs D07 l.675; the buyback programs D04 l.171 vs D05 l.143).
5. **Floor WARNs.** The single-passage hits are segment names appearing together: the 2025 "international" definition (D02/D03 l.201/225, D04 l.203/227) and the 2026 outlook footnotes. None of them gives the membership. origin: claude is accurate; the export tool takes only origin: user, so whether to submit is the user's decision.
6. **Platform-only checks, unknown:** whether the form treats the "&" in "Africa & APAC" as a list separator; whether "in any order" is accepted; restricted names, originality and duplicate checks; token window.
