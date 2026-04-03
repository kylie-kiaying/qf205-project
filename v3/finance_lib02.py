"""
finance_lib02.py - Personal Finance Library with Classes
=========================================================
This module provides a class-based approach to personal finance calculations.

Usage:
    from finance_lib02 import PersonalFinance

    budget = {'Rent': 1500, 'Food': 600, 'Transport': 300,
              'Utilities': 200, 'Entertainment': 150, 'Others': 250}
    pf = PersonalFinance(5000, budget)
    print(f'Savings Rate: {pf.savings_rate()}%')
"""

import pandas


def compute_savings_rate(income, expenses):
    """Compute savings rate as a percentage."""
    if income <= 0:
        return 0.0
    return round((income - expenses) / income * 100, 2)


class PersonalFinance:
    """A class to bundle personal finance data and computations."""

    def __init__(self, income, expenses_dict):
        self.income = income
        self.expenses = expenses_dict
        self.total_expenses = sum(expenses_dict.values())
        self.disposable = self.income - self.total_expenses

    def savings_rate(self):
        """Compute and return the savings rate."""
        return compute_savings_rate(self.income, self.total_expenses)

    def expense_breakdown(self):
        """Compute spending ratio for each category."""
        result = {}
        for cat, amt in self.expenses.items():
            result[cat] = round(amt / self.income * 100, 2) if self.income > 0 else 0
        return result

    def monthly_summary(self, months=12):
        """
        Generate a DataFrame showing cumulative savings over months.

        Parameters:
            months (int): Number of months to project (default: 12).

        Returns:
            pandas.DataFrame: Monthly savings projection.
        """
        data = {
            'Month': list(range(1, months + 1)),
            'Monthly Saving ($)': [self.disposable] * months,
            'Cumulative Savings ($)': [self.disposable * i for i in range(1, months + 1)]
        }
        return pandas.DataFrame(data)

    def financial_health(self):
        """Return a financial health assessment string."""
        rate = self.savings_rate()
        if rate >= 50:
            return 'Excellent'
        elif rate >= 30:
            return 'Good'
        elif rate >= 10:
            return 'Fair'
        else:
            return 'Needs Improvement'


if __name__ == '__main__':
    budget = {
        'Rent': 1500, 'Food': 600, 'Transport': 300,
        'Utilities': 200, 'Entertainment': 150, 'Others': 250
    }
    pf = PersonalFinance(5000, budget)

    print(f'Income: ${pf.income}')
    print(f'Total Expenses: ${pf.total_expenses}')
    print(f'Disposable Income: ${pf.disposable}')
    print(f'Savings Rate: {pf.savings_rate()}%')
    print(f'Financial Health: {pf.financial_health()}')
    print(f'\nExpense Breakdown: {pf.expense_breakdown()}')
    print(f'\nMonthly Summary:')
    print(pf.monthly_summary(6))
