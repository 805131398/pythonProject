import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QRadioButton, QLabel, QVBoxLayout
from PySide6.QtGui import QIcon, QFont


# 测试 QRadioButton 单选按钮
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 300, 200)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QRadioButton 单选按钮")
        # 设置窗口左上角图标
        self.setWindowIcon(
            QIcon(r'/PyQt6_Six/part_2/resource/image/guoshun.jpg'))
        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()
        #  声明一个单选按钮
        python_radio = QRadioButton("Python")
        python_radio.setIcon(
            QIcon(r'/PyQt6_Six/part_2/resource/image/Python.png'))
        python_radio.setIconSize(QSize(40, 40))
        python_radio.setFont(QFont("微软雅黑", 25, int(QFont.Weight.ExtraBold)))
        python_radio.setChecked(1)
        python_radio.toggled.connect(self.radio_selected2)
        #  声明一个单选按钮
        java_radio = QRadioButton("Java")
        java_radio.setIcon(
            QIcon(r'C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\image\java.png'))
        java_radio.setIconSize(QSize(40, 40))
        java_radio.setFont(QFont("微软雅黑", 25, int(QFont.Weight.ExtraBold)))
        java_radio.toggled.connect(lambda: self.radio_selected("Java"))

        #  声明一个单选按钮
        java_script = QRadioButton("JavaScript")
        java_script.setIcon(QIcon(
            r'C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\image\java-script.png'))
        java_script.setIconSize(QSize(40, 40))
        java_script.setFont(QFont("微软雅黑", 25, int(QFont.Weight.ExtraBold)))
        java_script.toggled.connect(lambda: self.radio_selected("JavaScript"))

        self.label = QLabel("nihao ~")
        self.label.setFont(QFont("Sanserif", 15))

        hbox.addWidget(python_radio)
        hbox.addWidget(java_radio)
        hbox.addWidget(java_script)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def radio_selected(self, language):
        self.label.setText(f"您选择的语言是:{language}")

    def radio_selected2(self):
        radio_btn = self.sender()
        if radio_btn.isChecked:
            self.label.setText(f"您选择的语言是:{radio_btn.text()}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
