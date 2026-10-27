# aq-03170 - document map

Maintained by the caller from `text/`. Navigation only; questions quote the documents, never this map.
Line numbers (L) are lines of `text/Dnn.txt`. Local ids are alphabetical by file name and differ from the task
page's Doc numbers: use Doc N in every form field.

## Bundle

- What it is: thirteen comment letters to the SEC on its proposed rule "Safeguarding Advisory Client Assets"
  (Release No. IA-6240, February 15, 2023; 88 Fed. Reg. 14672, March 9, 2023; File No. S7-04-23) and on the reopening
  of its comment period (Release No. IA-6384; 88 Fed. Reg. 59818, August 30, 2023). Ten letters are dated October 25
  or 30, 2023; three are later (December 7, 2023; February 6, 2024; May 28, 2024).
- Documents: 13; ids from `text/manifest.json`; 417,067 characters, 88,317 prompt tokens.
- Gaps: none. Capture header: "13 of 13 read in full"; every `matches_capture` true, `gap_characters` 0. The capture
  note about reloading the page concerns the form's buttons, not the documents.
- Extraction spot-checks (2026-10-12): plain-text originals, so no page counts. Script comparison of every `docs/`
  file with its `text/` body: identical except one trailing blank line, the ellipsis character written as three dots
  (D04 L39, D07 once) and a spacing cedilla in D04 L526. A quote that crosses one of those three spots must be taken
  from `docs/`; q01's five evidence quotes were found verbatim in the originals and in the capture. D03's Appendix A
  mark-up has lost its strikethrough and underline (removed and added words run together); D05 and D07 carry OCR
  ligatures ("ofthe", "exisƟng").
- Provenance: notes/intake.json, capture sha256 592dd07e..., one capture, no history.
- Reuse binding: source hashes in text/manifest.json; no earlier task shares them.
- Coverage: all thirteen read in full by the author on 2026-10-12.

| Local id | Task page | Author (signer) | Date | Chars |
| --- | --- | --- | --- | --- |
| D01 | Doc 1 | Blackstone Inc. (John Finley, Chief Legal Officer) | October 25, 2023 | 30,189 |
| D02 | Doc 4 | American Securities Association (Jessica R. Giroux, General Counsel) | October 30, 2023 | 10,304 |
| D03 | Doc 10 | JPMorgan Chase & Co. (Teresa Heitsenrether, Troy Rohrbaugh) | October 30, 2023 | 69,092 |
| D04 | Doc 9 | Futures Industry Association (Allison Lurton) | October 30, 2023 | 97,642 |
| D05 | Doc 7 | Milbank LLP, for aircraft adviser clients | October 30, 2023 | 31,684 |
| D06 | Doc 5 | TIAA and Nuveen (John McCally, Churchill Asset Management) | October 30, 2023 | 21,359 |
| D07 | Doc 8 | Investor Choice Advocates Network, ICAN (Nicolas Morgan) | October 30, 2023 | 17,216 |
| D08 | Doc 2 | The Real Estate Roundtable (Jeffrey D. DeBoer) | October 30, 2023 | 18,437 |
| D09 | Doc 3 | Managed Funds Association (Jennifer W. Han) | October 30, 2023 | 18,067 |
| D10 | Doc 6 | Investment Adviser Association (Gail C. Bernstein, Laura L. Grossman) | October 30, 2023 | 26,776 |
| D11 | Doc 11 | AICPA Investment Companies Expert Panel (Jaime Eichen, Daniel Noll) | December 7, 2023 | 38,305 |
| D12 | Doc 12 | Association of Global Custodians (Steven Wager) | February 6, 2024 | 27,772 |
| D13 | Doc 13 | Blockchain Association (Marisa T. Coppel, Laura Sanders) | May 28, 2024 | 10,229 |

## Per document

- D01 Blackstone: life sciences "Contracts" (defined wider in fn 2, L37: music and film rights, litigation
  settlements, life insurance contracts, accounts receivable). Staff meeting "August 2nd" (L12). fn 1 (L17): joint
  trades letter (Sep. 12, 2023) and AIC letter (May 8, 2023), neither Blackstone's. Four asks (L23-29). fn 12 (L101)
  privately offered security test; fn 15 (L115) five conditions of the exception. Legacy exception modelled on the
  Private Fund Adviser Rule (L122). Figures: $2.6 billion, 84.7%, twenty-seven drugs, $8 billion, over 80%, more than
  three dozen Contracts (L126). Same counsel's template as D08 (near-identical paragraphs).
- D02 ASA: general objections; Re line cites the reopening release; no figures, no earlier letter cited.
- D03 JPMorgan: Parts A-E (cash segregation safe harbor, asset scope, custodian liability, adviser authority,
  rehypothecation). Own May 8, 2023 letter (L14, L22). Cites LSTA June 20, 2023 (L103), FIA's FAQ (L117), IAA May 8,
  2023 (L207). Three custody elements (L80); four exclusion principles (L125-130). Appendix A mark-up (L244-301).
  Appendix B (L304-416) "copied with permission from FIA's comment letter dated May 8, 2023" (L319): eleven proposed
  requirements against CFTC rules (17 business days, 60 days, monthly statements).
