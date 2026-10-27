# aq-03120 - D02 document map (ANZ Bank New Zealand submission; "Doc 2" on the task page)

Navigation only. Facts and locations, not questions. Line numbers are `text/D02.txt` lines
(`L33` = line 33). Questions quote the document, never this map. Written by bundle-mapper
2026-10-11 for merge into `notes/doc-map.md`; only D02 was read.

## Binding, coverage ledger, extraction

- Source: `docs/nzcc_banking_r1_issues_anz_submission_on_market_study_into_personal_ban.txt`
- Reuse binding: manifest sha256 `cd19629c16926d894151fe66f69f2b6a2184192559ceed9dd0d05ee1a1b64945`
  (equals `notes/intake.json` captured_sha256 and source_sha256; `incomplete: false`, gap_characters 0),
  method `text`, pages null, 119,289 chars, 964 lines.
- Line offset: `text/D02.txt` has a 2-line header, so text line N = docs line N-2.
- Ledger of ranges read (sequential, every line): L1-160, L160-309, L309-438, L438-557, L557-666,
  L666-775, L775-874, L874-964. Remaining unread: none. Coverage: FULL for readable text.
- Extraction spot-checks against the docs original: (a) page markers `PUBLIC VERSION / n` run 1-46
  without a break (46 marker hits; last at L950-951); TOC page numbers agree with the markers.
  (b) Table 2 identical (docs L795-806 = text L797-808, 16 entries, asterisk note kept).
  (c) Footnote 29 identical (docs L526 = text L528). (d) "paragraph 1919" in fn 6 is in the
  original too (docs L85), so it is a source artefact, not a re-extraction fault.
  The original is itself a plain-text capture; no PDF/image was available, so chart visuals are unresolved.
