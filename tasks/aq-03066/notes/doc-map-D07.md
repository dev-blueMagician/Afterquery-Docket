# aq-03066 - D07 document map (single-document full map, for merging into doc-map.md)

Navigation only: where things are in `text/D07.txt`, not what to ask. Questions quote the
document, never this map. Line numbers (`L`) are `text/D07.txt` lines. The `docs/` original
is the same text two lines earlier (docs line = text line - 2; checked at L97, L397, L460, L676).
Quotes in backticks are copied verbatim from the extraction, including its typos.

## Binding and coverage ledger

- Source: `docs/nzcc_fibre_im_r1_framework_spark_submission_on_new_regulatory_framework_for.txt`
- Source sha256 (text/manifest.json): `71f962b5fb068a477a4ca08cc94ebe2aaeddbbb2e0acd8e234fcca49b9790a8a`;
  method `text`, pages `null`, chars 83131. notes/intake.json number 5 has the same captured and
  source sha256, `incomplete: false`, `gap_characters: 0`, `matches_capture: true`.
- Task-page label: "Doc 5" (intake number 5) = D07.
- Lines read, sequentially: L1-180, L180-369, L369-548, L549-725. Unread: none. File ends
  L723 `[END]`, L725 `-----`.
- Whole-file searches run on D07 (results folded in below): `%`, `$`, percentile, million,
  billion, Mbps; four-digit years; number words; `Q\d+`; hedge words (86 hits); conditionals
  (if / unless / to the extent / where possible / subject to / proviso); named-organisation
  negatives (see section 5).
- Extraction spot-checks against the docs original: page markers `Part 6 Implementation Public
  Version N` occur 26 times in both files (N = 1 to 26); one table row (`right first-time
  resolve %`, L676) and one footnote (fn 17, L397) are identical in the original. The original is
  itself plain text, so the table's column layout and any figure cannot be inspected: unresolved.

## 1. Identity and structure

- Title line L3: `New regulatory framework for fibre: proposed approach`
- L4: `Submission | Commerce Commission`
- Date L5: `21 December 2018`
- Author: the word "Spark" does not occur anywhere in D07's own text (case-insensitive search;
  the only hit is the file-name header at L1). The body speaks as "we"/"our". Authorship rests
  on the file name and on D06 (see Shared ground). No signatory, address or contact person is
  printed.
- Running header: `Part 6 Implementation Public Version 1` (L10) through `... Version 26` (L705).
  "Public Version" is printed; no confidential markers or redactions appear.
- Paper responded to, L57: `the fibre regulatory regime set out in Part 6 of Act (the approach paper)`.
  D07 never prints the approach paper's own title or date. It is cited by paragraph only
  (section 5). L68: `This submission generally follows the structure of the approach paper:`
- Other Commission papers named: `its earlier IM funding paper` (L90, no date); the fibre study
  (L379, L395, L535, L558); `The CEPA paper` / `the CEPA report` (L628, L637).
- Attachment, L77: `An Axiom Economics (Axiom) expert report is attached.` and
  `We asked Axiom to set out its thinking on the issues the Commission should consider through the early phases of the IMs process.`
  D07 names no individual Axiom author. No appendices or annexes in D07.
- Numbered paragraphs: 1 to 129 (L57 to L721). Footnotes: 1 to 32. Commission questions
  quoted: Q1, Q3 to Q29 (Q2 is not quoted anywhere); order as printed puts Q12 (L235) between
  Q5 (L206) and Q6 (L293).

### Contents line (L8), 23 entries with printed page numbers

Executive Summary 1; Introduction 3; Context within which utility regulation will be applied 3;
Process for developing the fibre input methodologies 3; Purpose statements and relevance of
Part 4 to IMs, s174 purpose 4; Practical application of s166(2)(b) 9; Approach to Input
Methodologies: Part 4 as a starting point for fibre IMs 10; Key issues for implementing Part 6
in our context 10; Economic principles potentially relevant to our new regime 11; Whether
Part 6 requires a BBM model 11; Economic principles in decision making 12; The proposed
economic principles 13; Cross-cutting features of input methodologies 14; Scope of regulated
services 14; Matters for which input methodologies are determined 16; Asset Valuation 16;
Scope of the regulated asset based and its valuation 16; Calculation of initial losses and
Crown financing 17; Other 21; Allocating common costs 21; Using Part 4/FPP approach to WACC 23;
Scope of the quality dimensions input methodology 24; Input methodologies that support the
setting of price quality paths 25. Heading levels are not marked in the extraction. All 23
printed page numbers agree with the running-header pages where the headings fall.

### Body headings with line ranges

| Heading (as printed) | Lines | Paras | Questions quoted |
|---|---|---|---|
| Executive Summary | L11-53 | unnumbered | none |
| - `Other key issues that the Commission will likely face` (not in Contents) | L42-51 | unnumbered | none |
| Introduction | L56-77 | 1-6 | none |
| Context within which utility regulation will be applied | L78 | - | - |
| - Process for developing the fibre input methodologies | L79-97 | 7-12 | Q1 |
| - Purpose statements and relevance of Part 4 to IMs, s174 purpose | L99-231 | 13-36 | Q3, Q4, Q5 |
| -- `Similarities with Part 4` (not in Contents) | L102-127 | 13-17 | |
| -- `Section 166` (not in Contents) | L129-146 | 18-19 | |
| -- `Section 166(2)(b)` (not in Contents) | L148-200 | 20-27 | |
| -- `Consumers v end-users` (not in Contents) | L201-204 | 28-29 | |
| -- (Q5, s174) | L206-231 | 30-36 | Q5 |
| - Practical application of s166(2)(b) | L233-254 | 37-41 | Q12 |
| - Approach to Input Methodologies: Part 4 as a starting point for fibre IMs | L256-264 | 42-44 | none |
| Key issues for implementing Part 6 in our context | L266-290 | 45-50 | none |
| Economic principles potentially relevant to our new regime / Whether Part 6 requires a BBM model | L292-309 | 51-55 | Q6 |
| - Economic principles in decision making | L311-331 | 56-59 | Q7, Q8, Q9 |
| - The proposed economic principles | L332-362 | 60-66 | none |
| Cross-cutting features of input methodologies / Scope of regulated services | L363-400 | 67-73 | Q10, Q11 |
| - Matters for which input methodologies are determined | L402-409 | 74-76 | Q13, Q14 |
| Asset Valuation / Scope of the regulated asset based and its valuation | L410-441 | 77-83 | Q15, Q16, Q17 |
| -- `Assets that can be included in the regulated asset base (RAB)` (not in Contents) | L414-430 | 77-81 | |
| - Calculation of initial losses and Crown financing | L443-544 | 84-105 | Q18, Q18a, Q18b, Q19, Q20 |
| Other / Allocating common costs | L546-598 | 106-119 | Q21, Q22 |
| -- `Cost allocation input methodology` (not in Contents) | L550-574 | 106-110 | |
| -- `Allocation of common costs must not exceed standalone cost` (not in Contents) | L576-583 | 111-114 | |
| -- (Q22, pricing methodologies) | L584-598 | 115-119 | Q22 |
| - Using Part 4/FPP approach to WACC | L600-621 | 120-122 | Q23, Q24 |
| - Scope of the quality dimensions input methodology | L623-699 | 123-127 | Q25, Q26 |
| - Input methodologies that support the setting of price quality paths | L701-721 | 128-129 | Q27, Q27a-c, Q28, Q29, Q29a-d |

Page starts (running header lines): p1 L10, p2 L38, p3 L55, p4 L87, p5 L113, p6 L140, p7 L165,
p8 L193, p9 L223, p10 L250, p11 L278, p12 L297, p13 L324, p14 L349, p15 L372, p16 L399,
p17 L427, p18 L451, p19 L477, p20 L510, p21 L534, p22 L562, p23 L588, p24 L615, p25 L648,
p26 L705.

