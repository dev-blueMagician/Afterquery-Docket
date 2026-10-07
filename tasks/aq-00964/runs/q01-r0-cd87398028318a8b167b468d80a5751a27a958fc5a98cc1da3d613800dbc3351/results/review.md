# q01 rev 0 - question-review

- Date: 2026-10-05
- tested_sha256: cd87398028318a8b167b468d80a5751a27a958fc5a98cc1da3d613800dbc3351
- Role: question-review, fresh context; input = root, slug, q01, rev 0, fingerprint, target easy,
  the run's results/ files (solver-A, solver-B, shortcut-audit, closed-book attempts 1-2).
- Usage: 243,764 subagent tokens, 63 tool uses, 576 s.

## Raw return (verbatim)

q01 (rev 0; tested_sha256: cd87398028318a8b167b468d80a5751a27a958fc5a98cc1da3d613800dbc3351)

**gold_verified: yes**, but only on the visible text. Corpus completeness is still unresolved (finding 1).
- I recomputed the gold from the originals in `docs/` and in `text/`:
  - D07 l.117: the sale completed "On June 15, 2026".
  - D07 l.531 and l.567: the segment is Africa & APAC ("Includes results of Bangladesh and the Philippines through dates of sale").
  - Outlook dates: D05 as of February 24, D06 as of April 28 (l.149), D07 as of July 28 (l.153). June 15 falls between April 28 and July 28.
  - D06 l.173: $1,595M to $1,615M, so (1,595 + 1,615) / 2 = 1,605.
- D07 is the only document that dates the sale, so on this evidence D06 is the outlook that was current on June 15:
  - D06 announced the first raise (+$145M), and D07 l.41 calls July's the "second time this year".
  - The stated raises chain exactly: 10,515 + 145 = 10,660 (D06) and 10,660 + 110 = 10,770 (D07).
  - Each edition's segment midpoints sum to its total, and the implied 2025 segment base (about 1,422.3–1,422.9) agrees across all three editions.