- Missing source text (distinct from unread): see "Gaps" at the end.
- Layout hazards that affect reading:
  - Footnote markers are detached from their sentence and often land at the START of the next
    line, where they look like paragraph numbers: L34 ("2 and 80% of customers"), L36 ("3 A 2019
    research report"), L47 ("4"), L58 ("5 i.e. the underlying"), L102 ("8 and"), L104 ("9"),
    L210 ("14 From a commercial perspective"), L331 ("17"), L391 ("22 Capital is the most expensive"),
    L416 ("25 There may be aspects"), L500 ("27 and"), L613 ("32"), L700 ("41"), L713 ("42 But they do
    switch"), L718 ("44 Accordingly"), L721 ("46"), L744 ("48"), L868 ("51 and"), L956 ("53 Many of").
  - Footnote markers fused onto a number, which can be misread as extra digits: "7.5%.12" (L183),
    "15%.16" (L318), "20.5 basis points,19" (L335), "October 2020.26" (L444), "end of 2019.37"
    (L659), "age of 17.39" (L687), "23-27.40" (L688), "October 202147" (L740 = October 2021 + fn 47),
    "interest rates.23" (L391), "12 months.45" (L719), "deposit accounts11" (L167), "income20" (L347).
  - Page headers interrupt sentences (e.g. L44-45, L120-121, L228-229, L326-327, L364-365, L406-407,
    L429-430, L531-532, L609-610, L737-738, L758-760, L858-860, L898-899, L912-913).
  - Sub-paragraph numbers run inline inside long lines (e.g. "58.2" in L472, "105.7"/"105.8" in L680,
    "137.1-137.6" in L814-815, "152.8-152.10" in L890).
  - Hyphenation losses: "nonbank", "midthirties", "payto-mobile", "peer-topeer", "oncall",
    "technologybased", "Tākiri-āRangi" (L607) vs "Tākiri-ā-Rangi" (L305).
  - Two paragraph-number series: Introduction paras 1-34 (L21-173) and Appendix 1 paras 1-170
    (L181-960). The same number can mean two different paragraphs (e.g. "25", "34").

## Identity

- Title: "MARKET STUDY INTO PERSONAL BANKING SERVICES / PRELIMINARY ISSUES PAPER / ANZ BANK NEW
  ZEALAND LIMITED SUBMISSION" (L5-7). Date: 7 September 2023 (L8). Edition: "Public Version" (L3, L9);
  confidential material shown as "[ REDACTED ]".
- Written/submitted by: ANZ Bank New Zealand Limited ("ANZ", L21). Addressee: New Zealand Commerce
  Commission ("Commission", L21). Study = "market study into personal banking services" (L21).
- Responds to: Commerce Commission, "Market study into personal banking services: Preliminary Issues
  paper (10 August 2023)" (fn 1, L37) = "Preliminary Issues Paper" (PIP).
- Annex 1: "Incenta Report on benchmarking bank performance (Provided separately)" (L18). NOT in D02;
  D02 only summarises it (L63-94, L310-316, L348-365, L368, L392).
- Scope ANZ gives its own response: "deposit accounts and home loans" (L167, L423, L437).
- Period convention: calendar months/years as printed; no fiscal-year statement. "2023 Half Year
  Results" (5 May 2023) cited in fn 31/44 without a period-end date.

## Structure (headings, line ranges, Commission question numbers)

Printed pages in brackets, from the `PUBLIC VERSION / n` markers.

| Lines | Heading / question | Paras | Page |
|---|---|---|---|
| L3-9 | Cover | - | 1 |
| L11-18 | Table of contents | - | 2 |
| L20-28 | INTRODUCTION | Intro 1-2 | 3 |
| L29-52 | "There is strong competition to supply personal banking services" | Intro 3-5 | 3-4 |
| L54-94 | "ANZ's profits are consistent with comparable overseas banks and reflect normal returns" | Intro 6-17 | 4-6 |
| L96-150 | "The regulatory environment is central to understanding and assessing competition to supply personal banking services"; sub-heads L97 "Personal banking market outcomes are influenced by the regulatory environment" (18-24), L143 "Regulation is an important part of our environment, even where it doesn't directly shape competitive conditions" (25-27) | Intro 18-27 | 6-8 |
| L152-161 | "The economic environment shapes competition and market outcomes" | Intro 28-32 | 8-9 |
| L163-173 | "ANZ's detailed comments on the Preliminary Issues Paper" | Intro 33-34 | 9-10 |
| L177-178 | APPENDIX 1: LIST OF QUESTIONS IN THE PRELIMINARY ISSUES PAPER (para numbering restarts) | - | 11 |
| L179-190 | Q1 structure of the sector | App 1-4 | 11 |
| L192-196 | Q1.1 other key participants | App 5-6 | 11 |
| L202-215 | Q1.2 measures of concentration/market share | App 7-10 | 12 |
| L216-231 | Q2 regulatory environment | App 11-14 | 12-13 |
| L233-292 | Q3 other legislation (Table 1) | App 15-16 | 13-14 |
| L293-306 | Q4 Māori | App 17-20 | 14-15 |
| L307-365 | Q5 financial performance data (Figure 1) | App 21-28 | 15-18 |
| L367-407 | Q6 factors influencing financial performance; sub-heads Competition L369, Monetary policy L371, Economic conditions L376, Regulatory settings L386, "Other elements of a bank's activities" L391 (inline) | App 29-41 | 18-20 |
| L409-420 | Q7 digital innovation/disruption | App 42-45 | 20 |
| L422-437 | Q8 choice of services | App 46-49 | 20-21 |
| L439-459 | Q9 intensity between provider groups; sub-heads "Home loans" L441, "Deposit accounts, including transaction accounts, savings accounts and term deposits" L454 | App 50-55 | 21-22 |
| L461-483 | Q10 / Q10.1 gaining and retaining; sub-heads L467, L477 | App 56-59 | 22-23 |
| L485-487 | Q10.2 | App 60 | 23 |
| L488-491 | Q10.3 national branding | App 61-62 | 23 |
| L495-514 | Q10.4 physical presence (Figure 2 caption) | App 63-67 | 24-25 |
| L516-518 | Q10.5 regions | App 68 | 25 |
| L520-548 | Q11 product variation; sub-heads "Home loan products" L522, "Deposit account products" L541 | App 69-75 | 25-26 |
| L552-560 | Q12 interactions between providers | App 76-77 | 27 |
| L562-575 | Q13 mortgage brokers | App 78-82 | 27-28 |
| L576-581 | Q14 segmentation (para 84 wholly redacted) | App 83-84 | 28 |
| L583-618 | Q15 population groups | App 85-91 | 28-30 |
| L620-636 | Q16 and Q17 answered together (L624); sub-heads L630, L635 | App 92-97 | 30-31 |
| L638-660 | Q18 open banking; sub-heads L640, L655 | App 98-104 | 31-32 |
| L662-682 | Q19 entry, expansion, exit | App 105-106 | 32-33 |
| L684-700 | Q20 first bank | App 107-110 | 33-34 |
| L701-783 | Q21 (Q21.1, Q21.2) and Q22 answered together (L709); sub-heads L716, L745, L768, L780 | App 111-132 | 34-37 |
| L785-831 | Q23 tools to search/compare/switch (Table 2); sub-heads L787, L811, L818 | App 133-141 | 37-39 |
| L832-849 | Q24 tying/bundling | App 142-148 | 39-40 |
| L851-902 | Q25 innovation in past five years | App 149-153 | 40-43 |
| L904-913 | Q26 innovation vs overseas | App 154-155 | 43-44 |
| L915-922 | Q27 latent demand | App 156-159 | 44 |
| L924-938 | Q28 incentives to innovate | App 160-163 | 44-45 |
| L940-952 | Q29 impediments to innovation | App 164-167 | 45-46 |
| L953-960 | Q30 ownership structure | App 168-170 | 46 |
| L962 | Footnote 53; L964 end marker "-----" | - | 46 |

- TOC group headings (L15-17) are NOT printed in the body; only Q headings are. By TOC page number:
  "Questions on the Commisison's [sic] overview of personal banking services" p11 (Q1-Q7 fall on
  p11-20); "...services the Commission is focusing on" p20 (Q8); "...nature of competition" p21
  (Q9-Q14 on p21-28); "...different population groups" p28 (Q15); "...consumer search and switch" p30
  (page 30 is where Q16/Q17 start; Q20-Q24 run p33-40); "...innovation" p40 (Q25-Q30). The TOC has
  no entry for the entry/expansion questions Q16-Q19. Grouping is a page-number inference only.
- L220 refers to "the Executive Summary to this response"; no section carries that name (the
  Introduction at L20-173 is the only front section).

## Figure inventory (every quantitative statement, in line order)

Format: line | value as printed | what it measures, scope words | period / as-at | attribution | flags.
"REDACTED fn" = the footnote giving the source is blanked, so the source is not stated.

Introduction
- L8 | 7 September 2023 | submission date | - | ANZ | -
- L23 | "three points" | points highlighted at 2.1-2.3 | - | ANZ | -
- L32 | "four other larger providers" | ASB, BNZ, Kiwibank and Westpac; ANZ "competes particularly closely" | - | ANZ | L183 "five larger banks"
- L33 | "just over $1 billion worth of home lending" | "switched in the home loan market"; market-wide, not ANZ-only | July 2023 | fn 2 "RBNZ, Bank Financial Strength Dashboard" (L39) | repeated in fn 43 (L729) with wording "represented mortgages that were switching"
- L33 | "20.9% of the total mortgage monies advanced" | share of home lending that switched | July 2023 | fn 2 RBNZ dashboard | repeated L729, same value
- L34 | "80% of customers surveyed" | "would consider switching purely based on interest rate considerations"; population = "customers surveyed" (not further defined) | April 2023 | REDACTED fn 3 (L41-42) | repeated L740 with comparator 54%
- L36+L45 | "two out of three savings account holders" | "would decide to switch based solely on rates" | "A 2019 research report" | REDACTED fn 4 (L65) | repeated L771; L772 adds "The remaining 35%"
- L52 | Questions 9 to 11 and 25 | cross-reference | - | - | -
- L67 | section 48 | Commerce Act 1986 (fn 5) | - | - | -
- L82 | 12.3% | "ANZ's average post-tax return on equity"; ANZ only, used "as a proxy for New Zealand banks" (L80); "like-for-like basis" | "over the 2010 to 2021 period" | Incenta (Annex 1, not in D02) | repeated L92, L365
- L82 | 12.2% | "average post-tax returns of its peer group of international banks" | 2010 to 2021 | Incenta | repeated L365 ("comparator set")
- L88 | 8 March 2022; page 8; "3.58 onwards" | Commerce Commission retail grocery study executive summary and final report (fn 7) | - | - | -
- L92 | "12.1% to 12.8%" | "cost of equity for New Zealand banks"; a range | "for the periods" (no years restated; L86 "over this period") | Incenta | -
- L92 | 12.3% | "ANZ's return on equity ... toward the lower end of that range" | same | ANZ/Incenta | "post-tax" not repeated here
- L127 | "most recently" | bank failures in "the United States and Switzerland" | undated | ANZ | -
- L149 | "approximately a five-year programme of work"; "over $580m" | ANZ's cost of implementing RBNZ outsourcing policy BS11; ANZ only | undated | ANZ | followed by "[ REDACTED ]"
- L150 | "2021 changes to the CCCFA"; "well over 2 years"; cost "approximately [REDACTED]" | ANZ implementation time and cost | - | ANZ | amount redacted
- L158 | "approximately NZ$53 billion worth of bonds" | RBNZ purchases "from the secondary market" (quantitative easing, Covid-19 response) | undated | ANZ statement about RBNZ; no footnote | -
- L166 | "three preliminary comments" | 34.1-34.3 | - | ANZ | -
- L169 | page 5 | PIP definition of 'deposit accounts' (fn 11) | - | - | -
- L173 | paragraph 206 | PIP consumer survey | - | - | -

Appendix 1, Q1-Q8
- L183 | "five larger banks" | banking sector structure; "should include Kiwibank" | - | ANZ | -
- L183 | 7.5% | Kiwibank's "market share in the home loan market", "recently reported" | undated; source dated 25 August 2023 | fn 12 Business Desk interview with Kiwibank CEO Steve Jurkovich (L198) | a figure about another bank
- L206 | "first two market studies" | wholesale fuel and supermarket; also Building Products study (plasterboard, cement, structural timber) | - | ANZ | comparison, no ratios given
- L208 | "World Bank CR3 ratios" | NZ "no more concentrated than many other banking markets internationally" | - | fn 14 World Bank Databank: Global Financial Development (L224) | no values printed
- L212 | "each month" | RBNZ Balance Sheet Survey lending and deposit share | - | - | -
- L223 | May 2022; [13]-[14] | Commerce Commission Mergers and Acquisitions Guidelines (fn 13) | - | - | -
- L225-226 | January 2018 | RBNZ BS19 "Framework for Restrictions on High LVR Residential Mortgage Lending" (fn 15) | - | - | -
- L265-266 | 1994 | Tax Administration Act 1994 (CRS) | - | - | -
- L298 | 1993 | Te Ture Whenua Māori Act 1993 | - | - | -
- L317 | 13.40% | "the New Zealand banking sector had a return on equity of"; sector-wide; pre/post-tax not stated | not stated in body; source is "Review of 2022" | fn 16 KPMG, Financial Institutions Performance Survey: Banks - Review of 2022 (March 2023), page 21 (L324) | -
- L317-318 | 15% | "average return on equity of NZX 50 Index companies" | same | KPMG (fn 16) | value split across a line break ("NZX" / "50 Index")
- L321 | Figure C3, Table C5 | PIP exhibits showing "a recent increase in NIM across banks" | - | - | -
- L329 | "81." | paragraph number of the quoted Treasury passage | - | fn 17 The Treasury, "Report: Windfall gains in the New Zealand banking sector, and responses (10 February 2023), at [81]" (L339) | -
- L332 | 1 October 2021; "seven-year period" | RBNZ new capital requirements "began to be phased in from" / "increases in capital phased in over" | - | ANZ about RBNZ | see L389
- L335 | "20.5 basis points" | "the RBNZ's estimate of the impact on lending rates of the 2019 reforms" | 2019 | fn 19 RBNZ, Capital Review: Decisions 2019, at [54] (L343) | restated L391 as "20.5bps on average"
- L336 | "rank lowest by some distance globally" | NZ banks, "non-interest income as a percentage of total income" | 2021 per Figure 1 title (L362) | World Bank (fn 20) | ranking only; no value printed
- L341 | page 2 | RBNZ, Capital Review: Decisions 2019 (fn 18) | - | - | -
- L348 | 2003 | "acquisition of the National Bank in 2003" (goodwill) | - | ANZ | -
- L355 | 8 March 2022; [3.33] | grocery Final Report (fn 21) | - | - | -
- L357-362 | axis "0 5 10 15 20 25 30 35 40 45 50", "Percent (%)", "Non interest income to total income - 2021" | Figure 1 remnants; 8 countries | 2021 | World Bank, country level (fn 20, L353) | bar values NOT extracted
- L365 | 12.3% and 12.2% | ANZ "average post-tax return on equity" vs "comparator set ... (average post-tax return of 12.2%)"; here stated after "an allowance for intangible assets that is equivalent to the goodwill on ANZ's balance sheet, and allowing for other adjustments" (L352) | 2010 to 2021 | Incenta | same values as L82
- L389 | "up to and including 2028" | capital requirements "progressively increasing each year" | - | ANZ | -
- L389 | "~$20billion of capital" | "material additional" capital "to be sourced over the seven-year transition period, which will be sourced across all banks" | seven-year transition | fn 22 New Zealand Bankers Association, Submission to the RBNZ on "How much capital is enough?" (17 May 2019), Appendix A of Appendix 1 (L398) | all banks, not ANZ-only
- L391 | "20.5bps on average" | "the RBNZ expected the impact of these changes to be an increase of ... on lending interest rates" | assumption "in 2019" (fn 23) | fn 23 (L400-404) | fn 23 qualifies: "The final calculation for ANZ is unknown"
- L395 | undated | "the collapse of Silicon Valley Bank" | - | ANZ | -
- L425, L427 | [123], [125] | PIP paragraphs on digital disruptors (fn 24, 25) | - | - | -
- L432 | "approximately 86 insurance companies, none of which are banks" | licensed by the RBNZ | undated | ANZ; no footnote | -

Q9-Q15
- L444 | 16.43% | "other providers (including smaller banks and non-banks)" share "of new registrations" (home loans) | July 2023 | REDACTED fn 26 (L449-450) | exact to two decimals
- L444 | "around 13%" | same series | October 2020 | REDACTED fn 26 | rounded comparator
- L472 | $50 | 'Join' campaign payment "to new customers (over 18) when opening an everyday account with an ANZ Visa Debit card" | "April - June 2023" | ANZ | -
- L472 | "April to August 2023" | home loan refinance campaign | - | ANZ | -
- L483 | "aged 18 to 24" | young adult customers, financial wellbeing programme | - | ANZ | -
- L491 | "approximately [REDACTED] of our marketing budget" | brand building initiatives | - | ANZ | redacted
- L499 | 15% | "branch over-the-counter transactions accounted for only 15% of our total payments"; ANZ only | "late 2017" | ANZ (Figure 2) | -
- L499 | 4% | same measure | "By June 2023" | ANZ (Figure 2) | -
- L499 | 61.7% | "of sales are now digitally originated"; ANZ only | "now" (undated) | ANZ | exact
- L499 | 38% | same measure | "in 2020" | ANZ | -
- L499 | 68% | "of ANZ customers say they use a branch only once or twice a year, or less" | undated | REDACTED fn 27 (L504) | -
- L501 | "three biggest drivers" | customer service; making banking simple; mobile (i.e. digital) banking | - | "our customer research" | -
- L502 | "approximately [ REDACTED ]" | contact centre staff growth | - | ANZ | redacted
- L506 | 21 December 2020 | NCR Corporation article on Gen Z (fn 28) | - | - | -
- L514 | "six banks"; "until the end of this year" | "we have agreed, with six banks in the regional banking hub trial, not to close regional branches" | end of 2023 by document date | fn 30 "New Zealand Banking Association, Regional Banking Hubs pilot" (L529) | wording does not say whether the six include ANZ
- L528 | 52 | "ANZ has 52 off-site Smart ATMs i.e. ATMs that are not connected to a branch" (fn 29) | undated | ANZ | footnote-only figure
- L542 | "typically one month to five years" | term range of savings/term deposit products, "most providers" | - | ANZ observation | -
- L557 | June 2023 | TVNZ launch of television documentary about scams | - | ANZ | -
- L564 | 57% | "of new lending to ANZ has come through a broker"; ANZ only | "Recent data" | fn 31 ANZ, 2023 Half Year Results: Results presentation and investor discussion pack (5 May 2023), page 134 (L565-566) | -
- L575 | 2013 | Financial Markets Conduct Act 2013 | - | - | -
- L605 | "Almost 700,000 people" | took part in a MoneyMinded course "across the Asia Pacific region" (not NZ-only) | "since 2002" | ANZ | -
- L606 | 2000; "over $9 million"; "more than 1,000 charities and community projects nationwide" | ANZ Staff Foundation grants "Since inception in 2000" | - | ANZ | -

Q16-Q24
- L645 | page 7 | RBNZ, Capital Review: Go-to-Guide 2019 (fn 33) | - | - | -
- L658 | "well over $1bn" | cost of the Australian consumer data right regime to "Government and the major banks" "to implement" | undated | "We understand"; fn 35 (L669) | fn 35 prints only component figures (next line)
- L669 | "more than $200 million"; "$200m" | (i) "the Federal Government has already spent more than $200 million on this ... a fraction of what the designated industries have spent" (Hon Stephen Jones MP, address to CEDA, 7 June 2023); (ii) "Westpac estimates cost of CDR compliance to be $200m" (WS02, 3 January 2019) | - | fn 35 | currency symbol "$" only; Australian context
- L659 | 173 | "accredited parties with offerings in the market" in the UK | "at the end of 2022" | fn 36 Open Banking Limited, New Impact Report ... (30 March 2023) (L670) | -
- L659 | "10 to 11%" | "of digitally enabled consumers and small businesses have now used open banking" | "five years after it went live" | "the UK estimates"; fn 36 | range
- L659 | "up to GBP1.5 billion" | industry investment in open banking | "to the end of 2019" | Lloyds Banking Group PLC estimate; fn 37 "Response to CMA consultation (April 2020)" (L672) | -
- L665 | 2023 | Revolut launched in New Zealand | - | ANZ | -
- L667 | 2023; 2016 | Sharesies savings account service; investment services launched 2016 | - | ANZ | -
- L676 | 2021 | Square One launched | - | ANZ | cross-ref "paragraph 152.12"
- L678 | 2021 | Dosh launched | - | ANZ | -
- L679 | 2019 | Simplicity home loan offering | - | ANZ | -
- L680 | 2018; 2019 | Wise borderless account in NZ; NZ debit Mastercard | - | ANZ | -
- L680 | 2023 | Squirrel on-call account | - | ANZ | -
- L680 | 2020 | Industrial and Commercial Bank of China Limited registered as a bank in NZ | - | ANZ | -
- L681 | 1 September 2023 | announcement that Pepper Money had agreed to acquire HSBC's New Zealand mortgage portfolio | - | fn 38 (L690) | -
- L690 | "$1.4 bln" | size of the HSBC NZ mortgage portfolio; appears only in the fn 38 article title (Interest.co.nz, 1 September 2023) | - | Interest.co.nz | footnote-only figure
- L686 | "broadly three segments" | groups choosing a first bank (children via parents; mid-twenties to mid-thirties; migrants) | - | ANZ | -
- L687 | "Well over half ... by the age of 10"; "over half ... by the age of 17" | children with a savings account / a transaction account | undated | REDACTED fn 39 (L692) | no exact percentage
- L688 | "mid-twenties to midthirties, peaking between the ages of 23-27" | when most customers choose their own provider | undated | REDACTED fn 40 (L694) | -
- L711 | 6% | "only 6% of people under 34 change their main bank in any year" | "in any year" | REDACTED fn 42 (L725-726) | population not ANZ-specific in wording
- L713 | "approximately every second person" | "has accounts with more than one bank" | undated | fn 43 (L728-729): REDACTED text, then the RBNZ July 2023 sentence | -
- L717 | 89% and 11% | "of ANZ Home Loans were on fixed rates" / "had floating rates"; ANZ only | "As of July 2023" | fn 44 ANZ 2023 Half Year Results (5 May 2023), page 134; "ANZ confirms this remains correct as of July 2023" (L730-731) | footnote restates as-at basis
- L719 | 15% | customers "with a fixed rate period ending in less than a year" who "said they were extremely likely to switch in the next 12 months" | "a recent survey" | REDACTED fn 45 (L733) | -
- L719 | "7% and 9%" | same measure for fixed rate periods "ending in the next 1-2 years and more than 2 years respectively" | same | REDACTED fn 46 (L735) | order: 7% = 1-2 years, 9% = more than 2 years
- L729 | "just over $1 billion (20.9% ...)" | repeat of L33 inside fn 43 | July 2023 | "RBNZ dashboard data" | -
- L740 | 80% | repeat of L34 | April 2023 | - | -
- L740 | 54% | same measure | October 2021 | REDACTED fn 47 (L754) | "when interest rates were at much lower levels"
- L742 | 20% | "of customers who switched providers cited dissatisfaction with their previous lender as a key reason for switching" | "A 2022 survey" | REDACTED fn 48 (L756) | -
- L751 | December 2021; "down approximately 20% on average" | "lower switching rates for home lending", "comparing pre-December 2021 and post-December 2021, although this dip has subsequently reduced" | pre/post December 2021 | "we observed" (ANZ) | a relative fall, not percentage points; no window lengths given
- L752 | May 2023 | "a constrained exception for switching was introduced in the CCCFA" | - | ANZ | -
- L753 | April 2023; "six weeks"; 2.3% | Simple Switch pilot launched; duration; "Only 2.3% of re-financing applications we received over that time were put through the Simple Switch process" | pilot period | ANZ | -
- L762 | $100 | "ANZ's mortgage discharge fee" | undated | ANZ | "ANZ does not charge specific home lending switching fees"
- L771 | "two out of three" | repeat of L36/45 | 2019 research report | - | -
- L772 | "The remaining 35%" | "were likely to consider service and quality in making switching decisions" | 2019 research report | REDACTED fn 49 (L775-776) | "two out of three" beside "remaining 35%"
- L782, L789 | "16 banks" | banks for which the Switching Request form / Payments NZ switching process is available | "currently" | ANZ; Table 2 | Table 2 lists 16 names
- L790 | "typically five to 10 working days" | standard service times for deposit/transaction account switching; no ANZ fee "for this inward or outward switching" | - | ANZ | working days
- L817 | "up to 14 calendar days"; "typically takes two days" | home loan switching process; two days is for "simple loans switching to us or from us" | - | ANZ | calendar days vs unqualified "days"
- L821 | "11 bank lenders" | coverage of Canstar comparisons | - | ANZ description | -
- L825 | "6 months and 1 to 5 years" | fixed-rate terms covered by Interest.co.nz data | - | ANZ description | -
- L848 | "Homestar rating of 6 or higher"; "two-year credit card fee waiver" | Healthy Home Loan package eligibility; Blueprint to Build package | - | ANZ | -

Q25-Q30
- L851, L853, L862 | "past five years" / "last five years" | innovation window set by the Commission's question | - | - | -
- L867 | "from five to seven days" | Seven-Day Payments, "a Payments New Zealand-led initiative to extend domestic banking payments" | fn 51 dated 22 May 2023 (L880) | Payments NZ | -
- L893 | "multi-year programme" | Ngā Tapuwae o ANZ, "underway"; no length or cost given | - | ANZ | -
- L894 | March 2021; December 2021 | "introduction of the financial advice changes in March 2021 and CCCFA changes in December 2021" | - | ANZ | -
- L926 | "two main incentives" | 160.1, 160.2 | - | ANZ | -
- L944 | "ranging from 13 years to over 100 years old" | ANZ customer age range | - | ANZ | -
- L948 | [132] | PIP paragraph on CDR regimes (fn 52) | - | - | -
- L962 | August 2023 | Reserve Bank of Australia, Australian CBDC Pilot project report (fn 53) | - | - | -

Figures stated more than once (same or different basis)
- July 2023 switching: L33 body ("$1 billion worth of home lending ... switched") and L729 fn 43 ("represented mortgages that were switching"); identical values; source named two ways ("Bank Financial Strength Dashboard" L39; "RBNZ dashboard data" L729).
- 80% (April 2023): L34 and L740; only L740 gives the 54% (October 2021) comparator.
- 2019 savings report: L36/45 and L771 ("two out of three"); L772 "The remaining 35%".
- 12.3% / 12.2%: L82 ("like-for-like basis") and L365 (after goodwill-equivalent allowance "and ... other adjustments"); 12.3% also L92 against the 12.1%-12.8% cost of equity range.
- 20.5 basis points: L335 ("estimate of the impact on lending rates of the 2019 reforms") and L391 ("20.5bps on average on lending interest rates"), qualified by fn 23.
- Seven years: L332 ("phased in from 1 October 2021 ... over a seven-year period") and L389 ("each year up to and including 2028"; "seven-year transition period").
- 16 banks: L782, L789, Table 2 (L797-808).
- CCCFA December 2021: L751, L894; L150 says "2021 changes to the CCCFA, which took well over 2 years ... to implement".
- ANZ Half Year Results page 134 supports two different figures: 57% broker share (fn 31) and 89%/11% fixed/floating (fn 44).
- No figure in D02 is printed twice with two different values. Nearest cases: "two out of three" vs "remaining 35%"; "around 13%" (rounded) beside 16.43% (exact) in one sentence.

## Tables and figure captions

- Table 1 (L238-292, pages 13-14): "Additional information on current regulation relevant to personal
  banking services". Columns: "Regulation and its purpose" | "Relevance to personal banking services" |
  "Key regulatory agency" (header repeated at L262-263 after the page break). Three rows, no numbers:
  1. Australian Prudential Regulatory Authority (APRA) rules, specifically Prudential Practice Guides
     (PPGs) (L240-258); agency APRA (L258).
  2. The Common Reporting Standard (CRS), implemented through the Tax Administration Act 1994
     (L263-274); agency "Te Tari Taake | Inland Revenue Department".
  3. Foreign Account Tax Compliance Act (FATCA) (US) (L275-292); agency "Te Tari Taake | Inland
     Revenue Department".
  Survived as text; cells are linearised and the header runs into row 1 (L240). Scope note L236:
  "The table does not include all regulation ... only those instruments that ANZ considers key".
- Figure 1 (caption L347; remnants L357-362, page 17): "non-interest income as a percentage of total
  income". Title in chart "Non interest income to total income - 2021"; axis 0-50 "Percent (%)".
  Category labels as printed, in this order: New Zealand, Australia, Norway, Israel, United States,
  Hong Kong SAR, China, Singapore, Canada (8 countries; "Hong Kong SAR, China" is one label).
  Source fn 20 (L353): World Bank Global Financial Development; "country level, the bank level data
  is not available, so it is not possible to control for bank type". DATA VALUES DID NOT SURVIVE;
  only caption, axis ticks and labels. Printed order cannot be tied to bar heights.
- Figure 2 (caption only, inline at L499, page 24): "Branch OTC as a percentage of total payments".
  No axis, no data. The two values tied to it are in prose (15% late 2017; 4% by June 2023).
- Table 2 (L797-808, page 38): "participants in industry switching arrangements"; single column
  "Participants"; note "*Participate via agency banking arrangements" (L808). Survived as text, two
  layout columns flattened. Members as printed: ASB (Auckland Savings Bank); BNZ (Bank of New
  Zealand); SBS (Southland Building, Land and Investment Society)*; Westpac; NBS (Nelson Building
  Society)*; Kiwibank; TSB (Taranaki Savings Bank); The Cooperative Bank; Heartland Bank*; RABO
  Bank*; ANZ Bank; Bank of China; China Construction Bank (NZ) Ltd; Citibank; HSBC; ICBC (NZ) Ltd.
  Count 16, including ANZ Bank itself. Asterisked: SBS, NBS, Heartland Bank, RABO Bank (4).
  Not asterisked: 12. Last entry: ICBC (NZ) Ltd (L807).
- PIP exhibits referred to but not reproduced: Tables 1 and 2 (L218, L235), Figure C3 and Table C5
  (L321), Attachment C (L307).

## Enumerated lists (membership and where the last item sits)

- Closest/larger competitors: ASB, BNZ, Kiwibank, Westpac - L32 ("four other larger providers") and
  L442 ("closest competitors in the supply of home loans"). With ANZ = "five larger banks" (L183).
- Intro 2.1-2.3 (L24-28): three points; 2.2 has (a), (b).
- Intro 4.1-4.3 (L33-50): price competition; non-price competition; innovation. Last L50.
- Intro 11.1-11.2 (L74-78): Incenta criticisms; 11.2 has (i) crisis countries "the European Union,
  the United Kingdom and Japan", (ii) "services beyond core banking services such as investment
  banking and complex instruments". Last L78.
- Intro 22.1-22.3 (L125-135): prudential regulation; AML and CCCFA (switching friction); LVR
  restrictions and CCCFA affordability. Each has (a) objective and (b) trade-off. Last L135.
- Intro 34.1-34.3 (L167-173): process comments. Last L173.
- App 4.1-4.4 (L188-190): cross-references to Q2/3, Q4, Q5/6, Q7.
- App 9.1-9.3 (L212-214): market-share metrics ANZ monitors - RBNZ Balance Sheet Survey lending and
  deposit share; share of registration; share of commitments. Trackers: "Valocity and the RBNZ" (L215).
- Markets said to be more concentrated (L206): wholesale fuel; supermarket; plasterboard; cement
  ("considered as part of the ready-mix concrete"); structural timber.
- Table 1 regulations: APRA PPGs; CRS; FATCA (3). Last L275-292.
- App 18.1-18.4 (L298-300): aspects affecting Māori. Last L300 "geographic barriers and proximity to
  local branches".
- App 21.1-21.3 (L311-314): matters the Incenta report addresses.
- App 25.1-25.4 (L323-337): NIM context points. Last L336-337.
- Q6 factor headings (L369-407): Competition; Monetary policy; Economic conditions; Regulatory
  settings; Other elements of a bank's activities (Leverage para 37; Balance between loans and
  deposits para 38; interest rate risk para 39; Trading and investment activities para 40; Cost
  structure and cost efficiencies para 41). Last L397/L407.
- App 47.1-47.3 (L431-433): product categories outside the focus - Kiwisaver; personal insurance;
  credit cards. Last L433.
- App 58.1-58.3 (L472-473): acquisition campaigns - 'Join'; home loan refinance; cash contribution
  offers. Last L473.
- App 59.1-59.8 (L480-483): retention programmes. Last 59.8 (L483) "streamlining our range of
  products and reducing fees".
- App 63.1-63.3 (L499-501): physical-presence evidence. Last L501.
- App 69.1-69.2 (L524-525) and 70.1-70.4 (L533-537): home loan differentiators - revolving or
  flexible home loans; off-set accounts; progressive drawdown features; low cost top-up loans. Last L537.
- App 76.1-76.4 (L556-558): interactions - business forums; events; industry bodies; other forums.
  Last L558.
- App 87.1-87.11 (L591-610): population-group initiatives; 87.2 (a)(b), 87.7 (a)(b). Last 87.11
  (L610) plain English / WriteMark.
- App 99.1-99.2 (L644, L651): open banking potential.
- App 105.1-105.9 (L665-681): entry and expansion examples - Revolut; Sharesies; Square One; Dosh;
  Simplicity; Wise; Squirrel; Industrial and Commercial Bank of China Limited; Pepper. Nine items;
  last = Pepper (L681). Exits: none listed "beyond those identified in the Preliminary Issues
  Paper" (L682).
- Non-bank debit/pre-paid card providers (L902): Wise, Revolut, Dosh, "OneSmart Air New Zealand /
  Travelex".
- Table 2: 16 switching participants (above). Last L807.
- App 137.1-137.6 (L814-815): home loan switching assistance. Last L815.
- App 139.1-139.8 (L821-829): comparison services - Canstar; Interest.co.nz; Consumer.org.nz;
  Moneyhub.co.nz; Moneycompare.co.nz; Finance.co.nz; Mortgages.co.nz; Citizens Advice Bureau.
  Last L829.
- App 147.1-147.2 (L848): packages - Healthy Home Loan package; Blueprint to Build package.
- App 152.1-152.15 (L863-900): ANZ innovations. 152.1 (a) View Bills, (b) Open Banking payments,
  (c) Seven-Day Payments, (d) Apple Pay; 152.2 (a) Good Energy Home Loan, (b) Blueprint to Build
  Loan Discount; 152.3 (a)-(d) financial management tools; 152.4 (a) ANZ fraud check, (b)
  behavioural indicators; 152.5 e-sign and proof of address; 152.6 KYC/AML/identity checks; 152.7
  Card Tracker; 152.8 digital onboarding; 152.9 video conferencing; 152.10 voice biometrics; 152.11
  (a) Ngā Tapuwae o ANZ, (b) regulatory systems changes; 152.12 agency banking services; 152.13 Tech
  NZ network engagement; 152.14 API standards / API Centre; 152.15 ANZ Group venture arm 1835i.
  Last L900.
- Tech NZ membership organisations named (L899): FintechNZ, Payments NZ, Digital Identity NZ, the
  AI Forum.
- App 155.1-155.3 (L908-913); App 160.1-160.2 (L928); App 163.1-163.5 (L938). Last L938.
- Superapps named (L909): Alipay, WeChat (China), Grab (Southeast Asia).
- Fees: no enumerated list of removed fees exists. Only general statements: "Most account fees
  have been removed over time" (L544); "Fees for transactional accounts are very low across the
  industry" (L783); CCCFA "has contributed to the trend of reducing the amount and number of fees"
  (L231); no fee for account switching (L790, L817); mortgage discharge fee $100 (L762).

## Definitions, rules, thresholds and scope exceptions (verbatim, short)

- Deposit accounts (fn 11, L169): "references to 'deposit accounts' include overdraft facilities",
  quoting the PIP page 5: "includes transaction, savings, and term deposit accounts, as well as any
  associated overdraft facilities...".
- Core services (L423): "ANZ characterises these products as 'core' personal banking services"
  (deposit accounts and home loans).
- Relevant profit measure (L60-61): "total profit is not the relevant measure - total profit simply
  reflects the scale of a business. What matters is unit profitability, and in the banking context
  in particular, return on equity."
- Comparison basis (L74-80): PIP analysis is "an aggregate country versus country comparison, rather
  than a firm-to-firm comparison"; Incenta did "a firm-to-firm comparison of ANZ's returns (as a
  proxy for New Zealand banks)".
