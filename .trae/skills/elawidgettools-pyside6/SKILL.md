---
name: "elawidgettools-pyside6"
description: "ElaWidgetTools 的 PySide6/shiboken6 Python 绑定专项 skill。当用户 import ElaWidgetTools、构建/调试 .so 绑定、用 ElaWindow/ElaMessageBar 等组件的 Python 侧 API，或排查枚举访问、out 参数元组、ElaRouter 不可用等绑定时使用。"
---

# ElaWidgetTools + PySide6 绑定专项

本 skill 聚焦 **ElaWidgetTools 通过 shiboken6 绑定到 Python（PySide6）** 的使用，覆盖构建坑、生成代码 bug 修复、API 差异、Python 调用约定与组件最小用法。与 `skill/SKILL.md`（C++ 侧）互补：C++ skill 讲类名选型与 `#include`，本 skill 讲 `from ElaWidgetTools import ...` 之后的 Python 侧一切问题。

## 触发判定

满足以下任一条件时启用本 skill：

1. 项目源码中出现 `from ElaWidgetTools import` 或 `import ElaWidgetTools`
2. 用户在 Python/PySide6 环境中调试 ElaWidgetTools 绑定（`.so` 加载、`import` 失败、shiboken 生成）
3. 用户提及 shiboken6 / shiboken6_generator / `fix_class_name.py` / `fix_out_params.py` / `fix_install_names.py`
4. 用户运行或修改 `PySide6Example/` 下的示例
5. 用户询问 ElaWindow 的 `addExpanderNode`/`addFooterNode`/`addCategoryNode` 在 Python 下如何拿 key
6. 用户询问 `ElaRouter` / `getNavigationSuggestDataList` / `QFlags.testFlag` 等在 Python 下不可用的原因

**反向规则**：纯 C++/Qt 项目走 `skill/SKILL.md`；不涉及 Python 绑定时不启用本 skill。

## 与 C++ skill 的关键区别

| 维度 | C++ skill | 本 skill（Python） |
|---|---|---|
| 语言 | C++ / Qt | Python / PySide6 |
| 接入方式 | `target_link_libraries(... ElaWidgetTools)` | `from ElaWidgetTools import ...`（.so 装入 site-packages） |
| 枚举访问 | `ElaIconType::IconName::House` | `ElaIconType.IconName.House` |
| out 参数 | `QString& key; addExpanderNode(..., key, ...)` | `_, key = addExpanderNode(..., "", ...)`（元组解包） |
| 资源路径 | `:/Resource/Image/...`（Qt rcc） | `"Resource/Image/..."`（文件系统相对路径） |
| 路由器 | `ElaRouter` 可用 | `ElaRouter.addRoute/addRoutes/push/beforeEach` **不可用**（std::function 限制） |
| 关闭窗口 | `eApp->init()` | `eApp = ElaApplication.getInstance(); eApp.init()` |

## 环境准备与构建

### 依赖版本（已验证可用组合）

```
PySide6            == 6.10.3
shiboken6          == 6.10.3
shiboken6_generator== 6.10.3
Qt                 == 6.10.3（编译用，独立目录）
```

三个 shiboken/PySide6 包版本必须**严格对齐**，且与编译用的 Qt 版本一致。版本不一致会导致符号缺失或 `.so` 加载即崩。

### Qt 编译环境（aqtinstall 装到独立目录）

为避免与 Homebrew Qt 或系统 Qt 串味，推荐用 aqtinstall 把 Qt 6.10.3 装到独立目录：

```bash
pip install aqtinstall
aqt install-qt mac desktop 6.10.3 clang_64 -m qtwidgets qtgui qtcore \
  -O /Users/cyber/Qt/6.10.3
# 安装后 Qt 前缀在 /Users/cyber/Qt/6.10.3/macos
```

运行时由 PySide6 自带的 Qt（`site-packages/PySide6/Qt/lib`）接管，编译期 Qt 只用于头文件/链接符号匹配。

### cmake 命令样板

```bash
cmake -S . -B build-python \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_OSX_SYSROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk \
  -DCMAKE_PREFIX_PATH=/Users/cyber/Qt/6.10.3/macos \
  -DPython3_EXECUTABLE=/Users/cyber/miniconda3/envs/aidub/bin/python \
  -DShiboken6_DIR=/Users/cyber/miniconda3/envs/aidub/lib/python3.10/site-packages/shiboken6/lib/cmake/Shiboken6 \
  -DPySide6_DIR=/Users/cyber/miniconda3/envs/aidub/lib/python3.10/site-packages/PySide6/lib/cmake/PySide6 \
  -DBUILD_PYTHON_BINDINGS=ON
cmake --build build-python --target ElaWidgetToolsPython -j
cmake --install build-python   # 自动装入目标 Python 的 site-packages
```

要点：

