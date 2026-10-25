# First property sample: findings and screening decisions

Observed 2026-10-25. This is an exploratory sample across strategies and locations, not a comprehensive inventory, valuation, or viewing recommendation.

## Artifacts

- [Cost comparison](property-cost-comparison.md): monthly mortgage, known tax/strata subtotal, rent sensitivity and rate/amortization alternatives.
- [Spreadsheet](property-comparison.csv): 45 examples with sources, MLS identifiers, yard/suite claims, uncertainty and next checks.
- [Source data and rental observations](property-sample.json): update this and run `python3 research/build_property_comparison.py` to regenerate both outputs.
- [Initial school and transit notes](school-and-transit-screen.md).

## What the sample changes

### Yard-bearing townhouses are a concrete research path

Examples P02–P05 advertise private/fenced outdoor space in the $799,800–$849,999 range. Mortgage-only estimates are about $3,120–$3,405 with the current assumptions. Mortgage plus advertised strata fees and tax is about $3,778–$4,203, before insurance, utilities, maintenance outside strata coverage or levies. Total monthly planning estimates for P02–P05 run about $4,461–$4,907/mo, all within the $5,000 total target. These are not total budgets.

P01 is a lower-price Port Coquitlam lead with unresolved availability and conflicting property details; retain the record but resolve status before investing time in schools. An advertised private yard still requires title/strata-plan/bylaw checks and an assessment of actual usable size.

### Existing one-bedroom suites do not automatically make $1.1M fit

P07 and P08 ask $1.099M and advertise existing one-bedroom suites. At 4.75%/25 years their mortgages are about $4,818/month. Total monthly planning estimates are about $5,948–$6,174/mo after the 50% rental offset on exploratory Maple Ridge one-bedroom advertisements at $1,250 and $1,650, above the $5,000 total target. The amount needed to meet $5,000 is about $3,550–$3,600 gross rent/month. These advertisements are a sparse sensitivity bracket, not a property-specific rent appraisal or the market range.

P09 also asks $1.099M. Nearby Clayton asking-rent leads around $1,400–$1,475 imply a total monthly planning estimate of about $5,968–$6,006/mo after the 50% rental offset, above the $5,000 total target. The amount needed to meet $5,000 is about $3,412 gross rent/month. Rental snapshots can be stale and utilities differ. Property taxes, insurance, utilities and maintenance are included in the total above.

Do not reject the whole suite strategy on this sample: a lower purchase price, different suite/owner layout, a verified higher rent, different rate or eligible 30-year amortization changes the result. Do not assume a higher rent merely because it makes the budget work.

### Several apparent suite bargains are future projects

- P10 Aldergrove: advertised two-bedroom unit is unfinished and described as a future legal suite; total floor area and bath counts conflict. Marketing rent and net-payment claims were not used.
- P11 Langley City: conversion potential only; space for a kitchen is not an operating suite. No current rent counted.
- P12 Langley City: new non-strata rowhome, despite some sites presenting it as a house. Bedroom/full bath/wet bar does not establish a self-contained rental suite. Yard and GST treatment unresolved.

No sampled suite has been independently established as permitted, insurable and rentable. The targeted legal-suite strategy therefore remains a search requirement, not a verified outcome of this sample.

P41 and P42 add two more detached-with-suite examples at $1,099,999 and $1,198,888. Both advertise an existing suite, but neither has a verified permit, tenancy or rent, so no rental income is counted for either. P41 fronts directly onto 240 Street, failing the no-direct-busy-road preference. P42's availability conflict was resolved toward Active on Oct 25, 2026 (EstateBlock, vancouvernashdom and Strawhomes all Active; the Zolo sitemap "Recently Removed" signal appears stale).

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

## Expansion

The original P01–P12 screen below is retained as research history. The active comparison now has 45 examples; see [sample expansion](sample-expansion.md), [fit assessments](property-fit.md) and the CSV for P13–P45. Added properties include lower-cost family-yard benchmarks and Murrayville options; this broadens the earlier $750k–$850k townhouse search band rather than treating it as a minimum.

The second expansion (P26–P45, 2026-10-25) adds fifteen more townhouses, two detached houses with existing suites and three lower-cost benchmarks. New fit leaders at 7.0/10 are P31 Coquitlam West (transit-strong), P36 Maple Ridge ($699,900; mortgage + strata + tax ~$3,222/mo, below the $3,500 target) and P40 Clayton (Clayton Park 4–8 min). No property scores above 7.0; all new scores are low confidence. P04 remains the only still-active home among the four first-priority candidates from the earlier set (P05 and P02 pending, P16 removed).
