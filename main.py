#!/usr/bin/python3

import sys
import time
from pathlib import Path
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mainForm(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "tbrpggepp"
        self.initUI()

    def initUI(self):

        # Create status bar on bottom of screen, displays tips
        self.statusBar()

        # Create menu-bar on top of screen
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        editMenu=menubar.addMenu('Edit')
        viewMenu=menubar.addMenu('View')
        searchMenu=menubar.addMenu('Search')
        toolsMenu=menubar.addMenu('Tools')
        helpMenu=menubar.addMenu('Help')

        # Create file open action
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        # Create application exit action
        exitButton=QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        # Add actions to 'file' option on menu bar
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitButton)

        # Create label and button widgets (from "https://www.learnpyqt.com/courses/start/basic-widgets/")
        introLabel = QLabel("Choose file or create new world map")
        introLabelFont = introLabel.font()
        introLabelFont.setPointSize(15)
        introLabelFont.setBold(True)
        introLabel.setFont(introLabelFont)

        selectFileButton = QPushButton("Select File")
        selectFileButton.clicked.connect(self.showDialog)
        newFileButton = QPushButton("New World")

        # Set layout (from "https://www.learnpyqt.com/courses/start/layouts/")
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(selectFileButton)
        buttonLayout.addWidget(newFileButton)

        introLayout = QVBoxLayout()
        introLayout.addWidget(introLabel)
        introLayout.addLayout(buttonLayout)

        introLayout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#        introLayout.setContentsMargins(20,20,20,20)
        introLayout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(introLayout)
        self.setCentralWidget(widget)

        self.show()

    def showDialog(self):
        # from "http://zetcode.com/gui/pyqt5/dialogs/"
        home_dir = str(Path.home())  # Cross-platform technique for finding home directory
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainForm()
    ex.show()
    sys.exit(app.exec_())
