from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog, QLabel

loader = QUiLoader()
blenderFilePath = ""


class UserInterface(QtCore.QObject):  # An object wrapping around our ui
    def __init__(self):
        super().__init__()
        self.ui = loader.load("ImageRenderer.ui", None)
        self.ui.setWindowTitle("Blender Image Renderer")
        self.ui.pushButton_2.clicked.connect(self.OpenFileLocaation)

    def show(self):
        self.ui.show()

    def OpenFileLocaation(self):
        filename, _ = QFileDialog.getOpenFileName()
        self.ui.FilePathTest.setText(filename)
        blenderFilePath = filename
