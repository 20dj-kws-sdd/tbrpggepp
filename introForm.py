#!/usr/bin/python3

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mainMenuForm import *

class introForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/introForm.ui", self)
        self.title = "tbrpggepp"

        self.mainMenu = parent

        # Add connections
        self.btnOpenFile.clicked.connect(self.btnOpenFileClicked)
        self.btnNewWorld.clicked.connect(self.btnNewWorldClicked)

    def btnOpenFileClicked(self):
        # from "http://zetcode.com/gui/pyqt5/dialogs/"
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getOpenFileName(self, 'Open world file', home_dir)

        if fname[0]:
            if not fname[0].endswith(".json"):
                error_dialog = QErrorMessage(self)
                error_dialog.setWindowTitle("Invalid file")
                error_dialog.showMessage('Invalid world map file!')
            else:
                self.mainMenu.loadWorldFile(fname[0])
                self.mainMenu.show()
                self.hide()

    def btnNewWorldClicked(self):
        # create new file
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getSaveFileName(self, 'Create world file', home_dir)
        if not fname[0].endswith(".json"):
            error_dialog = QErrorMessage(self)
            error_dialog.setWindowTitle("Invalid file")
            error_dialog.showMessage('Invalid world map file!')
        else:
            self.mainMenu.writeWorldFile(fname[0])
            self.mainMenu.show()
            self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = introForm()
    ex.show()
    sys.exit(app.exec_())
