import sys
import time

from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QMenu, QApplication, QVBoxLayout, QCalendarWidget, QLabel, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(1200, 400, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 日历")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        vbox = QVBoxLayout()

        # 时间日期控件
        self.calendar = QCalendarWidget()
        # 给时间控件加上网格
        self.calendar.setGridVisible(True)
        # 给一个点击\选择时间后的时间信号
        self.calendar.clicked.connect(self.calendar_clicked)
        self.label = QLabel("time:")
        self.label_time = QLabel("")
        vbox.addWidget(self.calendar)
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.label_time)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def calendar_clicked(self):
        print("timeText:", self.calendar.selectedDate().toPyDate())
        self.label_time.setText(str(self.calendar.selectedDate().toPyDate()))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
