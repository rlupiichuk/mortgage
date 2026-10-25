# Rent vs buy: net worth after 5 and 10 years

Computed 2026-10-25 with `python3 research/rent_vs_buy.py`. A planning comparison, not a forecast or a recommendation.

## The question

Renting an apartment at **$2,700/month** versus buying one of the homes in this sample, with the same $250,000 down payment. Which leaves the household wealthier after 5 and 10 years?

## How it is calculated

A monthly simulation, identical rules for both sides:

- **Buy:** $250,000 down, mortgage at 4.75% nominal compounded semi-annually, 25-year amortization. Monthly ownership costs from the ownership model (mortgage + strata + property tax/12 + maintenance + insurance + utilities), minus 50% of modelled gross rent at the midpoint of the modelled range where a suite exists. The mortgage payment is fixed; the other costs grow 2% a year. The home grows at 2% a year. At the horizon the owner sells: net worth is 95% of the home value (5% selling costs) minus the remaining mortgage balance, plus any months where rent exceeded owning costs, invested instead.
- **Rent:** keep the $250,000 invested at 5% a year, pay $2,700/month rent growing 2% a year, and invest each month's surplus (owning total minus rent) when owning costs more. Net worth is the invested down payment plus the invested monthly surpluses.

Both sides invest at the same return and face the same rent growth, so the comparison isolates the buy-vs-rent structure, not a return forecast. The "breakeven appreciation" column is the annual home-price growth at which buying equals renting over 5 years.

## Assumptions

| Input | Value |
|---|---|
| Rent | $2,700/month, growing 2%/year |
| Down payment / amount invested if renting | $250,000 |
| Mortgage | 4.75% nominal, compounded semi-annually, 25 years |
| Home appreciation (base case) | 2%/year |
| Investment return | 5%/year, monthly compounding |
| Selling costs | 5% of sale price |
| Ownership costs | Repo ownership model; non-mortgage parts grow 2%/year |

## Headline findings (base case: 2% appreciation, 5% investment return)

- Renting wins for **43 of the 43** homes with a known total at 5 years, and 42 of 43 at 10 years. The only exception is P23 (Langley City, $479,900, total $2,536/month — cheaper than rent), which breaks even by year 10 (+$20,793) but is still −$5,158 at year 5.
- The three fit leaders are all behind renting at 5 years: P36 −$58,791, P40 −$74,041, P31 −$103,129. At 10 years: P36 −$92,520, P40 −$123,900, P31 −$185,651.
- The cheapest total costs lose least: P43 −$34,620 and P45 −$39,686 at 5 years.
- The detached-with-suite homes lose most, because their totals run $6,000–$7,400/month: P07–P09 −$136,060 to −$144,061 at 5 years, P41 −$206,617, P42 −$210,475.
- Breakeven appreciation over 5 years runs 2.2% (P23) to 5.4% (P41). Most townhouses need **3.6–4.3% a year** — above the 2% base case, and above the recent direction: the August–September 2026 townhouse benchmarks in this research all fell.

## Why renting wins in this base case

Three forces, in order:

1. **The monthly gap.** Owning costs $3,300–$5,000/month for most townhouses versus $2,700 rent. The renter invests that $600–$2,300/month gap plus the $250,000 down payment at 5%.
2. **Selling costs.** 5% of the sale price comes off the owner's equity at exit — about $35,000–$60,000 on these homes. It roughly cancels the first years of appreciation.
3. **Leverage cuts both ways.** 2% appreciation on a $700,000–$900,000 home is $14,000–$18,000 a year on a $250,000 down payment, but the owner also pays roughly $14,000–$28,000 a year more than rent to carry it.

## What would change the answer

- **Higher appreciation.** At 4% a year, most townhouses break even or win by year 5; at 5%, buying wins broadly. The breakeven column shows the threshold per home.
- **Lower investment return.** At 3% instead of 5%, the renter's invested surplus grows slower and the gaps roughly halve.
- **A longer horizon with low appreciation.** The gap widens with time in the base case, because the renter's invested surplus compounds. Buying needs appreciation, not time, to catch up.
- **A cheaper home.** P23 shows the shape: a total monthly cost at or below rent removes the renter's monthly surplus, and buying wins by year 10 even at 2% appreciation.
- **Staying put.** The model assumes one purchase and one sale. Moving again adds another round of selling costs and resets the amortization clock.

## What this does not capture

