# ============================================================
# VERSION 1: Exploring with Jupyter Notebook
# Personal Finance Calculator - Basic Expressions & Variables
# ============================================================
# This version simulates Jupyter Notebook cells.
# Each "Cell" section represents a separate notebook cell.

# --- Cell 1: Using Python as a calculator with literals and operators ---
# Topic 1: Literals, operators, expressions and operator precedence

# Calculate monthly balance using literal values directly
# Monthly income (salary after tax)
5000 - 1200 - 300 - 150 - 200 - 100  # income minus all expenses
# Output: 3050


# --- Cell 2: Operator precedence in action ---
# Topic 1: Literals, operators, expressions and operator precedence

# Calculate weekly discretionary spending
(5000 - 1200 - 300 - 150) * 12 / 52   # annual to weekly conversion
# Output: 773.08

# Percentage of income spent on rent
1200 / 5000 * 100  # division happens before multiplication (left to right)
# Output: 24.0


# --- Cell 3: Variables and simple assignment statements ---
# Topic 2: Variables and simple assignment statements
# Topic 4: Indentation and comments

monthly_income = 5000
rent = 1200
groceries = 300
utilities = 150
transport = 200
entertainment = 100

# Calculate savings using variables instead of raw numbers
total_expenses = rent + groceries + utilities + transport + entertainment
monthly_savings = monthly_income - total_expenses

print("Total expenses: $" + str(total_expenses))
print("Monthly savings: $" + str(monthly_savings))
# Output:
# Total expenses: $1950
# Monthly savings: $3050


# --- Cell 4: Multiple assignments ---
# Topic 3: Multiple assignments

# Assign several budget categories at once
food, transport, phone = 300, 200, 50

# Swap values (useful for comparing months)
jan_savings, feb_savings = 3050, 2800
jan_savings, feb_savings = feb_savings, jan_savings  # swap without temp variable

print(f"Jan: ${jan_savings}, Feb: ${feb_savings}")
# Output: Jan: $2800, Feb: $3050


# --- Cell 5: Line joining techniques ---
# Topic 5: Line joining
# Topic 4: Indentation and comments

# Implicit joining inside parentheses
total_annual_expenses = (
    rent * 12
    + groceries * 12
    + utilities * 12
    + transport * 12
    + entertainment * 12
)

# Explicit joining with backslash
annual_savings = monthly_income * 12 \
                 - total_annual_expenses

print(f"Annual expenses: ${total_annual_expenses}")
print(f"Annual savings: ${annual_savings}")
# Output:
# Annual expenses: $23400
# Annual savings: $36600
