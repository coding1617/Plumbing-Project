# Dialog style application

import sys

from PyQt5.QtWidgets import (
    QApplication, 
    QDialog, 
    QDialogButtonBox, 
    QFormLayout, 
    QLineEdit, 
    QVBoxLayout,
)

# Creating a class
class Window(QDialog):
    # Used for initialization, similar to a constructor
    def __init__(self):
        # Parent argument set to None because this dialog is main window
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        
        # Add form layout to dialogLayout
        dialogLayout.addLayout(formLayout)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)
    
# Used for correctly executing program
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())