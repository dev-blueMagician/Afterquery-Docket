# Removal probe, packet solver-1 (Doc 4 / local D04 left out), q01 rev 0

- Date: 2026-10-09
- Question (verbatim, packet question.txt): To the nearest 10 MW, how much Calpine-owned capacity must be divested under DOJ's Constellation-Calpine settlement in relevant markets holding a coal plant covered by EPA's coal-ash deadline proposal?
- Packet renumbering (probe.json): D01->D01, D02->D02, D03->D03, D05->D04, D06->D05; Doc 4 removed.
- Agent: fresh blind-solver (claude-opus-5-5), packet path and question only.
- Bound to: q01 rev 0, tested_sha256 2e56252faf9b7786a217ca08d35315cfddc14a5b607a87fa8a140657e51b7c8f

## Raw return (verbatim)

answer: not answerable — the packet contains no EPA coal-ash deadline proposal, so it never identifies which coal plant(s) that proposal covers or where they sit; without that, it cannot be determined whether ERCOT, PJM Coastal Mid-Atlantic, both or neither is a "relevant market holding" such a plant. (Divestiture capacity per market is computable; see path/readings.)
confidence: high (that it is not answerable from this packet)

path:
1. Packet (text/manifest.json): D01–D05, all text-sourced, no PDFs/layout files. D01 = FERC reactive-power NOPR (Mar 2024); D02 = DOE North Plains Connector NOI (Oct 2024); D03 = WAPA rate order WAPA-218 (Jul 2025); D04 = DOJ proposed final judgment + Competitive Impact Statement, US v. Constellation/Calpine (90 FR 59205, Dec 18 2025); D05 = FERC order on inverter-based-resource reliability standards (Feb 2026), which mentions Calpine only as a motion to intervene.
2. Searched all of text/ for "EPA", "Environmental Protection Agency", "coal ash", "coal combustion", "CCR", "impoundment", "landfill", "unlined", "groundwater", "closure", "257": no EPA/coal-ash content. "Coal" appears only generically: D01 fn 11 ("Synchronous generating facilities (e.g., coal, gas, nuclear resources)…"); D04 ¶11 ("In PJM, Constellation owns … coal plants" — PJM-wide, Constellation not Calpine, no plant named); D04 ¶17 and CIS p. 59218 (generic descriptions of coal units). D02 mentions "Colstrip" only as a Montana town/substation, outside both markets.
3. Relevant markets (D04, CIS pp. 59216–17): "two relevant geographic markets… One market comprises the area operated by … ('ERCOT')… The second market comprises the Coastal Mid-Atlantic area of the PJM Interconnection." Complaint ¶33: that area "includes southeastern Pennsylvania, New Jersey, Delaware, and the eastern shores of Maryland and Virginia."
4. Capacities (D04, CIS p. 59220, §III.A.1):
   - ERCOT: "Jack A. Fusco is a 557 MW combined-cycle…"; "Gregory is a 365 MW combined-cycle… Calpine owns approximately 28.5% of Gregory." (Final judgment II.I.2: "Calpine's interest in the Gregory Power Plant.")
   - PJM Coastal Mid-Atlantic: "Bethlehem is a 1,134 MW…"; "York 1 is a 569 MW…"; "York 2 is an 828 MW…"; "Hay Road is a 1,136 MW…"; "Edge Moor is a 707 MW…"
   - Complaint ¶13 gives the Gregory stake slightly differently: "holds a 28% interest."
5. Calculations:
   - ERCOT: 557 + 0.285×365 = 557 + 104.025 = 661.0 MW → 660 MW (with 28%: 659.2 → 660).
   - PJM Coastal Mid-Atlantic: 1,134 + 569 + 828 + 1,136 + 707 = 4,374 MW → 4,370 MW.
   - Both markets: 5,035.0 MW → 5,040 MW (with 28%: 5,033.2 → 5,030; the total sits on a rounding boundary).
6. Missing fact: which coal plant(s) EPA's coal-ash deadline proposal covers and where they are. D04 does not say whether any coal plant is located in either relevant market.

minimal_documents: D04 suffices for the capacity side; no packet document supplies the coal-ash filter, and D01, D02, D03 and D05 cannot substitute for the missing EPA document.

readings (conditional on where the missing EPA document places the plant):
- ERCOT only: 660 MW (920 if Gregory's full 365 MW is wrongly counted).
- PJM Coastal Mid-Atlantic only: 4,370 MW.
- Both: 5,040 MW (5,030 with the 28% stake; 5,300 with Gregory in full).
- Neither (e.g., a covered plant in PJM outside the Coastal Mid-Atlantic area, or in Texas outside ERCOT): 0.

gaps:
- No EPA coal-ash deadline proposal in the packet.
- D01 read only for lines 1–60 plus targeted searches; D02, D03, D04 and D05 read in full.
- docs/ not opened (caller limited reading to text/); per the manifest text/ was extracted directly from docs/.
- No extraction problems.

contaminated: no — only the question and paths were received; the git-status context concerns a different task (aq-00949) and contains no answer, reasoning or lever.

forced_guess: 660
forced_probability: 0.4 | basis: mostly inference from the packet, partly memory.
- Packet inference: the coal-plant filter most likely selects one of the two markets; the "Calpine-owned" wording only matters in ERCOT (Gregory's 28.5% share); 661.0 rounds to 660 whether the stake is 28% or 28.5%, while the two-market total sits on a rounding boundary.
- General memory (not packet facts): Texas/ERCOT has many operating coal plants with coal-ash units, while southeastern Pennsylvania, New Jersey, Delaware and the eastern shores have few or none left.
- Rough alternatives: 4,370 at about 0.2; 5,040 at about 0.2.

## Caller assessment

Unforced: not answerable (no reach). Forced: the gold at p 0.4, reached through the question's wording ("Calpine-owned"
matters only where ownership is partial, i.e. Gregory in ERCOT; nearest-10 precision avoids the two-market boundary)
and remembered regional coal geography, not through any packet fact about coal plants. Under the removal-probe rule
an inference-based forced reach is treated as a failure risk for the platform's Document check on Doc 4; see q01
Lever checks for the repair decision.
