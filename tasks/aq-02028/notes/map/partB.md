# aq-02028 - document map, part B (D11, D12, D15, D17, D19)

Navigation only (facts and locations, not reasoning routes). Every location is `Dnn Lx` = line x of
`text/Dnn.txt`. Mapper: bundle-mapper group B, 2026-10-08. The caller merges this part into
`notes/doc-map.md`.

## Part B header

- Assigned scope: full sequential read of D11, D12, D15, D17 and D19, plus a whole-bundle Grep (D01-D20)
  for repeats of key figures and entities (see the final section).
- Reuse binding (manifest sha256, `text/manifest.json`): D11 `728999cc8e985eb29a06e759ad4d568f0834354b6c03a4025b5f6f7211b9455e`;
  D12 `92d27314e1b50fe8eaddb401187afd3c4c9467f2e24c6405cd091f6ba164fa92`;
  D15 `28ccb9082b3f73fc057e6e164c5dd95d0ed17320b3b83338d433e6406eda3ef8`;
  D17 `3afe656b69e1e323f6435fc573154546e6a4c11cf3247a6e17b479f8b61a83a5`;
  D19 `c86be22b86582074612dbb65b8a8c2151f3c760f303bb84e3ec4888d3a66de18`. `notes/intake.json` lists all five
  as `incomplete: false`, `gap_characters: 0`, `matches_capture: true`.
- Extraction: plain-text sources (no PDF, `pages: null`). The caller verified that text/ equals the
  NFKC-normalised source. None of the normalised characters reported (ellipses) is in these five documents.
  Line offset: `text/` line N = `docs/` line N-2 (2-line `# Dnn | source` header). Spot-checked: D11 L38/L39/L72 = docs L36/L37/L70;
  D12 L40/L60/L108 = docs L38/L58/L106; D15 L32/L119/L138 = docs L30/L117/L136; D17 L42/L109/L136 = docs L40/L107/L134;
  D19 L97/L304/L481/L694 = docs L95/L302/L479/L692 (all identical).
- Visual originals: none in the bundle. Chart and figure contents that were images in the original
  publication cannot be inspected, so they are recorded as unresolved, not as verified absences.

## D11 - Victorian Farmers Federation submission (February 2022)

- Source: `text/D11.txt` (128 lines; 14,682 chars), `docs/pcau_maritime_r1_sub032_maritime_logistics.txt`.
- Written or submitted by: Victorian Farmers Federation (VFF) (D11 L10, L116-125). No named signatory or person.
  Organisations that are mentioned only: Productivity Commission (L10), DP World (L56), National Transport Commission (L64), ACCC (L54, L72, L94),
  Essential Services Commission of Victoria (ESC) (L74-75), GrainCorp, Barret Burston Maltings, Victorian Regional
  Channels Authority, Victorian Civil and Administrative Tribunal (L41, L109), Harper Review (L94), New Zealand (L25, L100).
- Type, date, edition: submission to the PC inquiry "Australia's Maritime Logistics System", dated "February 2022" with no day (L3-6).
  Page markers: cover L3-6, then pages "2" L8, "3" L37, "4" L51, "5" L68, "6" L85, "7" L108, "8" L115 (8 pages).
- Period covered: hyphenated year spans "2019-20" (L33), "2020-21 period" (L39) and "2020-21" (L41). The text does not label them
  fiscal or calendar. Relative periods: "over the last 5 years" (L49), "in the last year alone" (L60), "each year" (L41), "per annum" (L117).
  Dated events: VFF since 1979 (L121), 2015 Harper Review (L94), ESC 2020 Market Rent Review (L74), ESC 2021 Pricing Order inquiry (L75),
  2020 Independent review of the Victorian Ports System (L110).
- Entities and aliases: "terminal access charges (or infrastructure charges as they are sometimes known)" (L54). "2021 ACCC Stevedore
  Monitoring report" (L72) is cited by the URL "Container stevedoring monitoring report 2020-21" (L54, L74). "Competition and Consumer Act"
  (L23, L98) = "Competition and Consumer Act 2010 (CCA)" (L94). Port of Melbourne = "the Port" (L39, L106), and "Port Melbourne areas" (L106).
  Other entities: Victorian Voluntary Pricing Protocol (L63); Port Management Act 1995 (Vic) (L75); Fishermans Bend (L106); Wimmera Mallee (L42).
- Tables: none in the text. Three graphics are referenced without data: (a) "Source: https://transport.vic.gov.au/ports-and-freight" (L38,
  between the p.3 marker and the PoM paragraph); (b) "As the below chart demonstrates, terminal access charges on containers have increased
  substantially at the Port of Melbourne over the last 5 years" (L49), source ACCC 2020-21 report URL (L52-54); (c) a chart in the "2021 ACCC
  Stevedore Monitoring report" on aggregate rent per square metre (L72), source URL L74. None of the chart values is in the text.
- Lists:
  - Six recommendations, listed at L22-28. R1 "Strengthen stevedore pricing regulation" (L22). R2 "Strengthen port pricing and market rent
    regulation" and R3 "Repeal Part X of the Competition and Consumer Act and replace with a block exemption that meets minimum standard of
    procompetitive features" share line L23. R4 "Work with New Zealand to make North-South shipping routes more attractive to shipping lines" (L25).
    R5 "Review port buffer planning provisions" (L27). R6 "Improve capability of local governments ... when considering zoning adjustments"
    (L28, the last item). Body repeats: R1 L66; R2 at L79, printed without its number ("Recommendation: Strengthen port pricing..."); R3 L98; R4 L100; R5 L112; R6 L113.
  - Victoria is "Australia's largest exporter of food and fibre, and Australia's largest exporter of dairy products, sheep meat, wool, poultry meat
    and horticulture" (L31). Three major ports: Melbourne, Geelong, Portland (L35). Imported inputs: "fuel, fertiliser and chemicals" (L16).
    Portland live export: "sheep, cattle and dairy cattle" (L42).
  - VFF commodity groups: "dairy, grains, horticulture ,chicken meat, eggs, pigs and livestock" (L123). Expert committees: "water, planning,
    environment and climate change, farming systems, farm business, transport and Infrastructure and workforce and social infrastructure" (L123).
    The text does not say how items joined by "and" are grouped.
  - Appellants at VCAT: GrainCorp, Barret Burston Maltings, Victorian Regional Channels Authority (L109).
- Forecasts, guidance, deadlines, effective dates: the Fishermans Bend renewal "will see substantial redevelopment ... an influx of thousands of
  new residents" (L106). There are no dated deadlines.
- Hedged claims:
  - "estimated the charges had cost him an additional $25,000": the hedge attaches to one member's figure (L60).
  - "is seen to contribute to these high prices": the hedge attaches to the causal link. The ESC findings in the same sentence are stated as findings (L74).
  - "there are reports of livestock artificial insemination products expiring" (L93).
  - "could have impacted the port's operations" attaches to the office development. The successful appeal itself is stated firmly (L109).
  - Firm statements: the Voluntary Pricing Protocol "has failed" (L63); the pulse packer "had to move" to bulk at Portland (L90).
- Rounded prose beside exact figures: "nearly half" (L33); "over 2 million tonnes" (L41); "approximately $7.8 billion" (L41); "over $13
  billion", "over 25 per cent" (L117); "more than double" and "increased substantially" (L72, L49) with the underlying chart values absent.
- Notes (quantitative index; all figures are uncited unless a source is given):
  - $14.5 billion: Victoria's food and fibre exports, 2019-20, "nearly half of Victoria's total goods exports" (L33).
  - 43%: share of "all containerised exports from the Port of Melbourne" that are agricultural goods. No period is given (L39).
  - 1.2 million tonnes of grain exported over the 2020-21 period, in the context of PoM's "bulk grain exporting facilities". 1.6m tonnes of grain
    were exported in containers out of PoM "during the same period" (L39).
  - Port of Geelong: "Australia's sixth largest port by tonnage", "approximately $7.8 billion of trade each year", and "over 2 million tonnes
    exported from the GrainCorp terminal alone in 2020-21" (L41).
  - "the entire 25MT to fill the containers" (L58). $25,000 extra cost "in the last year alone", estimated by one VFF member (Central Victoria,
    export hay) (L60). TAC increases "over the last 5 years" (chart, ACCC source) (L49-54).
  - The port's "24-hour operations"; "truck curfews on several streets" (L106). A "seven-story office development" (L109).
  - Victoria's agricultural production: "over $13 billion of Victoria's economy and over 25 per cent of the State's exports per annum" (L117).
    "Victoria's six million people" (L121).
  - Third-party sources: ACCC 2020-21 monitoring report (L49-54, L72-74); ESC 2020 review and 2021 inquiry (L74-75); 2015 Harper Review (L94);
    2020 Independent review (L110). The submitter's own evidence: the member estimate (L60) and "the VFF have sighted examples" (L61).
