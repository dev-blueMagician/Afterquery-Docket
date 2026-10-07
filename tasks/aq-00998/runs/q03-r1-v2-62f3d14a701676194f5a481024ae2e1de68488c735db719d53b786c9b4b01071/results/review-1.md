# q03 rev 1 independent review (question-review, fresh context), completed 2026-10-05

Dispatched with the frozen fields, corpus, fingerprint, target and raw returns only. Pasted unabridged.

q03 (rev 1; tested_sha256: 62f3d14a701676194f5a481024ae2e1de68488c735db719d53b786c9b4b01071)

gold_verified: yes. I recomputed it with my own script, reading the source lines directly:
- **Quarter:** D06 l.99 says "Discovered oil at the non-operated Far South prospect in the deepwater Gulf of America in April 2025". April is month 4, so the quarter is calendar Q2 2025. Chevron's quarters follow the calendar (D08: "Three Months Ended June 30").
- **Rates:** D08's title (l.17) says "Second Quarter 2025". Its l.85 gives growth of 22 percent for the Gulf of America and 14 percent for the Permian Basin. 22 − 14 = 8 percentage points.
- **Precision:** each input is stated once, and no other passage gives Q2 2025 regional rates. No regional volumes exist anywhere, so nothing finer can be recomputed. Choosing between figures cannot split the answer.
- **Alternatives:** D06's own Q1 rates give −5; the reversed order gives −8; mixing editions gives 10 or −7; pairing TCO gives 12 or 13. "In percentage points" excludes the relative reading (about 57%).
- **Readings of "when":** reading it as the announcement date (D06 was released May 2, 2025) also gives Q2. Only the reading "quarter the reporting release covers" differs, and the explicit "April 2025" refutes it.
- **Source check:** the deciding lines are identical in the docs/ originals and in the platform capture (l.3111, l.3751).

outcome: A: match; B: match. Both come from fresh packets holding only question.txt plus the corpus (I checked), both are rev 1 on the same fingerprint, and both answer 8 from D06 l.99 and D08 l.85. Both reject −5 because of the April date. B calls −5 "weaker", but its argument shows the text contradicts it, so it is not a defensible alternative. Neither is contaminated.

closed-book: misses. It answered "+4 pp (estimate, assumed Q1 2025)" at low confidence. That is not equivalent to 8 and not near it, and it did not know the rates. It did half-recall the timing of the discovery ("early 2025 … could have been Q2"), and the sketch-stage screen placed Far South "around April 2025".

necessity:
- **D06 is the only dated mention of Far South.** Without it, D10 l.117 names "the non-operated Far South well" among its 2025 full-year highlights without a date, and no other document mentions it. That D08 and D09 say nothing about it points away from Q2, not towards it. The overview lists "April 2025" for Doc 6 but not the event. The quarter cannot be settled.
- **D08 is the only source of the Q2 2025 rates.** D06 l.79 covers Q1. D09 l.84/l.130, D10 l.87, D11 l.85 and D12 l.85/l.135 give totals or barrels-per-day figures and no regional rates. No release gives quarterly Gulf or Permian volumes, and D03 has no Q2 2024 Permian volume to set against the "1 million BOE per day".
- **No smaller set, and no alternative pair:** D10 + D08 lacks the quarter; D06 + D12 lacks the rates.
- **Caveat:** without D06, D08 holds the only pair of regional rates in the bundle, so "use the only computable pair" happens to land on 8. Combined with the partly recallable bridge, this is a risk for the platform's document check, not a demonstrated substitution.

shortcut: clear. The shortest route I verified: search "Far South" → D06 l.99 (April 2025, so Q2) → D08 l.17 and l.85 → 22 − 14 = 8.
- No passage states the answer; "percentage point(s)" appears nowhere in the bundle.
- The overview names neither Far South nor any regional rate.
- My searches covered Far South, discover and prospect; Gulf of America or Mexico and Permian; every "(N percent)"; and every barrels-per-day line. That matches the auditor's coverage.
- The auditor was not contaminated. Its first search returned only question.txt. A search of the whole run folder would also have hit snapshot.json, so the search stayed inside shortcut/, which holds only the question and the corpus.

source_assessment: no known gaps.
- source_gaps is empty, and its hash matches sha256("[]") (4f53cda1…b945).
- The capture says "12 of 12 captured in full" and contains no "characters not shown" markers. The manifest method is "text" for all files.
- The local docs total 370,920 characters against the page's 349,777. That gap fits the pipe-table rendering recorded in memory. q03's three quotes are prose lines, not pipe rows, so the verbatim risk does not apply.
- No effect on premises, gold, exclusions, uniqueness, necessity or shortcut coverage. This does not prove completeness beyond the known-omission markers.

