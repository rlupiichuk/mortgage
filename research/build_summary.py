"""Build the standalone root HTML report from local research artifacts.

Run: python3 research/build_summary.py
No network calls or dependencies. Updates the compiled HTML, not historical data.
"""

from ownership_costs import ownership_cost_plan

import csv
import html
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent


def seed_history(sample):
    """Create initial history once; subsequent builds never replace observations."""
    path = ROOT / "listing-observations.csv"
    if not path.exists():
        with path.open("w", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["observed_on", "property_id", "mls", "address", "asking_price", "status_notes", "source"])
            for p in sample["properties"]:
                writer.writerow([sample["observed_on"], p["id"], p["mls"], p["address"], p["asking_price"], p["status"], p["source"]])
    path = ROOT / "rent-observations.csv"
    if not path.exists():
        with path.open("w", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["observed_on", "rent_id", "address", "bedrooms", "asking_rent", "confidence_notes", "source"])
            for r in sample["rent_observations"]:
                writer.writerow([sample["observed_on"], r["id"], r["address"], r["bedrooms"], r["asking_rent"], r["confidence"], r["source"]])


def build():
    sample = json.loads((ROOT / "property-sample.json").read_text())
    trends = json.loads((ROOT / "trends.json").read_text())
    catchments = json.loads((ROOT / "school-catchments.json").read_text())
    ratings = json.loads((ROOT / "school-ratings.json").read_text())
    context = json.loads((ROOT / "area-context.json").read_text())
    fit = json.loads((ROOT / "property-fit.json").read_text())
    estimates = json.loads((ROOT / "cost-estimates.json").read_text())
    school_notes = [
        "# Property school catchment research", "", f"Researched {catchments['researched_on']}.", "", catchments["method"], "",
        "Current means the proposed neighbourhood pathway for the current research year. Labels below retain their evidence status. No assignment is a district-confirmed address lookup or a guarantee of enrolment, capacity, safety or academic quality.", "",
        "| Property | Current school leads | Future change | Evidence status | Nearest fallback (not catchment) |", "|---|---|---|---|---|",
    ]
    for p in sample["properties"]:
        p["map_url"] = "https://www.google.com/maps/search/?" + urlencode({"api": "1", "query": f"{p['address']}, {p['city']}, BC, Canada"})
        origin = f"{p['address']}, {p['city']}, BC, Canada"
        p["drive_directions_url"] = "https://www.google.com/maps/dir/?" + urlencode({"api": "1", "origin": origin, "destination": "Waterfront Station, Vancouver, BC, Canada", "travelmode": "driving"})
        p["transit_directions_url"] = "https://www.google.com/maps/dir/?" + urlencode({"api": "1", "origin": origin, "destination": "Waterfront Station, Vancouver, BC, Canada", "travelmode": "transit"})
        p["fit_assessment"] = fit["properties"][p["id"]]
        p["ownership_cost_plan"] = ownership_cost_plan(p, sample["assumptions"], estimates)
        p["school_catchment"] = catchments["properties"][p["id"]]
        c = p["school_catchment"]
        def school_path(keys):
            return " → ".join(f"[{catchments['schools'][key]['name']}]({catchments['schools'][key]['url']})" for key in keys) or "Unresolved"
        school_notes.append(f"| [{p['address']}]({p['map_url']}) | {school_path(c['current'])} | {school_path(c['future']) if c['future'] else 'None established'} | {c['status']} | {school_path([n['school'] for n in c['nearest_fallback'].values()]) if c['nearest_fallback'] else 'Not needed'} |")
    school_notes.extend(["", "## Evidence and unresolved issues", ""])
    for p in sample["properties"]:
        c = p["school_catchment"]
        school_notes.extend([f"### {p['id']} — {p['address']}", "", c["notes"], "", f"[Official district locator/guidance]({c['locator_url']}). " + " · ".join(f"[{source['label']}]({source['url']})" for source in c["sources"]), ""])
    (ROOT / "school-catchments.md").write_text("\n".join(school_notes))
    criteria = []
    for line in (ROOT / "criteria.md").read_text().splitlines():
        if line.startswith("| ") and not line.startswith("| Item"):
            cells = [v.strip() for v in line.strip("|").split("|")]
            if len(cells) == 2:
                criteria.append({"label": cells[0], "value": cells[1]})
    payload = {"sample": sample, "trends": trends, "criteria": criteria, "catchments": catchments, "ratings": ratings, "context": context, "fit": fit}
    template = (ROOT / "summary.template.html").read_text()
    # Escape HTML-sensitive characters so source text cannot close the JSON script.
    encoded = json.dumps(payload, ensure_ascii=False).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    fallback = "".join(f"<tr><td><a href='{html.escape(p['map_url'], quote=True)}'>{html.escape(p['address'])}</a></td><td>{html.escape(p['city'])}</td><td>${p['asking_price']:,}</td><td><a href='{html.escape(p['source'], quote=True)}'>Listing source</a></td></tr>" for p in sample["properties"])
    output = template.replace("__REPORT_DATA__", encoded).replace("__FALLBACK_ROWS__", fallback)
    (ROOT.parent / "index.html").write_text(output)
    seed_history(sample)
    print(f"Built index.html with {len(sample['properties'])} properties and {len(trends['benchmark_prices'])} price observations.")


if __name__ == "__main__":
    build()
