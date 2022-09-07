from PySide6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()

# 底部状态展示
# window.statusBar().showMessage("nihao")

# 菜单栏
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())