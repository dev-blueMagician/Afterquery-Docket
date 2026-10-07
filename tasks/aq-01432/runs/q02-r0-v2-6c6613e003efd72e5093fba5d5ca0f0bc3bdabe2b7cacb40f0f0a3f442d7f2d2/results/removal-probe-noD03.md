# q02 rev 0 - removal probe without D03 (FTC staff Q&A on the reviews rule, platform Doc 2), 2026-10-06

Packet: runs/q02-r0-probe-h8/solver-2 (byte copy of solver-1 minus D03, ids renumbered D01-D10; inside
the probe CMA208 is D03 and the Endorsement Guides FAQ is D04; neutral run name). Fresh blind-solver;
question verbatim plus the forced-guess instruction.

Raw return as received:

I located the five UK examples and the US rule text, but the packet has no FTC staff reading of the rule itself (the only FTC staff document, D04, is dated June 2023, before the rule). So the answer is a forced best guess (probability 0.6).

**answer:** Four of the five UK examples (CMA208's "Commissioning fake reviews or concealed incentivised reviews" list) would breach the ban:
- Example 1: offering an existing customer a free or discounted product in exchange for a five-star review.
- Example 3: a social media post asking for five-star reviews in exchange for free products.
- Example 4: offering a customer who left a negative review a refund and/or gift card if they change it to remove the negative commentary.
- Example 5: telling consumers they will be reimbursed once they submit a positive review.
Example 2 (a free or discounted product without telling the reviewer to disclose it) would not breach.

**confidence:** medium

**path:**
1. UK examples (D03 = CMA208, 4 April 2025, Chapter 3, text/D03.txt L285–301, probe numbering): (1)–(6) as listed; example 6 (bot-generated reviews) offers nothing to customers or consumers, leaving 1–5.
2. US ban (D01 §465.4, L182–185); §465.1(m) (L120) things of value include "money, gift certificates, products, services, discounts, coupons, contest entries…".
3. FTC staff gloss (D04, "Our staff guidance" L25, dated "June 2023" L705): L526 "You can't condition an incentive – for example, a discount – on a review being positive."; L528–529 inviting all customers to post honest reviews is fine, disclose anything of value; L483–491 free products for honest reviews need disclosure, not banned; L509 "asking them to change or delete their initial negative reviews could mislead readers."
4. Classification: 1 and 3 five-star condition → breach; 5 "positive review" express condition → breach; 4 refund/gift card expressly conditioned on removing negative commentary → treated as sentiment-tied, matching "can't condition an incentive… on a review being positive" → breach; 2 no sentiment condition → disclosure matter, no breach. The UK qualifier "not reflective of their genuine experience" is irrelevant to §465.4.

**minimal_documents:** D03 (CMA208) + D01 for 1, 3, 5; D04 for the staff gloss on 4 and 2. No substitutes (D05 and D08 only point to "the full fake reviews guidance").

**readings:**
- Narrower reading 1, 3, 5 (about 0.3): if "writing or creation… expressing a particular sentiment" excludes paying to edit or remove negative content (the edited review might be merely neutral; suppression or general deception rather than §465.4; §465.7(a) covers threats, intimidation and false accusations, not incentives).
- "Offer" vs "provide": §465.4 says "provide"; schemes treated as carried out.

**gaps:** no FTC staff interpretation of Part 465 itself in the packet; D04 predates the rule (89 FR 68077, Aug. 22, 2024), so staff's view of example 4 is inferred. Read in full: D01, D03, D04, D05 (probe numbering); D08 in part; D02, D06, D07, D09, D10 targeted searches only; text-only packet; question.txt not read.

**contaminated:** no — git status of workspace file names only.

Caller adjudication: not answerable as asked (no staff reading of the rule); forced guess adds the decoy
example 4 ({1, 3, 4, 5}, p 0.6) and differs from the gold → D03 needed. Gold set appears only as a 0.3
alternative reading.
