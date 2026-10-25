#!/usr/bin/env python3
"""Rent vs buy: net-worth comparison for every property with a known total.

Buy scenario: $250,000 down, 4.75% nominal compounded semi-annually,
25-year amortization. Monthly ownership costs from research/ownership_costs.py
(mortgage + strata + tax/12 + maintenance + insurance + utilities), minus
50% of modelled gross rent at the midpoint of the modelled range where a
suite exists; the non-mortgage parts grow at RENT_GROWTH per year, the
mortgage payment is fixed.
Home value grows at APPRECIATION per year. At the horizon the owner sells:
net worth = 0.95 * home value - remaining mortgage balance (5% selling costs),
plus any months where rent exceeded owning costs, invested instead.

Rent scenario: keep the $250,000 invested at INVEST_RETURN, rent an apartment
at $2,700/month growing at RENT_GROWTH per year, and invest each month's
surplus (owning total - rent) when owning costs more. Net worth = invested
down payment + invested monthly surpluses.

Both scenarios invest at the same return and face the same rent growth, so
the comparison isolates the buy-vs-rent structure, not a return forecast.
Breakeven appreciation is the annual home-price growth at which buying
equals renting over 5 years (bisection; reported as >10% or <0% outside
the search range).

Excluded and noted in the write-up: property transfer tax and closing
costs (buyer only), renter's insurance, tax treatment of investments
and rental income, and any change in rent if the household moves.

Run: python3 research/rent_vs_buy.py
Writes research/rent-vs-buy.json for the site payload.
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mortgage_scenarios import monthly_payment
from ownership_costs import ownership_cost_plan

ROOT = Path(__file__).resolve().parent
RENT_MONTHLY = 2700.0
APPRECIATION = 0.02
INVEST_RETURN = 0.05
RENT_GROWTH = 0.02
SELLING_COST = 0.05
HORIZONS = (5, 10)


def monthly_rate(nominal):
    return (1 + nominal / 2) ** (1 / 6) - 1


def mortgage_balance(principal, nominal, years, months_paid):
    r = monthly_rate(nominal)
    pay = monthly_payment(principal, nominal, years)
    n = years * 12
    if months_paid >= n:
        return 0.0
    return principal * (1 + r) ** months_paid - pay * (((1 + r) ** months_paid - 1) / r)


def simulate(p, assumptions, estimates, years, appreciation):
    """Return (buy_net_worth, rent_net_worth) at `years`."""
    months = years * 12
    price = p["asking_price"]
    principal = price - assumptions["down_payment"]
    pay = monthly_payment(principal, assumptions["annual_rate"],
                          assumptions["amortization_years"])
    cost = ownership_cost_plan(p, assumptions, estimates)
    # Owning total after the 50% rent offset, at the midpoint of the modelled
    # range (for homes without rent, low == high == base). The net
    # non-mortgage part (costs minus rent offset) grows at RENT_GROWTH.
    own_base = (cost["low"] + cost["high"]) / 2
    non_mortgage = own_base - cost["mortgage"]
    rent = RENT_MONTHLY
    invest_monthly = INVEST_RETURN / 12
    buy_invested = 0.0
    rent_invested = assumptions["down_payment"]
    for m in range(months):
        year = m // 12
        growth = (1 + RENT_GROWTH) ** year
        own_total = pay + non_mortgage * growth
        rent_m = rent * growth
        if own_total > rent_m:
            rent_invested = rent_invested * (1 + invest_monthly) + (own_total - rent_m)
            buy_invested = buy_invested * (1 + invest_monthly)
        else:
            buy_invested = buy_invested * (1 + invest_monthly) + (rent_m - own_total)
            rent_invested = rent_invested * (1 + invest_monthly)
    home_value = price * (1 + appreciation) ** years
    balance = mortgage_balance(principal, assumptions["annual_rate"],
                               assumptions["amortization_years"], months)
    buy = home_value * (1 - SELLING_COST) - balance + buy_invested
    return round(buy), round(rent_invested)


def breakeven_appreciation(p, assumptions, estimates, years=5):
    """Annual appreciation at which buying equals renting over `years`."""
    def gap(app):
        buy, rent = simulate(p, assumptions, estimates, years, app)
        return buy - rent
    lo, hi = -0.05, 0.10
    if gap(lo) >= 0:
        return "<0%"
    if gap(hi) <= 0:
        return ">10%"
    for _ in range(40):
        mid = (lo + hi) / 2
        if gap(mid) >= 0:
            hi = mid
        else:
            lo = mid
    return f"{(lo + hi) / 2 * 100:.1f}%"


def main():
    sample = json.load(open(ROOT / "property-sample.json"))
    estimates = json.load(open(ROOT / "cost-estimates.json"))
    a = sample["assumptions"]
    out = {
        "rent_monthly": RENT_MONTHLY,
        "appreciation": APPRECIATION,
        "invest_return": INVEST_RETURN,
        "rent_growth": RENT_GROWTH,
        "selling_cost": SELLING_COST,
        "down_payment": a["down_payment"],
        "annual_rate": a["annual_rate"],
        "amortization_years": a["amortization_years"],
        "computed_on": sample["observed_on"],
        "properties": {},
    }
    rows = []
    for p in sample["properties"]:
        cost = ownership_cost_plan(p, a, estimates)
        if cost["base"] is None:
            out["properties"][p["id"]] = {"total_monthly": None}
            continue
        entry = {"total_monthly": round((cost["low"] + cost["high"]) / 2)}
        for years in HORIZONS:
            buy, rent = simulate(p, a, estimates, years, APPRECIATION)
            entry[f"buy_{years}yr"] = buy
            entry[f"rent_{years}yr"] = rent
            entry[f"diff_{years}yr"] = buy - rent
        entry["breakeven_5yr"] = breakeven_appreciation(p, a, estimates, 5)
        out["properties"][p["id"]] = entry
        rows.append((p, entry))
    with open(ROOT / "rent-vs-buy.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{'ID':4} {'total/mo':>9} {'5yr buy':>9} {'5yr rent':>9} {'5yr diff':>9} {'10yr diff':>10}  breakeven")
    for p, e in rows:
        print(f"{p['id']:4} ${e['total_monthly']:>8,} ${e['buy_5yr']:>8,} ${e['rent_5yr']:>8,} "
              f"${e['diff_5yr']:>+8,} ${e['diff_10yr']:>+9,}  {e['breakeven_5yr']}")
    missing = [p["id"] for p in sample["properties"]
               if out["properties"][p["id"]]["total_monthly"] is None]
    print(f"\nNo comparison (strata or tax unknown): {', '.join(missing)}")
    print("Wrote research/rent-vs-buy.json")


if __name__ == "__main__":
    main()
