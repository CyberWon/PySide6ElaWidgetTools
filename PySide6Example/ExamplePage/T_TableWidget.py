from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon, QColor, QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QHeaderView,
    QTableWidgetItem,
)

from ElaWidgetTools import ElaTableWidget, ElaScrollBar, ElaText
from ExamplePage.T_BasePage import T_BasePage

_SONG_DATA = [
    ("夜航星(Night Voyager)", "不才/三体宇宙", "我的三体之章北海传", "05:03"),
    ("玫瑰少年", "五月天", "玫瑰少年", "03:55"),
    ("Collapsing World(Original Mix)", "Lightscape", "Collapsing World", "03:10"),
    ("RAIN MAN (雨人)", "AKIHIDE (佐藤彰秀)", "RAIN STORY", "05:37"),
    ("黑暗森林", "雲翼星辰", "黑暗森林", "05:47"),
    ("轻(我的三体第四季主题曲)", "刘雪茗", "我的三体第四季", "01:59"),
    ("STYX HELIX", "MYTH & ROID", "STYX HELIX", "04:51"),
    ("LAST STARDUST", "Aimer", "DAWN", "05:18"),
    ("Running In The Dark", "MONKEY MAJIK/塞壬唱片", "Running In The Dark", "03:40"),
]

_ICON_PATHS = [
    "Resource/Image/Model/NaightNavigationStar.jpg",
    "Resource/Image/Model/MaVieEnRose.jpg",
    "Resource/Image/Model/CollapsingWorld.jpg",
    "Resource/Image/Model/RainMan.jpg",
    "Resource/Image/Model/DarkForest.jpg",
    "Resource/Image/Model/Light.jpg",
    "Resource/Image/Model/STYXHELIX.jpg",
    "Resource/Image/Model/LASTSTARDUST.jpg",
    "Resource/Image/Model/RunningInTheDark.jpg",
]


class T_TableWidget(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaTableWidget")
        self.createCustomWidget("表格部件被放置于此，可在此界面体验其效果并按需添加进项目中")

        tableText = ElaText("ElaTableWidget", self)
        tableText.setTextPixelSize(18)

        self._tableWidget = ElaTableWidget(self)
        self._tableWidget.setFixedHeight(450)
        self._tableWidget.setColumnCount(5)
        self._tableWidget.setRowCount(9)
        self._tableWidget.setHorizontalHeaderLabels(["预览", "歌名", "歌手", "专辑", "时长"])

        header = self._tableWidget.horizontalHeader()
        headerFont = QFont(header.font())
        headerFont.setPixelSize(16)
        header.setFont(headerFont)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setMinimumSectionSize(60)

        vHeader = self._tableWidget.verticalHeader()
        vHeader.setHidden(True)
        vHeader.setMinimumSectionSize(46)

        self._tableWidget.setAlternatingRowColors(True)
        self._tableWidget.setSelectionBehavior(QHeaderView.SelectionBehavior.SelectRows)
        self._tableWidget.setIconSize(QSize(38, 38))

        for row in range(9):
            previewItem = QTableWidgetItem()
            pix = QPixmap(_ICON_PATHS[row])
            previewItem.setIcon(QIcon(pix.scaled(38, 38, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)))
            previewItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self._tableWidget.setItem(row, 0, previewItem)

            for col in range(4):
                item = QTableWidgetItem(_SONG_DATA[row][col])
                if col == 3:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self._tableWidget.setItem(row, col + 1, item)

            if row == 0:
                for col in range(5):
                    self._tableWidget.item(row, col).setBackground(QColor(255, 150, 150))
            elif row == 1:
                for col in range(5):
                    self._tableWidget.item(row, col).setBackground(QColor(150, 255, 150))
            elif row == 2:
                for col in range(5):
                    self._tableWidget.item(row, col).setForeground(QColor(50, 50, 255))

        self._tableWidget.tableWidgetShow.connect(self._setColumnWidths)

        floatScrollBar = ElaScrollBar(self._tableWidget.verticalScrollBar(), self._tableWidget)
        floatScrollBar.setIsAnimation(True)

        tableWidgetLayout = QHBoxLayout()
        tableWidgetLayout.setContentsMargins(0, 0, 10, 0)
        tableWidgetLayout.addWidget(self._tableWidget)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaTableWidget")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(tableText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(tableWidgetLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)

    def _setColumnWidths(self):
        self._tableWidget.setColumnWidth(0, 60)
        self._tableWidget.setColumnWidth(1, 205)
        self._tableWidget.setColumnWidth(2, 170)
        self._tableWidget.setColumnWidth(3, 150)
        self._tableWidget.setColumnWidth(4, 60)
