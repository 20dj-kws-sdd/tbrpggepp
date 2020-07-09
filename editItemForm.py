#!/usr/bin/python3

import sys
import time
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editItemForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editItemForm.ui", self)
        self.title = "tbrpggepp"

        # Add connections
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveItem.clicked.connect(self.btnSaveItemClicked)


    def btnCancelClicked(self):
        # TODO: Clear form items
        self.close()

    def btnSaveItemClicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editItemForm()
    ex.show()
    sys.exit(app.exec_())
