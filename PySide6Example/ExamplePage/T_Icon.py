from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListView

from ElaWidgetTools import (
    ElaListView,
    ElaLineEdit,
    ElaMessageBar,
    ElaMessageBarType,
    ElaIconType,
)

from ExamplePage.T_BasePage import T_BasePage
from ModelView.T_IconModel import T_IconModel
from ModelView.T_IconDelegate import T_IconDelegate


class T_Icon(T_BasePage):
    """图标浏览页。对应 C++ T_Icon。

    ListView（IconMode）+ 自定义 Model/Delegate 渲染 ElaAwesome 字体图标。
    左键单击复制对应 ``ElaIconType::xxx`` 枚举名到剪贴板。
    顶部搜索框实时过滤图标名列表。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaIcon")
        self.createCustomWidget("一堆常用图标被放置于此，左键单击以复制其枚举")

        centralWidget = QWidget(self)
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 5, 0)
        centralWidget.setWindowTitle("ElaIcon")

        # ListView
        self._iconView = ElaListView(self)
        self._iconView.setIsTransparent(True)
        self._iconView.setFlow(QListView.Flow.LeftToRight)
        self._iconView.setViewMode(QListView.ViewMode.IconMode)
        self._iconView.setResizeMode(QListView.ResizeMode.Adjust)
        self._iconView.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self._iconView.clicked.connect(self._onIconClicked)

        # Model + Delegate
        self._iconModel = T_IconModel(self)
        self._iconDelegate = T_IconDelegate(self)
        self._iconView.setModel(self._iconModel)
        self._iconView.setItemDelegate(self._iconDelegate)

        # 搜索框
        self._searchEdit = ElaLineEdit(self)
        self._searchEdit.setPlaceholderText("搜索图标")
        self._searchEdit.setFixedSize(300, 35)
        self._searchEdit.textEdited.connect(self._onSearchEditTextEdit)

        centerVLayout.addSpacing(13)
        centerVLayout.addWidget(self._searchEdit)
        centerVLayout.addWidget(self._iconView)
        self.addCentralWidget(centralWidget, True, True, 0)

    def _onIconClicked(self, index):
        iconName = self._iconModel.getIconNameFromModelIndex(index)
        if not iconName:
            return
        QGuiApplication.clipboard().setText(iconName)
        ElaMessageBar.success(
            ElaMessageBarType.PositionPolicy.Top,
            "复制完成",
            iconName + "已被复制到剪贴板",
            1000,
            self,
        )

    def _onSearchEditTextEdit(self, searchText):
        if not searchText:
            self._iconModel.setIsSearchMode(False)
            self._iconModel.setSearchKeyList([])
            self._iconView.clearSelection()
            self._iconView.viewport().update()
            return
        searchKeyList = []
        for m in ElaIconType.IconName:
            if int(m.value) == 0:
                continue
            if searchText.lower() in m.name.lower():
                searchKeyList.append(m.name)
        self._iconModel.setIsSearchMode(True)
        self._iconModel.setSearchKeyList(searchKeyList)
        self._iconView.clearSelection()
        self._iconView.scrollTo(self._iconModel.index(0, 0))
        self._iconView.viewport().update()
