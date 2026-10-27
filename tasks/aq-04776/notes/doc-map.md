# aq-04776 - document map

Maintained by the caller from `text/`. Navigation only: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: seven Federal Register texts on veterans' and disability programs (page title "Veterans Disability Benefit Rules"): two VA SSVF funding notices (FY2026, FY2027), DEA/HHS final rule on VA telemedicine prescribing, VA apportionment final rule, VA Title VI proposed rule, ACUS 2026 adopted recommendations, SSA ruling SSR 26-2p.
- Documents: 7; local ids D01-D07 equal the page's Doc 1-7 (alphabetical file order matches the page order).
- Gaps: none. Capture "7 of 7 read in full"; intake.json shows every document complete, matches_capture true. The capture carried a "Docket has been updated. Reload this page" note only.
- Extraction spot-checks: plain-text sources; D02 tables 1-12 present as flattened rows (checked Table 9 and Table 12 against prose figures); D05 amendment table flattened (checked against section-by-section text); footnotes inline in D02, D05, D06, D07 (checked D02 fn 66, D07 fn 47).
- Provenance: notes/intake.json (capture_sha256 dcb107b7...); source hashes per document recorded there.
- Coverage: all seven read in full by the caller on 2026-10-14.

## D01 - VA SSVF Notice of Funding Opportunity, FY 2026 (FR Doc 2024-30662, 89 FR 105178, Dec 26, 2024)

- Written by: Department of Veterans Affairs; approved by Denis McDonough Dec 16, 2024; signed for publication by Luvenia Potts.
- Round: grants fund operations beginning October 1, 2025; applications due 4 p.m. EST March 3, 2025 (DATES, IV.C).
- Funding: "approximately $799 million via this NOFO with over 200 awards, with a range of $118,000 to $22,942,240" (I, Funding Details, line 38).
- Priorities (I.B and II.B): P1 new for FY 2026, Tribal and rural communities and U.S. territories, new and existing applicants, up to 3-year project period, 29 Tribal communities with Tribal HUD-VASH, five territories named; P2 accredited existing grantees (CARF 3-yr, COA 4-yr, Joint Commission 3-yr), 3-year; P3 other existing grantees with annual awards, renewal application. Existing grantees = MOA through Sept 30, 2025. 3-year grantees not ending by Sept 30, 2025 submit an LOI with CoC letter and FY 2026 budget.
- Definitions/resources (I.C): 2 months' rent to landlords under 62.34(g) for lease of at least 1 year; up to $1,000 move-in under 62.34(g); internet as utility; EHA clarifications. Prints 38 CFR 62.11(b)-(c) text (I.D, lines 74-78), incl. "exiting an institution where the Veteran family resided for 90 days or less".
- Income: current threshold 50% AMI; "up to 80% of AMI" for this NOFO (I.D).
- CoC letter: P2/P3 without a CoC letter "may limit the maximum award to 90%" (I.D) / "eligible for renewal funding at a level no greater than 90% of their previous award" (II.C.6); exception route for LOI grantees whose CoC by policy gives no letters.
- Requirements (I.F): admin max 10%; enroll at least 60% literally homeless (waiver floor 40%, V.B.4.a); TFA list; $1,000; 2 months' rent, payable at lease-up or within first 90 days.
- Allocation (II.C): renewal request equal to or less than current annualized amount; VA may increase; unspent funds may limit renewal (II.C.4); recoupment milestones by quarter end of the grant year: Q1 Dec 31, 2025 less than 15% (cap 35%), Q2 Mar 31, 2026 less than 40% (cap 60%), Q3 Jun 30, 2026 less than 65% (cap 80%); reductions on first business day after quarter end (II.C.5). Award periods: P1/P2 3-year, P3 1-year (II.D).
- Funding restrictions (IV.D): training max 5% of award excluding VA-mandated training; accreditation: initial once in 5 years, renewals per agency schedule (CARF every 3 years, COA every 4).
- Review (V): threshold 62.21; renewal rank at least 75 points and at least 1 point per category; Risk review cites Payment Integrity Information Act of 2019 (Pub. L. 116-117), Do Not Pay (31 U.S.C. 3354), OMB-designated databases.
- Award notices (VI.A): announce in Q4 FY 2025; 3-year eligibility: at least 1 year of ongoing operation measured "until March 3, 2025" (VI.C.6).
- Other (VII): eight target populations; payment limits without written approval: 35% Q1, 60% by end Q2, 80% by end Q3, 100% by end Q4 (VII.B).

## D02 - DEA/HHS final rule, Continuity of Care via Telemedicine for VA Patients (FR Doc 2025-01044, 90 FR 6523, Jan 17, 2025)