- `CMAKE_PREFIX_PATH` 指向 Qt 6.10.3 独立目录
- `Shiboken6_DIR` / `PySide6_DIR` 指向目标 Python 的 `site-packages`
- `Python3_EXECUTABLE` 指向目标 Python（决定 `.so` 装到哪个 site-packages）
- `BUILD_PYTHON_BINDINGS=ON` 触发 `bindings/CMakeLists.txt`

### 强制重新生成绑定源码

改了 `typesystem`/`global.h` 或 C++ 头文件后，shiboken 缓存的生成代码不会自动失效，必须手动删：

```bash
rm -rf build-python/bindings/ElaWidgetTools
cmake --build build-python --target ElaWidgetToolsPython -j
```

### macOS 特有：CMAKE_OSX_SYSROOT 必须用 MacOSX15.4.sdk

Qt 6.10.3 仍链接 `AGL.framework`，而新版 macOS SDK（26.1+）已移除 AGL，导致链接报错 `framework not found AGL`。

**必须**：

```bash
-DCMAKE_OSX_SYSROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk
```

系统上保留 13.3 / 14.4 / 15.4 三个旧 SDK 可用；若被 Xcode 升级清掉，从 Apple Developer 站单独下载安装。验证：

```bash
xcodebuild -showsdks | grep MacOSX
ls /Library/Developer/CommandLineTools/SDKs/
```

### macOS 运行时 Qt 冲突：fix_install_names.py

**问题**：编译期用独立 Qt 6.10.3，运行期 PySide6 自带 Qt 6.10.3（在 `site-packages/PySide6/Qt/lib`），两套 Qt 同时加载会报 `QEventDispatcherGlib::qt_metacall` 等符号缺失，进程启动即崩。

**解决**：`bindings/CMakeLists.txt` 在 POST_BUILD 阶段调用 `fix_install_names.py`，把 `.so` 里对 Qt framework 的引用从绝对路径改写为 `@rpath`，并设置三条 `@loader_path` rpath：

- `@loader_path/PySide6/Qt/lib`
- `@loader_path/PySide6`
- `@loader_path/shiboken6`

这样 `.so` 安装到 `site-packages/` 后能正确解析到同目录的 PySide6/shiboken6 自带 Qt。

**坑**：改了 `bindings/CMakeLists.txt` 后必须重新触发 POST_BUILD。若用 `cmake --build` 增量构建没重跑 fix_install_names，删 `build-python/bindings` 重生。手动验证：

```bash
otool -L $(python -c "import ElaWidgetTools, os; print(ElaWidgetTools.__file__)")
# 应看到 @rpath/QtWidgets.framework/... 而非绝对路径
```

### .so 文件名后缀必须带前导点

`bindings/CMakeLists.txt` 里 `SUFFIX` 必须是：

```cmake
set_target_properties(${BINDINGS_MODULE_TARGET} PROPERTIES
    PREFIX ""
    SUFFIX ".${Python3_SOABI}.so"   # 注意前导点
    OUTPUT_NAME "ElaWidgetTools"
)
```

即生成 `ElaWidgetTools.cpython-310-darwin.so`。若写成 `"${Python3_SOABI}.so"`（少一个点），生成 `ElaWidgetToolscpython-310-darwin.so`，Python 的 `import ElaWidgetTools` 找不到模块。

`Python3_SOABI` 由 `find_package(Python3 ... Development)` 自动推导（如 `cpython-310-darwin`）。

## shiboken 生成代码的两个 bug 及修复

生成流程：shiboken 生成 → `fix_class_name.py` → `fix_out_params.py` → 编译链接 → `fix_install_names.py`。三个脚本都接在 `bindings/CMakeLists.txt` 的 `add_custom_command` / POST_BUILD 里，改 typesystem/header 后 `rm -rf build-python/bindings/ElaWidgetTools` 重生即可，**无需手动跑脚本**。

### Bug 1：%CLASS_NAME 未替换

**现象**：`ElaMessageBar` / `ElaSnackbar` / `ElaToast`（无私有/公有构造函数的类）生成的代码形如 `cppSelf->::%CLASS_NAME::method(...)`，`%CLASS_NAME` 未被替换，编译报错 `expected a class or namespace`。

**原因**：shiboken 在无构造函数类上的模板变量替换缺陷，`%CLASS_NAME` 占位符未被实例化为真实类名。

**修复**：`bindings/fix_class_name.py` 从生成的 cpp 里 `reinterpret_cast< ::ClassName *` 正则提取真实类名，替换该文件内所有 `%CLASS_NAME`。

**影响范围**：所有"静态方法为主、无构造函数"的类，目前是 `ElaMessageBar`、`ElaSnackbar`、`ElaToast`。新增此类绑定时若编译报 `%CLASS_NAME` 未替换，确认 `fix_class_name.py` 跑过即可。

### Bug 2：非 void 返回函数的 QString& out 参数被丢弃（重要）

