#!/usr/bin/python3

import sys
import time
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class mainForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/introForm.ui", self)
        self.title = "tbrpggepp"

    def showDialog(self):
        # from "http://zetcode.com/gui/pyqt5/dialogs/"
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainForm()
    ex.show()
    sys.exit(app.exec_())
