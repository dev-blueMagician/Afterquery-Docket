# q01 rev 1 - independent review (fresh question-review subagent), 2026-10-07

q01 (rev 1; tested_sha256: 0fcfcb02914d5ee6538829c095f48733111454654ebd5d3934e372537f281dce)

gold_verified: yes. I recomputed it from the source text with Python. Inputs: D02 (Doc 1) L10 gives 37,963 GWh for 2024. L11 gives "Baseload power plants (coal, nuclear) … 28,46TWh", which is a decimal comma, so 28,460 GWh. L13 gives nuclear at "approximately 41.6%" of 2024 generation. D11 (Doc 2) L13 gives Poland's coal share at 56.2%.
- Nuclear output: 0.416 × 37,963 = 15,792.608 GWh.
- Coal output: 28,460 − 15,792.608 = 12,667.392 GWh, which is 33.3677% of production.
- Difference: 56.2 − 33.3677 = 22.832, which gives 22.8 percentage points.
- Every other printed candidate gives a different value at one decimal: 28.6, 29.2, 21.2, 21.6 and −18.8 on the Bulgaria side; 37.3, 27.1, 22.6 and 36.6 on the Poland side. Rebuilding Poland's share from its TWh figures gives 22.5 to 22.7, but the printed 56.2% is the stated figure for the asked quantity, so it governs.

outcome: A: match; B: match. Both got 22.8 by the same derivation, and each named and rejected 28.6 and 29.2. Both were fresh contexts. The only outside input was an auto-attached git status listing file names, with no answer content, so neither is contaminated. B's side remark "Every case rounds to 22.8" is wrong at a 41.65% nuclear share (22.88), but that does not affect its answer. Two supported matches.

closed-book: misses. It answered 27.7 (Poland about 57.1% minus Bulgaria about 29.4%), which is not equivalent to 22.8.

necessity:
- D02 (Doc 1, Bulgaria) is the only document with Bulgarian generation data. D13 names Bulgaria only as a trading neighbour and in the BRUA pipeline name; no other file matches Bulgaria. The removal probe without it answered "cannot be determined", with a forced guess of 28.2 (p 0.03) built from a recalled share of about 28%.
- D11 (Doc 2, Poland) is the only document that mentions Poland at all. The removal probe without it answered "cannot be determined", with a forced guess of 23.6 (p 0.15) built from a recalled share of about 57%.
- No smaller source set exists, and none of the deciding inputs is repeated in another document.
- I verified the probe packets: text bodies are byte-identical to the originals with only the header line renumbered, docs/ hashes match, and the question is verbatim in all six packets.

shortcut: clear. The shortest route is a lookup of D11 L13 plus a three-input derivation from D02 L10, L11 and L13, then a subtraction. No passage states Bulgaria's 2024 coal share or the difference. The capture overview prints 56.2%, 37,963 GWh and 41.6% as labelled figures, but not the baseload total or any Bulgarian coal share. That makes the inputs easier to find; it is not a whole-answer lookup.

source_assessment: no recorded gaps (source_gaps [], hash 4f53cda1…). One thing I assessed beyond that: D02 L42-44 refers to a monthly production chart whose data is not in the text. The capture matches docs/, so the platform's text lacks it too.
- Premises: they rest on L10, L11 and L13 only.
- Gold: the chart caption describes monthly totals, while the stated 2024 total is 37,963 GWh.
- Exclusions: none in this question.
- Uniqueness: the caption describes totals only, with no split by source, so it cannot supply a competing coal figure.
- Necessity: the chart sits inside D02, so it cannot replace D11.
- Shortcut: no answer can come from a chart that solvers cannot see.
This does not establish that the corpus is complete.

difficulty: medium (marginal). This is local suitability only; Easy is the single most likely platform outcome. Estimate: Too easy ~10%; Easy (Low 1-3/5) ~40%; Medium ~25%; Between levels (Low 0/5, Medium 4-5/5) ~20%; Too hard or Answer not supported ~5%.
What pushes toward Easy: the deciding inputs sit together in Doc 1's opening paragraphs, each dated 2024; the overview prints two of the three Bulgarian inputs; the 27.6% decoy is tied (its window opens its own sentence); "(coal, nuclear)" spells out the subtraction; about four dependent steps.
What supports Low 0/5: 27.6% is an answer-shaped coal share whose window label contains "2024", and a second printed share (27%, 2025) is nearby; no 2024 Bulgarian coal share is printed anywhere; the decimal comma in "28,46TWh"; workspace calibration shows the platform's low model takes printed decoys more often than local reviews predicted (aq-01278 q02, aq-01431 q01).
Risk of Between levels: once the medium model reads the window label, the derivation is short and unambiguous. The cue sits in the documents, not the wording, so there is nothing to remove from the question.
Noise that cuts across all tiers: early rounding near the 22.85 edge. Quick-test first if one is available. The local Opus solves measure fairness, not tier.

