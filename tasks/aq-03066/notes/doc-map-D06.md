# aq-03066 - document map fragment: D06 only (for merge into doc-map.md)

Navigation only: where things are in `text/D06.txt`, not what to ask. Questions quote the document, never this map.
Line numbers are `text/D06.txt` line numbers (the Read tool's numbering). The original in `docs/` is the same text
shifted by two lines (D06 line N = original line N-2; D06 line 1 is the extraction header).
Quotes are verbatim spans of 12+ characters. Curly quotes and en dashes are the document's own.

## Binding and coverage

- Source: `docs/nzcc_fibre_im_r1_framework_spark_axiom_economics_expert_report_21_december_.txt`
- Manifest: id D06, method `text`, pages null, chars 105880, sha256 `99cd53b911480eb2963d142112e5ae80d05dfdea496c9fbc310071888959733a`
- Intake: task-page document number 7; `incomplete: false`, `gap_characters: 0`, `matches_capture: true`
- Coverage ledger (full sequential read, 2026-10-11): lines 1-200, 200-419, 419-628, 629-829 read. Unread: none.
  Line 828 is the end marker `-----`; line 829 is empty.
- Extraction spot-checks against the original `docs/` file:
  - Size: original 529 non-empty lines, D06.txt 530 (the extra one is the header line 1). Page count: not applicable (text capture).
    Printed page markers in the text run i-v then 1-30 (see Structure).
  - Figure block: `Figure 4.1: Allocation of common costs` is at original line 697 = D06 line 699; `* Not to scale` original 717 = D06 719. Match.
  - Footnote: footnote 73 `Prepared for the New Zealand Commerce Commission, 23 June 2014, p.72.` original 567 = D06 569. Match.
- Tables: none in the document. Figures: one labelled (Figure 4.1, labels only) and one unlabelled figure inside Box 4.2 that is
  not present in the text (see Figure and boxes).

## Identity

- Title: `New regulatory framework for fibre` (L3); subtitle `A report for Spark` (L4); date `December 2018` (L5).
  The body gives month and year only. The day "21" appears only in the source file name, not in the text.
- Author: `Hayden Green` (L8), `Axiom Economics` (L9), under the heading `Project Team` (L7). One person is listed.
  L29: `My name is Hayden Matthew Green. I am a Director of Axiom Economics and the head of its New Zealand operations.`
  Footnote 1 (L47): `a Bachelor of Commerce and a Bachelor of Laws with Honours from the University of Auckland`.
- Offices listed: Australia (`Petersham NSW 2049`, L12) and New Zealand (`PO Box 5405 Wellesley St`, L15; `Auckland 1141`, L16).
- Client: `I have been asked by Spark New Zealand (Spark) to provide an independent economic review` (L29; repeated without
  "New Zealand" at L153).
- Paper responded to: `See: Commerce Commission, New regulatory framework for fibre, Invitation to comment on our proposed approach, 9 November 2018`
  (footnote 2 at L48 and footnote 6 at L165), short form `New Framework Paper`. L151 calls it the Commission's
  `represents the first step in this process`.
- Brief: `if there are any key messages that the Commission should take on board` (L31, L153).
- Stated limits of the report:
  - L161 `I do not offer any opinions on the precise form the various IMs should take` and `such assessments would be premature at this stage`.
  - L162 `the opinions expressed throughout this report are my own and do not necessarily reflect the views of Spark`.
- Fiscal/calendar convention: not applicable (no financial periods). Dates are calendar dates.
- Appendices: none. No bibliography; sources are in 85 footnotes (footnote 1 at L47, footnote 85 at L802).

## Structure (headings, line ranges, printed pages)

Contents block at L20-25 gives printed page numbers: Executive Summary ii; 1 Introduction 1; 2 Background 2 (2.1 p2, 2.2 p4,
2.3 p6, 2.4 p8, 2.5 p10); 3 General implications 13 (3.1 p13, 3.2 p15, 3.3 p17, 3.4 p19, 3.5 p20); 4 Specific observations 22
(4.1 p22, 4.2 p24, 4.3 p27, 4.4 p29).

| Section | Lines | Printed pages |
| --- | --- | --- |
| Cover and project team | 3-17 | cover |
| Contents | 19-25 | i |
| Executive Summary (sub-heads `Background` L32, `General implications` L72, `Specific observations` L123) | 27-147 | ii-v |
| 1. Introduction | 149-165 | 1 |
| 2. Background (intro) | 167-171 | 2 |
| 2.1 Greater scope for competition | 173-232 | 2-4 |
| 2.2 Transition between technologies | 222-277 | 4-6 |
| 2.3 Higher probability of future regulatory changes | 279-310 | 6-8 |
| 2.4 Greater focus on efficient pricing | 311-361 | 8-10 |
| 2.5 Summary | 362-412 | 10-12 |
| 3. General implications (intro) | 414-416 | 13 |
| 3.1 Focus on competition | 418-460 | 13-15 |
| 3.2 Matters for which IMs are determined | 461-505 | 15-17 |
| 3.3 Level of prescription | 507-545 | 17-18 |
| 3.4 Fewer concerns about underinvestment | 548-574 | 19-20 |
| 3.5 Summary | 576-628 | 20-21 |
| 4. Specific observations (intro) | 630-632 | 22 |
| 4.1 Asset valuation | 634-679 | 22-24 |
| 4.2 Cost allocation (Figure 4.1 L699-719; Box 4.1 L724-735) | 680-749 | 24-27 |
| 4.3 Pricing principles (Box 4.2 L767-783) | 750-792 | 27-29 |
| 4.4 Summary | 794-826 | 29-30 |

Printed page markers sit at L19 (i), 27 (ii), 56 (iii), 88 (iv), 121 (v), 149 (1), 167 (2), 188 (3), 215 (4), 234 (5), 268 (6),
288 (7), 309 (8), 329 (9), 352 (10), 372 (11), 406 (12), 414 (13), 434 (14), 456 (15), 481 (16), 500 (17), 526 (18), 547 (19),
573 (20), 605 (21), 630 (22), 659 (23), 678 (24), 698 (25), 722 (26), 743 (27), 764 (28), 782 (29), 811 (30). Several markers are
fused to the start of a text line (for example L215 `4 install transmission equipment`, L811 `30 between now and the inception date`).

Margin call-outs (short restatements printed beside the body, interleaved in the extraction) sit at L52, 54, 82, 84, 86, 115,
117, 119, 140-147, 186, 213, 232, 264, 266, 286, 307, 327, 350, 400, 402, 404, 412, 430, 432, 454, 479, 498, 523-524, 545, 571,
601, 603, 626, 628, 657, 675-676, 693-696, 720, 741, 758, 760, 762, 776-780, 803-809, 823-826.

The three summaries repeat the Executive Summary almost word for word: 2.5 = Executive Summary "Background" (L33-71 vs L363-411);
3.5 = "General implications" (L73-122 vs L577-625); 4.4 = "Specific observations" (L124-136 vs L795-821).

## Definitions and abbreviations (full name first, short form after)

| Term | Where introduced | Verbatim |
| --- | --- | --- |
| Commission | L29, L151 | `Commerce Commission’s (Commission’s)`; `Commerce Commission (Commission)` |
| the Act | L29, L151 | `Part 6 of the Telecommunications Act 2001 (the Act)` |
| IMs | L31, L151 | `input methodologies (IMs)` |
| FFLAS | L31, L151 | `fibre fixed line access services (FFLAS)` |
| Spark | L29 | `Spark New Zealand (Spark)` |
| LFC | L36, L375 | `Chorus is not the local fibre company (LFC)` |
| HFC | L38, L377; fn 3 L50, fn 10 L184, fn 47 L398 | `hybrid fibre coaxial (HFC) network`; `HFC is a broadband network based on a hybrid of fibre and coaxial cable technologies` |
| FWA | L40, L379; fn 4 L51, fn 11 L202, fn 48 L399 | `fixed wireless access (FWA)`; `access that is restricted to one premise (or location)` |
| New Framework Paper | fn 2 L48, fn 6 L165 | `(hereafter: ‘New Framework Paper’)`; shortened once to `New Framework, p.83.` (fn 58, L476) |
| RSPs | L194 | `retail service providers (RSPs)` |
| UFB | fn 13 L205; L223 | `ultra-fast broadband (UFB)`; used earlier undefined at L128 (`the UFB build`) |
| DFAS | fn 12 L204; L341; L732; defined fn 40 L347 | `Direct Fibre Access Service (DFAS)`; `DFAS is generally understood to be a service that allows RSPs to purchase access to dedicated parts of the fibre network` |
| equivalence | fn 14 L207 | `They must offer the same input services, systems and processes to all access seekers, themselves and related parties.` |
| non-discriminatory | fn 15 L209 | `The providers are obligated not to discriminate in how they treat access seekers, related parties and themselves.` |
| dark fibre / layer 2 | fn 16 L211 | `Dark fibre comprises either a separate physical`; `Chorus supplies the terminating equipment, splitter and the fibre` |
| anchor services | L245; fn 22-24 | `a basic fibre broadband service22 and a fibre-based voice service` |
| IRIS | L279; fn 30 L285 | `(or ‘IRIS’) is now applied to regulated energy businesses` |
| EA | L312 | `it was the Electricity Authority (EA) that had the power to set pricing methodologies` |
| GPBs | L312 | `gas pipeline businesses (GPBs)` |
| FCM | L442 | `(FCM) principle54` (preceded by `financial capital maintenance`) |
| fibre asset | L645-649 | `Furthermore, s.176(4) defines a`; `(whether or not the asset is also employed in the provision of other services)` |
| avoidable cost allocation methodology | L132, L739, L817 | described at L739: `this approach would result in all costs that are not directly attributable being allocated fully to FFLAS` |
| allocative efficiency | fn 38 L325 | `Allocative efficiency gains stem from reductions in` |
| price squeeze | L773-774 | `prevents an efficient rival procuring a wholesale product from being able to compete` |
| unders account | L296 | `grew to a sum that could not plausibly be recovered` |

Used but never expanded in D06: `RAB` (first at L124; L453 has `the opening regulatory asset value`), `WACC` (first at L107),
`UCLL`, `UBA`, `DSLAM` (fn 17 L226; L655), `EDBs` (fn 83 L757), `5G`. Not used at all: "ACAM", "ABAA", "OVABAA", "CIP", "CFH".

## Numbers ledger (every figure, date, count and reference number)

"Whose" = Axiom (the author's own statement), Commission (attributed to the Commerce Commission), Act (attributed to legislation),
third party (named), or bibliographic (a citation detail).

| Lines | Value | Unit / what it measures | Period or scope | Whose | Verbatim |
| --- | --- | --- | --- | --- | --- |
| 5 | December 2018 | report date (month, year) | - | Axiom | `December 2018` under `A report for Spark` |
| 48, 165 | 9 November 2018 | date of the Commission paper responded to | - | bibliographic | `Invitation to comment on our proposed approach, 9 November 2018` |
| 29, 151 | 2001; Part 6 | Telecommunications Act year; Part holding the fibre regime | - | Act | `Part 6 of the Telecommunications Act 2001` |
| 155-156, 169, 489, 635, 785, 788, 803-805 | 1986; Part 4 | Commerce Act year; Part for energy and airports | - | Act | `Part 4 of the Commerce Act 1986` (L169, L635) |
| 33, 169, 363 | "past decade" | length of the Commission's Part 4 experience | to December 2018 | Axiom | `over the past decade` |
| 50, 184, 398 | 2012 | year Vodafone merged with TelstraClear and acquired the Wellington HFC network | 2012 | Axiom | `when it merged with TelstraClear in 2012` |
| 111, 621 | $1b-$3b | dollars per year (currency not otherwise labelled); cost of a major supply disruption for regulated energy businesses | annual | third party (Oxera) | `well below the $1b-$3b annual cost estimated by Oxera` |
| 561 | $1bn and $3bn | dollars per year; cost of severe outage events | annual | third party (Oxera; fn 73) | `Oxera estimated the potential annual cost of severe outage events as being between $1bn and $3bn.` |
| 113, 549, 561, 623 | 67th percentile | percentile of the Commission's estimated WACC range adopted for regulated energy businesses | Part 4 process | Commission (as reported by Axiom) | `adopt the 67th percentile of its estimated WACC range for regulated energy businesses` (L549); `to the 67th percentile of the estimated range` (L113, L623) |
| 561 | 50th percentile | percentile the WACC was set above | Part 4 process | Commission (as reported) | `by setting the WACC above the 50th percentile (at the 67th percentile)` |
| 282 | 75th | percentile, in a report title only | May 2014 | bibliographic | `Green et al, Review of the use of the 75th WACC percentile, a report for Orion, May 2014, pp.43-48.` |
| 569 | 75th | percentile, in a report title only | 23 June 2014 | bibliographic | `Review of the ‘75th percentile’ approach` |
| 126, 651, 797 | pre-December 2011 | asset class cut-off label | before December 2011 | Act (s.176), as described by Axiom | `allocations of this kind will be required for both` (L126); `Allocations of this kind would be required for both` (L651) |
| 641 (twice) | 1 December 2011 | ownership cut-off and financial-statement date for Chorus assets | 1 December 2011 | Act (s.176(1) and (2)), as described | `for assets owned by Chorus before 1 December 2011, as the costs recorded in the published general-purpose financial statements as of 1 December 2011` |
| 655 | pre-2011 | same asset class, shorter label | - | Axiom | `the pre-2011 fibre assets are likely to include items like feeder fibre` |
| 139 (fn 5), 668 | 2022 | year up to which Chorus spending can be included in the initial fibre RAB | "between now and 2022" | Axiom | `anything that it spends between now and 2022 (given that the Commission has been granted a two-year extension)` (L139); L668 has `has now been granted` |
| 139, 668 | two-year | length of the extension granted to the Commission | - | Axiom | `a two-year extension` |
| 169, 312 | three | number of monitored airports | - | Axiom | `the three monitored airports` |
| 319 (fn 34) | 3 named | airports named | - | Commission (NFP p.83) | `when reviewing pricing decisions from Auckland, Wellington and Christchurch Airports` |
| 160 | three | matters covered by section four | - | Axiom | `three of the most important matters that the Commission will need to examine` |
| 189 | 3 named | operators that signalled 5G intentions | - | Axiom | `Spark, Vodafone and 2degrees have all signalled their intentions to deploy 5G networks.` |
| 191-192, 769 | 1 January 2020 | date from which Chorus must supply unbundled layer 1 services | from 1 January 2020 | Axiom describing the regime | `1 January 2020,13 Chorus will be required to supply` (L192); `From 1 January 2020, Chorus will be required to supply` (L769) |
| 205 (fn 13) | 1 January 2026 | same obligation in the UFB second-phase network | from 1 January 2026 | Axiom describing the regime | `And from 1 January 2026 in the network funded as part of the second phase of the ultra-fast broadband (UFB) deployment.` |
| 765 | post-2020 | period label for layer 1 vs layer 2 pricing | after 2020 | Axiom | `relative pricing of layer 1 and layer 2 services post-2020` |
| 257 (fn 24) | 1 January 2020; 2019 levels | start date and price base for anchor products | from 1 January 2020 | Axiom describing the regime | `anchor product prices (from 1 January 2020) will be set at 2019 levels then adjusted annually at the rate of inflation` |
| 252 (fn 21) | 2019 levels | price base for copper where FFLAS is not available | - | Axiom describing the regime | `copper services will continue to be regulated, with prices set at 2019 levels, with inflation adjustments` |
| 733 | 2019 levels | price base for the DFAS | first regulatory period, real terms | Axiom describing the regime | `The price of the DFAS will be fixed at 2019 levels for the first regulatory period (in real terms).` |
| 254 (fn 22) | 100/20Mbps | speed of the initial anchor broadband product | "Initially" | Axiom describing the regime | `Initially, this will be a 100/20Mbps UFB broadband product.` |
| 271, 305 | 100% | share of volume risk borne by the regulated business under a price cap | - | Axiom | `Because the regulated business assumes 100% of the volume risks with a price cap` (L271); `assumes 100% of the volume risks under a price cap` (L305) |
| 660 | 100% | share of fibre assets assigned to the initial RAB (rejected scenario) | - | Axiom | `Allowing Chorus to assign 100% of its` |
| 683 | 100% | share of directly attributable costs allocated to FFLAS | - | Axiom's reading of the Commission proposal | `(100% of which will, presumably, be allocated to FFLAS)` |
| 702 | 100% | share of fibre/copper common costs allocated to fibre (feared conduct) | - | Axiom | `allocate 100% of the costs (and assets) that are common across its fibre and copper networks to the former` |
| 748 | 100% | share of common costs reallocated to still-regulated FFLAS (feared conduct) | - | Axiom | `reallocate 100% of the costs that are common to the newly deregulated services` |
| 661 | "twice or more" | number of times common costs would be recouped | - | Axiom | `(i.e., recoup its common costs twice or more)` |
| 289 | December 2010 | month the Part 4 regimes were first introduced | - | Axiom | `when they were first introduced in December 2010` |
| 321 (fn 36), 323 (fn 37) | December 2010; pp.180-181; p.180 | Commission reasons paper date and pages | - | bibliographic | `Reasons paper, December 2010, pp.180-181.` |
| 757 (fn 83) | 22 December 2010; p.68 | Commission reasons paper date and page | - | bibliographic | `Input Methodologies (EDBs &GPBs) Reasons Paper, 22 December 2010, p.68.` |
| 292 | five or ten years | illustrative horizon for different regulation | future | Axiom | `could differ significantly` (preceded by "five- or ten-years’ time") |
| 312, 320 | 1966; s.4A | Airport Authorities Act year and section | - | Act | `s.4A of the Airport Authorities Act 1966` |
| 368 (fn 45) | 30 May 2017 | date of an Electricity Authority consultation paper | - | bibliographic | `Consultation paper, 30 May 2017.` |
| 428 (fn 49) | 1993; August 1993; pp.3-5 | Hilmer report date and pages | - | bibliographic | `Report by the Independent Committee of Inquiry, August 1993, pp.3-5.` |
| 466, 478 | three (others) | economic principles the Commission raised besides pricing efficiency | - | Commission (NFP p.83) | `(alongside three others)`; `the other three principles the Commission identifies` |
| 488 | 2025 | illustrative year for dark fibre pricing | "say, 2025" | Axiom | `need to know how the prices will be set in, say, 2025` |
| 495 (fn 64) | 3 years | time after the implementation date before a s.207 recommendation | - | Act (s.207), as described | `Section 207 states that, 3 years after the implementation date, the Commission can recommend` |
| 564 | 500,000km; 5,000km | odometer distances in an analogy | - | Axiom | `a car with 500,000km on its odometer` ; `a vehicle that has travelled only 5,000km` |
| 569 (fn 73) | 23 June 2014; p.72 | Oxera report date and page | - | bibliographic | `Prepared for the New Zealand Commerce Commission, 23 June 2014, p.72.` |
| 595 (fn 74) | 20 April 2018; pp.21-22 | Departmental Report date and pages | - | bibliographic | `Science and Innovation Committee, 20 April 2018, pp.21-22.` |
| 681 | two | broad categories of costs in the Commission's proposed cost allocation IM | - | Commission (as reported) | `allocates two broad categories of costs to FFLAS` |
| 738 | two | "key things" noted about cost allocation | - | Axiom | `two key things are worth noting at this preliminary stage` |
| 136, 679, 821 | dual | objectives served by prescriptive IMs | - | Axiom | `would serve the dual objectives` |
| 40, 80, 99, 189, 459, 460, 486, 527, 584, 609, 753 | 5G | mobile technology generation | - | Axiom | `deployments of 5G mobile infrastructure` (L189) |
| 42, 192, 194, 219, 381, 679, 706, 765-776 | layer 1; layer 2 | network layers | - | Axiom | `unbundled layer 1 services` |
| 11-17 | PO Box 334; 2049; +61 420 278 101; PO Box 5405; 1141; +64 212 664 884 | contact details | - | Axiom | `PO Box 5405 Wellesley St` |

New Framework Paper locators cited (all bibliographic): p.52 (fn 7, L178); p.36 (fn 18, L228); p.83 (fn 34, L319; fn 58, L476);
p.81 (fn 39, L345); p.59 (fn 51, L445; fn 52 `Ibid.`, L447); p.77 (fn 53, L449); p.72 (fn 54, L451); p.93 (fn 56, L472;
fn 57 `Ibid.`, L474); footnote 162 (fn 61, L490); pp.93-94 (fn 67, L520); footnote 133 (fn 72, L567); p.79 (fn 77, L599);
pp.33 and 95 (fn 78, L673).

Statute sections cited: Telecommunications Act s.162 and s.166(2)(b) (L76, 122, 220, 424-425, 435-439, 580, 625, 788);
s.174 (fn 62, L492); s.175(1) (L462, L482); s.176 (L124, 126, 660, 795, 797); s.176(1) and (2) (L637); s.176(2A) (fn 55, L453);
s.176(4) (L645); s.206 (L249, fn 23 L256, L483); s.206(6) (fn 63, L494); s.207 (L483, 486, fn 64 L495, fn 65 L496).
Commerce Act 1986 s.52T(b) (fn 60, L489); s.36 (L785-790, fn 84-85 L800-802, margin L803-805).
Airport Authorities Act 1966 s.4A (fn 35, L320).

Same quantity, different value or wording inside D06:
- Oxera cost: `$1b-$3b` (L111, L621, summaries; "major supply disruption") vs `$1bn and $3bn` (L561, body; "severe outage events").
- Asset cut-off: `pre-December 2011` (L126, 651, 797), `before 1 December 2011` (L641), `pre-2011` (L655).
- Commission 2010 reasons paper: `December 2010` with long title (fn 36, L321) vs `22 December 2010` with short title (fn 83, L757);
  the text does not say whether these are one paper or two.
- End of the locked-in revenue cap: `for the first regulatory period` (L63, L392) vs `until the reset date` (L271, L294).
- Extension wording: `has been granted` (L139) vs `has now been granted` (L668).

Not stated anywhere in D06 (searched): the length of a regulatory period; the implementation date as a calendar date; any WACC
value or cost-of-capital parameter (no beta, leverage, risk-free rate, debt premium, TAMRP); any financial-loss amount, period
or discount rate; any Chorus cost, revenue, connection or uptake number; any tax figure. The only percentages are the six "100%" uses.

## Lists ledger

Bullets in the extraction start with `-  `; sub-bullets with an em dash.

### The three summary lists (Executive Summary vs section summary vs body)

1. Differences between FFLAS and the Part 4 sectors. Heading sentence `there are several crucial differences between FFLAS and the sectors regulated under Part 4`
   (L34, L373). Four ordinal items; the body sections 2.1-2.4 are the four items.
   - First, competition: 4 bullets (L36-42; L375-381): copper vs fibre where Chorus is not the LFC; Vodafone HFC vs Chorus and Enable fibre;
     wireless (FWA and mobile) vs fixed line; access-based competition from layer 1.
   - Second, copper-to-fibre transition: 3 bullets (L46, 58, 60; L385, 387, 389): relative pricing of copper and fibre; demand harder to
     predict; under-investment unlikely to cause major outages.
   - Third, future regulatory change: 2 bullets (L63, 65; L392, 394): revenue cap only locked in for the first regulatory period;
     scope of regulated FFLAS may be redefined if rivalry emerges.
   - Fourth, pricing efficiency: 2 bullets (L68, 70; L408, 410): more scope for allocative efficiency gains; Chorus's incentive to
     price to foreclose.
   - Executive Summary vs 2.5: identical except the second bullet of "Second": L58 ends `electricity lines company or airport; and`
     while L387 adds `(hence the reason for an initial revenue cap)`.
   - Body vs summaries: body 2.1 groups the competition sources under two ordinals, `First` infrastructure-based (L175) and `Second`
     access-based (L191), where the summaries give four bullets. Body 2.3 (L294-296) gives the revenue-cap bullet two sub-bullets
     (demand easier to forecast; the unders account grows to an unrecoverable sum) that the summaries drop, and says
     `until the reset date` where the summaries say `for the first regulatory period`.

2. General implications, called `several principles or ‘themes’` (L73, L577). Four ordinal items; body sections 3.1-3.4.
   - First, competition as a paramount consideration: 3 bullets (L76, 78, 80; L580, 582, 584).
   - Second, a pricing principles IM: 2 "namely" bullets (L91, 93; L588, 590) plus 2 "this is vital, because" bullets (L97, 99; L607, 609).
   - Third, prescriptive IMs: 2 bullets (L103, 105; L613, 615).
   - Fourth, weaker case for a WACC uplift: 3 bullets (L109, 111, 113; L619, 621, 623).
   - Executive Summary vs 3.5: no wording difference found.
   - Body vs summaries:
     - The "Third" item lists `asset valuation, cost allocation, the cost of capital, and for any pricing principles` (L101, L611); body 3.3
       lists `key IMs such as asset valuation and cost allocation, and any pricing principles` (L515), without the cost of capital.
     - The foremost question is `how might this affect actual competition?` in the summaries (L78, L582) and
       `how might this affect actual competition across all telecommunications markets?` in the body (L438).
     - The "Fourth" item gives one reason for a lower outage cost, `because there are potential substitutes for FFLAS, such as mobile services`
       (L111, L621); body 3.4 (L574) gives two: `UFB services will not work in the event of a power outage` and substitutes.
     - The summaries add `(i.e., to the 67th percentile of the estimated range)` (L113, L623); the matching body sentence (L563) has no parenthesis.
     - Body 4.3 (L792) names the services, `for services like the unbundled fibre service and the DFAS`, where the summaries
       (L91, L588) and body 3.2 (L502) say `for particular services`.

3. Specific observations. Two ordinals plus "Finally" (L124-136; L795-821); body sections 4.1-4.3.
   - First, adjust fibre asset values before setting initial RABs: 2 bullets (L126, 128; L797, 799+811): allocate part of shared asset costs
     to other services; consider an efficiency examination of UFB build costs.
   - Second, cost allocation and pricing efficiency: 3 bullets (L130, 132, 134; L815, 817, 819): cost allocation IM gives clear guidance
     including between FFLAS types; avoidable cost allocation methodology off the table; prescriptive pricing principles methodology.
   - Finally: prescriptive IMs serve dual objectives (L136, L821).
   - Executive Summary vs 4.4: identical except that L128 carries footnote 5 and L811 does not.
   - Body vs summaries:
     - Avoidable cost allocation: summaries `one approach that should arguably be` off the table (L132, L817); body `one approach that should be`
       off the table (L739); margin `Chorus should not be able to use an avoidable cost allocation methodology.` (L758).
     - Efficiency examination: summaries `if the legislation permits` (L128, L799); body
       `if the legislation permits it (which is ultimately a legal question upon which I cannot opine)` (L666), with two further
       qualifiers at L670 (Crown Infrastructure Partners oversight; costs possibly locked in by contracts).
     - Body-only suggestion: an allocation method letting Chorus recover a rising share of copper/fibre common costs from fibre (L749).
     - The body's asset valuation part has three ordinals (first point at L651, `Second` L666, `Finally` L679); the summaries give two bullets.

### Other lists (all in the body)

| Lines | Heading or lead-in | Items | Content |
| --- | --- | --- | --- |
| 155-160 | Report structure | 3 | section two; section three; section four |
| 197-199 | How RSPs can differentiate before unbundling | 2 | cheapest basic offering; higher bandwidth product |
| 236-238 | How fibre investment differs from energy/airport replacement | 2 | new asset comparable to old; replacements piecemeal |
| 240-277 | Challenges from the transition (prose ordinals) | 2, then an offsetting point | `The first is the relative pricing of copper and fibre` (L240); `The second closely-related challenge` demand uncertainty (L251); under-investment concern reduced (L277) |
| 245-247 | Ways Parliament addressed copper/fibre pricing | 2 | defining anchor services; no explicit price controls where Chorus is not the LFC |
| 294-298 | Developments the Act allows for | 2 (first has 2 sub-items) | revenue cap locked in until the reset date; redefining the scope of regulated FFLAS |
| 315, 331 | Commission's reasons for not prescribing GPB pricing (`several reasons, including`) | 2 | limited allocative efficiency gains; GPBs have better information and data systems costly |
| 338-340 | Factors weighing the other way for FFLAS | 2 | more scope for allocative efficiency gains; Chorus's greater incentive to foreclose |
| 357-359 | What the EA observed could happen without appropriate access terms | 2 | connection standards favouring own business; discriminatory distribution charges |
| 469-471 | What is unclear about a "pricing efficiency" principle | 2 | no word on a pricing principles IM; legal status unclear |
| 486-488 | Examples of uncertainty without a pricing principles IM | 2 | 5G investors need DFAS tariff principles; dark fibre buyers need to know 2025 pricing |
| 529-531 | Why prescription benefits both sides | 2 | Chorus; access seekers |
| 553-559 | Subtler ways energy businesses could cut spending | 4 | not replacing ageing assets; higher utilisation; inefficiently small projects; operating cost solutions instead of capital |
| 563, 574 | Why an uplift is less compelling for FFLAS (prose ordinals) | 2 | assets nearly brand new; an outage would cost less |
| 639-643 | s.176(1) and (2): initial value of a fibre asset | 3 | cost of constructing or acquiring net of capital contributions; Chorus pre-1 December 2011 assets at financial statement cost; financial losses asset |
| 647-649 | s.176(4): fibre asset definition | 2 | constructed or acquired by a regulated provider; employed in providing FFLAS |
| 653-655 | Shared-asset examples | 2 | new UFB networks (shared ducts); pre-2011 assets (feeder fibre, ducts, man-hole covers) |
| 683-685 | Commission's two categories of cost | 2 | directly attributable to FFLAS; not directly attributable (common or shared) |
| 702-706 | Ways Chorus may be inclined to allocate common costs | 3 | all fibre/copper common costs to fibre; disproportionate share to mobile-input fibre services; disproportionate share to layer 1 |
| 727-729 | Box 4.1 customer options | 2 | Chorus local fibre; RSP mobile masts using parts of Chorus fibre |
| 737 | Candidate allocation bases (inline) | 3 named, then "etc." | routing factors; fibre strands used; connection numbers |
| 739-748 | `two key things` on cost allocation | 2 | `First` avoidable cost allocation off the table (with 2 reasons at L745-747); `Second` future-proofing by prescription |
| 788-790 | Why the Commission should act despite s.36 | 2 | pricing could comply with s.36 yet not promote the purposes; up-front principles better than litigation |

## Positions by topic (hedge words kept)

- Whether to copy Part 4. L71/L411: `it should not simply import its approaches from Part 4`; the Part 4 arrangements
  `can be a useful ‘starting point’, it should not be the ‘end point’`.
  L171 attributes the same recognition to the Commission (NFP p.52) and agrees: `it adopted under Part 4.7 I agree.`
- Competition as the lens. L74: `one of its paramount considerations should be ensuring that it does not unduly affect competition`.
  L442-457: `when faced with a choice between promoting competition or providing` more assured cost recovery, `the Commission should design its IMs with a view to achieving the former.`
  Limiting statement at L442: `This should not be taken to mean that Chorus should not be afforded a reasonable opportunity to earn a normal economic return`.
  L425: s.166(2)(b) `is likely to be a highly pertinent consideration a great deal of the time`; the statute itself is quoted as
  applying `to the extent it considers it relevant` (L424).
  L220: `this is perhaps the single most important difference`.
- Initial RAB / asset valuation (4.1).
  - Describes s.176 (L637-649). L651: `it does not follow that they should then be included in the initial fibre RABs (and the revenue cap and prices) without further adjustment`.
  - Should NOT apply: assigning all fibre assets to the RAB, L660 `would not be consistent with the purpose statements`.
  - Conditional, L661 opens `Unless a portion of the` fibre assets are allocated to other services, then
    `Chorus would almost certainly over-recover its costs (i.e., recoup its common costs twice or more)`.
  - Efficiency review, conditional and hedged: L666 `if the legislation permits it`, `the Commission may also wish to consider signalling its intention`;
    L670 `then an efficiency review of some fashion may be in order before the revenue cap is set`; counter-considerations in the same
    paragraph: `the stringency of the oversight provided by Crown Infrastructure Partners` and `It is also possible that` the
    `build costs over this window are largely` locked in.
  - Prescription: L679 `crafting a prescriptive asset valuation IM would serve the dual objectives`.
- Past financial losses. Description only, no recommendation. L643: `with a financial value equal to the financial losses incurred by the provider under the UFB initiative`.
  Footnote 55 (L453): s.176(2A) `is not intended to protect it from all risk of not fully recovering its financial losses through prices over time`.
  No period, discount rate or list of what counts is given.
- Crown financing. Not addressed. The only "Crown" references are `Crown Infrastructure Partners` (L93, 502, 590, 670, 792).
  The nearest related phrase is `(net of capital contributions)` in the s.176 description (L639).
- Cost allocation (4.2).
  - L700 `In my opinion, the cost allocation IM is vital.`
  - L737 `the IM should cover the allocation of costs between different types of FFLAS` and `should seek to provide clear directions about how all allocations should be done`.
  - Candidate bases are mentions, not recommendations: L737 `that could warrant consideration`.
  - Should NOT apply: avoidable cost allocation methodology (L739 `one approach that should be`; L132 and L817
    `one approach that should arguably be`; L758 margin `Chorus should not be able to use`). Two reasons at L745-747,
    the second attributed to `the experts advising regulated energy businesses and monitored airports throughout the Part 4 process agreed unanimously` (fn 83).
  - Copper vs fibre: allocating shared costs solely to fibre `would be inappropriate` (L739); footnote 31 (L301-303) says it
    `would be likely to result in Chorus over-recovering its costs`.
  - Hedged extra: L749 `It may also be beneficial for the Commission to specify an allocation methodology that enabled Chorus to recover an increasing proportion`;
    `an allocation based on customer numbers, routing factors, etc., might facilitate this outcome`.
  - Deregulation case: L748 `the methodology should be designed so as to preclude such possibilities`.
  - The accounting-based allocation approaches are not named anywhere in D06.
- Cost of capital. Only the percentile/uplift is discussed (3.4). L107/L617: `there may be less cause to be concerned` and
  `weaker justification for applying a` WACC uplift. L563: `the rationale for an uplift` ... `does not appear to be as compelling for FFLAS`,
  qualified by `or, at least, for an increment of similar magnitude`. No percentile is recommended and no parameter is discussed.
  The cost of capital is named once as a core methodology suited to prescription (L101, L611).
- Quality. No position on quality standards or dimensions. Related statements: L277 `it seems relatively unlikely that under-investment in service quality would result in major supply outages`
  (scoped `for the foreseeable future`); L277 `there is likely to be significant spare capacity for some time`.
- Capex IM, tax, regulatory processes and rules IMs. Not addressed. "capital expenditure" appears once, in the list of energy-business
  behaviours (L559); "processes" appears only inside the s.174 quotation (L483).
- Matters for which IMs are determined (3.2). L462: the Commission's preliminary proposal `is to determine only those IMs listed in s.175(1)`.
  L464 `For the most part, I agree with that assessment. However, there is one exception`. The exception is pricing principles:
  L482 `it is imperative that the Commission exercises this discretion and determines a pricing principles IM`; L483
  `that would represent a conspicuous hole in the regulatory tapestry`. Legal basis is stated as an understanding: L482
  `I understand that this list is` non-exhaustive.
- Pricing principles content. L502: `should consequently prepare a pricing principles IM that explains how the maximum` cost-based prices
  will be defined, and `reiterate and expand upon some of the principles set out in the deeds with Crown Infrastructure Partners`.
  Sequencing, footnote 66 (L518): `such an IM would ideally be prepared in close conjunction with the cost allocation methodology`.
- Prescriptiveness (3.3). The Commission's suggestion about principle-based regulation is quoted (L509, NFP pp.93-94) and answered
  `I am not sure that is correct.` (L510). L515: `the Commission should err on the side of more prescription, rather than less prescription`.
  L534: `I see no inconsistency between including greater prescription in the IMs` and future-proofing. Margin L117:
  `Prescriptive IMs are likely to be generally preferable to high-level principles.`
- Scope of regulated FFLAS. Conditional: L65/L298/L394 `it may be appropriate to redefine the scope of regulated FFLAS at those times`
  (if IMs prevent foreclosure and effective rivalry emerges). Footnote 20 (L231): `certain geographic areas might be candidates for deregulation`.
  Footnote 27 (L281): `it may not be appropriate for Chorus to expect to recover the costs of the assets in that area`.
- Anchor services and DFAS pricing. L341-343: the regime directly sets prices for the key anchor services and the DFAS
  `during the first regulatory period (i.e., Chorus has no discretion over the pricing of these products in the initial years). I see no obvious reason why this would`
  change beyond it. L249: the issue `may become a live issue again in the longer term` when anchor products are revisited under s.206.
- Unbundling / layer 1. L219: `it is conceivable that a time may come where it is neither necessary nor desirable to regulate the terms upon which Chorus offers its layer 2 services`
  (conditional on widespread layer 1 use); footnote 19 (L230): `it is likely to remain appropriate to continue regulating the terms and conditions upon which Chorus supplies its layer 1 service`.
  L776: `There are no controls over what Chorus can charge for layer 1 services in the initial regulatory period.` followed by
  `In my opinion, that is curious`. Footnote 65 (L496): `it is difficult to imagine a scenario in which it would not be desirable for the Commission to determine a maximum price for layer 1 dark fibre services`.
  s.36 of the Commerce Act as an alternative: L785 `It is possible that Parliament anticipated`; L786 `(which, in my view, is far from clear)`;
  margin L803-805 `may not be an effective tool for addressing such concerns`.
- Revenue cap and wash-up. L271: `the Act mandates the application of an initial revenue cap (until the reset date), with wash-ups`,
  introduced with `This is presumably one of the key reasons`. L273: `it is theoretically possible that it may never fully recoup its past costs`.
  L291: `there is a clear logic to the general architecture of the initial arrangements`, limited by footnote 31. L294: beyond the reset
  date `it is plausible that something quite different might be applied (such as individual price caps)`.
- Price-quality vs information disclosure. No position. "information disclosure" appears once, about airports (fn 34, L319).
  Other LFCs appear only as Enable (L38, 175, 377) and in a Commission quotation, `Chorus and the other LFCs` (L509).
- Timing. L139/L668: the two-year extension and 2022. L161: precise IM forms `would be premature at this stage`.
  L670: an efficiency review `before the revenue cap is set`.

## References to other organisations, people, statutes and documents

| Named | Lines | What D06 attributes to it |
| --- | --- | --- |
| Commerce Commission | throughout | Issuer of the New Framework Paper, 9 November 2018. Attributed views with page cites are listed under "New Framework Paper locators" above. Uncited attributions: proposes an IM with two cost categories (L681); `has also queried whether the IM should also specify the manner in which costs should be allocated across the different types of FFLAS` (L687); in the Part 4 process adopted the 67th percentile (L549) |
| Commerce Commission, 2010 reasons papers | fn 36 L321, fn 37 L323, fn 83 L757 | GPB pricing IM with high-level principles (pp.180-181); experts agreed firms recover some common costs from all services (p.68) |
| Spark New Zealand | L29, 153, 162, 189 | Client; also one of three operators signalling 5G deployment |
| Chorus | throughout | Regulated provider whose incentives are discussed; `Chorus clearly possesses substantial and enduring market power in those areas in which it is the provider of FFLAS` (L175) |
| Enable | L38, 175, 377 | Fibre network in Christchurch (`in Wellington and Christchurch, respectively`) |
| Vodafone | L38, 50, 175, 184, 189, 377, 398 | HFC network; `Vodafone acquired the HFC network in Wellington when it merged with TelstraClear in 2012`; 5G intentions |
| TelstraClear | L50, 184, 398 | Merged with Vodafone in 2012 |
| 2degrees | L189 | 5G intentions |
| Crown Infrastructure Partners | L93, 502, 590, 670, 792 | Counterparty to `the deeds with Crown Infrastructure Partners`, which contain `the obligations not to discriminate between access seekers when setting prices`; provides oversight of the UFB build (L670) |
| Oxera | L111, 561, 574, 621; fn 73 L569 | Estimated annual cost of severe outage events for regulated energy businesses; report dated 23 June 2014, p.72, prepared for the New Zealand Commerce Commission |
| Green et al; Orion | fn 28 L282 | Report for Orion, May 2014, pp.43-48, cited for non-zero stranding risks. D06 does not say whether this Green is the report's author |
| Electricity Authority | L312, 344, 355-361; fn 41-45 | Held the power to set pricing methodologies for electricity lines; `the EA is also moving towards more prescriptive pricing methodologies`; dissatisfied with distributors' tariff structures; principles `are voluntary and the EA therefore does not enforce compliance` (fn 43); consultation paper 30 May 2017 |
| Transpower | L357, 361 | Named in the EA's observations |
| Hilmer Committee | L419; fn 49 L428 | Quoted on efficiency and competition; `Committee of Inquiry into National Competition Policy (1993)`, August 1993, pp.3-5; Australia |
| Parliament | L241, 785 | Addressed copper/fibre pricing in two ways; possibly anticipated s.36 would deal with price squeezes |
| Minister | fn 23 L256 | Approves regulations setting anchor service speeds, specifications and maximum prices |
| Economic Development, Science and Innovation Committee | fn 74 L595 | Recipient of the Departmental Report on the Telecommunications (New Regulatory Framework) Amendment Bill, 20 April 2018 |
| Auckland, Wellington and Christchurch Airports | fn 34 L319 | Pricing decisions reviewed by the Commission under information disclosure |
| University of Auckland | fn 1 L47 | Author's degrees |

Not named in D06 (searched, zero hits): ACCC, Ofcom, High Court, merits review, Crown Fibre Holdings, Northpower, Ultrafast Fibre.
No court case is cited; "court" appears once, generically, in footnote 85 (L802). "merits" appears only in `competing merits` (L78, 438, 582).

## Figure and boxes

- Figure 4.1, `Figure 4.1: Allocation of common costs` (L699). No numbers. Labels as extracted (L707-719): `Costs directly attributable to FFAS`
  (three times, one printed as `Costs directly attributable to FFAS1`, L714); `Costs directly attributable to other regulated services` (L708);
  `Costs directly attributable to unregulated services` (L709); `Costs common across` / `FFAS and other regulated services` (L710-711);
  `Costs common across FFAS and unregulated services` (L712); `Allocation of common costs` twice (L713); `Common costs` twice,
  `All services`, `All FFAS` (L715); `Single fibre service` (L716); `The Commission has proposed to undertake this allocation` (L717);
  `The Commission has queried whether this additional allocation across individual fibre services is needed` (L718); `* Not to scale` (L719).
  Text describing it: three stacks, far left = all services, middle = all FFLAS, then a single fibre service (L688, fn 81 L692);
  `light blue boxes` are the shared costs (L700). The figure labels say "FFAS"; the body says "FFLAS". Colours and box sizes cannot be
  checked from the text capture (unresolved visual).
- Box 4.1, `Box 4.1: Potential effect of cost allocation on competition The Direct Fibre Access Service` (L724-735). Two customer options;
  DFAS price fixed at 2019 levels for the first regulatory period in real terms (L733).
- Box 4.2, `Box 4.2: Potential effect of pricing principles on competition Layer 1 vs. layer 2` price squeeze (L767-783). L771 says
  `The figure below illustrates.` No figure text follows; the illustration is absent from the capture (gap: image only).

## Footnotes that limit a body statement, and internal inconsistencies

Footnotes limiting the body:
- L191-192 says unbundled layer 1 supply is required from 1 January 2020 `on all parts of its fibre networks`; footnote 13 (L205) adds
  1 January 2026 for the UFB second-phase network. Box 4.2 (L769) repeats the 2020 statement with no footnote.
- L245 says Parliament acted `by defining` anchor services; footnote 23 (L256) says `Note that the anchor services themselves are not specified in the Act.`
  and that speeds, specifications and maximum prices are set in regulations approved by the Minister.
- Footnote 23 (L256) says a cost-based price `cannot be introduced until the second regulatory period`; footnote 63 (L494) says
  `Section 206(6) states that, after the start of the first regulatory period, the Commission may recommend` a maximum cost-based price
  for an anchor service. Both are recorded as printed.
- L247 says there are no explicit price controls on FFLAS or copper where Chorus is not the LFC; footnote 21 (L252) adds that where
  FFLAS is not available copper stays regulated at 2019 levels with inflation adjustments; footnote 25 (L259) says
  `In areas in which Chorus supplies both FFLAS and copper services, the latter will be deregulated.`
- L291 `there is a clear logic to the general architecture of the initial arrangements`; footnote 31 (L301) makes this conditional:
  `Note that this is under the assumption that the revenue cap is formulated in a way that recognises that Chorus will continue to supply copper services`.
- L312 `little point in preparing a pricing IM for the three monitored airports`; footnote 34 (L319) notes the Commission has since assessed
  airport pricing efficiency under information disclosure; footnote 35 (L320) notes a statutory consultation obligation.
- L482 says Part 4's list `explicitly included pricing methodologies`; footnote 60 (L489) adds that s.52T(b) exempted the Commission
  where another regulator such as the EA had the power.
- L551 the Commission `was not suggesting that there would be an` investment strike; footnote 72 (L567) gives its reason (Asset Management Plans
  and quality standards; NFP footnote 133).
- L574 UFB does not work in a power outage `(without a backup75)`; footnotes 75-76 (L596, L598): batteries may be unaffordable;
  `Unless there is widespread back-up for UFB services, the costs of a power outage should therefore be higher than a fibre network failure.`
- L219 on possibly not regulating layer 2; footnote 19 (L230) says layer 1 regulation is likely to remain appropriate.
- L128 efficiency examination; footnote 5 (L139) gives the reasoning (spending up to 2022 can enter the initial RAB).
- L275 mature Part 4 networks did not face the challenges to the same extent; the same sentence and footnote 28 add that stranding risks were non-zero.

Internal inconsistencies and slips (recorded as printed):
- Box numbering: the text refers to `Box 5.1` at L706, L765 (`are set out in Box 5.1`) and L785; no Box 5.1 exists. The price-squeeze box is `Box 4.2` (L767).
- "FFAS" for "FFLAS": L219 `hinges critically upon how the FFAS IMs are designed`; L748 `a FFAS is deregulated`; all Figure 4.1 labels.
- L219 `If this type of layer 1 bundling is sufficiently widespread` (the surrounding text is about unbundling).
- Footnote 65 (L496): `sales of level 2 services` ("level", elsewhere "layer") and `maximum prices cannot not be determined before a s.207 review`.
- Footnote 75 (L596): `It is possible to purchase a battery backup for a USB connection` (the surrounding text is about UFB).
- Strength of the avoidable-cost statement differs by location (L132/L817 `one approach that should arguably be`; L739 and L758 without "arguably").
- Margin vs body strength: L86 margin `ensuring it does not foreclose competition` vs L74 `does not unduly affect competition`;
  L119 margin `There are likely to be fewer concerns` vs L107 `there may be less cause to be concerned`.
- Section four's coverage is stated as three matters at L160 and L632 (asset valuation, cost allocation, pricing principles); L416
  names two with "such as": `core matters such as asset valuation and cost allocation`.
- Which prices are controlled in the first period, by service (different services, both statements recorded): anchor services and
  DFAS set directly (L341-343; L733); layer 1, L776 `There are no controls over what Chorus can charge for layer 1 services in the initial regulatory period.`

## Extraction artifacts (affect search)

- Footnote markers are fused to words or stranded on their own lines: L483 `s.20663 or s.20764` is "s.206" + marker 63 and "s.207" + marker 64;
  L192 `2020,13`; L245 `service22`, `service)23`, `prices,24`, `prices;25`; stranded markers at L243 (`21`), L310 (`33`), L354 (`43`), L539 (`71`);
  markers starting a line at L31, 194, 216, 275, 313, 343, 464, 504, 512, 537, 786.
- Margin text spliced into body sentences: L776-780 (`Chorus may have an incentive to` ... `1 competitors.`) interrupts the body sentence that
  resumes at L783 `Chorus is likely to have to discourage uptake of the service`; L707-719 (Figure 4.1 labels) interrupt `(see` ... L722 `the example in Box 4.1)`.
- Dropped line-break hyphens: `pricequality` (L220), `longerterm` (L105, 298, 615), `longterm` (L312), `infrastructurebased` (L186),
  `nondiscriminatory` (L769), `nonexhaustive` (L482), `peer-topeer` (L355), `overallocating` (L679), `endusers` (L195), `futureproofing` (L545).
- Hyperlink text without targets: `can be found: here.` (fn 41-42, L348-349); `(available: here)` (fn 44, L367).
- Nothing looked truncated. The text ends with the 4.4 summary and its two margin notes (L823-826) and the marker `-----` (L828).

## Shared ground from D06's side (keyword hits in other documents; hit lines only, not read in context by this mapper)

- "Axiom": D07 lines 72, 77, 229, 246, 264, 267, 269, 272, 274, 286, 288, 290, 354, 405, 409, 441, 563, 621, 721. No hit in D01-D05 or D08.
- "Oxera": D07 lines 84, 90, 109. No hit elsewhere outside D06.
- "67th percentile", "75th", "$1b": no hit outside D06.
- "avoidable cost allocation": D04 line 427.
- "9 November 2018": D01 line 33; D02 line 29; D04 lines 52, 61, 66.
- "1 December 2011": D03 line 159; D07 line 460.
- "1 January 2020": D01 line 87. "1 January 2026": no hit outside D06.
- "two-year extension": D04 line 139.
- "100/20": D04 line 174; D05 lines 81, 83; D08 lines 417, 499, 501, 506, 520.
- "TelstraClear": D02 line 64.
- "pricing principles": D07 lines 28, 49, 51, 251, 281, 282, 289, 405, 406, 409, 598; D08 lines 54, 194, 523, 526.
- Relationship located in D06 itself: D06 responds to the Commission paper of 9 November 2018 and is written for Spark. By manifest
  file name only (not read here): D07 is a Spark submission; D03 and D04 are "emerging views" items; no manifest file name carries
  the 9 November 2018 paper's title, so D06's New Framework Paper page cites (p.33 to p.95, footnotes 133 and 162) point outside
  the eight files unless another mapper finds that text.

## Gaps

- Unread ranges in D06: none.
- Visual: the Box 4.2 illustration is absent; Figure 4.1 survives as labels only (layout, colours and box sizes unresolved).
- Cross-document claims above are keyword hits only; the passages in D01-D05, D07 and D08 were not read by this mapper.
