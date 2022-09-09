from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout
from PySide6.QtGui import QIcon, QFont
import sys


# 水平布局
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QHBoxLayout 水平布局")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 创建一个布局容器
        hbox = QHBoxLayout()

        # 创建4 个按钮
        btn1 = QPushButton("click 1")
        btn2 = QPushButton("click 2")
        btn3 = QPushButton("click 3")
        btn4 = QPushButton("click 4")
        # 将4 个按钮,放到容器中
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        # 将布局添加设置到当前窗口 self
        self.setLayout(hbox)
        # 设置边距, addSpacing: 添加间隔
        hbox.addSpacing(100)
        # addStretch: 添加拉伸
        hbox.addStretch(100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