## 2. Numbers (complete inventory)

Negative finding first: D07 prints **no** money amount, no percentage value, no percentile, no
WACC or cost-of-capital parameter value, no connection or premises count, no price, no speed
value and no duration. `%` occurs only inside a URL (L322) and as a metric label with no value
(L676, `right first-time resolve %`). `$`, "percentile", "million", "billion", "Mbps" have no
hits. Every number in the document is a date/year, a statute or paragraph reference, a network
layer, a list ordinal or a small count in words.

### Dates and years

| Line | Value | What it is | Whose | Quote |
|---|---|---|---|---|
| L5 | 21 December 2018 | date of the submission | own | `21 December 2018` |
| L12, L22 | 1986 | year in statute name | statute | `Part 4 of the Commerce Act 1986 (Part 4)` |
| L13 | 2001 | year in statute name | statute | `Part 6 of the Telecommunications Act 2001 (the Act)` |
| L36 | 2020 (three times) | boundary year between the two frameworks; executive summary only | own characterisation | `from the period preceding 2020 in that RAB`; `the overlap between the pre-2020 regulatory framework`; `the post-2020 regulatory framework,` |
| L53, L111, L138, L508 | 2013 | year of High Court judgment | case citation | `[2013] NZHC 3289` |
| L85 | March 2018 | date of Oxera article (fn 2) | third party (Oxera) | `March 2018 https://www.oxera.com/agenda/legitimacy-renationalisation-utility-regulation/` |
| L88 | December 2018 | month of a workshop at which InternetNZ spoke | own recollection of a third party | `as InternetNZ reminded us at the December 2018 workshop` |
| L97 | January 2019 | month to which emerging views and Draft IMs papers could be pushed | own suggestion | `pushing the emerging views and Draft IMs papers out to January 2019` |
| L163 | 2007 | year of Supreme Court judgment (fn 6) | case citation | `Unison Networks Ltd v Commerce Commission [2007] NZSC 74` |
| L189 | 4 May 2018 | date of Select Committee report (fn 8) | third party | `Amendment Bill (4 May 2018)` |
| L226 | 2017 | year of Electricity Authority consultation | third party | `The Electricity Authority stressed in its 2017 consultation` |
| L248 | 4 October 2017 | date of the Electricity Authority document (fn 12) | third party | `Response and next steps decision 4 October 2017` |
| L322 | 2013, 0513 | inside an EY URL only (fn 14) | URL | `Mapping_Power_and_Utilities_Report_2013` |
| L395 | 17 December 2018 | date of the Commission fibre study (fn 16) | Commission | `16 Commission Study in to fibre services 17 December 2018 [23].` |
| L460 | 1 December 2011 | start of the period for financial losses under the UFB initiative | statute as described by author | `between 1 December 2011 and the implementation date under the UFB initiative` |
| L531, L532 | June 2010 | date of the Commission's EDB input methodologies Draft Reasons Paper (fn 22, 23) | Commission | `Draft Reasons Paper June 2010 at [3.3.21]` |
| L556 | 2015 | year of the Commission UCLL determination (fn 24) | Commission | `[2015] NZCC 37 at [B66] to [B70]` |

- The "implementation date" is never given a calendar date in D07 (L403, L432, L436, L460,
  L486, L590; `implementation day` at L441). The only year attached to the change of framework
  is "2020" in the executive summary (L36).
- The same loss period is described two ways: executive summary `the period preceding 2020`
  (L36); body `between 1 December 2011 and the implementation date` (L460).
- "January 2019" (L97) is the only forward-looking date. D07 does not print the Commission's
  proposed timetable dates. The sentence in full: `This could be done within the proposed timetable by pushing the emerging views and Draft IMs papers out to January 2019, resolving matters earlier de-risks process and provides certainty earlier.`

### Counts stated in words or digits

| Line | Count | Of what | Whose | Quote |
|---|---|---|---|---|
| L15-17 | 3 (numbered 1-3) | consequences of substantial market power | own | `As a starting point, that means:` (L13) |
| L288 | two | implications Axiom touches on | attributed to Axiom | `Axiom touch on two specific implications of the contextual matters discussed above.` |
| L312, L314 | three | key economic principles used under Part 4 | Commission (Q7, Q8 wording) | `the three key economic principles used under Part 4` |
| L328 | three | same, restated | own restatement | `the three key principles applied to Part 4 regulation` |
| L405 | one | additional IM suggested | own | `The one additional, but important IM we would suggest the Commission commits to developing, is a pricing principles IM.` |
| L448 | two | methods for reflecting Crown financing cost | Commission (Q19 wording) | `the two methods outlined above for reflecting the actual costs of Crown financing` |
| L452 | two | factors missing from the Commission approach to losses | own | `there are two key factors we consider are missing` |
| L520 | double or triple; three | counting of shared costs; types of regulated services an EDB may supply | Commission 2010 draft paper, quoted | `can result in the double or triple counting of shared costs`; `if the EDB supplies all three types of regulated services` |
| L535 | one, two | networks, technologies | attributed to Chorus via the s9A study | `Chorus considers that it operates one network that includes two technologies, copper and fibre` |
| L699 | two | "latter categories" of the quality table | own | `The two latter categories would need to reflect access seeker capabilities` |
| L269, L272, L328 | several | differences; themes; additional principles | Axiom / Axiom / Commission paper | `there are several crucial differences between FFLAS and the sectors regulated under Part 4` |

### Network layers and technology labels

- `layer 2`: L174 (Commission quote), L365 (Q10), L384, L405 (twice). `layer 1`: L405.
  `layer 3`: L391. `5G`: L158 `at the wholesale level (eg fixed wireless, 5G); and`.

### Statute sections (all are references, none a quantity)

- Telecommunications Act Part 6: s162 (L45, L99, L101, L103, L119, L127, L130, L136, L144,
  L145, L252, L286, L518); s166 (L130-141, L144-145, L210, L252, L293, L319, L352, L389);
  s166(2) (L135, L150, L156, L161, L168, L179, L279, L620); s166(2)(b) (L45, L99, L101, L141,
  L148, L175, L180, L185, L196, L198, L200, L233-254, L261, L286, L428, L574); s174 (L206,
  L212); s175(1) (L403); s176(2) and (2AA) (L444, Commission Q18 only); s176(3A) (L473, Select
  Committee quote only); s177 (L416, L488, L540, L542); s177 subsection (1) (L462); s177(2)
  (L460, L489 as `s177(2)`, L524); s177(3) (L466, L538); s177(5) (L464); s181 (L210);
  ss194(3) and (4) (L633); s201 (L589); s205 (L179, L254); s9A (L379, L535, L558).
- Commerce Act: Part 2 (L179, L254); Part 4 (throughout); s52A (L103); s52A(1) (L39, L120,
  L513); s52A(1)(a) to (d) (L120); s52A(1)(c) and (d) (L520); s52T(3) (L430).

### Paragraph and page pinpoints in cited sources

- Approach paper: [5.34] fn 7 L187; [5.39.3] fn 9 L191 and fn 10 L218; [5.69] fn 11 L221;
  [6.45] fn 13 L276 and fn 15 L347; [6.45.3] fn 30 L611; [6.52] fn 31 L613; [7.26] and
  `footnote 149` fn 17 L397; [7.43] fn 29 L609; [7.66] fn 19 L506; [7.80] fn 26 L560;
  `footnote [162]` fn 28 L607.
- Wellington Airport judgment: [758] to [760] fn 1 L53 and fn 20 L508 (text at L499, L511,
  L513); [14], [15], [18] and [21] fn 4 L111; [29] fn 5 L138; [228] fn 6 L163; [605] fn 21
  L529; [1809] fn 27 L586.
