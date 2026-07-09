---
name: "pyside6-ui-dev"
description: "通用 PySide6 UI 开发指南。当用户需要创建桌面 GUI、编写 Qt 控件、Model/View、自定义绘制、QSS 样式、多线程或排查 PySide6 问题时使用。"
---

# PySide6 UI 开发指南

本 Skill 是通用的 PySide6 桌面 UI 开发参考，不依赖任何第三方组件库（如 ElaWidgetTools）。涵盖应用启动、窗口、布局、信号槽、控件、Model/View、自定义绘制、QSS、事件、多线程与常见陷阱。所有示例均可在 PySide6 ≥ 6.5 上运行。

## 何时使用本 Skill

- 用户要创建/修改 PySide6 桌面 GUI
- 涉及 Qt 控件、Model/View、QSS、自定义绘制、事件处理、多线程
- 排查 PySide6 枚举、信号槽、parent 所有权等问题

## 导入约定

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QHBoxLayout,
    QGridLayout, QFormLayout, QStackedLayout, QPushButton, QLabel, QLineEdit,
    QComboBox, QSpinBox, QCheckBox, QRadioButton, QSlider, QProgressBar,
    QGroupBox, QListView, QTableView, QTreeView, QStyledItemDelegate,
    QStyleOptionViewItem,
)
from PySide6.QtCore import (
    Qt, QObject, QThread, QTimer, QModelIndex, QAbstractListModel,
    QAbstractTableModel, QAbstractItemModel, QSize, QRect, QPoint, Signal, Slot,
)
from PySide6.QtGui import (
    QPainter, QPen, QBrush, QColor, QFont, QPalette, QKeyEvent, QMouseEvent,
    QPixmap,
)
```

枚举一律使用完整形式（带 Flag / Type 后缀），例如 `Qt.AlignmentFlag.AlignCenter`、`Qt.Orientation.Horizontal`、`Qt.ItemDataRole.DisplayRole`、`Qt.ItemFlag.ItemIsEnabled`。

---

## 1. 应用启动模式

### 1.1 QApplication 与事件循环

每个 PySide6 GUI 程序有且仅有一个 `QApplication` 实例，负责初始化 Qt、处理事件循环。

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

def main() -> int:
    app = QApplication(sys.argv)
    # 可设置应用级属性
    app.setApplicationName("MyApp")
    app.setOrganizationName("MyOrg")

    window = QMainWindow()
    window.setWindowTitle("Hello PySide6")
    window.resize(640, 480)
    window.show()

    # exec() 进入事件循环，直到最后一个窗口关闭
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

### 1.2 命令行参数

`sys.argv` 传给 `QApplication` 可让 Qt 解析自带参数（如 `-style`）。如需屏蔽 Qt 参数，传 `[]` 或自定义列表：

```python
app = QApplication([])  # 不解析命令行
```

### 1.3 Offscreen 测试模式

在无显示环境（CI、SSH）下运行 GUI 测试，使用 `offscreen` 平台插件，无需真实显示器：

```python
import os
import sys
from PySide6.QtWidgets import QApplication

# 必须在 QApplication 构造前设置
os.environ["QT_QPA_PLATFORM"] = "offscreen"

app = QApplication(sys.argv)
# 此处可创建 widget、运行单元测试，不会弹出真实窗口
```

或在命令行指定：

```bash
QT_QPA_PLATFORM=offscreen python -m pytest tests/
```

### 1.4 ElaApplication 说明

ElaWidgetTools 提供 `ElaApplication`，是 `QApplication` 的子类，附加主题、动画、Mica 效果等增强。**本 Skill 不依赖它**；如项目使用 ElaWidgetTools，将 `QApplication(sys.argv)` 替换为 `ElaApplication(sys.argv)` 即可，事件循环用法不变。

```python
# 仅当项目依赖 ElaWidgetTools 时
# from ElaWidgetTools import ElaApplication
# app = ElaApplication(sys.argv)
```

### 1.5 优雅退出

```python
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

app = QApplication([])
# 最后一个窗口关闭时退出应用（默认即如此，显式设置更清晰）
app.setQuitOnLastWindowClosed(True)
```

---

## 2. 窗口类型

### 2.1 QMainWindow

适合主窗口，提供菜单栏、工具栏、状态栏、停靠区域，中央区域由 `setCentralWidget` 设置。

```python
from PySide6.QtWidgets import QMainWindow, QTextEdit, QMessageBox
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口示例")
        self.resize(800, 600)

        # 中央控件
        editor = QTextEdit()
        self.setCentralWidget(editor)

        # 菜单栏
        menu = self.menuBar().addMenu("文件(&F)")
        act_save = QAction("保存", self)
        act_save.setShortcut("Ctrl+S")
        act_save.triggered.connect(self.on_save)
        menu.addAction(act_save)

        # 状态栏
        self.statusBar().showMessage("就绪")

    def on_save(self):
        QMessageBox.information(self, "提示", "已保存")
```

### 2.2 QWidget

通用空白窗口/容器，无内置装饰。适合自定义窗口、嵌入式面板。

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PlainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget 窗口")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("我是一个 QWidget"))
```

### 2.3 QDialog

模态/非模态对话框，用于短期交互。`exec()` 阻塞式弹出，`show()` 非模态。

```python
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("关于")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("PySide6 Demo v1.0"))
        btn = QPushButton("关闭")
        btn.clicked.connect(self.accept)  # 返回 Accepted
        layout.addWidget(btn)

# 使用：
# dlg = AboutDialog(self)
# if dlg.exec() == QDialog.DialogCode.Accepted:
#     ...
```

### 2.4 选型建议

| 场景 | 选择 |
|------|------|
| 主窗口、带菜单/工具栏 | QMainWindow |
| 独立自定义窗口、面板 | QWidget |
| 模态弹窗、确认/输入 | QDialog |
| 嵌入式子组件 | QWidget（设 parent） |

---

## 3. 布局系统

布局自动管理子控件的位置和大小，窗口缩放时自动重排。

