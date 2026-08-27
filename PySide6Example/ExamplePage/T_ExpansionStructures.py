from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

import ElaWidgetTools
from ElaWidgetTools import (
    ElaCommandBar,
    ElaIconType,
    ElaInfoBar,
    ElaNotificationCenter,
    ElaPushButton,
    ElaScrollPageArea,
    ElaText,
    ElaTimeline,
    ElaWizard,
)
from ExamplePage.T_BasePage import T_BasePage


def _usageNote(text: str, parent: QWidget) -> ElaText:
    note = ElaText(text, 12, parent)
    note.setWordWrap(True)
    return note


class T_ExpansionStructures(T_BasePage):
    """结构体参数类组件与向导组件示例。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaExpansionStructures")
        self.createCustomWidget("Structured API and wizard examples")

        centralWidget = QWidget(self)
        centralLayout = QVBoxLayout(centralWidget)
        centralLayout.setContentsMargins(0, 0, 0, 0)
        centralLayout.setSpacing(10)

        # ElaCommandBar：CommandItem 是 icon/text/separator 的值类型。
        commandBar = ElaCommandBar(self)
        commandBar.setButtonSize(34)
        commandResult = ElaText("等待命令", self)
        if hasattr(commandBar, "addItem"):
            saveCommand = ElaCommandBar.CommandItem()
            saveCommand.icon = ElaIconType.IconName.FloppyDisk
            saveCommand.text = "保存"
            commandBar.addItem(saveCommand)

            downloadCommand = ElaCommandBar.CommandItem()
            downloadCommand.icon = ElaIconType.IconName.Download
            downloadCommand.text = "下载"
            commandBar.addItem(downloadCommand)
        else:
            commandResult.setText("当前绑定不含 addItem，需重新生成扩展")

        commandArea = ElaScrollPageArea(self)
        commandLayout = QVBoxLayout(commandArea)
        commandHeader = QHBoxLayout()
        commandHeader.addWidget(ElaText("ElaCommandBar", 15, self))
        commandHeader.addWidget(commandResult)
        commandHeader.addStretch()
        commandLayout.addLayout(commandHeader)
        commandLayout.addWidget(_usageNote(
            "用法：CommandItem 声明图标、文本和是否分隔符；addItem 按顺序加入命令栏。"
            "实现：itemClicked(index) 统一响应；新旧绑定兼容时才显示实际命令。",
            self,
        ))
        commandLayout.addWidget(commandBar)
        commandBar.itemClicked.connect(
            lambda index: commandResult.setText(
                f"已触发命令 {index}" if hasattr(commandBar, "addItem") else "当前绑定不含 addItem"
            )
        )
        centralLayout.addWidget(commandArea)

        # ElaInfoBar：严重等级通过 Q_PROPERTY 写入，便于保留 C++ 枚举接口。
        infoBar = ElaInfoBar(self)
        try:
            successSeverity = ElaWidgetTools.ElaInfoBarType.InfoBarSeverity.Success
        except AttributeError:
            successSeverity = 1
        infoBar.setProperty("pSeverity", successSeverity)
        infoBar.setTitle("构建完成")
        infoBar.setMessage("嵌套 value-type 已加入绑定生成流程。")
        infoBar.setIsClosable(True)
        infoArea = ElaScrollPageArea(self)
        infoLayout = QVBoxLayout(infoArea)
        infoHeader = QHBoxLayout()
        infoHeader.addWidget(ElaText("ElaInfoBar", 15, self))
        infoHeader.addStretch()
        infoLayout.addLayout(infoHeader)
        infoLayout.addWidget(_usageNote(
            "用法：setTitle/setMessage 之后，可用 setProperty 更新 pSeverity。"
            "实现：paintEvent 根据 severity 选择图标与配色；closed 信号可用于移除列表项。",
            self,
        ))
        infoLayout.addWidget(infoBar)
        centralLayout.addWidget(infoArea)

        # ElaNotificationCenter：通知面板可显示内容，点击通知会返回 index。
        notificationCenter = ElaNotificationCenter(self)
        notificationCenter.setPanelWidth(320)
        notificationResult = ElaText("还没有通知", self)
        if hasattr(notificationCenter, "addNotification"):
            notification = ElaNotificationCenter.NotificationItem()
            notification.title = "绑定更新"
            notification.content = "Nested value type 已支持。"
            notification.timestamp = "刚刚"
            notification.icon = ElaIconType.IconName.CircleInfo
            notificationCenter.addNotification(notification)
            notificationResult.setText("已添加 1 条通知")
        else:
            notificationResult.setText("需要重编扩展后传入 NotificationItem")
        notificationArea = ElaScrollPageArea(self)
        notificationLayout = QVBoxLayout(notificationArea)
        notificationHeader = QHBoxLayout()
        notificationHeader.addWidget(ElaText("ElaNotificationCenter", 15, self))
        notificationHeader.addWidget(notificationResult)
        notificationHeader.addStretch()
        notificationLayout.addLayout(notificationHeader)
        notificationLayout.addWidget(_usageNote(
            "用法：NotificationItem 描述标题、正文、时间与图标，showPanel(anchor) 显示面板。"
            "实现：panelVisibilityChanged 同步入口状态；clearAll 会重建列表。",
            self,
        ))
        notificationLayout.addWidget(notificationCenter)
        showNotificationPanelButton = ElaPushButton("显示通知面板", self)
        showNotificationPanelButton.clicked.connect(
            lambda: notificationCenter.showPanel(showNotificationPanelButton)
        )
        notificationCenter.notificationClicked.connect(
            lambda index: notificationResult.setText(f"已打开通知 {index}")
        )
        centralLayout.addWidget(notificationArea)

        # ElaTimeline：TimelineItem 用于标题、正文、时间和图标。
        timeline = ElaTimeline(self)
        if hasattr(timeline, "addItem"):
            releaseStep = ElaTimeline.TimelineItem()
            releaseStep.title = "扩展生成"
            releaseStep.content = "结构体 wrapper 已纳入构建。"
            releaseStep.timestamp = "10:00"
            timeline.addItem(releaseStep)

            reviewStep = ElaTimeline.TimelineItem()
            reviewStep.title = "GUI 冒烟"
            reviewStep.content = "组件实例化与事件循环通过。"
            reviewStep.timestamp = "10:05"
            timeline.addItem(reviewStep)
        else:
            _usageNote("当前绑定暂不能 addItem；需要重编扩展。", self).show()
        timelineArea = ElaScrollPageArea(self)
        timelineLayout = QVBoxLayout(timelineArea)
        timelineHeader = QHBoxLayout()
        timelineHeader.addWidget(ElaText("ElaTimeline", 15, self))
        timelineHeader.addStretch()
        timelineLayout.addLayout(timelineHeader)
        timelineLayout.addWidget(_usageNote(
            "用法：TimelineItem 逐条加入，clearItems 清空后 getItemCount 归零。"
            "实现：paintEvent 根据图标/颜色绘制圆点和连线。",
            self,
        ))
        timelineLayout.addWidget(timeline)
        centralLayout.addWidget(timelineArea)

        # ElaWizard：addStep 接收普通 QWidget，前后按钮只切换当前步骤。
        wizard = ElaWizard(self)
        basicStep = QWidget(self)
        basicLayout = QVBoxLayout(basicStep)
        basicLayout.addWidget(ElaText("选择组件版本", 16, basicStep))
        detailStep = QWidget(self)
        detailLayout = QVBoxLayout(detailStep)
        detailLayout.addWidget(ElaText("检查生成配置", 16, detailStep))
        finishStep = QWidget(self)
        finishLayout = QVBoxLayout(finishStep)
        finishLayout.addWidget(ElaText("完成并运行冒烟", 16, finishStep))
        wizard.addStep("Basic", basicStep)
        wizard.addStep("Detail", detailStep)
        wizard.addStep("Finish", finishStep)

        wizardStatus = ElaText(f"步骤 1 / {wizard.getStepCount()}", self)
        previousButton = ElaPushButton("上一步", self)
        nextButton = ElaPushButton("下一步", self)
        previousButton.clicked.connect(
            lambda: (wizard.previous(), wizardStatus.setText(
                f"步骤 {wizard.getCurrentStep() + 1} / {wizard.getStepCount()}"
            ))
        )
        nextButton.clicked.connect(
            lambda: (wizard.next(), wizardStatus.setText(
                f"步骤 {wizard.getCurrentStep() + 1} / {wizard.getStepCount()}"
            ))
        )
        wizardArea = ElaScrollPageArea(self)
        wizardLayout = QVBoxLayout(wizardArea)
        wizardHeader = QHBoxLayout()
        wizardHeader.addWidget(ElaText("ElaWizard", 15, self))
        wizardHeader.addWidget(wizardStatus)
        wizardHeader.addWidget(previousButton)
        wizardHeader.addWidget(nextButton)
        wizardHeader.addStretch()
        wizardLayout.addLayout(wizardHeader)
        wizardLayout.addWidget(_usageNote(
            "用法：每个 addStep 是独立 QWidget；getCurrentStep 从 0 开始。"
            "实现：next/previous 更新内部索引，finish 时可把 collected data 上报。",
            self,
        ))
        wizardLayout.addWidget(wizard)
        centralLayout.addWidget(wizardArea)

        centralLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)
