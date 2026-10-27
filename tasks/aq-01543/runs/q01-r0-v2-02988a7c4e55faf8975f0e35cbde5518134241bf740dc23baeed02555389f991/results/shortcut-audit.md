# q01 rev 0 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-07

Transcript audit (caller, parsed tool calls): 17 calls (Glob, Grep, Read), every path inside shortcut/; clean.

answer: 5.3 percentage points. Bulgaria's coal share is about 33.4% and has to be derived. South Korea's is 28.1%, stated directly.

verdict: clear

shortest_path:
1. South Korea (D15 line 9): "Korea's total electricity generation in 2024 reached 595.6 TWh… Coal and LNG each generated 167.2TWh, or 28.1%". The table at lines 71–92 repeats the 2024 row (coal 167.2 | 28.1%). Recomputing gives 167.2/595.6 = 28.07%.
2. Bulgaria (D02): no sentence gives a coal share for calendar 2024, so it has to be derived from three statements in the document:
   - line 10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". The comma is a decimal separator, so this is 28.46 TWh.
   - line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the… (IAEA)."
   - Nuclear = 0.416 × 37,963 = 15,792.6 GWh. Coal = 28,460 − 15,792.6 = 12,667.4 GWh. Coal share = 12,667.4 / 37,963 = 33.37%. The same result comes from 74.97% (baseload share) − 41.6%.
3. Difference: 33.37 − 28.1 = 5.27, or 33.37 − 28.07 = 5.30. Rounding Bulgaria to 33.4 first gives 33.4 − 28.1 = 5.3. Every variant rounds to 5.3 pp.

sufficient_documents: D02 (Bulgaria) and D15 (South Korea) are both needed, and there is no alternative. Bulgaria appears only in D02 and D13; D13 mentions it only for interconnections and the BRUA pipeline, with no coal data. Korea appears only in D15 and D11; D11 mentions it only as POSCO E&C, a South Korean contractor. The original files under docs/ match the text/ files on every line I checked.

searches:
- Read the manifest and D02, D15 and D13 in full. Read lines 180–194 of D11.
- Grepped all 20 text/ files for: Bulgaria/Bulgarian; Korea; ROK, Seoul, Sofia, Kozloduy, Maritsa/Maritza, KEPCO; and coal near share/percent/%.
- The other coal-share hits (D05, D07, D08, D11, D12, D14, D18, D20) are about other countries.
- Grepped the docs/ originals for Bulgaria (Baseload, 37,963, 41.6, 27.6%, coal) and South Korea (coal) to confirm the extracted text matches.
- No document states the Bulgaria–Korea difference, ranks the two countries, or gives Bulgaria's coal share for calendar 2024 directly. There is no single-document route and no whole-answer lookup. Following the guide, this is a simple cross-document difference where one input needs a short derivation within its document, so it is not a shortcut.

readings/gaps:
- Wrong-period distractors:
  - −0.5 pp: uses D02 line 18, "From September 2024 to August 2025… coal being dominant at 27.6%". That is a different period, and "calendar year 2024" rules it out.
  - −1.1 pp: uses the 2025 figure, "27 percent in 2025" (D02 lines 70 and 135).
  - 6.5 pp: mixes the September 2024–August 2025 nuclear figure of 40.38% (line 18) with the 2024 baseload number.
- Interpretive risk: the "(coal, nuclear)" parenthetical defines baseload. A reader who assumed baseload also covered gas-fired thermal plants would get a lower Bulgaria share, but the text doesn't support that.
- Sensitivity: the result falls between 5.27 and 5.30 using the stated 41.6% and either the stated 28.1% or the recomputed 28.07%. If the nuclear share were about 41.65% instead of 41.6%, the result would drop to about 5.2, but the document gives 41.6%.
- Extraction gaps (unresolved):
  - D02's monthly production chart ("View Bulgaria's Electricity Production from Jan 2024 to Dec 2024 in the chart:") has no content in the text.
  - D15's LNG import chart is missing.
  - D02's renewables figure, "3,3264 GWh", is garbled.
  - None of these is needed for the answer. The missing Bulgaria chart is the only gap that could have held a source split, and it can't be checked.
- Difficulty risk: South Korea's value is a one-line lookup. The main difficulty is the period trap in D02 (27.6% and 27% versus the 2024 derivation). The question's "calendar year 2024" wording flags the trap without giving away the answer.

contamination: none observed. The session context contained only an automatic git-status list of file names (other tasks such as aq-00949 and memory file names), with no content for this task. I read no notes, question files, snapshots or other packets, and no CLAUDE.md or memory content. I could not check the Claude Code version or the omitClaudeMd flag from inside the session.
