"""
personal_finance_gui.py - Personal Finance Calculator GUI
==========================================================
This script loads a .ui file created with Qt Designer and
connects the UI components to the VisualFinance class.

Requirements:
    pip install PyQt5 matplotlib pandas

Files required in the same directory:
    - FinanceCalculatorGUI.ui   (created with Qt Designer)
    - finance_visual.py         (VisualFinance class)
    - finance_lib02.py          (PersonalFinance class)

Usage:
    python personal_finance_gui.py
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from finance_visual import VisualFinance

qtCreatorFile = "FinanceCalculatorGUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.PB)
        fig1 = Figure()
        self.ax1 = fig1.add_subplot(111)
        self.canvas = FigureCanvas(fig1)
        self.chartLayout.addWidget(self.canvas)

    def PB(self):
        income = float(self.lineEdit_income.text())
        expenses = {
            'Rent': float(self.lineEdit_rent.text()),
            'Food': float(self.lineEdit_food.text()),
            'Transport': float(self.lineEdit_transport.text()),
            'Utilities': float(self.lineEdit_utilities.text()),
            'Entertainment': float(self.lineEdit_entertainment.text()),
            'Others': float(self.lineEdit_others.text()),
        }

        vf = VisualFinance(income, expenses)

        self.label_total.setText(f'${vf.total_expenses:,.2f}')
        self.label_disposable.setText(f'${vf.disposable:,.2f}')
        self.label_rate.setText(f'{vf.savings_rate()}%')
        self.label_health.setText(vf.financial_health())

        self.ax1.cla()
        vf.plot_breakdown(ax=self.ax1)
        self.canvas.figure.subplots_adjust(
            bottom=0.15, top=0.85, left=0.12, right=0.95)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
