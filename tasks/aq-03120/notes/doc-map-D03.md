# aq-03120 - D03 document map (ASB submission) - navigation only

Mapper file for one document. Line numbers are `text/D03.txt` line numbers (the Read tool's numbering; line 1 is the
`# D03 | docs/...` header added by extraction). Questions quote the document, never this map.

## 0. Identity, binding, coverage ledger

- Source: `docs/nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt`; local id D03; "Doc 3" on the task page.
- Reuse binding: manifest sha256 `3ca9a1af3015b11a8a5a2766f581ab8c097281994a119f8d90e60620f2455e46`, method `text`, pages null, chars 159310. `notes/intake.json`: captured_sha256 = source_sha256 (same value), incomplete false, gap_characters 0, matches_capture true.
- Title (L4): "ASB response to the Commerce Commission's Preliminary Issues paper for the market study into personal banking services". Running header "Public Version" + page number on every page break (48 headers; page numbers 2-48 appear as bare lines or glued to the next sentence).
- Written/submitted by: ASB Bank Limited ("ASB") (L6). Addressee: Commerce Commission ("Commission"). Paper responded to: Preliminary Issues paper ("PIP").
- Attached report: "NERA Report" (L100, L429, L1292) is referred to as attached; its text is NOT in D03 (the file ends at L1306 "-----" after Q32). Only ASB's summary of it (L99-147) is present. Missing source text, not unread coverage.
- Date of submission: none printed anywhere in D03. Latest dated events inside the text: "1 September 2023" (L980), "9 August 2023" (L1255), "3 July 2023" (L1160), "On 24 July this year" (L944, year not printed), "As at June 2023" (fn18 L184, fn76 L1176), "June 2023" (L83, L1117).
- Fiscal convention: "FY23", "FY22", "FY21", "FY18", "FY2023" are used for ASB and for other banks without any definition or stated year-end in D03 (grep for "financial year|fiscal|30 June|year end" finds only L1128 "Over the past financial year"). Other banks' periods as printed: SBS "year to 31 March 2023" (L18, L585); Kiwibank fn40 URL "june-year" (L574); Heartland "Q1 and Q2 of FY2023" (L25).
- Edition: "Public Version"; confidential material replaced by `[Redacted]` (59 occurrences).
- Structure in one line: Executive Summary (L5-154) + responses to Commission questions 1-32 (L158-1304). No appendices in the text.
- Coverage ledger (lines read in full, sequentially): 1-150, 150-299, 300-449, 450-599, 600-749, 750-899, 900-1039, 1040-1179, 1180-1306 (end of file). Complete.
- Lines remaining unread: none.
- Extraction spot-checks against `docs/` original (also plain text): original line N = text line N+2. Checked present and identical in the original: table row "***Privacy Act 2020***" (orig L335 / text L337); Figure 10 axis text "Deposits QoQ Change" (orig L642 / text L644); footnote 76 "As at June 2023" (orig L1174 / text L1176); footnote 81 (orig L1266 / text L1268). Page count: 48 by the running headers in both original and extraction (no other page structure to compare). Charts and colour marking are absent from the original capture itself, so they cannot be inspected here (unresolved visually).
- Not done by this mapper (caller instruction: D03 only): searching D01, D02, D04-D06 for repeats of D03 facts.

## 1. Structure (headings, line ranges, Commission question numbers)

Executive Summary (L5-154), own paragraph numbering 1.1-5.3:
- L5-7 intro (ASB facts).
- L9-62 "1. Ngā Tauwhāinga ā-Mākete Competition" paras 1.1-1.13 (footnotes 1-11 interleaved at L19-20, L34-40, L52-58).
- L64-72 "2. Te Pikinga o Ngā Waeture The increasing level of Regulation" paras 2.1-2.5.
- L74-96 "3. Ngā Kiritaki Customers" paras 3.1-3.7.
- L98-147 "4. Te Huamoni ō Ngā Pēke Bank Profitability" paras 4.1-4.5 (summary of NERA Report; fn 12-14 at L135-138; Figures 2-3 captions L142-144).
- L149-154 "5. Te Whakawhitinga o Ngā Raraunga Pūtea Kua Whakaaetia Open Banking" paras 5.1-5.3.

"Pātaitai Questions" (L158 onward). Paragraph numbers restart per Commission question (so "1.1", "3.1", "4.1" etc. occur both in the Executive Summary and in the Questions part - cite with the part name). Bracketed tags like "[1.1]" after a sub-question are the PIP's own sub-question references.
- L159 group heading "Overview of personal banking services in New Zealand"
  - Q1 L160-217 (structure of the sector; sub-question "[1.1]" other participants L164-217) and sub-question "[1.2]" measures of concentration L219-223 (paras 1.3-1.4).
  - Q2 L225-227 (regulatory environment) - one line: refers to Q3.
  - Q3 L229-378 (other legislation; paras 3.1-3.11; regulation table L245-369; fn 22-24).
  - Q4 L380-426 (impact on Māori; paras 4.1-4.4; fn 25).
  - Q5 L428-429 (financial performance data / Attachment C) - one line: "see the attached NERA Report and the comments in the Executive Summary".
  - Q6 L430-451 (factors influencing financial performance; list (a)-(j)).
  - Q7 L453-494 (digital innovation/disruption; paras 7.1-7.8; fn 26-35; Figure 4 caption L489-490).
- L498 group heading "Question on the services that the Commission will focus on in the study"
  - Q8 L499-516 (choice of services; paras 8.1-8.7; fn 36-38).
- L520 group heading "Questions on the nature of competition"
  - Q9 L521-633 (intensity of competition between groups; paras 9.1-9.32; sub-headings "Competition among the registered banks" L532, "Competition from smaller banks and fintech" L581 (glued to the Figure 9 source line), "Smaller banks" L584, "Fintech / product specific competitors" L599 (glued to end of para 9.22), "Competition in transaction and deposits" L607; fn 39-52; Figures 5-10).
  - Q10 L634-736 (how providers compete; paras 10.1-10.22). PIP sub-questions: "[10.1]" same effort gaining/retaining L638; "[10.2]" which services more/less competition L680; "[10.3]" national branding L704; "[10.4]" physical presence L725; "[10.5]" regional variation L734. Stray Figure 10 axis/legend text sits inside Q10 at L644-645. Figures 11-13.
  - Q11 L738-800 (how varied are home loans and deposit accounts; paras 11.1-11.5; fn53 L752; Figure 14 caption L800).
  - Q12 L801-811 (interactions between providers; para 12.1 (a)-(c); fn54 at L836).
  - Q13 L812-818 (mortgage brokers / intermediaries; paras 13.1-13.3).
- L820 group heading "Questions on how competition works for different population groups"
  - Q14 L821-822 (segmentation; one paragraph).
  - Q15 L823-904 (population groups; paras 15.1-15.18; sub-headings "ASB Community Council" L827, "NZBA Vulnerability Working Group" L851, "Good Shepherd New Zealand - Economic Harm Support Service Pilot" L857, "Overcoming financial abuse" L869, "Abuse in transactions" L874, "ASB Community Bankers" L878, "Other ASB programs of note" L886, "General comments" L900; fn 55-56).
- L906 group heading "Questions on conditions of entry and expansion"
  - Q16 L907-920 (conditions of entry; paras 16.1-16.2 (a)-(d)).
  - Q17 L922-934 (regulatory environment and entry; paras 17.1-17.6; fn57).
  - Q18 L938-964 (open banking reforms; paras 18.1-18.6).
  - Q19 L966-982 (entry, expansion, exit examples; paras 19.1-19.6; fn 58-63 at L972-976 and L1012-1014).
- L984 group heading "Questions on consumer search and switch"
  - Q20 L985-1021 (selecting first bank; paras 20.1-20.5; sub-headings "Home loan customers" L987, "Transaction and deposit account customers" L1001; Figures 15-18, all redacted).
  - Q21 L1023-1043 (how often/why search "[21.1]" and switch "[21.2]"; paras 21.1-21.5; sub-headings "Home loan" L1029, "Transaction and deposit accounts" L1038, "General points regarding switching" L1041; 21.1-21.3 and Figure 19 redacted).
  - Q22 L1045-1062 (factors prompting/hindering search and switching; paras 22.1-22.7; fn64).
  - Q23 L1064-1087 (tools to search, compare, switch; paras 23.1-23.7; Figure 20 caption L1083).
  - Q24 L1089-1101 (tied or bundled services; paras 24.1-24.2 (a)-(d); fn65).
- L1105 group heading "Questions on innovation"
  - Q25 L1106-1178 (innovation over past five years; paras 25.1-25.7; sub-headings "Focus on supporting digital" L1112, "Key innovations" L1119, "Home Lending and Home Lending Brokerage" L1143, "Digital banking (digital personal and digital home lending, and neo-banking)" L1157, "Payments (BNPL, digital wallets and merchant payment solutions)" glued to end of L1160; fn 66-77).
  - Q26 L1166-1207 (innovation vs overseas; paras 26.1-26.4; fn 78-80).
  - Q27 L1211-1222 (latent unmet demand; paras 27.1-27.3).
  - Q28 L1223-1231 (incentives to innovate; paras 28.1-28.4).
  - Q29 L1233-1259 (impediments to innovation; paras 29.1-29.9; fn81 at L1268).
  - Q30 L1261-1276 (ownership structure; paras 30.1-30.6).
- L1278 group heading "Questions on other analyses, factors, and priority"
  - Q31 L1279-1287 (other analyses or factors; paras 31.1-31.4).
  - Q32 L1289-1304 (priorities; paras 32.1-32.4). L1306 "-----" end of file.
- Questions answered only by cross-reference: Q2 (to Q3), Q5 (to NERA Report and Executive Summary). Questions with largely redacted answers: Q20, Q21.
<!-- STRUCT -->

Internal cross-references printed in the text: Exec Summary 2.2 -> "question 29 below" (L66); Q7 7.2 -> "question 16 and elsewhere" (L460); Q7 7.7 -> "response to question 26" for the World Bank publication (L487); Q7 7.8 -> "question 18 below" (L491); Q7 7.1 -> "question 1 above" (L458); Q2 -> Q3 (L227); Q5 -> NERA Report + Executive Summary (L429). Later: Q13 13.3 InvestNow "(discussed below)" (L818); Q15 15.1 -> "question 4 above" (L825); Q16 16.1 -> "questions 2 and 3" (L909), 16.2 -> "question 17" (L911, L913); Q18 18.5(a) "As noted earlier, a single entity overseeing all aspects of cyber security" (L948, back to L236); Q19 19.1 -> "questions 1 and 9 above" (L968); Q22 22.1 -> "question 21 above" (L1047); Q23 23.5 -> "question 13 above" (L1084); Q25 25.1 -> "question 1" (L1108); Q28 28.2 -> "survey data in response to question 20" (L1227; that survey data is redacted); Q32 32.2 -> Executive Summary and NERA Report (L1292).

## 2. Figure inventory (every quantitative statement, in line order)

Format: `Lnnn | value as printed | what / scope words | period or as-at | attributed to | notes`. "ES" = Executive Summary part.

### ES intro and ES 1 Competition (L5-62)
- L7 | "more than 176 years" | ASB has offered banking services to New Zealanders | to date | ASB | duration.
- L7 | "more than 6,000 people" | ASB employees "across New Zealand" | "Today" | ASB.
- L7 | "more than 1.5 million" | ASB customers - "personal, business and rural customers" (not personal only) | "Today" | ASB.
- L11, L13 | "five major banks" / "five, large, well-known players" | count of major banks (not named here) | - | ASB | restated L524, L533.
- L14 | "2022" ; "100%" | Kiwibank "move to 100% direct Government ownership" | 2022 | ASB | restated L570 as "New Zealand Government acquiring 100% of Kiwibank's parent company in 2022".
- L14 | "$225 million" | Kiwibank cash injection "to speed up growth" | "recently announced" | Kiwibank media release (fn1, L19) | restated L571 (fn41, same URL) with added source of funds.
- L18 | "approximately 12%" | SBS "total home lending" increase | "year to 31 March 2023" | SBS media release (fn2, L20) | restated L585 inside a quotation with dollar levels.
- L18 | "closer to 3.5%" | "broader industry growth rate" (home lending) | same period | SBS release (fn2); in L585 it is inside the quoted SBS release | hedge word "closer to".
- L20 | "16%" (inside fn2 URL text fragment: "...16%25%20from%20the%20previous%20year") | not explained in body | - | SBS URL | URL fragment only; also L586.
- L24 | "1.6x system (market) growth" | TSB residential lending growth relative to market | FY23 | TSB media release (fn3, L34-35) | restated verbatim L585 (para 9.20, fn44).
- L24 | "a further 6% to $6.2 billion" | TSB "lending assets" | FY23 | TSB media release (fn3) | restated L585.
- L25 | "highest growth rate in retail deposits of all main and domestic banks in New Zealand" (ranking) | Heartland | "Q1 and Q2 of FY2023" | "based on balance sheet data from the Reserve Bank of New Zealand (RBNZ)"; fn4 Heartland investor presentation slide 18 (L37-39) | restated L585 as "Q1 and Q2 of FY23".
- L26 | "8% growth in mortgages" | The Cooperative Bank | FY23 | Cooperative Bank Annual Results (fn5, L40) | "well above the market average"; restated L599 with dollar amounts.
- L27 | "late 2021" | when "the OCR began to rise" | - | ASB.
- L28 | "up 4.2%" | ASB "12-month home lending rates" | "since October 2021" (to submission) | ASB own | printed with "%" (not "percentage points"); ASB only.
- L28 | "increased 4.6%" | ASB "12-month term deposit rates" | "since October 2021" | ASB own | printed with "%"; ASB only. Claim attached: "passed through interest rate rises at a greater rate on term deposits than it has on home loans" (L27).
- L28 | no number | "a significant volume of new mortgages being written below ASB's current cost of capital" | - | ASB.
- L30 | "[Redacted]" | ASB marketing spend | FY23 | ASB | redacted.
- L45 | "2022" ; "125 countries" | World Bank publication "Global Patterns of Fintech Activity and Enabling Factors": cross-country regression analysis of 125 countries, "Fintech Activity Index" | 2022 | World Bank (fn6, L52).
- L45 | "5 out of 74 countries" and "4 out of 125 countries" | New Zealand's rank on the two measures | 2022 publication | World Bank (fn6) | "two different measures to rank countries"; cross-referenced again at L487 (and "question 26").
- L47 | "5% market share" | Macquarie, Australian mortgage market, "in a comparatively short period" | "recently" | fn7 (L53, macquarie.com.au) | restated L465 with a different footnote source (fn29, AFR article dated 2023-02-10 in URL).
- L47/L54 | "November 2022, p. 5" | US Treasury report date/page | - | fn8.
- L55, L57, L58 | "2023, at page 17"; "2020, at page 7"; "at page 5" (URL shows 2018-08) | World Bank, OECD, US Treasury citations | - | fn9, fn10, fn11.

