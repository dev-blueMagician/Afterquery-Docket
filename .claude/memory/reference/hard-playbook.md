# Hard playbook

Current design rulebook (adopted 2026-10-14, user-approved). Two pages at most. Only the batch review
edits it, every five platform results in [notes/hard-runs.md](../../../notes/hard-runs.md) (all bundles),
citing ledger rows. Older notes are history; this page wins where they differ. Batch reviews: 1 (2026-10-15,
rows 4, 13, 17, 21, 33); 2 (2026-10-15, row 32 with 21, 31, 33); 3 (user's request, 2026-10-17: rows 23,
25, 34 and the platform guide of 2026-10-15/16, saved verbatim in [platform-guide-2026-10-16.md](platform-guide-2026-10-16.md),
whose Hard bank is eight measured platform passes); 4 (2026-10-19: rows 71, 75, 83, 92, 95, 114).

## 1. Target, and what it takes

Hard (guide): "each of the two Hard solvers gets it wrong at least once in its three runs". Run page of
2026-10-18 (aq-06835, row 71): "Ready when both get it wrong at least once, even if every attempt is
wrong"; pages up to 2026-10-15 added "and not every attempt is wrong" (updated at the user's request,
2026-10-19). With a per-try success rate p for both, P(Hard) = (1-p^3)^2: 2% at p = 0.95, 24% at 0.8,
43% at 0.7, 77% at 0.5, 92% at 0.35. Each solver must miss at least once: a solver that never misses
scores 0 (rows 13, 34, 114: High 3/6; row 71: High 4/6; all Too easy). An all-miss passes only if the
gold is reachable: "In the final check, the high model was given every document and still did not reach
your answer" turned "Hard ✓ (both solvers missed at least once)" into "Answer not supported" (row 75,
High 0/6; the final check took the same first printings). A miss counts only where the model, given
every document, still reaches the gold (section 5).

Measured (ledger, 2026-10-19): 114 screened sentences, 342 of 342 local solves right (95% bound on the
miss rate: 0.9%); all fourteen screened runs, each local 3/3, not Hard at High: thirteen Too easy (rows
4, 17, 21, 23, 25, 32, 33, 34, 71, 83, 92, 95, 114), one Answer not supported (row 75). One deciding
step cannot reach the band, and three steps that each slip 2% give about 3%. Steps that each slip
15-30% of the time do: two give 39-78%, three 59-92%. So, as the guide says: "One lever is rarely
enough ... Questions that land Hard stack two or more levers, so the answer needs several documents to
line up."

## 2. What the High model clears (no single one of these makes a question Hard)

- **Finding or linking:** a member reached by a name, title, identifier or year; a buried aside worded
  like the question; a string join with spelling variants; a sweep for a property every document reports.
- **One rebuild:** level minus variance, FY minus nine months, a table sum, a date span, match then
  exclude across lists (rows 4, 17; quick tests rows 24, 35).
- **A rebuilt period as the selector, then a named basis:** rebuild every quarter (FY less H1 less Q4,
  six months less Q2), take the best or worst, answer on the basis the question names beside a look-alike
  (rows 71, 92, 95, 114; page notes: "Once Q3 is chosen, the answer follows from subtracting quoted
  headline figures", "per-quarter division and a minimum"). A rounded headline beside the exact figure
  was a check, not a lure (row 114: "letting the solver confirm the magnitude").
- **A deciding word where the question's words lead:** an exception in the rule's own sentence (row 31),
  an edit in the re-quoted passage the question asks about (row 32), a hedge another passage settles
  (row 33), a carve-out the scope phrase names (row 25), a value rebuilt from the lines the question's
  words name (row 83: "the question's wording ... pointed directly at those lines").
- **Signposts and cues:** a question naming its test ("first placed", "amounts"); cue clauses
  ("counting", "including", "anywhere"); decoys each ruled out by one sentence.

Each is a usable step inside a stack; none carries a Hard question alone.

## 3. Quiet levers (each has a platform Hard pass behind it)

In each pass the obvious passage gave a plausible wrong answer, and the step that avoided it sat on
the path to the answer, not in the ask's words (guide section 6; our three passes):

- A restated figure or changed definition, taken back to the named basis (PBF: H1 restated with a 24.3
  add-back). The guide's most effective lever: "Models reach for the figure as first reported." Row 75:
  all six High attempts took the first printings, and so did the final check (section 1).
- A clause that rules out the headline line, settled by a footnote on the line's scope (Booking:
  "private stakes included"; the second most effective move).
- A footnote deciding which column is which period (USDA marketing year), with first forecast against
  latest estimate across editions.
- One document stating a fact two ways (Brooks: two dates for one event).
- Ours: an exception in only one of two parallel rules (aq-02562); a second letter shown only as a
  quotation's source (aq-03170); a member stated only as a prose example beside its own table (aq-03169).
- Retired 2026-10-19 as quiet levers, kept as steps (section 2): a period no document reports, used to
  select and compute (PBF, 3M; Too easy in rows 71, 92, 95, 114), and a look-alike measure beside the
  right one (Ember; Too easy in rows 71, 83, 92, 95).

