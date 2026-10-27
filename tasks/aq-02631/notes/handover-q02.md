# aq-02631 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02631 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 bb40ae5c86df8a6ce5e6fca216f53309e184a1ed95fb7f8dd741d4c4c5ea4e78: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D04 = Doc 4, D05 = Doc 5.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 4: Doc 2 doesn't mention 4.78. Doc 2 prints it first at character 27,797, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 2 doesn't mention 5.02. Doc 2 prints it first at character 27,864, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 2 doesn't mention 1.50. Doc 2 prints it first at character 27,931, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 2 doesn't mention 0.27. Doc 2 prints it first at character 28,199, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many percentage points would Solana's weight in the Hashdex trust, at its index's December 31, 2024 weights under the strategy as Nasdaq filed it, exceed its June 30, 2025 weight in Bitwise 10 (two decimals)?
```

### Number of asks

1 ask

### Gold answer

```text
1.10 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, proposed Rule 5712(e)(1)(ii)): at least 90% of the weight of the trust's holdings must be in assets on which Nasdaq can obtain information through the Intermarket Surveillance Group or a surveillance sharing agreement.

Step 2. Source input (Doc 2, the proposed strategy): the trust's weights are expected to match the index, but the strategy as filed also says the sponsor checks the weights daily and, if the portfolio breaches that requirement, will limit all assets other than the eligible ones to a tenth of the portfolio together, each in proportion to its index weight.

Step 3. Source input (Doc 2, surveillance discussion): when the proposal was filed, the futures markets through which Nasdaq says it can obtain information were CME's for bitcoin and ether and Coinbase Derivatives' for Chainlink, Litecoin and Avalanche. The filing names none for Solana, XRP, Cardano or Uniswap, so those four are outside the eligible set.

Step 4. Source input and calculation (Doc 2, table of index constituents and weightings at the end of December 2024): the four are weighted Solana 4.78, XRP 5.02, Cardano 1.50 and Uniswap 0.27. Their combined weight: 4.78 + 5.02 + 1.50 + 0.27 = 11.57. That is more than a tenth of the index, so a portfolio held at index weights breaches the requirement and the method applies.

Step 5. Source input (Doc 5, portfolio weightings as of June 30, 2025): Solana is 3.03% of the Bitwise 10 trust's portfolio. The earlier staff order prints the same sentence.

Step 6. Calculation (Doc 2 and Doc 5): the factor that brings the capped group down to its limit: 10 / 11.57 = 86.43%.

Step 7. Calculation (Doc 2 and Doc 5): Solana's weight in the Hashdex portfolio after the cap: 4.78 × 86.43% = 4.131354.

Step 8. Final answer (Doc 2 and Doc 5): the capped Hashdex weight minus the Bitwise weight, in percentage points: 4.131354 - 3.03 = 1.101354, which is the gold answer at two decimals. Carrying the unrounded factor gives the same two decimals.
```

### Answer components

Component 1

```text
1.10
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: proposed Rule 5712(e)(1)(ii), L62)

```text
at least 90% of the weight of such holdings shall, on both an initial and continuing basis, consist of commodities and/or digital assets concerning which the Exchange is able to obtain information via the Intermarket Surveillance Group
```

Evidence 2: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: sponsor's method, L143)

```text
If the portfolio breaches the requirement, the Sponsor will adjust the portfolio to comply with its listing rule according to the following method:
```

Evidence 3: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: sponsor's method, L144)

```text
The combined allocation of all digital assets other than those eligible under the 90% requirement will be limited to 10% of the portfolio, with their individual weights proportionally adjusted to reflect their relative weightings in the Index.
```

Evidence 4: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: weight table heading, L127)

```text
As of December 31, 2024, the Index Constituents and their weightings
```

Evidence 5: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: weight table, L134)

```text
Bitcoin (BTC)................................................ 72.70 Ether (ETH).................................................. 14.48 Solana (SOL)................................................. 4.78 XRP Ledger (XRP)............................................. 5.02 Cardano (ADA)................................................ 1.50 Chainlink (LINK)............................................. 0.51 Avalanche (AVAX)............................................. 0.37 Litecoin (LTC)............................................... 0.37 Uniswap (UNI)................................................ 0.27
```

Evidence 6: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: surveillance discussion, L379)

```text
Notably, the Coinbase Derivatives offers derivative products for three additional Index Constituents (as of the filing date): chainlink (LINK), litecoin (LTC), and avalanche (AVAX).
```

Evidence 7: document Doc 2 (fr_2025_03662.txt), proves component 1. 1.10 (local note: statutory basis, L492)

```text
In particular, the CME bitcoin futures market and CME ether futures market are large, surveilled, and regulated markets
```

Evidence 8: document Doc 5 (fr_2025_20523.txt), proves component 1. 1.10 (local note: Summary of the Proposal, L58)

```text
As of June 30, 2025, the Trust's Portfolio Assets and their weightings were: 78.72% bitcoin (BTC), 11.10% ether (ETH), 4.97% XRP (XRP), 3.03% Solana (SOL), 0.78% Cardano (ADA), 0.35% SUI (SUI), 0.32% Chainlink (LINK), 0.28% Avalanche (AVAX), 0.24% Litecoin (LTC), and 0.19% Polkadot (DOT).
```

Evidence 9: document Doc 4 (fr_2025_14036.txt), proves component 1. 1.10 (local note: The Trust, L68)

```text
As of June 30, 2025, the Trust's Portfolio Assets and their weightings were: 78.72% bitcoin (BTC), 11.10% ether (ETH), 4.97% XRP (XRP), 3.03% Solana (SOL), 0.78% Cardano (ADA), 0.35% SUI (SUI), 0.32% Chainlink (LINK), 0.28% Avalanche (AVAX), 0.24% Litecoin (LTC), and 0.19% Polkadot (DOT).
```

### Necessary documents

- Tick Doc 2 (fr_2025_03662.txt), role: Answer component
- Tick Doc 5 (fr_2025_20523.txt), role: Answer component; also tick Doc 4 (fr_2025_14036.txt) and choose it in Doc 5's "or..." box

Leave unticked: Doc 1 (fr_2024_30683.txt), Doc 3 (fr_2025_10119.txt), Doc 6 (fr_2025_21402.txt), Doc 7 (fr_2026_08274.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 2's constituent table prints Solana's index weight, 4.78; taking it as the portfolio weight gives 1.75. The uncovered assets total 11.57, above the 10% cap, so the sponsor's method scales Solana to 4.13, and against Doc 5's 3.03 the answer is 1.10.
```

(45 / 50 words.)
