# aq-04874 - cross-document hooks

Target: medium (user, 2026-10-14: "there is no slot for Easy Tier for this bundle, we should target medium and
high"). Page at capture 12:17: Hard 0/5 · Medium 0/1 · Easy 1/0, "Still open on this set: Hard, Medium"; quick
tests 0 of 15; difficulty runs 15 of 15. Medium has one slot and runs on 2026-10-14 started at the High level on
other bundles, so every design is audited against the medium and the high solver.

Structural finding (caller's full read): no document cites, amends, forecasts or restates another; the four RBA
texts share themes and data sources only; Doc 5 (NCC) shares only the housing-supply theme. Cross-document
answers therefore come from one document's rule/method applied to a case only another document supplies, or
from the same measure in two documents for different periods/populations. Earlier captures: none (new bundle).

Page Doc numbers are used below (Doc 1 = D02, Doc 2 = D05, Doc 3 = D01, Doc 4 = D03, Doc 5 = D04).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 1 l.1114 super counted only if head over 40, vested linearly until 60; Doc 4 l.206-207 median investor age 45 (1999/2000) -> 51 (2022/23) | share of super the stress test counts for a household headed at the 2022/23 median investor age: (51-40)/20 = 55% | Calculate across documents; applying a rule | 1999/2000 age gives 25% | both steps pointed by the question's words (0 unpointed); household head vs individual investor | investigate as a fallback only |
| h2 | Doc 1 fn 24/30, l.1040, Table 4 (LVR > 90 default, LMI > 80, foreclosure 10%, housing -40%); Doc 2 l.294-299 deposits 20% / 5% | LVR or debt-at-risk of a loan made at the survey's deposit after the scenario's price fall (95/60 = 158.3%; baseline 80% loan uninsured, 35% of loan at risk) | Applying the rule | LMI wrongly applied at exactly 80% LVR; 40-ppt subtraction (135%) | US survey case under an Australian stress test is contrived; Fuster-Zafar 20%/5% deposits are recallable (delete-and-guess on Doc 2 likely reaches gold) | reject unless a non-recallable Doc 2 input replaces the deposit |
| h3 | Doc 2 fn 14 SIH biennial 2003/04-2019/20 without 2007/08; Doc 1 l.1270 waves 2003-04/2009-10/2015-16; Doc 3 l.75 tax sample 2006/07-2018/19 | counts of survey waves shared or not shared between studies (e.g. 8 - 3 = 5) | Temporal alignment; aggregation | 2007/08 counted gives one more | asks about the studies' data rather than the world (rule 10 advisory); the omission sits in the footnote of the sentence a lookup reaches | reject |
| h4 | Doc 2 l.1025 Spain/Switzerland highest/lowest OECD home ownership; Doc 1 Table A2 (Spain (a) not in narrow regression; Switzerland from 1999), l.959 Spain -37% prices | country bridge then a lookup (e.g. 37 - 20 = 17 ppt; Switzerland sample start 1999) | Who belongs where | Spain/Switzerland swap | bridge named by the question (pointed); trivia; flattened Table A2 is a surface obstacle only | reject |
| h5 | Doc 4 l.100-101 70% one property, multi-owners hold ~half of properties, 2.3m investors, ~20% of dwelling stock; Doc 5 l.56 Accord 1.2m homes | Accord target as a share of the implied dwelling stock (3.22m / 0.2 = 16.1m; 7.5%) | Calculate across documents | not applicable | product of "around" figures the documents never connect | reject |
| h6 | Doc 3 l.248 $850 a month (Apr 2022-Jan 2024); Doc 4 Appendix A loan = interest / rate x 100, Table 1 $224,000 | implied rate rise on a median loan (10,200 / 224,000 = 4.55 ppt) | Calculate across documents | not applicable | two populations and periods the documents never connect | reject |
| h7 | Doc 2 l.631-633 before-tax 5.5% / after-tax 3.6%, zero response at rho = after-tax rate; Doc 4 l.748 owner-occupier interest non-deductible in Australia | discount rate with zero WTP response for an Australian owner-occupier: 5.5% | Applying the right rule | 3.6% (US deduction kept) | Australian non-deductibility is general knowledge; Doc 2 itself names the US deduction difference (l.972); gold printed in Doc 2 | reject |
| h8 | Doc 2 l.184 Michigan US$140,000 home, l.299 5% minimum down payment; Doc 1 l.959 housing -40%, l.1040 foreclosure 10% of loan, fn 30 LMI | lender loss before insurance US$62,300 (author A i02); baseline 20% deposit gives US$39,200 with LMI excluded at exactly 80% LVR | Applying the rule | US$49,000 (foreclosure costs forgotten) | US survey case under an Australian stress test: numbers never connected; 0 unpointed | reject |
| h9 | Doc 3 Table A.1 windows; Doc 1 Table 4 investment income -30, lending rates 0 | number of windows keeping a mortgaged landlord's year: 1 (author B i02) | Applying the rule | 2 (medium window misread) | delete-and-guess fails on Doc 1 (any shock from -10 to -50 gives 1); non-mortgagor note conflicts with the main text (l.180) | reject |
| h10 | Doc 1's 2003-04 exemption (l.1272) bonuses/overtime not shocked, HPL; Doc 2 l.974 72% home ownership in 2003/04 | year bridge into the exemption | Applying the rule | Table 4's -50 | a genuine unpointed exception, but the bridge fails delete-and-guess (2003-04 is Doc 1's own earliest wave); no second-document input changes the answer | reject |
| h11 | Doc 4 Table 1 $1,054,000 vs prose "$1 million"; Doc 1 foreclosure 10% of loan | foreclosure cost on that debt $105,400 vs lazy $100,000 | Exact table vs rounded prose | $100,000 | 10% foreclosure cost is a standard assumption a solver may guess (delete-and-guess on Doc 1); debt and loan conflated | reject |
| h12 | Doc 4 Graph 5 vs endnote 13 quintile bases; Doc 3 Table A.4 base + interaction ($28.90 vs prose $25); Doc 4 "20 per cent of leveraged investors" (l.459) vs "of investors" (l.655) | strong levers inside one document only | not applicable | not applicable | no second document contributes | reject (single-document) |
| h13 | Doc 5 (NCC) figures: 1.2m homes, $185, $306m vs $1.3b, Victoria 115 -> 60 variations | no numeric link to Docs 1-4 | not applicable | not applicable | any pairing multiplies figures no document connects | reject |

Search coverage: the caller's full read plus two independent question-author agents (2026-10-14), each reading all
five texts in full (author A starting from Doc 1/Doc 2, author B from Doc 3/Doc 4/Doc 5). All three found no fair
design with an unpointed step and named h1 as the best fair design.
