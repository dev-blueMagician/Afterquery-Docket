# q01 rev 2 solver A (fresh blind-solver, packet solver-1), 2026-10-08
tested_sha256: 99e8be6702e935cdced668609df6ad03b34e4e0354300d5792a8720fa3941f87
Transcript audit (audit_transcript2.py): 16 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: 22.40%
confidence: high

path:
1. The question's wording matches the AUM footnote (D06 line 225; D10 line 189): "including SPDR(R) Gold Shares and SPDR(R) Gold MiniSharesSM Trust, for which we are not the investment manager but act as the marketing agent." So the asked assets = reported AUM minus the marketing-agent SPDR assets.
2. June 30, 2025 (D06, docs/stt_ex991_2025-07-15.txt): AUM $5,117B (line 223; also 47, 128, 241); marketing-agent portion $116B (line 394, docs line 415). 5,117 unchanged in D07 (60, 163, 181, 191), D08 (189, 200), D09 (205, 219), D10 (58, 209); D06's "revised from prior presentations" note covers only the 3Q24 and 2Q24 columns.
3. June 30, 2026 (D10, docs/stt_ex991_2026-07-16.txt): AUM $6,278B (line 162, column "Balance as of June 30, 2026"; also 58, 169, 176, 186, 209); marketing-agent portion $157B (line 360, docs line 371).
4. 5,117 - 116 = 5,001; 6,278 - 157 = 6,121; 1,120 / 5,001 = 0.2239552 -> 22.3955% -> 22.40%.

minimal_documents: D06 + D10 (the $116B only in D06; $157B and $6,278B only in D10; 5,117 also in D07-D10).

readings: total reported AUM 22.69% (D10 "23" YoY; ignores "investment manager"); whole Alternative Investments line 22.96% (unlikely: the clause refers to the SPDR Gold products and the only quantified amount is the SPDR amount); rounded headline figures not suitable at two decimals.

gaps: SPDR amounts "approximately"; D10 read in full; D06 lines 1-260 and 385-424; others by targeted searches (investment manager; AUM; marketing agent / SPDR / June 30, 2025; 5,117 / 6,278; revised / recast / restated; Gold / solely); other "Gold" mentions are unquantified inflow mentions.
contaminated: no.
