from PySide6.QtWidgets import QApplication, QWidget, QPushButton , QGridLayout
from PySide6.QtGui import QIcon, QFont
import sys


# 网格布局
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QqgridLayout 网格布局")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 创建一个布局容器(网格布局)
        grid = QGridLayout()

        # 创建8 个按钮
        btn1 = QPushButton("click 1")
        btn2 = QPushButton("click 2")
        btn3 = QPushButton("click 3")
        btn4 = QPushButton("click 4")
        btn5 = QPushButton("click 5")
        btn6 = QPushButton("click 6")
        btn7 = QPushButton("click 7")
        btn8 = QPushButton("click 8")

        # 将8 个按钮,放到容器中
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)
        grid.addWidget(btn3, 2, 0)
        grid.addWidget(btn4, 3, 0)
        grid.addWidget(btn5, 0, 1)
        grid.addWidget(btn6, 0, 2)
        grid.addWidget(btn7, 0, 3)
        grid.addWidget(btn8, 0, 4)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
