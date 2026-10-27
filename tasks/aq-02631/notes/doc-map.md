# aq-02631 - document map

Written by the caller (Claude Code, claude-opus-5-5) on 2026-10-10 from a full read of `text/D01-D07.txt`.
Navigation only, like the form's bundle overview. Questions quote the documents, never this map.
Line numbers are `text/Dnn.txt` lines; "@" is the character offset in that file (the form's reasoning
number check reads digits only in about the first 20,000 characters of a document).

## Bundle

- What it is: seven SEC Federal Register notices/orders on exchange proposals to list crypto-index
  products, December 2024 to April 2026. Four funds: Franklin Crypto Index ETF (Cboe BZX), Hashdex
  Nasdaq Crypto Index US ETF "NCIQ" (Nasdaq listing rule + Nasdaq ISE options), Bitwise 10 Crypto Index
  ETF (NYSE Arca; staff order then Commission order), T. Rowe Price Active Crypto ETF (NYSE Arca;
  original notice then Amendment No. 1 notice).
- Documents: 7; local D01-D07 = task page Doc 1-7 (same order; `notes/intake.json`).
- Gaps: none. Capture says "7 of 7 read in full (463,044 characters)"; every `matches_capture` true,
  `gap_characters` 0. Capture note carried forward: the page showed "Docket has been updated. Reload
  this page so its checks and buttons keep working." (a stale-page warning, not a document gap).
- Extraction spot-checks (plain-text captures, no pages): D02 weight table L132-134 against the
  capture L792-794 (nine rows, 72.70 ... 0.27, same order); D03 position-limit tables L189-208 against
  the capture; footnotes D05 \3\ (L25-26), D07 \22\ (L169), D06 \5\ (L42) present with their marks.
  Tables are flattened onto single lines with dot leaders (D02 L134, D03 L190/L195/L203); no pipe rows.
- Provenance: capture AQ-02631_2026-10-10_0411.txt, sha256 f0e70541...987a51; per-document hashes in
  `notes/intake.json`.
- Reuse binding: map is valid while `notes/intake.json` source hashes are unchanged.
- Coverage: all seven documents read in full by the caller, start to end (D06 in two reads, D02 in two).

## D01 - Franklin Crypto Index ETF, notice of Amendment No. 1 (Cboe BZX)

- Source: fr_2024_30683.txt; 89 FR 105109; Release 34-101963; File SR-CboeBZX-2024-091.
- Written by: SEC notice; Items I-II prepared by Cboe BZX Exchange, Inc.
- Dates (L17-19): notice December 18, 2024; FR Thursday December 26, 2024; original filed September 19,
  2024; published October 8, 2024 (@1365); longer period designated November 20, 2024 (date not
  printed); Amendment No. 1 filed December 17, 2024, "amended and replaced ... in its entirety";
  comments by January 16, 2025 (L337, @67531). No comments received (fn 3). Trust formed August 13,
  2024 (fn 6). Registration statement pre-effective amendment December 11, 2024 (fn 9).
- Entities: sponsor Franklin Holdings, LLC; trustee CSC Delaware Trust Company; cash custodian /
  administrator / transfer agent Bank of New York Mellon; custodian Coinbase Custody Trust Company, LLC;
  Index Provider CF Benchmarks Ltd.; index "CF Institutional Digital Asset Index--US-Settlement Price".
- Holdings: only bitcoin, ether, cash, cash equivalents (maturities under 3 months, fn 20); never other
  index assets (L104); no staking; forks/airdrops disclaimed (L116).
- Figures: Creation Basket 50,000 Shares, cash only (L117, @17624); minimum 100,000 Shares outstanding at
  commencement of listing (L205, @38630); purchase orders by 2:00 p.m. ET (L197); NAV as of 4:00 p.m.;
  CF Reference Rates: window 3:00-4:00 p.m., 12 partitions of 5 minutes, volume-weighted medians, equal
  average (L155-159, @26560); platforms Coinbase, Bitstamp, Kraken, itBit, LMAX Digital, Gemini; IIV
  every 15 seconds; index rebalanced quarterly (L141); eligibility "95th percentile" (L140).
- No "Timing for Commission Action" section (amendment notice).

