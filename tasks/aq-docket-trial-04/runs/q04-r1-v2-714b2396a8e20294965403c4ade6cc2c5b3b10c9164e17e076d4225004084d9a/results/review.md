# q04 rev 1, independent review (raw return, verbatim)

- Recorded: 2026-10-06. Fresh question-review agent (Claude Code, claude-opus-5-5).
- tested_sha256: 714b2396a8e20294965403c4ade6cc2c5b3b10c9164e17e076d4225004084d9a

q04 (rev 1; tested_sha256: 714b2396a8e20294965403c4ade6cc2c5b3b10c9164e17e076d4225004084d9a)

**gold_verified: yes.** Peru (+26%) holds on every figure route. I recomputed it with Decimal:
- Thousands: (107,635 − 85,535) / 85,535 = +25.837377%.
- Millions (Doc 6 A-3 107.6 / Doc 3 A-1 85.5): +25.847953%.
- Mixed: 107.635 / 85.5 gives +25.888889%; 107.6 / 85.535 gives +25.796458%.
- Every route rounds to +26 under both half-up and half-even. One decimal would split 25.8 / 25.9, so the whole-percent precision is correct.

The per-country ARP inference is supported; the documents do connect the figures:
- **Scope notes:** D05 note a excludes P.L. 117-2 (L1085-1087). D05's COVID box (L211) says the money is "not included in the country or regional totals". D06 note a includes it (L487).
- **Totals reconcile:** D05's rows add up exactly to its 1,794,345 total. D06's rows add up to 1,891,495, plus the 5,000 OAS contribution gives its 1,896,495 total.
- **Row differences:** 18 rows differ, none negative, and they sum to 97,150 (= "$97.2 million").
- **D08 marks:** the differing rows are exactly the rows D08 A-1 marks "a".
- **Accounts:** only ESF differs (378.5 + 97.2 + 5.0 = 480.7); every other account is identical.

No row differs for any other reason.

The Peru–Colombia margin holds on every route: 13,350 vs 13,100 in thousands; 13.385 vs 13.092 using D05 A-1's 465.1 for Colombia; 13.4 vs 13.1 rounded.

**outcome:** A: match; B: match. Both were fresh packets, answered Peru, +26% (25.84%), did the same reconciliation and rejected the same alternatives (Colombia −5%, base with ARP +9%, Haiti +54% out of region, share reading).

**closed-book:** misses. It answered "Colombia, about −11%", low confidence.

**necessity:**
- **D05** is the only ARP-free FY2021 source (85,535). Without it there is no per-country ARP figure. The no-D05 probe answered Colombia −4% (p 0.15). A +26% base would have to fall between 85,087 and 85,765, and no remaining Peru figure does.
- **D06** is the only FY2024 country request (107,635 / 107.6). The stand-ins give +28% (D05 FY2023 request 109,870; FY2022 109,134 / 109,159), +17% (FY2023 estimate) and +11% (FY2025 request). The +26% window is 107,346-108,202 and no printed figure falls in it.
- **D08** can replace only D06's FY2021 column. D01-D04 and D07 contain no Peru or FY2021 country data. There is no smaller valid set than D05 + D06.

**shortcut: clear.** The shortest route is D06 Table 2 plus its notes, then D05 Table 2 plus note a, then 12 differences, the maximum, and the percentage change. "American Rescue Plan" appears only in D05's COVID box and in the notes of D06 (two) and D08 (one), so search finds inputs, not the answer. The bundle overview for Docs 3, 6 and 8 never mentions ARP, Peru or 26% (capture L51-109).

**source_assessment:** The report shows `source_gaps: []`, and the capture says "8 of 8 captured in full". The only unrendered content is the Figure 1 maps and Figure 2 charts in D05, D06 and D08 (regional, all-agency obligations, FY1946-FY2019/2021/2022, inflation-adjusted). They cannot hold country FY2021 State/USAID figures, ARP splits or an FY2024 request. They therefore do not affect the premises, the gold, the Haiti exclusion (which rests on ordinary geography), uniqueness, necessity or shortcut coverage.

**Uniqueness:**
- **Universe:** 12 South American rows, all in D06; Peru 13,350 is the largest. Haiti (14,800) is Caribbean. Panama (2,250) and Trinidad and Tobago (125) cannot reach Peru even if counted.
- **Bolivia:** it has no D05 row, so its ARP is at most 4,000.
- **"Most" as a share:** this points to Bolivia, where the change is undefined (0 to 0). The next shares are Uruguay (0%) and Paraguay (+2%), but "most money" ordinarily means an amount, so this is not a defensible second answer.
- **Base and request:** the base is 85,535 on every route, and Peru's FY2024 request appears nowhere else in the bundle. D08 has FY2024 enacted figures only for CBSI, Colombia and Venezuela.

