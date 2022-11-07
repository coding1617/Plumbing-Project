# Layout example: horizontal, vertical, grid, and form layout

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()

# Horizontal layout example
window.setWindowTitle("QHBoxLayout")

hLayout = QHBoxLayout()
hLayout.addWidget(QPushButton("Left"))
hLayout.addWidget(QPushButton("Center"))
hLayout.addWidget(QPushButton("Right"))

# Vertical layout example
window.setWindowTitle("QVBoxLayout")

vLayout = QVBoxLayout()
vLayout.addWidget(QPushButton("Top"))
vLayout.addWidget(QPushButton("Center"))
vLayout.addWidget(QPushButton("Bottom"))

# Grid layout example
window.setWindowTitle("QGridLayout")
gLayout = QGridLayout()

gLayout.addWidget(QPushButton("Button (0,0)"), 0, 0)
gLayout.addWidget(QPushButton("Button (0,1)"), 0, 1)
gLayout.addWidget(QPushButton("Button (0,2)"), 0, 2)
gLayout.addWidget(QPushButton("Button (1,0)"), 1, 0)
gLayout.addWidget(QPushButton("Button (1,1)"), 1, 1)
gLayout.addWidget(QPushButton("Button (1,2)"), 1, 2)
gLayout.addWidget(QPushButton("Button (2,0)"), 2, 0)
gLayout.addWidget(
    QPushButton("Button (2,1) + 2 Columns Span"), 2, 1, 1, 2
    # The 4th and 5th arguments are rowSpan and columnSpan
)

# Form layout example
window.setWindowTitle("QFormLayout")

fLayout = QFormLayout()
fLayout.addRow("Name:", QLineEdit())
fLayout.addRow("Age:", QLineEdit())
fLayout.addRow("Job:", QLineEdit())
fLayout.addRow("Hobbies:", QLineEdit())


# hLayout, vLayout, gLayout, or fLayout
window.setLayout(fLayout)
window.show()

sys.exit(app.exec())