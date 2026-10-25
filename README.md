# Greater Vancouver home purchase research

Last updated: 2026-10-25. All amounts CAD.

This is a living decision record for exploring whether, where, and how to buy a family home. No purchase strategy, neighbourhood, lender, or school has been selected.

## Start here

- [Open the compiled HTML summary](index.html): collapsible research sections, charts, property filters and an interactive budget calculator. Opens locally without a server.
- [Household criteria](research/criteria.md): confirmed preferences and unresolved questions.
- [Purchase strategies and budget](research/strategies-and-budget.md): comparable scenarios and calculation assumptions.
- [Strategies from discussions and interviews](research/community-strategies.md): alternative paths, lived experiences, source caveats, and household fit.
- [Location shortlist](research/locations.csv): places to investigate, not recommendations or safety rankings.
- [First property sample](research/property-sample-notes.md): 12 examples, screening decisions and outstanding checks.
- [Property cost comparison](research/property-cost-comparison.md) and [spreadsheet](research/property-comparison.csv): reproducible costs with sources and uncertainty.
- [Initial school/transit screening](research/school-and-transit-screen.md): address-specific leads and verification gaps.
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

Personal financial details are stored in this folder and its local Git history. Nothing has been published or pushed remotely.

Save meaningful research and report updates in periodic Git commits, as requested by the user. Review the staged changes before committing; exclude caches and temporary files. Remote publication or pushing is not part of this instruction.

## Rebuild the summaries

After editing the property sample, run `python3 research/build_property_comparison.py` to regenerate the spreadsheet and cost table. Run `python3 research/build_summary.py` to compile `index.html` from the property sample, criteria, trend data and HTML template. These scripts do not fetch live data. They preserve existing listing/rent observation logs; append new dated observations rather than replacing history.

The HTML includes a compiled interpretation as well as data-driven charts: review its narrative and date labels when updating the research. It is a local report, with no external scripts, analytics, hosted deployment or scheduled refresh.