- Operative definitions, rules and scope exceptions:
  - TACs "are charged by stevedores to trucks and trains for collecting or dropping off full containers at their terminals" (L54).
  - "it is the shipping lines that choose the stevedore" (L55).
  - Part X of the CCA "regulates international liner shipping". Harper (2015) recommended repealing it, with "a block exemption granted by the ACCC ...
    for liner shipping agreements that meet a minimum standard of pro-competitive features" (L94).
  - The ESC 2020 review found that PoM "had exercised its market power in the process for setting and reviewing land rents in a way that caused material
    detriment to Victorian consumers". The ESC recommended "an enhanced negotiate-mediate-arbitrate framework independently overseen" (L74).
  - The ESC 2021 inquiry found "significant and sustained non-compliance" and that "existing incentives within the regulatory framework of the Port
    Management Act 1995 (Vic) are not working" (L75).
  - The 2020 Independent review found that buffer controls require "further strengthening" and recommended that a review of buffer planning
    provisions "be commissioned by the Government" (L110).
- Actions vs mentions: the VFF's own acts are its six recommendations (L20) and the examples it has "sighted" (L61). Third-party acts reported:
  a pulse packer "was forced to temporarily stop purchasing pulses" and moved from PoM containers to bulk out of Portland (L89-90); GrainCorp et al.
  "recently successfully appealed" (L109); the NTC "are developing" voluntary national guidelines (in progress) (L64). DP World is mentioned only for its
  "previous comments" that charges can be "passed through the supply chain, without negative impact" (L56).
- Amendments or contradictions: none stated. Different measures: food and fibre exports as "nearly half of Victoria's total goods exports" (2019-20, L33)
  vs agricultural production as "over 25 per cent of the State's exports per annum" (L117). R2's body heading has no number (L79).
- Coverage: full; L1-128 read sequentially in one chunk. Unresolved: the contents of the graphics at L38, L49-54 and L72-74.

## D12 - National Competition Council submission (11 February 2022)

- Source: `text/D12.txt` (111 lines; 15,058 chars), `docs/pcau_maritime_r1_sub033_maritime_logistics.txt`.
- Written or submitted by: National Competition Council ("the Council") (D12 L3, L13), signed by Richard York, "NCC Executive Director" (L104-106).
  Address: Level 17 Casselden, 2 Lonsdale Street Melbourne (L4-6). Organisations mentioned only: PNO, Glencore, ACCC, Australian Competition Tribunal,
  NSW Minerals Council, Flinders Ports, ESCOSA, DBCT, the Queensland Treasurer, Treasury, Federal and High Courts, ABS.
- Type, date, edition: letter submission dated 11 February 2022 (L7) to the "Australia's Maritime Logistics System Inquiry" / "Inquiry into the long-term
  productivity of Australia's maritime logistics system" (L8-13). No page markers. Two footnotes: fn 1 at L40 and fn 2 at L107-108.
- Period covered: events are dated by calendar month and year, 2014-December 2021 (L19-99). Prose prices are nominal, "per gross tonne" (L24-30).
  Figure 1 is "in 2020-dollar terms (i.e., adjusted for inflation)", covering prices "since 2014" (L38). It uses "the Sydney All Groups Consumer Price Index ...
  (CPI Sydney) and averaged over four quarter periods" (fn 1, L40). The Council counts "3 occasions ... between 2015 and 2020" (L89).
- Entities and aliases: Council = NCC (L13, L106). NAR = National Access Regime, "set out in Part IIIA of the Competition and Consumer Act 2010 (CCA)" (L15).
  The Port = Port of Newcastle (L19). PNO = Port of Newcastle Operations Pty Ltd (L19). Glencore = Glencore Coal Pty Ltd (L21). ACCC = Australian Competition
  and Consumer Commission (L21). The Tribunal = Australian Competition Tribunal (L22). NSC = Navigation Service Charge (L24). NSWMC = NSW Minerals Council (L32).
  Flinders Ports is "the port operator" in SA (L46). CPA = Competition Principles Agreement (L54). ESCOSA = Essential Services Commission of South Australia (L70).
  DBCT = Dalrymple Bay Coal Terminal (L73). The decision-maker is called the "designated Minister" (L22, L32), "the Minister" (L26, L32, L34) and the
  "responsible Minister" (L68, L79).
- Tables:
  - Figure 1, "Navigation Service Charges set by PNO, ACCC and Tribunal (adjusted for inflation)". The title is at L42, run together with the next heading.
    Its data labels are displaced to L60-63, after the s 44M(4) list. Text order: values "$0.78 $0.63 $1.04 $1.04 $0.81"; axis "$- $0.20 $0.40 $0.60 $0.80 $1.00
    $1.20"; categories "PNO 2018 Price | ACCC 2018 Determination | Tribunal 2019 Determination | PNO 2020 Price | PNO 2020 Deed Price". Read in order:
    PNO 2018 Price $0.78; ACCC 2018 Determination $0.63; Tribunal 2019 Determination $1.04; PNO 2020 Price $1.04; PNO 2020 Deed Price $0.81 (2020 dollars;
    the axis has no per-unit label). "PNO's price offerings are shaded in red" (L38), which is not visible in text. The value-to-bar pairing rests on text
    order alone; the visual check is unresolved.
  - Figure 2, "Timeframes for considerations of declaration applications under Part IIIA of the CCA" (L87): no data in the text (gap).
- Port of Newcastle case history, in calendar order (who acted, and prices):
  1. 2014: the NSW Government owned and operated the Port "until 2014 when it was privatised"; functions transferred to PNO "through a long-term lease arrangement" (L19).
  2. "Shortly after": PNO "implemented price increases and changes to the charging regime" (L21).
  3. May 2015: Glencore lodged an application for declaration under Part IIIA (L21).
  4. January 2016: "in accordance with the Council's recommendation", the designated Minister decided not to declare. Glencore then applied to the Tribunal (L22).
  5. May 2016: the Tribunal decided the service should be declared and set aside the Minister's decision (L22).
  6. November 2016: the ACCC commenced arbitration, Glencore v PNO (L24).
  7. July 2018 (presented "In the meantime", after the September/October 2018 items): following amendments to the declaration criteria in s 44CA, PNO applied for revocation (L26).
  8. September 2018: ACCC Final Determination, NSC $0.61 per gross tonne, "an approximately 20 per cent decrease on the then price set by PNO of $0.76 per gross tonne" (L24).
  9. October 2018: PNO and Glencore both applied to the Tribunal for review of the ACCC Final Determination (L24).
  10. September 2019: "following a recommendation made by the Council, the Minister was deemed to have decided to revoke the declaration" (L26).
  11. October 2019: Tribunal decision, NSC payable by Glencore to PNO "increased to $1.01 per gross tonne - an increase of 65 per cent above the price determined
      by the ACCC". This was "at the time, higher than the unregulated price set by PNO for other access seekers" (L28).
  12. January 2020: PNO increased the NSC to $1.04 per gross tonne, "equivalent to the price determined by the Tribunal when adjusted for inflation". It also offered
      "an alternative 10-year pricing commitment (commencing at $0.81 per gross tonne) if they agreed to the terms of a deed" (L30).
  13. July 2020: the Council received the NSWMC declaration application and recommended not declaring (L32).
  14. February 2021: the Minister decided not to declare, "in accordance with the Council's recommendation" (L32).
  15. March 2021: NSWMC applied to the Tribunal for review (L34).
  16. August 2021: the Tribunal "affirmed the Minister's decision not to declare" (L34).
  17. Undated ("subsequent"): appeals "to the Federal and High Courts by the ACCC and PNO respectively". The pricing matter "has now been remitted to the Tribunal" (L36).
  - Summary: "PNO's pricing for its NSC has largely been set between the range of prices arbitrated by the ACCC and Tribunal" (L38).
