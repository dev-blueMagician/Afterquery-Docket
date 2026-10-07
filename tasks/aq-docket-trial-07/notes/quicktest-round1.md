# Quick-test batch, round 1 (2026-10-06)

Target: medium (user: "set target difficulty as at least Medium"; one submission attempt).
A quick test is one low-model answer. "Survived" means that one attempt missed; it is a good sign, not
a tier pass (Medium needs the low model to miss all 5 attempts of the difficulty check and the medium
model to get 1-3 of 5). "Too easy" rules a sketch out for Medium. Paste each question and short answer
into a sketch slot as written; please send back each verdict line and the low model's answer as shown.

Local status (all local solvers are Opus, stronger than the platform's low model; they check fairness,
not difficulty): S1 is q01 rev 1 (rev 0 had two fresh blind matches, a closed-book miss, a clear audit, removal
probes showing both documents needed, and a review that found the gold and fairness sound; rev 1
changed only one phrase and the evidence quotes, and is being re-checked). S2 and S3 each had one fresh
blind solve that matched and one closed-book miss. S4 was recomputed by script only.

## S1 (q01) nondurable low month, then two changes

Question:
Measured from the month in which seasonally adjusted Midwest nondurable goods manufacturing employment hit its lowest level between January 1990 and December 2019, what were the percentage changes to December 2019 in that employment and in seasonally adjusted U.S. rail transportation employment, in that order? Give each to one decimal place with its sign.

Gold answer:
+10.4% and -8.6%

Why it may be missed: the nondurable series bottoms in March 2010 (1,318.5 thousand), 0.8 below the
January and February 2010 values. The Midwest article's nondurable passage measures the recovery from
June 2009, the business-cycle trough (wrong route: +9.4% and -10.2%), and its "bottomed out in
February 2010" sentence is about all manufacturing (wrong route: rail -8.3%). Fair: the question asks
for the series' own lowest month, which the monthly figures settle uniquely.

## S2 (i02) post-recession high month, then Class I composition

Question:
From the month in which seasonally adjusted Midwest manufacturing employment reached its highest level after the Great Recession, through December 2019, what percentage of the net decline in Class I railroad employment came from train-and-engine jobs? Give one decimal place.

Gold answer:
53.9%

Why it may be missed: the post-2010 high is February 2019 (4,128.8 thousand), 1.5 above March 2019;
the Class I share must be built from six occupational columns in two months (7,715 of 14,314). Wrong
routes: March 2019 start 56.0%; January 2019 55.8%; the rail article's "46 percent" covers November
2018-December 2020.

## S3 (i06) riskier: total-manufacturing low month against the article's own sentence

Question:
In the month in which seasonally adjusted Midwest manufacturing employment reached its lowest level of January 1990 to December 2019, how many people, in thousands, were employed in U.S. rail transportation (seasonally adjusted)?

Gold answer:
178.7 thousand

Why it may be missed: the Midwest article says manufacturing "bottomed out in February 2010" (rail
178.2), but its own monthly chart is lowest in December 2009 (3,528.4 vs 3,530.2). Risk: this rests on
a prose-chart conflict inside the article; the local blind solver listed the February 2010 route as a
reading, so the platform could see two defensible answers. Quick-test only to measure the decoy's pull;
not recommended for the single submission unless the user accepts that risk.

## S4 (i04, optional) first joint monthly rise after the recession

Question:
Starting with July 2009, the month after the Great Recession ended, what was the first month in which both seasonally adjusted U.S. rail transportation employment and seasonally adjusted Midwest durable goods manufacturing employment rose from the previous month?

Gold answer:
December 2009

Why it may be missed: twelve monthly differences across two articles; using total manufacturing gives
February 2010, using nondurable goods gives April 2010. Predicted too easy; included only as a data
point if a slot is spare.
