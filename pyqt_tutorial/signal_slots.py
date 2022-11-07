# Signals and slots example.
# Used when widgets respond to and change according to events.
# For a signal to trigger an action, it must be connected to a slot.

import sys
from functools import partial

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# This is our slot function.
def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        # functools allow the slot function to receive extra arguments
        msgLabel.setText(f"Hi {name}")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and Slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
# Format for signals and slots:
# widget.signal.connect(slot_function)
# Example:
# button.clicked.connect(greet)

button.clicked.connect(partial(greet, "Bob!"))

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)

window.setLayout(layout)
window.show()
sys.exit(app.exec())