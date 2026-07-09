from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QStyledItemDelegate, QStyle, QStyleOptionViewItem

from ElaWidgetTools import ElaTheme, ElaThemeType


class T_IconDelegate(QStyledItemDelegate):
    """图标单元格委托。对应 C++ T_IconDelegate。

    自绘 ElaAwesome 字体图标字符 + 图标名（支持按宽度折行 + 省略号）。
    文字颜色随主题切换（通过 ElaTheme.getThemeColor(BasicText)）。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._themeMode = ElaTheme.getInstance().getThemeMode()
        ElaTheme.getInstance().themeModeChanged.connect(self._onThemeChanged)

    def _onThemeChanged(self, themeMode):
        self._themeMode = themeMode

    def paint(self, painter, option, index):
        viewOption = QStyleOptionViewItem(option)
        self.initStyleOption(viewOption, index)
        # PySide6 中 QFlags.testFlag 在某些版本上不可用，改用按位与
        if bool(option.state & QStyle.StateFlag.State_HasFocus):
            viewOption.state &= ~QStyle.StateFlag.State_HasFocus
        super().paint(painter, viewOption, index)

        iconList = index.data(Qt.ItemDataRole.UserRole)
        if not iconList or len(iconList) != 2:
            return
        iconName, iconValue = iconList[0], iconList[1]
        textColor = ElaTheme.getInstance().getThemeColor(self._themeMode, ElaThemeType.ThemeColor.BasicText)

        painter.save()
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)

        # 图标字符
        painter.save()
        iconFont = QFont("ElaAwesome")
        iconFont.setPixelSize(22)
        painter.setFont(iconFont)
        painter.setPen(textColor)
        painter.drawText(
            option.rect.x() + option.rect.width() // 2 - 11,
            option.rect.y() + option.rect.height() // 2 - 11,
            iconValue,
        )
        painter.restore()

        # 图标名（按宽度折行 + 末尾省略）
        painter.setPen(textColor)
        titleFont = painter.font()
        titleFont.setPixelSize(13)
        painter.setFont(titleFont)
        fm = painter.fontMetrics()
        rowTextWidth = option.rect.width() * 0.8
        subTitleRow = int(fm.horizontalAdvance(iconName) / rowTextWidth)
        if subTitleRow > 0:
            subTitleText = iconName
            for i in range(subTitleRow + 1):
                text = fm.elidedText(subTitleText, Qt.TextElideMode.ElideRight, int(rowTextWidth))
                if text.endswith("…"):
                    text = text[:-1] + subTitleText[len(text) - 1:len(text)]
                subTitleText = subTitleText[len(text):]
                painter.drawText(
                    option.rect.x() + option.rect.width() // 2 - fm.horizontalAdvance(text) // 2,
                    option.rect.y() + option.rect.height() - 10 * (subTitleRow + 1 - i),
                    text,
                )
        else:
            painter.drawText(
                option.rect.x() + option.rect.width() // 2 - fm.horizontalAdvance(iconName) // 2,
                option.rect.y() + option.rect.height() - 20,
                iconName,
            )
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(100, 100)
