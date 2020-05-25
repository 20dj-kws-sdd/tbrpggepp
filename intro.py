#!/usr/bin/python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class introForm(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
