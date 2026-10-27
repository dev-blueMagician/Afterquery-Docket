"""Independent arithmetic for aq-06708 hooks (inputs typed from text/Dnn.txt; thousands unless noted)."""
# --- h1: currency effect on revenue, first nine months of 2025 ---
# Snap 2025 quarters, D06 supplemental table: Revenue and Constant Currency Revenue rows
snap_gaap = {"Q1": 1_363_217, "Q2": 1_344_930, "Q3": 1_506_839, "Q4": 1_716_461}
snap_cc   = {"Q1": 1_370_500, "Q2": 1_334_606, "Q3": 1_494_999, "Q4": 1_695_488}
fx = {q: snap_gaap[q] - snap_cc[q] for q in snap_gaap}
snap_9m = fx["Q1"] + fx["Q2"] + fx["Q3"]
print("Snap FX by quarter", fx, "9M net", snap_9m, "9M gross", abs(fx["Q1"]) + fx["Q2"] + fx["Q3"])
# Pinterest, D04 footnote (1): CC revenue $1,305.9M (Q4) and $4,205.3M (FY); favorable FX $13.5M and $16.5M
pin_fy_fx = 4_221_767 - 4_205_300; pin_q4_fx = 1_319_347 - 1_305_900
pin_9m = pin_fy_fx - pin_q4_fx
print("Pinterest FX FY", pin_fy_fx, "Q4", pin_q4_fx, "9M", pin_9m, "(stated 16.5 - 13.5 =", 16.5 - 13.5, ")")
gold1 = (snap_9m - pin_9m) / 1000
print("h1 gold Snap-Pinterest 9M ($M)", round(gold1, 3), "-> nearest million", round(gold1))
for lo, hi in ((16.45, 13.55), (16.55, 13.45)):
    print("  rounding bound", round(snap_9m / 1000 - (lo - hi), 3))
print("  lure gross Q1 sign:", round((abs(fx['Q1']) + fx['Q2'] + fx['Q3'] - pin_9m) / 1000, 2))
print("  lure Pinterest FY:", round((snap_9m - pin_fy_fx) / 1000, 2), " lure Pinterest ignored:", round(snap_9m / 1000, 2))
print("  lure both FY:", round((sum(fx.values()) - pin_fy_fx) / 1000, 2), " lure Snap FY vs Pin 9M:", round((sum(fx.values()) - pin_9m) / 1000, 2))
# --- h2: Pinterest 2025 quarters; Q3 = FY (D04) - Q4 (D04) - H1 (D03 six-month column) ---
fy = dict(rev=4_221_767, opinc=319_883, ebitda=1_269_976, cor=841_521)
q4 = dict(rev=1_319_347, opinc=301_174, ebitda=541_500, cor=226_917)
h1 = dict(rev=1_853_215, opinc=-39_807, cor=402_279)
q1_25 = dict(rev=854_988, opinc=-35_477, ebitda=171_649)   # D01
q2_25 = dict(rev=998_227, opinc=-4_330, ebitda=250_776)    # D03
assert q1_25["rev"] + q2_25["rev"] == h1["rev"] and q1_25["opinc"] + q2_25["opinc"] == h1["opinc"]
q3 = dict(rev=fy["rev"] - q4["rev"] - h1["rev"], opinc=fy["opinc"] - q4["opinc"] - h1["opinc"],
          ebitda=fy["ebitda"] - q4["ebitda"] - q1_25["ebitda"] - q2_25["ebitda"])
print("Pinterest Q3 2025", q3, "op margin %", round(100 * q3["opinc"] / q3["rev"], 3),
      "AdjEBITDA margin %", round(100 * q3["ebitda"] / q3["rev"], 3))
print("  operating income by quarter 2025:", q1_25["opinc"], q2_25["opinc"], q3["opinc"], q4["opinc"])
print("  lure Q4 margin %", round(100 * q4["ebitda"] / q4["rev"], 3), " FY %", round(100 * fy["ebitda"] / fy["rev"], 3),
      " Q2 %", round(100 * q2_25["ebitda"] / q2_25["rev"], 3))