- D04 FIA: body L13-133 (statutory trust, CFTC rules, MF Global $1.6 billion fn 35). Own May 8, 2023 letter (L13,
  L21). Appendix A from L136: FAQ "Protection of Customer Funds", Version 4.0, revised November 2014, 24 questions
  (three account classes; $1 billion regulatory capital; 25 percent residual-interest withdrawals; 20 percent
  buffer outside the US; 17 business days; six weeks; $100 million fund, $25,000 and $100,000).
- D05 Milbank: aircraft assets. Re line prints "File No. S7-18-21" (L13), unlike every other letter. Questions 3 and 4
  (L20), Question 149 (L142). SEC's assumption of about 8,000 transfers (L157). Quotes KPMG, Ernst & Young, PwC
  (May 8, 2023), Deloitte (May 3, 2023), ABA et al. (L144-151, L199). Closing keep-list labels paragraphs (b)(3),
  (b)(4), (c)(4) (L206-214) where its own earlier text uses (a)(3), (a)(4), (b)(4).
- D06 TIAA/Nuveen: commercial loans; fallback exception for institutional SMAs and CLOs. Agrees with SIFMA AMG's
  letter (L41, L94-99). Securitized asset fund audit exception of the Private Fund Advisers Rule (L87). Figures: 1918,
  2000, five million customers, 15,000 institutions, over $1 trillion.
- D07 ICAN: asks withdrawal. Quotes AIC's "May 2023 letter" (L74) and "the Investment Adviser Association in their
  June 2023 letter" (L89; link L99). Says it could not comment "during the prior open period" (L38). One-year
  compliance period (L76). Quotes Commissioner Peirce (L110).
- D08 RER: real estate. fn 2 (L18): signed the joint trades letter of Sep. 12, 2023. Board roster L22-103 (Chair-Elect
  Kathleen McCarthy of Blackstone). Proposing Release at 135 on deeds (L114-122). Figures: 20 percent, 9 million,
  two-thirds.
- D09 MFA: asks withdrawal. Earlier letters May 8, July 24, September 12, 2023 (L14, L43-44). Section headings cite
  Proposing Release Questions 1 – 6 and 136 (L39), 98, 118, 186 (L58), 58, 79, 125 (L74). Apr. 25, 2022 letter on
  another file (L93). Figures: more than 170 members, nearly $2.2 trillion.
- D10 IAA: supplemental comments on the audit provision. Own May 8, 2023 "Initial Safeguarding Letter" (L16, L26);
  no other earlier letter mentioned. Summary of eight recommendations (L35-52). 30-day cure (L88); 120/180/260 days
  (L91-92); 10 percent de minimis (L104); non-control exception (L126); one and four business days (L148); Madison
  Capital no-action letter, 11 conditions (L164-165); exclude CFTC-regulated assets (L173).
- D11 AICPA: supplements its letter dated 8 May 2023 (L14). RFC #158, #159, #160, #161, #162, #166, #170. Second
  periodic examination; 23 months (L47, fn 15 L53); worked date examples fn 20 (L63); 5% schedule threshold (L72).
- D12 AGC: answers five staff requests after a meeting of August 29, 2023 (L9) and a call on November 9, 2023 (L19);
  earlier letter March 8, 2023 (L17). Twelve members incl. JP Morgan (L27). Two-of-three custody criteria (L62-68).
  Sub-custodian liability (L158-163). Annex on securities, cash, credit risk (L176-208).
- D13 Blockchain Association: cost-benefit analysis of digital assets. Earlier letters May 8, 2023 and October 27,
  2023 (L20, L24). Nearly 100 members. Custody rule of March 6, 1962 (L51).

## Shared ground (navigation only)

- Commenters appearing in another commenter's letter: IAA (D03 L207; D07 L89), FIA (D03 L117, L319), Blackstone (D08
  roster), JP Morgan (D12 L27). The joint trades letter of Sep. 12, 2023: cited in D01 L17, D08 L18, D09 L14 and L44.
- Third-party letters cited: AIC (D01, D07), SIFMA AMG (D06), LSTA (D03), Mercatus Center (D09 L61), KPMG, Ernst &
  Young, PwC, Deloitte, ABA et al. (D05).
- The September 2023 private fund adviser rules (88 Fed. Reg. 63206) under five names: D01 L122, D09 L32, D06 L87,
  D10 L24, D11 L26; mentioned in D07 L38.
- Same proposed provisions described in several letters: the exception for assets a custodian cannot hold (D01 fn 15,
  D05 L94-96, D08 L163-171, D10 L110-113, D11 fn 3); auditor notifications in one and four business days (D10 L148,
  D11 L77); sampling (D09 L92, D10 L110-121, D11 L35).
- CFTC rules for futures commission merchants: D04 FAQ and body, D03 Appendix B and L109, D10 L173.
- Numbered questions of the proposing release: D09, D05, D03 L63, D11.
- Conflicting dates for one release: 68 Fed. Reg. 56,692 is "Sept. 25, 2003" in D01 L113 and "Oct. 1, 2003" in D04 L35.