- Other chronologies:
  - SA ports access regime: application under s 44NA received January 2021; the previous certification "ran for ten years until May 2021" (L42). The Council sought
    submissions after the application and after the draft recommendation, and issued information requests under s 44NAA (L44). It recommended a ten-year extension
    in September 2021. On 29 November 2021 the Minister "was deemed to have made a decision to certify the access regime for a further ten years" (L68). ESCOSA
    review "scheduled ... in 2022"; ESCOSA advised it is "supportive of including these considerations in its 2022 review" (L70).
  - DBCT access regime: application under s 44NA received January 2021; the previous certification "ran for ten years until July 2021" (L73). "no submissions were
    received" (L74). The recommendation was sent in July 2021; deemed certification decision on 14 September 2021 "for a further ten years" (L79).
  - NAR timeliness: April 2021, Council submission to Treasury's consultation (L83). May 2021, "the Government announced it would implement reforms" (L91).
    December 2021, Treasury "issued an exposure draft outlining proposed legislative amendments" (L99; fn 2 "Improving the Timeliness of National Access Regime
    Processes", L107-108).
- Lists: arguments against the SA regime, 2 bullets (L49, L51). s 44M(4) duties, 3 bullets (L54, L56, L58), the last being "not consider any other matters".
  May 2021 reforms, 3 bullets (L93, L95, L97), the last being "terminating arbitration proceedings and determinations where the underlying declaration is revoked".
- Forecasts, guidance, deadlines, effective dates: certification end dates May 2021 (SA, L42) and July 2021 (DBCT, L73); "further ten years" certifications
  (L68, L79); ESCOSA 2022 review (L70); 10-year deed pricing commitment starting at $0.81 (L30); proposed CCA amendments that the Council "considers ... will improve
  NAR processes" (L99).
- Hedged claims:
  - "is largely considered to be a 'bottleneck' facility" (L19).
  - "that we consider may be relevant" (L17).
  - "it is possible that the prospect of declaration may have helped achieve an outcome not too dissimilar to that one might expect with regulation": the hedge
    attaches to the effect of the prospect of declaration (L38).
  - "matters don't appear to be resolved by the Tribunal" (L87).
  - In "confidential information it may acquire" (L51), "may" sits in a side clause. The stated objection ("does not contain adequate protections") is firm.
  - Firm opinions: "the Council is of the opinion that current arrangements encourage repeat applications" (L89); "The Council is satisfied it can effectively
    influence ... without the need to legislate stronger powers" (L72).
- Rounded prose beside exact figures: "approximately 20 per cent decrease" ($0.76 to $0.61 = -19.7%) (L24). "65 per cent" above the ACCC price ($0.61 to $1.01 =
  +65.6%) (L28). The prose gives nominal prices ($0.76, $0.61, $1.01, $1.04, $0.81; L24-30); Figure 1 gives 2020-dollar values ($0.78, $0.63, $1.04, $1.04, $0.81; L60).
- Operative definitions, rules and scope exceptions:
  - The Council's role is to make "recommendations concerning access to services provided by nationally significant infrastructure" (L15).
  - Consequence of declaration: "users of a declared service have a right of access"; the ACCC "can be asked to arbitrate" (L21).
  - s 44I(4) of the CCA: "if a declaration is revoked, any arbitration process that has begun, or arbitration determination that has been made, prior to the
    revocation will continue" (L28).
  - s 44M(4): the Council must apply the CPA principles "(as amended on 13 April 2007)", have regard to the objects of Part IIIA and "not consider any other
    matters" (L52-58).
  - Scope limits: "the CPA provides significant discretion to states and territories" (L65). The Council's test "does not assess if the regime itself is ideal"
    (L66). The Council "is unable to mandate changes" (L72). "its role extends only to assessing the effectiveness of state-based access regimes themselves, and not
    to an assessment of decisions made by relevant governments" (L76, on the Queensland Treasurer's decision to declare coal handling services, which is "subject to
    judicial review").
- Amendments or contradictions:
  - Current rule vs proposal: s 44I(4) continuation after revocation (L28) vs the May 2021 announced reform "terminating arbitration ... where the underlying declaration
    is revoked" (L97), with the December 2021 exposure draft (L99). The announced reforms also cover "removing merits review by the Tribunal" (L93) and "limiting new
    applications" after previous declaration or revocation processes (L95).
  - Decision reversals: the Tribunal set aside the January 2016 Ministerial decision (L22) and replaced the ACCC's $0.61 with $1.01 (L24-28). The August 2021 Tribunal
    affirmed the February 2021 decision (L34). The arbitration was remitted after the court appeals (L36). The s 44CA amendments preceded PNO's revocation application (L26).
- Actions vs mentions: the Council's own acts are its recommendations (L22, L26, L32, L68, L79), submission requests and s 44NAA information requests (L44), its
  recommendation that ESCOSA consider improvements (L70) and its April 2021 Treasury submission (L83). It "supported removing" merits review (L87). The Council
  "does not consider it would be appropriate" to express views on the Queensland Treasurer's decision (L76).
- Coverage: full; L1-111 read sequentially in one chunk. Gaps: Figure 2 data (L87) and Figure 1 colour/bar visual (L38, L60-63) are unresolved.

## D15 - Housing Industry Association submission (11 February 2022)

- Source: `text/D15.txt` (142 lines; 16,936 chars), `docs/pcau_maritime_r1_sub040_maritime_logistics.txt`.
- Written or submitted by: Housing Industry Association (HIA) (D15 L7), "HOUSING INDUSTRY ASSOCIATION LIMITED" (L137). Signed by Kristin Brookfield,
  "Chief Executive Industry Policy" (L138-139). Contact: Melissa Adler (L135). Organisations mentioned only: ACCC, Harper Competition Review, the Royal Commission
  into Union Corruption and Governance, Boral, CFMEU, CFMMEU (and its MUA division), AIRC, ABCC, Fair Work Commission, ABS.
- Type, date, edition: letter dated 11 February 2022, "By email: maritime@pc.gov.au" (L3-6). Page markers "Page 2" L21, "Page 3" L52, "Page 4" L81,
  "Page 5" L121 (5 pages). One footnote, fn 1 at L119.
- Period covered: "2020/21 financial year" (L30, L38) and "2021/22 financial year" (L38). Calendar years for starts: 2017 (L27) and 2020-2025 (L32-36).
  Calendar quarters: "first two quarters of 2021" vs "of 2020" (L38). "During 2021 to September" (L30). "April 2021 – October 2021" (L27). "Over the past 12
  months" (L25). "7 years ago" (L11). "last 50 years" (L49). "1990s" (L53). "a dispute last year" (L123). The AIRC decision is dated 25 October 1993 (fn 1, L119).
- Entities and aliases: PC = Productivity Commission (L7). "ACCC Report" = "The ACCC's annual Container Stevedoring Monitoring Report" (L59). CCA = Competition
  and Consumer Act (L65), also "CC Act" inside the Heydon quote (L75). "FW Act" (L113) = "Fair Work Act" (L79). Union names: "CFMEU" (L77, Boral matter) vs
  "CFMMEU" and "the CFMMEU's MUA division" (L122-123); the text does not state that the two names are the same body. ABCC = Australian Building and Construction
  Commission (L122). "Act" = Building and Construction Industry (Improving Productivity) Act 2016 (L123). AIRC (L82). Commissioner Heydon (L73, L77). Boral is
  "building products manufacturer" (L77). HomeBuilder scheme (L25, L27).
- Tables: none.
- Lists:
  - Sector vulnerabilities, 3 bullets (L42-46): highly regulated (L42); small businesses (L44); uncertainties (L46).
  - AIRC agenda items, 3 bullets (L88-92). The quote closes at L92 with fn 1.
  - ACCC Report conclusions that HIA "urges the PC to support", 4 bullets (L97-103): regulation "inadequate and not fit for purpose" (L97); industrial relations,
    restrictive work practices and privatised ports' "excessive rents and charges" (L99); infrastructure investments for "larger ships, lack of rail access ...
    shortage of space in empty container parks" (L101); "Repealing Part X of the CCA" (L103, last).
  - Additional Harper recommendations, 3 bullets (L107-111): amend ss 45E and 45EA so they apply to awards and industrial agreements (with an exception) (L107);
    remove the "has been accustomed, or is under an obligation" limitation (L109); align the maximum penalty with other competition law breaches (L111, last).
  - ABCC "ancillary site" definition, 2 limbs (L127, L129).
- Forecasts, guidance, deadlines, effective dates (HIA's own forecasts; no external source cited):
  - Detached starts: 2021 "anticipated there will have been 148,880 ... a record and ... growth of 31.3 per cent over 2020". 2022: "121,200 ... expected ... 11 per cent
    above average for the 10 years to 2020". 2023: "expected to decline to 107,700 ... broadly in line with the average of the 10 years to 2020". 2024: "A further
    decline to 96,930 starts is anticipated" (L32).
  - Multi-unit starts: 2021 "anticipated ... 76,440 ... growth of 8.9 per cent on 2020". "drop to 70,130 in 2022 but improve to 72,010 in 2023 and stay around that
    level in 2024. Growth returns from 2025 onwards" (L34-36).
  - Renovations: "We expect that during the 2021/22 financial year renovation activity will increase by a further 5 per cent to a new high of $45.2 billion" (L38).
  - The boom "will be sustained throughout 2022" (L27, hedged "suggests").
- Hedged claims: "it is estimated that the residential building industry employees over 1 million people" (L19); "suggests that the current boom ... will be sustained"
  (L27); "anticipated" and "expected" on all starts figures (L32-35); "We expect" (L38); "whilst this might exempt legitimate strike activity" ("might" attaches to the
  exemption; the claim "it should not cover or enable aggressive picketing" is firm) (L72); "alleged 'black banning'" (L77); "alleged unlawful picketing" (L123).
- Rounded prose beside exact figures: "over $11.5 billion" in each of the first two quarters of 2021 vs "an average $9.4 billion" in the first two quarters of 2020
  (L38). FY2020/21 "$43 billion ... up by 14.8 per cent on the previous year" (L38). The 5% rise to "$45.2 billion" checks as 43 x 1.05 = 45.15 (L38). The 2020 bases
  for the 31.3% and 8.9% growth rates, the 10-year average and the 2019/20 renovation base are not printed.
- Notes (quantitative index): membership of 60,000 (L15); over 1 million employed, "tens of thousands of small businesses", over 200,000 subcontractors (L19);
  "over $100 billion per annum", "6.9 per cent of Gross Domestic Product" (L22); 2017 "over 115,000 detached homes commenced construction" (L27); price rises during
  "2021 to September" of 5.2% for skilled trades and 8% for materials ("as measured by the ABS"), and 8.5% for residential land in the 2020/21 financial year (L30);
  "7 years ago" for Harper (L11). All figures are uncited except the ABS materials measure.
- Operative definitions, rules and scope exceptions:
  - CCA s 51(2)(a) is the "broad exclusion" of workplace relations from competition law (L65).
  - s 45DD: "if conduct relates to employment matters, a person's activity is not deemed to fall under the illegal secondary boycotting provisions" (L70).
  - Exception in the Harper 45E/45EA amendment: "except to the extent they relate to the remuneration, conditions of employment, hours of work or working conditions
    of employees" (L107).
  - The ABCC's powers cover "the transportation or supply of goods to be used for such work, directly to building sites" and "unlawful picketing at an 'ancillary site'"
    (L125-129).
  - "industrial issues at the ports ... can only be responded to through the Fair Work Commission" (L115).
- Actions vs mentions: HIA urges (L95), recommends (L113), "would support" the Harper recommendation that the ACCC be able to intervene in Fair Work Commission
  proceedings (L117), "is supportive of moves to investigate" (L130), and "considers that the ABCC should hold joint powers with the ACCC" (L132). Acts by others:
  the ACCC "issued, ultimately successful Federal Court proceedings" (Boral matter; "belated") (L77); the ABCC's "recent move ... to inquire into picketing by the
  CFMMEU" on "Fremantle's docks" (L122-123). Heydon's statement is quoted (L73-75).
- Amendments or contradictions: none internal. CFMEU (L77) vs CFMMEU (L122) naming is recorded above.
- Coverage: full; L1-142 read sequentially in one chunk. No gaps.

## D17 - Offshore & Specialist Ships Australia submission (undated)

- Source: `text/D17.txt` (139 lines; 15,999 chars), `docs/pcau_maritime_r1_sub042_maritime_logistics.txt`.
- Written or submitted by: Offshore & Specialist Ships Australia Ltd (OSSA), 717 Flinders St, Docklands (D17 L3-4, L8). Signed by Ross Brewer, Chairman (L132-134).
  Organisations mentioned only: MIAL, BIMCO, International Chamber of Shipping, RAN, HMAS Australia, ADF, COMMA, Nautical Institute, AMSA, "Shipowners
  Associations", Lloyds, DNV.
- Type, date, edition: submission titled "Australia's Maritime Logistics System" (L6), with no date anywhere in the text. A running header repeats at L3-4, L28-29,
  L62-63, L77-78, L107-108 and L123-124 (6 pages). "Contacts:" (L136) is followed by nothing; the original is also empty there (docs L134-137). Missing source text.
- Period covered: calendar dates only. OSSA formed 2017 (L8); "Over the past 20-30 years" (L11); "late 1990s" East Timor (L31); 2018 census (L42); July 2021 report
  (L42); "by 2026" (L42); s 23AG rescinded "July 2009" (L75); "current" flooding, Tonga relief and temporary legislation (L24, L29).
- Entities and aliases: OSSA = "Offshore and Specialist Ships Australia" (L8) = "OSSA Ltd" (L81) = "Offshore and Specialist ships Australia Ltd." (L134).
  "MIAL (Maritime Industry Australis Ltd)" (L42; D19 spells it "Maritime Industry Australia Ltd"). "2018 Maritime Skills Census conducted by MIAL" (L42) =
  "The MIAL census" (L109). The July 2021 Seafarer Workforce Report is "from BIMCO and the International Chamber of Shipping" (L42). COMMA = Company of Master Mariners
  Australia (L105). RAN, HMAS Australia (L26-29); ADF (L31). The Income Tax Act section is "23AG" (L75). AMSA Marine Orders (L109).
- Tables: none.
- Lists:
  - Four resilience categories (L16-24): Self reliance; Disaster preparedness; Critical Maritime skills shortage; Security considerations (L24, last).
  - Security issues "Including but not limited to", 4 items (L34-40). The last is "Iron Ore and other inputs into steel production from interstate currently being shipped
    to Port Kembla by foreign ships" (L40).
  - Five training barriers (L52-60): Government Inertia; Cost of training; Berth Access; Quality of Applicants; Ability to Mentor (L60, last). The body discusses them in a
    different order: Government Inertia L64, Cost L70, Quality of Applicants L80, Mentoring L105, Berth Access L109 (last).
  - Shore careers "include but are not limited to", 10 items (L83-101): Management roles with owner operators; Port authorities; Stevedoring; Government Regulators;
    Classification Societies such as Lloyds, DNV etc.; Oil and Gas companies; Offshore wind farming; Shippers and Ships Agency; Fisheries and Aquaculture; Pilotage
    (L101, last).
  - "Summary and key recommendations", 4 numbered (L118-127): 1 a federal "Minister for Marine Affairs" overseeing a "Committee of Marine Affairs" (L119);
    2 an International Register framework (L121); 3 cost-effective training (L125); 4 a cadet program in government ship contracts (L127, last, after the page header
    at L123-124).
  - Also: vessel operators historically carried training costs for "Pilot services, Stevedores, Port Authorities, Regulators, Training institutions, Oil and Gas
    majors, Tugs and others" (L72). Career trades range "from RO RO vessels ... to Scientific research, inshore and offshore towing and fisheries" (L80).
- Forecasts, guidance, deadlines, effective dates: the BIMCO/ICS global officer shortfall of 26,240 "growing to 89,510 by 2026" (L42); continued disruption "will continue"
  (L42); proposed "Fund" with initial "Federal government support" (L72-73).
- Hedged claims: "to our knowledge there are no international agreements of "treaties"" (L24); "it is openly felt they actively support foreign flag ships" (L66);
  foreign seafarers "may have a significant competitive cost advantage" (L75-78); "Perhaps a cost of doing business in Australia might be a legislated provision of
  a single trainee berth per vessel" (L109). Firm statements: "Currently Australian capacity to move a container, bulk cargoes, oil, foodstuffs, medical supplies, is
  zero" (L24); the 2018 census "showed a shortage approaching 600 officers and this figure has grown substantially" (L42); "The discussion about foreign seafarers is
  in reality not about competency but about cost" (L78).
- Rounded prose beside exact figures: "approaching 600 officers" (L42); "some 250 members" (L11); "20-30 years" (L11).
- Notes (quantitative index, with dates and sources):
  - About 250 members, Australia-wide (L11). OSSA formed 2017 (L8).
  - Shortage "approaching 600 officers": 2018 Maritime Skills Census by MIAL (L42).
  - Global ships officer shortfall of 26,240, "growing to 89,510 by 2026": July 2021 Seafarer Workforce Report, BIMCO and ICS (L42).
  - 50 unused sea time berths "on vessels operating in and around Australia": "The MIAL census" (L109). "Very few" were accessed due to cost and state quarantine (L109).
  - s 23AG of the Income Tax Act gave tax relief "for contract periods more than 90 days (leave Inclusive)"; it was "rescinded in July 2009" (L75).
  - "a single trainee berth per vessel" (proposal, L109).
- Operative definitions, rules and scope exceptions: "Self reliance" is defined as "Australia's general capability to move critical resources, supplies and materials
  for the purposes of her own economy" (L24). s 23AG "was not just specific to seafarers" (L75). Sea time initiatives "would need to be dependent upon AMSA Marine Orders"
  (L109). A 2nd register "allows for international crew" (L117).
- Actions vs mentions: OSSA's own acts are its school program (L8, L81, with URL) and the statement that OSSA, COMMA and the Nautical Institute "are co operating on
  developing a mentoring program" (in progress) (L105). OSSA "could assist" with sea time (an offer, L109). Others' acts reported: "Current 'temporary legislation' to
  allow foreign shipping to transport cargoes between Eastern and Western states due to flooding" (L24); "current relief to Tonga using HMAS Australia which was the only
  option" (L29); "Australian controlled merchant vessels provided critical support to the ADF" in East Timor (L31).
- Amendments or contradictions: the minister is named differently within the document ("Minister for Shipping", L68, vs "federal Minister for Marine Affairs", L119).
- Coverage: full; L1-139 read sequentially in one chunk. Gap: the contact list after "Contacts:" (L136) is absent in the source itself.

## D19 - Maritime Industry Australia Ltd submission (18 February 2022)

- Source: `text/D19.txt` (703 lines plus a blank line 704; 75,880 chars), `docs/pcau_maritime_r1_sub046_maritime_logistics.txt`.
- Written or submitted by: Maritime Industry Australia Ltd (MIAL) (D19 L3, L25). Contact: Teresa Lloyd (L8). No signatory block. Organisations it cites or mentions:
  PwC, Oxford Economics, the National Transport Commission, the Department of Infrastructure and Transport, BITRE, ABS, the International Chamber of Shipping, the NSW Freight
  and Ports Strategy, the Productivity Commission, NSW Ports, Svitzer, the three seafarer unions, AMSA, EY, Moore Stephens, the Norwegian Tax Administration, the Danish
  Maritime Authority, and IRAS.
- Type, date, edition: submission dated 18 February 2022 (L9). Page markers 1-28 run unbroken (p1 L4, p2 L12, p3 L23, p4 L36, p5 L64, p6 L73, p7 L100, p8 L136,
  p9 L160, p10 L189, p11 L216, p12 L242, p13 L270, p14 L290, p15 L317, p16 L343, p17 L377, p18 L400, p19 L448, p20 L461, p21 L498, p22 L528, p23 L551, p24 L579,
  p25 L611, p26 L644, p27 L668, p28 L693). Every Contents page number (L13-20) matches the section's actual page. Footnotes run 1-24.
- Period covered: "2013/14" (L111, L403), "2012-13" (L226), "2015/16" (L97) and "2019/20 summer" (L236) are year-span labels, not stated as fiscal. Calendar years:
  1982 (L173), 2012 (L324, L517), 2014 (L320), 2018 (L256, L344), 2019 (L271, L340), 2021 (L38, L322, L326), Jan 2022 (L38, L205), 2023 (L256, L558), 2024 (L84),
  2050 (L103). "relevant financial year" appears for the Australian tax return (L580); "income year" for Norway (L665); "tax year" for the UK (L608, L614).
- Entities and aliases:
  - MIAL = Maritime Industry Australia Ltd (L25).
  - The 2018 census appears as "MIAL Seafaring Skills Census conducted in 2018 (Census)" (L256), "2018 Seafaring Skills Census, Maritime Industry Australia Ltd 2019"
    (fn 10, L267) and "The Seafarer Skills Census" (L558).
  - GL = General Licence (L86) ("General License", fn 2 L97). TGL = Transitional GL (fn 3, L97). AISR = Australian International Shipping Register (L274, L382-384).
  - STUFT = Ships Taken Up From Trade (L173). "Port Headland" (L320) vs the URL "port-hedland" (L337).
  - The three unions (L311): the Australian Maritime Officers Union (Deck Officers including masters); the Australian Institute of Marine and Power Engineers (marine
    engineers); "the Maritime Union of Australia division of the Construction Forestry, Maritime, Mining and Energy Union" (integrated ratings, cooks, caterers, stewards).
  - Roma Britnell is "Shadow Minister for Ports and Freight" (L336) and "Roma Britnell MP, Shadow Minister for Ports" (fn 16, L340). Melissa Horne is "the Ports
    Minister" (L336). "the Andrews Labor Government" (L336).
  - Green Paper titles: "Maritime Green Paper - A Maritime Transition, 2016" (fn 18, L374) vs "Coastal Trading Green paper, A Maritime Transition, 2016" (fn 19, L397).
  - PwC (2015) "Choosing your course" is cited with a pwc.com/kr URL (fn 8, L238) and a pwc.nl URL (fn 21, L495). The PwC Feb 2015 "economic contribution" report is
    cited at fn 9 (L239) and fn 24 (L548).
  - IRAS = Inland Revenue Authority of Singapore (L651). DIS = Danish International Ship Register (L670-690).
- Tables:
  - Seafarer training table (L283-304, straddling the p13/p14 marker at L289-290; no caption). Columns: "Occupation | Brief Description | Qualification | Seatime for
    Entry Level qual | Total Training time for certification" (L283). Rows:
    - Master and Deck Officers | "Advanced Diploma or Degree level" | 18 months | 3 years (L283-287).
    - Marine Engineer Officer | "Diploma – Advanced Diploma level" | 9 months | "Minimum 3 years" (L290-294).
    - Integrated Ratings (IRs), with duties L296-300 | "Certificate 3 Level" | 9 months | 12 months (L294-301).
    - Cooks and Caterers | "Marine Cook Certificate 3 Level Nil Cert of safety training 2 weeks." (L302-304). The column split for this row is ambiguous in the
      text; the probable reading is qualification Certificate 3, seatime Nil, total "Cert of safety training 2 weeks". It is unresolved because no visual original exists.
  - Flag/tax regime table "Flag Country Tax regime" (L469-516; source fn 21 PwC 2015 p.7, L495). It straddles the p20/p21 break (L497-498) and has 45 jurisdiction
    rows. Rows are run together on three lines: L481 Curaçao & St. Martin + Cyprus; L501 Marshall Islands + Netherlands; L513 Sweden + Taiwan. "Republic of Korea
    (South Korea)" spans L506-507. Category tallies as printed (multi-category rows counted in each):
    - "Tonnage tax – Dutch model", 21 rows including Sweden, whose entry reads "under review for possible implementation" (20 without Sweden): Belgium, Bulgaria,
      Curaçao & St. Martin, Denmark, Finland, France, Germany, India, Ireland, Italy, Japan, Netherlands, Norway, Poland, Republic of Korea, South Africa, Spain,
      [Sweden], Taiwan, UK, USA.
    - "Tonnage tax – Greek model", 3: Cyprus, Greece, Malta.
    - "Favourable tax regime", 10: Antigua and Barbuda, Barbados, Bermuda, British Virgin Islands, Cayman Islands, Estonia, Isle of Man, Marshall Islands,
      Saint Lucia, South Africa.
    - "Shipping incentives", 15: Brazil, Canary Islands, China, Curaçao & St. Martin, France, Hong Kong, Italy, Malaysia, Netherlands, Panama, Philippines,
      Russia, Singapore, Sweden, Turkey.
    - "Non-resident tax payer regime", 3: Canada, Liberia, Marshall Islands.
    - Seven rows carry two entries: Curaçao & St. Martin, France, Italy, Marshall Islands, Netherlands, South Africa, Sweden. The first row is Antigua and Barbuda (L470);
      the last is USA (L516). Australia is not in the table.
- Lists:
  - Capability points, 3 (L42-46). "Two key steps" (L53-57), repeated at L382-385.
  - Scope of Australian maritime activity (L74). Assets MIAL members operate (L27).
  - The 42 GL vessels by category (L88): 9 Bass Strait (6 certified to international standards); 3 dry bulk carriers; 5 expedition cruise vessels; 25 servicing
    Northern Australia, "a large number of which are landing barges". The categories sum to 42.
  - Road/rail funding 2013/14, 2 items (L113-115). Conclusions of MIAL's 2021 PC submission, 2 (L178-180).
  - Industrial action "instances", 3 bullets (L320, L322, L324) plus an unbulleted line "15. Industrial action at Gladstone also took place in 2021 on the tug boats." (L326).
    The "15." is probably the displaced footnote marker for L324 (fn 15 at L339); whether L326 is a fourth item or a continuation is unresolved.
  - Ship/port interface suggestions, 3 (L356-359). Benefits of a strong shipping industry, 4 (L363-369).
  - Strategic Fleet lists (L410-454):
    - Government vessels, 4 (L413-419): Australian Antarctic Division; CSIRO; Australian Maritime Safety Authority; Australian Border Force.
    - Defence, 5 (L422-430): Refuelling; Submarine Support; Training; Towage; Other support vessels.
    - Commercial, 9 (L433-454): Tankers; Passenger ships; Ro/ro and landing barges; Break bulk; Container; Dry bulk. Three more come after fn 20 and the p19 marker:
      Offshore vessels (L450), Bunker barges (L452), Tugs (L454, last).
    - The earlier prose list at L378 reads: "Defence and Border Protection fleets, the Antarctic Division Ice Breaker, CSIRO research vessel and AMSA emergency response vessels".
  - Corporate tax recommendations, 3 (L546, L552, L554; the last is on p23).
  - Seafarer tax offset shortcomings, 2, with sub-items a-c (L565-571). Seafarer Tax Offset amendments, 3 (L592-595).
  - UK deduction conditions, 3 (L604-608). UK prior deductions, 3 (L621-625). UK return-visit conditions, 2 (L629-631). Quebec conditions, 5 (L641).
    DIS wage requirements, 3 (L685-689).
  - Terms of Reference TOR 1-7 (L695-701; the last is TOR 7 at L701). Stray text "Australia's maritime logistics system" sits inside L696 before TOR 3.
- Forecasts, guidance, deadlines, effective dates:
  - "Australia has 4 LNG carriers – which will be departing that trade in 2024" (L84).
  - Projected shortfall "of over 560 individuals by 2023" (L256) and "some 560 by 2023" (L558).
  - "2050 targets" (L103).
  - PwC policy scenario: "$25 billion in GDP; 54,000 jobs; and $2.1 billion in tax revenue" (L228). The same scenario is restated at L542 with different jobs and tax
    figures (see contradictions).
  - Strategic Fleet example (L403).
  - Flood exemption from the Coastal Trading Act (January 2022; no end date given) (L205).
  - UK "qualifying period" of at least 365 days (L614, L626).
  - Proposed tax regime (L575) and amendments (L590-595) are proposals.
- Hedged claims:
  - "indeed may absolutely fail" (L48).
  - "That's probably a lot more than many observers ... realise" (L86).
  - "it is estimated that each one per cent increase in freight efficiency saves the national economy $1.5 billion" (L117).
  - "There is little doubt that ... shipping could deliver at least a 1% efficiency gain" (L118).
  - "would likely have immediate impact" (L122, attributed to "the Australian maritime industry"; L352, attributed to the Maritime Green Paper).
  - "vessels who may have the capacity": "may" attaches to the vessels; "This is a sensible move" is firm (L205).
  - "about three years", "somewhere in the region of $250,000" (L279); "in the region of $200,000 to $300,000" (L306).
  - "which reportedly saw the then Workplace Relations Minister intervene" (L324).
  - "potentially quite different ... could mean ... may be more aligned" (L390).
  - "it is entirely possible that ships themselves might be unavailable" (L178).
  - PwC "Our analysis suggests" (L532). "has been estimated at" (L542).
  - Singapore "may be deemed", "may be liable", "IRAS may not necessarily agree" (L651).
  - Firm claims: "total reliance on foreign shipping"; "what we have right now is total reliance" (L141). "The answer is almost none" (L183). "Such a change would have
    no effect on tax receipts" (L539).
- Rounded prose beside exact figures:
  - Rail/road shares of the $140m: "approximately 1.6% of the rail funding" vs 140/8,300 = 1.69%; "0.56% of the road funding" = 140/25,000 (L403 vs L113-115).
  - Port Botany: "nearly 100% for export (up from $43 to $81.94)" = +90.6%; "200% for import (up from $43 to $123.10)" = +186.3% (L344).
  - "$3.60 to $80.00 per container" = +2,122% vs "over 2 000 per cent in just two years" (L336).
  - "less than 6%" (MIAL estimate) vs BITRE 2015/16 GLs 6.5% (L94, L97).
  - "approximately 17%" (L79). "~$25 Bn", "~$8.3 Bn" (L113-115). "~100 seafarers" (L403).
- Notes (quantitative index, with dates and sources):
  - Trade: "over 90% of Australian trade" by international shipping; coastal shipping "approximately 17% of the domestic freight task" (fn 1, Who Moves What Where,
    NTC 2016) (L79, L97). "<1% of the 99% of export trade is carried on Australian ships 100% of imports are carried on foreign ships" (L85; infographic-style line).
    "less than 6%" of the coastal shipping freight task is carried by Australian vessels, an MIAL estimate based on the BITRE Australian Sea Freight 2015/16 report
    ("Transitional GLs carried 11.2% and GLs 6.5%"). "In 2022 there are no TGLs – and none converted from TGL to GL status; and the number of GLs has fallen from
    2015/16 levels" (L94, L97).
  - Licences/vessels: 42 vessels hold a General Licence (fn 2: "Department of Infrastructure and Transport list of General License granted dated 18/11/2021") (L86, L97),
    broken down at L88. 4 LNG carriers in international trades (L84). "no international trading container ships" (L186). The UK requisitioned "54 civilian ships from
    33 owners" in the Falklands war, 1982 (L173). Bass Strait commercial operators "have both recently renewed their shipping fleets" (L520).
  - Funding/economy: 2013/14 public funding of "~$25 Bn (Commonwealth, State/Territory and Local) for road" and "~$8.3 Bn (Commonwealth and State/Territory) for rail"
    (fn 5, "ABS (2015 c,e & h), BITRE estimates") (L111-115, L132). "$1.5 billion" per 1% freight efficiency (fn 6, NSW Freight and Ports Strategy, November 2013)
    (L117, L133). PwC: "in 2012-13 the total (including the direct and induced impacts) contribution of the shipping industry was $21 billion in GDP; 45,000 jobs and
    $1.3 billion in tax revenue" (fn 9, PwC Feb 2015) (L226, L239).
  - Strategic Fleet example: "20 vessels would result in 1800 permanent jobs, provide training for ~100 seafarers each year and deliver $173m in tax revenue. The support
    required ... is $140m annually" (fn 20, ABS/BITRE) (L403, L445).
  - Seafarers: the Census shows "52% are over 46 years old and 1% are over 70" (L258); "80% of employers require experience and skills beyond the base level
    qualifications" (L260); "tanker experience was the most sought after" (L262). Training takes about 3 years; cost about $250,000 (L279) or $200,000-$300,000 (L306).
  - Port charges: PoM stevedore access fees "increased from $3.60 to $80.00 per container over the past 2 years", quoting the media release of Roma Britnell MP dated
    Wednesday 20 February 2019 (fn 16) (L336, L340). Port Botany: "in 2018 NSW Ports released their new port pricing schedule" dropping separate coastal container
    pricing; export $43 to $81.94 and import $43 to $123.10 (fn 17 nswports.com.au URL). No unit is stated for these figures (L344, L374).
  - Industrial action: tugs at "Port Headland", threatened in 2014 (fn 13); "across the Svitzer fleet, Australia's largest supplier of harbour towage services in 2021"
    (fn 14); threatened action in Gladstone in 2012; Gladstone tugs 2021 (L320-326, L337-339).
  - Tax: in 2012, zero tax on profit from Australian-flagged ship operations (fn 22, "Shipping Reform (Tax Incentives) Act 2012 (Cth)") (L517, L525). Existing seafarer
    tax offset "provides a tax refund to the employer for 30% for eligible individuals" (L560). Eligibility requires "international service of at least 91 days" (L569).
  - Foreign tax rules (all labelled "Information taken directly from" EY Shipping Industry Almanac 2016, Moore Stephens, the Norwegian Tax Administration or the Danish
    Maritime Authority):
    - UK: 365-day qualifying period; no single return visit over 183 consecutive days; UK days "less than half" of days abroad; "183 days abroad followed by 182 days in
      the UK" does not qualify (L614-633).
    - Canada: rations and quarters excluded when "at sea for a period of not less than 36 hours"; Quebec deduction of "75% of the remuneration" (L639-644).
    - Singapore: "60-day de minimis rule" (L651).
    - Norway: seafarers' allowance "30 percent of the income earned onboard"; "minimum of 130 days at sea"; "item 3.2.13" (L665).
    - Denmark: limited-liability seafarer tax rate "30 per cent"; Danish ship "gross tonnage of 20 t or more" (L673-677).
- Operative definitions, rules and scope exceptions:
  - Flag vs Port States (L154, L157). Requisitioning "is typically applicable only to the ships flying the flag of the nation, however it is possible to apply to other
    flags" (L174).
  - The qualification "(as distinct from the certificate of competency issued by AMSA, effectively the licence to work on board) does not include the "sea time element""
    (L308).
  - The seafarer tax offset applies only to seafarers on trading ships, which must be Australian flagged, with international service of at least 91 days (L565-569). It
    "assumes an employment relationship between an Australian resident tax payer and an Australian company" (L572).
  - 2012 corporate regime: "zero tax on profit", with dividends taxed to shareholders, "In effect, the tax is deferred" (L517-518).
  - Exclusions in foreign rules: Norway's article "does not apply to those who work in the petroleum sector on the Norwegian continental shelf" (L662). In the UK,
    "share awards and termination payments, are not normally eligible" (L617). Denmark: "A ship which is registered with registered office in Denmark, and without crew is
    taken over for chartering by a Faroese, Greenland or a foreign shipping company, shall not be considered as Danish" (L679). "Since DIS wages are net wages, the
    seafarer has no possibility of income tax allowances" (L690).
  - A suggested test for Strategic Fleet vessels: "identify where there is sufficient cargo to warrant a stable and permanent presence" (L392).
- Amendments or contradictions (internal; recorded neutrally):
  - The PwC Feb 2015 report is cited at L226-228 (fn 9) for 2012-13 figures of $21bn GDP, 45,000 jobs and $1.3bn tax, and a policy scenario of $25bn GDP, 54,000 jobs and
    $2.1bn tax. L542 (fn 24, the same report) says the contribution "following introduction of such a policy has been estimated at $25Bn in GDP; 45,000 jobs and $1.3Bn
    in taxation revenue".
  - Census shortfall: "over 560 individuals by 2023" (L256) vs "some 560 by 2023" (L558).
  - Cadet cost: "somewhere in the region of $250,000" (L279) vs "$200,000 to $300,000" (L306).
  - The ro-ro investment claim is attributed to "the Australian maritime industry" (L122) and, in the same words, to the "Maritime Green Paper" (fn 18) (L352).
  - Repeated passages: hydrogen L59 = L456; "This and other future opportunities..." L61 = L458; two key steps L55-57 ~ L382-385.
  - Legal change reported: "the federal government exempted vessels from the requirements under the Coastal Trading (Revitalising Australian Shipping) Act 2012" after the
    January 2022 flood (L205). s 23AG-type relief is absent here; see D17 L75 for its rescission in 2009.
- Actions vs mentions: MIAL's own acts are its submission to the PC 2021 supply chain vulnerability inquiry (L174), its submission to the 2019 (Senate) Rural and Regional
  Affairs and Transport References Committee inquiry (L271, L522), the 2018 Census (L256, fn 10 dated 2019), "MIAL has consistently been advised" (L308), its proposals
  (L385) and its recommendations (L544-554). Acts by others: the federal government's exemption (L205); NSW Ports' 2018 schedule (L344); the UK requisition (L173); the
  Svitzer/Gladstone/Port Hedland actions (L320-326); the "Andrews Labor Government promised" (quoted, L336).
- Coverage: full. Chunk ledger: L1-110, L110-209, L210-299, L300-389, L390-469, L470-549, L550-629, L630-703 (EOF). Unresolved layout: the training table's last row
  (L302-304), the industrial-action list item at L326, and the infographic line at L85.

## Shared ground across group B (navigation only)

- ACCC: D11 L54, L72-74 (monitoring report charts), L94 (block exemption); D12 L21-36 (NSC arbitration); D15 L59-61, L77, L95-117, L132; D19 L701 (TOR 7).
- Part X and the Harper Review: D11 L23, L94, L98 (Harper 2015); D15 L11 ("7 years ago"), L103, L105-117; D19 L701 ("the Government's in-principle acceptance of the
  Harper Review's recommendation to repeal Part X").
- MIAL 2018 census: D17 L42 ("approaching 600 officers", "grown substantially since"), L109 (50 unused sea time berths); D19 L256-267 ("over 560 individuals by 2023";
  fn 10 "2018 Seafaring Skills Census ... 2019"), L558 ("some 560 by 2023").
- January 2022 east-west flood and coastal shipping: D17 L24 ("Current 'temporary legislation' to allow foreign shipping ... due to flooding"); D19 L38 (Jan 2022 flood
  "rendering the east/west rail connection inoperable"), L203-205 (exemption from the Coastal Trading Act 2012).
- Strategic oil stored in the USA: D17 L34 ("Australian strategic fuel reserve being on the west coast of the USA"); D19 L193-197 (PC Stage 1 report Pg 92: "By storing
  crude oil in the United States ...").
- Seafarer tax: D17 L75 (s 23AG relief for contracts "more than 90 days (leave Inclusive)", rescinded July 2009); D19 L560-569 (current offset, 30%, "at least 91 days"
  of international service).
- Registers: D17 L111-121 ("Australian 2nd Register", "International Register"); D19 L274, L382-384 (AISR).
- Union names: D15 L77 (CFMEU), L122-123 (CFMMEU, "MUA division"); D19 L311 (MUA division of the CFMMEU in full; AMOU; AIMPE).
- Fair Work / bargaining: D15 L65-79, L113-117; D19 L311-314.
- Submission dates: D11 "February 2022" (L6); D12 11 Feb 2022 (L7); D15 11 Feb 2022 (L3); D19 18 Feb 2022 (L9); D17 undated.
- People named (all group B): Richard York (D12 L105-106); Kristin Brookfield and Melissa Adler (D15 L135-139); Commissioner Heydon (D15 L73, L77); Ross Brewer (D17
  L132-133); Teresa Lloyd (D19 L8); Roma Britnell and Melissa Horne (D19 L336, L340). Two different people named Melissa: Adler (HIA contact) and Horne (Victorian
  Ports Minister).

## Repeats elsewhere in the bundle (whole-bundle Grep, D01-D20; inspected matches)

- Terminal access / infrastructure charges (group B: D11 L46-64; D19 L336):
  - Different values under similar labels:
    - D19 L336: PoM stevedore "access fees ... increased from $3.60 to $80.00 per container over the past 2 years" and "infrastructure access fee by over 2 000 per cent
      in just two years" (media release 20 Feb 2019, L340).
    - D08 L131: "Infrastructure Access Charge increasing from $3.57 to more than $140.00 per TEU in 3 years".
    - D08 L206: "Infrastructure Levy of currently up to $140.00 per container"; "from less than $3.57 per TEU three years ago to over $140.00 per TEU today".
    - D13 L222: "Stevedores Infrastructure Surcharge/Terminal Access Charge (TAC) Increased 2,600% in 11 years".
  - D02 L174-182, attachment table "INFRASTRUCTURE SURCHARGES - AS AT 25 January 2022 per full container / excluding GST" (export/import, effective date). Melbourne rows:
    DP World $105.90/$144.70 (1-Jan-22); Patrick $84.90/$129.50 (1-Mar-21), then 101.90/155.40 from 7/03/2022; VICT $141.80/$141.80 (1-Jan-22).
  - D02 L124-125 (quoting the ACCC): landside share of stevedore revenue "around 13% in 2010–11 to around 38% in 2020–21"; "TACs comprise around 20% of total revenue in
    2020–21".
  - Definitions: D11 L54 (TACs = "infrastructure charges"); D16 L153 ("'Infrastructure Surcharge' ... also commonly and sensibly referred to as 'Terminal Access Charges'";
    stevedore or empty container park); D13 L222.
  - The shipping line picks the stevedore: D11 L55; D16 L153; D08 L127-128.
  - Other TAC passages: D06 L33, L137-142, L163; D09 L38; D04 L63; D16 L24, L35, L157-159.
  - NTC guidelines described in different states: D11 L64 ("are developing voluntary national guidelines"); D13 L249-251 (December 2020 referral; NTC "will 'develop voluntary
    national guidelines'"); D02 L131-134 ("The voluntary guidelines published by the NTC"; "30 days' notice"; "Sixty days' notice operates at Port Botany"); D16 L35/L159 (an
    "NTC review of Terminal Access Charges").
- Port of Melbourne rents, ESC and lease (group B: D11 L72-75; D19 L336):
  - D10 L68: "land rents at the Port of Melbourne have increased significantly following its privatisation in 2016"; ESC 2020 found market power exercised in charging land
    rents. D06 L121 makes the same ESC 2020 point.
  - D10 L69: on "28 January 2022, the ESC publicly released its final report into the Port of Melbourne's compliance with the pricing order over the period 1 July 2016 to
    30 June 2021"; "significant and sustained non-compliance"; revenue requirement overstated "by around $300-650 million"; WACC "on average 2% higher".
    Footnotes: "Port of Melbourne – Market Rent Inquiry 2020, 14 August 2020" (D10 L83) and "Inquiry into Port of Melbourne compliance with the pricing order, 31 December 2021"
    (D10 L87). Compare D11 L74 ("2020 Port of Melbourne Market Rent Review") and L75 ("2021 Inquiry ... Pricing Order").
  - D07 L263, L333, L618 (ESC Victoria 2020 Market Rent Inquiry; Pricing Order governs prices and rents).
  - Lease date: D19 L336 "lease of the Port of Melbourne in March 2016" (quoted media release) vs D10 L68 "privatisation in 2016".
  - The "more than double" aggregate rent comparison (D11 L72) appears nowhere else.
- Port of Newcastle and Part IIIA (group B: D12 L19-38, L81, L89):
  - The NSC prices ($0.76, $0.61, $1.01, $1.04, $0.81; Figure 1 $0.78/$0.63/$1.04/$1.04/$0.81) appear only in D12.
  - D09 L145-160 (Box 2, a different matter): "During 2013 and 2014 the NSW Government privatised Port Botany, Port Kembla and the Port of Newcastle" (L152), vs D12 L19
    "until 2014 when it was privatised". 50-year port commitment deeds with NSW Ports (L152); cap "30,000 TEUs per annum" (L156); the ACCC says the arrangement "effectively
    doubles the cost of moving a container" (L158); "A federal court case brought by the ACCC against NSW Ports in 2018 was dismissed and is currently on appeal" (L159).
  - D09 L159 says regulation "could be achieved through a declaration by the Treasurer under Part IIIA". D12 calls the decision-maker the "designated Minister" (L22, L32).
  - Other Newcastle mentions: D13 L182 (alternate container port); D04 L31 (congestion example).
- Access regimes, Flinders Ports, ESCOSA, DBCT, CPA (group B: D12 L42-79):
  - D07 L194, L257 (ESCOSA 2017: Flinders Ports "has the potential to exercise market power even though it has not found any evidence"); L311 ("only the Dalrymple Bay Coal
    Terminal (DBCT) is presently subject to economic regulation by QCA"); L336-344 (ESCOSA reviews; MSA Act SA ports access regime); L69, L276 (certification under the
    Competition Principles Agreement); L679 (PC 2013 NAR draft report).
- Part X and Harper (group B: D11 L23, L94, L98; D15 L11, L103-117; D19 L701):
  - D10 L71-122 (the ACCC recommends repeal).
    - L103 quotes Harper: "A block (class) exemption ... for liner shipping agreements that meet a minimum standard of pro-competitive features", the same "minimum standard"
      wording as D11 L94. D06 L144 quotes it without "minimum": "meet a standard of pro-competitive features".
    - L113: Harper's "transition period of two years". L115: ACCC consultation began 3 December 2019. L120: the work is on hold "without a firm commitment that Part X will be
      repealed". Compare D19 L701, the "Government's in-principle acceptance".
  - Other Part X/Harper passages: D06 L38, L144, L148, L163; D16 L133-136; D03 L198.
  - Harper's date: 2015 (D11 L94; D06 L144; D10 L101); D15 L11 says "7 years ago". The 45E/45EA and Fair Work Commission intervention recommendations appear only in D15 L105-117.
- ACCC Container Stevedoring Monitoring Report 2020-21 (group B: D11 L54, L72-74; D15 L59-61, L95-103; D19 L701):
  - Release: "On 3 November 2021, the ACCC released its Stevedoring Report 2020-21" (D10 L19-20); its footnote reads "ACCC website, 4 November 2021" (D10 L31).
  - ACCC recommendations are listed as 4 bullets in D10 L26-30 (IR/restrictive practices; privatised ports' rents and charges; repeal Part X; infrastructure). D15 L97-103
    also has 4 bullets, grouped differently: it adds "regulation ... inadequate and not fit for purpose" and joins IR with rents and charges.
  - The clause "larger ships, lack of rail access to Australian container ports and shortage of space in empty container parks" appears verbatim in D06 L43, D10 L78 and D15 L101.
  - Other citations of the report: D16 L157; D06 L19; D13 L120; D02 L104-128.
- World Bank / IHS Markit port ranking: not in group B. Located in D10 L39 ("bottom 15% and 10%, respectively, of the 351 global ports"), D06 L133, D13 L120, D16 L112,
  D09 L86/L98 and D03 L98 ("bottom quartile").
- Coastal Trading Act, licences and the flood exemption (group B: D17 L24; D19 L86-97, L205, L209, L274):
  - D06 L40, L152, L163: "section 11 exemption of the Coastal Trading (Revitalising Australian Shipping) Act 2012 for voyages by container and roll-on, roll-off vessels to
    Western Australia until 31 March 2022". D19 L205 gives no end date; D17 L24 calls it "temporary legislation".
  - D13 L102: floods "washed away parts of the Trans-Australia Railway line".
  - D14 L28-47: aluminium industry coastal needs of ~3.5 Mt/yr interstate and ~14 Mt intrastate (L11). "Currently, no General Licence holder able to service the alumina dry
    bulk market"; "Previously, only a single General Licence holder" (L31-33). The temporary licence "five voyage minimum" (L43).
  - D20 L27 ("introduction of the Coastal Trading (Revitalising Australian Shipping) Act in July 2012"), L52-121 (bulk coastal freight "around 50 million tonnes" over 10 years
    L52; 2019 review reforms incl. removing "the five-voyage minimum" L90; temporary licence process; AISR at L158, L177, L185). D20 L80 points to fleet-size data in
    "Attachment 2", but Attachment 2 (L121-) describes the licensing process; it gives no vessel count.
  - D09 L122-130 ("The introduction of the Coastal Trading Act 2012 reduced competition"; "a decline in coastal shipping's share"; "flat in terms of tonne-kilometres").
  - No other document gives a General Licence vessel count (searched "General Licen", "licen", "vessels").
- Coastal shipping share figures (group B: D19 L79, L94, L97):
  - D19 L79: coastal shipping "approximately 17% of the domestic freight task" (NTC 2016).
  - D13 L100: "Movement of containerised goods via coastal shipping is limited, representing 0.1% of freight by volume". This is a different scope label.
  - D13 L101: "over 90% of Australia's fuel is imported". Compare D19 L79: "over 90% of Australian trade" by international shipping (different subject).
  - D09 L129: a declining share, no figure (BITRE Yearbook 2020 p.69, L147). D20 L52: ~50 Mt bulk.
- Seafarer shortage (group B: D17 L42, L109; D19 L256-262, L558): no other document mentions the census, BIMCO or seafarer shortfall figures (searched "Census", "BIMCO",
  "shortfall", "seafarer"). Census matches elsewhere are unrelated: D05 L82 (2016 population Census).
- Industrial action and unions (group B: D15 L77, L122-132; D19 L311-330):
  - Svitzer: D19 L322 (action "across the Svitzer fleet ... in 2021"); D10 L43 ("In January 2022, Svitzer, a tugboat operator, also applied to terminate its enterprise agreement
    with the MUA, the Australian Maritime Officers Union, and the Australian Institute of Marine and Power Engineers"). These are the same three unions as D19 L311.
  - Patrick/MUA: D10 L43-44 (applied to the FWC on 26 Oct 2021; in-principle agreement reported on 7 Feb 2022); D05 L251.
  - Fremantle: D15 L123 (ABCC, CFMMEU MUA division, "dispute last year"); D18 L43-48 (Fremantle Port mooring bans after the Qube dispute; source dated 27 October 2021);
    D09 L64 (at least five mining companies affected); D03 L152.
  - Other industrial-action passages: D16 L82 (last quarter of 2020, vessels bypassing Port Botany); D13 L208-216; D02 L158; D01 L91-95 (VICT EA under the Fair Work Act in
    2016, renegotiated 2021).
  - Fair Work Act reform passages: D18 L51-79; D09 L92-104; D05 L224; D16 L30; D03 L207.
  - Gladstone and Port Hedland industrial items appear only in D19; Gladstone port investment is in D09 L115, L173.
- Port Botany pricing (group B: D19 L344): the coastal-container uplift ($43 to $81.94 / $123.10) appears only in D19. Other Port Botany figures: D09 L107 (capacity "at least
  7.2 million" TEU/yr; handled "2.6 million TEU in 2019"), L109 (road over 80% of imports); D13 L167 (2.7 million TEU "today" to 8.4 million by 2045).
- Strategic fleet (group B: D19 L274, L378-454): D14 L49-50 ("There has been a suggestion ... The Council would welcome the inclusion of an assessment"); D20 L32 ("it is
  difficult to see how this could be a viable proposition").
- PC Vulnerable Supply Chains study (group B: D19 L174, L193-195, L701): D03 L170-172, L219, L223; D06 L19; D13 L271, L356. National Freight and Supply Chain Strategy:
  D19 L701 and D02 L79.
- Victorian exports and Port of Melbourne size (group B: D11 L31-39, L117):
  - D11 L33: Victoria's food and fibre exports "$14.5 billion", 2019-20, "nearly half of Victoria's total goods exports".
  - D13 L144: "Victoria accounts for almost a third of Australia's total food and fibre exports with $26 billion worth of Victorian goods exported each year ... accounting for
    28 per cent of the national total".
  - D11 L39 "Australia's largest container port" vs D01 L33 "Australasia's largest container port ... over 2.88 million Twenty-foot equivalent Units (TEU) annually". D10 L39
    names "Australia's largest container ports, Melbourne and Sydney".
- Container and empty-container shortages (group B: D11 L83-93; D15 L101): D05 L149 (shipping lines "reluctant to send empty containers to Adelaide as they can obtain higher
  revenue"); D16 L82, L95 (refrigerated container shortages); D03 L218 ("AdBlue, pallet and container (particularly refrigerated containers) shortages"; compare D17 L36
  "AD Blue"); D13 L186-201.
- Urban encroachment and curfews (group B: D11 L104-113): D13 L180, L282; D03 L163; D08 L193, L280 (truck curfews); D09 L40, L112; D19 L696 (TOR 2 names curfews and urban
  encroachment).
- Boral: D15 L77 ("building products manufacturer Boral"); D20 L13 ("Boral Australia Ltd" as an owner/operator of cement manufacturing facilities).
- Other single-topic repeats: Suez Canal blockage (D19 L38; D16 L53); hydrogen (D19 L59, L456; D06 L134); terms of reference (D19 L694-701 in full; D15 L9 and D19 L66
  paraphrase the purpose; D05 L59-63 lists ToR 2, 3 and 5; D06 L19). Searched with no hits outside D11/D12/D15/D17/D19: LNG carriers, Bass Strait, Falklands, Tonga,
  East Timor, Port Hedland, Minister for Shipping, second register, tonnage tax tables, s 23AG, and the submitter names
  OSSA/MIAL/VFF/HIA/NCC (MIAL appears only in D17 L42, L109 and in its own D19).

## Gaps (group B)

- Unresolved graphics, no visual original: D11 L38, L49-54, L72-74 (chart values absent); D12 Figure 1 colour and bar pairing (L38, L60-63) and Figure 2 data (L87).
- Ambiguous layout: D19 training table last row (L302-304); D19 L326 list membership; D19 L85 infographic line; D19 tax table merged rows (L481, L501, L513).
- Missing source text: D17 contact list after "Contacts:" (L136; the original is also empty).
- Unread ranges in D11, D12, D15, D17 and D19: none. Other documents were inspected only at the Grep-hit lines cited above (D01-D10, D13, D14, D16, D18, D20 are not
  mapped by group B).
