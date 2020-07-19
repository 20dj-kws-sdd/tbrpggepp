#!/usr/bin/python3

import sys
import time
import copy
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editEnemyForm(QMainWindow):

    def __init__(self, enemy_dict={"type":"monster_obj", "params":{}}, parent=None):
        super().__init__(parent)
        uic.loadUi("UI_Layouts/editEnemyForm.ui", self)
        self.title = "tbrpggepp"
        self.editTileForm = parent
        self.enemy_dict = enemy_dict
        dmg_types = [None,'a']
        self.cbDmgTypeValue.addItems(dmg_types)

        if self.enemy_dict != {"type":"monster_obj", "params":{}}:
            # non-empty tile, prefill forms
            self.leNameValue.setText(enemy_dict["params"]["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(enemy_dict["params"]["dmgtype"]))
            self.sbMaxHPValue.setValue(enemy_dict["params"]["max_health"])
            self.sbAttackDmgValue.setValue(enemy_dict["params"]["attack_damage"])

        # Add connections
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveItem.clicked.connect(self.btnSaveEnemyClicked)


    def btnCancelClicked(self):
        self.close()


    def btnSaveEnemyClicked(self):
        self.enemy_dict["params"]["name"] = self.leNameValue.text()
        self.enemy_dict["params"]["max_damage"] = self.sbAttackDmgValue.value()
        self.enemy_dict["params"]["dmgtype"] = self.cbDmgTypeValue.currentText()
        self.enemy_dict["params"]["max_health"] = self.sbMxHPValue.value()
        self.editTileForm.updateEnemy(self.enemy_dict)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editEnemyForm()
    ex.show()
    sys.exit(app.exec_())
