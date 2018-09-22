import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 test'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        nameLabel.move(300,70)
        button = QPushButton('Submit name', self)
        button.setToolTip('This is an example button')
        button.move(200,70)
        button.clicked.connect(self.submitContact)
        self.show()

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                "Hello %s!" % name)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())