# q02 rev 0 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-06

Raw return as received:

answer: Three of the UK examples — examples 1, 3 and 5 in CMA208's "Commissioning fake reviews or concealed incentivised reviews" list:
- Example 1: offering an existing customer a free or discounted product in exchange for a five-star review of a previous purchase.
- Example 3: sharing a social media post asking for five-star reviews in exchange for free products.
- Example 5: asking consumers to buy items with their own money and promising to reimburse them once they have submitted a positive review.
Not breaches: Example 2 (review of a free/discounted product without a disclosure instruction: no sentiment condition, at most an FTC Act disclosure issue); Example 4 (refund or gift card to change a negative review: FTC staff say the rule does not prohibit this); Example 6 (buying bot-generated reviews: not an offer to customers or consumers; under the US rule a fake-review matter, §465.2, not a sentiment-tied incentive).

verdict: clear

shortest_path:
1. D04 (CMA208) section 3 list "Commissioning fake reviews or concealed incentivised reviews", examples 1–6 (text/D04.txt L285–301); checked against the docs/ copy: same six items, nothing lost in extraction.
2. D03 (FTC staff Q&A), §465.4 heading: "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment." → rules out example 2 (staff also say merely expecting a positive review is not a violation). "Can my business pay incentives for 5-star reviews … so long as we ask the reviewers to add a disclosure…? No. That conduct would violate Section 465.4." → examples 1 and 3. "you can't suggest to consumers that their reviews must be positive (or negative) in order to obtain a promised incentive" → example 5 states the condition outright, breach. "Does the rule prohibit my business from offering compensation to a consumer to remove or change a review? No, but … may violate the FTC Act"; the §465.7 Q&A agrees ("Does the rule prohibit offering incentives to consumers for taking take down their negative reviews? No") → rules out example 4.
3. D01 §465.4 optional confirmation ("compensation or other incentives in exchange for, or conditioned expressly or by implication on, the writing or creation of consumer reviews expressing a particular sentiment"); §465.1(d) consumer reviews include ratings, so five-star ratings count; §465.1(m) lists products, discounts and money as things of value.

sufficient_documents: D04 + D03. D01 confirms but is not needed. D05 (Endorsement Guides FAQ) cannot replace D03 (never mentions the rule; its advice on changing negative reviews is about the Guides). No single document links the UK examples to the US rule: D04 and D06 never mention the FTC, D03 never mentions the UK.

searches: literal terms five-star, 5-star, reimburs, gift card, refund, 465.4, "particular sentiment", "Rule on the Use", rule/Part 465 in D05, FTC/US/CMA208 cross-references; concept terms commission, incentivis/incentiviz, fake review, review. Read in full: D01, D03, D04, D06. Read in part: D09 banned practice 13 section (points to separate guidance, no examples). Searched only: D02, D05, D07, D08, D10, D11 (no competing list of UK commissioning examples; D08 no review content).

readings/gaps:
- Rule text without D03: a reader using D01 and D04 alone could count example 4 as sentiment-tied (paying to strip negative commentary arguably conditions the incentive on sentiment) → 1, 3, 4, 5. Rejected because the question asks for the FTC staff reading and D03 explicitly says the conduct is not prohibited.
- Scope: a narrow or broad reading of "offering … something" only changes whether examples 2 and 6 are in the set; neither is a breach either way, so the answer holds.
- Difficulty risk: examples 1, 3 and 5 can be found by keyword ("five-star", "positive"); the only answer-separating step is excluding example 4, which needs D03's explicit answer — legitimate cross-document reasoning, not a single-document shortcut.
- Gaps: D02, D05, D07, D10, D11 searched but not read in full. No contamination: question.txt, notes and other packets not read.