### 3.1 基础布局类

```python
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QPushButton, QLabel, QLineEdit,
)

class LayoutDemo(QWidget):
    def __init__(self):
        super().__init__()

        # 垂直布局：自上而下
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("第一行"))
        vbox.addWidget(QLabel("第二行"))

        # 水平布局：从左到右
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("左"))
        hbox.addWidget(QPushButton("右"))

        # 网格布局：按 (row, col) 放置
        grid = QGridLayout()
        grid.addWidget(QLabel("姓名:"), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLabel("邮箱:"), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        # 表单布局：标签-字段对齐
        form = QFormLayout()
        form.addRow("用户名:", QLineEdit())
        form.addRow("密码:", QLineEdit())

        # 组合到主布局
        outer = QVBoxLayout(self)
        outer.addLayout(vbox)
        outer.addLayout(hbox)
        outer.addLayout(grid)
        outer.addLayout(form)
```

### 3.2 QStackedLayout

多页面切换，同一时间只显示一个，常配合左侧导航使用。

```python
from PySide6.QtWidgets import QStackedLayout, QPushButton, QWidget

class Pages(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedLayout()
        self.stack.addWidget(QLabel("页面 A"))  # index 0
        self.stack.addWidget(QLabel("页面 B"))  # index 1
        self.stack.setCurrentIndex(0)

        btn = QPushButton("切换")
        btn.clicked.connect(lambda: self.stack.setCurrentIndex(
            1 if self.stack.currentIndex() == 0 else 0
        ))

        outer = QVBoxLayout(self)
        outer.addWidget(btn)
        outer.addLayout(self.stack)
```

### 3.3 margins 与 spacing

```python
layout = QVBoxLayout()
layout.setContentsMargins(12, 12, 12, 12)  # 左 上 右 下
layout.setSpacing(8)  # 控件之间的间距

# 紧凑布局（无外边距）
layout.setContentsMargins(0, 0, 0, 0)
layout.setSpacing(0)
```

### 3.4 拉伸因子与对齐

```python
layout = QVBoxLayout()
layout.addWidget(QPushButton("顶部"))
layout.addStretch(1)  # 弹性空间，吸收多余高度
layout.addWidget(QPushButton("底部"))

# 横向布局中指定控件对齐方式
hbox = QHBoxLayout()
hbox.addWidget(QPushButton("居中"), alignment=Qt.AlignmentFlag.AlignCenter)
```

### 3.5 嵌套布局

布局可嵌套，外层布局用 `addLayout` 加入内层布局：

```python
outer = QVBoxLayout(self)
row = QHBoxLayout()
row.addWidget(QLabel("A"))
row.addWidget(QLabel("B"))
outer.addLayout(row)  # 内层布局加入外层
outer.addWidget(QPushButton("提交"))
```

### 3.6 修改布局属性

```python
# 设置网格列拉伸比（第 1 列拉伸优先）
grid.setColumnStretch(1, 1)

# 让控件跨多列
grid.addWidget(QPushButton("跨两列"), 0, 0, 1, 2)  # row, col, rowSpan, colSpan
```

---

## 4. 信号槽

信号槽是 Qt 的核心通信机制，实现对象间松耦合。

### 4.1 连接内置信号

```python
from PySide6.QtWidgets import QPushButton, QLineEdit

btn = QPushButton("点击")
btn.clicked.connect(self.on_click)  # clicked 是内置信号

edit = QLineEdit()
edit.textChanged.connect(self.on_text_changed)  # 带参数的信号
```

### 4.2 自定义信号

使用 `Signal`（在 `PySide6.QtCore` 中）声明类级信号，类型为 Python 类型或 Qt 类型名。

```python
from PySide6.QtCore import QObject, Signal

class Worker(QObject):
    # 声明信号：参数类型必须显式
    progress = Signal(int)              # 一个 int 参数
    finished = Signal(str, dict)        # str + dict
    error = Signal(str)

    def run(self):
        for i in range(101):
            self.progress.emit(i)
        self.finished.emit("done", {"steps": 100})
```

### 4.3 断开连接

```python
btn.clicked.connect(self.on_click)
# ...
btn.clicked.disconnect(self.on_click)  # 断开特定槽
# btn.clicked.disconnect()             # 断开所有槽（慎用）
```

### 4.4 Lambda 与部分绑定

```python
# 用 lambda 传递额外参数
for i in range(5):
    b = QPushButton(f"按钮 {i}")
    b.clicked.connect(lambda checked=False, idx=i: self.on_button(idx))

# 部分绑定：忽略信号参数
edit.textChanged.connect(lambda _text: self.refresh())
```

> 注意：lambda 中捕获循环变量时务必用默认参数（如 `idx=i`），否则闭包会拿到循环结束后的值。

### 4.5 信号连接信号

```python
btn.clicked.connect(self.some_signal)  # 信号直接转发到信号
```

### 4.6 Slot 装饰器

```python
from PySide6.QtCore import Slot

class MyWindow(QWidget):
    @Slot()
    def on_no_args(self): ...

    @Slot(int)
    def on_progress(self, value): ...

    @Slot(str, result=bool)  # result 指定返回类型
    def on_query(self, key) -> bool: ...
```

### 4.7 信号槽要点

- 信号参数类型必须与槽匹配，否则连接时报错或运行时静默失败
- 跨线程连接默认走 `QueuedConnection`（异步），同线程默认 `AutoConnection`（同步 `DirectConnection`）
- 显式指定连接类型：`sig.connect(slot, Qt.ConnectionType.QueuedConnection)`

---

## 5. 常用控件

### 5.1 QPushButton

```python
from PySide6.QtWidgets import QPushButton

btn = QPushButton("确定")
btn.setToolTip("点击确认")
btn.setEnabled(False)        # 禁用
btn.setDefault(True)         # 对话框默认按钮
btn.setCheckable(True)       # 切换按钮（toggle）
btn.clicked.connect(lambda checked: print("checked =", checked))
```

### 5.2 QLabel

