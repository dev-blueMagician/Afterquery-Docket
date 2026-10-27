# q02 rev 1 - removal probe without Doc 5 (D04, CMA208 fake reviews guidance), 2026-10-08

Packet: runs/q04-r0-alt-k8/solver-1. This bound probe run was built for q04, and q02 ticks the same two documents.
Before launch the caller verified it against q02 rev 1's prepared solver-1 packet: docs and text bodies are
byte-identical minus D04, with ids renumbered D01-D10. Only the packet's question.txt differs (q04's), which the read
guard does not let a solver open. A fresh blind-solver received q02's verbatim question plus the forced-guess
instruction.

Raw return as received (harness indent removed):

answer: Not answerable from this packet. The UK worked examples of traders commissioning reviews by offering people something are not in the packet. The US side is clear: FTC staff read § 465.4 as breached only when the incentive is expressly or impliedly conditioned on the review being positive (or negative). Without the UK examples, I can't say which ones meet that test.

Forced best guess (about 20–25% likely to be correct): the breaching examples are the UK examples where the reward (discount, refund, free product, cash, prize-draw entry) was offered for a positive or 5-star review, or for a negative review of a competitor. Examples that reward any review regardless of content, or that pay a customer to remove or change a negative review, would not breach. I can't name the specific examples because the source is missing.

confidence: medium. I'm confident the UK examples are absent. A second reading (below) gives "none".

path:
1. The UK guidance points elsewhere for the examples. D05 (UK fake-reviews short guide), line 15: "There are other things businesses must not do (such as writing or commissioning others to write fake reviews). These are further explained in the full fake reviews guidance where you can also find lots of examples." D08 (CMA207), line 573, on banned practice 13: "Explanation and illustrative examples in relation to banned practice 13 are provided in separate guidance." That full fake-reviews guidance is not among D01–D10.
2. The only UK incentive example in the packet is D05, line 33. It defines concealed incentivised reviews, "for example, not making it clear that a review has been written in exchange for money or other benefits, like a free stay at a hotel or another 'freebie'". It says nothing about sentiment and is about concealment.
3. The rule text, D01 § 465.4, bans incentives "in exchange for, or conditioned expressly or by implication on, the writing or creation of consumer reviews expressing a particular sentiment, whether positive or negative".
4. FTC staff reading (D03, staff Q&A):
   - Line 143: "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment."
   - Lines 145–147: paying incentives "for 5-star reviews", even with a disclosure, "would violate Section 465.4."
   - Line 155, implied condition: "Tell us how much you loved your visit to John's Steakhouse and get a $5 coupon" and "Tell your friends about all the fun you had at Jane's Arcade for a chance to win prizes."
   - Lines 157–159: an incentive for a review the business "merely expects to be positive" is "No" breach.
   - Lines 161–163 and 261–263: paying to "remove or change a review", or for taking down negative reviews, is not prohibited by the rule, though it may violate the FTC Act.
   - Lines 149–151: § 465.4 covers consumer reviews only, not hired influencers.
   - Lines 165–167: consumers who accept incentives are not liable.
5. Classification: a UK example would breach only if its offer is tied to sentiment as in fact 4. With no UK examples to enumerate, there is nothing to classify or count.

minimal_documents: D03 for the FTC staff test (D01 optional for the rule text). The UK source is missing; D05 and D08 only show that it exists. For reading B, D05 + D03 are enough.

readings:
- A (primary): the question means the worked examples in the full UK fake-reviews guidance. Not answerable here.
- B: the UK examples are D05's parenthetical incentives (money, a free hotel stay, another "freebie" given for a review). Answer: none. Nothing ties those incentives to sentiment, and FTC staff say incentives are allowed without an express or implied sentiment requirement (D03 lines 143, 157–159). Concealment may still breach the FTC Act, but not § 465.4. This reading is weak: D05 never presents these as traders commissioning reviews from customers or other consumers.

gaps:
- The full UK fake-reviews guidance (D05 line 15; D08 line 573) is not in the packet.
- Read fully: D01, D03, D05, D06, D07, D09, D10.
- D08: read lines 480–640 and banned practices 23–27, the footnote lines on reviews (1453, 1813), and searched it for review, rating, endorse, testimonial and star terms.
- D04: read only lines 480–544. It is pre-rule Endorsement Guides material, not a reading of the rule.
- D02: searched only.
- All of D01–D10 were searched for UK, CMA, trader, DMCC, incentive, freebie, voucher, prize draw and 5-star or positive-review terms. D02 and D04 have no UK content. No extraction problems; all documents are text, with no PDFs.

contaminated: no. I didn't read question.txt, notes or other packets. The harness auto-attached a workspace git status listing file names from another task (aq-00949). It contained nothing about this question or its answer, and no project instruction content was visible. I couldn't confirm whether the omitClaudeMd invocation was used.

Packet path: D:\Agents\Docket\tasks\aq-01432\runs\q04-r0-alt-k8\solver-1\text\ (D03.txt, D01.txt, D05.txt, D08.txt are the key files)

Caller adjudication: misses. Unforced: not answerable, because the UK examples are absent. The forced guess (p
0.20-0.25) is a generic description that names no example, so it is not the gold. Doc 5 is needed.