### ES 2 Regulation, ES 3 Customers (L64-96)
- L66 | "$[Redacted] million" | ASB spend "on regulatory initiatives" | "in FY23 alone" | ASB | redacted; restated L233 (Q3 para 3.3), also redacted.
- L83 | "more than 12,000 distinct customers" | customers "identified as likely to be particularly impacted" contacted by ASB re refixing home loans | "in recent months" | ASB own.
- L83-87 | "more than 6,000 such customers" | customers who had not refixed and reverted to floating, contacted by ASB | "July 2021 to June 2023" | ASB own | split across page break (L83/L87).
- L87 | "more than $1.1 million in annualised cost savings" | for those customers | July 2021 to June 2023 | ASB own.
- L89 | "[Redacted]" x3 | Home Central visits "in the last month alone"; visits to manage repayments; visits to manage fixed rate rollovers | last month | ASB | all redacted.
- L94 | "late 2019" | ASB Community Council introduced; "meets quarterly"; chaired by ASB's CEO (L95) | - | ASB.
- L96 | "2022" | Financial Markets (Conduct of Institutions) Amendment Act 2022 (CoFI) | - | -.

### ES 4 Bank Profitability (L98-147) - attributed to NERA unless noted
- L119 | "Aaa" ; "default spread of 0" | New Zealand sovereign rating and the Damodaran default spread | - | NERA's description of Professor Damodaran's method.
- L127 | "four largest New Zealand banks" | scope phrase for the ROE comparison ("if the four largest New Zealand banks do persistently derive higher ROE than the rest of the New Zealand banking sector") | - | NERA via ASB | compare "five major banks" at L11/L13.
- L132 | "fourth column of PIP Figure 10" | location of cost-structure comparison | - | PIP; quote attributed to RBNZ (2023) Financial Stability Report p.24 (fn12, L135).
- L133 | "late 1980s" | "New Zealand has not had a banking crisis since the late 1980s" | - | NERA.
- L133 | "2018 speech" ; fn13 L137 "13 November 2018" | RBNZ Deputy Governor Geoff Bascand speech "Financial Stability - risky, safe or just right?" | 2018 | RBNZ.
- L142-144 | "1988-2017" | period of Figures 2 and 3, "large New Zealand banks" | 1988-2017 | "taken from a RBNZ explanatory note" (fn14) | captions only.
- L145 | "2010 (Tables C6 and C7) or 2000 (Figure 11)" | start years of the PIP's earnings-volatility analysis | - | NERA re PIP.
- L145 | "2009" | year GFC impacts "were most acute" ("As Figure 3 makes clear") | 2009 | ASB/NERA | "prior to the 2010 start of the analysis".

### Q1 participants and concentration (L160-223)
- L171 | "some 37 providers" | KiwiSaver providers | - | ASB (no source).
- L174 | "8% Capital Bond" | SBS product launched "Most recently" | - | ASB.
- L177 | "US$30 billion" | Apple "reportedly accounting for US$30 billion in fee-free high-yielding savings accounts in the United States" | - | fn16 (L182, Apple newsroom URL dated 2023/04; URL text "4-point-15-percent-apy") | hedge "reportedly".
- L177 | ranking: "Apple Pay has surpassed Mastercard in total transaction value worldwide" | worldwide | - | fn17 (L183, Forbes URL dated 2022/09/08).
- L177 | "5% of total credit card spending and 10% of debit card spending" | Apple Pay share "in New Zealand" | "As at June 2023" (fn18, L184) | no source named beyond the as-at date | footnote supplies the date only.
- L200 | "from 3% in 2020 to 6% during 2022" | share of "the new-home loan market" held by "[c]ompanies including Basecorp, Bluestone, Avanti Finance and Resimac" ("largest finance companies had doubled their share of new home loans since 2020") | 2020 vs 2022 | 2022 Stuff article reporting CoreLogic data (fn20, L209).
- L200 | "from 10% in 2020 to 14% over the same period, an increase of 40%" | "non-bank and so-called second tier lenders" share (of new home loans) | 2020 vs 2022 | same Stuff article | "an increase of 40%" is relative (10 -> 14); "More recently their overall share has fallen" (no figure).
- L202 | "first 80% of a loan" | Squirrel "Launchpad": Squirrel acts as mortgage broker for first 80%, P2P pool finances "the residual equity" | - | fn21 (L210, interest.co.nz).
- L221 | no number | "RBNZ's C5 data series is a reasonable approximation for lending, although it excludes substitutes such as BNPL" | - | ASB.

### Q3 regulation (L229-378)
- L233 | "$[Redacted] million" | ASB spend on regulatory initiatives "in FY23 alone" | FY23 | ASB | duplicate of L66, redacted.
- L242 | "paragraphs 51 to 54 of the PIP (including Tables 1 and 2)" | PIP location of regulation list | - | -.
- L244 | "past five years" | window for the "***" marking | - | ASB.
- L252 | "over $10 billion in liabilities" | threshold: BS11 (Outsourcing Requirements) is a condition of registration for banks with over $10 billion in liabilities | - | ASB table.
- L342 | "up to $100,000" | Depositor Compensation Scheme (DCS) compensation to eligible depositors | - | DTA description.
- L346 | "May 2023" | Reserve Bank "completed further consultation" on liquidity policy issues | May 2023 | -.
- L350 | "November 2022" | Reserve Bank consulted on DTI restriction framework | Nov 2022 | -.
- L365 | "2018 and 2019" | joint RBNZ/FMA conduct and culture reviews of banks (and life insurers) | - | -.
- L376 | "eight supporting documents" | accompany BS11 | - | fn24 (L386).
- L376 | "approximately $[Redacted] million" | expected cost to ASB of complying with BS11 | - | ASB | redacted.
- Act years printed in table: RBNZ Act 2021 (L247-249); BPSA 1989 (L254-256); Non-Bank Deposit Takers Act 2013 (L261-262); FSP (Registration and Dispute Resolution) Act 2008 (L264-267); Financial Markets Infrastructures Act 2021 (L270-272); CCCFA 2003 (L282-284); FMCA 2013 (L289-291); FSLAA 2019 (L296-297, L300); Financial Sector (Climate-related Disclosures and Other Matters) Amendment Act 2021 (L302); Retail Payment System Act 2022 (L304-306); AML/CFT Act 2009 (L328-332); Privacy Act 2020 (L337); Deposit Takers Act 2023 (L340-341, also fn22-23 L276-278); CoFI Amendment Act 2022 (L356-364).

### Q4 Māori (L380-426)
- L382 | "just under $69 billion" | "growing Māori economy is estimated at" | undated | no source | "estimated".
- L384, L393, L400 | "three pou (pillars)"; three guiding principles; "two key areas" | counts | - | ASB.
- L391 | "FY23" | internships for Māori and Pasifika students introduced | FY23 | ASB.
- L404 | "31%, compared to 52% for non-Māori" | "Māori home ownership" | "As at June 2022" | no source named.
- L407 | "September 2022" | ASB submitted to RBNZ on Issues Paper on Improving Māori Access to Capital | Sept 2022 | fn25 (L413-414: "from page 83 to 87").
- L411 | "as little as 5% deposit" | Kāinga Ora first home loan scheme, "underwritten by Kāinga Ora in its capacity as a provider of Lenders' Mortgage Insurance" | - | ASB.
- L423 | "1,500 schools" | GetWise ("the ASB program run in 1,500 schools throughout New Zealand") | - | ASB.

### Q7 digital disruption (L453-494)
- L463 | "over 30 million users" | Revolut (global) | - | fn28 (L471, Revolut news URL "surpasses_30_million_retail_customers_worldwide").
- L463 | "almost one million new customers per month" | Revolut | - | fn28.
- L463 | "over 400 million transactions a month" | Revolut | - | fn28.
- L465 | "5% market share" | Macquarie, Australian mortgage market | - | fn29 (L472, AFR) | same figure as L47 (fn7 different source).
- L466 | ranking: "largest originator of mortgages for several consecutive years" | Rocket Mortgage, "an online non-bank lender", US | - | fn30 (L473, Forbes Advisor).
- L468 | "PIP, para 123" | source of the quotation at L455-458 | - | fn26.
- L470 | "2022" | IMF Global Financial Stability Report, Chapter 3 "The Rapid Growth of Fintech" | 2022 | fn27.
- L474-477, L493 | "November 2022, p. 5"; "2023, at page 17"; "2020, at page 7"; "at page 5" | repeat citations of fn8-11 as fn31-34 | - | -.
- L483 | "free five-day switching service" | "All major banks offer" | - | ASB | duration.
- L483 | no number | "there are generally no longer monthly account fees" | - | ASB.
- L487 | "2022" | World Bank publication (repeat reference) | - | -.

### Q8 services in scope (L499-516)
- L511 | "approximately 57%" | "New Zealanders aged 15+ had a credit card" | 2021 | "according to the Global Economy Data in 2021", "As referenced in the PIP" (fn36, L514: The Global Economy "Business and economic data for 200 countries").
- L511 | "only around a third" | "New Zealand households have a mortgage" | undated | "it is estimated" (fn37, L515, RNZ Mediawatch URL) | households basis, not persons.
- L511 | "more than 2.7 million people" | "had a credit card in New Zealand" | "As at April 2022" | fn38 (L516, Stuff) | persons basis.
- L511 | "around $600 million a year" | spending "on credit card interest payments" | as at April 2022 | fn38.

### Q9 nature of competition (L521-633)
- L524 | "five major banks" | count | - | ASB.
- L528 | "daily basis" ; "at least a [Redacted] basis" | ASB monitoring of competitor pricing; frequency of formal rate card review | - | ASB | second redacted.
- L537 | "9% in 1998 to 13% in 2003 and 17% in 2008" | ASB: "made a conscious decision to grow its home loan book, and in doing so doubled its overall size, going from 9% ..." (the text does not name the share measure beyond this sentence) | 1998, 2003, 2008; decision "in the late 1990s" | ASB own.
- L562 | "over one million customers" | Kiwibank "since its inception" | - | ASB (no footnote).
- L570 | "2022" | Kiwibank "total brand refresh" | 2022 | ASB.
- L570 | "up 34% on FY22" | Kiwibank "best results in the history of the bank for FY23" (the line item is not named in the body) | FY23 vs FY22 | fn39 (L573, Kiwibank media release).
- L570 | "$1.1 billion, (or 1.5x market)" | Kiwibank "Home lending growth" | FY23 | quotation of Kiwibank CEO (fn39).
- L570 | "$1.54 billion, or 6%" | Kiwibank "Total deposits rose" | FY23 | fn40 (L574, interest.co.nz; URL text "kiwibank-june-year-profit-hits-175-mln").
- L574 | "175 mln" (URL text only) | Kiwibank "june-year-profit" | June year | fn40 URL fragment | not stated in body.
- L570 | "100%" ; "2022" | NZ Government acquiring 100% of Kiwibank's parent company | 2022 | ASB | cf. L14.
- L571 | "$225 million" | Kiwibank cash injection, "via the reinvestment of the funds received from the sale of its former investment and insurance businesses" | - | fn41 (L575).
- L572 | no numbers | "ANZ, ASB and Westpac have all lost share over the period, while Kiwibank and BNZ ... have grown share" (home lending; graph "scaled to show changes rather than absolute share") | June 2018-March 2023 (Figure 9 caption L579) | RBNZ S31 Statistical Series and Bank Financial Strength Dashboard (L581).
- L578 | "2022" | Kiwibank launched a 'co-own' product | 2022 | ASB.
- L585 | "$624 million or 14% to $5.025 billion" | SBS "Lending rose" | "during the period" (FY23) | quotation from SBS release (fn42-43, L586-587).
- L585 | "$655 million to $4.230 billion" | SBS "member deposits rose" | FY23 | SBS release quotation.
- L585 | "approximately 12% from $3.6 billion to $4.0 billion" | "SBS Bank's total home lending" | "year to 31 March, 2023" | SBS release quotation | exact-vs-rounded: 3.6 -> 4.0 printed beside "approximately 12%".
- L585 | "closer to 3.5%" | "broader industry growth rate" | same | SBS release quotation.
- L585 | "1.6x system (market) growth"; "a further 6% to $6.2 billion" | TSB residential lending; lending assets | FY23 | fn44 (L589-590) | duplicate of L24.
- L585 | "NZD$399.5 million (9.2%) to $4.75 billion" | Heartland Bank "increased its borrowings" | FY23 | fn45 (L592-594, Heartland investor presentation slide 18).
- L585 | "NZ$534 million (~15%) to $4.13 billion" | Heartland Bank "deposits grew" | FY23 | fn45.
- L585 | ranking: highest growth rate in retail deposits "of all main and domestic banks in New Zealand" | Heartland | "Q1 and Q2 of FY23" | RBNZ balance sheet data; fn46 "Ibid, slide 18".
- L599 | "8% growth in mortgages" | The Cooperative Bank | FY23 | fn47 | duplicate of L26.
- L599 | "$204 million, compared to $41 million mortgage growth in FY22" | Cooperative Bank mortgage portfolio growth | FY23 vs FY22 | fn47.
- L599 | "5% deposit growth overall" | Cooperative Bank | FY23 | fn48.
- L600 | "two hourly transfers" | Squirrel on-call savings account (transfers to deposit or withdraw) | - | fn49 (L619).
- L600 | "April 2023" | Sharesies savings account "introduced in April 2023" | Apr 2023 | fn51 (L621).
- L603 | "[Redacted]" | para 9.25 entirely redacted (fn52 L622 also redacted) | - | -.
- L606 | "[Redacted]" x3 | Home Central visits "In the past month alone" | - | ASB | duplicate of L89 (there "In the last month alone").
- L608 | "over $[Redacted] million worth of fees" | fees ASB "has removed ... in relation to personal banking services" | "in the last two years" | ASB | redacted; scope word "personal banking services".
- L611 | "$20" -> "$10" -> "just $3 monthly" | ASB unarranged overdraft fee: "While they were at $20 for an unarranged overdraft, this reduced to $10 over time, and now sits at just $3 monthly" | undated | ASB own | the $3 is "monthly"; no period given for $20/$10.
- L612 | zero | "ASB no longer charges any fees for arranged overdrafts" | now | ASB.
- L610 | zero | "ASB no longer charges fees for an account ... no fees for self-service transactions or for access to online or mobile banking" | now | ASB.
- L616-617 | "at page 6" | Cooperative Bank Annual Results page for L599 figures | - | fn47, fn48.
- L628 | "over the past five years"; "quarter-by-quarter" | window and frequency of Figure 10 (text: "market shares for term deposits") | Jun-18 to Jun-23 axis (L644) | RBNZ Bank Financial Strength Dashboard (L631).
- L644 | axis "-0.80%" to "0.80%" in 0.20% steps; quarters "Jun-18 ... Jun-23" (21 labels) | Figure 10 axis text "Deposits QoQ Change" | - | - | no data values extracted.

