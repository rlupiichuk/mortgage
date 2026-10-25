"""Build the standalone root HTML report from local research artifacts.

Run: python3 research/build_summary.py
No network calls or dependencies. Updates the compiled HTML, not historical data.
"""

import csv
import html
import json
from pathlib import Path

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
    criteria = []
    for line in (ROOT / "criteria.md").read_text().splitlines():
        if line.startswith("| ") and not line.startswith("| Item"):
            cells = [v.strip() for v in line.strip("|").split("|")]
            if len(cells) == 2:
                criteria.append({"label": cells[0], "value": cells[1]})
    payload = {"sample": sample, "trends": trends, "criteria": criteria}
    template = (ROOT / "summary.template.html").read_text()
    # Escape HTML-sensitive characters so source text cannot close the JSON script.
    encoded = json.dumps(payload, ensure_ascii=False).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    fallback = "".join(f"<tr><td>{html.escape(p['address'])}</td><td>{html.escape(p['city'])}</td><td>${p['asking_price']:,}</td><td><a href='{html.escape(p['source'], quote=True)}'>Listing source</a></td></tr>" for p in sample["properties"])
    output = template.replace("__REPORT_DATA__", encoded).replace("__FALLBACK_ROWS__", fallback)
    (ROOT.parent / "index.html").write_text(output)
    seed_history(sample)
    print(f"Built index.html with {len(sample['properties'])} properties and {len(trends['benchmark_prices'])} price observations.")


if __name__ == "__main__":
    build()
