#!/usr/bin/python3

import sys
import time
import copy
import os
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editEnemyForm(QMainWindow):

    def __init__(self, enemy_dict={"type":"monster_obj", "params":{}}, parent=None):
        """ Intialises editEnemyForm and is ran when such an object is created. Preloads
        user-input boxes with data if an enemy for this tile already exists. """
        super().__init__(parent)
        self.FILE_PATH = os.path.normcase(os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(self.FILE_PATH + "/UI_Layouts/editEnemyForm.ui", self)
        self.title = "tbrpggepp"
        self.editTile = parent
        self.enemy_dict = copy.deepcopy(enemy_dict) # The structure that's manipulated and sent back to parent
        # Load combobox with dmgtypes.
        dmg_types = [None,'a']
        self.cbDmgTypeValue.addItems(dmg_types)

        if self.enemy_dict != {"type":"monster_obj", "params":{}}:
            # non-empty tile, prefill input fields
            self.leNameValue.setText(enemy_dict["params"]["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(enemy_dict["params"]["dmgtype"]))
            self.sbMaxHPValue.setValue(enemy_dict["params"]["max_health"])
            self.sbAttackDmgValue.setValue(enemy_dict["params"]["attack_damage"])

        # Add connections
        self.actionOnline_Help.triggered.connect(lambda: webbrowser.open_new("file://"+ self.FILE_PATH + "/manual/manual.pdf#page=11"))
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveEnemy.clicked.connect(self.btnSaveEnemyClicked)


    def btnCancelClicked(self):
        """ Simply closes form without sending any data back to parent. """
        self.close()


    def btnSaveEnemyClicked(self):
        """ Loads parameters into enemy_dict with user-input data and sends it back to editItemform. """
        self.enemy_dict["params"]["name"] = self.leNameValue.text()
        self.enemy_dict["params"]["attack_damage"] = self.sbAttackDmgValue.value()
        self.enemy_dict["params"]["max_health"] = self.sbMaxHPValue.value()
        # Programatically an empty dmgtype is saved as 'None' but the combobox returns an
        # empty string if this is selected. This if-statement catches that and corrects it.
        if self.cbDmgTypeValue.currentText() == "":
            self.enemy_dict["params"]["dmgtype"] = None
        self.editTile.updateEnemy(self.enemy_dict)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editEnemyForm()
    ex.show()
    sysexit(app.exec_())
