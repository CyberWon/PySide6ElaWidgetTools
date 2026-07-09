from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaTreeView,
    ElaPushButton,
    ElaScrollBar,
    ElaSlider,
    ElaText,
)
from ExamplePage.T_BasePage import T_BasePage
from ModelView.T_TreeViewModel import T_TreeViewModel


class T_TreeView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaTreeView")
        self.createCustomWidget("树型视图被放置于此，可在此界面体验其效果并按需添加进项目中")

        treeModel = T_TreeViewModel(self)

        treeLayout = QHBoxLayout()
        treeLayout.setContentsMargins(0, 0, 10, 0)

        # 设置面板
        treeSettingWidget = QWidget(self)
        treeSettingWidgetLayout = QVBoxLayout(treeSettingWidget)
        treeSettingWidgetLayout.setContentsMargins(0, 0, 0, 0)
        treeSettingWidgetLayout.setSpacing(15)

        dataText = ElaText(f"树模型总数据条数：{treeModel.getItemCount()}", self)
        dataText.setTextPixelSize(15)
        treeSettingWidgetLayout.addWidget(dataText)

        self._treeView = ElaTreeView(self)

        # ItemHeight
        itemHeightLayout = self._makeSliderRow(
            "ItemHeight", 200, 600, 350, lambda v: self._treeView.setItemHeight(v // 10)
        )
        treeSettingWidgetLayout.addLayout(itemHeightLayout)

        # HeaderMargin
        headerMarginLayout = self._makeSliderRow(
            "HeaderMargin", 0, 200, 50, lambda v: self._treeView.setHeaderMargin(v // 10)
        )
        treeSettingWidgetLayout.addLayout(headerMarginLayout)

        # Indentation
        indentationLayout = self._makeSliderRow(
            "Indentation", 200, 1000, 200, lambda v: self._treeView.setIndentation(v // 10)
        )
        treeSettingWidgetLayout.addLayout(indentationLayout)

        # 展开/收起
        expandCollapseLayout = QHBoxLayout()
        expandCollapseLayout.setContentsMargins(0, 0, 0, 0)
        expandButton = ElaPushButton("展开全部", self)
        expandButton.setFixedWidth(80)
        expandButton.clicked.connect(self._treeView.expandAll)
        collapseButton = ElaPushButton("收起全部", self)
        collapseButton.setFixedWidth(80)
        collapseButton.clicked.connect(self._treeView.collapseAll)
        expandCollapseLayout.addWidget(expandButton)
        expandCollapseLayout.addWidget(collapseButton)
        expandCollapseLayout.addStretch()
        treeSettingWidgetLayout.addLayout(expandCollapseLayout)
        treeSettingWidgetLayout.addStretch()

        # TreeView
        treeText = ElaText("ElaTreeView", self)
        treeText.setTextPixelSize(18)

        floatScrollBar = ElaScrollBar(self._treeView.verticalScrollBar(), self._treeView)
        floatScrollBar.setIsAnimation(True)
        headerFont = QFont(self._treeView.header().font())
        headerFont.setPixelSize(16)
        self._treeView.header().setFont(headerFont)
        self._treeView.setFixedHeight(450)
        self._treeView.setModel(treeModel)

        treeViewLayout = QVBoxLayout()
        treeViewLayout.setContentsMargins(0, 0, 0, 0)
        treeViewLayout.addWidget(self._treeView)
        treeViewLayout.addStretch()

        treeLayout.addWidget(treeSettingWidget)
        treeLayout.addLayout(treeViewLayout)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaView")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(treeText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(treeLayout)
        self.addCentralWidget(centralWidget, True, False, 0)

    def _makeSliderRow(self, title, lo, hi, init, callback):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        titleText = ElaText(title, self)
        titleText.setTextPixelSize(15)
        slider = ElaSlider(self)
        slider.setRange(lo, hi)
        slider.setValue(init)
        valueText = ElaText(str(init // 10), self)
        valueText.setTextPixelSize(15)

        def onChanged(v):
            valueText.setText(str(v // 10))
            callback(v)

        slider.valueChanged.connect(onChanged)
        layout.addWidget(titleText)
        layout.addWidget(slider)
        layout.addWidget(valueText)
        return layout