```python
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

label = QLabel("一段文字")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setWordWrap(True)                 # 自动换行
label.setTextFormat(Qt.TextFormat.RichText)  # 支持 HTML
label.setText("<b>粗体</b> <a href='#'>链接</a>")
label.setPixmap(QPixmap("icon.png"))    # 显示图片
label.setScaledContents(True)           # 图片缩放填充
```

### 5.3 QLineEdit

```python
from PySide6.QtWidgets import QLineEdit

edit = QLineEdit()
edit.setPlaceholderText("请输入用户名")
edit.setMaxLength(32)
edit.setEchoMode(QLineEdit.EchoMode.Password)  # 密码模式
edit.setReadOnly(True)
edit.setText("hello")
edit.selectAll()
edit.textChanged.connect(lambda t: print("变化:", t))
edit.returnPressed.connect(lambda: print("回车"))
```

### 5.4 QComboBox

```python
from PySide6.QtWidgets import QComboBox

combo = QComboBox()
combo.addItems(["苹果", "香蕉", "樱桃"])
combo.insertItem(0, "请选择")
combo.setCurrentIndex(1)
# 带用户数据
combo.addItem("红", userData="#FF0000")
color = combo.currentData()       # 取 userData
text = combo.currentText()
combo.currentIndexChanged.connect(lambda i: print("选中", i))
```

### 5.5 QSpinBox / QDoubleSpinBox

```python
from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox

spin = QSpinBox()
spin.setRange(0, 100)
spin.setValue(50)
spin.setSingleStep(5)
spin.setSuffix(" px")
spin.valueChanged.connect(lambda v: print(v))

dspin = QDoubleSpinBox()
dspin.setRange(0.0, 10.0)
dspin.setDecimals(2)
dspin.setSingleStep(0.1)
```

### 5.6 QCheckBox / QRadioButton

```python
from PySide6.QtWidgets import QCheckBox, QRadioButton, QButtonGroup, QVBoxLayout, QWidget

class Checks(QWidget):
    def __init__(self):
        super().__init__()
        # 复选框
        self.cb = QCheckBox("启用通知")
        self.cb.setChecked(True)
        self.cb.toggled.connect(self.on_toggle)

        # 单选框需配合 QButtonGroup 互斥
        self.group = QButtonGroup(self)
        for text in ("低", "中", "高"):
            rb = QRadioButton(text)
            self.group.addButton(rb)
        layout = QVBoxLayout(self)
        layout.addWidget(self.cb)
        for b in self.group.buttons():
            layout.addWidget(b)

    def on_toggle(self, checked: bool):
        print("启用" if checked else "禁用")
```

### 5.7 QSlider

```python
from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

slider = QSlider(Qt.Orientation.Horizontal)
slider.setRange(0, 100)
slider.setValue(30)
slider.setSingleStep(1)
slider.setPageStep(10)
slider.valueChanged.connect(lambda v: print("滑块:", v))
```

### 5.8 QProgressBar

```python
from PySide6.QtWidgets import QProgressBar

bar = QProgressBar()
bar.setRange(0, 100)
bar.setValue(40)
bar.setTextVisible(True)
# 不确定进度（忙碌指示）
# bar.setRange(0, 0)
```

### 5.9 QGroupBox

```python
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QCheckBox

group = QGroupBox("高级选项")
glayout = QVBoxLayout(group)
glayout.addWidget(QCheckBox("选项 A"))
glayout.addWidget(QCheckBox("选项 B"))
glayout.addStretch()
# group 本身作为一个控件加入父布局
```

### 5.10 控件状态

```python
widget.setEnabled(False)   # 禁用（灰显）
widget.setVisible(False)   # 隐藏
widget.setHidden(True)     # 同 setVisible(False)
widget.setVisible(True)
```

---

## 6. Model/View 体系

Qt 的 Model/View 解耦数据与显示：Model 管理数据，View 负责渲染，Delegate 负责编辑/绘制细节。

### 6.1 QAbstractListModel（列表模型）

列表模型是一维的，`rowCount` + `data`，`columnCount` 固定为 1。增删数据必须用 `beginInsertRows`/`endInsertRows` 等通知 View。

```python
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

class StringListModel(QAbstractListModel):
    def __init__(self, items=None, parent=None):
        super().__init__(parent)
        self._items: list[str] = list(items or [])

    def rowCount(self, parent=QModelIndex()) -> int:
        # 顶层（parent 无效）才有行；子项无子行
        return 0 if parent.isValid() else len(self._items)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._items)):
            return None
        item = self._items[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return item
        if role == Qt.ItemDataRole.EditRole:
            return item
        if role == Qt.ItemDataRole.ToolTipRole:
            return f"第 {index.row()} 项: {item}"
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self._items[index.row()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    # 增删必须用 begin/end 包裹
    def append_item(self, item: str):
        row = len(self._items)
        self.beginInsertRows(QModelIndex(), row, row)
        self._items.append(item)
        self.endInsertRows()

    def remove_item(self, row: int):
        if 0 <= row < len(self._items):
            self.beginRemoveRows(QModelIndex(), row, row)
            self._items.pop(row)
            self.endRemoveRows()
```

### 6.2 QAbstractTableModel（表格模型）

二维数据，实现 `rowCount`、`columnCount`、`data`，可选 `headerData`、`flags`、`setData`。

```python
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class TableModel(QAbstractTableModel):
    def __init__(self, rows=None, headers=None, parent=None):
        super().__init__(parent)
        self._rows: list[list] = rows or []
        self._headers: list[str] = headers or []

    def rowCount(self, parent=QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._rows)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        value = self._rows[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            return str(value)
        if role == Qt.ItemDataRole.EditRole:
            return value
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal and section < len(self._headers):
            return self._headers[section]
        return str(section + 1)  # 行号

    def flags(self, index):
        return (Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
                | Qt.ItemFlag.ItemIsEditable)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self._rows[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False
```

### 6.3 QAbstractItemModel（树形模型）

