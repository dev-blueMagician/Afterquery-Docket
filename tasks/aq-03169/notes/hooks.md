# aq-03169 - cross-document hooks

Target: Medium or Hard (user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we should target medium and
high"). No difficulty captures exist for these files or for any bundle sharing them. Family evidence used instead
(consultation-response bundles in `.claude/memory/docket-local-solver-calibration.md`): two lookups plus one operation, a
rate from one response applied to another's base, and list differences were all quick-test too easy; a hidden offset or an
unprinted figure was what caught the easier solver (aq-03120 q01, aq-02505 q01), and a gold lying between two plausible
wrong answers reached Medium once (aq-02673 q05).

## What the bundle offers

Ten parallel responses to one questionnaire. The only quantities that join across responses are the market share cap
proposals (Q19-Q23) and Deloitte's statistics. Positions on measures also join, but as respondent names or counts of
respondents, which rule 10 keeps out of answers.

Input hazard (decides precision everywhere): the present share of firms outside the Big Four is stated four ways. D02 L616
"currently perform 11 audits of the FTSE 350 today" (a count), D02 L254 "only 3%" (10.5), D02 L67 "98% ... audited by the four
largest" (7), D04 L181 "97% ... in 2016/17" (10.5). None is marked approximate, so a gold that changes with the choice has two
defensible answers (docket-one-clear-answer-precision). Every hook below is either free of that base or asked at a precision
where all four agree.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D06 L282 cap of 65 FTSE 350 companies per Big Four firm; D02 L616 11 audits today, about 60 tender wins in five years for a 20% share | Years of tender wins, at Deloitte's assumed yearly rate, to bring each Big Four firm within ICAEW's individual cap: (350 - 260 - 11) / 12 = 6.6, 7 years | Calculate across documents; State the rounding | Wrong routes: wins counted without the 11 already held, 90 / 12 = 7.5, 8 years; scaling five years by 90/70 = 6.4, 6 years; ICAEW's collective "around 60%" (D06 L408), 129 / 12 = 10.75, 11 years | D02's go-live lag of one to two years (L91) must stay out of the asked quantity: ask for years of wins. Base hazard: 6.58-6.70 on every stated base, all 7 | sketch i01, promote |
| h2 | D01 L145 no audit firm above 60 FTSE 350 clients by 2023; D02 L616 as h1, with 60 wins = 60% of FTSE 250 tenders | Share of the FTSE 250 tenders Deloitte expects that others must win for the Big Four to meet BDO's limit: 99 of about 100 | Calculate across documents; State the rounding | Scaling 60% by 110/70 = 94%, nearest ten 90%; without the 11 held, 110% | "about 60" makes the pipeline 98-105; 98-101% on every base, so only the nearest ten percent is safe. Shares h1's Deloitte paragraph: alternate, not a second question | sketch i02 |
| h3 | D04 L348 "c. 40-50 of the FTSE 350 firms" realistic in three to four years; D01 L145; D06 L282 | How many times Grant Thornton's realistic maximum others would have to audit under BDO's limit (110 / 50 = 2.2) and ICAEW's cap (90 / 50 = 1.8) | Scatter the pieces; Calculate across documents | Same-label decoy: D04 L40 "10-20% ... within three to four years" (70 companies: 1.6 and 1.3); D01 L221 80% and "say 50"; D06 L408 60% | Base-free. Each step is one plain sentence; three documents each give a number | sketch i03 |
| h4 | D08 L106 cap from 90% down 5% a year for 5 years, by number of companies (L99); D06 L282 | First annual cut at which Nexia's collective cap is tighter than the 74.3% that ICAEW's individual cap allows: the fourth (70%) | Calculate across documents; Unit normalization | Look-alike: ICAEW's 65 (companies per firm) beside Nexia's final 65% | "5% per annum" as points gives 85, 80, 75, 70, 65; as a rate 85.5, 81.2, 77.2, 73.3, 69.6: the fourth either way. Against BDO's 68.6% the two readings differ (fifth vs never), so BDO is not used. Small-integer answer | sketch i04 |
| h5 | D02 L234 74% of 213 tendering companies appointed a new firm, 2011-2017; D04 L155 "Only 8 of 29" changed auditor in the latest year | The two responses' switching rates differ by 74 - 27.6 = 46.4 points | Reconcile documents that disagree | D02 L274 "eight" of 244 tenders (won by BDO or Grant Thornton) is a look-alike 8 | Two lookups and one division: the family measured too easy | sketch i05, low priority |
| h6 | D04 L347 top 175 = 94% of FTSE fees; D07 L250 fee cap towards 70% | Fee share left outside the top 175 against Moore Stephens' fee cap: 24 points short | Unit or basis | - | "the FTSE" in D04 is not pinned to the FTSE 350; needs a what-if the documents do not make | not pursued |
| h7 | D05 L12, L23 "launched ... today" in a letter dated 30 October; D06 L6-7 launch on 9 October 2018 | Days from the study's launch to Hermes's letter: 21, against the letter's own "today" | Document convention | Lure: 0 days | The launch date is public and recallable, so D06 would fail the Document check; a plainly dated bridge measured too easy | not pursued |
| h8 | D04 Annex 1 L549-552 quotes Hermes's chief executive; D05 L19-21 AUM figures | Ratio of assets advised on to assets managed, 9.8 | Entity resolution | Federated's $392.2 billion | One named bridge plus one lookup: measured too easy family | not pursued |
| h9 | D02 L156, D04 L310-318 audit-related services each would still allow | Services allowed by one ban and not the other | Match, then exclude | Half-year review / interim review under two names | List difference over two short printed lists: measured too easy (aq-02102 q02); D02's "and similar services" leaves edge items open | not pursued |

## Closed for stated reasons

- Any exact count built on the present base (99 audits to shed under BDO's limit, 79 under ICAEW's, "tenfold"): the answer
  moves with the base figure chosen (99 / 99.5 / 103), and at a precision where the bases agree D04's 97% reproduces it
  without D02, so D02 would not be necessary.
- Respondent lists and counts (who supports a cap, who measures by fees): the answer would name or count the authors of the
  documents (rule 10).
- Tenure arithmetic on Grant Thornton's tendering proposal against the current twenty-year rule: the current rule is public
  regulation, recalled without D02.

## Measured on these files

- 2026-10-12, q01 rev 0 (h1), difficulty Run 1, Version 4e4850, raw verdicts/AQ-03169_difficulty_2026-10-12_1034.txt:
  "Answerable without the documents". The capture holds one attempt, the closed-book one (low model, no documents), read in
  full. It committed "7 years" as a guess from the rounding instruction ("maybe 7.2 rounds to 7"), then supplied figures to
  fit (8-10 wins a year, 50-65 audits to shift); it recalled neither the 65, the 60 wins nor the 11. Low, Medium and High
  with documents did not run, so h1's mechanism (the 11 audits already held, the yearly rate) is unmeasured.
  What made the hit cheap: the answer was a lone whole number of years under ten. Rev 1 keeps the mechanism and adds a
  first ask whose answer (260 audits) exists only through D06's 65.
- 2026-10-12, q01 (h1), form quick test, user chat only ("too easy for quick test"; wording not stated, rev 2 or rev 1):
  the easier solver reached the two-part gold. No trace, so no route is known. Reading for design: a five-step arithmetic
  chain across two responses, silent offset included, does not catch it. h1 and h2 closed; h3-h5 are plainer arithmetic
  and are not worth a test.

## Round 2 hooks (2026-10-12)

Source: two independent authors working from text/ only, then verified by the caller against D02 L391-436 and D04 L828-912.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h10 | D02 L391-436: 17 measures rated costs / benefits / implementation challenges, seven High/Low; D04 L828-912: costs and benefits per measure, independence listed for rows 1, 5, 11, 12, 13 and carried into row 3 by "All other benefits of 1 above" (L845) | The High-cost, Low-benefit measures (Deloitte) that carry an independence benefit (Grant Thornton): tendering and rotation reform, audit-only split, joint audits | Match, then exclude; Who belongs where | Break the link (independence, but Low cost); all-clients prohibition (High/Low, no independence); heading taken for the rating; cross-reference missed. Without the exclusion: seven | A carried-over member is the mechanism that held the easier solver on aq-02749; here it also risks the form's own solvers on the lean wording. Tendering's benefit is hedged ("Potentially"). Flattened tables | sketch i06, quick test first |
| h11 | D05 L67 "de facto being through prohibiting audit firms from providing consulting services to their audit clients"; D02 L397-398 "Non-audit services ban to audit clients", Medium High Low | Deloitte's ratings of what Hermes means by a de facto break-up | Who belongs where (one label, two meanings) | Rows 4.27, 4.8(b), 4.8(c): all High, Low, High | Bridge plus lookup; the definition sits beside the keyword | sketch i07 |
| h12 | D02 L404, L417-418 (merit group, High Low Medium); D06 L363 "for example Poland" | The merit-group measure rated High/Low and the country further along with it | Match, then exclude; Scatter the pieces | Joint audits / France | Group condition stated in the question; Poland may be recalled | sketch i08 |

Set aside by the authors, with reasons (spot-checked, not re-derived): permitted-service lists (list overlap; Deloitte's
"and similar services" leaves exclusions open); tender switch rates and non-audit fee ratios (one subtraction on unlike
bases); tendering and rotation rules (Grant Thornton gives 10 and up to 14 years; the current rule is duplicated and
public); "blind tender" and "shared audit" used in two senses (answers reduce to yes/no or are not settled by the text);
"proportionate" fines (firm size at D04 L265, audit fee at D06 L290: fair, but two explicit lookups); investor voting
figures (no common base); ICAEW and Deloitte paragraph labels (citation trivia); respondent-name answers of every kind.

- 2026-10-12, i06 (h10), form quick test, user chat only ("both of i06 survived, others not tested"): the easier solver
  missed the gold on the lean wording and on the explicit one. No trace, so which member it got wrong is not known.
  Promoted to q02 with the explicit wording.
- 2026-10-12, q02 rev 0 (h10), difficulty Run 2, Version 3beb81, raw verdicts/AQ-03169_difficulty_2026-10-12_1739.txt:
  "In band — Easy tier", Low 2/5. Routes (each wrong attempt read in full; see questions/q02.md Feedback log):
  - Low 2 and Low 3, right: found Annex 2 at the end of Doc 4, used it alone, followed "All other benefits of 1 above".
  - Low 1, 4, 5, wrong: decided Annex 2 was not in the text, used the reply, linked the audit-client ban to the
    all-clients prohibition (all three), and two read another respondent's Q27 answer as Grant Thornton's.
  - Every attempt read Deloitte's table correctly, headings and ratings alike. The strongest solver read the annex row by row.
  The recurring miss is locating the annex; it was cheap to avoid because an attempt that had the annex needed nothing
  else. Rev 1 makes the same hook need both places: h10b = concentration (annex rows 2 and 9 plus the reply's joint-audit
  sentence) and audit quality (two annex cost lines after page breaks).
- 2026-10-13, q02 rev 2 (h10b), difficulty Run 3, Version 2277b0, raw verdicts/AQ-03169_difficulty_2026-10-12_2314.txt:
  "Between levels", Low 0/5, Medium 4/5. Every wrong attempt and the three recorded right ones read in full
  (questions/q02.md Feedback log).
  - Low, 0 of 5: all listed Deloitte's seven High-cost, Low-benefit measures. Four never used Annex 2 and gave
    "joint audits" for concentration from the reply; one found the annex and gave its two rows without joint audits.
    Three took other respondents' sentences for Grant Thornton's; two carried the audit-client ban's remark to the
    all-clients ban.
  - Medium, 4 of 5: all visible attempts found the annex and also read the reply; the miss dropped the NAO-style
    auditor (reply paragraph used, continuation line after the page break not quoted).
  - Every visible medium attempt took Deloitte's set from the "Measures that we do not support" block and never listed
    tendering reform, rated High then Low under "appear to have merit". All ten low attempts of Runs 2 and 3 listed it.
    It cost nothing because tendering reform is in neither group. As a member it would be a row the medium model
    missed every time: an added trap, expected to separate medium from high outright (inference, unmeasured).
  Rev 3 removes the cue "anywhere in its response" and adds nothing.
- 2026-10-13, q02 rev 3 (h10b, no scope words), difficulty Run 4, Version 86b24a, raw
  verdicts/AQ-03169_difficulty_2026-10-13_0743.txt: "Answer not supported", Low 0/5, Medium 1/4, high model 0 of 3
  with every document (questions/q02.md Feedback log).
  - High, every document: all three answered from Annex 2. Two gave the annex's four members (break-up, all-clients
    ban; split, NAO-style auditor); one also dropped the break-up ("Immediate impact on market concentration" read
    as direction not stated). None credited joint audits; the reply's France sentences were not weighed.
  - Medium: read the reply first and found the joint-audit sentences in three of four attempts; failures were a
    truncated Deloitte set (four measures), a reply-only answer, and a partly read annex.
  - Low: four of five without the annex (joint audits; split), one annex-led (all-clients ban; NAO, split).
  Scope ladder on this hook: "say anywhere in its response" Between levels (Medium 4/5); no scope word not supported;
  "Grant Thornton's response" (rev 4) pending. The strong solver goes to the table and stays; the medium solver
  reads the prose and under-reads the table; the low solver rarely finds the table.
- 2026-10-13, q02 rev 4 (h10b, scope named: "Grant Thornton's response"), difficulty Run 5, Version 96eed6, raw
  verdicts/AQ-03169_difficulty_2026-10-13_1118.txt: "In band — Hard tier", Low 0/5, Medium 1/7, High 3/6;
  submitted by the user. Routes in notes/feedback-q02.md.
  - High, every document: both attempts now used "Annex 2 and main response" and weighed joint audits from the
    reply; one accepted the link, one called it "not explicit enough". Neither quoted the explicit sentence (L349).
  - Medium: one right; misses were the all-clients ban left out (two), joint audits left out (one, annex only), the
    all-clients ban added under quality (one). All recorded attempts listed six measures, without tendering reform.
  - Low: none used the annex rows.
  Scope ladder, same gold: "say anywhere in its response" Between levels; no scope word not supported; scope named
  Hard. What decided the tier was one term in the question, not the members.