### Q10-Q15 (L634-904)
- L730 | "five other banks" | "regional banking hub pilot program with five other banks" | - | ASB | cf. L889 "pilot partnership of six New Zealand banks".
- L730 | "two locations" | ASB "recently extended branch hours in two locations following customer demand" | recently | ASB.
- L746 | "up to $60,000"; "around 12 months" | ASB compassionate care offering: ASB "will pay the interest costs of up to $60,000 on eligible owner-occupied home lending for around 12 months if one of the eligible borrowers were to pass away" | - | ASB own.
- L752 (fn53) | "up to $50,000 for five years" | Westpac interest-free loans to home loan customers "to purchase an electric vehicle or other energy-efficient technology, subject to lending and affordability criteria" | - | NZ Herald (fn53) | figures appear ONLY in the footnote; body (L746) says only "interest free loans for electric vehicles".
- L784 | "over 72,000 reviews" | ASB financial wellbeing assessments completed | "last year" | ASB own.
- L785 | "404,000 customers" | using ASB digital financial wellbeing tools | "last year" | ASB own.
- L787 | "Approximately 166,000 customers" | have used Card Tracker "since its launch in November 2022" | Nov 2022 to submission | ASB own.
- L789 | "$14.3m" | government benefits accessed by customers via ASB's Support Finder tool | FY23 | ASB own.
- L800 | "2022" | Figure 14 caption: "ASB's 2022 EOY Announcement" | 2022 | -.
- L811 | "1989" | "any bank registered unders [sic] the RBNZ Act 1989" (NZBA full membership) | - | fn54 (L836, nzba.org.nz) | cf. table L247-257 (RBNZ Act 2021; BPSA 1989 "Provides for registration of banks").
- L816 | "[Redacted] at FY18, to [Redacted] at FY23" | mortgage advisers accredited with ASB | FY18, FY23 | ASB | redacted.
- L816 | "comfortably over [Redacted]%" | ASB's share of new home loan business originating via a broker | "now" | ASB | redacted; repeated L995 "([Redacted] of ASB's new home loan business originates via broker)".
- L818 | "2017" | InvestNow "launched in 2017" | 2017 | ASB | cf. L968 "the entry of Revolut and InvestNow into New Zealand" listed among "recent entry and expansion".
- L828 | "late 2019"; "meets quarterly" | ASB Community Council | - | ASB | duplicate of L94-95.
- L853 | "2018" | "FMA/RBNZ Bank Conduct and Culture Review in 2018" | 2018 | - | cf. L365 "in 2018 and 2019".
- L853 | "March 2021" | NZBA Council agreed NZBA establish a Vulnerability Working Group | Mar 2021 | -.
- L857 | "12 months from November 2021" | Good Shepherd NZ Economic Harm Support Service developed and piloted | Nov 2021 + 12 months | fn55 (L890) cites the "Interim six-month report".
- L865 | three banks | "ASB, BNZ, and Westpac banks' customer vulnerability teams were specifically acknowledged in the pilot review report" | - | Good Shepherd NZ report (fn55).
- L871 | "163 referrals"; "over 101 solutions" | ASB Extra Care team | "Between April 2022 and July 2023" | ASB own.
- L873 | "past 12 months" | Extra Care team scope extended | - | ASB.
- L875 | "FY23" | abuse in transactions addressed by Extra Care team | FY23 | ASB.
- L879-880 | "mid-2021"; "from five to 13 (including a Manager and Assistant Manager)" | ASB Community Bankers team introduced / expanded | mid-2021 to submission | ASB own | split across L879/L880.
- L884 | "300+ workshops, 200+ Hui, ... 2400+ customers, ... 130 repurposed ASB Laptops" | Community Bankers initiative | "since July 2022" | ASB own.
- L889 | "six New Zealand banks" | Regional Banking Hubs "pilot partnership" | - | fn56 (L891, NZBA).
- L896 | "over 65 year old customers"; "9am to 10am" | dedicated seniors line eligibility; in-branch priority hour | - | ASB.
- L898 | "October 2020" | Better Banking Workshops launched | Oct 2020 | ASB.
- L901 | "more than 12,000 distinct customers"; "more than 6,000 such customers"; "more than $1.1 million in annualised cost savings"; "July 2021 to June 2023" | verbatim repeat of L83-87 | - | ASB own.

### Q16-Q21 (L906-1039)
- L928 | "over $10bn in liabilities" | BS11 registration-condition threshold | - | ASB | same as L252 ("over $10 billion").
- L934 (fn57 URL text only) | "2.41-Billion-Market-by-2028"; "Market-Report-2023" | NZ BNPL market report title in a businesswire URL | - | ResearchAndMarkets via URL | not in body; body (L931) says only "continues to record strong growth".
- L944 | "24 July this year" | ASB submitted on MBIE's CDR Discussion Document | 24 July (year not printed; see section 0 date note) | ASB.
- L962 | "£1.5bn" | "it has been estimated that the cost incurred in the UK to design the mandated infrastructure was £1.5bn" (open banking) | - | fn58 (L972, UK Finance press release).
- L969 | "2017" | withdrawal of ASB's BankDirect brand | 2017 | Commission reference, ASB response.
- L976 (fn61 URL) | "2022-11-30" | Reuters article date on HSBC NZ retail sale | - | URL.
- L980 | "1 September 2023" | announcement that Pepper Money "was going to acquire HSBC's $1.4bn mortgage portfolio" | 1 Sep 2023 | fn62 (L1012, interest.co.nz: "14- bln-nz-mortgage-portfolio") | latest dated event in D03.
- L980 | "$1.4bn" | HSBC (NZ) mortgage portfolio | - | fn62.
- L980 | "2011" (twice) | Pepper Money active in NZ "since it acquired GE Capital's Australian and New Zealand home lending business in 2011"; CEO quote "since 2011" | 2011 | fn63 (L1014).
- L995 | "[Redacted]"; "compared to five years ago" | broker share of ASB new home loan business; comparison window | - | ASB.
- L1002 | "compared to five or more years ago" | comparison window for savings-account choice factors | - | ASB.
- L989-1039 | "[Redacted]" | paras 20.1 (part), 20.4, 20.5, 21.1, 21.2, 21.3 and Figures 15-19 | - | - | all redacted.

### Q22-Q24 (L1045-1101)
- L1051 | no number | "All major banks offer a free switching service ... which includes moving customers' recurring payments such as automatic payments and direct debits" | - | ASB | no duration here; L483 says "free five-day switching service"; repeated L1087.
- L1054 | "[Redacted] personal customers over the age of 18, but [Redacted] are considered to have their main banking relationship with ASB" | ASB personal customers aged over 18 vs main-bank customers | - | ASB | both redacted.
- L1054 | "two banks" | illustrative example only ("consumers may have savings accounts with two banks") | - | ASB.
- L1062 | "by the middle of 2023" | RBNZ "had indicated" the AML address-verification requirement "was likely to change for most or all customers by the middle of 2023"; "this has since been delayed as it requires a law change and no new timeframe has been communicated" | forecast mid-2023; not actioned | RBNZ (as reported by ASB).
- L1075 | "2017" | InvestNow launched | 2017 | ASB | repeat of L818.
- L1076 | five banks named | banks whose term deposits InvestNow offers ("including") | "currently" | ASB | membership in section 4.
- L1084 | "[Redacted]" | share "of ASB's home loan lending originating via brokers" | - | ASB | redacted; wording differs from L816/L995 ("new home loan business").

### Q25-Q26 (L1106-1207)
- L1106, L1110 | "past five years" | window of the innovation question and answer | - | PIP / ASB.
- L1113 | "[Redacted] of ASB product sales volume and more than [Redacted] of financial transactions completed via digital" | ASB digital channel share | - | ASB | redacted; fn66 attaches here.
- L1122 (fn66) | "first in Australia and NZ, and 2nd globally (of 200 banks)"; "77%"; "2017" | "Finalta's 2017 benchmark put ASB first in Australia and NZ, and 2nd globally (of 200 banks), for digital activity amongst personal customers at 77%. This figure is now higher." | 2017 | Finalta (footnote only) | figures appear ONLY in the footnote; "now higher" unquantified.
- L1115 | "June 2018" | "ASB mobile became ASB's most popular channel in June 2018 when it surpassed FastNet Classic (ASB's internet banking) in terms of monthly active users" | Jun 2018 | ASB own.
- L1115 | "Since 2017"; "2019" | start of ASB's stated digital focus; "ASB Mobile underwent a full redesign in 2019" | - | ASB.
- L1117 | "90%" | "of personal customers who were active with ASB were digitally active in that month (i.e. using either online banking or ASB Mobile)" | "In June 2023" | ASB own | scope: personal, active customers.
- L1121 | "2018"; "2019" | ASB ID capability "introduced in 2018"; "received a Canstar Innovation Excellence Award in 2019" | - | fn67 (L1124).
- L1128 | "404,000 customers"; "up 39% on FY22"; "five years ago" | used ASB digital financial wellbeing tools | "Over the past financial year" | ASB own | L785 gives 404,000 as "last year" without the growth rate.
- L1130 | "2020"; "Since 2022" | Josie chatbot introduced in ASB mobile app; chatbot hand-over to two-way messaging | - | ASB.
- L1133 | "71%" | "of bank active customers over 65 years of age were digitally active in June" | "in June" (year not printed) | ASB own | compare L1117 (90%, all active personal customers, June 2023); fn68 (L1153) is only a URL.
- L1135 | "2021" | Support Finder tool launched in ASB Mobile app | 2021 | ASB.
- L1137 | "2020" | Home Loan Explorer tool launched | 2020 | ASB.
- L1139 | "since 2019"; "since 2018" | "ASB has offered Apple Pay and Google Pay since 2019, and Garmin Pay and Fitbit Pay since 2018" | - | ASB own | ASB's offering dates, distinct from L1162 (Apple Pay in NZ 2016).
- L1158 | "2014" | Harmoney "Launched in 2014"; "the first company to receive a P2P lending license in New Zealand" | 2014 | fn69 (L1169, FMA media release).
- L1159 | "over 500,000 customers across Australia and New Zealand" | Sharesies | - | "Sharesies states" | two-country scope.
- L1160 | "five major currencies (NZD, AUD, GBP, EUR, USD)"; "more than 200 currencies" | Revolut users can hold / transact in | - | fn70-71.
- L1160 | "2021"; "26,000 New Zealanders"; "12-month test period"; "3 July 2023" | "Since Revolut registered as a financial service in New Zealand in 2021, 26,000 New Zealanders signed up to the waitlist over a 12-month test period prior to Revolut's official launch on 3 July 2023" | - | fn72 (L1172) | compare global figures at L463.
- L1162 | "2016" | "Apple launching in 2016" (Apple Pay in New Zealand) | 2016 | fn73 (L1173; URL text "now-available-in-11-countries").
- L1162 | "5% of total credit card spending and 10% of debit card spending" | Apple Pay in New Zealand | "As at June 2023" (fn76, L1176) | no source named | verbatim repeat of L177.
- L1165 | "1989" | "Worldline (previously called Paymark) first launched EFTPOS in 1989" | 1989 | fn77 (L1178).
- L1168-1181 | "2022"; "sample of 125 countries" | World Bank publication, quoted: "multivariate cross-country regression analysis for the sample of 125 countries with data on [its] fintech activity index" | 2022 | fn78 (L1205).
- L1181 | "fifth of 74 countries" | NZ rank in the "Aggregate Fintech Activity Index", "an average of four 'pillars'" | 2022 publication | World Bank | exact basis for L45's "5 out of 74 countries on one measure".
- L1181 | "fourth out of 125 countries" | NZ rank "if the Finance Mobile App Download pillar was excluded (which increased the eligible countries to 125)" | 2022 publication | World Bank | exact basis for L45's "4 out of 125 countries on the other".
- L1185 | "May 2016" | date of the Payments NZ report "Benchmarking New Zealand's payment systems" | May 2016 | fn79 (L1206); quotation at fn80 "Ibid, p4" (L1207).
- L1189 | rank 1 | "NZ had the highest number of cards transactions per capita in the study" | 2016 report | Payments NZ.
- L1191 | "29.7 people per POS terminal, just behind Australia" | NZ people per Point of Sale terminal | 2016 report | Payments NZ | NZ second to Australia on this item though listed under 'leader'.
- L1193 | rank 1 | "highest POS utilisation per terminal per capita among countries benchmarked" | - | Payments NZ.
- L1195 | rank 1 | value of card payments vs cash in circulation: "NZ led the world, followed by Sweden" | - | Payments NZ.
- L1196 | "2nd highest" | per capita ATM utilisation per machine | - | Payments NZ.
- L1197 | "2nd lowest" | ATM withdrawals relative to other retail payments | - | Payments NZ.
- L1199 | no rank | "high levels of ATM withdrawal values relative to cash in circulation" | - | Payments NZ.
- L1201 | rank: "lowest" | "level of active cash in circulation relative to GDP" | - | Payments NZ.
- L1202 | rank 1 | "NZ retail payments volume per capita led the countries surveyed" | - | Payments NZ.

