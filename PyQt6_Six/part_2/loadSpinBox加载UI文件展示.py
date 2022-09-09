from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QLineEdit


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi(r"C:\Users\Administrator\PycharmProjects\pythonProject\PyQt6_Six\part_2\resource\ui\sugar.ui",
                   self)

        self.lineEditPrice = self.findChild(QLineEdit, "lineEdit_price")
        self.doubleSpin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        # 点击增加、减少按钮时的回调函数
        # self.doubleSpin.valueChanged.connect(self.spin_changed)
        # 失去编辑焦点时触发的事件
        self.doubleSpin.editingFinished.connect(self.spin_changed)

        self.result = self.findChild(QLineEdit, "lineEdit_result")

    def spin_changed(self):
        price = int(self.lineEditPrice.text())
        if price != 0:
            dsb = self.doubleSpin.value()
            result = price * dsb
            self.result.setText(result.__str__())


app = QApplication([])
windows = UI()
windows.show()
app.exec()
