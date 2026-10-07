# q02 rev 0 - removal probe without D04 (CMA208 fake reviews guidance, platform Doc 5), 2026-10-06

Packet: runs/q02-r0-probe-h8/solver-1 (byte copy of solver-1 minus D04, ids renumbered D01-D10; inside
the probe the short reviews guide is D05, D09 is D08, etc.; neutral run name). Fresh blind-solver;
question verbatim plus the forced-guess instruction.

Raw return as received:

I located the US side but not the UK examples the question appears to describe, so "none" is a forced best guess.

answer: None. The only UK fake-review guidance in the packet gives one example list, a review written "in exchange for money or other benefits, like a free stay at a hotel or another 'freebie'"; none is tied to the review being positive or negative, so none would breach § 465.4 as FTC staff read it. Forced best guess; probability it matches the intended answer 0.4.

confidence: low

path:
1. The UK fake-review guidance in the packet is D05 (probe numbering; gov.uk "fake-reviews" publication). D05 L33: "concealed incentivised reviews: these are reviews that conceal the fact that they have been incentivised (for example, not making it clear that a review has been written in exchange for money or other benefits, like a free stay at a hotel or another 'freebie')" → candidates money, a free hotel stay, another freebie; none names a required rating or tone.
2. D05 L15 says the commissioning examples are elsewhere: "There are other things businesses must not do (such as writing or commissioning others to write fake reviews). These are further explained in the full fake reviews guidance where you can also find lots of examples." D08 (CMA207, probe numbering) L573 says the same for Banned Practice 13 ("... provided in separate guidance"). That full guidance is not in the packet.
3. US ban: D01 § 465.4 (L185).
4. FTC staff reading (D03): L143 no prohibition absent an express or implied sentiment requirement; L147 5-star incentives violate § 465.4 even with disclosure; L155 implied positivity also breaches (John's Steakhouse $5 coupon); L159 merely expecting a positive review does not; L163 and L263 paying to remove or change a review, or to take down negative reviews, not prohibited by the rule.
5. Applying 4 to 1: money, a free hotel stay and a freebie carry no sentiment condition → none breaches (the UK problem is concealment, an FTC Act matter in the US).
6. D04 (probe numbering; FTC Endorsement Guides FAQ) L526 consistent: "You can't condition an incentive – for example, a discount – on a review being positive".

minimal_documents: D05 + D03 (probe numbering); D01 supporting; D08 confirms the examples are in separate guidance. D01 cannot replace D03 because the question asks for the staff reading.

readings:
- Intended source outside the packet: the wording suggests a list of examples from the full CMA fake-review guidance; on D03's tests an example breaches if the incentive depends on a positive/5-star (or negative) review and does not if it rewards any review, is merely expected to be positive, or pays to remove/change a negative review — cannot name which examples qualify without that document.
- D06's incentive list (content-creator guidance) also gives none; hired-influencer posts are testimonials outside § 465.4 (D03 L149–151).
- D08 Banned Practice 12 example (influencer "gifted a free holiday"): none, same reasons.

gaps: the full UK fake-review guidance with the commissioning examples is missing (decisive). Read in full: D03, D05, D06, D07, D09, D10; in part plus searches: D01 L60–234, D04 L483–542, D08 L1–30, L490–630, L1805–1819; searched only: D02. question.txt not read.

contaminated: no

Caller adjudication: not answerable; forced guess "None" (p 0.4) differs from the gold → D04 needed.
