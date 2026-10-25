# Viewing checklist — family of three, child age six

For use at viewings and shortlist decisions. It turns the household criteria into checks you can do before, during and after a viewing. Nothing here is a purchase recommendation; every item names what to verify and where the answer goes.

## Before the viewing (desk checks)

- [ ] Run the exact address through the district school locator (SD35, SD43, SD42, or the SD36 Baragar tool). A listing's "nearby school" is not an assignment. Record the elementary and secondary result in `research/school-catchments.json`.
- [ ] Check whether the catchment school is closed to out-of-catchment registration, and whether any boundary change is planned (for example, Willoughby Elementary feeds Yorkson Creek Middle and Emery Dosdall Secondary from September 2027).
- [ ] Ask the school about before/after school care on site, and whether there is a waitlist. Ask how bullying incidents are reported and tracked, and whether the school publishes a code of conduct or safety/belonging report.
- [ ] Talk to parents at school pickup if you can. One conversation is not evidence, but a pattern across several is.
- [ ] Confirm the asking price, status, strata fee, annual tax and tax year from the listing sheet or strata documents. Keep anything unverified as null in `research/property-sample.json` — never $0.
- [ ] Request the strata documents before the viewing: depreciation report, contingency reserve balance, any special levies planned or underway, bylaws (pets, rentals, age restrictions), and insurance deductible. A low strata fee can hide a coming levy.
- [ ] Time the commute for real. Plan one live weekday-morning run from the address to Waterfront Station. West Coast Express runs weekday mornings only westbound; the ranges in the sample are planning estimates, not timed trips.
- [ ] Check flood/insurance exposure for the address and lot (Pitt Meadows/Maple Ridge low-lying areas especially), and confirm what a home insurer will cover.

## At the viewing (the home)

- [ ] Yard: fenced, flat, and visible from the kitchen or main living area. Confirm fencing and exclusive use on the title or strata plan — "fenced" in an ad does not establish size or rights.
- [ ] Kid's bedroom: near the parents' room, big enough for a bed plus a desk as the child grows. Count bedrooms against the future, not just today — a fourth bedroom or flex room pays off.
- [ ] Storage: garage, locker, shed or workshop space. Kids accumulate things; confirm what is exclusive-use and measure the garage rather than trusting "double".
- [ ] Street: stand outside and listen. Traffic volume, speed, cut-through use, parking pressure. Check whether the unit itself (not just the complex) faces or backs onto a busy road.
- [ ] Noise and sleep: road, rail, flight path, neighbouring units. Strata townhouses share walls — ask about sound between units.
- [ ] Building age risks (1980s–1990s builds especially): roof, furnace, windows, poly-B plumbing, aluminum wiring, Kitec. Note what is original and budget for it.
- [ ] Suite, if any: is it permitted, currently tenanted, separately metered, insurable? A suite that is not permitted, insurable and rentable cannot be counted toward the mortgage target. No rent is modelled until permit, tenancy and rent are all verified.
- [ ] Park walk: walk to the nearest playground, not just the nearest park. Check the route — sidewalks, crossings, gates — and whether the playground suits a six-year-old.

## After the viewing (second look)

- [ ] Visit the street a second time at a different hour — weekday evening and weekend. Noise, parking and cut-through traffic change by time of day.
- [ ] Walk the school route with the child in mind: sidewalks the whole way, safe crossings, school-zone speeds.
- [ ] Book a home inspection for any shortlisted home, and a strata document review for townhouses. Do not rely on the listing's condition claims.
- [ ] Re-check the numbers with the verified strata fee and tax: mortgage + strata + tax against the ~$3,500 target, plus insurance, utilities, maintenance and reserves. The cost table in `research/property-cost-comparison.md` is the comparison, not a budget.
- [ ] Check what is planned nearby: development applications, road or SkyTrain construction (Clayton/Surrey), school expansions. A quiet street can change.
- [ ] For offers: the two pending closes in this sample both landed about $15,000 under asking. That is context for one negotiation, not a market trend.

## Per-property gates

Each property's `next_gate` field in `research/property-sample.json` lists what is still open for that home, and `research/property-fit.md` carries the same notes in readable form. Close the gates for a shortlisted home before offering; do not close them by assumption.

## What this checklist does not cover

Lender pre-approval, legal/title review, tax treatment of rental income, and renovation costing are separate steps with professionals. The research log lists lender assessment as a next step when the user is ready.
