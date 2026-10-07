# q05 rev 2 independent review (question-review, fresh context), completed 2026-10-06

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns, the rev 1 review and the
platform context only. Pasted unabridged.

q05 is locally ready. The gold checks out independently, both blind solves match on this exact fingerprint, the closed-book solve misses and the shortcut audit is clear. Keep status `checked` until the platform measures this exact content. Suitability for Easy is marginal, with a high risk of a "Too easy" result.

q05 (rev 2; tested_sha256: fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e)

**gold_verified: yes.** I recomputed it by script from the passages, not from the author's sums.
- **ROCE earnings for the twelve months: 22,247 by four routes.**
  - 13,581 (D10 l.405) − 6,469 + 15,135 (D12 l.389).
  - The four quarters: 3,942 (D09) + 3,170 (D10) + 2,603 (D11) + 12,532 (D12).
  - D09's nine months minus the first half, plus Q4 and the 2026 first half: 10,411 − 6,469 + 3,170 + 15,135.
  - The components: 20,591 + 374 + 1,282.
- **Capital employed:**
  - June 30, 2025: 176,725 (D08). Working back from printed averages gives 176,725 or 176,726 (from D12's 177,212 with D10's December 2024 balance; from D09's 206,935; from D08's 178,243 with D06's March 2025 balance).
  - June 30, 2026: 232,633 (D12), or 232,633 to 232,634 worked back.
- **Result:** all 12 combinations give 10.86916–10.86921%, so 10.87% every time.
- **The method is pinned.**
  - The start-and-end average reproduces the printed full-year averages: D10's 205,316 exactly, D05's 180,232 and D01's 183,173.
  - Averaging five quarter-ends (200,852) or the quarterly averages (199,737) does not.
  - The year columns are not annualized (D10 l.406).
- **Margin:** the answer flips only if earnings move by −8.6/+11.8 or average capital by +79/−109.
- **Wrong routes:** every one the author claims recomputes as stated: 10.84, 10.85, 10.86, 9.98, 9.78, 9.56, 9.52, 10.06 and 11.05.

**outcome: A: match; B: match.**
- Each solver ran in its own fresh packet. The packet holds the frozen question and the 12 documents only, and its bytes match the snapshot.
- Both paths reproduce 22,247, 176,725 and 232,633.
- Both rejected the five-quarter-end (9.98) and quarterly-average (9.78) readings using the footnote.
- No sign of contamination, and the read guard is bound to this run. Two valid matches.

**closed-book: misses.** It answered "unknown (rough guess 6–8%)" with low confidence, which is not equivalent to 10.87%.

**necessity:**
- **D12 is indispensable.** It is the only source of Q2 2026 and first-half 2026 ROCE earnings (12,532 / 15,135) and the June 30, 2026 balances. It is the latest release, so no later comparative repeats them.
- **D10 is indispensable for the exact figure.** It alone prints full-year and Q4 2025 ROCE earnings (13,581 / 3,170) and Q4's noncontrolling interest and after-tax interest (75 / 325); I checked this by grep across D01–D12.
  - Without D10, D11 offers only Q4 2025 earnings of 2,770 and a Q4 ROCE of 5.4%.
  - With Q4 average capital of 235,039 (D09 plus D11/D12), the 5.4% bounds Q4 ROCE earnings to 3,143.65–3,202.41. That gives 10.856–10.885%, which could be 10.86, 10.87 or 10.88.
- **Caveat:** natural estimates without D10 still land on 10.87. Taking 5.4% at face value gives 10.8707; borrowing Q3's add-backs (403) gives the same; borrowing Q1's (393) gives 10.8658.
  - This route needs more documents, so it is not a shortcut.
  - It is not an ambiguity either, because D10's exact figures settle the answer.
- **D08, D09, D05, D06 and D11 are replaceable.**
- **Smallest valid set: {D10, D12}**, which equals the documents field.

**shortcut: clear.**
- No passage prints a twelve-month ROCE. The only trailing-12-month figures are for CFFO (D11 l.368, D12 l.376).
- None of "10.87", "22,247", "204,67x", "176,72x" or "232,633" appears in the text.
- The overview gives only 8.3% (Q1 2025), 4.5% (Q1 2026) and 21% (Q2 2026). D12 l.19's "21 percent" is the Q2 figure, and D07's "double-digit ROCE" is a target.
- The auditor's shortest route (D10 + D12, working back June 2025 as 176,726) gives 10.8692%, which I confirmed. Search finds the inputs, not the answer.

**source_assessment: no gaps to map.**
- source_gaps is [], and its stored hash 4f53cda1… is the sha256 of "[]", which I recomputed.
- No "not shown" markers appear in D01–D12.
- All 25 snapshot hashes match the current corpus and all three packets.
- The capture says "12 of 12 captured in full".

**difficulty: easy (marginal, high too-easy risk).** This is local suitability only, not a measured tier.
- **For difficulty:**
  - No passage states the answer.
  - It takes about 10 labelled figures from two or three releases, two standard constructions (a rolling twelve months and a start-and-end average), plus working back one figure or a third lookup.
  - At two decimals, at least ten near-miss methods give wrong answers.
  - The figures are from 2026, after model cutoffs.
- **Against:**
  - The method footnote sits under every ROCE table.
  - There is no trap like the one in aq-00964 or aq-00745 that a quick reader takes.
  - On this bundle, questions built on lookups of labelled figures measured Low 5/5.
  - The route without D10 adds no extra way to fail.

**verdict: ready** (local only; the platform measurement is pending).

**findings:**
1. **Gold:** verified as above. No figure-choice exposure: every stated figure for every input gives 10.87, including D11's rounded 5.4% taken at face value.
2. **Records:** the snapshot diff from rev 1 to rev 2 shows only the decoy-line split and the revision number. Question, answer, components, evidence and corpus are identical.
   - The report recomputes fc72fa12….
   - The A, B, closed-book and audit lines all carry rev 2 and fc72fa12, and they match the raw returns.
3. **Necessity (advisory):** the caveat above. The Lever checks "Necessity" line says guesses give "10.87 or 10.88" but leaves out that the face-value 5.4% gives 10.8707. Lever checks are outside the fingerprint, so this is a records note only.
4. **Reasoning against the form's number rule (advisory, the form's reaction is unseen).**
   - Under the documented rule (each number in a named document or straight after "="), I emulated all ten steps and found no flags. "December 31, 2024" is in D10 l.539, "June 30, 2026" is in D12 and "6.6%" is in D10.
   - **First residual risk:** Steps 2–7 each use the shape "label = expression = result", so each has two "=" signs. The only precedent (aq-00949 q03) accepted the first "=" result in a step and rejected a later one. If the form exempts only the first "=", it could flag the six results: 22,247; 177,698; 176,726; 232,633; 204,679.5; 10.87%.
   - **Second residual risk:** if the form reads a step that names two documents as citing only the first one, it could flag inputs such as 6,469, 15,135 and 177,212, and 6.6% in the first decoy check.
   - Check on the form after pasting. Any edit needs a new revision, a new prepare run and a full re-check.
5. **Q14, platform-only, unknown.**
   - Ten of the 15 quotes match only after tabs are turned into spaces. The originals and the platform capture both contain tabs (for example, capture l.5193).
   - The other five quotes are exact, and each necessary document has at least one: D10 l.359/405/412 and D12 l.341/389.
   - The floor ignores whitespace differences. Whether the platform's verbatim check (a submit block) does the same is unseen.
6. **Q1–Q12 and rule 10 pass.**
   - 32 words, one ask, precision and an exact period stated, and no hint or reference to the document set.
   - The tags match work actually done, the levers are active, and no which-items decoy is needed.
7. **Q13:** there is no platform record. The front matter still says `draft`; after this review it should become `checked`, platform pending. The origin WARN is a truthful "claude"; the export tool's user-only restriction is an authorship matter outside this review.
8. **Set:** q01–q04 are dropped, so there is no live sibling overlap.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q05.md
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r2-v2-fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r2-v2-fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D10.txt, D12.txt (D08, D09, D11 for the replacement tests)
- D:\Dev\Docket\AQ-00998_2026-10-06_0256.md (overview and platform text)
