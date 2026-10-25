# Trends tracker

Updated: 2026-10-25. Purpose: understand changing choices and affordability, without treating a short history as a forecast.

## Initial evidence

The [structured series](trends.json) contains August and September 2026 GVR townhouse benchmarks for Coquitlam, Port Coquitlam, Pitt Meadows and Maple Ridge, GVR regional detached/townhouse benchmarks, and regional sales/inventory. Sources and observation dates are stored with the data. Two monthly points describe a recent movement, not a durable trend. October is incomplete at this research date.

Across the four local townhouse series, September benchmarks are lower than August. GVR regional active listings increased from 15,798 to 16,394 while sales decreased from 1,869 to 1,717. Seasonal effects, composition, and source revisions must be considered before drawing conclusions. This does not establish a future bottom or a buy/wait recommendation.

Sources: [GVR August](https://members.gvrealtors.ca/news/GVR-Stats-Package-August-2026.pdf), [GVR September](https://members.gvrealtors.ca/news/GVR-Stats-Package-September-2026.pdf).

The Bank of Canada page reports a 2.25% overnight target effective September 2, 2026. This is a single policy-rate observation, not a mortgage quote or rate trend. [Bank of Canada](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/)

## What to track and why

| Series | Geographic/type scope | Suggested refresh | Decision relevance |
|---|---|---|---|
| HPI benchmark/index and completed sales | Each candidate municipality; detached and townhouse separately | Monthly; build 12–24 months | Price direction and relative house/townhouse affordability |
| Active/new listings, sales, reported sales-to-active ratio, months of inventory | Same board, geography and property type where available | Monthly | Choice and negotiating conditions; record definitions |
| Days on market, reductions, relistings, final sale price | Comparable homes with yards/suites, tracked by address and MLS | Monthly or fortnightly during active search | What sellers actually accept and which homes linger |
| Fixed/variable mortgage rates and personalized quotes | Same lender/product, term, amortization, insured status and fees | Monthly and at rate/quote changes | Payment and qualification at the intended purchase price |
| Asking and achieved suite rent, utility inclusions, lease-up time | Similar size/legal status/location; deduplicate ads | Monthly/quarterly | Whether rental support is strengthening or weakening |
| Affordability scenarios | Fixed household assumptions plus updated prices/rates/rent | With each market update | Your mortgage contribution, total ownership cost and vacancy resilience |
| School catchments/capacity and outcomes | Actual elementary/later-school pathway | Official changes; outcomes annually | Whether a location continues to meet family needs |
| Transit, parks, development and road changes | Actual home and walking/commute routes | Quarterly/event-driven | Usability, exposure and future construction disruption |

## Collection rules

- Preserve period, observation date, source, geography, property type, unit and methodology. Keep revisions rather than silently mixing vintages.
- Prefer official board/CREA series, lender/Bank of Canada sources, CMHC rental data, and district/municipal notices. A broker's forward-looking opinion belongs in commentary, not the historical series.
- Keep GVR and FVREB coverage separate. Langley/Surrey data remain pending because primary-source retrieval failed; this is a gap, not evidence about those markets.
- Use year-over-year, 3/6/12-month changes and seasonal comparisons once enough data exist. Monthly counts are not seasonally adjusted unless the source says so.
- Do not infer gang/bullying trends from news volume, demographic changes or house prices. Compare school survey outcomes only with definitions, response rates and sample sizes.
- Asking rents are not achieved rents, and cross-sectional rent differences are not time trends. HPI benchmarks describe a typical property, not a guaranteed value for a specific home.
- Evaluate purchase price, rate, after-tax rent and repairs together. A falling purchase price can coincide with a higher monthly payment.

## Maintenance

Edit `trends.json` to add verified observations. Append property/rent status updates to `listing-observations.csv` and `rent-observations.csv`; do not overwrite the baseline. The first rows are snapshots from the sample and preserve its uncertainty. Rebuild the HTML with `python3 research/build_summary.py` after updating source files.

No automatic refresh or scheduled monitoring is configured. Suggested cadence is monthly during exploration, with more frequent listing checks when actively searching.