### Q27-Q32 (L1211-1304)
- L1226 | "five major banks" | count | - | ASB.
- L1250 | "$[Redacted] million" | "ASB's investment envelope for FY23", "acts as an approximate financial ceiling" | FY23 | ASB | redacted; fn81 (L1268) states what is excluded.
- L1253 | "$[Redacted]" (FY23); "$[Redacted] in FY22"; "$[Redacted] in FY21"; "over $[Redacted] ... since 2018"; "$[Redacted] in the five-year period prior to that (2013-2017)" | ASB spend on regulatory initiatives ("e.g. BS11, CCCFA, financial crime compliance, FSLAA etc.") | FY21-FY23; since 2018; 2013-2017 | ASB | all five redacted; FY23 figure also at L66/L233 (there "$[Redacted] million").
- L1255 | "9 August 2023" | "MBIE released a cabinet paper proposing changes to the CCCFA" | 9 Aug 2023 | ASB.
- L1257 | "$[Redacted]" | ASB investment "in sustaining and securing core banking systems (and essential properties work)" | FY23 | ASB | redacted.
- L1259 | "$[Redacted]" x2 | "One Giant Leap transformation programme" spend; "remaining" envelope on other innovation initiatives | FY23 | ASB | redacted; benefits "both ASB's personal and business customers".
- L1265 | "over the past twenty-five years"; "from 9% to 18%" | ASB "has grown its share of total banking assets" | 25 years to submission | ASB own | basis "total banking assets"; compare L537 ("9% in 1998 to 13% in 2003 and 17% in 2008", home loan book context).
- L1265 | "$10 billion" | ASB "lifted its shareholder equity by $10 billion to support that growth" | same 25 years | ASB own.
- L1283, L1285 | "four large banks" | scope of the funding-cost claim ("large Australian-owned banks", L1281) | - | ASB.
- L1285 | "at least two notches lower (i.e. A instead of AA-)" | credit rating the four large banks would have "Without that backing" of parents | counterfactual, current | "ASB considers".
- L1285 | "$180 - $270 million" | "would currently experience higher funding costs in a range of $180 - $270 million" | counterfactual, "currently"; no per-year wording printed | "ASB estimates" / "ASB considers" | scope: the four large banks together (as worded), not ASB alone.
<!-- FIG -->

## 3. Tables and figure captions

- Figure 1 "Fee Income over time" (L32): caption only; no data, axes or source extracted.
- Figure 2 "Impaired assets as a share of gross loans and advances, large New Zealand banks, 1988-2017" (L142): caption only. Stated source: RBNZ explanatory note (fn14, L138).
- Figure 3 "Impaired asset expense and extraordinary items (12 month rolling total) as a share of gross loans and advances, large New Zealand banks, 1988-2017" (L143-144): caption only. Text reading of it at L145 ("GFC impacts were most acute in 2009").
- Regulation table (L245-369), two columns "Regulation" | "Relevance to personal banking services market". Extracted as running text: the left-column name is broken over several short lines and followed by the right-column description; group rows are "Prudential" (L246), "Other sector-specific" (L275), "Not sector-specific" (L311), "Proposed prudential regulation" (L339), "Proposed other sector-specific" (L355). "***...***" markers survive; the "red text" marking for regulations additional to the PIP's list (L242) did NOT survive extraction (colour lost). Membership in section 4.
- Figure 4 "FIS Global Payments Report" / "Source: FIS Global Payments Report" (L489-490): caption and source only.
- Figure 5 "Share of new home loans" (L543-544): "[Redacted]".
- Figure 6 "Home Lending - Net Refinances" (L550-551): "[Redacted]"; description of what it charts at L548.
- Figure 7 "Share of Voice (Marketing) Home Loans" (L557-558): "[Redacted]".
- Figure 8 "NPS Scores" (L565-566): "[Redacted]"; para 9.14 (L563) also wholly redacted.
- Figure 9 "Home Lending Market Share (June 2018-March 2023)" (L579); "Source: Data from RBNZ S31 Statistical Series and Bank Financial Strength Dashboard" (L581): caption and source only; direction of movement described in prose at L572.
- Figure 10 "Deposits Market Share Quarterly Change" (L630); "Source: Data from RBNZ Bank Financial Strength Dashboard" (L631). Axis and legend text survive, displaced to L644-645 inside Q10: y-axis ticks "-0.80% -0.60% -0.40% -0.20% 0.00% 0.20% 0.40% 0.60% 0.80%"; x-axis quarters "Jun-18 Sep-18 ... Mar-23 Jun-23" (21 labels); axis title "Deposits QoQ Change"; legend "ANZ ASB BNZ Co-op Heartland Kiwibank SBS TSB Westpac" (9 series). NO data values. Introducing prose (L628) calls it "market shares for term deposits ... over the past five years"; caption and axis say "Deposits".
- Figure 11 "Reasons customers opened primary savings account" (L693): "[Redacted]".
- Figure 12 "Key Drivers of Choice" (L708-709): "[Redacted]".
- Figure 13 "Motivators for why customers open primary transaction account" (L715): "[Redacted]".
- Figure 14 "Financial Progress extract from ASB's 2022 EOY Announcement" (L800): caption only (image not extracted). Para 11.5 (L799) says some features listed in 11.4 "are reflected" in it.
- Figure 15 "Average number of lenders seeking pre-approval form across range of lenders" (L991): "[Redacted]".
- Figure 16 "Top 10 drivers for motivating choice of mortgage lender" (L997): "[Redacted]".
- Figure 17 "Why customers opened PSA with current provider" (L1004): "[Redacted]" ("PSA" not expanded in D03).
- Figure 18 "Establishment of relationship with main bank" (L1018-1019): "[Redacted]".
- Figure 19 "% of home loan borrowers likely to switch lenders in next 12 months" (L1032): "[Redacted]".
- Figure 20 "InvestNow term deposit rates screenshot" (L1083): caption only.
- Totals: 20 figure captions (Figures 1-20). Redacted: 5-8, 11-13, 15-19 (12). Caption-only with no data: 1, 2, 3, 4, 9, 14, 20 (7). Caption plus axis/legend text but no values: 10 (1). The only table is the regulation table (L245-369); there is NO numeric table anywhere in D03.
<!-- TAB -->

## 4. Enumerated lists (full membership; last item location)

- Other banks cited as growing (ES 1.4, L16-26): (a) SBS, (b) TSB, (c) Heartland, (d) The Cooperative Bank [last, L26]. Same four in Q9 "Smaller banks" paras 9.19-9.22 (L585-599).
- Non-bank competitors named in ES 1.7 (L33, L43): Apple Pay; BNPL products; Harmoney (unsecured credit); Revolut; Sharesies (savings account, "deposits held in trust by an undisclosed New Zealand bank") [last, L43].
- Companies "not similarly regulated" in payments (L68, repeated L235): Apple, Google, Wise, "etc.".
- Regulatory developments "in train" (ES 2.4, L70): Deposit to Income Rules [as printed]; Deposit Takers Act (deposit insurance); real time payments; open banking initiatives. "The latter three in particular are designed to drive pro-competitive outcomes". Q3 3.6 (L241) lists three: Deposit Takers Act, open banking, real time payments reforms.
- ASB progress pillars (L76-79): Financial Progress - Toitū te Tahua; Social Progress - Toitū te Tangata; Environmental Progress - Toitū te Taiao.
- Community partnerships named (L7): KidsCan, Youthline, Hato Hone St John.
- NERA conclusions (ES 4.1, L102-132): (a) L102; (b)(i)(A)-(B) L104-108; (c)(i)-(iv) L110-122; (d)(i), (d)(ii)(A)-(C) L124-132 [last, L132].
- Q1 "[1.1]" participants not mentioned / under-emphasised (L169-217), items (a)-(j):
  - (a) L169 credit unions and building societies (7): Unity Credit Union, First CU, NZCU Auckland, Police CU, Heretaunga Building Society, The Wairarapa Building Society, Nelson Building Society.
  - (b) L171-172 savings/investment players: P2P lenders "such as Squirrel"; KiwiSaver ("some 37 providers"), e.g. Sharesies.
  - (c) L174 Aera (fn15, L181: "non-bank lender", founded by Derek Handley); Rabobank; SBS 8% Capital Bond; fixed interest offerings (NZX); KiwiBonds (Crown).
  - (d) L175 finance companies providing savings products (7): Christian Savings, Finance Direct, General Finance, Gold Band Finance, Liberty Financial, Mutual Credit Finance, Xceda Finance.
  - (e) L177 Apple, Alphabet (Google).
  - (f) L178 B2C and P2P payment apps / crypto wallets, e.g. WeChat, AliPay.
  - (g) L180-187 aggregator platforms (InvestNow); BNPL firms (Afterpay); account services (Dosh, Revolut).
  - (h) L189-190 savings alternatives: bonds, PIE funds, traditional managed funds, equities.
  - (i) L192-205 Home Lending and Home Lending Brokerage, sub-items (i)-(viii): (i) Simplicity L194-195; (ii) NZHL, Loan Market, Squirrel L196; (iii) Tella (digital broker), Neo (digital non-bank home lender) L197; (iv) First Mortgage Trust, Midlands Mortgage Trust L199; (v) finance companies (10): Avanti Finance, Basecorp Finance, Bluestone, CFML Loans, Hibernian, Liberty Financial, Paraloan, Pepper Money, Resimac, Xceda Finance L200; (vi) Squirrel "Launchpad" L202; (vii) rent-to-own (NZ Housing Foundation), Aera L203; (viii) RBNZ capital increases facilitating non-regulated institutions L205.
  - (j) L206-217 Payments, sub-items (i)-(iv): (i) BNPL: Afterpay, Laybuy, Klarna, Zip L207; (ii) Dosh L214; (iii) Wise L216; (iv) non-bank credit card providers (5): Amex, Finance Now, Latitude (GEM), FlexiGroup (Q card / Flight Centre / Farmers), The Warehouse [last, L217].
  - Liberty Financial and Xceda Finance appear in both the (d) list and the (i)(v) list.
- Regulation table membership (L245-369), "***" = marked as creating additional obligations in the past five years:
  - Prudential: ***RBNZ Act 2021*** (L247-252); ***BPSA 1989*** (L254-259); Non-Bank Deposit Takers Act 2013 (L261-263, no asterisks); Financial Service Providers (Registration and Dispute Resolution) Act 2008 (L264-268, no asterisks); ***Financial Markets Infrastructures Act 2021*** (L270-273).
  - Other sector-specific: ***CCCFA 2003*** (L282-287); ***FMCA 2013*** (L289-302); ***Retail Payment System Act 2022 (RSPA)*** [abbreviation printed "RSPA"] (L304-309).
  - Not sector-specific: FATCA (L312-318, no asterisks); CRS (L320-326, no asterisks); ***AML/CFT Act 2009*** (L328-335); ***Privacy Act 2020*** (L337).
  - Proposed prudential regulation: ***Deposit Takers Act 2023 (DTA)*** (L340-342); ***Changes to the Reserve Bank's liquidity policy*** (L344-346); ***Changes to the Reserve Bank's debt-to-income (DTI) restriction framework*** (L348-350); ***Proposed changes to the Reserve Bank's policy for branches of overseas banks*** (L352-353).
  - Proposed other sector-specific: ***Financial Markets (Conduct of Institutions) Amendment Act 2022 (CoFI Act)*** (L356-365); ***Consumer Data Right (CDR)*** (L367-369) [last row].
  - Count as extracted: 18 rows; 14 carry "***"; 4 do not (Non-Bank Deposit Takers Act 2013, FSP Act 2008, FATCA, CRS).
  - FMCA sub-list (L294-298): 1) fair dealing; 2) financial advice regime; 3) investment products (such as KiwiSaver). Related regimes named L300: FSLAA, CoFI, CRD, DIMS, MIS, fair dealing.
