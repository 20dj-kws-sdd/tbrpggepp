#!/usr/bin/python3

import sys
import time
import json
import random
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from introForm import *
from editTileForm import *

class mainMenuForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/mainMenuForm.ui", self)
        self.title = "tbrpggepp"
        self.world_file = None
        self.world_file_path = ""
        self.game_world = {}

        self.introForm = introForm(self)
        self.introForm.show()

        # Set tblWorldMap to have bold labels
        table_font = QFont()
        table_font.setBold(True)
        self.tblWorldMap.setFont(table_font)

        # Grey out edit tile button until a tile is clicked
        self.btnEditTile.setDisabled(True)

        # Add Connections
        self.btnEditTile.clicked.connect(self.btnEditTileClicked)
        self.btnDeleteTile.clicked.connect(self.btnDeleteTileClicked)
        self.actionOpen_File.triggered.connect(self.openNewFile)
        self.tblWorldMap.clicked.connect(self.tileClicked)


    def loadWorldFile(self, world_file_path):
        # Receives path to world file from intro form
        # Processes file and loads into program memory
        # and displays on tblWorldMap
        self.world_file_path = world_file_path
        self.world_file = open(self.world_file_path, 'r')
        self.game_world = json.load(self.world_file)
        self.tblWorldMap.clear()
        for tile in self.game_world.keys():
            cell = QTableWidgetItem(str(tile))
            self.tblWorldMap.setItem(self.game_world[tile]['coords'][1], self.game_world[tile]['coords'][0], cell)
        # Do all processing in main form just send data back including element data
        self.world_file.close()


    def writeWorldFile(self, world_file_path):
        self.world_file_path = world_file_path
        self.world_file = open(self.world_file_path, 'w')
        self.world_file.write(json.dumps(self.game_world))
        self.world_file.close()


    def tileClicked(self, index):
        # If edit tile button is grayed, ungray it
        self.btnEditTile.setDisabled(False)
        # Update side value information
        tile = self.tblWorldMap.item(index.row(), index.column())
        if tile == None:
            # empty tile
            self.lblNameValue.setText("")
            self.lblTypeValue.setText("")
            self.txtTextValue.setText("")
            self.lstMovesValue.clear()
            self.lblCoordsValue.setText(str(index.column()) + ", " + str(index.row()))
            return
        tile_json = self.game_world[tile.text()]
        self.lblNameValue.setText(tile.text())
        self.lblTypeValue.setText(tile_json["type"])
        self.lblCoordsValue.setText(str(tile_json["coords"][0]) + ", " + str(tile_json["coords"][1]))
        self.txtTextValue.setText(tile_json["params"]["effect_text"])
        self.lstMovesValue.clear()
        for key in tile_json["params"]["moves_dict"].keys():
            self.lstMovesValue.addItem(str(tile_json["params"]["moves_dict"][key]) + ": " + key)


    def btnEditTileClicked(self):
        tile = self.tblWorldMap.currentItem()
        if tile == None:
            self.editTile = editTileForm(coords=[int(self.lblCoordsValue.text().split(", ")[0]), int(self.lblCoordsValue.text().split(", ")[1])], parent=self)
        else:
            tile_name = tile.text()
            self.editTile = editTileForm(tile_name=tile_name, tile_dict=self.game_world[tile_name],  parent=self)
        self.editTile.show()


    def btnDeleteTileClicked(self):
        tile = self.tblWorldMap.currentItem()
        self.game_world.pop(tile.text())
        self.writeWorldFile(self.world_file_path)
        self.loadWorldFile(self.world_file_path)


    def updateTile(self, tile_name, tile_dict):
        clone_game_world = copy.deepcopy(self.game_world)
        for different_tile_name in self.game_world.keys():
            if different_tile_name == tile_name and self.game_world[different_tile_name]["coords"] != tile_dict["coords"]:
                error_dialog = QErrorMessage(self)
                error_dialog.setWindowTitle("Error")
                error_dialog.showMessage("Tile name already used! Please change the name of the new tile.")
                tile_name = "temp_name" + str(random.random() * 10)
            if self.game_world[different_tile_name]["coords"] == tile_dict["coords"]:
                clone_game_world.pop(different_tile_name)
        self.game_world = clone_game_world
        self.game_world[tile_name] = tile_dict
        self.writeWorldFile(self.world_file_path)
        self.loadWorldFile(self.world_file_path)


    def openNewFile(self):
        # Close all pre-existing sub-forms before opening new world-file
        if hasattr(self, "editTile"):
            self.editTile.close()
            self.editTile.delChildForms()
            del self.editTile
        self.introForm = introForm(self)
        self.introForm.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainMenuForm()
    ex.show()
    sys.exit(app.exec_())
