# Form implementation generated from reading ui file '.\like_food.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 409)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_food = QtWidgets.QListWidget(Form)
        self.listWidget_food.setObjectName("listWidget_food")
        self.verticalLayout.addWidget(self.listWidget_food)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_food = QtWidgets.QLineEdit(Form)
        self.lineEdit_food.setObjectName("lineEdit_food")
        self.horizontalLayout.addWidget(self.lineEdit_food)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "like_food"))
        self.label.setText(_translate("Form", "请添加喜欢的食物😍"))
        self.label_2.setText(_translate("Form", "食物:"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton.clicked.connect(self.add_item)

    def add_item(self):
        food = self.lineEdit_food.text()
        self.listWidget_food.addItem(food)
        self.lineEdit_food.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