树形模型最复杂，必须实现 `index`、`parent`、`rowCount`、`columnCount`、`data`。用 `internalPointer` 关联节点对象。

```python
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex

class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data            # list[str]，每列一个值
        self.parent = parent
        self.children: list[TreeNode] = []

    def row(self) -> int:
        return self.parent.children.index(self) if self.parent else 0


class TreeModel(QAbstractItemModel):
    def __init__(self, root: TreeNode, parent=None):
        super().__init__(parent)
        self._root = root

    # ---- 必须实现的五个方法 ----
    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parent_node = parent.internalPointer() if parent.isValid() else self._root
        child = parent_node.children[row]
        # internalPointer 存节点引用
        return self.createIndex(row, column, child)

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        node = index.internalPointer()
        parent = node.parent
        if parent is None or parent is self._root:
            return QModelIndex()
        return self.createIndex(parent.row(), 0, parent)

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        node = parent.internalPointer() if parent.isValid() else self._root
        return len(node.children)

    def columnCount(self, parent=QModelIndex()):
        return 1  # 本例单列

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == Qt.ItemDataRole.DisplayRole:
            return node.data[index.column()] if index.column() < len(node.data) else None
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return "名称"
        return None
```

构建树：

```python
root = TreeNode(["根"])
a = TreeNode(["A"], root); root.children.append(a)
a.children.append(TreeNode(["A1"], a))
a.children.append(TreeNode(["A2"], a))
b = TreeNode(["B"], root); root.children.append(b)

model = TreeModel(root)
```

> 关键点：`createIndex(row, column, internalPointer)` 的第三个参数用于在 `data`/`parent` 中取回节点；`internalPointer()` 返回该对象。注意 Python 对象只要被 model 持有引用就不会被 GC。

### 6.4 QStyledItemDelegate（自定义委托）

委托控制单元格的绘制与编辑。重写 `paint`、`sizeHint`，可选 `createEditor`、`setEditorData`、`setModelData`。

```python
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect

class ProgressBarDelegate(QStyledItemDelegate):
    """把 0-100 的整数值渲染为进度条样式"""

    def paint(self, painter: QPainter, option, index):
        value = index.data(Qt.ItemDataRole.DisplayRole)
        if not isinstance(value, (int, float)):
            super().paint(painter, option, index)
            return

        # 先绘制背景（选中态等）
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)
        # 让父类画好背景，再叠加进度
        super().paint(painter, opt, index)

        rect = option.rect.adjusted(4, 4, -4, -4)
        painter.save()
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("#3366CC"))
        w = int(rect.width() * max(0, min(100, value)) / 100.0)
        painter.drawRect(QRect(rect.left(), rect.top(), w, rect.height()))
        painter.setPen(QColor("#000000"))
        painter.drawText(option.rect, Qt.AlignmentFlag.AlignCenter, f"{int(value)}%")
        painter.restore()

    def sizeHint(self, option, index):
        return super().sizeHint(option, index).expandedTo(QSize(80, 24))
```

### 6.5 View 配置

```python
from PySide6.QtWidgets import QListView, QTableView, QTreeView

# 列表视图
lv = QListView()
lv.setModel(model)
lv.setEditTriggers(QListView.EditTrigger.DoubleClicked | QListView.EditTrigger.EditKeyPressed)
lv.setSelectionMode(QListView.SelectionMode.ExtendedSelection)

# 表格视图
tv = QTableView()
tv.setModel(table_model)
tv.horizontalHeader().setStretchLastSection(True)
tv.setAlternatingRowColors(True)
tv.setItemDelegateForColumn(2, ProgressBarDelegate(tv))  # 第 3 列用进度条委托

# 树视图
tree = QTreeView()
tree.setModel(tree_model)
tree.setHeaderHidden(False)
tree.expandAll()
tree.setIndentation(20)
```

### 6.6 UserRole 存储附加数据

```python
# Model 的 data 方法
def data(self, index, role=Qt.ItemDataRole.DisplayRole):
    if role == Qt.ItemDataRole.DisplayRole:
        return self._items[index.row()].name
    if role == Qt.ItemDataRole.UserRole:   # 存原始对象
        return self._items[index.row()]
    return None

# View 取值
item = index.data(Qt.ItemDataRole.UserRole)
```

> `UserRole` 默认值为 0x0100，可继续用 `UserRole + 1`、`UserRole + 2` 存多个自定义字段。

---

## 7. 自定义绘制

`QPainter` 只能在 `paintEvent` 中使用（或在 `QPixmap`/`QImage` 上绘制时无此限制）。

### 7.1 基本绘制

```python
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PySide6.QtCore import Qt, QRect

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 抗锯齿

        # 画笔（轮廓）
        pen = QPen(QColor("#333333"))
        pen.setWidth(2)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        # 画刷（填充）
        painter.setBrush(QBrush(QColor("#66CCFF")))

        rect = self.rect().adjusted(10, 10, -10, -10)
        painter.drawEllipse(rect)            # 圆/椭圆
        painter.drawRect(rect)               # 矩形
        painter.drawLine(rect.topLeft(), rect.bottomRight())  # 线

        # 文字
        font = QFont("Arial", 14, QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(QColor("#FF0000"))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Hello")
```

### 7.2 save / restore

`save()` 保存当前画笔/画刷/变换状态，`restore()` 恢复，避免状态污染：

```python
def paintEvent(self, event):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    painter.save()
    painter.translate(100, 100)       # 平移坐标原点
    painter.rotate(45)                # 旋转 45 度
    painter.drawRect(QRect(-25, -25, 50, 50))
    painter.restore()                 # 恢复，后续绘制不受影响

    painter.drawEllipse(10, 10, 40, 40)
```

### 7.3 在 QPixmap 上离屏绘制

非 paintEvent 场景（如生成图标）可绘制到 `QPixmap`：

