# aq-01322 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Line references are `text/Dnn.txt` line numbers (Lnn). Monetary tables are "(in thousands,
except per share data)" unless stated; prose and guidance tables use rounded $M/$B.

## Bundle

- What it is: six quarterly earnings releases (Form 8-K Item 2.02, Exhibit 99.1) issued by
  Cencora, Inc. (NYSE: COR), Conshohocken, PA, covering fiscal Q2 2025 through fiscal Q3 2026
  (fiscal year ends September 30). Fiscal Q1 2025 has no release in the bundle.
- Documents: 6 (D01-D06 from `text/manifest.json`). Local ids are alphabetical by file name and
  differ from the task page's numbering - see each Source line. Chronological order:
  D02 (Doc 1) -> D04 (Doc 2) -> D06 (Doc 3) -> D01 (Doc 4) -> D03 (Doc 5) -> D05 (Doc 6).
- Gaps:
  - Unread readable text: none. All six documents were read line by line in chunks (ledgers in each
    Coverage line). Missing source text: none (intake: every document `incomplete: false`,
    `gap_characters: 0`, `matches_capture: true`).
  - Formatting not recoverable from text (visual gap): the bold marking referenced by guidance
    footnotes - D01 L122, D03 L131, D05 L126 "Bolded figures indicate updates to guidance metrics."
    and D06 L160 "Bold numbers indicate updates to guidance ranges." - is not rendered in `docs/` or
    `text/` (no bold markup anywhere). Which cells were bolded is unresolved; only the prose
    statements of changes (D01 L19, D03 L17/L112, D05 L17/L107, D06 L152) identify updates.
  - Material referenced but not in the bundle: Exhibit 99.2 to the November 5, 2025 Form 8-K (fiscal
    2025 revised segment detail; D06 L146, D01 L124, D03 L133, D05 L128); investor slide
    presentations (constant-currency guidance; D01 L126, D03 L137, D05 L132); Forms 10-K. No release
    for fiscal Q1 2025 or fiscal Q4 2026 in the bundle; fiscal 2026 full-year actuals absent;
    restated (three-part) fiscal Q4 2025 segment figures and exact restated fiscal 2025 segment
    totals are not printed anywhere (only the rounded "Fiscal 2025 Actuals" column).
  - No PDFs, images or charts; page counts not applicable. D03 and D05 carry printed page-number
    lines ("1"-"19", "1"-"21") that sometimes fall mid-sentence (D03 L58-62, L90-94; D05 L217-221
    between footnotes); paragraph breaks mid-sentence also at D01 L89-91, D02 L612-614, D04 L83-85,
    L202-204, L632-634, D06 L680-682. Text is continuous across them. Line 1 of each `text/Dnn.txt`
    is an extraction header, not source text.
  - Tables are Markdown pipe tables in both `docs/` and `text/`; per memory note, the platform shows
    these rows without pipes, so cell-spanning verbatim quotes may not match the form's text.
- Extraction spot-checks (all against `docs/` originals with exact-line grep; non-blank line counts
  docs/text, text = docs + 1 header line): D01 352/353 - table row "|Adjusted free cash
  flows|$(2,436.7)M|" (docs L492), "|Diluted|195,319||195,188||0.1%|" (docs L199), footnote "2
  Includes an $86.8 million credit related to a derivative lawsuit settlement..." (docs L206). D02
  446/447 - six-month "Adjusted Non-GAAP|$5,450,110" row (docs L347), cash-flow fn1 (docs L605),
  typo row "case equivalents" (docs L598). D03 516/517 - "Adjusted free cash flows|$(1,280.2)M" (docs
  L723), "Assets held for sale|3,849,666" (docs L604), fn1 "$3.0 billion of senior notes" (docs
  L673), page line "19" (docs L753). D04 458/459 - nine-month "Adjusted Non-GAAP|$8,310,448" (docs
  L366), fn1 "$1.1 billion ... $500 million ... $200 million" (docs L625), split fn3 continuation
  "reform for the three months ended June 30, 2025" (docs L206). D05 520/521 - "Adjusted free cash
  flows|$1,142.3M" (docs L732), merged "Other, net|...|(34,007)" row (docs L346), fn3 "$55.2 million
  and $37.5 million" (docs L219), "previous range of $17.70 to $17.90" sentence (docs L15). D06
  504/505 - "Non-GAAP diluted shares outstanding|195,340" (docs L310), fn1 "$700 million of term
  loan repayments" (docs L682), heading "Reportable Segments (revised as of October 1, 2025)" (docs
  L121), "(1) Bold numbers indicate updates to guidance ranges." (docs L166). All matched verbatim.
- Provenance: `notes/intake.json` schema 1, capture_sha256
  7aaca131c238bd44d3daca120a2cf552337ff895bb3ec9849c1d51196e7d2575; intake "number" = platform Doc N
  (1 = D02, 2 = D04, 3 = D06, 4 = D01, 5 = D03, 6 = D05); every captured_sha256 = source_sha256 =
  `text/manifest.json` sha256 (D01 832feeed..., D02 8685053b..., D03 62d39b72..., D04 d5eef0ac...,
  D05 87700baa..., D06 4958de65...). No recovered-source history recorded. The platform's bundle
  overview text was not inspected (not in the bundle folder); it is navigation only.

## D01 - Cencora Reports Fiscal 2026 First Quarter Results

- Source: `docs/cencora-inc-q1-fy2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-04.txt`
  | `text/D01.txt` L1-495, no pages (plain text) | platform **Doc 4**.
- Written or submitted by: Cencora, Inc. (issuer; dateline L17 "CONSHOHOCKEN, PA, February 4,
  2026"). Quotes Robert P. Mauch, President and CEO (L21-23). Call participants Mauch and James
  F. Cleary, EVP & CFO (L136-138). Contact Bennett S. Murphy, SVP Investor Relations and
  Enterprise Productivity (L486-490).
- Type, date, edition: Exhibit 99.1 earnings release dated February 4, 2026 (L3, L17).
  FY2026 guidance edition 2 of 4 in the bundle (after D06, before D03).
- Period covered: "fiscal year 2026 first quarter ended December 31, 2025" (L17); comparative
  three months ended December 31, 2024; balance sheet Dec 31, 2025 vs Sep 30, 2025 (L355-357).
  No year-to-date columns (Q1). FY end: 10-K "for the fiscal year ended September 30, 2025" (L160).
- Entities and aliases:
  - Segments (L81): "two reportable segments: U.S. Healthcare Solutions and International
    Healthcare Solutions. Additionally, other businesses for which the Company is exploring
    strategic alternatives have been grouped together in Other. These businesses include MWI
    Animal Health, Profarma, U.S. Consulting Services, and certain components of PharmaLex."
  - OneOncology: acquisition completed, "the majority of the outstanding equity interests that it
    did not own in OneOncology, a leading management services organization (MSO) for oncology
    practices" (L99; headline L15; L19; L23; guidance rationale L103 "operating income and equity
    method income contributions"). No closing date or price printed. Cash flow "Cost of acquired
    companies, net of cash acquired" (219,686) Q1 FY26 (L407) - not labelled as OneOncology.
  - Retina Consultants of America = "RCA" (L45): "January 2025 acquisition" (L45, L47, L53, L65,
    L67, L71, L85); exact date "January 2, 2025" only in cash-flow fn1 (L426).
  - U.S. Consulting Services business "classified as held for sale"; "$249.5 million impairment
    of assets" (L47); table 249,498 (L181, L227, L321); fn3 L204 / fn2 L244 "Impairment of assets
    held for sale, including goodwill, related to its U.S. Consulting Services business."
  - Customer losses: "a grocery customer and an oncology customer" (U.S., L85); "loss of a
    manufacturer customer program" (Other / consulting services, L95). GLP-1 class (L85).
  - Derivative lawsuit settlement credit $86.8M (fn2 L202; fn1 L242).
- Tables (all in thousands unless noted):
  - Summary Results L27-37 (rounded $B/$M; GAAP vs Adjusted columns).
  - Financial Summary L170-196 (three months Dec 31, 2025 vs 2024; % of revenue; % change),
    footnotes 1-4 L200-206.
  - GAAP to non-GAAP reconciliation Q1 FY26 L216-232 (fn L242-246); Q1 FY25 L258-273 (fn
    L283-285; stray cell "2" at end of the Adjusted Non-GAAP row L273 = fn2 "sum of the
    components does not equal the total due to rounding"). Percentages of revenue L234-238,
    L275-279.
  - Summary Segment Information L297-343: revenue and operating income for U.S., International,
    Other, Intersegment eliminations, three months Dec 31, 2025 vs 2024 (2024 column on the
    three-part basis: U.S. $72,555,294; Intl 6,958,895; Other 2,002,455; elims (29,584); OI U.S.
    $686,925; Intl 165,180; Other 97,329; elims (126); total segment OI 949,308); segment margin
    block L323-343.
  - Balance sheet L355-383 (Dec 31, 2025 vs Sep 30, 2025). Cash flows L393-422 (three months
    Dec 31, 2025 vs 2024); fn1 L426; fn2 cash reconciliation L430-435 (four dates: Dec 31 2025,
    Sep 30 2025, Dec 31 2024, Sep 30 2024).
  - Adjusted FCF reconciliation L463-469 ($M, one decimal; "three months ended December 31,
    2025"): Operating cash flows $(2,305.2)M; Capex $(119.4)M; Free cash flows $(2,424.5)M;
    "(Less) gains from antitrust litigation settlements" $(12.2)M; Adjusted free cash flows
    $(2,436.7)M. No prior-year adjusted FCF column.
  - Constant currency L473-482 (consolidated and International; revenue $B, adjusted OI $M).
- Lists: investor events L148-150 (2 items: Leerink Partners Global Healthcare Conference,
  March 8-11, 2026; Barclays Global Healthcare Conference, March 10-12, 2026). Adjusted-measure
  definitions L445-461 (9 bullets; adjusted FCF last at L461). Other businesses list L81 (4 items).
- Forecasts, guidance, deadlines, effective dates:
  - Headlines L11 "Adjusted Operating Income Guidance Raised to Growth of 11.5% to 13.5%"; L13
    "Adjusted Diluted EPS Guidance Range Reaffirmed at $17.45 to $17.75 for Fiscal 2026".
  - L19: "Adjusted operating income guidance has been raised from the previous range of growth of
    8% to 10% to growth of 11.5% to 13.5% primarily to reflect the completion of the acquisition
    of OneOncology and the performance of the U.S. Healthcare Solutions segment."
  - L103 rationale: OneOncology contributions, U.S. performance "and improved results in Other as
    certain depreciable assets have been fully impaired as of December 31, 2025"; "reaffirming
    its full fiscal 2026 adjusted diluted EPS guidance range."
  - Guidance table L105-120, columns "2026 Guidance(1)" | "Fiscal 2025 Actuals": Revenue 7% to 9%
    growth | $321.3B; U.S. 7% to 9% | $285.0B; International 7% to 9% | $28.3B; Other 1% to 5% |
    $8.2B; Adjusted operating income 11.5% to 13.5% | $4.2B; U.S. 14% to 16% | $3.3B;
    International 5% to 8% | $588M; Other Flat | $352M; Adjusted diluted EPS $17.45 to $17.75 |
    $16.00; Net interest expense $480M to $500M | $292M; Adjusted effective tax rate ~20% |
    20.6%; Diluted weighted average shares outstanding 195.5M | 195.2M; Adjusted free cash flow
    ~$3.0B | $3.0B; Capital expenditures ~$900M | $668M.
  - Fn (1) L122 "Bolded figures indicate updates to guidance metrics." Bold is NOT rendered
    anywhere in docs/ or text/ (no markup) - which cells were bolded is unresolvable from text.
  - Fn (2) L124 points to "Exhibit 99.2 to the Company's Current Report on Form 8-K dated November
    5, 2025" for revised segment information (that exhibit is not in the bundle; D06 is Exhibit
    99.1 of that date). Fn (3) L126 International rows "As reported guidance"; constant-currency
    guidance only in the investor slide presentation (not in bundle).
  - Dividend L130: $0.60 per share, payable March 2, 2026, record February 13, 2026.
  - Conference call L134: 8:30 a.m. ET, February 4, 2026; access code 909212; replay code 618561.
- Hedged claims: L81 Other = businesses "for which the Company is exploring strategic
  alternatives" (status, no transaction stated). Guidance labelled forward-looking (L160
  boilerplate). Fn3 L126 constant-currency guidance not given in release.
- Rounded prose beside exact figures:
  - L47 prose "a litigation and opioid-related credit of $86.8 million related to a litigation
    settlement" vs table net line (86,151) (L178, L224, L318); $86.8M is the derivative-lawsuit
    component per fn2 L202 / fn1 L242, not the printed net.
  - L51 "$760.4 million" vs 760,449; L53 net interest "$72.4 million, an increase of $44.5
    million" vs 72,409 and 27,933 (L185); L45 GP margin 3.58% "+44 basis points"; L65 adjusted GP
    margin 3.48% "+37 basis points"; L69 adjusted OI margin 1.24% "+8 basis points"; L57 diluted EPS
    +14.8%; L91 International constant currency revenue +6.2%, segment OI -17.0%.
  - Summary table L32 adjusted OI "$1.1B" vs reconciliation $1,062,714 (L231) and constant-currency
    table "$1,063M" (L476).
- Notes: L49 is a stray "." line between bullets (present in source). L89-91 paragraph split
  mid-sentence ("lower / operating income") - layout break, no text missing. About Cencora L156:
  "51,000+ worldwide team members", "#10 on the Fortune 500 and #18 on the Global Fortune 500",
  "more than $300 billion in annual revenue". Share repurchases: "Purchases of common stock" -
  (none) Q1 FY26 vs (385,471) Q1 FY25 (L413). Cash dividends (126,516) vs (110,888) (L415). Net
  debt borrowings 266,212 vs 3,788,240 (L412) with fn1 L426: "$2.0 billion of net borrowings to
  cover seasonal short-term working capital needs and the issuance of $1.8 billion of senior notes
  to finance a portion of the January 2, 2025 acquisition of Retina Consultants of America in the
  three months ended December 31, 2024."
- Operative definitions, rules and scope exceptions:
  - Adjusted FCF (L461): "net cash provided by operating activities, excluding significant
    unpredictable or non-recurring cash payments or receipts relating to legal settlements, minus
    capital expenditures."
  - Adjusted gross profit excludes "gains from antitrust litigation settlements, LIFO expense
    (credit), and Türkiye highly inflationary impact" (L445); adjusted opex exclusions L447 (incl.
    "impairment of assets, including goodwill"); adjusted income before taxes adds "gain (loss) on
    remeasurement of an equity investment", Swiss tax reform remeasurement, "loss on divestiture of
    non-core businesses" (L451); adjusted EPS list L459; constant currency definition L471;
    non-GAAP guidance basis L484.
