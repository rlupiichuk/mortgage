# First property sample: findings and screening decisions

Observed 2026-10-25. This is an exploratory sample across strategies and locations, not a comprehensive inventory, valuation, or viewing recommendation.

## Artifacts

- [Cost comparison](property-cost-comparison.md): monthly mortgage, known tax/strata subtotal, rent sensitivity and rate/amortization alternatives.
- [Spreadsheet](property-comparison.csv): 12 examples with sources, MLS identifiers, yard/suite claims, uncertainty and next checks.
- [Source data and rental observations](property-sample.json): update this and run `python3 research/build_property_comparison.py` to regenerate both outputs.
- [Initial school and transit notes](school-and-transit-screen.md).

## What the sample changes

### Yard-bearing townhouses are a concrete research path

Examples P02–P05 advertise private/fenced outdoor space in the $799,800–$849,999 range. Mortgage-only estimates are about $3,120–$3,405 with the current assumptions. Mortgage plus advertised strata fees and tax is about $3,778–$4,203, before insurance, utilities, maintenance outside strata coverage or levies. These are not total budgets.

P01 is a lower-price Port Coquitlam lead with unresolved availability and conflicting property details; retain the record but resolve status before investing time in schools. An advertised private yard still requires title/strata-plan/bylaw checks and an assessment of actual usable size.

### Existing one-bedroom suites do not automatically make $1.1M fit

P07 and P08 ask $1.099M and advertise existing one-bedroom suites. At 4.75%/25 years their mortgages are about $4,818/month. Exploratory Maple Ridge one-bedroom advertisements at $1,250 and $1,650 imply a mortgage contribution of about $3,880 and $3,580 after the 25% rental allowance, before rental income tax. Thus neither scenario meets $3,500 at those assumptions. These advertisements are a sparse sensitivity bracket, not a property-specific rent appraisal or the market range.

P09 also asks $1.099M. Nearby Clayton asking-rent leads around $1,400–$1,475 imply about $3,711–$3,768 toward mortgage after the allowance. Rental snapshots can be stale and utilities differ. The amount needed to meet $3,500 is about $1,757 gross rent/month. Property taxes and all other ownership costs remain extra.

Do not reject the whole suite strategy on this sample: a lower purchase price, different suite/owner layout, a verified higher rent, different rate or eligible 30-year amortization changes the result. Do not assume a higher rent merely because it makes the budget work.

### Several apparent suite bargains are future projects

- P10 Aldergrove: advertised two-bedroom unit is unfinished and described as a future legal suite; total floor area and bath counts conflict. Marketing rent and net-payment claims were not used.
- P11 Langley City: conversion potential only; space for a kitchen is not an operating suite. No current rent counted.
- P12 Langley City: new non-strata rowhome, despite some sites presenting it as a house. Bedroom/full bath/wet bar does not establish a self-contained rental suite. Yard and GST treatment unresolved.

No sampled suite has been independently established as permitted, insurable and rentable. The targeted legal-suite strategy therefore remains a search requirement, not a verified outcome of this sample.

## Preliminary order for deeper research

This ordering measures usefulness for the next research pass, not safety or academic quality.

| Priority | Examples | Reason to investigate | First gate |
|---|---|---|---|
| First | P04 Walnut Grove; P05 Willoughby | Around $800k; four bedrooms and advertised fenced yards | Confirm availability, catchments, yard and total strata costs |
| First | P02 Burke Mountain | Three bedrooms, yard, SD43 middle-school pathway candidate | Verify address-level schools and practical bus commute |
| First | P03 Pitt Meadows | Larger advertised yard and three bedrooms | Verify assignment, grade structure, flood exposure and WCE access |
| Conditional | P07/P08 Maple Ridge; P09 Clayton | Illustrate detached-plus-suite tradeoffs | Verify suite permits and rent, then solve mortgage-contribution gap |
| Secondary | P06 South Surrey half-duplex | Yard/title alternative around $799k | Two-bedroom space fit, shared obligations and commute |
| Hold | P01 | Lower-price lead but conflicting availability/data | Confirm actual listing status |
| Hold | P10/P11/P12 | Useful construction/new-home comparators | Resolve conversion, permit, yard, GST and capital-cost gaps |

## Rental evidence quality

Six asking-rent observations are stored, with source-specific confidence. R01 and R05 were opened directly; R03 changed from $1,300 in search results to $1,400 on the opened page. Other observations include search-only classifieds and may overlap syndicated advertisements. Do not count copies of the same rental as independent comparables. No achieved rents, demand/lease-up times, legal-suite status or actual operating expenses verified.

## Refresh procedure

Nearby parks are now a user-confirmed nice-to-have. Each property record includes a `parks_nearby` field for park names, walking time, route crossings, playgrounds/trails/fields, and sources. Existing properties remain marked unresearched until checked; park proximity does not establish school or neighbourhood safety.

The user prefers no direct exposure to a busy street, including frontage, rear or side exposure. Being one street away is acceptable: proximity alone is not a reason to reject a home. Each property has a `street_setting` field to track direct exposure, buffering, traffic/noise, cut-through traffic, and crossings on school/park routes. Assess the actual unit position within a complex rather than relying on the development's street address. Listing descriptions such as "quiet" are claims until checked; no fixed road-distance cutoff assumed.

1. Search the MLS identifier and exact unit/address. Record listing price/status with observation date; preserve old record if withdrawn or sold.
2. Prefer listing brokerage/MLS-fed property pages; distinguish a live property page from an old Insight/history page.
3. Refresh taxes, fee inclusions, yard rights, dimensions, permits and lease terms. Keep missing costs null.
4. Replace exploratory rent brackets with several genuinely comparable, independent listings and property-manager/lender estimates when authorized.
5. Compare 25/30-year and rate sensitivity; itemize after-tax rental cash flow and reserves before setting a maximum offer.

## Scope still outstanding

Exact address-level school assignments, comparative safety/academic outcomes, municipal suite records, lender approval, complete ownership budgets, hazards, title, achieved rents, live trip-planner itineraries and property inspections remain unresolved. No outreach or applications were made. Visits and professional assessments are later steps, not implied completed tasks.
