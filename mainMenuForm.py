#!/usr/bin/python3

import sys
import time
import json
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

        #self.introForm = introForm(self)
        #self.introForm.show()
        self.loadWorldFile("/home/quiterion/Projects/text-rpg-game/worlds/canola.json")

        # Set tblWorldMap to have bold labels
        table_font = QFont()
        table_font.setBold(True)
        self.tblWorldMap.setFont(table_font)

        # Grey out edit tile button until a tile is clicked
        self.btnEditTile.setDisabled(True)

        # Add Connections
        self.btnEditTile.clicked.connect(self.btnEditTileClicked)
        self.actionOpen_File.triggered.connect(self.openNewFile)
        self.tblWorldMap.clicked.connect(self.tileClicked)


    def loadWorldFile(self, world_file_path):
        # Receives path to world file from intro form
        # Processes file and loads into program memory
        # and displays on tblWorldMap
        self.world_file_path = world_file_path
        self.world_file = open(self.world_file_path, 'r')
        self.game_world = json.load(self.world_file)
        for tile in self.game_world.keys():
            cell = QTableWidgetItem(str(tile))
            self.tblWorldMap.setItem(self.game_world[tile]['coords'][1], self.game_world[tile]['coords'][0], cell)
        # Do all processing in main form just send data back including element data
        self.world_file.close()


    def writeWorldFile(self, new_game_world=self.game_world):
        self.world_file = open(self.world_file_path, 'w')
        self.world_file.write(json.dumps(new_game_world))
        self.world_file.close()



    def tileClicked(self, index):
        # If edit tile button is grayed, ungray it
        self.btnEditTile.setDisabled(False)
        # Update side value information
        tile = self.tblWorldMap.item(index.row(), index.column())
        if tile == None:
            # empty tile
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
        self.editTile = editTileForm(self.game_world, self.tblWorldMap.currentItem(), self)
        self.editTile.show()
        print(self.game_world[self.tblWorldMap.currentItem().text()])

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
