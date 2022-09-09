# 多选按钮

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QLabel, QCheckBox, \
    QVBoxLayout
from PySide6.QtGui import QIcon, QFont
import sys


# 水平布局
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 多选按钮 CheckBox")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 布局
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(
            QIcon(r"C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\image\Python.png"))
        self.check1.setIconSize(QSize(40, 40))
        self.check1.setFont(QFont("微软雅黑", 25))
        self.check1.stateChanged.connect(self.item_selected)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(
            QIcon(r"C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\image\java.png"))
        self.check2.setIconSize(QSize(40, 40))
        self.check2.setFont(QFont("微软雅黑", 25))
        self.check2.stateChanged.connect(self.item_selected)

        self.check3 = QCheckBox("java-script")
        self.check3.setIcon(
            QIcon(
                r"C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\image\java-script.png"))
        self.check3.setIconSize(QSize(40, 40))
        self.check3.setFont(QFont("微软雅黑", 25))
        self.check3.stateChanged.connect(self.item_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("微软雅黑", 25))

        hbox.addWidget(self.check1)
        hbox.addWidget(self.check2)
        hbox.addWidget(self.check3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def item_selected(self):
        value = []
        if self.check1.isChecked():
            value.append(self.check1.text())
        if self.check2.isChecked():
            value.append(self.check2.text())
        if self.check3.isChecked():
            value.append(self.check3.text())

        self.label.setText(f"你选择了{value.__str__()}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
