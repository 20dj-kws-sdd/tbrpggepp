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

    def __init__(self, game_world, tile, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editTileForm.ui", self)
        self.title = "tbrpggoepp"
        self.tile = tile
        self.game_world = copy.deepcopy(game_world)
        self.openEnemyInsteadOfItem = None
        self.btnEditElement.setDisabled(True)
        types = ["basic_room", "enemy_room", "item_room", "victory_room"]
        self.cbTypeValue.addItems(types)

        if self.tile != None:
            # non-empty tile, prefill forms
            tile_json = self.game_world[self.tile.text()]

            self.leNameValue.setText(self.tile.text())
            self.cbTypeValue.setCurrentIndex(types.index(tile_json["type"]))
            self.cbTypeValueActivated() # update logic with new type value
            self.sbXCoordValue.setValue(tile_json["coords"][0])
            self.sbYCoordValue.setValue(tile_json["coords"][1])

            self.pteDescValue.setPlainText(tile_json["params"]["location_text"])
            self.pteRetTextValue.setPlainText(tile_json["params"]["after_text"])
            self.pteNarrTextValue.setPlainText(tile_json["params"]["effect_text"])

        # Add connections
        self.btnEditElement.clicked.connect(self.btnEditElementClicked)
        self.btnEditMoves.clicked.connect(self.btnEditMovesClicked)
        self.cbTypeValue.activated.connect(self.cbTypeValueActivated)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)


    def btnCancelClicked(self):
        self.delChildForms()
        self.close()


    def cbTypeValueActivated(self):
        if self.cbTypeValue.currentText() == "enemy_room":
            self.openEnemyInsteadOfItem = True
            self.btnEditElement.setText("Edit Enemy")
            self.btnEditElement.setDisabled(False)

        elif self.cbTypeValue.currentText() == "item_room":
            self.openEnemyInsteadOfItem = False
            self.btnEditElement.setText("Edit Item")
            self.btnEditElement.setDisabled(False)

        else:
            self.openEnemyInsteadOfItem = None
            self.btnEditElement.setText("Edit Element")
            self.btnEditElement.setDisabled(True)


    def btnEditElementClicked(self):
        if self.openEnemyInsteadOfItem:
            self.editEnemy = editEnemyForm(self.game_world, self.tile, self)
            self.editEnemy.show()
        else:
            self.editItem = editItemForm(self.game_world, self.tile, self)
            self.editItem.show()


    def btnEditMovesClicked(self):
        self.editMoves = editMovesForm(self.game_world, self.tile, self)
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

    def propogateChanges(self, new_game_world):
        # Called by child forms, propogates changes back to tile edit form when a child form is saved
        self.game_world = new_game_world


    def btnSaveClicked(self):
        content = {}
        conent
        self.game_world[self.leNameValue.text()] = content
        # etc


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editTileForm()
    ex.show()
    sys.exit(app.exec_())
