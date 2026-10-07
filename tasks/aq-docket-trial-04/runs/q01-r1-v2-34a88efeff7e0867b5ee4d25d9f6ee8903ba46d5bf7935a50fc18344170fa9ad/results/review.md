# q01 rev 1, independent review (raw return, verbatim)

- Recorded: 2026-10-06. Fresh question-review agent (Claude Code, claude-opus-5-5), given the
  frozen snapshot, corpus, raw returns and floor output; no writer conversation.
- tested_sha256: 34a88efeff7e0867b5ee4d25d9f6ee8903ba46d5bf7935a50fc18344170fa9ad

q01 (rev 1; tested_sha256: 34a88efeff7e0867b5ee4d25d9f6ee8903ba46d5bf7935a50fc18344170fa9ad)

**gold_verified:** yes. I parsed D05 Table 2 (25 countries; the FY2023 column sums exactly to the stated 2,407,408) and D08 Table A-1 straight from the text files. Honduras goes from 133,450 to 86,300, a 35.33% decline. The millions route (133.5 to 86.3) gives 35.36%, and both mixed combinations also round to 35. The next countries are El Salvador (29.73%), Guatemala (28.87%) and Mexico (22.51%). Every country is unchanged or higher from Venezuela (2.27%) on.

**outcome:** A: match; B: match. Both answered Honduras at about 35% (35.3%), which is equivalent to the gold. Both rejected D08's percentage column, which uses the FY2023 estimate as its base, and both excluded regional programs. The packets held only the question and the documents, and each solver's file list stays inside its own packet.

**closed-book:** misses. It answered "Mexico, about 32%" at low confidence, which is the wrong country and the wrong value. The earlier sketch probe also missed ("El Salvador, about 40%").

**necessity:**
- **D05 (Doc 3)** is the only source of FY2023 requests by country (Table 2, and Table A-3 in millions). Without it, D06 and D08 offer only the FY2023 estimate (Honduras 141,774). That route gives Costa Rica at 95% or "cannot determine".
- **D08 (Doc 8)** is the only source of FY2025 requests (Table A-1, Table A-3, and the prose "$86.3 million for Honduras"). D06 is dated August 2024 and prints no FY2025 figures. Without D08, the latest request is FY2024: Honduras rises 2.25% and Mexico leads at 21.31%.
- No smaller source set works.

**shortcut:** clear. The shortest route I verified is D05 Table 2 column 5 plus D08 Table A-1 column 4, a ratio over the 25 countries both tables share, with the 7 program rows excluded. No passage, comparative table or overview summary states the answer. D01-D04 and D07 hold no country request figures.

**source_assessment:** There are no gaps (source_gaps [], hash 4f53cda1…). Intake shows all 8 documents captured in full with 0 gap characters. Each text file matches its original after the two-line header. The one exception is a "..." vs "…" normalization at D04 text line 747, inside a quoted FAA title III provision; D04 has no Latin American country request data, so this affects none of the six dimensions.

**difficulty:** medium (marginal). This is local suitability only, not an observed tier.
- **For Medium:** the question has the shape of the one measured Medium pass. D08's own "% Change: FY2023-FY2025" column carries the asked years and gives Costa Rica 95% (Honduras 39%); only the "(est. actual)" header rules it out. Other miss routes:
  - prose-only countries give Mexico 23%
  - including USAID Central America Regional gives 59%
  - a FY2024-request base gives Honduras 37%
  - parsing D05's one-value-per-line rows across 25 countries invites misreads
- **Against:** the question says "request" twice, which directly contradicts the decoy's label. Label-ruled decoys were rated weak in earlier local reviews, and the measured Medium decoy was ruled out by timing. Once the decoy is escaped, the path is two labelled lookups and a division. D08's prose also singles out Honduras's decrease.
- **Main risk:** Easy placement (low model right in 1 or more of 5 attempts), not "Too hard": both Opus solves matched with high confidence.

**verdict:** ready (local only). Status stays `checked` until a platform pass at Medium or above on this exact fingerprint.

