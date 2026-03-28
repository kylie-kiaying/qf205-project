# models.py — AppConfig, Expense, and finance logic functions

# === Topic 15: import statements without the from clause ===
import math


# === Topic 17: Simple class definition without __init__ ===
class AppConfig:
    """Application-wide settings using class attributes.
    No __init__ method needed - all attributes are class-level defaults."""

    APP_TITLE = 'Personal Finance Calculator'        # Topic 1: string literal
    WINDOW_WIDTH = 800                               # Topic 1: integer literal
    WINDOW_HEIGHT = 650
    CURRENCY = '$'
    DEFAULT_CATEGORIES = [                           # Topic 6: list
        'Rent', 'Groceries', 'Utilities',
        'Transport', 'Entertainment', 'Phone',
        'Subscriptions', 'Dining Out', 'Other'
    ]
    THRESHOLDS = {                                   # Topic 6: dictionary
        'excellent': 30,
        'good': 20,
        'fair': 10,
    }


# === Topic 18: Class definition with __init__ ===
class Expense:
    """Represents a single expense entry."""

    def __init__(self, category, amount, is_fixed=True):  # Topic 13: default param
        self.category = category                     # Topic 2: variable assignment
        self.amount = amount
        self.is_fixed = is_fixed


# === Topic 11: Function definitions using def keyword ===
def calculate_totals(expenses):
    """Calculate total expenses from a list of Expense objects."""
    return sum(exp.amount for exp in expenses)


def assess_health(savings_rate):
    """Assess financial health based on savings rate.
    Topic 9: if statements for multi-branch decisions."""
    if savings_rate >= AppConfig.THRESHOLDS['excellent']:
        return 'Excellent', '#27AE60'                # green
    elif savings_rate >= AppConfig.THRESHOLDS['good']:
        return 'Good', '#2ECC71'
    elif savings_rate >= AppConfig.THRESHOLDS['fair']:
        return 'Fair', '#F39C12'                     # orange
    else:
        return 'Needs Attention', '#E74C3C'          # red


# === Topic 13: Function with default parameter values ===
def project_savings(monthly, months=12, raise_pct=0.0):
    """Project savings over time with optional annual raise."""
    total, current = 0, monthly                      # Topic 3: multiple assignment
    for m in range(1, months + 1):                   # Topic 8: for statement
        if m % 12 == 0 and raise_pct > 0:            # Topic 9: if statement
            current *= (1 + raise_pct)               # Topic 1: expression
        total += current
    return math.floor(total * 100) / 100


# === Topic 14: Function with *args and **kwargs ===
def add_custom_expenses(expenses, *args, **kwargs):
    """Add expenses flexibly.
    *args accepts (category, amount) tuples.
    **kwargs accepts category=amount keyword pairs."""
    result = list(expenses)                          # copy the list
    for item in args:                                # Topic 8: for loop
        if isinstance(item, tuple) and len(item) == 2:  # Topic 7: membership/comparison
            cat, amt = item                          # Topic 3: multiple assignment
            result.append(Expense(cat, amt))
    for cat, amt in kwargs.items():
        result.append(Expense(cat, amt))
    return result