- Foreign regulations (L371-374): (a) Australian - CDE and other APRA requirements (assist CBA group); (b) global - ISO 20022, EU GDPR.
- BS11 outsourced functions examples (L376): IT processing, accounting, call centres, "etc.".
- Te Ao Māori strategy pou (L390-392): (a) Te Ao Māori - The Māori World; (b) Rangatiratanga - Leadership; (c) Ōhanga Māori. Guiding principles (L395-398): (a) Tika, Pona, Aroha; (b) Whanaungatanga; (c) Toitutanga.
- Q4 two key areas (L402-426): (a) home ownership, sub-items (i)-(vi) L404-418; (b) lack of confidence to engage with banks, initiatives (i)-(iv) L421-426 [last: Whaihua app relaunch, L426]. Whānau Programme partners (L425): The Retirement Commission, NZBA, Tāwhia, Te Puni Kōkiri. Māori Freehold Land ownership forms ASB can lend on without Government support (L407): sole owner; joint tenants or owners in common (up to a limited number of owners); Māori Land Act Trusts or Incorporations.
- Q6 factors influencing financial performance (L433-451), (a)-(j), ten items: (a) interest rates achieved on assets; (b) costs of funding; (c) costs of hedging; (d) other sources of income (fee revenue, commission); (e) operating expenses; (f) expenses for investment programs (regulatory, technology); (g) loan impairment expenses; (h) amount of equity; (i) prevailing level of interest rates; (j) level of risk [last, L451]. Introduced as "In addition to the level of competition" (L432).
- Q7 international non-bank examples (L462-466): (a) IMF report on US mortgage market; (b) Revolut (and Venmo, Sharesies); (c) Macquarie; (d) Rocket Mortgage [last, L466].
- Payment methods named from FIS report (L487): Afterpay, Apple Pay, Google Wallet, Paypal, Zip, "Layby" [as printed], alongside EFTPOS.
- Services the Commission proposes to omit (L502): foreign exchange, investments, insurance; services ASB says should not be left out: personal consumer loans, credit cards.
- Substitutes for customers' money (L512): pay down debt; increase KiwiSaver contributions; managed fund or shares; "etc.".
- ASB competitive levers other than price (L530): marketing, distribution, service levels, digital offerings, credit policy.
- Banks by share movement in Figure 9 prose (L572): lost share - ANZ, ASB, Westpac; grown share - Kiwibank, BNZ.
- Smaller competitors with term savings / deposit products (9.23, L600): Squirrel, Sharesies, Forsyth Barr [last].
- Fee removals (9.28, L610-612): (a) no account fees, no fees for self-service transactions or online/mobile banking access; (b) unarranged overdraft fee $20 -> $10 -> $3 monthly; arranged overdraft fees removed [L612, unlettered sentence after (b)].
- Figure 10 legend, nine banks (L645): ANZ, ASB, BNZ, Co-op, Heartland, Kiwibank, SBS, TSB, Westpac [last].
- Alternatives to savings/term deposits (9.32, L633): bonds, PIE funds, traditional managed funds, equities "and the like" (same four as L189).
- Innovations "largely aimed at retaining customers" (10.4, L649-654): (a) Apple Pay / Google Pay; (b) Card Tracker; (c) Home Central; (d) Support Finder [last].
- Trigger-based conversations (10.6, L658-661): customers who (a) may be better off on a different product; (b) could avoid paying fees by changing behaviour; (c) may have a significant deposit that could be moved.
- Initiatives "more targeted at winning new customers" (10.7, L665-678), eight: (a) Back my Build; (b) online joining and ID verification; (c) self-service digital advice tool (KiwiSaver); (d) new card propositions; (e) improvements to True Rewards; (f) product simplification; (g) removing all fees on personal accounts; (h) Community Bankers [last, L678].
- Home loan choice factors (10.9, L683): product offering; likelihood of approval (credit settings/appetite); price; service - time to approval.
- Substitutes by market cycle (10.13, L700-703): (a) paying down debt; (b) KiwiSaver; (c) shares or managed funds.
- Online-only entrants (10.22, L736): Revolut, Sharesies, "Area" [as printed], "etc.".
- Home loan differentiation (11.2, L744-760), eight: (a) pricing and price specials; (b) product offering; (c) approval criteria; (d) channel of choice (online, broker, in person, contact centres); (e) geographic representation and scale, people/capability/experience; (f) brand/reputation; (g) promotions (cashback or general insurance offerings); (h) guidance and advice [last].
- Deposit account differentiation (11.3, L764-777), eight: (a) pricing; (b) mobile app / online banking functionality; (c) support across other channels; (d) account features; (e) tools/alerts ('Save the Change'); (f) brand/reputation; (g) promotions or other incentives; (h) guidance and advice [last].
- ASB free tools (11.4, L781-795), nine: (a) Card Control; (b) Alerts; (c) Financial wellbeing assessments; (d) Digital financial wellbeing tools; (e) Card Tracker; (f) Support Finder; (g) Save the Change; (h) Easy ways to pay (Apple Pay, Google Pay, Garmin Pay); (i) Guidance and advice [last]. L1139 adds Fitbit Pay to the pay methods.
- Interactions with other providers (12.1, L804-811): (a) Market research - Morningstar, Ipsos KiwiSaver NPS data, Consumer NZ, Canstar, Mindful Money, Sorted Smart Investors platform, Risk Managers Round Table, RBNZ market statistics (8); (b) Working Groups - Payments NZ, Payments Council, SWIFT, AML / CFT, Financial Services Council, CCCFA (6); (c) NZBA [last].
- Community Council outcomes (15.3, L831-849), eight: (a) treatment of financially vulnerable customers; (b) ASB Support Finder; (c) education session for ASB's Board; (d) Council priority areas - BNPL being treated as a credit contract; domestic violence / joint debt; access for financial mentors; focus groups with assisted technology users; (e) 7-day payments communications (passed to Payments New Zealand); (f) referral pathways to MoneyTalks; (g) financial abuse awareness guides; (h) vulnerability lens on operational changes [last].
- NZBA Vulnerability Working Group topics "in recent months" (15.6, L855): barriers to opening bank accounts; development of vulnerability guidelines; basic banking information for migrants and refugees; cultural competency and harmful gambling.
- Good Shepherd pilot aims (15.7, L859-864): (a)-(d). Banks acknowledged in its report (L865): ASB, BNZ, Westpac.
- Extra Care partner organisations (15.10, L873): Age Concern New Zealand, Women's Refuge, Public Trust.
- Community Bankers outputs since July 2022 (15.15, L884): 300+ workshops; 200+ Hui; 2400+ customers; 130 repurposed laptops; bespoke calls (unarranged overdrafts, flood and cyclone relief, 7-day payments); better banking workshops; financial wellbeing workshops and GetWise.
- Other ASB programs (15.16, L889-898): (a) Regional Banking Hubs; (b) seniors line and priority hour; (c) Better Banking Workshops [last].
- Conditions of entry and expansion (16.2, L913-920): (a) Regulation; (b) Capital; (c) Technology; (d) Small size of New Zealand's personal banking market [last]. 16.1 names regulation as "the condition of entry and expansion most significantly affecting competition".
- What a CDR regime should do (18.5, L948-957), five: (a) Protect customer information and money; (b) Minimise regulatory overlap (Privacy Laws, Consumer Credit Laws, Financial Services Regulations, AML obligations, IP laws, Commerce Act); (c) Impose reciprocal obligations; (d) Exclude "derived" data; (e) Set practical standards [last].
- Open banking general points (18.6, L961-964): (a) data security; (b) cost (UK £1.5bn); (c) compliance cost; (d) existing offerings such as InvestNow [last].
- Recent entry/expansion named (19.1, L968): Sharesies' new savings account; entry of Revolut and InvestNow; expansion of Kiwibank. Exit examples: BankDirect brand (19.2, L969); HSBC (19.3-19.6, L970-982); acquirer Pepper Money (L980).
- Life milestones triggering a switch (21.4, L1042): study, "employment migration" [as printed, no comma], relationships, acquisition of assets.
- Comparison sites (23.1, L1066-1073): interest.co.nz (in the lead-in); (a) Mortgagerates.co.nz; (b) Goodreturns.co.nz; (c) Moneyhub.co.nz; (d) Canstar.co.nz [last].
- Banks whose term deposits InvestNow offers (23.3, L1076), "including": ANZ, BNZ, "Bank of China Construction Bank" [as printed - no separator between names], Heartland Bank, SBS Bank [last]. ASB is not in the printed list; a following sentence is redacted.
- Bundling exceptions (24.2, L1094-1099): (a) multi-policy insurance discount; (b) preferential pricing packages - Tertiary, Graduate, Job Starters, Headstart (School Banking), Friends and Family, "among others"; (c) loan repayments from an ASB transaction account; (d) transaction account required for overdraft service, moving money overseas, Visa Debit [last].
- Key ASB innovations (25.6, L1121-1139): (a) ASB ID; (b) Financial Wellbeing in digital; (c) Digital messaging (Josie); (d) Fraud protection (push notifications, 2-step verification, online security check-ups); (e) Education and support; (f) Other tools launched - (i) Support Finder 2021, (ii) Home Loan Explorer 2020, (iii) Apple Pay/Google Pay since 2019, Garmin Pay/Fitbit Pay since 2018 [last, L1139].
- Innovative players (25.7, L1144-1165), eleven lettered items under three sub-headings: Home Lending and Home Lending Brokerage - (a) Aera; (b) Simplicity; (c) Heartland Bank; (d) NZHL, Loan Market, Squirrel; (e) Tella, Neo. Digital banking - (f) Harmoney; (g) Sharesies; (h) Revolut. Payments - (i) Apple and Google Pay; (j) BNPL (e.g. Afterpay); (k) Worldline (previously Paymark) [last, L1165]. Heartland Bank appears here but not in the Q1 (i) home-lending list (L192-205).
- Fintech index pillars (26.1, L1181), four: Equity Investments in Fintech Companies; Usage of Fintech Credit; Digital Payments; Finance Mobile App Downloads. (L45 lists the same four as things "assessed".)
- Payments NZ report findings (26.4, L1187-1203): (a) 'leader' areas (i)-(ix) - (i) card transactions per capita; (ii) people per POS terminal; (iii) POS overall utilisation; (iv) value of card payments vs cash in circulation; (v) overall ATM utilisation; (vi) ATM withdrawals vs all retail payments; (vii) ATM withdrawals vs cash in circulation; (viii) cash in circulation relative to GDP; (ix) retail payment instruments per capita. (b) 'strong' areas "such as" (7): POS terminal fleet usage; Average combined card spend (USD); Total card volumes vs. all retail payments; Count of ATM withdrawals per capita; Credit transfers per capita; Combined credit transfers & direct debits; Credit transfer average value ($USD) [last, L1203].
- Short-term finance forms affected by CCCFA changes (27.2, L1217-1220): (a) short-term overdraft; (b) small credit card loan; (c) small personal loan.
- Impediments to innovation (29.1, L1236-1237): (a) a tight labour market; (b) the regulatory compliance burden.
- Investment envelope "in order of priority" (29.3, L1242-1248): (a) regulatory compliance; (b) sustaining technology; (c) innovation [L1248, after a page break].
- Regulatory initiatives named as spend examples (29.6, L1253): BS11, CCCFA, financial crime compliance, FSLAA "etc.". Change "underway or on the horizon" (29.7, L1255): significant prudential changes; further retail payment reforms; CoFI; Climate Change Reporting; the CDR.
- One Giant Leap capability areas (29.9, L1259): Cloud, Digital, Data, Identity.
- Suggested regulatory changes (32.3, L1295-1302): (a) principle-based regulation; (b) changing the penalty regime; (c) simplifying the disclosure regime; (d) removing barriers to innovation, e.g. reconsidering restrictions on fees [last, L1302, after a page break].
<!-- LIST -->

## 5. Definitions, rules, thresholds, scope exceptions, dated regulatory events