- **Property transfer tax and closing costs** (~$15,000–$25,000 on these prices) fall on the buyer only and are excluded; including them would widen renting's lead.
- **Tax treatment** of investments and rental income is not modelled; TFSA/RRSP room and the principal-residence exemption change the numbers both ways.
- **The $2,700 apartment is not the same home.** The comparison is financial, not like-for-like living: a rented apartment may be smaller, in a different neighbourhood, or without the yard and school catchment the purchase is for.
- **Rent growth and investment returns are assumptions**, not forecasts. The 2026 BC rent-increase guideline caps most existing tenancies, but a new tenancy starts at market rent.
- **Behaviour.** The rent side assumes the household actually invests the monthly difference and the down payment, every month, for 5–10 years. If the surplus is spent, renting's advantage shrinks or reverses.
- **Non-financial reasons** — stability, a yard, a school catchment, control over the home — are the reason to buy in this sample, and this comparison does not price them.

## Results

| ID | Address | Asking | Total/mo | Net worth 5 yr: buy | Net worth 5 yr: rent | 5-yr difference | 10-yr difference | Breakeven appreciation (5 yr) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| P23 | 77-20350 53 Avenue, Langley City | $479,900 | $2,536 | $315,682 | $320,840 | −$5,158 | $20,793 | 2.2% |
| P43 | 37-20460 66 Avenue, Township of Langley | $615,999 | $3,305 | $323,457 | $358,077 | −$34,620 | −$40,431 | 3.1% |
| P45 | 4-12070 207a Street, Maple Ridge | $599,900 | $3,335 | $320,764 | $360,450 | −$39,686 | −$53,606 | 3.3% |
| P24 | 11-6555 192A Street, Surrey | $655,880 | $3,491 | $330,130 | $370,616 | −$40,486 | −$51,764 | 3.2% |
| P36 | 23-12018 237 Street, Maple Ridge | $699,900 | $3,863 | $337,496 | $396,287 | −$58,791 | −$92,520 | 3.6% |
| P13 | 8-19240 119 Avenue, Pitt Meadows | $675,000 | $3,847 | $333,329 | $395,493 | −$62,164 | −$102,240 | 3.7% |
| P01 | 3363 Sefton Street, Port Coquitlam | $739,000 | $4,052 | $344,038 | $409,033 | −$64,995 | −$104,716 | 3.7% |
| P18 | 109-550 Seaborne Place, Port Coquitlam | $749,900 | $4,082 | $345,862 | $410,956 | −$65,094 | −$104,222 | 3.6% |
| P25 | 49-19760 55 Avenue, Langley City | $745,000 | $4,118 | $345,042 | $413,588 | −$68,546 | −$112,791 | 3.7% |
| P29 | 51-4967 220 Street, Township of Langley | $769,900 | $4,213 | $349,208 | $419,970 | −$70,762 | −$116,414 | 3.7% |
| P39 | 26-15850 85 Avenue, Surrey | $775,000 | $4,230 | $350,061 | $421,039 | −$70,978 | −$116,586 | 3.7% |
| P16 | 114-21928 48th Avenue, Township of Langley | $749,000 | $4,200 | $345,711 | $419,356 | −$73,645 | −$124,695 | 3.8% |
| P40 | 14-6945 185 Street, Surrey | $775,000 | $4,273 | $350,061 | $424,102 | −$74,041 | −$123,900 | 3.8% |
| P46 | 231 Balmoral Place, Port Moody | $748,000 | $4,207 | $345,544 | $419,871 | −$74,327 | −$126,392 | 3.9% |
| P14 | 42-19141 124 Avenue, Pitt Meadows | $734,000 | $4,208 | $343,201 | $420,134 | −$76,933 | −$133,549 | 4.0% |
| P37 | 30-13260 236 Street, Maple Ridge | $750,000 | $4,258 | $345,878 | $423,432 | −$77,554 | −$133,960 | 3.9% |
| P21 | 11-23986 104 Avenue, Maple Ridge | $749,900 | $4,265 | $345,862 | $423,930 | −$78,068 | −$135,197 | 3.9% |
| P22 | 38-11851 232 Street, Maple Ridge | $769,900 | $4,342 | $349,208 | $429,051 | −$79,843 | −$138,095 | 3.9% |
| P15 | 14-22128 48A Avenue, Township of Langley | $814,900 | $4,460 | $356,737 | $436,745 | −$80,008 | −$135,473 | 3.8% |
| P30 | 29-5515 199a Street, Langley City | $769,900 | $4,372 | $349,208 | $431,212 | −$82,004 | −$143,253 | 4.0% |
| P05 | 94-8068 207 Street, Township of Langley | $799,800 | $4,461 | $354,211 | $437,004 | −$82,793 | −$143,136 | 3.9% |
| P04 | 9-8968 208 Street, Township of Langley | $799,900 | $4,528 | $354,227 | $441,733 | −$87,506 | −$154,378 | 4.0% |
| P27 | 17-8120 200a Street, Township of Langley | $839,000 | $4,680 | $360,770 | $451,878 | −$91,108 | −$160,361 | 4.0% |
| P06 | 15669 20 Avenue, Surrey | $799,000 | $4,621 | $354,077 | $448,361 | −$94,284 | −$170,622 | 4.2% |
| P02 | 27-1338 Hames Crescent, Coquitlam | $849,999 | $4,756 | $362,610 | $457,115 | −$94,505 | −$167,735 | 4.1% |
| P33 | 17-2560 Pitt River Road, Port Coquitlam | $879,000 | $4,848 | $367,462 | $463,163 | −$95,701 | −$168,647 | 4.0% |
| P19 | 3-98 Begin Street, Coquitlam | $849,000 | $4,797 | $362,443 | $460,033 | −$97,590 | −$175,168 | 4.1% |
| P38 | 4-11282 Cottonwood Drive, Maple Ridge | $799,900 | $4,700 | $354,227 | $453,921 | −$99,694 | −$183,475 | 4.3% |
| P31 | 13-621 Langside Avenue, Coquitlam | $889,900 | $4,981 | $369,286 | $472,415 | −$103,129 | −$185,651 | 4.2% |
| P32 | 112-1225 Mitchell Street, Coquitlam | $899,000 | $5,025 | $370,809 | $475,357 | −$104,548 | −$188,430 | 4.2% |
| P34 | 40-1355 Citadel Drive, Port Coquitlam | $879,000 | $4,979 | $367,462 | $472,391 | −$104,929 | −$190,678 | 4.2% |
| P03 | 1-19236 119 Avenue, Pitt Meadows | $849,800 | $4,907 | $362,577 | $467,759 | −$105,182 | −$193,239 | 4.3% |
| P20 | 2-2990 Mariner Way, Coquitlam | $849,000 | $4,906 | $362,443 | $467,709 | −$105,266 | −$193,493 | 4.3% |
| P17 | 35-2450 Lobb Avenue, Port Coquitlam | $849,900 | $4,909 | $362,593 | $467,902 | −$105,309 | −$193,533 | 4.3% |
| P47 | 461 Carlsen Place, Port Moody | $880,000 | $5,153 | $367,630 | $484,730 | −$117,100 | −$219,670 | 4.5% |
| P09 | 6926 190 Street, Surrey | $1,099,000 | $5,987 | $404,272 | $540,332 | −$136,060 | −$250,268 | 4.3% |
| P08 | 12326 Aurora Street, Maple Ridge | $1,099,000 | $6,048 | $404,272 | $544,680 | −$140,408 | −$260,650 | 4.4% |
| P07 | 24222 103 Avenue, Maple Ridge | $1,089,000 | $6,074 | $402,599 | $546,660 | −$144,061 | −$270,041 | 4.5% |
| P12 | 4536 208 Street, Langley City | $1,099,000 | $6,728 | $404,272 | $592,703 | −$188,431 | −$375,301 | 5.1% |
| P41 | 11382 240 Street, Maple Ridge | $1,099,999 | $6,988 | $404,440 | $611,057 | −$206,617 | −$418,654 | 5.4% |
| P10 | 27191 28A Avenue, Township of Langley | $1,199,000 | $7,289 | $421,004 | $630,844 | −$209,840 | −$419,718 | 5.2% |
| P42 | 2663 275a Street, Township of Langley | $1,198,888 | $7,298 | $420,985 | $631,460 | −$210,475 | −$421,241 | 5.2% |
| P11 | 20030 48 Avenue, Langley City | $1,199,000 | $7,423 | $421,004 | $640,303 | −$219,299 | −$442,301 | 5.3% |

Seven homes have no comparison: P26, P28, P35, P44, P48, P49, P50 (strata or tax unknown, so no total). P41 and P42 now use $0 strata (detached, no strata — fixed 2026-10-25).