- Select Committee Report: `at 4` fn 8 L189 and again fn 18 L475 (two different passages).
- Electricity Authority: paragraph `3.5` L227. Commission fibre study: `[23]` fn 16 L395;
  `[44.1]` fn 25 L558. EDB Draft Reasons Paper: `[3.3.21]` fn 23 L532. NZCC 37: `[B66] to
  [B70]` fn 24 L556. EY report: `page [18]` fn 32 L646.

## 3. Enumerated lists

### Executive summary lists

| Id | Lines | Heading / lead-in | Items |
|---|---|---|---|
| ES-1 | L15-17 | `As a starting point, that means:` (L13) | 3 numbered: (1) no meaningful competitive constraints on FFLAS; (2) power to set prices, terms and conditions substantially different from competitive markets; (3) incentive and ability to prevent new competitive constraints and distort downstream and adjacent markets |
| ES-2 | L26-34 | `In our view, the list of differences will include:` | 4 bullets: `Pricing Principles IM;` / `FCM;` / `Asymmetric social consequences;` / `Cost allocation.` |
| ES-3 | L43-51 | `Other key issues that the Commission will likely face`; lead-in `This will likely require first principle consideration of key IM parameters, for example:` | 4 bullets: (i) IMs and Price/Quality paths that do not unduly affect competition from potential rivals; (ii) efficient incentives and allocation of risks; (iii) setting out key pricing principles; (iv) erring towards more prescriptive IMs |

### Executive summary compared with the body (locations only)

- ES-2 has no body list under the same lead-in. Its four labels sit in the body at: pricing
  principles IM para 74 L405; FCM para 63a L343-350; asymmetric consequences para 63c L354;
  cost allocation paras 106-114 L551-583. The word "social" occurs once in D07, at L32; the
  body item reads `Asymmetric consequences of over and under-investment.` (L354).
- Body para 63 (L340-354) has three lettered items: a FCM; b `The Commission should look to allocate risk to where it is best addressed.`; c asymmetric consequences. Item b (risk
  allocation) is not a bullet in ES-2; ES-2's "Pricing Principles IM" and "Cost allocation"
  are not items of para 63.
- ES-3 is stated in the author's own voice. The nearest body list, para 47 a-d (L272-284), is
  attributed: `Axiom notes that these contextual matters give rise to several principles`.
  - ES-3 (i) L45 corresponds to 47a L274; ES-3 (iii) L49 to 47b L281; ES-3 (iv) L51 to 47c L282.
  - ES-3 (ii) L47 `To determine efficient incentives and allocation of risks in this markedly different context` has no item in para 47; related body text is para 11 L95 and para 63b L352.
  - Para 47d L284 (reduced concern about under- versus over-investment; weaker justification
    for a WACC uplift) is not a bullet in ES-3.
  - ES-3 (i) says the IMs and paths `should support the complementary s162 and s166(2)(b) aims` (L45); 47a says they can be reached `without compromising the objective in s.166(2)` (L279).
- The four "core" methodologies named for prescription are the same in three places: L51
  `asset valuation, cost allocation, the cost of capital and any pricing principles`; L282;
  L409. ES-3 (iv) gives the purpose as `to promote competition over time` (L51); 47c gives the
  reason as Chorus incentives `to foreclose competition` (L282).
- ES-1 is not restated as a list in the body.

### Body lists

| Id | Lines | Para | Lead-in (quote) | Items |
|---|---|---|---|---|
| B-1 | L68-75 | 5 | `This submission generally follows the structure of the approach paper:` | 4 (a-d): context incl. purpose statements; key issues (draws on Axiom); economic principles and cross cutting technical features; specific Part 6 issues `including asset valuation, allocation of common costs and WACC` |
| B-2 | L88, L95 | 8, 11 | `First, the approach paper` / `Second, the paper highlights` | 2 process suggestions (end-user engagement; more time earlier on key approach decisions), previewed in para 7 L82 |
| B-3 | L91-94 | 10 | `we encourage the Commission to consider:` | 2 (a, b) joined by `and/or`: add a consumer expert to the advisory panel; ask the panel to apply an end-user lens |
| B-4 | L144-146 | 19 | `This is because:` | 2 (a, b) |
| B-5 | L152-166 | 21 | `In our view:` | 3 (a-c); item b has sub-items i wholesale level (fixed wireless, 5G), ii retail level |
| B-6 | L168-174 | 22 | `The Commission suggests that particular areas where section 166(2) will be relevant include:` | 2 (a wireless substitutes; b access-based competition) - the Commission's list, not the author's |
| B-7 | L177-183 | 24 | `In our view:` | 2 (a, b); item b has sub-items i service-level cost allocation rules and disclosure, ii pricing methodologies |
| B-8 | L196-199 | 26 | `Instead:` | 2 (a, b) |
| B-9 | L214-224 | 33 | `these investments will be promoted by:` | 2 (a, b); split across pages 8-9 by footnotes 10-11 |
| B-10 | L240-251 | 39 | `s166(2)(b) considerations will likely be key to almost all parameter decisions, for example:` | 4 (a assets admitted to the RAB; b RAB approach to geographic deregulation; c specification of allocation rules; d prescriptive pricing principles methodologies) |
| B-11 | L259-262 | 43 | `different approaches if required by:` | 2 (a s166(2)(b); b differences between the sectors) |
| B-12 | L269 | 46 | `For example, there is more potential` | 3 differences in one sentence (impact on actual competition; copper-to-fibre transition; higher probability the framework changes) plus a separate sentence on pricing efficiency - attributed to Axiom |
| B-13 | L272-284 | 47 | `several principles or 'themes' that cut across many of the IMs:` | 4 (a-d) - attributed to Axiom |
| B-14 | L288-289 | 49 | `two specific implications` | 2 (First: allocate a portion of shared asset costs to other services; Second: cost allocation and pricing efficiency) - attributed to Axiom |
| B-15 | L303-305 | 53 | `In the case of Part 6:` | 2 (a, b) |
| B-16 | L327-330 | 58 | `Economic principles are implicit to, or underly, many statutory decisions:` | 2 (a, b) |
| B-17 | L335-337 | 61 | `the helpful principles will become apparent through the Part 6 process:` | 2 steps (a first, b second) |
| B-18 | L340-354 | 63 | `the proposed principles are unlikely to apply in the same manner:` | 3 (a FCM; b risk allocation; c asymmetric consequences) |
| B-19 | L358-360 | 65 | `that could:` | 2 (a, b) joined by `but` |
| B-20 | L373-379 | 69 | `FFLAS potentially captures a wide range of services that enable access to the fibre network:` | 3 (a codified; b less distinct; c apparent over time) |
| B-21 | L382-385 | 71 | `will likely need to be considered more fully, for example:` | 2 (a, b) |
| B-22 | L387-390 | 72 | `the Commission will likely need to consider:` | 2 (a, b) |
| B-23 | L416-418 | 77 | `"fibre asset" is defined to mean an asset that is:` | 2 (a, b) joined by `and` - statutory definition as the author states it |
| B-24 | L422-425 | 79 | `For example:` | 2 (a, b) |
| B-25 | L438-441 | 83 | `We expect that the Commission will need to:` | 2 (a, b) |
| B-26 | L452-456 | 84 | `two key factors we consider are missing` | 2 (a time period; b total revenue incl. copper revenues) |
| B-27 | L466-469 | 89 | `Section 177(3) further constrains` | 2 (a, b) |
| B-28 | L481-484 | 91 | `designed to achieve a balance between:` | 2 (a, b) |
| B-29 | L489-493 | 94 | `The added difficulties in applying s177(2) in light of the purpose statement include that:` | 3 (a-c) |
| B-30 | L499-504 | 96 | `[758] We have already explained why we agree with the Commission that initial RAB values have:` | 3 ((a)-(c)), each `little or no impact` - High Court quote |
| B-31 | L539-543 | 104 | `This would mean:` | 3 (a-c) |
| B-32 | L567-572 | 109 | `it will be important that:` | 3 (a-c); a and b begin `Where possible` |
| B-33 | L616-620 | 121 | `The matters that it will need to carefully consider include:` | 2 (a, b) |

