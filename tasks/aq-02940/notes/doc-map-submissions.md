# aq-02940 - document map, part: submissions and merchant survey

Part file written by the bundle-mapper for 14 of the 16 documents (D01-D05, D07-D12, D14-D16).
D06 (Keystone report) and D13 (draft decision) are NOT mapped here; another mapper / the caller
has them. The caller merges this part into `notes/doc-map.md`.
Navigation only: where things are, not what to ask. Questions quote the documents, never this map.
Line numbers are the `text/Dnn.txt` line numbers (line 1 is the `# Dnn | docs/...` header line the
extraction tool adds; the last line of every file is `-----`).

## Bundle (this part)

- What it is: submissions to the New Zealand Commerce Commission on its draft decision to cap
  commercial credit card interchange fees for the Mastercard and Visa networks, plus the
  Commission's merchant survey slide pack.
- Documents in this part: 14. Local id -> platform Doc number: D01=Doc 3, D02=Doc 4, D03=Doc 5,
  D04=Doc 6, D05=Doc 7, D07=Doc 9, D08=Doc 10, D09=Doc 2, D10=Doc 15, D11=Doc 16, D12=Doc 11,
  D14=Doc 12, D15=Doc 13, D16=Doc 14.
- Provenance: `notes/intake.json` marks every document `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true`. Sources are plain-text captures (`docs/*.txt`), `method: text`,
  `pages: null` in `text/manifest.json`. There is no PDF or page image to compare against, so
  page counts and visual table checks are not applicable; redactions and lost table alignment
  are noted per document as they appear in the text.
- Reuse binding (sha256 from `text/manifest.json`, read 2026-10-11):
  - D01 c9bb6cb16574c68a8a24ec23b4848c280747d158fe50ab112a8ee382ef1ba0e2
  - D02 8c4c0804e356ddd2f4280449e308d7595fa1128753de1702bd4dc56779e2415a
  - D03 008de5e2352ab0190d3b52d48b2c7fd175c55e2a0e8b048342697b47447b50a6
  - D04 8dc0dab93c4e80c7defe7e8f203fec2c34f06ca9b9fe4f8cac5e6399da72d506
  - D05 7d7ff1ee6f5dcfa8dbd0a716d3a3ce608ac309be2771f2c7fb0db4ea3a884888
  - D07 56054d916ac5da0f57c2d9378748ac9e04a9028a3d2cb0485da6c245c290de2a
  - D08 ad66ecd751505e16c96c57a195258d7356e5ba718ed72b6abea79bfa91c3e317
  - D09 a96111351577b577a666864930daf86b22da80fc686276900479c25449258234
  - D10 483d7f793e23ded1484840c61594b31060f7ef14b525f98564ad93de9cb3cff9
  - D11 12e9c2e899acb681525d96983ee447ddd45633eb247a34d1878b7464fd4cebf1
  - D12 53c9c2e26e86516d2f9a715f287a1a10cb309a1d19359a946ace0b4c64d15ab5
  - D14 104f7cd7b915953b9d123d3371c25913d8e26f85d21c09ecd5837ed50f72d784
  - D15 57cecf07ea83153ee1ba572b319d0108cc6485a1dd20d12a8c8e881449d9b740
  - D16 7794a1b56e230136dfcba215aefb7c7eddee9797e0cc15925d4cd40f9c9dcea3
- Mapping progress ledger: all 14 sections saved (D01, D02, D03, D04, D05, D07, D08, D09, D10,
  D11, D12, D14, D15, D16), each read in full, then Shared ground and the coverage ledger at the
  end of this file. Mapped 2026-10-11.

## D01 (Doc 3) - ANZ submission

- Source: `text/D01.txt`, 67 lines (text capture; no pages).
- Written or submitted by: ANZ Bank New Zealand Limited ("ANZ"), L8, L12. Contact is the
  "General Manager Business Products" (name and address blank/redacted), L15.
- Type, date, edition: submission on the draft decision; dated "16 July 2026" (L9). One edition.
- Period covered: its own data compares 2022 with 2026 (L50); other comparisons are undated
  "previous submission" vs now (L52).
- Entities and aliases: "Commerce Commission's (Commission)" L12; "Draft Decision" = 'Commercial
  Credit Card Interchange Fee Regulation for Mastercard and Visa Networks - Draft Decision and
  Reasons Paper dated 4 June 2026' L12; "Draft Network Standard" = '[Draft] Mastercard and Visa
  Interchange Fee Amendment Network Standard 2026' L12; "Limiting Mechanism" L20; "Business
  Enhancement Release (BER) cycle" L23; "Buy Now Pay Later (BNPL)", "American Express (Amex)" L58;
  "Reserve Bank of Australia Issues Paper dated 25 June 2026 on the Review of Payment System
  Regulation" L62. "schemes" = Mastercard/Visa (used throughout, not formally defined).
- Positions (verbatim, with line):
  - Overall stance, L20: "ANZ supports the Commission's intention to reduce costs to consumers and
    merchants and to promote efficiency, competition and innovation within the retail payment
    system. However, ANZ considers that the implementation timeframe is too short, and that the
    proposed Limiting Mechanism (Limiting Mechanism) entrenches historic advantages".
  - Cap level / premium: none proposed anywhere in D01 (no figure for a cap or premium is printed).
    L34 refers to "the proposed caps" only conditionally ("If the proposed caps are at the
    appropriate level...").
  - Implementation, L23: "The 2- to 3-month implementation period from the date of the
    Commission's final decision is not long enough to safely and accurately implement the changes.
    This period is shorter than the 4-month implementation period for the changes to consumer
    rates which, as noted in ANZ's submission in relation to those changes, was also too short."
    L23 also: "Significant parts of the implementation need to be completed before customer
    notice, reducing the implementation period by an additional 30 days."
  - Implementation request, L29: "ANZ suggests that all changes be tied to the structured update
    schedule used by the schemes, namely the BER cycle, specifically the April 2027 release.
    Failing that we consider that the implementation period should be a minimum of 6 months."
  - Limiting Mechanism, L42-44: "ANZ recommends removing the Limiting Mechanism. Alternatively,
    ... the Limiting Mechanism could be retained as a targeted deterrent ... rather than being
    applied at the outset." Reasons at L32-40 (creates "a floor based on historical pricing" L34;
    "advantages that existed at an arbitrary date" L36).
  - Surcharging, L48: "Regulation of surcharging, including its prohibition, is essential ... ANZ
    does not set, require or support surcharging."
  - Scope across providers, L58: regulation "should be applied to all payment providers who charge
    interchange, or similar fees, in excess of the proposed caps in the Draft Decision or the
    current network standard"; names BNPL, Amex and "any future market entrants" as exclusions it
    objects to.
  - Drafting, L65: if the Limiting Mechanism stays, the Draft Network Standard "should be clear
    that the applicable interchange fee is the interchange fee set by the schemes in New Zealand
    and not any further reduction provided by a given participant."
- Quantitative statements (all New Zealand, ANZ's own data unless noted):
  - L23: "2- to 3-month implementation period" (attributed to the Commission's proposal); "4-month
    implementation period for the changes to consumer rates" (earlier consumer change; no date
    given); "an additional 30 days" (customer notice).
  - L29: "April 2027 release" (BER cycle); "minimum of 6 months".
  - L50: "Based on a subset of ANZ merchants using terminals on the network, surcharging has
    increased from 8% in 2022 to 26% in 2026." Base: a subset of ANZ merchants on terminals; the
    network is not named in the text ("on the network"; L18 says certain aspects of the
    submission are withheld). Unit: % (of merchants, as worded).
  - L52: "Based on network data, the average merchant service fee has reduced by 44 basis points
    from 1.35% (disclosed in previous submission) to 0.91%." Network not named. No years printed
    for either figure.
  - L52: "The average surcharge has reduced by 22 basis points from 2.24% to 2.02% but is still
    more than double the average merchant service fee."
  - L52: "The number of terminals that surcharge at a level above the merchant service fee has
    increased from 91% of terminals to approximately 94% of terminals." Base: terminals (not
    merchants); "approximately" attaches to 94%.
  - No card-type split (commercial vs consumer, credit vs debit) is stated for L50-L52 figures.
- Restates / disputes the draft decision: the "2- to 3-month implementation period from the date
  of the Commission's final decision" L23; "The Commission notes that parties have had extensive
  notice that changes were possible" L25 (disputed: notice "does not enable implementation work
  to be started any earlier"); the Limiting Mechanism "similar to the mechanism in place
  previously" L32 and applying "at a category-specific level" L36; "The Commission has identified
  caps intended to reflect an efficient interchange rate for each category" L34. Draft Decision
  date "4 June 2026" L12. No draft-decision cap figures, savings figures or paragraph/question
  numbers are quoted.
- Events and dates: draft decision dated 4 June 2026 (L12); submission 16 July 2026 (L9);
  "Australia is intending to empower schemes to reintroduce rules preventing card surcharging
  from October 2026" (L48); RBA Issues Paper dated 25 June 2026 (L62); April 2027 BER release
  (L29); surcharging data points 2022 and 2026 (L50).
- Hedged claims:
  - L20 "surcharging practices and uneven regulation across payment providers may undermine the
    Commission's intended outcomes" - "may" attaches to the undermining.
  - L38 "A mechanism that effectively permits movement in only one direction is unlikely to
    support efficient market outcomes" - "unlikely" attaches to the outcome claim.
  - L48 "There is no evidence that reductions in interchange and merchant service fees resulted
    in a reduction in surcharging or prices." - stated firmly (no hedge).
  - L48 "Australia is intending to empower schemes ..." - "is intending" (an intention, not an
    action taken).
  - L53 "These outcomes suggest that reductions in payment acceptance costs are not consistently
    being passed through" - "suggest".
  - L58-60 excluding BNPL/Amex "will likely distort outcomes and may undermine the Commission's
    aims. Over time, this selective regulation is likely to shift activity" - "likely"/"may".
- Rounded prose beside exact figures: L52 "more than double" beside 2.02% vs 0.91%;
  "approximately 94%".
- Notes: redactions show as blanks at L15 (name/contact); the "network" at L50 and L52 is not
  named.
- Coverage: FULL. Lines 1-67 read sequentially (2026-10-11). Nothing unread.

## D02 (Doc 4) - ASB submission

- Source: `text/D02.txt`, 141 lines. Stray page numbers at L29, L57, L59, L83, L100/L139 etc.
- Written or submitted by: ASB Bank Limited (L4), signed by "GM Global Transaction Banking"
  (name blank, L55). Organisations it only names: Reserve Bank of Australia (RBA), RBNZ, American
  Express, Airwallex, Mastercard, Visa, Australian Bureau of Statistics, MWE.
- Type, date, edition: cover letter (L3-56) plus Appendix answering the Commission's "targeted
  questions" (L60-137). Date printed "[20 July] 2026" with the day/month in square brackets (L3).
- Period covered: Australia July 2017 to now; New Zealand 2022 / November 2022 to now; fraud
  figure "12-months to May 2026" (value redacted).
- Entities and aliases: "Commerce Commission (Commission)", "Draft Decision or 'these proposals'"
  L17; "Reserve Bank of Australia" L25 = "RBA" L79, L88; "Card Present and Card Not Present" L110;
  "Strategic Merchant" and "Industry Program" interchange rates L110; "initial pricing standard"
  (New Zealand, 2022 / November 2022) L98, L108.
- Positions (verbatim, with line):
  - Stance on caps: "ASB welcomes an interchange premium above the consumer credit card caps and
    agrees with the intention underpinning their inclusion. However, we challenge the size of the
    premium" L104. It does not say it opposes caps; it says the caps "will reduce competition and
    limit cardholder access to credit" (concern, L106).
  - Cap level, L22: "ASB Recommendation 1: An interchange cap of 1.1% for all market participants
    is simple for merchants and acquirers to understand, sustains some degree of domestic issuer
    value and still delivers a top line saving for New Zealand merchants." Repeated L110 as "A
    level of approximately 1.1% for all market participants".
  - Single flat cap / no tiering, L20: "ASB does not believe there should be a distinct or higher
    interchange cap for foreign issued cards or card-notpresent cards." L110: "a single flat
    interchange cap across all issuer locations (domestic and foreign) and card usage
    environments (Card Present and Card Not Present)".
  - Premium, L32: "ASB Recommendation 2: ASB asks the Commerce Commission to consider whether 50
    bps over the existing interchange caps for personal credit cards is at least the starting
    point for commercial credit card cap consideration."
  - Implementation, L37: "Two to three months istherefore insufficient to make the required
    system changes"; L125 "materially insufficient".
  - Implementation request, L48: "ASB Recommendation 3: Set an implementation date of no earlier
    than 8 months from the announcement date and Commission to direct the schemes to confirm
    applicable rates and criteria no later than 2 months from announcement date to allow
    acquirers 6 months for implementation." Repeated L137 ("Our preference would be ...").
  - Limiting mechanism question (targeted question 6), L124: "We suggest Visa and Mastercard are
    best placed to answer this question".
