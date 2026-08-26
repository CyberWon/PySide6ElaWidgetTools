import sys
import os
import signal

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication
from ElaWidgetTools import ElaApplication

from mainwindow import MainWindow

app = QApplication(sys.argv)
eApp = ElaApplication.getInstance()
eApp.init()
w = MainWindow()
w.show()

# Ctrl+C 退出：Qt 事件循环会阻塞 Python 的 SIGINT 处理，
# 用 QTimer 周期性唤醒 Python 解释器，使其能响应 SIGINT
signal.signal(signal.SIGINT, signal.SIG_DFL)
_timer = QTimer()
_timer.timeout.connect(lambda: None)
_timer.start(200)

rc = app.exec()
# 显式销毁主窗口，避免 PySide6 6.10+ 在解释器退出时
# 因 C++ Qt 对象析构顺序不当导致段错误
del w
del app
sys.exit(rc)
