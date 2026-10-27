# aq-04797 - document map

Navigation only (like the form's overview); questions quote `text/`, never this map. Line numbers
are `text/Dnn.txt` lines. Read in full by the caller on 2026-10-14 (all nine documents, every line).

## Bundle

- What it is: nine academic papers on lithium-ion (and one lithium-metal) battery state-of-health
  (SOH) estimation; platform label "Academic papers", 86,630 prompt tokens.
- Documents: 9; local ids are alphabetical by file name and differ from the page's Doc numbers
  (see `notes/intake.json`): D05 = Doc 1, D07 = Doc 2, D01 = Doc 3, D06 = Doc 4, D02 = Doc 5,
  D08 = Doc 6, D03 = Doc 7, D09 = Doc 8, D04 = Doc 9.
- Gaps: none in the capture (9 of 9 read in full, 0 gap characters). Table bodies are absent in
  the platform text itself (not an extraction fault): Doc 2 Table 1 (cell characteristics) and
  Tables 2-5 (correlations); Doc 3 Tables 1-3 and Supporting Information; Doc 6 Tables 1-11. Only
  their prose descriptions exist.
- Provenance: capture `AQ-04797_2026-10-14_0909.txt`, sha256 in `notes/intake.json`; repeat-bundle
  check 2026-10-14: no earlier task shares any file name or content (earlier academic bundles
  aq-01650 and trial-01 are different papers).

## Doc 1 (D05) - LSTM + PPO hybrid ("physics-informed hybrid RL"), Salem et al.

- NASA cells (line 65): B0005, B0006, B0007 NCA/graphite 2 Ah; B0018 NMC/graphite 1.35 Ah; CC-CV
  1.5 A to 4.2 V, 20 mA cut-off; discharge 2 A to 2.7 / 2.5 / 2.2 V (B0005/6/7), B0018 1.5 A to
  2.5 V; 24 °C. SOH_n = C_n / C_0, C_0 = initial capacity (line 69).
- Split 60% training from cycle 1, 40% test+validation (line 231). LSTM 128/64 units, dropout 0.3,
  window 10; Table 2 (lines 142-149) 119,617 params. PPO 1,000,000 steps, clip 0.2 (line 209).
- Table 3 (lines 237-253) NASA MAE/RMSE labelled "(%)" on values like 0.0038 (unit ambiguous);
  R² hybrid 0.9958/0.9940/0.9945/0.9916; LSTM 0.9657/0.8966/0.8708/0.9587. BPINN/FNN quoted from ref 19.
- CALCE CS2_35-38 (line 267): 0.5C to 4.2 V, CV to 0.05 A; "constant temperature of 1 °C" (garbled);
  "3712 complete cycles" each vs "several hundred cycles until end-of-life". Table 4 lines 279-289.

## Doc 2 (D07) - KLD of terminal-voltage PDF as health indicator, Hammou et al. (Entropy)

- 3 NMC cylindrical + 4 LFP cells (line 55), WLTC discharge, cycling 35 °C, check-ups 25 °C every
  five days; C/5 capacity; DCIR 1C 30 s pulse. Fade relative to BoL (lines 75-83).
- NMC capacity/energy fade 21%/27%, DCIR +350%; LFP 14%; NMC lose 20% in <850 cycles, LFP 1057 cycles
  <15% (lines 89-97). EOL 20% capacity loss, KLD 0.20-0.23 at EOL (line 143).
- Abstract says Spearman >86%/74%; conclusion says Pearson >86%/74%; LFP cell 2 Pearson ~74%,
  Spearman ~66% (line 151). Noise: insensitive above 30 dB SNR (line 155).

## Doc 3 (D01) - Ridge-Conv-Bi-LSTM, dual-level transfer, high temperature

- Data (line 31): Tsinghua 6 Ah LiFePO4 pouch cells (own, unpublished; "lithium iron phosphate",
  never "LFP"), Oxford Dataset 1 740 mAh pouch cells, Tongji (Zhu et al.). B1-B6, C1-C3, D1-D6 (line 143).
- Single-battery: 7:3, first 25% of the later segment for calibration (line 145). Cross-battery:
  15% nominal calibration, 80-180 cycles, <=35% (line 145). Net 32 filters, 64 Bi-LSTM units,
  dropout 0.12, lr 7e-4 / fine-tune 2e-4 (lines 133, 147).
- B6 RMSE 0.0009 vs Ridge 0.0050, LSTM 0.0079, Bi-LSTM 0.0073, RF 0.0101 (line 173; prose wrongly
  says the largest gain is over LSTM). D6 45 °C 0.0023 (line 183). Temperatures for Tsinghua
  conflict: B6 at 50 °C (lines 5, 25, 199) vs "25 °C, 35 °C, and 45 °C" (line 169).
- Ablations on D4->D3 disagree: non-transfer 0.00907 -> dual 0.00290 (line 225) vs hierarchical
  A0..A3 at 15% calibration, A3 0.004325 (lines 227-233). Calibration study lines 239-247.

## Doc 4 (D06) - DTV features + PSO-GRU

- NASA B0005, "NCM" cathode (line 23) but "lithium cobalt oxide" in limitations (line 348); SOH =
  C_curr / C_nom x 100%, C_nom 2.0 Ah (lines 23-27); EOL 1.4 Ah; 166 valid cycles, 3 excluded
  (lines 31, 93). "All experiments were conducted on the NASA B0005 dataset" (line 221) but 3.4
  adds B0007 (lines 316-320: MAE 0.9869%, RMSE 1.4024%, trained on B0007's own first 70%).
- Split 70/30; optimized strategy drops cycles 1-32 from training, cut-off chosen with test-set
  errors (lines 245, 294-300). Table 1 (255-259) GRU/LSTM/PSO-GRU; Table 2 (287-290) 0.8886 ->
  0.9165 R², MAE 1.4544 -> 0.7462, RMSE 1.8587 -> 0.9660.

## Doc 5 (D02) - CNN + multi-head self-attention, fast-charging LFP, transfer learning, Zhao et al.

- 222 LFP cells, 146,074 cycles (line 7); #1 177 cells 111,211 cycles, #2 45 cells 37,955 cycles
  (line 61); Table 1 (67-70): 1.1 Ah, 3.3 V, 2.0 V cut-off, 30 °C, #1 CV cut-off C/50. Lifetime to
  80% of nominal (line 61); initial capacities mostly 1.06-1.08 Ah (line 63).
- 20 cells removed -> 202; 142 train / 21 validation / 39 test (line 206). Fine-tuning uses the
  test set (lines 184-186, 389): post-fine-tuning scores are on cells the network was tuned on.
- Before/after transfer: RMSE 0.00609 -> 0.00479 Ah, R² 0.959 -> 0.977 (Table 4 lines 192-196,
  line 212, line 393) but line 188 says 0.00741 -> 0.00109 and 0.986 -> 0.998. Summary "R2 of 0.97",
  "approximately 22,000 parameters"; Table 3 (155-164) sums to 20,000. Tables 5-7 lines 224-306.

## Doc 6 (D08) - GAT-BiGRU-Res on IC-peak feature fragments

- XJTU Batch1 8 + Batch2 15 cells, NCM523 2 Ah; CALCE CX2 four LiCoO2 1.35 Ah, 0.5C/1C, 1/30 Hz
  (line 139). SOH = C_aged / C_0 x 100%, C_0 = rated capacity (lines 143-145).
- Main test: random 6:4 split within every cell (line 169). MAEs 0.355/0.303/1.025% (line 231);
  abstract "average" 0.561% / RMSE 0.783% = per-dataset mean (line 5). Held-out cells: train on
  first four Batch1 cells, test on the rest: MAE 0.608, RMSE 0.802, R² 0.977 (line 215).
- 0.45 M params, 1.68 MFLOPs, 17.55 ms on Raspberry Pi 4 (line 219); GRU 0.706% -> 0.395% with GAT (line 189).

## Doc 7 (D03) - label-free swarm of DNNs with domain adaptation, Lu et al.

- 65 cells, 5 manufacturers, 10,757 samples (Table 1 lines 45-51); 71,588 samples over 80 cases.
  Table 1: CALCE LCO 1.1 Ah 2807 / 1397 h; SANYO NMC 1.85 Ah; PANASONIC NCA 3.03 Ah; KOKAM LCO/NCO
  0.74 Ah 503 / 8473 h; GOTION LFP 27 Ah 4262 / 2238 h. PANASONIC and GOTION are in-lab (line 41).
- SOH = present / initial capacity (line 13); C-rate vs nominal (line 41); 500 mV window, 10 mV grid
  (lines 35, 61). Methods (line 191): #3 20 °C, 0.3C to 4.2 V, CV to 0.03 A, 2C discharge; #5 45 °C,
  1C to 3.65 V, CV to 1.35 A, 1C. Fine-tuning works "require at least 25-30%" target labels (line 17).
- Results: max AE 10.09 -> 8.87% after trim; 89.4% < 3%, 98.9% < 5%; swarm 300, ~0.7 h (line 77).

## Doc 8 (D09) - commentary: future SOH definitions and automotive battery data

- SOH_C = C(t) / C_nom (line 45), SOH_E, SOH_UBE, SOH_R; vector SOH. Warranty USABC 15 y / 1000
  cycles, EUCAR 150,000 km / 22-24 MWh, NEDO 10-15 y / 1000-1500 cycles (line 11). Sauer 48 cells,
  grade C (line 109). Table 1 sampling (lines 145-152): V and I 100 ms; T and SOC 1 s; capacity daily/weekly.

## Doc 9 (D04) - ML on EIS for lithium-metal ML2032 coin cells

- Li-Al anode, MnO2 cathode; 105 cells, 25 °C, 6.5 mA (10x recommended), 3.25/1.5 V, stop at 50% of
  initial capacity (line 126); EIS 54 points 100 kHz-50 mHz every five cycles (line 130).
- 695 spectra, 556 train / 139 test (line 37); R² XGBoost 0.9471, CatBoost 0.9395, RF 0.9533,
  LightGBM 0.9476 (Table 1 lines 67-72) against claims of ">95%" and ">93%". Li 3850, graphite 372,
  Li-Al 993 mAh/g (lines 11, 23).

## Shared ground (navigation only)

- NASA B0005 and B0007: Doc 1 and Doc 4 (same protocol figures; cathode NCA vs NCM; SOH basis
  initial vs nominal). B0006 and B0018 only in Doc 1. Doc 2 mentions "the NASA dataset" (line 13).
- CALCE: Doc 1 (CS2_35-38, capacity not stated), Doc 6 (CX2, 1.35 Ah), Doc 7 (LCO 1.1 Ah) - different
  series; the bundle never links them.
- Oxford 740 mAh (Doc 3) and KOKAM 0.74 Ah (Doc 7): the bundle never says they are the same data.
- LFP: Doc 2 (4 cells, capacity not stated), Doc 3 (Tsinghua 6 Ah), Doc 5 (1.1 Ah), Doc 7 (GOTION 27 Ah).
- Citation inside the bundle: Doc 5 ref 52 (line 43) describes Doc 7's framework.
- SOH bases: initial (Doc 1, Doc 2, Doc 7); nominal/rated (Doc 4, Doc 6, Doc 8); none stated (Doc 3,
  Doc 9; Doc 5 states end of life against nominal).
- Held-out-cell evaluations: Doc 6 4.4 only clean one; Doc 5 pre-fine-tuning; Doc 3 transfer tasks
  use target calibration labels; Doc 4's B0007 test trains on B0007.
