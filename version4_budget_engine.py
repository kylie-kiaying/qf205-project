# ============================================================
# VERSION 4 - MODULE: budget_engine.py
# Core calculation and file I/O module
# ============================================================

# --- Topic 15: import statements without the from clause ---
import math     # import entire module - access via math.floor(), math.ceil()
import json     # for saving/loading budget data
import datetime # for timestamping reports


def round_to_cents(amount):
    """Round a float to 2 decimal places using math module."""
    return math.floor(amount * 100) / 100


def save_budget(budget_dict, filename):
    """Save budget to a JSON file with a timestamp."""
    data = {
        "budget": budget_dict,
        "saved_at": datetime.datetime.now().isoformat(),
        "total": math.fsum(budget_dict.values()),  # precise float sum
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Budget saved to {filename}")


def load_budget(filename):
    """Load budget from a JSON file."""
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Budget loaded from {filename} (saved at {data['saved_at']})")
    return data["budget"]


def calculate_compound_savings(monthly, rate, years):
    """Calculate compound savings using math module functions."""
    months = years * 12
    monthly_rate = rate / 12
    if monthly_rate == 0:
        return monthly * months
    # Compound interest formula
    total = monthly * ((math.pow(1 + monthly_rate, months) - 1) / monthly_rate)
    return round_to_cents(total)