# --- h10: Snap revenue excluding Other Revenue, YoY growth, Q4 2025 (D07) and Q1 2026 (D05) ---
def ex_other(total_now, total_prior, other_now, growth):
    prior_other = other_now / (1 + growth)
    return (total_now - other_now) / (total_prior - prior_other) - 1
q4 = ex_other(1_716.461, 1_557.283, 232, 0.62); q1 = ex_other(1_528.791, 1_363.217, 285, 0.87)
print("h10 ex-Other growth Q4 2025 %", round(100 * q4, 3), "Q1 2026 %", round(100 * q1, 3), "change pp", round(100 * (q1 - q4), 3))
lo = ex_other(1_528.791, 1_363.217, 284.5, 0.875) - ex_other(1_716.461, 1_557.283, 231.5, 0.615)
hi = ex_other(1_528.791, 1_363.217, 285.5, 0.865) - ex_other(1_716.461, 1_557.283, 232.5, 0.625)
cands = [ex_other(1_528.791, 1_363.217, o1, g1) - ex_other(1_716.461, 1_557.283, o4, g4)
         for o1 in (284.5, 285.5) for g1 in (0.865, 0.875) for o4 in (231.5, 232.5) for g4 in (0.615, 0.625)]
print("  bounds pp", round(100 * min(cands), 3), round(100 * max(cands), 3))
tot_q4 = 1_716.461 / 1_557.283 - 1; tot_q1 = 1_528.791 / 1_363.217 - 1
print("  lure total revenue change pp", round(100 * (tot_q1 - tot_q4), 3))
sub_q4 = (1_716.461 - 232) / (1_557.283 - 232) - 1; sub_q1 = (1_528.791 - 285) / (1_363.217 - 285) - 1
print("  lure current Other off both years pp", round(100 * (sub_q1 - sub_q4), 3), " lure Other growth change", 87 - 62)
# --- h11: share-based compensation line of each Adjusted EBITDA reconciliation, H1 2026 vs H1 2025 ---
pin_26 = 222_121 + 319_729; pin_25 = 187_426 + 227_234          # D01 l.267, D03 l.272
snap_26, snap_25 = 486_720, 499_224                             # D06 l.235 six-month columns
g_pin = pin_26 / pin_25 - 1; g_snap = snap_26 / snap_25 - 1
print("h11 Pinterest %", round(100 * g_pin, 3), "Snap %", round(100 * g_snap, 3), "gap pp", round(100 * (g_pin - g_snap), 3))
g_pin_cf = 555_963 / 414_660 - 1; g_snap_tbl = 513_229 / 499_224 - 1  # D03 six-month cash flow; D06 SBC table
print("  lures: both totals", round(100 * (g_pin_cf - g_snap_tbl), 2), " Pinterest cash-flow line", round(100 * (g_pin_cf - g_snap), 2),
      " Snap table", round(100 * (g_pin - g_snap_tbl), 2))
# --- h12: 2031 Notes converted in full at 150% of the conversion price (D02 Note 5), vs shares outstanding ---
rate = 44.0063; notes = 1_000_000            # per $1,000 principal; $1.0B principal
for cp in (1000 / rate, 22.72):
    price = 1.5 * cp
    net_shares = notes * (rate - 1000 / price)   # cash up to principal, shares for the excess
    print("h12 conversion price", round(cp, 4), "price", round(price, 3), "net shares", round(net_shares))
    for label, base in (("Jun 30 A+B (D03)", 490_712_000 + 74_785_000), ("Mar 31 A+B (D02)", 493_991_000 + 79_680_000),
                        ("Apr 28 A+B (D02 cover)", 481_750_308 + 78_407_019), ("Jun 30 A only", 490_712_000)):
        print("   ", label, round(100 * net_shares / base, 3))
print("  lure physical 44,006,300:", round(100 * 44_006_300 / 565_497_000, 3), " max-rate net:",
      round(100 * notes * (57.2082 - 1000 / (1.5 * 1000 / rate)) / 565_497_000, 3))