```python
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt, QRect

pm = QPixmap(64, 64)
pm.fill(Qt.GlobalColor.transparent)
p = QPainter(pm)
p.setRenderHint(QPainter.RenderHint.Antialiasing)
p.setBrush(QColor("#FF8800"))
p.setPen(Qt.PenStyle.NoPen)
p.drawEllipse(QRect(4, 4, 56, 56))
p.end()  # 必须显式结束
# pm 可用于 QLabel.setPixmap 或 QIcon
```

### 7.4 常用绘制方法速查

| 方法 | 作用 |
|------|------|
| `drawPoint(p)` | 点 |
| `drawLine(p1, p2)` | 直线 |
| `drawRect(rect)` | 矩形 |
| `drawRoundedRect(rect, x, y)` | 圆角矩形 |
| `drawEllipse(rect)` | 椭圆 |
| `drawArc(rect, a, alen)` | 圆弧（角度 1/16 度） |
| `drawPolyline(points)` | 折线 |
| `drawPolygon(points)` | 多边形（自动闭合） |
| `drawText(rect, flags, text)` | 文字 |
| `drawPixmap(target, pm)` | 位图 |
| `fillRect(rect, color)` | 填充矩形 |

> 角度单位：`drawArc` 等用 1/16 度，`90 * 16` 表示 90 度。

---

## 8. QSS 样式

QSS（Qt Style Sheets）类似 CSS，通过 `setStyleSheet` 设置。

### 8.1 基本用法

```python
from PySide6.QtWidgets import QPushButton, QWidget

btn = QPushButton("按钮")
btn.setStyleSheet("""
    QPushButton {
        background-color: #4A90E2;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        font-size: 14px;
    }
""")

# 应用到整个应用
app.setStyleSheet("QWidget { font-family: 'Microsoft YaHei'; }")
```

### 8.2 选择器

```css
/* 类型选择器：所有该类控件 */
QPushButton { background: #eee; }

# /* ID 选择器：setObjectName 设置的 */
# #loginButton { background: #4A90E2; }

/* 类选择器 */
.QPushButton { background: #eee; }

/* 后代选择器：QDialog 内的所有 QPushButton */
QDialog QPushButton { margin: 4px; }

/* 子选择器：直接子级 */
QDialog > QPushButton { margin: 4px; }

/* 属性选择器 */
QPushButton[primary="true"] { background: #4A90E2; }
```

属性选择器需要动态属性：

```python
btn = QPushButton()
btn.setProperty("primary", True)
btn.style().unpolish(btn); btn.style().polish(btn)  # 刷新样式
```

### 8.3 伪状态

```css
QPushButton:hover { background: #5AA1F2; }
QPushButton:pressed { background: #3A80D2; }
QPushButton:disabled { color: #999; background: #ddd; }
QPushButton:checked { background: #2E7D32; }
QLineEdit:focus { border: 2px solid #4A90E2; }
```

常用伪状态：`:hover`、`:pressed`、`:checked`、`:unchecked`、`:focus`、`:disabled`、`:enabled`、`:selected`、`:on`、`:off`、`:first`、`:last`。

### 8.4 常用属性

| 属性 | 说明 |
|------|------|
| `background-color` | 背景色 |
| `color` | 文字色 |
| `border` / `border-radius` | 边框 / 圆角 |
| `padding` | 内边距 |
| `margin` | 外边距 |
| `font-size` / `font-weight` / `font-family` | 字体 |
| `min-width` / `min-height` | 最小尺寸 |
| `text-align` | 文字对齐 |
| `selection-background-color` | 选中色 |

### 8.5 子控件选择器

复杂控件（如 QComboBox、QSpinBox）有子控件，用 `::` 选中：

```css
QComboBox::drop-down { border: none; width: 20px; }
QComboBox::down-arrow { image: url(arrow.png); }
QSpinBox::up-button { width: 16px; }
QScrollBar::handle:vertical { background: #ccc; min-height: 30px; }
```

### 8.6 样式注意事项

- QSS 不支持 CSS 全部特性，无 `box-shadow`（部分平台有），无动画（用 `QPropertyAnimation`）
- 设置 QSS 后，原生主题外观被覆盖，可能影响平台一致性
- 优先级：控件级 `setStyleSheet` > 父控件继承 > 应用级
- 修改动态属性后需 `unpolish`/`polish` 刷新

---

## 9. 事件系统

Qt 事件由 `event()` 分发到具体的 `xxxEvent` 处理函数。重写这些虚函数即可自定义行为。

### 9.1 鼠标事件

```python
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent

class DrawingPad(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 不按下也接收 mouseMoveEvent
        self._last: QPoint | None = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._last = event.position().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._last is not None:
            cur = event.position().toPoint()
            # ... 绘制连线
            self._last = cur

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._last = None
```

> `event.position()` 返回 `QPointF`，用 `.toPoint()` 转 `QPoint`；`event.button()` 区分按键；`event.buttons()` 返回当前按下的所有键（位掩码）。

### 9.2 键盘事件

```python
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class KeyWidget(QWidget):
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        elif event.key() == Qt.Key.Key_Return:
            print("回车")
        elif event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_S:
                self.save()

    def save(self):
        print("保存")
```

> `event.modifiers()` 返回 `Qt.KeyboardModifier` 位掩码，用 `&` 判断是否按下 Ctrl/Shift/Alt。

### 9.3 QEvent 类型

`event.type()` 返回 `QEvent.Type` 枚举，常见：

```python
from PySide6.QtCore import QEvent

# QEvent.Type.MouseButtonPress
# QEvent.Type.MouseMove
# QEvent.Type.KeyPress
# QEvent.Type.Paint
# QEvent.Type.Resize
# QEvent.Type.Close
# QEvent.Type.HoverEnter / HoverLeave / HoverMove
# QEvent.Type.Wheel
```

重写通用 `event()` 可拦截所有事件（少用，优先用具体事件函数）：

```python
def event(self, ev: QEvent) -> bool:
    if ev.type() == QEvent.Type.HoverEnter:
        ...
        return True
    return super().event(ev)
```

### 9.4 eventFilter（事件过滤器）

`eventFilter` 可拦截其他对象的事件，无需子类化。安装过滤器：