- NIM (L319): "NIM is 'raw' and by itself a poor indicator - risk adjusted NIM is a better indicator".
- Goodwill (L349): RBNZ and World Bank data "also includes goodwill in its denominator, which is
  appropriate"; the Commission "has previously expressed a view that goodwill should not be included
  in the denominator" (fn 21).
- Share of registration (L213): "measures a provider's share of registrations of new home loans".
- Share of commitments (L214): "measures a provider's share of firm offers of finance to a mortgage
  applicant, using the RBNZ definition of when the provider sends loan documents to the applicant or
  the applicant's solicitor."
- Market share caveat (L204): "market share estimates are not a definitive indication of the health
  of competition in a market".
- CCCFA fee rule (L231): "fees charged on home loans and overdrafts closely reflect lenders' cost
  recovery with no ability to price on commercial terms that incorporate a profit margin"; exception
  in the same paragraph: "(with the exception of fees that are subject to the reasonableness limitation)".
- CCCFA switching exception (L752): "If another provider can offer a customer a better rate on an
  existing loan amount, the customer can switch without the new bank being required to complete the
  affordability inquiries in the Regulations (although reasonable inquiries are still required)."
  Limit: "only in simple transactions. The exception does not apply where a customer wishes to
  increase their lending - even by a small amount."
