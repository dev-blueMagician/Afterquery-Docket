"""Author arithmetic check for the buyback hooks (aq-06634). Reads text/ and recomputes."""
from decimal import Decimal as D
import pathlib, re

T = {n: pathlib.Path(f"text/{n}.txt").read_text(encoding="utf-8") for n in ["D01","D02","D03","D04","D05","D06"]}

def pos(doc, s):
    i = T[doc].find(s)
    assert i >= 0, (doc, s)
    return i

quotes = {
 "D04 Sep row": ("D04", "|September 1, 2025 - September 30, 2025|$—|$—|$—|$135.9|"),
 "D04 Oct row": ("D04", "|October 1, 2025 - October 31, 2025|1.0|122.54|126.5|$9.4|"),
 "D04 Q2 total": ("D04", "|Total for the period|1.0|$122.54|$126.5|$9.4|"),
 "D06 Dec row": ("D06", "|December 1, 2025 - December 31, 2025|$—|$—|$—|$9.4|"),
 "D06 Jan row": ("D06", "|January 1, 2026 - January 31, 2026|0.5|102.59|50.0|$950.0|"),
 "D06 Feb row": ("D06", "|February 1, 2026 - February 28, 2026|0.3|92.65|25.0|$925.0|"),
 "D06 Q3 total": ("D06", "|Total for the period|0.8|$99.05|$75.0|$925.0|"),
 "D06 expiry": ("D06", "at which time $9.4 million of unused repurchase authorization expired"),
 "D02 Jun row": ("D02", "|June 1, 2026 - June 30, 2026|—|$—|$—|$675.6|"),
 "D02 Q1 total": ("D02", "|Total for the period|—|$—|$—|$675.6|"),
 "D02 new program": ("D02", "On January 16, 2026, the Company's Board approved a program to repurchase up to an additional $1.0 billion of its common stock with no expiration date"),
 "D02 cash flow": ("D02", "|Repurchases of common shares|—|(160.1)|"),
 "D01 cash flow": ("D01", "|Repurchases of common shares|—|(160.1)|"),
 "D03 six months": ("D03", "Repurchased 2.1 million shares of our common stock for $286.6 million."),
 "D05 nine months": ("D05", "Repurchased 2.9 million shares of our common stock for $361.6 million."),
 "D06 nine months cf": ("D06", "|Repurchases of common shares|(361.6)|(104.5)|"),
 "D04 six months cf": ("D04", "|Repurchases of common shares|(286.6)|(104.5)|"),
}
for k,(d,s) in quotes.items():
    print(f"{k:20s} {d} char {pos(d,s):>7,d} of {len(T[d]):,d}")

q1_26 = D("160.1"); q2 = D("126.5"); q3 = D("75.0")
rem_feb = D("925.0"); rem_may = D("675.6"); q1_27 = D("0")
q4 = rem_feb - rem_may
print("Q4 FY26 =", q4)
assert D("286.6") - q1_26 == q2 and D("361.6") - D("286.6") == q3
# authorization route: old program after Aug 31 2025 = 135.9 - 9.4 expired; new = 1000 - 675.6
old_after_aug = D("135.9") - D("9.4"); new_used = D("1000.0") - rem_may
print("old program used Sep 2025-Jan 16 2026 =", old_after_aug, "; new program used to Aug 31 2026 =", new_used)
assert D("1000.0") - D("50.0") == D("950.0") and D("950.0") - D("25.0") == rem_feb
ttm = q2 + q3 + q4 + q1_27
assert ttm == old_after_aug + new_used
fy26 = q1_26 + q2 + q3 + q4
assert fy26 == D("361.6") + q4 == D("286.6") + new_used
print("TTM to Aug 31 2026 =", ttm, "| FY2026 =", fy26, "| max quarter FY26 =", max(q1_26,q2,q3,q4))
print("lures: omit Q4 ->", q2+q3+q1_27, "| FY26 instead of TTM ->", fy26,
      "| new-program total as Q4 ->", q2+q3+new_used, "| forget 9.4 expiry ->", D("135.9")+new_used,
      "| nine months + new program ->", D("361.6")+new_used, "| old life + new ->", D("400.0")-D("9.4")+new_used)
