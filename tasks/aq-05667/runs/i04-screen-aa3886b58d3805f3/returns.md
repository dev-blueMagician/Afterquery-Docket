# i04 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i04-screen-aa3886b58d3805f3/solver-1 and the exact sentence. Gold: +148.
Returns kept in substance below (the harness indents subagent reports; indentation removed).

## Solve 1: +148 (right), confidence high

answer: +148 stores; combined count 5,012 at Dec 31, 2023 to 5,160 at Dec 31, 2025; Paint Stores Group and
Consumer Brands Group, "the two segments the filings say have stores 'in operation'".
confidence: high; "The only real risk is which stores the question means".
path: D01 L44 (PSG 84 opened, 5 closed, +79; 4,773), L45 (CBG 18/2, +16; 334 in Latin America), L46 (PCG
"branches", left out); D02 L41 (PSG +80; 4,853), L42 (CBG 13/40, -27; 307), L43 (PCG branches, left out).
End-2023 4,694 + 318 = 5,012; end-2025 5,160; +148 (= 95 + 53; PSG +159, CBG -11).
minimal_documents: D01 + D02; the 10-Qs give no store count.
readings: PSG only +159; CBG only -11; with PCG branches +143 (weak: "branches").
gaps: end-2023 derived; 10-Qs searched, not read in full.
contaminated: no

## Solve 2: +148 (right), confidence high

answer: +148 stores. Company-wide store count went from 5,012 at Dec 31, 2023 to 5,160 at Dec 31, 2025,
counting Paint Stores Group and Consumer Brands Group stores.
confidence: high (arithmetic checked twice; "the only real risk is how broad 'stores' is meant to be").
path: D01 L44-45, D02 L41-42 quoted; 4,694 + 318 = 5,012; 4,853 + 307 = 5,160; +148; checks 4,773 + 80,
334 - 27; Suvinil added no stores; PCG "branches" excluded (D01 L46, D02 L43).
minimal_documents: D01 + D02, both required; no 10-Q store counts.
readings: PSG only +159; with branches +143 (weak); CBG only -11 (not natural).
gaps: end-2023 derived assuming no acquired/divested stores in 2024.
contaminated: no

## Solve 3: +148 (right), confidence high on arithmetic, medium-high on the reading

answer: +148 stores; 5,012 to 5,160; PSG +159, CBG -11.
confidence: "high (that the arithmetic is right); medium-high (that 'stores Sherwin-Williams operated' means
both store-operating segments, not just the Paint Stores Group)".
path: D01 L44-45, D02 L41-42; same derivation and checks; PCG branches left out.
minimal_documents: D01 + D02; 10-Q mentions of "new stores" are generic.
readings: PSG only +159 ("the US/Canada/Caribbean 'Sherwin-Williams' stores"); with branches +143 (weak);
one-year readings +53 / +80.
gaps: end-2023 derived; 10-Qs searched, not read in full.
contaminated: no