## D02 - Nasdaq proposed Rule 5712 + Hashdex Nasdaq Crypto Index US ETF (notice)

- Source: fr_2025_03662.txt; 90 FR 11563; Release 34-102513; File SR-NASDAQ-2025-016.
- Dates (L18-19): notice March 3, 2025; FR Friday March 7, 2025; filed February 18, 2025; Amendment
  No. 1 February 27, 2025 (superseded the original); comments by March 28, 2025 (L529); S-1 filed
  February 7, 2025 (fn 11). Trust approved under Rule 5711(d) December 19, 2024 (L42, fn 6; 89 FR 106707
  (December 30, 2024)); SR-NASDAQ-2025-006 updated service providers and basket size (fn 6).
- Proposed Rule 5712 (L53-79): 5712(e)(1)(ii) at least 90% of holdings weight must be commodities /
  digital assets on which the Exchange can get information via ISG or a CSSA (L62, @10589); continued
  listing after the first twelve months: fewer than 50 holders with more than 60 days to termination,
  fewer than 50,000 securities outstanding, market value under $1,000,000, 15-second value/IIV (L64).
- Trust as proposed: index Nasdaq Crypto Settlement Price Index (NCIS; real-time NCI), overseen by NIMC;
  sponsor Hashdex Asset Management Ltd.; administrator/transfer agent U.S. Bancorp Fund Services, LLC;
  cash custodian U.S. Bank, N.A.; crypto custodians Coinbase Custody Trust Company, LLC and BitGo Trust
  Company, Inc.; index owner Nasdaq, Inc.; calculation agent CF Benchmarks Limited.
- Table, index constituents and weights as of December 31, 2024 (L132-134, @27693): BTC 72.70, ETH 14.48,
  SOL 4.78, XRP 5.02, ADA 1.50, LINK 0.51, AVAX 0.37, LTC 0.37, UNI 0.27 (sum 100.00).
- Sponsor's exclusion circumstances (five, L138-142) and the breach adjustment (L143-145): other assets
  capped at 10% pro rata, remaining 90% spread pro rata over eligible assets.
- Eligibility criteria (five, L165-181); reconstitution first Business Day of March, June, September,
  December (L193); Circulating Supply fixed eight business days before (fn 19); settlement price = TWAP
  of per-minute VWAPs 3:50:00-4:00:00 p.m. (L198, @42696); index level calculated 4:05 p.m.; penalty
  factor example 1/2.5 (L204). Core Crypto Platforms as of December 31, 2024: BitStamp, Coinbase, Gemini,
  itBit, Kraken, LMAX Digital (fn 17). Core Custodians as of December 31, 2024: BitGo, Coinbase,
  Fidelity, Gemini, Komainu, Zodia (fn 18, fn 22).
- Baskets of 10,000 Shares (fn 24-25, @56954); creation order by 2:00 p.m. ET; T / T+1 tables
  (L279-310); Fair Value Event "Relevant Transaction" window 3:00-4:00 p.m. (fn 27); IIV 9:30-4:00 every
  15 seconds; minimum 40,000 Shares = four Baskets at commencement (L434, @95453); trading 4:00 a.m. to
  8:00 p.m. ET.
- Surveillance: CME (ISG member) for bitcoin and ether; Coinbase Derivatives (CFTC regulated, ISG member)
  lists LINK, LTC, AVAX futures "as of the filing date" (L379-380, L493); sponsor concedes other
  constituents (L381); GSG (2007) and USCI (2010) 10% precedents (L397-411).
- Timing rule: 45 days from publication, or up to 90 days (L514, @121654).

## D03 - Nasdaq ISE: options on the Hashdex Nasdaq Crypto Index US ETF (notice)

- Source: fr_2025_10119.txt; 90 FR 23753; Release 34-103144; File SR-ISE-2025-16.
- Dates: notice May 29, 2025; FR Wednesday June 4, 2025; filed May 15, 2025; comments by June 25, 2025;
  NCIQ commenced trading February 14, 2025 (fn 3, @3282). Cites the approval order as 89 FR 106707
  "(December 20, 2024)" (fn 3, fn 39), where D02/D04/D05/D06 print December 30, 2024.
