# coding = 'utf-8'
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_untitled
import time


# 函数功能：在textBrowser中添加hello world字段
# 输入参数：ui对象
# 输出参数：
def buttonClicked(girl):
    girl.textBrowser.append("hello world")


class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, MainWindow, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()

    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction("显示通知", self, triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        # 设置图标
        self.setIcon(QtGui.QIcon("guoshun.jpg"))
        self.icon = self.MessageIcon()

        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)

    def show_window(self):
        # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()

    def quit(self):
        QtWidgets.qApp.quit()

    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                self.ui.showNormal()
                self.ui.activateWindow()

                self.ui.show()
            else:
                # 若不是最小化，则最小化
                self.ui.showMinimized()

                self.ui.hide()


if __name__ == '__main__':
    # 创建一个应用对象
    app = QtWidgets.QApplication(sys.argv)
    # 创建QT主窗口对象
    MainWindow = QtWidgets.QMainWindow()
    # 创建UI对象
    ui = Ui_untitled.Ui_MainWindow()
    # 调用setupUi方法，将设计好的界面-->主窗口上
    ui.setupUi(MainWindow)

    MainWindow.setWindowFlags(QtCore.Qt.Window)

    ui.pushButton.clicked.connect(lambda: buttonClicked(ui))

    # 显示一个非模式的对话框，用户可以随便切窗口，.exec()是模式对话框，用户不能随便切
    MainWindow.show()

    ti = TrayIcon(MainWindow)
    ti.show()

    sys.exit(app.exec_())