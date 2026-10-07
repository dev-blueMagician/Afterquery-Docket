# q02 rev 1 - blind solver A (fresh blind-solver subagent, packet solver-1), 2026-10-07

Raw return as received:

answer: Three of the six UK examples would breach the rule — Example 1 (offering an existing customer a free or discounted product in exchange for a five-star review of their previous purchase), Example 3 (sharing a social media post asking for five-star reviews in exchange for free products), Example 5 (asking consumers to buy items with their own money and telling them they will be reimbursed once they have submitted a positive review). Two others in the "offering something" set do not breach the rule as FTC staff read it: example 2 (a review of a free or discounted product without telling the reviewer to disclose it) and example 4 (a refund or gift card for changing a negative review).

confidence: high

path:
1. UK examples: D04 (CMA208, 4 April 2025) "Commissioning fake reviews or concealed incentivised reviews" (text/D04.txt L285–301; docs/ L389–405): (1) five-star review for a free or discounted product (not reflective of genuine experience); (2) review of a free or discounted product without making clear the incentive must be disclosed; (3) social media post asking for five-star reviews for free products; (4) refund and/or gift card to change a negative review; (5) reimbursement once a positive review is submitted; (6) buying bot-generated reviews. Example 6 left out (offers customers or consumers nothing) → examples 1–5.
2. Rule: D01 § 465.4 (L185) "compensation or other incentives in exchange for, or conditioned expressly or by implication on, the writing or creation of consumer reviews expressing a particular sentiment, whether positive or negative"; definition L101 consumer reviews "include consumer ratings".
3. FTC staff (D03, November 2024): L143 no prohibition absent an express or implied sentiment requirement (non-disclosure an FTC Act issue); L145–147 5-star incentives even with disclosure "No. That conduct would violate Section 465.4… applies whether the reviews appear on your website or third-party review platforms"; L155 implied positivity; L159 merely expecting a positive review is not a violation; L161–163 compensation to remove or change a review "No, but paying consumers to change or remove truthful negative reviews may violate the FTC Act…"; L261–263 same for incentives to take down negative reviews.
4. Classification: 1 and 3 five-star condition → breach ("not reflective of their genuine experience" irrelevant, § 465.4 does not require falsity); 5 express positive condition → breach; 2 no sentiment condition (FTC Act disclosure issue) → no breach; 4 compensation to change or remove → no breach.

minimal_documents: D04 + D03 (D01 confirms). No replacement: D06, D10, D11 lack the examples; D09 L573 "provided in separate guidance"; D05 (Endorsement Guides staff guidance, L523–526 similar) would not replace D03; D02, D05, D07, D11 have no § 465 reference.

readings: rule text without staff gloss → 1, 3, 4, 5 (excluded by the staff reading the question asks for); wider candidate set (example 6, ¶3.7 incentives, fn8 prize draw) adds no breach; example 3 as social media posts rather than review-platform ratings might fall outside the definition, but "five-star" points to ratings.

gaps: none material (staff Q&A "isn't definitive or comprehensive", D03 L13; D01, D03, D04, D06 read in full; D05, D09 in part; D02, D07, D08, D10, D11 keyword searches; text sources, no PDF pages).

contaminated: no — git status file names only; no notes or question files opened.