**difficulty: easy** (local suitability against the Medium target). My rough split: Too easy ~20%, Easy ~60%, Medium or higher ~17%, Too hard ~3%.
- **In favour:** the deciding per-country amount is printed nowhere. The winner leads the salient prior (Colombia) by 1.9%, and any heuristic or column misread of D05's one-value-per-line rows picks Colombia. It takes three dependent steps.
- **Against:** the question names the scope fact it depends on ("American Rescue Plan Act money"), like trial-02 q04's pin. The low model has derived carve-outs from original vs restated rows on its own. The +9% same-row decoy is defused by "without that money", and the printed +7.2% carries a different label.
- **Caveat:** local reviews have underestimated untied traps before (aq-00964 q01, aq-00745 q09).

**verdict: revise**

**findings:**
1. **Form number check (Q14, Reasoning).** Several steps break the recorded rule of one "=" per step:
   - Step 4 holds four "=" results. Neither cited document prints 5,200 or 500, and the form has flagged second results in multi-sum steps before (aq-00949 q03).
   - Step 6 has two "=" results; "26%" is printed nowhere.
   - Step 7's "only a 9% increase" is the unprinted-restatement pattern ("or 10.1%"), and 0.955 is a second result.

   Fix: one simple a-op-b per numbered step. For example "Doc 3 and Doc 6: 107,635 - 85,535 = 22,100.", then "Doc 3: 22,100 / 85,535 = +26% (to the nearest whole percent)." Give each decoy its own step with the value after "=".
2. **Verbatim evidence (block; platform-only, unknown).** These quotes span many lines in the platform text too:
   - D05's header and its Peru, Colombia and Brazil rows (one value per line; capture L1246).
   - D06's header: "FY2021 (actual)a" never occurs contiguously, and neither do the reasoning's quoted labels "FY2021 (actual)a" and "FY2024 (request)".
   - D06's pipe rows.

   q03 avoided quotes like these. Fix:
   - Add D05 L211's single-line sentence "These supplemental funds are not included in the country or regional totals found in Table 1, Table 2, or the Appendix of this report."
   - Replace the header quotes with single-line titles (D06 L329 "FY2021 Actual-FY2024 Request"; D05 L545 "FY2019-FY2023 Request").
   - Have the user Save passage for the D05 and D06 Peru rows and read the form's check before preparing.
3. **Difficulty below target.** I found no fair wording that lifts it. Quick-test before spending the difficulty check, and ask the user whether Easy is acceptable for this bundle.
4. **Optional PIN3 fix.** Write "the largest dollar amount of American Rescue Plan Act money". The Coach has flagged "largest" before even when both readings agreed.
5. **Optional reconciliation step.** Add one step to the reasoning, e.g. "Doc 3 and Doc 6: 1,896,495 - 1,794,345 = 102,150", noting that this is the $97.2 million plus the $5 million OAS. It shows the platform reviewer that the inference is exact.
6. **Lever-checks record error** (not part of the fingerprint). "FY2023 request -2%, FY2022 -1%" measures the stand-ins against 107,635. The answers they actually produce are +28%, +28%, +17% and +11%.
7. **Probe hygiene.** The rev 1 no-D05 probe noticed "The manifest has no D05". Use neutral, renumbered ids next time. It is design evidence only; the result was still a miss.
8. **Set.**
   - q03 uses a different dependency (footnoted remainder, D05 + D08); there are no mutual giveaways.
   - q01 has the same name-plus-percentage shape.
   - q02's answer includes Peru and uses the same 107,635; don't submit q02 alongside q04.
   - "State Department- and USAID-managed aid" and "Biden Administration's fiscal year … request" recur across all four questions, a possible Sibling-question advisory.
9. **Records.**
   - The report shows the current rev 1 records (A match, B match, closed-book miss) bound to 714b2396…; the q04.md shortcut audit for rev 1 is also bound to it with "verdict: clear".
   - Rev 0 records (889117de…) are stale.
   - Floor: 0 FAIL and 2 WARN (origin; "if any" format), both explained adequately.
   - The fingerprint covers question, answer, components, reasoning and evidence, so findings 1, 2, 4 and 5 make a rev 2 that needs a new prepare and fresh A/B solves, closed-book solve and audit. Fold all of them into that one revision.

The platform tier and any form behaviour for multi-line quotes are still unmeasured.

Files:
- D:\Dev\Docket\tasks\aq-docket-trial-04\questions\q04.md
- D:\Dev\Docket\tasks\aq-docket-trial-04\runs\q04-r1-v2-714b2396a8e20294965403c4ade6cc2c5b3b10c9164e17e076d4225004084d9a\results\
- D:\Dev\Docket\tasks\aq-docket-trial-04\text\D05.txt, D06.txt, D08.txt