- Written by: DEA (DOJ) and SAMHSA (HHS); signed Jan 13, 2025 by Administrator Anne Milgram; Heather Achbach (contact, FR liaison); Miriam E. Delphin-Rittmon (HHS).
- Effective February 18, 2025. Finalizes VA parts of the March 1, 2023 General Telemedicine NPRM (comment period closed March 31, 2023; 35,454 comments). 233 veteran-related comments, 87 out of scope; categories 45, 39, 28 (IV).
- Rule: VA practitioner may prescribe schedule II-V via telemedicine if any VA practitioner did an in-person evaluation at any time; review VA EHR/internal database and state PDMP for previous 12 calendar months; 7-day limit if either unavailable; no-PDMP state: review internal database, may exceed 7 days; excludes contracted practitioners outside VA facilities via CCN or conducting disability compensation evaluations (21 CFR 1306.52; 42 CFR 12.4).
- Background: temporary rules through Nov 11, 2023 / Dec 31, 2024 / Dec 31, 2025; listening sessions Sept 12-13, 2023 (about 58 presenters); 2.7 million rural or underserved veterans (54% 65+, 44% under $35,000); 2,564,653 veterans compensated for a mental health condition (1.4 million PTSD, 322,158 MDD).
- Economic analysis (VI): median wage $23.11, 45.3% load, loaded $33.58; 0.75 h time, $25.19; 19.8 miles x $0.67 = $13.27; VA $0.415/mile, $6 deductible, $18 monthly cap, net $2.22; 9,400,000 x 0.1 x 0.72 x 0.16 x 0.61 = 66,056 visits; savings $2,540,514, transfers $146,644, net $2,393,870; reviewer wages $129.71/$62.51/$60.70 loaded x1.453; 64 seconds = 0.017 h; registrants 15,148/5,351/1,513 = 22,012; weighted $2.67; 660,560 visits x $2.67 = $1,763,695. Footnote 66 states a 16% controlled share via an inconsistent formula.
- Significance: "significant regulatory action" per DEA/HHS, not 3(f)(1); "not been submitted to the Office of Management and Budget for review".

## D03 - VA SSVF Notice of Funding Opportunity, FY 2027 (FR Doc 2026-00009, 91 FR 390, Jan 6, 2026)

- Written by: VA; approved by Richard F. Topping Dec 12, 2025; signed for publication by Taylor N. Mattson; contact Adrienne Nash Melendez.
- Round: operations beginning October 1, 2026; applications due 4:00 p.m. ET Thursday, February 19, 2026.
- Funding: "approximately $855 million via this NOFO with over 200 awards, with a range of $262,981 to $23,153,846" (I, line 37).
- Priorities (III.C): P1 renewal for grantees "who received a grant award under Priority 1 during FY 2026 to expand services to rural communities", LOI; P2 accredited, LOI except reprioritized; P3 renewal application, "Renewal applications can request funding that is equal to or less than their current annualized award"; P4 new applicants. Existing grantees = MOA through Sept 30, 2026.
- Same as D01: 2 months' rent (cited as 62.34(c)), $1,000 (62.34(g)), 80% AMI, admin 10%, 60%/40% homeless, Health Care Navigator, 75-point ranking, risk review (Pub. L. 116-117).
- Absent vs D01: CoC 90% cap, recoupment milestones, payment caps, training and accreditation-expense rules, target populations, internet and EHA text, 62.11 text (cited only).
- New vs D01: Before You Begin (EIN/UEI/SAM), "There is no limit on the number of applications", performance goals 1-6 (over 80,000 veterans, over 20,000 children, at least 70% exits, 90 days or less, under 5% returns, at least 90% prevented) (VII), pre-award costs ineligible, E.O. 14332 restrictions (IX).
- 3-year eligibility measured "until March 3, 2026" (VII item 6), 12 days after the deadline. Award notices: "fourth quarter of FY 2027 with grants beginning October 1, 2026" (sic); unsuccessful applicants notified before Oct 1, 2026.

## D04 - VA final rule, Apportionments (FR Doc 2026-00237, 91 FR 899, Jan 9, 2026)

