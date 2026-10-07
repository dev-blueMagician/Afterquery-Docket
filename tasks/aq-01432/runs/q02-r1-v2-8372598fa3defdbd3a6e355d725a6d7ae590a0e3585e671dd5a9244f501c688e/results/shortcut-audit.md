# q02 rev 1 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-07

Raw return as received:

answer: Three of the six CMA208 commissioning examples would breach §465.4 as FTC staff read it — Ex. 1 (free or discounted product for a five-star review of an earlier purchase), Ex. 3 (social media post asking for five-star reviews in exchange for free products), Ex. 5 (buy with own money, paid back once a positive review is posted). Not breaches: Ex. 2 (no sentiment tie; non-disclosure an FTC Act issue), Ex. 4 (refund or gift card to remove negative commentary; staff say the rule does not cover it), Ex. 6 (bot-generated reviews: nothing offered to customers or consumers; no sentiment condition).

verdict: clear

shortest_path:
1. D04 (CMA208, 4 Apr 2025) Ch. 3 box "Commissioning fake reviews or concealed incentivised reviews", items 1–6 (checked against docs/ L391–405).
2. D03 (FTC staff Q&A) §465.4 entries: "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment. But remember that failing to disclose incentives could be a violation of the FTC Act." (excludes Ex. 2); "Can my business pay incentives for 5-star reviews … so long as we ask the reviewers to add a disclosure…? No. That conduct would violate Section 465.4." (Ex. 1 and 3; Ex. 5 also fits "you can't suggest … reviews must be positive … to obtain a promised incentive"); "Does the rule prohibit my business from offering compensation to a consumer to remove or change a review? No, but paying consumers to change or remove truthful negative reviews may violate the FTC Act." (excludes Ex. 4; the §465.7 entry agrees).
3. D01 §465.4 text optional; §465.1(m) things of value include money, products, discounts (covers reimbursement).

sufficient_documents: D04 + D03 minimum; D01 cannot rule out Ex. 4 by itself; no single document is enough (UK examples only in D04; staff reading only in D03).

searches: 465.4, sentiment, five-star/5-star, reimburs, gift card, refund, commission, incentivis/incentiviz, in exchange for, discount, change/remove/take down review, rule, Part 465. Read in full D01, D03, D04, D06; in part D05 (L490–569), D09 (banned practice 13, defers to separate guidance); keyword only D02, D07, D08, D10, D11. Only D01 and D03 mention the Part 465 rule. question.txt not opened.

readings/gaps:
- Main trap: Ex. 4 looks sentiment-tied; a rule-text-only reading gives four examples; rejected (the question asks for the staff view; D03 excludes it).
- Alternative referent: "examples" read as CMA208 ¶2.10's list of commissioning forms (money, commissions, discounts/vouchers, leases or loans, freebies, free stays, event invitations) → "none" (none sentiment-tied); weaker — that list gives kinds of reward, not scenarios of traders making offers, and includes asking staff to write reviews.
- D05 (Endorsement Guides FAQ) says similar things under the Guides and FTC Act, not the rule; no effect.
- Difficulty risk, not a shortcut: D03 entries match the UK examples almost one-to-one; still a genuine cross-document join with a distractor.
- Contamination: git-status file names only. Extraction gaps: none that matter.
