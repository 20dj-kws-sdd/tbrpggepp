#!/usr/bin/python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class introForm(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = "tbrpggepp"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit()
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.onClick)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.textbox)
        windowLayout.addWidget(self.button)
        self.setLayout(windowLayout)

    @pyqtSlot()
    def onClick(self):
        textboxValue = self.textbox.text()
        buttonReply = QMessageBox.question(self, "Clicked", textboxValue, QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = introForm()
    ex.show()
    sys.exit(app.exec_())