# --- h13: ASR average price after settlement (D02) vs year-to-date average (D03 headline) ---
asr_total = 41_279_670 + 13_516_943
asr_avg = 1_000_000_000 / asr_total
print("h13 ASR shares", asr_total, "avg", round(asr_avg, 4), "minus YTD 18.17:", round(asr_avg - 18.17, 4),
      " lures: initial only", round(1e9 / 41_279_670 - 18.17, 3), " 80% expected", round(1e9 / (41_279_670 / 0.8) - 18.17, 3))
q1_avg = (472.9e6 + 493.0e6 + 1e9) / (27_664_663 + 26_188_857 + asr_total)
print("  Q1 purchases incl. April settlement avg", round(q1_avg, 4))
# --- h14: quarters Q1 2025-Q2 2026 in which free cash flow exceeded cash spent on share repurchases ---
pin_fcf = {"Q1'25": 356_417, "Q2'25": 196_683, "Q4'25": 380_368, "Q1'26": 311_682, "Q2'26": 269_933}   # D01, D03, D04
pin_fcf["Q3'25"] = 1_251_889 - 380_368 - (571_399 - 18_299)                                         # D04 FY/Q4 less D03 H1
pin_buy = {"Q1'25": 175_000, "Q2'25": 52_626, "Q4'25": 502_000, "Q1'26": 1_946_308, "Q2'26": 78_578}
pin_buy["Q3'25"] = 927_013 - 502_000 - 227_626
pin_tax = {"Q1'25": 93_754, "Q2'25": 105_714, "Q3'25": 398_982 - 84_722 - 199_468, "Q4'25": 84_722, "Q1'26": 68_899, "Q2'26": 111_633}
snap_fcf = {"Q1'25": 114_396, "Q2'25": 23_793, "Q3'25": 93_444, "Q4'25": 205_556, "Q1'26": 286_007, "Q2'26": 120_538}  # D06 table
snap_buy = {"Q1'25": 257_100, "Q2'25": 243_473, "Q4'25": 250_293, "Q1'26": 350_499, "Q2'26": 250_465}
snap_buy["Q3'25"] = 750_866 - 250_293 - 500_573                                                     # D07 FY/Q4 less D06 H1
order = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"]
print("h14 Pinterest FCF > buybacks:", [q for q in order if pin_fcf[q] > pin_buy[q]],
      " incl. tax withholding:", [q for q in order if pin_fcf[q] > pin_buy[q] + pin_tax[q]])
