# aq-02631 q03 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02631 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 0bcf30b364952305fc99ced1dd651a236fe6df7f1e5431c3b29ffd33e2d2d05e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D06 = Doc 6.
- Floor: 0 FAIL, 7 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 4.78. Doc 2 prints it first at character 27,797, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 5.02. Doc 2 prints it first at character 27,864, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 1.50. Doc 2 prints it first at character 27,931, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 2 doesn't mention 0.27. Doc 2 prints it first at character 28,199, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 6 doesn't mention 18. Doc 6 prints it first at character 24,844, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 6 doesn't mention 20. Doc 6 prints it first at character 29,007, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On what date would a Hashdex trust portfolio held at the index weights of December 31, 2024 first have met proposed Rule 5712's 90% requirement?
```

### Number of asks

1 ask

### Gold answer

```text
March 18, 2025
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, proposed Rule 5712(e)(1)(ii)): at least 90% of the weight of the trust's holdings must be in assets on which Nasdaq can obtain information through the Intermarket Surveillance Group (ISG) or a surveillance sharing agreement. Assets without that coverage may therefore make up no more than a tenth of the portfolio.

Step 2. Source input (Doc 2, surveillance discussion): Nasdaq gets that information from futures markets run by fellow ISG members: CME for bitcoin and ether, and Coinbase Derivatives for Chainlink, Litecoin and Avalanche. The filing names no such market for Solana, XRP, Cardano or Uniswap.

Step 3. Source input and calculation (Doc 2, table of index constituents and weightings at the end of December 2024): the four uncovered constituents are weighted Solana 4.78, XRP 5.02, Cardano 1.50 and Uniswap 0.27. Together: 4.78 + 5.02 + 1.50 + 0.27 = 11.57. That is more than a tenth, so a portfolio held at those weights does not meet the requirement when Nasdaq proposes the rule.

Step 4. Source input (Doc 6, asset backgrounds in the T. Rowe Price filing): Solana futures became available for trading on CME on March 18, 2025, and XRP futures on May 20, 2025. No document dates a futures market for Cardano or Uniswap.

Step 5. Calculation (Doc 2 and Doc 6): once Solana is covered through CME, the uncovered weight is: 11.57 - 4.78 = 6.79. That is under a tenth, so the requirement is met from the day Solana futures start trading on CME.

Step 6. Final answer (Doc 2 and Doc 6): Solana's CME futures come before XRP's, and Solana alone is enough, so the portfolio would first have met the requirement on March 18, 2025.
```

### Answer components

Component 1

```text
March 18, 2025
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_03662.txt), proves component 1. March 18, 2025 (local note: proposed Rule 5712(e)(1)(ii), L62)

```text
at least 90% of the weight of such holdings shall, on both an initial and continuing basis, consist of commodities and/or digital assets concerning which the Exchange is able to obtain information via the Intermarket Surveillance Group
```

Evidence 2: document Doc 2 (fr_2025_03662.txt), proves component 1. March 18, 2025 (local note: CME and ISG, L352)

```text
The exchanges have comprehensive surveillance-sharing agreements with the CME via their common membership in the ISG
```

Evidence 3: document Doc 2 (fr_2025_03662.txt), proves component 1. March 18, 2025 (local note: surveillance discussion, L379)

```text
Notably, the Coinbase Derivatives offers derivative products for three additional Index Constituents (as of the filing date): chainlink (LINK), litecoin (LTC), and avalanche (AVAX).
```

Evidence 4: document Doc 2 (fr_2025_03662.txt), proves component 1. March 18, 2025 (local note: weight table heading, L127)

```text
As of December 31, 2024, the Index Constituents and their weightings
```

Evidence 5: document Doc 2 (fr_2025_03662.txt), proves component 1. March 18, 2025 (local note: weight table, L134)

```text
Bitcoin (BTC)................................................ 72.70 Ether (ETH).................................................. 14.48 Solana (SOL)................................................. 4.78 XRP Ledger (XRP)............................................. 5.02 Cardano (ADA)................................................ 1.50 Chainlink (LINK)............................................. 0.51 Avalanche (AVAX)............................................. 0.37 Litecoin (LTC)............................................... 0.37 Uniswap (UNI)................................................ 0.27
```

Evidence 6: document Doc 6 (fr_2025_21402.txt), proves component 1. March 18, 2025 (local note: SOL background, L144)

```text
On March 18, 2025, SOL futures became available for trading on CME, a CFTC-regulated marketplace.
```

Evidence 7: document Doc 6 (fr_2025_21402.txt), proves component 1. March 18, 2025 (local note: XRP background, L156)

```text
On May 20, 2025, XRP futures became available for trading on CME, a CFTC-regulated marketplace.
```

### Necessary documents

- Tick Doc 6 (fr_2025_21402.txt), role: Answer component
- Tick Doc 2 (fr_2025_03662.txt), role: Used to identify

Leave unticked: Doc 1 (fr_2024_30683.txt), Doc 3 (fr_2025_10119.txt), Doc 4 (fr_2025_14036.txt), Doc 5 (fr_2025_20523.txt), Doc 7 (fr_2026_08274.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Scope: Doc 6's six-month futures test belongs to NYSE Arca's generic standards, not Nasdaq's Rule 5712; applying it gives September 18, 2025. Linking: Doc 6 also dates XRP futures, May 20, 2025, but Solana's alone lifts covered weight past 90%, so the first date is March 18, 2025.
```

(48 / 50 words.)