- "workably competitive" (L10): "the personal banking sector is, to use the relevant term, 'workably competitive'"; restated L62, L533.
- Abbreviations defined: ASB (L6); Commission (L6); PIP (L6); RBNZ (L25); BNPL (L33); NIM (L105); ROA, ROE (L110); ERP (L112); CDR (L149); API (L149); P2P (L171); B2C (L178); CoFI (L96); LVR (L259); DCS (L342); DTI (L349); CRE (L302); FSLAA, CRD, DIMS, MIS (L300); CBA group / CDE / APRA (L373); GDPR (L374); "non-banks" (L460); IDIs = "insured depository institutions i.e., banks" (L47, L467).
- NIM rule (L105-108): "the net interest margin (NIM) does not account for the cost of equity. Accordingly, for example, NIM will increase: (A) as interest rates increase even if the interest rate spread does not change; and (B) as a bank's equity share increases".
- Damodaran method as described (L119): "gives the same ERP for any country that has the same sovereign credit rating. Because New Zealand has a sovereign rating of Aaa, it is given a default spread of 0". Damodaran ERP for NZ "is the same as that for the US, Canada and Australia and lower than the ERP for the UK" (L114). NZ government debt cost "generally higher than that of the US, Canada and Australia, despite having the same (Moody's) credit rating" and "generally higher than that of the UK, despite the UK having a lower sovereign credit rating" (L121).
- Entity vs activity regulation (L68, L235): "banks are regulated at an entity level, but many of the payments made are facilitated by companies who are not similarly regulated (such as Apple, Google, Wise, etc.)".
- "***" marking rule (L244): "existing or new legislation which, in the past five years, has resulted in additional regulatory obligations". Red-text rule (L242): further regulations beyond the PIP's list "are described in red text below" (colour not extracted). Table "does not purport to be a complete list" (L242).
- BS11 threshold (L252): "a condition of registration for banks with over $10 billion in liabilities"; BS11 = "the RBNZ's policy in relation to banks' outsourcing of functions" (L376).
- LVR (L259): "Restrictions on high-LVR residential mortgage lending set a 'speed limit' on how much new low-deposit lending banks can do" (placed under the BPSA row).
- Replacement notes: BPSA 1989 "will be replaced in the near future by a new regime under the Deposit Takers Act 2023" (fn22, L276); Non-Bank Deposit Takers Act 2013 likewise (fn23, L278).
- CCCFA (L285): consumer credit contract = "where credit is loaned for personal, domestic or household purposes and interest/credit fees are payable or a security interest is taken"; "Lenders must be certified ... (unless exempt). Banks and non-bank deposit takers are exempt from certification on the basis that they are licensed by the Reserve Bank."
- FMCA fair dealing scope exception (L294): applies to "financial products and financial services (other than credit contracts)".
- Climate reporting (L302): "large, registered banks are now Climate Reporting Entities (CREs) under part 7A of the FMCA", introduced by the Financial Sector (Climate-related Disclosures and Other Matters) Amendment Act 2021.
- AML/CFT supervision split (L335): Department of Internal Affairs, the Reserve Bank, the FMA.
- DTA (L342): "will merge the currently separate frameworks for registered banks and licensed nonbank deposit takers (e.g. credit unions and building societies) under a single regulatory regime"; DCS "a fund that will compensate eligible depositors up to $100,000". The DTA sits under the heading "Proposed prudential regulation" although titled "Deposit Takers Act 2023".
- Liquidity policy review (L346): principles consulted on and finalised earlier; "completed further consultation in May 2023".
- DTI (L350): "consulted on a framework for restrictions on DTI residential lending in November 2022. When the DTI restriction framework is implemented, limits will be set" (not yet implemented as described).
- Branches of overseas banks (L353): proposal that branches "be restricted to engaging in wholesale business only, meaning they could not take retail deposits or offer products or services to retail customers" (proposed, "recently consulted").
- CoFI Act (L359-365): certain institutions including registered banks "must be licensed in relation to their general conduct towards consumers"; "market services licence"; monitored and enforced by the FMA; arose from joint RBNZ/FMA reviews "in 2018 and 2019". Listed under "Proposed other sector-specific".
- CDR (L369): MBIE discussion document on draft "Customer and Product Data Bill"; "applied to one sector at a time, and to the banking sector first"; "The application of the CDR to the banking sector is referred to as 'open banking'".
- Kāinga Ora first home loan scheme (L411): "allows customers to get into the housing market with as little as 5% deposit, underwritten by Kāinga Ora in its capacity as a provider of Lenders' Mortgage Insurance".
- Māori Freehold Land lending rule (L407): "without Government support, ASB can only apply lending for Māori Freehold Land where owners are a sole owner, joint tenants or owners in common (up to a limited number of owners), Māori Land Act Trusts or Incorporations".
- "non-banks" (L460): "firms that are not traditional banks"; "fintechs" = "primarily digital platforms that offer specific banking services, without needing to offer physical branches and cash services".
- Switching service (L483): "All major banks offer a free five-day switching service; it is as simple as a customer advising their new bank they want to switch banks. The new bank then facilitates all of the switching for the customer."
- Net refinances measure (Figure 6, L548): "the net position for each of the larger banks by charting the number of home loan titles from customers switching that business to that bank less the number of home loan titles lost to other banks".
- Concentration measures (L221): "There is no readily available robust measure of concentration or market share that includes all competitors"; "RBNZ's C5 data series is a reasonable approximation for lending, although it excludes substitutes such as BNPL. Deposit statistics will generally exclude substitutes such as fixed interest managed funds."
- Scope of study as ASB describes it (L502): Commission focus = "deposits and loans to personal customers"; proposal "to omit foreign exchange, investments and insurance"; "decision not to focus on personal consumer loans and credit cards". Cabinet Paper "envisaged that personal loans would be one of the primary focus products" (L504).
- Return measures: NIM, ROA, ROE and ERP are named and abbreviated (L105-112) but NOT defined by formula anywhere in D03; no ASB or sector NIM/ROA/ROE value is printed in D03.
- Fee position (several wordings): "there are generally no longer monthly account fees" (L483); "ASB no longer charges fees for an account ... no fees for self-service transactions or for access to online or mobile banking" (L610); "ASB no longer charges any fees for arranged overdrafts" (L612); "Removing all fees on personal accounts" (L676); transaction accounts "have become free for customers" (L684); deposit accounts "(which are now generally free)" (L762); "fee free accounts are largely ubiquitous across providers" (L779); "all major banks offering free accounts" (L1053); "(now free) transactional accounts" (L1110). Remaining fee printed: unarranged overdraft "$3 monthly" (L611).
- Compassionate care offering (L746): "ASB will pay the interest costs of up to $60,000 on eligible owner-occupied home lending for around 12 months if one of the eligible borrowers were to pass away".
- LVR and approval (L747): "approval criteria, particularly for first home buyers where supply is constrained with LVR limits".
- NZBA (L808-811): "a non-profit unincorporated organisation that acts as a forum for member banks to work together on non-competitive industry issues"; "funded by member banks through subscriptions"; "Full membership of the NZBA is open to any bank registered unders the RBNZ Act 1989" [as printed].
- Transaction abuse (L875): "occurs when people use payment transaction description fields to send abusive or coercive messages to others".
- Regional Banking Hubs (L889-894): "a pilot partnership of six New Zealand banks to provide banking services in small regional communities via banking hubs"; "Most of the hubs also have people from each bank available on site for a few hours on separate weekdays".
- Seniors line (L896): "for over 65 year old customers"; priority hour "from 9am to 10am in branch for senior and more vulnerable customers".
- Asymmetric conditions (L911): "fintechs are not subject to anywhere near the same regulatory or capital requirements as banks". Capital (L917): "New Zealand-registered banks have strict capital requirements relative to both international guidelines and to non-bank lenders operating in New Zealand."
- Stringency rule (L924): "the requirements are most stringent for institutions holding customer funds on deposit or providing consumer credit".
- Scope exception on BS11-type costs (L930): "Such costs are not required to be borne by smaller banks, or providers that are not registered as deposit-takers"; Revolut "not registered as deposit-takers in New Zealand and are not regulated by the RBNZ, nor are they required to hold capital".
- BNPL and the CCCFA (L931): "Currently, BNPL products are not subject to the CCCFA because they do not charge interest, credit fees or take a security interest over goods. While there are proposed regulations that may soon see BNPL providers classified as consumer credit providers and subject to certain obligations under the CCCFA" (proposed, not actual). BNPL defined (L1163): "a purchasing scheme that allows consumers to access goods and services now, but pay for them later through a series of flexible payment instalments".
- CDR positions (L943-957): mandating of APIs "should only occur as part of a well-designed CDR framework with a Digital ID"; reciprocity "As in the Australian CDR regime, accredited requestors should be required to share customer data as if they were also designated data holders" (L951); derived data = "the result of intricate analysis of data using proprietary methodologies developed by businesses" (L955); standards consistent with "the Payments NZ API Centre Standards" (L957).
- BankDirect (L969): "a sub-brand of ASB, rather than a separate registered bank"; withdrawn 2017.
- Switching, second statement (L1051-1054): "All major banks offer a free switching service for customers which includes moving customers' recurring payments such as automatic payments and direct debits"; "many customers do not need to 'switch' in a traditional sense ... they already hold accounts with multiple institutions and simply pick and choose which product from which provider best suits their needs ... generally leaving their account open at the bank from which they previously acquired that product".
- Main bank (L1054): customers "considered to have their main banking relationship with ASB" are distinguished from "personal customers over the age of 18" (both counts redacted; no criterion for "main banking relationship" is printed). Figure 18 caption uses "main bank" (L1018). L562 uses "main banks" for a group of banks (different sense).
- AML address verification (L1062): "The RBNZ had indicated the requirement that customers be address verified as a component of AML compliance was likely to change for most or all customers by the middle of 2023 ... However this has since been delayed as it requires a law change and no new timeframe has been communicated."
- InvestNow (L1075): "a New Zealand-based investment platform that launched in 2017. It acts as an online intermediary offering customers a way to access KiwiSaver, Managed Funds and Term Deposits".
- Bundling rule and exceptions (L1091-1099): "In general, ASB does not bundle or offer personal banking services that are only available in conjunction with other products"; exceptions (a)-(d); "there is no requirement for multiple products to be taken by a customer to receive preferential pricing" (L1095); "their loan repayments must technically be made from an ASB transaction account" (L1097). fn65 (L1101): "ASB is a distributor of insurance, not an underwriter."
- Digitally active (L1117): "(i.e. using either online banking or ASB Mobile)"; denominator "personal customers who were active with ASB".
- Fintech index (L1181): "'Aggregate Fintech Activity Index', which was an average of four 'pillars'"; alternative metric excludes "the Finance Mobile App Download pillar ... (which increased the eligible countries to 125)".
- Investment envelope (L1240-1250): "includes (in order of priority) investments in: (a) regulatory compliance; (b) sustaining technology; and (c) innovation"; FY23 amount "acts as an approximate financial ceiling". Exclusion (fn81, L1268): "the cost and time associated with responding to allegations of breaches of the bank's regulatory regime is not allocated to the investment envelope (provided that it is outside specific live projects)".
- Ownership (L1263-1274): "ASB has a long history of innovation that predates CBA's acquisition of share ownership"; Australian "Four Pillars" policy named, not explained (L1265); "a co-operative ownership structure will need to source capital from other means. To the contrary, Government ownership means a shareholder with significant financial resources" (L1274).
- Parent-backing counterfactual (L1285): "Without that backing, ASB considers that the four large banks would have a credit rating at least two notches lower (i.e. A instead of AA-) and would currently experience higher funding costs in a range of $180 - $270 million".
- Dated events in one place: late 1980s last NZ banking crisis (L133); 1989 EFTPOS launch (L1165); 1998/2003/2008 ASB share points (L537); 2011 Pepper Money enters NZ (L980); 2014 Harmoney (L1158); 2016 Apple Pay NZ (L1162); May 2016 Payments NZ report (L1185); 2017 BankDirect withdrawn (L969), InvestNow launched (L818, L1075), Finalta benchmark (L1122); June 2018 ASB mobile most popular channel (L1115); 2018 ASB ID, Garmin/Fitbit Pay (L1121, L1139); 2018 (and 2019) conduct and culture reviews (L365, L853); 13 Nov 2018 Bascand speech (L137); 2019 ASB Mobile redesign, Apple/Google Pay at ASB, Canstar award (L1115, L1139, L1121); late 2019 Community Council (L94, L828); 2020 Josie, Home Loan Explorer (L1130, L1137); Oct 2020 Better Banking Workshops (L898); March 2021 NZBA working group (L853); mid-2021 Community Bankers (L879); 2021 Support Finder, Revolut NZ registration (L1135, L1160); Oct 2021 start of ASB rate comparison (L28); late 2021 OCR begins to rise (L27); Nov 2021 Good Shepherd pilot start (L857); 2022 Kiwibank ownership change, brand refresh, co-own product (L14, L570, L578); Sept 2022 ASB submission to RBNZ (L407); Nov 2022 DTI consultation, Card Tracker launch, US Treasury report (L350, L787, L54); April 2023 Sharesies savings account (L600); May 2023 liquidity consultation completed (L346); 3 July 2023 Revolut launch (L1160); 24 July "this year" ASB CDR submission (L944); 9 Aug 2023 MBIE cabinet paper (L1255); 1 Sept 2023 Pepper Money/HSBC announcement (L980).
<!-- DEF -->

## 6. Statements about OTHER named organisations (kept apart from statements about ASB)

- Kiwibank: 100% direct Government ownership 2022; "$225 million cash injection"; "steadily growing its home lending share in recent years" (L14). "Government-funded"; "grown to over one million customers since its inception"; "should have the lowest cost of funds of any of the main banks" (L562). Brand refresh 2022; FY23 "best results in the history of the bank ... up 34% on FY22"; home lending growth "$1.1 billion, (or 1.5x market)"; deposits "rose $1.54 billion, or 6%" (L570). Injection funded "via the reinvestment of the funds received from the sale of its former investment and insurance businesses" (L571). "particularly gaining in home lending, where it is growing above the market"; expanding adviser channels, "significant cash contributions", 2022 'co-own' product (L572, L578).
- ANZ, Westpac (with ASB): "have all lost share over the period" in home lending (L572). BNZ: has "grown share" "(likely off the back of its reengagement with mortgage brokers)" (L572).
- SBS: L18; L174 (8% Capital Bond); L585 (first home buyer proposition "has caused some ASB customers to switch to SBS"; FY23 figures; "record number of first home buyer and investment members").
- TSB: L24; L585. Heartland: L25; L585. The Cooperative Bank: L26; L599.
- CBA: ASB is required "to assist CBA group to meet its regulatory requirements" (L373). Shareholders of the four largest banks described as "(Australian banks)" (L129).
- RBNZ: capital requirements increasing equity shares (L108); FSR 2023 p.24 quotation on cost structures (L132); Bascand 2018 speech "has weathered the GFC better than most" (L133); explanatory note figures (L133, fn14); C5 series (L221); liquidity, DTI, overseas-branch consultations (L346-353); BS11 (L252, L376); "RBNZ-required increases in capital for the traditional banks is likely to facilitate the expansion of non-regulated ... institutions" (L205); ASB's Sept 2022 submission to RBNZ (L407).
- Commerce Commission / PIP: "preliminary observation that the New Zealand banking sector appears to have persistently high profitability ... is likely to be overstated" (L102, NERA); Commission "uses Professor Damodaran's estimates" (L112); "finds there is little correlation between ERP and ROE" (L119); PIP volatility analysis start years (L145); PIP para 123 quotation (L455-458, fn26); Commission's reason for excluding personal loans - "level of concentration among providers of personal loans is less than for home loans" (L506); Revolut "mentioned briefly in the PIP" (L463).
- NERA: author of the attached report summarised in ES 4 (L100-147).
- Apple / Apple Pay / Alphabet (Google): L33, L68, L177, L235. Revolut: L33, L187, L463. Sharesies: L43, L171-172, L464. Harmoney: L33. Macquarie: L47, L465. Rocket Mortgage: L466. Venmo: L464. Squirrel: L171, L196, L202. Aera: L174, L181 (fn15), L203. Simplicity: L194-195. Dosh: L187, L214. Wise: L68, L216, L235.
- US Treasury, World Bank, OECD, IMF: L45-47, L462, L467, L481 (quotations with fn 6, 8-11, 27, 31-34).
- Cyber Security Agency of Singapore (L236-240): "provides centralised oversight of national cyber security functions"; oversees the Cyber Security Act.
- Kāinga Ora, Te Puni Kōkiri, The Retirement Commission, NZBA, Tāwhia: L409-425.
- Kiwibank (later): "win customers due to its more aggressive competitive position in term deposits" (L626); "expansion of competitors like Kiwibank" (L968).
- Westpac (later): "has recently offered home loan customers interest free loans for electric vehicles" (L746) with terms in fn53 (L752); acknowledged with ASB and BNZ in the Good Shepherd report (L865).
- BNZ (later): acknowledged in Good Shepherd report (L865); a bank whose term deposits InvestNow offers (L1076). ANZ: InvestNow term deposit bank (L1076); in Figure 10 legend (L645).
- Heartland (later): "providing online only distribution (i.e. application and approval)" (L1147); InvestNow term deposit bank (L1076). SBS: InvestNow term deposit bank (L1076). Co-op, TSB: Figure 10 legend only (L645).
- CBA (later): innovation "predates CBA's acquisition of share ownership" (L1263); "CBA's ownership has, if anything, supported ASB's ability to continue to innovate" (L1265); "a large parent that has greater resources" (L1267); Support Finder as "leveraged innovation" (L1267); "CBA can take a long-term view" (L1272).
- "The four large banks" / "large Australian-owned banks" (L1281-1285): "enable New Zealand borrowers to access a greater volume of funds than New Zealand domestic savers can provide"; borrow at lower cost because of parent backing; counterfactual rating and cost range (L1285). The four are not named in D03.
- HSBC (L970-982): said it could "no longer justify investing into the business [Wealth and Personal Banking]" (fn59); media release quotation (fn60); Reuters report (fn61); mortgage portfolio "$1.4bn" to Pepper Money (L980). Pepper Money: "Australian non-bank lender", "ASX listed", "one of Australia's leading non-bank lenders", in NZ since 2011; CEO Mario Rehayem quotations (L980, fn63).
- Macquarie Bank: "rapid growth ... in Australia" (L719).
- Revolut (later): online-only nationwide (L736); "not registered as deposit-takers in New Zealand and are not regulated by the RBNZ" (L930); entry (L968); HQ London, currencies, waitlist, launch date (L1160). Sharesies: L600 (savings account April 2023), L721, L736, L968, L1159 (500,000 customers; deposits "held in a trust by an undisclosed New Zealand bank"). Squirrel: L600, L721, L1149. Forsyth Barr: L600. InvestNow: L818, L964, L968, L1058, L1075-1078, L1083. Aera: L736 (printed "Area"), L1144. Harmoney: L1158. Simplicity: L1145. Tella, Neo: L1151. Apple / Google: L930, L1162. Worldline (Paymark): L1165.
- RBNZ (later): BS11 (L928); AML address-verification indication and delay (L1062); "RBNZ Act 1989" membership wording (L811).
- MBIE: CDR Discussion Document (L944); cabinet paper of 9 August 2023 on CCCFA (L1255). FMA: P2P licence to Harmoney (fn69); 2018 review with RBNZ (L853).
- Commerce Commission (later): "the Commission's reference to the withdrawal of ASB's BankDirect brand in 2017" (L969).
- NZBA (L808-811, L852-855); Payments New Zealand / Payments NZ (L843, L957, L1185-1203); Good Shepherd New Zealand (L857-868); Age Concern New Zealand, Women's Refuge, Public Trust (L873); MoneyTalks (L845); Finalta (fn66, L1122); Canstar (L1073, L1121); World Bank (L1168-1181); UK Finance (fn58).
- Regional hubs: "five other banks" (L730) / "six New Zealand banks" (L889) - the other banks are not named in D03.
<!-- ORG -->

