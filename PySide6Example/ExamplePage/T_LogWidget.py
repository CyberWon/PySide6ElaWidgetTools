from PySide6.QtWidgets import QWidget, QVBoxLayout

from ElaWidgetTools import ElaListView, ElaLog
from ModelView.T_LogModel import T_LogModel


class T_LogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 5, 5, 0)

        logView = ElaListView(self)
        logView.setIsTransparent(True)
        self._logModel = T_LogModel(self)
        logView.setModel(self._logModel)
        mainLayout.addWidget(logView)

        ElaLog.getInstance().logMessage.connect(self._logModel.appendLogList)
        for _ in range(4):
            self._logModel.appendLogList("测试条例11223344556677889900")
