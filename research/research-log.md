# Research log

## 2026-10-25 — P29 catchment district-confirmed (Baragar); repo brought in line with the delivered correction

Live-browser lookup on the SD35 Baragar School Locator, Oct 25, 2026. P29 (51-4967 220 Street, Murrayville): James Hill Elementary (K–5), H.D. Stafford Middle (6–8), Langley Secondary (9–12). Alex Hope Elementary is not the catchment elementary; Langley Fundamental Middle and Secondary School is a choice school, not the catchment secondary. Locator result is at street-number level (4967 220 Street as a whole, not unit 51 specifically). No capacity, before/after care, or school safety conclusion; James Hill Fraser Institute 2023/24 score 6.0 was already in the records. This corrects the earlier listing-lead record, which had shown Alex Hope / Langley Fundamental. P29 is now the third district-confirmed catchment in the sample (after P34 and P40). School records, fit note and next gate updated; outputs rebuilt.

## 2026-10-25 — Third expansion: Port Moody added (P46–P50); sample now 50 homes

Added 5 resale townhouses in Port Moody (SD43), the new municipality in scope, all verified Active Oct 25, 2026. P46 231 Balmoral Place ($748,000, fenced yard, end unit; total ~$4,207/mo, within the $5,000 total target; 241 days on market, $30,000 cut Oct 14). P47 461 Carlsen Place ($880,000, 4-bed with yard; total ~$5,153/mo, above target; covered-parking count conflicts inside Zolo's own data). P48 520 Cardiff Way ($824,800, 1,802 sqft — largest in the batch; strata/tax/year built not found publicly). P49 23-15 Forest Park Way ($799,900, 2-bed corner, fenced yard; $720/sqft, highest in the batch; strata/tax/year built not found publicly). P50 57-65 Foxwood Drive ($879,000, 3-bed; patio only — does not meet the private-yard criterion, included flagged; strata/tax not found publicly). No candidate scores above 6.0; fit leaders unchanged (P31/P36/P40 at 7.0). Market-fit median for the Port Moody group is $581/sqft (n=5): P46 in line, P47 in line (−8.9%), P48 below (−21.2%), P49 above (+23.9%), P50 above (+10.1%).

Fit notes supplied by the researcher were rewritten from the retired $3,500 mortgage-only target to the $5,000 total target before merging; totals recomputed with the repo model. Two corrections from verification: the agent's Port Moody Secondary slug (sd43.bc.ca/pmss) 404s — the page is https://www.sd43.bc.ca/portmoody/ — and the `pmss` key in the schools dict is Pitt Meadows Secondary (SD42), so Port Moody Secondary uses the new key `portmoodysecondary`. Seven new school keys added (60→67 schools). No Port Moody school has a Fraser Institute rating on file; catchments are listing/nearby leads only. Rent-vs-buy now covers 43 homes with a known total: renting wins 43 of 43 at 5 years and 42 of 43 at 10 years (P23 still the only 10-year exception). P46: −$74,327 at 5 years, breakeven 3.9%. P47: −$117,100 at 5 years, breakeven 4.5%.

## 2026-10-25 — Monthly target changed to $5,000 total; repo audit; rent-vs-buy comparison added

Roman replaced the $3,500 mortgage-only target with a **$5,000 total monthly payment** target (mortgage + strata + property tax + insurance + utilities + maintenance, after rent for suite homes). Audit of every repo file against the recent requests found the $3,500 target still referenced in criteria.md, the sample assumptions, the fit notes for P01–P45, the cost table, the site metrics/callout/budget lab/chart, the viewing checklist, the strategies table and the sample notes. All updated: assumption renamed to `monthly_total_target: 5000`; fit notes now state the total monthly planning estimate and its verdict vs $5,000; the cost table gains Total/month, Total after rent and over-total-target columns; `required_gross_rent` is now the gross rent needed for the total to meet $5,000 at the 50% offset; the budget lab gained an "other monthly costs" slider and tests the total; the comparison chart now plots totals with the $5,000 line. Data fix: P41/P42 strata null → 0 (detached, no strata, matching P07–P12), so their totals are now computable ($6,988 and $7,298/mo). Verified earlier requests still hold: fit marks on the site and spreadsheet, market-fit estimates, the instructions paragraph above the table is removed, Port Moody scope in criteria.md and the weekly cron. Dated log/expansion entries that cite the old $3,500 target were left as history, with a note of the change.

Result under the new target: every townhouse with known strata+tax is within $5,000 except P32 ($5,025, by ~$25). P31 $4,981 and P34 $4,979 sit just inside. The suite houses are all above even after modelled rent: P07–P09 $5,948–$6,174/mo, P41 $6,988, P42 $7,298; they need ~$3,400–$3,600/mo gross rent to meet the target.

Rent-vs-buy comparison added (`research/rent_vs_buy.py`, `research/rent-vs-buy.md`, and a block in the site's budget chapter): renting an apartment at $2,700/month vs buying, $250,000 down at 4.75%/25yr, 2% home appreciation, 5% investment return, 2% rent growth, 5% selling costs. At those assumptions renting wins for 40 of 41 homes at 5 years (only P23 breaks even by year 10, +$20,793); fit leaders P36 −$58,791, P40 −$74,041, P31 −$103,129 at 5 years. Most townhouses need 3.6–4.3% annual appreciation to break even over 5 years. Closing costs and tax treatment excluded; see the write-up.

## 2026-10-25 — Market-fit estimates added

Each property now carries a market-fit estimate: asking $/sqft vs the median asking $/sqft of comparable homes in this sample (same city + type, n≥3, else same type across cities, n≥3). Tiers: below −10%, in line ±10%, above +10%. Computed by `research/compute_market_fit.py` and stored in property-fit.json; shown under each asking price on the site (🟢 below, 🟡 in line, 🔴 above) and as market_fit columns in the spreadsheet. Above: P25, P27, P28, P29, P33. Below: P05, P20, P23, P34, P38. Seven properties have too few comparables for an estimate (P06, P10, P11, P12, P18, P41, P42). Asking-vs-asking only — not a valuation; $/sqft ignores age, condition and size effects. The three pending closes in this sample settled 0.1–1.9% below asking.

## 2026-10-25 — District-confirmed catchments for P34 and P40 (Baragar)

Live-browser lookups on the Baragar School Locator, Oct 25, 2026. P34 (1355 Citadel Drive, Port Coquitlam): Hazel Trembath Elementary (K–5), École Citadel Middle (6–8), École Riverside Secondary (9–12) — Castle Park is not the catchment elementary. Early French Immersion pathway (École Kilmer / École Pitt River Middle) requires application through the Program of Choice. P40 (6945 185 Street, Surrey): Regent Road Elementary (K–7) and École Salish Secondary (8–12) — Clayton Heights and Hillcrest are not the catchment schools; no middle school listed. Four school records added (60 total): Hazel Trembath, École Citadel Middle, Regent Road, École Salish. Both locator pages presented a reCAPTCHA after the street name was entered; each was cleared in the browser session. No sign-in used. P29's SD35 catchment secondary is still unresolved (its locator is also an interactive form).

## 2026-10-25 — Gap-filling pass: P01 pending, P42 resolved, P32/P43 resolved

Re-checked 20 properties (P26–P44 plus P01) against listing pages and index snapshots on Oct 25, 2026; 20 dated rows appended to listing-observations.csv. Resolved: P01 is pending (close $738,000 vs $739,000 asking, contract change 2026-09-13) — retained as a pricing comparable; P42's availability conflict resolved toward Active (EstateBlock, vancouvernashdom and Strawhomes all Active; the Zolo sitemap "Recently Removed" signal appears stale); P32 bath count 2.5 (Zolo structured data: 2 full + 1 half); P43 parking 1 space (single tandem garage; a conflicting "Covered Parking Places: 2" field inside Zolo's own data remains flagged); P29 floor area 1,337 sqft confirmed by three structured sources (1,344 appears only in marketing prose); P33's listing states its catchment directly (Central Community / École Pitt River Middle / École Riverside Secondary). Confirmed with new detail: P39 Walnut Road Elementary closed to out-of-catchment registration for 2025-26 (Surrey Schools registration page; 2026-27 status not yet published); P36's $80,000 Oct 13 cut has no stated reason anywhere public (implied original $779,900 — ask the listing agent); P38's complex is ~1.5 km south of Lougheed Hwy by desktop geocode ("only seconds" is marketing; on-site check still needed); P27's price change Sep 25 was -$10,000, and a stale $948,000 duplicate under old MLS R3117232 is not the current listing; P41's tax is $8,378.71 (year still not found). Still not found on public pages: strata/tax for P26, P28 (unit 32) and P35, P44 (plus parking); tax years for P30 and P42. Still unresolved: P34 elementary catchment and P40 secondary catchment (both need the interactive Baragar locator — live-browser lookups in progress); P29 catchment secondary (SD35 locator is also an interactive form).

Fit marks added to the site table and the spreadsheet: 7.0 and above shows 🟢 Top fit with a green-tinted row, 6.0–6.5 shows 🟡 Promising. The marks only rank this sample; all scores stay low confidence.

## 2026-10-25 — Second expansion: sample grows from 25 to 45 homes

Added 20 candidates (P26–P45) in four parallel batches: five Langley townhouses (P26–P30), five Coquitlam/Port Coquitlam/Pitt Meadows townhouses (P31–P35), five Maple Ridge/Surrey townhouses (P36–P40), and two detached houses with existing suites plus three lower-cost benchmarks (P41–P45). All were verified Active on Oct 25, 2026 from public advertisements/index snapshots, except P42, whose availability is unresolved (Active on EstateBlock and the vancouvernashdom Aldergrove list; "Recently Removed" on a Zolo sitemap list).

New fit leaders at 7.0/10: P31 (Coquitlam West, transit-strong), P36 (Maple Ridge, $699,900 — mortgage + strata + tax ~$3,222/mo, below the $3,500 target) and P40 (Surrey Clayton, Clayton Park 4–8 min). No property scores above 7.0. P36's $80,000 Oct 13 price cut, P39's 88 days on market, P32's bath-count discrepancy, P34's ambiguous elementary catchment, P38's Lougheed Highway proximity and P43's parking conflict are all flagged as next gates. The two suite properties have no rent modelled and no rental income is counted for either; suite permits and tenancy remain unverified. P26, P28, P35 and P44 have unverified strata/tax, recorded as null. Two verified Fraser Institute 2023/24 ratings were already in the record (Willoughby 6.8, Gordon Greenwood 7.3); no new rating entries were added. Sixteen new school records were added (56 total); duplicate keys were unified (Thomas Haney under 'thss', Clayton Heights under 'clayton', R.C. Garnett under 'rcgarnett'). Monthly mortgage figures in fit notes were computed with the repo's own formula (4.75% nominal compounded semi-annually, 25 years, $250k down). No new geocoded route observations were added; park ranges for the 20 additions are rough proximity estimates.

Next research: confirm P42's availability; verify P36's price-cut reason; resolve P40's secondary catchment (Clayton Heights vs École Salish); confirm P29's catchment secondary; verify suite permits/rents for P41/P42; fill the null strata/tax for P26, P28, P35, P44.

## 2026-10-25 — Availability re-check of top candidates

Re-checked the four first-priority townhouses against live listing pages.

- **P05 — 94-8068 207 Street (Willoughby), asking $799,800: pending.** Zolo shows status Pending with a $785,000 close price; contract status change 2026-09-30. The page states the property is not currently for sale. This was the joint-best fit (6.5/10); it is no longer an active candidate. Retain as a Willoughby pricing comparable.
- **P02 — 27-1338 Hames Crescent (Burke Mountain), asking $849,999: pending.** Zolo shows status Pending with a $835,000 close price; contract status change 2026-09-24. The REW source page now returns a historical Insight page rather than a live listing. Retain as a Burke Mountain pricing comparable; its school-pathway question is moot for this unit unless it returns to market.
- **P04 — 9-8968 208 Street (Walnut Grove), asking $799,900: confirmed active.** REALTOR.ca lists it for sale, 16 days on site, with an open house Oct 25, 2:00–4:00 pm. Strata fee confirmed at $481.42/month (was recorded as $481). Floor-area conflict (1,686 vs 1,695 sqft) remains unresolved.
- **P16 — 114-21928 48th Avenue (Murrayville), asking $749,000: status check in progress.** Its source page returned 404; a live-browser read was requested and the result is pending. No status conclusion recorded yet.

Price signal, not a trend claim: both pending units show close prices below asking (P05 −$14,800; P02 −$14,999). Two observations do not establish a market movement; treat them as comparable data points only.

Next research focus shifts to P04 (active) and P16 (status pending), with P13 as the lower-cost large-yard alternative. Availability observations appended to `listing-observations.csv`; statuses updated in `property-sample.json`; comparison outputs rebuilt.

## 2026-10-25 — P16 status resolved

The live-browser read of P16's source page (114-21928 48th Avenue, Murrayville, asking $749,000) returned "Listing no longer available". No asking price, close price, MLS number or last-updated date is shown on the page, so none of those could be verified from the listing itself. Removal is not evidence of a sale. P16 is no longer an active candidate and is retained as a Murrayville pricing comparable.

That leaves P04 as the only still-active home among the four first-priority candidates; P13 is the lower-cost large-yard alternative. Status, observation log, fit notes and workbench next-research line updated; outputs rebuilt.

## 2026-10-25 — Property-first workbench, address links and catchment investigation

User requested clickable addresses, school catchment investigation and school links; then directed that properties become the first/focal block, using a table with expandable rows and columns for location, home type, downtown driving/public transport, elementary/secondary schools, size and yard.

Reorganized the HTML with properties first. Added sticky location/expansion controls, separate school stages including middle school, price/mortgage columns, size/yard, route links and evidence status. Addresses link to Google Maps; listings remain separate. Expanded rows show costs, suite/yard/transit notes, sources, school evidence/conflicts and future changes. School-name search and expand/collapse/print state updated for table rows. Waterfront Station is an explicit comparison endpoint; all travel times remain unmeasured.

Added `school-catchments.json` and generated Markdown summary. Identified 25 official school pages and proposed school leads for 11 properties; P01 remains unresolved. Public address locators require CAPTCHA, so no locator bypass or district-confirmed result claimed. Inspected published SD35 maps, checked official feeder information and recorded source age. Corrected nearby-school assumptions and rejected obvious listing-data errors (private-school catchment label; Betty Gilbert assigned remotely to Willoughby; choice programs treated as guaranteed neighbourhood schools).

SD35's official May 2026 notice establishes the Willoughby Elementary → Yorkson Creek → Emery Dosdall transition from September 2027, conditional on home address. Current/future pathways displayed separately. SD43 P02 elementary sources conflict and middle assignment is unresolved. No safety/academic outcome ranking inferred.

Validation: generated HTML/data and CSV checks; JavaScript syntax and mocked-DOM smoke checks for 24 table rows, 12 expansion buttons, 24 route links, school search, expand/collapse and calculator. No browser visual layout validation available. Commit this completed batch as a research/report checkpoint.

## 2026-10-25 — Periodic version-control checkpoints authorized

User requested commits from time to time. Create an initial checkpoint for the existing research and report, then commit meaningful batches of completed updates. Exclude generated Python caches and temporary files; retain the compiled HTML and comparison artifacts. No remote push requested.

## 2026-10-25 — Trends tracker and compiled HTML report

User requested tracking trends, then a root HTML summary with charts, examples and collapsible sections. Created `index.html`, generated from `research/summary.template.html` and local JSON/criteria data via `research/build_summary.py`.

Included household criteria, strategy comparison, 12 filterable property cards, six rent observations, mortgage calculator with rate/rent/amortization controls, school/park/street/transit evidence gaps, source links and printable expandable sections. HTML uses embedded data and no external dependencies or network requests.

Created `trends.json` and `trends.md`. Seeded August–September 2026 GVR local townhouse benchmarks and regional detached/townhouse prices plus sales/inventory; recorded one Bank of Canada policy-rate observation. Langley/Surrey primary series remain pending after FVREB retrieval failures. A two-month movement is explicitly distinguished from a durable trend/forecast; asking-rent snapshots are not charted as time trends.

Seeded append-only listing/rent observation CSVs. Rebuild preserves existing history. No automated monitoring or deployment configured. Checked generated HTML structure/local links and exercised calculator, filters and SVG generation in a mocked DOM JavaScript smoke check. No browser engine is installed, so visual rendering and browser-native print/layout were not verified.

## 2026-10-25 — Busy-road preference clarified

User clarified that one street away from a busy road is fine; direct exposure is the concern. Updated criteria and screening guidance accordingly. Assess front/rear/side exposure and buffering at the actual unit, rather than rejecting homes based on proximity alone. Added explicit exposure/buffering fields to the sample; no existing home assessed by this update.

## 2026-10-25 — Quieter street preference added

User prefers not to be next to busy streets if possible. Added this preference to criteria and a street-setting field to all property records/the generated spreadsheet. Assess frontage and rear exposure, unit location within complexes, traffic noise, cut-through traffic, and school/park-route crossings. No absolute exclusion rule or minimum setback inferred. Existing properties remain unassessed.

## 2026-10-25 — Nearby parks preference added

User added nearby parks as a nice-to-have. Updated household criteria and added a parks field to all 12 property records and the generated spreadsheet. Future checks should record park names, actual walking access, major road crossings, child-friendly features, source and verification date. No distance threshold or priority above school safety/academics assumed; existing park access remains unresearched.

## 2026-10-25 — Initial durable record

### User direction

Explore possible purchase strategies rather than assume an imminent purchase or a selected property type. Preserve artifacts for periodic research and later decision-making.

### Confirmed changes during discussion

- Safety at school (bullying, drugs, gang activity) comes before academics.
- Consider elementary and middle-school ages; separate middle-school requirement remains unclear.
- Backyard preferred; approximately one-hour public-transit downtown commute is flexible.
- Add Langley City and Township explicitly.
- $250,000 down payment is separate from emergency and closing savings.
- $180,000 annual household income; no debt.
- $3,500 target is mortgage-only; a larger mortgage payment is acceptable if rent covers part.

### Current research position

No property type or location selected. Compare townhouse without rental reliance with detached-plus-suite and farther-out detached alternatives. Prior price bands are screening estimates, not approved affordability. Rental allowances are assumptions, not verified rents or tax estimates.

### Next research, in order

1. Collect representative live examples across Port Coquitlam/Coquitlam, Pitt Meadows/Maple Ridge, Surrey and Langley. Include permitted-suite houses and yard-bearing townhouses; date and source each example.
2. Verify suite status and comparable long-term rents; distinguish existing lease income from achievable vacant-possession rent.
3. Map exact elementary and later-school catchments. Compare academic progress and safety evidence separately; identify unavailable/suppressed data. Ask about capacity and support rather than relying on rankings alone.
4. Measure weekday door-to-door commute at the expected travel time; separate existing transit from planned infrastructure.
5. Build itemized ownership and after-tax rental scenarios, including no-rent and renewal-rate sensitivity; compare 25- and 30-year amortization where available.
6. Investigate neighbourhood-specific value drivers: comparable sales, supply, land/title, hazards, building condition, and resale audience. Do not assume future transit or land automatically produces higher returns.
7. Obtain lender assessment when the user is ready; do not submit applications or contact third parties without authorization.

### Suggested refresh cadence

- During exploration: refresh market/rate/listing/rent evidence every 1–3 months or when plans change.
- Before a viewing shortlist: refresh current listings and address-level catchments/transit.
- Before an offer: verify financing, title, permits, tenancy, condition, insurance and applicable taxes using current property-specific records.

This is a suggested workflow, not an automated schedule. No recurring task has been created.

## 2026-10-25 — Discussion and interview review

User requested online discussions/interviews to uncover missed ownership strategies. Added `community-strategies.md` with linked evidence, limitations and household-fit assessments. Reviewed local co-owner and cohousing interviews; Reddit discussions about suites, leaseholds, co-ops, starter purchases, renting/investing and rent-to-own; checked regulator/sector/operator explanations.

New research branches: co-buying a house with separate living units; cohousing including Compass Commons in Langley; occupying the smaller unit and renting the larger one; leasehold and equity co-op ownership; nonprofit co-op as a non-ownership alternative; rentvesting; homestay. Recorded lower-priority rent-to-own and investment leverage rather than treating them as affordability fixes.

No consensus or prevalence claim established. Two CityNews articles concern the same family. One BC suite discussion originates in Prince George, not Metro Vancouver. Reddit relative dates sometimes conflict. No school, listing, rent or project eligibility findings established by this pass.

Next: use household interest to select a few strategy branches, then compare actual properties and conservative total costs. Do not narrow the original geographic scope or school priorities based on this exploratory review.

## 2026-10-25 — First property sample and financial screen

User authorized proceeding with the proposed property research. Recorded 12 advertised examples across Port Coquitlam, Coquitlam, Pitt Meadows, Maple Ridge, Surrey, Langley City and Township. Added six exploratory rental advertisements. Created JSON source data, CSV comparison, generated mortgage/known-cost table, sensitivity scenarios, screening notes and preliminary school/transit notes.

Key finding: at 4.75%/25 years, sampled $1.099M one-bedroom-suite houses need about $1,757 gross rent to meet the $3,500 contribution target using a 25% rental allowance. The sparse rent advertisements found do not establish that amount; several scenarios remain over target before taxes and ownership costs. Townhouse examples around $800k have mortgage payments around $3,120 plus strata/tax and other costs.

Recorded as conditional/hold: unfinished Aldergrove suites, Langley City conversion potential, new rowhome wet-bar configuration, and conflicting/stale availability. No suite permit has been independently verified. School leads and primary-source policies/directories gathered; no comparative safety/academic outcome conclusion. Transit corridors identified; no live door-to-door itineraries or one-hour commute clearance.

Next focus: confirm availability of P02–P05; establish official school assignments and outcomes; improve suite rental comparables and permit evidence for the detached branch. Retain original priorities and full location scope.

## 2026-10-25 — Property comparison workbench

Moved property examples first; added expandable comparison rows, address/direction links, preliminary official school pathways and future catchment changes. Added sourced elementary academic scores (2023/24 data, 2025 report), jurisdiction crime context and park leads. Park preference clarified as a 20–30 minute walk; routes/crossings remain unverified. Size now follows home type. Overall fit remains provisional while school safety and street exposure are unresolved. Replaced mortgage-only table amount with ownership planning estimates including tax, strata, reserves and conservative rent offsets. These placeholders are not quotes or an individual rental tax calculation.

## 2026-10-25 — Follow up unresearched blocks

Researched all 12 park/street/commute records. Added 12 family walking estimates (six network distances), 12 drive/transit planning ranges (five driving map baselines), street-specific notes and arterial flags, school policy evidence and the Burke Mountain Fall 2027 schedule correction. Retained unavailable routing outcomes explicitly. Added a sourced three-comparable $0 strata estimate for P06; located the three missing advertised tax figures and refreshed P07’s relisting/price while preserving history. Centralized total ownership calculations shared by HTML and CSV. See address-research.md for methods and remaining verification.

## 2026-10-25 — Personal fit estimates

Added low-confidence editorial fit estimates for all 12 examples, with strengths, tradeoffs and explicit priority order. Scores distinguish the $3,500 mortgage-only goal from broader ownership expenses and do not imply school safety clearance. P05 leads the next-research list; P04 is conditional on unit buffering from 208 Street. Kept expand button first and moved rating to second. Source assessments are stored in property-fit.json/markdown and compiled into HTML/CSV.

## 2026-10-25 — Nearest-school fallback and secondary clarification

Removed the Middle school comparison column; the requested comparison is elementary and secondary. Added clearly labelled nearest identified regular public school fallbacks: P01 Birchland Elementary/Terry Fox Secondary; P02 Smiling Creek Elementary where assignment evidence conflicts. Original assignment evidence is preserved separately; nearest does not establish eligibility. Added exact-school Fraser 2023/24 indicators for Birchland (4.5) and Smiling Creek (6.8), using the 2025 report. Fit ratings remain conditional and unchanged by proximity alone.

## 2026-10-25 — Important notes column

Added concise address-specific decision notes to the property table and CSV, backed by existing research. Notes emphasize suite readiness, cost assumptions, street exposure, school changes and listing conflicts. The field supports an empty list, rendered as a blank cell when there is no material note.

## 2026-10-25 — Sortable property columns

Added accessible clickable sort controls to all 15 data columns. Numeric ranges use midpoints; school columns use displayed names, including nearest fallbacks; location uses city/neighbourhood/address. Text columns sort alphabetically, crime uses jurisdiction CSI with missing/transition values last in either direction. Sorting preserves filters and expanded property rows, with stable ID tie-breaking and visible/announced direction.

## 2026-10-25 — Garage, parking and storage

Added a sortable garage/parking/locker column and sourced advertised details for the initial 12 homes. Distinguishes total/covered spaces, tandem versus side-by-side, sheds/workshops and unconfirmed lockers. P03’s 3-versus-4 space conflict is preserved as a range. Counts are not verified exclusive rights or garage dimensions; suite examples require owner/tenant allocation checks.

## 2026-10-25 — Expanded sample from 12 to 25

Added 13 linked property examples with costs, school leads, parks, street notes, garage/parking/storage and provisional fit scores. Included two Murrayville options, lower-priced Pitt Meadows/Langley City benchmarks and a ground-floor yard apartment. Pending/conflicting availability is retained. Rejected a $0 tax placeholder and added a labelled two-property Coquitlam tax proxy; no unsupported rental income. New park intervals use checked BC geocodes and rough family-pace assumptions; no new live/network travel measurement claimed. Added apartment-specific ownership allowances and preserved append-only observations.