- Trust as approved: assets "only of bitcoin and ether"; index Nasdaq Crypto US Settlement Price Index
  (NCIUSS; intraday NCIUS), NCIOC; Core Custodians "as of May 27, 2024" BitGo, Coinbase, Fidelity,
  Gemini (fn 11, @14666). Service providers as D02.
- Option rules: strike intervals $1 up to $200, $5 above; short-term $0.50 under $100, $1 from $100 to
  $150, $2.50 above $150 (L158); minimum increment $0.05 under $3.00, $0.10 at or above (L162);
  continued listing 6,300,000 shares / 1,600 holders / 1,800,000 shares volume (fn 14, fn 16); 50 holders
  for 30 days (L139); LEAPS twelve to thirty-nine months.
- Position limit analysis (L177-208, all past @29,000): limits of 250,000 / 200,000 / 75,000 / 50,000 /
  25,000 contracts; proposed 25,000; 1,358 ETFs sampled from OCC on May 2, 2025; NCIQ AUM $103,716,000
  (text: May 2, 2025; table label "05/01/25") and April ADV 15,358 shares; fewer than 100 shareholders
  (fn 35). Table rows per bucket 25,000 / 50,000 / 75,000: average mkt cap 429,719,975 / 2,250,652,578 /
  5,098,488,634; median 100,096,008 / 1,106,881,955 / 2,597,821,743; rank 499 / 173 / 140; ETFs 1,012 /
  196 / 150; percentile 50.7% / 11.7% / 6.7%; April ADV average 127,982 / 356,675 / 702,589; median
  32,412 / 335,919 / 677,025; rank 669 / 195 / 150; percentile 34.0% / 0.5% / 0.0%. Prose rounds the
  median to 100,096,000 and the percentiles to "50th" and "34th".
- Creation exercise (L197-208): closing price $24.12 on May 2, 2025; 25,000 contracts = 2,500,000 shares
  = $60,300,000; actual weights "as reported on 05/02" BTC 90.16, ETH 9.85; market capitalisation "on
  05/03" 1,909,708,673,172 and 220,466,191,469; value required 54,366,480 and 5,939,550; 0.00285% and
  0.00269%.
- No basket size, no minimum shares outstanding. FLEX excluded. Timing rule 45 / 90 days (L287).

## D04 - Bitwise 10 Crypto Index ETF: order by delegated authority (set aside by D05)

- Source: fr_2025_14036.txt; 90 FR 35339; Release 34-103531; File SR-NYSEARCA-2024-98.
- Dates: order July 22, 2025; FR Friday July 25, 2025; Amendment No. 1 Release 103499 (July 18, 2025),
  cited by PDF page, no FR citation (fn 3); Grayscale Order Release 103364 (July 1, 2025), 90 FR 29923
  (July 7, 2025), "currently stayed" (fn 6). Issued "by the Division of Trading and Markets, pursuant to
  delegated authority" (L192).
- Trust (L68-93): sponsor Bitwise Investment Advisers, LLC; trustee Delaware Trust Company; custodian
  Coinbase Custody Trust Company, LLC; administrator / cash custodian / transfer agent The Bank of New
  York Mellon; index administrator Bitwise Index Services, LLC; valuation vendor CF Benchmarks Ltd.
  (window 3:00-4:00 p.m.; Bitstamp, Coinbase, Gemini, itBit, LMAX, Kraken). Monthly rebalance. At least
  85% Approved Components, at most 15% others; rebalance by the next Core Trading Session, notify by
  9:15 a.m. E.T. (fn 19). Creation Units of at least 10,000 Shares, cash.
- Weights as of June 30, 2025 (L68, @7333): BTC 78.72, ETH 11.10, XRP 4.97, SOL 3.03, ADA 0.78, SUI 0.35,
  LINK 0.32, AVAX 0.28, LTC 0.24, DOT 0.19 (printed weights sum to 99.98).
- Approved Components = bitcoin and ether only (fn 18: "As of the filing of Amendment No. 1").
- Findings: 80% precedent (L125, fn 32); accelerated approval before "the 30th day after the date of
  publication of Amendment No. 1" (L169, @33172).
