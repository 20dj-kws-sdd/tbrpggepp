#!/usr/bin/python3

import sys
import time
import os
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mainMenuForm import *

class introForm(QMainWindow):

    def __init__(self, parent=None):
        """ Initialises introForm upon creation of such an object """
        super().__init__(parent)
        self.FILE_PATH = os.path.normcase(os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(self.FILE_PATH + "/UI_Layouts/introForm.ui", self)
        self.title = "tbrpggepp"

        self.mainMenu = parent

        # Add connections
        self.actionOnline_Help.triggered.connect(lambda: webbrowser.open_new("file://"+ self.FILE_PATH + "/manual/introFormManual.pdf"))
        self.btnOpenFile.clicked.connect(self.btnOpenFileClicked)
        self.btnNewWorld.clicked.connect(self.btnNewWorldClicked)


    def btnOpenFileClicked(self):
        """ Ran when a user selects a preexisting file, checks validity of file and sends to mainMenuForm. """
        # from "http://zetcode.com/gui/pyqt5/dialogs/"
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getOpenFileName(self, 'Open world file', home_dir)

        if fname[0]:
            # If the filename is an empty string then the user pressed cancel on the file dialog
            if not fname[0].endswith(".json") and fname[0] != "":
                # File isn't json therefore is invalid
                error_dialog = QErrorMessage(self)
                error_dialog.setWindowTitle("Invalid file")
                error_dialog.showMessage('Invalid world map file!')
            elif fname[0] != "":
                self.mainMenu.loadWorldFile(fname[0])
                self.mainMenu.show()
                self.close()

    def btnNewWorldClicked(self):
        """ Ran when the user intends to create a new world file, checks validity of file
        and sends it mainMenuForm to create the file. """
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getSaveFileName(self, 'Create world file', home_dir)
        # If the filename is an empty string then the user pressed cancel on the file dialog
        if fname[0]:
            if not fname[0].endswith(".json") and fname[0] != "":
                # File isn't json therefore is invalid
                error_dialog = QErrorMessage(self)
                error_dialog.setWindowTitle("Invalid file")
                error_dialog.showMessage('Invalid world map file!')
            elif fname[0] != "":
                self.mainMenu.writeWorldFile(fname[0])
                self.mainMenu.loadWorldFile(fname[0])
                self.mainMenu.show()
                self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = introForm()
    ex.show()
    sys.exit(app.exec_())
