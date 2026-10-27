# aq-06789 - cross-document hooks

Caller inventory, 2026-10-18 (Claude Opus 5.5, after reading all nine text files and notes/mine.md).
Target hard (user, 2026-10-18: "there is no slot for Easy or Medium Tier for this bundle, we should
target high"). Repeat of aq-01188 (Medium target, 10-05/06; q01 rev 1 never reached the platform);
its hooks h1-h15 (`tasks/aq-01188/notes/hooks.md`) were re-read against the playbook here.

Mine result: section 1 is boilerplate (contact paragraphs, methodology sentences); sections 3-5 hold no
restatement, cumulative period or shared row; the only figures printed in two documents with the same
meaning are NFIP's $250,000 / $100,000 limits and the 3.3 percent WYO allowance (D02, D09; scratch
script shared_numbers.py). The nine products share entities (NFIP, four or five bank regulators, NAIC,
hurricanes) but almost no quantities.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D09 L185, fn 21 L311 Katrina over $15.7B; L304 Katrina + Rita about $16.2B; L185 P-C about $22.4B excl. flood; D02 L96 about $12B since inception; L101 2004 storms over $1.3B | Katrina's NFIP payments less the program's whole history to Apr 2005 = $3.7B | Look-alike metric x2; Calculate across documents | 4.2 (Katrina + Rita), 10.4 (P-C), 14.4 (2004 storms) | lower bounds; D09 figures past the form's number window | i01 |
| h2 | D02 L67/L119/L170 about 40 FEMA + about 170 contractors; D09 L187 about 68 + about 170 (Sep 2007); D02 fn 1 about 2,500 FEMA staff (Mar 2003) | FEMA's own NFIP staff growth = 70% | Look-alike metric x2 | 13.3% (with contractors) | "about" counts; number window | i02 |
| h3 | D02 L172, fn 7 about 95% WYO, other 5% direct; D09 L153 about 96% | Non-WYO share change, -1 point or -20% | Calculate across documents | +1.05% (WYO share) | a relative change of rounded complements is precision the inputs do not carry | drop |
| h4 | D02 L101 2004 storms; L99 Isabel; D09 L304 averages over $95,000 / $47,000 "respectively" | Average payment ratios between storms | Who belongs where (respectively) | Katrina/Rita swap | per-claim averages mix closed-claim payments with all claims (L101) and "filed ... for" amounts (L99); lower bounds | drop |
| h5 | D02 L190 4 years experience for NFIP certification; D09 L239, L261 Louisiana had no adjuster licensing | Experience needed to adjust NFIP claims in Louisiana | Exception in parallel rules | 0 (state rule) | D02 alone answers; D09 only holds the decoy (fails necessity) | drop |
| h6 | D07 Figure 1 L177-419, MA sentence L421, "at least 4" L175, LA fn 19 L546 | States phasing in / first-year shortfalls (18 vs 17) | Footnotes and prose change the table; Summary vs detail | figure-only count | single document: no partner fact anywhere in the bundle | drop |
| h7 | D04 L208-211 OCC 87/74 (fiscal, with inquiries) vs GAO 66/55 (calendar, complaints only) | Points missed against the 80% target | Look-alike metric; period mapping | 6 points (reported 74) | single document; "calendar year" lands on the settling sentence | drop |
| h8 | D04 L160-194 per-regulator outcome ranks; D03 L148 / D08 L164 regulator facts | One regulator's outcome ranking | Ordered answers; Who belongs where | pooled order (= OCC) | any D03/D08 selector is an unrelated hop (send-back pitfall 1); aq-01188 q01 rated easy | drop |
| h9 | D04 L268 Rita phone outage; D05 L173 Katrina vehicles; D09 Rita/Katrina claims | Event bridges between agencies | Who belongs where | - | contrived selectors; Rita average recalled (aq-01188 S5) | drop |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
