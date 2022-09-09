# 多选按钮

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QLabel, QCheckBox, \
    QVBoxLayout, QSpinBox
from PySide6.QtGui import QIcon, QFont
import sys


# 数字加减框
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 数字输入框")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 布局
        hbox = QHBoxLayout()

        self.label = QLabel("笔记本电脑的价格是:")
        self.price = QLineEdit("500 ")
        self.label1 = QLabel("你选择:")
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.label2 = QLabel("台")
        self.result = QLineEdit()

        hbox.addWidget(self.label)
        hbox.addWidget(self.price)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.result)

        self.setLayout(hbox)

    def spin_selected(self):
        # 判断笔记本电脑价格不能等于0
        if self.price != 0:
            price = int(self.price.text())
            totalPrice = self.spinbox.value() * price
            self.result.setText(str(totalPrice))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
