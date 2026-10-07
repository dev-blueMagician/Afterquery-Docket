# q01 rev 0, independent question-review (raw return, 2026-10-06)

Fresh question-review agent (Claude Code, claude-opus-5-5), given the frozen snapshot, corpus,
raw A/B/audit/closed-book returns, removal-probe returns and floor output; no writer conversation.
784 s, 63 tool uses. Return copied verbatim.

---

q01 (rev 0; tested_sha256: 3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd)

**gold_verified: yes.** The gold is -34 TWh, and it is the one defensible answer.
- **The three inputs** (I checked the windows myself):
  - D06 L1076 gives -182 TWh. The coal sentence prints no years, but its own paragraph sets the window as 2019 to 2024 ("lower in 2024 than it was in 2019"). L1078 ("from 17% in 2019 to 29% in 2024") and L1068 (gas "fifth year in a row") agree.
  - D07 L1036 gives -162 TWh "since 2021", and L1034 sets that window as "between 2021 and 2025". The -162 is coal's own part: 162/257 = 63%, matching "almost two-thirds". Gas is -81 TWh ("almost a third").
  - D07 L1020 gives -14 TWh for 2025.
- **Result:** my own script gives -182 - (-162 + 14) = -34. Moving each input by ±0.5 gives -35.5 to -32.5.
- **Rebuilding levels** from the printed TWh changes always gives -34, whatever the level (I tried 2019 at 448, 455 and 462).
- **Mixed routes don't hold up.** Setting D07's 9.2% coal share × (367/13.1%) against D06's "-40%" level gives -35.3. Using the 5% to set the 2024 level gives -27, ranging +4 to -53 over the rounding band. Both contradict the printed -182, so neither is a careful reading.
- **Rejected readings:** forgetting the 2025 step gives -20. Treating -162 as the fossil total gives -88; L1034's -257 rules that out. Starting D06's window in 2020 would put 2021 34 TWh below 2020, which contradicts D05 L229 ("strongly rebounded"). A UK-inclusive EU-28 reading has no data anywhere in the bundle, and D07 L271 says "EU-27".
- **Mixing editions:** D07 did revise the EU's 2024 demand growth (D06 L1070 says +1.1%; D07 L1010 says 1.9%). But D06's -40% and -16% put 2024 coal at about 266-276 TWh, and D07's shares put it at about 269-274. The gas check also matches: I compute 2025 at -18.1% against 2019, and D07 L1022 says "18% below". No document prints a competing figure.
- All six evidence quotes appear word for word in the source files.

**outcome: A: match; B: match.** Both answered -34 TWh by the same window steps from D06 and D07, with medium-high confidence. Both rejected the -20, -88 and 2020-start readings. Neither was contaminated (runtime git-status names only). They are separate solvers (A and B) on the current fingerprint.

**closed-book: misses.** The answer was about -30 TWh (low confidence, ±10). That is 4 TWh from the gold, and the platform graded strictly before (10.871 vs 10.869 counted as different), so it is not equivalent. The sketch-stage run gave about -27. My estimate of an exact -34 from the platform's low model is about 5%.

**necessity:**
- **D06 (Doc 3)** is the only source tying EU coal to 2019 in TWh.
  - Without it, approximations from the remaining documents miss -34. D04's EU -20% (2020) plus D05's other-country proxies gives -33 (US +16%), -32 (US 7% below 2019), -18 (Germany) or -3. Probe k3 forced a guess of -31 (p 0.04).
  - Residual risk: memory of a 2019 level near 450-458, set against D07's share-derived 2021 level of about 420, puts -34 inside the guess band. I estimate about 10% per platform document-check attempt.
- **D07 (Doc 4)** is the only source tying EU coal to 2021 in TWh.
  - Without it, 2021 is only bounded between 364 and 455, so the change lies between -91 and 0. Probe t8 forced -50 (p 0.05).
  - One coincidence lands exactly on -34: D06's 2024 fall of 50 TWh, plus D02's first-half-2023 fall of 49 TWh doubled, plus an assumption that 2022 equalled 2021 (50 + 98 = 148). It needs two unsupported assumptions, so the risk is low.
- No smaller set of documents works, and no substitute set exists.

**shortcut: clear.** The shortest route I verified is D06 L1076 (window dated in the same paragraph), then D07 L1034/L1036, then D07 L1020.
- I searched every line where EU, European Union, EU-27 or Europe appears with coal, in all eight documents. I also checked every coal line that mentions 2019-2023 or "since / five years / four years".
- No passage prints the 2019-2021 change, a 2019 or 2021 EU coal level, or a 2022 level.
- The capture's overview entries for Doc 3 and Doc 4 list no EU coal figure. Chart content is missing for every reader (see below).