- Comments (fn 36, fn 43): Multicoin Capital (April 29, 2025) supports; Anonymous (February 10, 2025)
  opposes over XRP and Solana; Better Markets (March 28, 2025) opposes. CME "currently lists and trades
  both XRP and Solana futures".

## D05 - Bitwise 10 Crypto Index ETF: Commission order setting aside D04 and approving

- Source: fr_2025_20523.txt; 90 FR 52724; Release 34-104212; File SR-NYSEARCA-2024-98.
- Dates (L17-29, all before @3500): order November 18, 2025; FR Friday November 21, 2025; filed
  November 14, 2024; published December 3, 2024; extension January 14, 2025; proceedings instituted
  March 3, 2025; extension May 28, 2025; Amendment No. 1 filed July 17, 2025, published July 23, 2025
  (90 FR 34681); delegated approval July 22, 2025; stayed the same day (Rule 431 letter); scheduling
  order July 29, 2025; statements by August 22, 2025. "By the Commission." (L167).
- Same trust facts and the same June 30, 2025 weights as D04 (L58, @8877), cited to FR pages.
- Differences from D04: fn 14 Grayscale Digital Large Cap Order (Sept. 17, 2025), 90 FR 45440 (Sept. 22,
  2025), approved; fn 19 widens Approved Components to commodities that would qualify under the generic
  listing standards (Release 103995, Sept. 17, 2025); fn 19 dates the 85% remark "As of June 30, 2025";
  a "Comments" section: two letters in support (Multicoin; Hashdex Asset Management Ltd., Samir Kerbage,
  August 12, 2025) and two opposed (Anonymous; Better Markets); fn 41: the Hashdex letter cites
  SR-NASDAQ-2025-016 and SR-NYSEArca-2024-87; the former "has been withdrawn" (@30222).

## D06 - T. Rowe Price Active Crypto ETF: notice of the original filing (NYSE Arca)

- Source: fr_2025_21402.txt; 90 FR 54769; Release 34-104243; File SR-NYSEARCA-2025-77.
- Dates: notice November 24, 2025; FR Friday November 28, 2025; filed November 6, 2025 (@936); S-1 filed
  October 22, 2025 (fn 5); comments by December 19, 2025 (L416). Listing rule 8.201-E (Non-Generic).
- Entities: sponsor T. Rowe Price Sponsor LLC; trustee CSC Delaware Trust Company; administrator T. Rowe
  Price Associates, Inc.; custodians unnamed; reference-rate vendor unnamed ("a third-party vendor(s)").
