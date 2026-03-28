# ============================================================
# VERSION 1: Jupyter Notebook Exploration (Chapters 2-3)
# Personal Finance Calculator
# Topics covered: 1-7 (Literals, operators, expressions,
#   precedence, variables, assignments, comments, indentation,
#   line joining, lists, tuples, dictionaries, membership tests)
# ============================================================
# Each "Cell" section represents a separate Jupyter Notebook cell.
# Press Shift + Enter to run each cell.


# ── CHAPTER 2: USING PYTHON AS A CALCULATOR ──────────────────

# --- Cell 1 (Example 2-1): Numerical literals ---
# Topic 1: Literals, operators, expressions and operator precedence

# Integer literals - dollar amounts
5200      # monthly income
1200      # rent

# Floating-point literals - rates and percentages
0.05      # annual interest rate
100.50    # a precise dollar amount

# Using underscores for readability
800_000   # equivalent to 800000 (e.g., loan principal)


# --- Cell 2 (Example 2-2): Operator precedence ---
# Topic 1: Literals, operators, expressions and operator precedence

# Without parentheses: * is evaluated before -
5200 - 1200 + 300 * 0.1    # 5200 - 1200 + 30.0 = 4030.0
# Output: 4030.0


# --- Cell 3 (Example 2-3): Parentheses override precedence ---
# Topic 1: Operator precedence

# With parentheses: subtraction happens first
(5200 - 1200) * 0.1         # 4000 * 0.1 = 400.0
# Output: 400.0


# --- Cell 4 (Example 2-4): Monthly savings ---
# Topic 1: Expressions with operators

# Monthly income minus each expense category
5200 - 1200 - 300 - 150 - 200 - 100 - 50 - 80 - 80
# Output: 3040


# --- Cell 5 (Example 2-5): Percentage calculation ---
# Topic 1: Expressions

# Rent as a percentage of income
1200 / 5200 * 100
# Output: 23.076923076923077


# --- Cell 6 (Example 2-6): Rounding ---
# Topic 1: Expressions with built-in functions

# Use the round() function for a cleaner result
round(1200 / 5200 * 100, 2)
# Output: 23.08


# --- Cell 7 (Example 2-7): Annual projection ---
# Topic 1: Operator precedence with parentheses

# Monthly savings * 12 months
(5200 - 1200 - 300 - 150 - 200 - 100 - 50 - 80 - 80) * 12
# Output: 36480


# --- Cell 8 (Example 2-8): Comments ---
# Topic 4: Indentation and comments

# --- Personal Finance Quick Calculations ---

# Monthly budget
5200 - 2160                 # income minus total expenses

# What percentage of income goes to housing?
round(1200 / 5200 * 100, 2) # rent / income * 100

# Daily spending allowance from discretionary budget
# Discretionary = income - fixed expenses (rent + utilities)
(5200 - 1200 - 150) / 30    # divide by days in month
# Output: 128.33333333333334


# --- Cell 9 (Example 2-9): Implicit line joining ---
# Topic 5: Line joining

# Calculate total annual expenses across all categories
# Using parentheses to split across multiple lines
total_annual = (
    1200 * 12    # rent
    + 300 * 12   # groceries
    + 150 * 12   # utilities
    + 200 * 12   # transport
    + 100 * 12   # entertainment
    + 50 * 12    # phone
    + 80 * 12    # subscriptions
    + 80 * 12    # dining out
)
total_annual
# Output: 25920


# --- Cell 10 (Example 2-10): Explicit line joining ---
# Topic 5: Line joining with backslash

# The same calculation using backslash continuation
annual_savings = 5200 * 12 \
                 - 25920
annual_savings
# Output: 36480


# ── CHAPTER 3: VARIABLES AND DATA STRUCTURES ─────────────────

# --- Cell 11 (Example 3-1): Variables and simple assignment ---
# Topic 2: Variables and simple assignment statements

# Assign meaningful names to our financial values
monthly_income = 5200
rent = 1200
groceries = 300
utilities = 150
transport = 200
entertainment = 100
phone = 50
subscriptions = 80
dining = 80

# Now calculations are self-documenting
total_expenses = rent + groceries + utilities + transport + entertainment + phone + subscriptions + dining
monthly_savings = monthly_income - total_expenses

