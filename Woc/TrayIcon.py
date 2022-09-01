from PyQt5 import QtCore, QtGui, QtWidgets


#  这个类是托盘图标
class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, MainWindow, parent=None):

        super(TrayIcon, self).__init__(parent)
        self.hideStatus = None
        self.ui = MainWindow
        self.paused = False
        self.createMenu()

    def createMenu(self):
        # 设置图标
        self.setIcon(QtGui.QIcon("guoshun.jpg"))
        self.icon = self.MessageIcon()
        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)
        self.hideStatus = False

    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            self.hideStatus = bool(1 - self.hideStatus)
        if self.hideStatus:
            self.ui.show()
        else:
            self.ui.hide()
