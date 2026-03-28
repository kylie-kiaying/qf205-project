# ============================================================
# VERSION 4 - MODULE: finance_models.py (Chapter 6)
# Data models: classes with and without __init__
# Topics: 17, 18, 19 (classes, scopes and namespaces)
# ============================================================


# === Example 6-1: Simple class without __init__ ===
# Topic 17: Simple class definition without the __init__ method

class BudgetConfig:
    """Configuration for budget analysis.
    Class attributes are shared across all instances.
    No __init__ method needed - all attributes are class-level defaults."""

    # Class attributes (shared by all instances)
    currency = '$'
    savings_target = 20.0        # target savings rate percentage
    rent_threshold = 30.0        # max recommended rent % of income
    categories = [               # default expense categories
        'rent', 'groceries', 'utilities',
        'transport', 'entertainment'
    ]

    def get_threshold_message(self, category, percentage):
        """Check if a category exceeds recommended thresholds."""
        if category == 'rent' and percentage > self.rent_threshold:
            return (
                f'Warning: Rent is {percentage:.1f}% of income '
                f'(recommended: under {self.rent_threshold}%)'
            )
        return None


# === Example 6-2: Classes with __init__ ===
# Topic 18: Class definition with the __init__ method

class ExpenseCategory:
    """Represents a single expense category."""

    def __init__(self, name, amount, is_fixed=True):  # Topic 13: default param
        self.name = name
        self.amount = amount
        self.is_fixed = is_fixed    # fixed vs variable expense

    def annualize(self):
        """Calculate annual cost."""
        return self.amount * 12

    def __repr__(self):
        kind = 'fixed' if self.is_fixed else 'variable'
        return f"ExpenseCategory('{self.name}', ${self.amount}, {kind})"


class Budget:
    """Complete budget with income and categorised expenses."""

    def __init__(self, income, expenses=None):         # Topic 13: default param
        self.income = income
        self.expenses = {}                              # Topic 6: dictionary
        self.config = BudgetConfig()                    # Topic 17: uses config class

        if expenses:                                    # Topic 9: if statement
            for name, amount in expenses.items():       # Topic 8: for statement
                self.add_expense(name, amount)

    def add_expense(self, name, amount, is_fixed=True):
        """Add an expense category to the budget."""
        self.expenses[name] = ExpenseCategory(name, amount, is_fixed)

    def total_expenses(self):
        """Calculate total of all expenses."""
        return sum(exp.amount for exp in self.expenses.values())

    def savings(self):
        """Calculate monthly savings."""
        return self.income - self.total_expenses()

    def savings_rate(self):
        """Calculate savings rate as percentage."""
        if self.income == 0:                            # Topic 7: comparison
            return 0.0
        return (self.savings() / self.income) * 100     # Topic 1: expression

    def get_high_expenses(self, threshold=100):         # Topic 13: default param
        """Return expenses above a threshold using list comprehension."""
        return [                                        # Topic 10: list comprehension
            exp for exp in self.expenses.values()
            if exp.amount > threshold                   # Topic 7: comparison
        ]

    def summary(self):
        """Generate a complete budget summary."""
        sorted_expenses = sorted(
            self.expenses.values(),
            key=lambda e: e.amount,                     # Topic 12: lambda
            reverse=True
        )

        lines = []
        lines.append(f'\nIncome: {self.config.currency}{self.income:,.2f}')
        lines.append('Expenses:')
        for exp in sorted_expenses:                     # Topic 8: for statement
            pct = (exp.amount / self.income) * 100
            lines.append(f'  {exp.name:15s} {self.config.currency}{exp.amount:>8,.2f}  ({pct:.1f}%)')
            warning = self.config.get_threshold_message(exp.name, pct)
            if warning:                                 # Topic 9: if statement
                lines.append(f'    ^ {warning}')

        lines.append(f'\nTotal Expenses: {self.config.currency}{self.total_expenses():,.2f}')
        lines.append(f'Savings: {self.config.currency}{self.savings():,.2f} ({self.savings_rate():.1f}%)')
        return '\n'.join(lines)


# === Example 5-4 (revisited): Scopes and namespaces ===
# Topic 19: Scopes and namespaces

# Global scope: accessible everywhere in this module
APP_VERSION = '4.0'
DEFAULT_CURRENCY = '$'


def create_report(budget):
    """Demonstrates local vs enclosing vs global scope."""

    # Local scope: 'report_title' exists only inside this function
    report_title = 'Monthly Finance Report'

    def format_amount(amount):
        # Enclosing scope: could access report_title
        # Global scope: accesses DEFAULT_CURRENCY from module level
        return f'{DEFAULT_CURRENCY}{amount:,.2f}'

    def format_header():
        # Accesses 'report_title' from enclosing scope
        # Accesses 'APP_VERSION' from global scope
        return f'=== {report_title} (v{APP_VERSION}) ==='

    # Use the nested functions
    print(format_header())
    print(f'Total: {format_amount(budget.total_expenses())}')
    print(f'Savings: {format_amount(budget.savings())}')
