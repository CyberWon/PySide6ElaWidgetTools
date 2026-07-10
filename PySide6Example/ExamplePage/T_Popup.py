from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaPushButton,
    ElaContentDialog,
    ElaMessageDialog,
    ElaInputDialog,
    ElaFlyout,
    ElaToolTip,
    ElaScrollPageArea,
    ElaText,
)
from ExamplePage.T_BasePage import T_BasePage


class T_Popup(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaPopup")
        self.createCustomWidget("Popup and dialog components")

        dialogBtn = ElaPushButton("ContentDialog", self)
        dialogBtn.setFixedSize(140, 38)
        dialog = ElaContentDialog(self)
        dialog.setLeftButtonText("取消")
        dialog.setMiddleButtonText("最小化")
        dialog.setRightButtonText("确定")
        dialogBtn.clicked.connect(lambda: dialog.exec())
        dialogArea = ElaScrollPageArea(self)
        dialogLayout = QHBoxLayout(dialogArea)
        dialogLayout.addWidget(ElaText("ElaContentDialog", self))
        dialogLayout.addWidget(dialogBtn)
        dialogLayout.addStretch()

        msgDialogBtn = ElaPushButton("MessageDialog", self)
        msgDialogBtn.setFixedSize(140, 38)
        msgDialog = ElaMessageDialog(self)
        msgDialog.setTitle("标题")
        msgDialog.setContent("左眼用来忘记你、右眼用来记忆你。")
        msgDialog.setFixedSize(280, 150)
        # ElaMessageDialog 继承自 QWidget（非 QDialog），用 show() 显示
        msgDialog.confirmed.connect(lambda: print("确认按钮被点击"))
        msgDialog.cancelled.connect(lambda: print("取消按钮被点击"))
        msgDialogBtn.clicked.connect(
            lambda: msgDialog.show()
        )
        msgDialogArea = ElaScrollPageArea(self)
        msgDialogLayout = QHBoxLayout(msgDialogArea)
        msgDialogLayout.addWidget(ElaText("ElaMessageDialog", self))
        msgDialogLayout.addWidget(msgDialogBtn)
        msgDialogLayout.addStretch()

        inputDialogBtn = ElaPushButton("InputDialog", self)
        inputDialogBtn.setFixedSize(140, 38)
        inputDialog = ElaInputDialog(self)
        inputDialogBtn.clicked.connect(lambda: inputDialog.exec())
        inputDialogArea = ElaScrollPageArea(self)
        inputDialogLayout = QHBoxLayout(inputDialogArea)
        inputDialogLayout.addWidget(ElaText("ElaInputDialog", self))
        inputDialogLayout.addWidget(inputDialogBtn)
        inputDialogLayout.addStretch()

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaPopup")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.addWidget(dialogArea)
        centerLayout.addWidget(msgDialogArea)
        centerLayout.addWidget(inputDialogArea)
        centerLayout.addStretch()
        centerLayout.setContentsMargins(0, 0, 0, 0)
        self.addCentralWidget(centralWidget, True, True, 0)
