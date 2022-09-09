from PySide6.QtWidgets import QApplication, QWidget, QMenu, QLabel
from PySide6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口的坐标以及宽高
        self.setGeometry(200, 200, 700, 400)
        # 设置窗口标题
        self.setWindowTitle("标题")
        # 设置窗口左上角图标
        self.setWindowIcon(QIcon('resource/image/guoshun.jpg'))

        '''  文本模块
        label = QLabel("创建了一个标签", self)
        label.setText("新标签文本")
        # 移动文本位置
        label.move(100, 100)
        # 设置文本大小
        label.setFont(QFont("微软雅黑", 20))
        # 设置文本颜色
        label.setStyleSheet('color:red')

        # 注意: 文本是字符串格式
        label.setText("123")
        # 设置数字可以调用函数
        label.setNum(12)
        # 清空label
        label.clear()
        '''

        '''
        # 将label设置为一张图片
        label = QLabel(self)
        pixmap = QPixmap('resource/image/guoshun.jpg')
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        # 多媒体文件位置
        movie = QMovie("resource/image/u.gif")
        # 设置播放速度
        movie.setSpeed(600)
        # 绑定
        label.setMovie(movie)
        # 开始
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
