#!/usr/bin/python3

import sys
import time
import copy
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editEnemyForm(QMainWindow):

    def __init__(self, game_world, tile, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editEnemyForm.ui", self)
        self.title = "tbrpggepp"
        self.tile = tile
        self.game_world = copy.deepcopy(game_world)
        dmg_types = [None,'a']
        self.cbDmgTypeValue.addItems(dmg_types)

        if self.tile != None:
            # non-empty tile, prefill forms
            enemy_json = self.game_world[self.tile.text()]["params"]["enemy"]

            self.leNameValue.setText(enemy_json["params"]["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(enemy_json["params"]["dmgtype"]))
            self.sbMaxHPValue.setValue(enemy_json["params"]["max_health"])
            self.sbAttackDmgValue.setValue(enemy_json["params"]["attack_damage"])

        # Add connections
        self.btnCancel.clicked.connect(self.btnCancelClicked)


    def btnCancelClicked(self):
        # TODO: Clear form items
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editEnemyForm()
    ex.show()
    sys.exit(app.exec_())
