"""
Personal Finance Calculator - Complete GUI Application
=======================================================
This is the final version of the Personal Finance Calculator
built with PyQt5 and Matplotlib.

Requirements:
    pip install PyQt5 matplotlib

Usage:
    python personal_finance_gui.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QGridLayout,
    QGroupBox, QMessageBox
)
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# ── Finance Library Functions ──

def compute_savings_rate(income, expenses):
    """Compute the savings rate as a percentage."""
    if income <= 0:
        return 0.0
    return round((income - expenses) / income * 100, 2)


def budget_breakdown(income, budget_dict):
    """Compute the spending ratio for each category."""
    result = {}
    for cat, amt in budget_dict.items():
        result[cat] = round(amt / income * 100, 2) if income > 0 else 0
    return result


def financial_health(savings_rate):
    """Return a financial health assessment based on savings rate."""
    if savings_rate >= 50:
        return "Excellent - You're saving more than half your income!"
    elif savings_rate >= 30:
        return "Good - Healthy savings habit."
    elif savings_rate >= 10:
        return "Fair - Consider reducing some expenses."
    elif savings_rate >= 0:
        return "Needs Improvement - Try to cut discretionary spending."
    else:
        return "Warning - You're spending more than you earn!"


# ── PersonalFinance Class ──

class PersonalFinance:
    """A class to bundle personal finance data and computations."""

    def __init__(self, income, expenses_dict):
        self.income = income
        self.expenses = expenses_dict
        self.total_expenses = sum(expenses_dict.values())
        self.disposable = income - self.total_expenses

    def savings_rate(self):
        return compute_savings_rate(self.income, self.total_expenses)

    def expense_breakdown(self):
        return budget_breakdown(self.income, self.expenses)

    def health_status(self):
        return financial_health(self.savings_rate())

    def monthly_projection(self, months=12):
        """Project cumulative savings over multiple months."""
        projections = []
        for i in range(1, months + 1):
            projections.append({
                'Month': i,
                'Cumulative Savings': self.disposable * i
            })
        return projections


# ── GUI Application ──

class FinanceCalculatorGUI(QMainWindow):
    """Main window for the Personal Finance Calculator."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Personal Finance Calculator')
        self.setMinimumSize(750, 800)

        # Central widget and main layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # ── Title ──
        title = QLabel('Personal Finance Calculator')
        title.setStyleSheet(
            'font-size: 22px; font-weight: bold; '
            'color: #2C3E50; margin: 10px;'
        )
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # ── Input Section ──
        input_group = QGroupBox('Financial Inputs')
        input_group.setStyleSheet('QGroupBox { font-weight: bold; font-size: 14px; }')
        grid = QGridLayout()

        # Income input
        grid.addWidget(QLabel('Monthly Income ($):'), 0, 0)
        self.income_input = QLineEdit('5000')
        self.income_input.setStyleSheet('padding: 4px; font-size: 13px;')
        grid.addWidget(self.income_input, 0, 1)

        # Expense inputs
        self.categories = [
            'Rent', 'Food', 'Transport',
            'Utilities', 'Entertainment', 'Others'
        ]
        self.defaults = ['1500', '600', '300', '200', '150', '250']
        self.expense_inputs = {}

        for i, (cat, default) in enumerate(
            zip(self.categories, self.defaults)
        ):
            label = QLabel(f'{cat} ($):')
            self.expense_inputs[cat] = QLineEdit(default)
            self.expense_inputs[cat].setStyleSheet(
                'padding: 4px; font-size: 13px;'
            )
            grid.addWidget(label, i + 1, 0)
            grid.addWidget(self.expense_inputs[cat], i + 1, 1)

        input_group.setLayout(grid)
        main_layout.addWidget(input_group)

        # ── Compute Button ──
        btn = QPushButton('Compute Budget')
        btn.setStyleSheet(
            'font-size: 16px; padding: 10px; '
            'background-color: #3498DB; color: white; '
            'border-radius: 5px; font-weight: bold;'
        )
        btn.clicked.connect(self.compute)
        main_layout.addWidget(btn)

        # ── Results Section ──
        results_group = QGroupBox('Results')
        results_group.setStyleSheet(
            'QGroupBox { font-weight: bold; font-size: 14px; }'
        )
        results_layout = QVBoxLayout()

        self.total_label = QLabel('Total Expenses: -')
        self.disposable_label = QLabel('Disposable Income: -')
        self.rate_label = QLabel('Savings Rate: -')
        self.health_label = QLabel('Financial Health: -')

        for lbl in [self.total_label, self.disposable_label,
                     self.rate_label, self.health_label]:
            lbl.setStyleSheet('font-size: 13px; padding: 2px;')
            results_layout.addWidget(lbl)

        results_group.setLayout(results_layout)
        main_layout.addWidget(results_group)

        # ── Chart ──
        self.fig = Figure(figsize=(7, 4.5))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        main_layout.addWidget(self.canvas)

        # Initial placeholder chart
        self.ax.text(
            0.5, 0.5, 'Click "Compute Budget" to see results',
            ha='center', va='center', fontsize=14, color='gray',
            transform=self.ax.transAxes
        )
        self.ax.set_axis_off()
        self.canvas.draw()

    def compute(self):
        """Read inputs, compute finance metrics, and update display."""
        try:
            income = float(self.income_input.text())
            expenses = {}
            for cat in self.categories:
                expenses[cat] = float(self.expense_inputs[cat].text())
        except ValueError:
            QMessageBox.warning(
                self, 'Input Error',
                'Please enter valid numbers for all fields.'
            )
            return

        # Use the PersonalFinance class
        pf = PersonalFinance(income, expenses)

        # Update result labels
        self.total_label.setText(
            f'Total Expenses: ${pf.total_expenses:,.2f}'
        )
        self.disposable_label.setText(
            f'Disposable Income: ${pf.disposable:,.2f}'
        )
        self.rate_label.setText(
            f'Savings Rate: {pf.savings_rate()}%'
        )
        self.health_label.setText(
            f'Financial Health: {pf.health_status()}'
        )

        # Colour the health label based on status
        rate = pf.savings_rate()
        if rate >= 30:
            colour = '#27AE60'  # green
        elif rate >= 10:
            colour = '#F39C12'  # orange
        else:
            colour = '#E74C3C'  # red
        self.health_label.setStyleSheet(
            f'font-size: 13px; padding: 2px; '
            f'color: {colour}; font-weight: bold;'
        )

        # Update chart
        self.ax.clear()
        cats = list(expenses.keys())
        amts = list(expenses.values())
        colours = ['#3498DB', '#2ECC71', '#E67E22',
                   '#9B59B6', '#E74C3C', '#1ABC9C']
        bars = self.ax.bar(cats, amts, color=colours[:len(cats)])
        self.ax.set_title(
            'Expense Breakdown by Category',
            fontsize=13, fontweight='bold', pad=12
        )
        self.ax.set_ylabel('Amount ($)')
        self.ax.tick_params(axis='x', rotation=0, labelsize=10)

        # Add value labels on bars
        for bar, amt in zip(bars, amts):
            self.ax.text(
                bar.get_x() + bar.get_width() / 2., bar.get_height(),
                f'${amt:,.0f}',
                ha='center', va='bottom', fontsize=9
            )

        # Add headroom so value labels aren't clipped
        max_amt = max(amts) if amts else 1
        self.ax.set_ylim(0, max_amt * 1.15)

        self.fig.subplots_adjust(bottom=0.12, top=0.85, left=0.12, right=0.95)
        self.canvas.draw()


# ── Main Entry Point ──

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinanceCalculatorGUI()
    window.show()
    sys.exit(app.exec_())