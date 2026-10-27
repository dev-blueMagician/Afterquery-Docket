# q04 rev 1 - removal probe without Doc 5 (D04, CMA208 fake reviews guidance), 2026-10-08

Packet: runs/q04-r0-alt-k8/solver-1 (bound probe run, reused). Before launch it was verified as rev 1's prepared
solver-1 packet minus D04, with identical question bytes and identical docs and text bodies under renumbered ids
D01-D10 (CMA207 is D08 and the reviews short guide is D05 inside the probe). A fresh blind-solver received the
verbatim question plus the forced-guess instruction.

Raw return as received (harness indent removed):

answer: Not answerable from this packet. The packet doesn't contain the examples of prohibited services offered to traders that the UK fake-review guidance gives. D08 only gives the statutory description and says the examples are "provided in separate guidance". D05 refers to "the full fake reviews guidance where you can also find lots of examples", but that document isn't included.
Answer if D08's three service categories stand in for the missing examples: only a service that **submits/writes or commissions (brokers/sells) fake reviews** would make the provider liable, under §465.2(a). The other three would not: services for concealed-incentive reviews, misleading publication of reviews, and pure facilitation.
Forced best guess: the gold list contains only the fake-review services (writing/posting fake reviews for traders, and commissioning/brokering fake reviews). It excludes concealed-incentive, misleading-publication/suppression and facilitation-only services. Probability of being correct: about 0.25.

confidence: high that the packet can't answer it as asked; low for the forced guess.

path:
1. D08 lines 561-571: "Offering services to traders to either: submit or commission fake reviews or reviews which hide the fact that they are incentivised / publish consumer reviews or consumer review information in a misleading way / or which facilitate any of those things." Line 573: "Explanation and illustrative examples in relation to banned practice 13 are provided in separate guidance." Line 1453 also points to separate fake-review guidance.
2. D05 line 15: "There are other things businesses must not do (such as writing or commissioning others to write fake reviews). These are further explained in the full fake reviews guidance where you can also find lots of examples." The rest of D05 covers only publishers' duties. Searches of text/ and docs/ for "services to traders", facilitat*, broker, swap, reputation/review management, review club/group, upvote and "trader" found no examples of these services. The docs/ files match text/ (method "text", no PDFs).
3. D01 (the FTC rule):
   - §465.2(a): "for a business to write, create, or sell a consumer review… that materially misrepresents… That the reviewer… exists… used or otherwise had experience… [or] experience."
   - §465.4: incentives "conditioned… on… consumer reviews expressing a particular sentiment."
   - §465.7(a): "anyone" using an "unfounded or groundless legal threat, a physical threat, intimidation, or a public false accusation" to prevent or remove a review.
   - §465.7(b): limited to "a business" and reviews of "products or services it sells" shown on "its website or platform."
   - §465.8(a): "Sell or distribute fake indicators of social media influence."
   - §465.1(a): "Business" includes "any other commercial entity that sells products or services", which covers service providers.
4. D03 (FTC staff Q&A):
   - Line 35: agencies, review brokers and reputation firms "could be liable under Section 465.2(a) if they write, create, or sell a fake or false consumer review…; …465.4 if they provide compensation… conditioned… [on] a particular sentiment…; …465.7(a) if they engage in review suppression or… 465.8."
   - Line 63: "Brokers of fake reviews would generally fall under Section 465.2(a)'s prohibition against selling a consumer review."
   - Line 31: someone "in the business of selling or creating fake consumer reviews could be liable."
   - Line 53: "The rule's only disclosure requirements relate to certain situations involving company insiders."
   - Line 67: incentives for honest reviews: "No."
   - Line 143: "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement… particular sentiment."
   - Lines 269-275: sorting reviews by rating and selective use in marketing are not covered by the rule.
5. Classification of the D08 categories:
   - Writing fake reviews: covered (§465.2(a)).
   - Commissioning/brokering fake reviews: covered (§465.2(a), "sell").
   - Concealed-incentive honest reviews: not covered (FTC Act only), unless the incentive depends on sentiment (§465.4).
   - Misleading publication: not covered for a third-party provider (§465.7(b) applies only to the seller's own site), unless suppression uses threats, intimidation or false public accusations (§465.7(a)).
   - Facilitation: not covered, since it isn't writing, creating or selling, unless it sells fake reviews or fake social-media metrics (§465.8).

minimal_documents: To show it can't be answered: D08 + D05. For the conditional classification: D08, D01, D03. D02, D04, D06, D07, D09 and D10 aren't needed and none could replace the missing guidance.

readings:
- (a) Treat D08's statutory list as the illustration: the answer is the "submit or commission fake reviews" service only.
- (b) If the missing examples include sentiment-conditioned incentive schemes, removing reviews through threats or false public accusations, or selling fake likes/followers, those would be added (§465.4, §465.7(a), §465.8).
- (c) Strict reading: not answerable.

gaps:
- The full CMA fake-reviews guidance and its examples are absent. That is a preparation gap, not an extraction problem.
- Read in full: D01, D03, D05, D06, D07, D09, D10.
- D08 read at lines 1-30, 480-640 and 1805-1819, plus searches.
- D04 read at lines 470-514, plus searches.
- D02 was only searched, with no hits.
- The D01 text of §465.2(a)-(b) is scrambled in extraction, but the meaning can be recovered.

contaminated: no. Nothing about this question leaked. The forced guess is general background inference (my own reasoning, not from the packet) and goes beyond the documents. Files: D:\Agents\Docket\tasks\aq-01432\runs\q04-r0-alt-k8\solver-1\text\D08.txt, D05.txt, D01.txt, D03.txt.

Caller adjudication: misses. Unforced: not answerable; the guidance's examples are missing. The forced guess (p
0.25) is generic classes drawn from CMA207's summary of banned practice 13, not the three specific services of the
gold. Doc 5 is needed.
