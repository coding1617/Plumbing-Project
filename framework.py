# Source for image upload PyQt code:
# https://stackoverflow.com/questions/60614561/how-to-ask-user-to-input-an-image-in-pyqt5

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import cv2 as cv
import numpy as np

count = 0
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.generalLayout = QGridLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createPhoto()
        self._createButtonsAndLabels(count)

    def _createPhoto(self):
        self.photo = Template()
        self.generalLayout.addWidget(self.photo, 0, 0)
        
    def _createMarker(self):
        self.moveObject = MovingObject(50, 50, 40)
        self.generalLayout.addWidget(self.moveObject)

    def _createButtonsAndLabels(self, count):
        self.countButton = QPushButton("Count")
        self.countButton.setFixedSize(100, 30)
        self.countLabel = QLabel("Circle Count:")
        self.countDisplay = QLineEdit("{0}".format(count))
        self.countDisplay.setFixedSize(400, 30)
        self.addMarkerButton = QPushButton("Add marker")
        self.removeMarkerButton = QPushButton("Remove marker")

        self.countButton.clicked.connect(lambda: self.countDots("photos/unnamed.png"))
        # self.addMarkerButton.clicked.connect(self._createMarker)
        
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
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        # Filter out large non-connecting objects
        cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv.contourArea(c)
            if area < 500:
                cv.drawContours(thresh,[c],0,0,-1)

        # Morph open using elliptical shaped kernel
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=3)

        # Find circles 
        cnts = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv.contourArea(c)
            if area > 10 and area < 10:
                ((x, y), r) = cv.minEnclosingCircle(c)
                cv.circle(image, (int(x), int(y)), int(r), (36, 255, 12), 2)

        self.countDisplay.setText(str(len(cnts)))
        cv.waitKey()

class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(Qt.blue)
        self.setAcceptHoverEvents(True)

    # mouse hover event
    def hoverEnterEvent(self, event):
        app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        app.instance().restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
        
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