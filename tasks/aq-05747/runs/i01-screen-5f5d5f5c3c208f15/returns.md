# i01 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i01-screen-5f5d5f5c3c208f15/solver-1 and the exact sentence. Gold: 1,274.
Returns kept verbatim in substance (harness indentation removed).

## Solve 1: 1,274 (right), confidence high

answer: $1,274 million. The charge for the bottling operations in Africa, recorded when they became held
for sale in Q4 2025. The FY2025 release lists it as a transaction loss; the 2026 releases call it an
impairment charge.
confidence: high; the only open point is how to classify the charge.
path: (1) D05 L514 BODYARMOR $960M; LatAm trademark 13/44; APAC 41; L516 OTTI 40 and 25; tables
L680/L884 1,045 and L718 1,110; D05 L43/147/177 "non-cash impairment charge of $960 million".
(2) D05 L528 "a charge of $1,274 million related to our bottling operations in Africa that became held for
sale, primarily due to the negative net foreign currency translation adjustments"; Q4 row (709) and FY row
(713) reconcile. (3) D01 L404 "an impairment charge of $10 million related to our bottling operations in
Africa, which are held for sale" (table L494, same line item). (4) D03 L500 "reduction in the previously
recorded impairment charge of $66 million and $56 million"; tables L596/L674; 66 > 10 (66 - 56 = 10 from
D03 alone), so the previously recorded charge must include the FY2025 Africa charge. (5) Ranking: 1,274;
960; 393 (Nigeria); 44, 41, 40, 36 (Ghana), 31, 25. No other impairment wording for 2025.
minimal_documents: D05 + D03; alternative D05 + D01 (weaker, no pointer back to 2025).
readings: narrow (FY2025 release's Asset Impairments only) -> $960M; "the words 'together' in the
question point to the cross-release reading instead"; net of 2026 revisions -> $1,218M, rejected (recorded
in 2026); totals 1,110/1,045 rejected as aggregates.
gaps: no release says outright that the $1,274M was an impairment in fiscal 2025 (inferred from D03 and
the 66 > 10 arithmetic); text only; searches plus full reads of the impairment/transaction sections.
contaminated: no

## Solve 2: 1,274 (right), confidence high

answer: $1,274 million (the Q4 2025 charge on the African bottling operations, CCBA, when classified held
for sale; the 2026 releases call it an impairment charge; larger than the $960M BODYARMOR impairment).
confidence: high (the main alternative, $960 million, covered in readings)
path: (1) D05 L528 quote; Q4 row (709) = -(1,952 + 31) + 1,274; FY row (713) reconciled; operating 59 =
47 + 12. (2) D03 L500 quote; D01 L404 quote; same table line +10, (66), (56); 10 - 66 = -56; the $66M
reduction exceeds the only 2026 charge, so the previously recorded impairment includes the Q4 2025
$1,274M; D04 L43 and D05 L219 identify CCBA. (3) D05 Asset Impairments items (960, 13/44, 41, 40, 25;
tables 1,045 + 65 = 1,110). (4) Charges never called impairments: 393 Nigeria, 36 Ghana (28 "related to
assets held for sale" in Q2 + 8), 47 fairlife. (5) Ranking 1,274 > 960 > 393 > 44 > 41 > 40 > 25; the 2026
+10 and -66 belong to fiscal 2026.
minimal_documents: D05 + D03; weaker alternative D05 + D01 (impairment only by analogy); D02, D04
redundant.
readings: narrow (Asset Impairments heading or FY2025 labels) -> $960M, "D05 alone would be enough for
this, which fits poorly with 'earnings releases together'"; net of revisions -> $1,218M, rejected; totals
ruled out by "single".
gaps: no 10-K to confirm the classification; sections read in full listed; searches for impair, held for
sale, Africa, write-down, loss on, fair value less, 1,274, 1.3 billion, CCBA.
contaminated: no

## Solve 3: 1,274 (right), confidence high

answer: $1,274 million (Q4 2025 charge on the African bottling operations that became held for sale; the
FY2025 release lists it under transaction losses, the 2026 releases call it an impairment charge).
confidence: high (for the "releases together" reading; see readings for the single-release answer)
path: (1) D05 L514 $960M and the smaller impairments; 960 + 44 + 41 = 1,045 (L884) + 65 = 1,110 (L718).
(2) D05 L528 $1,274M; Q4 row (709). (3) D01 L404 $10M impairment, same row (L494). (4) D03 L500
reduction of 66 and 56; six-month table (56) (L674); 10 - 66 = -56; 66 > 10, so the previously recorded
impairment includes a pre-2026 charge, and the only one is D05's $1,274M. (5) Ranking 1,274 > 960 > 393
> 47 (fairlife, not an impairment) > 44 > 41 > 40 > 36 > 25. Quotes checked in the docs/ originals.
minimal_documents: D05 + D03; weaker alternative D05 + D01; D02, D04 not needed.
readings: single-release reading (what D05 itself labels an impairment) -> $960M, "D05 alone supports
this"; "The question's 'earnings releases together' wording favours the combined reading, which gives
$1,274M."
gaps: D05 never calls the $1,274M an impairment (label from D01/D03 only); the packet does not say
whether all of the $1,274M was the impairment or only part; searches across all five texts.
contaminated: no
