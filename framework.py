# Source for image upload PyQt code:
# https://stackoverflow.com/questions/60614561/how-to-ask-user-to-input-an-image-in-pyqt5
# Source for counting dots
# #https://stackoverflow.com/questions/60603243/detect-small-dots-in-image 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import cv2 as cv
import numpy as np

COUNT = 0
PATH = ""

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.generalLayout = QGridLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createPhoto()
        self._createButtonsAndLabels(COUNT)

    def _createPhoto(self):
        self.photo = Template()
        self.generalLayout.addWidget(self.photo, 0, 0)

    def _createButtonsAndLabels(self, count):
        self.countButton = QPushButton("Count")
        self.countButton.setFixedSize(100, 30)
        self.countButton.setCheckable(True)
        self.countLabel = QLabel("Circle Count:")
        self.countDisplay = QLineEdit("{0}".format(count))
        self.countDisplay.setFixedSize(400, 30)
        self.addMarkerButton = QPushButton("Add marker")
        self.removeMarkerButton = QPushButton("Remove marker")

        self.countButton.clicked.connect(lambda: self.countDots(PATH))
        
        self.smallGridLayout = QGridLayout()
        self.smallGridLayout.addWidget(self.countButton, 0, 1)
        self.smallGridLayout.addWidget(self.countLabel, 1, 0)
        self.smallGridLayout.addWidget(self.countDisplay, 1, 1)
        self.smallGridLayout.addWidget(self.addMarkerButton, 2, 1)
        self.smallGridLayout.addWidget(self.removeMarkerButton, 3, 1)

        self.generalLayout.addLayout(self.smallGridLayout, 0, 1)

    def countDots(self, filename):
        # Load image, grayscale, Otsu's threshold
        image = cv.imread(filename)
        grayScale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        threshold = cv.threshold(grayScale, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        # Filter out large non-connecting objects
        count = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        count = count[0] if len(count) == 2 else count[1]
        for c in count:
            if cv.contourArea(c) < 500:
                cv.drawContours(threshold,[c],0,0,-1)

        # Morph open using elliptical shaped kernel
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
        opening = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel, iterations=3)

        # Find circles 
        count = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        count = count[0] if len(count) == 2 else count[1]
        for c in count:
            if cv.contourArea(c) > 10 and cv.contourArea(c) < 500:
                ((x, y), r) = cv.minEnclosingCircle(c)
                cv.circle(image, (int(x), int(y)), int(r), (36, 255, 12), 2)

        self.countDisplay.setText(str(len(count)))

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
        self.path = ""
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
            photo_path = str(filename)
            # print("Checking if string: {}".format(isinstance(path, str)))
            
            self.photo.setPixmap(QPixmap(filename))
        
        global PATH
        PATH = str(photo_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())