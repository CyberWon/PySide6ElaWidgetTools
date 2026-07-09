from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

from ElaWidgetTools import ElaIconType

# 预先枚举全部图标（跳过值为 0 的 None）。每个元素: (name, codepoint)
_ALL_ICONS = [
    (m.name, int(m.value))
    for m in ElaIconType.IconName
    if int(m.value) != 0
]


class T_IconModel(QAbstractListModel):
    """图标列表模型。对应 C++ T_IconModel。

    C++ 用 QMetaEnum 反射 ElaIconType::IconName；Python 侧直接枚举
    ``ElaIconType.IconName`` 枚举（共 3280 个有效图标，首个 None 跳过）。

    data() 在 UserRole 返回 [图标名, 图标字符(QChar)]，供委托绘制。
    支持搜索模式：setSearchKeyList 传入过滤后的图标名列表。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._isSearchMode = False
        self._searchKeyList = []
        self._rowCount = len(_ALL_ICONS)

    def rowCount(self, parent=QModelIndex()):
        return self._rowCount

    def setSearchKeyList(self, keyList):
        self.beginResetModel()
        self._searchKeyList = list(keyList)
        if self._isSearchMode:
            self._rowCount = len(self._searchKeyList)
        else:
            self._rowCount = len(_ALL_ICONS)
        self.endResetModel()

    def getSearchKeyList(self):
        return list(self._searchKeyList)

    def setIsSearchMode(self, on):
        self._isSearchMode = on
        self.setSearchKeyList(self._searchKeyList)

    def getIsSearchMode(self):
        return self._isSearchMode

    def data(self, index, role=Qt.ItemDataRole.UserRole):
        if role != Qt.ItemDataRole.UserRole or not index.isValid():
            return None
        row = index.row()
        if not self._isSearchMode:
            if row >= len(_ALL_ICONS):
                return None
            name, cp = _ALL_ICONS[row]
            return [name, chr(cp)]
        else:
            if row >= len(self._searchKeyList):
                return None
            name = self._searchKeyList[row]
            cp = self._codepointForName(name)
            return [name, chr(cp)] if cp is not None else [name, ""]

        return None

    def getIconNameFromModelIndex(self, index):
        row = index.row()
        if self._isSearchMode:
            if row < len(self._searchKeyList):
                return "ElaIconType::" + self._searchKeyList[row]
        else:
            if row < len(_ALL_ICONS):
                return "ElaIconType::" + _ALL_ICONS[row][0]
        return ""

    @staticmethod
    def _codepointForName(name):
        for n, cp in _ALL_ICONS:
            if n == name:
                return cp
        return None
