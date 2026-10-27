"""Author arithmetic check for round-2 sketches i03 (leverage) and i04 (stores), aq-05667."""
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path

TEXT = Path(__file__).resolve().parent.parent / "text"


def has(doc: str, snippet: str) -> None:
    assert snippet in (TEXT / f"{doc}.txt").read_text(encoding="utf-8"), (doc, snippet)


def r2(x: D) -> D:
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


# i03: Doc 7 = D02 (definition, FY2025 EBITDA), Doc 8 = D08 (Q1 2026 and Q1 2025 EBITDA, debt, cash).
has("D02", "The Company targets Net debt, which is total debt outstanding, net of Cash and cash equivalents, to be 2.0 to 2.5 times EBITDA")
has("D02", "EBITDA |\t4,480.1\t4,491.5")
has("D02", "Adjusted EBITDA $ | 4,608.9 $ | 4,491.5")
has("D08", "EBITDA $ | 998.2 $ | 917.7")
has("D08", "Adjusted EBITDA $ | 998.2 $ | 937.0")
has("D08", "Total debt, net of Cash and cash equivalents, was $11.483 billion")
has("D08", "Total debt outstanding $ | 11,699.8")
has("D08", "Cash and cash equivalents of $216.9 million")
ttm = D("4480.1") - D("917.7") + D("998.2")
ttm_adj = D("4608.9") - D("937.0") + D("998.2")
net = D("11699.8") - D("216.9")
print("i03 TTM EBITDA", ttm, "| net debt", net, "(printed 11.483B)")
print("i03 gold net/TTM:", r2(net / ttm), "| with printed 11,483:", r2(D("11483") / ttm))
print("i03 lures: gross/TTM", r2(D("11699.8") / ttm), "| net/TTM adjusted", r2(net / ttm_adj),
      "| net/FY2025", r2(net / D("4480.1")), "| gross/FY2025", r2(D("11699.8") / D("4480.1")))
print("i03 check Doc 7's own 2.4x: 10,664/4,480.1 =", r2(D("10664") / D("4480.1")))

# i04: Doc 3 = D01 (2024 changes, end-2024 counts), Doc 7 = D02 (2025 changes, end-2025 counts).
has("D01", "opened 84 new stores and closed 5 locations for a net increase of 79 stores")
has("D01", "The total number of stores in operation at December 31, 2024 was 4,773")
has("D01", "opened 18 new stores and closed 2 locations for a net increase of 16 new stores")
has("D01", "The total number of stores in operation at December 31, 2024 was 334 in Latin America")
has("D02", "The total number of stores in operation at December 31, 2025 was 4,853")
has("D02", "The total number of stores in operation at December 31, 2025 was 307 in the Latin America region")
psg23, cbg23 = 4773 - 79, 334 - 16
print("i04 end-2023: PSG", psg23, "CBG", cbg23, "total", psg23 + cbg23)
print("i04 end-2025 total", 4853 + 307)
print("i04 gold change:", (4853 + 307) - (psg23 + cbg23), "| lure PSG only:", 4853 - psg23,
      "| gross openings all:", 84 + 18 + 83 + 13, "| PSG gross:", 84 + 83)
