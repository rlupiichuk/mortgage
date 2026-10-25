"""Illustrative CAD mortgage scenarios; run with Python 3, no dependencies.

Canadian nominal annual rate compounded semi-annually, monthly payments.
Does not model lender approval, taxes, mortgage insurance or ownership expenses.
Edit the explicit assumptions below to refresh scenarios.
"""

DOWN_PAYMENT = 250_000
ANNUAL_RATE = 0.0475
AMORTIZATION_YEARS = 25
PERSONAL_MORTGAGE_TARGET = 3_500
RENT_COUNTED_FRACTION = 0.75  # Planning allowance, not lender or tax policy.
PURCHASE_PRICES = (850_000, 1_000_000, 1_100_000, 1_200_000, 1_250_000)


def monthly_payment(principal, annual_rate, years):
    months = years * 12
    monthly_rate = (1 + annual_rate / 2) ** (1 / 6) - 1
    if monthly_rate == 0:
        return principal / months
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)


if __name__ == "__main__":
    print(f"Down payment ${DOWN_PAYMENT:,.0f}; rate {ANNUAL_RATE:.2%}; "
          f"amortization {AMORTIZATION_YEARS} years")
    print("Required rents are hypothetical, before income tax; ownership costs extra.")
    print("Price,Principal,Monthly mortgage,Required gross monthly rent")
    for price in PURCHASE_PRICES:
        principal = price - DOWN_PAYMENT
        payment = monthly_payment(principal, ANNUAL_RATE, AMORTIZATION_YEARS)
        required_rent = max(0, payment - PERSONAL_MORTGAGE_TARGET) / RENT_COUNTED_FRACTION
        print(f"{price:.0f},{principal:.0f},{payment:.0f},{required_rent:.0f}")
