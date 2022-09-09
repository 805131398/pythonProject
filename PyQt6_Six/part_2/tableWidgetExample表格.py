from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QLineEdit, QHBoxLayout, QTableWidget, \
    QTableWidgetItem, QVBoxLayout
from PySide6.QtGui import QIcon, QFont
import sys


# 表格
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 QTable 表格")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 创建一个布局容器
        vbox = QVBoxLayout()

        # 声明一个 表格 控件
        self.table_widget = QTableWidget()
        # 设置有多少行
        self.table_widget.setRowCount(3)
        # 设置有多少列
        self.table_widget.setColumnCount(3)
        # 表格表头
        self.table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("Phone"))

        self.table_widget.setItem(1, 0, QTableWidgetItem("张三"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("8888@qq.com"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("136662828201"))

        self.table_widget.setItem(2, 0, QTableWidgetItem("李四"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("99998@qq.com"))
        self.table_widget.setItem(2, 2, QTableWidgetItem("1387838201"))

        vbox.addWidget(self.table_widget)
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
