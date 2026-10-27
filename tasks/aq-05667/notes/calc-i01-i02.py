"""Author arithmetic check for sketches i01 and i02 (aq-05667). Inputs are the printed figures,
read back from text/ so a transcription slip shows up as an assertion failure."""
from decimal import Decimal as D
from pathlib import Path

TEXT = Path(__file__).resolve().parent.parent / "text"


def has(doc: str, snippet: str) -> None:
    body = (TEXT / f"{doc}.txt").read_text(encoding="utf-8")
    assert snippet in body, (doc, snippet)


# i01: 2025 interest expense, anticipated in the 2024 10-K (Doc 3 = D01) vs actual (Doc 7 = D02).
has("D01", "Interest expense is expected to increase by approximately $40 million in 2025")
has("D01", "approximately $20 million of Interest expense")
has("D02", "Interest expense | 465.0 1.9 % 415.7 1.8 %")
has("D02", "Interest expense increased $49.3 million in 2025 compared to 2024")
refinancing, hq_interest = D("40"), D("20")
anticipated = refinancing + hq_interest
actual = D("465.0") - D("415.7")
assert actual == D("49.3")
print("i01 anticipated total:", anticipated, "| actual:", actual)
print("i01 gold, actual minus anticipated:", actual - anticipated)          # -10.7
print("i01 lure, against the $40M sentence only:", actual - refinancing)    # +9.3

# i02: cash from selling HQ buildings and leasing them back, 2022-2025.
has("D01", "proceeds of $47.2 million were received")
has("D01", "Proceeds received $ | 244.2 $ | 305.0 $ | 210.0")
has("D02", "Proceeds received $ | 40.9 $ | 244.2")
has("D02", "for a total of $800 million")
new_hq_table = D("210.0") + D("305.0") + D("244.2") + D("40.9")
old_hq = D("47.2")
print("i02 new HQ proceeds by table:", new_hq_table, "| stated total: 800")
print("i02 gold:", new_hq_table + old_hq, "/", D("800") + old_hq, "-> nearest million 847")
print("i02 lure, new HQ only: 800")
