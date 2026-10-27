# aq-01539 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Target: medium, hard optional (page 2026-10-07: "Hard 0/2 · Medium 1/3 · Easy 1/1", "Easy questions are
full on this set"). Ids D01-D14 = Doc 1-14. Caller hooks written 2026-10-08 after the caller's own full
read of D01-D14 (not the mapper's map). Line numbers are text/Dnn.txt lines.

Bundle character: one MDL docket (In re Snowflake, Inc., Data Security Breach Litigation, MDL 3126,
D. Mont.), Oct 2024 - Aug 2026: JPML transfer (D01), conflict order (D02), two amended preliminary
settlement approvals (D03 Advance Auto, D04 Neiman Marcus), three MTD rulings (D05 consumer, D06
financial institutions, D08 LAUSD), judicial notice (D07), arbitration denial (D09), five 2026 discovery
orders (D10-D14). No forecasts, no restatements, no tables beyond D01's schedules and D03/D04 deadline
lists. Numerics are sparse and mostly single-document.

Repeated (non-unique) facts, so no single carrier is individually necessary: MDL start Oct 8, 2024
(D01, D02, D10-D14); breach announced May 30, 2024 and ads from May 24, 2024 (D05, D06); FAC July 9,
2025 (D05, D06, D08); Oct 6, 2025 hearing (D05, D06, D08, D09); Dec 27, 2024 CCPA letter (D05, D07,
D08); "Substantial completion ... July 31, 2026" (D10-D14); Special Master Doc 383 (D10-D14);
sanctions warning "$5000 ... ten-fold each subsequent time" (D12 L184, D13 L78); co-lead/class
counsel five names (D02, D03, D04); FAC spoke list (D05 L21-22, D06 L22-23, D08 L21-22); LendingTree
plaintiffs' four names (D07 L36, D09 L17); 560 million ad (D05, D06); Zappos 24 million (D05, D08).

Document defects to keep out of any premise or decoy: D03/D04 set the Final Approval Hearing on
"Thursday October 23, 2025" in the body (D03 L50, D04 L40) but list "July 10, 2025" in the deadline
table (D03 L152, D04 L142), and key every deadline to the "original"/"initial scheduled" date: two
defensible anchors. D05 cites "Doc. 4577", D08 "Doc. 28"/"Doc. 418" for LAUSD arguments (typos).
Possible person collisions not resolvable from the bundle: "Garcia-Nixon" (D05 L145, no notice) vs
"Susie Garcia" (D07 L38, Ticketmaster notice) vs "Plaintiff Garcia" (D10 L59); two Miller v. Snowflake
case numbers (D01 L138 2:24-00067 vs D02 L35 2:24-cv-96); "Chaidez" movant (D01 L19, two Chaidez
actions L125/L143) vs class representative Emmanuel Chaidez (D03 L17).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D12 L184/L187 (Ticketmaster $5000, pay within 15 days of July 1, 2026) + D13 L78/L84 (Innive $5000, July 16, 2026; respond within 7 days, pay within 15) | Sanction totals / due dates; escalation "ten-fold each subsequent time" | Calculate across documents | escalation misapplied ($55,000) | each order prints its own $5000; rule sentence repeated; next-sanction asks are hypothetical | reject (lookups; hypothetical) |
| h2 | D12 L184-187 payment due July 16, 2026 = D13 order date; D13 L84 respond by July 23 | Bridge by computed date into the other sanctioned defendant | Scatter the pieces | none | only two sanctioned parties: without D12 the description still picks Innive (removal fail) | reject |
| h3 | D02 L10/L24 (AT&T I = MDL 3114, ~20,000 opt-out arbitration clients of Keller's firm) + D01 L41-42 fn 3 (MDL 3114 "centralizing twelve actions"), L69-70 fn 6 (MDL 3114: "2019 data set"; Snowflake AT&T data May-Oct 2022) | Size or data year of the AT&T MDL where Keller's firm holds the opt-out clients: twelve actions / 2019 | Linking across documents; Who belongs where | MDL 3124 four actions (D01 L19, Schedule A); 2022 records (fn 6 same footnote) | D02 prints "MDL 3114" beside AT&T I (tied); 2019 and 70 million are public; "twelve" small integer | investigate (Easy-leaning; closed-book risk) |
| h4 | D03 L53 (up to 33.33% of $10,000,000; $2,500 x 6 reps) + D04 L43 (up to one-third of $3,500,000; $3,000 x 6) | Combined fee caps $4,499,666.67; service awards $33,000 | State the rounding; Calculate across documents | $4,500,000 if 33.33% read as one-third | precision trap reads as manufactured; "too vague" block if both form solvers take 1/3 | reject |
| h5 | D01 L21-22 fn 1 (seven defendant groups incl. Cricket Wireless, Neiman Marcus) - D05 L21-22 FAC spokes (or D06/D08) - D04 (Neiman Marcus settlement) | Transfer-order defendant neither in the July 2025 complaint nor settling: Cricket Wireless | Match then exclude | Neiman Marcus (absent from FAC but settled) | FAC list repeated in 3 docs (platform removal of one leaves two); Cricket may sit inside "AT&T" (bundle silent); guessable | investigate (fairness doubt) |
| h6 | D05 L413-415 (TM consumer Counts I and IV dismissed: contract, UCL) + D06 L309 (TM FI Count IV dismissed: declaratory/injunctive) | Same count number, different claims; surviving counts 4 + 3 = 7 | Who belongs where; Aggregation | "Count IV" = same claim | ORDER sections print every count; lookups | investigate (Easy) |
| h7 | D09 L28 (motion May 16, 2025), L103 (denied Oct 30, 2025) + D14 L31-32 (subpoena July 7, 2026; objection July 27, 2026 citing the appeal of Doc 595) | Days from denial / motion to the Coinbase objection: 270 / 437 | Calculate across documents | hearing Oct 6, 2025; subpoena date | plainly dated bridge (measured Too easy family) | park (Easy) |
| h8 | D12 L33 (CrowdStrike retained May 17, 2024) + D05 L35 / D06 L33 (announcement May 30; ads May 24, 2024) | Retention 13 days before announcement / 7 before ads | Calculate across documents | May 24 vs May 30 | D05 and D06 duplicate the second date (removal flag); plain dates | reject (necessity) |
| h9 | D13 L68 (Snowflake cannot schedule LAUSD Plaintiffs' depositions; Innive silent since March 23, 2026) + D08 L29-31 ("eight students ... and four of their parents") | Named plaintiffs in the group whose depositions Innive's silence stalled: 12 | Aggregation; Linking across documents | 8, 4, "4M+ Student" | D13 names "LAUSD Plaintiffs" outright (two-hop lookup) | park (Easy) |
| h10 | D11 L80 (lawyer letter: NIST-800, ISO27001, PCI DSS, FERPA, HIPAA, FTC Act s.5) x D07 L26-32 (FTC article, Mandiant, PCI SSC guidelines, CIS guide) x D06 L247-265 (FTC Act s.5 supports negligence per se) | Standard on the plaintiffs' list that the court accepted as a negligence-per-se basis: FTC Act s.5 | Mentions vs does | PCI (incorporated by reference in D07) | FTC Act s.5 as negligence-per-se basis is general knowledge (closed-book); PCI DSS -> PCI SSC mapping is outside knowledge | reject |
| h11 | D01 L29-32 (Snowflake and Advance Auto Parts opposed centralization) + D03 L17 ($10,000,000 Advance Auto fund) | Opposer that later settled, and its fund | Match then exclude | Snowflake (opposed, no settlement), Neiman Marcus (settled, supported) | lookups; without D01 the larger-fund guess hits | park (Easy) |
| h12 | D05 L42 (nine consumer injury categories) vs D08 L37 (seven LAUSD categories; court analyzes three, refers rest to Doc 591) | Categories neither ruling analyzes | Mentions vs does | dark-web postings discussed under traceability | judgment about what "analyzed" means; about the rulings' structure (rule 10) | reject |
| h13 | D03 L50/L152, D04 L40/L142 hearing dates and keyed deadlines | Opt-out / notice deadlines | n/a | n/a | internal contradiction (two anchors) | reject |
| h14 | D07 L36 + D09 L17 (same four LendingTree plaintiffs); D07 L38 vs D05 L145 Garcia | Notice recipients vs no-notice plaintiffs | Entity resolution | Garcia vs Garcia-Nixon | identity unresolvable in the bundle | reject |
| h15 | D01 L27/L66/L67 fn 5 (45 actions; Montana 14 + 12 tag-alongs; 42 related in 12 districts counting Montana and E.D.N.C. as one each) | Derived: E.D.N.C. tag-alongs 3; actions transferred from outside Montana 31 | Figure that must be computed | printed 45 | single document; no partner fact in another document | reject (one source) |
| h17 | D03 L17/L62 (Kroll administers the Advance Auto settlement) + D01 L61 (Advance Auto actions consolidated in E.D.N.C.), L27 (45; 34), L66 (Montana 14 + 12), L67 fn 5 (42 related in 12 districts, Montana and E.D.N.C. counted once each), L140-150 (10 E.D.N.C. actions) | E.D.N.C. potential tag-alongs at centralization: 3 (total related 13) | Scatter the pieces; Calculate across documents | Montana's printed twelve; 13 (total); 34; 10 | D03 identification bypassable by elimination (forced-guess probe 3 at p 0.55); answer-not-supported risk if the high model misses the footnote algebra | promoted q01 (author A's i01; revives h15) |
| h16 | D12 L144 (Snowflake payments 2022 $750,000; 2023 $1,312,500; 2024 $1,386,467.97) | Any year selected by another document's event | Scatter the pieces | other years | every natural bridge year (breach 2024, retention 2024) is in D12 itself; cross-spoke bridges (AT&T 2022 records) are contrived and span two years | reject |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.

Caller assessment after h1-h16: the bundle has no forecast/outlook series, no restated figures and no
dated value "in force" that changes between documents, so the measured Medium family (untied edition
trap) has no direct analogue. Cross-document links are identifier/date/name joins and repeated
boilerplate. Independent authors are asked to search again before any write-up.