- Alternatives I refuted:
  - 1,630 (D07's range): that outlook is dated after the sale.
  - 1,545 (D05): superseded on April 28.
  - 1,740 (Latin America): wrong segment.
  - 10,660: a total, not a segment.
  - The "at the midpoint" components table (pass-through 403, straight-line 70) is a breakdown, not the segment total.
  - KTBL's June 29 sale selects the same edition.

**outcome: A: match; B: match**
- Both returned $1,605M with high confidence. B's "About" is an equivalent form, since the midpoint is exact.
- Both cite D07 l.117/531/567/153/41 and D06 l.149/173, and both reject 1,630 and 1,545 on the dates.
- They used distinct fresh packets (solver-1, solver-2), declared themselves uncontaminated and list only files inside their packets.
- Each packet holds only `question.txt` plus a corpus whose hashes match the snapshot.
- The gap both solvers raised (an off-bundle update between April and July) is closed by the $110M chain.

**closed-book: misses**
- Attempt 2 answered about $1.35B at low confidence and recalled neither the closing date nor the 2026 outlook. That is about 16% off the gold, so it is neither equivalent nor near.
- Attempt 1 stopped on an API 529 error before answering. It is invalid, not a miss.

**necessity:** D06 and D07 together are the minimal set; no smaller set exists.
- **D07** is the only source of the completion date and of the explicit segment tie.
  - Without it, D02–D06 mention the Philippines only in FX-rate lists (D02 l.175, D03 l.175, D04 l.177, D05 l.175, D06 l.151).
  - All of them predate June 15, so even their clipped rows cannot carry the date, and the edition cannot be chosen.
- **D06** is the only source of the April Africa & APAC range.
  - Without it, D07 gives only consolidated changes (+$110M, FX +$35M; l.157–159) and its own range. D05 has only the superseded range.
  - 10,660 can be recovered from D07, but not its segment split, and D06's 12.8% growth rate appears nowhere else.
- D05 is a decoy source and is correctly left unlisted.

**shortcut: clear**
- The auditor's path matches my derivation and the documents (D07 l.117/531/567, then D06 l.149/173, then the midpoint, checked with D07 l.41/153).
- Its searches covered all seven documents ("Philippine", "divest", "held for sale", "Africa & APAC property revenue", 1,595/1,605/1,615).
- My own probes:
  - No passage or overview prints 1,605 or links the sale to an outlook.
  - "1,605" matches only the 1,605.2 beginning-cash figure (D06 l.507, D07 l.505).
  - "Africa & APAC property revenue" returns three ranges, and choosing among them needs the date join.
- Concrete warnings, though none is a trivial route:
  - A direct search for "Philippines" lands on the bridge date.
  - The answer is a calculation on a labelled range.
  - The capture overview lists "June 15, 2026" and "ATC Philippines" for Doc 7, which exposes the bridge but not the answer.

**difficulty: easy (marginal)**
This is local suitability for the Easy target only, not an observed tier.
- **D1 holds:** the deciding facts are 2026 and bundle-only, and the closed-book solve missed.
- **D2 holds for the answer:** only the bridge date shows in the overview.
- **D3 holds:** taking the outlook from the release that reports the sale gives 1,630.
- **D4 is weak:** that decoy is defeated by a date printed in its own document, and "then-current" prompts the check.
- **D5 holds:** dates, ranges and the raise chain are all explicit.
- **D6 holds:** there is one condition.
- **D7 partly holds:** the date lever changes the answer, but the Latin America and KTBL routes are already rejected by the wording or give the same answer. They are no evidence of difficulty.
- The shape is close to trial-07 q05, which the platform's low model solved: a fact in one document picks a labelled value in another.

**verdict: revise**

**findings:**
1. **Source completeness blocks readiness.** The report lists 151 known-gap identities (145 markers plus 6 capture notes; source_gaps_sha256 482e178f…4b19).
   - The markers sum exactly to each recorded omitted total (D02 7,808; D03 8,081; D04 8,464; D05 11,021; D06 7,412; D07 8,075), so nothing is missing outside the marked spots.
   - The first marker in each document comes after the narrative and outlook sections: D05 l.439 (outlook l.171–331), D06 l.415 (l.147–309), D07 l.419 (l.117, l.151–313). D07's footnote at l.567 is visible.
   - Every marker sits inside a balance sheet, statement of operations, cash flow, segment table or reconciliation.
   - For this question I found no possible effect on premises, gold, exclusions, uniqueness, necessity or shortcut:
     - Chronology rules out a duplicate date in D02–D06.
     - No historical-results table row can hold a 2026 outlook range.
     - Uniqueness rests on the visible text at D07 l.41 and l.159.
   - Even so, under my rules known clipped sources block readiness until a complete capture is re-ingested and every check is re-run on a fresh snapshot with a new fingerprint. All five current records would then be stale.
2. **Records bind but are not entered.** All five returns are rev 0 under the current fingerprint, and the report reproduces cd873980…3351. But `## Blind solve`, `## Shortcut audit` and `## Review` in q01.md are empty, so the report shows no current-revision records. Closed-book attempt 1 should be recorded as an invalid run.
3. **Too-easy risk (Q3/D4, not blocking).** The question has one live decoy, which a printed date defeats; the rest is an identifier search, a labelled range and a midpoint. The capture shows "Quick tests used: 0 of 10", so Easy survival has not been measured.
4. **Authorship and export.** `origin: claude` is accurate. Export accepts only `origin: user`, and the form's "I wrote this question myself" box cannot truthfully be ticked. This is separate from local readiness; do not change the origin to get around it.
5. **Passes:** the floor (0 FAIL, origin WARN only), all six quotes verbatim, 28 words, one ask, no semicolon, no giveaway, the period pinned, and local Dnn equal to the platform's Doc N per the capture headings. My emulation of the form's number rule on the reasoning passes, but that is unconfirmed on the form.
6. **Unknown (platform-only):** restricted names, originality and duplicates, the token window, and the form's model checks.
