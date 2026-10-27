# aq-02501 - cross-document hooks

Target: medium (user 2026-10-09: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."). Caller inventory (origin claude), written after a full read of
D01-D07. No document in the bundle cites, amends or responds to another; there are no editions of
one series and no proposal/final pair, so the measured Medium family (an event dated in one
release selecting an edition in another) has no natural home here. Two independent
question-author agents (A numeric, B rule/scope) were dispatched for further hooks.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D02 L125/L203 AY 2015-16 4.9%; D04 L41 2019-20 3.7% | change in veterans' share of undergraduates (-1.2 points; -24.5%) | calculate across documents | D02 5.1% (MSI), 9.2% (for-profit), 6.4% (adults); D04 13% for-profit share of veterans | two lookups + one operation, both years named in the question | weak: measured too-easy shape |
| h2 | D02 L72 56 comments; D03 L91 148 total, L56-57 "over 70"/"over 45" | comment-count gap 92 | calculate across documents | 115 from summing the approximate parts | arbitrary pairing; two lookups | weak |
| h3 | D03 L40 effective June 25, 2024; D05 L30 effective Nov 29, 2024; D02 L27 effective Feb 15, 2024 / applies Jan 16, 2025 | day gaps between rule effective/applicability dates (157; 205 vs 131) | calculate across documents; temporal alignment | D02's two dates sit in one sentence (tied) | tied trap; arbitrary pairing | weak |
| h4 | D06 L102 caps $25M FY2019 / $75M FY2020-22 / $100M FY2023+, L82 funding released Oct 1; bridge dates: D02 L76 NPRM Oct 12, 2022 (FY2023); D05 L118 Dec 20, 2019 (FY2020); D05 L530 first report Oct 1, 2022 holding FY 2022 data | STEM cap in the fiscal year of a dated event elsewhere ($100M or $75M) | temporal alignment (fiscal vs calendar) | calendar-year mapping gives $75M (NPRM) or $25M (Dec 2019) | contrived bridge; federal FY convention widely known; three-valued answer guessable; caps possibly recallable | hold as fallback sketch only |
| h5 | D05 L428/L469-472 DARB "less than honorable" incl. general; D03 L82-86, L210 GI Bill only honorable, no COD for general | characterizations that are DARB-eligible yet bar GI Bill | conditional filter | none: every DARB-eligible characterization bars GI Bill | D03 alone answers the general-discharge point; trick framing | reject |
| h6 | D01 L133-147 GI Bill programs by chapter; D02 L32 "VA aid" chapters | GI Bill programs DEERS supports that count as VA aid | match then exclude | REAP / National Call to Service | final rule text (L298) says "under title 10" generally, conflicting with the preamble list; transferability chapter unstated | reject: two defensible readings |
| h7 | D06 L86-96, L221-234 priority regime before/after Jan 5, 2021; D05 L131 Jan 1, 2021 deadline | priority scheme for enrollment starting on DoD's deadline date | temporal alignment | six groups (post-Isakson-Roe) | answer is a small count (2 vs 6), contrived bridge | reject |
| h8 | D04 L154-159 $8,910,000, 12 awards, $700,000 average, $750,000 max | implied average $742,500 / max-size awards 11 | exact figure vs printed estimate | printed $700,000 / 12 | single document | reject (rule 2) |
| h9 | D05 L275 "$6.24 to $69.35" vs Table 1 L283 "$69.73"; 0.08 h x $24.95 = $2.00 not $6.24 | petitioner's maximum cost | exact table vs prose | $69.35 | single document; two printed answers | reject |
| h10 | D02 L80 9,247 approved, 5,257 exempt, "57 percent" | exact exempt share 56.85% | exact vs rounded | 57% | single document | reject (rule 2) |
| h11 | D04 L121 "military- or veteran-connected student" (member, veteran or spouse); D06 L45 STEM eligibility incl. Fry Scholarship spouses and children, Purple Heart recipients | STEM-eligible groups outside ED's definition (children) | definition applied to instance | Fry spouses (a surviving spouse may or may not be a "spouse of a service member") | surviving-spouse reading disputable; one-item answer | reject |

Notes: no instance-level facts (cases, programs, enrolments) exist for D02/D03/D05/D06 rules to be
applied to; every rule-to-case design would need the case in the question (rulebook risk).

## Independent author returns (2026-10-09, origin claude, no files written by them)

- Author A (numeric): no fair Medium-capable numeric design. Hooks: a01 lettered routine uses 37 - 26 = 11
  (held; -> sketch i03); h2 proposal-to-final gaps 1,386 - 461 = 925 (rejected by A as plain dated lookups;
  -> sketch i02 for a free quick test only); h3 STEM FY-cap bridge (rejected); h4-h6 single-document
  look-alikes in D05/D04/D02 (rejected, rule 2); h7 veterans' share (rejected); h8 VA-aid chapters (two
  readings); h9 characterization counts (single document or general knowledge); h10 trivial joins.
- Author B (rule/scope): no fair Medium-capable design. b01 DARB "less than honorable" vs VA automatic
  acceptance: general discharges and entry-level separations (held as fair; -> sketch i01). Rejected:
  STEM FY cap, 81-month DEA cap, Fry child yes/no, STEM relatives vs ED definition, veterans' share,
  regulatory-bar count by anchor date, Coast Guard Secretary (general knowledge), VA-aid chapters,
  waiver-criteria count, date/count joins with tied decoys.
- Caller verification: a01 counts by regex enumeration (37, 26); h2 dates and alternatives by datetime
  (925; 955, 930, 878, 559); b01 passages D05 L244/L427/L428/L470, D03 L50/L52/L68/L82/L117/L210/L244/L277-
  279/L282/L383 read in context.
