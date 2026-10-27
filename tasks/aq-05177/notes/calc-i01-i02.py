"""Author arithmetic check for aq-05177 sketches i01 and i02 (inputs as printed, $ millions)."""

# i01: Q4 2023 cash interest net of swap settlements and interest earned on cash.
fy_2023 = 38.3          # D04 L158 "net cash interest expense was $38.3 million in 2023"
nine_months_2023 = 41.7  # D03 L171 "$41.7 million for the first nine months of 2023"
q1_23, q2_23, q3_23 = 17.5, 12.4, 11.7  # D05 L127, D06 L134 (and D02 L122), D07 L136 (and D03 L171)
q4_gross_paid = 5.6     # D04 L141, excludes swap flows, not net of interest income (lure)

route_a = fy_2023 - nine_months_2023
route_b = fy_2023 - (q1_23 + q2_23 + q3_23)
# Rounding bounds: every printed input is +/- 0.05.
lo = (fy_2023 - 0.05) - (nine_months_2023 + 0.05)
hi = (fy_2023 + 0.05) - (nine_months_2023 - 0.05)
print(f"i01 route A FY - 9M          = {route_a:.2f}")
print(f"i01 route B FY - (Q1+Q2+Q3)   = {route_b:.2f}")
print(f"i01 route A bounds            = [{lo:.2f}, {hi:.2f}] -> nearest million {round(route_a)}")
print(f"i01 lure (printed Q4 paid)    = {q4_gross_paid} -> nearest million {round(q4_gross_paid)}")

# i02: growth implied by the bottom of the first 2024 IC revenue range, same-business 2023 base.
aug_range = (1685.0, 1735.0)  # D06 L149 "$1.685,000,000 to $1,735,000,000" after +10 both ends
aug_step, may_step = 10.0, 25.0  # D06 L149; D05 L138
first_range = (aug_range[0] - aug_step - may_step, aug_range[1] - aug_step - may_step)
ic_2023 = 1604.0   # D04 L143-144 "$1.604 billion"
erad_2023 = 37.1   # D04 L169 "$37.1 million of revenue"
base = ic_2023 - erad_2023
growth_low = first_range[0] / base - 1
growth_top = first_range[1] / base - 1
print(f"\ni02 first range               = {first_range}")
print(f"i02 same-business 2023 base   = {base:.1f}")
print(f"i02 growth at bottom          = {growth_low*100:.3f}%")
print(f"i02 growth at top (check 8.5) = {growth_top*100:.3f}%")
# Quarter-sum base: 388.4 (D01) + 401.3 (D02) + 399.1 (D03) + 415.3 (D04) = 1,604.1
qsum = 388.4 + 401.3 + 399.1 + 415.3
print(f"i02 quarter-sum base          = {qsum - erad_2023:.1f} -> {(first_range[0]/(qsum-erad_2023)-1)*100:.3f}%")
# Base backed out of the printed 8.5% top
print(f"i02 base from 8.5% top        = {first_range[1]/1.085:.1f} -> {(first_range[0]/(first_range[1]/1.085)-1)*100:.3f}%")
# Bounds: 1.604B is +/- 0.5, 37.1 +/- 0.05
for b in (1603.5 - 37.15, 1604.5 - 37.05):
    print(f"i02 bound base {b:.2f} -> {(first_range[0]/b-1)*100:.3f}%")
# Lures
print("\ni02 lures:")
print(f"  analyst 8% to 8.5% (D04 L475)        -> 8.0%")
print(f"  as-reported base 1,604               -> {(first_range[0]/ic_2023-1)*100:.2f}%")
print(f"  May raise missed (1,675 / base)      -> {((aug_range[0]-aug_step)/base-1)*100:.2f}%")
print(f"  May raise missed, as-reported base   -> {((aug_range[0]-aug_step)/ic_2023-1)*100:.2f}%")
print(f"  August range taken as first (1,685)  -> {(aug_range[0]/base-1)*100:.2f}%")
print(f"  D03 $50M on $1.6B                    -> {50/1600*100:.2f}%")
