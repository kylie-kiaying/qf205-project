"""
finance_visual.py - Visual Finance Class with Plotting
========================================================
This module adds visualisation capabilities to the PersonalFinance class
by defining a child class VisualFinance.

The plot_breakdown method accepts **kwargs, allowing the caller to pass
an optional 'ax' parameter for embedding plots in a GUI.

Usage (standalone):
    from finance_visual import VisualFinance
    budget = {'Rent': 1500, 'Food': 600, 'Transport': 300,
              'Utilities': 200, 'Entertainment': 150, 'Others': 250}
    vf = VisualFinance(5000, budget)
    vf.plot_breakdown()

Usage (with GUI - passing an axes object):
    fig, ax = plt.subplots()
    vf.plot_breakdown(ax=ax)
"""

import matplotlib.pyplot as plt
from finance_lib02 import PersonalFinance


class VisualFinance(PersonalFinance):
    """Child class that adds visualisation to PersonalFinance."""

    def plot_breakdown(self, **kwargs):
        """
        Plot the expense breakdown as a bar chart.

        Parameters:
            **kwargs: Optional keyword arguments.
                      If 'ax' is provided, plot on that axes object.
                      Otherwise, create a new figure and call plt.show().
        """
        ax = kwargs.get('ax', None)
        show_plot = False

        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 5))
            show_plot = True

        cats = list(self.expenses.keys())
        amts = list(self.expenses.values())
        colours = ['#3498DB', '#2ECC71', '#E67E22',
                   '#9B59B6', '#E74C3C', '#1ABC9C']

        bars = ax.bar(cats, amts, color=colours[:len(cats)])
        ax.set_title('Expense Breakdown by Category',
                     fontsize=13, fontweight='bold', pad=12)
        ax.set_ylabel('Amount ($)')
        ax.tick_params(axis='x', rotation=0, labelsize=10)

        # Add value labels on bars
        for bar, amt in zip(bars, amts):
            ax.text(bar.get_x() + bar.get_width() / 2., bar.get_height(),
                    f'${amt:,.0f}',
                    ha='center', va='bottom', fontsize=9)

        # Add headroom so value labels are not clipped
        max_amt = max(amts) if amts else 1
        ax.set_ylim(0, max_amt * 1.15)

        if show_plot:
            plt.tight_layout()
            plt.show()


if __name__ == '__main__':
    budget = {
        'Rent': 1500, 'Food': 600, 'Transport': 300,
        'Utilities': 200, 'Entertainment': 150, 'Others': 250
    }
    vf = VisualFinance(5000, budget)
    print(f'Savings Rate: {vf.savings_rate()}%')
    print(f'Financial Health: {vf.financial_health()}')
    vf.plot_breakdown()