**现象**：`ElaWindow::addExpanderNode` / `addFooterNode` / `addCategoryNode` 通过 `QString&` out 参数返回新建节点 key，但 Python 侧只拿到 `NodeResult`，key 丢失，**无法嵌套页面**（拿到 key 才能给子节点当 parentKey）。

**原因**：shiboken 的 return-value-heuristic 只对 `void` 返回函数把 out-ref 提升为元组元素；非 void 返回时 out-ref 被静默丢弃，生成代码只 `copyToPython(&cppResult)`，不处理 `cppArg1`（即那个 `QString&`）。

**修复**：`bindings/fix_out_params.py` 硬编码 6 个重载：

- `addCategoryNode` case0 / case1
- `addExpanderNode` case0 / case1
- `addFooterNode` case0 / case1

把生成代码里的 `pyResult = copyToPython(NodeResult)` 改写为构造 `(NodeResult, key)` 元组。key 变量映射：除 `addFooterNode case1`（带 page 重载）是 `cppArg2` 外，其余都是 `cppArg1`。

### Python 调用约定：key 是 in/out 参数

C++ 里 key 是 out 参数（传引用带回），shiboken 把它做成 in/out。Python 侧必须：

1. 传 `""`（空字符串）占位
2. 解包返回的元组：`_, viewKey = addExpanderNode("title", "", IconName)`

```python
# 正确：元组解包
_, viewKey = self.addExpanderNode("ElaView", "", ElaIconType.IconName.CameraViewfinder)
_, viewCategoryKey = self.addCategoryNode("View Content", "", viewKey)
self.addPageNode("ElaListView", self._listViewPage, viewKey, 9, ElaIconType.IconName.List)

# 错误：直接拿返回值，key 丢失，无法嵌套
viewKey = self.addExpanderNode("ElaView", "", ElaIconType.IconName.CameraViewfinder)
# viewKey 此时是 NodeResult 枚举，不是字符串
```

### 新增带 out 参数的绑定方法

若后续给其他带 `QString&` out 参数的方法加绑定，需在 `fix_out_params.py` 的 `TARGETS` 列表追加 `(函数名, case索引, key变量名)`，并从生成代码里确认 key 对应的局部变量名（一般是 `cppArg1`，重载带额外前置参数时可能是 `cppArg2`）。

## Python 绑定限制

### std::function<QWidget*()> 无法绑定到 Python 可调用对象

`ElaRouter` 的路由回调签名是 `std::function<QWidget*()>`。shiboken 对 `std::function` 返回裸指针的绑定支持有限，当前 **`ElaRouter.addRoute` / `addRoutes` / `push` / `beforeEach` 在 Python 侧不可用**（调用即崩或不生效）。

**替代方案**：用 `ElaWindow` 的 `addPageNode` 系列提前注册页面实例（传 `QWidget*`），通过 `self.navigation(pageKey)` 跳转。需要"懒加载"时自己在外层 Python 代码里按需 `new` 页面再 `addPageNode`。

### getNavigationSuggestDataList 未绑定

`ElaWindow::getNavigationSuggestDataList`（C++ 用于填充 `ElaSuggestBox` 的导航建议列表）未绑定到 Python。需**手动构建 SuggestBox 建议列表**：

```python
def _populateSuggestBox(self):
    suggestions = [
        (ElaIconType.IconName.House, "HOME"),
        (ElaIconType.IconName.CabinetFiling, "ElaBaseComponents"),
        (ElaIconType.IconName.List, "ElaListView"),
        # ...
    ]
    pageKeyMap = {
        "HOME": self._homePage.property("ElaPageKey"),
        "ElaBaseComponents": self._baseComponentsPage.property("ElaPageKey"),
        # ...
    }
    for icon, title in suggestions:
        key = pageKeyMap.get(title, "")
        self._windowSuggestBox.addSuggestion(icon, title, {"ElaPageKey": key})
```

点击建议时从 `suggestData.getSuggestData()` 取 `ElaPageKey`，调 `self.navigation(key)` 跳转。

### QFlags.testFlag 在某些版本不可用

PySide6 部分 `QFlags` 子类没有 `.testFlag`，或行为异常。用**按位与 + bool** 替代：

```python
from PySide6.QtWidgets import QStyle

# 不可靠
# if option.state.testFlag(QStyle.StateFlag.State_HasFocus):

# 可靠
if bool(option.state & QStyle.StateFlag.State_HasFocus):
    ...
```

适用于自定义 Delegate 的 `paint` 里判断 `State_HasFocus` / `State_Selected` / `State_MouseOver` 等场景。

## 核心组件 Python 用法

以下每个组件给出最小可用 Python 代码。所有 `import` 形如 `from ElaWidgetTools import ...`。

### ElaApplication

全局单例，**必须** `init()`，否则主题/Mica/暗色模式全部失效。

