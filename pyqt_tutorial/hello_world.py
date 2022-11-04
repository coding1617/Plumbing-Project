# Hello world example with PyQt
# PyQt version: PyQt5

import sys

# 1. Import QApplication and all required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create the application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello World</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Show the application's GUI
window.show()

# 5. Run the application's event loop
sys.exit(app.exec())

# Run commands from the VS Code terminal
# `python hello_world.py` while inside this folder