- BS11 (L148): "The main objective of BS11 is to ensure that outsourcing arrangements entered into by
  a large bank do not compromise the options available for resolving bank failures".
- PPGs (L249-250): "do not themselves create enforceable requirements"; L252-254 "New Zealand-owned
  banks that do not have an Australian parent do not experience the same impact."
- LVR (L135): "the LVR restrictions operate by restricting supply of loans to customers with a high LVR".
- Monetary policy (L372): "the actions taken by the central bank to influence monetary conditions in
  the economy".
- Switching vs multi-banking: L688 "joining another provider often does not involve 'switching' in
  the sense of leaving one bank and joining another - rather, 'multi-banking' is common"; L711
  "customers do not often switch banks completely"; L746 "switching (or at least, taking up services
  from a new provider)"; L769 "This movement of funds is switching, even if the customer does not
  formally close their account."; L714 "switching data is a poor proxy for customers' engagement".
- "Main bank": used at L711 without a definition. L842: customers "do not need to use their ANZ
  account as their 'primary' bank account".
- Deposit switching data (L769): "ANZ does not hold current data about switching trends for deposit
  accounts"; the switching-process count "is not a reliable indicator".
- Table 2 membership rule (L789): "either Payments NZ members that participate in industry account
  switching arrangements via registration on the Payments NZ Account Switching Notifications
  Register, or non-member banks that have agency banking arrangements via a Payments NZ member."
  Outside Table 2 (L792): "they open and close the accounts themselves".