```python
import sys
from PySide6.QtWidgets import QApplication
from ElaWidgetTools import ElaApplication

app = QApplication(sys.argv)
eApp = ElaApplication.getInstance()   # 单例，不是 new
eApp.init()                            # 必须
```

### ElaWindow

带侧边导航 + 堆栈页面 + 面包屑路由的主窗口。继承使用。

```python
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget
from ElaWidgetTools import (
    ElaWindow, ElaIconType, ElaContentDialog, ElaThemeType,
)

class MainWindow(ElaWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaWidgetTools - PySide6")
        self.resize(1200, 740)
        self.setUserInfoCardPixmap(QPixmap("Resource/Image/Cirno.jpg"))
        self.setUserInfoCardTitle("ElaWidgetTools")
        self.setUserInfoCardSubTitle("PySide6 Example")
        self.moveToCenter()

        # 关闭前弹确认框（拦截默认关闭）
        closeDialog = ElaContentDialog(self)
        closeDialog.rightButtonClicked.connect(self.close)
        self.setIsDefaultClosed(False)
        self.closeButtonClicked.connect(lambda: closeDialog.exec())

        self._registerPages()

    def _registerPages(self):
        # 顶层页面：直接传 page 实例 + 图标
        self.addPageNode("HOME", self._homePage, ElaIconType.IconName.House)

        # 分类节点（不可点击的分组标题）：key 解包
        _, controlKey = self.addCategoryNode("Controls", "")

        # 展开节点（可折叠、可嵌套）：key 解包后用作子节点 parentKey
        _, viewKey = self.addExpanderNode(
            "ElaView", "", ElaIconType.IconName.CameraViewfinder
        )
        self.addPageNode(
            "ElaListView", self._listViewPage, viewKey, 9, ElaIconType.IconName.List
        )
        self.expandNavigationNode(viewKey)

        # Footer 节点（导航栏底部）：key 解包
        _, settingKey = self.addFooterNode(
            "Setting", self._settingPage, "", 0, ElaIconType.IconName.GearComplex
        )
        self._settingKey = settingKey

    def navigationTo(self, page):
        # 通过页面属性拿 key 再跳转
        self.navigation(page.property("ElaPageKey"))
```

`addPageNode` 签名（Python 侧）：

- `addPageNode(title, page, icon)` — 顶层
- `addPageNode(title, page, parentKey, icon)` — 指定父节点
- `addPageNode(title, page, parentKey, keyDepth, icon)` — 带深度

`addExpanderNode` / `addCategoryNode` / `addFooterNode` 都返回 `(NodeResult, key)` 元组，**必须解包**。

### ElaScrollPage

页面基类。核心方法 `createCustomWidget(desText)` 装配顶部标题栏，`addCentralWidget(widget)` 装入主内容区。

```python
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from ElaWidgetTools import (
    ElaScrollPage, ElaText, ElaToolButton, ElaMenu,
    ElaIconType, ElaTheme, ElaThemeType,
)

class T_BasePage(ElaScrollPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 主题变化时刷新
        eTheme = ElaTheme.getInstance()
        eTheme.themeModeChanged.connect(lambda _: self.update() if parent else None)

    def createCustomWidget(self, desText: str):
        customWidget = QWidget(self)
        subTitleText = ElaText(self)
        subTitleText.setText("https://github.com/RainbowCandyX/ElaWidgetTools")
        subTitleText.setTextPixelSize(11)

        themeButton = ElaToolButton(self)
        themeButton.setFixedSize(35, 35)
        themeButton.setIsTransparent(False)
        themeButton.setElaIcon(ElaIconType.IconName.MoonStars)
        eTheme = ElaTheme.getInstance()
        themeButton.clicked.connect(
            lambda: eTheme.setThemeMode(
                ElaThemeType.ThemeMode.Dark
                if eTheme.getThemeMode() == ElaThemeType.ThemeMode.Light
                else ElaThemeType.ThemeMode.Light
            )
        )

        layout = QVBoxLayout(customWidget)
        layout.addWidget(subTitleText)
        layout.addWidget(themeButton)
        self.setCustomWidget(customWidget)

    def setupContent(self):
        centralWidget = QWidget(self)
        centerLayout = QVBoxLayout(centralWidget)
        # ... 装内容
        self.addCentralWidget(centralWidget, True, True, 0)
```

`addCentralWidget` 签名：`addCentralWidget(widget, isShowTittle=False, isAddScrollBar=True, spacing=0)`。

### ElaMessageBar

弹出式信息栏，八方向锚定。**全部静态方法**（无构造函数，受 `fix_class_name.py` 修复）。

