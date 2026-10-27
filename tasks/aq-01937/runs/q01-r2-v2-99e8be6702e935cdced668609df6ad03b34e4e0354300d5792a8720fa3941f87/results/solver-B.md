# q01 rev 2 solver B (fresh blind-solver, packet solver-2), 2026-10-08
tested_sha256: 99e8be6702e935cdced668609df6ad03b34e4e0354300d5792a8720fa3941f87
Transcript audit (audit_transcript2.py): 21 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: 22.40%
confidence: high

path:
1. AUM table footnote (D06 line 225; D10 line 189): "Includes real estate investment trusts, currency and commodities, including SPDR(R) Gold Shares and SPDR(R) Gold MiniSharesSM Trust, for which we are not the investment manager but act as the marketing agent." The boilerplate footnote gives the dollar amount.
2. June 30, 2025 (D06, 2Q25 release dated July 15, 2025): AUM 5,117 (line 223; line 47); about $116 billion marketing-agent-only (line 394, docs line 415); 5,117 unrevised in D07-D10.
3. June 30, 2026 (D10, 2Q26 release dated July 16, 2026): AUM 6,278 (line 162 "Balance as of June 30, 2026"; line 58); about $157 billion (line 360, docs line 371).
4. 5,001; 6,121; 1,120 / 5,001 = 0.2239552 -> 22.3955% -> 22.40%.
5. Table checks: D06 asset classes 3,218 + 700 + 525 + 449 + 225 = 5,117; D10 4,051 + 776 + 621 + 567 + 263 = 6,278.

minimal_documents: D06 + D10 (D06 only source of the $116B; D10 only source for June 30, 2026; D07-D09 repeat 5,117 but not the $116B; D01, D04 predate the period).

readings: total reported AUM 22.69% (ignores the qualifier; headline "increased 23%"); whole Alternative Investments line 22.96% (weaker: the clause refers to the SPDR Gold products, not the REITs; the boilerplate quantifies the marketing-agent-only assets directly); rounded headline figures about 23.25% (not defensible at two decimals).

gaps: "approximately" amounts taken at face value. Read D06 lines 1-62, 120-254, 388-399 and D10 lines 1-231, 340-399; others by targeted searches (investment manager, marketing agent, AUM, sub-advisory, 5,117, 6,278); nothing defines AUM differently.
contaminated: no.
