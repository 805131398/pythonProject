from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton ,QMenu
from PySide6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 按钮 QPushButton")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        self.create_button()

    def create_button(self):
        # 只要声明了就会在页面中显示
        btn = QPushButton("按钮显示的名称", self)
        # 设置位置及大小
        btn.setGeometry(100, 100, 130, 130)
        btn.setFont(QFont("Times", 10, 0x320))
        # 设置按钮图片，显示的图片与问题大小相同
        btn.setIcon(QIcon("resource/image/guoshun.jpg"))
        # 修改显示的图片的的大小
        # btn.setIconSize(QSize(50, 50))

        # 点击弹出菜单  功能未能实现
        menu = QMenu()
        menu.setFont(QFont("微软雅黑", 30))
        menu.setStyleSheet('background-color:red')
        menu.addAction("aa")
        menu.addAction("bb")
        menu.addAction("cc")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
