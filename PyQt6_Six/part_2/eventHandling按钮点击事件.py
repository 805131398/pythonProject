from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QLabel
from PySide6.QtGui import QIcon, QFont
import sys


# 水平布局
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 eventHandling按钮点击事件.py 信号事件处理")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))
        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("改变 Text")
        btn.clicked.connect(lambda: self.clicked_btn())
        self.label = QLabel("Q Label")
        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText(" 已经改变成新的文本")
        self.label.setFont(QFont("JetBrains Mono", 24))
        self.label.setStyleSheet("color:red")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