**findings:**
1. **(1) No conflicting figures anywhere in the bundle.**
   - Honduras FY2023 request: 133,450 (D05 L763-775) and 133.5 (L3169-3187, 126.7+6.0+0.8). FY2025: 86,300 (D08 L733), 86.3 (Table A-3) and "$86.3 million" (L463).
   - El Salvador 124.8 to 87.7, Guatemala 162.8 to 115.8 and Mexico 141.6 to 109.7 agree across tables and prose.
   - Same-name figures that differ are other measures: the FY2023 DA directive "$126.7 million of DA for Honduras" (D05 L1313), the FY2024 requests in D06 ($136.5M Honduras; its $124.8M for El Salvador only coincides with the FY2023 request), DA-only Senate directives, and the FY2023 estimates.
   - The only Table A-1/A-3 mismatch is the USAID Central America Regional program row (29,950 vs 29.5).
2. **(2) "Country" exclusions are clean.**
   - Without the exclusion, USAID Central America Regional (59.02% decline) wins.
   - The Central America aggregate, which the lever notes leave out, would give 35.89% on D05's $986.8M base (above Honduras) or 34.04% on the $959.0M base. "Country" excludes it.
   - State Central America Regional (33.94%) ranks below Honduras. Barbados and Eastern Caribbean rose 14.1%. Bolivia has no D05 row and is 0 in FY2025.
3. **(3) Wording ambiguity is low.** The base, request-vs-estimate and precision are pinned. The phrase names both the measure and its base, the form the Coach itself proposed after its earlier "largest" (PIN3) flag. A reversed base gives 54.6%, which is non-standard. Reading "decline" as absolute would give Colombia (49,600); "percentage" rules that out. The advisory "Answer matches a stated figure" may cite D08's printed -39.1%, but the question states how to compute.
4. **(4) Verbatim check: the platform result is unknown and matters.**
   - The six D08 row/prose quotes are exact single-line matches.
   - The D08 header quote and all seven D05 quotes match only once line breaks are collapsed. The capture shows the platform's Doc 3 text is also one value per line.
   - No single-line D05 passage of 12 or more characters carries the Honduras value. If the form does not collapse whitespace, both blocking checks ("Verbatim evidence" and "Necessary documents cited") fail for Doc 3.
   - Required: Save passage on a Doc 3 Table 2 row before submission. Evidence is part of the fingerprint, so any change means a new revision and fresh checks.
5. **(5) Number rule:** the only flag is Step 4's operand 47,150. It is Step 3's "=" result and is printed in neither Doc 3 nor Doc 8. The one recorded form precedent (aq-00949 q05) accepted derived operands in a step citing two documents, so the risk is low. Step 9 cites only Doc 8 for "600 in both years"; it passes the number rule, but the FY2023 half comes from Doc 3.
6. **Error in the lever-check notes (not part of the fingerprint):** the D08 removal counterfactual is wrong. The -36.75% it quotes is the FY2024→FY2025 change, which itself needs D08. Without D08 the result is Honduras +2.25%, with Mexico leading at -21.31%. Also, D05 has no Bolivia row; it does not show 0. Correct the notes; no re-test is needed.
7. **Coincidence:** D08 L287, "$47.2 million decrease in DA for Honduras" (DA only, against the FY2023 estimate), equals the gold's total decline (47.15). This happens because requested FY2023 DA equals estimated FY2023 DA (126.7) and Honduras's other requested accounts (GHP-USAID 6.0, IMET 0.8) are the same in both requests. A model without D05 computing 47.2/133.5 lands on 35 only through an unsupported reading, so the removal-test risk is low. The sentence does make the answer country stand out, which adds to the too-easy risk.
8. **External checks I could not run:** authorship ("I wrote this question myself" and the export accepting only `user`), and the duplicate check against the earlier returned trial-04 q03 (same family, Venezuela). The capture's drafts panel is empty.
9. **Process disclosure:** early on I wrote temporary body copies of the texts to the session scratchpad for a comparison. I wrote no workspace files.

Files: `D:\Dev\Docket\tasks\aq-docket-trial-04\questions\q01.md`, `D:\Dev\Docket\tasks\aq-docket-trial-04\text\D05.txt`, `D:\Dev\Docket\tasks\aq-docket-trial-04\text\D08.txt`, `D:\Dev\Docket\tasks\aq-docket-trial-04\runs\q01-r1-v2-34a88efeff7e0867b5ee4d25d9f6ee8903ba46d5bf7935a50fc18344170fa9ad\results\`
