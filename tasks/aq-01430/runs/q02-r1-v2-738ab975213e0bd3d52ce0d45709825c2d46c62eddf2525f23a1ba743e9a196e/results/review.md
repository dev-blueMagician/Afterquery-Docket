# q02 rev 1, independent question-review (raw return, 2026-10-06)

Fresh question-review agent (Claude Code, claude-opus-5-5), given the frozen snapshot, corpus,
raw rev 1 A/B/audit/closed-book returns, rev 0 history, removal-probe returns and floor output;
no writer conversation. 688 s, 60 tool uses. Return copied verbatim.

---

q02 (rev 1; tested_sha256: 738ab975213e0bd3d52ce0d45709825c2d46c62eddf2525f23a1ba743e9a196e)

**gold_verified: yes.** I recomputed the gold with Decimal arithmetic. The first-half figures come from D03 L277: coal −56, gas −2.7 and other fossil −0.1, which sum to −58.8. D03 L49 sets the period and no document prints a China first-half fossil total. The full-year figure is −56 (D07 L900, repeated at L139 and L225). So July–December = −56 − (−58.8) = **+2.8 TWh**.
- **Checks:** by fuel, −15 + 16.7 + 1.1 = +2.8. By quarter, using D08's January–September −52, Q3 is +6.8 and Q4 is −4.0. That sums to +2.8, but it is the same identity, not independent evidence.
- **Precision:** no input has a second stated figure, and no step rounds an intermediate value. The rounding band is +1.70 to +3.90, positive throughout.
- **Item 2, the readings:** none of them is defensible.
  - 0.0 uses the first-half coal figure as fossil. L277 says "Coal generation".
  - +2.7 leaves out the other fossil fuels. The question asks for fossil fuels, and D03 L152 builds its fossil total from coal, gas and other fossil.
  - +1.7 uses coal and gas only for both periods. D07 prints the fossil total directly.
  - +0.8 takes the full year as demand minus clean growth (503 − 561). That is a proxy, and D07 prints −56.
  - −4 is October–December, which is the wrong period.

**outcome: A match; B match.** Both answered "rose by 2.8 TWh", which is equivalent to +2.8. They used separate fresh packets (solver-1 and solver-2), and their D03 and D07 text files are hash-identical to the corpus. Neither saw anything beyond the runtime git-status listing, so neither is contaminated.

**closed-book: misses.** The two rev 1 runs answered about +8 and about +55, both at low confidence. Both recalled Ember's first-half "−58.7" but not the April 2026 full-year −56.
- **Item 4:** rev 0 reached "+3" only at whole-TWh precision. At one decimal, a "flat" or "+3.0" guess misses. I put the platform low-model risk at about 2–4%: it would need both the April 2026 figure and the exact −58.8.

**necessity:**
- **D07 (Doc 4):** the only full-year China fossil change. Without it, D03 plus D08 give Q3 = +6.8 but no Q4 and no full year. D08's forecast is global and in words only, D01 gives only China's gas level (334 TWh), and D06 covers 2024. The n2 probe's forced estimate (+7, via +6.8) misses at one decimal. The remaining risk is a model recalling the April 2026 −56 headline. Three local closed-book runs did not recall it; I put this risk at about 10%.
- **D03 (Doc 6):** the only China first-half fuel changes. Without it, D07 plus D08 give only Q4 = −4. The v6 probe forced −15 (p 0.02). The recalled −58.7 gives +2.7, which is a different answer at one decimal. At whole TWh it would give +3, the gold.
- **Item 3:** D08 is not needed. No smaller valid set exists, and D03 + D07 is the only minimal pair.

**shortcut: clear.** The shortest route is D07 L900 (or L139/L225) plus D03 L277, then a three-term sum and one subtraction. That matches the gold. No passage, overview entry or chart text states a China first-half total, July–December, Q3 or Q4 fossil figure. The overview lists only global figures for Docs 4 and 6 and China's gas level for Doc 8. Searching finds the inputs, not the answer. The auditor's band of "+2.3 to +3.3" understates the true +1.7 to +3.9, but that does not change its verdict.