print("    Pinterest Q3'25 FCF", pin_fcf["Q3'25"], "buybacks", pin_buy["Q3'25"], "+tax", pin_buy["Q3'25"] + pin_tax["Q3'25"])
print("h14 Snap FCF > buybacks:", [q for q in order if snap_fcf[q] > snap_buy[q]], " Snap Q3'25 buybacks", snap_buy["Q3'25"])
# --- h15: Snap quarters with interest expense above interest income ---
inc = {"Q1'25": 37_018, "Q2'25": 33_199, "Q4'25": 31_687, "Q1'26": 26_459, "Q2'26": 24_672}
exp = {"Q1'25": 23_399, "Q2'25": 27_607, "Q4'25": 36_498, "Q1'26": 36_756, "Q2'26": 36_941}
inc["Q3'25"] = 134_159 - 31_687 - 70_217; exp["Q3'25"] = 121_998 - 36_498 - 51_006
print("h15 Snap expense > income:", [q for q in order if exp[q] > inc[q]], " Q3'25 income", inc["Q3'25"], "expense", exp["Q3'25"])
# --- h16: Pinterest quarters Q2 2025-Q2 2026 whose share-based compensation (cash-flow add-back) exceeded the prior quarter's ---
sbc_cf = {"Q1'25": 187_426, "Q2'25": 227_234, "Q4'25": 230_667, "Q1'26": 231_446, "Q2'26": 324_517}   # D01/D02, D03, D04
sbc_cf["Q3'25"] = 880_463 - 230_667 - 414_660                                                        # D04 FY/Q4 less D03 H1
sbc_ng = dict(sbc_cf, **{"Q1'26": 222_121, "Q2'26": 319_729})                                         # reconciliation lines
seq = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"]
rise = lambda d, qs: [qs[i] for i in range(1, len(qs)) if d[qs[i]] > d[qs[i-1]]]
print("h16 cash-flow basis:", rise(sbc_cf, seq), " Q3'25", sbc_cf["Q3'25"], " Q1'26 minus Q4'25", sbc_cf["Q1'26"] - sbc_cf["Q4'25"])
print("    no Q3 (Q4 vs Q2):", rise(sbc_cf, [q for q in seq if q != "Q3'25"]), " reconciliation basis:", rise(sbc_ng, seq))
# --- h17: Snap gross margin, Q3 2025 (printed nowhere: cost of revenue FY - Q4 - H1) to Q4 2025, vs headline "up 4 percentage points" ---
rev_q3, rev_q4 = 1_506_839, 1_716_461                       # D07 supplemental / statement
cor_q4 = 702_443; cor_q3 = 2_669_575 - 702_443 - 1_292_912     # D07 FY and Q4; D06 six-month 2025 (= D05 Q1 639,579 + D06 Q2 653,333)
gm3 = 1 - cor_q3 / rev_q3; gm4 = 1 - cor_q4 / rev_q4
print("h17 Q3 cost", cor_q3, "GM Q3 %", round(100 * gm3, 4), "GM Q4 %", round(100 * gm4, 4), "change pp", round(100 * (gm4 - gm3), 4))
gm_q4_24 = 1 - 671_660 / 1_557_283; gm_fy = 1 - 2_669_575 / 5_931_447; gm_h1 = 1 - 1_292_912 / 2_708_147
print("    lures: headline 4; vs FY2025", round(100 * (gm4 - gm_fy), 2), " vs H1 2025", round(100 * (gm4 - gm_h1), 2), " YoY", round(100 * (gm4 - gm_q4_24), 2))
# --- h18: Pinterest Q3 2026 revenue guidance midpoint vs Q3 2025 (printed nowhere), vs printed "13% - 15%" ---
q3_25 = 4_221_767 - 1_319_347 - 1_853_215
for label, v in (("low", 1_190_000), ("mid", 1_200_000), ("high", 1_210_000)):
    print("h18", label, round(100 * (v / q3_25 - 1), 3))
# --- h19: Snap minus Pinterest gross-margin rise, Q3 to Q4 2025 (both Q3s printed nowhere) ---
p_rev_q3 = 4_221_767 - 1_319_347 - 1_853_215; p_cor_q3 = 841_521 - 226_917 - 402_279      # D04 FY/Q4, D03 six-month 2025
p_gm3 = 1 - p_cor_q3 / p_rev_q3; p_gm4 = 1 - 226_917 / 1_319_347
s_rise = gm4 - gm3; p_rise = p_gm4 - p_gm3
print("h19 Pinterest Q3 rev", p_rev_q3, "cost", p_cor_q3, "GM Q3 %", round(100 * p_gm3, 4), "Q4 %", round(100 * p_gm4, 4), "rise", round(100 * p_rise, 4))
print("    Snap rise", round(100 * s_rise, 4), " difference pp", round(100 * (s_rise - p_rise), 4))
p_gm_fy = 1 - 841_521 / 4_221_767
print("    lures: Snap headline 4:", round(4 - 100 * p_rise, 3), " Pinterest FY as Q3:", round(100 * (s_rise - (p_gm4 - p_gm_fy)), 3),
      " Snap FY as Q3:", round(100 * ((gm4 - gm_fy) - p_rise), 3), " both FY:", round(100 * ((gm4 - gm_fy) - (p_gm4 - p_gm_fy)), 3))
p_gm3_m = 1 - 212.325 / (4_222 - 1_319 - 855 - 998)
print("    rounding path (Pinterest Q3 revenue from $M table):", round(100 * (s_rise - (p_gm4 - p_gm3_m)), 3))