- Quantitative statements:
  - L22, L110: cap "1.1%" / "approximately 1.1%" (ASB proposal; NZ; commercial credit; all issuer
    locations and CP/CNP).
  - L24 (heading): "A 20bps higher interchange cap on commercial credit (compared to personal
    credit)" - attributed to the Commission's proposal; L30 "The Draft Decision's proposed 20-bps
    premium"; L88 "The Commerce Commission's 20-bps premium".
  - L104 (quoting the Commission's targeted question 3.1): "the additional 10 basis-point premium
    we have applied above domestic personal credit card interchange to reflect the incremental
    issuer costs and merchant benefits associated with domestic commercial credit cards". NOTE:
    same document prints the Commission's premium as "20bps"/"20-bps" (L24, L30, L88) and as
    "additional 10 basis-point" (L104, the Commission's own question wording). Both recorded;
    D13 is the source to check.
  - L25, L88: "the 50-bps interchange premium for commercial credit cards (versus consumer) that
    was codified by the Reserve Bank of Australia's latest regulations" (Australia). Footnote 1
    (L26-27): "Reserve Bank of Australia Review of Merchant Card Payment Costs and Surcharging
    Conclusions Paper 31 March 2026".
  - L32: "50 bps over the existing interchange caps for personal credit cards" (ASB ask, NZ).
  - L35: "For the domestic rate changes announced in July 2025, the details of the changes being
    made by the schemes was [blank] allowing us 3 months to complete implementation work." (NZ)
  - L37, L124-125: "Two to three months" / "two to three-month implementation period" (the
    Commission's proposal).
  - L48, L137: "8 months", "2 months", "6 months".
  - L62 (Australia; source footnote 2 = "RBA's 'Review of Merchant Card Payment Costs and
    Surcharging - consultation paper'", L79): "the imposition of the initial 80 bps cap in July
    2017. Since that time, commercial credit cards on issue in Australia has dropped 41.8%, the
    prevalence of charge cards increased and American Express now commands a ~50% commercial card
    market share, up from 18.2% in July 2017".
  - L68-71 table "Commercial Credit Cards | ASB | Australia Market" (source footnote 3, L79,
    printed "RBZ Payment data"): Annual Spend AUD$166,428; Average Balance AUD$12,495; Interest
    Bearing Balance AUD$2,951. Only ONE value per row survives; the ASB column is blank
    (redacted). The surviving values sit under "Australia Market" by position, and are in AUD.
    No period is printed for the table.
  - L73: "An 80-bps interchange cap in Australia ... Australian commercial credit cardholders
    carry 184% higher interestbearing balances, spend 271% more and on average pay higher fees."
    (Australia vs ASB/NZ; relative %.)
  - L76: "[blank] of balances are currently incurring interest (revolving) within ASB's
    commercial card portfolio. At the national level, that figure is 51.8% for consumer credit
    cards" (NZ; consumer credit cards; footnote 4 "RBNZ data", L80-81). ASB commercial figure
    redacted.
  - L77: "The Reserve Bank of Australia has had two, soon to be three, regulatory interventions
    in the market, with the 2017 change likely most relevant for commercial credit cards, as it
    introduced an 80-bps cap."
  - L90 (Australia; footnote 5, L101: "Reserve Bank of Australia 'Payments Data' and The
    Australian Bureau of Statistics"): "total number of credit cards (consumer and commercial) on
    issue in Australia, which has fallen by 27.1% since 2017, whilst the population has grown by
    16%".
  - L94: "Australia's GDP is 7x that of New Zealand's ... The population base is 5x higher".
  - L96: "even with an 80-bps cap on interchange" (Australia, commercial).
  - L98 (NZ; footnote 6, L102: "MWE New Zealand Payment Cards Report"): "American Express has
    doubled their market share in New Zealand since the implementation of the initial pricing
    standard in November 2022".
  - L108 (NZ; no source cited): "since the initial pricing standard was introduced in New Zealand
    in 2022. Since this time, commercial credit card balances have grown 4%. Over the same period
    consumer credit cards grew only 0.7%."
  - L110: ASB's share of commercial vs consumer transactions that are Card Not Present, and the
    share at preferential rates - all values blank (redacted).
  - L114: "In the 12-months to May 2026, ASB recorded fraud rate [blank] rather than the 1 - 2
    bps quoted in the consultation paper." ASB value redacted; "1 - 2 bps" attributed to the
    Commission's paper (printed with a long dash: "1 — 2 bps").
- Restates / disputes the draft decision:
  - Targeted questions quoted or named: 2.1 (L60), 2.2 (L77), 2.3 (L93), 3.1 (L104), 3.2 (L112),
    4.1 and 4.2 (L119), 6 (L122), 8 & 9 (L124). Question 6 text L122: "We propose that the
    limiting mechanism apply to domestic commercial credit transactions only, on the basis that
    foreign-issued transactions do not appear to have preferential interchange categories."
    Question 8 & 9 text L124: "whether a proposed two to three-month implementation period would
    be sufficient ... Implementing interchange fee changes following the Commission's July 2025
    decision, including repricing activity."
  - Premium: "20bps"/"20-bps" (L24, L30, L88) and "additional 10 basis-point premium" (L104).
  - Fraud: "the 1 - 2 bps quoted in the consultation paper" L114.
  - Dispute: "The Commerce Commission has been heavily informed by Australia's approach ...
    without fully acknowledging the key structural differences between the two markets" L62.
- Events and dates: Australia "initial regulation in 2003" (companion cards) L84; Australia
  "initial 80 bps cap in July 2017" L62 (both called "initial"; 2003 = first RBA regulation, July
  2017 = first 80 bps commercial cap, as worded); Australia "October 2026 caps on consumer credit
  cards go live" L86; RBA Conclusions Paper 31 March 2026 L26-27; NZ "domestic rate changes
  announced in July 2025" L35 / "the Commission's July 2025 decision" L124; NZ "initial pricing
  standard in November 2022" L98 / "in 2022" L108; fraud window "12-months to May 2026" L114.
- Hedged claims:
  - L24/L30 "would suggest that New Zealand's smaller market ... needs less competition" -
    "suggest(s)" attaches to ASB's inference about the Commission's view.
  - L77 "the 2017 change likely most relevant" - "likely" attaches to relevance, not to the cap.
  - L86 "even greater divergence ... can be expected once the October 2026 caps ... go live" -
    expectation.
  - L106 "There is a risk that issuers reassess their market participation" - "risk".
  - L120 "The proposed commercial credit card caps may prompt issuers to consider revenue levers
    ... and may impact issuers' future commercial credit card investment" - "may" on both effects.
  - L62 "American Express now commands a ~50% commercial card market share" - "~" approximates.
- Rounded prose beside exact figures: "~50%" vs exact "18.2%", "41.8%" L62; "approximately 1.1%"
  L110 vs "1.1%" L22; "7x", "5x" L94.
- Tables: one, L68-71 (see above). Column alignment lost: header row has three labels, each data
  row has a label and one value.
- Extraction oddities: L3 "[20 July] 2026"; L15 email "RetailPaymentSvstem@"; L25 "regulationsl"
  (footnote marker 1 fused), L26 footnote starts with a stray apostrophe; L62 "July 20172"
  (footnote marker 2 fused to the year); L98 "November 20226" (footnote 6 fused); L90 "16%5"
  (footnote 5 fused); L79 "RBZ Payment data" (as printed); redactions leave gaps at L35, L41,
  L43, L52, L76, L110, L114, L118, L130, L132.
- Coverage: FULL. Lines 1-141 read sequentially. Nothing unread. Redacted values are missing
  source text, not unread text.

## D03 (Doc 5) - BNZ submission

- Source: `text/D03.txt`, 72 lines.
- Written or submitted by: Bank of New Zealand ("BNZ"), Regulatory Affairs (L4, L13); signed Paul
  Hay, "Chief Regulatory and Compliance Officer" (L69-70).
- Type, date, edition: letter submission, "17 July 2026" (L6). Numbered paragraphs 1.1-5.2.
- Entities and aliases: "Commerce Commission"/"the Commission"; "draft Amendment Network Standard"
  L43; "Retail Payment System Act 2022" L62; "'interchange plus' and alternative pricing options"
  L37.
- Positions (verbatim, with line):
  - Stance on caps, L18 (para 1.2): "BNZ is broadly supportive of the introduction of caps on
    commercial cards, although in our view, the currently proposed level is too low and is not
    reflective of the specific characteristics of commercial cards." L62 (5.1): "We are broadly
    supportive of appropriate commercial credit card interchange caps".
  - Cap level / premium: no figure proposed. L47 (4.2): "BNZ is concerned that the proposed caps
    are so low that they may affect issuer incentives".
  - Implementation, L23 (1.3.2): "we recommend a minimum six-month implementation period between
    the final decision and commencement". L37 (3.3): "BNZ strongly recommends a period of at
    least six months from the final decision date before the new settings take effect."
  - Timing exclusion, L39 (3.4): "We also urge the Commission to avoid a pre-Christmas
    deployment".
  - Other networks, L22 (1.3.1) and L30 (2.3): "set out a clear approach to monitoring and,
    designate other payment systems and issue a comparable network standard where there is
    evidence of substitution, rising merchant costs, or increased acceptance pressure."
  - Drafting, L41-43 (3.5): "the commencement date in clause 2 of the network standard should be
    amended to identify when the commercial credit card caps come into effect. The present
    drafting of the draft Amendment Network Standard does not include placeholder drafting to
    insert a date".
  - Asks the final decision to address six listed consequences, L50-59 (4.3.1-4.3.6).
- Quantitative statements: only durations/dates. L23 "minimum six-month"; L37 "around a
  six-month process from the point rates are published through to implementation" (BNZ's own
  alternative-pricing remodelling; NZ); L37 "this may be the third recent repricing for some
  merchants, following repricing in December 2025 and May 2026"; L37 "at least six months". No
  percentages, basis points or dollar figures anywhere in D03.
- Restates the draft decision: L27 (2.1) "the draft decision recognises the risk that commercial
  cardholders may switch to alternative payment networks, to retain rewards and other benefits";
  L33 (3.1) "The proposal for commercial credit cards, if set at a sustainable level, together
  with aligning pre-paid card interchange settings, would substantially complete the remaining
  part of the interchange framework for those schemes"; L45 (4.1) "the Commission is seeking to
  reduce merchant service fees". No cap figures, savings or question numbers quoted.
- Lists: three focus points L22-24 (1.3.1-1.3.3); six consequences L50-59 (4.3.1-4.3.6; last item
  is small businesses, L59).
- Events and dates: submission 17 July 2026 (L6); repricings "December 2025 and May 2026" (L37).
- Hedged claims:
  - L29 "there is a clear risk that spend continues the shift towards less regulated or
    higher-cost payment systems. We believe that outcome may not necessarily reduce merchant
    costs overall, but instead may simply move, and even increase, costs" - "risk", "may".
  - L37 "this may be the third recent repricing for some merchants" - "may" attaches to the
    count being the third, scoped to "some merchants".
  - L47 "may affect issuer incentives" - "may".
  - L50-59 each item is framed "Whether ..." (questions for the Commission, not assertions).
- Coverage: FULL. Lines 1-72 read sequentially. Nothing unread.

## D04 (Doc 6) - Citibank N.A. New Zealand submission

- Source: `text/D04.txt`, 161 lines. "Page 2".."Page 7" markers at L15, L47, L77, L100, L122,
  L157 (the source ran to 7 pages; no page 1 marker; cover block L3-13).
- Written or submitted by: Citibank, N.A. New Zealand ("Citi"), L8, L17. No signatory printed.
  Organisations it only names: Commerce Commission, Reserve Bank of Australia, World Bank,
  Korefusion/KoreFusion (research "commissioned by Visa"), Visa, American Express.
- Type, date, edition: submission, "17th July 2026" (L13).
- Entities and aliases: "Citibank NA - New Zealand ("Citi")" L17; "Draft Decision" L17;
  "Commercial Card(s)" (capitalised product term; described as "typically structured as charge
  card products ... balances are settled in full each billing cycle" L23); "Enterprise Resource
  Planning ("ERP")" L35; "three-party payment network(s)" L106-112; "SMEs" L62.
- Positions (verbatim, with line):
  - Stance, L44: "We support the Commission's objective of improving outcomes in the payments
    ecosystem. However, we are concerned that the Draft Decision, in its current form, may lead
    to unintended consequences".
  - Caps, L136 (Recommendation 1): "Continue to exclude Commercial Card interchange from
    regulatory cap, or if the Commerce Commission decides to proceed with implementing a cap then
    implement a materially higher Commercial Card interchange differential than that proposed in
    the Draft Decision". No numeric cap or premium is proposed by Citi.
  - Premium, L54: "Proposal of a 20 basis point premium to consumer interchange is insufficient";
    L86: "Citi does not view the 10 basis point premium as sufficient"; L90: "We do not consider
    the proposed 10 basis points premium to domestic personal credit card interchange to be
    sufficient for Commercial Cards".
  - Complementary measures, L138: "Introduce complementary measures addressing acquiring
    transparency and surcharging before implementing interchange reductions"; L82 "Any regulation
    of Commercial Card interchange fees, should be accompanied by regulatory intervention with
    regards to acquiring and surcharging fees."
  - In-person/online tiering, L140: "Reconsider the proposed differentiation between in person
    and online Commercial Card interchange rates"; L104 discussion.
  - Implementation, L129: "A two-to-three month implementation period would not be achievable for
    many issuers and corporate clients." L133: "Citi recommends a minimum implementation period of
    twelve months, mapped to four major quarterly technology releases if the Draft Decision is
    implemented." L142: "Allow a minimum of 12 months implementation period".
- Quantitative statements:
  - L45 (attributed to "World Bank data"; no year): "New Zealand's population is approximately
    5.3 million compared to approximately 27.2 million in Australia, while New Zealand's GDP is
    approximately USD 260 billion compared to approximately USD 1.76 trillion in Australia."
  - L54: "20 basis point premium to consumer interchange" (the Draft Decision's proposal, as Citi
    words it in the Executive Summary).
  - L84, L86, L90: "additional 10 basis point premium above domestic personal credit card
    interchange" / "10 basis point premium" / "10 basis points premium to domestic personal
    credit card interchange" (the Commission's step 3). NOTE: D04 prints both "20 basis point"
    (L54) and "10 basis point" (L84-90) for the Commission's premium; recorded neutrally.
  - L62-63 (Asia Pacific suppliers; footnote 1, L75: Korefusion "From Transaction to
    Transformation Quantifying the Value of B2B Card Acceptance to Large Asia Pacific Suppliers"
    June 2025 P13 commissioned by Visa): "Merchants can significantly reduce bad debts, by 106
    basis points on average, thanks to a guarantee provided by card acceptance."
  - L96: "merchants typically receive payment within one to two days of transaction settlement";
    "KoreFusion research paper estimates the potential benefit at approximately 15 days of
    accelerated payment" (footnote 2, L98: same paper, "P17", title printed with "Supplier"
    singular).
  - L104: "This differentiation, coupled with the limiting mechanism, could be significantly
    lower that then assumed 78bps implied weighted average in New Zealand." (78bps attributed to
    the Commission's assumption; NZ; commercial credit.)
  - L127-133, L142: "two-to-three month"; "twelve months"; "four major quarterly technology
    releases"; "12 months".
- Restates / disputes the draft decision: question numbers answered - Question 2 (steps 1 and 2)
  L70; Question 3 (step 3) L88; Question 4 (competition) L105; Question 9 (implementation) L127.
  L74 "the Commerce Commission has used the Australian interchange fee as a benchmark for New
  Zealand interchange"; L81 "Unlike Australia, New Zealand does not include regulation of
  surcharging or acquiring practices"; L104 "implementing two distinct interchange rates for
  in-person and online is a meaningful variation to the Reserve Bank of Australia's approach";
  premium 20 bp (L54) / 10 bp (L84-90); "assumed 78bps implied weighted average" L104; "proposed
  two-to-three month implementation period" L127.
- Lists: product characteristics, 3 bullets L25-29; value, 4 bullets L33-39; Draft Decision
  criticisms, 7 bullets L52-65; step-3 reasons, 4 bullets L92-102 (the 4th is after the Page 5
  break, L102); three-party advantage, 3 bullets L108-112; issuer participation, 2 bullets
  L116-118; "Summary of Citi's Recommendations" 4 bullets L136-142 (the 4th runs into the word
  "Conclusion" on L142); Conclusion "it may:" 6 bullets L145-155.
- Events and dates: submission 17th July 2026 (L13); Korefusion paper "June 2025" (L75, L98).
- Hedged claims:
  - L44 "may lead to unintended consequences"; L58, L60, L62 bullets begin "May ..." (the Draft
    Decision "May alter competitive dynamics", "May diminish the commercial viability", "May
    disproportionately affect SMEs"); the first three bullets (L52-56) are stated firmly ("Does
    not fully reflect", "is insufficient", "Does not include").
  - L67 "may risk creating a less competitive ... ecosystem and may place New Zealand corporates
    at a relative disadvantage".
  - L79 "risks overstating the ability of the New Zealand market to absorb similar reductions".
  - L82 "The result may simply be a redistribution of revenue".
  - L86 "the premium may be insufficient to attract issuers" (but the first sentence of L86 is
    firm: "does not view the 10 basis point premium as sufficient").
  - L104 "could be significantly lower" - "could" attaches to the realised weighted average.
  - L108 firm: three-party networks "will gain a relative competitive advantage"; L110 "While
    American Express may currently represent a relatively small share ... its position within
    commercial payments is growing. The Draft Decision will create an uneven playing field." -
    "may" sits in the concession clause about current share; the uneven-playing-field claim is
    firm.
  - L116 "Existing issuers may scale back their offerings or potentially exit the market";
    L118 "may result in the only issuers remaining"; L120 "could be constrained".
  - L143 Conclusion list is governed by "it may:".
- Rounded prose beside exact figures: all L45 figures are "approximately".
- Coverage: FULL. Lines 1-161 read sequentially. Nothing unread.

## D05 (Doc 7) - Financial Services Federation submission

- Source: `text/D05.txt`, 101 lines. Letter L3-16; Appendix A (member list) L19-65; Appendix B
  (infographic "THE SPECIALIST LENDING SECTOR - 2025") L68-99.
- Written or submitted by: Financial Services Federation ("the FSF"), signed Katie Rawlinson,
  "Legal and Policy Manager" (L14-16). Appendix A names its members (organisations it lists, not
  authors), including "American Express" (L35), "AfterPay NZ Finance Ltd" (L34), "Latitude
  Financial" (L62), "Zip Co NZ Finance Limited" and "Humm Group" (L56).
- Type, date, edition: letter, "13 July 2026" (L3). It calls the Commission's paper "the
  Consultation document on the Commercial Credit Interchange discussion paper (the
  Consultation)" (L6), not "Draft Decision".
- Period covered: Appendix A "as at May 2026" (L20); Appendix B "2025", data "as at 31 Mar 2025".
- Positions (verbatim, with line):
  - L10: "we are accepting of the direction that interchange fees are heading in due to the fact
    this has been signalled. Despite this we are concerned at the impact this will have on
    competition as we have previously highlighted in our submissions."
  - L10: "one of our members went a long way towards developing a commercial credit card
    offering but pulled out due to the signalled interchange changes." (member not named.)
  - L11: "This is a direct negative impact on competition from the work the Commission is doing.
    We believe more thought should be put into the unintended consequences on competition".
  - No cap level, premium, tiering, exemption or implementation period is proposed in D05.
- Quantitative statements (New Zealand; FSF's own data; none are card or interchange figures):
  - L8: "We have around 100 members (a list of which is attached as Appendix A)".
  - L9: "more than 1.5 million New Zealand consumers and businesses".
  - L65: "Total 101 members" (Appendix A, list "as at May 2026" L20).
  - L99: "FSF Members (as at 31 Mar 2025) Number of Members 100". (Three member counts: "around
    100" L8; "Total 101 members" L65 as at May 2026; "100" L99 as at 31 Mar 2025.)
  - L71-74 infographic header (alignment lost): "57% Percent of Loan Requests Approved" / "50%
    NON-BANK J._ BANK" / "of personal consumer loans are financed by the specialist lending
    sector represented by FSF members Percent of Loan Book in Arrears ..." / "2016 5.8% 4, 2022
    3.7% 2025 5.9%". Which of 57% / 50% belongs to "Percent of Loan Requests Approved" and which
    to "of personal consumer loans are financed by the specialist lending sector" cannot be
    settled from this text line order; related exact figures at L99 are "Applications Processed
    1,187,492", "Loan Requests Approved 588,671" and "% of Total Consumer Loans 57.2%".
    Arrears series L74: 2016 5.8%; 2022 3.7%; 2025 5.9% (L99 repeats "Percent of Loan Book in
    Arrears 5.9%").
  - L77-84 "Consumer Loans (as at 31 Mar 2025)": labels are printed first (L78-83), then the
    values in one run on L84, so pairing is by order only: Total Value of Loans "$12 0B" (as
    printed, decimal point lost); Number of Customers 1,383,344; Number of Loans 1,488,692;
    Average Loan Size $8,070; Total Value of Loans by type - Mortgage $1,839M, Vehicle Loan
    $4,850M, Unsecured $4,772M, Other Security $541M, Lease Finance $11M; Average Value of Loan -
    Mortgage $293,661, Vehicle Loan $15,719, Unsecured $4,280, Other Security $9,244, Lease
    Finance $38,981.
  - L84-97 "Business Loans (as at 31 Mar 2025)": Total Value of Loans "$10.26" (as printed; unit
    letter lost); Number of Customers 137,075; Number of Loans 226,820; Average Loan Size
    $45,146; by type (L91) Mortgage $3,033M, Vehicle Loan $3,033M (same figure printed twice),
    Unsecured $441M, Other Security $1,960M, Lease Finance $1,773M; Average Value of Loan
    (L93-97) Mortgage $824,431, Vehicle Loan $35,177, Unsecured $29,182, Other Security $42,184,
    Lease Finance $23,532.
  - L99 "KEY FACTS": FSF Members (as at 31 Mar 2025) - Number of Members 100; Number of Employees
    3,162; Total Value of Loans $22.25B; Applications Processed 1,187,492; Loan Requests Approved
    588,671; Percent of Loan Book in Arrears 5.9%; Loan Disputes Upheld TBC. Bank Sector (as at
    31 Mar 2025) - Value of Mortgage Loans $369B; Value of Consumer Loans $7.6B; Value of
    Business Loans "$1276" (as printed; unit lost). Specialist Lending Sector Share (mar 2025) -
    "0/0 of Total Mortgage Loans 0.5%"; % of Total Consumer Loans 57.2%; % of Total Business
    Loans 7.4%. Insurance Credit Related (as at 31 Mar 2025) - Number of Employees 174; Number of
    Policies 285,371; Gross Claims (annual) $13.2M.
- Lists: Appendix A category headings L21-33; member names L34-64 are interleaved across columns
  (names split and merged, some garbled, e.g. L49 "Rdiktalal&ffol Leasing", L55 "Quii1zusla",
  "Ha rmoney"); a reliable member count from the names is not possible from this text - only the
  printed "Total 101 members" (L65) is usable.
- Restates the draft decision: none (no figures, caps, paragraphs or question numbers). Refers
  only to "the direction that interchange fees are heading" and "the signalled interchange
  changes" L10.
- Events and dates: letter 13 July 2026 (L3); membership list as at May 2026 (L20); sector data
  as at 31 Mar 2025 (L77, L84, L99).
- Hedged claims: none of substance; L10-11 are stated firmly ("This is a direct negative impact
  on competition"). L8 "around 100 members" is an approximation.
- Rounded prose beside exact figures: "around 100 members" L8 vs "Total 101 members" L65 and
  "Number of Members 100" L99; 57% (L71) vs 57.2% (L99).
- Tables: Appendix B only (see above). Problems: label/value alignment lost in the consumer-loan
  block; lost characters in "$12 0B", "$10.26", "$1276", "0/0".
- Coverage: FULL. Lines 1-101 read sequentially. Nothing unread. Garbled Appendix A/B text is an
  extraction-quality gap (visual original not available), not unread text.

## D07 (Doc 9) - Kiwibank submission

- Source: `text/D07.txt`, 87 lines. Numbered paragraphs 1-22; page numbers fused into L39 ("2
  insufficient"), L61 ("3 the likelihood"), L77.
- Written or submitted by: Kiwibank (L14). "Public Version" (L10). No signatory printed.
- Type, date, edition: submission, "Date: 17 July 2026" (L9).
- Entities and aliases: "Commerce Commission (Commission)", "Draft Decisions and Reasons Paper
  ... (Draft Decision)" L14; "CCC Interchange Caps" = "the proposed interchange fee caps for
  domestic commercial credit cards" L15; "strategic merchant pricing/rates" L48-54; "limiting
  mechanism" L52; "Market Study Report" = "the final report for its market study into personal
  banking services" L75; "initial pricing standard in 2022" L29; a "large terminal provider"
  whose name is blank L27.
- Positions (verbatim, with line):
  - Opposes proceeding now, L16 / L25: "The Commission should not proceed with further
    interchange regulation until it can demonstrate clear and evidenced benefits for customers."
  - Cap level, L18 / L37: "The proposed CCC Interchange Caps are too low." No alternative figure
    proposed.
  - Premium, L67: "A 0.20% premium is insufficient to reflect long run average net credit and
    fraud losses."
  - Smaller banks, L20: "The Draft Decision will disproportionately impact smaller banks."
  - Implementation, L84 (para 21): "The implementation period for any CCC Interchange Caps should
    be at least six months from the final decision. A two to three month implementation period
    is not sufficient." Also L84: "A six month implementation period would align with the
    implementation period for the decisions in relation to domestic personal cards, with some
    additional time to recognise that some implementation activities cannot occur over December
    and January."
  - Benchmarks, L42-43 (para 7): "The Commission should more fully consider the position in the
    UK and EU before deciding whether to adopt the CCC Interchange Caps."
  - Losses data, L70 (para 16): "The Commission should consider average net fraud and credit
    losses over a longer period".
  - Market study, L75 (para 18): "The Commission should reconsider its Draft Decision in light of
    its findings in the final report for its market study into personal banking services".
- Quantitative statements:
  - L52 (para 9; NZ; domestic commercial credit): "For example, Government interchange fees are
    0.20%."
  - L54 (para 10): "Kiwibank estimates that its implied weighted average domestic commercial
    credit card interchange fee would be approximately 0.63% - far lower than the Commission's
    estimate of 0.78%." (0.63% = Kiwibank's own estimate for itself, with strategic merchant
    rates; 0.78% = attributed to the Commission.)
  - L67 (para 15): "A 0.20% premium" (the Commission's step 3 premium as Kiwibank states it).
  - L68: "the Commission requested average net fraud and credit losses for a 12-month period
    from issuers"; the example after "For example, for commercial cards:" is blank (redacted).
  - L84: "at least six months"; "two to three month"; "six month".
  - Surcharging statements L27-32 are qualitative only (no numbers): attributed to "Data provided
    by [blank], a large terminal provider".
- Restates / disputes the draft decision:
  - "The Commission's three step analysis" L37; steps headed L41 (Step 1 benchmarks), L45 (Step 2
    New Zealand context), L66 (Step 3 issuer costs and merchant benefits).
  - L42-43: "The Commission acknowledges that commercial credit card interchange fees remain
    unregulated in the EU and UK. However, the Commission has excluded the UK and EU as benchmark
    jurisdictions".
  - L52: "The Commission is intending to implement a limiting mechanism to prevent these
    strategic merchant rates from being raised."
  - L54: "the Commission's estimate of 0.78%" (implied weighted average domestic commercial
    credit card interchange fee).
  - L63 (para 13): "At paragraph 2.37 of the Draft Decision, the Commission states that in
    jurisdictions with many small businesses that also act as merchants, transparency and
    surcharging are less effective at constraining commercial credit card pricing than in
    jurisdictions where commercial credit card usage is more concentrated among larger or
    medium-sized merchants with greater bargaining power. We note that the Commission's only
    benchmark jurisdiction is Australia, which has a similar proportion of firms classified as
    SMEs."
  - L65 (para 14): the Commission "believes that, although American Express has grown its market
    share in Australia under current interchange caps, its Draft Decision is unlikely to cause a
    similar shift in New Zealand" (Kiwibank's restatement; "It is unclear why").
  - L67: "0.20% premium". L75: "The Draft Decision considers the ability of small issuers to
    enter and compete in commercial credit card markets, but does not consider potential impacts
    on banking competition more broadly."
  - L80: quoted phrase "enhance allocative, productive and dynamic efficiency".
  - L85 (para 22) direct quotation: "this advance notice of our proposed implementation timing,
    alongside our previous intent to regulate commercial credit cards in the July 2025 decision
    paper, strikes an appropriate balance."
- Lists: key points (a)-(d) L16-22; surcharging observations (a)-(c) L29-32; Draft Decision
  omissions (a)-(b) L48-49.
- Events and dates: submission 17 July 2026 (L9); "initial pricing standard in 2022" (L29);
  "further reduction of interchange fees in late 2025" (L29); "decision to reduce interchange
  fees in 2025" (L34); terminals with surcharging enabled "reached a record high in May 2026"
  (L32); "July 2025 decision paper" (L85, inside the quotation).
- Hedged claims:
  - L25 "there is no evidence that existing interchange caps have translated into improved
    outcomes for customers" - firm.
  - L34 "Lower interchange revenue is likely to result in issuers adjusting pricing and reducing
    rewards, as observed following the decision to reduce interchange fees in 2025" - "likely"
    attaches to the future effect; the 2025 observation is stated as fact.
  - L39 caps "risk under-compensating issuers".
  - L52 "the real-world effects of the proposed caps are likely to be more pronounced than
    anticipated"; L54 "is likely to be far lower than in Australia"; L57 "there are several
    rational reasons they may be higher" / "are likely to result in lower weighted average fees
    than in Australia".
  - L54 "approximately 0.63%" - approximation on Kiwibank's estimate; "0.78%" unhedged.
  - L78 "This disparity is likely to be more pronounced"; L80-81 "are unlikely to "enhance ...
    efficiency". Instead, they may lead to cross subsidisation".
  - L20 "will disproportionately impact smaller banks" - firm.
- Notes: redactions at L27 (provider name) and after L68 (loss example).
- Coverage: FULL. Lines 1-87 read sequentially. Nothing unread.

## D08 (Doc 10) - Mastercard's own submission

- Source: `text/D08.txt`, 254 lines. Themed sections L8-144, then "Question Responses" Q1-Q9
  L146-252. Footnotes 1-18 are interleaved in the body text (several fused to sentences).
- Written or submitted by: Mastercard (L9). No signatory printed. It says it is "supported by an
  independent economic assessment by Keystone Economics" (L13), "The independent Keystone
  Economics report at Appendix A" (L64) - that report is a separate document (D06), not part of
  D08's text. Organisations it only names/cites: Commerce Commission, Keystone Economics, Amex,
  Visa, RBA, Kantar Public, Newsroom, RFI Global, Federal Reserve Bank of Richmond, Mandala
  Partners/Mandala Research, Oxera, BCG, MWE Consulting, European Commission (EC), Copenhagen
  Economics (URL only), Bain & Company, Xinja, 86 400, NAB, Volt, Judo Bank, Commissioner Chapple.
- Type, date, edition: submission, "16 July 2026" (L6).
- Entities and aliases: "the Draft Decision" = Draft Decision and Reasons Paper "dated 4 June
  2026" L9; "July 2025 Final Decision" L14, L28 = footnote 1 "Final Decision and Reasons Paper
  (17 July 2025)" L41; "American Express (Amex)" L17; "merchant service fees (MSF)" L34; "the
  Reserve Bank of Australia's (the RBA)" L82; "European Union (EU)", "United Kingdom (UK)" L13;
  "EC", "IFR" (Interchange Fee Regulation) L93; "2024 Personal Banking Services Market Study"
  L17, L104; "Retail Payment System Act 2022" L109; "Network Standard" clause 8.4 L114;
  "limiting mechanism" L21, L106; "Mastercard Rules Section 8.3 for the Asia Pacific region"
  L123; "four-party"/"three-party networks" L82; "cross-border" = foreign-issued (used for the
  May 2026 changes, L32 vs L234).
- Positions (verbatim, with line):
  - Stance, L14: "there is limited evidence of a market failure in commercial cards that would
    justify the introduction of price regulation on this product." L19: "A further round of
    interchange caps, without first addressing the structural reasons for that outcome, is not
    supported on the record."
  - Recommendation 1, L134: "Defer the Final Decision: pending updated acquirer monitoring data
    capturing the December 2025 and May 2026 changes; an independent New Zealand-specific
    cost-of-acceptance study; and forward-looking modelling of Amex substitution risk."
  - Recommendation 2, L136-138: "Address surcharging and the structural conditions driving
    pass-through: before further interchange compression."
  - Recommendation 3, L140: "Designate American Express as a matter of priority ... The
    Commission should designate Amex under the Retail Payment System Act ... Pending designation,
    any interim differential should match the observed MSF differential between Amex and the
    regulated networks."
  - Recommendation 4, L142: "Remove the limiting mechanism: If the Commission considers it
    necessary to retain a form of it, adopt an alternative weighted-average benchmark approach
    across commercial credit categories rather than a per-category lock". Also L110 "Mastercard's
    position is that the mechanism should be removed."; L223 "should be removed in its entirety".
  - Recommendation 5, L144: "Implement any change iteratively: on minimum nine-month (domestic)
    and twelve-month (cross-border) timelines, aligned with established scheme release cycles,
    with published analysis between successive rounds."
  - Implementation, L123: "A minimum of nine months is required for domestic rate changes and
    twelve months for cross-border changes, from the date of final announcement." Repeated L236,
    L248.
  - Differential, L80 / L172: "If a differential is to be applied at all, it should reflect the
    observed differential between average Amex commercial card MSF and average Visa/Mastercard
    commercial card MSF in the New Zealand market, which on the Commission's own data is in the
    order of 40 basis points". No cap level is proposed by Mastercard.
- Quantitative statements:
  - L16, L62: "a 20-basis point differential" (how the Draft Decision distinguishes commercial
    cards from personal/consumer credit, as Mastercard words it).
  - L17, L76-78: the Draft Decision "proposes a 10-basis point differential as a mitigant"
    (against the caps advantaging Amex). L70 "the-10 basis point adjustment understates merchant
    value"; L72 "the proposed 10bps adjustment"; L80, L172 "The 10 basis point differential";
    L140 "a 10-basis point adjustment"; L192 "The 10-basis point cost-and-benefit differential".
  - L168 (Commission's Q2, last bullet, quoted): "The additional 10 basis-point premium we have
    applied to promote stable and sustainable market outcomes and mitigate the risk of market
    disruption." L186 (Commission's Q3, first bullet, quoted): "The additional 10 basis-point
    premium we have applied above domestic personal credit card interchange to reflect the
    incremental issuer costs and merchant benefits associated with domestic commercial credit
    cards." (Two separately worded 10 basis-point premiums in the Commission's questions; "20-
    basis point differential" at L16/L62.)
  - L32: "The acquirer monitoring data underpinning the analysis runs only to March 2024. It
    pre-dates both the December 2025 domestic interchange reductions on personal cards and the
    May 2026 caps on foreign-issued cards".
  - L41-45 (NZ; merchants; all cards; footnote 3, L55: Newsroom, "Commerce Commission clampdown
    won't stop 'insane' card surcharges" (17 December 2024), citing RFI Global data): "The
    proportion of New Zealand merchants applying surcharges rose from 20 per cent in 2016, to 49
    per cent in 2022 (the year of the first reforms), to 57 per cent in 2024 following further
    reductions." (The sentence is split by footnotes 1-2 at L41-43.)
  - L45 (NZ; attributed to "The Commission's own Kantar Public survey work"): "merchants applying
    surcharges of up to 7.5 per cent, and surcharges on EFTPOS transactions that should not
    incur additional cost."
  - L46 (NZ; Mastercard's own estimate; footnote 4, L57): "Mastercard estimated excessive
    surcharging in New Zealand at more than $90 million annually in our September 2024
    submission." Footnote 4 adds "referenced by the Commission in its December 2024 Draft
    Decision."
  - L49 (United States; debit; Federal Reserve Bank of Richmond survey after the Durbin
    Amendment): "77 per cent of merchants made no change to retail prices, 22 per cent increased
    prices, and only 1 per cent reduced prices."
  - L50 (Australia; Mandala Partners, submitted to the RBA): "as the market share of the four
    major Australian banks in payment service provider services fell from 77 per cent to 64 per
    cent between 2018 and 2024, average merchant service fees fell by 12 per cent over the same
    period." (Two different "77 per cent" figures at L49 and L50.)
  - L66 (several European countries; Oxera 2019; footnote 5, L76): "end-to-end administration
    cost associated with relying on invoicing rather than commercial cards amounted to 4.3 per
    cent of the average transaction value, rising to 5.6 per cent if the costs of non/late
    payment are included." L192 restates as "4.3 to 5.6 per cent of transaction value" (fn 18).
  - L80, L172: Amex vs Visa/Mastercard commercial card MSF differential "in the New Zealand
    market, which on the Commission's own data is in the order of 40 basis points, see figure 2
    below". Figure 2's caption (L82) is "Australian Total Merchant Service Fees (% of
    transaction values acquired) Source: The Cost of Card Payments for Merchants, Reserve Bank
    of Australia (2022)" - the prose says New Zealand / Commission's data, the caption says
    Australian / RBA; recorded as printed, unresolved.
  - L82, L157 (Australia): "The RBA retained the 0.80 per cent cap on commercial credit in March
    2026".
  - L92, L169 (footnotes 10/15: "Mastercard analysis, MWE Consulting data (2026)"): "commercial
    card spend equates to around 4.3 per cent of Australian GDP, compared with approximately 1.9
    per cent of New Zealand GDP"; "under half the Australian level". ("4.3 per cent" also appears
    at L66/L192 for the unrelated Oxera invoicing cost.)
  - L104: "the Government has agreed to all 14 recommendations" (2024 Personal Banking Services
    Market Study; footnote 12, L116: Cabinet Paper CBC-24-SUB0129, December 2024).
  - L109, L112, L218, L228: limiting mechanism reference date "1 December 2025"; Q7 wording
    L218: "capping fees at the lower of the applicable cap or the published rate as at 1
    December 2025".
  - L123, L144, L236, L248: "nine months" (domestic) and "twelve months" (cross-border).
  - L228, L234, L238: "two to threemonth" / "two to three months" / "two-to-three-month" (the
    Commission's proposal).
  - L64: commercial cards used by "multiple authorized employees of an organisation (ranging
    from one to thousands)".
- Restates / disputes the draft decision:
  - L14, L28: "The Commission deferred commercial credit card regulation in its July 2025 Final
    Decision on the basis that the evidence was not sufficient to support intervention."
  - L34: "We understand the Draft Decision anticipates broad alignment with Australian outcomes
    on a weighted-average basis"; "no other jurisdiction has, to date, set commercial credit
    interchange caps at the absolute levels proposed here through formal regulation." L92:
    "Setting New Zealand caps below the Australian floor". L153 "Australia is the only
    jurisdiction that has regulated commercial credit card interchange comparably to the levels
    proposed here."
  - L39: "The Draft Decision records that the average fell modestly after the 2022 reforms but
    increased for some merchants" - footnote 2 (L43): "Draft Decision, page 16."
  - L76-78: "The Commission acknowledges in the Draft Decision that the proposed caps could
    materially advantage Amex in commercial credit" (footnote marker 7; no footnote 7 text is
    printed in D08).
  - L88-89: "The Draft Decision indicates the Commission will monitor Amex's commercial credit
    share and may propose designation if its share grows materially. There is no stated
    threshold and no stated timeline."
  - L109: the mechanism freezes "every category currently below the proposed cap at its 1
    December 2025 rate indefinitely"; L112 "the Draft Decision offers no methodology for the
    date chosen"; L228 "the proposed extension of the net compensation prohibition".
  - L129: "the Commission's own acknowledgement that compliance with a cap does not necessarily
    equate with achievement of the policy objective".
  - L198: "the Draft Decision accepts that fraud and administrative costs are higher for
    commercial card transactions but assesses the differential conservatively."
  - Full wording of the Commission's nine targeted questions is quoted: Q1 L147-151; Q2
    L158-168; Q3 L184-190; Q4 L200-204; Q5 L210; Q6 L214; Q7 L218-222; Q8 L228-232; Q9
    L238-246. L24 says there are "nine targeted consultation questions". Q8 is addressed to
    "card acquirer views", Q9 to "card issuer views ... from an acquiring perspective" (as
    printed, L228, L238). Q5 answer: "Further information has been provided confidentially" L212.
- Lists: four central issues (First-Fourth) L14-19 plus "Two further matters" L21-23; three-step
  pass-through chain L36; Policy Recommendations 1-5 L134-144; Q1-Q9.
- Events and dates: submission 16 July 2026 (L6); Draft Decision 4 June 2026 (L9); Final
  Decision and Reasons Paper 17 July 2025 (L41); "the 2022 round or the July 2025 round of
  regulation" (L37); "December 2025 domestic interchange reductions on personal cards" (L32) =
  "July 2025 domestic changes (effective 1 December 2025)" (L234); "May 2026 caps on
  foreign-issued cards" (L32) / "May 2026 cross-border changes" (L234); acquirer data to March
  2024 (L32); Mastercard's September 2024 submission and the Commission's "December 2024 Draft
  Decision" (L46, L57); "Retail Payment System (Ban on Merchant Surcharges) Amendment Bill
  passed first reading in September 2025 but has not progressed to enactment" (L47); Australia
  "RBA ... 2003 reforms" (L82); RBA Conclusions Paper March 2026 (L82-83, L160); RBA "will
  commence a further review in mid-2026" (L86, L157); Australian Government "passed legislation
  expanding the RBA's powers under the Payment Systems (Regulation) Act 1998" (L86, no date);
  Australia's "2018 licensing reforms"; "Xinja returned its banking licence in December 2020, 86
  400 was acquired by NAB in January 2021, and Volt returned its licence in June 2022" (L102-
  103); Oxera study 2019 (L66); EC study 2020 and Article 17 report "submitted 29 June 2020",
  Press Release IP/20/1217, 29 June 2020 (L175-178); Bain paper December 2022 (L115); meeting
  "with Commissioner Chapple on 8 July" (L120, L225; year not printed).
- Hedged claims:
  - L14 "limited evidence of a market failure" - "limited" (not "no").
  - L59 "This suggests that ... is unlikely to produce the consumer outcome" - "suggests",
    "unlikely".
  - L76 the caps "could materially advantage Amex" (attributed to the Commission) vs L80/L172
    "the competitive advantage the Draft Decision itself acknowledges Amex will gain" ("will").
  - L88 "may not, on its own, be sufficient"; L89 Commission "may propose designation".
  - L92/L169 "is more likely to increase substitution risk than reduce it".
  - L109 "risks exceeding the proper scope of the Commission's mandate" (L21 and L223 state it
    without the hedge: "reaches beyond the Commission's mandate").
  - L126 "creates a real risk of withdrawal of commercial credit products".
  - L208 "may force some to exit issuing and merge with other banks".
  - L80 "in the order of 40 basis points"; L92 "around 4.3 per cent" / "approximately 1.9 per
    cent" - approximations.
  - L82 quoted RBA text "American Express is the largest issuer of commercial cards" vs
    Mastercard's paraphrase L155 "one of the largest issuers of commercial cards in Australia".
- Rounded prose beside exact figures: "more than $90 million annually" L46; "under half the
  Australian level" L92 beside 4.3 / 1.9 per cent; "more than two decades" L82.
- Figures: Figure 1 (L51-53) "Average MSF against market share concentration (Aus)", "Source:
  Mandala Research (2024)" and Figure 2 (L82) are captions only - no chart data in the text.
- Footnote ledger: 1 L41; 2 L43; 3 L55; 4 L57; 5 and 6 L76; 7 marker L76, text absent; 8 L83; 9
  "Ibid" L97-98; 10 L99; 11 L115; 12 L116; 13 L160; 14 marker L157, text absent; 15 L173; 16
  L175-176; 17 L177-180; 18 L206.
- Extraction oddities: footnote text fused mid-sentence at L41 ("the year of the first
  1Commerce Commission ..."), L76, L97, L115; L228 "headline rate.Q8:"; L107 "it would existing
  below-cap rates" (verb missing as printed).
- Coverage: FULL. Lines 1-254 read sequentially. Nothing unread. Charts (Figures 1-2) and
  footnotes 7 and 14 are missing source content, not unread text.

## D09 (Doc 2) - Commerce Commission merchant survey results slide pack

- Source: `text/D09.txt`, 390 lines; 41 numbered slides (slide numbers appear as bare numbers,
  often fused to the start of a data line, e.g. L99 "10 39 15 ...", L138 "14 36% ...", L346 "37
  9% ...", L362 "39 14% ..."). Footer on each slide: "Commercial Credit Card Interchange Fee
  Regulation - Merchant Survey Results (July 2026)".
- Written or submitted by: the Commerce Commission (first person "We conducted a survey" L9; "our
  draft decision" L9, L387). Not a submission.
- Type, date, edition: slide pack "Merchant Survey Results", "Published 23 July 2026" (L4),
  "Survey conducted June 2026" (L7).
- Period covered: "The survey was open for three weeks from 4 June to 29 June 2026" (L22).
- Method and caveats (verbatim, with line):
  - L9: "The survey was conducted anonymously through SurveyMonkey."
  - L15: "The survey results are one of the factors that we will weigh up when making our final
    decision on commercial credit card fee regulation."
  - L24: "In total 94 completed responses were received - where completed refers to respondents
    who reached the end of the survey and clicked 'Submit'."
  - L26: "2 of the respondents identified themselves as responding on behalf of merchants - such
    as a merchant association or industry body."
  - L28: "Participation in the survey was voluntary."
  - L30: "The data in this slide pack are for information and do not include analysis,
    interpretation, or conclusions."
  - L37: "All questions are based on 94 responses unless otherwise stated."
  - L39: "Some questions allowed respondents to select multiple answers and so frequencies are
    greater than total completed responses (94)."
  - L41: "Due to rounding, data may not precisely reflect absolute totals or %."
  - L44: "In free-text questions (Q16, Q17 and Q23), we identified common themes to categorise
    and count responses."
  - L46-47: in "Q3, Q5, Q10, Q13, Q20 and Q21" respondents could specify details; these are
    summarised in call-out boxes "but did not recode the responses"; example Q3 (slide 7):
    'tourism' "not recoded as Arts and recreation ... but left as 'other - please specify'".
  - L50-52 disaggregation: size categories "0-19 employees, 20-99 employees and 100+ employees";
    for sector, "due to the small number of respondents, 'other' includes: health and medical;
    information media and telecommunications; professional services; retail; trades and home
    services and 'other' as self selected by respondents."
- Defined terms: "merchants (businesses)" L9; "completed" response L24; "virtual cards or
  one-time virtual card numbers (VCNs)" L254; sector 'other' L52; size bands L51.
- How the numbers are printed: each slide's "Note:" gives explicit label-count pairs (reliable).
  Chart data labels are printed as a bare run of numbers followed by the option labels; pairing
  is BY ORDER ONLY, and in the breakdown charts zero/hidden bars are simply absent, so a series
  can have fewer values than options. No image of the slides is available to verify. Everything
  below marked "by order" or "run" is in that state. Remarks below about which group is short of
  values come from reading each run in consecutive groups (size or sector order, where complete
  groups sum to 100%) and are themselves unverified.

### D09 slide ledger (question, base, options; C = count, % = percentage)

- Slide 1 (L3-7): title.
- Slide 2 "Introduction" (L9-20): purpose bullets (see caveats).
- Slide 3 "Key survey considerations" (L22-33): dates, 94 responses, 2 on behalf, voluntary.
- Slide 4 "Data considerations" (L35-53): see caveats.
- Slide 5 (L55-57): section "Respondent Profile Questions 1 to 3".
- Slide 6 (L59-65):
  - Q1 "Which of the following best describes you?" Base 94 (L61). C: "50 as employee or manager
    at a business, 42 as business owner and 2 as responding on behalf of a business." No
    percentages printed.
  - Q2 "Approximately how many people does your business currently employ in New Zealand?" Base
    94 (L62). C: "12 responses for 2-5 employees, 27 responses for 6-19 employees, 14 responses
    for 20-49 employees, 16 responses for 50-99 employees and 25 responses for 100 or more
    employees. No respondents with 1 employee (sole trader)." Aggregated %, L62: "41% for 0-19
    employees, 32% for 20-99 and 27% for 100 or more employees." Chart %, L63-64 (by order):
    2-5 13%; 6-19 29%; 20-49 15%; 50-99 17%; 100 or more 27%.
- Slide 7 (L67-85): Q3 "Which industry best describes the business you are responding for?"
  Base 94 (default). C run L75: "46 26 7 5 4 2 1 1 1 1"; labels in order L77-85: Accommodation
  (hotel, motel, Airbnb etc.); Hospitality (cafe, restaurant, bar, take away shop etc.); Other
  (please specify); Arts and recreation (including leisure and tourism experiences); Transport &
  logistics (airlines, taxi, car-rental, courier, delivery etc.); Retail (clothing, electronics,
  home goods etc.); Professional services (legal, accounting, consulting, real estate etc.);
  Trades & home services (builder, electrician, plumber etc.); Health & medical (clinic, dental,
  physio etc.); Information media and telecommunications. Axis "Number of Respondents". By
  order: Accommodation 46; Hospitality 26; Other 7; Arts and recreation 5; Transport & logistics
  4; Retail 2; Professional services 1; Trades & home services 1; Health & medical 1;
  Information media and telecommunications 1 (ten values, ten labels; consistent with the sector
  bases n=46/26/13/5/4 printed on later slides). Call-out "Other sectors specified" L69-74:
  Travel and tourism (3); Transport (2); Wholesale (1); Government (1).
- Slide 8 (L87-88): section "Acceptance and use of commercial credit cards Questions 4 to 8".
- Slide 9 (L90-96): Q4 "How does your business use commercial credit cards? (Select all that
  apply)". Base 94, "Multiple answers permitted" (L95). C, L92-93 (by order; "Response
  Frequency"): "Our business accepts commercial credit cards from customers" 92; "Our business
  uses commercial credit cards to make payments" 56.
- Slide 10 (L98-106): Q4 by size and sector, "count of respondents". Size bases L102: 0-19
  (n=39), 20-99 (n=30), 100+ (n=25). Run L99 (after slide no. 10): "39 15 29 24 24 17". Sector
  bases L106: Accommodation (n=46), Hospitality (n=26), Other (n=13), Arts & recreation (n=5),
  Transport & logistics (n=4). Run L103: "46 25 26 12 11 11 5 4 4 4". Pairing of values to
  option x group is not printed (reading the run as accepts/uses pairs per group reproduces the
  slide-9 totals 92 and 56; unverified against an image).
- Slide 11 (L108-121): Q5 "How do your trade/corporate customers usually pay you? (Select all
  that apply)". Base "92 respondents. Multiple answers permitted." (L118). C run L109: "1 3 32
  56 58 58 85"; labels in order L111-117: Other (please specify) 1; Buy now, Pay later products
  3; Cash 32; Debit cards / EFTPOS 56; Bank transfer 58; Invoices / trade accounts 58; "Credit
  cards (Commercial or personal such as Visa, Mastercard and American Express etc. including..."
  85 (label truncated as printed). Call-out L119-121: "Invoice-Based Payments / Chargebacks (1)".
- Slide 12 (L123-129): Q5 by size and sector (counts). Size bases L127: 0-19 (n=39), 20-99
  (n=29), 100+ (n=24). Run L125: "37 24 19 12 2 24 1 26 18 23 13 1 19 22 14 16 7 15" (18 values
  for 7 options x 3 groups). Option order printed L125-126: Credit cards; Debit cards/EFTPOS;
  Bank transfer; Cash; Buy Now, Pay Later products; Invoices/trade accounts; Other. Sector bases
  L129: Accommodation (n=46), Hospitality (n=26), Other (n=11), Arts & recreation (n=5),
  Transport & logistics (n=4). Run L128: "45 33 32 18 2 35 1 24 18 11 12 12 8 3 8 1 6 4 5 3 4 2
  2 1 1 2" (26 values for 7 x 5). Values are missing for some cells; cell assignment unresolved.
- Slide 13 (L131-134): Q6 "Thinking about the business overall, what proportion of sales are
  commercial credit card transactions?" Base 92 (L134). C (L134): "29 noted 'under 25%', 18
  'noted 25% to 50%,' 36 noted '50% or more' and 9 noted 'not sure.'" % (L132-133, by order):
  Under 25% 32%; 25% to 50% 20%; 50% or more 39%; Not sure 10%.
- Slide 14 (L136-143): Q6 by size and sector, "% of respondents in each group". Option order:
  Under 25%; 25% to 50%; 50% or more; Not sure. Size (n=39/29/24, L140) run L138 (after slide
  no. 14): "36% 15% 46% 3% 24% 24% 38% 14% 33% 21% 29% 17%" (12 values = 4 x 3; each consecutive
  four sums to 100). Sector (n=46/26/11/5/4, L143) run L141: "15% 28% 46% 11% 42% 12% 38% 8% 73%
  9% 40% 20% 40% 25% 0% 50% 25%" then the axis "0% 10% ...". 17 values for 4 x 5: the third
  group (Other) shows only "73% 9%" and the fourth (Arts & recreation) only three values.
- Slide 15 (L145-159): Q7 "From your experience, what are the main benefits of accepting
  commercial credit cards? (Select up to three)". Base 92, "Multiple answers permitted" (L159).
  C run L154: "78 56 48 36 10"; labels in order L154-157: Faster payment than invoices/trade
  accounts 78; Less admin work than invoices/trade accounts 56; Not having to provide credit 48;
  Attracts more customers 36; Other (please specify) 10. Call-out "Other specified reasons"
  L146-154: Customer driven (6); No benefit (2); Better than cash (1); Unknown (1).
- Slide 16 (L161-168): Q7 by size and sector (counts). Option order here (L163-164): Faster
  payment; Less admin work; Attracts more customers; Not having to provide credit; Other (note:
  "Attracts more customers" and "Not having to provide credit" are in the opposite order to
  slide 15). Size (n=39/29/24, L165) run L163: "30 23 17 21 6 25 17 11 14 4 23 16 8 13" (14
  values for 5 x 3). Sector (n=46/26/11/5/4, L168) run L166: "43 33 19 29 1 18 15 11 9 5 9 4 3 6
  2 4 3 1 2 2 4 1 2 2" (24 values for 5 x 5).
- Slide 17 (L170-180): Q8 "Compared to accepting personal credit cards, do commercial credit
  cards offer any additional advantages to your business?" Base 92 (L179). C: "65 noted 'no
  difference', 18 noted 'not sure/don't know' and 9 noted 'yes'." % (L177-178, by order): No
  difference 71%; Not sure / don't know 20%; Yes (please explain) 10%. Call-out "Explanations
  given" L172-176: "Customer driven (5) eg no choice - have to accept, to keep customer happy";
  "Ease and security of payments (4) eg less risk of default with commercial than personal".
- Slide 18 (L182-190): Q8 by size and sector, "% of total respondents in each gropup" (sic).
  Option order: Yes; No difference; Not sure/don't know. Size (n=39/29/24, L186) run L183: "15%
  72% 13% 7% 69% 24% 4% 71% 25%" (9 = 3 x 3). Sector (n=46/26/11/5/4, L190) run L187: "11% 67%
  22% 8% 69% 23% 18% 82%80% 20% 75% 25%" (12 values for 3 x 5; the last three groups show two
  values each; "82%80%" fused).
- Slide 19 (L192-193): section "American Express and Buy-Now, Pay-Later Questions 9 to 13".
- Slide 20 (L195-203):
  - Q9 "Do you accept American Express from trade/corporate customers?" Base 92 (L199). C: "58
    noted 'yes', 30 noted 'no' and 4 noted 'previously but no longer'." No % printed.
  - Q11 "If you accept American Express transactions, do they mainly:" Base "58 respondents ,
    who accepted American Express as noted in Question 9" (L200). C (L201-202): "24 noted
    'replace Mastercard/Visa payments', 21 noted 'additional sales', 12 'noted not sure' and 1
    noted 'replace invoicing or trade accounts'." No % printed.
- Slide 21 (L205-225): Q10 "What are the reasons for not accepting American Express from
  trade/corporate customers?" Base "34 respondents, who answered 'no' or 'previously but no
  longer' to Q9. Multiple answers permitted." (L221-222). C run L223-224 (by order;
  "Frequency"): High cost 24; Low demand 12; Other (please specify) 8. Call-out "Other specified
  reasons" L208-220: Unknown/unsure (2); High charges (2); Inability to surcharge differently
  (1); Customer has a commercial card already (1); No demand (1); Business choice (1).
- Slide 22 (L227-233):
  - Q12 "Do you accept Buy now, Pay later from trade/corporate customers?" Base "92 respondents
    who answered this question" (L231). C: "77 answered 'no', 15 answered 'yes'. Nil responses to
    'previously, but no longer.'" % (L232, by order): No 84%; Yes 16%.
  - Q13 "What are the reasons for not accepting Buy-Now, Pay-Later from trade/corporate
    customers?" Base "77 respondents who answered 'No' to Question 12 ... Multiple answers
    permitted." (L232). NO response options or counts for Q13 are present in the text (chart
    content missing) - gap.
- Slide 23 (L235-236): section "Virtual commercial credit card focused questions Questions 14
  to 18".
- Slide 24 (L238-241): Q14 "Do you receive bookings from online platforms such as Booking.com,
  Expedia etc.?" Base "92 respondents who answered this question" (L240). C: "63 noted 'yes', 28
  noted 'no' and 1 respondent noted 'not sure/don't know'." No % printed.
- Slide 25 (L243-252): Q14 by size and sector, "% of respondents in each group". Options: Yes;
  No; Not sure/don't know. Size (n=39/29/24, L248) run L245: "59% 41% 72% 28% 79% 17% 4%" (7
  values for 3 x 3). Sector (n=46/26/11/5/4, L252) run L249: "100% 35% 65% 9% 82% 9% 80% 20% 75%
  25%" (10 values for 3 x 5).
- Slide 26 (L254-257): Q15 "Do you receive payments via virtual cards or one-time virtual card
  numbers (VCNs)?" Base 92 (L256). C: "54 noted 'yes', 29 noted 'no' and 9 noted 'Not sure/don't
  know'." No % printed.
- Slide 27 (L259-268): Q15 by size and sector, "% of respondents in each group". Options: Yes;
  No; Not sure/don't know. Size (n=39/29/24, L264) run L261: "46% 38% 15% 62% 31% 7% 75% 21% 4%"
  (9 = 3 x 3). Sector (n=46/26/11/5/4, L268) run L265: "91% 9% 0% 31% 46% 23% 55% 18% 0% 80% 20%
  25% 75% 0%" then the axis "0% 10% ...". The third group (Other, n=11) shows only "55% 18%";
  which options those two belong to is not determinable by position (slide 30 prints Other
  (n=3) as the number of "Other" respondents who answered Yes to Q15).
- Slide 28 (L270-278), both "Key themes" free-text questions, base for each "54 respondents who
  answered 'Yes' to Question 15 ... Multiple answers permitted." (L272, L273):
  - Q16 "What are the benefits to your business for receiving payments via virtual cards or
    one-time virtual card numbers (VCNs)? (Key themes)". C run L275 (by order; "Frequency"):
    Faster and guaranteed payment 26; Security and reduced fraud risk 12; Customer convenience
    and business necessity 13; Administrative efficiency 9; Limited or no merchant benefit 8.
  - Q17 "Are there any challenges in receiving payments via virtual cards or one-time virtual
    card numbers (VCNs)?" C run L276-278 (by order): No challenges experienced 20; Costs
    associated with accepting virtual cards 15; Restrictions on payment processing 15; Issues
    with card processing and system functionality 6; Additional administration and payment
    management 10.
  - Both runs are not in descending order (12 before 13; 6 before 10), so the by-order pairing
    of the middle labels is unverified.
- Slide 29 (L280-283): Q18 "Have you noticed more of these virtual cards or one-time virtual
  card numbers (VCNs) in recent years?" Base "54 respondents who answered 'Yes' to Question 15"
  (L282). C: "43 noted 'yes', 7 noted 'no' and 4 noted 'not sure/don't know'." No % printed.
- Slide 30 (L285-293): Q18 by size and sector, "% of respondents in each group". Options: Yes;
  No; Not sure/don't know. Size bases L289: 0-19 (n=18), 20-99 (n=18), 100+ (n=18). Run L286:
  "83% 11% 6% 94% 19% 72% 11% 17%" (8 values for 3 x 3; read in groups the middle pair "94%
  19%" exceeds 100% - unresolved as printed). Sector bases L293: Accommodation (n=42),
  Hospitality (n=8), Other (n=3), Arts & recreation (n=0), Transport & logistics (n=1). Run
  L290: "90% 5% 5% 50% 38% 13% 67% 33% 100%".
- Slide 31 (L295-296): section "Commercial credit cardholder questions Questions 19 to 22".
- Slide 32 (L298-301): Q19 "Does your business use commercial credit cards for your business
  expenses?" Base 94 (L300). C: "63 noted 'yes', 31 noted 'no'." % (L301, by order): Yes 67%; No
  33%. (Compare Q4, slide 9: "Our business uses commercial credit cards to make payments" 56 of
  94 - a different question with a different count.)
- Slide 33 (L303-310): Q19 by size and sector, "% of respondents in each group". Options: Yes;
  No. Size (n=39/30/25, L307) run L305: "56% 44% 83% 17% 64% 36%". Sector (n=46/26/13/5/4,
  L310) run L308: "67% 33% 46% 54% 92% 8% 80% 20% 100%" (9 values for 2 x 5).
- Slide 34 (L312-323): Q20 "From your experience, what are the main benefits of using
  commercial credit cards for your business expenses? (Select all that apply)". Base "63
  respondents who answered 'Yes' to Question 19 ... Multiple answers permitted." (L313). C run
  L323 (by order; "Response Frequency"): Expense reporting 27; Employee cards 20; Smooth
  expenses to optimise cash flow 19; Other (please specify) 20; Interest free period 18; Reward
  benefits such as Airpoints 17; Travel benefits such as travel insurance 7. Call-out "20
  responses:" L315-322: Online & Supplier Payments (7); Convenience & Faster Purchasing (3);
  Operational Efficiency & Reduced Administration (4); Travel & Employee Expenses (3); No clear
  benefit (2); Security & Risk Reduction (1).
- Slide 35 (L325-329): Q20 by size and sector (counts). Option order here (L327): Interest free
  period; Expense reporting; Employee cards; Reward benefits such as Airpoints; Travel benefits
  such as travel insurance; Smooth expenses to optimise cash flow; Other (different order from
  slide 34). Size bases printed L328: 0-19 (n=39), 20-99 (n=30), 100+ (n=25) (the all-respondent
  bases, although slide 34 gives the question base as 63). Run L327: "6 5 5 9 1 8 6 10 12 8 8 6
  10 7 2 10 7 1 6" (19 values for 7 x 3). Sector bases printed L329: n=46/26/13/5/4. Run L329:
  "9 18 7 8 4 10 7 8 5 4 5 3 5 3 2 5 1 1 7 2 3 2 2 1 1 1 1 1 1" (29 values for 7 x 5). Cell
  assignment unresolved.
- Slide 36 (L331-342): Q21 "If these commercial credit cardholder benefits were no longer
  included, would you be willing to pay separately to keep any of them?" Base "63 respondents
  who answered 'Yes' to Question 19" (L334). C: "33 noted 'not sure', 27 noted 'no' and 3 noted
  'yes'." No % printed. Call-out "3 responses" L335-341: Airpoints (1); Staff expense management
  (1); Did not understand question (1).
- Slide 37 (L344-353): Q21 by size and sector, "% of total respondents in each group". Options:
  Yes; No; Not sure. Size bases L349: 0-19 (n=22), 20-99 (n=25), 100+ (n=16). Run L346 (after
  slide no. 37): "9% 41% 50% 4% 36% 60% 56%" (7 values for 3 x 3; the 100+ group shows one
  value, "56%", with no label for which option). Sector bases L353: Accommodation (n=31),
  Hospitality (n=12), Other (n=12), Arts & recreation (n=4), Transport & logistics (n=4). Run
  L350: "3% 42% 55% 42% 58% 17% 33% 50% 50% 50% 75% 25%" (12 values for 3 x 5).
- Slide 38 (L355-358): Q22 "Thinking about commercial credit card fees charged to your business
  and the benefits cardholders receive. Would you prefer:" Base "the 63 respondents who answered
  'Yes' to Question 19" (L358). C: "49 noted 'lower card acceptance fees etc.' 9 noted 'not
  sure' and 5 noted 'keep things as they are today'." No % printed. Full option wording appears
  only on slide 39: "Keep things as they are today"; "Lower card acceptance feed, even if
  cardholders receive few benefits" (sic, L362); "Not sure".
- Slide 39 (L360-367): Q22 by size and sector (%). Size (n=22/25/16, L365) run L362 (after
  slide no. 39): "14% 82% 5% 8% 68% 24%" (6 values for 3 x 3: no values at all for the third
  group, 100+). Sector (n=31/12/12/4/4, L367) run L366: "10% 68% 23% 8% 92% 83% 17% 25% 75%
  100%" (10 values for 3 x 5).
- Slide 40 (L369-371): section "Final comments from survey respondents Question 23".
- Slide 41 (L373-385): Q23 "Is there anything else you'd like to tell us about accepting or
  using business credit cards?" Base "39 responses who answered this question. Multiple answers
  permitted." (L381). C run L377-379 (by order; "Frequency"): High costs and fees 18; No
  additional feedback 11; Fee caps, regulation, and transparency 11; Surcharging and cost
  recovery 8; Limited merchant benefit vs operational benefits 5. Four boxed respondent quotes
  (L375-376, L377, L383, L384-385); L382: "Text in boxes are direct quotes from the survey and
  illustrate how free-text comments were categorised into themes."
- Closing (L387-388): "Further information, including our draft decision please refer to:
  https://www.comcom.govt.nz/regulated-industries/projects/interchange-fee-regulation/".

### D09 base sizes at a glance (as printed)

- 94: Q1, Q2, Q3 (default), Q4, Q19. 92: Q5, Q6, Q7, Q8, Q9, Q12, Q14, Q15. 58: Q11. 34: Q10.
  77: Q13. 54: Q16, Q17, Q18. 63: Q20, Q21, Q22. 39: Q23.
- Size bases: 39/30/25 (94-base slides 10, 33, and slide 35 as printed); 39/29/24 (92-base
  slides 12, 14, 16, 18, 25, 27); 18/18/18 (slide 30); 22/25/16 (slides 37, 39).
- Sector bases: 46/26/13/5/4 (slides 10, 33, 35); 46/26/11/5/4 (slides 12, 14, 16, 18, 25, 27);
  42/8/3/0/1 (slide 30); 31/12/12/4/4 (slides 37, 39).
- Question numbering on slides is not sequential: Q11 shares slide 20 with Q9; Q10 is slide 21;
  Q13 is printed before Q12 on slide 22.

### D09 remaining fields

- Entities named: SurveyMonkey L9; Visa, Mastercard, American Express/Amex L117, L125;
  Booking.com, Expedia L238; Airpoints L323, L337.
- Restates the draft decision: none (only "our draft decision" L9, L387). No interchange rates,
  caps or dollar figures appear anywhere in D09.
- Hedged claims: L41 "data may not precisely reflect absolute totals or %"; L15-17 results are
  "one of the factors" in "a balancing exercise". Survey answers are respondent reports.
- Rounded percentages beside exact counts: every slide with both (Q2, Q6, Q8, Q12, Q19); Q6
  percentages 32/20/39/10 are printed beside counts 29/18/36/9.
- Table/slide problems (gaps): (1) Q13 has no option data; (2) all size/sector breakdown charts
  (slides 10, 12, 14, 16, 18, 25, 27, 30, 33, 35, 37, 39) are unlabelled runs with absent cells -
  value-to-cell mapping is not printed; (3) slide 30 size run contains "94% 19%"; (4) slide 39
  has no values for the 100+ group; (5) Q9, Q11, Q14, Q15, Q18, Q21, Q22 charts print no
  percentages (counts only in notes); (6) slide 11 credit-card label truncated ("including...").
- Coverage: FULL. Lines 1-390 read sequentially. Nothing unread. The items in "problems" are
  missing/unresolvable source content (no slide image available), not unread text.

## D10 (Doc 15) - Paymark submission

- Source: `text/D10.txt`, 101 lines. Page footers "Paymark Limited 2".."5" at L20, L38, L55, L79.
- Written or submitted by: Paymark Limited ("Paymark"), L6. Contact: Julia Nicol, "Head of Public
  Affairs, Regulatory & Corporate Communications" (L99). Organisations it only names: Cuscal
  Limited (its owner), Mastercard, Visa, UK Payment Systems Regulator, Reserve Bank of Australia,
  European Union, RTE / Reuters.
- Type, date, edition: submission "By email", "30 June 2026" (L3) - the earliest-dated of the
  submissions in this part.
- Entities and aliases: "the consultation document" = the Draft Decision and Reasons Paper
  "published 4 June 2026" L6; "Honour All Cards rule" L9; "honour all issuers" vs "honour all
  products" rule L61; "Visa's Fleet 2.0 programme"/"Visa Fleet 2.0" L51; "Retail Payment System
  Act 2022" L67; Paymark self-description: "established in the 1980s" L14; "employing around 200
  people locally and, since 2 June 2026, part of Cuscal Limited, an ASX-listed corporation" L15.
- Positions (verbatim, with line):
  - Supports caps, L6: "We support the Commission's proposed intervention to reduce commercial
    card interchange fees"; L22: "Paymark supports regulation of commercial card interchange
    fees."; L40: "We support the Commission's proposal to cap commercial card interchange fees."
  - L24 / L39: "While fee caps are necessary, they are not sufficient."
  - Honour All Cards, L11: "merchants should be able to decline commercial cards, or categories
    of commercial cards, while continuing to accept other Mastercard and Visa cards, provided
    customers receive clear and accurate information at the point of sale." L67: "We recommend
    that the Commission consider using its powers under the Retail Payment System Act 2022 to
    introduce a regulatory measure that prevents scheme rules or acquirer arrangements from
    requiring merchants to accept commercial cards as a condition of accepting other Mastercard
    or Visa cards." L97: "Removing the Honour All Cards rule for commercial cards".
  - Cap level, premium, tiering, exemption, implementation period for the caps: none stated. L88
    asks only for "clear implementation timeframes" for any Honour All Cards change (no figure).
- Quantitative statements:
  - L26 (NZ; Mastercard and Visa commercial credit cards; attributed to the Commission): "The
    Commission has identified that New Zealand businesses currently pay approximately $125
    million each year in interchange fees to accept Mastercard and Visa commercial credit cards,
    and that commercial credit cards make up a small share of transactions but generate a
    disproportionately large share of interchange fees. The Commission's proposed caps are
    expected to reduce business costs by approximately $40 million annually."
  - L44 (United Kingdom; Mastercard and Visa scheme and processing fees, not interchange;
    footnote 1, L53: "Payment Systems Regulator, MR22/1.10 Market review of card scheme and
    processing fees: final report, 6 March 2025"): "Mastercard and Visa increased core scheme
    and processing fees to acquirers by at least 25% since 2017, costing businesses at least
    £170 million extra per year" (pounds sterling; UK).
  - L44 footnote 2 (L53): "RTE / Reuters, EU widens probe into Visa and Mastercard fees, 26 May
    2025".
  - L15: "around 200 people".
- Restates the draft decision: $125 million / $40 million (L26); "commercial credit cards make up
  a small share of transactions but generate a disproportionately large share of interchange
  fees" (L26); publication date 4 June 2026 (L6). L18-20 paraphrases the consultation's request
  for views. No cap percentages, paragraph or question numbers.
- Lists: "merchants may:" five bullets L71-81 (the fifth, "communicate any card acceptance
  limitations clearly to customers before payment is initiated", is after the page break, L81).
- Events and dates: submission 30 June 2026 (L3); draft decision published 4 June 2026 (L6);
  Paymark part of Cuscal "since 2 June 2026" (L15); Paymark "established in the 1980s" (L14);
  UK scheme fee rise "since 2017", PSR final report 6 March 2025 (L44, L53); EU probe article 26
  May 2025 (L53); "In 2007, the Reserve Bank of Australia distinguished between an "honour all
  issuers" rule ... and an "honour all products" rule" (L61); "In 2016, the European Union
  restricted the Honour All Cards rule" with "a limited carve-out for consumer cards of the same
  brand and the same category of prepaid, debit or credit card" (L62).
- Hedged claims:
  - L9 the rule "can require merchants ... to accept higher-cost commercial cards" - "can".
  - L22 "those costs are likely to be reflected in prices paid by consumers and businesses".
  - L34 costs "may ultimately be passed through in retail prices".
  - L42 "incentives to keep total acceptance costs low may remain limited".
  - L44 "A further risk is that reductions in regulated interchange may be offset by increases
    in unregulated scheme and processing fees" - "may"; the UK finding that follows is firm, with
    "at least" on both figures.
  - L51 "affected fuel and service station merchants may need compatible POS systems ... some
    legacy equipment may require upgrades" - attributed to "Industry guidance".
  - L61 an "honour all issuers" rule "may support network efficiency"; "honour all products"
    rule "can prevent merchants from declining".
  - L26 "approximately $125 million", "approximately $40 million" - approximations as restated.
- Coverage: FULL. Lines 1-101 read sequentially. Nothing unread.

## D11 (Doc 16) - Restaurant Association of New Zealand submission

- Source: `text/D11.txt`, 89 lines. Page numbers at L19, L34, L54, L74. OCR inserts stray spaces
  inside words and before hyphens (e.g. "2, 300", "percentage -point", "w elcomes").
- Written or submitted by: The Restaurant Association of New Zealand ("the Association"), L8,
  L85. No individual signatory printed. Organisations it only names: Commerce Commission,
  Australian Restaurant & Cafe Association, Australian Hotels Association, Visa, Mastercard.
- Type, date, edition: letter submission, "20 July 2026" (L3).
- Entities and aliases: "the Association"/"The Restaurant Association" L8-12; "Credit Contracts
  and Consumer Finance Act" L30; "interchange-plus pricing" vs "blended pricing" L48;
  "limiting mechanism" heading L43, described as "the safeguard that prevents existing
  interchange rates that are already below the proposed caps from being increased" L44.
- Positions (verbatim, with line):
  - Supports, L12 / L79: "The Restaurant Association supports regulating and lowering commercial
    credit card interchange fees." L24: "We support the introduction of caps on commercial
    credit card interchange fees and welcome the substantial reduction proposed."
  - Domestic caps too high, L27: "we are not convinced that the proposed domestic caps of 0.50%
    for in-person transactions and 0.90% for online transactions go far enough."
  - Premium, L32: "We do not consider market-stability considerations sufficient reason for
    merchants to fund an additional premium. The Commission should align domestic commercial
    credit card caps with the equivalent personal credit card caps, or limit any premium to the
    amount clearly supported by evidence of additional issuer costs and merchant benefits."
  - Foreign-issued caps, L36: "The proposed foreign-issued caps of 0.70% for in-person
    transactions and 1.50% for online transactions also remain particularly high." L41: "should
    be lowered unless the Commission can demonstrate why these higher rates are necessary and
    proportionate."
  - Limiting mechanism, L44: "We also support the safeguard ... we ask the Commission to confirm
    whether preferential or negotiated foreign-issued rates exist that could similarly be
    repriced upward, and to extend the same protection to foreign-issued transactions if so."
  - Implementation, L59: "finalise and implement the new limits without unnecessary delay; the
    proposed two-to-three-month implementation period appears reasonable, provided there is a
    clear effective date and practical information for businesses".
  - Surcharging, L76: "Businesses should retain the ability to recover the reasonable,
    provider-specific cost of accepting a payment method. Any consideration of applying
    surcharge restrictions should be separately consulted on and supported by evidence about
    merchants' total costs."
- Quantitative statements:
  - L9: "Since 1972"; "more than 2, 300 restaurants, cafes, bars, caterers and takeaway
    businesses" (printed "2, 300" with a space).
  - L14 (NZ hospitality; the Association's "August 2024 retail-payments survey"; base not
    printed): "more than 98% of respondents ... accepted Visa or Mastercard credit card
    payments, while 96% accepted contactless payments."
  - L17 (NZ; attributed to the Commission): "The Commission estimates that businesses pay
    approximately $1 billion per year overall to accept Visa and Mastercard payments and pay
    $170 million annually in merchant service fees for Mastercard and Visa commercial credit
    card payments, including approximately $125 million in interchange fees. The Commission's
    estimate that the proposed caps would reduce merchant costs by around $40 million".
    ($1 billion = all Visa and Mastercard payments; $170 million = MSF on commercial credit;
    $125 million = interchange within that; $40 million = saving, no "annually" in D11's
    sentence.) Also L17: "card use has accelerated dramatically since 2019".
  - L27 (the Draft Decision's proposed domestic caps, as restated): "0.50% for in-person
    transactions and 0.90% for online transactions".
  - L28: "The proposed rates include a 0.20 percentage-point premium above the equivalent
    domestic personal credit card caps. The Commission attributes 0.10 percentage points to a
    combination of additional issuer costs and merchant benefits."
  - L31: "The remaining 0.10 percentage-point premium is intended to promote market stability
    and align the proposed rates with the Australian benchmark - not to recover an identified
    additional cost or merchant benefit."
  - L36 (proposed foreign-issued caps, as restated): "0.70% for in-person transactions and 1.50%
    for online transactions".
  - L55: "Despite two previous rounds of interchange fee regulation".
  - L59: "two-to-three-month implementation period".
  - L66 (the Association's "small November 2025 snapshot poll of members"; base not printed):
    "interest-free repayment periods were valued by 56% of respondents, more than 62% rated the
    additional benefits offered by their card as low value."
  - The personal credit card cap levels themselves are not printed in D11.
- Restates / disputes the draft decision: all L17, L27, L28, L31, L36 figures; L28 "the
  Commission's detailed analysis describes the differences in fraud costs as minor and the
  effect of differences in administrative costs as small. It also finds that many merchant
  benefits are already reflected in the personal credit card settings, although it identifies
  avoiding the cost of establishing and operating trade accounts as an additional benefit"; L30
  "commercial credit cards are exempt from the Credit Contracts and Consumer Finance Act"; L38
  "the Commission's draft decision cites evidence from the Australian Restaurant & Cafe
  Association and the Australian Hotels Association that card acceptance costs are hardest for
  the hospitality sector to absorb or pass on"; L44 "the Commission is not currently proposing to
  extend this safeguard to foreign-issued commercial credit transactions"; L57 "the Commission's
  stated intention to monitor these areas"; L69 "the Commission's view that current interchange
  costs may not be proportionate to the value of cardholder benefits". No paragraph or question
  numbers quoted.
- Lists: "We recommend that the Commission:" five bullets L52-63 (explain pricing L52; publicly
  report monitoring L57; finalise without delay L59; monitor availability/cost L61; monitor
  migration L63). The unbulleted paragraph at L55 sits between bullets 1 and 2.
- Events and dates: submission 20 July 2026 (L3); Association founded/representing "Since 1972"
  (L9); August 2024 survey (L14); November 2025 poll (L66); card use "since 2019" (L17).
- Hedged claims:
  - L27 "we are not convinced that ... go far enough" - a stance, not a figure.
  - L39 "foreign-issued and online transactions may involve additional costs and fraud risks" -
    "may" sits in the concession clause ("Although we recognise ..."); the main claim (merchants
    should not bear higher fees unless supported by evidence) is firm.
  - L59 the implementation period "appears reasonable, provided there is a clear effective date"
    - "appears" plus a condition.
  - L68 "Given the small sample size, these results should be treated as indicative only." -
    scope: the November 2025 poll figures (56%, 62%) at L66.
  - L69 "they support the Commission's view that current interchange costs may not be
    proportionate" - "may" inside the attributed view.
  - L48 fees "can be difficult to understand" ... "blended pricing may prevent merchants from
    seeing".
- Rounded prose beside exact figures: "more than 98%", "more than 62%", "more than 2, 300",
  "approximately $1 billion", "approximately $125 million", "around $40 million"; "$170 million"
  is printed without a qualifier.
- Coverage: FULL. Lines 1-89 read sequentially. Nothing unread.

## D12 (Doc 11) - Retail NZ submission

- Source: `text/D12.txt`, 118 lines. Numbered paragraphs 1-46; page numbers fused at L31 ("2
  methods"), L53, L74 ("4 cashflow"), L89.
- Written or submitted by: Retail NZ (L3, L13), signed Carolyn Young, "CHIEF EXECUTIVE"
  (L114-115). Organisations it only names: Commerce Commission, Reserve Bank of Australia, Stats
  NZ, Visa, Mastercard, American Express.
- Type, date, edition: letter submission, "20 July 2026" (L8). L46 para: "No part of this
  submission should be withheld under the OIA" (L111).
- Entities and aliases: "Merchant Service Fee (MSF)" L25; "small and medium enterprises (SMEs)"
  L22; "the Commerce Commission draft decision and reasons paper" L20 = "the paper" L25 = "the
  reasons paper" L69 = "reason paper" L72; "Monitoring Snapshot from Commerce Commission in June
  2026" L54; "Retail NZ member survey" (several questions; no base or date printed) L31-63.
- Positions (verbatim, with line):
  - Stance, L25 (para 6): "Overall Retail NZ is in support of the recommendations included in
    the paper, but believe the caps could go further to limit not just the interchange fee for
    commercial credit cards, but the total Merchant Service Fee (MSF)." L61 (para 21): "Retail
    NZ and our members support the rebalancing of the interchange fee for commercial cards".
  - Cap level / premium, L65 (para 23): "Our members would argue therefore that the interchange
    fee for commercial cards should be set at the same level as personal cards, as opposed to
    the 0.20% premium that the Commerce Commission is proposing." L101 (para 40): "Retail NZ
    supports the interchange fee for commercial credit cards being set at the same level as the
    interchange fee for personal credit cards. Furthermore, Retail NZ encourages the Commerce
    Commission to consider capping the MSF across the whole Visa and Mastercard network as
    noted in our earlier submission in 2024."
  - Scope, L66 (para 24) and L102 (para 41): "Retail NZ would support the inclusion of all
    credit card companies included in the interchange cap, across all credit card types, not
    just card types on the Visa and Mastercard network."
  - Limiting mechanism, L104 (para 42): "Retail NZ supports the limiting mechanism date to be
    set at 1 December 2025, to align with the prior interchange fee decision."
  - Implementation, L106 (para 43): "Retail NZ supports the 2-3 month implementation period for
    the decision to ensure that these benefits are passed on to merchants efficiently."
  - Monitoring, L108 (para 44): "actively monitor the noninterchange components of the MSF".
  - Statements, L43 (para 14): "A standardised bank statement across all banks ... would be a
    useful benefit to all merchants."
  - Disagreement, L69 (para 25): "Retail NZ does not agree with the Commerce Commission's point
    in the reasons paper that accepting commercial credit cards offers an alternative for
    retailers which would otherwise need to offer credit terms through trade accounts, as
    outlined in Table 2.1."
- Quantitative statements (New Zealand unless noted):
  - L15 (para 1): membership "accounting for nearly 70% of all domestic retail turnover"; "New
    Zealand's retail sector comprises approximately 30,000 businesses and employs around 222,000
    Kiwis."
  - L28 (para 7; attributed to the Commission's paragraph 2.9): "the cost of commercial credit
    cards is 50% higher than the growth in the value of the transactions" (wording as printed).
  - L31 (para 8; Retail NZ member survey): "58% of respondents told us the ability to adjust
    their surcharge depending on the payment type would be useful."
  - L35-36 (para 10; Retail NZ member survey, on personal credit card caps "Since December
    2025"): "Close to half (46.3%) said they have not seen any difference, while 21% said they
    hadn't looked closely enough to know. 26.3% said they had noticed a small change, while just
    5% reported their fees had decreased significantly."
  - L38 (para 11; member survey): "66% of Retail NZ members who answered our survey said they do
    not currently surcharge customers for contactless and credit card transactions and instead
    absorb those costs."
  - L39 (para 12; "June 2026 Stats NZ data"): "Most electronic card transactions (70.5% in the
    June 2026 Stats NZ data) go through the Mastercard and Visa credit card rails, which
    includes contactless debit payments ... By comparison, in 2016 only 45% of transactions were
    credit card transactions."
  - L43 (para 14; member survey): "34.7% of respondents could distinguish between domestic and
    international card fees on their statements, while 14.7% could distinguish between personal
    and commercial credit card fees."
  - L54 (para 18; "Monitoring Snapshot from Commerce Commission in June 2026"): "3 in 4 payments
    (74%) now use Mastercard and Visa, with only 26% of payments using EFTPOS, open banking
    payments and American Express."
  - L63 (para 22; member survey on the proposed caps): "Only 10.5% responded that the caps go
    far enough and would make a real difference; 66.3% felt the caps needed to go further."
  - L65 (para 23): "the 0.20% premium that the Commerce Commission is proposing".
  - L87 (para 34; United States): "Both Visa and Mastercard advised the Senate Hearings in the
    USA that their profit margin is in the vicinity of 50%."
  - L91 (para 35): "Over the past 18 months" (open banking discussion).
  - L104, L106: "1 December 2025"; "2-3 month".
  - Two different 66-ish figures: "66%" do not surcharge (L38) and "66.3%" caps need to go
    further (L63). Two different statements of Mastercard/Visa share: 70.5% of electronic card
    transactions (Stats NZ, L39) and 74% of payments (Commission Monitoring Snapshot, L54).
- Restates / disputes the draft decision (paragraph references it gives):
  - "paragraph 2.9" L28 (cost growth 50% higher than growth in transaction value).
  - "paragraphs 2.11.3, 2.11.4, 2.11.5 and 2.11.6" L48 ("We strongly support the analysis");
    "paragraph 2.11.1" L58 ("fees should come down once there is widespread adoption of new
    methods of payment").
  - "Table 2.1" L69 (trade accounts alternative) - disagrees.
  - "section 2.36" L72 ("how widely used commercial credit cards by SMEs") - cautions.
  - "paragraph 3.7.1" L82 ("higher fraud rates for commercial credit cards") - "We would like to
    see the data to support this statement."
  - "the 0.20% premium" L65; limiting mechanism date "1 December 2025" L104; "2-3 month
    implementation period" L106; "the prior interchange fee decision" L104.
  - L20 (para 4): major retailers' negotiated fees "are already significantly lower than those
    outlined in the Commerce Commission draft decision and reasons paper".
  - RBA quotation, L65: "The Reserve Bank of Australia consultation from July 2025 stated that
    "there is no clear evidence, including from the Issuer Cost Study, that issuers incur higher
    costs on commercial cards than on consumer cards"."
- Events and dates: submission 20 July 2026 (L8); "Since December 2025, the Commerce Commission
  capped interchange fees on personal credit cards" (L35); Stats NZ data June 2026 and 2016
  comparison (L39); Commission Monitoring Snapshot June 2026 (L54); RBA consultation July 2025
  (L65); Retail NZ's "earlier submission in 2024" (L101).
- Hedged claims:
  - L20 "fee caps are less likely to impact the current fees that they pay" - scoped to "Major
    retailers".
  - L25 "believe the caps could go further".
  - L65 "Our members would argue therefore that ..." - attributed to members; L101 states the
    same position as Retail NZ's own, unhedged.
  - L66 "It could also potentially benefit customers".
  - L76 "in some situations SME's may use a credit card as short term extended credit" - "may",
    scoped "in some situations"; contrasts with L76 "Retail NZ is not aware of any members
    using commercial credit cards in that way".
  - L82 "Our members do not believe that commercial credit cards necessarily have higher rates
    of fraud."
  - L87 "in the vicinity of 50%" - approximation, attributed to Visa and Mastercard testimony.
  - L15 "nearly 70%", "approximately 30,000", "around 222,000".
- Rounded prose beside exact figures: "Close to half (46.3%)" L35; "3 in 4 payments (74%)" L54;
  "the vast majority of respondents" beside 66.3% L63.
- Coverage: FULL. Lines 1-118 read sequentially. Nothing unread.

## D14 (Doc 12) - Revolut submission

- Source: `text/D14.txt`, 206 lines. Letter and policy sections L3-169; "Annexure 1" infographic
  text L171-204 (garbled labels only, no usable figures).
- Written or submitted by: Revolut Payments New Zealand Pty Ltd (L3), marked "PUBLIC" (L12),
  signed Georgia Grange, "Head of New Zealand" (L168-169). Organisations it only names/cites:
  Commerce Commission ("the Commission"/"ComCom"), RBNZ, American Express (Amex), Visa, MC,
  Payment Systems Europe (PSE), Kiwibank and Talbot Mills, NY Fed, BNZ, European Commission,
  Copenhagen Economics, EY, Inland Revenue Department (IRD), Auckland Council, Xero.
- Type, date, edition: letter submission, "20 July 2026" (L14).
- Entities and aliases: "merchant service charge (MSC)" L31 and "Merchant Service Fees (MSFs)"
  L80 (both used); "American Express ("Amex")" L43; "Commercial Virtual Credit Cards (VCCs)"
  L66 / "B2B VCCs" L123; "OTAs" L45, L116 (not expanded); "RevPay" L50; "Payment Systems Europe
  (PSE)" L64; "Merchant Indifference Test (MIT)" L161; "Accounts Payable (AP)" L131; "Retail
  Payment Systems Act" (printed with plural "Systems") L47, L52-54; "four party"/"three-party"
  L43-47.
- Positions (verbatim, with line):
  - Opposes caps, L17: "we do not believe capping commercial card interchange is the correct
    tool to deliver these objectives or that the proposed caps are set at an economically
    efficient level." L157: "Revolut recommends that the Commission reconsider the introduction
    of interchange price caps entirely."
  - If the Commission proceeds, three "strict prerequisites" (L159-164): "1. Prioritise
    Alternatives Over Price Caps ... maintaining and optimising merchants' rights to surcharge
    transparently"; "2. Require Comprehensive Data Collection and an MIT Study: Any proposed cap
    must be preceded by a major, industry-wide data collection exercise and a formal Merchant
    Indifference Test (MIT) study."; "3. Enforce Universal Application Across All Participants:
    No price cap should be considered unless it is applied universally across all payment
    network participants. This must explicitly include three-party schemes".
  - Exemption, L123: "the Commission should not include B2B VCCs as part of this blunt, blanket
    interchange cap framework."
  - Cost-benefit analysis, L27: "a more detailed cost benefit analysis which directly addresses
    these points would need to be done before such an action could be justified."
  - Surcharging, L58: "Alternative interventions, such as maintaining surcharging while
    supporting adoption of non-card alternatives and boosting schemes and acquiring competition,
    we think would be a much more effective and proportionate intervention."
  - Cap level, premium, implementation period: none proposed.
- Quantitative statements:
  - L50: RevPay "generally at a cost >50% cheaper than cards" (Revolut's own claim).
  - L56: Revolut services "up to 10 times cheaper than legacy banks in NZ - and have already
    resulted in hundreds of millions of direct savings for consumers" (no unit/currency printed).
  - L64 (NZ; "Payment Systems Europe (PSE) conducted merchant research on Revolut's behalf in
    June 2026"): "about three-quarters experience operational challenges when handling cash."
  - L75 (NZ; "Research conducted by Kiwibank and Talbot Mills in January 2026"): "45% of New
    Zealand business leaders surveyed (800) identify the ability to move quickly and adapt as a
    top critical factor for successful growth. Furthermore, 85% of local firms report that their
    organisation's values heavily influence everyday decision-making". Also "key research from
    the NY Fed in 2026" (no figure).
  - L78 (NZ; consumer cards): "BNZ reduced its interest-free window from 55 to 44 days within
    two months of new caps being introduced."
  - L86 (NZ; PSE research June 2026): "Among surveyed merchants accepting Amex (52%), 28% report
    that its Merchant Service Fee (MSF) is more expensive than Visa and Mastercard."
  - L88: "54% of those accepting Amex pass the fees onto consumers, carrying an average
    surcharge of 2.16% (significantly higher than standard Visa and Mastercard rates)."
  - L97 (Europe): "The 2025 European Commission study by Copenhagen Economics and EY revealed
    that ten years after Europe's 2015 Interchange Fee Regulation, the average price of payments
    actually increased." (no figure).
  - L105 (NZ; attributed to the Commission): "The Commission notes that New Zealanders spend
    approximately $45-65 million annually in 'excessive surcharges' and expects surcharge rates
    to drop alongside interchange reductions." (printed with an en dash: "$45–65 million").
  - L105 (NZ public sector): "the New Zealand Inland Revenue Department (IRD) currently charges
    a 1.42% convenience fee, and the Auckland Council charges 1.75% for online card payments,
    both of which are significantly higher than the Commission's proposed baseline."
  - L106-112 ("Our June 2026 research of New Zealand SMEs (revenues up to $50m)"; base size not
    printed): L108 "Less than half of surveyed merchants (44%) apply a surcharge for Visa and
    Mastercard, with 1.50% being the most frequent rate. The remaining 56% already absorb these
    costs." L110 "67% of merchants currently surcharging state they will look to pass on costs
    through alternative means (i.e., increasing shelf prices), while only 33% would absorb
    them." L112 "Respectively, 23% of all surveyed merchants and 23% of merchants who would pass
    on costs specifically state that removing surcharging would lead them to increase retail
    shelf prices. Among pure B2C operations, this risk spikes further, with 71% seeking
    alternative cost-pass-throughs and 29% anticipating direct price hikes."
  - L137 ("Our June 2026 merchant research"): "while 100% of surveyed B2B merchants face
    baseline Merchant Service Fees between 3.01% and 5.00%, their typical surcharges top out at
    2.50%. This reveals that B2B operators actively and deliberately absorb a cost deficit of up
    to 2.50% per transaction".
  - L141: "Revolut offers over nine distinct card controls, whereas incumbent Kiwi banks
    currently offer a maximum of three." L145: "within 100 meters of the terminal".
- Restates / disputes the draft decision: L17 "the proposed caps"; L37 "There appears little
  analysis in the ComCom paper on this point" (surcharging as alternative); L47 "not covered
  adequately in the publicly shared consultation document"; L54 "the Commission's June 2026
  commitment to "support the entry and growth of new payment alternatives,""; L62 quotation of
  Commissioner Bryan Chapple: "corner dairy should not be forced to absorb additional costs or
  increase their prices to cover the costs of rewards and benefits that only those with
  commercial credit cards get" (source of the quotation not stated); L62 "by treating corporate
  cards as a variation of consumer credit, the Draft Decision overlooks their unique utility";
  L95 "Because the Commission lacks an enforcement mechanism to mandate pass-through savings";
  L97 "the omission of multinational scheme fees from the regulatory scope"; L105 "$45-65
  million annually in 'excessive surcharges'"; L121 "Amex networks are structurally excluded
  from these specific network caps". No cap figures, premium, paragraph or question numbers.
- Lists: threats (i)-(iii) L22-25 (item (i) ends mid-sentence as printed); merchant-impact
  points First-Third L31-35; unintended-impact points First-Third L41-54; two "blind spots"
  L73-75; PSE Amex bullets L86-88; SME research bullets L108-112; four operational advantages
  L129-135; two card-control features L145-147; recommendations 1-3 L159-164.
- Events and dates: submission 20 July 2026 (L14); PSE merchant research June 2026 (L64, L84,
  L99, L106, L137); Kiwibank/Talbot Mills research January 2026 (L75); "NY Fed in 2026" (L75);
  Commission's "June 2026 commitment" (L54); "Europe's 2015 Interchange Fee Regulation" and
  "The 2025 European Commission study" (L97); "as highlighted by the RBNZ in 2025" on EFTPOS
  (L150); BNZ interest-free change "within two months of new caps being introduced" (L78, no
  date).
- Hedged claims:
  - L18 "this proposal will fail to create material savings" - firm.
  - L31 "may have a negligible impact on a merchant's total costs and in fact in many markets
    MSCs actually increase after a price cap" - "may" on the first clause, second clause firm.
  - L35 "If a merchant is choosing to not surcharge its customers, that is likely because they
    see the economic value" - "likely".
  - L41 "there will be a significant risk of a reduction in credit availability"; L43 "there is
    a real risk that a price cap distorts the payments market"; L49 "there is a risk a price cap
    will lock in the dominant payment providers".
  - L45 "It is very likely that businesses will move quickly to utilise Amex".
  - L92 "this intervention may actually push the blended MSF upwards" - "may".
  - L95 "Revolut expects that large B2B suppliers will keep the savings as pure margin" -
    expectation; "the regulation risks failing its consumer-welfare objective".
  - L99 "this remains a compelling cautionary example" after conceding Europe is "not directly
    comparable".
  - L101 "a portion of surveyed merchants reported that their overall processing fees have
    actually gone up" - unquantified "a portion".
  - L117 "international platforms will be inclined to seek alternative arrangements. Potentially
    shifting towards slower, riskier or less efficient payment settlement mechanisms".
  - L143 "Revolut believes it is the first to offer this comprehensive suite of features".
- Rounded prose beside exact figures: "Less than half ... (44%)" L108; "about three-quarters"
  L64 (no exact figure); "hundreds of millions" L56.
- Annexure 1 (L171-204): diagram labels, e.g. "OLIGOPOLY STRENGTHENED - MARKET POWER OF
  INCUMBENT BANKS INCREASES" L173-175, "Well meaning but potentially unintended outcomes of
  proposed interchange fee regulation." L189, "END RESULT Less competition and innovation, but
  no guarantee of lower surcharge fees to consumers." L197-198, "'FOR ILLUSTRATIVE PURPOSES"
  L200. Any numbers in the diagram are not legible in the text (L191 "aaSs.42", L201-202
  garbled) - visually unresolved.
- Extraction oddities: L13 email printed "PaymentsTeam@the Commission.govt.nz"; L22 item (i)
  truncated; L49-50 "(.e. Visa, MC and Amex)".
- Coverage: FULL. Lines 1-206 read sequentially. Nothing unread. Annexure diagram content is a
  visual gap.

## D15 (Doc 13) - TSB submission

- Source: `text/D15.txt`, 109 lines. Cover letter L4-32; "Appendix 1 - TSB's key concerns with
  the proposed calibration" L35-107, nine numbered headings.
- Written or submitted by: TSB Bank Limited ('TSB'), L8; signed Helen Barrowcliffe, "Head of
  Retail Banking Products, TSB" (L31-32). Organisations it only names: Toi Foundation (owner),
  American Express, Mastercard, Visa, Reserve Bank (NZ), Reserve Bank of Australia.
- Type, date, edition: letter submission, "20 July 2026" (L4).
- Entities and aliases: "Commerce Commission's ('Commission')" L8; "Draft Decision" L8, L23;
  "proportionate issuer framework" = "two-tier framework" L12, L25, L90, L96; "The Reserve
  Bank's Proportionality Framework under the Deposit Takers Act 2023" L25-28, L88; "Retail
  Payment System Act" L59.
- Positions (verbatim, with line):
  - Stance, L40: "TSB's concern is not necessarily that commercial credit cards are being
    regulated. It is that the proposed calibration may unintentionally weaken the very
    competition the Commission is required to promote." L12: "TSB welcomes the Commission's
    recognition that commercial credit cards warrant separate treatment from personal cards".
  - Premium, L43: "the Draft Decision does not demonstrate why those factors justify only a
    20-basis point premium." L23: "The Draft Decision clearly establishes why commercial cards
    warrant a premium, but it does not explain why the proposed premium is appropriate."
  - Tiering, L96: "Recommendation: The Commission should adopt a two-tier commercial interchange
    framework that provides proportionately different treatment for smaller issuers using
    objective eligibility criteria appropriate to the New Zealand payments market, such as
    issuer size, market share or another objective measure as determined by the Commission."
    L90: "The Commission could determine the most appropriate eligibility criteria".
  - Own viability, L22: "At the proposed cap settings, our commercial card proposition is likely
    to become economically unsustainable."
  - Cap level, alternative premium figure, implementation period: none stated.
- Quantitative statements: L10 "served customers for more than 175 years"; L43 "20-basis point
  premium" (the Draft Decision's). No other figures (no percentages, dollars or dates of rules).
- Restates / disputes the draft decision: L43 "The Commission accepts that commercial products
  involve higher fraud costs, higher administrative costs, higher servicing costs, and distinct
  merchant benefits"; L53 "The Commission suggests these additional capabilities should be
  funded through fees or interest rather than interchange"; L69 "The Commission relies heavily
  on Australia as its principal comparator yet departs materially from Australia's regulatory
  settings in key respects. Australia has retained higher commercial interchange settings than
  those proposed for New Zealand while simultaneously considering broader reforms ...
  including the treatment of American Express and merchant surcharging"; L69 "the New Zealand
  proposal regulates only Mastercard and Visa commercial interchange"; L53, L74 American
  Express "excluded from the proposed caps". No paragraph or question numbers.
- Lists: cover-letter highlights, 2 bullets L16-18; Appendix 1 headings 1-9 (L36, L41, L47, L57,
  L67, L72, L78, L82, L97); the Recommendation bullet is the last bullet of section 8, after the
  page-5 break (L96).
- Events and dates: submission 20 July 2026 (L4); Deposit Takers Act 2023 (L28, L88). No dated
  rule changes.
- International references: L101 "In the United States, debit interchange regulation exempts
  issuers below a defined asset threshold" (no threshold figure); L103 "the Reserve Bank of
  Australia's recent review of interchange regulation considered evidence that lower
  interchange caps would disproportionately affect smaller issuers" (no date/figure).
- Hedged claims:
  - L18 "This risks reducing competition, customer choice and long-term investment".
  - L20 "the proposed calibration risks reducing effective competition".
  - L22 "is likely to become economically unsustainable" / "smaller domestic issuers may be
    forced to withdraw commercial card products altogether" - "likely", "may".
  - L40 "may unintentionally weaken"; L59 "may inadvertently weaken competition".
  - L61 "For larger issuers, lower interchange may reduce returns, but commercial card products
    are likely to remain viable ... For smaller issuers, however, lower interchange may
    determine whether those products remain economically viable at all."
  - L71 "is likely to have a disproportionate impact on smaller domestic issuers and may reduce,
    rather than enhance, effective competition".
  - L74 "TSB would be captured by the proposed framework despite having a smaller market
    presence than American Express" - firm comparison, no figures.
  - L92 "would have only a limited impact on overall merchant costs" - asserted, unquantified.
- Coverage: FULL. Lines 1-109 read sequentially. Nothing unread.

## D16 (Doc 14) - Westpac submission

- Source: `text/D16.txt`, 101 lines. "Page 2".."Page 6" markers L12, L34, L52, L70, L87; numbered
  paragraphs 1.1-3.23; footnotes 1-3 at L50, L68, L85.
- Written or submitted by: Westpac New Zealand Limited ("Westpac"), L4-5, L14; "Classification:
  PROTECTED" (L3, L98). No signatory ("contact ... provided separately" L16). Organisations it
  only names: Commerce Commission, American Express, Visa, Mastercard, RBA, MWE Consulting.
- Type, date, edition: submission, "21 July 2026" (L10) - the latest-dated submission in this
  part.
- Entities and aliases: "Commerce Commission (Commission)", "Draft Decision" L14; "three-party
  scheme"/"four-party" L49, L58; "free EFTPOS" L31, L74; "RBA" L72.
- Positions (verbatim, with line):
  - Stance: no sentence supporting or opposing the caps outright. L19 "Westpac supports payments
    regulation that promotes innovation, effective competition and a level playing field"; L24
    "Westpac is concerned the Draft Decision does not:" followed by (a)-(e) L26-32; L47 "the
    cost-benefit analysis supporting the Draft Decision is not sufficiently established".
  - Premium, L60 (3.10): "A higher commercial card premium is therefore warranted to reflect the
    New Zealand context"; L65 (3.12): "A higher premium over commercial card interchange is
    therefore warranted to reflect New Zealand's smaller scale and higher relative
    cost-to-serve." No figure proposed.
  - Implementation, L91 (3.21): "Westpac considers that a minimum six-month implementation
    period, with changes taking effect from 1 March 2027 at the earliest, would better support
    orderly delivery". L90: "December implementation carries operational risks". L93 (3.22):
    "Implementation over the December to February period would introduce additional operational
    complexity." L95 (3.23): "any interchange changes should align with a first-of-month
    effective date."
  - Pass-through, L37 (3.1): "While Westpac will pass on these reductions to merchants, the
    extent of passthrough across the system has not been adequately articulated by the
    Commission."
  - Surcharging, L45 (3.4): "Further interchange reductions alone are therefore unlikely to
    deliver the intended benefits without a more direct regulatory focus on surcharging
    behaviour and transparency."
  - Whole-of-system, L74 (3.15), L78 (3.17), L88 (3.20).
- Quantitative statements:
  - L39 (3.2; NZ; attributed to the Commission): "the Commission's cost-benefit analysis, which
    relies on an expected annual reduction of approximately $40 million, depends on an
    unsubstantiated assumption that this reduction will be passed on fully to merchants."
  - L43 (3.4; NZ; attributed to the Commission; footnote 1, L50: "Retail Payment System (Ban on
    Merchant Surcharges) Amendment Bill | New Zealand Legislation"): "The Commerce Commission
    estimates that that New Zealand consumers continue to pay ~$150 million per annum in
    surcharges, with $45-65 million estimated to be excessive and above underlying merchant
    costs." (printed "$45–65 million" with an en dash; "that that" as printed.)
  - L56 (3.8; Australia vs NZ commercial card market; footnote 2, L68): "The Australian
    commercial card market is significantly larger than the New Zealand market (AUD119 billion
    annual spend versus NZD8.2 billion spend)". Footnote 2 as printed: "Source: MWE Consulting
    January and February 2027 reports respectively." (The year printed is 2027, later than the
    submission's own date of 21 July 2026; recorded as printed, unresolved.)
  - L74 (3.15; NZ): "EFTPOS continues to support around 20 percent of in-store card payments and
    is currently available to merchants and consumers without direct transaction fees."
  - L91: "minimum six-month"; "1 March 2027".
- Restates / disputes the draft decision:
  - L37 (3.1): "The Commission acknowledges at paragraph 4.5 of the Draft Decision that there is
    uncertainty about the extent to which the full benefits of interchange reductions are passed
    through to merchants due to the complexity of the cards eco-system and proposes to assess
    pass-through only after implementation."
  - L39: "expected annual reduction of approximately $40 million".
  - L43 direct quotation: "current surcharging practices are often imperfect and may not
    accurately reflect underlying acceptance costs".
  - L49: "Interchange caps would apply to Visa and Mastercard commercial credit transactions,
    while American Express remains outside scope as a three-party scheme."
  - L58 (3.9): "The Commission's approach relies on an Australian-based premium".
  - L72 (3.14): "in contrast to the RBA's approach, which has been informed by issuer cost
    analysis, the Commission has not published substantive evidence or analysis to support its
    assertions regarding issuer costs in the New Zealand market."
  - L78 (3.17): "The Draft Decision appears to assess commercial card interchange primarily by
    reference to expected reductions in merchant acceptance costs, ignoring all card holder
    benefits."
  - No cap percentages, premium figure or question numbers are quoted.
- Lists: concerns (a)-(e) L26-32; five headed themes in section 3 (L36, L49, L62, L74, L78) plus
  implementation (L90).
- Events and dates: submission 21 July 2026 (L10); earliest requested effective date 1 March
  2027 (L91); footnote 3 (L85) names a Westpac cross-submission file dated "13-May-2025" "(para
  2.3)"; "MWE Consulting January and February 2027 reports" (L68, as printed); "the end of
  support for mag-stripe cards" (L76, no date).
- Hedged claims:
  - L21 "there is uncertainty as to whether further changes will achieve these results".
  - L28 "the competitive distortion that may arise from American Express remaining outside".
  - L45 "are therefore unlikely to deliver the intended benefits without ..." - "unlikely",
    conditional on no surcharging focus.
  - L49 "The current framework risks distorting competition".
  - L54-55 "this is likely to encourage commercial cardholders to favour products with richer
    benefits ... spend may shift toward American Express. A migration ... would be likely to
    increase merchant acceptance costs".
  - L67 "smaller issuers are likely to be affected disproportionately"; "That could reduce
    product viability".
  - L76 "The Draft Decision risks weakening that cross-subsidy ... may face higher overall
    payment costs" (the heading at L74 states it firmly: "will become unsustainable").
  - L78 "The Draft Decision appears to assess" - "appears".
  - L82 "issuers may need to recover costs through higher cardholder fees".
  - L37 "Westpac will pass on these reductions to merchants" - firm commitment about itself.
- Rounded prose beside exact figures: "~$150 million", "approximately $40 million", "around 20
  percent".
- Coverage: FULL. Lines 1-101 read sequentially. Nothing unread.

## Shared ground (navigation only; the 14 documents of this part)

Locations only. Where the same thing is stated differently, both statements are listed without
choosing between them. D06 and D13 were not read; "keyword hit" lines at the end are raw search
matches in those two files, not read in context.

### Submission dates and authors (side by side)

- D10 Paymark 30 June 2026 (L3) | D05 FSF 13 July 2026 (L3) | D01 ANZ 16 July 2026 (L9) | D08
  Mastercard 16 July 2026 (L6) | D03 BNZ 17 July 2026 (L6) | D04 Citi 17th July 2026 (L13) | D07
  Kiwibank 17 July 2026 (L9) | D02 ASB "[20 July] 2026" (L3) | D11 Restaurant Association 20
  July 2026 (L3) | D12 Retail NZ 20 July 2026 (L8) | D14 Revolut 20 July 2026 (L14) | D15 TSB 20
  July 2026 (L4) | D16 Westpac 21 July 2026 (L10).
- D09 survey: open 4 June to 29 June 2026 (L22); published 23 July 2026 (L4) - after every
  submission date above.
- Draft decision date as stated: "dated 4 June 2026" D01 L12, D08 L9; "published 4 June 2026"
  D10 L6. Same day the D09 survey opened (D09 L22).
- Author types (as self-described): banks/issuers ANZ, ASB, BNZ, Citi, Kiwibank, TSB, Westpac;
  card scheme Mastercard; fintech issuer Revolut; payments network/processor Paymark; industry
  bodies FSF (specialist lenders), Restaurant Association, Retail NZ; regulator's own survey D09.

### Stance on the caps (side by side)

- Supports capping: Paymark D10 L6, L22, L40; Restaurant Association D11 L12, L24, L79; Retail NZ
  D12 L25, L61; BNZ "broadly supportive ... although ... the currently proposed level is too
  low" D03 L18, L62.
- Wants lower caps / no premium: Restaurant Association D11 L27, L32, L36, L41; Retail NZ D12
  L63, L65, L101.
- Says proposed caps/premium too low (wants higher): ASB D02 L22, L32; BNZ D03 L18, L47; Citi D04
  L54, L136; Kiwibank D07 L18, L37, L67; Mastercard D08 L80; TSB D15 L43; Westpac D16 L60, L65.
- Says do not proceed / defer / reconsider: Kiwibank D07 L16, L25 ("should not proceed ...
  until"); Mastercard D08 L134 ("Defer the Final Decision"); Citi D04 L136 ("Continue to exclude
  Commercial Card interchange from regulatory cap, or ..."); Revolut D14 L17, L157 ("reconsider
  ... entirely").
- "Accepting of the direction" but concerned about competition: FSF D05 L10-11.
- No outright support/oppose sentence: ANZ D01 L20 (supports the intention; objects to timing
  and Limiting Mechanism); Westpac D16 L19-32; TSB D15 L40.

### Implementation period: the Commission's proposal as restated, and each request

- Proposal restated: "2- to 3-month implementation period from the date of the Commission's
  final decision" D01 L23; "two to three-month" D02 L124 (also L37, L125); "two-to-three month"
  D04 L127, L129; "two to three month" D07 L84; D08 L228, L234, L238; "two-to-three-month" D11
  L59; "2-3 month" D12 L106.
- Requests:
  - ANZ D01 L29: BER cycle "April 2027 release. Failing that ... a minimum of 6 months."
  - ASB D02 L48, L137: "no earlier than 8 months from the announcement date"; schemes to confirm
    "no later than 2 months from announcement date"; "6 months" for acquirers.
  - BNZ D03 L23, L37: "minimum six-month ... between the final decision and commencement"; avoid
    "a pre-Christmas deployment" L39.
  - Citi D04 L133, L142: "minimum implementation period of twelve months, mapped to four major
    quarterly technology releases".
  - Kiwibank D07 L84: "at least six months from the final decision"; "some implementation
    activities cannot occur over December and January".
  - Mastercard D08 L123, L144, L236, L248: "minimum of nine months ... for domestic rate changes
    and twelve months for cross-border changes, from the date of final announcement".
  - Westpac D16 L91: "minimum six-month implementation period, with changes taking effect from 1
    March 2027 at the earliest"; first-of-month L95; avoid December to February L93.
  - Restaurant Association D11 L59: proposed period "appears reasonable, provided ...".
  - Retail NZ D12 L106: "supports the 2-3 month implementation period".
  - No implementation period stated: FSF D05; Paymark D10 (only "clear implementation
    timeframes" for an Honour All Cards change, L88); Revolut D14; TSB D15.
- Start point wording differs: "final decision" (D01 L23, D03 L23/L37, D07 L84); "announcement
  date" (D02 L48); "date of final announcement" (D08 L123).
- Earlier changes' implementation time, stated differently: "the 4-month implementation period
  for the changes to consumer rates" D01 L23; "the implementation period for the decisions in
  relation to domestic personal cards" equated with "A six month implementation period ... with
  some additional time" D07 L84; "allowing us 3 months" after scheme details for "the domestic
  rate changes announced in July 2025" D02 L35; "the July 2025 domestic changes (effective 1
  December 2025)" D08 L234; "around a six-month process from the point rates are published" (BNZ
  alternative-pricing remodelling) D03 L37.
- Scheme release-cycle alignment: D01 L29 (BER, April 2027); D08 L128, L144, L252; D04 L133
  (quarterly technology releases).

### The Commission's premium, as restated (20 vs 10 basis points) and counter-proposals

- Total premium over personal credit: "20bps"/"20-bps" D02 L24, L30, L88; "20 basis point
  premium to consumer interchange" D04 L54; "A 0.20% premium" D07 L67; "20-basis point
  differential" D08 L16, L62; "0.20 percentage-point premium above the equivalent domestic
  personal credit card caps" D11 L28; "the 0.20% premium" D12 L65; "20-basis point premium" D15
  L43.
- "10 basis point" wording: D02 L104 (question 3.1 quoted: "additional 10 basis-point premium
  ... above domestic personal credit card interchange to reflect the incremental issuer costs
  and merchant benefits"); D04 L84 ("additional 10 basis point premium above domestic personal
  credit card interchange to promote stable and sustainable market outcomes and mitigate the
  risk of market disruption"), L86, L90; D08 L17, L70, L72, L76-80, L140, L172, L192, and the two
  quoted question bullets L168 (stability / market disruption) and L186 (issuer costs and
  merchant benefits).
- The split printed in one place: D11 L28 "The Commission attributes 0.10 percentage points to a
  combination of additional issuer costs and merchant benefits" and L31 "The remaining 0.10
  percentage-point premium is intended to promote market stability and align the proposed rates
  with the Australian benchmark".
- Mastercard describes the stability/Amex 10 bp as "a mitigant" for the Amex advantage (D08 L17,
  L76-78) and the cost/benefit 10 bp as "the 10-basis point cost-and-benefit differential" (D08
  L192).
- Counter-proposals: ASB "50 bps over the existing interchange caps for personal credit cards
  is at least the starting point" D02 L32 and a flat "1.1%" cap D02 L22, L110; Mastercard
  differential "in the order of 40 basis points" (Amex vs Visa/Mastercard commercial MSF gap)
  D08 L80, L140, L172; Citi "materially higher ... differential" D04 L136; Westpac "higher
  premium" D16 L60, L65; Kiwibank "0.20% premium is insufficient" D07 L67; TSB two-tier issuer
  framework D15 L96; Retail NZ same level as personal cards D12 L65, L101; Restaurant
  Association align with personal caps or evidence-limited premium D11 L32.
- Australia's premium: "50-bps interchange premium for commercial credit cards (versus
  consumer) ... codified by the Reserve Bank of Australia's latest regulations" D02 L25, L88
  (only in D02).

### Cap levels and interchange rates as restated

- Proposed caps printed in full only in D11: domestic "0.50% for in-person transactions and
  0.90% for online transactions" L27; foreign-issued "0.70% for in-person ... and 1.50% for
  online" L36.
- In-person vs online split discussed without figures: D04 L104, L140; D02 L20, L110.
- Implied weighted average: "assumed 78bps implied weighted average in New Zealand" D04 L104;
  "the Commission's estimate of 0.78%" D07 L54; Kiwibank's own "approximately 0.63%" D07 L54;
  "broad alignment with Australian outcomes on a weighted-average basis" D08 L34.
- Below-cap / strategic rates: "Government interchange fees are 0.20%" D07 L52; "Strategic
  Merchant" and "Industry Program" rates D02 L110 (values redacted); D08 L115, L212; D01 L36;
  D12 L20 (major retailers' negotiated rates).
- Australia's commercial cap: "initial 80 bps cap in July 2017" D02 L62; "80-bps" D02 L73, L77,
  L96; "The RBA retained the 0.80 per cent cap on commercial credit in March 2026" D08 L82,
  L157; "Australia has retained higher commercial interchange settings than those proposed for
  New Zealand" D15 L69; "Setting New Zealand caps below the Australian floor" D08 L92, L169.
- Note the three different uses of "0.20%": Government interchange rate (D07 L52), the premium
  (D07 L67, D12 L65, D11 L28).

### The Commission's dollar estimates as restated

- Interchange paid on Mastercard/Visa commercial credit: "approximately $125 million each year"
  D10 L26; "approximately $125 million in interchange fees" D11 L17.
- Expected saving: "approximately $40 million annually" D10 L26; "around $40 million" D11 L17;
  "expected annual reduction of approximately $40 million" D16 L39.
- MSF on commercial credit "$170 million annually" and "approximately $1 billion per year
  overall to accept Visa and Mastercard payments": D11 L17 only.
- Surcharges: "~$150 million per annum in surcharges, with $45-65 million estimated to be
  excessive" D16 L43; "approximately $45-65 million annually in 'excessive surcharges'" D14
  L105. Different figure, different source: Mastercard's own estimate of excessive surcharging
  "more than $90 million annually" (September 2024 submission) D08 L46, L57.
- A different "170 million": UK "at least £170 million extra per year" scheme fees D10 L44.

### Limiting mechanism

- Remove: ANZ D01 L42; Mastercard D08 L110, L142, L223. Alternative weighted-average benchmark:
  D08 L120, L142, L225. Retain as later deterrent: D01 L42-44.
- Support: Restaurant Association D11 L44 (and extend to foreign-issued); Retail NZ D12 L104
  ("date to be set at 1 December 2025").
- Mentions only: Kiwibank D07 L52, L57; Citi D04 L104; ASB D02 L122-124 (defers to schemes).
- Reference date "1 December 2025": D08 L109, L112, L218, L228; D12 L104. Mechanism wording
  quoted: "capping fees at the lower of the applicable cap or the published rate as at 1
  December 2025" D08 L218.
- Domestic-only scope (question 6): D02 L122; D08 L214; D11 L44.
- Network Standard drafting: D01 L65; D03 L41-43 (clause 2 commencement); D08 L114 (clause 8.4).

### New Zealand regulatory timeline as stated across documents

- 2022 / November 2022 initial pricing standard: D02 L98, L108; D07 L29; D08 L37, L39, L41.
- July 2025 decision (17 July 2025 Final Decision): D02 L35, L124; D07 L85; D08 L14, L28, L41,
  L128, L234; RBA consultation also "July 2025" D12 L65 (a different, Australian document).
- December 2025 / 1 December 2025 personal credit reductions: D03 L37 ("repricing in December
  2025"); D07 L29 ("late 2025"), L34 ("in 2025"); D08 L32, L234; D12 L35, L104.
- May 2026 foreign-issued / cross-border caps: D03 L37 ("May 2026" repricing); D08 L32, L234.
- "two previous rounds of interchange fee regulation" D11 L55; "the 2022 round or the July 2025
  round" D08 L37; "this may be the third recent repricing for some merchants" D03 L37.
- Surcharge-ban bill: "passed first reading in September 2025 but has not progressed to
  enactment" D08 L47; cited as a footnote source D16 L50.
- Personal banking market study: D07 L75; D08 L17, L104 ("all 14 recommendations"), L116, L208.
- Commissioner Chapple: D08 L120, L225 (8 July discussion); D14 L62 (quotation).
- Acts named: Retail Payment System Act 2022 D03 L62, D08 L109, D10 L67, D15 L59 (D14 prints
  "Retail Payment Systems Act" L47); Credit Contracts and Consumer Finance Act D11 L30; Deposit
  Takers Act 2023 D15 L28, L88; Official Information Act D01 L18, D02 L50, D12 L111.

### Draft-decision references the submissions give

- Paragraph/table/page: para 2.9 D12 L28; para 2.11.1 D12 L58; paras 2.11.3-2.11.6 D12 L48;
  Table 2.1 D12 L69; "section 2.36" D12 L72; para 2.37 D07 L63; para 3.7.1 D12 L82; para 4.5
  D16 L37; "Draft Decision, page 16" D08 L43.
- Targeted questions: all nine quoted D08 L147-246; ASB numbering 2.1, 2.2, 2.3, 3.1, 3.2, 4.1,
  4.2, 6, 8 & 9 (D02 L60-124); Citi Questions 2, 3, 4, 9 (D04 L70, L88, L105, L127).
- Direct quotations of the Draft Decision: D07 L85 (implementation "strikes an appropriate
  balance"); D07 L80 ("enhance allocative, productive and dynamic efficiency"); D16 L43
  ("current surcharging practices are often imperfect ...").
- Fraud: "the 1 - 2 bps quoted in the consultation paper" D02 L114; "differences in fraud costs
  as minor" D11 L28; "higher fraud rates for commercial credit cards" (para 3.7.1) D12 L82;
  "accepts that fraud and administrative costs are higher ... but assesses the differential
  conservatively" D08 L198; 12-month loss data request D07 L68; D15 L43.
- Trade accounts as a merchant benefit: D11 L28; D12 L69-70 (disagrees); D08 L66, L190-192;
  D16 L80; survey evidence D09 slides 11, 15 (Q5, Q7).
- Three-step methodology: D07 L37-66; D04 L70, L88; D08 L158, L184; D02 L104.
- Benchmarks: Australia as benchmark D04 L74, D07 L63, D15 L69, D16 L58; UK/EU excluded as
  benchmarks D07 L42-43, D08 L93, L171.

### Surcharging: every stated figure and position

- ANZ D01 L50 (subset of ANZ merchants on terminals): surcharging "from 8% in 2022 to 26% in
  2026"; L52 average surcharge "2.24% to 2.02%"; average MSF "1.35% ... to 0.91%"; terminals
  surcharging above MSF "91% ... to approximately 94%".
- Mastercard D08 L41-45 (RFI Global via Newsroom): merchants applying surcharges "20 per cent
  in 2016, to 49 per cent in 2022 ..., to 57 per cent in 2024"; "up to 7.5 per cent" (Kantar
  Public) L45; "more than $90 million annually" L46.
- Kiwibank D07 L27-32 (unnamed large terminal provider; no numbers): share of transactions
  surcharged rose after 2022 and after late 2025; average surcharge "has not changed
  significantly since 2022"; terminals with surcharging "record high in May 2026".
- Retail NZ D12 L38: "66% ... do not currently surcharge"; L31 "58%" want payment-type-specific
  surcharging.
- Revolut D14 L108 (PSE, June 2026, SMEs): "44%" surcharge Visa and Mastercard, "1.50% being the
  most frequent rate", "56% already absorb"; Amex L86-88: "52%" accept, "28%" say MSF dearer,
  "54%" pass on, "average surcharge of 2.16%"; L110-112 "67%"/"33%", "23%", "71%"/"29%"; L137
  B2B "typical surcharges top out at 2.50%"; L105 IRD "1.42%", Auckland Council "1.75%".
- Westpac D16 L43: "~$150 million per annum", "$45-65 million".
- D09: Q10 call-out "Inability to surcharge differently (1)" L214; Q23 theme "Surcharging and
  cost recovery" 8 (L377-378, by order).
- Positions: prohibit/regulate surcharging - ANZ D01 L48; address surcharging first/alongside -
  Citi D04 L82, L138; Mastercard D08 L136; Westpac D16 L45; keep merchants' right to surcharge -
  Revolut D14 L58, L103, L159; Restaurant Association D11 L76 (separate consultation).
- Different populations: merchants (D08, D14, D12), terminals (D01 L52, D07 L32), transactions
  (D07 L29), a subset of one bank's merchants (D01 L50).

### Australia: rules, dates and scale comparisons

- RBA 2003 regulation: "initial regulation in 2003" D02 L84; "RBA ... 2003 reforms", "more than
  two decades" D08 L82, L155.
- July 2017 80 bps cap D02 L62, L77; cap retained March 2026 D08 L82, L157.
- RBA Conclusions Paper: "31 March 2026" D02 L26-27; "March 2026" D08 L82-83, L160. RBA
  consultation paper: D02 L79; "consultation from July 2025" D12 L65. RBA Issues Paper "25 June
  2026" D01 L62; "further review in mid-2026" D08 L86, L157.
- October 2026 in Australia: "empower schemes to reintroduce rules preventing card surcharging
  from October 2026" D01 L48; "the October 2026 caps on consumer credit cards go live" D02 L86.
- 2007 RBA honour-all-issuers/products distinction D10 L61.
- Amex in Australia: "~50% commercial card market share, up from 18.2% in July 2017" D02 L62;
  RBA quotation "American Express is the largest issuer of commercial cards" D08 L82 and
  paraphrase "one of the largest issuers" D08 L155; "has grown its market share in Australia
  under current interchange caps" D07 L65.
- Cards on issue: commercial "dropped 41.8%" since July 2017 D02 L62; all credit cards "fallen
  by 27.1% since 2017" D02 L90.
- Scale, four different measures: GDP "7x", population "5x" D02 L94; population "approximately
  5.3 million" vs "approximately 27.2 million", GDP "approximately USD 260 billion" vs
  "approximately USD 1.76 trillion" D04 L45; commercial card spend "around 4.3 per cent of
  Australian GDP" vs "approximately 1.9 per cent of New Zealand GDP" D08 L92, L169; "AUD119
  billion annual spend versus NZD8.2 billion spend" D16 L56.
- MWE as source: "MWE New Zealand Payment Cards Report" D02 L102; "MWE Consulting data (2026)"
  D08 L99, L173; "MWE Consulting January and February 2027 reports" D16 L68.
- Issuer cost evidence: RBA "Issuer Cost Study" quotation D12 L65; "RBA's approach, which has
  been informed by issuer cost analysis" D16 L72; RBA review and smaller issuers D15 L103.
- Australian neobanks D08 L102-103; Airwallex D02 L94; Mandala (four major banks' share 77 to
  64 per cent, 2018-2024; MSF down 12 per cent) D08 L50.

### UK, EU and US references

- UK/EU do not cap commercial card interchange: D07 L42-43; D08 L93, L171; D14 L37.
- EU Interchange Fee Regulation: "Regulation (EU) 2015/751" D08 L177; "Europe's 2015
  Interchange Fee Regulation" D14 L97. EC studies as cited differ: "European Commission (2020)
  "Study on the application of the Interchange Fee Regulation Final"" with a Copenhagen
  Economics URL, and the Article 17 report "29 June 2020" D08 L175-178; "The 2025 European
  Commission study by Copenhagen Economics and EY" D14 L97.
- EU 2016 Honour All Cards restriction D10 L62; EU scheme-fee probe 26 May 2025 D10 L53.
- UK Payment Systems Regulator scheme-fee finding ("at least 25% since 2017", "at least £170
  million") D10 L44, L53.
- Oxera 2019 European invoicing cost "4.3 per cent ... rising to 5.6 per cent" D08 L66, L192.
- US: Durbin Amendment survey (77 / 22 / 1 per cent) D08 L49; debit interchange small-issuer
  exemption D15 L101; Visa/Mastercard "profit margin ... in the vicinity of 50%" D12 L87; "NY
  Fed in 2026" D14 L75.
- Korefusion (Asia Pacific; commissioned by Visa): "106 basis points" bad-debt reduction D04
  L62-63; "approximately 15 days of accelerated payment" D04 L96.

### American Express / three-party networks

- Named as outside the regulation and a competitive concern: D01 L58; D02 L62, L98; D04
  L106-112; D07 L65; D08 L17, L76-89, L140; D14 L43-47, L82-92, L121; D15 L18, L53, L74; D16
  L49-55; D12 L66, L102 (include all card companies). BNZ refers to "comparable payment
  networks"/"other payment systems" without naming Amex D03 L27-30.
- Amex in NZ, stated facts: "doubled their market share in New Zealand since ... November
  2022" D02 L98; "may currently represent a relatively small share ... its position within
  commercial payments is growing" D04 L110; "TSB ... having a smaller market presence than
  American Express" D15 L74; PSE figures D14 L86-88; D09 Q9 (58 of 92 accept Amex, L199), Q11
  (24 of 58 say it mainly replaces Mastercard/Visa, L201), Q10 (High cost 24 of 34, L223-224).
- Designation / universal application asked for: BNZ D03 L30; Mastercard D08 L140; Revolut D14
  L163-164; Retail NZ D12 L102; ANZ D01 L58. Draft Decision's monitoring approach restated D08
  L88-89; D11 L57.
- American Express appears as a listed FSF member D05 L35 (a member list entry, not a comment
  on Amex).
- BNPL: D01 L58, L62; D09 Q5 (3 of 92), Q12 (15 of 92 accept); AfterPay/Zip/Humm/Latitude as
  FSF members D05 L34, L56, L62.

### Scheme fees and other non-interchange costs

- D10 L44 (UK), L48-51 (Visa Fleet 2.0); D12 L108 (monitor non-interchange MSF); D14 L31, L97;
  D15 L80; D16 L41 ("acquirer scheme fees and costs have continued to rise"); D01 L49; D11 L57.
- Pass-through doubts: D01 L48-53; D04 L56, L81-82; D07 L25; D08 L36-39; D12 L35-36 (46.3% saw
  no difference); D14 L95-101; D16 L37-47. Westpac's own commitment to pass on D16 L37.

### Small issuers, market scale and exit

- D03 L59; D04 L45-48, L65, L116-118; D05 L10 (member "pulled out"); D07 L20, L75-78; D08 L17,
  L104, L208; D14 L52-56; D15 L16-22, L61, L96; D16 L67-71. EFTPOS cross-subsidy D16 L74-76;
  EFTPOS decline D12 L54, D14 L150; Paymark's EFTPOS history D10 L14.

### Survey evidence by source (who ran which survey)

- Commerce Commission merchant survey, June 2026, 94 completed responses: D09 (whole document).
  No submission in this part cites D09 (it was published 23 July 2026, after all of them).
- Restaurant Association: August 2024 retail-payments survey D11 L14; November 2025 member poll
  D11 L66 ("indicative only" L68).
- Retail NZ member survey (undated, base not printed): D12 L31, L35-36, L38, L43, L63.
- Revolut/PSE merchant research June 2026: D14 L64, L84-88, L99-101, L106-112, L137;
  Kiwibank/Talbot Mills January 2026 (800 business leaders) D14 L75.
- Kantar Public surveys for the Commission D08 L45, L57; Richmond Fed survey D08 L49.
- Topics that recur between D09 and submissions (locations only): share of sales on commercial
  cards D09 slide 13; hospitality/accommodation weighting of respondents D09 slide 7 vs D11
  (hospitality body); virtual cards / online travel platforms D09 slides 24-30 vs D14 L66,
  L116-123; cardholder benefits and willingness to pay D09 slides 34-39 vs D11 L66, D12 L77;
  interest-free period D09 slide 34 vs D11 L61, L66, D14 L78, D16 L82.

### Card-payment share figures (different measures)

- "70.5% in the June 2026 Stats NZ data" of electronic card transactions on Mastercard/Visa
  credit rails, vs "45%" in 2016 D12 L39; "3 in 4 payments (74%) now use Mastercard and Visa,
  with only 26% ... EFTPOS, open banking payments and American Express" D12 L54; "EFTPOS
  continues to support around 20 percent of in-store card payments" D16 L74; "more than 98%"
  accept Visa/Mastercard credit, "96%" contactless D11 L14.

### Keyword hits in D06 and D13 (raw search matches only; those documents were NOT read here)

- "$125 million": D13 L66, L132, L272. "$170 million": D13 L131. "$40 million": D13 L105, L324,
  L932, L936. "$50 million" (a figure none of the 14 documents print): D13 L104, L105, L175,
  L324, L936.
- Caps "0.50%"/"0.90%"/"0.70%"/"1.50%": D13 L99-103, L170-174, L570-579, L586, L784, L1205-1206.
  "0.78%": D13 L572, L605, L606. "0.80%": D13 L570, L571, L605, L612, L674; D06 L662. "0.30%":
  D13 L588, L596, L1199.
- "0.20 percentage": D13 L88; "0.10 percentage": D13 L377; "10 basis": D13 L1153, L1156; "50
  basis": D06 L214, L223, L261; "106 basis": D06 L221.
- "1 December 2025": D13 L107, L114, L183, L552, L564, L893, L906, L1172; D06 L531. "April
  2027": D13 L802. "two to three-month"/"two-to-three-month": D13 L921, L1177, L1183. "17 July
  2025": D13 L19 and many more; D06 L663, L754. "4 June 2026": D13 L6. "29 June": D13 L1129.
- Paragraph anchors: "2.11.1".."2.11.6" D13 L287-312; "Table 2.1" D13 L503; "3.7.1" D13 L591;
  "Market Study" D13 L627. "merchant survey": D06 L291.
- No keyword hit in D06 or D13 for: "$45", "65 million", "$150", "$90 m", "excessive surcharg"
  (case-insensitive). This records the search result only; it does not establish that D13
  lacks those facts in other wording.

## Coverage ledger and gaps (this part)

| Doc | Lines in file | Lines read | Unread |
| --- | --- | --- | --- |
| D01 | 67 | 1-67 | none |
| D02 | 141 | 1-141 | none |
| D03 | 72 | 1-72 | none |
| D04 | 161 | 1-161 | none |
| D05 | 101 | 1-101 | none |
| D07 | 87 | 1-87 | none |
| D08 | 254 | 1-254 | none |
| D09 | 390 | 1-390 | none |
| D10 | 101 | 1-101 | none |
| D11 | 89 | 1-89 | none |
| D12 | 118 | 1-118 | none |
| D14 | 206 | 1-206 | none |
| D15 | 109 | 1-109 | none |
| D16 | 101 | 1-101 | none |

- Not mapped in this part (by instruction): D06, D13. Only the keyword searches listed above
  touched them.
- Missing or unresolved source content (not unread text):
  - D02: redacted ASB values (table ASB column L68-71; L35, L76, L110, L114, L118).
  - D05: Appendix A member list interleaved/garbled (L34-64); Appendix B label/value alignment
    and lost characters ("$12 0B", "$10.26", "$1276", L71-99).
  - D07: redacted terminal-provider name L27 and loss example after L68.
  - D08: Figures 1 and 2 are captions only (L51-53, L82); footnotes 7 and 14 have no text;
    Figure 2 caption (Australian, RBA 2022) vs the prose it is cited for (New Zealand,
    Commission's data) L80-82.
  - D09: Q13 option data absent (L227-232); all size/sector breakdown charts are unlabelled
    number runs with absent cells; slide 30 "94% 19%" (L286); slide 39 no 100+ values (L362).
  - D14: Annexure 1 diagram (L171-204).
  - D16: footnote 2 year "2027" (L68) as printed.
- Extraction spot-checks: originals are the same plain-text captures (`docs/*.txt`, hashes equal
  to `text/manifest.json` per `notes/intake.json`); no PDF/page image exists, so page-count and
  visual table checks are not applicable. Internal checks done on the text: D09 slide 7 run has
  ten values for ten labels; D09 Q6 note counts (29/18/36/9, L134) sit beside chart percentages
  (32/20/39/10, L132); D08 footnote markers 1-18 traced to text except 7 and 14.
- Next mapping chunk for the bundle: D06 and D13 (owned by the other mapper / the caller); then
  re-check this part's "restated draft decision" entries against D13's own wording.
