# i07 strong-solver screen: raw returns (2026-10-18)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i07-screen-0cc67f6a6786954d/solver-1 and the exact sentence. Gold: gain of $4.6 million.
Returns kept in substance (harness indentation removed), numbered by launch label (arrival order: 1, 2, 3).

## Solve 1: net gain of $4.6 million (right), confidence high

answer: A net gain of $4.6 million (Q3 plus Q4 2025)

path: (1) Definition (D09; same in D01, D04, D07): non-GAAP excludes "(iii) gains or losses related to the fair value of the company's strategic investments"; the reconciliation line is added to GAAP other income (expense), net; positive = decrease (loss), parentheses = increase (gain); fiscal year = calendar year. (2) Q3 2025, D07 L256/288: "|Decrease in fair value of strategic investments|2.6|10.8|12.2|50.5|" (Q3'25, Q3'24, 9M'25, 9M'24) → $2.6M loss; check (9.8) + 2.6 = (7.2) matches printed non-GAAP other expense. (3) Q4 2025, D09 L277/309: "|(Increase) decrease in fair value of strategic investments|(7.2)|7.2|5.0|57.7|" (Q4'25, Q4'24, FY'25, FY'24) → $7.2M gain; check 6.5 + (7.2) = (0.7) matches; FY 2025 $5.0M loss: (7.7) + 5.0 = (2.7) matches. (4) H2 = 2.6 + (−7.2) = −4.6 → net increase 4.6 → gain $4.6M. (5) Check: D04 L272 "|(Increase) decrease ...|(5.4)|12.7|9.6|39.7|" → H1 loss 9.6; FY 5.0 − 9.6 = −4.6 → gain 4.6; D01 Q1'25 15.0 − 5.4 = 9.6; 9.6 + 2.6 = 12.2 (D07 9M); 12.2 − 7.2 = 5.0 (D09 FY). (6) Not restated in D05/D02. (7) docs/ rows unchanged.

minimal_documents: D07 + D09 (alternatives D04 + D09, D05 + D09; D09 needed in every set).

readings: intended H2 gain $4.6M; misreadings: Q4 alone gain $7.2M; FY loss $5.0M; both quarters as decreases loss $9.8M; after-tax not disclosed.

gaps: D09 read in full; D07 L160-319, D04 L178-327, D01 L196-325 in part; D02, D03, D05, D06, D08 by targeted searches; the figure is the pre-tax reconciliation item.

contaminated: no

## Solve 2: gain of $4.6 million (right), confidence high

answer: Gain of $4.6 million (net rise in fair value in the second half of 2025)

path: (1) H2 2025 = July 1 – December 31, 2025 (calendar fiscal year per D09); no document prints a second-half figure. (2) D07 and D09: non-GAAP excludes "(iii) gains or losses related to the fair value of the company's strategic investments" → "decrease" adjustment = loss in GAAP, "(increase)" = gain. (3) Q3 2025, D07 L256/288 (docs L261/297): "Decrease in fair value of strategic investments|2.6|10.8|12.2|50.5|" → Q3 loss 2.6, 9M loss 12.2; sign check (9.8) + 2.6 = (7.2). (4) Q4 2025, D09 L277/309 (docs L282/318): "(Increase) decrease in fair value of strategic investments|(7.2)|7.2|5.0|57.7|" → Q4 gain 7.2, FY loss 5.0; check 6.5 − 7.2 = (0.7). (5) H1 2025, D04 L272/304: "(5.4)|12.7|9.6|39.7" → H1 loss 9.6; D05 repeats; D01 Q1 15.0 − 5.4 = 9.6. (6) Route A: −2.6 + 7.2 = +4.6 gain; Route B: 5.0 − 9.6 = −4.6 net decrease = gain 4.6; consistency 9.6 + 2.6 = 12.2; 12.2 − 7.2 = 5.0.

minimal_documents: {D07, D09} (alternatives {D04, D09}, {D05, D09}; D09 indispensable).

readings: after-tax not answerable; misreading → loss $9.8M (D09's "(7.2)" read as a decrease, or D08's Q4 2024 "Decrease ... |7.2|" used, added to Q3's 2.6), ruled out by the sign check; no other fiscal calendar.

gaps: none for the answer; D07 and D09 read in full; D04, D05 L180-329; others by searches; text-only; question.txt not opened.

contaminated: no (session context had only an automatic git-status snapshot of unrelated filenames)

## Solve 3: net gain of $4.6 million (right), confidence high

answer: A net gain of $4.6 million (pre-tax) in the second half of 2025 — a $2.6M loss in Q3 2025 plus a $7.2M gain in Q4 2025

path: (1) Definition (D09 L189; D07 L168; D04 L184): "(iii) gains or losses related to the fair value of the company's strategic investments"; decrease = loss, (increase) = gain. (2) Q3 2025, D07 L237-257: "Decrease in fair value of strategic investments|2.6|10.8|12.2|50.5|" → loss 2.6; 9M loss 12.2; check (9.8) + 2.6 = (7.2). (3) Q4 2025, D09 L258-278: "(Increase) decrease in fair value of strategic investments|(7.2)|7.2|5.0|57.7|" → gain 7.2; FY loss 5.0; checks 6.5 − 7.2 = (0.7), FY (7.7) + 5.0 = (2.7). (4) H1 2025, D04 L253-273: "(5.4)|12.7|9.6|39.7" → Q2 gain 5.4, H1 loss 9.6; D01 Q1 loss 15.0; 2026 releases repeat comparatives unchanged. (5) Q3 + Q4 = −2.6 + 7.2 = +4.6 (gain); FY − H1 = 5.0 − 9.6 = −4.6 decrease = gain; 12.2 − 9.6 = 2.6; 5.0 − 12.2 = −7.2; GAAP other H2 (9.8) + 6.5 = (3.3) = FY (7.7) − H1 (4.4); non-GAAP H2 (7.2) + (0.7) = (7.9) = (2.7) − 5.2; GAAP minus non-GAAP = 4.6 gain. (6) docs/ match.

minimal_documents: D09 + D07, or D09 + D04, or D09 + D05 (D09 in every set).

readings: naive "loss of $4.6M" from FY − H1 is wrong (the row label is "(Increase) decrease"); Q4 only → gain $7.2M; whole H2 GAAP other income (expense) $(3.3)M is a different quantity.

gaps: pre-tax reconciliation item only (no tax effect or realized/unrealized split); D09 read in full, D07 L160-319, D04 L176-335, D01 L270-285; searches across all files.

contaminated: no
