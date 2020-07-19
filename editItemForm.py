#!/usr/bin/python3

import sys
import time
import copy
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editItemForm(QMainWindow):

    def __init__(self, game_world, tile, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editItemForm.ui", self)
        self.title = "tbrpggepp"
        self.tile = tile
        self.game_world = copy.deepcopy(game_world)
        dmg_types = [None,'a']
        self.cbDmgTypeValue.addItems(dmg_types)

        if self.tile != None:
            # non-empty tile, prefill forms
            item_json = self.game_world[self.tile.text()]["params"]["item"]

            self.leNameValue.setText(item_json["params"]["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(item_json["params"]["dmgtype"]))
            self.sbHPEffectValue.setValue(item_json["params"]["hpdelta"])
            self.chbHealingValue.setChecked(item_json["params"]["heal_bool"])
            self.pteEffectTextValue.setPlainText(item_json["params"]["effect_text"])

        # Add connections
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveItem.clicked.connect(self.btnSaveItemClicked)


    def btnCancelClicked(self):
        # TODO: Clear form items
        self.close()

    def btnSaveItemClicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editItemForm()
    ex.show()
    sys.exit(app.exec_())