```python
from ElaWidgetTools import ElaMessageBar, ElaMessageBarType

# PositionPolicy 八个方向：Top / TopLeft / TopRight / Bottom / BottomLeft / BottomRight / Left / Right
ElaMessageBar.success(
    ElaMessageBarType.PositionPolicy.Top,
    "Success",
    "初始化成功!",
    2000,                # 显示时长 ms
)

ElaMessageBar.information(
    ElaMessageBarType.PositionPolicy.BottomRight, "Info", "提示", 2000, self
)

ElaMessageBar.warning(
    ElaMessageBarType.PositionPolicy.Top, "Warning", "警告", 3000
)

ElaMessageBar.error(
    ElaMessageBarType.PositionPolicy.Top, "Error", "出错了", 5000
)
```

签名：`success(position, title, text, duration, parent=None)`。`parent` 不传时挂在全局窗口。

### ElaIconType

3280 个 FluentUI 图标的枚举容器。访问形式 `ElaIconType.IconName.<名字>`。

```python
from ElaWidgetTools import ElaIconType, ElaToolButton, ElaMenu

btn = ElaToolButton(self)
btn.setElaIcon(ElaIconType.IconName.House)         # 房子
btn.setElaIcon(ElaIconType.IconName.GearComplex)   # 齿轮
btn.setElaIcon(ElaIconType.IconName.MoonStars)     # 月亮

# 菜单图标
menu = ElaMenu(self)
menu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
menu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
```

枚举值名采用 PascalCase（`House` / `GearComplex` / `ArrowRotateRight` / `Bluetooth` / `Cards`），与 C++ `ElaIconType::IconName::House` 一一对应。完整列表见 `ElaWidgetTools/IconEngine/ElaIconType.h`（3280 项）。

### ElaTheme

主题管理器单例。`Light` / `Dark` 两模式，无 `FollowSystem` 枚举（跟随系统是独立开关）。

```python
from ElaWidgetTools import ElaTheme, ElaThemeType

eTheme = ElaTheme.getInstance()

# 当前模式
mode = eTheme.getThemeMode()   # ElaThemeType.ThemeMode.Light / Dark

# 切换
eTheme.setThemeMode(ElaThemeType.ThemeMode.Dark)

# 跟随系统
eTheme.setIsFollowSystemTheme(True)

# 主题色（Light/Dark 各一套独立色板，两边都 set 才两个模式都生效）
eTheme.setThemeColor(ElaThemeType.ThemeMode.Dark,
                     ElaThemeType.ThemeColor.PrimaryNormal,
                     QColor("#3498db"))

# 当前主题色
color = eTheme.getThemeColor(ElaThemeType.ThemeColor.PrimaryNormal)

# 信号：模式实际生效时
eTheme.themeModeChanged.connect(lambda mode: print("切换到", mode))
# 信号：跟随系统开关变化
eTheme.pIsFollowSystemThemeChanged.connect(lambda follow: print("follow", follow))
```

`ElaThemeType.ThemeMode` 只有 `Light` / `Dark`。`ElaThemeType.ThemeColor` 含 `PrimaryNormal` / `ScrollBarHandle` / `ToggleSwitchNoToggledCenter` 等数十种色键，见 `ElaWidgetTools/ElaDef.h`。

### ElaNavigationRouter

前进/后退历史导航单例。

```python
from ElaWidgetTools import ElaNavigationRouter, ElaToolButton, ElaIconType

router = ElaNavigationRouter.getInstance()

backBtn = ElaToolButton(self)
backBtn.setElaIcon(ElaIconType.IconName.AngleLeft)
backBtn.clicked.connect(router.navigationRouteBack)

forwardBtn = ElaToolButton(self)
forwardBtn.setElaIcon(ElaIconType.IconName.AngleRight)
forwardBtn.clicked.connect(router.navigationRouteForward)

# 路由状态变化信号：routeMode 是 ElaNavigationRouterType.RouteMode 枚举
# BackValid=0 / BackInvalid=1 / ForwardValid=2 / ForwardInvalid=3
router.navigationRouterStateChanged.connect(self._onRouteStateChanged)

def _onRouteStateChanged(self, routeMode):
    try:
        rm = int(routeMode)
    except (TypeError, ValueError):
        return
    if rm == 0:
        self._leftButton.setEnabled(True)
    elif rm == 1:
        self._leftButton.setEnabled(False)
    elif rm == 2:
        self._rightButton.setEnabled(True)
    elif rm == 3:
        self._rightButton.setEnabled(False)
```

注意 `routeMode` 是枚举对象，`int()` 转换更稳。

### ElaListView / ElaTreeView / ElaTableView

视图三件套，配合自定义 Model/Delegate。

```python
from PySide6.QtWidgets import QListView
from ElaWidgetTools import ElaListView, ElaIconType

view = ElaListView(self)
view.setIsTransparent(True)                       # 透明背景
view.setFlow(QListView.Flow.LeftToRight)
view.setViewMode(QListView.ViewMode.IconMode)
view.setResizeMode(QListView.ResizeMode.Adjust)
view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

view.setModel(self._iconModel)
view.setItemDelegate(self._iconDelegate)
view.clicked.connect(self._onClicked)
```

