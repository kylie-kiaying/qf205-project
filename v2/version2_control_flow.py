# ============================================================
# VERSION 2: Structured Script with Control Flow (Chapter 4)
# Personal Finance Calculator
# Topics covered: 8-10 (for statements, if statements,
#   list comprehensions) plus 4, 6, 7 from earlier chapters
# ============================================================


# === Data setup (using concepts from Chapters 2-3) ===

# Tuple of income sources (immutable)                    # Topic 6
income_sources = (4800, 200, 200)
monthly_income = sum(income_sources)

# Dictionary mapping category names to amounts           # Topic 6
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


# === Example 4-1: Iterating through the budget ===
# Topic 8: for statements
# Topic 4: Indentation and comments

print('--- Monthly Budget Breakdown ---')
for category, amount in budget.items():
    percentage = amount / monthly_income * 100
    print(f'  {category:15s} ${amount:>7,}  ({percentage:.1f}%)')


# === Example 4-2: Calculating totals with a for loop ===
# Topic 8: for statements

total = 0
for amount in budget.values():
    total += amount    # shorthand for total = total + amount

savings = monthly_income - total
print(f'  {"TOTAL":15s} ${total:>7,}')
print(f'  {"SAVINGS":15s} ${savings:>7,}')
print(f'  Savings rate: {savings / monthly_income * 100:.1f}%')


# === Example 4-3: Financial health assessment ===
# Topic 9: if statements

savings_rate = savings / monthly_income * 100

print('\n--- Financial Health Assessment ---')
if savings_rate >= 30:
    status = 'Excellent'
    advice = 'Consider investing the surplus.'
elif savings_rate >= 20:
    status = 'Good'
    advice = 'Maintain this rate consistently.'
elif savings_rate >= 10:
    status = 'Fair'
    advice = 'Try reducing discretionary spending.'
else:
    status = 'Needs Attention'
    advice = 'Review expenses urgently.'

print(f'Savings Rate: {savings_rate:.1f}%')
print(f'Status: {status}')
print(f'Advice: {advice}')


# === Example 4-4: Checking individual categories ===
# Topic 8 + 9: for loop combined with if/elif/else

print('\n--- Category Analysis ---')
for category, amount in budget.items():
    pct = amount / monthly_income * 100
    if pct > 20:
        print(f'  WARNING: {category} is {pct:.1f}% of income (too high!)')
    elif pct > 10:
        print(f'  CAUTION: {category} is {pct:.1f}% of income')
    else:
        print(f'  OK: {category} is {pct:.1f}% of income')


# === Example 4-5: List comprehensions ===
# Topic 10: List comprehensions

# Find all categories where spending exceeds $100
high_expenses = [
    (cat, amt) for cat, amt in budget.items()
    if amt > 100
]
print('\nHigh expenses (over $100):', high_expenses)

# Calculate annual amount for each category
annual_amounts = [amt * 12 for amt in budget.values()]
print('Annual amounts:', annual_amounts)

# Get names of categories exceeding 5% of income
flagged = [
    cat for cat, amt in budget.items()
    if amt / monthly_income * 100 > 5
]
print('Flagged (>5% of income):', flagged)


# === Example 4-6: Complete budget analyser ===
# Combines all Topics 1-10

print('\n\n=== COMPLETE BUDGET ANALYSIS (Version 2) ===')

# Data setup
income_sources = (4800, 200, 200)                        # Topic 6: tuple
monthly_income = sum(income_sources)                     # Topic 2: variable

budget = {                                               # Topic 6: dictionary
    'rent': 1200, 'groceries': 300, 'utilities': 150,
    'transport': 200, 'entertainment': 100,
    'phone': 50, 'subscriptions': 80, 'dining': 80,
}

# Compute totals using for loop                          # Topic 8
total = 0
for amount in budget.values():
    total += amount
savings = monthly_income - total                         # Topic 1: expression
rate = savings / monthly_income * 100                    # Topic 1: expression

# Display breakdown using for loop                       # Topic 8
print('=== Budget Breakdown ===')
for cat, amt in budget.items():
    pct = amt / monthly_income * 100
    print(f'  {cat:15s} ${amt:>7,}  ({pct:.1f}%)')
print(f'  {"TOTAL":15s} ${total:>7,}')
print(f'  {"SAVINGS":15s} ${savings:>7,}  ({rate:.1f}%)')

# Health assessment using if/elif/else                   # Topic 9
if rate >= 30:
    status = 'Excellent'
elif rate >= 20:
    status = 'Good'
elif rate >= 10:
    status = 'Fair'
else:
    status = 'Needs Attention'
print(f'\nFinancial Health: {status}')

# List comprehension to flag high-spend categories       # Topic 10
flagged = [cat for cat, amt in budget.items() if amt / monthly_income * 100 > 5]
if flagged:                                              # Topic 7: membership
    print(f'High-spend categories: {", ".join(flagged)}')
