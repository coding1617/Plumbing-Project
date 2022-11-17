# Source for image upload PyQt code:
# https://stackoverflow.com/questions/60614561/how-to-ask-user-to-input-an-image-in-pyqt5

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.generalLayout = QGridLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createPhoto()
        self._createButtonsAndLabels()

    def _createPhoto(self):
        self.photo = Template()
        self.generalLayout.addWidget(self.photo, 0, 0)

    def _createButtonsAndLabels(self):
        self.countButton = QPushButton("Count")
        self.countButton.setFixedSize(100, 30)
        self.countLabel = QLabel("Circle Count:")
        self.countDisplay = QLineEdit("(Number)")
        self.countDisplay.setFixedSize(400, 30)
        self.addMarkerButton = QPushButton("Add marker")
        self.removeMarkerButton = QPushButton("Remove marker")

        self.smallGridLayout = QGridLayout()
        self.smallGridLayout.addWidget(self.countButton, 0, 1)
        self.smallGridLayout.addWidget(self.countLabel, 1, 0)
        self.smallGridLayout.addWidget(self.countDisplay, 1, 1)
        self.smallGridLayout.addWidget(self.addMarkerButton, 2, 1)
        self.smallGridLayout.addWidget(self.removeMarkerButton, 3, 1)

        self.generalLayout.addLayout(self.smallGridLayout, 0, 1)


class PhotoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n (Image will appear here) \n\n')
        self.setStyleSheet('''
        QLabel {
            border: 4px dashed #aaa;
        }''')
        
    def setPixmap(self, *args, **kwargs):
        super().setPixmap(*args, **kwargs)

class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.photo = PhotoLabel()
        btn = QPushButton('Browse')
        btn.clicked.connect(self.open_image)
        grid = QGridLayout(self)
        grid.addWidget(btn, 0, 0, Qt.AlignHCenter)
        grid.addWidget(self.photo, 1, 0)
        self.setAcceptDrops(True)
        self.resize(300, 200)

    def open_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return
        self.photo.setPixmap(QPixmap(filename))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())