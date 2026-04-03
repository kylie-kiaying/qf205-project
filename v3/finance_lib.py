"""
finance_lib.py - Personal Finance Library Module
=================================================
This module provides reusable functions for personal finance calculations.
It is designed to be imported into other scripts or notebooks.

Usage:
    import finance_lib
    rate = finance_lib.compute_savings_rate(5000, 3000)

    or:

    from finance_lib import compute_savings_rate
    rate = compute_savings_rate(5000, 3000)
"""


def compute_savings_rate(income, expenses):
    """
    Compute the savings rate as a percentage.

    Parameters:
        income (float): Total monthly income.
        expenses (float): Total monthly expenses.

    Returns:
        float: The savings rate rounded to 2 decimal places.
    """
    if income <= 0:
        return 0.0
    return round((income - expenses) / income * 100, 2)


def budget_breakdown(income, budget_dict):
    """
    Compute the spending ratio for each expense category.

    Parameters:
        income (float): Total monthly income.
        budget_dict (dict): Dictionary of {category: amount}.

    Returns:
        dict: Dictionary of {category: percentage}.
    """
    result = {}
    for cat, amt in budget_dict.items():
        result[cat] = round(amt / income * 100, 2) if income > 0 else 0
    return result


def total_expenses(*args):
    """
    Compute total expenses from variable number of arguments.

    Parameters:
        *args: Variable number of expense amounts.

    Returns:
        float: Sum of all expenses.
    """
    return sum(args)


def budget_report(**kwargs):
    """
    Print a detailed budget report using keyword arguments.

    Parameters:
        **kwargs: Named expenses (e.g., Rent=1500, Food=600).

    Returns:
        float: Total of all expenses.
    """
    total = sum(kwargs.values())
    for category, amount in kwargs.items():
        ratio = round(amount / total * 100, 2) if total > 0 else 0
        print(f'{category}: ${amount} ({ratio}%)')
    return total


def financial_health(income, expenses):
    """
    Return financial health assessment based on savings rate.

    Parameters:
        income (float): Monthly income.
        expenses (float): Monthly expenses.

    Returns:
        str: Health assessment string.
    """
    savings_rate = compute_savings_rate(income, expenses)
    if savings_rate >= 50:
        return 'Excellent'
    elif savings_rate >= 30:
        return 'Good'
    elif savings_rate >= 10:
        return 'Fair'
    else:
        return 'Needs Improvement'


# Lambda expression equivalents
savings_rate_lambda = lambda income, expenses: round(
    (income - expenses) / income * 100, 2
) if income > 0 else 0


if __name__ == '__main__':
    # This block only runs when the file is executed directly
    print("Testing finance_lib.py functions:")
    print(f"Savings Rate (5000, 3000): {compute_savings_rate(5000, 3000)}%")
    print(f"Savings Rate (8000, 5500): {compute_savings_rate(8000, 5500)}%")
    print(f"Financial Health: {financial_health(5000, 3000)}")
    print(f"Lambda result: {savings_rate_lambda(5000, 3000)}%")

    budget = {'Rent': 1500, 'Food': 600, 'Transport': 300}
    print(f"\nBudget Breakdown: {budget_breakdown(5000, budget)}")
    print(f"\nTotal expenses: {total_expenses(1500, 600, 300, 200, 150, 250)}")

    print("\nBudget Report:")
    budget_report(Rent=1500, Food=600, Transport=300, Utilities=200)
