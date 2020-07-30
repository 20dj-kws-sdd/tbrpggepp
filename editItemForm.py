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

class editItemForm(QMainWindow):

    def __init__(self, item_dict={"type":"item_obj", "params":{}}, quantity=1, parent=None):
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
            # non-empty tile, prefill input fields

            self.leNameValue.setText(item_dict["params"]["name"])
            self.cbDmgTypeValue.setCurrentIndex(dmg_types.index(item_dict["params"]["dmgtype"]))
            self.sbHPEffectValue.setValue(item_dict["params"]["hpdelta"])
            self.chbHealingValue.setChecked(item_dict["params"]["heal_bool"])
            self.pteEffectTextValue.setPlainText(item_dict["params"]["effect_text"])

        if quantity != 1:
            # Non-default quantity value passed from
            # tile form, prefill input field
            self.sbQuantityValue.setValue(quantity)

        # Add connections
        self.actionOnline_Help.triggered.connect(lambda: webbrowser.open_new("file://"+ self.FILE_PATH + "/manual/editItemFormManual.pdf"))
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnSaveItem.clicked.connect(self.btnSaveItemClicked)


    def btnCancelClicked(self):
        """ Simply closes form without updating any data. """
        self.close()

    def btnSaveItemClicked(self):
        """ Loads parameters into item_dict with user-input data and sends it back to editItemform. """
        self.item_dict["params"]["name"] = self.leNameValue.text()
        self.item_dict["params"]["hpdelta"] = self.sbHPEffectValue.value()
        self.item_dict["params"]["heal_bool"] = self.chbHealingValue.isChecked()
        self.item_dict["params"]["effect_text"] = self.pteEffectTextValue.toPlainText()
        # Programatically an empty dmgtype is saved as 'None' but the combobox returns an
        # empty string if this is selected. This if-statement catches that and corrects it.
        if self.cbDmgTypeValue.currentText() == "":
            self.item_dict["params"]["dmgtype"] = None
        self.editTile.updateItem(self.item_dict, self.sbQuantityValue.value())
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = editItemForm()
    ex.show()
    sys.exit(app.exec_())
