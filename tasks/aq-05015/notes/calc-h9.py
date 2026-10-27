# aq-05015 h9: U.S. West Coast operating expenses (excluding D&A) per barrel, Q3 -> Q4 2025.
# Inputs typed from tasks/aq-05015/text (line numbers in comments). $ millions; thousand bbl/day.

days_q3, days_q4 = 92, 92                       # Jul-Sep, Oct-Dec
opex_q3, thru_q3 = 239, 259                     # D05:433 (row "(a) 239"), D05:624
opex_q4, thru_q4 = 213, 265                     # D06:463 (row "(c) 213"), D06:657
retention_q3 = 50                               # D05:799 note (a); D05:857-860 West Coast 239 - 50 = 189
printed_adj_q3, printed_adj_q4 = 7.94, 8.72     # D05:628, D06:661 ("Adjusted operating expenses ... per barrel")

bbl_q3 = thru_q3 * days_q3                       # thousand barrels
bbl_q4 = thru_q4 * days_q4
gaap_q3 = opex_q3 / bbl_q3 * 1000                # $ per barrel
gaap_q4 = opex_q4 / bbl_q4 * 1000
print(f"Q3 GAAP {gaap_q3:.3f}  Q4 GAAP {gaap_q4:.3f}  change {gaap_q4 - gaap_q3:+.3f}")
print(f"Q4 printed 8.72 vs computed {gaap_q4:.3f}: change with printed Q4 {printed_adj_q4 - gaap_q3:+.3f}")
# Route via printed adjusted Q3 plus retention per barrel
alt_q3 = printed_adj_q3 + retention_q3 / bbl_q3 * 1000
print(f"Q3 via printed adjusted + retention: {alt_q3:.3f}; change {printed_adj_q4 - alt_q3:+.3f}")

# Lure: compare the two printed per-barrel rows (both "Adjusted")
print(f"lure (printed rows): {printed_adj_q4 - printed_adj_q3:+.3f}")
# Second reading: opex including D&A (rejected by 'excluding depreciation')
da_q3, da_q4 = 173, 173                          # D05:434, D06:464
print(f"opex+D&A reading: {(opex_q4 + da_q4) / bbl_q4 * 1000 - (opex_q3 + da_q3) / bbl_q3 * 1000:+.3f}")

# Without D05: Q3 rebuilt from D06 full year minus first half (D04 or D08) minus Q4
fy_opex, fy_thru = 844, 249                      # D06:463, D06:657
h1_opex, h1_thru = 392, 237                      # D08:436 / D04:427 ; D08:626 / D04:619
q3_bbl_rebuilt = fy_thru * 365 - h1_thru * 181 - bbl_q4
q3_rebuilt = (fy_opex - h1_opex - opex_q4) / q3_bbl_rebuilt * 1000
print(f"without D05: Q3 {q3_rebuilt:.3f} -> change {gaap_q4 - q3_rebuilt:+.3f}")

for v in [gaap_q4 - gaap_q3, printed_adj_q4 - gaap_q3, printed_adj_q4 - alt_q3]:
    assert round(v, 1) == -1.3, v
assert round(printed_adj_q4 - printed_adj_q3, 1) == 0.8
print("gold -1.3 on every D05+D06 route; lure +0.8")
