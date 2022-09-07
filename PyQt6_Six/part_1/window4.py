from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("国舜")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/guoshun.jpg'))
        # 设置窗口固定高宽
        self.setFixedWidth(700)
        self.setFixedHeight(700)

        # 设置窗口背景颜色, css
        self.setStyleSheet("background-color:red")
        # 设置窗口透明度
        self.setWindowOpacity(0.5)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
