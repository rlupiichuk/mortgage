"""Regenerate the sample CSV and cost comparison from property-sample.json.

Run: python3 research/build_property_comparison.py
Standard library only. No live data retrieval. Null costs remain unknown.
"""

import csv
import json
from pathlib import Path
from urllib.parse import urlencode

from mortgage_scenarios import monthly_payment
from ownership_costs import ownership_cost_plan

ROOT = Path(__file__).resolve().parent


def money(value):
    return "unknown" if value is None else f"${value:,.0f}"


def build():
    data = json.loads((ROOT / "property-sample.json").read_text())
    a = data["assumptions"]
    catchments = json.loads((ROOT / "school-catchments.json").read_text())
    estimates = json.loads((ROOT / "cost-estimates.json").read_text())
    fit = json.loads((ROOT / "property-fit.json").read_text())
    rows = []
    summary = [
        "# First property sample: cost comparison",
        "",
        f"Observed {data['observed_on']}. Asking-price research examples, not confirmed available homes or recommendations.",
        "",
        "$250,000 down; 4.75% nominal interest compounded semi-annually; 25-year amortization. No lender approval implied. New-home GST and any rebates are excluded until verified.",
        "",
        "The known-cost subtotal includes mortgage, advertised strata fees and advertised tax/12 ONLY where both are available. It excludes insurance, utilities, owner maintenance, special levies and rental tax. Historical tax years and advertised strata fees need refreshing. Unknown is not zero.",
        "",
        "After-rent figures count 75% of exploratory asking rent; this allowance is not an itemized expense/tax model. They cover mortgage only. No rent is counted for unfinished, merely potential or wet-bar configurations.",
        "",
        "The HTML total-expense column and CSV total_expenses fields use the broader ownership model: mortgage + property tax + strata + maintenance + insurance + utilities, minus 50% of modelled gross rent. Missing inputs use a labelled matched-advertisement mean from cost-estimates.json where available. The older mortgage-only sensitivity table below retains its separate 75% rent allowance.",
        "",
        "| ID | Address | Asking | Mortgage/month | Strata/month | Tax/year | Known-cost subtotal/month | Mortgage after rental allowance |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for p in data["properties"]:
        principal = p["asking_price"] - a["down_payment"]
        payment = monthly_payment(principal, a["annual_rate"], a["amortization_years"])
        known = None
        if p["strata_monthly"] is not None and p["annual_tax"] is not None:
            known = payment + p["strata_monthly"] + p["annual_tax"] / 12
        rent = p["rent_model"]
        after_low = after_high = None
        if rent:
            after_low = payment - a["rent_counted_fraction"] * rent["high"]
            after_high = payment - a["rent_counted_fraction"] * rent["low"]
        required = max(0, payment - a["personal_mortgage_target"]) / a["rent_counted_fraction"]
        row = {k: (json.dumps(v, ensure_ascii=False) if isinstance(v, dict) else v) for k, v in p.items()}
        cost = ownership_cost_plan(p, a, estimates)
        row["overall_fit_score"] = fit["properties"][p["id"]]["score"]
        row["overall_fit_assessment"] = json.dumps(fit["properties"][p["id"]], ensure_ascii=False)
        row["ownership_cost_plan"] = json.dumps(cost, ensure_ascii=False)
        row["total_expenses_after_rent_low"] = None if cost["low"] is None else round(cost["low"])
        row["total_expenses_after_rent_high"] = None if cost["high"] is None else round(cost["high"])
        row["drive_range_minutes"] = json.dumps(p["commute"]["drive_range_minutes"])
        row["transit_range_minutes"] = json.dumps(p["commute"]["transit_range_minutes"])
        row.update(observed_on=data["observed_on"], mortgage_monthly=round(payment),
                   known_cost_subtotal_monthly=None if known is None else round(known),
                   required_gross_rent=round(required),
                   mortgage_after_rent_low=None if after_low is None else round(after_low),
                   mortgage_after_rent_high=None if after_high is None else round(after_high))
        rows.append(row)
        row["map_url"] = "https://www.google.com/maps/search/?" + urlencode({"api": "1", "query": f"{p['address']}, {p['city']}, BC, Canada"})
        assignment = catchments["properties"][p["id"]]
        row["school_catchment_status"] = assignment["status"]
        row["school_pathway"] = " → ".join(catchments["schools"][key]["name"] for key in assignment["current"])
        row["school_urls"] = " | ".join(catchments["schools"][key]["url"] for key in assignment["current"])
        row["future_school_pathway"] = " → ".join(catchments["schools"][key]["name"] for key in assignment["future"])
        row["school_catchment_evidence"] = json.dumps(assignment, ensure_ascii=False)
        for level in ("elementary", "middle", "secondary"):
            selected = [catchments["schools"][key] for key in assignment["current"] if catchments["schools"][key]["level"] == level]
            row[f"{level}_school"] = " | ".join(s["name"] for s in selected)
            row[f"{level}_school_url"] = " | ".join(s["url"] for s in selected)
        row["drive_to_downtown_minutes"] = p["commute"]["drive_minutes"]
        row["transit_to_downtown_minutes"] = p["commute"]["transit_door_to_door_minutes"]
        row["downtown_reference"] = p["commute"]["downtown_reference"]
        after = "not modelled" if rent is None else f"{money(after_low)}–{money(after_high)}"
        summary.append(f"| {p['id']} | [{p['address']}]({row['map_url']}) | {money(p['asking_price'])} | {money(payment)} | {money(p['strata_monthly'])} | {money(p['annual_tax'])} | {money(known)} | {after} |")
    summary.extend([
        "", "## Mortgage sensitivity", "",
        "| Purchase price | 4.75%, 25 years | 5.75%, 25 years | 4.75%, 30 years |",
        "|---|---:|---:|---:|",
    ])
    for price in (800000, 850000, 1100000, 1200000):
        principal = price - a["down_payment"]
        values = [monthly_payment(principal, rate, years) for rate, years in ((.0475,25),(.0575,25),(.0475,30))]
        summary.append(f"| {money(price)} | " + " | ".join(money(v) for v in values) + " |")
    summary.extend(["", "The 30-year illustration does not establish lender eligibility or equal pricing. A longer amortization reduces monthly payments but increases interest at an unchanged rate over the full repayment period.", "", "For sources, availability caveats, suite classifications, tax years and next checks, use [the sample data](property-sample.json) and [screening notes](property-sample-notes.md).", ""])
    with (ROOT / "property-comparison.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / "property-cost-comparison.md").write_text("\n".join(summary))
    print(f"Generated comparison for {len(rows)} properties.")


if __name__ == "__main__":
    build()