`ElaTreeView` / `ElaTableView` 同理：`setIsTransparent(True)` + `setModel` + `setItemDelegate`。`ElaTableWidget` 是直接填值的便捷版（无需 Model）。

### ElaFlowLayout

流式布局，自动换行 + 动画。

```python
from ElaWidgetTools import ElaFlowLayout

flowLayout = ElaFlowLayout(0, 5, 5)        # (margin, hSpacing, vSpacing)
flowLayout.setContentsMargins(30, 0, 0, 0)
flowLayout.setIsAnimation(True)
for card in cards:
    flowLayout.addWidget(card)
```

`ElaFlowLayout` 是 `QLayout` 子类，直接 `setLayout` 或加到父 layout。

### ElaScrollPageArea

圆角背景的滚动区域容器，**最常用的内容包装器**。

```python
from PySide6.QtWidgets import QHBoxLayout
from ElaWidgetTools import ElaScrollPageArea, ElaText, ElaToggleSwitch

area = ElaScrollPageArea(self)
areaLayout = QHBoxLayout(area)
areaLayout.addWidget(ElaText("启用通知", self))
areaLayout.addStretch()
areaLayout.addWidget(ElaToggleSwitch(self))
```

### ElaContentDialog

带遮罩的对话框，三按钮（左/中/右）。

```python
from ElaWidgetTools import ElaContentDialog

dialog = ElaContentDialog(self)
# 默认三按钮：左/中/右，文字可改
dialog.setLeftButtonText("取消")
dialog.setMiddleButtonText("最小化")
dialog.setRightButtonText("退出")

dialog.rightButtonClicked.connect(self.close)
dialog.middleButtonClicked.connect(lambda: (dialog.close(), self.showMinimized()))

dialog.exec()   # 模态
```

`ElaInputDialog` / `ElaMessageDialog` 用法相同（`exec()` 弹出）。

### ElaDockWidget

可拖拽停靠浮动面板。

```python
from PySide6.QtCore import Qt
from ElaWidgetTools import ElaDockWidget

logDock = ElaDockWidget("日志信息", self)
logDock.setWidget(self._logWidget)   # 装入内容 widget
self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, logDock)
self.resizeDocks([logDock], [200], Qt.Orientation.Horizontal)
```

## PySide6Example 示例结构

参考实现位于 `/Users/cyber/projects/ElaWidgetTools-main/PySide6Example/`。

### 目录布局

```
PySide6Example/
├── main.py                 # 入口：QApplication + eApp.init() + MainWindow
├── mainwindow.py           # 主窗口：注册全部页面、停靠、菜单栏、状态栏
├── ExamplePage/
│   ├── T_BasePage.py       # 页面基类（继承 ElaScrollPage）
│   ├── T_Home.py           # 首页
│   ├── T_Icon.py           # 图标浏览
│   ├── T_ListView.py
│   ├── T_TableView.py
│   ├── T_TreeView.py
│   ├── T_Popup.py          # 对话框示例
│   ├── T_Setting.py
│   ├── T_Router.py
│   ├── ...                 # 其他 T_* 页面
│   └── __init__.py
├── ModelView/
│   ├── T_IconModel.py      # QAbstractListModel
│   ├── T_IconDelegate.py   # QStyledItemDelegate
│   ├── T_ListViewModel.py
│   ├── T_TableViewModel.py
│   ├── T_TreeViewModel.py
│   ├── T_TreeItem.py
│   ├── T_LogModel.py
│   └── __init__.py
└── Resource/               # 资源目录（文件系统相对路径，非 :/ Qt 资源）
    └── Image/
        ├── Cirno.jpg
        ├── Home_Background.png
        ├── WindowBase/
        │   ├── Miku.png / Miku.gif
        │   └── WorldTree.jpg / WorldTree.gif
        └── ...
```

### main.py 入口模式

```python
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # 切到脚本目录，相对路径才生效

from PySide6.QtWidgets import QApplication
from ElaWidgetTools import ElaApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
eApp = ElaApplication.getInstance()
eApp.init()
w = MainWindow()
w.show()
sys.exit(app.exec())
```

`os.chdir` 必要：示例用文件系统相对路径（`Resource/Image/...`）加载图片，不切目录会找不到。

### T_BasePage 基类模式

所有内容页继承 `T_BasePage`（继承 `ElaScrollPage`），构造里调 `createCustomWidget(desText)` 装顶部，再 `addCentralWidget(widget)` 装主区：

```python
class T_Popup(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaPopup")
        self.createCustomWidget("Popup and dialog components")  # 顶部

        centralWidget = QWidget(self)
        centerLayout = QVBoxLayout(centralWidget)
        # ... 装内容
        self.addCentralWidget(centralWidget, True, True, 0)    # 主区
```

### mainwindow.py 页面注册模式