- Written by: VA (VBA Compensation Service); approved by Douglas A. Collins Sept 30, 2025; signed by Taylor N. Mattson.
- Effective February 9, 2026; proposed Oct 14, 2021 (86 FR 57084), 60-day comment period ended Dec 13, 2021; 46 comments; eight commenters named (I).
- Rule: no new need-based apportionments; continue for incarcerated veteran or surviving spouse and incompetent veteran without fiduciary institutionalized at government expense; existing apportionments continue; 3.450 applies to claims received on or after Feb 9, 2026; effective date first day of month after receipt (3.400(e)); $50 / $90 pension reductions (3.452(b)(2)); DIC to child under 18 (3.455).
- PRA: 2,888 claims in 2024; 343 hospital adjustments, about 8 incompetent; about 320 incarcerated; about 328 still processed; 1,444 h -> 82 h; $32.66 BLS mean hourly wage, all occupations, unloaded; $2,678.12; savings $44,482.92 ($47,161.04 - $2,678.12).
- Not a significant regulatory action (OIRA); deregulatory under E.O. 14192.

## D05 - VA proposed rule, Title VI nondiscrimination (FR Doc 2026-12924, 91 FR 38569, June 26, 2026)

- Written by: VA (Office of Resolution Management, Sterling Akins); approved by Douglas A. Collins June 22, 2026; signed by Gabriela DeCuir; DOJ reviewed and approved (E.O. 12250).
- Comments by July 27, 2026. Removes 18.3(b)(2), "or effect" in (b)(3), (b)(6), (d)(2), Appendix B (d); technical changes (b)(1)(v), 18.12(a)(1), Appendix A.
- History: Dec 31, 1964; July 5, 1973; Nov 25, 1977; Aug 26, 2003; E.O. 14281 Apr 23, 2025; DOJ final Dec 10, 2025; E.O. 14173 Jan 31, 2025.
- FY25: "eight VA discretionary grant programs supported 621 awards, totaling $1,055,770,349".
- Appendix A: 14 statutory provisions in the regulatory text; preamble names 9 being updated; SSVF's 38 U.S.C. 2044 not listed ("this list is outdated").
- OIRA: significant under 3(f), not 3(f)(1); deregulatory under E.O. 14192 (requires identifying at least 10 regulations to repeal).

## D06 - ACUS, Adoption of Recommendations (FR Doc 2026-13127, 91 FR 39584, June 30, 2026)

- Written by: Administrative Conference of the United States; dated June 25, 2026, Shawne C. McGibbon, General Counsel. 85th Plenary Session June 11, 2026; four recommendations, all adopted.
- 2026-5 Interagency Communication in Rulemaking (contact Adam Cline; report Christopher Carrigan); 2026-6 Drafting Regulatory Preambles (Kazia Nowacki; Daniel T. Deacon), lists APA's four NPRM contents incl. plain-language summary address; 2026-7 Agreements Between Agencies (Becaja Caldwell; Blaine G. Saito); 2026-8 Effectuation of Awards of Recurring Monetary Benefits (Lea Robbins, also report author): example programs SSDI, Railroad Retirement, DOL programs, Veterans Disability Compensation, SCAADL (Department of War), OPM retirement, SS Retirement Insurance; metrics 11(a)-(c).

## D07 - SSA, SSR 26-2p, Documenting and Evaluating Disability in Young Adults (FR Doc 2026-17814, 91 FR 56262, Sept 1, 2026)

- Written by: SSA (Mark Steffensen, General Counsel; contact Michael J. Goldstein). Applies October 1, 2026; rescinds SSR 11-2p.
- Young adults 18 to approximately 25; title II child benefits for disability before 22; age-18 redeterminations; CDRs.
- Development: at least 12 months before application / interview / report.
- Insured status: under 24, 6 QCs in 12-quarter period; fn 47: 24 to 31, half the quarters from the quarter after attaining 21 (age 25 example: 8 of 16; odd count reduced by one).
- WIOA in-school 14-21, out-of-school 16-24 (signed July 22, 2014); IDEA through 21; IEP by 16; Section 301 continued payments, IEP ages 18-21.

## Shared ground (navigation only)

- D01 and D03 are consecutive editions of one SSVF notice; most text is identical. Differences: see D03 entry. D03 refers back to FY 2026 Priority 1 awards; D01 refers forward to the FY 2027 grant year (reprioritized grantees) and to "years two and three" of multi-year renewals.
- Taylor N. Mattson signs D03 and D04; Douglas A. Collins approves D04 and D05.
- BLS all-occupations wage used in D02 (median $23.11, loaded $33.58) and D04 (mean $32.66, unloaded).
- E.O. 12866 classification in D02, D04, D05 (and described in D06); E.O. 14192 in D04, D05.
- Comment periods: D02's 2023 NPRM (Mar 1 - Mar 31, 2023), D04's 2021 proposal (60 days), D05 (June 26 - July 27, 2026).
- SAMHSA: SOAR program owner in D01 (D03 drops the agency name); co-issuer of D02.
- Social Security: D01/D03 benefits screening and SOAR; D07 SSA ruling; D06 SSA programs as examples.
- No document cites another bundle document by FR citation.
