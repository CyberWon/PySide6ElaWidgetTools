from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide6.QtGui import QIcon

from ModelView.T_TreeItem import T_TreeItem


class T_TreeViewModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rootItem = T_TreeItem("root")
        self._itemsMap = {}
        for i in range(20):
            level1 = T_TreeItem(f"Lv1--TreeItem{i + 1}", self._rootItem)
            for j in range(6):
                level2 = T_TreeItem(f"Lv2--TreeItem{j + 1}", level1)
                for k in range(6):
                    level3 = T_TreeItem(f"Lv3--TreeItem{k + 1}", level2)
                    for l in range(6):
                        level4 = T_TreeItem(f"Lv4--TreeItem{l + 1}", level3)
                        level3.appendChildItem(level4)
                        self._itemsMap[level4.getItemKey()] = level4
                    level2.appendChildItem(level3)
                    self._itemsMap[level3.getItemKey()] = level3
                level1.appendChildItem(level2)
                self._itemsMap[level2.getItemKey()] = level2
            self._rootItem.appendChildItem(level1)
            self._itemsMap[level1.getItemKey()] = level1
        self._icon = QIcon("Resource/Image/Cirno.jpg")

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parentItem = self._rootItem if not parent.isValid() else parent.internalPointer()
        childItem = None
        if len(parentItem.getChildrenItems()) > row:
            childItem = parentItem.getChildrenItems()[row]
        if childItem is not None:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    def parent(self, child):
        if not child.isValid():
            return QModelIndex()
        childItem = child.internalPointer()
        parentItem = childItem.getParentItem()
        if parentItem == self._rootItem or parentItem is None:
            return QModelIndex()
        return self.createIndex(parentItem.getRow(), 0, parentItem)

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        parentItem = self._rootItem if not parent.isValid() else parent.internalPointer()
        return len(parentItem.getChildrenItems())

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        item = index.internalPointer()
        if role == Qt.ItemDataRole.DisplayRole:
            return item.getItemTitle()
        elif role == Qt.ItemDataRole.DecorationRole:
            return self._icon
        elif role == Qt.ItemDataRole.CheckStateRole:
            if item.getIsHasChild():
                return item.getChildCheckState()
            return Qt.CheckState.Checked if item.getIsChecked() else Qt.CheckState.Unchecked
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.CheckStateRole):
        if role == Qt.ItemDataRole.CheckStateRole:
            item = index.internalPointer()
            item.setIsChecked(not item.getIsChecked())
            item.setChildChecked(item.getIsChecked())
            self.dataChanged.emit(QModelIndex(), QModelIndex(), [role])
            return True
        return super().setData(index, value, role)

    def flags(self, index):
        flags = super().flags(index)
        flags |= Qt.ItemFlag.ItemIsUserCheckable
        return flags

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return "ElaTreeView-Example-4Level"
        return super().headerData(section, orientation, role)

    def getItemCount(self):
        return len(self._itemsMap)
