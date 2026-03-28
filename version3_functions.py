# ============================================================
# VERSION 3: Standalone Script with Functions
# Personal Finance Calculator - def, lambda, defaults, *args/**kwargs
# ============================================================


# --- Topic 11: Function definition using def keyword ---

def calculate_total_expenses(budget):
    """Calculate the sum of all expenses in the budget dictionary."""
    total = 0
    for amount in budget.values():
        total += amount
    return total


def calculate_savings(income, expenses):
    """Return the difference between income and total expenses."""
    return income - expenses


def get_savings_rate(savings, income):
    """Calculate savings as a percentage of income."""
    if income == 0:
        return 0.0
    return (savings / income) * 100


def assess_financial_health(savings_rate):
    """Return a status and advice based on the savings rate."""
    if savings_rate >= 30:
        return "Excellent", "Consider investing the surplus."
    elif savings_rate >= 20:
        return "Good", "Maintain this rate consistently."
    elif savings_rate >= 10:
        return "Fair", "Try reducing discretionary spending."
    else:
        return "Needs Attention", "Review expenses urgently."


# --- Topic 12: Function definition using lambda expressions ---

def generate_report(budget, income):
    """Generate a sorted budget report using lambda for sorting."""
    total_exp = calculate_total_expenses(budget)
    savings = calculate_savings(income, total_exp)

    # Lambda to calculate percentage of income
    to_percentage = lambda amount: round(amount / income * 100, 1)

    # Sort categories by amount (highest first) using lambda as sort key
    sorted_budget = sorted(
        budget.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n=== Personal Finance Report ===")
    print(f"Monthly Income: ${income:,.2f}\n")

    for category, amount in sorted_budget:
        pct = to_percentage(amount)
        print(f"  {category.capitalize():15s} ${amount:>8,.2f}  ({pct}%)")

    print(f"\n  {'TOTAL EXPENSES':15s} ${total_exp:>8,.2f}")
    print(f"  {'SAVINGS':15s} ${savings:>8,.2f}")

    return savings


# --- Topic 13: Function definition with default parameter values ---

def project_savings(monthly_savings, months=12, annual_raise=0.0):
    """Project future savings with optional raise percentage.

    Args:
        monthly_savings: Current monthly savings amount.
        months: Number of months to project (default: 12).
        annual_raise: Expected annual salary raise as decimal (default: 0.0).
    """
    total = 0
    current = monthly_savings
    for month in range(1, months + 1):
        if month % 12 == 0 and annual_raise > 0:
            current *= (1 + annual_raise)
        total += current
    return round(total, 2)


# --- Topic 14: Function definition with *args, **kwargs or both ---

def add_expenses(budget, *args, **kwargs):
    """Add expenses to the budget. Accepts:
       - Positional args as (category, amount) tuples
       - Keyword args as category=amount pairs."""
    updated = budget.copy()

    # Process positional arguments (tuples)
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            category, amount = item
            updated[category] = amount

    # Process keyword arguments
    for category, amount in kwargs.items():
        updated[category] = amount

    return updated


# --- Putting it all together ---

if __name__ == "__main__":
    budget = {
        "rent": 1200, "groceries": 300, "utilities": 150,
        "transport": 200, "entertainment": 100,
        "phone": 50, "subscriptions": 80,
    }
    income = 5200

    # Add extra expenses flexibly (Topic 14: *args and **kwargs)
    budget = add_expenses(budget, ("gym", 40), insurance=120)

    # Generate the report (Topic 12: lambda used inside)
    savings = generate_report(budget, income)

    # Assess financial health (Topic 11: def functions)
    rate = get_savings_rate(savings, income)
    status, advice = assess_financial_health(rate)  # Topic 3: multiple assignment
    print(f"\nStatus: {status} | {advice}")

    # Project future savings (Topic 13: default parameter values)
    print(f"\n--- Savings Projections ---")
    print(f"1-year projection:              ${project_savings(savings):,.2f}")
    print(f"2-year projection:              ${project_savings(savings, 24):,.2f}")
    print(f"2-year (with 5% raise):         ${project_savings(savings, 24, 0.05):,.2f}")
    print(f"1-year (3% raise, named arg):   ${project_savings(savings, annual_raise=0.03):,.2f}")