What solvers reliably miss (guide): a document's own numbers and summaries; differences between
documents they are not forced to compare; a second mention in other words; what is not there to search
for; short references ("Id.", "the Company"). And they use every clue the question gives.

## 4. Designing a Hard sketch

1. **Mine first.** `docket_agent.py mine tasks/<slug>` writes `notes/mine.md` (changed re-quotes, one
   rule in two documents' words, restatements, cumulative-only quarters, two names for one thing,
   rounded prose, table notes, stated counts). Read each candidate's passages in full.
2. **Pick a shape** (guide section 4, 1-6, or Hard shapes A-D) whose answer is one value an analyst
   would want, and **stack two or three levers** on its path, at least one quiet (section 3). Each lever
   has its own wrong answer (skip only that lever and recompute). The chain has three dependent steps:
   identify the period or case, take inputs on the right basis from different documents, compute or
   apply the rule. Name the decoy a quick reader gives.
3. **Ask downstream of the levers.** The question's rare words may lead to a lure, never to a settling
   passage (rows 2, 21, 25, 31-33). Pin the rest by structure: the period, the basis by a named document
   ("using the definition in its full-year 2025 release"), units, precision, and the formula for the
   non-trap parts (the bank's USDA and Booking questions state theirs). No hint words ("actually",
   "originally", "not rounded"), no cue clause, no filter that rules out the decoy. A selector must be
   the analysis (the company's own best quarter), never an unrelated hop (send-back pitfall 1).
4. **Fair means each settlement can be quoted.** A plain statement in the bundle, or a word of the
   question, rules each lure out. These made High miss only through unfairness, then went Easy once
   pinned: an unstated inclusion rule (aq-02673, aq-01937), a date no document prints (aq-02505 q01),
   an unnamed scope (aq-02933), "X states" fitting the wrong party (aq-02028). If the pinned version is
   a lookup, drop the hook.
5. **Write the stack** in the sketch's `## Lever stack` (template i00.md). `screen` checks two levers,
   their quotes, distinct wrong answers, three steps, a decoy and signposts.

## 5. Fairness checks before the screen

- **Readings.** For each phrase, name the other reading, its answer and the words that reject it; test
  each qualifier on each gold member. Read the question literally: "the latest release" must point at
  exactly the gold's document (send-back reason 8); "On the basis used in Albemarle's Q3 2025 earnings
  release" read as that release's definition, not its revised figures (row 75: Answer not supported).
  Define every word that decides what counts.
- **Necessity.** Delete-and-guess each ticked document, from the rest and from recall; redo after any
  narrowing; tick every sole source; check that no wrong pair of documents gives the gold.
- **Gold.** The bare value in the asked format: no "about", no "increase of", no bracketed note (pitfall
  5; rows 24, 26: a parenthesis made quick tests read as survivals). A stated figure wins unless the
  question says to compute.
- **Shape.** One line of analysis (pitfall 2), no riddle chain (3), no judgement condition (4).
- Settle every note `screen` prints before the strong-solver screen. The screened sentence is final.

## 6. Screen, then hand over

- Strong-solver screen ([WORKFLOW](../../../WORKFLOW.md) section 4): `packet`, three fresh solves,
  `record-screen`. Three right happens 13% of the time at p = 0.5 and 73% at p = 0.9.
  - **Three right:** rank it last, "local 3/3: likely Too easy at High"; design a new stack next.
  - **One or two right, each miss at an intended lever:** rank it first.
  - **None right, or misses at a second reading:** check the gold and the wording first. A reading a
    solver doubts and then settles is a second reading too: the platform took it (rows 34, 75).
  - Never reword or re-screen a sentence to find a miss.
- Quick tests now run "against the high model" and "never set a tier" (task page, 2026-10-16).
  Quick-test survivors still went Too easy at High (rows 4, 17, 21, 25, 34, 71, 83, 95, 114) or Answer
  not supported (row 75); a quick-test failure went Too easy too (row 92).
- The screen ranks; it never withholds. Hand over every fair sketch, paste-ready, with its screen result,
  stack and decoy; the user chooses (aq-05049). Never recommend release before the user has them all.
- Write the chosen sketch up word for word, prepare, preflight, hand over; the last message before a run
  asks for the capture. Declare only traps whose wrong answers Lever checks recompute.

## 7. After a verdict; batch review

- **Every verdict:** record it, one ledger row, read the traces (`verdict_summary.py`; no route without
  the attempt's text), decide only this question's next action. No rule, note or tool check for one run.
- **"Too easy" at High:** replace the stack, not the wording ("change where the answer lives, not how
  many rules the question has").
- **A defensible miss or "Answer not supported":** compare the attempts with the gold and readings; one
  repair to a single reading with no cue, then a new screen (rows 28, 30).
- **Every five platform results** (ledger rows with a run, all bundles): compare screen against platform
  per row; add a kind only with a platform pass behind it; retire one after two "Too easy" results at
  High. Two pages at most.