**source_assessment:** prepare/report list no source gaps (source_gaps [], hash 4f53cda1…). The capture shows "8 of 8 read in full", with matches_capture true and gap_characters 0 for every document. The "Loading data..." chart placeholders are not capture gaps: they appear in the originals and on the captured platform page (103 in the capture, 46 in D07 including L902/914/924/934 in its China section, none in D03).
- **Premises:** the question asserts no chart fact.
- **Gold:** both inputs are prose sentences.
- **Exclusions:** none are claimed.
- **Uniqueness:** no chart text can show any solver a competing figure.
- **Necessity:** the platform's document check sees the same placeholders, so no chart can replace D03 or D07.
- **Shortcut:** there is no chart text to search.

**difficulty: easy.** This is below the medium target.
- The mechanism is a standard partial-period step (full year minus first half) on labelled prose. That is the same profile as trial-02 q01 (Too easy) and aq-01322 q03 (Low 4/5).
- The only close reading is a same-paragraph sum of three figures. Both decoys are excluded by the sentence's own words: coal −56 next to fossil −56 (0.0, helped along by D07 L239's "flat"), and leaving out the 0.1 (+2.7).
- No same-document decoy that "looks current" exists. One decimal does make the omission count.
- **Tier odds:** Too easy ~50%, Easy ~40%, Medium ~7%, High ~2%, Too hard ~1%.

**verdict: ready.** This is local fairness only. Difficulty is easy, so the gate's target-suitable-difficulty condition for medium is not met. Q13 is pending.

**findings:**
1. **Precision (item 1), Answer field and D07 L900/D03 L277.** Every route through the printed figures gives exactly +2.8, and none of the platform's "answered inconsistently" mechanisms is present. The +1.7 to +3.9 band is measurement uncertainty, not a stated alternative answer. I would not change the precision or the wording. Whole TWh would bring back the measured closed-book reach (+3) and would let the recalled −58.7 replace D03 (+2.7 rounds to +3). Adding a method phrase would hint at the path. A reviewer objecting to false precision is a low risk. To verify, check the platform's "One defensible answer" result.
2. **Form number rule (item 5), Steps 3–4.** The derived operands −58.7 (citing Doc 6) and 58.8 (citing Docs 4 and 6) match patterns that passed before (aq-00949 q05 Step 3, aq-01320 q01, aq-01321 q02 steps 7–8). The one flagged pattern was a result labelled with a period that the cited document states as a rounded figure. That pattern is absent here. This is a platform-only check: look at the form panel after pasting.
3. **Advisory "Answer matches a stated figure".** It may falsely flag "Doc 4 states 56 TWh", as happened on aq-01320 q01. This is advisory only; do not add method wording to clear it.
4. **Lever-checks record (outside the fingerprint).** The "+2 (coal and gas only on both sides)" entry is from rev 0. At one decimal that route gives +1.7, and the first-half-only omission gives +2.7. Update the record.
5. **Mixing data releases.** D06's 2024 coal figure of 5,864 against D07's implied 5,828 shows Ember revised its data between editions. But no revised first-half figure exists anywhere in the bundle, so +2.8 is the only value that can be computed. This is a low residual risk.
6. **Set (item 6).** q01 (EU coal 2019→2021) and q02 share the same family of subtracting overlapping windows, the same tags and levers, and Doc 4. Neither gives the other away. Token overlap with q01 is 0.31 with a longest shared run of 3 tokens. Across all 75 workspace questions the maximum is 0.31, and the longest run anywhere is 4 tokens (aq-01333 q01). The planned quick-test batch (h3, a04) uses the same family too, so there is little variety in mechanisms, and one Too-easy result predicts the others.
7. **Q1–Q12 and Q14** pass locally. Restricted names, Original question and Not a duplicate can only be checked on the platform and remain unknown. The origin WARN (claude; export accepts user only) is explained.
8. **Records.** The current fingerprint (738ab975…) matches the snapshot. The rev 1 A/B, closed-book and audit records are all bound to it. The removal probes ran on rev 0 with the same inputs, so their conclusions still hold at one decimal.

Files:
- D:\Dev\Docket\tasks\aq-01430\questions\q02.md
- D:\Dev\Docket\tasks\aq-01430\runs\q02-r1-v2-738ab975213e0bd3d52ce0d45709825c2d46c62eddf2525f23a1ba743e9a196e\results\
- D:\Dev\Docket\tasks\aq-01430\runs\q02-r0-probe-v6\probe-return.md
- D:\Dev\Docket\tasks\aq-01430\runs\q02-r0-probe-n2\probe-return.md
- D:\Dev\Docket\AQ-01430_2026-10-06_1949.txt