```python
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)  # self 拦截 edit 的事件

    def eventFilter(self, obj, ev: QEvent) -> bool:
        if obj is self.edit and ev.type() == QEvent.Type.KeyPress:
            key = ev.key()
            if key == Qt.Key.Key_Escape:
                self.edit.clear()
                return True  # 事件已处理，不再传递
        return super().eventFilter(obj, ev)
```

> 返回 `True` 表示吃掉事件，`False` 表示继续传递。常用于全局快捷键、滚轮转发、输入校验。

### 9.5 paintEvent 与 update

修改绘制内容后调用 `update()` 触发重绘（异步合并）：

```python
class Bar(QWidget):
    def __init__(self):
        super().__init__()
        self._value = 0

    def set_value(self, v: int):
        self._value = v
        self.update()  # 触发 paintEvent，不要直接调用 paintEvent

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawRect(10, 10, self._value, 20)
```

> `repaint()` 是同步立即重绘，一般用 `update()` 即可。

---

## 10. 多线程

**核心原则**：永远不要在非 GUI 线程创建或操作 widget，所有 UI 更新必须通过信号槽回到主线程。

### 10.1 QThread + moveToThread

把 `QObject` 派生类移到 worker 线程，槽函数在该线程执行。

```python
import time
from PySide6.QtCore import QObject, QThread, Signal, Slot

class HeavyWorker(QObject):
    progress = Signal(int)
    finished = Signal(str)

    @Slot()
    def do_work(self):
        for i in range(1, 11):
            time.sleep(0.3)
            self.progress.emit(i * 10)
        self.finished.emit("完成")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 1. 创建 worker 和 thread，不要给 worker 设 parent
        self.thread = QThread()
        self.worker = HeavyWorker()
        self.worker.moveToThread(self.thread)

        # 2. 连接信号（跨线程自动走 QueuedConnection）
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_finished)
        self.thread.started.connect(self.worker.do_work)
        self.worker.finished.connect(self.thread.quit)

        # 3. 启动
        self.thread.start()

    @Slot(int)
    def on_progress(self, v):
        print("进度", v)   # 在主线程执行，可安全更新 UI

    @Slot(str)
    def on_finished(self, msg):
        print(msg)

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()   # 等待线程退出
        event.accept()
```

> 注意：`worker` 不能有 parent；`thread.finished` 后 worker 可设为 None 释放。`thread.wait()` 防止线程未退出就析构导致崩溃。

### 10.2 QTimer

`QTimer` 在所属线程的事件循环中触发，主线程用于定时刷新，worker 线程用于周期任务。

```python
from PySide6.QtCore import QTimer

# 单次触发
QTimer.singleShot(1000, lambda: print("1 秒后执行"))

# 周期触发
self.timer = QTimer(self)
self.timer.setInterval(500)  # 500ms
self.timer.timeout.connect(self.on_tick)
self.timer.start()

def on_tick(self):
    print("tick")

# 停止
self.timer.stop()
```

### 10.3 跨线程通信

跨线程信号槽默认 `QueuedConnection`：发射方的参数被拷贝到接收线程事件队列，接收线程事件循环时执行槽。**只需用信号槽，不要直接调用对方的方法**。

```python
# worker 线程发射，主线程槽函数接收（自动队列连接）
self.worker.progress.connect(self.on_progress)  # 自动 Queued

# 显式指定
sig.connect(slot, Qt.ConnectionType.QueuedConnection)
```

| 连接类型 | 行为 |
|---------|------|
| `DirectConnection` | 同步，在发射线程直接调用槽 |
| `QueuedConnection` | 异步，放到接收线程队列 |
| `AutoConnection`（默认） | 同线程→Direct，跨线程→Queued |
| `BlockingQueuedConnection` | 同 Queued 但发射方阻塞等待，必须跨线程 |

### 10.4 禁止事项

- 不要在 worker 线程调用 widget 方法（`setText`、`update` 等）
- 不要在 worker 线程创建 `QPixmap`、`QImage` 之外的 widget
- 不要用 Python `threading` 直接操作 Qt 对象（如需用，配合 `QMetaObject.invokeMethod` 或信号槽）

---

## 11. 常见陷阱与最佳实践

### 11.1 枚举访问形式

PySide6 6.x 要求（或推荐）完整形式，带 `Flag` / `Type` 后缀：

```python
# 正确
Qt.AlignmentFlag.AlignCenter
Qt.ItemDataRole.DisplayRole
Qt.ItemFlag.ItemIsEnabled
Qt.Orientation.Horizontal
Qt.CheckState.Checked
Qt.PenStyle.SolidLine
Qt.MouseButton.LeftButton
Qt.KeyboardModifier.ControlModifier
QPainter.RenderHint.Antialiasing
QLineEdit.EchoMode.Password
QDialog.DialogCode.Accepted

# 旧形式（可能仍可用，但已弃用/不推荐）
# Qt.AlignCenter       # 弃用
# Qt.DisplayRole       # 弃用
```

### 11.2 QFlags.testFlag 不可用

部分版本 `QFlags` 子类没有 `testFlag`，用按位与 `&` 判断：

```python
modifiers = event.modifiers()
# 不要：if modifiers.testFlag(Qt.KeyboardModifier.ControlModifier):  # 可能报错
# 用：
if modifiers & Qt.KeyboardModifier.ControlModifier:
    print("Ctrl 按下")

flags = index.flags()
if flags & Qt.ItemFlag.ItemIsEditable:
    print("可编辑")

# 判断对齐是否包含某 flag
alignment = label.alignment()
if alignment & Qt.AlignmentFlag.AlignRight:
    ...
```

### 11.3 ItemDataRole.UserRole 的使用

`DisplayRole` 等是 Qt 内置角色，存自定义数据用 `UserRole`（值 0x100）及以上：

