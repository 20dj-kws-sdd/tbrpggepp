#!/usr/bin/python3

import sys
import time
import copy
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editMovesForm(QMainWindow):

    def __init__(self, moves_dict={}, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editMovesForm.ui", self)
        self.title = "tbrpggepp"
        self.editTileForm = parent
        self.moves_dict = moves_dict
        self.moves = {"[0,-1]":[0,-1], "[1,0]":[1,0], "[0,1]":[0,1], "[-1,0]":[-1,0]}
        self.cbMoveDirValue.addItems(self.moves.keys())

        self.reloadMovesListbox()

        # Add connections
        self.btnClear.clicked.connect(self.btnClearClicked)
        self.btnAddMove.clicked.connect(self.btnAddMoveClicked)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveMoves.clicked.connect(self.btnSaveMovesClicked)


    def reloadMovesListbox(self):
        self.lstMoves.clear()
        for key in self.moves_dict.keys():
            self.lstMoves.addItem(str(self.moves_dict[key]) + ": " + key)


    def btnAddMoveClicked(self):
        key = self.leMoveNameValue.text()
        value = self.moves[self.cbMoveDirValue.currentText()]
        self.moves_dict[key] = value
        self.reloadMovesListbox()


    def btnClearClicked(self):
        self.moves_dict = {}
        self.reloadMovesListbox()


    def btnCancelClicked(self):
        self.close()


    def btnSaveMovesClicked(self):
        self.editTileForm.updateMoves(self.moves_dict)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editMovesForm()
    ex.show()
    sys.exit(app.exec_())