- Off-site Smart ATM (fn 29, L528): "ATMs that are not connected to a branch".
- Brokers (L564, L572): "Mortgage brokers, more commonly known as mortgage advisers"; "Brokers do
  not charge consumers ... remunerated through commissions paid by the ultimate loan provider."
- Home loan tie (L835): "ANZ requires home loan customers to have a transaction account with us";
  L844 "ANZ may impose a condition ... that the customer's salary must be direct credited to an ANZ
  account" (for a special interest rate). Packages are "not tied and do not form a true bundle" (L849).
- Early Repayment Recovery (L764): "compensates ANZ for the cost of changing hedging arrangements".
- NBDT (L457): non-bank deposit takers; "not as close competitors as other larger banks".
- LSAP (L327): Large Scale Asset Purchase programme. OCR (L154): official cash rate.
- Regional approach (L518, L602): "We do not vary our competitive approach between regions";
  "our pricing is agnostic of location".

## Dated regulatory and market events

- 2003: ANZ acquisition of the National Bank; cleared by the Commission (L348-351).
- January 2018: RBNZ BS19 high-LVR framework document date (fn 15, L225-226).
- 2019: RBNZ Capital Review decisions (L335; fn 18, 19, 33); 17 May 2019 NZBA submission on "How
  much capital is enough?" (fn 22).
