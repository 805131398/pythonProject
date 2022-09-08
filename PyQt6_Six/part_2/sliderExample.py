from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QLabel, \
    QVBoxLayout, QSpinBox, QSlider
from PySide6.QtGui import QIcon, QFont
import sys


# 滑块
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("测试Qt6 slider 滑块")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        # 布局
        hbox = QHBoxLayout()

        # 创建一个滑动模块
        self.slider = QSlider()
        # 设置为水平的
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        # 刻度,在下面[TicksBelow] 😳
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        # 设置间隔区间宽度, 滑动模块的总长为 100, 调整参数看结果直观!
        self.slider.setTickInterval(5)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.change_slider)

        self.label = QLabel('0')

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def change_slider(self):
        self.label.setText(f"{self.slider.value()}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
