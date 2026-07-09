import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from ElaWidgetTools import ElaApplication

from mainwindow import MainWindow

app = QApplication(sys.argv)
eApp = ElaApplication.getInstance()
eApp.init()
w = MainWindow()
w.show()
rc = app.exec()
# 显式销毁主窗口，避免 PySide6 6.10+ 在解释器退出时
# 因 C++ Qt 对象析构顺序不当导致段错误
del w
del app
sys.exit(rc)