- 1 October 2021: new capital requirements begin phasing in; seven-year period; to 2028 (L332, L389).
- March 2021: financial advice changes introduced (L894).
- December 2021: CCCFA changes "introduced strict affordability inquiries" (L751, L894); "2021
  changes to the CCCFA" (L150).
- April 2023: ANZ Simple Switch pilot launched, described as "under the CCCFA exception" (L753).
- May 2023: "constrained exception for switching was introduced in the CCCFA" (L752). The document
  prints April for the pilot and May for the exception; no reconciliation is given.
- 22 May 2023: Payments NZ item on seven-day payments (fn 51).
- 10 August 2023: Preliminary Issues Paper (fn 1). 7 September 2023: this submission.
- 1 September 2023: Pepper Money / HSBC NZ mortgage portfolio announcement (L681, fn 38).
- Undated: BS11 (L148); Covid-19 quantitative easing (L158); wage subsidy scheme (L323); "newly
  introduced Retail Payment System Act" (L433); Australian Government 'pause' on CDR roll-out (L658);
  regional banking hub trial with no regional branch closures "until the end of this year" (L514);
  "proposed open banking reforms" (Q18, L638).
- Statutes named: Commerce Act 1986 s 48 (L67); CCCFA (L131); Tax Administration Act 1994 (L265);
  FATCA (US) (L275); Te Ture Whenua Māori Act 1993 (L298); Financial Markets Conduct Act 2013 (L575);
  Retail Payment System Act (L433).

## Statements about other named organisations (kept apart from statements about ANZ)

- ASB, BNZ, Kiwibank, Westpac: closest competitors (L32, L442); "account for most new mortgage
  registrations" (L442); all four in Table 2 (L798-803). ASB appears only at L32, L442, L798.
- Kiwibank: "references to the larger banks should include Kiwibank"; self-reported home loan share
  7.5% (L183, fn 12 L198).
- BNZ (as a bank; "BNZ" also occurs inside "RBNZ"): L32, L442, L798, and L680 Squirrel's on-call
  account "which ANZ understands is held on trust in a BNZ account".
- Westpac: besides L32, L442, L802, only fn 35 (L669) "Westpac estimates cost of CDR compliance to
  be $200m" (Australian CDR).
