#!/usr/bin/python3

import sys
import time
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from editEnemyForm import *
from editItemForm import *
from editMovesForm import *

class editTileForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editTileForm.ui", self)
        self.title = "tbrpggoepp"
        self.openEnemyInsteadOfItem = None
        self.btnEditElement.setDisabled(True)
        self.cbTypeValue.addItems(["Basic", "Enemy", "Item", "Victory"])

        # Add connections
        self.btnEditElement.clicked.connect(self.btnEditElementClicked)
        self.btnEditMoves.clicked.connect(self.btnEditMovesClicked)
        self.cbTypeValue.activated.connect(self.cbTypeValueActivated)
        self.btnCancel.clicked.connect(self.btnCancelClicked)


    def btnCancelClicked(self):
        # TODO: Clear form items
        self.delChildForms()
        self.close()


    def cbTypeValueActivated(self):
        if self.cbTypeValue.currentText() == "Enemy":
            self.openEnemyInsteadOfItem = True
            self.btnEditElement.setText("Edit Enemy")
            self.btnEditElement.setDisabled(False)

        elif self.cbTypeValue.currentText() == "Item":
            self.openEnemyInsteadOfItem = False
            self.btnEditElement.setText("Edit Item")
            self.btnEditElement.setDisabled(False)

        else:
            self.openEnemyInsteadOfItem = None
            self.btnEditElement.setText("Edit Element")
            self.btnEditElement.setDisabled(True)



    def btnEditElementClicked(self):
        if self.openEnemyInsteadOfItem:
            self.editEnemy = editEnemyForm(self)
            self.editEnemy.show()
        else:
            self.editItem = editItemForm(self)
            self.editItem.show()


    def btnEditMovesClicked(self):
        self.editMoves = editMovesForm(self)
        self.editMoves.show()


    def delChildForms(self):
        # Closes all child forms
        if hasattr(self, "editEnemy"):
            self.editEnemy.close()
            del self.editEnemy
        if hasattr(self, "editItem"):
            self.editItem.close()
            del self.editItem
        if hasattr(self, "editMoves"):
            self.editMoves.close()
            del self.editMoves


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editTileForm()
    ex.show()
    sys.exit(app.exec_())
