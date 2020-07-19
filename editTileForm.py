#!/usr/bin/python3

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from editEnemyForm import *
from editItemForm import *
from editMovesForm import *

class editTileForm(QMainWindow):

    def __init__(self, tile_name="", tile_dict={"params":{}}, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editTileForm.ui", self)
        self.title = "tbrpggepp"
        self.mainMenuForm = parent
        self.tile_name = tile_name
        self.tile_dict = tile_dict
        self.openEnemyInsteadOfItem = None
        self.btnEditElement.setDisabled(True)
        types = ["basic_room", "enemy_room", "item_room", "victory_room"]
        self.cbTypeValue.addItems(types)

        if self.tile_dict != {"params":{}} and self.tile_name != "":
            # non-empty tile, prefill forms
            self.leNameValue.setText(self.tile_name)
            self.cbTypeValue.setCurrentIndex(types.index(tile_dict["type"]))
            self.cbTypeValueActivated() # update logic with new type value
            self.sbXCoordValue.setValue(tile_dict["coords"][0])
            self.sbYCoordValue.setValue(tile_dict["coords"][1])

            self.pteDescValue.setPlainText(tile_dict["params"]["location_text"])
            self.pteRetTextValue.setPlainText(tile_dict["params"]["after_text"])
            self.pteNarrTextValue.setPlainText(tile_dict["params"]["effect_text"])

        # Add connections
        self.btnEditElement.clicked.connect(self.btnEditElementClicked)
        self.btnEditMoves.clicked.connect(self.btnEditMovesClicked)
        self.cbTypeValue.activated.connect(self.cbTypeValueActivated)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)


    def cbTypeValueActivated(self):
        if self.cbTypeValue.currentText() == "enemy_room":
            self.openEnemyInsteadOfItem = True
            self.btnEditElement.setText("Edit Enemy")
            self.btnEditElement.setDisabled(False)
            if "quantity" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("quantity")
            if "item" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("item")

        elif self.cbTypeValue.currentText() == "item_room":
            self.openEnemyInsteadOfItem = False
            self.btnEditElement.setText("Edit Item")
            self.btnEditElement.setDisabled(False)
            if "enemy" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("enemy")

        else:
            self.openEnemyInsteadOfItem = None
            self.btnEditElement.setText("Edit Element")
            self.btnEditElement.setDisabled(True)
            if "quantity" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("quantity")
            if "enemy" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("enemy")
            if "item" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("item")



    def btnEditElementClicked(self):
        if self.openEnemyInsteadOfItem:
            if "enemy" in self.tile_dict["params"].keys():
                self.editEnemy = editEnemyForm(self, self.tile_dict["params"]["enemy"])
            else:
                self.editEnemy = editEnemyForm(self)
            self.editEnemy.show()
        else:
            if "item" in self.tile_dict["params"].keys():
                self.editEnemy = editEnemyForm(self, self.tile_dict["params"]["item"])
            else:
                self.editEnemy = editEnemyForm(self)
            self.editItem.show()


    def btnEditMovesClicked(self):
        if "moves_dict" in self.tile_dict["params"].keys():
            self.editMoves = editMovesForm(self, self.tile_dict["params"]["moves_dict"])
        else:
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


    def updateItem(self, new_item_dict, quantity):
        self.tile_dict["params"]["item"] = new_item_dict
        self.tile_dict["params"]["quantity"] = quantity


    def updateEnemy(self, new_enemy_dict):
        self.tile_dict["params"]["enemy"] = new_enemy_dict


    def updateMoves(self, new_moves_dict):
        self.tile_dict["params"]["moves_dict"] = new_moves_dict


    def btnCancelClicked(self):
        self.delChildForms()
        self.close()


    def btnSaveClicked(self):
        self.tile_dict["type"] = self.cbTypeValue.currentText()
        self.tile_dict["params"]["effect_text"] = self.pteNarrTextValue.toPlainText()
        self.tile_dict["params"]["location_text"] = self.pteDescValue.toPlainText()
        self.tile_dict["params"]["after_text"] = self.pteRetTextValue.toPlainText()
        self.tile_dict["coords"] = [sbXCoordValue.value(), sbYCoordValue.value()]
        self.mainMenuForm.updateTile(self.tile_name, self.tile_dict)
        self.delChildForms()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editTileForm()
    ex.show()
    sys.exit(app.exec_())
