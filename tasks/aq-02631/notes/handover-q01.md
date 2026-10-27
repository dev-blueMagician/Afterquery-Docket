# aq-02631 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02631 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 c288004cfb21e669c62e8b2461153b938e2035bb601df17ce37bca2dceb298c9: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN precision: the answer is a rate or decimal; state the precision in the question
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What weight of Bitwise 10's June 30, 2025 portfolio lay outside the eligible assets in T. Rowe Price's ETF proposal when the SEC instituted proceedings on it?
```

### Number of asks

1 ask

### Gold answer

```text
0.35%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, opening paragraphs): the SEC instituted proceedings on NYSE Arca's proposal to list the T. Rowe Price Active Crypto ETF on January 28, 2026. Doc 7 itself is the notice of Amendment No. 1, which the Exchange filed later, on April 21, 2026, and which replaced the original filing. Its list of Eligible Assets is given as of that amendment, so it shows the proposal only as it stood after the proceedings were instituted.

Step 2. Source input (Doc 6, opening paragraph and "Background on Eligible Assets"): the proposal in front of the SEC on that day was still the original filing, made on November 6, 2025. As of that filing the Sponsor considers these to be Eligible Assets: bitcoin (BTC), ether (ETH), SOL, XRP, ada (ADA), AVAX, litecoin (LTC), DOT, Dogecoin (DOGE), HBAR, Bitcoin Cash (BCH), LINK, lumen (XLM) and Shiba Inu (SHIB).

Step 3. Source input (Doc 5, summary of the proposal): as of June 30, 2025 the Bitwise 10 Crypto Index ETF held bitcoin (BTC), ether (ETH), XRP, Solana (SOL), Cardano (ADA), SUI, Chainlink (LINK), Avalanche (AVAX), Litecoin (LTC) and Polkadot (DOT), and SUI's weighting was 0.35%. The staff order the Commission later set aside prints the same sentence.

Step 4. Comparison (Doc 6 and Doc 5): matched by ticker, nine of the Bitwise holdings are on the original filing's list: BTC, ETH, XRP, SOL, ADA, LINK, AVAX, LTC and DOT. SUI is the only holding that is not on it.

Step 5. Final answer (Doc 6 and Doc 5): the weight of the Bitwise portfolio outside the proposal's eligible assets when the SEC instituted proceedings is SUI's 0.35%.

Check on the other version (Doc 7): the amended list adds Sui (SUI). Read against it, every Bitwise holding would be eligible and nothing would lie outside, which is why the date of the proceedings decides the answer.
```

### Answer components

Component 1

```text
0.35%
```

### Evidence

Evidence 1: document Doc 6 (fr_2025_21402.txt), proves component 1. 0.35% (local note: Background on Eligible Assets, L118)

```text
the Sponsor considers the following to be Eligible Assets (ticker symbols in parentheses): bitcoin (BTC), ether (ETH), SOL (SOL), XRP (XRP), ada (ADA), AVAX (AVAX), litecoin (LTC), DOT (DOT), Dogecoin (DOGE), HBAR (HBAR), Bitcoin Cash (BCH), LINK (LINK), lumen (XLM), and Shiba Inu (SHIB).
```

Evidence 2: document Doc 6 (fr_2025_21402.txt), proves component 1. 0.35% (local note: notice, L18)

```text
notice is hereby given that on November 6, 2025, NYSE Arca, Inc.
```

Evidence 3: document Doc 5 (fr_2025_20523.txt), proves component 1. 0.35% (local note: Summary of the Proposal, L58)

```text
As of June 30, 2025, the Trust's Portfolio Assets and their weightings were: 78.72% bitcoin (BTC), 11.10% ether (ETH), 4.97% XRP (XRP), 3.03% Solana (SOL), 0.78% Cardano (ADA), 0.35% SUI (SUI), 0.32% Chainlink (LINK), 0.28% Avalanche (AVAX), 0.24% Litecoin (LTC), and 0.19% Polkadot (DOT).
```

Evidence 4: document Doc 4 (fr_2025_14036.txt), proves component 1. 0.35% (local note: The Trust, L68)

```text
As of June 30, 2025, the Trust's Portfolio Assets and their weightings were: 78.72% bitcoin (BTC), 11.10% ether (ETH), 4.97% XRP (XRP), 3.03% Solana (SOL), 0.78% Cardano (ADA), 0.35% SUI (SUI), 0.32% Chainlink (LINK), 0.28% Avalanche (AVAX), 0.24% Litecoin (LTC), and 0.19% Polkadot (DOT).
```

### Necessary documents

- Tick Doc 6 (fr_2025_21402.txt), role: Used to identify
- Tick Doc 5 (fr_2025_20523.txt), role: Answer component; also tick Doc 4 (fr_2025_14036.txt) and choose it in Doc 5's "or..." box

Leave unticked: Doc 1 (fr_2024_30683.txt), Doc 2 (fr_2025_03662.txt), Doc 3 (fr_2025_10119.txt), Doc 7 (fr_2026_08274.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong edition: Doc 7 reports the January 28, 2026 proceedings but lists eligible assets as of its April 21, 2026 amendment, adding Sui, so every Bitwise holding looks eligible and the answer becomes zero. The filing then pending, Doc 6, omits Sui, leaving its 0.35%.
```

(45 / 50 words.)