```python
# Model 端
def data(self, index, role=Qt.ItemDataRole.DisplayRole):
    obj = self._items[index.row()]
    if role == Qt.ItemDataRole.DisplayRole:
        return obj.name
    if role == Qt.ItemDataRole.UserRole:
        return obj              # 存原始对象
    if role == Qt.ItemDataRole.UserRole + 1:
        return obj.id           # 第二个自定义字段
    return None

# View 端
obj = index.data(Qt.ItemDataRole.UserRole)
obj_id = index.data(Qt.ItemDataRole.UserRole + 1)
```

### 11.4 parent 所有权与内存管理

Qt 用 parent-child 树管理对象生命周期，parent 析构时自动 delete 子对象。Python 侧的 GC 与之叠加，需注意：

```python
class Bad(QWidget):
    def __init__(self):
        super().__init__()
        # 错误：局部变量，方法结束后被 Python GC 回收，widget 立刻消失
        # self.child = QLabel("ok", self)  # 正确：作为属性持有
        label = QLabel("会消失", self)  # 错误示范

class Good(QWidget):
    def __init__(self):
        super().__init__()
        # 方式1：作为属性持有
        self.label = QLabel("ok", self)
        # 方式2：设了 parent 后 Qt 会管理，但仍建议 Python 侧持有引用
        layout = QVBoxLayout(self)
        btn = QPushButton("ok")
        layout.addWidget(btn)  # addWidget 会重设 parent 为布局所在的 widget
```

要点：
- 给 widget 设了 parent（构造参数或 `setParent`），Qt 会管理其销毁
- 但若 Python 侧无引用，对象可能被 GC，导致 C++ 对象被二次释放或提前销毁
- 布局中的控件由布局父 widget 接管 parent
- 跨线程对象不能有 GUI parent

### 11.5 信号参数类型必须匹配

声明信号时类型要明确，连接的槽参数类型必须兼容：

```python
class W(QObject):
    ok = Signal(int)        # int
    msg = Signal(str, dict) # str + dict

w = W()
w.ok.connect(lambda v: print(v))          # OK
# w.ok.connect(lambda s: print(s.upper()))  # 运行时 v 是 int，.upper() 报错
w.msg.emit("hi", {"k": 1})                # OK
# w.msg.emit("hi", 1)                      # 类型不符，行为未定义
```

> PySide6 信号参数是 Python 类型，类型检查较松，但 mismatch 会运行时报错。复杂对象传 `object` 类型：`Signal(object)`。

### 11.6 QPainter 必须在 paintEvent 中使用

```python
# 错误：在任意方法中创建 QPainter(self)
def update_ui(self):
    p = QPainter(self)   # 警告/崩溃：不在 paintEvent 中

# 正确：在 paintEvent 中，或绘制到离屏 QPixmap
def paintEvent(self, event):
    p = QPainter(self)
    p.drawRect(...)

# 离屏绘制
pm = QPixmap(100, 100)
p = QPainter(pm)  # OK，非 widget
```

### 11.7 QModelIndex 的 internalPointer / internalId

树形模型中 `createIndex(row, col, internalPointer)` 的第三个参数用于在 `data`/`parent` 中取回节点：

```python
def index(self, row, column, parent=QModelIndex()):
    node = parent.internalPointer() if parent.isValid() else self._root
    child = node.children[row]
    return self.createIndex(row, column, child)   # 存 Python 对象引用

def parent(self, index):
    node = index.internalPointer()                # 取回对象
    parent = node.parent
    if parent is None or parent is self._root:
        return QModelIndex()
    return self.createIndex(parent.row(), 0, parent)

# 替代方案：用 internalId 存整数 ID，再从字典查（更轻量）
def index(self, row, column, parent=QModelIndex()):
    node = ...
    return self.createIndex(row, column, id(node))   # 存 id
def data(self, index, role):
    node = self._nodes_by_id[index.internalId()]     # 查回
```

> 用 `internalPointer` 时务必保证 Python 侧持有节点引用（防止 GC 导致悬空指针）；用 `internalId` 更安全。

### 11.8 其他常见坑

- **`app.exec()` 还是 `app.exec_()`**：PySide6 用 `exec()`，`exec_()` 已弃用
- **`print` 在 GUI 线程大量调用会卡 UI**：用日志文件或 `qDebug`
- **`QThread` 不能 `wait()` 自己**：在 worker 线程内调用 `thread.wait()` 会死锁
- **`setStyleSheet` 不生效**：检查选择器、属性名拼写、是否需要 `unpolish/polish`
- **中文乱码**：源文件用 UTF-8，`# -*- coding: utf-8 -*-`（Py3 默认），字体设中文字体
- **`QObject` 不能 move 到自己所在的线程**：`moveToThread` 必须在对象创建后、信号连接前
- **lambda 连接循环变量**：用默认参数 `lambda checked=False, i=i: ...`
- **`deleteLater()`**：安全删除对象，在事件循环空闲时执行，优于直接 `del`

### 11.9 deleteLater 与对象销毁

```python
# 安全销毁：事件循环回到后删除
widget.deleteLater()

# 在 worker 完成后清理
self.worker.finished.connect(self.worker.deleteLater)
self.thread.finished.connect(self.thread.deleteLater)
```

### 11.10 推荐项目结构

```
myapp/
├── main.py              # 入口：QApplication + 主窗口
├── models/              # Model/View 模型
│   ├── list_model.py
│   └── tree_model.py
├── widgets/             # 自定义控件
│   ├── chart_widget.py
│   └── delegate.py
├── workers/             # 后台线程任务
│   └── data_loader.py
├── styles/
│   └── dark.qss
└── resources/
    └── icons/
```

加载外部 QSS：

```python
with open("styles/dark.qss", "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())
```

---

## 12. 完整最小示例

一个整合上述概念的最小可运行应用：

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QTableView,
)
from PySide6.QtCore import (
    Qt, QModelIndex, QAbstractTableModel, QThread, QObject, Signal, Slot,
)