主窗口在 `_initContent` 里实例化所有页面，再用 `addPageNode` / `addExpanderNode` / `addCategoryNode` / `addFooterNode` 注册到侧边导航。**所有返回 key 的方法都元组解包**：

```python
def _initContent(self):
    self._homePage = T_Home(self)
    self._listViewPage = T_ListView(self)
    # ...

    # 顶层
    self.addPageNode("HOME", self._homePage, ElaIconType.IconName.House)

    # 分类
    _, controlCategoryKey = self.addCategoryNode("Controls", "")

    # 展开节点 + 嵌套子页面
    _, viewKey = self.addExpanderNode("ElaView", "", ElaIconType.IconName.CameraViewfinder)
    _, viewCategoryKey = self.addCategoryNode("View Content", "", viewKey)
    self.addPageNode("ElaListView", self._listViewPage, viewKey, 9, ElaIconType.IconName.List)
    self.expandNavigationNode(viewKey)

    # Footer
    _, self._settingKey = self.addFooterNode(
        "Setting", self._settingPage, "", 0, ElaIconType.IconName.GearComplex
    )

    # 页面间跳转：通过 property("ElaPageKey") 拿 key
    self._homePage.elaBaseComponentNavigation.connect(
        lambda: self.navigation(self._baseComponentsPage.property("ElaPageKey"))
    )
```

### Resource 资源目录

Python 示例用**文件系统相对路径**，不是 Qt 的 `:/Resource/...` rcc 路径：

```python
# 正确（Python 示例）
QPixmap("Resource/Image/Cirno.jpg")
QImage("Resource/Image/Home_Background.png")
self.setWindowMoviePath(ElaThemeType.ThemeMode.Light, "Resource/Image/WindowBase/Miku.gif")

# 错误（C++ 风格，Python 下找不到）
QPixmap(":/Resource/Image/Cirno.jpg")
```

前提是 `main.py` 里 `os.chdir` 到脚本目录。若嵌入到自己的项目，把 `Resource/` 拷到工作目录或改用绝对路径。

## 枚举访问差异（C++ vs Python）

shiboken 把 C++ 嵌套枚举翻成 Python 类属性。规则：`Outer::Inner::Value` → `Outer.Inner.Value`。

| C++ | Python |
|---|---|
| `ElaIconType::IconName::House` | `ElaIconType.IconName.House` |
| `ElaMessageBarType::PositionPolicy::Top` | `ElaMessageBarType.PositionPolicy.Top` |
| `ElaThemeType::ThemeMode::Dark` | `ElaThemeType.ThemeMode.Dark` |
| `ElaThemeType::ThemeColor::PrimaryNormal` | `ElaThemeType.ThemeColor.PrimaryNormal` |
| `ElaAppBarType::CustomArea::MiddleArea` | `ElaAppBarType.CustomArea.MiddleArea` |
| `ElaNavigationType::NavigationType::Compact` | `ElaNavigationType.NavigationType.Compact` |
| `ElaNavigationRouterType::RouteMode::BackValid` | `ElaNavigationRouterType.RouteMode.BackValid` |

### 关键字冲突：枚举值名 None / Value 加下划线

C++ 枚举值名若与 Python 关键字/内置冲突，shiboken 自动加尾下划线：

| C++ | Python |
|---|---|
| `ElaStatCard::TrendType::None` | `ElaStatCard.TrendType.None_` |
| `ElaInfoBadge::BadgeMode::Value` | `ElaInfoBadge.BadgeMode.Value_` |

原因：`None` 是 Python 关键字，`Value` 在某些枚举容器里与内置冲突。出现 `pyside_type_init:_resolve_value UNRECOGNIZED: 'ElaIconType.None'` 警告是同类问题，不影响运行。

记忆口诀：**枚举值名是 Python 关键字/内置时，加尾下划线**。

## 常见笔误修正

### addPivot → appendPivot

`ElaPivot` 的 API 是 `appendPivot`，不是 `addPivot`。C++ 头文件 `ElaPivot.h` 第 20-21 行定义。

```python
# 正确
pivot.appendPivot("Tab1", widget, ElaIconType.IconName.House)

# 错误
pivot.addPivot("Tab1", widget, ...)   # AttributeError
```

### self.closeWindow → self.close

`ElaWindow` 继承自 `QWidget`，关闭方法是 `self.close()`，没有 `closeWindow`。

```python
# 正确
closeDialog.rightButtonClicked.connect(self.close)

# 错误
closeDialog.rightButtonClicked.connect(self.closeWindow)   # AttributeError
```

### :/Resource/Image/... → "Resource/Image/..."

Python 示例用文件系统相对路径，不用 Qt rcc 的 `:/` 前缀（见上"Resource 资源目录"）。

## 代码风格约定

