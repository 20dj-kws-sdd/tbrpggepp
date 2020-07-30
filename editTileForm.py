#!/usr/bin/python3

import sys
import time
import os
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from editEnemyForm import *
from editItemForm import *
from editMovesForm import *

class editTileForm(QMainWindow):

    def __init__(self, tile_name=None, tile_dict={"params":{"effect_text":"", "location_text":"", "after_text":"", "moves_dict":{}}, "coords":[]}, coords=[], parent=None):
        """ Initialises editTileForm, is ran when such an object is created. Preloads forms with data if passed a preexisting tile. """
        super().__init__(parent)
        self.FILE_PATH = os.path.normcase(os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(self.FILE_PATH + "/UI_Layouts/editTileForm.ui", self)
        self.title = "tbrpggepp"
        self.mainMenuForm = parent
        self.tile_name = copy.deepcopy(tile_name)
        self.tile_dict = copy.deepcopy(tile_dict) # This is the structure that's manipulated and sent to mainMenu when the user hits save.
        self.openEnemyInsteadOfItem = None
        self.btnEditElement.setDisabled(True)
        types = ["basic_room", "enemy_room", "item_room", "victory_room"]
        self.cbTypeValue.addItems(types)

        if self.tile_name != None:
            # non-empty tile, prefill fields
            self.leNameValue.setText(self.tile_name)
            self.cbTypeValue.setCurrentIndex(types.index(tile_dict["type"]))
            self.cbTypeValueActivated() # update logic with new type value
            self.sbXCoordValue.setValue(tile_dict["coords"][0])
            self.sbYCoordValue.setValue(tile_dict["coords"][1])

            self.pteDescValue.setPlainText(tile_dict["params"]["location_text"])
            self.pteRetTextValue.setPlainText(tile_dict["params"]["after_text"])
            self.pteNarrTextValue.setPlainText(tile_dict["params"]["effect_text"])
        else:
            # Even if no preexisting tile was pessed there's still going to be coords
            self.sbXCoordValue.setValue(coords[0])
            self.sbYCoordValue.setValue(coords[1])

        # Add connections
        self.actionOnline_Help.triggered.connect(lambda: webbrowser.open_new("file://"+ self.FILE_PATH + "/manual/editTileFormManual.pdf"))
        self.btnEditElement.clicked.connect(self.btnEditElementClicked)
        self.btnEditMoves.clicked.connect(self.btnEditMovesClicked)
        self.cbTypeValue.activated.connect(self.cbTypeValueActivated)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)


    def cbTypeValueActivated(self):
        """ Ran when the user changes the tile type. Updates the editElement button to display correct text
        and sets a flag so the program knows which form to open. Also cleans tile data if the user switches
        from enemy to item or other. Disables editElement button if user selects a basic-type tile. """
        if self.cbTypeValue.currentText() == "enemy_room":
            self.openEnemyInsteadOfItem = True
            self.btnEditElement.setText("Edit Enemy")
            self.btnEditElement.setDisabled(False)
            # Clean data that's specific only to other tile types
            if "quantity" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("quantity")
            if "item" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("item")

        elif self.cbTypeValue.currentText() == "item_room":
            self.openEnemyInsteadOfItem = False
            self.btnEditElement.setText("Edit Item")
            self.btnEditElement.setDisabled(False)
            # Clean data that's specific only to other tile types
            if "enemy" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("enemy")

        else:
            self.openEnemyInsteadOfItem = None
            self.btnEditElement.setText("Edit Element")
            self.btnEditElement.setDisabled(True)
            # Clean data that's specific only to other tile types
            if "quantity" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("quantity")
            if "enemy" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("enemy")
            if "item" in self.tile_dict["params"].keys():
                self.tile_dict["params"].pop("item")



    def btnEditElementClicked(self):
        """ Ran when the user intends to edit a sub-property of a specific tile type. Preloads
        child form with data if that sub-property already exists and opens appropriate form. """
        if self.openEnemyInsteadOfItem:
            if "enemy" in self.tile_dict["params"].keys():
                # Preload child form with preexisting element data
                self.editEnemy = editEnemyForm(enemy_dict=self.tile_dict["params"]["enemy"], parent=self)
            else:
                self.editEnemy = editEnemyForm(parent=self)
            self.editEnemy.show()
        else:
            if "item" in self.tile_dict["params"].keys():
                # Preload child form with preexisting element data
                self.editItem = editItemForm(item_dict=self.tile_dict["params"]["item"], quantity=self.tile_dict["params"]["quantity"], parent=self)
            else:
                self.editItem = editItemForm(parent=self)
            self.editItem.show()


    def btnEditMovesClicked(self):
        """ Ran when the user intends to edit the moves of a tile. Preloads editMoves form with data and opens it. """
        if self.sbXCoordValue.value() == 0 and self.sbYCoordValue.value() == 0:
            is_origin = True
        else:
            is_origin = False
        self.editMoves = editMovesForm(moves_dict=self.tile_dict["params"]["moves_dict"], origin=is_origin, parent=self)
        self.editMoves.show()


    def delChildForms(self):
        """ Helper function that closes all child forms, ran when the editTile form itself is closed from mainMenu """
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
        """ Called by child form, updates relevant property """
        self.tile_dict["params"]["item"] = new_item_dict
        self.tile_dict["params"]["quantity"] = quantity


    def updateEnemy(self, new_enemy_dict):
        """ Called by child form, updates relevant property """
        self.tile_dict["params"]["enemy"] = new_enemy_dict


    def updateMoves(self, new_moves_dict):
        """ Called by child form, updates relevant property """
        self.tile_dict["params"]["moves_dict"] = new_moves_dict


    def btnCancelClicked(self):
        """ Closes form without updating game_world in mainMenu """
        self.delChildForms()
        self.close()


    def btnSaveClicked(self):
        """ Updates relevant properties in item_dict with user-input data and closes form,
        sending tile data back to be updated in mainMenu. """
        self.tile_name = self.leNameValue.text()
        if self.tile_name == "":
            # User forgot to add a name to the tile.
            # Not an issue programmatically but makes the tile hard to see in tblWorldMap
            error_dialog = QErrorMessage(self)
            error_dialog.setWindowTitle("Error")
            error_dialog.showMessage("Tile name left blank! Please choose a unique name for the tile.")
            return
        self.tile_dict["type"] = self.cbTypeValue.currentText()
        self.tile_dict["params"]["effect_text"] = self.pteNarrTextValue.toPlainText()
        self.tile_dict["params"]["location_text"] = self.pteDescValue.toPlainText()
        self.tile_dict["params"]["after_text"] = self.pteRetTextValue.toPlainText()
        self.tile_dict["coords"] = [self.sbXCoordValue.value(), self.sbYCoordValue.value()]
        self.mainMenuForm.updateTile(self.tile_name, self.tile_dict)
        self.delChildForms()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editTileForm()
    ex.show()
    sys.exit(app.exec_())
