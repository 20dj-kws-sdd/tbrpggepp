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
        self.game_world = {}

        #self.introForm = introForm(self)
        #self.introForm.show()
        self.loadWorldFile("/home/quiterion/Projects/text-rpg-game/worlds/canola.json")

        # Set tblWorldMap to have bold labels
        table_font = QFont()
        table_font.setBold(True)
        self.tblWorldMap.setFont(table_font)

        # Add Connections
        self.btnEditTile.clicked.connect(self.btnEditTileClicked)
        self.actionOpen_File.triggered.connect(self.openNewFile)
        self.tblWorldMap.clicked.connect(self.tileClicked)


    def loadWorldFile(self, world_file_path):
        # Receives path to world file from intro form
        # Processes file and loads into program memory
        # and displays on tblWorldMap

        self.world_file = open(world_file_path, 'r+')
        self.game_world = json.load(self.world_file)
        for tile in self.game_world.keys():
            cell = QTableWidgetItem(str(tile))
            self.tblWorldMap.setItem(self.game_world[tile]['coords'][1], self.game_world[tile]['coords'][0], cell)


    def tileClicked(self, tile):
        print(tile.column(), tile.row())


    def btnEditTileClicked(self):
        self.editTile = editTileForm(self)
        self.editTile.show()

    def openNewFile(self):
        # Close all pre-existing sub-forms before opening new world-file
        if hasattr(self, "editTile"):
            self.editTile.close()
            self.editTile.delChildForms()
            del editTile
        self.introForm = introForm(self)
        self.introForm.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainMenuForm()
    ex.show()
    sys.exit(app.exec_())