- Amendments or contradictions: guidance change stated L19 (adjusted OI growth previous 8% to 10%
  -> 11.5% to 13.5%); EPS reaffirmed (L13, L103). No other stated amendment. Prose $86.8M vs net
  86,151 noted above (explained by fn2, not a conflict in figures).
- Coverage: FULL. Read L1-200, L200-380, L380-495 (all lines). Unread: none. Missing source text:
  none (intake matches capture). Formatting gap: guidance-table bold (fn1 L122) not rendered.

## D02 - Cencora Reports Fiscal 2025 Second Quarter Results

- Source: `docs/cencora-inc-q2-fy2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-05-07.txt`
  | `text/D02.txt` L1-625, no pages | platform **Doc 1** (earliest release in the bundle).
- Written or submitted by: Cencora, Inc. (dateline L13 "CONSHOHOCKEN, PA, May 7, 2025"). Quotes
  Robert P. Mauch, President and CEO (L17-19). Call: Mauch and James F. Cleary, EVP & CFO
  (L127-129). Contact Bennett S. Murphy, "Senior Vice President, Head of Investor Relations and
  Treasury" (L616-618; title differs from D01 L488).
- Type, date, edition: Exhibit 99.1 earnings release dated May 7, 2025. FY2025 guidance edition 1
  of 2 in the bundle (D04 is the later one).
- Period covered: "fiscal year 2025 second quarter ended March 31, 2025" (L13). Three-month
  tables (Mar 31, 2025 vs Mar 31, 2024) AND six-month tables (six months ended Mar 31, 2025 vs
  2024). Balance sheet Mar 31, 2025 vs Sep 30, 2024 (L501-503). Cash flow six months only.
  10-K cited: fiscal year ended September 30, 2024 (L149).
- Entities and aliases:
  - Segments (L75): "two reportable segments: U.S. Healthcare Solutions and International
    Healthcare Solutions." No "Other" grouping; segment tables have only U.S., International,
    Intersegment eliminations (original two-segment basis).
  - Retina Consultants of America (RCA) (L41): "January 2025 acquisition"; exact "January 2, 2025"
    only in cash-flow fn1 L573. L79: "no significant increase in U.S. Healthcare Solutions revenue
    resulting from the acquisition of RCA as inventory sales from our specialty distribution
    business to RCA are now being eliminated in consolidation." L97: "the 15% equity interest
    retained by certain RCA physicians and members of management is accounted for by the Company
    as a contingent liability as opposed to a noncontrolling interest in equity." Fn2 L190 / fn3
    L233: RCA equity/incentive-unit "expense adjustments" of $37.5 million "in the three months
    ended March 31, 2025".
  - "Turkey" spelling throughout (L188, L249, L592 etc.) - D01 uses "Türkiye".
  - ERM Certification and Verification Services (assurer of 2024 Corporate Responsibility Report,
    "seventh consecutive year", L87).
