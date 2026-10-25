# Greater Vancouver home purchase research

Last updated: 2026-10-25. All amounts CAD.

This is a living decision record for exploring whether, where, and how to buy a family home. No purchase strategy, neighbourhood, lender, or school has been selected.

## Start here

- [Open the property workbench](index.html): property-first comparison table with expandable rows, map/listing links, linked school pathways, route links, charts and a budget calculator. Opens locally without a server.
- [Household criteria](research/criteria.md): confirmed preferences and unresolved questions.
- [Viewing checklist](research/viewing-checklist.md): what to check before, during and after a viewing, for a family with a six-year-old.
- [Purchase strategies and budget](research/strategies-and-budget.md): comparable scenarios and calculation assumptions.
- [Strategies from discussions and interviews](research/community-strategies.md): alternative paths, lived experiences, source caveats, and household fit.
- [Location shortlist](research/locations.csv): places to investigate, not recommendations or safety rankings.
- [First property sample](research/property-sample-notes.md): 45 examples, screening decisions and outstanding checks.
- [Property cost comparison](research/property-cost-comparison.md) and [spreadsheet](research/property-comparison.csv): reproducible costs with sources and uncertainty.
- [Initial school/transit screening](research/school-and-transit-screen.md): address-specific leads and verification gaps.
- [School catchment research](research/school-catchments.md) and [structured school records](research/school-catchments.json): linked schools, evidence status, conflicts and future changes for the 45 examples.
- [Trends tracker](research/trends.md) and [historical observations](research/trends.json): initial price/inventory history, sources, coverage gaps and refresh method.
- [Evidence register](research/sources.md): source links, dates, scope, and verification gaps.
- [Research log and next steps](research/research-log.md): decisions, changes, and future work.
- [Mortgage calculator](research/mortgage_scenarios.py): regenerate illustrative payment scenarios locally.

## Updating this research

1. Date each update and record changes in the research log.
2. Keep user-confirmed requirements separate from estimates and recommendations.
3. Recheck rates, listings, comparable rents, school catchments/capacity, transit schedules, and applicable rules before relying on them.
4. Record source, observation date, and limitations for every material finding. An asking price is not a sale price; advertised rent is not achieved rent.
5. Evaluate school safety and academics separately. Do not infer school quality or safety from municipal reputation, demographics, or house prices.
6. Compare total ownership costs, mortgage qualification, and household cash flow separately. Do not treat a lender maximum as a spending target.

Personal financial details are stored in this folder and its Git history. The repo is public (since 2026-10-25) and the workbench is published as a GitHub Pages site at https://rlupiichuk.github.io/mortgage/.

Save meaningful research and report updates in periodic Git commits, as requested by the user. Review the staged changes before committing; exclude caches and temporary files. Remote publication or pushing is not part of this instruction.

## Rebuild the summaries

After editing the property sample or school records, run `python3 research/build_property_comparison.py` to regenerate the spreadsheet and cost table. Run `python3 research/build_summary.py` to compile `index.html` and the school research summary from the property sample, school records, criteria, trend data and HTML template. These scripts do not fetch live data. They preserve existing listing/rent observation logs; append new dated observations rather than replacing history.

The HTML includes a compiled interpretation as well as data-driven charts: review its narrative and date labels when updating the research. It has no external scripts or analytics; it is also published as a GitHub Pages site from this repo, with no scheduled refresh.

The property-first HTML comparison includes preliminary school links and academic ratings, police-jurisdiction crime context, park walking-route leads, provisional overall fit and a broader monthly ownership estimate. Supporting records: `research/school-ratings.json` and `research/area-context.json`. Walk target: 20–30 minutes. Expanded cost assumptions are illustrative and editable in `research/summary.template.html`; rental allowance reserves 50% of gross rent for combined tax, vacancy and expenses, not a personal tax estimate.

Follow-up findings: `research/address-research.md`. All 45 examples now have approximate drive/transit ranges, park walking ranges and street-setting notes. `route-observations.json` preserves successful network-modelled baselines and unavailable results. `cost-estimates.json` preserves labelled matched advertised comparisons for missing costs; raw unknown values remain null. `ownership_costs.py` shares the full planning calculation between the HTML and CSV.

Expanded sample: [25-home intake and selection notes](research/sample-expansion.md). Added P13–P25, including Murrayville, lower-priced townhouse comparisons and a yard apartment comparator. All homes have parking/storage observations, school leads, fit assessments and cost/travel estimates with evidence labels.
