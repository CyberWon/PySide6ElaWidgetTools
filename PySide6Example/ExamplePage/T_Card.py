from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaLCDNumber,
    ElaPromotionCard,
    ElaPromotionView,
    ElaScrollPageArea,
    ElaText,
)
from ExamplePage.T_BasePage import T_BasePage


class T_Card(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaCard")
        self.createCustomWidget("A collection of card components")

        lcdNumber = ElaLCDNumber(self)
        lcdNumber.setIsUseAutoClock(True)
        lcdNumber.setIsTransparent(False)
        lcdNumber.setFixedHeight(100)

        # ElaPromotionCard 用法：先设置 CardPixmap，再设置多层标题；
        # promotionCardClicked 可直接接业务跳转。
        # 实现：paintEvent 按圆角裁剪图片，并用主题色绘制促销角标与文字层。
        promotionCard = ElaPromotionCard(self)
        cardPixmap = QPixmap(320, 180)
        cardPixmap.fill(QColor("#1F6FEB"))
        promotionCard.setFixedSize(600, 300)
        promotionCard.setCardPixmap(cardPixmap)
        promotionCard.setCardTitle("Promotion")
        promotionCard.setPromotionTitle("Feature")
        promotionCard.setTitle("ElaPromotionCard")
        promotionCard.setSubTitle("A compact banner for highlighted actions")

        # ElaPromotionView 用法：appendPromotionCard 依次加入卡片；
        # IsAutoScroll 让演示页轮播，鼠标滚轮也可切换到相邻卡片。
        # 实现：当前索引决定展开宽度，resizeEvent 会重新计算可见卡片几何。
        promotionView = ElaPromotionView(self)
        promotionColors = ["#0EA5E9", "#8B5CF6", "#10B981", "#F97316"]
        promotionTitles = ["Navigation", "Views", "Components", "Themes"]
        for index, (colorName, title) in enumerate(zip(promotionColors, promotionTitles)):
            viewCard = ElaPromotionCard(self)
            itemPixmap = QPixmap(280, 150)
            itemPixmap.fill(QColor(colorName))
            viewCard.setCardPixmap(itemPixmap)
            viewCard.setCardTitle(f"Item {index + 1}")
            viewCard.setPromotionTitle("Ela")
            viewCard.setTitle(title)
            viewCard.setSubTitle("Drag the mouse or scroll to switch")
            promotionView.appendPromotionCard(viewCard)
        promotionView.setIsAutoScroll(True)
        promotionView.setFixedHeight(240)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaCard")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.addWidget(ElaText("ElaLCDNumber", self))
        centerLayout.addWidget(lcdNumber)
        centerLayout.addWidget(ElaText("ElaPromotionCard", self))
        centerLayout.addWidget(promotionCard)
        centerLayout.addWidget(ElaText("ElaPromotionView", self))
        centerLayout.addWidget(promotionView)
        centerLayout.setContentsMargins(0, 0, 0, 0)
        self.addCentralWidget(centralWidget, True, True, 0)
