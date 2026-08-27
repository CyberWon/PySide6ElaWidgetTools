from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from ElaWidgetTools import (
    ElaDialog,
    ElaDrawerArea,
    ElaDropDownButton,
    ElaEmojiPicker,
    ElaExpander,
    ElaFloatButton,
    ElaIconType,
    ElaMenu,
    ElaPopconfirm,
    ElaPushButton,
    ElaScrollPageArea,
    ElaSnackbar,
    ElaTeachingTip,
    ElaText,
    ElaToast,
    ElaToggleSwitch,
)
from ExamplePage.T_BasePage import T_BasePage


def _usageNote(text: str, parent: QWidget) -> ElaText:
    note = ElaText(text, 12, parent)
    note.setWordWrap(True)
    return note


class T_ExpansionComponents2(T_BasePage):
    """弹窗、反馈与轻量交互组件的第二批完整示例。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaExpansionComponents2")
        self.createCustomWidget("Popup and feedback component examples")

        centralWidget = QWidget(self)
        centralLayout = QVBoxLayout(centralWidget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(10)

        # ElaDialog：无边框对话框仍继承 QDialog，open() 是非模态入口。
        settingsDialog = ElaDialog(self)
        settingsDialog.setFixedSize(360, 210)
        dialogContent = QWidget(settingsDialog)
        dialogContentLayout = QVBoxLayout(dialogContent)
        dialogContentLayout.addWidget(ElaText("同步设置", 18, dialogContent))
        dialogContentLayout.addWidget(_usageNote(
            "打开后可移动窗口；右上角按钮由 WindowButtonFlag 控制。",
            dialogContent,
        ))
        openDialogButton = ElaPushButton("打开 ElaDialog", self)
        openDialogButton.clicked.connect(settingsDialog.open)
        dialogArea = ElaScrollPageArea(self)
        dialogAreaLayout = QVBoxLayout(dialogArea)
        dialogAreaLayout.addWidget(ElaText("ElaDialog", 15, self))
        dialogAreaLayout.addWidget(_usageNote(
            "用法：设置尺寸并调用 moveToCenter，用户触发时再 open() 或 exec()。"
            "实现：内置 AppBar 负责拖动、关闭和主题按钮，内容区仍使用普通 Qt 布局。",
            self,
        ))
        dialogBody = QHBoxLayout()
        dialogBody.addWidget(openDialogButton)
        dialogBody.addStretch()
        dialogAreaLayout.addLayout(dialogBody)
        centralLayout.addWidget(dialogArea)

        # ElaDropDownButton：主按钮显示文本，箭头区弹出独立 ElaMenu。
        sortButton = ElaDropDownButton(self)
        sortButton.setText("排序方式")
        sortButton.setElaIcon(ElaIconType.IconName.BarsSort)
        sortMenu = ElaMenu(self)
        sortMenu.addAction("按名称")
        sortMenu.addAction("按日期")
        sortMenu.addAction("按大小")
        sortButton.setMenu(sortMenu)
        exportButton = ElaDropDownButton(self)
        exportButton.setText("导出")
        exportMenu = ElaMenu(self)
        exportMenu.addAction("PDF")
        exportMenu.addAction("Excel")
        exportButton.setMenu(exportMenu)
        dropdownArea = ElaScrollPageArea(self)
        dropdownAreaLayout = QVBoxLayout(dropdownArea)
        dropdownAreaLayout.addWidget(ElaText("ElaDropDownButton", 15, self))
        dropdownAreaLayout.addWidget(_usageNote(
            "用法：setMenu 决定点击箭头时展开的菜单。"
            "实现：setElaIcon 控制左侧图标；菜单本身仍由 ElaMenu 管理主题与快捷键。",
            self,
        ))
        dropdownBody = QHBoxLayout()
        dropdownBody.addWidget(sortButton)
        dropdownBody.addWidget(exportButton)
        dropdownBody.addStretch()
        dropdownAreaLayout.addLayout(dropdownBody)
        centralLayout.addWidget(dropdownArea)

        # ElaEmojiPicker：popup(anchor) 会自动定位到触发控件附近。
        emojiPicker = ElaEmojiPicker(self)
        emojiPicker.setColumns(8)
        emojiPicker.setEmojiSize(24)
        emojiResult = ElaText("未选择表情", self)
        emojiPicker.emojiSelected.connect(emojiResult.setText)
        emojiTrigger = ElaPushButton("😀", self)
        emojiTrigger.setFixedSize(42, 36)
        emojiTrigger.clicked.connect(lambda: emojiPicker.popup(emojiTrigger))
        emojiArea = ElaScrollPageArea(self)
        emojiAreaLayout = QVBoxLayout(emojiArea)
        emojiAreaLayout.addWidget(ElaText("ElaEmojiPicker", 15, self))
        emojiAreaLayout.addWidget(_usageNote(
            "用法：popup 可以锚定 QWidget 或 QPoint。"
            "实现：网格按 Columns 和 EmojiSize 重绘，选中后通过 emojiSelected 返回字符。",
            self,
        ))
        emojiBody = QHBoxLayout()
        emojiBody.addWidget(emojiTrigger)
        emojiBody.addWidget(emojiResult)
        emojiBody.addStretch()
        emojiAreaLayout.addLayout(emojiBody)
        centralLayout.addWidget(emojiArea)

        # ElaExpander：头部承担展开动画，contentWidget 承载普通表单。
        expander = ElaExpander("网络设置", self)
        expander.setSubTitle("代理与网络参数")
        expander.setHeaderIcon(ElaIconType.IconName.WifiExclamation)
        expanderContent = QWidget(self)
        expanderContentLayout = QVBoxLayout(expanderContent)
        proxyCheckBox = ElaToggleSwitch(self)
        proxyRow = QHBoxLayout()
        proxyRow.addWidget(ElaText("启用代理", 13, self))
        proxyRow.addWidget(proxyCheckBox)
        proxyRow.addStretch()
        expanderContentLayout.addLayout(proxyRow)
        expander.setContentWidget(expanderContent)

        reverseExpander = ElaExpander("高级设置", self)
        reverseExpander.setExpandDirection(ElaExpander.ExpandDirection.Up)
        reverseExpander.setHeaderIcon(ElaIconType.IconName.GearComplex)
        reverseContent = QWidget(self)
        reverseContentLayout = QVBoxLayout(reverseContent)
        reverseContentLayout.addWidget(_usageNote("向上展开，适合靠近页面底部的高级区域。", self))
        reverseExpander.setContentWidget(reverseContent)
        expandArea = ElaScrollPageArea(self)
        expandAreaLayout = QVBoxLayout(expandArea)
        expandAreaLayout.addWidget(ElaText("ElaExpander", 15, self))
        expandAreaLayout.addWidget(_usageNote(
            "用法：先构建 contentWidget，再调用 setContentWidget。"
            "实现：点击 header 触发高度动画；ExpandDirection.Down/Up 决定伸展方向。",
            self,
        ))
        expandAreaLayout.addWidget(expander)
        expandAreaLayout.addWidget(reverseExpander)
        centralLayout.addWidget(expandArea)

        # ElaFloatButton：悬浮按钮通常挂在父窗口或父容器边角。
        floatButton = ElaFloatButton(ElaIconType.IconName.Plus, self)
        floatButton.setPosition(ElaFloatButton.Position.BottomRight)
        floatButton.setMargin(28)
        floatMenu = ElaMenu(self)
        floatMenu.addAction("新建笔记")
        floatMenu.addAction("上传文件")
        floatButton.setMenu(floatMenu)
        topLeftFloat = ElaPushButton("移到左上", self)
        bottomRightFloat = ElaPushButton("移到右下", self)
        topLeftFloat.clicked.connect(
            lambda: floatButton.setPosition(ElaFloatButton.Position.TopLeft)
        )
        bottomRightFloat.clicked.connect(
            lambda: floatButton.setPosition(ElaFloatButton.Position.BottomRight)
        )
        floatArea = ElaScrollPageArea(self)
        floatAreaLayout = QVBoxLayout(floatArea)
        floatArea.setFixedHeight(150)
        floatAreaLayout.addWidget(ElaText("ElaFloatButton", 15, self))
        floatAreaLayout.addWidget(_usageNote(
            "用法：Position 决定角点，Margin 决定到父容器的间距。"
            "实现：eventFilter 跟随父级 resize，可绑定菜单或直接发出 clicked。",
            self,
        ))
        floatBody = QHBoxLayout()
        floatBody.addWidget(topLeftFloat)
        floatBody.addWidget(bottomRightFloat)
        floatBody.addStretch()
        floatAreaLayout.addLayout(floatBody)
        centralLayout.addWidget(floatArea)

        # ElaPopconfirm：轻量确认气泡，比 Dialog 更适合删除类操作。
        deletePopconfirm = ElaPopconfirm(self)
        deletePopconfirm.setTitle("确认删除")
        deletePopconfirm.setContent("删除后将无法恢复，是否继续？")
        popResult = ElaText("等待选择", self)
        deletePopconfirm.confirmed.connect(lambda: popResult.setText("已确认删除"))
        deletePopconfirm.cancelled.connect(lambda: popResult.setText("已取消"))
        popTrigger = ElaPushButton("删除项目", self)
        popTrigger.clicked.connect(lambda: deletePopconfirm.showPopconfirm(popTrigger))
        commitPopconfirm = ElaPopconfirm(self)
        commitPopconfirm.setTitle("提交变更")
        commitPopconfirm.setContent("确定要提交到远程仓库吗？")
        commitPopconfirm.setConfirmButtonText("提交")
        commitPopconfirm.setCancelButtonText("再想想")
        commitPopconfirm.setIcon(ElaIconType.IconName.CloudArrowUp)
        commitTrigger = ElaPushButton("提交代码", self)
        commitTrigger.clicked.connect(lambda: commitPopconfirm.showPopconfirm(commitTrigger))
        confirmArea = ElaScrollPageArea(self)
        confirmAreaLayout = QVBoxLayout(confirmArea)
        confirmAreaLayout.addWidget(ElaText("ElaPopconfirm", 15, self))
        confirmAreaLayout.addWidget(_usageNote(
            "用法：showPopconfirm(target) 自动靠近目标控件。"
            "实现：confirmed/cancelled 分别对应确认和取消；Light Dismiss 关闭时不触发确认。",
            self,
        ))
        confirmBody = QHBoxLayout()
        confirmBody.addWidget(popTrigger)
        confirmBody.addWidget(popResult)
        confirmBody.addWidget(commitTrigger)
        confirmBody.addStretch()
        confirmAreaLayout.addLayout(confirmBody)
        centralLayout.addWidget(confirmArea)

        # ElaToast / ElaSnackbar：静态工厂负责创建、定位和自动销毁。
        toastButton = ElaPushButton("显示 Toast", self)
        snackbarButton = ElaPushButton("可撤销 Snackbar", self)
        snackbarResult = ElaText("等待用户操作", self)
        toastButton.clicked.connect(
            lambda: ElaToast.success("操作已完成", 1800, self.window())
        )
        snackbarButton.clicked.connect(
            lambda: self.showUndoSnackbar(snackbarResult)
        )
        feedbackArea = ElaScrollPageArea(self)
        feedbackAreaLayout = QVBoxLayout(feedbackArea)
        feedbackAreaLayout.addWidget(ElaText("ElaToast / ElaSnackbar", 15, self))
        feedbackAreaLayout.addWidget(_usageNote(
            "用法：Toast 是短暂提示；Snackbar 可附加动作按钮。"
            "实现：静态工厂负责创建、定位和自动销毁，actionClicked 用于撤销等业务回调。",
            self,
        ))
        feedbackBody = QHBoxLayout()
        feedbackBody.addWidget(toastButton)
        feedbackBody.addWidget(snackbarButton)
        feedbackBody.addWidget(snackbarResult)
        feedbackBody.addStretch()
        feedbackAreaLayout.addLayout(feedbackBody)
        centralLayout.addWidget(feedbackArea)

        # ElaTeachingTip：指向目标控件的引导气泡。
        teachingTip = ElaTeachingTip(self)
        teachingTip.setTitle("截图功能升级")
        teachingTip.setSubTitle("版本 2.0")
        teachingTip.setContent("现在支持区域截图、延时截图和 OCR 文字识别。")
        teachingTip.setTipIcon(ElaIconType.IconName.CameraRetro)
        teachingTip.setTailPosition(ElaTeachingTip.TailPosition.Bottom)
        teachingTip.setIsLightDismiss(True)
        tipTrigger = ElaPushButton("显示引导", self)
        tipTrigger.setFixedSize(150, 38)
        teachingTip.setTarget(tipTrigger)
        tipTrigger.clicked.connect(teachingTip.showTip)
        tipArea = ElaScrollPageArea(self)
        tipAreaLayout = QVBoxLayout(tipArea)
        tipAreaLayout.addWidget(ElaText("ElaTeachingTip", 15, self))
        tipAreaLayout.addWidget(_usageNote(
            "用法：先 setTarget，再 showTip；箭头方向由 TailPosition 控制。"
            "实现：Light Dismiss 时点击外部关闭，closeButtonClicked 可用于埋点。",
            self,
        ))
        tipBody = QHBoxLayout()
        tipBody.addWidget(tipTrigger)
        tipBody.addStretch()
        tipAreaLayout.addLayout(tipBody)
        centralLayout.addWidget(tipArea)

        # ElaDrawerArea：header 内嵌开关；展开状态双向同步给外部控件。
        drawerArea = ElaDrawerArea(self)
        drawerHeader = QWidget(self)
        drawerHeaderLayout = QHBoxLayout(drawerHeader)
        drawerHeaderLayout.addWidget(ElaText("通知抽屉", 14, self))
        drawerHeaderLayout.addStretch()
        drawerSwitch = ElaToggleSwitch(self)
        drawerState = ElaText("折叠", self)
        drawerHeaderLayout.addWidget(drawerState)
        drawerHeaderLayout.addWidget(drawerSwitch)

        def onDrawerToggled(expanded: bool):
            drawerState.setText("展开" if expanded else "折叠")
            if expanded:
                drawerArea.expand()
            else:
                drawerArea.collapse()

        drawerSwitch.toggled.connect(onDrawerToggled)
        drawerArea.expandStateChanged.connect(drawerSwitch.setIsToggled)
        drawerArea.setDrawerHeader(drawerHeader)
        firstDrawerItem = QWidget(self)
        firstItemLayout = QHBoxLayout(firstDrawerItem)
        firstItemLayout.addWidget(ElaText("安全警报", self))
        firstItemLayout.addStretch()
        secondDrawerItem = QWidget(self)
        secondItemLayout = QHBoxLayout(secondDrawerItem)
        secondItemLayout.addWidget(ElaText("系统更新", self))
        secondItemLayout.addStretch()
        drawerArea.addDrawer(firstDrawerItem)
        drawerArea.addDrawer(secondDrawerItem)
        drawerContainer = ElaScrollPageArea(self)
        drawerContainerLayout = QVBoxLayout(drawerContainer)
        drawerContainerLayout.addWidget(ElaText("ElaDrawerArea", 15, self))
        drawerContainerLayout.addWidget(_usageNote(
            "用法：addDrawer 添加多条内容，expand/collapse 控制整体高度。"
            "实现：custom header 可以放任意 Widget；expandStateChanged 反向同步开关。",
            self,
        ))
        drawerContainerLayout.addWidget(drawerArea)
        centralLayout.addWidget(drawerContainer)

        centralLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)

    def showUndoSnackbar(self, resultText: ElaText):
        snackbar = ElaSnackbar.info(
            "已删除 3 个项目", "撤销", 5000, self.window()
        )
        snackbar.actionClicked.connect(
            lambda: (resultText.setText("已撤销删除操作"), snackbar.dismiss())
        )
