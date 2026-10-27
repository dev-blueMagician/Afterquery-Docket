# Removal probe: Doc 5 (D03) left out

- Date: 2026-10-08
- Role: fresh blind-solver (non-fork, omitClaudeMd), packet tasks/aq-01547/runs/q01-r0-alt-m4/solver-1 (six documents renumbered D01-D06; D03 withheld)
- Question: verbatim q01 rev 0
- Unforced answer: Walden-Bing. Forced guess: Walden-Bing, p 0.85.
- Result: misses (gold "Walden-Bing and Wonneman" not reached)

## Raw return (verbatim)

answer: Walden-Bing. She is the only whistleblower who qualifies.
Forced best guess: Walden-Bing, with probability 0.85 that this guess is correct.

confidence: high

path:
1. Time window. All six rulings fall between July 1 and September 30, 2026, so the date filter removes none of them:
   - D05 (S.D. Tex.): "ENTERED July 20, 2026"
   - D04 (D. Md.): "Dated: September 2, 2026"
   - D06 (D. Vt.): "Filed 09/10/26"
   - D02 (9th Cir.): "Filed September 24, 2026"
   - D03 (N.D. Ga.): "Filed 09/29/26"
   - D01 (D. Alaska): "Filed 09/30/26"
2. Walden-Bing qualifies (D05, Walden-Bing v. Horne, LLP et al., Background, pp. 1-3).
   - Employment: "Walden-Bing was employed by Horne as a Quality Assurance/Quality Control Specialist."
   - Reports while employed: "She reported her concerns to management and human resources ... Meanwhile, Walden-Bing made reports to the Office of Inspector General, the Securities and Exchange Commission, and the U.S. Department of Labor."
   - Sequence: "Walden-Bing was terminated around September 2, 2022 ... Two months later, she 'communicated' with the Office of Inspector General regarding her concerns and termination." The OIG/SEC/DOL reports come before the termination, separately from the later OIG contact.
   - Later suit: she "originally filed this case as a qui tam action ... naming four defendants: Horne, Deloitte, ..." "Dkt. 1 (filed May 8, 2023)." The order also lets her add FCA and NDAA retaliation claims against Horne.
   - The SEC and the U.S. Department of Labor are federal, so she qualifies even though the OIG is not named.
3. The other five are excluded:
   - D04, De Simone: he did go to federal agencies (FTC on Nov 7 and Dec 1, 2016 and in Feb/May 2017; HHS and DOJ in July 2020 and Aug 2021). But all of this came after "In November 2014, Professor De Simone resigned from VSL." So it was not while employed.
   - D06, Adler: he is a "former TSC employee" (Jan 2016 to Dec 2019). The concerns described went to CEO Perry Sporn inside the company: a June 2016 meeting, emails on June 28 and July 4, 2018, a talk on July 8, 2018, and a meeting on March 18, 2019. His only federal link is that he "seeks to recover a portion of the CBP's $172,845.00 settlement payment under 19 U.S.C. § 1619," which pays someone who "furnishes ... original information." No date is given. The DOJ referral and the CBP settlement (Oct 11, 2023) came after he left TSC. Nothing shows he reported to federal authorities while employed.
   - D03, Ghattas: he "sues his former employer," OrthoAtlanta, but his complaints were internal only, to the Executive Committee. The court lists "reports to the Government" as a type of conduct he did not allege.
   - D01, Feduccia: he is a relator, but the order says nothing about him working for I.C.E. or reporting before suit.
   - D02, Ling: she sued the City of Los Angeles, which is not a company, and no employment is stated.

minimal_documents: D05 alone establishes the answer. D01–D04 and D06 are needed only to confirm that nobody else qualifies. No other document could stand in for D05.

readings:
- Counting only clearly federal bodies (ignoring the unnamed OIG): still Walden-Bing, through the SEC and DOL.
- Counting any federal informant role whatever its timing: this would add Adler (the § 1619 CBP claim). The documents give no date and suggest it came after he left, so I reject it. Answer under this reading: Walden-Bing, Adler.
- Reading "Meanwhile" as not fixing the reports before her termination: Walden-Bing's timing becomes uncertain and the answer would be "cannot be determined." I reject this because the text separates the pre-termination reports from the later contact ("Two months later").

gaps:
- The OIG is not named, so I can't say which agency it was.
- D06 gives no date for Adler's disclosure to CBP or for his original filing in the Southern District of New York.
- D04 does not say what De Simone's role at VSL was. This doesn't change the result.
- The packet holds text extractions only (manifest method "text", pages null), so there were no PDF pages to check. I read text/D01–D06 in full. I did not read the docs/ files separately, since text/ is their extraction. I did not read question.txt, as instructed.

contaminated: no. The environment's git-status snapshot listed unrelated workspace paths from another task (aq-00949) but nothing about this question or its answer.

Note (caller): probe ids map D01 = D01, D02 = D02, D03 = D04, D04 = D05, D05 = D06, D06 = D07 of the bundle.
