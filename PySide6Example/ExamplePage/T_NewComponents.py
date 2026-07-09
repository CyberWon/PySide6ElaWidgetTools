from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QButtonGroup

from ElaWidgetTools import (
    ElaComboBox,
    ElaDivider,
    ElaInfoBadge,
    ElaLineEdit,
    ElaPagination,
    ElaPushButton,
    ElaQRCode,
    ElaRadioButton,
    ElaRatingControl,
    ElaScrollPageArea,
    ElaSkeleton,
    ElaSlider,
    ElaStatCard,
    ElaSteps,
    ElaTag,
    ElaText,
    ElaIconType,
)
from ExamplePage.T_BasePage import T_BasePage


class T_NewComponents(T_BasePage):
    """新增组件演示页面（代表性子集）。

    已跳过以下组件（Python 绑定中 API 不可用或实现过于复杂）：
    - ElaTimeline: addItem / TimelineItem 结构体未在 Python 绑定中暴露
    - ElaCommandBar: addItem 重载未在 Python 绑定中暴露
    - ElaWizard / ElaTransfer / ElaNotificationCenter / ElaSpotlight /
      ElaSheetPanel 等: 依赖大量 C++ lambda 信号槽或延迟创建，复杂度过高
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaNewComponents")
        self.createCustomWidget("新增组件的演示页面")

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaNewComponents")

        # ========== ElaInfoBadge 示例（三种模式：Dot / Value / Icon）==========
        dotTargetButton = ElaPushButton("邮件", self)
        dotTargetButton.setFixedSize(80, 36)
        self._dotBadge = ElaInfoBadge(self)
        self._dotBadge.setBadgeMode(ElaInfoBadge.BadgeMode.Dot)
        self._dotBadge.setSeverity(ElaInfoBadge.Severity.Attention)
        self._dotBadge.attachTo(dotTargetButton)

        valueTargetButton = ElaPushButton("通知", self)
        valueTargetButton.setFixedSize(80, 36)
        self._valueBadge = ElaInfoBadge(5, self)
        self._valueBadge.setSeverity(ElaInfoBadge.Severity.Informational)
        self._valueBadge.attachTo(valueTargetButton)

        iconTargetButton = ElaPushButton("设置", self)
        iconTargetButton.setFixedSize(80, 36)
        self._iconBadge = ElaInfoBadge(
            ElaIconType.IconName.CircleExclamation, self
        )
        self._iconBadge.setSeverity(ElaInfoBadge.Severity.Caution)
        self._iconBadge.attachTo(iconTargetButton)

        badgeArea = ElaScrollPageArea(self)
        badgeLayout = QHBoxLayout(badgeArea)
        badgeLayout.addWidget(ElaText("ElaInfoBadge", 15, self))
        badgeLayout.addSpacing(20)
        badgeLayout.addWidget(dotTargetButton)
        badgeLayout.addSpacing(20)
        badgeLayout.addWidget(valueTargetButton)
        badgeLayout.addSpacing(20)
        badgeLayout.addWidget(iconTargetButton)
        badgeLayout.addStretch()

        # InfoBadge 值控制（滑块联动）
        badgeControlArea = ElaScrollPageArea(self)
        badgeControlLayout = QHBoxLayout(badgeControlArea)
        badgeControlLayout.addWidget(ElaText("InfoBadge 值控制", 15, self))
        badgeSlider = ElaSlider(self)
        badgeSlider.setRange(0, 150)
        badgeSlider.setValue(5)
        badgeSlider.setFixedWidth(200)
        badgeValueText = ElaText("5", self)
        badgeValueText.setTextPixelSize(13)

        def onBadgeValueChanged(v):
            self._valueBadge.setValue(v)
            badgeValueText.setText(str(v))

        badgeSlider.valueChanged.connect(onBadgeValueChanged)
        badgeControlLayout.addWidget(badgeSlider)
        badgeControlLayout.addWidget(badgeValueText)
        badgeControlLayout.addStretch()

        # InfoBadge 严重等级（单选切换）
        severityArea = ElaScrollPageArea(self)
        severityLayout = QHBoxLayout(severityArea)
        severityLayout.addWidget(ElaText("InfoBadge 严重等级", 15, self))
        severityGroup = QButtonGroup(self)
        severities = [
            (ElaInfoBadge.Severity.Attention, "Attention"),
            (ElaInfoBadge.Severity.Informational, "Informational"),
            (ElaInfoBadge.Severity.Success, "Success"),
            (ElaInfoBadge.Severity.Caution, "Caution"),
            (ElaInfoBadge.Severity.Critical, "Critical"),
        ]
        for idx, (sev, name) in enumerate(severities):
            radio = ElaRadioButton(name, self)
            severityGroup.addButton(radio, idx)
            if sev == ElaInfoBadge.Severity.Informational:
                radio.setChecked(True)
            severityLayout.addWidget(radio)

        def onSeverityClicked(idx):
            self._valueBadge.setSeverity(severities[idx][0])

        severityGroup.idClicked.connect(onSeverityClicked)
        severityLayout.addStretch()

        # ========== ElaTag 示例（5 种颜色）==========
        tagArea = ElaScrollPageArea(self)
        tagLayout = QHBoxLayout(tagArea)
        tagLayout.addWidget(ElaText("ElaTag", 15, self))
        tagLayout.addSpacing(10)
        tagColors = [
            (ElaTag.TagColor.Default, "Default"),
            (ElaTag.TagColor.Primary, "Primary"),
            (ElaTag.TagColor.Success, "Success"),
            (ElaTag.TagColor.Warning, "Warning"),
            (ElaTag.TagColor.Danger, "Danger"),
        ]
        for color, name in tagColors:
            tag = ElaTag(self)
            tag.setTagText(name)
            tag.setTagColor(color)
            tagLayout.addWidget(tag)
        tagLayout.addStretch()

        # Tag 可关闭
        tagCloseArea = ElaScrollPageArea(self)
        tagCloseLayout = QHBoxLayout(tagCloseArea)
        tagCloseLayout.addWidget(ElaText("ElaTag 可关闭", 15, self))
        tagCloseLayout.addSpacing(10)
        closableTags = ["可关闭", "北京", "上海"]
        for idx, text in enumerate(closableTags):
            tag = ElaTag(self)
            tag.setTagText(text)
            tag.setIsClosable(True)
            if idx == 0:
                tag.setTagColor(ElaTag.TagColor.Primary)
            tag.closed.connect(tag.hide)
            tagCloseLayout.addWidget(tag)
        tagCloseLayout.addStretch()

        # Tag 可选中
        tagCheckArea = ElaScrollPageArea(self)
        tagCheckLayout = QHBoxLayout(tagCheckArea)
        tagCheckLayout.addWidget(ElaText("ElaTag 可选中", 15, self))
        tagCheckLayout.addSpacing(10)
        checkableTags = [("周一", False), ("周二", True), ("周三", False)]
        for text, checked in checkableTags:
            tag = ElaTag(self)
            tag.setTagText(text)
            tag.setIsCheckable(True)
            tag.setIsChecked(checked)
            tagCheckLayout.addWidget(tag)
        tagCheckLayout.addStretch()

        # ========== ElaRatingControl 示例 ==========
        self._ratingControl = ElaRatingControl(self)
        self._ratingControl.setRating(5)
        ratingValue = ElaText("5", self)
        ratingValue.setTextPixelSize(15)

        def onRatingChanged(r):
            ratingValue.setText(str(r))

        self._ratingControl.ratingChanged.connect(onRatingChanged)

        ratingArea = ElaScrollPageArea(self)
        ratingLayout = QHBoxLayout(ratingArea)
        ratingLayout.addWidget(ElaText("ElaRatingControl", 15, self))
        ratingLayout.addWidget(self._ratingControl)
        ratingLayout.addWidget(ratingValue)
        ratingLayout.addStretch()

        # ========== ElaDivider 示例 ==========
        divider1 = ElaDivider(self)
        divider2 = ElaDivider("分隔文字", self)

        # ========== ElaSkeleton 示例 ==========
        skelCircle = ElaSkeleton(self)
        skelCircle.setSkeletonType(ElaSkeleton.SkeletonType.Circle)
        skelCircle.setFixedSize(40, 40)
        skelText1 = ElaSkeleton(self)
        skelText1.setSkeletonType(ElaSkeleton.SkeletonType.Text)
        skelText1.setFixedSize(250, 16)
        skelRect = ElaSkeleton(self)
        skelRect.setSkeletonType(ElaSkeleton.SkeletonType.Rectangle)
        skelRect.setFixedSize(200, 80)
        skelRect.setBorderRadius(8)

        skelArea = ElaScrollPageArea(self)
        skelLayout = QHBoxLayout(skelArea)
        skelLayout.addWidget(ElaText("ElaSkeleton", 15, self))
        skelLayout.addSpacing(10)
        skelLayout.addWidget(skelCircle)
        skelLayout.addSpacing(10)
        skelLayout.addWidget(skelText1)
        skelLayout.addSpacing(10)
        skelLayout.addWidget(skelRect)
        skelLayout.addStretch()

        # ========== ElaSteps 示例 ==========
        self._steps = ElaSteps(self)
        self._steps.setStepCount(4)
        self._steps.setStepTitles(["选择商品", "确认订单", "支付", "完成"])
        self._steps.setCurrentStep(1)
        prevBtn = ElaPushButton("上一步", self)
        prevBtn.setFixedSize(80, 32)
        nextBtn = ElaPushButton("下一步", self)
        nextBtn.setFixedSize(80, 32)
        prevBtn.clicked.connect(self._steps.previous)
        nextBtn.clicked.connect(self._steps.next)

        stepsCtrl = QHBoxLayout()
        stepsCtrl.addWidget(ElaText("ElaSteps", 15, self))
        stepsCtrl.addStretch()
        stepsCtrl.addWidget(prevBtn)
        stepsCtrl.addWidget(nextBtn)

        # ========== ElaPagination 示例 ==========
        self._pagination = ElaPagination(self)
        totalPages = 50
        self._pagination.setTotalPages(totalPages)
        self._pagination.setCurrentPage(1)
        self._pagination.setJumperVisible(True)
        pageInfo = ElaText("第 1 / {} 页".format(totalPages), self)
        pageInfo.setTextPixelSize(13)

        def onPageChanged(pg):
            pageInfo.setText("第 {} / {} 页".format(pg, totalPages))

        self._pagination.currentPageChanged.connect(onPageChanged)

        pgArea = ElaScrollPageArea(self)
        pgLayout = QHBoxLayout(pgArea)
        pgLayout.addWidget(ElaText("ElaPagination", 15, self))
        pgLayout.addWidget(self._pagination)
        pgLayout.addWidget(pageInfo)
        pgLayout.addStretch()

        # ========== ElaStatCard 示例（三张统计卡片）==========
        statCard1 = ElaStatCard(self)
        statCard1.setTitle("今日销售额")
        statCard1.setValue("¥86,400")
        statCard1.setCardIcon(ElaIconType.IconName.CartShopping)
        statCard1.setTrend(ElaStatCard.TrendType.Up)
        statCard1.setTrendText("+15.3%")
        statCard1.setDescription("较昨日")

        statCard2 = ElaStatCard(self)
        statCard2.setTitle("CPU 使用率")
        statCard2.setValue("62%")
        statCard2.setCardIcon(ElaIconType.IconName.Gauge)
        statCard2.setTrend(ElaStatCard.TrendType.Down)
        statCard2.setTrendText("-8.1%")
        statCard2.setDescription("较上小时")

        statCard3 = ElaStatCard(self)
        statCard3.setTitle("在线设备")
        statCard3.setValue("1,024")
        statCard3.setCardIcon(ElaIconType.IconName.WifiExclamation)
        statCard3.setTrend(ElaStatCard.TrendType.Neutral)
        statCard3.setTrendText("稳定")
        statCard3.setDescription("当前在线")

        statLayout = QHBoxLayout()
        statLayout.addWidget(ElaText("ElaStatCard", 15, self))
        statLayout.addSpacing(10)
        statLayout.addWidget(statCard1)
        statLayout.addWidget(statCard2)
        statLayout.addWidget(statCard3)
        statLayout.addStretch()

        # ========== ElaQRCode 示例 ==========
        self._qrCode = ElaQRCode(
            "https://github.com/RainbowCandyX/ElaWidgetTools", self
        )
        self._qrCode.setFixedSize(180, 180)

        qrInput = ElaLineEdit(self)
        qrInput.setText("https://github.com/RainbowCandyX/ElaWidgetTools")
        qrInput.setFixedHeight(35)
        qrInput.setMinimumWidth(300)

        def onQrTextChanged(text):
            self._qrCode.setText(text)

        qrInput.textChanged.connect(onQrTextChanged)

        qrEcLevel = ElaComboBox(self)
        ecLevels = [
            (ElaQRCode.ErrorCorrectionLevel.Low, "低 (7%)"),
            (ElaQRCode.ErrorCorrectionLevel.Medium, "中 (15%)"),
            (ElaQRCode.ErrorCorrectionLevel.Quartile, "较高 (25%)"),
            (ElaQRCode.ErrorCorrectionLevel.High, "高 (30%)"),
        ]
        for _, label in ecLevels:
            qrEcLevel.addItem(label)
        qrEcLevel.setCurrentIndex(1)

        def onEcChanged(index):
            self._qrCode.setErrorCorrectionLevel(ecLevels[index][0])

        qrEcLevel.currentIndexChanged.connect(onEcChanged)

        qrArea = ElaScrollPageArea(self)
        qrArea.setFixedHeight(240)
        qrMainLayout = QVBoxLayout(qrArea)
        qrHeader = QHBoxLayout()
        qrHeader.addWidget(ElaText("ElaQRCode", 15, self))
        qrHeader.addWidget(qrInput)
        qrHeader.addSpacing(10)
        qrHeader.addWidget(ElaText("纠错:", 13, self))
        qrHeader.addWidget(qrEcLevel)
        qrHeader.addStretch()
        qrMainLayout.addLayout(qrHeader)
        qrBody = QHBoxLayout()
        qrBody.addWidget(self._qrCode)
        qrBody.addStretch()
        qrMainLayout.addLayout(qrBody)

        # ========== 中心布局 ==========
        c = QVBoxLayout(centralWidget)
        c.setContentsMargins(0, 0, 0, 0)
        c.addWidget(badgeArea)
        c.addWidget(badgeControlArea)
        c.addWidget(severityArea)
        c.addWidget(tagArea)
        c.addWidget(tagCloseArea)
        c.addWidget(tagCheckArea)
        c.addWidget(ratingArea)
        c.addWidget(divider1)
        c.addWidget(skelArea)
        c.addWidget(divider2)
        c.addLayout(stepsCtrl)
        c.addWidget(self._steps)
        c.addWidget(pgArea)
        c.addLayout(statLayout)
        c.addWidget(qrArea)
        c.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
