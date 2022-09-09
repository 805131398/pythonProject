# 多选按钮
import time

from PySide6.QtCore import QSize, QTimer, QTime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QLabel, QCheckBox, \
    QVBoxLayout, QSpinBox, QLCDNumber
from PySide6.QtGui import QIcon, QFont
import sys


# 数字展示框
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 LCD 动态数字")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.showLCD)

    def showLCD(self):
        vbox = None
        timeText = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(timeText)
        lcd = QLCDNumber()

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)

        lcd.display(timeText)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
