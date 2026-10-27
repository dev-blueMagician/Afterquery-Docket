# i01 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i01-screen-240e29debb0ddde8/solver-1 and the exact sentence. Gold: -10.7.
Returns are kept verbatim in substance below (the harness indents subagent reports; indentation removed).

## Solve 1: -10.7 (right), confidence medium

answer: -10.7 (2025's actual increase of $49.3 million was $10.7 million below the roughly $60 million
increase anticipated in the 2024 annual report)
confidence: medium. The facts are certain. The uncertainty is whether the anticipated increase is $60M
or only $40M.
path: D01 L23 outlook quoted in full ("$40 million in 2025. In addition, ... approximately $20 million of
Interest expense"); anticipated 40 + 20 = 60, the $20M "explicitly 'In addition'"; support: D01 L128-134
construction completes 2025, HQ financing interest capitalized in 2023-2024 (45.2, 23.8), so not expensed
then. Actual: D02 L61 465.0 vs 415.7 = 49.3; D02 L76 "Interest expense increased $49.3 million ...
interest expense related to the new global headquarters"; D01 L64 2024 = 415.7 (no restatement);
quarterly cross-check +0.8, +1.6, +13.8 (9M +16.2), implied Q4 +33.1, total 49.3; D02 L130 capitalized
interest fell 45.2 -> 37.2. 49.3 - 60.0 = -10.7; like-for-like because the actual includes HQ interest.
minimal_documents: D01 + D02; no alternatives (2025 10-Q outlooks do not restate it; D02's 2026 outlook
is another year; full-year 2025 only in D02).
readings: narrow reading, only the sentence phrased as an increase -> 49.3 - 40.0 = +9.3, judged weaker
("In addition" / "additional costs ... in 2025" mark the $20M as more interest on top of the $40M, and the
actual includes HQ interest).
gaps: both anticipated figures "approximately"; several ranges read by search only.
contaminated: no

## Solve 2: -10.7 (right), confidence medium

answer: -10.7 (in $ millions: the actual 2025 increase was $49.3M, which is $10.7M below the ~$60M the
2024 10-K anticipated)
confidence: medium. The facts and arithmetic are certain. The only risk is the reading: whether the
separately stated "~$20 million of Interest expense" for the HQ transition counts as part of "the increase
it had anticipated".
path: D02 L61 465.0 - 415.7 = 49.3, L76 confirms; D01 L64 base; 10-Q cross-check 9M +16.2, Q4 +33.1.
D01 L23 both sentences quoted; context: 2024 HQ interest capitalized (D01 L134 45.2, 23.8), construction
completes 2025 (L121), placed into service 2025 (D02 L116). Total anticipated 40 + 20 = 60; 49.3 - 60.0 =
-10.7. No later revision of the 2025 interest outlook (D05-D07 outlooks; regex over all text).
minimal_documents: D01 + D02, no replacements.
readings: narrow reading (only the "$40 million" sentence) -> +9.3, weaker for three reasons ("In
addition" / "additional costs ... in 2025"; the HQ interest was capitalized in 2024; D02's actual includes
HQ interest). Sign: signed -10.7, magnitude 10.7 below.
gaps: none; partial reading ranges listed.
contaminated: no

## Solve 3: -10.7 (right), confidence medium

answer: -10.7 (in $ millions). The actual increase of $49.3M was $10.7M less than the roughly $60M
increase the 2024 annual report anticipated.
confidence: medium. The text clearly supports adding the two anticipated amounts, but the alternative
reading below flips the sign of the answer.
path: D01 L23 refinancing and headquarters sentences; "In addition" and "additional costs" mean the $20M
comes on top; D01 L121 construction completes 2025. D02 L61 465.0 vs 415.7, L76 +49.3 incl. HQ interest,
L252 EBITDA table same; D01 L64. Like for like: the actual includes HQ interest, so compare with $60M:
49.3 - 60 = -10.7. D02 L21 later calls HQ interest "the incremental interest expense".
minimal_documents: D01 + D02, no substitutes; "expected to increase" found only at D01 L23 and D02 L21.
readings:
- Reading B: only the sentence that literally says "Interest expense is expected to increase by
  approximately $40 million in 2025", the $20M treated as transition cost rather than an increase ->
  +9.3. "It is defensible because of the wording and because the question says 'the increase' in the
  singular. It is weaker because D01 explicitly says the $20M is in addition, and the actual $49.3M
  includes headquarters interest."
- Reading C: the $20M already inside the $40M -> +9.3, contradicted by "In addition".
- Interest income and Suvinil borrowing do not change the subtraction.
gaps: none; partial reading ranges listed.
contaminated: no (context included an unrelated git status listing aq-00949 file names; no answer, reasoning
or source hint)