- Tables (thousands):
  - Summary Results L23-33 (rounded).
  - Financial Summary three months L159-184 (fn L188-190); six months L200-225 (fn L229-233).
  - GAAP to non-GAAP reconciliations: Q2 FY25 L243-257 (adjusted EPS $4.42; % change row "vs.
    prior year quarter"); Q2 FY24 L281-294 ($3.80); six months FY25 L320-335 ($8.15); six months
    FY24 L359-373 ($7.08). Footnotes L267-269, L304-308, L345-347, L383-387.
  - Summary Segment Information three months L399-438 and six months L450-489 (U.S.,
    International, Intersegment eliminations only): Q2 FY25 revenue U.S. $68,283,831, Intl
    7,173,556, elims (3,714); Q2 FY24 U.S. 61,292,897, Intl 7,123,385, elims (1,975); Q2 OI U.S.
    $1,033,150 / 841,064, Intl 159,301 / 192,720, total 1,192,264 / 1,033,784. Six months revenue
    U.S. $142,316,959 / 126,476,699, Intl 14,630,897 / 14,193,612, elims (7,123) / (3,171); six
    months OI U.S. $1,800,494 / 1,539,188, Intl 341,394 / 380,315, elims (316) / -, total
    2,141,572 / 1,919,503. Segment margin blocks L422-438, L473-489.
  - Balance sheet L501-529 ("Total equity" label L528; "Other long-term liabilities" L527).
  - Cash flows six months L539-569 (fn1 L573; fn2 cash reconciliation L577-582, four dates).
    "Non-customer note receivable" (34,814) / (50,000) L555. Typo "case equivalents" L567 (in
    source).
- Lists: guidance bullets L101-117 (8 items: 1 under "now expects", 7 under "Additional
  expectations now include"; sub-bullets marked "◦" at L107, L111, L113; constant-currency
  International OI at L115 is a top-level "-" bullet). Investor event L139 (1 item: Bank of
  America Global Healthcare Conference, May 13, 2025). Non-GAAP definitions L592-608 (9 bullets).
- Forecasts, guidance, deadlines, effective dates (FY2025, bullet form - no table, no "Fiscal 2024
  actuals" column):
  - Headline L11 / L15 / L101: adjusted diluted EPS "$15.70 to $15.95, up from the previous range
    of $15.30 to $15.60."
  - L105 International revenue growth "3 to 4 percent, down from the previous range of 4 to 5
    percent"; L107 constant currency "6 to 8 percent, down from the previous range of 7 to 9
    percent"; L109 "Adjusted consolidated operating income growth to be in the range of 13.5 to
    15.5 percent, up from the previous range of 11.5 to 13.5 percent"; L111 U.S. segment OI growth
    "17.5 to 19.5 percent, up from the previous range of 14.5 to 16.5 percent"; L113 International
    "as reported operating income decline of 1 to 4 percent, down from the previous guidance of no
    growth"; L115 constant-currency International OI "down 3 percent to flat, from the previous
    guidance of an increase of approximately 5 percent"; L117 diluted shares "195.0 to 195.5
    million, revised from the previous expectation of under 196 million."
  - Not stated in D02: consolidated revenue growth, U.S. revenue growth, net interest expense, tax
    rate, adjusted FCF, capex guidance (unchanged items are not restated).
  - Rationale L95: "stronger earnings growth in the U.S. Healthcare Solutions segment and a lower
    contribution from the International Healthcare Solutions segment." L97: "no reduction to
    updated EPS guidance for a noncontrolling interest in RCA" (contingent liability treatment).
  - Dividend L121: $0.55 per share, payable June 2, 2025, record May 16, 2025.
  - Call L125: 8:30 a.m. ET, May 7, 2025; access code 962235; replay 839530.
- Hedged claims: L19 "We believe this leadership ... drives our resilient financial performance now
  and will continue to drive it in the future" (quote). L612 non-GAAP guidance basis.
- Rounded prose beside exact figures:
  - L47 interest "$104.0 million, an increase of 62.2 percent" vs 103,988 / 64,130 (L173).
  - L43 prior-year "$214.0 million litigation accrual" (fn1 L304 "$214.0 million opioid litigation
    accrual"); six-month fn2 L231 / fn1 L383 adds "$92.2 million opioid settlement accrual
    reduction" (prepayment of net present value under opioid settlement agreements).
  - L41 GP margin 4.06% "+35 basis points"; L59 adjusted GP margin 3.86% "+16 basis points"; L63
    adjusted OI margin 1.58% "+7 basis points"; L83 International constant currency revenue +5.7%,
    OI -13.9%.
  - Constant currency prose L610 (no table): Q2 revenue $75.5B, FX $357.7M, constant currency
    $75.8B; adjusted OI $1,192.3M, FX $6.6M, $1,198.9M; International Q2 revenue $7.2B -> $7.5B, OI
    $159.3M -> $165.9M; six months revenue $156.9B, FX $574.4M -> $157.5B; adjusted OI $2,141.6M,
    FX $18.4M -> "$2,159.9 million" (as printed); International six months $14.6B -> $15.2B, OI
    $341.4M -> $359.8M.
- Notes: About Cencora L145: "more than $290 billion in annual revenue" (D01 says $300 billion).
  Highlights L87: 2024 Corporate Responsibility Report released. Purchases of common stock six
  months (435,471) / (436,378) (L560); dividends paid (222,076) / (212,692) (L562). Net debt
  borrowings 3,455,501 (L559) with fn1 L573 "Includes the issuance of $1.8 billion of senior notes
  and a $1.5 billion term loan to finance a portion of the January 2, 2025 acquisition of Retina
  Consultants of America." Interest prose L47: "$1.8 billion of senior notes in December 2024 and
  the $1.5 billion variable-rate term loan, which we borrowed in January 2025". Cost of acquired
  companies (3,947,761) six months (L553). Effective tax rate prior-year 9.8% included "discrete tax
  benefits associated with foreign valuation allowance adjustments" (L49). Diluted shares -3.0%
  "primarily due to share repurchases" (L53).
- Operative definitions, rules and scope exceptions:
  - Adjusted FCF definition L608 (same wording as D01 L461) and the period figure in prose (no
    table): "For the six months ended March 31, 2025, adjusted free cash flow of $176.0 million
    consisted of net cash provided by operating activities of $632.5 million, minus capital
    expenditures of $235.0 million and gains from antitrust litigation settlements of $221.5
    million." (Cash-flow table: 632,456 L550; capex (234,953) L552.)
  - Adjusted opex exclusions L594 list four items (no "impairment of assets" item, unlike D01
    L447). Adjusted income before taxes L598 includes "loss on the divestiture of non-core
    businesses".
- Amendments or contradictions: guidance changes stated with "previous" values (L101-117); no
  other stated amendment.
- Coverage: FULL. Read L1-160, L160-330, L330-500, L500-625. Unread: none. Missing: none.

## D03 - Cencora Reports Fiscal 2026 Second Quarter Results

- Source: `docs/cencora-inc-q2-fy2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-06.txt`
  | `text/D03.txt` L1-716; the source carries printed page-number lines "1"-"19" (e.g. L23 "1",
  L60 "2", L92 "3", L135 "4", L713 "19") - 19 printed pages | platform **Doc 5**.
- Written or submitted by: Cencora, Inc. (dateline L15 "CONSHOHOCKEN, PA, May 6, 2026"). Quotes
  Robert P. Mauch (L19-21, "Mr. Mauch continued"). Call: Mauch and James F. Cleary (L147-149).
  Contact (singular "Contact:") Bennett S. Murphy, SVP Investor Relations and Enterprise
  Productivity (L705-709).
- Type, date, edition: Exhibit 99.1 earnings release dated May 6, 2026. FY2026 guidance edition 3
  of 4 (after D01, before D05).
- Period covered: "fiscal year 2026 second quarter ended March 31, 2026" (L15). Three-month and
  six-month tables (Mar 31, 2026 vs Mar 31, 2025). Balance sheet Mar 31, 2026 vs Sep 30, 2025.
  Cash flow six months. 10-K cited: fiscal year ended September 30, 2025 (L171).
- Entities and aliases:
  - Segments L86: same wording as D01 L81 (two reportable segments + "Other": MWI Animal Health,
    Profarma, U.S. Consulting Services, certain components of PharmaLex).
  - OneOncology: "the February 2026 acquisition of OneOncology" (L46, L48, L54, L70, L72, L76,
    L94); exact date "February 2, 2026" only in cash-flow fn1 L639. Q2 gain: "a gain of $1.1
    billion on the remeasurement of its equity method investment and the extinguishment of the
    put option liability related to its previously held investment in OneOncology" (L52; fn2 L214;
    fn4 L262); reconciliation row "Remeasurement gain related to OneOncology acquisition"
    (1,086,612) pre-tax, (834,152) net, $(4.27) per share (L285, L368); GAAP "Other (income) loss,
    net" (1,086,439) Q2 (L196), (1,107,039) six months (L240). EPS prose L58-62 "included a $1.1
    billion remeasurement gain related to the OneOncology acquisition, which was recorded as
    'Other (income) loss, net.'"
  - MWI Animal Health / "MWI": L106 "Cencora and Covetrus, a global animal health technology and
    services company, announced that they entered into a definitive agreement under which MWI
    Animal Health and Covetrus will merge"; L112 "MWI now being accounted for as 'held for sale'".
    Balance sheet "Assets held for sale" 3,849,666 (L573) and "Liabilities held for sale" 851,949
    (L585) at Mar 31, 2026 (not labelled by business in the table).
  - EyeSouth Partners: L108 "definitive agreement to acquire EyeSouth Partners' retina business.
    Upon completion of the transaction, the affiliated retina physicians of EyeSouth Partners will
    join Cencora's Retina Consultants of America ('RCA'), a leading management services
    organization." (signed, not completed, as of this release).
  - RCA "January 2, 2025 acquisition" in cash-flow fn1 L639 (prior-year column).
  - Customers (L90): "lower sales to our large mail order customer as a result of brand
    conversions, and the 2025 losses of an oncology customer and a grocery customer".
  - U.S. Consulting Services held-for-sale impairment carried in six-month figures (fn3 L260, fn2
    L384; 249,498 L237, L367, L527).
  - "Türkiye" used for both periods, including restated FY2025 comparatives (D02 printed "Turkey").
- Tables (thousands):
  - Summary Results L27-38 (adds an "Other Income, Net" row: $1.1B GAAP / $8M adjusted).
  - Financial Summary three months L183-208 (fn L212-214); six months L226-252 (fn L256-262).
    Line label now "Acquisition and divestiture-related deal and integration expenses" (L192,
    L235), applied also to the FY2025 comparative values (99,380; 138,092).
  - GAAP to non-GAAP: Q2 FY26 L274-289 (adj EPS $4.75); Q2 FY25 L317-330 ($4.42, same values as
    D02 L243-256, relabelled); six months FY26 L356-372 ($8.83); six months FY25 L404-418 ($8.15).
  - Summary Segment Information three months L444-489 and six months L503-549, on the
    U.S./International/Other basis, FY2025 comparatives restated: Q2 FY25 revenue U.S.
    $66,819,265, Intl 6,696,779, Other 1,956,407, elims (18,778) (D02 L402-404 printed U.S.
    68,283,831, Intl 7,173,556, elims (3,714)); Q2 FY25 OI U.S. $944,969, Intl 154,598, Other
    92,851, elims (154) (D02 L410-412: 1,033,150 / 159,301 / (187)); totals unchanged (75,453,673;
    1,192,264). Six months FY25 restated revenue U.S. $139,374,559, Intl 13,655,674, Other
    3,958,862, elims (48,362) (D02 L453-455: 142,316,959 / 14,630,897 / (7,123)); OI U.S.
    $1,631,894, Intl 319,778, Other 190,180, elims (280) (D02 L461-463: 1,800,494 / 341,394 /
    (316)). Q2 FY26: revenue U.S. $68,765,078, Intl 7,565,749, Other 2,055,571, elims (30,482); OI
    U.S. $998,300, Intl 175,797, Other 91,633, elims (2,381). Six months FY26: revenue U.S.
    $144,976,903, Intl 15,189,722, Other 4,184,518, elims (63,211); OI U.S. $1,829,630, Intl
    317,953, Other 183,050, elims (4,570). Segment margin blocks L469-489 and L529-549 (restated
    FY25 margins differ from D02's, e.g. Q2 FY25 U.S. OI margin 1.41% here vs 1.51% in D02 L426).
  - Balance sheet L563-593 (adds "Assets held for sale" and "Liabilities held for sale").
  - Cash flows six months L605-635; fn1 L639; fn2 cash reconciliation L643-648. Six-month FY25
    comparative column is condensed versus D02: investing "Other, net" (45,372) (D02 split it into
    "Non-customer note receivable" (34,814) and "Other, net" (10,558)); financing has no "Exercises
    of stock options" row and "Other, net" (2,984) (D02: 15,778 and (18,762)). Totals unchanged.
    New lines L631-633 for cash classified within assets held for sale ((24,487)).
  - Adjusted FCF reconciliation L680-686 ($M; "six months ended March 31, 2026"): Operating cash
    flows $(966.5)M; Capex $(285.0)M; Free cash flows $(1,251.5)M; "Less gains from antitrust
    litigation settlements" $(28.7)M; Adjusted free cash flows $(1,280.2)M. No prior-year column.
  - Constant currency L692-701 (three months ended March 31, 2026): consolidated $78.4B / $1,263M,
    FX $(0.4)B / $(1)M, constant currency $78.0B / $1,262M; International $7.6B / $176M -> $7.2B /
    $175M.
- Lists: highlights L106-108 (2 items: MWI-Covetrus merger agreement; EyeSouth agreement).
  Investor event L159 (1 item: Bank of America Global Healthcare Conference, May 12-14, 2026).
  Non-GAAP definitions L660-678 (9 bullets; page line "17" at L670 splits them).
- Forecasts, guidance, deadlines, effective dates:
  - Headlines L11 "Adjusted Diluted EPS Guidance Range Raised to $17.65 to $17.90 for Fiscal 2026";
    L13 "Cencora Expects to Repurchase $1 Billion in Shares by the End of Calendar 2026" (headline
    only; body L21 "in a position to resume opportunistic share repurchases"; L112 "as it resumes
    opportunistic share repurchases").
  - L17: "Adjusted diluted EPS guidance has been raised from the previous range of $17.45 to $17.75
    to a range of $17.65 to $17.90."
  - L112 rationale: U.S. operating income growth; "updated operating income expectations in Other
    as a result of MWI now being accounted for as 'held for sale'"; "narrowed its expectations for
    interest expense"; "incrementally lower expected share count". (Revenue guidance rows also
    differ from D01 but L112 gives no revenue rationale.)
  - Guidance table L114-129, "2026 Guidance(1)" | "Fiscal 2025 Actuals": Revenue 4% to 6% growth |
    $321.3B; U.S. 4% to 6% | $285.0B; International 8% to 10% | $28.3B; Other 1% to 5% | $8.2B;
    Adjusted operating income 12% to 14% | $4.2B; U.S. 14% to 16% | $3.3B; International 5% to 8%
    | $588M; Other "High-single digit growth" | $352M; Adjusted diluted EPS $17.65 to $17.90 |
    $16.00; Net interest expense ~$485M | $292M; Adjusted ETR ~20% | 20.6%; Diluted shares "Under
    195.5M" | 195.2M; Adjusted FCF ~$3.0B | $3.0B; Capex ~$900M | $668M. Fn (1) L131 bold note
    (bold not rendered); fn (2) L133 Exhibit 99.2 of Nov 5, 2025 8-K; fn (3) L137.
  - Dividend L141: $0.60 per share, payable June 1, 2026, record May 15, 2026.
  - Call L145-151: 8:30 a.m. ET May 6, 2026; meeting ID 280720750, access code 528015; webcast
    replay only (no telephone replay text, L153).
- Hedged claims: L13 "Expects to Repurchase $1 Billion" (expectation, headline only). L108
  EyeSouth "Upon completion of the transaction" (future). L106 merger "will merge" (agreement,
  not completed). L86 Other "exploring strategic alternatives".
- Rounded prose beside exact figures: L54 net interest "$140.5 million, an increase of $36.5
  million" vs 140,460 / 103,988 (L197); L50 OI margin 1.46% vs 1.37%; L46 GP margin 4.58% "+52 basis
  points"; L70 adj GP margin 4.31% "+45 basis points"; L74 adj OI margin 1.61% "+3 basis points";
  L98 International cc revenue +7.2%, OI +12.9%; L52/L62 "$1.1 billion" gain vs (1,086,612) /
  (1,086,439). L78 adjusted ETR 18.9% vs 20.8% "primarily due to discrete tax benefits".
- Notes: About Cencora L165 omits a team-member count ("Our worldwide team members"); "more than
  $300 billion". Purchases of common stock six months FY26 "—" (L625). Dividends paid (243,972)
  (L626). Net debt borrowings 4,377,761 (L624) with fn1 L639: "Includes the issuance of $3.0
  billion of senior notes and $1.5 billion of term loans to finance a portion of the February 2,
  2026 acquisition of OneOncology in the six months ended March 31, 2026." Long-term debt
  12,182,860 vs 7,542,988 (L587). Cost of acquired companies (4,932,036) six months (L619).
- Operative definitions, rules and scope exceptions: adjusted FCF definition L678 (same wording as
  D01/D02); adjusted income before taxes now names "the remeasurement gain related to the
  OneOncology acquisition" (L666); adjusted EPS list L676 adds the OneOncology remeasurement gain
  and uses "acquisition and divestiture-related deal and integration expenses".
- Amendments or contradictions: EPS guidance change stated L17 (previous $17.45 to $17.75).
  Restated FY2025 segment comparatives differ from D02 originals (see Tables); the restatement is
  not explained inside D03 except via guidance fn (2) L133.
- Coverage: FULL. Read L1-150, L150-309, L309-478, L478-647, L647-716. Unread: none. Missing: none.

## D04 - Cencora Reports Fiscal 2025 Third Quarter Results

- Source: `docs/cencora-inc-q3-fy2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-08-06.txt`
  | `text/D04.txt` L1-645, no pages | platform **Doc 2**.
- Written or submitted by: Cencora, Inc. (dateline L13 "CONSHOHOCKEN, PA, August 6, 2025"). Quotes
  Robert P. Mauch (L17-19). Call: Mauch and James F. Cleary (L131-133). Contacts: Bennett S.
  Murphy, "Senior Vice President, Head of Investor Relations and Treasury" (L636-638).
- Type, date, edition: Exhibit 99.1 earnings release dated August 6, 2025. FY2025 guidance edition 2
  of 2 (the later FY2025 edition; D06 then reports FY2025 actuals).
- Period covered: "fiscal year 2025 third quarter ended June 30, 2025" (L13). Three-month and
  NINE-month tables (June 30, 2025 vs June 30, 2024). Balance sheet June 30, 2025 vs Sep 30, 2024
  (L521-523). Cash flow nine months. 10-K cited: fiscal year ended September 30, 2024 (L159).
- Entities and aliases:
  - Segments L75: "two reportable segments: U.S. Healthcare Solutions and International Healthcare
    Solutions." (no Other; original two-segment basis in all segment tables).
  - RCA: "January 2025 acquisition of Retina Consultants of America (RCA)" (L41); "January 2, 2025"
    in cash-flow fn1 L593. RCA equity/incentive-unit expense adjustments: $37.5 million in the
    three months ended June 30, 2025 (fn2 L200) and $74.9 million in the nine months (fn3 L247).
  - International OI decline attributed to "our global specialty logistics business and our
    specialized consulting services business" (L83).
  - Good Neighbor Pharmacy, "Cencora's national franchise for independent pharmacies"; July 2025,
    "more than 4,000 community pharmacy owners", "14th annual ThoughtSpot" (L89).
  - Unnamed "equity method investment's gain on the sale of a business" ($39.7 million; fn3
    L202-204, fn4 L249; reconciliation row "Gain on equity method investment 1" (39,718) L270,
    L348; fn L285, L364). The investee and business are not named.
  - "Turkey" spelling throughout.
- Tables (thousands):
  - Summary Results L23-33 (Operating Income "$0.9B" GAAP / "$1.1B" adjusted).
  - Financial Summary three months L169-194 (fn L198-204; fn3 split across a layout break at
    L202-204 "Swiss tax / reform", text complete); nine months L214-239 (fn L243-249).
  - GAAP to non-GAAP: Q3 FY25 L259-275 (adj EPS $4.00; "Gains from antitrust litigation
    settlements" tax column printed +7,668 with NI (17,163), L263); Q3 FY24 L301-315 ($3.34; no
    rounding footnote); nine months FY25 L337-354 ($12.15); nine months FY24 L380-394 ($10.42).
  - Summary Segment Information, original two-segment basis: three months L420-459 - revenue U.S.
    $72,876,563 / 67,191,598, Intl 7,790,438 / 7,051,876, elims (3,469) / (2,121); OI U.S.
    $901,793 / 698,305, Intl 156,222 / 179,391, elims 316 / -, total 1,058,331 / 877,696. Nine
    months L471-509 - revenue U.S. $215,193,522 / 193,668,297, Intl 22,421,335 / 21,245,488,
    elims (10,592) / (5,292); OI U.S. $2,702,287 / 2,237,493, Intl 497,616 / 559,706, total
    3,199,903 / 2,797,199 (no intersegment-eliminations row in the nine-month OI table, L482-484).
  - Balance sheet L521-549 ("Total equity", "Other long-term liabilities").
  - Cash flows nine months L559-589 (separate "Non-customer note receivable" and "Exercises of stock
    options" rows); fn1 L593; fn2 cash reconciliation L597-602.
- Lists: guidance bullets L99-119 (10 items: 5 under "now expects" L99-107, 5 under "Additional
  expectations now include" L111-119; "◦" sub-bullets L101, L103, L113, L115). Investor events
  L143-149 (4 items: Wells Fargo Healthcare Conference, September 5, 2025; Baird Healthcare
  Conference, September 9, 2025; Morgan Stanley Global Healthcare Conference, September 10, 2025;
  Nephron Healthcare Summit, September 16, 2025 - last item). Non-GAAP definitions L612-628 (9).
- Forecasts, guidance, deadlines, effective dates (FY2025, bullet form, with "previous" values):
  - L11/L15/L107: adjusted diluted EPS "$15.85 to $16.00, from the previous range of $15.70 to
    $15.95."
  - L99 "Revenue growth to be approximately 9 percent, from the previous range of 8 to 10 percent";
    L101 U.S. revenue growth "9 to 10 percent, from the previous range of 9 to 11 percent"; L103
    International revenue growth "6 to 7 percent, from the previous range of 3 to 4 percent"; L105
    constant-currency International revenue "7 to 8 percent, from the previous range of 6 to 8
    percent"; L111 "Adjusted consolidated operating income growth to be in the range of 15 to 16
    percent, from the previous range of 13.5 to 15.5 percent"; L113 U.S. OI growth "20 to 21
    percent, from the previous range of 17.5 to 19.5 percent"; L115 International OI "decline of
    approximately 6 percent, from the previous range of a decline of 1 to 4 percent"; L117
    constant-currency International OI "decline of approximately 5 percent, from the previous range
    of a decline of 3 percent to flat"; L119 "Adjusted effective tax rate to be in the range of 20.5
    to 21 percent, from the prior expectation of approximately 21 percent."
  - L121: "All other previously communicated aspects of the Company's fiscal year 2025 consolidated
    financial guidance and assumptions remain the same." (diluted shares, interest, FCF, capex not
    restated.)
  - L97 rationale: "primarily to reflect stronger earnings growth in the U.S. Healthcare Solutions
    segment."
  - Dividend L125: $0.55 per share, payable September 3, 2025, record August 15, 2025.
  - Call L129-137: 8:30 a.m. ET August 6, 2025; access code 015103; replay 676245.
- Hedged claims: guidance "approximately" values (L99, L115, L117); L19 quote (strategic drivers).
- Rounded prose beside exact figures:
  - L47 net interest "$81.8 million, an increase of $50.5 million" vs 81,794 / 31,328 (L183).
  - L41 GP margin 3.60% "+35 basis points"; L59 adjusted GP margin 3.55% "+36 basis points"; L63
    adjusted OI margin 1.31% "+13 basis points"; L45 OI margin 1.08% vs 0.91%.
  - L79 U.S. segment OI "$0.9 billion ... up 29.1 percent" vs $901,793 (L431).
  - L83-85 International OI "$156.2 million, a decrease of 12.9 percent"; constant currency revenue
    +8.8%, OI -16.2%.
  - Constant currency prose L630 (no table): Q3 revenue $80.7B "positively impacted by foreign
    currency translation of $116.3 million, resulting in revenue on a constant currency basis of
    $80.5 billion"; adjusted OI $1,058.3M positively impacted by $5.9M -> $1,052.5M (as printed);
    International $7.8B -> $7.7B, OI $156.2M -> $150.4M (as printed); nine months revenue $237.6B,
    negatively impacted by $458.1M -> $238.1B; adjusted OI $3,199.9M, FX $12.5M -> $3,212.4M;
    International nine months $22.4B -> $22.9B, OI $497.6M -> $510.1M.
- Notes: About Cencora L155 "51,000+", "more than $290 billion". Q3 "Other (income) loss, net"
  (110,417) (L182) with fn3 L202-204: "$39.7 million for the Company's portion of an equity method
  investment's gain on the sale of a business, a $27.3 million gain on the remeasurement of an
  equity investment, and a $26.0 million currency remeasurement gain of the deferred tax assets
  relating to 2020 Swiss tax reform". Nine-month fn4 L249 adds "a $35.5 million loss on the
  divestiture of non-core businesses". Purchases of common stock nine months (435,471) (L580; same
  as D02's six-month figure) vs (986,388) prior year. Dividends paid (329,569) (L582). Net debt
  borrowings 3,777,905 (L579) with fn1 L593: "Includes the issuance of $1.8 billion of senior notes
  and a $1.5 billion term loan to finance a portion of the January 2, 2025 acquisition of Retina
  Consultants of America and the issuance of $1.1 billion of senior notes, offset in part by the
  repayment of $500 million of senior notes and a $200 million repayment of the term loan."
  Diluted shares -2.4% "primarily due to share repurchases" (L53).
- Operative definitions, rules and scope exceptions:
  - Adjusted FCF definition L628 with nine-month figure in prose: "For the nine months ended June
    30, 2025, adjusted free cash flow of $92.5 million consisted of net cash provided by operating
    activities of $741.7 million, minus capital expenditures of $418.2 million and gains from
    antitrust litigation settlements of $231.0 million." (Table: 741,703 L570; capex (418,169)
    L572.)
  - Adjusted income before taxes L618 adds "the Company's portion of an equity method investment's
    gain on the sale of a business"; adjusted EPS list L626 likewise.
- Amendments or contradictions: guidance changes stated with "previous" values (L99-119); its
  "previous" revenue (8 to 10%), U.S. revenue (9 to 11%) and tax rate (~21%) figures are not printed
  in D02 (D02 did not restate unchanged items). No other stated amendment.
- Coverage: FULL. Read L1-150, L150-319, L319-488, L488-645. Unread: none. Missing: none.

## D05 - Cencora Reports Fiscal 2026 Third Quarter Results

- Source: `docs/cencora-inc-q3-fy2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt`
  | `text/D05.txt` L1-725; printed page-number lines "1"-"21" (L23 "1" ... L722 "21") | platform
  **Doc 6** (latest release in the bundle).
- Written or submitted by: Cencora, Inc. (dateline L15 "CONSHOHOCKEN, PA, August 5, 2026"). Quotes
  Robert P. Mauch (L19-21). Call participants L142-144: Mauch and "Eva C. Boratto, Executive Vice
  President & Chief Financial Officer" (James F. Cleary, listed as EVP & CFO in the D02, D04, D01
  and D03 call lists, does not appear in D05; D06 prints no participant list). Contact Bennett S. Murphy, SVP Investor Relations and Enterprise Productivity
  (L714-718).
- Type, date, edition: Exhibit 99.1 earnings release dated August 5, 2026. FY2026 guidance edition 4
  of 4 (latest). Section heading changes to "Fiscal Year 2026 Guidance on an Adjusted (non-GAAP)
  Basis" (L105; earlier editions say "Expectations").
- Period covered: "fiscal year 2026 third quarter ended June 30, 2026" (L15). Three-month and
  nine-month tables (June 30, 2026 vs June 30, 2025). Balance sheet June 30, 2026 vs Sep 30, 2025.
  Cash flow nine months. 10-K cited: fiscal year ended September 30, 2025 (L170).
- Entities and aliases:
  - Segments L81: same as D01/D03 but "U.S. Consulting Services (which was divested in April
    2026)". L95: "the April 2026 divestiture of U.S. Consulting Services"; fn4 L269 and fn2 L393
    "Impairment of assets held for sale, including goodwill, related to our U.S. Consulting Services
    business, which was divested in April 2026." No exact divestiture day or price printed.
  - MWI Animal Health: L95 Other OI increase partly from "a decline in depreciation expense resulting
    from its classification as held for sale". Balance sheet "Assets held for sale" 3,836,060 and
    "Liabilities held for sale" 869,700 at June 30, 2026 (L582, L594). No closing of the Covetrus
    merger is reported in D05.
  - OneOncology: "February 2026 acquisition" (L45, L47, L51, L65, L67, L71, L85); "February 2, 2026"
    in cash-flow fn1 L648. Nine-month $1.1 billion remeasurement gain fn5 L271; reconciliation row
    (1,086,612) / (834,152) / $(4.28) per share (L377; D03 printed $(4.27) for the same gain in six
    months, L368).
  - RCA and OneOncology equity units: fn3 L215 "Includes $55.2 million and $37.5 million of
    adjustments to Retina Consultants of America 'RCA' and OneOncology equity units in the three
    months ended June 30, 2026 and 2025, respectively."; fn3 L265 "$152.7 million and $74.9 million
    ... in the nine months ended June 30, 2026 and 2025, respectively." (D04 fn2/fn3 attributed the
    2025 amounts to RCA alone.)
  - Opioid: L47 / fn2 L213 / fn1 L307 "$102.0 million reduction of opioid liability related to the
    dismissal of opioid litigation" (three months ended June 30, 2026). Nine-month fn2 L263 / fn1
    L391 adds "$86.8 million credit related to a derivative lawsuit settlement".
  - People (highlights L101-103): "appointment of Eva Boratto to its Enterprise Leadership Team as
    Executive Vice President & Chief Financial Officer"; "appointment of Samantha Hammock ... as
    Executive Vice President & Chief Human Resources Officer". No appointment dates printed.
    Alias: "Eva Boratto" (L101) = "Eva C. Boratto" (L144).
  - Good Neighbor Pharmacy (L99): "a national franchise for independent pharmacies offered through
    Cencora"; ranked "#1 in Customer Satisfaction with Chain Drug Store Pharmacies" in the "J.D.
    Power 2026 U.S. Pharmacy Study"; "This is the fourteenth time" (cf. D04 L89 "14th annual
    ThoughtSpot" - a different fourteenth).
  - Customers L85: "the 2025 loss of an oncology customer, and lower sales to our large mail order
    customer, as expected and consistent with our second quarter" (no grocery customer mentioned).
  - "Türkiye" throughout; GAAP line label "Other income, net" (L195, L245).