**source_assessment:**
- **Recorded gaps:** none (source_gaps is empty, hash 4f53cda1…). The capture read all 8 documents in full, with no gap characters, and every file matches it.
- **Chart placeholders:** "Loading data..." appears 57 times in D06 and 46 in D07. The capture shows the same 103, including the EU-section charts (D06 L1072, L1082, L1090, L1098; D07 L1026, L1044, L1056, L1064).
  - Premises and gold: no effect, because every input is in the prose.
  - Exclusions: not applicable.
  - Uniqueness: a visible chart could have added a second, differently rounded EU coal series. It is not visible to any platform reader.
  - Necessity and shortcut: a visible EU generation chart could have given the 2019 and 2021 levels from one review alone. It is not visible on the platform, so that route does not exist.
- **Uncaptured methodology pages** (D06 L188; D07 L237, L426) and link targets are not cited or needed. The EU-27 scope is already stated at D07 L271.
- The warning that chart contents are unavailable stands.

**difficulty: easy.** This is below the medium target; it is a local suitability judgement, not a measured tier.
- **Odds on the platform ladder:**

| Tier | Estimate |
| --- | --- |
| Too easy | about 35% |
| Easy | about 47% |
| Medium | about 12% |
| High | about 4% |
| Too hard | about 2% |

- **Why it reads as Easy:**
  - The inputs are three plainly printed TWh figures in the two EU sections.
  - The traps are real but don't hold up under careful arithmetic:
    - forgetting that the 2021 window ends in 2025 (-20);
    - the "(-162 TWh)" placed after "fossil power decline" (-88);
    - the 2019 start printed only in the neighbouring gas clause.
  - There is no same-document decoy that "looks current", which is the mechanism measured at Medium in aq-00964 q01 and above it in aq-00745 q09.
  - Building a period that no document reports matches the aq-00998 q05 Easy result.
  - Window arithmetic resembles the year-to-date transformation measured Too easy in trial-02 q01.
- **Medium needs Low 0/5,** meaning every low attempt falls for -20 or -88. How the platform scores Low 0/5 followed by Medium 4-5/5 is unmeasured.
- **No fair rewording found:**
  - The question already avoids mentioning 2024, 2025, editions or windows.
  - Adding decimal places would split the answer, since all inputs are whole TWh.
  - A percentage ask is guessable without the documents (about -6 to -8%) and splits on the -40% base.
  - Naming the windows would give away the trap.
  - Other periods either lose a necessary document (2019 to 2023 is D06 alone) or ask about a widely reported 2023 fall.
  - An EU gas version (its 2025 step has the opposite sign) is a different question, not clearly stronger, and has a competing route via the "-15%" four-year figure.

**verdict: ready.** It is ready locally but below the Medium target; status stays checked until the platform measures it.

**findings:**
1. **Gold and scope (Q4/Q9):** -34 verified independently. The mix of 2025- and 2026-edition data is supported by the consistency checks above; no action needed.
2. **Necessity (Q2):** holds. The residual memory risk (about 10% per attempt without D06) and the D02 doubling coincidence without D07 are low and not demonstrated. As optional extra evidence, run one more forced-guess probe per document.
3. **Form reasoning check (Q14):** in Step 4, the operand "148" is printed in neither Doc 3 nor Doc 4 (I found zero standalone hits). It was derived in Step 3 as "-148". In aq-00949 q05 and aq-01320 q01, derived operands in steps citing their source documents raised no number flag, so the risk is low; the only open point is the dropped sign. Check the form's reasoning panel after pasting. If it flags the number, make the operand match the earlier derived value exactly.
4. **Records:** the lever-check line still says "Removal probes pending". Probes k3 (-31) and t8 (-50) have returned on this fingerprint. Lever checks are outside the fingerprint (check_questions.submission_sha256), so recording them changes nothing that was tested. Also, k3's docs/ file names showed which edition was missing, a minor leak; the probe still could not answer.
5. **Platform-only checks:** unknown. The capture shows "Quick tests used: 0 of 10". For a medium target, run a quick test before the difficulty check. Expect possible false-positive "Answer matches a stated figure" warnings on the printed coal TWh figures. The origin warning (export accepts user only) is the user's decision.
6. **Set:** this is the first question on the bundle. Keep any sibling off the same overlapping-window path (EU gas or fossil windows), since it would repeat the answer path.

Files:
- D:\Dev\Docket\tasks\aq-01430\questions\q01.md
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\snapshot.json
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-v2-3c4106b71dd45b00932614e7a49573a3dde8d87b2888f480debf4e5220d7fdfd\results\ (blind-solver-A.md, blind-solver-B.md, shortcut-audit.md, closed-book.md)
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-probe-k3\probe-return.md
- D:\Dev\Docket\tasks\aq-01430\runs\q01-r0-probe-t8\probe-return.md
- D:\Dev\Docket\tasks\aq-01430\text\D06.txt (L1068-L1078)
- D:\Dev\Docket\tasks\aq-01430\text\D07.txt (L1010-L1038)
