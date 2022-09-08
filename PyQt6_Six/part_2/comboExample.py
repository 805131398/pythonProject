# 多选按钮
import PySide6
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QLabel, QCheckBox, \
    QVBoxLayout, QSpinBox, QComboBox
from PySide6.QtGui import QIcon, QFont
import sys


# 数字加减框
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.resultLabel = None
        self.combo = None
        self.label = None
        self.setGeometry(200, 200, 500, 200)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 组合框")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        self.create_combo()

    def create_combo(self):
        # 布局
        hbox = QHBoxLayout()
        self.label = QLabel("选择账户类型：")
        self.combo = QComboBox()
        self.combo.addItem("请选择")
        self.combo.addItem("中国银行")
        self.combo.addItem("中国工商银行")
        self.combo.addItem("中国农业银行")

        # self.combo.currentIndexChanged.connect(self.combo_changed)
        self.combo.currentIndexChanged.connect(self.combo_changed)

        vbox = QVBoxLayout()
        self.resultLabel = QLabel("")

        hbox.addWidget(self.label)
        hbox.addWidget(self.combo)
        vbox.addLayout(hbox)
        vbox.addWidget(self.resultLabel)
        self.setLayout(vbox)

    def combo_changed(self):
        # 获取文本
        print(self.combo.currentText())
        # 获取下标
        print(self.combo.currentIndex())
        result = "您最终选择了：" + self.combo.currentText()
        self.resultLabel.setText(result)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
