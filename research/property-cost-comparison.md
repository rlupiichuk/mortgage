# First property sample: cost comparison

Observed 2026-10-25. Asking-price research examples, not confirmed available homes or recommendations.

$250,000 down; 4.75% nominal interest compounded semi-annually; 25-year amortization. No lender approval implied. New-home GST and any rebates are excluded until verified.

The known-cost subtotal includes mortgage, advertised strata fees and advertised tax/12 ONLY where both are available. It excludes insurance, utilities, owner maintenance, special levies and rental tax. Historical tax years and advertised strata fees need refreshing. Unknown is not zero.

After-rent figures count 75% of exploratory asking rent; this allowance is not an itemized expense/tax model. They cover mortgage only. No rent is counted for unfinished, merely potential or wet-bar configurations.

The HTML total-expense column and CSV total_expenses fields use the broader ownership model: mortgage + property tax + strata + maintenance + insurance + utilities, minus 50% of modelled gross rent. Missing inputs use a labelled matched-advertisement mean from cost-estimates.json where available. The older mortgage-only sensitivity table below retains its separate 75% rent allowance.

| ID | Address | Asking | Mortgage/month | Strata/month | Tax/year | Known-cost subtotal/month | Mortgage after rental allowance |
|---|---|---:|---:|---:|---:|---:|---|
| P01 | [3363 Sefton Street](https://www.google.com/maps/search/?api=1&query=3363+Sefton+Street%2C+Port+Coquitlam%2C+BC%2C+Canada) | $739,000 | $2,775 | $370 | $2,991 | $3,394 | not modelled |
| P02 | [27-1338 Hames Crescent](https://www.google.com/maps/search/?api=1&query=27-1338+Hames+Crescent%2C+Coquitlam%2C+BC%2C+Canada) | $849,999 | $3,405 | $367 | $3,360 | $4,052 | not modelled |
| P03 | [1-19236 119 Avenue](https://www.google.com/maps/search/?api=1&query=1-19236+119+Avenue%2C+Pitt+Meadows%2C+BC%2C+Canada) | $849,800 | $3,404 | $400 | $4,789 | $4,203 | not modelled |
| P04 | [9-8968 208 Street](https://www.google.com/maps/search/?api=1&query=9-8968+208+Street%2C+Township+of+Langley%2C+BC%2C+Canada) | $799,900 | $3,120 | $481 | $2,912 | $3,844 | not modelled |
| P05 | [94-8068 207 Street](https://www.google.com/maps/search/?api=1&query=94-8068+207+Street%2C+Township+of+Langley%2C+BC%2C+Canada) | $799,800 | $3,120 | $400 | $3,092 | $3,778 | not modelled |
| P06 | [15669 20 Avenue](https://www.google.com/maps/search/?api=1&query=15669+20+Avenue%2C+Surrey%2C+BC%2C+Canada) | $799,000 | $3,115 | unknown | $3,483 | unknown | not modelled |
| P07 | [24222 103 Avenue](https://www.google.com/maps/search/?api=1&query=24222+103+Avenue%2C+Maple+Ridge%2C+BC%2C+Canada) | $1,089,000 | $4,761 | $0 | $6,970 | $5,342 | $3,523–$3,823 |
| P08 | [12326 Aurora Street](https://www.google.com/maps/search/?api=1&query=12326+Aurora+Street%2C+Maple+Ridge%2C+BC%2C+Canada) | $1,099,000 | $4,818 | $0 | $5,879 | $5,308 | $3,580–$3,880 |
| P09 | [6926 190 Street](https://www.google.com/maps/search/?api=1&query=6926+190+Street%2C+Surrey%2C+BC%2C+Canada) | $1,099,000 | $4,818 | $0 | $5,065 | $5,240 | $3,711–$3,768 |
| P10 | [27191 28A Avenue](https://www.google.com/maps/search/?api=1&query=27191+28A+Avenue%2C+Township+of+Langley%2C+BC%2C+Canada) | $1,199,000 | $5,385 | $0 | $4,260 | $5,740 | not modelled |
| P11 | [20030 48 Avenue](https://www.google.com/maps/search/?api=1&query=20030+48+Avenue%2C+Langley+City%2C+BC%2C+Canada) | $1,199,000 | $5,385 | $0 | $5,867 | $5,874 | not modelled |
| P12 | [4536 208 Street](https://www.google.com/maps/search/?api=1&query=4536+208+Street%2C+Langley+City%2C+BC%2C+Canada) | $1,099,000 | $4,818 | $0 | $5,336 | $5,262 | not modelled |

## Mortgage sensitivity

| Purchase price | 4.75%, 25 years | 5.75%, 25 years | 4.75%, 30 years |
|---|---:|---:|---:|
| $800,000 | $3,121 | $3,438 | $2,854 |
| $850,000 | $3,405 | $3,750 | $3,113 |
| $1,100,000 | $4,823 | $5,313 | $4,410 |
| $1,200,000 | $5,391 | $5,938 | $4,929 |

The 30-year illustration does not establish lender eligibility or equal pricing. A longer amortization reduces monthly payments but increases interest at an unchanged rate over the full repayment period.

For sources, availability caveats, suite classifications, tax years and next checks, use [the sample data](property-sample.json) and [screening notes](property-sample-notes.md).