- TSB: Table 2 only (L804, "TSB (Taranaki Savings Bank)"). Rabobank: Table 2 only (L804, "RABO
  Bank*", agency arrangement). Heartland, SBS, NBS, The Cooperative Bank, Bank of China, China
  Construction Bank (NZ) Ltd, Citibank: Table 2 only.
- HSBC: Table 2 (L807); selling NZ mortgage portfolio to Pepper Money (L681, L690).
- ICBC: registered as a bank in NZ in 2020 (L680); Table 2 as "ICBC (NZ) Ltd" (L807).
- "Other larger banks": ANZ's refinance campaign committed "to match other larger banks advertised
  fixed rates" (L472). "Other banks have developed discount offerings on loans for sustainable
  energy purposes" (L537); "our competitors have followed ANZ's Good Energy Home Loan" (L938).
- Smaller banks and non-banks: 16.43% of new registrations (L444); "meaningful competitive
  constraint" (L32); NBDTs perceived "as less safe or of lower quality than banks" (L457).
- Fintech / new entrants: L665-681 (list above); L902 Wise "has won industry recognition for its
  domestic service quality (MoneyHub)", Revolut "a 'fast follower' to Wise"; L899 Square One "uses
  our offering to supply its own-branded accounts for children"; App para 96 (L634) "Many of
  the new entrant providers ... do not offer services that give rise to higher regulatory burdens".
- Digital disruptors (L414): "we disagree that they have a more customer-centric approach than
  existing participants".
- RBNZ: policy statement quoted (L106-111, fn 10); BS11 (L148); OCR and QE, NZ$53 billion (L154-158);
  Balance Sheet Survey (L212); commitments definition (L214); capital requirements and the 20.5 bp
  estimate (L332-335, L389-391, fn 23); "licenced approximately 86 insurance companies" (L432);
  Central Bank Digital Currency Forum (L558); "acknowledged ... they were conservative compared to
  other countries' minimum capital ratios" (L632, fn 33); dashboard switching data (L33, L729).
- Commerce Commission: member of the Council of Financial Regulators (L106); PIP analysis "largely
  based on existing work conducted by the RBNZ and the World Bank" (L61); in the grocery study
  "focused on its bottom-up estimates and expressed doubt about the validity of international
  comparisons" (L86, fn 7); earlier studies of fuel, supermarkets, building products (L206); "has
  used NIM as an indication of earnings" (L319); goodwill view (L349, fn 21); cleared the National
  Bank acquisition (L351); regulatory importance "underemphasised" (L28, L139, L220); economic
  conditions not canvassed (L161); consumer survey (L173).
- Incenta Economic Consulting: all profitability figures (L71-94, L352-365).
- KPMG: 13.40% vs 15% (L317-318). The Treasury: quoted para 81 (L329). World Bank: CR3 (L208),
  Figure 1 (L353). NZBA: ~$20 billion capital (L389, fn 22).
- APRA / Australian regulators: L196, L229, L240-258, L960. Inland Revenue: L270-292.
- Australian Government and Federal Minister Stephen Jones: L658, L669. Open Banking Limited (UK),
  Lloyds Banking Group PLC: L659, L670-672. Reserve Bank of Australia: L955, L962.
- Payments New Zealand / API Centre: L557, L788-789, L867, L899-900, L952. NZBA, Financial Services
  Council, BusinessNZ, TVNZ, MBIE, Banking Ombudsman Scheme: L556-558.
- Others: Apple (L50, L869); Spark, "initially" the partner biller for View Bills (L865); Valocity
  (L215); Silicon Valley Bank (L395); Age Concern (L591); Solomon Group (L605); NCR Corporation
  (L506); Business Desk (L198); Interest.co.nz, Canstar, Consumer.org.nz and the other comparison
  services (L821-829); ANZ Group / "ANZ in Australia" and 1835i (L900, L955-960).

## Hedged claims (claim | hedge | what the hedge attaches to)

- L84 | "it is suggestive of normal returns" | "suggestive" qualifies the normal-returns inference;
  L94 states "consistent with ANZ's profits being normal" without that word.
- L71 | Incenta: PIP analysis "does not support a position that ... persistently high profitability" |
  negative framing; attributed to Incenta, not asserted as ANZ's own finding.
- L121 | regulatory objectives "may enhance competition, impede it or be a mix of the two" | "may" on
  the direction of effect.
- L141 | "small changes in one area may have large, unexpected outcomes in another" | "may" on outcomes.
- L184 | "we have not yet seen the full impact of their presence" | "not yet" on new entrants' impact.
- L329 (Treasury quote) | "This effect may have been amplified by higher liquid assets / settlement
  cash" | "may have been" attaches to amplification by LSAP; "often boost" qualifies the base effect.
- L336-337 | low/no-fee trend "is partly driven by the CCCFA" | "partly" on causation.
- L351 | clearance "suggesting the goodwill did not include any capitalised market power rents" |
  "suggesting" on the inference from clearance.
- L400-404 (fn 23) | "The final calculation for ANZ is unknown" | attaches to ANZ's own lending-rate
  impact, not to the RBNZ's 20.5 bp assumption.
- L416 | "There may be aspects of certain digital disruptors that appeal to certain customers" | "may".
- L444 | "around 13%" | approximation on the October 2020 value only (16.43% is exact).
- L457 | "customers tend to perceive NBDTs as less safe" | "tend to".
- L587 | "there may be some population groups ... not experiencing all the benefits" | "may be".
- L618 | consumers "may be worse off when branch networks reduce" | "may", conditional on access difficulty.
- L641 | "We do not consider customer data access, in and of itself, will have any material impact on
  the prospect of large-scale entry" | firm negative; "in and of itself" limits scope.
- L640, L643-644 | open banking "is likely to positively impact"; "has the potential to"; "is likely
  to improve" | all attach to future effects.
- L656 | "development and uptake of open banking may be slow" | "may", "Based on overseas experience".
- L658 | "We understand that the Australian ... regime has cost ... well over $1bn" | "We understand"
  attaches to the cost figure and to the adoption barriers.
- L659 | "we understand uptake is increasing"; "the UK estimates"; "appears to have been costly";
  "estimating ... up to GBP1.5 billion" | each attaches to its own figure.
- L666 | Revolut cards and bill payment services "are likely to be launched in New Zealand soon" |
  "likely" on a future launch; the 2023 payments launch is stated as fact.
- L680 | Squirrel account "which ANZ understands is held on trust in a BNZ account" | "understands"
  attaches to the custody arrangement, not to the 2023 launch.
- L746 | "in general, switching (or at least, taking up services from a new provider) is readily
  achievable" | "in general"; parenthesis narrows the claim.
- L748 | high-interest environment "may make it more difficult" to pass affordability checks | "may".
- L751 | "This drop may have been because of an increase of the switching burden" | "may have been"
  attaches to the cause; the drop ("we observed ... down approximately 20% on average") is stated
  as observed, with "although this dip has subsequently reduced".
- L752 | "This exception may ultimately reduce the impact"; "it is also possible that customers may
  perceive" | "may" on the exception's effect and on customer perception.
- L766 | "ANZ understands that in many cases the costs ... are often met by a cash contribution
  offer from their new bank" | "understands", "often".
- L809 | "ANZ surmises that many people choose instead to 'multi-bank'" | "surmises" on the reason
  for low use; "used in only low volumes" is stated as fact.
- L833 | "Those very limited exceptions have no impact on competition" | unhedged.
- L844 | "ANZ may impose a condition" (salary credit) | "may" = discretion, not uncertainty.
- L905 | "ANZ has not seen any basis to view innovation in New Zealand to be less advanced" |
  absence-of-evidence framing.
- L909 | "We link the current lack of demand ... to New Zealand not yet embracing a 'digital
  identity'" | ANZ's attribution; "To date" limits the observation.
- L922 | "We expect these developments may increase demand" | "expect ... may".
- L952 | "some innovations may be impeded" | "may", alongside "innovations are continuing".

## Footnotes (53; marker line -> text line)

Footnotes sit at the foot of each printed page, i.e. inside the body text flow.

| Fn | Marker | Text | Content |
|---|---|---|---|
| 1 | L21 | L37 | Commerce Commission, Preliminary Issues paper (10 August 2023) |
| 2 | L34 | L39 | RBNZ, Bank Financial Strength Dashboard |
| 3 | L36 | L41-42 | REDACTED |
| 4 | L47 | L65 | REDACTED |
| 5 | L58 | L67 | Commerce Act 1986, section 48 |
| 6 | L77 | L87 | PIP at [45] and [48], "and below at paragraph 1919" [sic] |
| 7 | L86 | L88 | Grocery study executive summary (8 March 2022) p 8; final report 3.58 onwards |
| 8 | L102 | L114 | PIP at [45] |
| 9 | L104 | L116 | PIP at [48] |
| 10 | L106 | L118 | RBNZ, Our approach to policy |
| 11 | L167 | L169 | Definition: 'deposit accounts' include overdraft facilities (PIP p 5) |
| 12 | L183 | L198 | Business Desk, interview with Kiwibank CEO Steve Jurkovich (25 August 2023) |
| 13 | L204 | L223 | Commerce Commission, Mergers and Acquisitions Guidelines, May 2022, [13]-[14] |
| 14 | L210 | L224 | World Bank Databank: Global Financial Development |
| 15 | L214 | L225-226 | RBNZ BS19 (January 2018) |
| 16 | L318 | L324 | KPMG FIPS: Banks - Review of 2022 (March 2023), page 21 |
| 17 | L331 | L339 | The Treasury, Windfall gains report (10 February 2023), at [81] |
| 18 | L334 | L341 | RBNZ, Capital Review: Decisions 2019, page 2 |
| 19 | L335 | L343 | RBNZ, Capital Review: Decisions 2019, at [54] |
| 20 | L347 | L353 | Figure 1 data source; country-level limitation |
| 21 | L349 | L355 | Grocery Final Report (8 March 2022), at [3.33] |
| 22 | L391 | L398 | NZBA submission to RBNZ (17 May 2019), Appendix A of Appendix 1 |
| 23 | L391 | L400-404 | Qualifier on the 20.5 bp figure (two bullet reasons) |
| 24 | L412 | L425 | PIP at [123] |
| 25 | L416 | L427 | PIP at [125] |
| 26 | L444 | L449-450 | REDACTED |
| 27 | L500 | L504 | REDACTED |
| 28 | L501 | L506 | NCR Corporation article (21 December 2020) |
| 29 | L513 | L528 | "ANZ has 52 off-site Smart ATMs" |
| 30 | L514 | L529 | "New Zealand Banking Association, Regional Banking Hubs pilot" |
| 31 | L564 | L565-566 | ANZ 2023 Half Year Results pack (5 May 2023), page 134 |
| 32 | L613 | L626 | REDACTED |
| 33 | L632 | L645 | RBNZ, Capital Review: Go-to-Guide 2019, page 7 |
| 34 | L633 | L647 | RBNZ, Applying for Bank Registration; Applying for a non-bank deposit takers licence |
| 35 | L658 | L669 | Stephen Jones MP address (7 June 2023); WS02 (3 January 2019), Westpac $200m |
| 36 | L659 | L670 | Open Banking Limited, New Impact Report (30 March 2023) |
| 37 | L659 | L672 | Lloyds Banking Group PLC, Response to CMA consultation (April 2020) |
| 38 | L681 | L690 | Interest.co.nz (1 September 2023), "$1.4 bln NZ mortgage portfolio" |
| 39 | L687 | L692 | REDACTED |
| 40 | L688 | L694 | REDACTED |
| 41 | L700 | L723 | REDACTED |
| 42 | L713 | L725-726 | REDACTED |
| 43 | L713 | L728-729 | REDACTED, then RBNZ dashboard July 2023 sentence |
| 44 | L718 | L730-731 | ANZ 2023 Half Year Results p 134; "remains correct as of July 2023" |
| 45 | L719 | L733 | REDACTED |
| 46 | L721 | L735 | REDACTED |
| 47 | L740 | L754 | REDACTED |
| 48 | L744 | L756 | REDACTED |
| 49 | L772 | L775-776 | REDACTED |
| 50 | L788 | L793 | Payments NZ, Switching banks |
| 51 | L868 | L880 | Payments NZ, Payments every day arrives in Aotearoa New Zealand (22 May 2023) |
| 52 | L946 | L948 | PIP at [132] |
| 53 | L956 | L962 | Reserve Bank of Australia, Australian CBDC Pilot project report (August 2023) |

Footnotes that qualify, restate or change the basis of a body figure
- fn 11 (L169): widens "deposit accounts" to include overdraft facilities for the whole document.
- fn 20 (L353): Figure 1 is country-level; "not possible to control for bank type".
- fn 22 (L398): the ~$20 billion is sourced to an NZBA submission on the RBNZ consultation paper
  "How much capital is enough?" dated 17 May 2019; the 20.5 bp figure is sourced to the RBNZ's
  "Capital Review: Decisions 2019" (fn 19), for which D02 gives no day or month.
- fn 23 (L400-404): the 20.5 bp figure is an RBNZ assumption "in 2019"; ANZ's own outcome "unknown".
- fn 29 (L528): supplies a count (52) that the body does not give.
- fn 35 (L669): body says "well over $1bn" for Government and major banks; the footnote prints
  "more than $200 million" (Federal Government) and "$200m" (Westpac estimate). No total is printed.
- fn 38 (L690): supplies the portfolio size ($1.4 bln) absent from the body.
- fn 43 (L729): restates the L33 switching figures and attaches them to the multi-banking sentence.
- fn 44 (L730-731): source is the 5 May 2023 half-year pack, while the body says "As of July 2023";
  footnote adds "ANZ confirms this remains correct as of July 2023".
- fn 31 (L565-566): 57% is "Recent data" in the body; the source is dated 5 May 2023.
- Twenty-one redaction markers in total; 15 footnotes are wholly or partly blanked (3, 4, 26, 27,
  32, 39-43, 45-49), so every figure they support has no stated source.

## Internal cross-references and aliases

- Intro para 5 -> Q9-11, Q25 (L52). Intro para 33 -> Appendix 1 (L164). App para 22 -> Intro paras
  "10 to 17" (L316). L231 -> Q5 (NIM). L184 -> Q19. L196, L229 -> Q3. L370 -> Q10, Q11, Q25.
  L410, L419 -> Q25-29. L416 -> Q15. L455 -> Q21, Q10. L514 -> Q15. L539 -> Q25. L570 -> Q23.
  L607 -> Q4. L616 -> Q10.4. L634 -> Q7. L636 -> Q18. L641 -> Q17. L676 -> para 152.12 (L896-899).
  L769, L781-782 -> Q23. L790, L817 -> Q22. L830 -> Q13. L831 -> Q18. L860 -> Q30. L909 -> Q27.
  L922 -> Q26. L938 -> Q15, Q25, Q27. L958 -> Q25.
- PIP locations cited: [45], [48], [123], [125], [132], paragraph 206, page 5, Tables 1 and 2,
  Figure C3, Table C5, Attachment C.
- Aliases: ANZ Bank New Zealand Limited = ANZ = "ANZ Bank" (Table 2); ANZ Group / "ANZ in
  Australia" / "our Australian parent company" are the parent, distinct from ANZ. Commission = New
  Zealand Commerce Commission. RBNZ = Reserve Bank. NZBA = "New Zealand Bankers' Association"
  (L557) = "New Zealand Bankers Association" (L398) = "New Zealand Banking Association" (L529).
  Payments NZ = Payments New Zealand. Wise "(formally Transfer Wise)" (L680) = "(formerly Transfer
  Wise)" (L902). Pepper = Pepper Money. ICBC (NZ) Ltd = Industrial and Commercial Bank of China
  Limited. goMoney = "ANZ goMoney app". CCCFA, AML, LVR, NIM, OCR, LSAP, NBDT, CDR, CRS, FATCA,
  PPG, APRA, PTE, CBDC ("Central Bank Digital Asset (CBDC)" at L955; "Central Bank Digital Currency
  Forum" at L558). Good Energy Home Loan: L420, L537, L873, L938. Banking hubs: L419, L514, L618.

## Gaps (missing source text, not unread text)

- Annex 1 (Incenta report) is "Provided separately" and absent; every Incenta figure in D02 is
  second-hand (12.3%, 12.2%, 12.1%-12.8%).
- Figure 1 bar values and Figure 2 chart data are absent (labels/caption only). Visual originals
  could not be inspected: unresolved.
- Redactions: fn 3, 4, 26, 27, 32, 39, 40, 41, 42, 43 (part), 45, 46, 47, 48, 49; body L149
  (after "$580m"), L150 (CCCFA cost), L445-447 (end of para 52), L491 (marketing budget share),
  L502 (contact centre growth), L581 (para 84 entire).
- L812: "An overview of the process is accessible here" - link target lost.
- fn 6 "paragraph 1919" garbled in the source itself.
- Unread ranges: none.
