# Platform guide, sections 4-7 (last updated Oct 15-16, 2026)

Source: pasted by the user on 2026-10-17 ("We now get stuck to hard questions. The following is the updated
guide"), verbatim below the line. It is newer than `instruction.md` (sections 1-4 of an earlier guide) and
than the 2026-10-04 and 2026-10-15 summaries in `../docket-platform-guide-newer-than-instruction.md`; where
they differ, this text governs. Design use of it is in `hard-playbook.md`; do not edit the text below.

---

4. Task shapes

Copy link
Last updated Oct 15, 2026

Strong questions ask about what happens in the documents, not about the documents themselves (who cites whom, which authors or journals appear). Aim for a single, exact answer: a number, a name, a date or a short value. Use a list only when the list itself is the point.

1. Use a clue to identify the right period or case, then work out the answer
The solver first works out which period, entity or case the question means, then uses evidence elsewhere to calculate or find the answer.

Example: "For the year identified by this operational milestone, what was second-half revenue, using the annual and first-half figures?"
Why it's hard: the solver must find the right year, pick compatible figures and tell cumulative amounts from single quarters. The wrong period still gives a plausible answer.
Works with: annual and interim reports, operating updates, dated case histories.
2. Compare original and revised figures, then use the right one
The solver must tell an original figure from a later revision, decide which version applies, and use it.

Example: "Using the most recently published figures, how much did the segment's operating margin change between the two years?"
Why it's hard: both figures look authoritative. The one a solver finds first is often the outdated one.
Works with: restated financial reports, revised statistics, amended policies, proposed vs final rules.
3. Find the qualifying items, then calculate and compare
The solver builds the qualifying set, calculates a comparable result for each, then selects or compares.

Example: "Among entities that qualified in one year but not the next, which had the largest later allocation, and by how much had it grown?"
Why it's hard: the filter, ranking and calculation must happen in the right order. Ranking everyone first picks an ineligible answer.
Works with: grant tables, company segments, settlements, program registers, annual performance records.
4. Select the right case, then apply the rules
The solver combines rules from the documents with facts about one case, including any condition or exception that changes the outcome.

Example: "For the smallest qualifying recipient, assuming it uses the maximum permitted reservation, what minimum amount must it distribute?"
Why it's hard: finding the rule is only one step. The solver must confirm it applies, combine the limits and apply them to the correct case.
Works with: funding rules and allocation tables, fee schedules, eligibility policies and case records.
5. Compare earlier and later events, then find the qualifying case
The solver follows what happened across documents and identifies the case that meets a combination of events or changes.

Example: "Which organization introduced an exception only in its later submission, having submitted both before and after the hearing?"
Why it's hard: the solver must keep earlier and later positions apart and keep track of who did what.
Works with: consultation submissions, successive policy updates, litigation histories, quarterly reports.
6. Count the items that pass a judgement call
The solver reads each item, decides whether it really meets the test, then counts.

Example: "How many commenters explicitly support draft recommendation 4, counting only letters that state that support in their own words?"
Why it's hard: plain counts are easy. Models slip when the call is subtle: support that is hedged, support buried in a bundled point, or a letter that only quotes another letter's view.
Works with: comment letters on proposed rules, consultation responses, survey submissions.
Pick your target before you write
Choose your shape and your trap before you write the question, and know your decoy.

Shape is one of the six above.
Trap is a lever from the table under How to make a question harder in section 5. Two traps beat one: one usually lands Easy, two together land Medium or Hard (see Where solvers fail in section 5).
Decoy is the plausible wrong answer a quick reader would give. If you can't name one, the question is probably too easy.
When the task form asks which failure modes your task targets, pick the matching ones. You no longer need a target line at the top of your reasoning.
5. Hitting your difficulty

Copy link
Last updated Oct 16, 2026

What Hard means
A question is Hard when each of the two Hard solvers gets it wrong at least once in its three runs. For example, 2 of 3 right plus 2 of 3 right counts as Hard; 3 of 3 plus 1 of 3 does not, because one solver never missed. That's the whole definition. Everything below is about how to get there.

One lever is rarely enough. The difficulty check uses a panel of strong models, and they do act on clauses like "to the nearest basis point" or "exactly". On their own, those usually land Medium. Questions that land Hard stack two or more levers, so the answer needs several documents to line up: for example, a quarter no release reports plus a definition that changed, or a restated figure plus a precision the release doesn't print.

New Hard shapes that can help
Four shapes that keep landing Hard in our recent work. Each still needs one short answer and two documents that have to line up.

A. Rebuild a figure no document prints. The number you need isn't printed anywhere. It has to be backed out from a revision note, or built from its parts.

Example: a September report says one State's yield was cut and another's raised, with every other State unchanged from August. The August report isn't in the bundle. Ask for the change from the first forecast to the last.
Why it works: solvers grab the nearest printed figure, which here is already a revision.
B. Compute, then let a rule change the result. A waiver, minimum, cap or threshold changes the number once it's worked out.

Example: two agencies' fee proposals, each with a per-page rate and free pages. One also waives any fee of $25 or less. Ask for the total a reporter pays both.
Why it works: solvers do the arithmetic and stop. The rule that flips the answer sits in a different paragraph or document.
C. Each part's latest figure is in a different document. Ask for "the latest estimate for each," across several editions of a report series.

Example: add up three crops for one country using the latest estimate for each. The newest report dropped one crop from its table, so that crop's latest figure is in an older report.
Why it works: solvers take one edition and use it for everything.
D. Map the period first. Fiscal vs calendar year, marketing years, Southern Hemisphere seasons, or which quarter a date falls in.

Example: "calendar 2024" for an Argentine harvest is the 2023/24 column, not the 2024/25 one. Only a table note says so.
Why it works: the column that looks right is the wrong one.
Where solvers fail
Tips from Tadael, one of our Special Squad top producers. Thanks, Tadael!

Solvers read every page, footnote and table, so hiding a fact the documents state plainly doesn't work. Look for something the documents never say directly. Solvers reliably miss these:

They trust a document's own numbers and summaries. A report says "8 people," but a footnote elsewhere adds a ninth.
They don't compare documents unless they have to. One changed word in a re-quoted passage, or a figure that quietly changes from one report to the next, slips by.
They stop at the first match. Make the second mention look different: other wording, another label, a different section. "Revenue declined" in one report, "sales came in below the prior year" in another.
They can't search for what isn't there. A summary or conclusion mentions something the main text never discusses. There's no word to search for, so they'd have to read it all.
They lose track of short references: "Id.", "the same case", "the Company", abbreviations.
They use every clue you give. Leave out extra filters that would rule out your decoy.
One weakness usually lands Easy. Two together land Medium or Hard.

How to find them: compare every quote of the same passage across documents, every spelling of each name, each figure against its earlier versions, and each summary against the rest of the document. The quieter and rarer the slip, the harder the question.

Rules that still apply:

Use the slip to hide the answer, but ask for a real fact (a date, an amount, a count, a name), never which document has the slip (ground rule 10).
Ask for one value that needs both documents, and check that no wrong pair of documents gives the same answer.
Give no hints: don't say where to look, don't copy the documents' wording, and skip words like "actually" or "originally."
Still pin down the period, terms and basis. If a stated figure disagrees with the document's own table, say which basis you want ("calculated from the reported quarterly figures"). Otherwise it's send-back reason 1.
Coming back too hard? Hint at what to look for, never where.
My difficulty check timed out, or I'm getting Low 0/5 · Medium 0/5 · High 2/3. What do I do?

Open every model attempt and check whether the model's reasoning is really wrong.
If its reasoning is defensible (for example, a different but valid approach, or an answer off by a rounding step), the problem is the question or the gold answer. Tighten it.
If the model is clearly wrong, or a run failed because of the platform, post the task ID in the channel and an admin can help.
My questions keep coming back too easy.

Start with the Hard shapes and the worked examples above.
Use test ideas at the top of the task page to try several questions without using runs.
Ask the Question Coach why a run came back too easy.
Difficulty belongs in the documents, not in the question. If you add a rule about what to count or leave out, applying it should take looking, not judgment. A reader should never have to decide what your rule means.

Bad: "...consider only analyses where the court expressly assumes a substantive claim element... Exclude procedural assumptions, general acceptance of pleaded facts, and issues left undecided." Every term needs a ruling before you start. Two careful readers can reach different answers.
Good: worked example 1 below. Nothing to interpret; it's hard because the obvious figure was later restated.
My legal questions keep coming back too easy. Models read court opinions well, so a filter with clear criteria ("which rulings granted X") is usually solved. Add a step that needs a second document: a date or amount from another filing, or a later ruling that changed the outcome.

My task shows "In progress" and I can't edit it. Bundles you haven't acted on for 48+ hours can be released so someone else can use them. Submit the same day you start when you can.

Worked Hard examples
Only about 1 in 13 accepted questions lands Hard. The ones that do rarely use exotic tricks. In each one, the obvious passage gives a plausible but wrong answer, and the right answer needs a second document or a closer reading. Lever names match the table under How to make a question harder.

1. The figure was restated (Same series, right edition · Temporal alignment)
Bundle: Harlow Freight's quarterly earnings releases for Q3 2025 through Q3 2026. Early in 2026 the company sold its ferry division and began reporting it as discontinued operations.

Question: "On the basis used in Harlow Freight's most recent earnings release, what was its adjusted EBITDA for Q3 2025?" The Q3 2025 release still shows the old figure, with the ferry business included. The right figure appears only in the prior-year column of the latest release (Q3 2026), restated without the ferries.
Why it works: the obvious number really is in the bundle, but it is the wrong one. The reader has to find the latest release and notice that the basis changed.
2. The rule was amended (Scatter the pieces · Temporal alignment)
Bundle: several appellate opinions applying the same statute. The statute was amended partway through the period, and the filing deadline changed.

Question: "What filing deadline applied to the appeal decided last in these opinions?" Most of the opinions quote the old deadline. Only a footnote in a later opinion gives the amendment and its effective date, and the reader has to check the filing date of the last appeal against it.
Why it works: the deadline quoted most often is the wrong one. The answer is a single number of days, and it's a fact about the law, not about the documents.
3. The same judge in two cases, plus one calculation (Who belongs where · Calculate across documents)
Bundle: district-court rulings in several suits against the Northgate Water Authority, plus the Authority's own notices.

Question: "One judge ruled in two of these suits against the Authority, the same way both times. How many days after the Authority's notice of intent was that judge's earlier ruling issued?"
Why it works: the reader first has to work out which judge appears in both suits and which way each ruling went. Then they take one date from a ruling and the other from a notice, and count the days. The answer is one number.
What the Hard versions have in common
Two documents are needed, and the obvious one gives the wrong answer. Tie the question to a basis, edition, role or date that only the second document settles.
The answer stays short: one figure, one name or one date gap. Difficulty comes from finding the answer, not from a long list.
Exact wording beats paraphrase: restated tables, unmarked edits in quotations, and dates in captions versus dates in notices.
If a run comes back Easy, change where the answer lives, not how many rules the question has. Two clear conditions are enough.
Keep it Hard, not ambiguous
Most recent send-backs on Hard attempts weren't too easy. They were ambiguous. Before you submit:

Define every judgement word ("flatly rejected", "supports", "concerned about") with a test a reader can apply.
Name the source when two passages give different figures (the MD&A sentence or the Note 3 table).
Add a tie-break if two items could qualify.
Ask for a fact, not a typo. Never ask which document contains a mistake.
More traps to add
Start from a shape in Task shapes above, then use one of these moves to hide a decoy: an item that looks right on a quick read but isn't. Name the decoy in your reasoning and say why it's out. The answer should be one value, such as an amount, a name or a date gap.

Restated figures. When a later release restates earlier periods, only the figure on the basis the question names counts.

Easy: "What operating income did the company report for Q3 2025?"
Harder: "On the basis used in the company's latest earnings release, what was its operating income for Q3 2025?" (Decoy: the figure printed in the Q3 2025 release itself, before a division that was later sold was taken out.)
Mentions it vs does it. Only items that actually do the thing count, not ones that just mention the topic.

Easy: "Which press release announces a share buyback?"
Harder: "What did the company spend in total on buybacks it completed during the year?" (Decoy: a program that was authorized but never carried out.)
Does the hedge apply? A "may" or "likely" only matters if it qualifies the claim itself, not a side clause.

Easy: "What does the report say caused the drop in enrollment?"
Harder: "By how many points does the report say its one confirmed cause reduced enrollment?" (Decoy: a cause with a bigger number, stated as only "likely".)
Look-alike metric. We have plenty of date traps; try this one. The right figure sits next to a similar one: a subtotal vs the total line, adjusted vs reported, "operating income" vs "income from operations".

Easy: "What was the company's revenue in 2024?"
Harder: "What was the company's operating income for Q2 2025, excluding only the litigation charge?" (Decoy: the "adjusted operating income" line, which also strips out restructuring costs.)
Still coming back Low? Use the full lever table under How to make a question harder below, press Harder variants, or come to office hours.

How to make a question harder
These patterns most often trip up strong AI models while staying fair to a careful human reader. The two marked "most effective" beat strong models most often in our testing. Use one or two per question, not all of them.

Every "which items…" question needs a decoy. At least one item in the bundle should look like it qualifies on a quick read but fail the real test. Name the decoy in the reasoning field and say why it's out. Without a decoy, the hedge, exclude and mentions-vs-does levers test nothing.

Lever	How to use it
Restated figures (most effective)	Use a bundle where a later release restates earlier periods (a business sold, a new segment, a correction). Ask for an earlier period's figure on the basis a named later release uses. Models reach for the figure as first reported almost every time. Name the release so only one document fits (send-back reason 8).
Ask for a precision the document doesn't print	The release gives a rounded headline (growth to the nearest percent, a margin to one decimal, a buyback to the nearest $0.1 billion). Ask for the same figure more precisely ("to the nearest basis point", "to one decimal place", "to the nearest million"), so it has to be computed from the raw lines. Say "do not round intermediate values", and check your gold isn't one rounding step away from a different answer. Example: the release says revenue grew 23%; ask for growth to one decimal place, computed from the two revenue figures. Most solvers return the headline.
Ask about a period no document reports on its own	Bundle a full-year release with the quarterly ones and ask for a quarter that has to be backed out (Q4 = full year minus the first nine months; Q2 = six months minus Q1), or ask "across every quarter, including any not reported on its own". If a window includes the earliest quarter, say whether it is compared with the quarter before it. Example: "In which 2025 quarter did the company take the fewest orders?", where Q3 only exists as the full year minus the other three. Solvers skip the quarter they'd have to derive.
Like for like across a definition change	Bundle releases from before and after a change in how a line is defined (a wider same-store pool, a new pricing basis, a metric that starts leaving an item out, a segment carve-out), where the later release restates the earlier period on the new basis. Ask for the change "on the same basis as the [named] release" or "like for like". Both figures in your gold must come from the same basis, and the bundle must actually contain the restated earlier period. Example: a REIT widens its same-store pool and restates last year's quarter on the new pool; ask for the year-over-year change on the new pool. Solvers mix the two pools.
Mentions it vs does it (most effective)	Ask for items that actually do something (blame an event on a cause, apply a legal test, promise a benefit) when other items in the bundle only mention the same topic.
Scatter the pieces	Put the parts of the answer in different documents, so no single passage has it.
Same series, right edition	Ask about one edition when the bundle holds several from the same series.
Who belongs where	Ask which person, organization, figure or citation appears in which document, when similar ones cross documents. A table that repeats across two years' editions works especially well, and so does asking which organization wrote or submitted a document rather than one it names.
Exact table vs rounded prose	Make the answer depend on the exact figure in a table, not the rounded number in the text. Check it: redo the answer with the rounded figure, and if you get the same answer, the lever isn't doing anything.
Does the hedge apply?	Ask which findings or claims are stated with uncertainty, where some "may" or "likely" words sit in a side clause and don't qualify the claim itself.
Match, then exclude	Ask for items that meet one condition, minus those that also meet a second one stated elsewhere. In our latest testing, a clause that rules out the headline figure ("merely accepting a voluntary start does not count", "private stakes included", "the half that last ended before the announcement") was the second most effective move, behind restated figures. Put the clause in the question, not the explanation.
Ordered answers	Ask for a ranking or a sequence rather than a single item, so every position has to be right.
Calculate across documents	Combine figures from two or more documents. One lookup plus one operation is usually solved; three or more dependent steps (find the period from a clue, pull figures from different releases, then compute) usually aren't.
State the rounding	Ask for a figure to a stated precision, where rounding too early changes the result.
Summary vs detail	Make the answer depend on a detail that corrects the document's own headline or summary: a footnote that adds a ninth person to "8 people," or a stated percentage that its own table doesn't support. Say which basis you want, so the key still matches a stated figure.
Quiet edit in a re-quoted passage	The same passage is quoted in two documents and one word or figure differs. Ask for the fact that depends on the changed word, not for which document changed it.
Second mention, different words	Solvers stop at the first match. Make the mention that matters use other wording, another label or a different section ("sales came in below the prior year" vs "revenue declined").
Claimed but never discussed	A summary or conclusion cites something the main text never covers, such as a ruling that dismisses a claim its analysis never addresses. There's no word to search for.
Short references	The answer depends on resolving "Id.", "the same case", "the Company" or an abbreviation back to the right party.
Footnotes and prose can change how a table is read. A marketing-year footnote that shifts which row is which year, a State total that appears only in the text, or columns that are cumulative rather than annual. Questions that depend on one are reliably missed, but your explanation must cite the footnote or sentence.

Combine two. One lever usually lands Easy; two together land Medium or Hard. Solvers also use every clue you give, so don't add filters that would rule out your decoy.

Four levers, worked through
Mentions it vs does it.

Weak: "Which findings mention training?" A keyword search answers it.
Strong: "Which findings blame the event on a gap in training or policy, rather than on the crew's own actions?" A finding that says training "would benefit" controllers in future mentions training but doesn't blame the event on it, so it doesn't count. That finding is the decoy.
Does the hedge apply? Read what the uncertain word is attached to. In "Rules would give inspectors a standard for risk areas that may influence loading," the claim ("would give") is stated firmly. The "may" only describes the risk areas, so the claim is not hedged.

Who belongs where: who wrote it. Documents often name other organizations in their text, such as a submission that quotes its partner groups or co-signers. Ask for the organization that wrote or submitted the document, not one it mentions.

Weak: "Which organization's comments focus most on hardship?" It's a judgment call, and a reader can argue for any group named in the text.
Strong: "Which submitting organization proposed a hardship cap, not counting groups it quotes or lists as partners?"
Exact table vs rounded prose: check that rounding changes the answer. Before you submit, redo the answer using the rounded figure from the text. If you get the same answer, the lever isn't doing anything. For example, the text says margins "grew about 15% and 6%" (a difference of 9), while the tables give 14.6% and 6.4% (a difference of 8). The answer must be 8. If both routes gave 9, the question tests nothing.

Reasoning tags
Every question carries at least two of these tags, picked on the task form. Tag the reasoning a reader actually has to do to reach the answer.

Tag	What it means
Cross-document join	The answer combines facts from two or more documents.
Temporal alignment	Matching each fact to the right time period.
Unit normalization	Numbers must be converted or put on the same scale before they can be combined.
Conditional filter	Keeping only items that meet a condition, or excluding some.
Entity resolution	Recognizing the same person or organization under different names, or telling apart similar ones.
Aggregation	Counting, summing, averaging or ranking across several items.
Common mistakes when making a question harder
These make models fail for the wrong reason, and a reviewer will usually reject the question.

Undefined terms. For example, asking for "capacity added" without saying whether a site that just opened counts.
Answers no document states. For example, a date the documents only hint at ("within the next 12 months"), or a figure that exists only by multiplying numbers the documents never connect.
Judgment calls. "Most strongly aligned," "most relevant," or "best." Two careful readers will disagree.
Unsigned superlatives. "Largest change" can mean the biggest number or the biggest move in one direction. Write "largest in absolute size" or "largest increase."
Strength scales without edge rules. If readers grade how firmly something is stated, say where the in-between cases land, such as "contributed to" or a claim that is stated and then hedged.
Format traps. Wording like "give count" that could mean one total or a count for each item. Say exactly which fields you want.
Rulebooks. See the requirements above.
AI use and the Question Coach
The questions must be yours. Their value is that they come from a human expert reading the documents, and AI-written questions are easy for our checks to spot.

Not allowed: asking any AI tool to write questions or answers for you, or pasting bundle text into an outside AI tool. A question generated this way is rejected, and repeat cases end your access.
Allowed, inside the platform: the Question Coach. It can explain the ground rules and tell you whether a draft question looks ambiguous or too shallow, and why. Its “Get a second opinion” button has three models check your saved draft against the rules. It won't reword, write questions or find answers for you.
Activity on the platform, including Question Coach chats, may be reviewed.
6. Accepted examples

Copy link
Last updated Oct 15, 2026

Question bank: Hard only. Every question here measured Hard on the platform's difficulty check and passed review. Corporate filings come first, because that's the shape we need most. Copy the move, not the topic, and never reuse a bank question on the same bundle.

What these have in common: each one stacks at least two levers, and the answer needs two or more documents to line up (a derived period plus a definition change, or a restated figure plus a precision the release doesn't print). On the current check, a single lever on its own usually lands Medium.

Hard · Corporate filings: the quarter no release reports, on a definition that later changed
Docs: PBF Energy's quarterly earnings releases for 2025 and 2026. Question: For PBF Energy's 2025 quarter with the highest gross refining margin per barrel of throughput (as reported, before excluding special items), what was PBF's Adjusted EBITDA, in $ millions, using the Adjusted EBITDA definition in its full-year 2025 earnings release? One decimal. Answer: 144.4 Why it's good:

Three levers stacked. Q3 2025 isn't reported on its own: its margin per barrel has to be derived as full year minus H1 minus Q4 ((2,347.5 − 1,031.8 − 594.6) / (304.0 − 142.1 − 81.8) = 9.00), and it beats the reported quarters (Q2 8.38, Q4 7.26).
The 2026 release restated H1 2025 Adjusted EBITDA (−172.7) on a new definition that adds back 24.3. Back on the full-year 2025 definition: 205.5 − 258.1 + 172.7 + 24.3 = 144.4.
Decoys: the "excluding special items" margin points to Q4, and using the restated H1 figure as printed gives the wrong total. The selector is part of the analysis (the company's own best quarter), not an unrelated fact.
Hard · Corporate filings: back out a quarter no release reports on its own
Docs: 3M's quarterly earnings releases for 2025 and 2026. Question: How much did 3M pay out to shareholders through dividends and share buybacks combined in the second quarter of 2026? Give the answer to the nearest million dollars. Answer: $1,395 million Why it's good:

The Q2 release's cash-flow statement shows only the six months (3,806), so the quarter has to be backed out with the Q1 release (2,411): 3,806 − 2,411 = 1,395.
Decoys: the highlights' "$1.4 billion" is rounded to a tenth of a billion; last year's six-month figure (3,013) sits right next to this year's.
Hard · Corporate filings: a quarter no release reports, plus a clause that rules out the obvious line
Docs: Annual and quarterly releases from Booking Holdings and peers. Question: In the October to December 2025 quarter, what net gain or loss did Booking Holdings record on all its equity securities, private stakes included? Work it out as the full year less the first nine months. Answer: Net loss of $69 million Why it's good:

Two levers stacked: the quarter has to be derived (full year less nine months, stated in the question), and "private stakes included" rules out the non-GAAP adjustment line, which a footnote says covers only securities with readily determinable fair values.
Decoy: that adjustment line gives a loss of $79 million.
Hard · Industry research: a footnote decides which column is which year
Docs: USDA Foreign Agricultural Service citrus circulars with country production, trade and consumption tables. Question: Take USDA's latest estimate of the fresh oranges Australia consumed at home in its orange marketing year that ended in March 2024, and subtract USDA's first forecast for that same year. The tables give Australia no consumption row, so count it as Australia's crop plus imports, less oranges for processing and exports. Answer in thousand metric tons. Answer: 32 thousand metric tons Why it's good:

The table footnote says Australia's April–March marketing year begins in the second year shown, so the year ending March 2024 is the "2022/23" column, not "2023/24".
The question gives the formula and the calendar anchor, so the only trap is the footnote. Decoy: reading the column label literally gives −10.
Hard · Industry research: filter the outages, then compare two periods (shape 3)
Docs: Ember electricity reviews and heatwave analyses, including a 2025 heatwave impact study and a later report on how Europe's grid handled extreme heat. Question: Using the reported GW figures, what was the percentage-point change in the minimum share of unavailable French nuclear capacity marked forced (or environmental in 2026), from 1–2 July 2025 to 12 July 2026? Give a signed answer to two decimals. Answer: +7.50 percentage points Why it's good:

Needs two documents: the 2025 study gives 7 GW forced out of 23 GW of reductions on 1–2 July, and the later report gives at least 11 GW forced or environmental out of 29 GW unavailable on 12 July 2026.
Decoy: the later report also says the heatwave hit up to 18% of France's nuclear capacity, against 15% in 2025. Those are shares of total installed capacity, not of unavailable capacity, so 3 points is wrong. The 2–3 GW of "Planned" heatwave-period reductions and the 30 GW summer-2025 maximum are further traps.
One exact answer: 11/29 − 7/23 = 37.93% − 30.43% = +7.50 points, and "minimum" matches the reports' "at least" wording.
Hard · Law and contracts: spot the conflict, then do the date math
Docs: court rulings in Brooks v. Trans Union. Question: Two court rulings in Brooks v. Trans Union each give a date from the case in two conflicting versions within that same ruling. How many days after the earlier one was filed was the later one filed? Answer with a number. Answer: 706 Why it's good:

The reader has to check every ruling for a date stated two different ways. One says "30th day of July 2021" in its text but was filed July 30, 2024; another gives the same hearing as June 25 and June 24, 2026.
The other rulings give each date only one way, so exactly two rulings qualify.
Decoys: using the wrong 2021 date, or measuring inside one ruling, gives a different number. The answer is a single number.
Hard · Public policy: a dollar figure each submitter names, plus one defined second test
Docs: Submissions to an Australian Treasury consultation on multinational tax integrity, including the proposed fixed ratio (interest-limitation) rule. Question: Which submissions identify a dollar level for the de minimis threshold intended to exclude low-risk entities from the proposed fixed ratio rule, and what level does each provide? Put an asterisk after those who also want denied interest deductions to be able to be carried back to earlier years. Answer alphabetically as Name (level). Answer: Ashurst ($10 million), BDO ($10 million), CPA Australia ($5 million), Deloitte ($2 million) Why it's good:

The membership test is a concrete fact (a stated dollar level), not a judgement call, and the second test (a carry-back) is a clear yes or no.
Decoys: the EU directive's threshold in a CPA Australia footnote, the current rule quoted by another submitter who wants it raised but gives no figure, and a submitter that gives no figure at all. One of the figures sits after a page break that splits the term.
Hard · Public policy: a fixed-size list with the boundary defined in the question
Docs: Submissions on the New Zealand Commerce Commission's draft report on its telecommunications dispute resolution scheme. Question: Which six submissions to the draft report want the December 2021 deadline for extending the scheme to include complaints about equipment, coverage and broadband speeds pushed back? Endorsing another submission counts as sharing its views. List them alphabetically in one comma-separated list, marking those that would settle governance and the terms of reference before revising the complaints code. Answer: 2degrees (governance first), Chorus (governance first), New Zealand Telecommunications Forum (governance first), Spark, Vodafone Aotearoa, WISPA New Zealand Why it's good:

"Endorsing another submission counts" settles the most common boundary dispute in submitter questions before it starts, and "which six" fixes the size of the answer.
The marker is a step on the same thread (what each one wants done first), not an unrelated second question.
Example questions
The two worked examples come from real bundles, with answers checked against the documents. The short tables after them are invented illustrations. Match the shape, not the topic.

Worked example 1. Company documents: eleven Netflix earnings releases
Question: For each quarter, from Q1 '25 through Q2 '26, compare Netflix's actual revenue with the revenue forecast for that quarter. List every quarter in which actual revenue was lower than the forecast.

Answer: Q3 '25 and Q2 '26.

Why it works: each quarter's forecast is in one release and the actual figure is in the next one, so the reader pairs up six quarters across documents. The releases call both misses "in line," so reading the prose alone gives the wrong answer. The answer is an ordered list.

Worked example 2. Government consultations: seven Federal Register rules
Question: Treasury and the IRS proposed, then finalized, a change to how a "coverage month" is defined for the premium tax credit. How many days after the deadline for public comments on the proposal did the final regulations take effect, and how many of the public comments opposed the proposed rules?

Answer: 47 days, none (all nine comments supported the rules)

Why it works: the comment deadline (November 1, 2024) is only in the proposed rule. The effective date (December 18, 2024) and the comment count are only in the final rule. The reader has to find the right two documents among seven unrelated rules, then do a date calculation. It uses two parallel asks, which is the limit.

Good questions
Bundle type	Question	Answer	Why it works
Company annual reports (3 firms)	Of the three companies, which one grew operating profit fastest between its two most recent fiscal years, and by what percentage?	Harlow Freight, 18.4%	Needs the right figure from each of three reports, a calculation, then a comparison.
Legal documents (contract + two amendments)	After both amendments, what is the notice period, in days, for terminating the supply agreement without cause?	60 days	The original term was changed twice; the reader must apply the amendments in order.
Industry reports (two market studies)	The two reports disagree on market size for one year they both cover. Which year, and what is the gap between their estimates?	2024, $1.2 billion	The reader must find the overlap and notice the conflict, not just look up a number.
Weak questions, and how to fix them
Weak question	Problem	Stronger version
What was Harlow Freight's revenue in 2025?	One lookup in one place (rule 2).	Which of the three companies had the highest revenue per employee in 2025?
Summarize the main concerns raised in the consultation.	Answer is an essay, not checkable (rule 5).	Which concern was raised by the most respondents, and how many raised it?
Is the company likely to hit its 2030 emissions target?	Opinion; more than one defensible answer (rule 4).	If emissions keep falling by the same amount each year as between the last two reported years, in what year would the company first meet its 2030 target?
Example moves for each lever
Lever	Example move
Restated figures	Ask for Q3 2025 on the basis of the latest release, after a division was sold in 2026.
Scatter the pieces	The comment deadline is in the proposed rule; the effective date is in the final rule.
Same series, right edition	Use the March report, when January, March and April are all in the bundle.
Who belongs where	"Which analysts were on both calls?" when two different Lees appear.
Exact table vs rounded prose	The summary says "up 15%" for both quarters; the table shows which quarter grew more.
Does the hedge apply?	"Which numbered findings are stated as uncertain?" One finding says new rules "would provide inspectors with a regulatory standard" and mentions risks "that may influence improper loading" only as a side detail. The "may" is there, but the finding isn't hedged.
Match, then exclude	"Which documents cite a legal section the reference document also cites, and are not co-issued by any of its co-issuers?" Answer: 1. Skipping the exclusion gives 5. Keep it to two plain conditions; five is a rulebook.
Ordered answers	Rank four countries by share of workers covered, lowest first.
Calculate across documents	Days between the comment deadline and the effective date.
State the rounding	"To one decimal place" on a growth rate computed from raw totals.
An example of each reasoning tag
Tag	Example
Cross-document join	Deadline from the proposed rule + effective date from the final rule.
Temporal alignment	FY2024 column vs FY2025; fiscal vs calendar year; the right report edition.
Unit normalization	Turning a dollar amount and a percentage share into a total; millions vs billions.
Conditional filter	Rulings that granted suppression; documents not co-issued by another agency.
Entity resolution	"SBA" vs "Small Business Administration"; two different analysts named Lee.
Aggregation	How many rulings granted; rank four states by share.
7. Common send-back reasons

Copy link
Last updated Oct 15, 2026

The five pitfalls reviewers see most
1. Contrived selectors (the most common problem). The question picks its quarter, company or item through an unrelated fact, just to make the solver open a second document: "liabilities in the first quarter in which revenue topped $11.5B", or "Company A's metric in the quarter Company B grew faster". No analyst asks this way. The hop adds lookup work, not reasoning, and the selector is often the part that breaks (rounding ties, partial-year coverage). Fix: name the period or company directly, and get the multi-document reasoning from the question itself: compare two companies, or combine figures that belong together. A selector is fine when it is the analysis: "In the quarter its gross margin was lowest, what was its operating margin?"

2. Two questions in one. Two unrelated asks joined into one task, such as "which groups want X, and which of them drops a word mid-quote". Reviewers see two separate findings, and one wrong half sinks the whole task. Fix: keep one line of analysis. If the second part isn't a step toward the first, make it its own task or drop it. Don't build a ratio from figures that don't belong together, such as counts from one notice divided by States named in an unrelated notice.

3. Riddle chains. Clue hunts like "Four studies err: an abstract's count is one above the body's; a text and a table split one total… In that order, how many workers did each analyse?" These test puzzle-solving, not reading, and every clue adds another chance for a second valid reading. Fix: ask what a real analyst would want to know about these documents, then make it hard through the reasoning, not by hiding the target.

4. Conditions that need judgement. Wording where two careful readers could disagree on what counts: "brought back in the same or a narrower form", "wants it scrutinised", "spend on capital". When the documents report more than one candidate (capex with or without capitalised interest, for example), a solver who is right can land on a different answer and be marked wrong. Fix: define the term in the question ("capital expenditures including capitalised interest", "fiscal Q2 2025, ended June 30"), or pick a condition the documents decide on their own. If you need a paragraph to explain what qualifies, the condition is too loose.

5. Gold answers that punish a right answer.

Recomputing a figure the document already states: the document says 14%, but the gold uses 89/643 to require 11.8 instead of 12.0.
Adding words the question didn't ask for: "Increase of about 4.6%", "Woolworths New Zealand (WWNZ)", "(cover date)".
Spelling out the trap in the question ("not rounded percentages", "one of them isn't internally consistent"), which hands the solver the method.
Fix: if a document states the figure, the gold uses it, unless the question explicitly says to recompute. The gold is the bare value only, in exactly the format the question asks for: no "about", no "increase of", no labels in brackets. Let the solver find the trap on their own.

Other common send-back reasons
1. The gold is computed from rounded inputs, but the document states the figure. If a document says "approximately 4.3 percent," don't compute 4.2 from rounded dollar amounts. Use the stated figure, or say in the question to compute from the dollar figures.

2. A description fits more than one thing. "The marine mammal whose shutdown zones extend beyond its Level B zones" matched two species in the bundle. Search the bundle for everything your description matches, in the tables as well as the text, and check for ties. Narrow it until only one thing fits.

3. The question asks for two things, but the answer gives one. If the question asks for the quarter and the percentage, the answer must include both, in the order the question asks for them. If one part is only a step on the way, ask for the final value only.

4. The question is too long. Aim for 20–45 words. Over 60 gets a warning and over 80 can't be submitted. Cut setup, not substance.

5. The period or terms aren't pinned down. Say fiscal or calendar year (and the quarter-end if it isn't December), define comparison words (percentage points vs percent, absolute vs relative) and name the exact line item.

6. Thin reasoning or missing evidence. Your step-by-step reasoning should say which document gives which fact and how they combine. Every necessary document needs at least one quote.

7. A word that decides what counts isn't defined. If a word decides which items are in or out, or what you divide by, define it in the question. "Percentage of all funding" can mean base plus emergency funding or emergency funding only, and each gives a different answer.

8. Read literally, the question points at a different document or period than your answer uses. Words like "the most recent release," "the latest report" or "the quarter in which it was declared" must point at exactly the document and period your answer comes from. Before you submit, forget what you meant, read only the words, and work the answer out again. If you get a different answer, rewrite the question.
