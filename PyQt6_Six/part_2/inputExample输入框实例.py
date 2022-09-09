import sys
import time

from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QDialog, QLineEdit, \
    QInputDialog


class Window(QDialog):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.btn = None
        self.lineEdit = None
        self.label = None
        self.setGeometry(1200, 400, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 input 输入框")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        self.create_dialog()

    def create_dialog(self):
        font = QFont("Times", 15)

        hbox = QHBoxLayout()
        self.label = QLabel("Choose Country:")
        self.label.setFont(font)

        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(font)

        self.btn = QPushButton("Choose Country")
        self.btn.clicked.connect(self.get_int)

        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.btn)
        self.setLayout(hbox)

    def show_dialog(self):
        countries = [
            "枣庄市", "济南市", "德州市", "济宁市", "临沂市", "青岛市", "泰安市", "威海市", "淄博市", "菏泽市",
            "烟台市", "莱芜市", "滨州市", "东营市", "聊城市", "日照市", "潍坊市"
        ]
        # getItem: 就是说弹出的输入框的类型是下拉列表,用于选择元素,元素的内容是上面的数组
        country, ok = QInputDialog.getItem(self, "Input Dialog", "山东省城市列表", countries, 0, False)

        if country and ok:
            self.lineEdit.setText(country)

    def get_text_dialog(self):
        # getText: 弹出一个输入框
        text, ok = QInputDialog.getText(self, "获取用户名称", "输入你的姓名:")
        # 判断他俩不为空或者不是False 然后展示出来 (赋值给: self.lineEdit
        if text and ok:
            self.lineEdit.setText(text)

    def get_int(self):
        # getInt 获取数字
        text, ok = QInputDialog.getInt(self, "获取用户名称", "输入你的姓名:", 1, 2, 30, 50)
        # 判断他俩不为空或者不是False 然后展示出来 (赋值给: self.lineEdit
        if text and ok:
            self.lineEdit.setText(str(text))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
