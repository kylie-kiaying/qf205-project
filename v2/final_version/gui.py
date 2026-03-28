# FinanceCalculator main window (PyQt5)

# === Topic 16: import statements with the from clause ===
# === Topic 5: Line joining (implicit, inside parentheses) ===
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QGroupBox, QComboBox, QHeaderView
)
from PyQt5.QtGui import QFont

from models import (
    AppConfig, Expense,
    calculate_totals, assess_health, project_savings, add_custom_expenses
)

# ══════════════════════════════════════════════════════════════
# Topic 20: GUI Development
# ══════════════════════════════════════════════════════════════

class FinanceCalculator(QMainWindow):
    """Main application window.
    Topic 18: Class with __init__ for instance initialization."""

    def __init__(self):
        super().__init__()
        self.expenses = []                           # Topic 6: list
        self.setWindowTitle(AppConfig.APP_TITLE)
        self.setMinimumSize(AppConfig.WINDOW_WIDTH, AppConfig.WINDOW_HEIGHT)
        self.init_ui()

    def init_ui(self):
        """Build the user interface with widgets and layouts."""
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(10)

        # ── Income Section ──
        income_group = QGroupBox('Monthly Income')
        income_layout = QHBoxLayout()
        income_layout.addWidget(QLabel('Income ($):'))
        self.income_input = QLineEdit()
        self.income_input.setPlaceholderText('e.g. 5200')
        income_layout.addWidget(self.income_input)
        income_group.setLayout(income_layout)
        main_layout.addWidget(income_group)

        # ── Add Expense Section ──
        expense_group = QGroupBox('Add Expense')
        expense_layout = QHBoxLayout()

        self.category_combo = QComboBox()
        self.category_combo.addItems(AppConfig.DEFAULT_CATEGORIES)  # Topic 6: list
        self.category_combo.setEditable(True)
        expense_layout.addWidget(QLabel('Category:'))
        expense_layout.addWidget(self.category_combo)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText('Amount')
        expense_layout.addWidget(QLabel('Amount ($):'))
        expense_layout.addWidget(self.amount_input)

        add_btn = QPushButton('Add Expense')
        add_btn.clicked.connect(self.add_expense)    # event handling
        expense_layout.addWidget(add_btn)

        expense_group.setLayout(expense_layout)
        main_layout.addWidget(expense_group)

        # ── Expense Table ──
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(['Category', 'Amount', '% of Income'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        # ── Buttons Row ──
        btn_layout = QHBoxLayout()

        calc_btn = QPushButton('Calculate Summary')
        calc_btn.clicked.connect(self.calculate)
        btn_layout.addWidget(calc_btn)

        clear_btn = QPushButton('Clear All')
        clear_btn.clicked.connect(self.clear_all)
        btn_layout.addWidget(clear_btn)

        # Topic 12: Lambda expression for event handling
        sample_btn = QPushButton('Load Sample Data')
        sample_btn.clicked.connect(
            lambda: self.load_sample()               # lambda expression
        )
        btn_layout.addWidget(sample_btn)

        main_layout.addLayout(btn_layout)

        # ── Results Display ──
        results_group = QGroupBox('Financial Summary')
        results_layout = QGridLayout()

        self.result_labels = {}                      # Topic 6: dictionary
        labels = ('Total Expenses', 'Monthly Savings',
                  'Savings Rate', 'Health Status',
                  '1-Year Projection', '2-Year Projection')  # Topic 6: tuple

        for i, name in enumerate(labels):            # Topic 8: for statement
            results_layout.addWidget(QLabel(f'{name}:'), i, 0)
            value_label = QLabel('--')
            value_label.setFont(QFont('Arial', 11, QFont.Bold))
            results_layout.addWidget(value_label, i, 1)
            self.result_labels[name] = value_label

        results_group.setLayout(results_layout)
        main_layout.addWidget(results_group)

    def add_expense(self):
        """Add an expense from the input fields."""
        category = self.category_combo.currentText().strip()
        amount_text = self.amount_input.text().strip()

        # Topic 9: if statements for validation
        if not category or not amount_text:
            QMessageBox.warning(self, 'Input Error',
                                'Please enter both category and amount.')
            return

        try:
            amount = float(amount_text)
            if amount <= 0:                          # Topic 7: comparison operator
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, 'Input Error',
                                'Please enter a valid positive number.')
            return

        # Topic 7: membership test + Topic 10: list comprehension
        existing = [
            i for i, exp in enumerate(self.expenses)
            if exp.category.lower() == category.lower()
        ]

        if existing:                                 # Topic 9: if statement
            self.expenses[existing[0]].amount = amount  # update existing
        else:
            self.expenses.append(Expense(category, amount))  # add new

        self.update_table()
        self.amount_input.clear()

    def update_table(self):
        """Refresh the expense table display."""
        self.table.setRowCount(len(self.expenses))
        income = self.get_income()

        for row, exp in enumerate(self.expenses):    # Topic 8: for statement
            self.table.setItem(row, 0, QTableWidgetItem(exp.category))
            self.table.setItem(
                row, 1,
                QTableWidgetItem(f'{AppConfig.CURRENCY}{exp.amount:,.2f}')
            )
            if income > 0:                           # Topic 9: if statement
                pct = exp.amount / income * 100      # Topic 1: expression
                self.table.setItem(
                    row, 2, QTableWidgetItem(f'{pct:.1f}%')
                )

    def get_income(self):
        """Safely parse income input."""
        try:
            return float(self.income_input.text())
        except ValueError:
            return 0.0

    def calculate(self):
        """Calculate and display the full financial summary."""
        income = self.get_income()
        if income <= 0:
            QMessageBox.warning(self, 'Input Error',
                                'Please enter a valid income first.')
            return

        if not self.expenses:
            QMessageBox.warning(self, 'No Data',
                                'Please add at least one expense.')
            return

        # Use standalone functions (Topic 11: def)
        total = calculate_totals(self.expenses)
        savings = income - total                     # Topic 1: expression
        rate = (savings / income) * 100 if income > 0 else 0
        status, color = assess_health(rate)          # Topic 3: multiple assignment

        # Projections using default parameters (Topic 13)
        proj_1yr = project_savings(savings)          # uses default 12 months, 0% raise
        proj_2yr = project_savings(savings, 24, 0.05)  # 24 months, 5% raise

        # Update display
        c = AppConfig.CURRENCY                       # Topic 2: variable assignment
        self.result_labels['Total Expenses'].setText(f'{c}{total:,.2f}')
        self.result_labels['Monthly Savings'].setText(f'{c}{savings:,.2f}')
        self.result_labels['Savings Rate'].setText(f'{rate:.1f}%')
        self.result_labels['Health Status'].setText(status)
        self.result_labels['Health Status'].setStyleSheet(
            f'color: {color}; font-weight: bold;'
        )
        self.result_labels['1-Year Projection'].setText(f'{c}{proj_1yr:,.2f}')
        self.result_labels['2-Year Projection'].setText(f'{c}{proj_2yr:,.2f}')

        self.update_table()

        # Flag high expenses (Topic 10: list comprehension + Topic 7: comparison)
        high = [
            exp.category for exp in self.expenses
            if exp.amount / income * 100 > 15
        ]
        if high:                                     # Topic 9: if statement
            QMessageBox.information(
                self, 'Budget Alert',
                f'High spending categories (>15% of income):\n'
                + ', '.join(high)                    # Topic 5: line joining
            )

    def load_sample(self):
        """Load sample budget data for demonstration."""
        self.income_input.setText('5200')
        self.expenses = []
        sample = {                                   # Topic 6: dictionary
            'Rent': 1200, 'Groceries': 300,
            'Utilities': 150, 'Transport': 200,
            'Entertainment': 100, 'Phone': 50,
            'Subscriptions': 80, 'Dining Out': 120,
        }
        for cat, amt in sample.items():              # Topic 8: for loop
            self.expenses.append(Expense(cat, amt))

        # Topic 14: *args and **kwargs in action
        self.expenses = add_custom_expenses(
            self.expenses,
            ('Gym', 40),                             # *args (positional tuple)
            Insurance=120,                           # **kwargs (keyword argument)
        )
        self.update_table()

    def clear_all(self):
        """Reset all inputs and results."""
        self.expenses = []
        self.income_input.clear()
        self.table.setRowCount(0)
        for label in self.result_labels.values():    # Topic 8: for loop
            label.setText('--')
            label.setStyleSheet('')
