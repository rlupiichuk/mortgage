#!/usr/bin/env python3
"""Compute a market-fit estimate for every property in the sample and
write it into research/property-fit.json.

Method (see research/property-fit.md for the full write-up):
- For each property, compare its asking $/sqft with the median asking
  $/sqft of comparable homes in this sample: same city + same strategy
  when that group has at least 3 homes, otherwise the same strategy
  across all cities when that group has at least 3. Groups smaller
  than 3 get no estimate (null) — a median of one or two is not a
  market signal.
- Tier: more than 10% below the median -> "Below comparable asking
  prices"; within +/-10% -> "In line with comparable asking prices";
  more than 10% above -> "Above comparable asking prices".
- This compares asking prices with asking prices inside this sample.
  It is NOT a valuation: $/sqft ignores age, condition, lot, layout
  and renovations, and it runs lower for larger homes. Sold prices
  would be needed for a real market check.

Re-run after any sample change (additions, removals, price changes)
before rebuilding the site and spreadsheet.
"""
import json
import statistics
from collections import defaultdict

ROOT = "/home/hatch/workspace/mortgage/research"

# Extra evidence verified Oct 25, 2026 (days on market, price changes,
# third-party estimates). Appended to the auto-generated note.
EVIDENCE = {
    "P27": "Price change Sep 25, 2026: -$10,000.",
    "P29": "59 days on market.",
    "P36": ("46 days on market; price cut $80,000 on Oct 13, 2026. Zolo "
            "home-value estimate $691,753 vs $699,900 asking (-1.2%)."),
    "P37": "Listed Oct 23, 2026 (fresh listing).",
    "P39": "88 days on market; price cut $20,000 on Sep 21, 2026.",
    "P40": "15 days on market.",
    "P42": "BC Assessment 2026 total $1,169,000 vs $1,198,888 asking (+2.6%).",
    "P43": "55 days on market.",
}


def psf(p):
    return p["asking_price"] / p["interior_sqft"]


def main():
    with open(f"{ROOT}/property-sample.json", encoding="utf-8") as f:
        sample = json.load(f)["properties"]
    with open(f"{ROOT}/property-fit.json", encoding="utf-8") as f:
        fit = json.load(f)

    by_city_strategy = defaultdict(list)
    by_strategy = defaultdict(list)
    for p in sample:
        by_city_strategy[(p["city"], p["strategy"])].append(p)
        by_strategy[p["strategy"]].append(p)

    for p in sample:
        entry = fit["properties"][p["id"]]
        group = by_city_strategy[(p["city"], p["strategy"])]
        if len(group) >= 3:
            basis = f"{p['city']} {p['strategy'].lower()}s"
            n = len(group)
            median = statistics.median([psf(x) for x in group])
        elif len(by_strategy[p["strategy"]]) >= 3:
            group = by_strategy[p["strategy"]]
            basis = f"{p['strategy'].lower()}s, all cities"
            n = len(group)
            median = statistics.median([psf(x) for x in group])
        else:
            entry["market_fit_pct"] = None
            entry["market_fit_tier"] = None
            entry["market_fit_basis"] = None
            entry["market_fit_note"] = (
                "Too few comparable asking prices in this sample to judge "
                "market fit.")
            continue

        pct = round(100 * (psf(p) / median - 1), 1)
        if pct <= -10:
            tier = "Below comparable asking prices"
        elif pct >= 10:
            tier = "Above comparable asking prices"
        else:
            tier = "In line with comparable asking prices"
        note = (f"Asking ${psf(p):.0f}/sqft vs ${median:.0f}/sqft median for "
                f"{basis} (n={n}, {pct:+.1f}%).")
        if p["id"] in EVIDENCE:
            note += " " + EVIDENCE[p["id"]]
        entry["market_fit_pct"] = pct
        entry["market_fit_tier"] = tier
        entry["market_fit_basis"] = f"{basis} (n={n})"
        entry["market_fit_note"] = note

    with open(f"{ROOT}/property-fit.json", "w", encoding="utf-8") as f:
        json.dump(fit, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"{'ID':4} {'$/sqft':>7} {'pct':>7}  tier")
    for p in sample:
        e = fit["properties"][p["id"]]
        pct = "" if e["market_fit_pct"] is None else f"{e['market_fit_pct']:+.1f}%"
        print(f"{p['id']:4} ${psf(p):6.0f} {pct:>7}  {e['market_fit_tier']}")


if __name__ == "__main__":
    main()