- 所有示例用 Python，`import` 形如 `from ElaWidgetTools import ElaWindow, ElaIconType, ...`
- 枚举用完整形式：`ElaIconType.IconName.House`，不要简写
- 注释用中文
- 代码块用 ` ```python ` 标记
- 单例用 `getInstance()`：`ElaApplication.getInstance()` / `ElaTheme.getInstance()` / `ElaNavigationRouter.getInstance()`
- 返回 key 的方法**必须元组解包**：`_, key = self.addExpanderNode(...)`
- 主题切换用 `ElaThemeType.ThemeMode.Light/Dark`，无 `FollowSystem` 枚举
- 图片路径用文件系统相对路径，不用 `:/`

## 无害警告（可忽略）

| 警告 | 原因 | 处理 |
|---|---|---|
| `pyside_type_init:_resolve_value UNRECOGNIZED: 'ElaIconType.None'` | 枚举值名恰为 `None`，与 Python 关键字冲突 | 仅影响类型签名提示，不影响运行 |
| `This plugin does not support propagateSizeHints()` | offscreen 平台插件提示 | 测试环境才出现 |
| `missing font family "ElaAwesome"` | `.qrc` 内嵌字体未注册为系统字体 | 非致命，图标仍可显示 |

## 验证运行

```bash
# 正常运行（GUI）
QT_QPA_PLATFORM=offscreen /Users/cyber/miniconda3/envs/aidub/bin/python \
  /Users/cyber/projects/ElaWidgetTools-main/PySide6Example/main.py

# 冒烟测试：500ms 后自动退出
QT_QPA_PLATFORM=offscreen /Users/cyber/miniconda3/envs/aidub/bin/python -c "
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from ElaWidgetTools import ElaApplication
from mainwindow import MainWindow
app = QApplication(sys.argv)
ElaApplication.getInstance().init()
w = MainWindow()
w.show()
QTimer.singleShot(500, app.quit)
sys.exit(app.exec())
"
```

正常应无 traceback（GUI 模式会阻塞在 `app.exec()`，Ctrl-C 退出）。

## 排查清单

`import ElaWidgetTools` 失败 / 崩溃时按顺序检查：

1. **`.so` 是否装入 site-packages**：`python -c "import ElaWidgetTools; print(ElaWidgetTools.__file__)"`
2. **`.so` 文件名是否带前导点**：应是 `ElaWidgetTools.cpython-310-darwin.so`，不是 `ElaWidgetToolscpython-310-darwin.so`
3. **Qt 引用是否改写为 @rpath**：`otool -L <.so>` 应看到 `@rpath/QtWidgets.framework/...`
4. **macOS SDK 是否含 AGL**：`-DCMAKE_OSX_SYSROOT=.../MacOSX15.4.sdk`
5. **PySide6/shiboken6/Qt 版本是否一致**：三者必须 6.10.3
6. **是否重生了绑定源码**：改 typesystem/header 后 `rm -rf build-python/bindings/ElaWidgetTools`
7. **`fix_class_name.py` 是否跑过**：`ElaMessageBar`/`ElaSnackbar`/`ElaToast` 编译失败说明没跑
8. **`fix_out_params.py` 是否跑过**：`addExpanderNode` 返回非元组说明没跑
9. **`fix_install_names.py` 是否跑过**：启动即崩 + `otool` 显示绝对 Qt 路径说明没跑

## 注意事项

1. **`eApp.init()` 必须调用**——否则主题/Mica/暗色模式失效
2. **三个 shiboken 脚本必须跑**——`fix_class_name.py` / `fix_out_params.py` / `fix_install_names.py`，缺一即崩或功能缺失
3. **版本严格对齐**——PySide6 / shiboken6 / shiboken6_generator / Qt 全部 6.10.3
4. **macOS SDK 锁定 15.4**——新版 SDK 移除 AGL，Qt 链接失败
5. **`.so` 后缀带前导点**——`".${Python3_SOABI}.so"`
6. **`addExpanderNode`/`addFooterNode`/`addCategoryNode` 必须元组解包**——`_, key = ...`
7. **`ElaRouter` 不可用**——`addRoute`/`addRoutes`/`push`/`beforeEach` 受 `std::function` 限制
8. **`getNavigationSuggestDataList` 不可用**——手动构建 SuggestBox
9. **`QFlags.testFlag` 不可靠**——用 `bool(flag & Flag)` 按位与
10. **图片用文件系统相对路径**——`"Resource/Image/..."`，不用 `:/`
11. **枚举值名 None/Value 加下划线**——`None_` / `Value_`
12. **改 typesystem/header 后必须删 `build-python/bindings/ElaWidgetTools` 重生**——shiboken 不自动失效缓存
13. **Debug/MinSizeRel 构建被禁止**——只允许 Release / RelWithDebInfo（库 CMakeLists 主动 fatal）
14. **Python 侧无 `FollowSystem` 枚举**——跟随系统是 `setIsFollowSystemTheme(bool)` 独立开关
