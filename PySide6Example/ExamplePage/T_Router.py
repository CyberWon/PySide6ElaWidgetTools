from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaRouter,
    ElaPushButton,
    ElaScrollPageArea,
    ElaPlainTextEdit,
    ElaText,
    ElaLineEdit,
)

from ExamplePage.T_BasePage import T_BasePage


class T_Router(T_BasePage):
    """ElaRouter 路由演示页（Python 简化版）。对应 C++ T_Router。

    说明：
    ElaRouter 的 addRoute/addRoutes/addDynamicRoute/push/beforeEach 等核心 API
    依赖 ``std::function<QWidget*()>`` 与 ``ElaRouteConfig``（含 std::function 字段），
    shiboken 无法在无显式类型系统支持时绑定到 Python 可调用对象，故这些方法
    在 Python 侧不可用。

    本页演示 Python 侧可用的功能：
      - routeChanged / navigationBlocked 信号监听
      - back / forward 导航
      - getRoutePaths / hasRoute / getRouteMeta / getCurrentPath 路由表查询
      - bindWindow / installRoutes（配合 C++ 侧已注册的路由）
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaRouter")
        self.createCustomWidget(
            "ElaRouter 声明式路由演示 - Python 侧仅支持查询/导航/信号监听"
        )

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaRouter")
        c = QVBoxLayout(centralWidget)
        c.setContentsMargins(0, 0, 0, 0)

        # ========== 路由表查询 ==========
        queryArea = ElaScrollPageArea(self)
        queryArea.setMinimumHeight(100)
        queryLayout = QVBoxLayout(queryArea)
        queryLayout.addWidget(ElaText("路由表查询 (getRoutePaths / hasRoute / getRouteMeta)", 15, self))

        self._queryEdit = ElaLineEdit(self)
        self._queryEdit.setPlaceholderText("输入路由路径 (如: /router-demo/page-a)")
        self._queryEdit.setFixedSize(300, 35)

        queryBtn = ElaPushButton("查询", self)
        queryBtn.setFixedSize(80, 32)

        refreshBtn = ElaPushButton("刷新列表", self)
        refreshBtn.setFixedSize(90, 32)

        self._queryStatus = ElaText("", self)
        self._queryStatus.setTextPixelSize(13)
        self._queryStatus.setMinimumWidth(300)

        queryBtn.clicked.connect(self._onQuery)
        refreshBtn.clicked.connect(self._onRefreshPaths)

        queryBtnLayout = QHBoxLayout()
        queryBtnLayout.addWidget(self._queryEdit)
        queryBtnLayout.addWidget(queryBtn)
        queryBtnLayout.addWidget(refreshBtn)
        queryBtnLayout.addWidget(self._queryStatus)
        queryBtnLayout.addStretch()
        queryLayout.addLayout(queryBtnLayout)

        # ========== 导航控制 ==========
        navArea = ElaScrollPageArea(self)
        navArea.setMinimumHeight(100)
        navLayout = QVBoxLayout(navArea)
        navLayout.addWidget(ElaText("导航控制 (back / forward)", 15, self))

        backBtn = ElaPushButton("back", self)
        backBtn.setFixedSize(80, 32)
        forwardBtn = ElaPushButton("forward", self)
        forwardBtn.setFixedSize(80, 32)

        backBtn.clicked.connect(lambda: (self._router().back(), self._appendLog("back()")))
        forwardBtn.clicked.connect(
            lambda: (self._router().forward(), self._appendLog("forward()"))
        )

        navBtnLayout = QHBoxLayout()
        navBtnLayout.addWidget(backBtn)
        navBtnLayout.addWidget(forwardBtn)
        navBtnLayout.addStretch()
        navLayout.addLayout(navBtnLayout)

        # ========== 绑定/安装说明 ==========
        bindArea = ElaScrollPageArea(self)
        bindArea.setMinimumHeight(100)
        bindLayout = QVBoxLayout(bindArea)
        bindLayout.addWidget(ElaText("绑定窗口 (bindWindow / installRoutes)", 15, self))

        bindBtn = ElaPushButton("bindWindow", self)
        bindBtn.setFixedSize(110, 32)
        installBtn = ElaPushButton("installRoutes", self)
        installBtn.setFixedSize(120, 32)

        self._bindStatus = ElaText("", self)
        self._bindStatus.setTextPixelSize(13)
        self._bindStatus.setMinimumWidth(300)

        bindBtn.clicked.connect(self._onBindWindow)
        installBtn.clicked.connect(self._onInstallRoutes)

        bindBtnLayout = QHBoxLayout()
        bindBtnLayout.addWidget(bindBtn)
        bindBtnLayout.addWidget(installBtn)
        bindBtnLayout.addWidget(self._bindStatus)
        bindBtnLayout.addStretch()
        bindLayout.addLayout(bindBtnLayout)

        # ========== 限制说明 ==========
        limitArea = ElaScrollPageArea(self)
        limitArea.setMinimumHeight(100)
        limitLayout = QVBoxLayout(limitArea)
        limitLayout.addWidget(ElaText("Python 绑定限制说明", 15, self))
        limitText = ElaText(
            "addRoute / addRoutes / addDynamicRoute / push / replace / beforeEach / afterEach\n"
            "依赖 std::function<QWidget*()> 与 ElaRouteConfig（含 std::function 字段），\n"
            "shiboken 在无显式类型系统支持时无法绑定到 Python 可调用对象。\n"
            "如需完整路由功能，请在 C++ 侧注册路由后于 Python 侧调用 installRoutes/back/forward。",
            self,
        )
        limitText.setTextPixelSize(13)
        limitLayout.addWidget(limitText)

        # ========== 路由日志 ==========
        logArea = ElaScrollPageArea(self)
        logArea.setFixedHeight(200)
        logLayout = QVBoxLayout(logArea)

        logHeader = QHBoxLayout()
        logHeader.addWidget(ElaText("路由日志", 15, self))

        self._currentPathText = ElaText("当前路由: (无)", self)
        self._currentPathText.setTextPixelSize(13)
        self._currentPathText.setMinimumWidth(400)
        logHeader.addSpacing(20)
        logHeader.addWidget(self._currentPathText)
        logHeader.addStretch()

        clearLogBtn = ElaPushButton("清除", self)
        clearLogBtn.setFixedSize(60, 28)
        clearLogBtn.clicked.connect(lambda: self._logEdit.clear())
        logHeader.addWidget(clearLogBtn)

        logLayout.addLayout(logHeader)

        self._logEdit = ElaPlainTextEdit(self)
        self._logEdit.setReadOnly(True)
        logLayout.addWidget(self._logEdit)

        # 连接路由信号
        router = self._router()
        router.routeChanged.connect(self._onRouteChanged)
        router.navigationBlocked.connect(
            lambda path: self._appendLog("BLOCKED: " + path)
        )

        # ========== 中心布局 ==========
        c.addWidget(queryArea)
        c.addWidget(navArea)
        c.addWidget(bindArea)
        c.addWidget(limitArea)
        c.addWidget(logArea)
        c.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)

        self._onRefreshPaths()

    @staticmethod
    def _router():
        return ElaRouter.getInstance()

    def _appendLog(self, text):
        if self._logEdit:
            self._logEdit.appendPlainText("> " + text)

    def _onRouteChanged(self, path, params):
        paramStr = ""
        if params and len(params) > 0:
            parts = [f"{k}={params[k]}" for k in params]
            paramStr = " {" + ", ".join(parts) + "}"
        self._currentPathText.setText("当前路由: " + path + paramStr)
        self._appendLog("routeChanged: " + path + paramStr)

    def _onQuery(self):
        path = self._queryEdit.text().strip()
        if not path:
            self._queryStatus.setText("请输入路由路径")
            return
        router = self._router()
        if router.hasRoute(path):
            meta = router.getRouteMeta(path)
            metaStr = ", ".join(f"{k}={meta[k]}" for k in meta) if meta else "(无)"
            self._queryStatus.setText(f"存在; meta: {metaStr}")
            self._appendLog(f"hasRoute({path}) = True; meta={metaStr}")
        else:
            self._queryStatus.setText("路由不存在")
            self._appendLog(f"hasRoute({path}) = False")

    def _onRefreshPaths(self):
        router = self._router()
        paths = router.getRoutePaths()
        self._queryStatus.setText(f"路由表共 {len(paths)} 条")
        self._appendLog(f"getRoutePaths: {len(paths)} 条路由")
        for p in paths:
            self._appendLog("  " + p)

    def _onBindWindow(self):
        router = self._router()
        win = self.window()
        if win is None:
            self._bindStatus.setText("未找到父窗口")
            return
        try:
            router.bindWindow(win)
            self._bindStatus.setText("已绑定到当前窗口")
            self._appendLog("bindWindow: 已绑定")
        except Exception as e:
            self._bindStatus.setText(f"绑定失败: {e}")
            self._appendLog(f"bindWindow 失败: {e}")

    def _onInstallRoutes(self):
        router = self._router()
        if router.getBoundWindow() is None:
            self._bindStatus.setText("请先 bindWindow")
            return
        try:
            router.installRoutes()
            self._bindStatus.setText("已调用 installRoutes")
            self._appendLog("installRoutes: 已调用")
        except Exception as e:
            self._bindStatus.setText(f"安装失败: {e}")
            self._appendLog(f"installRoutes 失败: {e}")
