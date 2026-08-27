from PySide6.QtCore import QDate, QDateTime, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget

from ElaWidgetTools import (
    ElaAutoComplete,
    ElaCalendarPicker,
    ElaCaptcha,
    ElaCheckBox,
    ElaColorDialog,
    ElaCopyButton,
    ElaCountdown,
    ElaDoubleSpinBox,
    ElaGroupBox,
    ElaIconButton,
    ElaIconType,
    ElaKeyBinder,
    ElaNumberBox,
    ElaPasswordBox,
    ElaPushButton,
    ElaRadioButton,
    ElaRoller,
    ElaRollerPicker,
    ElaScrollPageArea,
    ElaSplitter,
    ElaTabWidget,
    ElaText,
    ElaTreeSelect,
    ElaUploadArea,
)
from ExamplePage.T_BasePage import T_BasePage


def _usageNote(text: str, parent: QWidget) -> ElaText:
    note = ElaText(text, 12, parent)
    note.setWordWrap(True)
    return note


class T_ExpansionComponents(T_BasePage):
    """第一批未覆盖组件的完整交互示例。

    每个区块都同时给出可见的使用说明和关键 API 顺序：
    先设置状态，再连接信号，最后把控件加入布局。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaExpansionComponents")
        self.createCustomWidget("More missing component examples")

        centralWidget = QWidget(self)
        centralLayout = QVBoxLayout(centralWidget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(10)

        # ElaAutoComplete：维护候选词数组；MatchMode 决定前缀/包含等匹配规则。
        autoComplete = ElaAutoComplete(self)
        autoComplete.setFixedHeight(38)
        autoComplete.setPlaceholderText("输入 Python、Qt 或 PySide6")
        autoComplete.setCompletions(["Python", "PyQt", "PySide6", "Qt Widgets", "Fluent Design"])
        autoCompleteResult = ElaText("输入后按回车确认", self)
        autoCompleteResult.setTextPixelSize(12)
        autoComplete.completionSelected.connect(autoCompleteResult.setText)
        autoComplete.returnPressed.connect(
            lambda value: autoCompleteResult.setText(f"已提交：{value}")
        )
        autoCompleteArea = ElaScrollPageArea(self)
        autoCompleteAreaLayout = QVBoxLayout(autoCompleteArea)
        autoCompleteAreaLayout.addWidget(ElaText("ElaAutoComplete", 15, self))
        autoCompleteAreaLayout.addWidget(_usageNote(
            "用法：setCompletions 提供候选集合。实现：控件在文本变化时过滤候选项，"
            "completionSelected 返回选中结果，returnPressed 表示用户直接提交。",
            self,
        ))
        autoCompleteBody = QHBoxLayout()
        autoCompleteBody.addWidget(ElaText("搜索:", 13, self))
        autoCompleteBody.addWidget(autoComplete)
        autoCompleteBody.addWidget(autoCompleteResult)
        autoCompleteBody.addStretch()
        autoCompleteAreaLayout.addLayout(autoCompleteBody)
        autoCompleteArea.setMinimumHeight(140)
        centralLayout.addWidget(autoCompleteArea)

        # ElaCalendarPicker：按钮外壳承载弹出日历，选中日期通过 QDate 返回。
        calendarPicker = ElaCalendarPicker(self)
        calendarPicker.setSelectedDate(QDate.currentDate())
        calendarResult = ElaText(QDate.currentDate().toString("yyyy-MM-dd"), self)
        calendarPicker.selectedDateChanged.connect(
            lambda date: calendarResult.setText(date.toString("yyyy-MM-dd"))
        )
        calendarArea = ElaScrollPageArea(self)
        calendarAreaLayout = QVBoxLayout(calendarArea)
        calendarAreaLayout.addWidget(ElaText("ElaCalendarPicker", 15, self))
        calendarAreaLayout.addWidget(_usageNote(
            "用法：用 setSelectedDate 提供初始值，点击按钮后选择日期。"
            "实现：内部弹出日历面板，selectedDateChanged 信号把 QDate 同步回外部。",
            self,
        ))
        calendarBody = QHBoxLayout()
        calendarBody.addWidget(calendarPicker)
        calendarBody.addWidget(calendarResult)
        calendarBody.addStretch()
        calendarAreaLayout.addLayout(calendarBody)
        centralLayout.addWidget(calendarArea)

        # ElaCaptcha：分格输入；AlphaNumeric 允许数字与字母混排。
        captcha = ElaCaptcha(self)
        captcha.setInputMode(ElaCaptcha.InputMode.AlphaNumeric)
        captcha.setCodeLength(5)
        captcha.setFixedHeight(48)
        captchaResult = ElaText("等待输入", self)
        captcha.codeCompleted.connect(lambda code: captchaResult.setText(f"完成: {code}"))
        captcha.codeChanged.connect(
            lambda code: captchaResult.setText("等待输入")
            if len(code) < captcha.getCodeLength() else None
        )
        clearCaptchaButton = ElaPushButton("清除", self)
        clearCaptchaButton.clicked.connect(captcha.clear)
        captchaArea = ElaScrollPageArea(self)
        captchaAreaLayout = QVBoxLayout(captchaArea)
        captchaAreaLayout.addWidget(ElaText("ElaCaptcha", 15, self))
        captchaAreaLayout.addWidget(_usageNote(
            "用法：InputMode 控制字符集，setCodeLength 控制位数。"
            "实现：每个格子独立接收输入，clear 清空全部格位，codeCompleted 在满足长度时触发。",
            self,
        ))
        captchaBody = QHBoxLayout()
        captchaBody.addWidget(captcha)
        captchaBody.addWidget(clearCaptchaButton)
        captchaBody.addWidget(captchaResult)
        captchaBody.addStretch()
        captchaAreaLayout.addLayout(captchaBody)
        centralLayout.addWidget(captchaArea)

        # ElaColorDialog：无模态打开对话框；选中颜色后再更新外部文本。
        colorDialog = ElaColorDialog(self)
        colorDialog.setCurrentColor("#0078D4")
        colorResult = ElaText("未选择颜色", self)
        colorDialog.colorSelected.connect(
            lambda color: colorResult.setText(f"已选择 {color.name()}")
        )
        openColorButton = ElaPushButton("打开颜色对话框", self)
        openColorButton.clicked.connect(colorDialog.open)
        colorArea = ElaScrollPageArea(self)
        colorAreaLayout = QVBoxLayout(colorArea)
        colorAreaLayout.addWidget(ElaText("ElaColorDialog", 15, self))
        colorAreaLayout.addWidget(_usageNote(
            "用法：setCurrentColor 只是初始值；用户确认后才会发出 colorSelected。"
            "实现：HSV 色域与亮度面板计算 RGB，避免直接依赖系统原生 QColorDialog。",
            self,
        ))
        colorBody = QHBoxLayout()
        colorBody.addWidget(openColorButton)
        colorBody.addWidget(colorResult)
        colorBody.addStretch()
        colorAreaLayout.addLayout(colorBody)
        centralLayout.addWidget(colorArea)

        # ElaCopyButton：把 copyText 写入剪贴板，并短暂切换成功样式。
        copyButton = ElaCopyButton("复制仓库地址", self)
        copyButton.setCopyText("https://github.com/CyberWon/PySide6ElaWidgetTools")
        copyButton.setSuccessText("已复制")
        copyButton.setSuccessDuration(1600)
        copyButton.copyCompleted.connect(lambda value: print(f"复制完成: {value}"))
        copyArea = ElaScrollPageArea(self)
        copyAreaLayout = QVBoxLayout(copyArea)
        copyAreaLayout.addWidget(ElaText("ElaCopyButton", 15, self))
        copyAreaLayout.addWidget(_usageNote(
            "用法：setCopyText 指定实际写入剪贴板的内容。"
            "实现：mouseReleaseEvent 触发复制、发出 copyCompleted，并按 setSuccessDuration 回退样式。",
            self,
        ))
        copyBody = QHBoxLayout()
        copyBody.addWidget(copyButton)
        copyBody.addStretch()
        copyAreaLayout.addLayout(copyBody)
        centralLayout.addWidget(copyArea)

        # ElaCountdown：倒计时内部维护 QTimeLine；暂停后用 resume 继续。
        self._countdown = ElaCountdown(self)
        self._countdown.setIsShowDays(True)
        self._countdown.setRemainingSeconds(24 * 3600 + 3661)
        targetCountdown = ElaCountdown(self)
        targetCountdown.setIsShowDays(False)
        targetCountdown.setTargetDateTime(QDateTime.currentDateTime().addSecs(7200))
        targetCountdown.start()
        startButton = ElaPushButton("开始", self)
        pauseButton = ElaPushButton("暂停", self)
        resumeButton = ElaPushButton("继续", self)
        resetButton = ElaPushButton("重置", self)
        startButton.clicked.connect(self._countdown.start)
        pauseButton.clicked.connect(self._countdown.pause)
        resumeButton.clicked.connect(self._countdown.resume)
        resetButton.clicked.connect(
            lambda: (self._countdown.stop(), self._countdown.setRemainingSeconds(86400 + 3661))
        )
        countdownArea = ElaScrollPageArea(self)
        countdownAreaLayout = QVBoxLayout(countdownArea)
        countdownHeader = QHBoxLayout()
        countdownHeader.addWidget(ElaText("ElaCountdown", 15, self))
        countdownHeader.addWidget(startButton)
        countdownHeader.addWidget(pauseButton)
        countdownHeader.addWidget(resumeButton)
        countdownHeader.addWidget(resetButton)
        countdownHeader.addStretch()
        countdownBody = QHBoxLayout()
        countdownBody.addWidget(self._countdown)
        countdownBody.addWidget(ElaText("2 小时后:", 13, self))
        countdownBody.addWidget(targetCountdown)
        countdownBody.addStretch()
        countdownAreaLayout.addWidget(_usageNote(
            "用法：setRemainingSeconds 或 setTargetDateTime 二选一，随后调用 start。"
            "实现：剩余时间逐步刷新数字位图；pause/resume 复用同一目标时间。",
            self,
        ))
        countdownAreaLayout.addLayout(countdownHeader)
        countdownAreaLayout.addLayout(countdownBody)
        centralLayout.addWidget(countdownArea)

        # ElaNumberBox / ElaDoubleSpinBox：分别用于整数步进与小数精度输入。
        numberBox = ElaNumberBox(self)
        numberBox.setMinimum(-50)
        numberBox.setMaximum(200)
        numberBox.setStep(5)
        numberBox.setValue(25)
        doubleSpinBox = ElaDoubleSpinBox(self)
        doubleSpinBox.setRange(0.0, 10.0)
        doubleSpinBox.setSingleStep(0.1)
        doubleSpinBox.setDecimals(2)
        doubleSpinBox.setValue(3.14)
        numberResult = ElaText("25", self)
        numberResult.setTextPixelSize(13)
        numberBox.valueChanged.connect(lambda value: numberResult.setText(str(int(value))))
        numberArea = ElaScrollPageArea(self)
        numberAreaLayout = QVBoxLayout(numberArea)
        numberAreaLayout.addWidget(ElaText("ElaNumberBox / ElaDoubleSpinBox", 15, self))
        numberAreaLayout.addWidget(_usageNote(
            "用法：range、step、decimals 三者决定可编辑范围。"
            "实现：两侧加减按钮和滚轮操作都经过同一 valueChanged 路径，保证数据来源统一。",
            self,
        ))
        numberBody = QHBoxLayout()
        numberBody.addWidget(numberBox)
        numberBody.addWidget(numberResult)
        numberBody.addWidget(doubleSpinBox)
        numberBody.addStretch()
        numberAreaLayout.addLayout(numberBody)
        centralLayout.addWidget(numberArea)

        # ElaPasswordBox：可见性切换由控件内部完成，外部只需要同步状态文本。
        passwordBox = ElaPasswordBox(self)
        passwordBox.setFixedSize(280, 38)
        passwordBox.setPlaceholderText("请输入密码")
        passwordResult = ElaText("密码已隐藏", self)
        passwordArea = ElaScrollPageArea(self)
        passwordAreaLayout = QVBoxLayout(passwordArea)
        passwordAreaLayout.addWidget(ElaText("ElaPasswordBox", 15, self))
        passwordAreaLayout.addWidget(_usageNote(
            "用法：placeholder 和 fixed size 使用 Qt 基类能力。"
            "实现：眼睛按钮切换回显模式，getIsPasswordVisible 可用于保存用户偏好。",
            self,
        ))
        passwordBody = QHBoxLayout()
        passwordBody.addWidget(passwordBox)
        passwordBody.addWidget(passwordResult)
        passwordBody.addStretch()
        passwordAreaLayout.addLayout(passwordBody)
        centralLayout.addWidget(passwordArea)

        # ElaIconButton：只用图标绘制，Hover 颜色由主题模式分别提供。
        heartButton = ElaIconButton(ElaIconType.IconName.Plus, self)
        selectedButton = ElaIconButton(ElaIconType.IconName.StarChristmas, 18, 42, 42, self)
        selectedButton.setIsSelected(True)
        iconResult = ElaText("0", self)

        def onIconClicked():
            iconResult.setText(str(int(iconResult.text()) + 1))

        heartButton.clicked.connect(onIconClicked)
        selectedButton.clicked.connect(
            lambda: iconResult.setText(str(int(iconResult.text()) + 1))
        )
        iconArea = ElaScrollPageArea(self)
        iconAreaLayout = QVBoxLayout(iconArea)
        iconAreaLayout.addWidget(ElaText("ElaIconButton", 15, self))
        iconAreaLayout.addWidget(_usageNote(
            "用法：可以只传图标，或传入 pixelSize、fixedWidth、fixedHeight。"
            "实现：paintEvent 根据 Light/Dark 状态绘制 Fluent 图标和 Hover 背景。",
            self,
        ))
        iconBody = QHBoxLayout()
        iconBody.addWidget(heartButton)
        iconBody.addWidget(selectedButton)
        iconBody.addWidget(iconResult)
        iconBody.addStretch()
        iconAreaLayout.addLayout(iconBody)
        centralLayout.addWidget(iconArea)

        # ElaGroupBox：圆角分组容器，内部仍然使用普通 Qt 布局。
        groupBox = ElaGroupBox("ElaGroupBox", self)
        groupBox.setFixedSize(360, 190)
        groupBoxLayout = QVBoxLayout(groupBox)
        groupBoxLayout.setContentsMargins(15, 25, 15, 12)
        groupBoxLayout.setSpacing(6)
        groupBoxLayout.addWidget(ElaText("适合聚合一组相关控件", self))
        groupCheckBox = ElaCheckBox("启用高级选项", groupBox)
        groupCheckBox.setChecked(True)
        primaryRadio = ElaRadioButton("主题一", groupBox)
        secondaryRadio = ElaRadioButton("主题二", groupBox)
        primaryRadio.setChecked(True)
        groupBoxLayout.addWidget(groupCheckBox)
        groupBoxLayout.addWidget(primaryRadio)
        groupBoxLayout.addWidget(secondaryRadio)
        groupBoxLayout.addStretch()
        groupArea = ElaScrollPageArea(self)
        groupAreaLayout = QHBoxLayout(groupArea)
        groupArea.setFixedHeight(220)
        groupInfoLayout = QVBoxLayout()
        groupInfoLayout.addWidget(ElaText("ElaGroupBox", 15, self))
        groupInfoLayout.addWidget(_usageNote(
            "用法：ElaGroupBox 只负责标题、圆角和背景。"
            "实现：子控件仍放在标准 QVBoxLayout 中，因此布局行为与 QGroupBox 相同。",
            self,
        ))
        groupInfoLayout.addStretch()
        groupAreaLayout.addWidget(groupBox)
        groupAreaLayout.addLayout(groupInfoLayout)
        groupAreaLayout.addStretch()
        centralLayout.addWidget(groupArea)

        # ElaSplitter：继承拖拽比例逻辑，手柄由 Fluent 样式绘制。
        horizontalSplitter = ElaSplitter(Qt.Orientation.Horizontal, self)
        leftPanel = QLabel("左侧面板")
        rightPanel = QLabel("右侧面板")
        leftPanel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rightPanel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        leftPanel.setMinimumWidth(120)
        rightPanel.setMinimumWidth(120)
        horizontalSplitter.addWidget(leftPanel)
        horizontalSplitter.addWidget(rightPanel)
        horizontalSplitter.setStretchFactor(0, 1)
        horizontalSplitter.setStretchFactor(1, 1)
        splitterArea = ElaScrollPageArea(self)
        splitterAreaLayout = QVBoxLayout(splitterArea)
        splitterArea.setFixedHeight(200)
        splitterAreaLayout.addWidget(ElaText("ElaSplitter", 15, self))
        splitterAreaLayout.addWidget(_usageNote(
            "用法：setMinimumWidth 和 setStretchFactor 保护最小尺寸与默认比例。"
            "实现：createHandle 的 Fluent 手柄只负责视觉，拖拽仍由 QSplitter 维护。",
            self,
        ))
        splitterAreaLayout.addWidget(horizontalSplitter)
        centralLayout.addWidget(splitterArea)

        # ElaTabWidget：每个 tab 可以放独立 QWidget；关闭/切页行为由内部信号处理。
        tabWidget = ElaTabWidget(self)
        tabWidget.setFixedSize(520, 200)
        overviewTab = QLabel("基础用法")
        interactionTab = QLabel("交互状态")
        themeTab = QLabel("主题与动画")
        for panel in (overviewTab, interactionTab, themeTab):
            panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tabWidget.addTab(overviewTab, "Overview")
        tabWidget.addTab(interactionTab, "Interaction")
        tabWidget.addTab(themeTab, "Theme")
        tabArea = ElaScrollPageArea(self)
        tabAreaLayout = QVBoxLayout(tabArea)
        tabAreaLayout.addWidget(ElaText("ElaTabWidget", 15, self))
        tabAreaLayout.addWidget(_usageNote(
            "用法：addTab 接受普通 QWidget，页面切换逻辑由 QTabWidget 继承而来。"
            "实现：标签条重新绘制为浏览器式拖拽样式，tab 页面仍由 Qt 管理生命周期。",
            self,
        ))
        tabBody = QHBoxLayout()
        tabBody.addWidget(tabWidget)
        tabBody.addStretch()
        tabAreaLayout.addLayout(tabBody)
        centralLayout.addWidget(tabArea)

        # ElaRoller / ElaRollerPicker：单滚轮选择与组合滚轮选择。
        roller = ElaRoller(self)
        roller.setItemList(["Priority", "High", "Medium", "Low"])
        roller.setIsEnableLoop(True)
        roller.setCurrentData("Medium")
        hourItems = [f"{hour:02d}" for hour in range(24)]
        minuteItems = [f"{minute:02d}" for minute in range(60)]
        rollerPicker = ElaRollerPicker(self)
        rollerPicker.addRoller(hourItems)
        rollerPicker.addRoller(minuteItems)
        rollerPicker.setCurrentData(["08", "30"])
        rollerArea = ElaScrollPageArea(self)
        rollerAreaLayout = QVBoxLayout(rollerArea)
        rollerArea.setFixedHeight(260)
        rollerAreaLayout.addWidget(ElaText("ElaRoller / ElaRollerPicker", 15, self))
        rollerAreaLayout.addWidget(_usageNote(
            "用法：ElaRoller 一列数据；ElaRollerPicker 通过 addRoller 组合多列。"
            "实现：每个滚轮独立维护 item index，picker.setCurrentData 会按列表顺序同步各列。",
            self,
        ))
        rollerBody = QHBoxLayout()
        rollerBody.addWidget(roller)
        rollerBody.addWidget(rollerPicker)
        rollerBody.addStretch()
        rollerAreaLayout.addLayout(rollerBody)
        centralLayout.addWidget(rollerArea)

        # ElaKeyBinder：录制实际虚拟键，macOS 的 Fn 键也能进入录制状态。
        keyBinder = ElaKeyBinder(self)
        keyBinderResult = ElaText("未绑定", self)
        keyBinder.binderKeyTextChanged.connect(keyBinderResult.setText)
        keyArea = ElaScrollPageArea(self)
        keyAreaLayout = QVBoxLayout(keyArea)
        keyAreaLayout.addWidget(ElaText("ElaKeyBinder", 15, self))
        keyAreaLayout.addWidget(_usageNote(
            "用法：点击控件开始录制，再点击别的控件结束录制。"
            "实现：记录 native virtual key 并渲染可读文本，keyBindingChanged 返回绑定结果。",
            self,
        ))
        keyBody = QHBoxLayout()
        keyBody.addWidget(keyBinder)
        keyBody.addWidget(keyBinderResult)
        keyBody.addStretch()
        keyAreaLayout.addLayout(keyBody)
        centralLayout.addWidget(keyArea)

        # ElaTreeSelect：QStandardItemModel 提供层级数据，控件只负责展示与筛选。
        treeModel = QStandardItemModel(self)
        rootItem = treeModel.invisibleRootItem()
        platformItem = QStandardItem("Platforms")
        platformItem.appendRow(QStandardItem("macOS"))
        platformItem.appendRow(QStandardItem("Windows"))
        languageItem = QStandardItem("Languages")
        languageItem.appendRow(QStandardItem("C++"))
        languageItem.appendRow(QStandardItem("Python"))
        rootItem.appendRow(platformItem)
        rootItem.appendRow(languageItem)

        treeSelect = ElaTreeSelect(self)
        treeSelect.setModel(treeModel)
        treeSelect.setPlaceholderText("选择平台或语言")
        treeSelect.setIsSearchVisible(True)
        treeSelect.setFixedHeight(38)
        treeResult = ElaText("未选择", self)
        treeSelect.currentTextChanged.connect(treeResult.setText)
        treeArea = ElaScrollPageArea(self)
        treeAreaLayout = QVBoxLayout(treeArea)
        treeAreaLayout.addWidget(ElaText("ElaTreeSelect", 15, self))
        treeAreaLayout.addWidget(_usageNote(
            "用法：先用 QStandardItem 组装树形 model，再传给 setModel。"
            "实现：搜索框过滤可见项，展开逻辑由标准 item model 驱动。",
            self,
        ))
        treeBody = QHBoxLayout()
        treeBody.addWidget(treeSelect)
        treeBody.addWidget(treeResult)
        treeBody.addStretch()
        treeAreaLayout.addLayout(treeBody)
        centralLayout.addWidget(treeArea)

        # ElaUploadArea：拖拽和文件对话框共用同一套校验规则。
        uploadArea = ElaUploadArea(self)
        uploadArea.setFixedHeight(180)
        uploadArea.setTitle("拖拽文件到此处")
        uploadArea.setSubTitle("支持 png、jpg、pdf、txt，最多 5 个")
        uploadArea.setDialogTitle("选择上传文件")
        uploadArea.setAcceptedSuffixes(["png", "jpg", "jpeg", "pdf", "txt"])
        uploadArea.setMaxFileCount(5)
        uploadResult = ElaText("已选择 0 个文件", self)
        clearUploadButton = ElaPushButton("清空", self)
        uploadArea.filesSelected.connect(
            lambda files: uploadResult.setText(f"已选择 {len(files)} 个文件")
        )
        clearUploadButton.clicked.connect(
            lambda: (uploadArea.clearFiles(), uploadResult.setText("已选择 0 个文件"))
        )
        uploadContainer = ElaScrollPageArea(self)
        uploadContainerLayout = QVBoxLayout(uploadContainer)
        uploadHeader = QHBoxLayout()
        uploadHeader.addWidget(ElaText("ElaUploadArea", 15, self))
        uploadHeader.addSpacing(10)
        uploadHeader.addWidget(uploadResult)
        uploadHeader.addWidget(clearUploadButton)
        uploadHeader.addStretch()
        uploadContainerLayout.addLayout(uploadHeader)
        uploadContainerLayout.addWidget(uploadArea)
        centralLayout.addWidget(uploadContainer)

        centralLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)
