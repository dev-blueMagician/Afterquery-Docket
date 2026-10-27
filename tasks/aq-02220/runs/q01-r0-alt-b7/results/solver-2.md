# Removal probe return: q02 rev 0 without Doc 1 (D03)

- Date: 2026-10-08
- tested_sha256: 9a2b416cec8ce40625eb5806aff73a1fedd2dd1aecd670ea5c496946dc6ed5ce
- Packet: tasks/aq-02220/runs/q01-r0-alt-b7/solver-2 (Doc 2 -> D01, Doc 3 -> D02, Doc 4 -> D03; neutral headers)
- Role: blind-solver (fresh context, question only, plus the forced-guess instruction)

Raw return (verbatim):

answer: £9.5 million, undiscounted. This is Stage 1a national mapping at £1.0m plus Stage 1b local refinement at £8.5m. It assumes that in the private-sector-led model central government leads stages 1a and 1b and the private sector leads Stage 2 (feasibility). The packet does not state outright who leads Stage 1b in that model; that part is inferred.
confidence: medium

path:
1. D01, para 61: "The methodology is assumed to be deployed in 200 towns and cities in the central scenario".
2. D01, Table 6 "Central assumptions for the cost to government of designating zones" (around lines 1083–1175):
   - "Stage 1a - National mapping … Cost per town/ city £5,000"
   - "Proportion of cities going forward to Stage 1b 85%"
   - "Stage 1b - Local Refinement … Cost per city £50,000"
   - "Average number of zones per city 3"
   - "Stage 2 - Feasibility … Cost per feasibility study £40,000"
   - Procurement stage: £300,000 per concession, £850,000 per town/city for DPD, 75% concession-style.
3. D01, para 64 confirms the 85% gives 170: "each of the 170 towns and cities that designate zones".
4. D01, Table 17 (sensitivity) gives central values "Stage 1, cost per city £5,000" and "Stage 2, cost per city £50,000". The "Stage 2" label here is loose: the £50,000 is the Table 6 Stage 1b cost, and feasibility is listed separately as "Feasibility per zone £40,000".
5. D02 (2022 government response):
   - line 61: "a national mapping exercise, led by a central authority"
   - line 1146: "the central authority will be the body who carries out the national mapping exercise"
   - line 1148: "The consultation outlined three possible models for the roles of the Central Authority, Zoning Coordinator, and the private sector in the local refinement and feasibility stages."
6. D02, line 956: "the model where local authorities lead on both local refinement and feasibility stages … (stage 1b and stage 2, respectively). The same number of respondents supported the model where the private sector leads (or at least informs) the feasibility stage." Line 958: "In contrast, 4 respondents did not consider the central authority should play a role in either the national mapping (1a) nor the local refinement (1b) stages."
7. Inference: in the private-sector model the private sector leads Stage 2. The central authority leads 1a (stated) and 1b (inferred from the contrast sentence and the plural "stages" in the question).
8. Calculation:
   - 1a: 200 × £5,000 = £1,000,000
   - 1b: 200 × 0.85 = 170 cities; 170 × £50,000 = £8,500,000
   - Total: £9,500,000

minimal_documents: D01 + D02. D03 (the 2026 summary) is not needed: it uses renamed bodies and has no private-sector-led model. D02 is the only source on the models, so nothing in the packet replaces it.

readings:
- If only the explicitly central stage counts (1a): £1.0m.
- If "or at least informs" means central government still leads feasibility with private-sector input: 1a + 1b + 2 = £1.0m + £8.5m + (170 × 3 × £40,000 = £20.4m) = £29.9m.
- If the 85% progression is ignored (200 × £50,000 for 1b): £11.0m.

gaps:
- The 2021 consultation that defined the three models is not in the packet. Who leads Stage 1b in the private-sector-led model is never stated, so the main answer rests on inference.
- The Table 6 columns were scrambled in extraction and there is no layout file. I rebuilt the row pairings from the cell order, and Table 17 and para 64 confirm them.
- Coverage: I read D03 in full. In D01 I read the cost-to-government, assumptions and sensitivity sections; in D02 the roles, methodology and delivery-model sections. The rest of D01 and D02 was covered only by keyword searches (private, model, stage, lead, central authority, refinement, mapping, feasibility, inform). Per your instruction I did not inspect docs/.

contaminated: no

Files: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-02220\runs\q01-r0-alt-b7\solver-2\text\D01.txt, D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-02220\runs\q01-r0-alt-b7\solver-2\text\D02.txt

forced_guess: £9.5 million
forced_probability: 0.6, source: both (the figures are from the documents; assigning Stage 1b to central government is inferred from the documents, with an unreliable memory of the 2021 consultation pointing the same way)
