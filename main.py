# import Renderer
#
#
# Renderer.say_hello()
# # ImageRenderer(blenderFilePath, exportType, selectedFrame, exportPath):
# Renderer.ImageRenderer("0.blend", "PNG", "200", "png/image")

import sys

from PySide6 import QtWidgets
from user_interface import UserInterface

app = QtWidgets.QApplication(sys.argv)

window = UserInterface()
window.show()

app.exec()