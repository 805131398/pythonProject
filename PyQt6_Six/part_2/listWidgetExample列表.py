from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QLabel, \
    QVBoxLayout, QSpinBox, QSlider, QListWidget
from PySide6.QtGui import QIcon, QFont
import sys


# 列表
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 listWidget 列表")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 布局
        vbox = QVBoxLayout()

        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "java")
        self.list_widget.insertItem(2, "c++")
        self.list_widget.insertItem(3, "C#")
        self.list_widget.insertItem(4, "Kotlin")

        self.list_widget.setFont(QFont("微软雅黑", 14))
        self.list_widget.setStyleSheet('background-color:gray')

        self.list_widget.clicked.connect(self.item_click)

        self.list_widget.setFixedWidth(150)

        self.label = QLabel("")
        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def item_click(self):
        self.label.setText(f'您选择了{self.list_widget.currentItem().text()}')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
