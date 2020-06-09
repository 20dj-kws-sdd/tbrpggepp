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
        uic.loadUi("UI_Layouts/editTileForm.ui", self)
        self.title = "tbrpggepp"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainForm()
    ex.show()
    sys.exit(app.exec_())
