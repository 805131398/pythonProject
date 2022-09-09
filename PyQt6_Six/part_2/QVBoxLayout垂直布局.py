from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QVBoxLayout
from PySide6.QtGui import QIcon, QFont
import sys


# 垂直布局
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QvboxLayout 水平布局")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 创建一个布局容器
        vbox = QVBoxLayout()

        # 创建4 个按钮
        btn1 = QPushButton("click 1")
        btn2 = QPushButton("click 2")
        btn3 = QPushButton("click 3")
        btn4 = QPushButton("click 4")
        # 将4 个按钮,放到容器中
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        # 将布局添加设置到当前窗口 self
        self.setLayout(vbox)
        # 设置边距, addSpacing: 添加间隔
        vbox.addSpacing(100)
        # addStretch: 添加拉伸
        vbox.addStretch(5)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