### Short in-sentence item sets

- Part 4 sectors, L12: `electricity distribution businesses, gas pipeline operators and airport owners` (3).
- Typical regulator aims, L59: `affordability of services, investment, and efficiency` (3).
- Key utility model settings, L82: `(eg incentives, risk, promotion of competition)` (3); L95 `incentives, risk allocation and promotion of competition`.
- Efficiency components (High Court), L107: `technical efficiency, allocative efficiency and dynamic efficiency` (3).
- Codified access services, L376: `a wholesale broadband access, DFAS and unbundled fibre access` (3).
- Uses of the Ethernet Aggregation Switch, L384: `regulated fibre broadband services, copper bitstream services, and other national transport and access services` (3).
- Current framework components, L525: `regulated broadband and voice access price caps, UFB agreements and Crown funding`, introduced by `for example`.
- Items set aside in the alternative loss approach, L539: `setting aside operating costs, tax and depreciation` (3).
- Shared-use asset examples in electricity, L565: `(eg batteries, solar and meters)` (3).
- Industry-specific WACC parameters, L605: `(eg asset beta, leverage and credit rating)` (3).
- Commission approach quoted at L552: `information disclosure regulation, customised price paths and individual price path regulation under Part 4` (3).

### Commission questions quoted (28 numbered, 9 lettered sub-questions)

Q1 L80; Q3 L99; Q4 L101; Q5 L206; Q12 L235-236; Q6 L293; Q7 L312; Q8 L314; Q9 L315; Q10 L365;
Q11 L367; Q13 L403; Q14 L407; Q15 L412; Q16 L432; Q17 L434; Q18 L444; Q18a and Q18b L446;
Q19 L448; Q20 L449; Q21 L548; Q22 L584; Q23 L601; Q24 L602; Q25 L624; Q26 L626; Q27 L701;
Q27a L703; Q27b L706; Q27c L708; Q28 L709; Q29 L713; Q29a L714; Q29b L716; Q29c L718;
Q29d L719. Q2 is absent. Answers are grouped, not one per question: the paragraph ranges per
question group are in the section 1 table. Q27, Q27a-c and Q28 share a single one-sentence
answer (para 128 L711); Q29a-d share one sentence (para 129 L721); Q19 and Q20 have no
separately labelled answer inside paras 84-105.

## 4. Positions by topic (hedge words kept)

Attribution key: [own] the author's statement; [Axiom] attributed to its expert; [Comm]
quoted or paraphrased Commission view; [HC] High Court; [SC] Select Committee.

### Overall framing and purpose statements

- [own] L12: `Our key interest is that the Commission’s proposed approach to implementing the new fibre regulatory framework gives best effect to the purpose of the new Part 6`
- [own] L20: `The competitive landscape in telecommunications is much more dynamic than that of the Part 4 sectors`; `In contrast, Part 4 asked the Commission to promote outcomes that were consistent with competition.`
- [own] L103: `The Part 6 purpose statement (Section 162 of the Telecommunications Act) is modelled on the Part 4 purpose statement (section 52A of the Commerce Act).`
- [own] L127: `section 162 requires the Commission to set input methodologies that only allow regulated suppliers to set prices that recover efficiently incurred costs and a reasonable return`
- [own] L145: `This language is not present in Part 4.` (the explicit direction in s166 to give effect to s162).
- [own, hedged "may not"] L156: `limiting prices to recover the efficient costs of providing FFLS may not be sufficient to comply with section 166(2)`
- [own, agreement] L185: `The Commission correctly notes that section 166(2)(b) is a mandatory relevant consideration`
- [own, disagreement] L196: `However, we disagree that section 166(2)(b) is only mandatory`; L198 `For every decision, the Commission must consider whether section 166(2)(b) is relevant; and`; L199 `Its decision on relevance must be objectively reasonable, eg supported by evidence.`
- [own, "expect"/"very cautious"] L200: `the Commission will need to be very cautious before determining that a particular decision can have no possible relevancy`
- [own, "not clear"] L202: `it is not clear how it could have a practical impact on the determination of input methodologies` (consumers versus end-users).
- [own, "could suggest"/"might"] L239: `The worked example could suggest an additive approach or that the competition consideration might be incidental.`
- [own, "likely"/"almost all"] L240: `s166(2)(b) considerations will likely be key to almost all parameter decisions`
- [own, "plausible"/"not clear cut"] L252: `a plausible interpretation of section 162 is that it is focused on markets for fixed fibre line services only`; `we consider that such an interpretation is not clear cut`
- [own, conditional "would support"] L252: `While we would support an interpretation of section 166 which recognise the interdependence of fibre markets and downstream services`

### Part 4 as starting point; level of prescription; s174 certainty

- [own, agreement] L257: `We agree that the general approach under Part 4 can inform the approach to Part 6, and that re-litigation of established principles should be avoided.`
- [own, should NOT] L259: `must not be equated to a presumption that the Part 4 approach is correct`; conditional `if required by:` L259-262.
- [Axiom] L270: `These differences mean the Commission should not simply import its approach from Part 4.`
- [own] L290: `the Commission can’t assume Part 4 methodologies will achieve the desirable Part 6 outcomes`
- [own] L208: `The purpose of IMs is to promote certainty relating to how regulation will apply to Chorus, access seekers and end users.`
- [own, agreement] L210: `We agree that promoting certainty does not mean that IMs are static and cannot be changed`; `Section 181 provides a framework for considering amendments.`
- [own, "likely"] L212: `there will likely need to be more emphasis on access seeker and end user requirements than was necessary under Part 4 considerations`
- [own, "likely"/"ideally"/"could"] L229: `We believe that while a mix of both is likely, there will also likely need to be a significant increase in the prescription applied to some IMs as set out in the Axiom report.`; `a high level of prescription will ideally need to be provided`
- [Axiom] L282: `That the Commission should err towards more prescriptive (as opposed to 'principlebased') IMs`
- [own citing Axiom] L409: `The IMs will likely be a mix of principles and specific requirements. As Axiom advise, the Commission should err towards a more prescriptive approach`

### BBM and economic principles

- [own] L294: `The Commission is right to question whether Part 6 objectives are best met through a BBM model.`; L295 `The Act does not require a specific model and there are many options available to the Commission.`
- [own, agreement, "likely"] L303: `We agree that, in practice, Part 6 regulation is likely to be a building block model approach in its broadest sense`
- [own] L307: `will inevitably result in BBM implementation that differs from Part 4 approach and that applied in other jurisdictions, including Australia`
- [own, "may"] L317: `economic principles may be used to give effect to the purpose statement, but they do not replace the purpose statement`
- [own, proviso] L331: `with the proviso that they should be used cautiously as a tool to help make better decisions required by the Act, and not as a complete answer to the statutory requirements`
- [own, "unlikely"] L340-341: `the proposed principles are unlikely to apply in the same manner`
- FCM [own, "likely"/"unlikely"] L343: `no regulatory framework is required to guarantee a return`; L345 `the principle will likely be difficult to apply in this context`; L350 `Applying FCM to the Part 6 financial model in isolation is unlikely to deliver the desirable end user outcomes.`
- Risk allocation [own, "suspect"/"likely"] L352: `We suspect this will likely be largely an empirical exercise`; `a natural hedge likely exists for key uncertainties such as fibre volumes`
- Asymmetric consequences [own citing Axiom] L354: `As set out in the Axiom paper we don’t see the same investment consequences in the fibre network setting`
- Pricing efficiency [own, agreement; conditional "If ... could"] L358: `We agree that pricing efficiency is also an important consideration.`

### Scope of regulated services (FFLAS); anchor services; unbundling