difficulty: easy. This is local suitability only, it is marginal, and the too-easy risk is high. The path is one plain date sentence, a month-to-quarter step, one prose sentence holding both inputs, and one subtraction.
- **In its favour:** the release that holds the bridge also prints same-label figures for the wrong quarter (D06 l.79, 20 lines above the Far South bullet), which gives a coherent −5. That is the element that beat the low model 5/5 in aq-00964 q01, and that question's local profile was the same as this one (two Opus matches, clear audit, "easy (marginal)"). Rev 1's neutral "minus" removed the rev 0 assumption that the Gulf grew faster.
- **Against it:** this trap is cheaper to escape than aq-00964's. The bullet prints "April 2025" and the question says "calendar quarter", so rejecting D06's figures needs only month-to-quarter knowledge. In aq-00964 the decoy was dated after the event and looked current. The rest of the path matches the recorded too-easy patterns:
  - aq-00949 q02: a one-sentence date bridge leading to one passage.
  - trial-02 q01: labelled figures plus one standard calculation.
  - trial-07 q01: a bridge models can recall.

  A low model that recalls April 2025 never sees the decoy.
- **Likeliest wrong routes for a quick reader, most likely first:**
  1. −5: take the release where "Far South" is found (D06) and use its own Q1 growth sentence.
  2. −8: subtract in reverse. D06 lists the Permian before the Gulf; D08 lists the Gulf first.
  3. 10 or −7: mix D08's Gulf rate with D06's Permian rate, or the reverse.
  4. Pick an arbitrary 2025 quarter from D10's undated bullet. Only −5 and +8 are computable.

  How often the low model takes route 1 is essentially the whole difficulty margin.

verdict: ready. This is local readiness only; status stays `checked` until a platform pass on this exact fingerprint.

findings:
1. **Q4/Q9:** the gold is verified (above). No action.
2. **Q8:** the rev 1 fix is verified. The wording no longer assumes the Gulf grew faster, and −5 is now a coherent wrong answer.
3. **Q2:** see the necessity caveat above. It needs the platform's document check or quick test on this fingerprint.
4. **Q3 and lever:** the Lever checks line saying q03 "mirrors aq-00964 q01" overstates the match. Here the decoy predates the event and the bridge bullet prints the month. Record that difference at hand-over.
5. **Precision WARN:** the explanation is adequate. Each input is stated once, the result is an integer and no competing figure exists, so there is no "answered inconsistently" exposure. The form may still show an advisory rounding prompt.
6. **Q14, cosmetic:** Reasoning Step 2 quotes "company's" with a straight apostrophe, while D08 prints a curly one. The Evidence field is unaffected because its D08 quote starts at "in the Gulf of America", so the blocking verbatim check is untouched. Changing the reasoning changes the fingerprint, so only fix this inside some future revision.
7. **Q14, optional:** no quote ties D08's quarter to April–June (Attachment 1, "Three Months Ended June 30"). Not needed, given "calendar quarter" and the D08 title.
8. **Records:**
   - The rev 1 records for A, B, the closed-book solve and the audit all carry 62f3…1071, and the report recomputes the current file as 62f3…1071.
   - question.txt is identical in all four packets and matches the snapshot.
   - The report lists only records from the blind-solve section by design; the audit record is under "## Shortcut audit".
   - The latest platform record is null, so Q13 is unknown and no tier has been observed.
9. **Floor:** 0 FAIL and 2 WARN. The origin warning is accurate and its export restriction is outside this review; the precision warning is covered by finding 5.
10. **Set:**
    - All four questions follow one pattern: a quarter defined by an event, then figures from another release, then one subtraction or lookup. They use the same tag pair and run 32–38 words, which may trigger the "Question length spread" advisory. q03 and q04 open almost identically.
    - No question gives another away. q03 alone touches 2Q 2025 or the Gulf and Permian rates.
    - q03 is the only one whose bridge is reported in the previous quarter's release, next to a wrong-quarter decoy, which makes it the set's strongest trap.
    - For variety, the bundle has a revised target series not yet used: "$2-3 billion by the end of 2026" in D04–D06, "$3-4 billion" in D10 and D12, with $3 billion reported achieved in D12.

Files:
- D:\Dev\Docket\tasks\aq-00998\questions\q03.md
- D:\Dev\Docket\tasks\aq-00998\runs\q03-r1-v2-62f3d14a701676194f5a481024ae2e1de68488c735db719d53b786c9b4b01071\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q03-r1-v2-62f3d14a701676194f5a481024ae2e1de68488c735db719d53b786c9b4b01071\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D06.txt, D08.txt, D10.txt
