#!/usr/bin/python3

import sys
import time
import json
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class mainMenuForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/mainMenuForm.ui", self)
        self.title = "tbrpggepp"
        self.world_file = None
        self.game_world = {}

    def loadWorldFile(self, world_file_path):
        self.world_file = open(word_file_path, 'rw')
        self.game

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainMenuForm()
    ex.show()
    sys.exit(app.exec_())