- [own, agreement] L368: `We agree the scope of regulated services is important`
- [own, "appears"/"potentially"] L373-374: `The regulatory scope appears to be defined by both the technical extent of the Fibre Network and FFLAS`; `FFLAS potentially captures a wide range of services`
- [own] L378: `Chorus provides the 2Degrees national backhaul network and is trialling a wi-fi access service`; hedge `While it is unclear what fibre network inputs might be used for these services`
- [own] L380: `the regulated services may change over time, but they still need to be defined/assessed by reference to the defined physical infrastructure`
- [own, conditional "if left unchecked"] L385: `Chorus should be expected to act on incentives, if left unchecked, to design services in a way that maximises the scope of RAB or allocation of costs`
- [own, "will likely need to consider"] L389: `Taking a more prescriptive approach to defining FFLAS than the principles set out in the approach paper`; `We expect that related company principles will have a key role in the regime`
- [own, "We believe", does NOT extend] L391: `We believe that the FFLAS service description does not extend to wireless or layer 3 elements of the networks, irrespective of LOB restrictions.` Footnote 17 (L397) attaches here; see section 8. Continuation L393/L400: `are not directly related to access to the fibre network - eg could include CDNs and switching – and are not required.`
- Anchor services: one mention only, as a description of the Act. L589: `The Act contains a scheme for determining prices for anchor products, and section 201 requires Chorus to set geographically consistent prices.` No position on which services should be anchor services.
- Unbundling: mentions only. L174 [Comm quote] `an RSP has the choice between purchasing layer 2 bitstream services and investing in unbundled fibre services`; L376 `unbundled fibre access` listed as a codified access service; L405 `layer 1 access products that support competitive layer 2 services`. No stated position on unbundling terms or price.
- Geographic deregulation [own, "potentially"] L244: `permitting the automatic recovery of the cost of those assets where the provider is subject to competition will potentially distort competition`

### Pricing principles / pricing methodologies

- [own, "may be desirable"] L183: `pricing methodologies may be desirable.`
- [Axiom] L281: `the Commission should avail itself of its broad power to determine IMs to prepare a methodology articulating some key pricing principles`
- [own, "would suggest"] L405: pricing principles IM is `The one additional, but important IM we would suggest the Commission commits to developing`
- [own] L406: `A more prescriptive pricing principles IM will be important to help guard against the incentive to price in a way that undermines the competitive outcomes`
- [Comm, as reported] L589: the Commission's list of mandatory IMs `excludes pricing methodologies` (fn 28) and `It also states that it only proposes to determine the mandatory input methodologies.` (fn 29).
- [own, "must consider whether"] L590: `we think the Commission must consider whether further pricing methodologies are required to be in effect at the implementation date`; L591 `specifying a maximum price for a service may be insufficient to achieve the purpose statements`
- [own, "could be considered"] L598: `The same type of approach could be considered under Part 6.`; `Chorus and LFCs would be required to disclose how their pricing is consistent with those principles`

### Initial RAB / asset valuation

- [own] L36: Part 6 `provides greater direction to the Commission on the starting value of the RAB`
- [own] L420: `The statutory provisions relating to the starting RAB are also more prescriptive than they are under Part 4.`
- [own] L422: `it does not follow that the Commission has little or no discretion to set rules to determine what assets can be included in the RAB`
- [own, "may be relevant"] L428: `it may be relevant to take a more prescriptive approach to the asset valuation methodology than its Part 4 counterpart`
- [own] L430: `Part 6 does not include an equivalent to section 52T(3) of Part 4`; `This suggests that, compared to Part 4 entities, Parliament is more concerned`
- [own, "unclear"] L436: after noting the Commission proposes cost for post-implementation assets, `The Act defines the initial value as of the asset as being the cost incurred.`
- [own, "We expect"] L440: `measures to ensure that legacy copper assets do not inefficiently transition in to the regulated fibre business`
- [own, "should"] L441: `The Commission should allocate the cost of assets used to provide services in addition to FFLAS to those other services and consider the efficiency of the costs incurred on the UFB build between now and implementation day.`
- Depreciation and revaluations: the Commission says in Q15 (L412) it has `not yet set out our views on the treatment of depreciation or asset revaluations`; D07 states no position on either. Other occurrences: L330 (High Court topic), L539 and L544 (losses).

### Past financial losses