## 7. Hedged claims (claim | hedge word | what the hedge attaches to)

- L14 | "is expected to increase Kiwibank's access to capital" | "expected" | effect of 2022 ownership move (repeated L570).
- L18, L585 | "approximately 12%"; "closer to 3.5%" | approximations | SBS growth figure; industry growth rate.
- L47 | "competition is only likely to increase from non-bank players" | "suggests", "only likely" | future competition (ES 1.10).
- L47, L467 | non-banks "appear to be contributing to competitive pressures" | "appear" | US Treasury's quoted finding.
- L47, L467 | "digital technology may have a large impact" | "may" | OECD quoted statement.
- L48 | "Competition is likely to intensify" | "likely" | future competition from new business models.
- L70 | "are likely to mean yet more innovation" | "likely", "in ASB's view" | effect of DTA / real time payments / open banking (repeated L241).
- L94 | "certain consumer groups may find it more difficult to navigate the financial system" | "may" | consumer groups' difficulty.
- L96 | "to the extent there are any residual concerns ... CoFI will provide further assistance" | conditional | residual concerns; the CoFI effect itself is stated with "will".
- L102 | Commission's observation "is likely to be overstated" | "likely" | NERA conclusion on the Commission's profitability observation; the Commission's own observation is that the sector "appears to have" persistently high profitability.
- L114-117 | "On its face, this is surprising" | "on its face" | Damodaran ERP equality.
- L119 | "this appears to be because" | "appears" | NERA's explanation of little ERP/ROE correlation.
- L121 | "presumably on Professor Damodaran's own logic" | "presumably" | the logic imputed.
- L127-132 | "if the four largest New Zealand banks do persistently derive higher ROE ... this: (A) may be at least partly justified ...; (B) may be partly explained ...; (C) likely reflects (accounting) cost efficiencies" | "if", "may", "may", "likely" | the premise is conditional; (A) and (B) are "may", (C) is "likely".
- L177 | Apple "reportedly accounting for US$30 billion" | "reportedly" | the US$30 billion figure.
- L205 | "it is reasonable to assume that the RBNZ-required increases in capital ... is likely to facilitate the expansion" | "reasonable to assume", "likely" | effect of capital increases.
- L337 | role of Privacy Act "will likely become more prominent" | "likely" | future prominence.
- L376 | BS11 "is expected to have cost ASB approximately $[Redacted] million" | "expected", "approximately" | cost figure.
- L382 | Māori economy "is estimated at just under $69 billion" | "estimated", "just under" | the figure.
- L400 | aspects of competition "may have a particular impact on Māori" | "may" | impact.
- L409 | "in discussions with Kāinga Ora to potentially provide Government guarantee support (at some level)" | "potentially" | the guarantee; "This would unlock better access".
- L463 | Revolut "is expected to eventually introduce open banking features, loan partnerships and apply for a New Zealand banking license" | "expected", "eventually" | future Revolut actions (not actual actions).
- L467 | "competition from non-banks is already material and is likely to keep growing" | "likely" | growth; materiality is stated firmly.
- L511 | "approximately 57%"; "it is estimated that only around a third"; "more than 2.7 million"; "around $600 million" | approximations | credit card / mortgage statistics.
- L562 | Kiwibank "should have the lowest cost of funds of any of the main banks" | "should" | cost of funds (reasoned from Government funding, not a reported figure).
- L572 | BNZ "(likely off the back of its reengagement with mortgage brokers)" | "likely" | the cause of BNZ's share growth, not the growth itself.
- L604 | "even the smallest of rate differentials can have a material impact on share" | "can" | the effect; introduced "In ASB's view".
- L734 | "some subtle differences between some regions ... this does not drive any relevant variation in the overall level of competition" | none on the main claim | the regional-variation denial is firm; "subtle differences" is conceded.
- L816 | broker growth "is likely to be at least partly driven by the CCCFA requirements" | "likely", "at least partly" | the cause; "Broker numbers have been increasing" is firm.
- L913 | sunk costs "may prove to be high at the start-up and market entry stages" | "may" | size of sunk costs.
- L931 | "proposed regulations that may soon see BNPL providers classified as consumer credit providers" | "proposed", "may soon" | future classification; current exemption stated firmly ("Currently ... not subject to the CCCFA").
- L942 | "to the extent there remains any perceived or real impediments to switching, then a carefully designed open banking framework has the potential to reduce any such friction" | "to the extent", "has the potential" | both the premise and the effect; followed by "we need to be realistic about what such a framework may achieve".
- L944 | "A well-designed CDR has the potential to do this" | "potential" | CDR benefits.
- L948 | "While this may mean progress may be slower than some may hope" | "may" x3 | pace; "getting this aspect right is critical" is firm. "International experience suggests that trying to build in the necessary resilience after the initial implementation is difficult" | "suggests".
- L955 | including derived data "may have the unintended consequence of stifling innovation" | "may" | consequence; "risks undermining intellectual property rights" also hedged by "risks".
- L957 | data holders "are likely to be the best placed to comment" | "likely" | suitability.
- L962 | "it has been estimated that the cost incurred in the UK ... was £1.5bn" | "estimated" | the £1.5bn figure.
- L968 | "The international experience suggests this trend will only continue" | "suggests" | continuation.
- L1062 | RBNZ "had indicated" requirement "was likely to change ... by the middle of 2023" | "indicated", "likely" | a forecast, followed by the firm statement that it "has since been delayed".
- L1122 (fn66) | "This figure is now higher" | unquantified | the 77% digital-activity figure.
- L1144 | Aera's offering "appears to be the first 'integrated proposition' from savings to home ownership in New Zealand" | "appears" | the "first" claim.
- L1159 | "Sharesies states it has over 500,000 customers" | attribution "states" | customer count.
- L1160 | Revolut "claims to offer free deposit accounts and cheaper money transfers"; "is expected to eventually introduce open banking features ..." | "claims"; "expected", "eventually" | offering as claimed; future actions.
- L1213 | "a few pockets of demand which may not yet be fully met" | "may" | unmet demand.
- L1257 | "if the bank's technology fails, that failure may result in a breach of a compliance obligation" | "if", "may" | link to compliance ("peripherally linked").
- L1265 | "CBA's ownership has, if anything, supported ASB's ability to continue to innovate" | "if anything" | direction of effect; the 9% to 18% and $10 billion figures in the same paragraph are stated firmly.
- L1285 | "ASB estimates that the four large banks are able to borrow at a lower cost"; "ASB considers that the four large banks would have a credit rating at least two notches lower ... and would currently experience higher funding costs in a range of $180 - $270 million" | "estimates", "considers", "would", "at least", range | counterfactual estimate, not an observed cost.
- L1302 | restrictions on fees "which may act to limit product innovation" | "may" | effect of fee restrictions.
- Firm (unhedged) claims sitting near hedged ones, for contrast: "the personal banking sector is ... 'workably competitive'" (L10, "In ASB's view"); "customers can and do switch between / try services ... with comparative ease" (L940); "switching is easy for customers" (L1087); "ASB believes there is strong competition across all personal banking categories" (L682).
<!-- HEDGE -->

## 8. Footnotes (location; any that qualify or restate a body figure)

Footnotes are interleaved at page bottoms, numbered continuously.
- fn1 L19 Kiwibank media release URL (Kiwi Group Capital invests $225 million) - source for L14. Same URL as fn41 (L575).
- fn2 L20 SBS media release URL - source for L18; URL fragment contains "16% from the previous year" (not in body). Same URL as fn42 (L586).
- fn3 L34-35 TSB media release URL (fragment: "TSB reported a net profit ... Shareholder, philanthropic organisation Toi Foundation") - source for L24. Same as fn44 (L589-590).
- fn4 L37-39 Heartland investor presentation slide 18 (Heartland Group FY23 Investor Presentation) - source for L25. Same as fn45/46.
- fn5 L40 Cooperative Bank Annual Results - L26.
- fn6 L52 World Bank 2022 publication. fn7 L53 macquarie.com.au. fn8 L54 US Treasury Nov 2022 p.5. fn9 L55-56 World Bank 2023 p.17. fn10 L57 OECD 2020 p.7. fn11 L58 US Treasury (URL dated 2018-08) p.5.
- fn12 L135 RBNZ (2023) Financial Stability Report p.24 - source of the cost-structure quotation at L132.
- fn13 L137 Bascand speech 13 November 2018. fn14 L138 RBNZ explanatory note on portfolio risk modelling (source of Figures 2-3).
- fn15 L181 Aera description: "Founded by NZ entrepreneur Derek Handley, Aera is a non-bank lender offering attractive annual savings rates for home loan deposit savers, positioned specifically against the larger New Zealand banks." (a statement about Aera made by ASB.)
- fn16 L182 Apple newsroom (2023/04). fn17 L183 Forbes (2022/09/08).
- fn18 L184 "As at June 2023." - QUALIFIES the body figures at L177 (Apple Pay 5% of credit card spending, 10% of debit card spending) by supplying the as-at date; no source.
- fn19 L208 FMT and Midlands URLs. fn20 L209 Stuff article "largest-finance-companies-double-home-loan-market-share-since-2020". fn21 L210 interest.co.nz Squirrel.
- fn22 L276, fn23 L278 - QUALIFY the table rows: BPSA 1989 and Non-Bank Deposit Takers Act 2013 "will be replaced in the near future" by the Deposit Takers Act 2023.
- fn24 L386 RBNZ outsourcing policy URL (BS11). fn25 L413-414 ASB's RBNZ submission "from page 83 to 87".
- fn26 L468 "PIP, para 123." fn27 L470 IMF GFSR Ch.3 2022. fn28 L471 Revolut. fn29 L472 AFR (Macquarie; URL date 20230210). fn30 L473 Forbes Advisor. fn31 L474 = fn8. fn32 L475-476 = fn9. fn33 L477 = fn10. fn34 L493 = fn11. fn35 L494 FIS Global Payments Report URL.
- fn36 L514 The Global Economy. fn37 L515 RNZ Mediawatch (URL fragment: "Senior business journalist Miriam Bell ... over the next 12 months"). fn38 L516 Stuff (URL fragment: "More than 2.7 million people ... on credit card interest payments").
- fn39 L573 Kiwibank full year results media release. fn40 L574 interest.co.nz (URL fragment "kiwibank-june-year-profit-hits-175-mln") - gives a profit level in the URL only. fn41 L575 = fn1.
- fn42 L586 = fn2. fn43 L587 "Ibid." fn44 L589-590 = fn3. fn45 L592-594 = fn4. fn46 L595 "Ibid, slide 18."
- fn47 L616 Cooperative Bank Annual Results "(at page 6)" (same URL as fn5, which gives no page). fn48 L617 "Ibid, at page 6."
- fn49 L619 Squirrel on-call account URL. fn50 L620 Stuff ("new-account-aims-to-level-the-playing-field-for-savers"). fn51 L621 sharesies.nz/save. fn52 L622 "[Redacted]" (the footnote itself is redacted).
- fn53 L752 NZ Herald URL plus a sentence - ADDS figures and conditions absent from the body (L746): "Westpac will offer home loan customers interest-free loans of up to $50,000 for five years to purchase an electric vehicle or other energy-efficient technology, subject to lending and affordability criteria." URL text also says "but-theres-a-catch".
- fn54 L836 nzba.org.nz/about-us (attached to the NZBA membership sentence at L811).
- fn55 L890 Good Shepherd New Zealand "Economic Harm Support Service Pilot - Interim six-month report" (URL "6-month-insights-report", 2022/08). Body calls it "the pilot review report" and the pilot "12 months from November 2021" (L857, L865).
- fn56 L891 NZBA regional banking hubs pilot URL.
- fn57 L934 businesswire URL - URL text only: "New-Zealand-Buy-Now-Pay-Later-Market-Report-2023-A-2.41-Billion-Market-by-2028-Featuring-OpenPay-Afterpay-humm-Laybuy-Zippay-Payright-Genoapay-Art-Money" (dated 20230317 in the path). Supports body phrase "continues to record strong growth" (L931); no figure in body.
- fn58 L972 UK Finance press release (source of £1.5bn). fn59 L973 HSBC webpage "Latest updates on the New Zealand wind-down" "(available here)" - hyperlink target lost. fn60 L974 "See the media release (available here)" - hyperlink target lost. fn61 L976 Reuters URL dated 2022-11-30.
- fn62 L1012 interest.co.nz ("australian-non-bank-lender-pepper-money-acquiring-14- bln-nz-mortgage-portfolio-hsbc"). fn63 L1014 "Pepper Money buys HSBC's NZ residential mortgage portfolio (businessnewsaustralia.com)".
- fn64 L1079 investnow.co.nz.
- fn65 L1101 "ASB is a distributor of insurance, not an underwriter." - QUALIFIES the multi-policy discount exception at L1094.
- fn66 L1122 "Finalta's 2017 benchmark put ASB first in Australia and NZ, and 2nd globally (of 200 banks), for digital activity amongst personal customers at 77%. This figure is now higher." - attached to redacted body figures at L1113; the only unredacted numbers for that sentence, on a 2017 basis.
- fn67 L1124 ASB ID app and Canstar 2019 award URLs. fn68 L1153 ASB "branch-changes-workshop" URL (attached to L1133).
- fn69 L1169 FMA media release (first P2P licence). fn70 L1170, fn72 L1172 Revolut "launches_in_new_zealand" (same URL). fn71 L1171 Revolut about page. fn73 L1173 financemagnates ("apple-pay-launches-in-new-zealand-now-available-in-11-countries"). fn74 L1174 nzbusinesstraveller.
- fn75 L1175 = fn17. fn76 L1176 "As at June 2023." = fn18 - supplies the as-at date for the Apple Pay 5% / 10% figures at L1162.
- fn77 L1178 paymark.co.nz our-story. fn78 L1205 = fn6. fn79 L1206 Payments NZ article URL. fn80 L1207 "Ibid, p4."
- fn81 L1268 investment-envelope exclusion - QUALIFIES the (redacted) FY23 envelope figure at L1250; placed mid-Q30 by pagination.
- Total: 81 numbered footnotes (1-81), all located. The "1" after "in the world." at L1185 is a marker inside the quoted Payments NZ text, not a D03 footnote.
- Footnotes that carry numbers the body does not: fn2/fn42 (16% in URL), fn40 (175 mln in URL), fn53 ($50,000, five years), fn57 (2.41 billion by 2028 in URL), fn66 (77%, 2nd of 200 banks, 2017), fn73 (11 countries in URL), fn47-48 (page 6), fn25 (pages 83 to 87).
<!-- FN -->

