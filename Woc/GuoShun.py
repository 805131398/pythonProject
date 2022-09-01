import _thread
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from TrayIcon import TrayIcon
from console import YanHua
from Woc import Woc
from ui import main
import ctypes

from ui.main import Dialog

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


# 这个是窗口
class GuoShun(object):
    def __init__(self):
        self.paused = False
        # 创建一个应用对象
        app = QtWidgets.QApplication(sys.argv)
        # 创建QT主窗口对象
        MainWindow = Dialog()

        MainWindow.setWindowIcon(QIcon("guoshun.jpg"))

        MainWindow.resize(287, 177)
        MainWindow.setFixedSize(287, 177)
        # 创建UI对象
        ui = main.Ui_GuoShun()
        # 调用setupUi方法，将设计好的界面-->主窗口上
        ui.setupUi(MainWindow)

        ui.startButton.clicked.connect(lambda: self.control(ui))

        MainWindow.setWindowFlags(QtCore.Qt.Window)
        # 显示一个非模式的对话框，用户可以随便切窗口，.exec()是模式对话框，用户不能随便切
        MainWindow.show()

        ti = TrayIcon(MainWindow)
        ti.show()

        sys.exit(app.exec_())



    def control(self, ui):
        if self.paused:
            self.paused = bool(1 - self.paused)
            ui.startButton.setText("开启")
            self.paused = False
            ui.label_status.setText("未启动")
        else:
            _thread.start_new_thread(self.do_vpn, ())
            self.paused = True
            ui.startButton.setText("暂停")
            ui.label_status.setText("运行中...")

    def do_vpn(self):
        w = Woc()
        w.login()
        devices = {}
        for key, item in w.data.items():
            # 生成一条连接通道
            devices[item['projectName']] = YanHua(item)
        while self.paused:
            w.getVpn()
            for key, item in w.data.items():
                devices[item['projectName']].sendData(item)
            time.sleep(2)