- Period: L460 `between 1 December 2011 and the implementation date under the UFB initiative`; executive summary L36 `the period preceding 2020`.
- [own] L460: `"Financial loss" is not defined and must be determined by the Commission.`
- [own] L462: the loss asset `need not be determined on a` cost-incurred basis.
- [own, "should"; proviso] L464: `any estimate of past financial loss should be based on an estimate of efficiently incurred costs`; `The only proviso to this is under section 177(5), which allows costs to be recovered if it can be shown they were a direct result of meeting specific requirements of the UFB initiative.`
- [own] L454: `it cannot have been expected that material costs components will have been recovered prior to the commencement of the initial regulatory period`
- [own, "may well"] L456: `we consider that copper revenues were always designed as a means to cross-subsidise the costs of the fibre roll-out`; `may well have been compensated for by copper revenues`
- [own] L458: `determining accumulated unrecovered costs cannot be done without considering preferential funding terms and copper revenues`; recovery period `should be spread over the same period applied to other like costs (under the IMs)`
- [Comm] L486: `to require the use of a building blocks approach`
- [own, NOT required] L488: `the use of a building blocks methodology to calculate past losses is not required by the Act`
- [own, "likely"] L489: `This is likely to be a highly contended issue in the IMs process.`
- [own] L493: `The Commission must avoid double recovery`; L39 `It will be important for the Commission to ensure there is no double recovery during this period.`
- [own, conditional "where"] L495: `Past losses has no benefit for end users of the Fibre Network where these losses have not occurred in practice or are inflated by, for example, double counting.`
- [own, "would require"] L524: `section 177(2) would require a carefully considered approach with evidence that Chorus would be unable to recover its costs and that there was no double counting`
- [own] L525: the current framework `was expected to leave Chorus whole`; L527 `While we accept that this network was a hypothetical one`
- [own] L535: `It is artificial to consider fibre financial outcomes in isolation`
- [own, "equally plausible"] L539: `an equally plausible approach that better supports the Part 6 purposes is to focus the analysis solely on required returns investment, setting aside operating costs, tax and depreciation`
- [own, "and / or"] L542: `Other "non-capital" costs are not included in the assessment of past losses, on the basis that section 177 does not anticipate their inclusion and / or it is unreasonable to include such costs`
- [SC, mention of others' views] L537: the Select Committee `received submissions on past losses supporting specific provision` and `submissions from those concerned that there was no evidence that past losses existed and raising the possibility of unearned profits`
- Discount rate / rate of return for the loss period: asked in Q18b (L446, `how the rate of return on investment and discount rate for the loss period should be calculated`). D07 gives no rate, no method and no separately labelled answer; "discount rate" occurs only at L446.
- Simplifying assumptions for common costs (Q18a, L446): no separately labelled answer.

### Crown financing

- [own, statute as described] L469: `In respect of any crown financing, must refer to the actual financing costs incurred by the provider.`
- [SC quote] L472: `the Commission should take into account the concessional element, and should not assume that commercial financing rates were applied to the whole of the asset base`; L473 `we recommend inserting new section 176(3A)`; L478 `the principal amount of the debt/equity investment would remain reflected in the value of assets in the asset base`
- [own, "It appears to us"] L481-484: `ensuring that only the actual (low) financing costs are taken into account when calculating losses`
- Q19 (preference between `the two methods`, L448) and Q20 (related parties, `eg, LFC parent companies`, L449): D07 states no preference between the two methods and does not describe them; no separately labelled answer to Q20. Related-party text elsewhere: L440 (asset valuation), L389 (`related company principles`).

### Cost allocation

- [own] L182: `cost allocation rules and disclosure should be at the service level (eg not at the aggregate FFLS level)`
- [Axiom] L288: `the Commission would need to allocate a portion of the costs of assets that are used to provide services in addition to FFLAS to those other services. Chorus would almost certainly overrecover its costs without this step.`; `Chorus has likely strong incentives to allocate those common costs in ways that reduce or foreclose potential competition`
- [Comm] L552: `We propose adopting the approach to cost allocation we have used for information disclosure regulation, customised price paths and individual price path regulation under Part 4`
- [own, "likely"] L554: `Although the general principles of cost allocation under Part 4 are likely to be appropriate under Part 6`
- [own] L565: `The Commission has appropriately recognised these risks.`
- [own, "Where possible"] L569-572: three conditions, e.g. `Where possible, the cost allocation methodology prescribes appropriate allocation approaches for particular assets; and`
- [own, conditional "if it simply adopts"] L574: `the Commission will be open to legal challenge if it simply adopts the Part 4 input methodology without consideration of whether further allocation rules are required`
- Standalone cross-check: heading L576 `Allocation of common costs must not exceed standalone cost`; [own, "may also need"] L577 `The Commission may also need to consider the standalone cost of FFLAS services`; [HC, as described] L579 `the allocation of costs should fall between incremental cost (IC) and standalone cost (SAC)`; [own, "should ensure"] L583 `the Commission should ensure that common costs allocated to the fibre network do not exceed the level that would be required by a standalone wholesale only business of this nature`; [own, "may wish"/"could"] L583 `the Commission may wish to consider whether a standalone cross check should be applied and how it will be derived`; `the Commission could apply a cross check and cap based on benchmark fibre and wholesale infrastructure providers`
- Copper versus fibre: L269 (transition), L384 (shared switch), L440, L456, L535 `set copper service prices on the basis of a fibre network cost`, L542 `copper service prices had been set at a generous level that allowed for substantial recovery of fibre costs`, L581 `likely to be significantly less complex than would be required for the copper broadband and integrated services`.
- ACAM appears only inside the quoted 2010 Commission passage (L520). The terms ABAA and OVABAA do not occur in D07.
- Allocation between FFLAS services (Q22, L584): answered through pricing methodologies, paras 115-119; also L563 `It will also be important to understand how costs are allocation between regulated services`.

### Cost of capital

- [own, agreement; "would need to"] L604: `can serve as a starting point for Part 6`; `the Commission would need to confirm that the underlying principles and parameters remain valid for this instance`
- [own, "likely"] L605: `Appropriate industry specific parameters (eg asset beta, leverage and credit rating) – likely using the methods established under Part 4 and the FPP process – would need to be established.`
- [own, expectation about others' arguments] L616: `We expect that it will be argued that the Commission should apply an uplift to the WACC IM mid-point.`
- [Comm, as described] L618: under Part 4 for airports, `an uplift is not required when the regulated entity is subject to information disclosure only (as each supplier establishes its own target return for pricing purposes)`
- [own] L620: `the Commission will need to consider how section 166(2) should change the analytical approach adopted under Part 4`
- [Axiom] L284: `weaker justification for applying a` WACC uplift; L621 `Axiom also addresses some differences in its report.`
- No parameter value, percentile or WACC number is printed. TAMRP occurs only in the Commission's Q24 (L602); D07 does not say whether cross-sector parameters should be re-estimated.

### Quality dimensions and standards

- [own] L628: `The CEPA paper helpfully sets out the dimensions of quality and how they might be expressed.`
- [own, "suggests"] L633: `Sections 194(3) and (4) reinforce that the Commission may apply quality incentives to maintain or improve quality of supply`
- [own, "may wish"] L635: `the Commission may wish to consider the outcomes it seeks to achieve from quality standards early in the process`
- [own, "likely"] L637: `these are likely to occur at a principle level for the IM but would need to be specific in the PQ determination`; `quality dimensions should address the full lifecycle dimensions set out in the CEPA report`
- [own, "could"] L699: `the Commission could ask the TCF to report back on these latter quality elements, setting out where proposed commitments are agreed and where not agreed`
- Table of possible standards: section 7.

### Price-quality versus information disclosure; revenue cap and wash-up; paths

- L127: `or, in the case of ID regulation only, allow the Commission to monitor whether prices recover efficiently incurred costs`
- L242: assets `admitted in to the RAB and recovered from the revenue cap`
- L305: `specific Part 6 requirements, eg to apply a revenue cap and wash-up mechanism` (described as a Part 6 requirement; no position on wash-up design).
- L618: uplift difference between price control and information disclosure (above).
- [own, "We suspect"] L711: `We suspect that the Commission will need to take a proactive and specific role to developing the price-quality path and forecasts.` This is the whole answer to Q27, Q27a-c and Q28; D07 states no view on supplier proposals, totex or IRIS.
- L721: `Suggestions are set out in the Axiom report and above.` (whole answer to Q29).

### Capex input methodology; tax

- No capex IM position. "capital and operating expenditure" occurs only in the Commission's
  Q18a (L446) and Q27c (L708).
- Tax: one occurrence, L539 (`setting aside operating costs, tax and depreciation`). No tax IM position.

### Process and timing

- [own, "suggest"/"may also want"] L82: `We suggest the Commission consider further how it can engage end users`
- [own, "does not appear"] L88: `the approach paper does not appear to canvas in substantive detail what is important to end-users`
- [own, "could help"] L91: `the Commission has appointed an advisory panel which we think could help to strengthen the consumer voice in the process`
- [own, "recommend"/"potentially"] L95: `We recommend that the Commission consider spending more time considering these matters earlier in the process, potentially lengthening the emerging views phase of the process to do this.`
- [own, "could"] L97: January 2019 sentence (section 2).
- [own] L231: `the Commission can enhance certainty by setting out how it will address issues that may emerge over time`

## 5. References to organisations, people, cases, statutes and documents

| Entity / source | Lines | What D07 attributes to it |
|---|---|---|
| Commerce Commission (`the Commission`) | throughout; L4 | recipient; author of the approach paper, the IM funding paper (L90), the fibre study, the 2010 EDB Draft Reasons Paper and NZCC 37 |
| Approach paper | L24, L57, L68, L88, L187-191, L218-221, L238, L246, L276, L328, L339, L347, L389, L397, L506, L560, L607-613 | proposals and preliminary views; pinpoints in section 2 |
| Chorus | L36, L39, L66, L208, L282, L288, L345, L378, L385, L390, L405, L440, L492, L524-527, L535, L540-544, L556, L581, L589-590, L598, L657, L683 | regulated provider; `Chorus is both a wholesaler of an essential input and competitor of its wholesale customers.` (L66) |
| LFCs | L379, L449 (Q20), L598 | product range finding from the fibre study; would disclose pricing consistency |
| 2Degrees | L378 | Chorus provides its national backhaul network |
| Axiom Economics (`Axiom`) | L72, L77, L229, L246, L264, L267-290, L354, L405, L409, L441, L563, L621, L721 | attached expert report; paras 46-49 are attributed summaries of it |
| InternetNZ | L88 | reminded participants at the December 2018 workshop that end user outcomes `include efficient use of fibre infrastructure` |
| Oxera | L84-85 (fn 2), L90, L109 (fn 3) | article `Legitimacy and renationalisation: where next for utility regulation?`, March 2018 |
| High Court, `Wellington International Airport Limited v Commerce Commission [2013] NZHC 3289` | L39, L53, L105-123, L138, L144, L163, L330, L497-516, L529, L531, L579, L586 | definition of workably competitive market; prices at the heart of Part 4; purpose statements must be given effect; initial RAB values; under-utilisation; IC to SAC |
| Supreme Court, `Unison Networks Ltd v Commerce Commission [2007] NZSC 74` | L163 (fn 6) | quoted through the High Court at [228] |
| Economic Development, Science and Innovation Committee (`Select Committee`) | L175, L189, L471-478, L537 | report of 4 May 2018 on the Telecommunications (New Regulatory Framework) Amendment Bill; s166 amendment; financing-cost recovery; submissions received on past losses |
| Parliament | L163, L175, L430 | intent |
| Electricity Authority | L226-227, L248 (fn 12), L594 | 2017 passage on confidence in access regimes; power to set pricing methodologies for electricity lines services (in Commission quote) |
| Ernst and Young (`EY`); Council of European Energy Regulators (`CEER`) | L321-322 (fn 14), L646 (fn 32) | summaries of European approaches |
| CEPA | L624 (Q25), L628, L637 | paper/report on quality dimensions |
| TCF | L699 | body the Commission could ask to report back; not expanded |
| Minister | L132-141 | in the s166 text |
| Commission fibre study (`9A Fibre Study`, `s9A fibre study`, `Commission Study in to fibre services 17 December 2018`) | L379, L395, L535, L558 | LFC product spread; Chorus considers it operates one network |
| `Final pricing review determination for Chorus’ unbundled copper local loop service [2015] NZCC 37` | L556 (fn 24) | copper prices set on a fibre network cost basis |
| `Input Methodologies electricity distribution services Draft Reasons Paper June 2010` | L531-532 (fn 22, 23) | ACAM passage quoted at L520 |
| Fibre deeds / Fibre Deeds | L281, L589 | non-discrimination obligations continue |
| UFB agreements, Crown funding | L525 | parts of the current framework |
| Countries/regions | L84 (UK), L307 (Australia), L321 and L646 (Europe) | comparators mentioned |
| Part 4 sectors | L12, L565, L594, L598, L618 | electricity distribution, gas pipelines, airports; `gas businesses (the only entities for which it can set pricing methodologies)`; airports subject to ID only |

Not mentioned anywhere in D07 (whole-file search): Transpower, Vodafone, CIP, Crown Fibre
Holdings, Crown Infrastructure, ACCC, Ofcom, Enable (as a company; the verb "enable" occurs),
Northpower, Ultrafast, Spark (own name), any individual person's name.

## 6. Definitions and abbreviations

| Term | Where introduced | Notes |
|---|---|---|
| Part 4 | L12 `Part 4 of the Commerce Act 1986 (Part 4)` | |
| the Act | L13 `Part 6 of the Telecommunications Act 2001 (the Act)` | L57 prints `Part 6 of Act` |
| FFLAS | used undefined from L15; expanded L130 `fibre fixed line access services (FFLAS)` | author's description L370; variant `FFLS` at L154, L156, L180, L182 |
| Fibre network | L370 `a network structure used to deliver telecommunications services over fibre media` | capitalised `Fibre Network` at L373, L382, L384, L495 |
| UFB | L13, not expanded | `UFB handover` L370; `UFB POI access` L391 |
| RAB | used from L36; expanded L414 `regulated asset base (RAB)` | Contents prints `regulated asset based` |
| IM / IMs | `Pricing Principles IM` L28; expanded L144 `input methodologies (IMs)` | |
| the approach paper | L57 | |
| Axiom | L77 `An Axiom Economics (Axiom) expert report` | |
| Wellington Airport | L105 | also `Wellington Airports` L330, L529, L531, L579, L586 |
| Select Committee; Select Committee Report | L175; L189 | |
| FCM | used L30; expanded L343 `Financial Capital Maintenance (FCM)` | |
| IC, SAC | L579 `incremental cost (IC) and standalone cost (SAC)` | |
| BBM | Contents L8, L216; `building block model approach` L303; `building blocks approach` L486 | no "X (BBM)" expansion |
| totex | L708 `forecast total expenditure (totex)` | Commission wording |
| fibre asset | L416-418 | two-limb definition for s177 |
| Financial loss | L460 | `is not defined and must be determined by the Commission` |
| workably competitive market | L107 | High Court definition |
| Access-based competition | L171 | Commission definition, quoted |
| implementation date / implementation day | L403 etc. / L441 | no calendar date |
| Not expanded in D07 | | ID (L127), PQ (L637), RSP/RSPs (L174), LFC/LFCs (L379), DFAS (L376), POI/POIs (L365), LOB (L391), CDNs (L400), WACC (L8), TAMRP (L602), UCLL/UBA FPP (L601), ACAM and EDB (L520), IRIS (L709), CEPA (L624), TCF (L699), SLA (L689), API (L678), B2B (L670) |

## 7. Table (one, linearised): possible quality standards, L639-697

Column labels L639 and repeated after the page break at L649: `Domain/Purpose Examples of possible quality standards`.
No units, no numeric cells. The extraction lists each domain label and then its bullets;
column alignment is lost and cannot be checked (text-only original).

| Domain/Purpose (left column) | Lines | Examples (right column), as printed |
|---|---|---|
| `Establish high level expected outcomes relating to the regime and anticipated network level incentives` | L640-655 | 5 bullets: `Required aggregate innovation, revenue, costs, volume and service dimensions, including:` (L642); `Network wide quality - avoiding systemic outages in geographic areas or nationwide, aiming to maximise overall network uptime and quality.` (L644); `Fit for purpose quality – identify what a fit for purpose service is and how it evolves over time (eg minimum speeds, maximum latency).` (L651); `Network fault rates.` (L653); `Investment and improvement in service quality.` (L655). The first bullet ends `including:`; whether the next four are its sub-items is not shown by the extraction. |
| `Chorus operating efficiency and approach` / `Including how regulated providers interact with access seekers.` | L657-680 | 7 bullets: `Responsiveness to access seeker requests for new services.` (L660); `Commitments relating to:` (L662) with 2 sub-items `making new FFLAS variants available at the same time as to itself.` (L664) and `consultation and development.` (L666); `Installation of technical capability, eg handover links.` (L668); `B2B/portal/system to system:` (L670) with 2 sub-items (L672, L674); `Person to person interactions (call answer times/dropped calls, query to completion response times, right first-time resolve %).` (L676); `Commitments around outages – eg API for RSP to handle data relationship with customer directly` (L678); `Accuracy and integrity of service level reporting.` (L680) |
| `Directly impacting end user service quality` / `Including how end users interact with Chorus.` | L682-697 | 4 bullets: `Engaging with end users:` (L685) with 3 sub-items `Meeting appointment commitments;` (L687), `Completing jobs within agreed SLA (eg rapid fault resolution) etc.` (L689), `Professional standards when on site` (L691); `Minimising complaints and compensation incentives.` (L693); `Agreed service variant performance metrics (eg speed performance, individual line quality, watching for repeat faults.` (L695, parenthesis not closed); `Provisioning connection commitments.` (L697) |

- Three domains; the page break falls inside the first (L646-649).
- Para 127 (L699) refers to `The two latter categories` (the second and third domains).

## 8. Internal inconsistencies, footnote qualifiers and extraction oddities

### Same matter stated differently in two places (neutral, both locations)

1. Section numbers for the loss provisions. The Commission's Q18 as quoted: `our interpretation and proposed application of ss 176(2) and (2AA) for the calculation of financial losses` (L444). The author's own text: `Under section 177(2)` (L460), `Section 177(3) further constrains` (L466), `under section 177(5)` (L464), `Section 177 provides direction on how the initial value of fibre assets must be determined.` (L416). The Select Committee quote: `new section 176(3A)` (L473). D07 does not reconcile these.
2. `inconsistent with the Part 4 (s162) purpose` (L518) against L103, which gives s162 as the Part 6 purpose and s52A as the Part 4 purpose.
3. `actual losses` in quotation marks in the executive summary (L36) against `financial losses` / `Financial loss` as the quoted statutory term in the body (L460).
4. Executive summary: the pre-2020 framework was `designed to ensure Chorus received a normal return on a hypothetical efficient fibre network` (L36). Body: `as if it was achieving a normal return on a modern efficient fibre network already` (L525) and `this network was a hypothetical one` (L527).
5. Executive summary paraphrase `there is little or no impact to beneficial consumer outcomes from increasing the value of the initial RAB` (L39) against the three-part judgment quote at L499-504 and the continuation at L511 that initial RAB values `do have some impact on the general investment environment for regulated industries`.
6. Footnotes 9 (L191) and 10 (L218) cite the same approach paper paragraph `[5.39.3]`: once for a statement the author calls correct (L185) and once for wording the author disagrees with (L196).
7. Body `in its 2017 consultation` (L226) against the footnote title `Response and next steps decision 4 October 2017` (L248).
8. L20 says Part 6 directs promotion of `actual competition` while Part 4 promotes outcomes `consistent with competition`; L103 says `The focus of both is on promoting outcomes consistent with workably competitive markets.` L150 locates the difference in s166(2), not s162.
9. Case short name: `(Wellington Airport)` L105, L144, L497 against `Wellington Airports` L330, L529, L531, L579, L586.
10. Para 5d (L75) lists `asset valuation, allocation of common costs and WACC`; the body also has sections on losses and Crown financing (L443), quality dimensions (L623) and price-quality path IMs (L701).
11. Executive summary lists against body lists: section 3.

### Footnotes that qualify or limit the body statement

- fn 17 (L397) on L391. Body: `We believe that the FFLAS service description does not extend to wireless or layer 3 elements of the networks, irrespective of LOB restrictions.` Footnote: `While unclear, the approach paper could be interpreted as suggesting this was a possibility. See [7.26], footnote 149.`
- fn 2 (L84) on L61. Body: `can deliver above normal returns for regulated entities and poor services for end-users, undermining public confidence in utility regulation`. Footnote: `For example, Oxera note declining public confidence in UK utility regulatory brought about by the outcomes from these models.`
- fn 22 (L531) on L518. Body: `A further principle developed through Part 4 implementation is that expected returns over the life of an investment exceeding normal returns is inconsistent`. Footnote: `For example, see discussion relating to cost allocation in Wellington Airports and Input Methodologies electricity distribution services Draft Reasons Paper June 2010` (a paper labelled Draft).
- fn 23 (L532) on L520. Body introduces the quote as `The Commission summarised this underlying principle in considering cost allocation principles`; the source is the same June 2010 Draft Reasons Paper, and the quote concerns electricity distribution and gas pipeline services.
- fn 27 (L586) on L579: `For example, see Wellington Airports at [1809]` for the IC-to-SAC principle.
- fn 6 (L163) on L144: the High Court statement that purpose statements must be given effect is quoted with its Supreme Court source.
- fn 13 (L276; marker at L263): `As per [6.45] of the approach paper.` The marker sits after item 43b (`Differences between the sectors, including greater potential for competition.`).
- fn 24 (L556) on L535: the statement that copper prices were set `on the basis of a fibre network cost` is sourced to NZCC 37 at [B66] to [B70].
- fn 28 (L607) on L589: the exclusion of pricing methodologies from the mandatory list is sourced to an approach paper footnote, `footnote [162]`.
- Bracketed editorial notes: `[emphasis added]` L117, L123, L142; `[Emphasis added].` L479; `[footnotes omitted]` L514; `[emphasis added – footnotes omitted]` L522. The emphasised words themselves are not marked in the extraction: unresolved.

### Extraction oddities (as printed in the capture; original is the same text)

- Footnote markers detached onto their own lines or fused into words: `1` L41; `2 The Commission should be mindful` L63; `11` L220; `13` L263; `14` L300; `17` L392; `27` L580; `32` L632; in-line `stated that4:` L105, `Oxera article.3` L90, `(IMs).6` L144, `future:7` L171, `differences15` L339, `values20:` L497.
- A sentence split around a footnote block and page header: `irrespective of LOB restrictions.` L391 / `These services` L393 / `are not directly related to access to the fibre network` L400.
- Para 3 continues after a footnote marker: L61 then L63-64.
- Lost hyphens: `utilitystyle` L13; `endusers` L141; `longterm` L200, L212; `principlesbased` L229; `principlebased` L282; `nondiscrimination` L281; `overrecover` L288; `underversus over-investment` L284.
- Missing or wrong words as printed: missing full stop `adjacent markets The Commission has` L12; `rules than ensure` L119; `access-based in the competition` L171; `that or Part 4` L264; `specific and specific` L305; `dynamic is more important that static efficiency` L356; `is likely to require greater to ensure` L428; `investment in in the provision` L430; `initial value as of the asset` L436; `Providing FFLAS provides with` L483; `how costs are allocation between` L563; `likely significant more common costs` L581; `it consideration of pricing efficiency` L598; `band whom would it affect` L716; unclosed quote `'WACC uplift.` L284; unclosed parenthesis L695.
- Nothing is truncated: the file ends with para 129 and `[END]`.

## Shared ground (navigation only; cross-bundle search hits, context in other documents not read unless stated)

- Author identity: "Spark" occurs in D06 L4 (`A report for Spark`), L29, L153, L162, L189; D01 L834,
  L1356; D02 L81, L85; D08 L165; never in D07's body. D06 L1-30 was read: title
  `New regulatory framework for fibre`, `December 2018` (L5, no day), project team `Hayden Green` /
  `Axiom Economics` (L8-9), and L29 `I have been asked by Spark New Zealand (Spark) to provide an independent economic review`.
  D06's file name carries "21_december_". D07 L77 says an Axiom report is attached.
- D07 passages that are attributed summaries of D06: L269-289 (paras 46-49), L229, L246, L264,
  L354, L405, L409, L441, L563, L621, L721. D06's contents (L23-25) list 4.1 Asset valuation,
  4.2 Cost allocation, 4.3 Pricing principles, 3.4 Fewer concerns about underinvestment.
- `1 December 2011`: D07 L460; D03 L159 (`for the period starting on 1 December 2011 and ending on the close of the day immediately before the implementation date`); D06 L641 (different use: `for assets owned by Chorus before 1 December 2011`).
- `NZHC 3289`: D07 L53, L111, L138, L508; D01 L377, L378, L422, L425.
- Only in D07: `January 2019` (L97), `NZSC 74` (L163), `NZCC 37` (L556).
- Strings found only in D06 and D07 across the bundle (combined search): Axiom, Oxera, 52T(3),
  176(3A), advisory panel, 2Degrees, Ethernet Aggregation, Enabling mass participation, Council
  of European Energy, Ernst and Young (D06 8 hits, D07 30 hits; which of these are in D06 was not
  separated).
- Hit counts only, not read: "pricing principles / standalone / WACC uplift / percentile"
  D01 10, D04 2, D06 34, D07 16, D08 11; "Electricity Authority / CEPA / TCF / InternetNZ /
  Select Committee / 9A / consumer expert" D01 12, D03 7, D04 1, D05 3, D06 3, D07 17, D08 4;
  "emerging views / approach paper / proposed approach / November 2018" D01 12, D02 3, D03 11,
  D04 31, D06 4, D07 18, D08 2.
- Edition/sequence relationships visible from D07: it is a response to the Commission's approach
  paper (no manifest file name corresponds to that paper); it refers forward to an `emerging views`
  phase and `Draft IMs papers` (L95, L97). Manifest file names only, texts not read here: D03
  `fibre_emerging_views_presentation_25_june_2019`; D04 `fibre_regulation_emerging_views_summary_paper_21`
  (name cut off after "21", date not established here); D05 `internet_nz_submission`. D07 L88
  reports an InternetNZ statement at the December 2018 workshop.
- The Commission's consultation questions quoted in D07 (Q1, Q3-Q29) are wording from the
  approach paper; other submissions in the bundle may quote the same questions (not checked).

## Gaps

- Unread ranges in D07: none.
- Unresolved (cannot be inspected in a text-only source): table column layout (L639-697);
  which words carry the "emphasis added" in the quoted passages (L107-123, L141, L471-478,
  L520); whether "January 2019" (L97) and the s176/s177 references are as printed in the
  published PDF.
- Not covered here: D01-D06 and D08 beyond the search hits and D06 L1-30 listed above.
