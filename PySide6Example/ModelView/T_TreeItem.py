import uuid

from PySide6.QtCore import Qt


class T_TreeItem:
    """树节点。对应 C++ T_TreeItem，纯 Python 实现（不继承 QObject）。

    保留对父节点和子节点列表的引用即可，生命周期由 T_TreeViewModel 持有。
    """

    def __init__(self, itemTitle, parent=None):
        self._itemKey = uuid.uuid4().hex
        self._itemTitle = itemTitle
        self._parentItem = parent
        self._isChecked = False
        self._childrenItems = []

    def getItemKey(self):
        return self._itemKey

    def getItemTitle(self):
        return self._itemTitle

    def getParentItem(self):
        return self._parentItem

    def getChildrenItems(self):
        return self._childrenItems

    def getIsChecked(self):
        return self._isChecked

    def setIsChecked(self, isChecked):
        self._isChecked = isChecked

    def appendChildItem(self, childItem):
        self._childrenItems.append(childItem)

    def getIsHasChild(self):
        return len(self._childrenItems) > 0

    def getRow(self):
        if self._parentItem is not None:
            return self._parentItem.getChildrenItems().index(self)
        return 0

    def setChildChecked(self, isChecked):
        # 与 C++ 保持一致：勾选时先自身后子级，取消时先子级后自身
        if isChecked:
            for node in self._childrenItems:
                node.setIsChecked(isChecked)
                node.setChildChecked(isChecked)
        else:
            for node in self._childrenItems:
                node.setChildChecked(isChecked)
                node.setIsChecked(isChecked)

    def getChildCheckState(self):
        isAllChecked = True
        isAnyChecked = False
        for node in self._childrenItems:
            if node.getIsChecked():
                isAnyChecked = True
            else:
                isAllChecked = False
            childState = node.getChildCheckState()
            if childState == Qt.CheckState.PartiallyChecked:
                isAllChecked = False
                isAnyChecked = True
                break
            elif childState == Qt.CheckState.Unchecked:
                isAllChecked = False
        if len(self._childrenItems) > 0:
            if isAllChecked:
                return Qt.CheckState.Checked
            if isAnyChecked:
                return Qt.CheckState.PartiallyChecked
            return Qt.CheckState.Unchecked
        return Qt.CheckState.Checked