## 9. Figures stated more than once inside D03 (same or different wording)

- Kiwibank $225 million injection: L14 and L571 (same value; L571 adds funding source).
- Kiwibank 100% Government ownership 2022: L14 ("100% direct Government ownership") vs L570 ("acquiring 100% of Kiwibank's parent company").
- SBS home lending ~12% / industry ~3.5%: L18 (paraphrase) and L585 (quotation, adds "$3.6 billion to $4.0 billion").
- TSB 1.6x / 6% / $6.2 billion: L24 and L585 (identical).
- Heartland retail deposit growth ranking: L25 ("FY2023") and L585 ("FY23").
- Cooperative Bank 8%: L26 and L599.
- Macquarie 5%: L47 (fn7) and L465 (fn29).
- ASB regulatory spend FY23: L66 and L233 (both redacted).
- "five" major banks: L11, L13, L524, L533; "four largest New Zealand banks": L127 (NERA context).
- US Treasury / World Bank / OECD quotations: L47 and L467/L481.
- Refix outreach 12,000 / 6,000 / $1.1 million / July 2021 to June 2023: L83-87 and L901 (verbatim).
- Home Central visit counts: L89 and L606 (both redacted).
- ASB Community Council (late 2019, quarterly, chaired by CEO): L94-95 and L828.
- 404,000 digital financial wellbeing tool users: L785 ("last year") and L1128 ("Over the past financial year ... (up 39% on FY22)").
- Apple Pay vs Mastercard and NZ 5% / 10% shares "As at June 2023": L177 (fn17-18) and L1162 (fn75-76), verbatim.
- World Bank fintech ranks: L45 (summary: "5 out of 74 countries on one measure and 4 out of 125 countries on the other") and L1168-1181 (which names the two measures).
- BS11 threshold: L252 ("over $10 billion in liabilities") and L928 ("over $10bn in liabilities"). BS11 cost: L376 (redacted), L928 ("significant financial outlay").
- Broker-originated share of ASB home lending: L816, L995, L1084 (all redacted).
- InvestNow launched 2017: L818 and L1075.
- Revolut "is expected to eventually introduce open banking features, loan partnerships and apply for a New Zealand banking license as it has done overseas": L463 and L1160 (verbatim).
- Aera description: fn15 (L181) and L1144. Sharesies deposits held in trust by an undisclosed New Zealand bank: L43 and L1159.
- Simplicity / NZHL, Loan Market, Squirrel / Tella, Neo descriptions: L194-197 and L1145-1151. BNPL description: L207 and L1163.
- "five major banks": also L1226; "larger five banks" L528. "four large banks": L1283, L1285 (ASB's own words) besides L127/L131 (NERA summary).
- Support Finder: L654, L789 ($14.3m, FY23), L832, L1135 (launched 2021), L1267. Card Tracker: L651, L787. Better Banking Workshops: L898, L1133. Community Bankers: L678, L879-884.
- Deposit Takers Act effect on deposit competition: L485 ("reducing the perceived risk of investing with smaller less well-known institutions") and L1060 ("reducing the risk of investing ...").
- Executive Summary paragraphs reused almost verbatim in answers: ES 2.2-2.3 (L66-68) = Q3 3.3-3.4 (L233-235); ES 3.3-3.5 (L83-92) = Q15 15.17-15.18 (L901-904); ES 3.6 (L94-95) = Q15 15.2 (L828); ES 1.4 (L16-26) = Q9 9.19-9.22 (L585-599); ES 1.8 (L45) = Q26 26.1-26.2 (L1168-1183); ES 5.1-5.3 (L149-153) = Q18 18.3, 18.5 (L943-948) and Q32 32.4 (L1304); ES 1.2 (L13) = Q9 9.6 (L533).

### Same subject, different wording or basis inside D03 (both locations; no precedence stated by the document)
- ASB share: L537 "going from 9% in 1998 to 13% in 2003 and 17% in 2008" (sentence about growing "its home loan book" and doubling "its overall size") vs L1265 "over the past twenty-five years ASB has grown its share of total banking assets from 9% to 18%".
- Conduct and culture review year: L365 "in 2018 and 2019" (RBNZ and FMA joint reviews, banks and life insurers) vs L853 "FMA/RBNZ Bank Conduct and Culture Review in 2018".
- Act under which banks are registered: L254-257 BPSA 1989 "Provides for registration of banks"; L247-249 "Reserve Bank of New Zealand Act 2021 (RBNZ Act)"; vs L811 "any bank registered unders the RBNZ Act 1989".
- Switching service: L483 "free five-day switching service" vs L1051 / L1087 "free switching service" (no duration).
- Figure 10: L628 prose "market shares for term deposits" vs L630 caption / L644 axis "Deposits".
- Kiwibank ownership: L14 "100% direct Government ownership" vs L570 "New Zealand Government acquiring 100% of Kiwibank's parent company".
- Heartland period label: L25 "FY2023" vs L585 "FY23".
- DTA status: table heading "Proposed prudential regulation" with row "Deposit Takers Act 2023 (DTA)" and "The Bill also introduces" (L339-342) vs fn22-23 "a new regime under the Deposit Takers Act 2023" "in the near future" (L276-278) vs "planned legislation ... such as the Deposit Takers Act" (L241).
- CoFI: named "Financial Markets (Conduct of Institutions) Amendment Act 2022" (L96, L356-364) and listed under "Proposed other sector-specific" (L355); abbreviation "CoFI" (L96) and "CoFI Act" (L364).
- Retail Payment System Act 2022 is abbreviated "RSPA" as printed (L306).
- "Deposit to Income Rules" (L70) vs "debt-toincome (DTI) restriction framework" [as printed, hyphen lost] (L349) and "restrictions on DTI residential lending" (L350).
- Aera spelled "Area" at L736.
- Home Central: "In the last month alone" (L89) vs "In the past month alone" (L606).
- ASB regulatory spend FY23: "$[Redacted] million" (L66, L233) vs "$[Redacted]" without "million" (L1253).
- Regional hub participants: "five other banks" (L730) and "six New Zealand banks" (L889) - consistent counts on different bases (others vs total).
- Apple Pay dates: "Apple launching in 2016" in New Zealand (L1162) vs "ASB has offered Apple Pay and Google Pay since 2019" (L1139) - different subjects.
- Digital activity: 77% (Finalta 2017 benchmark, personal customers, fn66 L1122) vs 90% (June 2023, active personal customers, L1117) vs 71% (June, bank-active customers over 65, L1133) - three different bases.
- Credit-card holders: "approximately 57% of New Zealanders aged 15+" (2021, L511) vs "more than 2.7 million people" (April 2022, L511) - share vs count, different dates and sources (fn36, fn38).
- Non-bank home-loan share: 3% -> 6% ("largest finance companies", named four "including") vs 10% -> 14% ("non-bank and so-called second tier lenders"), both 2020 vs 2022, same Stuff article (L200).
<!-- DUP -->

## 10. Gaps and extraction problems

- All 20 figures/charts are caption-only or "[Redacted]" (Figure 10 also keeps axis and legend text): no chart data values anywhere in the text.
- Regulation table extracted as running text; red-text marking lost.
- Redactions: L30, L66, L89 (x3), L233, L376, L528, L544-568 (Figures 5-8, para 9.14 and surrounding sentences).
- Later redactions: L600 (end of 9.23), L603 (9.25) and fn52 L622, L606 (x3), L608, L626, L693-695 (Figure 11), L706-719 (10.14 part, Figures 12-13, 10.15, start of 10.16), L732 (10.20 survey data), L816 (x4), L989-1010 (20.1 part, Figures 15-17, 20.2 parts, 20.4, 20.5), L1019-1021 (Figure 18), L1030-1039 (21.1-21.3, Figure 19), L1054 (x2), L1076, L1084, L1113 (x2), L1250 (x2), L1253 (x5), L1257, L1259 (x2). Total 59 "[Redacted]" tokens. Consequence: ASB's own market shares, NPS, marketing spend, fee totals, regulatory spend, broker share, customer counts by main-bank status and all survey results are NOT available from D03.
- Missing source text (not unread): the attached NERA Report; all chart images/data (Figures 1-4, 9, 10, 14, 20); two "(available here)" hyperlink targets (fn59, fn60) and "can be found here" at L418; red-text marking in the regulation table.
- Layout artefacts that affect verbatim matching: running header "Public Version" + page number sometimes glued to the next sentence (e.g. L43, L117, L187, L458, L546, L578, L687, L811, L868, L894, L1181); paragraph numbers glued to the previous paragraph's end (e.g. "7 1.10" L47, "12 4.2" L132, "40 9.16" L570, "43 9.20 ... 44 9.21" L585, "80 26.4" L1185); footnote markers fused to preceding digits or words (e.g. "Index".6" L45, "period.7" L47, "FY22.39" L570, "6%.40" L570, "FY22.47" L599, "overall.48" L599, "money.49" and "month.50" L600, "2023. 51" L600, "vehicles;53" L746, "1989.54" L811, "£1.5bn;58" L962, "portfolio.62" L980, "digital.66" L1113, "2016.73" L1162, "spending.76" L1162); words joined where a line-end hyphen was dropped ("toaccelerate" L19, "debt-toincome" L349, "nonbank" L342, "Climaterelated" L300, "welldesigned" L149, "triggerbased" L657, "one-onone" L882, "marketwide" L1094); sentences or lists split across line or page breaks (L83/L87, L808/L811, L1244/L1248, L1295/L1299 at page breaks; L28, L50, L172, L190, L195, L612, L880 at plain line breaks).
- Page markers: 48 "Public Version" headers (L3 and pages 2-48).
- Unread ranges: none. Coverage of readable text: complete (L1-1306).

## 11. Densest numeric regions (unredacted), by line range

- L14-28 (ES 1.3-1.5): Kiwibank, SBS, TSB, Heartland, Cooperative Bank growth figures; ASB 12-month rate changes.
- L45-47: World Bank ranks; Macquarie 5%.
- L83-87: ASB refix outreach counts.
- L171-202 (Q1): KiwiSaver providers, Apple, Apple Pay shares, non-bank home-loan shares, Launchpad 80%.
- L382-423 (Q4): Māori economy, home ownership rates, 5% deposit, 1,500 schools.
- L463-466 (Q7): Revolut global figures; Macquarie.
- L511 (Q8): credit card and mortgage penetration.
- L537 and L562-599 (Q9): ASB share points; Kiwibank FY23; SBS, TSB, Heartland, Cooperative Bank FY23 amounts (the single densest line is L585).
- L608-612: fee levels. L644-645: Figure 10 axis text.
- L746-752 and L784-789 (Q11): compassionate care, Westpac EV loan, ASB tool usage counts.
- L853-898 (Q15): dates and programme counts.
- L962-980 (Q18-19): £1.5bn; HSBC $1.4bn; dates.
- L1113-1165 (Q25): digital activity percentages, launch years, Sharesies and Revolut counts, Apple Pay shares.
- L1181-1203 (Q26): fintech ranks; Payments NZ benchmarks.
- L1265 and L1285 (Q30-31): ASB share of total banking assets and equity; funding-cost counterfactual.
- Numerically dense but redacted: L544-568, L816, L989-1039, L1054, L1250-1259.

## 12. Basis index for the unredacted figures (line pointers only)

- ASB only: L7 (years, staff, customers incl. business and rural); L28 (12-month home lending and term deposit rate changes since Oct 2021); L83-87 = L901 (outreach); L423 (GetWise schools); L537 (9% / 13% / 17%); L611 (overdraft fee levels); L746 (compassionate care); L784-789 (tool usage, Support Finder $14.3m FY23); L871 (Extra Care referrals); L879-884 (Community Bankers); L1115-1139 (digital dates, 90%, 71%, 404,000 up 39%); L1122 (Finalta 77%, 2017); L1265 (9% to 18% of total banking assets; $10 billion equity).
- Four large banks (ASB's estimate): L1285 ($180 - $270 million; A vs AA-). Four largest banks (NERA summary, no numbers): L127-132.
- Other named NZ banks, from their own releases: Kiwibank L14, L562, L570-571; SBS L18, L585; TSB L24, L585; Heartland L25, L585; Cooperative Bank L26, L599; Westpac fn53 L752; HSBC L980.
- NZ market or population wide: L18/L585 (industry home lending growth ~3.5%, via SBS release); L171 (37 KiwiSaver providers); L177 = L1162 (Apple Pay 5% / 10%, June 2023); L200 (non-bank new home loan shares 2020 vs 2022, CoreLogic via Stuff); L382 (Māori economy); L404 (home ownership 31% vs 52%, June 2022); L511 (credit cards, mortgages, interest paid); L1160 (26,000 waitlist); L1189-1203 (Payments NZ benchmarks, 2016 report); L45 = L1181 (fintech ranks).
- RBNZ-sourced items: Heartland retail-deposit growth ranking "based on balance sheet data from the Reserve Bank" (L25, L585); Figure 9 source (S31 series and Dashboard, L581); Figure 10 source (Dashboard, L631); RBNZ FSR 2023 p.24 quotation (L132); Figures 2-3 from RBNZ explanatory note (L133-144); C5 series comment (L221). No RBNZ number is printed in D03 other than thresholds ($10 billion BS11, $100,000 DCS).
- International: L45-47, L177, L463-466, L962, L1122, L1159 (Australia and NZ combined), L1160, L1191-1197.
- KPMG: not mentioned anywhere in D03. NERA: named as author of the attached report; no NERA number is printed in D03.
<!-- GAP -->
