"""Monthly planning costs; advertised and imputed inputs remain distinguishable."""
from mortgage_scenarios import monthly_payment


def ownership_cost_plan(p, assumptions, estimates):
    fields = estimates.get('properties', {}).get(p['id'], {})
    def amount(key):
        return p[key] if p[key] is not None else fields.get(key, {}).get('estimate')
    strata, tax = amount('strata_monthly'), amount('annual_tax')
    townhouse = 'townhouse' in p['strategy'].lower()
    apartment = 'apartment' in p['strategy'].lower()
    mortgage = monthly_payment(p['asking_price'] - assumptions['down_payment'], assumptions['annual_rate'], assumptions['amortization_years'])
    maintenance = p['asking_price'] * (.0025 if apartment else .005 if townhouse else .01) / 12
    insurance, utilities = (100, 150) if apartment else (150, 200) if townhouse else (250, 300)
    base = None if strata is None or tax is None else mortgage + strata + tax / 12 + maintenance + insurance + utilities
    rent = p['rent_model']
    return dict(mortgage=mortgage, strata=strata, annual_tax=tax, maintenance=maintenance,
                insurance=insurance, utilities=utilities, base=base,
                low=None if base is None else base - (rent['high'] if rent else 0) * .5,
                high=None if base is None else base - (rent['low'] if rent else 0) * .5,
                estimated_fields={key: value for key, value in fields.items() if isinstance(value, dict) and p.get(key) is None and 'estimate' in value})
