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
        """ Initialises editMovesForm, ran when such an object is created.
        Preloads listbox with data if moves for this tile already exists. """
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editMovesForm.ui", self)
        self.title = "tbrpggepp"
        self.editTileForm = parent
        self.moves_dict = copy.deepcopy(moves_dict) # The structure that is manipulated and sent back to parent
        # Add moves to combobox. They're displayed in the format of coordinate deltas
        self.moves = {"[0,-1]":[0,-1], "[1,0]":[1,0], "[0,1]":[0,1], "[-1,0]":[-1,0]}
        self.cbMoveDirValue.addItems(self.moves.keys())

        # Clear listbox and fill with any preexisting moves
        self.reloadMovesListbox()

        # Add connections
        self.btnClear.clicked.connect(self.btnClearClicked)
        self.btnAddMove.clicked.connect(self.btnAddMoveClicked)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveMoves.clicked.connect(self.btnSaveMovesClicked)


    def reloadMovesListbox(self):
        """ Helper function that clears the visible listbox and refills it with moves_dict contents. """
        self.lstMoves.clear()
        for key in self.moves_dict.keys():
            self.lstMoves.addItem(str(self.moves_dict[key]) + ": " + key)


    def btnAddMoveClicked(self):
        """ Ran when the user adds a move. Inserts data into moves_dict and reloads listbox. """
        key = self.leMoveNameValue.text()
        value = self.moves[self.cbMoveDirValue.currentText()]
        self.moves_dict[key] = value
        self.reloadMovesListbox()


    def btnClearClicked(self):
        """ Clears moves_dict and reloads listbox """
        self.moves_dict = {}
        self.reloadMovesListbox()


    def btnCancelClicked(self):
        """ Simply closes form without sending back data to parent. """
        self.close()


    def btnSaveMovesClicked(self):
        """ Sends back moves data to be integrated into editTileForm and closes editMoves form. """
        self.editTileForm.updateMoves(self.moves_dict)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editMovesForm()
    ex.show()
    sys.exit(app.exec_())
