#!/usr/bin/python3

import sys
import time
import copy
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class editItemForm(QMainWindow):

    def __init__(self, item_dict={"type":"item_obj", "params":{}}, parent=None):
        """ Initialises editItem form, preloading input boxes if a prexisting item exists.
        Ran when an editItemForm object is created. """
        super().__init__(parent)
        self.FILE_PATH = os.path.normcase(os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(self.FILE_PATH + "/UI_Layouts/editItemForm.ui", self)
        self.title = "tbrpggepp"
        self.item_dict = copy.deepcopy(item_dict) # The structure that is manipulated and sent back to parent
        self.editTile = parent
        # Add dmgtypes to combobox
        dmg_types = [None,'a']
        self.cbDmgTypeValue.addItems(dmg_types)

        if self.item_dict != {"type":"item_obj", "params":{}}:
            # non-empty tile, prefill forms

            self.leNameValue.setText(item_dict["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(item_dict["params"]["dmgtype"]))
            self.sbHPEffectValue.setValue(item_dict["params"]["hpdelta"])
            self.chbHealingValue.setChecked(item_dict["params"]["heal_bool"])
            self.sbQuantityValue.setValue(item_dict["params"]["quantity"])
            self.pteEffectTextValue.setPlainText(item_dict["params"]["effect_text"])

        # Add connections
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveItem.clicked.connect(self.btnSaveItemClicked)


    def btnCancelClicked(self):
        """ Simply closes form without updating any data. """
        self.close()

    def btnSaveItemClicked(self):
        """ Loads parameters into item_dict with user-input data and sends it back to editItemform. """
        self.item_dict["params"]["name"] = self.leNameValue.text()
        self.item_dict["params"]["hpdelta"] = self.sbHPEffectValue.value()
        self.item_dict["params"]["dmgtype"] = self.cbDmgTypeValue.currentText()
        self.item_dict["params"]["heal_bool"] = self.chbHealingValue.isChecked()
        self.item_dict["params"]["effect_text"] = self.pteEffectTextValue.toPlainText()
        self.editTile.updateItem(item_dict, self.sbQuantityValue.value())
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editItemForm()
    ex.show()
    sys.exit(app.exec_())