- Tables (thousands):
  - Summary Results L27-37 (no Other income row).
  - Financial Summary three months L182-207 (fn L211-219, page lines "7"/"8" interleaved at L217,
    L221); nine months L231-257 (fn L261-271).
  - GAAP to non-GAAP: Q3 FY26 L283-297 (adj EPS $4.48); Q3 FY25 L323-337 ($4.00); nine months FY26
    L365-381 ($13.31); nine months FY25 L411-425 ($12.15). FY2025 recasts merge rows: Q3 FY25
    "Other, net" (34,007) (L335) = D04's separate "Gain on remeasurement of equity investment"
    (27,259) + "Other, net" (6,748) (D04 L271-272); nine months FY25 "Other, net" 9,226 (L423) =
    D04's (30,559) + 35,539 + 4,246 (D04 L349-351). Totals unchanged ($4.00; $12.15).
  - Summary Segment Information, U.S./International/Other basis with restated FY2025: three months
    L453-498 - Q3 FY26 revenue U.S. $74,860,763, Intl 7,680,456, Other 2,253,330, elims (39,712); Q3
    FY25 restated U.S. $71,342,873, Intl 7,253,396, Other 2,107,464, elims (40,201) (D04 L423-425
    printed 72,876,563 / 7,790,438 / (3,469)); OI Q3 FY26 U.S. $966,178, Intl 165,852, Other
    108,736, elims (2,680); Q3 FY25 restated U.S. $833,650, Intl 137,275, Other 87,104, elims 302
    (D04 L431-433: 901,793 / 156,222 / 316). Nine months L512-558 - FY26 revenue U.S. $219,837,666,
    Intl 22,870,178, Other 6,437,848, elims (102,923); FY25 restated U.S. $210,717,432, Intl
    20,909,070, Other 6,066,326, elims (88,563) (D04 L474-476: 215,193,522 / 22,421,335 /
    (10,592)); OI FY26 U.S. $2,795,808, Intl 483,805, Other 291,786, elims (7,250); FY25 restated
    U.S. $2,465,544, Intl 457,053, Other 277,284, elims 22 (D04 L482-483: 2,702,287 / 497,616).
  - Balance sheet L572-602. Cash flows nine months L614-644 (FY25 column condensed: investing
    "Other, net" (39,172) = D04 (34,814) + (4,358); financing "Other, net" (2,295) = D04 22,613 +
    (24,908); totals unchanged); fn1 L648; fn2 cash reconciliation L652-657.
  - Adjusted FCF reconciliation L689-695 ($M; "nine months ended June 30, 2026"): Operating cash
    flows $1,687.5M; Capex $(511.0)M; Free cash flows $1,176.5M; "Gains from antitrust litigation
    settlements" $(34.2)M; Adjusted free cash flows $1,142.3M. No prior-year column.
  - Constant currency L701-710 (three months ended June 30, 2026): consolidated $84.8B / $1,238M,
    FX "$—B" / $3M, constant currency $84.8B / $1,241M; International $7.7B / $166M -> $7.7B / $169M.
- Lists: highlights L99-103 (3 items; Samantha Hammock last). Investor events L154-158 under the
  singular heading "Upcoming Investor Event" (3 items: Wells Fargo Healthcare Conference, September
  8-10, 2026; Morgan Stanley Global Healthcare Conference, September 14-16, 2026; Baird Global
  Healthcare Conference, September 15, 2026 - last). Non-GAAP definitions L669-687 (9; page line
  "19" at L679).
- Forecasts, guidance, deadlines, effective dates:
  - L11 "Adjusted Diluted EPS Guidance Range Raised to $17.75 to $17.95 for Fiscal 2026"; L17
    "Adjusted diluted EPS guidance has been raised from the previous range of $17.70 to $17.90 to a
    range of $17.75 to $17.95." (D03 L11/L17/L124 printed the range as $17.65 to $17.90; no bundle
    document prints a $17.70 to $17.90 range - see Shared ground.)
  - L13 "Cencora Repurchased $1 Billion of Shares in the Third Fiscal Quarter"; L107 "In the
    quarter, the Company opportunistically repurchased $1 billion of shares, which is the amount that
    the Company previously expected to complete by the end of calendar 2026." Cash flow: purchases of
    common stock (1,000,052) nine months FY26 (L634); D03 six months "—" (D03 L625).
  - Guidance table L109-124, "2026 Guidance(1)" | "Fiscal 2025 Actuals": Revenue 4% to 6% growth |
    $321.3B; U.S. 4% to 6% | $285.0B; International ~8% growth | $28.3B; Other ~6% growth | $8.2B;
    Adjusted operating income 13% to 14% growth | $4.2B; U.S. 14.5% to 15.5% | $3.3B; International
    ~9% growth | $588M; Other ~10% growth | $352M; Adjusted diluted EPS $17.75 to $17.95 | $16.00;
    Net interest expense ~$490M | $292M; Adjusted ETR ~20% | 20.6%; Diluted shares ~194M | 195.2M;
    Adjusted FCF ~$3.0B | $3.0B; Capex ~$900M | $668M. Fn (1) L126 bold note (not rendered); fn (2)
    L128 "please refer to Exhibit 99.2 ... dated November 5, 2025"; fn (3) L132.
  - L107 rationale: "continued strong full year performance and opportunistic share repurchases
    completed in the third quarter".
  - Dividend L136: $0.60 per share, payable August 31, 2026, record August 14, 2026.
  - Call L140-148: 8:30 a.m. ET August 5, 2026; meeting ID "632 369 927"; webcast replay only.
