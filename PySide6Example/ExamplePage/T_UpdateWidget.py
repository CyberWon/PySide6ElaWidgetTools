from PySide6.QtWidgets import QWidget, QVBoxLayout

from ElaWidgetTools import ElaText


class T_UpdateWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 260)
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(5, 10, 5, 5)
        mainLayout.setSpacing(4)

        updateTitle = ElaText("2026-4-30更新", self)
        updateTitle.setTextPixelSize(15)
        updates = [
            "1、ElaAppBar无边框优化, 修正了Close窗口后再次打开失去原生动画的问题",
            "2、为ElaWindow添加了Dock的便利API",
            "3、组件整体绘制风格和效果优化",
            "4、为部分组件添加了Disable等状态效果",
            "5、QQ交流群: 850243692",
        ]
        mainLayout.addWidget(updateTitle)
        for i, text in enumerate(updates):
            t = ElaText(text, self)
            t.setTextPixelSize(13)
            if i < 4:
                t.setIsWrapAnywhere(True)
            mainLayout.addWidget(t)
        mainLayout.addStretch()
