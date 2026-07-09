from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaChatBubble,
    ElaDashboardGauge,
    ElaScrollPageArea,
    ElaSlider,
    ElaTerminalWidget,
    ElaText,
)
from ExamplePage.T_BasePage import T_BasePage


class T_NewComponents2(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaNewComponents2")
        self.createCustomWidget("新增组件演示页面 II - ChatBubble / DashboardGauge / TerminalWidget")

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaNewComponents2")

        # ========== ElaChatBubble ==========
        chatTitle = ElaText("ElaChatBubble", self)
        chatTitle.setTextPixelSize(18)

        chatLeft = ElaChatBubble(self)
        chatLeft.setDirection(ElaChatBubble.BubbleDirection.Left)
        chatLeft.setSenderName("Alice")
        chatLeft.setMessageText("你好！最近在忙什么项目？听说你在做一个新的组件库？")
        chatLeft.setTimestamp("10:30")
        chatLeft.setMinimumWidth(500)

        chatRight = ElaChatBubble(self)
        chatRight.setDirection(ElaChatBubble.BubbleDirection.Right)
        chatRight.setSenderName("Bob")
        chatRight.setMessageText("是的，我在开发 ElaWidgetTools 的新组件，包括聊天气泡、仪表盘和终端模拟器！")
        chatRight.setTimestamp("10:31")
        chatRight.setStatus(ElaChatBubble.MessageStatus.Read)
        chatRight.setMinimumWidth(500)

        chatSystem = ElaChatBubble(self)
        chatSystem.setDirection(ElaChatBubble.BubbleDirection.Left)
        chatSystem.setMessageText("这个组件支持左右对齐、头像、时间戳、发送状态等功能。")
        chatSystem.setTimestamp("10:32")
        chatSystem.setStatus(ElaChatBubble.MessageStatus.Sending)
        chatSystem.setMinimumWidth(500)

        chatImage = ElaChatBubble(self)
        chatImage.setDirection(ElaChatBubble.BubbleDirection.Right)
        chatImage.setSenderName("Bob")
        chatImage.setMessageImage(QPixmap("Resource/Image/Cirno.jpg"))
        chatImage.setMessageText("看看这张图片！")
        chatImage.setTimestamp("10:33")
        chatImage.setStatus(ElaChatBubble.MessageStatus.Sent)
        chatImage.setMinimumWidth(500)

        chatLayout = QVBoxLayout()
        chatLayout.setSpacing(4)
        chatLayout.addWidget(chatLeft)
        chatLayout.addWidget(chatRight)
        chatLayout.addWidget(chatSystem)
        chatLayout.addWidget(chatImage)

        chatArea = ElaScrollPageArea(self)
        chatArea.setFixedHeight(700)
        chatAreaLayout = QVBoxLayout(chatArea)
        chatAreaLayout.addWidget(chatTitle)
        chatAreaLayout.addLayout(chatLayout)

        # ========== ElaDashboardGauge ==========
        gaugeTitle = ElaText("ElaDashboardGauge", self)
        gaugeTitle.setTextPixelSize(18)

        self._gauge = ElaDashboardGauge(self)
        self._gauge.setMinimum(0)
        self._gauge.setMaximum(200)
        self._gauge.setValue(80)
        self._gauge.setTitle("速度")
        self._gauge.setUnit("km/h")
        self._gauge.setValuePixelSize(16)
        self._gauge.setTickWarningPercent(0.7)
        self._gauge.setDecimals(2)

        gaugeSmall = ElaDashboardGauge(self)
        gaugeSmall.setFixedSize(180, 180)
        gaugeSmall.setMinimum(0)
        gaugeSmall.setMaximum(100)
        gaugeSmall.setValue(50)
        gaugeSmall.setTitle("CPU")
        gaugeSmall.setUnit("%")
        gaugeSmall.setValuePixelSize(24)
        gaugeSmall.setTickWarningPercent(0.6)
        gaugeSmall.setDecimals(2)

        gaugeSlider = ElaSlider(self)
        gaugeSlider.setRange(int(self._gauge.getMinimum()), int(self._gauge.getMaximum()))
        gaugeSlider.setValue(72)
        gaugeSlider.setFixedWidth(260)
        gaugeValueLabel = ElaText("80", self)
        gaugeValueLabel.setTextPixelSize(12)

        def onGaugeChanged(v):
            self._gauge.setValue(v)
            gaugeValueLabel.setText(str(v))

        gaugeSlider.valueChanged.connect(onGaugeChanged)

        gaugeWidgetLayout = QHBoxLayout()
        gaugeWidgetLayout.addWidget(self._gauge)
        gaugeWidgetLayout.addSpacing(20)
        gaugeWidgetLayout.addWidget(gaugeSmall)
        gaugeWidgetLayout.addStretch()

        gaugeControlLayout = QHBoxLayout()
        ctlText = ElaText("值控制:", self)
        ctlText.setTextPixelSize(13)
        gaugeControlLayout.addWidget(ctlText)
        gaugeControlLayout.addWidget(gaugeSlider)
        gaugeControlLayout.addWidget(gaugeValueLabel)
        gaugeControlLayout.addStretch()

        gaugeArea = ElaScrollPageArea(self)
        gaugeArea.setFixedHeight(340)
        gaugeAreaLayout = QVBoxLayout(gaugeArea)
        gaugeAreaLayout.addWidget(gaugeTitle)
        gaugeAreaLayout.addLayout(gaugeWidgetLayout)
        gaugeAreaLayout.addLayout(gaugeControlLayout)

        # ========== ElaTerminalWidget ==========
        terminalTitle = ElaText("ElaTerminalWidget", self)
        terminalTitle.setTextPixelSize(18)

        self._terminal = ElaTerminalWidget(self)
        self._terminal.setFixedHeight(300)
        self._terminal.setPrompt("ela> ")
        self._terminal.appendSuccess("ElaTerminalWidget 已启动")
        self._terminal.appendOutput("输入 help 查看可用命令，输入 clear 清屏。")
        self._terminal.commandSubmitted.connect(self._onCommand)

        terminalArea = ElaScrollPageArea(self)
        terminalArea.setFixedHeight(360)
        terminalAreaLayout = QVBoxLayout(terminalArea)
        terminalAreaLayout.addWidget(terminalTitle)
        terminalAreaLayout.addWidget(self._terminal)

        # ========== 布局 ==========
        c = QVBoxLayout(centralWidget)
        c.setContentsMargins(0, 0, 0, 0)
        c.addWidget(chatArea)
        c.addWidget(gaugeArea)
        c.addWidget(terminalArea)
        self.addCentralWidget(centralWidget, True, False, 0)

    def _onCommand(self, cmd):
        t = self._terminal
        if cmd == "help":
            t.appendOutput("可用命令: help, clear, version, echo <text>, gauge <value>")
        elif cmd == "clear":
            t.clear()
        elif cmd == "version":
            t.appendOutput("ElaWidgetTools PySide6 Example")
        elif cmd.startswith("echo "):
            t.appendOutput(cmd[5:])
        elif cmd.startswith("gauge "):
            try:
                val = float(cmd[6:])
            except ValueError:
                t.appendError("无效数值")
                return
            lo = self._gauge.getMinimum()
            hi = self._gauge.getMaximum()
            clamped = max(lo, min(hi, val))
            self._gauge.setValue(clamped)
            if val < lo:
                t.appendOutput(f"值 {val} 低于最小值，已设置为 {clamped}", QColor(0xF7, 0x94, 0x0B))
            elif val > hi:
                t.appendOutput(f"值 {val} 超过最大值，已设置为 {clamped}", QColor(0xF7, 0x94, 0x0B))
            else:
                t.appendSuccess(f"仪表盘值已设置为 {clamped}")
        else:
            t.appendError(f"未知命令: {cmd}")
