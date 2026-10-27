# q04 rev 0 - removal probe without Doc 5 (D04, CMA208 fake reviews guidance), 2026-10-08

Packet: runs/q04-r0-alt-k8/solver-1. It is a byte copy of the prepared solver-1 packet minus D04, with ids and header
lines renumbered D01-D10 (so CMA207 is D08 and the reviews short guide is D05 inside the probe) and a neutral run
name. A fresh blind-solver received the verbatim question plus the forced-guess instruction.

Raw return as received (harness indent removed):

answer: **The packet can't fully answer this.** The examples that the UK fake-review guidance gives of prohibited services are not in the packet. D08 sends readers elsewhere for them, and the full guidance D05 refers to is missing. The packet does contain the UK guidance's own list of the prohibited services offered to traders (D08, banned practice 13). Using that list, only the two fake-review services would expose the provider under the FTC rule as FTC staff read it:
(1) a service that writes or posts fake reviews for traders;
(2) a service that commissions or brokers (sells) fake reviews for traders.
Both fall under §465.2(a). Three other services would not, on their own:
- a service that writes or commissions reviews hiding that they were incentivised;
- a service that publishes reviews or review information in a misleading way;
- a service that only "facilitates" any of these.

**Forced best guess:** the same two fake-review services, and none of the others. Probability correct: about 0.35.

confidence: low

path:
1. The UK list of services is in D08 (text\D08.txt lines 561-573): "Offering services to traders to either: submit or commission fake reviews or reviews which hide the fact that they are incentivised / publish consumer reviews or consumer review information in a misleading way / or which facilitate any of those things." Line 573 then says "illustrative examples in relation to banned practice 13 are provided in separate guidance." D05 line 15 says the same: "further explained in the full fake reviews guidance where you can also find lots of examples." Neither source is in the packet.
2. D03 is the FTC staff interpretation. Line 11: "Here are FTC staff answers…"
3. Writing fake reviews is covered. D01 §465.2(a) (lines 132-147) makes it a violation "for a business to write, create, or sell a consumer review…that materially misrepresents" that the reviewer exists, that they used the product, or what their experience was. D03 lines 33-35 say agencies, review brokers and reputation-management companies "could be liable under Section 465.2(a) if they write, create, or sell a fake or false consumer review." D03 line 31 adds that "an individual in the business of selling or creating fake consumer reviews could be liable." **Result: yes.**
4. Commissioning fake reviews is covered. D03 line 63: "Brokers of fake reviews would generally fall under Section 465.2(a)'s prohibition against selling a consumer review, given that such brokers are generally being paid to provide fake reviews." **Result: yes.**
5. Hidden-incentive reviews are not covered by the rule itself:
   - D03 line 53: "The rule's only disclosure requirements relate to certain situations involving company insiders."
   - D03 line 143: "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment. But… failing to disclose incentives could be a violation of the FTC Act."
   - D03 lines 65-67: paying for honest reviews → "No."

   The §465.5 insider provisions bind the trader's own business and officers, not the provider. **Result: no, unless the incentive depends on the review being positive or negative (§465.4).**
6. Misleading publication is not covered for a provider:
   - §465.7(b) (D01 line 227) applies only to "a business" and to reviews "of…the products or services it sells."
   - §465.2(d)(2) exempts mere review hosting.
   - D03 line 71: no liability "assuming you didn't write or buy them." Line 267: "Organizing reviews is not suppressing reviews." Line 271: ordering reviews by rating — "the rule does not cover that situation." Line 275: selective use of positive reviews in marketing is not covered.

   **Result: no, as such.**
7. Bare facilitation is not covered. The rule has no facilitation provision. D03 line 35 limits intermediary liability to §§465.2(a), 465.4, 465.7(a) and 465.8. **Result: no, as such.**

minimal_documents: D08 and D03, plus D01 for the rule text of §465.7(b) and §465.2(d). D05 only confirms that the examples are missing. No document in the packet can replace the missing examples. D10 (line 126) lists breaches by intermediaries, but not services offered to traders.

readings:
- **Strict reading:** "illustrates" refers to the examples in the separate full fake-review guidance. On that reading the question is not answerable from this packet.
- **Broader reading:**
  - If the incentivised reviews being commissioned must be positive, the provider is liable under §465.4 (D03 lines 35 and 147), which adds the hidden-incentive service.
  - If "misleading publication" means removing reviews through threats, intimidation or false accusations, §465.7(a) applies.
- **Counting D08's two bullets plus facilitation as three services:** only the first bullet counts, and only its fake-review part.

gaps:
- The full UK fake-review guidance and its examples are missing. This is decisive.
- Read in full: D01, D03, D05, D06, D07, D08, D09, D10.
- D02 and D04 were checked by keyword search only. D04 has no match for "rule", "465" or "consumer reviews and testimonials".
- There are no layout files or PDFs. The docs\ version of D05 matches the text\ version.
- Files: D:\Agents\Docket\tasks\aq-01432\runs\q04-r0-alt-k8\solver-1\text\D08.txt, ...\text\D03.txt, ...\text\D01.txt, ...\text\D05.txt

contaminated: no. The session context included a git-status snapshot listing other tasks' files. It contained nothing about this question, and I opened none of those files. The forced guess does not draw on any outside knowledge of the missing guidance.

Caller adjudication: misses. Unforced: not fully answerable, because the guidance's examples are missing. Its
two-item answer and its forced guess (p 0.35) are generic classes built from CMA207's summary of banned practice 13
("writes or posts", "commissions or brokers"), not the three specific services of the gold. Doc 5 is needed.