- Eligible Assets: four criteria (L63-69: ISG market; futures on a DCM for at least six months; 40% of an
  ETF's NAV; generic standards). List "As of the date of this filing" (L118, @19117), fourteen: bitcoin,
  ether, SOL, XRP, ada, AVAX, litecoin, DOT, Dogecoin, HBAR, Bitcoin Cash, LINK, lumen, Shiba Inu.
- Index: FTSE Crypto US Listed Index, top ten by market capitalisation, square-root weights, quarterly
  rebalance (L77). Fund expects five to 15 crypto assets (L79).
- Asset backgrounds (L119-234, @19,400-58,000), supplies "as of October 2025": bitcoin 19.93 million of
  21 million; ether about 121 million (72.0 million initial: 60.0 / 6.0 / 3.0 / 3.0); SOL about 612
  million, CME futures March 18, 2025 (@27293); XRP about 60 billion of 100 billion (total 99.98
  billion), CME futures May 20, 2025 (@29700); ada about 36 billion of 45 billion; AVAX about 422 million
  of 720 million; LTC about 76 million of 84 million; DOT 1.6 billion; Dogecoin about 151 billion; HBAR
  about 42 billion of 50 billion; BCH about 20 million of 21 million; LINK about 678 million of one
  billion; lumen about 50 billion (30 billion SDF, 20 billion open market); SHIB about 589 trillion of 1
  quadrillion.
- Staking allowed; written liquidity policies if under 85% of crypto assets readily available (L93).
- Creation Units of 10,000 Shares, cash only (L274-275, @64289); Slippage and Total Cash Amount (L284-293);
  minimum 100,000 Shares outstanding at commencement (L328-329, @77796); NAV at the close or 4:00 p.m.,
  whichever is earlier; ITV every 15 seconds; trading 4:00 a.m. to 8:00 p.m.
- Timing rule 45 / 90 days (L401, @93671).

## D07 - T. Rowe Price Active Crypto ETF: notice of Amendment No. 1 (NYSE Arca)

- Source: fr_2026_08274.txt; 91 FR 23135; Release 34-105308; File SR-NYSEARCA-2025-77.
- Dates (L17-34, all before @2600): notice April 24, 2026; FR Wednesday April 29, 2026; original filed
  November 6, 2025, published November 28, 2025; longer period designated January 7, 2026 (to February
  26, 2026, fn 5); proceedings instituted January 28, 2026 (@1789); Amendment No. 1 filed April 21, 2026
  (@2518), "replaced and superseded the original filing in its entirety"; amended S-1 February 11, 2026
  (fn 10); comments by May 20, 2026 (L248). Listing rule 8.201-E (Generic).
- Changes against D06: crypto asset "does not include stablecoins" (fn 11); stablecoins only USDC
  (GENIUS Act, July 18, 2025; fn 12); Eligible Assets defined by the generic standards only (L71); list
  "As of the date of this filing" (L104, @14626) is D06's fourteen plus "Sui (SUI)"; reference rates by
  Lukka, Inc. (L129); NAV "normally 4:00 p.m."; Creation Units of "at least 5,000 Shares", cash and/or
  in-kind (L166, @29780); minimum 10,000 Shares outstanding at commencement (fn 22, L169, @30209);
  authorized-participant agreements with the Distributor and the Sponsor; market-maker rule 8.201-E(m);
  no asset backgrounds; no timing section.
- Unchanged: sponsor, trustee, administrator; FTSE index of ten; five to 15 assets; 85% staking
  liquidity test; six-month futures and 40% ETF criteria (L146-151); ITV every 15 seconds.

## Shared ground (navigation only)

- One approval order (Release 101998, December 19, 2024) covers the Hashdex trust and the Franklin fund;
  cited in D02, D03, D04, D05, D06.
- Same fund, two documents: Hashdex D02 (proposed strategy and rule) / D03 (options, trust as approved);
  Bitwise D04 (staff order) / D05 (Commission order); T. Rowe Price D06 (original) / D07 (amended).
- Repeated word for word: Bitwise June 30, 2025 weights (D04, D05); T. Rowe Price index and five-to-15
  text (D06, D07).
- Asset sets: Hashdex index nine (D02), Bitwise portfolio ten (D04/D05), T. Rowe Price eligible fourteen
  (D06) then fifteen (D07). Bitwise holds SUI and DOT, not UNI; Hashdex holds UNI, not SUI or DOT; UNI is
  in neither T. Rowe Price list; SUI is in D07's only.
- Creation sizes and launch minimums: Franklin 50,000 / 100,000 (D01); Hashdex 10,000 / 40,000 (D02);
  Bitwise at least 10,000 / none stated (D04/D05); T. Rowe Price 10,000 / 100,000 (D06), then at least
  5,000 / 10,000 (D07).
- Thresholds: Hashdex 90% surveillance-covered (D02); Bitwise 85% Approved Components and the
  Commission's 80% precedent (D04/D05); T. Rowe Price 85% readily available, 40% ETF NAV (D06/D07).
- Service providers shared: CSC Delaware Trust Company (D01, D06, D07) against Delaware Trust Company
  (D04, D05); Bank of New York Mellon (D01, D04, D05); Coinbase Custody Trust Company, LLC (D01, D02,
  D03, D04, D05); CF Benchmarks (D01, D02, D03, D04, D05).
- Futures facts: CME bitcoin and ether (D01, D02, D03, D06); Coinbase Derivatives LINK, LTC, AVAX (D02
  only); CME SOL and XRP launch dates (D06 only); CME lists both (D04, D05, undated).
- Commission timing rule (45 / 90 days) printed in D02, D03, D06; applied dates in D01, D05, D07.
- Hashdex Asset Management Ltd.: sponsor in D02/D03 and commenter in D05.