verdict: revise. Only the failure-mode text and the lever label need changing. Both are outside the fingerprint, so the rev 1 checks stand. After the fixes, status can go to checked, with the platform still pending. Platform-only checks (restricted names, original question, duplicate, token window) are unknown.

failure_modes:
- FM1 (Out-of-range period / Uses the wrong period or date): real. The D02 L18 passage exists and yields 56.2 − 27.6 = 28.6. The labels fit (Fiscal vs calendar period is the nearest alternative, but no fiscal year is involved). The wording does not rule it out, because the window starts in 2024. Soft claims: "because … coal had already fallen further" asserts a cause the documents don't establish (L18 is also on a consumption and energy-mix basis); "a few paragraphs below" (it is seven paragraphs after L10); "lands on it first" holds only for a search pairing "coal" with a percentage.
- FM2 (Figure that must be computed / Takes the wrong line item): needs revision. The trap is real (only coal percentages at L18, L70, L135); both wrong answers recompute (29.2, −18.8). False claim: "the next paragraph gives nuclear's 2024 share" (L12 sits between L11 and L13). The cause label doesn't fit the primary wrong answer (29.2 comes from a 2025-labelled figure: "Uses the wrong period or date"); "In 2024" plainly excludes a 2025 figure and the route repeats FM1's mechanism; −18.8 fits "Takes the wrong line item" (or Part vs total) but no run produced or named it. The supported in-derivation misstep is 21.6 (the September-August nuclear 40.38% mixed in), named by solver A and the auditor and recomputed in Lever checks. Re-anchor FM2 on a supported route or withdraw it; FM1 alone meets the 1-3 requirement.
- Necessary documents: blank, defaulting both to Answer component; correct.

findings:
1. Q15, FM2 box 3: "the next paragraph" is false. Correct it.
2. Q15, FM2 cause and route: mismatch; re-anchor or withdraw; keep each wrong answer recomputed in Lever checks.
3. Q15, FM1: tighten the three soft claims.
4. Q11, levers metadata: "Same series, right edition" is not active (one edition per country). Relabel; outside the fingerprint.
5. Q4/Q9 precision: 22.832 is 0.018 below the 22.85 edge. Early rounding at one decimal in TWh flips it: nuclear 15.8 gives 22.852 (22.9), coal 12.7 gives 22.746 (22.7), production 38.0 gives 22.9. A 41.6% share of 41.633 or more gives 22.9, and the source hedges both inputs ("some", "approximately"). Not a second defensible answer (each input has one stated figure and the precision is set), but a reviewer-note risk. Lever checks cite 15.79 giving 22.8 but omit that 15.8 gives 22.9; add it.
6. Q12 inference: the derivation assumes baseload means all coal plus nuclear generation, and that the IAEA share uses the same base as 37,963 GWh. The document's words support both; solver B, probe 2 and the auditor flagged them. A platform reviewer may note it.
7. Number-citation check: Steps 1-6 pass (aq-00949 q05 precedent for derived operands). The unnumbered "Decoys:" line holds two "=" calculations, and 29.2 is printed in neither document (aq-00949 q03: the second result of a multi-calculation step was flagged). Step 3's quote uses a straight apostrophe where the document has a curly one. Both advisory; editing the reasoning changes the fingerprint.
8. Q2 residual: if the platform's high model recalls exactly 56.2% for Poland, Doc 2 could be flagged as not needed. Local recall gave about 57% twice. State this at hand-over.
9. Records: every rev 1 record carries 0fcfcb02…, matching the report. The floor does not parse removal-probe records; probe coverage verified by hand. Wording overlap at most 0.33 (aq-01541 q03; shared run only "in percentage points to one decimal").
