from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaWindow,
    ElaAppBarType,
    ElaIconType,
    ElaNavigationType,
    ElaThemeType,
    ElaTheme,
    ElaContentDialog,
    ElaMenuBar,
    ElaMenu,
    ElaToolBar,
    ElaToolButton,
    ElaDockWidget,
    ElaStatusBar,
    ElaText,
    ElaProgressBar,
    ElaProgressRing,
    ElaSuggestBox,
    ElaCheckBox,
    ElaNavigationRouter,
)

from ExamplePage.T_Home import T_Home
from ExamplePage.T_BaseComponents import T_BaseComponents
from ExamplePage.T_Icon import T_Icon
from ExamplePage.T_Card import T_Card
from ExamplePage.T_Navigation import T_Navigation
from ExamplePage.T_Popup import T_Popup
from ExamplePage.T_ListView import T_ListView
from ExamplePage.T_TableView import T_TableView
from ExamplePage.T_TableWidget import T_TableWidget
from ExamplePage.T_TreeView import T_TreeView
from ExamplePage.T_Graphics import T_Graphics
from ExamplePage.T_CodeEditor import T_CodeEditor
from ExamplePage.T_NewComponents import T_NewComponents
from ExamplePage.T_NewComponents2 import T_NewComponents2
from ExamplePage.T_Router import T_Router
from ExamplePage.T_Setting import T_Setting
from ExamplePage.T_About import T_About
from ExamplePage.T_LogWidget import T_LogWidget
from ExamplePage.T_UpdateWidget import T_UpdateWidget


