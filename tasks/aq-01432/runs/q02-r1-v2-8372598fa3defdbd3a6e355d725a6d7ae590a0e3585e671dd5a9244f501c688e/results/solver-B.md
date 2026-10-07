# q02 rev 1 - blind solver B (fresh blind-solver subagent, packet solver-2), 2026-10-07

Raw return as received:

answer: Three of the UK examples would breach it — Example 1 (offering an existing customer a free or discounted product in exchange for a five-star review), Example 3 (posting on social media asking for five-star reviews in exchange for free products) and Example 5 (asking consumers to buy items with their own money and promising to reimburse them once they post a positive review). Examples 2 and 4 would not breach the sentiment ban; Example 6 is outside the question's scope.

confidence: high

path:
1. UK examples (D04, CMA208 chapter 3 "Commissioning fake reviews or concealed incentivised reviews", D04.txt L285–301): 1 free or discounted product for a five-star review (not reflective of genuine experience) of a previous purchase; 2 review of a free or discounted product without making clear the incentive must be disclosed; 3 social media post asking for five-star reviews in exchange for free products; 4 refund and/or gift card if a negative review is changed to remove the negative commentary; 5 buy with own money, reimbursed once a positive review is submitted; 6 buying bot-generated reviews. 1–5 offer something to customers or consumers; 6 does not (left out).
2. Rule (D01 § 465.4, L185): bans "compensation or other incentives in exchange for, or conditioned expressly or by implication on, the writing or creation of consumer reviews expressing a particular sentiment, whether positive or negative."
3. FTC staff (D03 § 465.4 Q&A): L143 "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment. But remember that failing to disclose incentives could be a violation of the FTC Act"; L147 5-star incentives "No. That conduct would violate Section 465.4"; L155 "you can't suggest to consumers that their reviews must be positive (or negative) in order to obtain a promised incentive"; L163 compensation to remove or change a review "No, but paying consumers to change or remove truthful negative reviews may violate the FTC Act"; § 465.7 section L263 incentives to take down negative reviews "No, but offering such incentives could be an unfair practice in violation of the FTC Act".
4. Classification: 1 breach (five-star; genuineness irrelevant under § 465.4); 3 breach; 5 breach (money expressly conditioned on a positive review); 2 no breach (non-disclosure is an FTC Act matter); 4 no breach (staff: not prohibited by the rule).

minimal_documents: D04 + D03 (D01 supporting). No replacements: D05 covers the Endorsement Guides under the FTC Act and never mentions the rule; D06, D09, D10, D11 lack the commissioning examples.

readings:
- Rule text without the staff Q&A: example 4 as conditioned on a non-negative review → 1, 3, 4, 5; "as FTC staff read" points to D03, which rejects it.
- Weak: example 3 as social-media testimonials (D03: § 465.4 "only applies to consumer reviews", not hired influencers) → 1 and 5; rejected because five-star ratings from the public are consumer reviews (D01 § 465.1(d)).
- Other UK lists (D04 2.10, fn8 prize draws) add nothing (none tied to sentiment).

gaps: read in full D01, D03, D04, D06; D05 L470–559 plus searches; D09 L505–579 plus searches; D02, D07, D08, D10, D11 searched only; D04 text-only (line numbers); question.txt not opened.

contaminated: no
