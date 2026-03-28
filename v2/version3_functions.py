# ============================================================
# VERSION 3: Standalone Script with Functions (Chapter 5)
# finance_calculator.py
# Topics covered: 11-14, 19 (def, lambda, default params,
#   *args/**kwargs, scopes and namespaces)
# ============================================================


# === Global scope variables ===
# Topic 19: Scopes and namespaces
DEFAULT_CURRENCY = '$'
APP_VERSION = '3.0'


# === Example 5-2: Function definition using def ===
# Topic 11: Function definition using def keyword

def calculate_savings_rate(income, expenses):
    """Calculate savings rate as a percentage of income."""
    savings = income - expenses
    rate = (savings / income) * 100
    return round(rate, 1)


# === Example 5-3: More finance functions ===
# Topic 11: Function definition using def keyword

def calculate_total(budget):
    """Sum all values in a budget dictionary."""
    total = 0
    for amount in budget.values():
        total += amount
    return total


def assess_health(savings_rate):
    """Return status and advice based on savings rate."""
    if savings_rate >= 30:
        return 'Excellent', 'Consider investing the surplus.'
    elif savings_rate >= 20:
        return 'Good', 'Maintain this rate consistently.'
    elif savings_rate >= 10:
        return 'Fair', 'Try reducing discretionary spending.'
    else:
        return 'Needs Attention', 'Review expenses urgently.'


# === Example 5-4: Scopes and namespaces ===
# Topic 19: Scopes and namespaces

def create_report(budget, income):
    """Demonstrates local vs enclosing vs global scope."""

    # Local scope: report_title exists only inside this function
    report_title = 'Monthly Finance Report'

    def format_amount(amount):
        # Accesses DEFAULT_CURRENCY from global scope
        return f'{DEFAULT_CURRENCY}{amount:,.2f}'

    def format_header():
        # Accesses report_title from enclosing scope
        # Accesses APP_VERSION from global scope
        return f'=== {report_title} (v{APP_VERSION}) ==='

    total = calculate_total(budget)
    savings = income - total
    print(format_header())
    print(f'Total expenses: {format_amount(total)}')
    print(f'Savings: {format_amount(savings)}')


# === Example 5-5: Lambda expressions ===
# Topic 12: Function definition using lambda expressions

def generate_sorted_report(budget, income):
    """Generate a sorted budget report using lambda for sorting."""
    # Lambda to convert an amount to a percentage of income
    to_percentage = lambda amount: round(amount / income * 100, 1)

    # Lambda as a sort key: sort budget by amount (highest first)
    sorted_budget = sorted(
        budget.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print(f'\n{DEFAULT_CURRENCY} Monthly Income: {income:,.2f}')
    print('Expenses ranked by amount:')
    for cat, amt in sorted_budget:
        pct = to_percentage(amt)
        print(f'  {cat:15s} ${amt:>8,.2f}  ({pct}%)')

    total = calculate_total(budget)
    print(f'\n  {"TOTAL":15s} ${total:>8,.2f}')
    print(f'  {"SAVINGS":15s} ${income - total:>8,.2f}')
    return income - total


# === Example 5-6: Functions with default parameter values ===
# Topic 13: Function definition with default parameter values

def project_savings(monthly_savings, months=12, annual_raise=0.0):
    """Project total savings over a period.

    Args:
        monthly_savings: Current monthly savings amount.
        months: Number of months to project (default: 12).
        annual_raise: Annual salary increase as decimal (default: 0.0).
    """
    total = 0
    current = monthly_savings
    for month in range(1, months + 1):
        if month % 12 == 0 and annual_raise > 0:
            current *= (1 + annual_raise)
        total += current
    return round(total, 2)


# === Example 5-7: Functions with *args and **kwargs ===
# Topic 14: Function definition with *args, **kwargs or both

def add_expenses(budget, *args, **kwargs):
    """Add expenses to a budget dictionary.

    *args:   (category, amount) tuples
    **kwargs: category=amount keyword pairs
    """
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


# === Example 5-8: Main block ===
# Topic 19: Scopes (__name__ guard uses module namespace)

if __name__ == '__main__':
    budget = {
        'rent': 1200, 'groceries': 300, 'utilities': 150,
        'transport': 200, 'entertainment': 100,
        'phone': 50, 'subscriptions': 80, 'dining': 80,
    }
    income = 5200

    # Add extra expenses using *args and **kwargs (Topic 14)
    budget = add_expenses(budget, ('gym', 40), insurance=120)

    # Generate sorted report using lambda (Topic 12)
    savings = generate_sorted_report(budget, income)

    # Assess financial health (Topic 11: def functions)
    rate = calculate_savings_rate(income, calculate_total(budget))
    status, advice = assess_health(rate)    # Topic 3: multiple assignment
    print(f'\nStatus: {status} | {advice}')

    # Create report demonstrating scopes (Topic 19)
    print()
    create_report(budget, income)

    # Project future savings (Topic 13: default parameter values)
    print(f'\n--- Savings Projections ---')
    print(f'1-year, no raise:     ${project_savings(savings):>10,.2f}')
    print(f'2-year, no raise:     ${project_savings(savings, 24):>10,.2f}')
    print(f'2-year, 5% raise:     ${project_savings(savings, 24, 0.05):>10,.2f}')
    print(f'1-year, 3% raise:     ${project_savings(savings, annual_raise=0.03):>10,.2f}')
