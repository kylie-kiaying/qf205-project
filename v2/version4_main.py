# ============================================================
# VERSION 4 - MODULE: main.py (Chapter 6)
# Application entry point
# Topics: 14, 15, 16 (imports, *args/**kwargs)
# ============================================================

# === Example 6-3: import without the from clause ===
# Topic 15: import statements without the from clause
import math
import json

# === Example 6-4: import with the from clause ===
# Topic 16: import statements with the from clause
from version4_budget_engine import round_to_cents, save_budget, calculate_compound_savings
from version4_finance_models import Budget, BudgetConfig, ExpenseCategory, create_report


# === Topic 14: Function with *args and **kwargs ===
def add_expenses_flexible(budget_obj, *args, **kwargs):
    """Add expenses to a Budget object flexibly.
       - *args: (category, amount) tuples
       - **kwargs: category=amount pairs"""
    for item in args:                                   # Topic 8: for loop
        if isinstance(item, tuple) and len(item) == 2:  # Topic 7: membership
            category, amount = item                     # Topic 3: multiple assignment
            budget_obj.add_expense(category, amount)

    for category, amount in kwargs.items():             # Topic 8: for loop
        budget_obj.add_expense(category, amount)

    return budget_obj


# === Example 6-5: Running the modular application ===
if __name__ == '__main__':
    # Create a budget using the Budget class (Topic 18: __init__)
    my_budget = Budget(5200, {
        'rent': 1200,
        'groceries': 300,
        'utilities': 150,
        'transport': 200,
        'entertainment': 100,
    })

    # Add more expenses using *args and **kwargs (Topic 14)
    my_budget = add_expenses_flexible(
        my_budget,
        ('phone', 50),                              # positional tuple arg
        ('subscriptions', 80),                       # positional tuple arg
        dining=120,                                  # keyword arg
        gym=40,                                      # keyword arg
    )

    # Print summary (uses class methods, for loops, if statements)
    print(my_budget.summary())

    # Show high expenses (Topic 10: list comprehension inside class)
    print('\nHigh expenses (over $100):')
    for exp in my_budget.get_high_expenses():        # Topic 8: for loop
        print(f'  {exp}')

    # Create and display report (Topic 19: demonstrates scopes)
    print()
    create_report(my_budget)

    # Financial health assessment
    rate = my_budget.savings_rate()
    config = BudgetConfig()                          # Topic 17: class without __init__
    if rate >= config.savings_target:                 # Topic 9: if statement
        print(f'\nYou\'re meeting your {config.savings_target}% savings target!')
    else:
        print(f'\nYou\'re below your {config.savings_target}% savings target.')

    # Savings projections (Topic 15: uses math module)
    savings = my_budget.savings()
    print(f'\n--- Savings Projections ---')
    print(f'1-year (simple):    ${savings * 12:,.2f}')
    print(f'1-year (compound):  ${calculate_compound_savings(savings, 0.05, 1):,.2f}')
    print(f'5-year (compound):  ${calculate_compound_savings(savings, 0.05, 5):,.2f}')

    # Save to file (Topic 15: uses json and datetime modules)
    budget_dict = {                                  # Topic 10: dict comprehension
        name: exp.amount
        for name, exp in my_budget.expenses.items()
    }
    save_budget(budget_dict, 'my_budget.json')

    # Use math module directly (Topic 15: import without from)
    annual_savings = savings * 12
    print(f'\nAnnual savings (rounded down): ${math.floor(annual_savings):,}')
    print(f'Annual savings (rounded up):   ${math.ceil(annual_savings):,}')
