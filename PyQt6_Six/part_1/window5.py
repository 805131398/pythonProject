from PySide6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic


# 错误实例
class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"guoshun.py", self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