class ProgressModel(QAbstractTableModel):
    def __init__(self, headers):
        super().__init__()
        self._rows: list[list] = []
        self._headers = headers

    def rowCount(self, parent=QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._rows)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        v = self._rows[index.row()][index.column()]
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return v
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return str(section + 1)

    def add_row(self, row: list):
        r = len(self._rows)
        self.beginInsertRows(QModelIndex(), r, r)  # 顶层行的 parent 为无效 index
        self._rows.append(row)
        self.endInsertRows()


class Loader(QObject):
    tick = Signal(int, str)

    @Slot()
    def run(self):
        import time
        for i in range(1, 11):
            time.sleep(0.2)
            self.tick.emit(i * 10, f"步骤 {i}")
        self.tick.emit(100, "完成")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 最小示例")
        self.resize(500, 360)

        central = QWidget()
        self.setCentralWidget(central)
        outer = QVBoxLayout(central)

        self.label = QLabel("点击开始加载")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer.addWidget(self.label)

        self.bar = QProgressBar()
        outer.addWidget(self.bar)

        self.table = QTableView()
        self.model = ProgressModel(["进度", "说明"])
        self.table.setModel(self.model)
        outer.addWidget(self.table)

        btn_row = QHBoxLayout()
        self.btn = QPushButton("开始")
        self.btn.clicked.connect(self.start)
        btn_row.addStretch()
        btn_row.addWidget(self.btn)
        outer.addLayout(btn_row)

        # 线程
        self.thread = QThread()
        self.worker = Loader()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.tick.connect(self.on_tick)
        self.worker.tick.connect(lambda _v, _m: None)

    def start(self):
        self.btn.setEnabled(False)
        self.model.beginResetModel()
        self.model._rows.clear()
        self.model.endResetModel()
        self.thread.start()

    @Slot(int, str)
    def on_tick(self, value: int, msg: str):
        self.bar.setValue(value)
        self.label.setText(msg)
        self.model.add_row([value, msg])
        if value == 100:
            self.btn.setEnabled(True)
            self.thread.quit()

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait(3000)
        event.accept()


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QMainWindow { background: #fafafa; }
        QPushButton {
            background: #4A90E2; color: white; border: none;
            padding: 6px 16px; border-radius: 4px;
        }
        QPushButton:hover { background: #5AA1F2; }
        QPushButton:disabled { background: #ccc; }
        QTableView { gridline-color: #ddd; }
        QHeaderView::section { background: #eee; padding: 4px; border: none; }
    """)
    w = MainWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
```

---

## 附录：速查表

### A. 常用枚举完整形式

| 用途 | 完整形式 |
|------|---------|
| 居中对齐 | `Qt.AlignmentFlag.AlignCenter` |
| 左对齐 | `Qt.AlignmentFlag.AlignLeft` |
| 水平方向 | `Qt.Orientation.Horizontal` |
| 垂直方向 | `Qt.Orientation.Vertical` |
| 显示角色 | `Qt.ItemDataRole.DisplayRole` |
| 编辑角色 | `Qt.ItemDataRole.EditRole` |
| 用户角色 | `Qt.ItemDataRole.UserRole` |
| 文本对齐角色 | `Qt.ItemDataRole.TextAlignmentRole` |
| 可启用 | `Qt.ItemFlag.ItemIsEnabled` |
| 可选中 | `Qt.ItemFlag.ItemIsSelectable` |
| 可编辑 | `Qt.ItemFlag.ItemIsEditable` |
| 左键 | `Qt.MouseButton.LeftButton` |
| Ctrl 修饰 | `Qt.KeyboardModifier.ControlModifier` |
| ESC 键 | `Qt.Key.Key_Escape` |
| 回车键 | `Qt.Key.Key_Return` |
| 实线笔 | `Qt.PenStyle.SolidLine` |
| 无笔 | `Qt.PenStyle.NoPen` |
| 抗锯齿 | `QPainter.RenderHint.Antialiasing` |
| 密码模式 | `QLineEdit.EchoMode.Password` |
| 对话框接受 | `QDialog.DialogCode.Accepted` |
| 双击编辑 | `QAbstractItemView.EditTrigger.DoubleClicked` |
| 扩展选择 | `QAbstractItemView.SelectionMode.ExtendedSelection` |
| 队列连接 | `Qt.ConnectionType.QueuedConnection` |
| 鼠标按下事件 | `QEvent.Type.MouseButtonPress` |

### B. 常用信号

| 控件 | 信号 |
|------|------|
| QPushButton | `clicked(bool)`, `pressed()`, `released()`, `toggled(bool)` |
| QLineEdit | `textChanged(str)`, `textEdited(str)`, `returnPressed()`, `editingFinished()` |
| QComboBox | `currentIndexChanged(int)`, `currentTextChanged(str)`, `activated(int)` |
| QSpinBox | `valueChanged(int)` |
| QSlider | `valueChanged(int)`, `sliderMoved(int)` |
| QCheckBox | `toggled(bool)`, `stateChanged(int)` |
| QAbstractItemModel | `dataChanged`, `rowsInserted`, `rowsRemoved`, `modelReset` |
| QThread | `started()`, `finished()` |
| QTimer | `timeout()` |

### C. 排查清单

- [ ] 是否有且仅有一个 `QApplication`？
- [ ] `exec()` 是否被调用（事件循环）？
- [ ] 控件是否设了 parent 或加入布局？
- [ ] 是否在 worker 线程操作了 widget？
- [ ] 信号参数类型是否匹配槽？
- [ ] 枚举是否用了完整形式？
- [ ] `QPainter` 是否只在 `paintEvent` 或 `QPixmap` 上使用？
- [ ] Model 增删行是否用了 `begin/endInsertRows`？
- [ ] 树形模型 `internalPointer` 节点是否被 Python 持有？
- [ ] QSS 选择器、伪状态拼写是否正确？

---

## 参考资源

- PySide6 官方文档：https://doc.qt.io/qtforpython-6/
- Qt 6 文档：https://doc.qt.io/qt-6/
- Model/View 教程：https://doc.qt.io/qt-6/model-view-programming.html
- QSS 参考：https://doc.qt.io/qt-6/stylesheet-reference.html
