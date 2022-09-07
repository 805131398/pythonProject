from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit
from PySide6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QLineEdit 输入文本框")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("微软雅黑", 20))
        # line_edit.setText("默认文本")
        line_edit.setPlaceholderText("提示文本")
        # 是否允许输入
        # line_edit.setEnabled(False)
        # 设置文本显示类型 如:密码等
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
