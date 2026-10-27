# q01 rev 2 - independent review (fresh question-review subagent), 2026-10-07

Input: root, slug, question id, revision, fingerprint, target, source-gap hash, paths to the frozen snapshot, the
question file, the six raw returns of this fingerprint and the rev 1 review; three adjudication requests (rev 1
findings, probe results and Poland recall risk, probe 2's "Caveat on A"). No writer conversation.
Raw return below, unchanged except for this header.

q01 (rev 2; tested_sha256: 26ad5885c50053f6c5941ed69c351e22a71f110d3c0a91774b05256a9c2d5010)

**Short version:** the gold (22.8) holds, both blind solves match, the closed-book run misses, both probes miss and the shortcut audit is clear. The verdict is still revise, but only for four small corrections outside the fingerprint (findings 1–4). No new revision or re-test is needed.

gold_verified: yes. I recomputed it with Python from the originals. All four evidence quotes appear word for word in docs/ and text/, including the curly apostrophe (U+2019).
- Inputs: Poland 56.2% (Doc 2, D11 L13). Bulgaria: 37,963 GWh (D02 L10), "28,46TWh" coal plus nuclear = 28,460 GWh (L11), nuclear 41.6% (L13).
- Nuclear = 15,792.608 GWh. Coal = 12,667.392 GWh, which is 33.3677% of production. 56.2 − 33.3677 = 22.832, giving 22.8.
- Input precision: the coal-plus-nuclear total anywhere from 28.455 to 28.465 TWh still gives 22.8. A nuclear share of 41.55–41.65% gives 22.78–22.88; 22.9 needs 41.6177% or more. The stated 41.6% decides.
- Every other printed route differs at one decimal: 28.6, 29.2, 21.2, 21.6, −18.8 on the Bulgaria side; 37.3, 27.1, 22.6, 36.6 on the Poland side. Rebuilding Poland's share from its TWh figures gives 22.5–22.7, but the printed 56.2% is the stated figure and governs.

outcome: A: match; B: match. Both reached 22.8 by the same derivation, and each rejected 28.6, 29.2 and 21.6 as wrong-period readings. I checked the six transcripts myself:
- Prompts held only the root, packet path and the exact question; the probes also had the forced-guess line.
- Every read stayed inside its own packet (13, 14, 15, 1, 21 and 19 tool calls).
- Each saved result matches the run's final report.
- question.txt is byte-identical across all six packets. Probe packets are correctly renumbered, and the left-out source is absent from text/, docs/ and the manifest.

That gives two fresh, uncontaminated matches.

closed-book: misses. It answered 28.6 (Poland about 57.1% minus Bulgaria about 28.5%) with low confidence. That is not equivalent to 22.8; it equals failure mode 1's wrong value only by coincidence.

necessity:
- **D02 (Doc 1):** the only source of Bulgaria's three 2024 inputs. D13 names Bulgaria only as a trading partner and in the BRUA pipeline name (L23, L40), and no document has an EU-wide coal table. Without it, probe 1 said "not answerable" (forced guess 26.2, p 0.04).
- **D11 (Doc 2):** the only document that names Poland. Without it, probe 2 said "can't answer" (forced guess 23.6, p 0.15).
- No smaller document set exists, and nothing can replace either document.
- **Residual risk (not demonstrated):** Doc 2 is replaceable only by recalling a Poland share between 56.12% and 56.21%. Every local recall (two closed-book runs, two probes, one recall test) gave 57.0–57.1%. D11 credits its renewables paragraph to the Forum Energii yearbook, a likely source of the 56.2%, so a model trained on it could recall the exact figure. I put the Doc 2 removal-flag risk at about 5–10%. For Doc 1 it is under 3%, since that needs a recalled Bulgarian share of 33.35–33.45% and recalls gave 28–30%. State this at hand-over; it cannot be fixed without changing the partner country.

shortcut: clear. The verified shortest route is the D11 L13 lookup, plus the D02 L10/L11/L13 derivation (74.968 − 41.6 = 33.368), plus one subtraction. No passage states Bulgaria's 2024 coal share or the difference, and 22.8, 22.83, 33.37 and 33.4 appear nowhere. The capture's overview prints 56.2%, 37,963 GWh and 41.6%, but not the coal-plus-nuclear total or any Bulgarian coal share. That helps a solver find inputs; it does not give the answer.

source_assessment: no recorded gaps (source_gaps [], 4f53cda1…). One known unrendered item: D02 text L42–44 (docs lines 41–43), a monthly 2024 production chart.
- Premises: none rest on it.
- Gold: it shows monthly totals only, and the annual 37,963 GWh is already stated.
- Exclusions: none in this question.
- Uniqueness: a production chart has no split by source, so it cannot give a rival coal figure.
- Necessity: it sits inside Doc 1, so it cannot replace Doc 2.
- Shortcut: it is missing from the platform's text too, so it offers no route.

L11's "3,3264 GWh" renewables figure is malformed but unused. None of this shows the corpus is complete.

difficulty: medium (marginal), as local suitability only.
- **For Medium:** Bulgaria's 2024 share is printed nowhere and needs three 2024 inputs (decimal comma, GWh vs TWh). A precise 27.6% coal share whose window starts in "September 2024" sits in the same chapter, with a 40.38% nuclear share beside it. 22.832 sits 0.018 below a rounding edge that one-decimal TWh rounding crosses.
- **Against:** the inputs sit in Doc 1's opening paragraphs, each dated 2024. "(coal, nuclear)" spells out the subtraction. The decoy's window opens its own paragraph, which is the one-sentence disarm that measured Easy on aq-01320. Poland is a single lookup. A derived-window electricity question measured Easy on aq-01430 (q01).
- **Estimate:** Too easy ~10%, Easy ~37%, Medium ~27%, Between levels ~18%, Too hard or Answer not supported ~8%. Easy is still the likeliest outcome and this bundle has no Easy slot, so quick-test first if possible.

verdict: revise. Only findings 1–4 need fixing, and they sit outside the fingerprint (Lever checks and failure-mode boxes). Every fingerprinted field and all six checks stand, and the report recomputes 26ad5885 from the current file. After the fixes, status can go to checked, with the platform pending.

failure_modes:
- **FM1 (Out-of-range period / Uses the wrong period or date):** real. D02 L18 exists and gives 56.2 − 27.6 = 28.6, which is 5.8 above the gold, so "almost six points" is true. The label is the best fit, the cause fits, and "In 2024" does not plainly rule out a window that opens in 2024. All claims hold except the paragraph count (finding 2).
- **FM2 (Figure that must be computed / Uses the wrong period or date):** real. L11 with L18's 40.38% gives 74.968 − 40.38 = 34.588, then 21.612, so 21.6. The label is acceptable, the cause matches the first wrong step, no trap repeats, and the wording does not rule it out. No run produced 21.6, but four named it as a rejected reading. It has two inaccuracies (findings 3 and 4). FM1 alone meets the form if FM2 is withdrawn.
- **Necessary documents:** blank, so both default to "Answer component". That is correct, since each supplies inputs to the single component.

findings:
1. **Lever checks threshold is wrong.** "22.9 from 41.633% up" should be 41.6177%. Solver A's 41.62% is right; the caller note in solver-A.md (41.6323%) is wrong. This affects the record only, not the form.
2. **FM1 box 1, "seven paragraphs after".** The 27.6% paragraph is the Energy chapter's 10th (L18) and the production paragraph is its 2nd (L10). So it is eight after, with seven between. The rev 1 review's own count was off by one.
3. **FM2 boxes 1 and 3, "Energy overview".** Doc 1's Energy chapter has no Overview heading; its only one opens Environmental Technologies (docs line 156). The IAEA sentence is the Energy chapter's 5th paragraph (text L13). A reviewer following the label could land in the wrong chapter.
4. **FM2 box 1, "two shares".** Doc 1 L94 also says nuclear generates "more than one-third of its electricity". Say two numeric shares.
5. **Rev 1 findings (your item 1):**
   - Rev 1 #1 and #2 are resolved: FM2 is re-anchored on 21.6 and the cause now fits.
   - Rev 1 #3 is mostly resolved: the causal claim and "lands on it first" are gone, but the paragraph count is still off (finding 2).
   - Rev 1 #4 is resolved, and "State the rounding" is active. Rounding nuclear to 15.8 TWh gives 22.852, coal to 12.7 TWh gives 22.746, and production to 38.0 TWh gives 22.905. Rounding the coal share to 33.4 or the coal-plus-nuclear share to 75.0 still gives 22.8.
   - Rev 1 #5 is resolved except the threshold (finding 1).
   - Rev 1 #6 and #8 are recorded; the Poland recall risk must also go into the hand-over.
   - Rev 1 #7 is resolved: the decoy line has one "=" calculation, and the apostrophe is now curly (U+2019).
   - Rev 1 #9 is verified: all rev 2 records carry 26ad5885, and I checked the probe records by hand.
6. **"Caveat on A" in probe 2 (your item 3): it does not open a second defensible answer.**
   - The roughly 9.5 TWh (25.0%) left for other sources is fixed by two printed 2024 figures (37,963 GWh minus 28,46 TWh). It does not depend on how coal and nuclear are split.
   - Keeping the printed coal-plus-nuclear total, a 2024 coal share of 27.6% or 27% would need nuclear at 47.4% or 48.0%. That contradicts the printed 2024 figure of 41.6% (and the later window's 40.38%).
   - The 27–27.6% figures are dated 2025 and September 2024 to August 2025, on a consumption/supply basis. "35 percent in 2020 to 27 percent in 2025" brackets 33.4%.
   - Getting about 27% for 2024 means substituting a non-2024 figure or rejecting printed 2024 figures on outside plausibility. Neither is a document reading.
   - The derivation is the single defensible reading. All four rev 1/rev 2 solves, the auditor and probe 2 itself preferred it. Residual reviewer-note risk remains, and I put the "Answer not supported" risk at about 5%.
7. **Precision.** The stated "approximately 41.6%" spans the 22.85 edge, but the stated figure decides, so this is a reviewer-note risk, not a second answer. Asking for a whole number would remove the edge, but a recalled Poland share of about 56.5–56.8% would then hit the gold without Doc 2. One decimal place is the better choice.
8. **Form emulation.** The number check passes: each new result follows "=", and Steps 4–6 reuse derived operands in steps that name their source document (the pattern accepted on aq-00949 q05). The "Answer matches a stated figure" advisory may fire on 56.2% or 27.6%; per the aq-01320 precedent that is a false positive. The floor shows 0 FAIL and 1 WARN (origin: claude; the export takes user only).
9. **Platform-only checks are unknown:** restricted names, Original question, Not a duplicate, token window (the capture shows 85,970 prompt tokens), the form's solvers, and difficulty. Local wording overlap is at most 0.35; the only 6-token shared run is the generic phrase "in percentage points to one decimal", shared with aq-01541 q03. There is no platform evidence, and nothing here is a tier pass.
10. **Set.** q01 is the bundle's only question. The planned q02 candidate (iB1) uses different documents, so there is no shared answer path or giveaway.

I wrote no files; please save this return as the rev 2 review.md.

Files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\questions\q01.md
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\text\D02.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\text\D11.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r2-v2-26ad5885c50053f6c5941ed69c351e22a71f110d3c0a91774b05256a9c2d5010\results\solver-A.md
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r2-alt-k5\results\probes.md

Caller verification (2026-10-07): findings 1-4 confirmed against the sources (python: 22.85 is reached at a nuclear
share of 41.61773%; D02 Energy paragraphs L9-L18 make L18 the tenth and L10 the second; D02's only "Overview"
heading is at text L157; L94 "more than one-third of its electricity"). Fixed outside the fingerprint in q01.md.