class MainWindow(ElaWindow):
    """主窗口。对应 C++ MainWindow。

    注册全部示例页面到导航栏，配置停靠窗口（日志/更新）、
    顶部 MenuBar + ToolBar、中央 SuggestBox + 路由按钮、底部 StatusBar。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._initWindow()
        self._initEdgeLayout()
        self._initContent()

        # 拦截默认关闭事件
        closeDialog = ElaContentDialog(self)
        closeDialog.rightButtonClicked.connect(self.close)
        closeDialog.middleButtonClicked.connect(
            lambda: (closeDialog.close(), self.showMinimized())
        )
        self.setIsDefaultClosed(False)
        self.closeButtonClicked.connect(lambda: closeDialog.exec())
        self.moveToCenter()

    # ==================== 窗口初始化 ====================
    def _initWindow(self):
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setWindowIcon(QIcon("Resource/Image/Cirno.jpg"))
        self.resize(1200, 740)
        self.setUserInfoCardPixmap(QPixmap("Resource/Image/Cirno.jpg"))
        self.setUserInfoCardTitle("ElaWidgetTools")
        self.setUserInfoCardSubTitle("PySide6 Example")
        self.setWindowTitle("ElaWidgetTools - PySide6")

        # 主堆栈占位页
        centralStack = ElaText("这是一个主窗口堆栈页面", self)
        centralStack.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        centralStack.setTextPixelSize(32)
        centralStack.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addCentralWidget(centralStack)

        # 窗口背景图（明/暗主题）
        self.setWindowPixmap(
            ElaThemeType.ThemeMode.Light, QPixmap("Resource/Image/WindowBase/Miku.png")
        )
        self.setWindowPixmap(
            ElaThemeType.ThemeMode.Dark,
            QPixmap("Resource/Image/WindowBase/WorldTree.jpg"),
        )
        self.setWindowMoviePath(
            ElaThemeType.ThemeMode.Light, "Resource/Image/WindowBase/Miku.gif"
        )
        self.setWindowMoviePath(
            ElaThemeType.ThemeMode.Dark, "Resource/Image/WindowBase/WorldTree.gif"
        )

        # 自定义 AppBar 菜单
        appBarMenu = ElaMenu(self)
        appBarMenu.setMenuItemHeight(27)
        act = appBarMenu.addAction("跳转到一级主要堆栈")
        act.triggered.connect(lambda: self.setCurrentStackIndex(0))
        act2 = appBarMenu.addAction("跳转到二级主要堆栈")
        act2.triggered.connect(lambda: self.setCurrentStackIndex(1))
        act3 = appBarMenu.addAction("更改页面切换特效(Scale)")
        act3.triggered.connect(lambda: self.setStackSwitchMode(1))  # Scale
        act4 = appBarMenu.addElaIconAction(
            ElaIconType.IconName.GearComplex, "自定义主窗口设置"
        )
        act4.triggered.connect(lambda: self.navigation(self._settingKey))
        appBarMenu.addSeparator()
        act5 = appBarMenu.addElaIconAction(ElaIconType.IconName.MoonStars, "更改项目主题")
        act5.triggered.connect(self._toggleTheme)
        self.setCustomMenu(appBarMenu)

        # 堆栈独立自定义窗口：路由按钮 + SuggestBox + 进度环
        centralCustomWidget = QWidget(self)
        centralCustomWidgetLayout = QHBoxLayout(centralCustomWidget)
        centralCustomWidgetLayout.setContentsMargins(13, 15, 9, 6)

        self._leftButton = ElaToolButton(self)
        self._leftButton.setElaIcon(ElaIconType.IconName.AngleLeft)
        self._leftButton.setEnabled(False)
        self._leftButton.clicked.connect(
            lambda: ElaNavigationRouter.getInstance().navigationRouteBack()
        )

        self._rightButton = ElaToolButton(self)
        self._rightButton.setElaIcon(ElaIconType.IconName.AngleRight)
        self._rightButton.setEnabled(False)
        self._rightButton.clicked.connect(
            lambda: ElaNavigationRouter.getInstance().navigationRouteForward()
        )

        # 路由状态信号
        router = ElaNavigationRouter.getInstance()
        router.navigationRouterStateChanged.connect(self._onRouteStateChanged)

        self._windowSuggestBox = ElaSuggestBox(self)
        self._windowSuggestBox.setFixedHeight(32)
        self._windowSuggestBox.setPlaceholderText("搜索关键字")
        self._windowSuggestBox.suggestionClicked.connect(self._onSuggestionClicked)

        progressBusyRingText = ElaText("系统运行中", self)
        progressBusyRingText.setIsWrapAnywhere(False)
        progressBusyRingText.setTextPixelSize(15)

        progressBusyRing = ElaProgressRing(self)
        progressBusyRing.setBusyingWidth(4)
        progressBusyRing.setFixedSize(28, 28)
        progressBusyRing.setIsBusying(True)

        centralCustomWidgetLayout.addWidget(self._leftButton)
        centralCustomWidgetLayout.addWidget(self._rightButton)
        centralCustomWidgetLayout.addWidget(self._windowSuggestBox)
        centralCustomWidgetLayout.addStretch()
        centralCustomWidgetLayout.addWidget(progressBusyRingText)
        centralCustomWidgetLayout.addWidget(progressBusyRing)
        self.setCentralCustomWidget(centralCustomWidget)

    def _toggleTheme(self):
        eTheme = ElaTheme.getInstance()
        eTheme.setThemeMode(
            ElaThemeType.ThemeMode.Dark
            if eTheme.getThemeMode() == ElaThemeType.ThemeMode.Light
            else ElaThemeType.ThemeMode.Light
        )

    def _onRouteStateChanged(self, routeMode):
        # routeMode: ElaNavigationRouterType.RouteMode 枚举
        # BackValid=0, BackInvalid=1, ForwardValid=2, ForwardInvalid=3
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

    def _onSuggestionClicked(self, suggestData):
        # suggestData: ElaSuggestBox.SuggestData
        try:
            data = suggestData.getSuggestData()
            if "ElaPageKey" in data:
                self.navigation(data["ElaPageKey"])
        except Exception:
            pass

    # ==================== 边缘布局 ====================
    def _initEdgeLayout(self):
        # 菜单栏
        menuBar = ElaMenuBar(self)
        menuBar.setFixedHeight(30)
        menuBarWidget = QWidget(self)
        menuBarWidget.setFixedWidth(500)
        menuBarLayout = QVBoxLayout(menuBarWidget)
        menuBarLayout.setContentsMargins(0, 0, 0, 0)
        menuBarLayout.addWidget(menuBar)
        menuBarLayout.addStretch()
        self.setCustomWidget(ElaAppBarType.CustomArea.MiddleArea, menuBarWidget)
        self._menuBarWrapper = menuBarWidget

        menuBar.addElaIconAction(ElaIconType.IconName.AtomSimple, "动作菜单")
        iconMenu = menuBar.addMenu(ElaIconType.IconName.Aperture, "图标菜单")
        iconMenu.setMenuItemHeight(27)
        iconMenu.addElaIconAction(ElaIconType.IconName.BoxCheck, "排序方式")
        iconMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        iconMenu.addElaIconAction(ElaIconType.IconName.MagnifyingGlassPlus, "显示设置")
        iconMenu.addSeparator()
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addSeparator()
        shortCutMenu = ElaMenu("快捷菜单(&A)", self)
        shortCutMenu.setMenuItemHeight(27)
        shortCutMenu.addElaIconAction(ElaIconType.IconName.BoxCheck, "排序方式")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.MagnifyingGlassPlus, "显示设置")
        shortCutMenu.addSeparator()
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addMenu(shortCutMenu)
        for label in ["样例菜单(&B)", "样例菜单(&C)", "样例菜单(&E)", "样例菜单(&F)", "样例菜单(&G)"]:
            m = menuBar.addMenu(label)
            m.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "样例选项")

        # 工具栏
        toolBar = ElaToolBar("工具栏", self)
        toolBar.setAllowedAreas(
            Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea
        )
        toolBar.setToolBarSpacing(3)
        toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        toolBar.setIconSize(QSize(25, 25))

        for icon in [
            ElaIconType.IconName.BadgeCheck,
            ElaIconType.IconName.ChartUser,
        ]:
            btn = ElaToolButton(self)
            btn.setElaIcon(icon)
            toolBar.addWidget(btn)
        toolBar.addSeparator()
        bluetoothBtn = ElaToolButton(self)
        bluetoothBtn.setElaIcon(ElaIconType.IconName.Bluetooth)
        bluetoothBtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        bluetoothBtn.setText("Bluetooth")
        toolBar.addWidget(bluetoothBtn)
        for icon in [
            ElaIconType.IconName.BringFront,
        ]:
            btn = ElaToolButton(self)
            btn.setElaIcon(icon)
            toolBar.addWidget(btn)
        toolBar.addSeparator()
        for icon in [
            ElaIconType.IconName.ChartSimple,
            ElaIconType.IconName.FaceClouds,
            ElaIconType.IconName.Aperture,
            ElaIconType.IconName.ChartMixed,
            ElaIconType.IconName.Coins,
        ]:
            btn = ElaToolButton(self)
            btn.setElaIcon(icon)
            toolBar.addWidget(btn)
        alarmBtn = ElaToolButton(self)
        alarmBtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        alarmBtn.setElaIcon(ElaIconType.IconName.AlarmPlus)
        alarmBtn.setText("AlarmPlus")
        toolBar.addWidget(alarmBtn)
        crownBtn = ElaToolButton(self)
        crownBtn.setElaIcon(ElaIconType.IconName.Crown)
        toolBar.addWidget(crownBtn)

        toolBar.addSeparator()

        progressBar = ElaProgressBar(self)
        progressBar.setMinimum(0)
        progressBar.setMaximum(0)
        progressBar.setFixedWidth(350)
        toolBar.addWidget(progressBar)

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolBar)

        # 停靠窗口：日志 + 更新
        logDockWidget = ElaDockWidget("日志信息", self)
        logDockWidget.setWidget(T_LogWidget(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, logDockWidget)
        self.resizeDocks([logDockWidget], [200], Qt.Orientation.Horizontal)

        updateDockWidget = ElaDockWidget("更新内容", self)
        updateDockWidget.setWidget(T_UpdateWidget(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, updateDockWidget)
        self.resizeDocks([updateDockWidget], [200], Qt.Orientation.Horizontal)

        # 状态栏
        statusBar = ElaStatusBar(self)
        statusText = ElaText("初始化成功！", self)
        statusText.setTextPixelSize(14)
        statusBar.addWidget(statusText)
        self.setStatusBar(statusBar)

    # ==================== 中心内容 ====================
    def _initContent(self):
        # 实例化全部页面
        self._homePage = T_Home(self)
        self._iconPage = T_Icon(self)
        self._baseComponentsPage = T_BaseComponents(self)
        self._graphicsPage = T_Graphics(self)
        self._navigationPage = T_Navigation(self)
        self._popupPage = T_Popup(self)
        self._cardPage = T_Card(self)
        self._listViewPage = T_ListView(self)
        self._tableViewPage = T_TableView(self)
        self._tableWidgetPage = T_TableWidget(self)
        self._treeViewPage = T_TreeView(self)
        self._newComponentsPage = T_NewComponents(self)
        self._newComponents2Page = T_NewComponents2(self)
        self._codeEditorPage = T_CodeEditor(self)
        self._routerPage = T_Router(self)
        self._settingPage = T_Setting(self)

        # ---- 注册导航节点 ----
        # HOME
        self.addPageNode("HOME", self._homePage, ElaIconType.IconName.House)

        # Controls 分类
        _, controlCategoryKey = self.addCategoryNode("Controls", "")
        self.addPageNode(
            "ElaBaseComponents",
            self._baseComponentsPage,
            ElaIconType.IconName.CabinetFiling,
        )

        # ElaView 展开节点 + 子页面
        _, viewKey = self.addExpanderNode(
            "ElaView", "", ElaIconType.IconName.CameraViewfinder
        )
        _, viewCategoryKey = self.addCategoryNode("View Content", "", viewKey)
        self.addPageNode(
            "ElaListView",
            self._listViewPage,
            viewKey,
            9,
            ElaIconType.IconName.List,
        )
        self.addPageNode(
            "ElaTableView",
            self._tableViewPage,
            viewKey,
            ElaIconType.IconName.Table,
        )
        self.addPageNode(
            "ElaTableWidget",
            self._tableWidgetPage,
            viewKey,
            ElaIconType.IconName.TableCells,
        )
        self.addPageNode(
            "ElaTreeView",
            self._treeViewPage,
            viewKey,
            ElaIconType.IconName.ListTree,
        )
        self.expandNavigationNode(viewKey)

        # 独立页面
        self.addPageNode(
            "ElaGraphics", self._graphicsPage, 9, ElaIconType.IconName.Paintbrush
        )
        self.addPageNode("ElaCard", self._cardPage, ElaIconType.IconName.Cards)

        # Custom 分类
        _, customKey = self.addCategoryNode("Custom", "")
        self.addPageNode(
            "ElaNavigation",
            self._navigationPage,
            ElaIconType.IconName.LocationArrow,
        )
        self.addPageNode("ElaPopup", self._popupPage, ElaIconType.IconName.Envelope)
        self.addPageNode(
            "ElaNewComponents",
            self._newComponentsPage,
            ElaIconType.IconName.Sparkles,
        )
        self.addPageNode(
            "ElaNewComponents2",
            self._newComponents2Page,
            ElaIconType.IconName.StarChristmas,
        )
        self.addPageNode(
            "ElaCodeEditor", self._codeEditorPage, ElaIconType.IconName.Code
        )
        self.addPageNode("ElaRouter", self._routerPage, ElaIconType.IconName.SignsPost)
        self.addPageNode(
            "ElaIcon", self._iconPage, 99, ElaIconType.IconName.FontCase
        )

        # 测试用展开节点（演示嵌套）
        _, testKey1 = self.addExpanderNode(
            "TEST_EXPAND_NODE1", "", ElaIconType.IconName.Acorn
        )
        _, testKey2 = self.addExpanderNode(
            "TEST_EXPAND_NODE2", "", testKey1, ElaIconType.IconName.Acorn
        )
        self.addPageNode("TEST_NODE3", QWidget(self), testKey2, ElaIconType.IconName.Acorn)
        for i in range(10):
            self.addExpanderNode(
                f"TEST_EXPAND_NODE{i + 4}",
                "",
                testKey2,
                ElaIconType.IconName.Acorn,
            )

        # ---- Footer 节点 ----
        _, aboutKey = self.addFooterNode(
            "About", None, "", 0, ElaIconType.IconName.User
        )
        self._aboutPage = T_About()
        self._aboutPage.hide()

        def onNavClicked(nodeType, nodeKey):
            if aboutKey == nodeKey:
                self._aboutPage.setFixedSize(400, 400)
                self._aboutPage.show()

        self.navigationNodeClicked.connect(onNavClicked)

        _, self._settingKey = self.addFooterNode(
            "Setting", self._settingPage, "", 0, ElaIconType.IconName.GearComplex
        )

        # 用户卡片点击 → 跳转 Home
        self.userInfoCardClicked.connect(
            lambda: self.navigation(self._homePage.property("ElaPageKey"))
        )

        # ---- Home 页面导航信号连接 ----
        self._homePage.elaBaseComponentNavigation.connect(
            lambda: self.navigation(self._baseComponentsPage.property("ElaPageKey"))
        )
        self._homePage.elaSceneNavigation.connect(
            lambda: self.navigation(self._graphicsPage.property("ElaPageKey"))
        )
        self._homePage.elaIconNavigation.connect(
            lambda: self.navigation(self._iconPage.property("ElaPageKey"))
        )
        self._homePage.elaCardNavigation.connect(
            lambda: self.navigation(self._cardPage.property("ElaPageKey"))
        )

        # ---- 填充 SuggestBox ----
        self._populateSuggestBox()

    def _populateSuggestBox(self):
        """手动构建建议列表（C++ 的 getNavigationSuggestDataList 未绑定到 Python）。"""
        suggestions = [
            (ElaIconType.IconName.House, "HOME"),
            (ElaIconType.IconName.CabinetFiling, "ElaBaseComponents"),
            (ElaIconType.IconName.List, "ElaListView"),
            (ElaIconType.IconName.Table, "ElaTableView"),
            (ElaIconType.IconName.TableCells, "ElaTableWidget"),
            (ElaIconType.IconName.ListTree, "ElaTreeView"),
            (ElaIconType.IconName.Paintbrush, "ElaGraphics"),
            (ElaIconType.IconName.Cards, "ElaCard"),
            (ElaIconType.IconName.LocationArrow, "ElaNavigation"),
            (ElaIconType.IconName.Envelope, "ElaPopup"),
            (ElaIconType.IconName.Sparkles, "ElaNewComponents"),
            (ElaIconType.IconName.StarChristmas, "ElaNewComponents2"),
            (ElaIconType.IconName.Code, "ElaCodeEditor"),
            (ElaIconType.IconName.SignsPost, "ElaRouter"),
            (ElaIconType.IconName.FontCase, "ElaIcon"),
            (ElaIconType.IconName.GearComplex, "Setting"),
        ]
        # 页面 → key 映射
        pageKeyMap = {
            "HOME": self._homePage.property("ElaPageKey"),
            "ElaBaseComponents": self._baseComponentsPage.property("ElaPageKey"),
            "ElaListView": self._listViewPage.property("ElaPageKey"),
            "ElaTableView": self._tableViewPage.property("ElaPageKey"),
            "ElaTableWidget": self._tableWidgetPage.property("ElaPageKey"),
            "ElaTreeView": self._treeViewPage.property("ElaPageKey"),
            "ElaGraphics": self._graphicsPage.property("ElaPageKey"),
            "ElaCard": self._cardPage.property("ElaPageKey"),
            "ElaNavigation": self._navigationPage.property("ElaPageKey"),
            "ElaPopup": self._popupPage.property("ElaPageKey"),
            "ElaNewComponents": self._newComponentsPage.property("ElaPageKey"),
            "ElaNewComponents2": self._newComponents2Page.property("ElaPageKey"),
            "ElaCodeEditor": self._codeEditorPage.property("ElaPageKey"),
            "ElaRouter": self._routerPage.property("ElaPageKey"),
            "ElaIcon": self._iconPage.property("ElaPageKey"),
            "Setting": self._settingKey,
        }
        for icon, title in suggestions:
            key = pageKeyMap.get(title, "")
            try:
                self._windowSuggestBox.addSuggestion(
                    icon, title, {"ElaPageKey": key}
                )
            except Exception:
                pass
