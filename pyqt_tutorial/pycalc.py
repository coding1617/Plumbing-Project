# PyCalc is a simple calculator built with Python and PyQt
# Tutorial reference: https://realpython.com/python-pyqt-gui-calculator/

import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow, 
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Global constants
ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class PyCalcWindow(QMainWindow):
    # PyCalc's main window (GUI or view).

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        # Two for loops, nested
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        # Set the display's text
        self.display.setText(text)
        self.display.setFocus() # Set cursor's focus on display

    def displayText(self):
        # Get the display's text (getter method)
        return self.display.text()

    def clearDisplay(self):
        # Clear the display
        self.setDisplayText("")

def evaluateExpression(expression):
    # Evaluate an expression (Model)
    # Not the most exact function, very basic
    # Shows basic error handling
    try:
        result = str(eval(expression, {}, {}))  # Note: eval() can lead to security issues
    except Exception:
        result = ERROR_MSG  # Doesn't catch a specific exception -- not recommended
    return result

class PyCalc:
    # PyCalc's controller class (connects view and model)
    # Access interface, handle creation of math expressions, connect button signals & slots

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    # PyCalc's main function.
    pyCalcApp = QApplication([])
    pyCalcWindow = PyCalcWindow()
    pyCalcWindow.show()
    PyCalc(model=evaluateExpression, view=pyCalcWindow)
    sys.exit(pyCalcApp.exec())

if __name__ == "__main__":
    main()