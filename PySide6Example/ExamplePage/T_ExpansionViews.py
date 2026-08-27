from PySide6.QtCore import QDate, QSize, QPointF
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QWidget

from ElaWidgetTools import (
    ElaAppBar,
    ElaCalendar,
    ElaGraphicsItem,
    ElaGraphicsLineItem,
    ElaGraphicsScene,
    ElaGraphicsView,
    ElaInteractiveCard,
    ElaNavigationType,
    ElaIconType,
    ElaMenu,
    ElaMarkdownViewer,
    ElaNavigationBar,
    ElaPersonPicture,
    ElaReminderCard,
    ElaRibbonBar,
    ElaRibbonGroup,
    ElaRibbonTabBar,
    ElaScreenCaptureManager,
    ElaScrollPageArea,
    ElaPushButton,
    ElaSheetPanelType,
    ElaSelectorBar,
    ElaSheetPanel,
    ElaSplashScreen,
    ElaSplitButton,
    ElaSpotlight,
    ElaTabBar,
    ElaText,
    ElaTransfer,
    ElaVirtualList,
    ElaWatermark,
)
from ExamplePage.T_BasePage import T_BasePage


class T_ExpansionViews(T_BasePage):
    """高级视图、卡片与容器组件示例。"""

    def _makeSection(self, title: str, noteText: str, parent: QWidget):
        area = ElaScrollPageArea(parent)
        areaLayout = QVBoxLayout(area)
        header = QHBoxLayout()
        header.addWidget(ElaText(title, 15, parent))
        header.addStretch()
        areaLayout.addLayout(header)
        note = ElaText(noteText, 12, parent)
        note.setWordWrap(True)
        areaLayout.addWidget(note)
        return area, areaLayout

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaExpansionViews")
        self.createCustomWidget("Advanced view and container examples")

        centralWidget = QWidget(self)
        centralLayout = QVBoxLayout(centralWidget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(10)

        # ElaCalendar：显示完整月历，并用最小/最大日期约束选择范围。
        calendarArea, calendarLayout = self._makeSection(
            "ElaCalendar",
            "用法：setSelectedDate 提供当前值。实现：Minimum/MaximumDate 会裁剪可选日期。",
            self,
        )
        calendar = ElaCalendar(self)
        calendar.setSelectedDate(QDate.currentDate())
        calendar.setFixedHeight(280)
        calendarLayout.addWidget(calendar)
        centralLayout.addWidget(calendarArea)

        # ElaMarkdownViewer：多行 Markdown 字符串直接交给控件解析。
        markdownViewer = ElaMarkdownViewer(self)
        markdownViewer.setMarkdown(
            "# Python 绑定示例\n\n"
            "- 支持标题、列表和引用\n"
            "- 文本改动后立即重绘\n\n"
            "> 内容保存在 Markdown 属性中。\n"
        )
        markdownViewer.setFixedHeight(240)
        markdownArea, markdownLayout = self._makeSection(
            "ElaMarkdownViewer",
            "用法：setMarkdown 接收完整文本。实现：内部解析块级元素并使用主题颜色渲染。",
            self,
        )
        markdownLayout.addWidget(markdownViewer)
        centralLayout.addWidget(markdownArea)

        # ElaPersonPicture：没有图片时绘制显示名首字母。
        personPicture = ElaPersonPicture(self)
        personPicture.setDisplayName("Cyber Won")
        personPicture.setPictureSize(72)
        cardPixmap = QPixmap(320, 180)
        cardPixmap.fill(QColor("#1F6FEB"))

        interactiveCard = ElaInteractiveCard(self)
        interactiveCard.setTitle("Fluent 组件")
        interactiveCard.setSubTitle("Hover 时透明度变化")
        interactiveCard.setCardPixmap(cardPixmap)
        interactiveCard.setCardPixmapSize(220, 120)

        reminderCard = ElaReminderCard(self)
        reminderCard.setTitle("今日提醒")
        reminderCard.setSubTitle("检查新组件覆盖率")
        reminderCard.setCardPixmap(cardPixmap)
        reminderCard.setCardPixmapSize(180, 100)
        cardArea, cardLayout = self._makeSection(
            "ElaPersonPicture / Cards",
            "用法：QPixmap 或 QImage 作为卡片图。实现：CardPixMode 决定图片裁剪方式。",
            self,
        )
        cardBody = QHBoxLayout()
        cardBody.addWidget(personPicture)
        cardBody.addWidget(interactiveCard)
        cardBody.addWidget(reminderCard)
        cardBody.addStretch()
        cardLayout.addLayout(cardBody)
        centralLayout.addWidget(cardArea)

        # ElaSelectorBar / ElaSplitButton / ElaTabBar：导航控件和主副操作拆分。
        selectorBar = ElaSelectorBar(self)
        selectorBar.addItem("全部")
        selectorBar.addItem("已读")
        selectorBar.addItem("归档")
        selectorBar.setCurrentIndex(1)

        splitButton = ElaSplitButton(self)
        splitButton.setText("下载")
        splitButton.setElaIcon(ElaIconType.IconName.Download)
        downloadMenu = ElaMenu(self)
        downloadMenu.addAction("普通质量")
        downloadMenu.addAction("高清质量")
        splitButton.setMenu(downloadMenu)

        tabBar = ElaTabBar(self)
        tabBar.addTab("Overview")
        tabBar.addTab("Performance")
        tabBar.addTab("Settings")
        tabBar.setTabSize(QSize(110, 38))
        navigationArea, navigationLayout = self._makeSection(
            "ElaSelectorBar / ElaSplitButton / ElaTabBar",
            "用法：SelectorBar 用 addItem 添加文本页签；SplitButton 主区域触发 clicked，箭头区弹菜单。"
            "ElaTabBar 继承 QTabBar，支持拖拽排序。",
            self,
        )
        rowOne = QHBoxLayout()
        rowOne.addWidget(selectorBar)
        rowOne.addWidget(splitButton)
        rowOne.addStretch()
        rowTwo = QHBoxLayout()
        rowTwo.addWidget(tabBar)
        rowTwo.addStretch()
        navigationLayout.addLayout(rowOne)
        navigationLayout.addLayout(rowTwo)
        centralLayout.addWidget(navigationArea)

        # ElaNavigationBar：独立导航栏也能添加分类、展开节点和页面。
        navigationBar = ElaNavigationBar(self)
        navigationBar.setDisplayMode(ElaNavigationType.NavigationDisplayMode.Compact)
        firstViewPage = QWidget(self)
        secondViewPage = QWidget(self)
        expandKey = "workspace"
        navigationBar.addExpanderNode(
            "Workspace", "workspace", ElaIconType.IconName.Folder
        )
        navigationBar.addPageNode("Files", firstViewPage, expandKey)
        navigationBar.addPageNode("History", secondViewPage, expandKey)
        navigationBar.expandNode(expandKey)
        navContainer, navLayout = self._makeSection(
            "ElaNavigationBar",
            "用法：NodeResult 返回 key，可继续挂在 category 或 expander 下。"
            "实现：这个示例是独立导航栏；主窗口里的 ElaWindow 使用同一套节点模型。",
            self,
        )
        navLayout.addWidget(navigationBar)
        centralLayout.addWidget(navContainer)

        # ElaRibbonTabBar / ElaRibbonBar / ElaRibbonGroup：Ribbon 的三层结构。
        ribbonTabBar = ElaRibbonTabBar(self)
        ribbonTabBar.appendTab("Home")
        ribbonTabBar.appendTab("Review")
        ribbonBar = ElaRibbonBar(self)
        homePage = ribbonBar.addTab("Home")
        reviewPage = ribbonBar.addTab("Review")
        homeGroup = ribbonBar.addGroup(homePage, "Document")
        homeGroup.addToolButton(
            ElaIconType.IconName.FloppyDisk, "保存", ElaRibbonGroup.ButtonSize.Large
        )
        homeGroup.addWidget(ElaText("可在 Ribbon 中嵌控件", self))
        reviewGroup = ribbonBar.addGroup(reviewPage, "Comments")
        reviewGroup.addToolButton(
            ElaIconType.IconName.Comment, "评论", ElaRibbonGroup.ButtonSize.Small
        )
        ribbonBar.bindTabBar(ribbonTabBar)
        ribbonArea, ribbonLayout = self._makeSection(
            "ElaRibbonBar",
            "用法：addTab 返回页面容器，addGroup 在其中创建分组，bindTabBar 关联外部页签。"
            "实现：RibbonBar 处理折叠/固定动画，RibbonGroup 管理大小按钮布局。",
            self,
        )
        ribbonBody = QVBoxLayout()
        ribbonBody.addWidget(ribbonTabBar)
        ribbonBody.addWidget(ribbonBar)
        ribbonLayout.addLayout(ribbonBody)
        centralLayout.addWidget(ribbonArea)

        # ElaSheetPanel：带遮罩的抽屉面板，Full/Half/Peek 三档停靠。
        sheetPanel = ElaSheetPanel(self)
        sheetContent = QWidget(self)
        sheetContentLayout = QVBoxLayout(sheetContent)
        sheetContentLayout.addWidget(ElaText("从右侧滑出的面板", 16, self))
        sheetContentLayout.addWidget(ElaText("支持拖拽手柄和遮罩点击关闭。", 12, self))
        sheetPanel.setCentralWidget(sheetContent)
        sheetPanel.setDirection(ElaSheetPanelType.Direction.Right)
        sheetPanel.setDragHandleVisible(True)
        sheetPanel.setCloseOnOverlayClick(True)
        sheetOpenButton = ElaPushButton("打开 Sheet", self)
        sheetCloseButton = ElaPushButton("关闭 Sheet", self)
        sheetOpenButton.clicked.connect(
            lambda: sheetPanel.open(ElaSheetPanelType.DetentLevel.Half)
        )
        sheetCloseButton.clicked.connect(sheetPanel.close)
        sheetArea, sheetLayout = self._makeSection(
            "ElaSheetPanel",
            "用法：setCentralWidget 后按 DetentLevel 打开。实现：Ratio 控制三个档位占父容器的比例。",
            self,
        )
        sheetRow = QHBoxLayout()
        sheetRow.addWidget(sheetOpenButton)
        sheetRow.addWidget(sheetCloseButton)
        sheetRow.addStretch()
        sheetLayout.addLayout(sheetRow)
        centralLayout.addWidget(sheetArea)

        # ElaSplashScreen / ElaSpotlight：启动过程与分步引导。
        splash = ElaSplashScreen(self)
        splashLogo = QPixmap(96, 96)
        splashLogo.fill(QColor("#0078D4"))
        splash.setLogo(splashLogo)
        splash.setTitle("ElaWidgetTools")
        splash.setSubTitle("PySide6 Example")
        splash.setStatusText("正在准备组件...")
        splash.setMinimum(0)
        splash.setMaximum(100)
        splash.setValue(60)
        spotlightTarget = ElaPushButton("引导目标", self)
        spotlight = ElaSpotlight(self)
        spotlight.setTitle("快速开始")
        spotlight.setContent("这里是第一步，点击继续查看下一步。")
        spotlightTarget.clicked.connect(
            lambda: spotlight.showSpotlight(spotlightTarget, "知道了")
        )
        launchArea, launchLayout = self._makeSection(
            "ElaSplashScreen / ElaSpotlight",
            "用法：Splash 由进度和文案组成；Spotlight 对目标控件做遮罩高亮。"
            "实现：show() 拉起 Splash，finish(mainWindow) 结束；start() 开始多步引导。",
            self,
        )
        launchRow = QHBoxLayout()
        splashButton = ElaPushButton("显示 Splash", self)
        splashButton.clicked.connect(splash.show)
        launchRow.addWidget(splashButton)
        launchRow.addWidget(spotlightTarget)
        launchRow.addStretch()
        launchLayout.addLayout(launchRow)
        centralLayout.addWidget(launchArea)

        # ElaTransfer：搜索可见时，源列表与目标列表都可快速定位。
        transfer = ElaTransfer(self)
        transfer.setSourceTitle("可用角色")
        transfer.setTargetTitle("已选角色")
        transfer.addSourceItems(["Editor", "Renderer", "Router", "Model"])
        transfer.setIsSearchVisible(True)
        transferArea, transferLayout = self._makeSection(
            "ElaTransfer",
            "用法：addSourceItems 填充左侧列表，moveToTarget/moveAllToTarget 交换选择。"
            "实现：目标项可反向移回源列表， getSourceItems/getTargetItems 返回当前状态。",
            self,
        )
        transferLayout.addWidget(transfer)

        # ElaVirtualList：只填充视口附近的数据，适合超大列表。
        virtualList = ElaVirtualList(self)
        virtualList.setItemCount(1000)
        virtualList.setItemHeight(38)
        virtualList.setIsAlternatingRowColors(True)
        listArea, listLayout = self._makeSection(
            "ElaVirtualList",
            "用法：setItemCount 只声明规模，不预创建所有子项。"
            "实现：itemRequestData 报告将要显示的范围，供外部延迟填充数据。",
            self,
        )
        listLayout.addWidget(virtualList)
        centralLayout.addWidget(transferArea)
        centralLayout.addWidget(listArea)

        # ElaWatermark：父级 resize 时自动铺满重复文本。
        watermarkHost = QWidget(self)
        watermarkHost.setFixedSize(320, 160)
        watermark = ElaWatermark("ElaWidgetTools", watermarkHost)
        watermark.setFontPixelSize(16)
        watermark.setOpacity(0.12)
        watermark.setRotation(-30)
        watermark.show()

        # ElaAppBar：独立标题栏可嵌入任意容器窗口。
        appBarHost = QWidget(self)
        appBarHost.setFixedSize(360, 150)
        appBar = ElaAppBar(appBarHost)
        appBar.setFixedHeight(42)
        appBar.setIsFixedSize(True)
        appBarItem = ElaText("无边框容器 AppBar", 14, appBarHost)

        watermarkArea, watermarkLayout = self._makeSection(
            "ElaWatermark / ElaAppBar",
            "用法：Watermark 绑定到要覆盖的 QWidget；AppBar 提供拖动、按钮和自定义菜单。"
            "实现：两者都在 paintEvent 中绘制 Fluent 材质，并跟随父级几何变化。",
            self,
        )
        advancedRow = QHBoxLayout()
        advancedRow.addWidget(watermarkHost)
        advancedRow.addWidget(appBarHost)
        advancedRow.addStretch()
        watermarkLayout.addWidget(appBarItem)
        watermarkLayout.addLayout(advancedRow)
        centralLayout.addWidget(watermarkArea)

        # ElaGraphicsLineItem：两个节点之间的连线；坐标点连接适合静态示意图。
        graphicsScene = ElaGraphicsScene(self)
        graphicsScene.setSceneRect(0, 0, 480, 260)
        firstNode = ElaGraphicsItem()
        firstNode.setWidth(96)
        firstNode.setHeight(68)
        secondNode = ElaGraphicsItem()
        secondNode.setWidth(96)
        secondNode.setHeight(68)
        lineScene = QGraphicsScene(0, 0, 320, 190, self)
        pointLine = ElaGraphicsLineItem(QPointF(30, 40), QPointF(290, 150))
        graphicsScene.addItem(firstNode)
        graphicsScene.addItem(secondNode)
        lineScene.addItem(pointLine)
        lineView = QGraphicsView(lineScene)
        lineView.setFixedSize(320, 190)
        graphicsScene.addItemLink(firstNode, secondNode)
        graphicsView = ElaGraphicsView(graphicsScene)
        graphicsView.setScene(graphicsScene)
        graphicsView.setFixedSize(480, 220)
        graphicsArea, graphicsLayout = self._makeSection(
            "ElaGraphicsLineItem",
            "用法：通过两个 ElaGraphicsItem 可建立交互连线；QPointF 构造适合固定连线。"
            "实现：Python 侧推荐 addItemLink；直接构造的 LineItem 可用于检查几何属性。",
            self,
        )
        graphicsBody = QHBoxLayout()
        graphicsBody.addWidget(graphicsView)
        graphicsBody.addWidget(lineView)
        graphicsLayout.addLayout(graphicsBody)
        centralLayout.addWidget(graphicsArea)

        # ElaScreenCaptureManager：屏幕采集是平台相关能力，示例只展示配置。
        captureResult = ElaText("点击检查显示器，本页面不会默认启动采集。", 12, self)
        captureResult.setWordWrap(True)
        captureArea, captureLayout = self._makeSection(
            "ElaScreenCaptureManager",
            "用法：DisplayID/GrabArea/FrameRate 三项决定采集源。"
            "实现：startGrabScreen 后 grabImageUpdate 发送 QImage；此示例只初始化，不默认采集。",
            self,
        )
        captureLayout.addWidget(captureResult)
        checkCaptureButton = ElaPushButton("检查显示器", self)
        checkCaptureButton.clicked.connect(
            lambda: self.refreshCaptureDisplays(captureResult)
        )
        captureLayout.addWidget(checkCaptureButton)
        centralLayout.addWidget(captureArea)

        centralLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)

    def refreshCaptureDisplays(self, resultText: ElaText):
        captureManager = ElaScreenCaptureManager.getInstance()
        captureManager.setGrabFrameRate(30)
        displayNames = captureManager.getDisplayList()
        resultText.setText(", ".join(displayNames) if displayNames else "当前环境未报告显示器")