- Hedged claims: L21 quote ("positioning Cencora for sustainable long-term growth"); guidance "~"
  values; L81 Other "exploring strategic alternatives".
- Rounded prose beside exact figures: L51 net interest "$140.7 million, an increase of $58.9
  million" vs 140,705 / 81,794 (L196); L49 OI margin 1.32% "+24 basis points"; L45 GP margin 4.26%
  "+66 basis points"; L65 adj GP margin 4.16% "+61 basis points"; L69 adj OI margin 1.46% "+15 basis
  points"; L91 International cc revenue +6.1%, OI +23.1%; L85 U.S. segment OI "$966.2 million ... up
  15.9 percent"; L95 Other OI "$108.7 million, an increase of 24.8 percent".
- Notes: About Cencora L164 "#10 on the Fortune 500 and #17 on the Global Fortune 500" (D01, D02,
  D03, D04 and D06 say #18); no team-member count. Long-term debt 11,444,086 (L596). Net debt borrowings 3,729,556 (L633)
  with fn1 L648 (OneOncology $3.0B notes + $1.5B term loans; RCA $1.8B notes + $1.5B term loan).
  Dividends paid (360,561) (L635). Cost of acquired companies (4,973,696) (L628).
- Operative definitions, rules and scope exceptions: adjusted FCF definition L687 (same wording);
  adjusted income before taxes L675 now lists "the remeasurement gain related to the OneOncology
  acquisition, gain on an equity method investment, and the gain (loss) on the currency
  remeasurement" (equity-investment remeasurement and non-core divestiture loss no longer named);
  adjusted EPS list L685 likewise.
- Amendments or contradictions: EPS "previous range" statement L17 vs D03's printed range (above).
  FY2025 restated segments and condensed recast rows vs D04 (above). No stated precedence.
- Coverage: FULL. Read L1-150, L150-309, L309-478, L478-647, L647-725. Unread: none. Missing: none.

## D06 - Cencora Reports Fiscal 2025 Fourth Quarter and Fiscal Year End Results

- Source: `docs/cencora-inc-q4-fy2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-11-05.txt`
  | `text/D06.txt` L1-697, no pages | platform **Doc 3**.
- Written or submitted by: Cencora, Inc. (dateline L19 "CONSHOHOCKEN, PA, November 5, 2025").
  Quotes "Bob Mauch, President and Chief Executive Officer" (L21; = Robert P. Mauch elsewhere) and
  "Mr. Mauch" (L23). No call-participant list (L164). Contacts: Bennett S. Murphy, SVP Investor
  Relations and Enterprise Productivity (L688-690).
- Type, date, edition: Exhibit 99.1 Q4 and fiscal-year-end release dated November 5, 2025. Holds
  FY2025 actuals and the FIRST FY2026 guidance edition (1 of 4) plus the only long-term guidance.
- Period covered: "fiscal year 2025 fourth quarter ended September 30, 2025" (L19); three months
  and "Fiscal Year Ended September 30, 2025" vs 2024. Balance sheet Sep 30, 2025 vs Sep 30, 2024
  (L570-572). Cash flow fiscal year. 10-K cited: fiscal year ended September 30, 2024 (L186).
- Entities and aliases:
  - Segments L79 (for FY2025 reporting): "two reportable segments: U.S. Healthcare Solutions and
    International Healthcare Solutions."
  - "Reportable Segments (revised as of October 1, 2025)" L119-121: "Beginning in the first quarter
    of fiscal 2026, the Company's reporting structure will be comprised of U.S. Healthcare
    Solutions, International Healthcare Solutions, and Other. The U.S. Healthcare Solutions
    reportable segment will consist of U.S. Human Health (excluding legacy U.S. Consulting
    Services). The International Healthcare Solutions reportable segment will consist of Alliance
    Healthcare, Innomar, World Courier, and strategic components of PharmaLex. Other, which is not
    considered a reportable segment, will consist of businesses for which the Company has begun to
    explore strategic alternatives and includes MWI Animal Health, Profarma, U.S. Consulting
    Services and the other components of PharmaLex." (Alliance Healthcare, Innomar, World Courier,
    U.S. Human Health appear only here in the bundle.) L21 quote: "the decision to strategically
    refocus our existing business portfolio".
  - PharmaLex goodwill impairment: L47 "a $723.9 million goodwill impairment charge related to
    PharmaLex in the current year period compared to a similar $418.0 million charge in the prior
    year period"; table "Goodwill impairment 4" 723,884 / 418,000 (L207, L255); fn4 L232, L280.
    L53: income tax "did not benefit from the PharmaLex goodwill impairments, which were largely
    not deductible". Reconciliation row label "Impairment of assets, including goodwill" (L324,
    L399): OI column 723,884 but income-before-taxes column 837,378 (the IBT figure is larger than
    the goodwill charge; fn5 L234 separately lists a "$113.5 million impairment of an equity
    investment"; the row itself does not itemize).
  - International OI decline Q4 "primarily due to lower operating income at our specialized
    consulting services business" (L87).
  - RCA: "January 2025 acquisition of Retina Consultants of America ('RCA')" (L45); fn3 L230 RCA
    equity-unit expense adjustments $46.7 million (three months ended Sep 30, 2025) and "increased
    its estimate for contingent consideration related to the RCA acquisition by $19.6 million"; fn3
    L278 $121.7 million for fiscal 2025 plus the same $19.6 million.
  - Equity investments: fn5 L234 Q4 "$113.5 million impairment of an equity investment and a $16.5
    million loss on the remeasurement of an equity investment"; fn5 L282 FY "$113.5 million
    impairment ... $35.5 million loss on the divestiture of non-core businesses, offset in part by
    ... gain on the sale of a business of $39.7 million and a $14.1 million gain on the
    remeasurement of an equity investment".
  - "Turkey" spelling throughout.
- Tables (thousands; segment tables say "(dollars in thousands)"):
  - Q4 Summary Results L27-37 (rows "Income Tax Expense" $146M / $197M and "Diluted Shares
    Outstanding" 193.9M GAAP / 195.3M adjusted; Operating Income "$19M" / "$1.0B").
  - Fiscal Year 2025 Summary Results L91-101 (Revenue $321.3B; GP $11.5B / $11.2B; Opex $8.8B /
    $7.0B; OI $2.6B / $4.2B; Interest $292M; ETR 30.6% / 20.6%; NI $1.6B / $3.1B; EPS $7.96 /
    $16.00; shares 195.2M).
  - Financial Summary Q4 L196-222 (fn L226-234); fiscal year L244-270 (fn L274-282).
  - Reconciliation of diluted weighted average shares L292-299 (Q4 FY25 GAAP 193,899 vs non-GAAP
    195,340; FY25 195,214 both; fn L301 antidilutive RSUs/options).
  - GAAP to non-GAAP: Q4 FY25 L313-328 (adj EPS $3.84); Q4 FY24 L352-366 ($3.34); FY25 L388-405
    ($16.00; adjusted OI 4,222,973); FY24 L429-444 ($13.76).
  - Summary Segment Information, ORIGINAL two-segment basis: Q4 L468-507 - revenue U.S.
    $75,788,501 / 71,671,130, Intl 7,944,988 / 7,382,054, elims (4,935) / (3,078); OI U.S.
    $872,412 / 697,384, Intl 150,658 / 153,673, total 1,023,070 / 851,057 (no eliminations row).
    Fiscal year L519-558 - revenue U.S. $290,982,023 / 265,339,427, Intl 30,366,323 / 28,627,542,
    elims (15,527) / (8,370), total 321,332,819 / 293,958,599; OI U.S. $3,574,699 / 2,934,877, Intl
    648,274 / 713,379, total 4,222,973 / 3,648,256.
  - Balance sheet L570-598 ("Total equity" 1,747,085; "Other long-term liabilities" 3,639,862).
  - Cash flows fiscal year L608-638 (keeps "Non-customer note receivable" (34,814) and "Exercises
    of stock options" 29,133 rows; "Net debt borrowings (repayments) 1" 3,195,668); fn1 L642; fn2
    cash reconciliation L646-652 (Sep 30, 2025 / 2024 / 2023).
- Lists: investor events L172-176 (3 items: Citi Global Healthcare Conference, December 2, 2025;
  Evercore Healthcare Conference, December 2, 2025; J.P. Morgan Healthcare Conference, January
  12-15, 2026 - last). Long-term guidance rows L156-158 (3). Non-GAAP definitions L662-680 (10
  bullets; adds "Adjusted net income/loss attributable to noncontrolling interest" L674).
- Forecasts, guidance, deadlines, effective dates:
  - FY2026 guidance table L129-144, "2026 Guidance" | "Fiscal 2025 Actuals": Revenue 5% to 7% growth
    | $321.3B; U.S. 5% to 7% | $285.0B; International 6% to 8% | $28.3B; Other 0% to 4% | $8.2B;
    Adjusted operating income 8% to 10% growth | $4.2B; U.S. 9% to 11% | $3.3B; International 5%
    to 8% | $588M; Other "1% to 4% decline" | $352M; Adjusted diluted EPS $17.45 to $17.75 |
    $16.00; Net interest expense $315M to $335M | $292M; Adjusted ETR 20% to 21% | 20.6%; Diluted
    shares ~194M | 195.2M; Adjusted FCF ~$3.0B | $3.0B; Capex ~$900M | $668M. No "bolded figures"
    footnote on this table. Fn (1) L146 Exhibit 99.2 "to the Company's form 8-K dated November 5,
    2025"; fn (2) L148 "As reported and constant currency guidance."
  - Long-Term Guidance L150-160: "raising its long-term guidance for adjusted diluted EPS and
    adjusted operating income" (L152); table: Adjusted operating income 6% to 9%; Capital deployment
    3% to 4%; Adjusted diluted earnings per share 9% to 13%. Fn (1) L160 "Bold numbers indicate
    updates to guidance ranges." (bold not rendered; prior long-term ranges not printed anywhere).
  - Dividend L117: "On November 4, 2025, the Company's Board of Directors declared a quarterly
    dividend of $0.60 per common share, a 9 percent increase in its quarterly dividend rate from
    $0.55 per common share ... payable December 1, 2025, to stockholders of record at the close of
    business on November 14, 2025." (Headline L15.)
  - Highlights L113: "$1 billion in investments through 2030 to strengthen its U.S. distribution
    network" incl. "opening a second national distribution center" (planned).
  - Call L164-166: 8:30 a.m. ET November 5, 2025; access code 837725; replay 457149.
- Hedged claims: L23 quote ("will continue driving growth well into the future"); L113 "planned
  investments"; L121 "will consist", "has begun to explore strategic alternatives".
- Rounded prose beside exact figures:
  - L49 OI "$18.5 million, an 85.4 percent decrease" vs 18,503 (L209); summary "$19M" (L32).
  - L51 net interest "$77.8 million, an increase of $56.9 million" vs 77,833 / 20,969 (L211).
  - L53 income tax "$146.0 million and $117.7 million" vs 146,027 / 117,711.
  - L55 diluted EPS "$(1.75) ... a decrease of $1.77"; L57 GAAP shares 193.9M (-2.1%); L75 adjusted
    shares 195.3M (-1.4%).
  - L45 GP margin 3.53% "+38 basis points"; L63 adj GP margin 3.47% "+37 bps"; L65 adj opex margin
    2.25% "+22 bps"; L67 adj OI margin 1.22% "+14 bps"; L105 FY OI margin "increased by 8 basis
    points to 0.82 percent"; L109 FY adjusted OI margin "increased by 7 basis points to 1.31
    percent".
  - L83 U.S. segment OI "$872.4 million ... up 25.1 percent"; L87 International "$150.7 million, a
    decrease of 2.0 percent"; constant currency revenue +5.7%, OI -6.0%.
  - Constant currency prose L684 (no table): Q4 revenue $83.7B "positively impacted by foreign
    currency translation of $140.2 million, resulting in revenue on a constant currency basis of
    $83.6 billion"; Q4 "operating income of $1.0 billion" FX $6.2M -> "$1.0 billion"; International
    Q4 $7.9B -> $7.8B, OI $150.7M -> $144.4M (as printed); FY revenue $321.3B negatively impacted by
    $317.9M -> $321.7B; FY OI $4.2B, FX $6.3M -> $4.2B; International FY revenue "$30.4 billion" ->
    $30.7B, OI "$648.3 million" -> $654.6M (two-segment basis figures).
  - Guidance "Fiscal 2025 Actuals" (rounded): Adjusted FCF $3.0B vs prose $2,970.8M (L680); capex
    $668M vs (667,981) (L621) and prose $668.0M; net interest $292M vs 291,548 (L259).
- Notes: About Cencora L182 "51,000+", "#18 on the Global Fortune 500", "more than $300 billion".
  Purchases of common stock FY25 (435,471) (L629; same figure as D02 six months and D04 nine months)
  vs (1,491,367) FY24. Dividends paid (437,081) (L631). Cash flow fn1 L642: "Includes the issuance
  of $1.8 billion of senior notes and a $1.5 billion term loan to finance a portion of the January 2,
  2025 acquisition of Retina Consultants of America and the issuance of $1.1 billion of senior notes,
  offset in part by $700 million of term loan repayments and the repayment of $500 million of senior
  notes." (D04 fn1 L593 at nine months: "$200 million repayment of the term loan".) Q4 FY24 fn2
  L228 "$49.1 million litigation accrual"; FY24 fn2 L276 "$263.1 million of litigation accruals,
  offset in part by a $92.2 million opioid settlement accrual reduction".
- Operative definitions, rules and scope exceptions:
  - Adjusted FCF definition L680 with FY figure in prose: "For the fiscal year ended September 30,
    2025, adjusted free cash flow of $2,970.8 million consisted of net cash provided by operating
    activities of $3,875.1 million, minus capital expenditures of $668.0 million and the gains from
    antitrust litigation settlements of $236.4 million." (Table: 3,875,120 L619; capex (667,981)
    L621; antitrust gains 236,372 L392.)
  - Adjusted opex L664 excludes "goodwill impairment"; adjusted income before taxes L668 lists Swiss
    remeasurement, "gain (loss) on the divestiture of non-core businesses", equity-method gain,
    "the impairment of an equity investment", equity-investment remeasurement; adjusted income tax
    L670 "discrete tax items primarily attributable to foreign valuation allowance adjustments";
    adjusted EPS L678 includes antidilution share adjustment for the GAAP net loss.
- Amendments or contradictions: segment reorganization announced (L119-121) with the FY2025 tables
  in the same release still on the two-segment basis while the guidance "Fiscal 2025 Actuals" column
  uses the revised basis (U.S. $285.0B vs table $290,982,023; International $28.3B vs 30,366,323;
  U.S. OI $3.3B vs 3,574,699; International OI $588M vs 648,274). No restated FY2025 segment table is
  printed in the bundle (fn (1) L146 points to Exhibit 99.2, not in bundle).
- Coverage: FULL. Read L1-170, L170-319, L319-468, L468-617, L617-697. Unread: none. Missing: none.

## Shared ground (navigation only)

Facts and locations only; the author owns hooks. "n/p" = not printed anywhere in the bundle.

### Entities that appear in more than one document, and where

- Issuer of all six: Cencora, Inc. (NYSE: COR), Conshohocken, PA. Every other organization is
  mentioned, never an issuer: RCA, OneOncology, MWI Animal Health, Profarma, PharmaLex, Covetrus,
  EyeSouth Partners, Good Neighbor Pharmacy (Cencora's franchise), ERM Certification and
  Verification Services (D02 L87), J.D. Power (D05 L99), and conference hosts (events list below).
- Retina Consultants of America / "RCA": D02 L41, L79, L97, L190, L233, L573; D04 L41, L200, L247,
  L593; D06 L21 ("our acquisition of RCA"), L45, L230, L278, L642; D01 L45-85, L426; D03 L108
  (EyeSouth physicians "will join Cencora's Retina Consultants of America ('RCA'), a leading
  management services organization"), L639; D05 L215, L265, L648. Exact date "January 2, 2025" in
  every cash-flow footnote (D02 L573, D04 L593, D06 L642, D01 L426, D03 L639, D05 L648).
- OneOncology: D01 (completion, undated: L15, L19, L21-23, L99, L103); D03 ("February 2026": L46-94;
  "February 2, 2026": L639; gain L52, L62, L214, L262, L285, L299, L368, L386; definitions L666,
  L676); D05 ("February 2026": L45-85; "February 2, 2026": L648; L215, L265, L271, L377, L395,
  L675, L685). Not in D02, D04, D06.
- U.S. Consulting Services: D06 L121 (U.S. segment "excluding legacy U.S. Consulting Services";
  placed in Other); D01 L47, L81, L204, L244 (held for sale; $249.5 million impairment); D03 L86,
  L260, L384; D05 L81, L95, L269, L393 ("divested in April 2026"). Not in D02, D04.
- MWI Animal Health / "MWI": D06 L121; D01 L81, L95; D03 L86, L102, L106 (Covetrus merger
  agreement), L112 (held for sale); D05 L81, L95 (held for sale). Profarma: D06 L121; D01 L81, L95;
  D03 L86, L102; D05 L81, L95. PharmaLex: D06 L47, L53, L121, L232, L280; D01 L81; D03 L86; D05 L81
  (not named in D02, D04; D04 L83 and D06 L87 say "specialized consulting services business").
  Covetrus and EyeSouth Partners: D03 L106, L108 only. Alliance Healthcare, Innomar, World Courier,
  U.S. Human Health: D06 L121 only.
- Good Neighbor Pharmacy: D04 L89 (July 2025 "14th annual ThoughtSpot"); D05 L99 (J.D. Power 2026,
  "the fourteenth time").
- People: Robert P. Mauch, President & CEO - quoted in all six ("Bob Mauch" D06 L21; "Mr. Mauch"
  D03 L21, D05 L21, D06 L23); James F. Cleary, EVP & CFO - call lists D02 L129, D04 L133, D01 L138,
  D03 L149; Eva Boratto / "Eva C. Boratto", EVP & CFO - D05 L101, L144; Samantha Hammock, EVP &
  Chief Human Resources Officer - D05 L103; Bennett S. Murphy - contact in all six, title "Senior
  Vice President, Head of Investor Relations and Treasury" (D02 L618, D04 L638) vs "Senior Vice
  President, Investor Relations and Enterprise Productivity" (D06 L690, D01 L488, D03 L707, D05
  L716).
- Unnamed counterparties: "a grocery customer and an oncology customer" (D01 L85), "the 2025 losses
  of an oncology customer and a grocery customer" + "our large mail order customer" (D03 L90), "the
  2025 loss of an oncology customer" + "large mail order customer" (D05 L85; no grocery customer);
  "a manufacturer customer program" (D01 L95); an unnamed equity-method investee's "gain on the sale
  of a business" $39.7 million (D04 L202/L249, D05 L219/L271, D06 L282).

### Periods or series that more than one document covers, and where

- Release / period chronology: D02 May 7, 2025 (Q2 FY25, quarter ended Mar 31, 2025; + six months)
  -> D04 Aug 6, 2025 (Q3 FY25, June 30, 2025; + nine months) -> D06 Nov 5, 2025 (Q4 FY25, Sep 30,
  2025; + fiscal year) -> D01 Feb 4, 2026 (Q1 FY26, Dec 31, 2025) -> D03 May 6, 2026 (Q2 FY26, Mar
  31, 2026; + six months) -> D05 Aug 5, 2026 (Q3 FY26, June 30, 2026; + nine months). Each call is
  at 8:30 a.m. ET on the release date.
- Consolidated series (thousands; EPS in $). Total segment operating income = adjusted operating
  income in every reconciliation.

  | Period | Revenue | Total segment OI | Adj. diluted EPS | GAAP diluted EPS | Locations |
  |---|---|---|---|---|---|
  | Q1 FY25 (3M Dec 31, 2024) | 81,487,060 | 949,308 | 3.73 | 2.50 | D01 L172, L313, L273, L193 (comparative only) |
  | Q2 FY24 | 68,414,307 | 1,033,784 | 3.80 | 2.09 | D02 L161, L413, L294, L181 |
  | Q2 FY25 | 75,453,673 | 1,192,264 | 4.42 | 3.68 | D02 L161, L413, L256, L181; D03 L185, L460, L330, L205 |
  | 6M FY24 | 140,667,140 | 1,919,503 | 7.08 | 5.07 | D02 L202, L464, L373, L222 |
  | 6M FY25 | 156,940,733 | 2,141,572 | 8.15 | 6.18 | D02 L202, L464, L334, L222; D03 L228, L519, L418, L249 |
  | Q3 FY24 | 74,241,353 | 877,696 | 3.34 | 2.42 | D04 L171, L434, L315, L191 |
  | Q3 FY25 | 80,663,532 | 1,058,331 | 4.00 | 3.52 | D04 L171, L434, L274, L191; D05 L184, L469, L337, L204 |
  | 9M FY24 | 214,908,493 | 2,797,199 | 10.42 | 7.49 | D04 L216, L484, L394, L236 |
  | 9M FY25 | 237,604,265 | 3,199,903 | 12.15 | 9.70 | D04 L216, L484, L353, L236; D05 L233, L528, L425, L254 |
  | Q4 FY24 | 79,050,106 | 851,057 | 3.34 | 0.02 | D06 L198, L481, L366, L219 |
  | Q4 FY25 | 83,728,554 | 1,023,070 | 3.84 | (1.75) | D06 L198, L481, L327, L219 |
  | FY24 | 293,958,599 | 3,648,256 | 13.76 | 7.53 | D06 L246, L532, L444, L267 |
  | FY25 | 321,332,819 | 4,222,973 | 16.00 | 7.96 | D06 L246, L532, L404, L267; rounded "Fiscal 2025 Actuals" D06 L131-144, D01 L107-120, D03 L116-129, D05 L111-124 |
  | Q1 FY26 | 85,932,016 | 1,062,714 | 4.08 | 2.87 | D01 L172, L313, L231, L193 |
  | Q2 FY26 | 78,355,916 | 1,263,349 | 4.75 | 8.40 | D03 L185, L460, L288, L205 |
  | 6M FY26 | 164,287,932 | 2,326,063 | 8.83 | 11.27 | D03 L228, L519, L371, L249 |
  | Q3 FY26 | 84,754,837 | 1,238,086 | 4.48 | 3.94 | D05 L184, L469, L296, L204 |
  | 9M FY26 | 249,042,769 | 3,564,149 | 13.31 | 15.21 | D05 L233, L528, L380, L254 |

- Periods with no standalone release: Q1 FY25 (only D01's comparative column and inside D02's
  six-month totals); Q4 FY26 / FY26 (absent). Q4 FY25 three-month figures appear only in D06.
- Net interest expense, net (thousands): Q1 FY25 27,933 / Q1 FY26 72,409 (D01 L185); Q2 64,130 /
  103,988 / 140,460 (D02 L173, D03 L197); 6M 104,694 / 131,921 / 212,869 (D02 L214, D03 L241); Q3
  31,328 / 81,794 / 140,705 (D04 L183, D05 L196); 9M 136,022 / 213,715 / 353,574 (D04 L228, D05
  L246); Q4 FY24 20,969 / Q4 FY25 77,833 (D06 L211); FY24 156,991 / FY25 291,548 (D06 L259).
- Diluted weighted shares (thousands): Q1 FY25 195,188 / Q1 FY26 195,319 (D01 L196); Q2 FY25
  195,094 / Q2 FY26 195,383 (D03 L208); Q3 FY25 195,230 / Q3 FY26 193,944 (D05 L207); 9M FY25
  195,172 / 9M FY26 194,883 (D05 L257); Q4 FY25 GAAP 193,899 vs non-GAAP 195,340 (D06 L297-299);
  FY25 195,214 (D06 L270).
- Balance sheets: Sep 30, 2024 in D02 L503, D04 L523, D06 L572 (total assets 67,101,667 in each);
  Sep 30, 2025 in D06 L572, D01 L357, D03 L565, D05 L574 (total assets 76,590,112; D06 labels "Total
  equity" / "Other long-term liabilities", D01/D03/D05 "Total stockholders' equity" / "Other
  liabilities", same values 1,747,085 / 3,639,862). Long-term debt: Sep 30, 2024 3,811,745; Mar 31,
  2025 7,085,886 (D02 L523); Jun 30, 2025 8,043,699 (D04 L543); Sep 30, 2025 7,542,988 (D06 L592);
  Dec 31, 2025 7,579,459 (D01 L377); Mar 31, 2026 12,182,860 (D03 L587); Jun 30, 2026 11,444,086
  (D05 L596).

### Segment reorganization and the two FY2025 bases

- Announcement: D06 L119-121 "Reportable Segments (revised as of October 1, 2025)", "Beginning in the
  first quarter of fiscal 2026". Two-segment wording (no Other): D02 L75, D04 L75, D06 L79.
  Three-part wording (two reportable segments + Other "exploring strategic alternatives"): D01 L81,
  D03 L86, D05 L81. D06 L121 says Other "is not considered a reportable segment".
- Original two-segment tables: D02 L399-489, D04 L420-509, D06 L468-558. Restated U.S./
  International/Other tables: D01 L297-343 (Q1 FY25 comparative), D03 L444-549 (Q2 and 6M FY25),
  D05 L453-558 (Q3 and 9M FY25). Consolidated revenue and total segment OI are unchanged by the
  restatement; segment splits, eliminations and segment margin blocks change.

  | Period / line | Original (two-segment) | Restated (three-part) |
  |---|---|---|
  | Q1 FY25 revenue U.S. / Intl / Other / elims | n/p (only inside D02 6M totals) | 72,555,294 / 6,958,895 / 2,002,455 / (29,584) (D01 L300-303) |
  | Q1 FY25 OI U.S. / Intl / Other / elims | n/p | 686,925 / 165,180 / 97,329 / (126) (D01 L309-312) |
  | Q2 FY25 revenue U.S. / Intl / Other / elims | 68,283,831 / 7,173,556 / - / (3,714) (D02 L402-404) | 66,819,265 / 6,696,779 / 1,956,407 / (18,778) (D03 L447-450) |
  | Q2 FY25 OI U.S. / Intl / Other / elims | 1,033,150 / 159,301 / - / (187) (D02 L410-412) | 944,969 / 154,598 / 92,851 / (154) (D03 L456-459) |
  | 6M FY25 revenue U.S. / Intl / Other / elims | 142,316,959 / 14,630,897 / - / (7,123) (D02 L453-455) | 139,374,559 / 13,655,674 / 3,958,862 / (48,362) (D03 L506-509) |
  | 6M FY25 OI U.S. / Intl / Other / elims | 1,800,494 / 341,394 / - / (316) (D02 L461-463) | 1,631,894 / 319,778 / 190,180 / (280) (D03 L515-518) |
  | Q3 FY25 revenue U.S. / Intl / Other / elims | 72,876,563 / 7,790,438 / - / (3,469) (D04 L423-425) | 71,342,873 / 7,253,396 / 2,107,464 / (40,201) (D05 L456-459) |
  | Q3 FY25 OI U.S. / Intl / Other / elims | 901,793 / 156,222 / - / 316 (D04 L431-433) | 833,650 / 137,275 / 87,104 / 302 (D05 L465-468) |
  | 9M FY25 revenue U.S. / Intl / Other / elims | 215,193,522 / 22,421,335 / - / (10,592) (D04 L474-476) | 210,717,432 / 20,909,070 / 6,066,326 / (88,563) (D05 L515-518) |
  | 9M FY25 OI U.S. / Intl / Other / elims | 2,702,287 / 497,616 / - / no row (D04 L482-483) | 2,465,544 / 457,053 / 277,284 / 22 (D05 L524-527) |
  | Q4 FY25 revenue / OI | U.S. 75,788,501, Intl 7,944,988, elims (4,935); OI 872,412 / 150,658 (D06 L471-480) | n/p |
  | FY25 revenue U.S. / Intl / Other | 290,982,023 / 30,366,323 / - (D06 L522-523) | $285.0B / $28.3B / $8.2B (rounded; D06 L132-134, D01 L108-110, D03 L117-119, D05 L112-114) |
  | FY25 OI U.S. / Intl / Other | 3,574,699 / 648,274 / - (D06 L530-531) | $3.3B / $588M / $352M (rounded; D06 L136-138, D01 L112-114, D03 L121-123, D05 L116-118) |

- Segment growth percentages in each release are computed against that release's own basis (e.g.
  Q2 FY25 U.S. revenue +11.4% on the original basis, D02 L39/L402; Q2 FY26 U.S. +2.9% against the
  restated 66,819,265, D03 L44/L447).
- Segment margin blocks restated too, e.g. Q2 FY25 U.S. operating income margin 1.51% (D02 L426) vs
  1.41% (D03 L473); Q3 FY25 U.S. 1.24% (D04 L447) vs 1.17% (D05 L482).

### Forecast/actual pairs, changed guidance tables across editions, same-series conflicts

- FY2025 guidance (bullet lists; only changed items are printed):

  | Metric | "Previous" per D02 | D02 (May 7, 2025) | "Previous" per D04 | D04 (Aug 6, 2025) | FY2025 actual in D06 |
  |---|---|---|---|---|---|
  | Adjusted diluted EPS | $15.30 to $15.60 | $15.70 to $15.95 (L101) | $15.70 to $15.95 | $15.85 to $16.00 (L107) | $16.00 (L13, L404) |
  | Revenue growth | n/p | n/p | 8 to 10% | ~9% (L99) | 9.3% (L19, L246) |
  | U.S. revenue growth | n/p | n/p | 9 to 11% | 9 to 10% (L101) | 9.7%, two-segment (L522) |
  | International revenue growth | 4 to 5% | 3 to 4% (L105) | 3 to 4% | 6 to 7% (L103) | 6.1%, two-segment (L523) |
  | Intl revenue, constant currency | 7 to 9% | 6 to 8% (L107) | 6 to 8% | 7 to 8% (L105) | FY amounts only, no % (L684: $30.4B; $30.7B constant currency) |
  | Adjusted consolidated OI growth | 11.5 to 13.5% | 13.5 to 15.5% (L109) | 13.5 to 15.5% | 15 to 16% (L111) | 15.8% (L109, L405, L532) |
  | U.S. segment OI growth | 14.5 to 16.5% | 17.5 to 19.5% (L111) | 17.5 to 19.5% | 20 to 21% (L113) | 21.8%, two-segment (L530) |
  | International OI | "no growth" | decline of 1 to 4% (L113) | decline of 1 to 4% | decline of ~6% (L115) | (9.1)%, two-segment (L531) |
  | Intl OI, constant currency | increase of ~5% | down 3% to flat (L115) | decline of 3% to flat | decline of ~5% (L117) | FY amounts only (L684: $648.3M; $654.6M) |
  | Diluted shares | under 196 million | 195.0 to 195.5 million (L117) | n/p | unchanged per L121 | 195.2M (L101), 195,214 (L270) |
  | Adjusted effective tax rate | n/p | n/p | ~21% | 20.5 to 21% (L119) | 20.6% (L98) |
  | Net interest / adj. FCF / capex | n/p | n/p | n/p | n/p | 291,548 (L259) / $2,970.8M (L680) / 667,981 (L621) |

  D04's "previous" values for EPS, International, constant-currency, OI and U.S. OI rows equal
  D02's new values; D04's previous revenue, U.S. revenue and tax-rate values have no printed source
  in the bundle.
- FY2026 guidance (tables; verbatim cells):

  | Row | D06 L129-144 (Nov 5, 2025) | D01 L105-120 (Feb 4, 2026) | D03 L114-129 (May 6, 2026) | D05 L109-124 (Aug 5, 2026) | Fiscal 2025 Actuals (all four) |
  |---|---|---|---|---|---|
  | Revenue | 5% to 7% growth | 7% to 9% growth | 4% to 6% growth | 4% to 6% growth | $321.3B |
  | U.S. Healthcare Solutions | 5% to 7% growth | 7% to 9% growth | 4% to 6% growth | 4% to 6% growth | $285.0B |
  | International Healthcare Solutions | 6% to 8% growth | 7% to 9% growth | 8% to 10% growth | ~8% growth | $28.3B |
  | Other | 0% to 4% growth | 1% to 5% growth | 1% to 5% growth | ~6% growth | $8.2B |
  | Adjusted operating income | 8% to 10% growth | 11.5% to 13.5% growth | 12% to 14% growth | 13% to 14% growth | $4.2B |
  | U.S. Healthcare Solutions | 9% to 11% growth | 14% to 16% growth | 14% to 16% growth | 14.5% to 15.5% growth | $3.3B |
  | International Healthcare Solutions | 5% to 8% growth | 5% to 8% growth | 5% to 8% growth | ~9% growth | $588M |
  | Other | 1% to 4% decline | Flat | High-single digit growth | ~10% growth | $352M |
  | Adjusted diluted EPS | $17.45 to $17.75 | $17.45 to $17.75 | $17.65 to $17.90 | $17.75 to $17.95 | $16.00 |
  | Net interest expense | $315M to $335M | $480M to $500M | ~$485M | ~$490M | $292M |
  | Adjusted effective tax rate | 20% to 21% | ~20% | ~20% | ~20% | 20.6% |
  | Diluted weighted average shares | ~194M | 195.5M | Under 195.5M | ~194M | 195.2M |
  | Adjusted free cash flow | ~$3.0B | ~$3.0B | ~$3.0B | ~$3.0B | $3.0B |
  | Capital expenditures | ~$900M | ~$900M | ~$900M | ~$900M | $668M |

  International footnote: D06 L148 "As reported and constant currency guidance."; D01 L126, D03 L137,
  D05 L132 "As reported guidance" (constant currency only in slides). Prose-stated changes: D01 L19
  (adjusted OI "from the previous range of growth of 8% to 10%" - equals D06 L135); D01 L13/L103
  (EPS reaffirmed); D03 L17 (EPS "previous range of $17.45 to $17.75" - equals D01 L115); D03 L112
  ("narrowed its expectations for interest expense", "incrementally lower expected share count",
  Other OI because MWI is held for sale); D05 L17 (EPS "previous range of $17.70 to $17.90"). No
  FY2026 full-year actuals in the bundle; latest year-to-date is nine months (D05).
- Same-series conflict: D05 L17 states the previous EPS range as $17.70 to $17.90; the bundle's
  preceding edition D03 prints $17.65 to $17.90 (D03 L11, L17, L124). No document prints $17.70 as a
  lower bound, mentions an intervening update, or states which figure governs.
- Long-term guidance: D06 L150-160 only (adjusted OI 6% to 9%; capital deployment 3% to 4%; adjusted
  diluted EPS 9% to 13%); previous long-term ranges n/p.
- Expectation -> outcome pairs: share repurchase "Expects to Repurchase $1 Billion in Shares by the
  End of Calendar 2026" (D03 L13; L21, L112) -> "Repurchased $1 Billion of Shares in the Third Fiscal
  Quarter" (D05 L13, L107; cash flow (1,000,052) nine months L634 vs "—" six months D03 L625 and Q1
  D01 L413). U.S. Consulting Services held for sale (D01 L47) -> "divested in April 2026" (D05 L81).
  MWI-Covetrus merger agreement (D03 L106) and MWI held for sale (D03 L112) -> still held for sale
  (D05 L95, L582, L594); no merger completion printed. EyeSouth agreement (D03 L108) -> no later
  mention. $1 billion distribution investments through 2030 (D06 L113) -> no later mention.

### Adjusted free cash flow (same definition text in all six: D02 L608, D04 L628, D06 L680, D01 L461, D03 L678, D05 L687)

| Period (all year-to-date) | Adjusted FCF | Printed components | Location / form |
|---|---|---|---|
| Six months ended Mar 31, 2025 | $176.0 million | OCF $632.5M, capex $235.0M, antitrust gains $221.5M | D02 L608, prose |
| Nine months ended June 30, 2025 | $92.5 million | OCF $741.7M, capex $418.2M, antitrust gains $231.0M | D04 L628, prose |
| Fiscal year ended Sep 30, 2025 | $2,970.8 million ("$3.0B" in actuals columns) | OCF $3,875.1M, capex $668.0M, antitrust gains $236.4M | D06 L680, prose |
| Three months ended Dec 31, 2025 | $(2,436.7)M | OCF $(2,305.2)M, capex $(119.4)M, FCF $(2,424.5)M, "(Less) gains" $(12.2)M | D01 L463-469, table |
| Six months ended Mar 31, 2026 | $(1,280.2)M | OCF $(966.5)M, capex $(285.0)M, FCF $(1,251.5)M, "Less gains" $(28.7)M | D03 L680-686, table |
| Nine months ended June 30, 2026 | $1,142.3M | OCF $1,687.5M, capex $(511.0)M, FCF $1,176.5M, "Gains from antitrust litigation settlements" $(34.2)M | D05 L689-695, table |

- No release prints prior-year adjusted FCF or a standalone non-Q1 quarter. The only printed
  adjustment in every reconciliation is antitrust settlement gains; other legal items in the same
  periods (D01 $86.8M derivative-lawsuit credit; D05 $102.0M opioid liability reduction) do not
  appear in the FCF reconciliations. FY2025 adjusted FCF guidance n/p; FY2026 ~$3.0B in all four
  editions.
- Underlying cash-flow lines (thousands): OCF D02 L550 632,456; D04 L570 741,703; D06 L619
  3,875,120; D01 L404 (2,305,169) [Q1 FY25 (2,718,782)]; D03 L616 (966,530); D05 L625 1,687,530.
  Capex D02 L552 (234,953); D04 L572 (418,169); D06 L621 (667,981); D01 L406 (119,376) [(105,893)];
  D03 L618 (284,994); D05 L627 (511,033). Antitrust gains: Q1 FY25 22,870 (D01 L262); Q2 FY25
  198,646; 6M FY25 221,516; Q3 FY25 9,495; 9M FY25 231,011; Q4 FY25 5,361 (D06 L317); FY25 236,372;
  Q1 FY26 12,152; Q2 FY26 16,538; 6M FY26 28,690; Q3 FY26 5,494; 9M FY26 34,184.

### Recast comparatives (same period, different presentation)

- Cash-flow statements: D02 six months FY25 vs D03's FY25 column (D03 folds "Non-customer note
  receivable" (34,814) into investing "Other, net" (45,372) and "Exercises of stock options" 15,778
  into financing "Other, net" (2,984)); D04 nine months FY25 vs D05's FY25 column (investing "Other,
  net" (39,172); financing "Other, net" (2,295)). Totals unchanged. Q1 FY25 cash flow only in D01.
- Reconciliations: D05 Q3 FY25 "Other, net" (34,007) merges D04's "Gain on remeasurement of equity
  investment" (27,259) and "Other, net" (6,748); D05 nine-month FY25 "Other, net" 9,226 merges D04's
  (30,559), 35,539 and 4,246. D03 restates D02's Q2/6M FY25 reconciliations with identical numbers
  but new labels.
- Label/spelling variants: "Turkey" (D02, D04, D06) vs "Türkiye" (D01, D03, D05, including restated
  FY2025 rows); "Acquisition-related deal and integration expenses" (D02, D04, D06, D01) vs
  "Acquisition and divestiture-related deal and integration expenses" (D03, D05, applied to FY2025
  values too); "Goodwill impairment" (D06 tables) vs "Impairment of assets, including goodwill" (D06
  reconciliation L324/L399; D01, D03, D05); "Other (income) loss, net" (D04, D01, D03), "Other loss
  (income), net" (D06 L210), "Other loss, net" (D02 L172, D06 L258), "Other income, net" (D05 L195).
- About Cencora boilerplate: Global Fortune 500 "#18" (D02 L145, D04 L155, D06 L182, D01 L156, D03
  L165) vs "#17" (D05 L164); "more than $290 billion" (D02, D04) vs "more than $300 billion" (D06,
  D01, D03, D05); "51,000+" team members (D02, D04, D06, D01) vs no count (D03, D05).

### Dated events and where reported (first -> last mention)

- RCA acquisition, January 2, 2025: D02 (first) ... D05 L648 (last). Financing: $1.8 billion senior
  notes "in December 2024" and $1.5 billion variable-rate term loan "borrowed in January 2025" (D02
  L47); repeated in cash-flow fn of every release. Q1 FY25 fn (D01 L426): "$2.0 billion of net
  borrowings to cover seasonal short-term working capital needs and the issuance of $1.8 billion of
  senior notes". RCA 15% retained equity as contingent liability (D02 L97 only). Contingent
  consideration +$19.6 million (D06 L230, L278 only).
- RCA (and later OneOncology) equity-unit expense adjustments: Q2 FY25 $37.5M (D02 L190, L233); Q3
  FY25 $37.5M (D04 L200; D05 L215); 9M FY25 $74.9M (D04 L247; D05 L265); Q4 FY25 $46.7M (D06 L230);
  FY25 $121.7M (D06 L278); Q3 FY26 $55.2M and 9M FY26 $152.7M "RCA and OneOncology" (D05 L215, L265).
- Debt: $1.1 billion senior notes issued; $500 million senior notes repaid; term loan repayment "$200
  million" at nine months (D04 L593) and "$700 million of term loan repayments" for the fiscal year
  (D06 L642). OneOncology financing "$3.0 billion of senior notes and $1.5 billion of term loans"
  (D03 L639; D05 L648).
- OneOncology acquisition: completion first reported D01 L15/L99 (no date); dated "February 2026"
  (D03 L46) and "February 2, 2026" (D03 L639, D05 L648); $1.1 billion remeasurement gain in Q2 FY26
  (D03 L52; D05 L271 nine months).
- U.S. Consulting Services: held for sale + $249.5M impairment in Q1 FY26 (D01 L47, L181, L204);
  "divested in April 2026" (D05 L81, L95, L269, L393).
- PharmaLex goodwill impairments: $723.9M Q4 FY25 and $418.0M Q4 FY24 (D06 L47, L207, L232, L255,
  L280). Equity investment impairment $113.5M Q4 FY25 (D06 L234, L282).
- Opioid / litigation: $214.0M accrual Q2 FY24 (D02 L43, L304, L231, L383; D04 L245, L404); $92.2M
  accrual reduction in 6M FY24 (D02), 9M FY24 (D04), FY24 (D06 L276); $49.1M litigation accrual Q4
  FY24 (D06 L228); $263.1M FY24 litigation accruals (D06 L276); $86.8M derivative-lawsuit credit Q1
  FY26 (D01 L47, L202, L242; D03 L258, L382; D05 L263, L391); $102.0M opioid liability reduction
  "related to the dismissal of opioid litigation" Q3 FY26 (D05 L47, L213, L263, L307, L391).
- Segment revision "as of October 1, 2025" (D06 L119). MWI-Covetrus merger agreement and EyeSouth
  agreement (D03 L106, L108; undated). Appointments of Eva Boratto and Samantha Hammock (D05
  L101-103; undated). $1 billion investments through 2030 (D06 L113). 2024 Corporate Responsibility
  Report (D02 L87). ThoughtSpot, July 2025 (D04 L89). J.D. Power 2026 U.S. Pharmacy Study (D05 L99).
- Share repurchases (thousands, cash flow "Purchases of common stock"): Q1 FY25 (385,471) and Q1
  FY26 "—" (D01 L413); 6M FY25 (435,471) (D02 L560; D03 L625); 9M FY25 (435,471) (D04 L580; D05
  L634); FY25 (435,471), FY24 (1,491,367) (D06 L629); 6M FY26 "—" (D03 L625); 9M FY26 (1,000,052)
  (D05 L634).
- Dividends declared (per share; payable; record): $0.55, June 2, 2025, May 16, 2025 (D02 L121);
  $0.55, September 3, 2025, August 15, 2025 (D04 L125); $0.60 declared November 4, 2025 ("a 9 percent
  increase" from $0.55), December 1, 2025, November 14, 2025 (D06 L117); $0.60, March 2, 2026,
  February 13, 2026 (D01 L130); $0.60, June 1, 2026, May 15, 2026 (D03 L141); $0.60, August 31, 2026,
  August 14, 2026 (D05 L136). Dividends paid (cash flow): D01 L415, D02 L562, D03 L626, D04 L582, D05
  L635, D06 L631.
- Investor conferences (16 entries; last item of each list marked *): D02 L139 Bank of America Global
  Healthcare Conference, May 13, 2025*; D04 L143-149 Wells Fargo Healthcare Conference, Sep 5, 2025;
  Baird Healthcare Conference, Sep 9, 2025; Morgan Stanley Global Healthcare Conference, Sep 10,
  2025; Nephron Healthcare Summit, Sep 16, 2025*; D06 L172-176 Citi Global Healthcare Conference, Dec
  2, 2025; Evercore Healthcare Conference, Dec 2, 2025; J.P. Morgan Healthcare Conference, Jan 12-15,
  2026*; D01 L148-150 Leerink Partners Global Healthcare Conference, Mar 8-11, 2026; Barclays Global
  Healthcare Conference, Mar 10-12, 2026*; D03 L159 Bank of America Global Healthcare Conference, May
  12-14, 2026*; D05 L154-158 Wells Fargo Healthcare Conference, Sep 8-10, 2026; Morgan Stanley Global
  Healthcare Conference, Sep 14-16, 2026; Baird Global Healthcare Conference, Sep 15, 2026*. Hosts
  repeated across years: Bank of America (D02, D03), Wells Fargo (D04, D05), Morgan Stanley (D04,
  D05), Baird (D04 "Baird Healthcare Conference" vs D05 "Baird Global Healthcare Conference").

### Same-period figures printed differently across or within releases (index)

- Segment revenue/OI for Q2, 6M, Q3, 9M FY25: original (D02, D04) vs restated (D03, D05) - table in
  "Segment reorganization" above; consolidated totals identical in both editions.
- FY2025 segments within D06 and the three later guidance tables: exact two-segment table values
  (D06 L522-531) vs rounded three-part "Fiscal 2025 Actuals" (D06 L132-138; D01 L108-114; D03
  L117-123; D05 L112-118). International FY2025 revenue also appears as "$30.4 billion" in D06's
  constant-currency prose (L684).
- FY2025 rounded actuals vs exact: adjusted FCF "$3.0B" (D06 L143, D01 L119, D03 L128, D05 L123) vs
  $2,970.8 million (D06 L680); capex "$668M" vs (667,981) (D06 L621) and "$668.0 million" (L680); net
  interest "$292M" vs 291,548 (D06 L259); adjusted OI "$4.2B" vs 4,222,973 (D06 L404, L532).
- FY2026 EPS guidance range before the D05 raise: "$17.65 to $17.90" (D03 L11, L17, L124) vs "the
  previous range of $17.70 to $17.90" (D05 L17).
- Same 2025 equity-unit amounts described differently: "$37.5 million" Q3 FY25 and "$74.9 million"
  9M FY25 attributed to RCA (D04 L200, L247) vs to "RCA and OneOncology equity units" (D05 L215,
  L265).
- Same values, regrouped rows: Q3 FY25 and 9M FY25 reconciliation "Other, net" (D04 L271-272,
  L349-351 vs D05 L335, L423); 6M and 9M FY25 cash-flow investing/financing "Other, net" (D02
  L555-564 vs D03 L621-628; D04 L575-584 vs D05 L630-637).
- Same values, relabelled lines: Q3 FY25 "Other (income) loss, net" (110,417) (D04 L182) = "Other
  income, net" (110,417) (D05 L195); Q2 FY25 "Other loss, net" 3,546 (D02 L172) = "Other (income)
  loss, net" 3,546 (D03 L196); "Turkey" vs "Türkiye"; "Acquisition-related" vs "Acquisition and
  divestiture-related" deal and integration expenses (D02/D04 vs D03/D05 for the same FY2025 values).
- Restated segment margin percentages for the same FY2025 periods (D02 L422-489 vs D03 L469-549; D04
  L443-509 vs D05 L478-558).
- Within one release, by definition: Q4 FY25 diluted shares 193.9M GAAP vs 195.3M adjusted (D06
  L37, L57, L75, L297-301); D01 prose "$86.8 million" litigation credit (L47) vs net line (86,151)
  (L178) with fn2 L202 identifying $86.8M as the derivative-lawsuit component.
- Same item, different period: OneOncology remeasurement gain per share $(4.27) for Q2 FY26 and 6M
  FY26 (D03 L285, L368) vs $(4.28) for 9M FY26 (D05 L377), pre-tax (1,086,612) in all three.

### First / last mention index (release order D02 -> D04 -> D06 -> D01 -> D03 -> D05)

| Event / item | First reported | Last reported |
|---|---|---|
| RCA acquisition (January 2, 2025) and its $1.8B notes / $1.5B term loan | D02 (L41, L47, L573) | D05 (L648) |
| RCA 15% retained equity as contingent liability | D02 L97 | D02 only |
| $1.1B senior notes issued, $500M notes repaid | D04 L593 | D06 L642 |
| Term loan repayment ($200 million -> $700 million) | D04 L593 | D06 L642 |
| Equity-method investee's $39.7M gain on sale of a business | D04 L202 | D05 L219, L271 (prior-year) |
| Segment revision (as of October 1, 2025) | D06 L119-121 | applied through D05 (L81) |
| PharmaLex goodwill impairments; $113.5M equity-investment impairment | D06 L47, L234 | D06 only |
| Dividend raised to $0.60 (declared November 4, 2025) | D06 L15, L117 | $0.60 declared again in D05 L136 |
| $1 billion distribution investments through 2030 | D06 L113 | D06 only |
| Long-term guidance | D06 L150-160 | D06 only |
| OneOncology acquisition (completed; dated February 2, 2026 from D03) | D01 L15, L99 | D05 L648 |
| U.S. Consulting Services held for sale / $249.5M impairment | D01 L47 | divested April 2026: D05 L81, L393 |
| Derivative-lawsuit $86.8M credit | D01 L202 | D05 L263, L391 |
| OneOncology financing ($3.0B notes, $1.5B term loans) and $1.1B remeasurement gain | D03 L52, L639 | D05 L271, L648 |
| MWI-Covetrus merger agreement; MWI held for sale | D03 L106, L112 | held for sale still in D05 L95 |
| EyeSouth Partners retina-business agreement | D03 L108 | D03 only |
| Expected $1B repurchase by end of calendar 2026 | D03 L13 | completion D05 L13, L107 |
| $102.0M opioid liability reduction (dismissal of opioid litigation) | D05 L47 | D05 only |
| Eva Boratto (CFO) and Samantha Hammock (CHRO) appointments | D05 L101-103 | D05 only |
| James F. Cleary as CFO on call list | D02 L129 | D03 L149 |
| 2024 Corporate Responsibility Report / ThoughtSpot July 2025 / J.D. Power 2026 | D02 L87 / D04 L89 / D05 L99 | each in one release only |

### Documents that cite, amend or respond to another document in the bundle

- Guidance "previous" statements: D02 L15/L101-117 (refers to a pre-bundle edition); D04 L15/L99-119
  (D02 values plus pre-bundle values); D01 L19 (D06's adjusted OI range); D03 L17 (D01's EPS range);
  D05 L17 (an EPS range differing from D03's) and D05 L107 ("the amount that the Company previously
  expected to complete by the end of calendar 2026" - D03 L13).
- D06 announces the segment revision applied in D01, D03, D05; all FY2026 guidance footnotes point
  to Exhibit 99.2 of the November 5, 2025 8-K (D06 is Exhibit 99.1 of that date; 99.2 not in bundle).
- 10-K citations: fiscal year ended Sep 30, 2024 (D02 L149, D04 L159, D06 L186); Sep 30, 2025 (D01
  L160, D03 L171, D05 L170).

### Narrative / overview passages that repeat table results (rounded)

- Headlines + summary tables + GAAP/adjusted bullets + segment prose: D02 L7-11, L23-33, L39-71,
  L77-83; D04 L7-11, L23-33, L39-71, L77-85; D06 L7-17, L27-37, L43-75, L81-87, FY L91-109; D01
  L7-15, L27-37, L43-77, L83-95; D03 L7-13, L27-38, L44-82, L88-102; D05 L7-13, L27-37, L43-77,
  L83-95. Constant-currency results: prose only in D02 L610, D04 L630, D06 L684; tables in D01
  L473-482, D03 L692-701, D05 L701-710.

### Hedge scope, actions vs mentions, exclusions

- Completed actions stated as done: RCA acquisition; OneOncology acquisition (D01 L99); U.S.
  Consulting Services divestiture (D05 L81); $1 billion repurchase (D05 L107); dividend declarations;
  appointments "announced" (D05 L101-103). Agreements / plans / expectations only: MWI-Covetrus
  "will merge" (D03 L106); EyeSouth "Upon completion of the transaction" (D03 L108); "planned
  investments" through 2030 (D06 L113); repurchase "Expects" (D03 L13); Other businesses "exploring
  strategic alternatives" (D01 L81, D03 L86, D05 L81) / "has begun to explore" (D06 L121).
- Guidance qualifiers "~" / "approximately" (D04 L99, L115, L117, L119; D03, D05, D06 tables);
  forward-looking boilerplate D02 L149, D04 L159, D06 L186, D01 L160, D03 L171, D05 L170.
- Negative evidence: no participant list in D06 (L164); no "Other" grouping in D02/D04; no
  intersegment-eliminations row in D04 nine-month OI (L482-484) and D06 Q4/FY OI tables (L479-481,
  L530-532); constant-currency FX revenue impact printed "$—B" in D05 (L705, L709); D05 no longer
  names the grocery customer (L85); no repurchases in Q1 FY26 or 6M FY26; no bold-update footnote on
  D06's FY2026 table.
- Identical printed values for different periods/items (location aid for entity/period
  resolution): adjusted EPS $3.34 in both Q3 FY24 (D04 L13, L315) and Q4 FY24
  (D06 L73, L366); $37.5M equity-unit adjustments in Q2 FY25 (D02 L190) and Q3 FY25 (D04 L200);
  GAAP diluted shares 193.9M in Q4 FY25 (D06 L57) and Q3 FY26 (D05 L57); 195.3M in Q4 FY25 adjusted
  (D06 L75) and Q1 FY26 (D01 L59); "$1 billion" for 2030 investments (D06 L113) and repurchases (D03
  L13, D05 L13); "$1.1 billion" for 2025 senior notes (D04 L593, D06 L642) and the OneOncology gain
  (D03 L52); "14th" ThoughtSpot (D04 L89) vs "fourteenth" J.D. Power recognition (D05 L99).
