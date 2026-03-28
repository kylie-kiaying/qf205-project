# main.py — Application entry point

# === Topic 15: import statements without the from clause ===
import sys

from PyQt5.QtWidgets import QApplication

from gui import FinanceCalculator


# ── Application Entry Point ──
# Topic 19: Scopes and namespaces
# The __name__ == '__main__' guard uses Python's module namespace system.
# When this file is run directly, __name__ is set to '__main__' in the
# global namespace. When imported, __name__ would be the module's filename.

if __name__ == '__main__':
    app = QApplication(sys.argv)                     # Topic 2: variable assignment
    window = FinanceCalculator()                     # creates instance, calls __init__
    window.show()
    sys.exit(app.exec_())                            # Topic 1: expression
