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
        self.setFixedSize(500, 500)
        self.generalLayout = QGridLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createPhoto()

    def _createPhoto(self):
        self.photo = Template()
        self.generalLayout.addWidget(self.photo, 0, 0)

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