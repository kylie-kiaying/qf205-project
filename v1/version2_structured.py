# ============================================================
# VERSION 2: Structured Scripting with Data Structures & Control Flow
# Personal Finance Calculator - Lists, Loops, Conditionals
# ============================================================

# --- Topic 6: Lists, tuples and dictionaries ---

# A list of expense amounts (ordered, mutable)
expense_amounts = [1200, 300, 150, 200, 100, 50, 80]

# A tuple of fixed income sources (immutable - income doesn't change mid-month)
income_sources = (5000, 200)  # (salary, freelance)

# A dictionary mapping category names to amounts
budget = {
    "rent": 1200,
    "groceries": 300,
    "utilities": 150,
    "transport": 200,
    "entertainment": 100,
    "phone": 50,
    "subscriptions": 80,
}

monthly_income = sum(income_sources)  # sum works on tuples too


# --- Topic 7: Membership test and comparison operators ---

# Membership test: check if a category exists before accessing it
if "rent" in budget:
    print(f"Rent is ${budget['rent']} per month")

# Check if a category is NOT in the budget
if "insurance" not in budget:
    print("Warning: No insurance budget allocated!")

# Comparison operators for budget analysis
if budget["rent"] > monthly_income * 0.3:
    print("Warning: Rent exceeds 30% of income!")
if budget["groceries"] == 300:
    print("Groceries budget unchanged from last month")


# --- Topic 8: for statements ---
# --- Topic 4: Indentation and comments ---

# for statement: iterate through all budget categories
print("\n--- Monthly Budget Breakdown ---")
for category, amount in budget.items():
    percentage = amount / monthly_income * 100
    print(f"  {category.capitalize():15s} ${amount:>7.2f}  ({percentage:.1f}%)")

# Calculate total using a for loop
total = 0
for amount in budget.values():
    total += amount

print(f"  {'TOTAL':15s} ${total:>7.2f}")
print(f"  {'Savings':15s} ${monthly_income - total:>7.2f}")


# --- Topic 9: if statements ---

# if statements: categorize financial health
savings = monthly_income - total
savings_rate = savings / monthly_income * 100

print("\n--- Financial Health Assessment ---")
if savings_rate >= 30:
    status = "Excellent"
    advice = "You are saving well. Consider investing the surplus."
elif savings_rate >= 20:
    status = "Good"
    advice = "Solid savings rate. Try to maintain this consistently."
elif savings_rate >= 10:
    status = "Fair"
    advice = "Consider reducing discretionary spending."
else:
    status = "Needs Attention"
    advice = "Review expenses urgently - savings are too low."

print(f"Savings Rate: {savings_rate:.1f}%")
print(f"Status: {status}")
print(f"Advice: {advice}")


# --- Topic 10: List comprehensions ---

# List comprehension: find categories over $100
high_expenses = [
    (cat, amt) for cat, amt in budget.items()
    if amt > 100
]

# List comprehension: calculate annual amounts
annual_amounts = [amt * 12 for amt in budget.values()]

# List comprehension: get category names that exceed 5% of income
flagged = [
    cat for cat, amt in budget.items()
    if amt / monthly_income * 100 > 5
]

print("\nHigh expenses (over $100):", high_expenses)
print("Flagged categories (>5% of income):", flagged)