print('Total expenses: $' + str(total_expenses))
print('Monthly savings: $' + str(monthly_savings))
# Output:
# Total expenses: $2160
# Monthly savings: $3040


# --- Cell 12 (Example 3-2): Multiple assignments ---
# Topic 3: Multiple assignments

# Assign several related values at once
salary, freelance, bonus = 4800, 200, 200
monthly_income = salary + freelance + bonus
print(f'Monthly income: ${monthly_income}')

# Swap values without a temporary variable
jan_savings, feb_savings = 3040, 2850
print(f'Before swap - Jan: ${jan_savings}, Feb: ${feb_savings}')

jan_savings, feb_savings = feb_savings, jan_savings
print(f'After swap  - Jan: ${jan_savings}, Feb: ${feb_savings}')
# Output:
# Monthly income: $5200
# Before swap - Jan: $3040, Feb: $2850
# After swap  - Jan: $2850, Feb: $3040


# --- Cell 13 (Example 3-3): Lists ---
# Topic 6: Lists, tuples and dictionaries

# A list of monthly expense amounts
expense_amounts = [1200, 300, 150, 200, 100, 50, 80, 80]

# Access individual items by index (starting from 0)
print(f'First expense (rent): ${expense_amounts[0]}')
print(f'Total expenses: ${sum(expense_amounts)}')
print(f'Number of categories: {len(expense_amounts)}')

# Lists are mutable - we can modify them
expense_amounts[1] = 350    # groceries went up
print(f'Updated groceries: ${expense_amounts[1]}')

# Add a new expense
expense_amounts.append(120)  # gym membership
print(f'New total: ${sum(expense_amounts)}')
# Output:
# First expense (rent): $1200
# Total expenses: $2160
# Number of categories: 8
# Updated groceries: $350
# New total: $2330


# --- Cell 14 (Example 3-4): Tuples ---
# Topic 6: Lists, tuples and dictionaries

# Income sources are fixed for the month - use a tuple
income_sources = (4800, 200, 200)  # (salary, freelance, bonus)
total_income = sum(income_sources)
print(f'Total income: ${total_income}')

# Tuples can hold mixed types - a category-amount pair
rent_entry = ('rent', 1200)
print(f'{rent_entry[0].capitalize()}: ${rent_entry[1]}')

# Unpacking a tuple into separate variables
category, amount = rent_entry
print(f'{category}: ${amount}')
# Output:
# Total income: $5200
# Rent: $1200
# rent: $1200


# --- Cell 15 (Example 3-5): Dictionaries ---
# Topic 6: Lists, tuples and dictionaries

# Dictionary: category names -> amounts
budget = {
    'rent': 1200,
    'groceries': 300,
    'utilities': 150,
    'transport': 200,
    'entertainment': 100,
    'phone': 50,
    'subscriptions': 80,
    'dining': 80,
}

# Access by key name (much clearer than by index!)
print(f'Rent: ${budget["rent"]}')
print(f'Total expenses: ${sum(budget.values())}')
print(f'Categories: {list(budget.keys())}')

# Add a new category
budget['gym'] = 40
print(f'Updated total: ${sum(budget.values())}')
# Output:
# Rent: $1200
# Total expenses: $2160
# Categories: ['rent', 'groceries', ...]
# Updated total: $2200


# --- Cell 16 (Example 3-6): Membership tests and comparisons ---
# Topic 7: Membership test and comparison operators

budget = {'rent': 1200, 'groceries': 300, 'utilities': 150,
          'transport': 200, 'entertainment': 100}
monthly_income = 5200

# Membership test: is a category in the budget?
print('rent' in budget)           # True
print('insurance' in budget)      # False
print('insurance' not in budget)  # True

# Comparison operators
print(budget['rent'] > 1000)      # True - rent exceeds $1000
print(budget['rent'] == 1200)     # True - exact match
print(budget['rent'] != 1300)     # True - not equal to 1300

# Practical check: does rent exceed 30% of income?
rent_percentage = budget['rent'] / monthly_income * 100
print(f'Rent is {rent_percentage:.1f}% of income')
print(f'Exceeds 30%? {rent_percentage > 30}')
# Output:
# True / False / True / True / True / True
# Rent is 23.1% of income
# Exceeds 30%? False
