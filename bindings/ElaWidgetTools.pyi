# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
ElaWidgetTools, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `ElaWidgetTools`

import ElaWidgetTools
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import os
import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class ElaAcrylicUrlCard(PySide6.QtWidgets.QPushButton):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getBrushAlpha(self, /) -> int: ...
    def getCardPixMode(self, /) -> ElaWidgetTools.ElaCardPixType.PixMode: ...
    def getCardPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getCardPixmapBorderRadius(self, /) -> int: ...
    def getCardPixmapSize(self, /) -> PySide6.QtCore.QSize: ...
    def getMainOpacity(self, /) -> float: ...
    def getNoiseOpacity(self, /) -> float: ...
    def getSubTitle(self, /) -> str: ...
    def getSubTitlePixelSize(self, /) -> int: ...
    def getSubTitleSpacing(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def getTitlePixelSize(self, /) -> int: ...
    def getTitleSpacing(self, /) -> int: ...
    def getUrl(self, /) -> str: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pBrushAlphaChanged(self, /) -> None: ...
    def pCardPixModeChanged(self, /) -> None: ...
    def pCardPixmapBorderRadiusChanged(self, /) -> None: ...
    def pCardPixmapChanged(self, /) -> None: ...
    def pCardPixmapSizeChanged(self, /) -> None: ...
    def pMainOpacityChanged(self, /) -> None: ...
    def pNoiseOpacityChanged(self, /) -> None: ...
    def pSubTitleChanged(self, /) -> None: ...
    def pSubTitlePixelSizeChanged(self, /) -> None: ...
    def pSubTitleSpacingChanged(self, /) -> None: ...
    def pTitleChanged(self, /) -> None: ...
    def pTitlePixelSizeChanged(self, /) -> None: ...
    def pTitleSpacingChanged(self, /) -> None: ...
    def pUrlChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setBrushAlpha(self, BrushAlpha: int, /) -> None: ...
    def setCardPixMode(self, CardPixMode: ElaWidgetTools.ElaCardPixType.PixMode, /) -> None: ...
    def setCardPixmap(self, CardPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setCardPixmapBorderRadius(self, CardPixmapBorderRadius: int, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, CardPixmapSize: PySide6.QtCore.QSize, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, width: int, height: int, /) -> None: ...
    def setMainOpacity(self, MainOpacity: float, /) -> None: ...
    def setNoiseOpacity(self, NoiseOpacity: float, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setSubTitlePixelSize(self, SubTitlePixelSize: int, /) -> None: ...
    def setSubTitleSpacing(self, SubTitleSpacing: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTitlePixelSize(self, TitlePixelSize: int, /) -> None: ...
    def setTitleSpacing(self, TitleSpacing: int, /) -> None: ...
    def setUrl(self, Url: str, /) -> None: ...


class ElaAppBar(PySide6.QtWidgets.QWidget):

    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    customMenuChanged        : typing.ClassVar[Signal] = ... # customMenuChanged()
    customWidgetChanged      : typing.ClassVar[Signal] = ... # customWidgetChanged()
    navigationButtonClicked  : typing.ClassVar[Signal] = ... # navigationButtonClicked()
    pAppBarHeightChanged     : typing.ClassVar[Signal] = ... # pAppBarHeightChanged()
    pAppBarVisibleChanged    : typing.ClassVar[Signal] = ... # pAppBarVisibleChanged()
    pIsDefaultClosedChanged  : typing.ClassVar[Signal] = ... # pIsDefaultClosedChanged()
    pIsFixedSizeChanged      : typing.ClassVar[Signal] = ... # pIsFixedSizeChanged()
    pIsOnlyAllowMinAndCloseChanged: typing.ClassVar[Signal] = ... # pIsOnlyAllowMinAndCloseChanged()
    pIsStayTopChanged        : typing.ClassVar[Signal] = ... # pIsStayTopChanged()
    routeBackButtonClicked   : typing.ClassVar[Signal] = ... # routeBackButtonClicked()
    routeForwardButtonClicked: typing.ClassVar[Signal] = ... # routeForwardButtonClicked()
    themeChangeButtonClicked : typing.ClassVar[Signal] = ... # themeChangeButtonClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def eventFilter(self, obj: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getAppBarHeight(self, /) -> int: ...
    def getAppBarVisible(self, /) -> bool: ...
    def getCustomMenu(self, /) -> PySide6.QtWidgets.QMenu: ...
    def getCustomWidget(self, customArea: ElaWidgetTools.ElaAppBarType.CustomArea, /) -> PySide6.QtWidgets.QWidget: ...
    def getIsDefaultClosed(self, /) -> bool: ...
    def getIsFixedSize(self, /) -> bool: ...
    def getIsOnlyAllowMinAndClose(self, /) -> bool: ...
    def getIsStayTop(self, /) -> bool: ...
    def getWindowButtonFlags(self, /) -> ElaWidgetTools.ElaAppBarType.ButtonType: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def setAppBarHeight(self, AppBarHeight: int, /) -> None: ...
    def setAppBarVisible(self, AppBarVisible: bool, /) -> None: ...
    def setCustomMenu(self, customMenu: PySide6.QtWidgets.QMenu, /) -> None: ...
    def setCustomWidget(self, customArea: ElaWidgetTools.ElaAppBarType.CustomArea, customWidget: PySide6.QtWidgets.QWidget, /, hitTestObject: PySide6.QtCore.QObject | None = ..., hitTestFunctionName: str = ...) -> None: ...
    def setIsDefaultClosed(self, IsDefaultClosed: bool, /) -> None: ...
    def setIsFixedSize(self, IsFixedSize: bool, /) -> None: ...
    def setIsOnlyAllowMinAndClose(self, IsOnlyAllowMinAndClose: bool, /) -> None: ...
    def setIsStayTop(self, IsStayTop: bool, /) -> None: ...
    def setRouteBackButtonEnable(self, isEnable: bool, /) -> None: ...
    def setRouteForwardButtonEnable(self, isEnable: bool, /) -> None: ...
    def setWindowButtonFlag(self, buttonFlag: ElaWidgetTools.ElaAppBarType.ButtonType, /, isEnable: bool = ...) -> None: ...
    def setWindowButtonFlags(self, buttonFlags: ElaWidgetTools.ElaAppBarType.ButtonType, /) -> None: ...


class ElaAppBarType(Shiboken.Object):

    class ButtonType(enum.IntFlag):

        NoneButtonHint            = 0x0
        RouteBackButtonHint       = 0x1
        RouteForwardButtonHint    = 0x2
        NavigationButtonHint      = 0x4
        StayTopButtonHint         = 0x8
        ThemeChangeButtonHint     = 0x10
        MinimizeButtonHint        = 0x20
        MaximizeButtonHint        = 0x40
        CloseButtonHint           = 0x80

    class CustomArea(enum.IntEnum):

        LeftArea                  = 0x1
        MiddleArea                = 0x2
        RightArea                 = 0x3

    class WMMouseActionType(enum.IntFlag):

        WMLBUTTONDOWN             = 0x1
        WMLBUTTONUP               = 0x2
        WMLBUTTONDBLCLK           = 0x4
        WMNCLBUTTONDOWN           = 0x8


class ElaApplication(PySide6.QtCore.QObject):
    @staticmethod
    def containsCursorToItem(item: PySide6.QtWidgets.QWidget, /) -> bool: ...
    def getElaMicaImagePath(self, /) -> str: ...
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaApplication: ...
    def getWindowDisplayMode(self, /) -> ElaWidgetTools.ElaApplicationType.WindowDisplayMode: ...
    def init(self, /) -> None: ...
    def pElaMicaImagePathChanged(self, /) -> None: ...
    def pWindowDisplayModeChanged(self, /) -> None: ...
    def setElaMicaImagePath(self, ElaMicaImagePath: str, /) -> None: ...
    def setWindowDisplayMode(self, WindowDisplayMode: ElaWidgetTools.ElaApplicationType.WindowDisplayMode, /) -> None: ...
    def syncWindowDisplayMode(self, widget: PySide6.QtWidgets.QWidget, /, isSync: bool = ...) -> None: ...


class ElaApplicationType(Shiboken.Object):

    class WindowDisplayMode(enum.IntEnum):

        Normal                    = 0x0
        ElaMica                   = 0x1


class ElaAutoComplete(PySide6.QtWidgets.QWidget):

    completionSelected       : typing.ClassVar[Signal] = ... # completionSelected(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCaseSensitivityChanged  : typing.ClassVar[Signal] = ... # pCaseSensitivityChanged()
    pMaxVisibleItemsChanged  : typing.ClassVar[Signal] = ... # pMaxVisibleItemsChanged()
    returnPressed            : typing.ClassVar[Signal] = ... # returnPressed(QString)
    textChanged              : typing.ClassVar[Signal] = ... # textChanged(QString)
    textEdited               : typing.ClassVar[Signal] = ... # textEdited(QString)

    class MatchMode(enum.IntEnum):

        Contains                  = 0x0
        StartsWith                = 0x1
        EndsWith                  = 0x2
        RegExp                    = 0x3


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def completions(self, /) -> typing.List[str]: ...
    def getBorderRadius(self, /) -> int: ...
    def getCaseSensitivity(self, /) -> PySide6.QtCore.Qt.CaseSensitivity: ...
    def getMaxVisibleItems(self, /) -> int: ...
    def matchMode(self, /) -> ElaWidgetTools.ElaAutoComplete.MatchMode: ...
    def placeholderText(self, /) -> str: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCaseSensitivity(self, CaseSensitivity: PySide6.QtCore.Qt.CaseSensitivity, /) -> None: ...
    def setCompletions(self, completions: collections.abc.Sequence[str], /) -> None: ...
    def setFixedHeight(self, h: int, /) -> None: ...
    def setMatchMode(self, mode: ElaWidgetTools.ElaAutoComplete.MatchMode, /) -> None: ...
    def setMaxVisibleItems(self, MaxVisibleItems: int, /) -> None: ...
    def setPlaceholderText(self, placeholderText: str, /) -> None: ...
    def setText(self, text: str, /) -> None: ...
    def text(self, /) -> str: ...


class ElaBreadcrumbBar(PySide6.QtWidgets.QWidget):

    breadcrumbClicked        : typing.ClassVar[Signal] = ... # breadcrumbClicked(QString,QStringList)
    pIsAutoRemoveChanged     : typing.ClassVar[Signal] = ... # pIsAutoRemoveChanged()
    pTextPixelSizeChanged    : typing.ClassVar[Signal] = ... # pTextPixelSizeChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def appendBreadcrumb(self, breadcrumb: str, /) -> typing.List[str]: ...
    def getBreadcrumbList(self, /) -> typing.List[str]: ...
    def getBreadcrumbListCount(self, /) -> int: ...
    def getIsAutoRemove(self, /) -> bool: ...
    def getTextPixelSize(self, /) -> int: ...
    def removeBreadcrumb(self, breadcrumb: str, /) -> typing.List[str]: ...
    def setBreadcrumbList(self, breadcrumbList: collections.abc.Sequence[str], /) -> None: ...
    def setIsAutoRemove(self, IsAutoRemove: bool, /) -> None: ...
    def setTextPixelSize(self, TextPixelSize: int, /) -> None: ...


class ElaCalendar(PySide6.QtWidgets.QWidget):

    clicked                  : typing.ClassVar[Signal] = ... # clicked(QDate)
    pBorderRaiudsChanged     : typing.ClassVar[Signal] = ... # pBorderRaiudsChanged()
    pMaximumDateChanged      : typing.ClassVar[Signal] = ... # pMaximumDateChanged()
    pMinimumDateChanged      : typing.ClassVar[Signal] = ... # pMinimumDateChanged()
    pSelectedDateChanged     : typing.ClassVar[Signal] = ... # pSelectedDateChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRaiuds(self, /) -> int: ...
    def getMaximumDate(self, /) -> PySide6.QtCore.QDate: ...
    def getMinimumDate(self, /) -> PySide6.QtCore.QDate: ...
    def getSelectedDate(self, /) -> PySide6.QtCore.QDate: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRaiuds(self, BorderRaiuds: int, /) -> None: ...
    def setMaximumDate(self, MaximumDate: PySide6.QtCore.QDate, /) -> None: ...
    def setMinimumDate(self, MinimumDate: PySide6.QtCore.QDate, /) -> None: ...
    def setSelectedDate(self, SelectedDate: PySide6.QtCore.QDate, /) -> None: ...


class ElaCalendarPicker(PySide6.QtWidgets.QPushButton):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    selectedDateChanged      : typing.ClassVar[Signal] = ... # selectedDateChanged(QDate)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getSelectedDate(self, /) -> PySide6.QtCore.QDate: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setSelectedDate(self, SelectedDate: PySide6.QtCore.QDate, /) -> None: ...


class ElaCaptcha(PySide6.QtWidgets.QWidget):

    codeChanged              : typing.ClassVar[Signal] = ... # codeChanged(QString)
    codeCompleted            : typing.ClassVar[Signal] = ... # codeCompleted(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pBoxSizeChanged          : typing.ClassVar[Signal] = ... # pBoxSizeChanged()
    pBoxSpacingChanged       : typing.ClassVar[Signal] = ... # pBoxSpacingChanged()
    pCodeLengthChanged       : typing.ClassVar[Signal] = ... # pCodeLengthChanged()

    class InputMode(enum.IntEnum):

        DigitOnly                 = 0x0
        AlphaNumeric              = 0x1


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clear(self, /) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getBoxSize(self, /) -> int: ...
    def getBoxSpacing(self, /) -> int: ...
    def getCode(self, /) -> str: ...
    def getCodeLength(self, /) -> int: ...
    def getInputMode(self, /) -> ElaWidgetTools.ElaCaptcha.InputMode: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setBoxSize(self, BoxSize: int, /) -> None: ...
    def setBoxSpacing(self, BoxSpacing: int, /) -> None: ...
    def setCodeLength(self, CodeLength: int, /) -> None: ...
    def setInputMode(self, mode: ElaWidgetTools.ElaCaptcha.InputMode, /) -> None: ...


class ElaCardPixType(Shiboken.Object):

    class PixMode(enum.IntEnum):

        Default                   = 0x0
        RoundedRect               = 0x1
        Ellipse                   = 0x2


class ElaChatBubble(PySide6.QtWidgets.QWidget):

    imageDoubleClicked       : typing.ClassVar[Signal] = ... # imageDoubleClicked(QPixmap)
    pAvatarSizeChanged       : typing.ClassVar[Signal] = ... # pAvatarSizeChanged()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pMaxBubbleWidthChanged   : typing.ClassVar[Signal] = ... # pMaxBubbleWidthChanged()
    pMessageTextChanged      : typing.ClassVar[Signal] = ... # pMessageTextChanged()
    pSenderNameChanged       : typing.ClassVar[Signal] = ... # pSenderNameChanged()
    pTimestampChanged        : typing.ClassVar[Signal] = ... # pTimestampChanged()

    class BubbleDirection(enum.IntEnum):

        Left                      = 0x0
        Right                     = 0x1

    class MessageStatus(enum.IntEnum):

        None_                     = 0x0
        Sending                   = 0x1
        Sent                      = 0x2
        Read                      = 0x3
        Failed                    = 0x4


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getAvatar(self, /) -> PySide6.QtGui.QPixmap: ...
    def getAvatarSize(self, /) -> int: ...
    def getBorderRadius(self, /) -> int: ...
    def getBubbleColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDirection(self, /) -> ElaWidgetTools.ElaChatBubble.BubbleDirection: ...
    def getImageMaxWidth(self, /) -> int: ...
    def getMaxBubbleWidth(self, /) -> int: ...
    def getMessageImage(self, /) -> PySide6.QtGui.QPixmap: ...
    def getMessageText(self, /) -> str: ...
    def getSenderName(self, /) -> str: ...
    def getStatus(self, /) -> ElaWidgetTools.ElaChatBubble.MessageStatus: ...
    def getTimestamp(self, /) -> str: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAvatar(self, avatar: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setAvatarSize(self, AvatarSize: int, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setBubbleColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDirection(self, direction: ElaWidgetTools.ElaChatBubble.BubbleDirection, /) -> None: ...
    def setImageMaxWidth(self, width: int, /) -> None: ...
    def setMaxBubbleWidth(self, MaxBubbleWidth: int, /) -> None: ...
    def setMessageImage(self, image: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setMessageText(self, MessageText: str, /) -> None: ...
    def setSenderName(self, SenderName: str, /) -> None: ...
    def setStatus(self, status: ElaWidgetTools.ElaChatBubble.MessageStatus, /) -> None: ...
    def setTimestamp(self, Timestamp: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaCheckBox(PySide6.QtWidgets.QCheckBox):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...


class ElaCodeEditor(PySide6.QtWidgets.QWidget):

    class Language(enum.IntEnum):

        CPP                       = 0x0
        C                         = 0x1
        CSharp                    = 0x2
        Python                    = 0x3
        JavaScript                = 0x4
        Lua                       = 0x5
        Rust                      = 0x6
        PHP                       = 0x7


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getCode(self, /) -> str: ...
    def getIsReadOnly(self, /) -> bool: ...
    def getLanguage(self, /) -> ElaWidgetTools.ElaCodeEditor.Language: ...
    def getTabSize(self, /) -> int: ...
    def pCodeChanged(self, /) -> None: ...
    def pIsReadOnlyChanged(self, /) -> None: ...
    def pTabSizeChanged(self, /) -> None: ...
    def setCode(self, Code: str, /) -> None: ...
    def setIsReadOnly(self, IsReadOnly: bool, /) -> None: ...
    def setLanguage(self, lang: ElaWidgetTools.ElaCodeEditor.Language, /) -> None: ...
    def setTabSize(self, TabSize: int, /) -> None: ...


class ElaColorDialog(PySide6.QtWidgets.QDialog):

    colorSelected            : typing.ClassVar[Signal] = ... # colorSelected(QColor)
    pCurrentColorChanged     : typing.ClassVar[Signal] = ... # pCurrentColorChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getCurrentColor(self, /) -> PySide6.QtGui.QColor: ...
    def getCurrentColorRGB(self, /) -> str: ...
    def getCustomColor(self, index: int, /) -> PySide6.QtGui.QColor: ...
    def getCustomColorList(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setCurrentColor(self, CurrentColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...


class ElaComboBox(PySide6.QtWidgets.QComboBox):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def hidePopup(self, /) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setEditable(self, editable: bool, /) -> None: ...
    def showPopup(self, /) -> None: ...


class ElaCommandBar(PySide6.QtWidgets.QWidget):

    itemClicked              : typing.ClassVar[Signal] = ... # itemClicked(int)
    pButtonSizeChanged       : typing.ClassVar[Signal] = ... # pButtonSizeChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addSeparator(self, /) -> None: ...
    def clearItems(self, /) -> None: ...
    def getButtonSize(self, /) -> int: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setButtonSize(self, ButtonSize: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaContentDialog(PySide6.QtWidgets.QDialog):

    leftButtonClicked        : typing.ClassVar[Signal] = ... # leftButtonClicked()
    middleButtonClicked      : typing.ClassVar[Signal] = ... # middleButtonClicked()
    rightButtonClicked       : typing.ClassVar[Signal] = ... # rightButtonClicked()

    def __init__(self, parent: PySide6.QtWidgets.QWidget, /) -> None: ...

    def close(self, /) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def onLeftButtonClicked(self, /) -> None: ...
    def onMiddleButtonClicked(self, /) -> None: ...
    def onRightButtonClicked(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setCentralWidget(self, centralWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setLeftButtonText(self, text: str, /) -> None: ...
    def setLeftButtonVisible(self, visible: bool, /) -> None: ...
    def setMiddleButtonText(self, text: str, /) -> None: ...
    def setMiddleButtonVisible(self, visible: bool, /) -> None: ...
    def setRightButtonText(self, text: str, /) -> None: ...
    def setRightButtonVisible(self, visible: bool, /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...


class ElaCopyButton(PySide6.QtWidgets.QPushButton):

    copyCompleted            : typing.ClassVar[Signal] = ... # copyCompleted(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCopyTextChanged         : typing.ClassVar[Signal] = ... # pCopyTextChanged()
    pSuccessDurationChanged  : typing.ClassVar[Signal] = ... # pSuccessDurationChanged()
    pSuccessTextChanged      : typing.ClassVar[Signal] = ... # pSuccessTextChanged()

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCopyText(self, /) -> str: ...
    def getSuccessDuration(self, /) -> int: ...
    def getSuccessText(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCopyText(self, CopyText: str, /) -> None: ...
    def setElaIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setSuccessDuration(self, SuccessDuration: int, /) -> None: ...
    def setSuccessIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setSuccessText(self, SuccessText: str, /) -> None: ...
    def setText(self, text: str, /) -> None: ...


class ElaCountdown(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pDigitHeightChanged      : typing.ClassVar[Signal] = ... # pDigitHeightChanged()
    pDigitSpacingChanged     : typing.ClassVar[Signal] = ... # pDigitSpacingChanged()
    pDigitWidthChanged       : typing.ClassVar[Signal] = ... # pDigitWidthChanged()
    pFontPixelSizeChanged    : typing.ClassVar[Signal] = ... # pFontPixelSizeChanged()
    pIsShowDaysChanged       : typing.ClassVar[Signal] = ... # pIsShowDaysChanged()
    pIsShowHoursChanged      : typing.ClassVar[Signal] = ... # pIsShowHoursChanged()
    pIsShowMinutesChanged    : typing.ClassVar[Signal] = ... # pIsShowMinutesChanged()
    pIsShowSecondsChanged    : typing.ClassVar[Signal] = ... # pIsShowSecondsChanged()
    tick                     : typing.ClassVar[Signal] = ... # tick(qlonglong)
    timeout                  : typing.ClassVar[Signal] = ... # timeout()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getDigitHeight(self, /) -> int: ...
    def getDigitSpacing(self, /) -> int: ...
    def getDigitWidth(self, /) -> int: ...
    def getFontPixelSize(self, /) -> int: ...
    def getIsShowDays(self, /) -> bool: ...
    def getIsShowHours(self, /) -> bool: ...
    def getIsShowMinutes(self, /) -> bool: ...
    def getIsShowSeconds(self, /) -> bool: ...
    def getRemainingSeconds(self, /) -> int: ...
    def getTargetDateTime(self, /) -> PySide6.QtCore.QDateTime: ...
    def isRunning(self, /) -> bool: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def pause(self, /) -> None: ...
    def resume(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDigitHeight(self, DigitHeight: int, /) -> None: ...
    def setDigitSpacing(self, DigitSpacing: int, /) -> None: ...
    def setDigitWidth(self, DigitWidth: int, /) -> None: ...
    def setFontPixelSize(self, FontPixelSize: int, /) -> None: ...
    def setIsShowDays(self, IsShowDays: bool, /) -> None: ...
    def setIsShowHours(self, IsShowHours: bool, /) -> None: ...
    def setIsShowMinutes(self, IsShowMinutes: bool, /) -> None: ...
    def setIsShowSeconds(self, IsShowSeconds: bool, /) -> None: ...
    def setRemainingSeconds(self, seconds: int, /) -> None: ...
    def setTargetDateTime(self, dateTime: PySide6.QtCore.QDateTime, /) -> None: ...
    def start(self, /) -> None: ...
    def stop(self, /) -> None: ...


class ElaDashboardGauge(PySide6.QtWidgets.QWidget):

    pArcWidthChanged         : typing.ClassVar[Signal] = ... # pArcWidthChanged()
    pDecimalsChanged         : typing.ClassVar[Signal] = ... # pDecimalsChanged()
    pIsAnimatedChanged       : typing.ClassVar[Signal] = ... # pIsAnimatedChanged()
    pMajorTickCountChanged   : typing.ClassVar[Signal] = ... # pMajorTickCountChanged()
    pMaximumChanged          : typing.ClassVar[Signal] = ... # pMaximumChanged()
    pMinimumChanged          : typing.ClassVar[Signal] = ... # pMinimumChanged()
    pMinorTickCountChanged   : typing.ClassVar[Signal] = ... # pMinorTickCountChanged()
    pSpanAngleChanged        : typing.ClassVar[Signal] = ... # pSpanAngleChanged()
    pStartAngleChanged       : typing.ClassVar[Signal] = ... # pStartAngleChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()
    pUnitChanged             : typing.ClassVar[Signal] = ... # pUnitChanged()
    pValueChanged            : typing.ClassVar[Signal] = ... # pValueChanged()
    pValuePixelSizeChanged   : typing.ClassVar[Signal] = ... # pValuePixelSizeChanged()
    valueChanged             : typing.ClassVar[Signal] = ... # valueChanged(double)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getArcWidth(self, /) -> int: ...
    def getDangerPercent(self, /) -> float: ...
    def getDecimals(self, /) -> int: ...
    def getIsAnimated(self, /) -> bool: ...
    def getMajorTickCount(self, /) -> int: ...
    def getMaximum(self, /) -> float: ...
    def getMinimum(self, /) -> float: ...
    def getMinorTickCount(self, /) -> int: ...
    def getSpanAngle(self, /) -> int: ...
    def getStartAngle(self, /) -> int: ...
    def getTickWarningPercent(self, /) -> float: ...
    def getTitle(self, /) -> str: ...
    def getUnit(self, /) -> str: ...
    def getValue(self, /) -> float: ...
    def getValuePixelSize(self, /) -> int: ...
    def getWarningPercent(self, /) -> float: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setArcWidth(self, ArcWidth: int, /) -> None: ...
    def setDangerPercent(self, percent: float, /) -> None: ...
    def setDecimals(self, Decimals: int, /) -> None: ...
    def setIsAnimated(self, IsAnimated: bool, /) -> None: ...
    def setMajorTickCount(self, MajorTickCount: int, /) -> None: ...
    def setMaximum(self, Maximum: float, /) -> None: ...
    def setMinimum(self, Minimum: float, /) -> None: ...
    def setMinorTickCount(self, MinorTickCount: int, /) -> None: ...
    def setSpanAngle(self, SpanAngle: int, /) -> None: ...
    def setStartAngle(self, StartAngle: int, /) -> None: ...
    def setTickWarningPercent(self, percent: float, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setUnit(self, Unit: str, /) -> None: ...
    def setValue(self, Value: float, /) -> None: ...
    def setValuePixelSize(self, ValuePixelSize: int, /) -> None: ...
    def setWarningPercent(self, percent: float, /) -> None: ...


class ElaDialog(PySide6.QtWidgets.QDialog):

    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    navigationButtonClicked  : typing.ClassVar[Signal] = ... # navigationButtonClicked()
    pAppBarHeightChanged     : typing.ClassVar[Signal] = ... # pAppBarHeightChanged()
    pIsDefaultClosedChanged  : typing.ClassVar[Signal] = ... # pIsDefaultClosedChanged()
    pIsFixedSizeChanged      : typing.ClassVar[Signal] = ... # pIsFixedSizeChanged()
    pIsStayTopChanged        : typing.ClassVar[Signal] = ... # pIsStayTopChanged()
    routeBackButtonClicked   : typing.ClassVar[Signal] = ... # routeBackButtonClicked()
    themeChangeButtonClicked : typing.ClassVar[Signal] = ... # themeChangeButtonClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getAppBarHeight(self, /) -> int: ...
    def getIsDefaultClosed(self, /) -> bool: ...
    def getIsFixedSize(self, /) -> bool: ...
    def getIsStayTop(self, /) -> bool: ...
    def getWindowButtonFlags(self, /) -> ElaWidgetTools.ElaAppBarType.ButtonType: ...
    def moveToCenter(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAppBarHeight(self, AppBarHeight: int, /) -> None: ...
    def setIsDefaultClosed(self, IsDefaultClosed: bool, /) -> None: ...
    def setIsFixedSize(self, IsFixedSize: bool, /) -> None: ...
    def setIsStayTop(self, IsStayTop: bool, /) -> None: ...
    def setWindowButtonFlag(self, buttonFlag: ElaWidgetTools.ElaAppBarType.ButtonType, /, isEnable: bool = ...) -> None: ...
    def setWindowButtonFlags(self, buttonFlags: ElaWidgetTools.ElaAppBarType.ButtonType, /) -> None: ...


class ElaDivider(PySide6.QtWidgets.QWidget):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getContentPosition(self, /) -> int: ...
    def getOrientation(self, /) -> PySide6.QtCore.Qt.Orientation: ...
    def getText(self, /) -> str: ...
    def pContentPositionChanged(self, /) -> None: ...
    def pOrientationChanged(self, /) -> None: ...
    def pTextChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setContentPosition(self, ContentPosition: int, /) -> None: ...
    def setOrientation(self, Orientation: PySide6.QtCore.Qt.Orientation, /) -> None: ...
    def setText(self, Text: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaDockWidget(PySide6.QtWidgets.QDockWidget):

    @typing.overload
    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...


class ElaDoubleSpinBox(PySide6.QtWidgets.QDoubleSpinBox):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def getButtonMode(self, /) -> ElaWidgetTools.ElaSpinBoxType.ButtonMode: ...
    def pButtonModeChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setButtonMode(self, ButtonMode: ElaWidgetTools.ElaSpinBoxType.ButtonMode, /) -> None: ...


class ElaDrawerArea(PySide6.QtWidgets.QWidget):

    expandStateChanged       : typing.ClassVar[Signal] = ... # expandStateChanged(bool)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pHeaderHeightChanged     : typing.ClassVar[Signal] = ... # pHeaderHeightChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addDrawer(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def collapse(self, /) -> None: ...
    def expand(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getHeaderHeight(self, /) -> int: ...
    def getIsExpand(self, /) -> bool: ...
    def removeDrawer(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDrawerHeader(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setHeaderHeight(self, HeaderHeight: int, /) -> None: ...


class ElaDropDownButton(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getElaIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getMenu(self, /) -> ElaWidgetTools.ElaMenu: ...
    def getText(self, /) -> str: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pElaIconChanged(self, /) -> None: ...
    def pTextChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setElaIcon(self, ElaIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setMenu(self, menu: ElaWidgetTools.ElaMenu, /) -> None: ...
    def setText(self, Text: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaEmojiPicker(PySide6.QtWidgets.QWidget):

    emojiSelected            : typing.ClassVar[Signal] = ... # emojiSelected(QString)
    pColumnsChanged          : typing.ClassVar[Signal] = ... # pColumnsChanged()
    pEmojiSizeChanged        : typing.ClassVar[Signal] = ... # pEmojiSizeChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getColumns(self, /) -> int: ...
    def getEmojiSize(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    @typing.overload
    def popup(self, anchor: PySide6.QtWidgets.QWidget, /) -> None: ...
    @typing.overload
    def popup(self, pos: PySide6.QtCore.QPoint, /) -> None: ...
    def setColumns(self, Columns: int, /) -> None: ...
    def setEmojiSize(self, EmojiSize: int, /) -> None: ...


class ElaEvent(PySide6.QtCore.QObject):

    def __init__(self, eventName: str, functionName: str, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def getConnectionType(self, /) -> PySide6.QtCore.Qt.ConnectionType: ...
    def getEventName(self, /) -> str: ...
    def getFunctionName(self, /) -> str: ...
    def pConnectionTypeChanged(self, /) -> None: ...
    def pEventNameChanged(self, /) -> None: ...
    def pFunctionNameChanged(self, /) -> None: ...
    def registerAndInit(self, /) -> ElaWidgetTools.ElaEventBusType.EventBusReturnType: ...
    def setConnectionType(self, ConnectionType: PySide6.QtCore.Qt.ConnectionType, /) -> None: ...
    def setEventName(self, EventName: str, /) -> None: ...
    def setFunctionName(self, FunctionName: str, /) -> None: ...


class ElaEventBusType(Shiboken.Object):

    class EventBusReturnType(enum.IntEnum):

        Success                   = 0x0
        EventInvalid              = 0x1
        EventNameInvalid          = 0x2


class ElaExpander(PySide6.QtWidgets.QWidget):

    expandStateChanged       : typing.ClassVar[Signal] = ... # expandStateChanged(bool)
    pAnimationDurationChanged: typing.ClassVar[Signal] = ... # pAnimationDurationChanged()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pHeaderIconChanged       : typing.ClassVar[Signal] = ... # pHeaderIconChanged()
    pSubTitleChanged         : typing.ClassVar[Signal] = ... # pSubTitleChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    class ExpandDirection(enum.IntEnum):

        Down                      = 0x0
        Up                        = 0x1


    @typing.overload
    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getAnimationDuration(self, /) -> int: ...
    def getBorderRadius(self, /) -> int: ...
    def getContentWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getExpandDirection(self, /) -> ElaWidgetTools.ElaExpander.ExpandDirection: ...
    def getHeaderIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getIsExpanded(self, /) -> bool: ...
    def getSubTitle(self, /) -> str: ...
    def getTitle(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAnimationDuration(self, AnimationDuration: int, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setContentWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setExpandDirection(self, direction: ElaWidgetTools.ElaExpander.ExpandDirection, /) -> None: ...
    def setHeaderIcon(self, HeaderIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setHeaderWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setIsExpanded(self, expanded: bool, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...


class ElaFloatButton(PySide6.QtWidgets.QWidget):

    clicked                  : typing.ClassVar[Signal] = ... # clicked()
    pButtonSizeChanged       : typing.ClassVar[Signal] = ... # pButtonSizeChanged()
    pMarginChanged           : typing.ClassVar[Signal] = ... # pMarginChanged()

    class Position(enum.IntEnum):

        BottomRight               = 0x0
        BottomLeft                = 0x1
        TopRight                  = 0x2
        TopLeft                   = 0x3


    @typing.overload
    def __init__(self, icon: ElaWidgetTools.ElaIconType.IconName, position: ElaWidgetTools.ElaFloatButton.Position, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, icon: ElaWidgetTools.ElaIconType.IconName, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getButtonSize(self, /) -> int: ...
    def getIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getMargin(self, /) -> int: ...
    def getMenu(self, /) -> ElaWidgetTools.ElaMenu: ...
    def getPosition(self, /) -> ElaWidgetTools.ElaFloatButton.Position: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setButtonSize(self, ButtonSize: int, /) -> None: ...
    def setIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setMargin(self, Margin: int, /) -> None: ...
    def setMenu(self, menu: ElaWidgetTools.ElaMenu, /) -> None: ...
    def setPosition(self, position: ElaWidgetTools.ElaFloatButton.Position, /) -> None: ...


class ElaFlowLayout(PySide6.QtWidgets.QLayout):

    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget, /, margin: int = ..., hSpacing: int = ..., vSpacing: int = ...) -> None: ...
    @typing.overload
    def __init__(self, /, margin: int = ..., hSpacing: int = ..., vSpacing: int = ...) -> None: ...

    def addItem(self, item: PySide6.QtWidgets.QLayoutItem, /) -> None: ...
    def count(self, /) -> int: ...
    def expandingDirections(self, /) -> PySide6.QtCore.Qt.Orientation: ...
    def hasHeightForWidth(self, /) -> bool: ...
    def heightForWidth(self, arg__1: int, /) -> int: ...
    def horizontalSpacing(self, /) -> int: ...
    def itemAt(self, index: int, /) -> PySide6.QtWidgets.QLayoutItem: ...
    def minimumSize(self, /) -> PySide6.QtCore.QSize: ...
    def setGeometry(self, rect: PySide6.QtCore.QRect, /) -> None: ...
    def setIsAnimation(self, isAnimation: bool, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...
    def takeAt(self, index: int, /) -> PySide6.QtWidgets.QLayoutItem: ...
    def verticalSpacing(self, /) -> int: ...


class ElaFlyout(PySide6.QtWidgets.QWidget):

    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pContentChanged          : typing.ClassVar[Signal] = ... # pContentChanged()
    pIsLightDismissChanged   : typing.ClassVar[Signal] = ... # pIsLightDismissChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def closeFlyout(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getContent(self, /) -> str: ...
    def getIsLightDismiss(self, /) -> bool: ...
    def getTitle(self, /) -> str: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setContent(self, Content: str, /) -> None: ...
    def setContentWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setIsLightDismiss(self, IsLightDismiss: bool, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def showFlyout(self, target: PySide6.QtWidgets.QWidget, /) -> None: ...


class ElaGraphicsItem(PySide6.QtWidgets.QGraphicsObject):

    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int, /, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None: ...

    def boundingRect(self, /) -> PySide6.QtCore.QRectF: ...
    def getDataRoutes(self, /) -> typing.Dict[str, typing.Any]: ...
    def getHeight(self, /) -> int: ...
    def getItemImage(self, /) -> PySide6.QtGui.QImage: ...
    def getItemName(self, /) -> str: ...
    def getItemSelectedImage(self, /) -> PySide6.QtGui.QImage: ...
    def getItemUID(self, /) -> str: ...
    @typing.overload
    def getLinkPortState(self, /) -> typing.List[bool]: ...
    @typing.overload
    def getLinkPortState(self, portIndex: int, /) -> bool: ...
    def getMaxLinkPortCount(self, /) -> int: ...
    def getUnusedLinkPort(self, /) -> typing.List[int]: ...
    def getUnusedLinkPortCount(self, /) -> int: ...
    def getUsedLinkPort(self, /) -> typing.List[int]: ...
    def getUsedLinkPortCount(self, /) -> int: ...
    def getWidth(self, /) -> int: ...
    def pDataRoutesChanged(self, /) -> None: ...
    def pHeightChanged(self, /) -> None: ...
    def pItemImageChanged(self, /) -> None: ...
    def pItemNameChanged(self, /) -> None: ...
    def pItemSelectedImageChanged(self, /) -> None: ...
    def pMaxLinkPortCountChanged(self, /) -> None: ...
    def pWidthChanged(self, /) -> None: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, /, widget: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def setDataRoutes(self, DataRoutes: typing.Dict[str, typing.Any], /) -> None: ...
    def setHeight(self, Height: int, /) -> None: ...
    def setItemImage(self, ItemImage: PySide6.QtGui.QImage, /) -> None: ...
    def setItemName(self, ItemName: str, /) -> None: ...
    def setItemSelectedImage(self, ItemSelectedImage: PySide6.QtGui.QImage, /) -> None: ...
    @typing.overload
    def setLinkPortState(self, isFullLink: bool, /) -> None: ...
    @typing.overload
    def setLinkPortState(self, isLink: bool, portIndex: int, /) -> None: ...
    def setMaxLinkPortCount(self, MaxLinkPortCount: int, /) -> None: ...
    def setWidth(self, Width: int, /) -> None: ...


class ElaGraphicsLineItem(PySide6.QtWidgets.QGraphicsPathItem):

    @typing.overload
    def __init__(self, startItem: ElaWidgetTools.ElaGraphicsItem, endItem: ElaWidgetTools.ElaGraphicsItem, startItemPort: int, endItemPort: int, /, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None: ...
    @typing.overload
    def __init__(self, startPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, endPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /, parent: PySide6.QtWidgets.QGraphicsItem | None = ...) -> None: ...

    def boundingRect(self, /) -> PySide6.QtCore.QRectF: ...
    def getEndItem(self, /) -> ElaWidgetTools.ElaGraphicsItem: ...
    def getEndItemPort(self, /) -> int: ...
    def getEndPoint(self, /) -> PySide6.QtCore.QPointF: ...
    def getStartItem(self, /) -> ElaWidgetTools.ElaGraphicsItem: ...
    def getStartItemPort(self, /) -> int: ...
    def getStartPoint(self, /) -> PySide6.QtCore.QPointF: ...
    @typing.overload
    def isTargetLink(self, item: ElaWidgetTools.ElaGraphicsItem, /) -> bool: ...
    @typing.overload
    def isTargetLink(self, item1: ElaWidgetTools.ElaGraphicsItem, item2: ElaWidgetTools.ElaGraphicsItem, /) -> bool: ...
    @typing.overload
    def isTargetLink(self, item1: ElaWidgetTools.ElaGraphicsItem, item2: ElaWidgetTools.ElaGraphicsItem, port1: int, port2: int, /) -> bool: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, /, widget: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def setEndItem(self, EndItem: ElaWidgetTools.ElaGraphicsItem, /) -> None: ...
    def setEndItemPort(self, EndItemPort: int, /) -> None: ...
    def setEndPoint(self, EndPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    def setStartItem(self, StartItem: ElaWidgetTools.ElaGraphicsItem, /) -> None: ...
    def setStartItemPort(self, StartItemPort: int, /) -> None: ...
    def setStartPoint(self, StartPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...


class ElaGraphicsScene(PySide6.QtWidgets.QGraphicsScene):

    mouseDoubleClickedItem   : typing.ClassVar[Signal] = ... # mouseDoubleClickedItem(ElaGraphicsItem*)
    mouseLeftClickedItem     : typing.ClassVar[Signal] = ... # mouseLeftClickedItem(ElaGraphicsItem*)
    mouseRightClickedItem    : typing.ClassVar[Signal] = ... # mouseRightClickedItem(ElaGraphicsItem*)
    pIsCheckLinkPortChanged  : typing.ClassVar[Signal] = ... # pIsCheckLinkPortChanged()
    pSerializePathChanged    : typing.ClassVar[Signal] = ... # pSerializePathChanged()
    showItemLink             : typing.ClassVar[Signal] = ... # showItemLink()

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def addItem(self, item: ElaWidgetTools.ElaGraphicsItem, /) -> None: ...
    def addItemLink(self, item1: ElaWidgetTools.ElaGraphicsItem, item2: ElaWidgetTools.ElaGraphicsItem, /, port1: int | None = ..., port2: int | None = ...) -> bool: ...
    def clear(self, /) -> None: ...
    def createAndAddItem(self, width: int, height: int, /, count: int = ...) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    def deserialize(self, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    @typing.overload
    def getElaItems(self, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    @typing.overload
    def getElaItems(self, pos: PySide6.QtCore.QPoint, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    @typing.overload
    def getElaItems(self, rect: PySide6.QtCore.QRect, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    @typing.overload
    def getElaItems(self, rect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    @typing.overload
    def getElaItems(self, pos: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    def getIsCheckLinkPort(self, /) -> bool: ...
    def getItemLinkList(self, /) -> typing.List[typing.Dict[str, typing.Any]]: ...
    def getItemsDataRoute(self, /) -> typing.List[typing.Dict[str, typing.Any]]: ...
    def getSceneMode(self, /) -> ElaWidgetTools.ElaGraphicsSceneType.SceneMode: ...
    def getSelectedElaItems(self, /) -> typing.List[ElaWidgetTools.ElaGraphicsItem]: ...
    def getSerializePath(self, /) -> str: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent, /) -> None: ...
    def removeItem(self, item: ElaWidgetTools.ElaGraphicsItem, /) -> None: ...
    @typing.overload
    def removeItemLink(self, item1: ElaWidgetTools.ElaGraphicsItem, /) -> bool: ...
    @typing.overload
    def removeItemLink(self, item1: ElaWidgetTools.ElaGraphicsItem, item2: ElaWidgetTools.ElaGraphicsItem, /, port1: int | None = ..., port2: int | None = ...) -> bool: ...
    def removeSelectedItems(self, /) -> None: ...
    def selectAllItems(self, /) -> None: ...
    def serialize(self, /) -> None: ...
    def setIsCheckLinkPort(self, IsCheckLinkPort: bool, /) -> None: ...
    def setSceneMode(self, mode: ElaWidgetTools.ElaGraphicsSceneType.SceneMode, /) -> None: ...
    def setSerializePath(self, SerializePath: str, /) -> None: ...


class ElaGraphicsSceneType(Shiboken.Object):

    class SceneMode(enum.IntEnum):

        Default                   = 0x0
        DragMove                  = 0x1
        MultiSelect               = 0x2
        ItemLink                  = 0x3


class ElaGraphicsView(PySide6.QtWidgets.QGraphicsView):

    @typing.overload
    def __init__(self, scene: PySide6.QtWidgets.QGraphicsScene, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getMaxTransform(self, /) -> float: ...
    def getMinTransform(self, /) -> float: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def pMaxTransformChanged(self, /) -> None: ...
    def pMinTransformChanged(self, /) -> None: ...
    def setMaxTransform(self, MaxTransform: float, /) -> None: ...
    def setMinTransform(self, MinTransform: float, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaGroupBox(PySide6.QtWidgets.QGroupBox):

    @typing.overload
    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...


class ElaIconButton(PySide6.QtWidgets.QPushButton):

    @typing.overload
    def __init__(self, awesome: ElaWidgetTools.ElaIconType.IconName, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, awesome: ElaWidgetTools.ElaIconType.IconName, pixelSize: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, awesome: ElaWidgetTools.ElaIconType.IconName, pixelSize: int, fixedWidth: int, fixedHeight: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, pix: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getAwesome(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getBorderRadius(self, /) -> int: ...
    def getDarkHoverColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDarkHoverIconColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDarkIconColor(self, /) -> PySide6.QtGui.QColor: ...
    def getIsSelected(self, /) -> bool: ...
    def getLightHoverColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightHoverIconColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightIconColor(self, /) -> PySide6.QtGui.QColor: ...
    def getOpacity(self, /) -> float: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pDarkHoverColorChanged(self, /) -> None: ...
    def pDarkHoverIconColorChanged(self, /) -> None: ...
    def pDarkIconColorChanged(self, /) -> None: ...
    def pIsSelectedChanged(self, /) -> None: ...
    def pLightHoverColorChanged(self, /) -> None: ...
    def pLightHoverIconColorChanged(self, /) -> None: ...
    def pLightIconColorChanged(self, /) -> None: ...
    def pOpacityChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAwesome(self, awesome: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDarkHoverColor(self, DarkHoverColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDarkHoverIconColor(self, DarkHoverIconColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDarkIconColor(self, DarkIconColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setIsSelected(self, IsSelected: bool, /) -> None: ...
    def setLightHoverColor(self, LightHoverColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLightHoverIconColor(self, LightHoverIconColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLightIconColor(self, LightIconColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setOpacity(self, Opacity: float, /) -> None: ...
    def setPixmap(self, pix: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...


class ElaIconType(Shiboken.Object):

    class IconName(enum.IntEnum):

        None_                     = 0x0
        Broom                     = 0xe800
        Number00                  = 0xe801
        Numbe0                    = 0xe802
        Numbe1                    = 0xe803
        Numbe2                    = 0xe804
        Numbe3                    = 0xe805
        Numbe4                    = 0xe806
        Numbe5                    = 0xe807
        Numbe7                    = 0xe808
        Numbe6                    = 0xe809
        Numbe9                    = 0xe80a
        Numbe8                    = 0xe80b
        Degrees360                = 0xe80c
        A                         = 0xe80d
        Abacus                    = 0xe80e
        AccentGrave               = 0xe80f
        Acorn                     = 0xe810
        AddressBook               = 0xe811
        AddressCard               = 0xe812
        AirConditioner            = 0xe813
        Airplay                   = 0xe814
        AlarmClock                = 0xe815
        AlarmExclamation          = 0xe816
        AlarmPlus                 = 0xe817
        Album                     = 0xe818
        AlbumCirclePlus           = 0xe819
        AlbumCircleUser           = 0xe81a
        AlbumCollection           = 0xe81b
        AlbumCollectionCirclePlus = 0xe81c
        AlarmSnooze               = 0xe81d
        AlbumCollectionCircleUser = 0xe81e
        Alicorn                   = 0xe81f
        Alien8bit                 = 0xe820
        AlignCenter               = 0xe821
        AlignLeft                 = 0xe822
        AlignRight                = 0xe823
        Ampersand                 = 0xe824
        Alt                       = 0xe825
        AnchorCircleExclamation   = 0xe826
        AlignSlash                = 0xe827
        AmpGuitar                 = 0xe828
        AlignJustify              = 0xe829
        Anchor                    = 0xe82a
        AnchorLock                = 0xe82b
        Angle                     = 0xe82c
        AnchorCircleXmark         = 0xe82d
        Angel                     = 0xe82e
        Angle90                   = 0xe82f
        Alien                     = 0xe830
        AnchorCircleCheck         = 0xe831
        AngleDown                 = 0xe832
        AngleRight                = 0xe833
        AnglesLeft                = 0xe834
        AnglesDown                = 0xe835
        AnglesUp                  = 0xe836
        AnglesRight               = 0xe837
        AnglesUpDown              = 0xe838
        AngleUp                   = 0xe839
        Ankh                      = 0xe83a
        Apartment                 = 0xe83b
        Aperture                  = 0xe83c
        Apostrophe                = 0xe83d
        AppleCore                 = 0xe83e
        AngleLeft                 = 0xe83f
        AppleWhole                = 0xe840
        Archway                   = 0xe841
        ArrowDown                 = 0xe842
        ArrowDown19               = 0xe843
        ArrowDown91               = 0xe844
        ArrowDownArrowUp          = 0xe845
        ArrowDownAZ               = 0xe846
        ArrowDownBigSmall         = 0xe847
        ArrowDownFromArc          = 0xe848
        ArrowDownFromDottedLine   = 0xe849
        ArrowDownFromLine         = 0xe84a
        ArrowDownLeft             = 0xe84b
        ArrowDownLeftAndArrowUpRightToCenter = 0xe84c
        ArrowDownLong             = 0xe84d
        ArrowDownRight            = 0xe84e
        ArrowDownShortWide        = 0xe84f
        ArrowDownSquareTriangle   = 0xe850
        ArrowDownSmallBig         = 0xe851
        ArrowDownToArc            = 0xe852
        ArrowDownToBracket        = 0xe853
        ArrowDownToDottedLine     = 0xe854
        ArrowDownToLine           = 0xe855
        ArrowDownTriangleSquare   = 0xe856
        ArrowDownUpAcrossLine     = 0xe857
        ArrowDownUpLock           = 0xe858
        ArrowDownWideShort        = 0xe859
        ArrowDownZA               = 0xe85a
        ArrowLeft                 = 0xe85b
        ArrowLeftFromArc          = 0xe85c
        ArrowLeftFromLine         = 0xe85d
        ArrowLeftLong             = 0xe85e
        ArrowLeftLongToLine       = 0xe85f
        ArrowLeftToArc            = 0xe860
        ArrowPointer              = 0xe861
        ArrowDownToSquare         = 0xe862
        ArrowLeftToLine           = 0xe863
        ArrowProgress             = 0xe864
        ArrowRight                = 0xe865
        ArrowRightArrowLeft       = 0xe866
        ArrowRightFromArc         = 0xe867
        ArrowRightFromBracket     = 0xe868
        ArrowRightFromLine        = 0xe869
        ArrowRightLong            = 0xe86a
        ArrowRightLongToLine      = 0xe86b
        ArrowRightToArc           = 0xe86c
        ArrowRightToBracket       = 0xe86d
        ArrowRightToCity          = 0xe86e
        ArrowRightToLine          = 0xe86f
        ArrowRotateLeft           = 0xe870
        ArrowRotateRight          = 0xe871
        ArrowsCross               = 0xe872
        ArrowsDownToLine          = 0xe873
        ArrowsDownToPeople        = 0xe874
        ArrowsFromDottedLine      = 0xe875
        ArrowsFromLine            = 0xe876
        ArrowsLeftRight           = 0xe877
        ArrowsLeftRightToLine     = 0xe878
        ArrowsMaximize            = 0xe879
        ArrowsMinimize            = 0xe87a
        ArrowsRepeat              = 0xe87b
        ArrowsRepeat1             = 0xe87c
        ArrowsRetweet             = 0xe87d
        ArrowsRotate              = 0xe87e
        ArrowsRotateReverse       = 0xe87f
        ArrowsSpin                = 0xe880
        ArrowsSplitUpAndLeft      = 0xe881
        ArrowsToCircle            = 0xe882
        ArrowsToDot               = 0xe883
        ArrowsToDottedLine        = 0xe884
        ArrowsToEye               = 0xe885
        ArrowsToLine              = 0xe886
        ArrowsTurnRight           = 0xe887
        ArrowsTurnToDots          = 0xe888
        ArrowsUpDown              = 0xe889
        ArrowsUpDownLeftRight     = 0xe88a
        ArrowsUpToLine            = 0xe88b
        ArrowTrendDown            = 0xe88c
        ArrowTrendUp              = 0xe88d
        ArrowTurnDown             = 0xe88e
        ArrowTurnDownLeft         = 0xe88f
        ArrowTurnDownRight        = 0xe890
        ArrowTurnLeft             = 0xe891
        ArrowTurnLeftDown         = 0xe892
        ArrowTurnLeftUp           = 0xe893
        ArrowTurnRight            = 0xe894
        ArrowTurnUp               = 0xe895
        ArrowUp                   = 0xe896
        ArrowUp19                 = 0xe897
        ArrowUp91                 = 0xe898
        ArrowUpArrowDown          = 0xe899
        ArrowUpAZ                 = 0xe89a
        ArrowUpBigSmall           = 0xe89b
        ArrowUpFromArc            = 0xe89c
        ArrowUpFromBracket        = 0xe89d
        ArrowUpFromDottedLine     = 0xe89e
        ArrowUpFromGroundWater    = 0xe89f
        ArrowUpFromLine           = 0xe8a0
        ArrowUpFromSquare         = 0xe8a1
        ArrowUpFromWaterPump      = 0xe8a2
        ArrowUpLeft               = 0xe8a3
        ArrowUpLeftFromCircle     = 0xe8a4
        ArrowUpLong               = 0xe8a5
        ArrowUpRight              = 0xe8a6
        ArrowUpRightAndArrowDownLeftFromCenter = 0xe8a7
        ArrowUpRightDots          = 0xe8a8
        ArrowUpRightFromSquare    = 0xe8a9
        ArrowUpShortWide          = 0xe8aa
        ArrowUpSmallBig           = 0xe8ab
        ArrowUpSquareTriangle     = 0xe8ac
        ArrowUpToArc              = 0xe8ad
        ArrowUpToDottedLine       = 0xe8ae
        ArrowUpToLine             = 0xe8af
        ArrowUpTriangleSquare     = 0xe8b0
        ArrowUpWideShort          = 0xe8b1
        ArrowUpZA                 = 0xe8b2
        Asterisk                  = 0xe8b3
        At                        = 0xe8b4
        Atom                      = 0xe8b5
        AtomSimple                = 0xe8b6
        AudioDescription          = 0xe8b7
        AudioDescriptionSlash     = 0xe8b8
        AustralSign               = 0xe8b9
        Avocado                   = 0xe8ba
        Award                     = 0xe8bb
        AwardSimple               = 0xe8bc
        Axe                       = 0xe8bd
        AxeBattle                 = 0xe8be
        B                         = 0xe8bf
        Baby                      = 0xe8c0
        BabyCarriage              = 0xe8c1
        Backpack                  = 0xe8c2
        Backward                  = 0xe8c3
        BackwardFast              = 0xe8c4
        BackwardStep              = 0xe8c5
        Bacon                     = 0xe8c6
        Bacteria                  = 0xe8c7
        Badge                     = 0xe8c8
        Bacterium                 = 0xe8c9
        BadgeCheck                = 0xe8ca
        BadgeDollar               = 0xe8cb
        BadgePercent              = 0xe8cc
        BadgerHoney               = 0xe8cd
        BadgeSheriff              = 0xe8ce
        Badminton                 = 0xe8cf
        Bagel                     = 0xe8d0
        BagSeedling               = 0xe8d1
        BagShopping               = 0xe8d2
        BagShoppingMinus          = 0xe8d3
        BagShoppingPlus           = 0xe8d4
        BagsShopping              = 0xe8d5
        Baguette                  = 0xe8d6
        Bahai                     = 0xe8d7
        BahtSign                  = 0xe8d8
        Balloon                   = 0xe8d9
        Balloons                  = 0xe8da
        Ballot                    = 0xe8db
        BallotCheck               = 0xe8dc
        BallPile                  = 0xe8dd
        Ban                       = 0xe8de
        Banana                    = 0xe8df
        BanBug                    = 0xe8e0
        Bandage                   = 0xe8e1
        BangladeshiTakaSign       = 0xe8e2
        Banjo                     = 0xe8e3
        BanParking                = 0xe8e4
        BanSmoking                = 0xe8e5
        Barcode                   = 0xe8e6
        BarcodeRead               = 0xe8e7
        BarcodeScan               = 0xe8e8
        Bars                      = 0xe8e9
        BarsFilter                = 0xe8ea
        BarsProgress              = 0xe8eb
        BarsSort                  = 0xe8ec
        BarsStaggered             = 0xe8ed
        Baseball                  = 0xe8ee
        BaseballBatBall           = 0xe8ef
        Basketball                = 0xe8f0
        BasketballHoop            = 0xe8f1
        BasketShopping            = 0xe8f2
        BasketShoppingMinus       = 0xe8f3
        BasketShoppingPlus        = 0xe8f4
        BasketShoppingSimple      = 0xe8f5
        Bat                       = 0xe8f6
        Bath                      = 0xe8f7
        BatteryBolt               = 0xe8f8
        BatteryEmpty              = 0xe8f9
        BatteryExclamation        = 0xe8fa
        BatteryFull               = 0xe8fb
        BatteryHalf               = 0xe8fc
        BatteryLow                = 0xe8fd
        BatteryQuarter            = 0xe8fe
        BatterySlash              = 0xe8ff
        BatteryThreeQuarters      = 0xe900
        Bed                       = 0xe901
        BedBunk                   = 0xe902
        BedEmpty                  = 0xe903
        BedFront                  = 0xe904
        BedPulse                  = 0xe905
        Bee                       = 0xe906
        BeerMug                   = 0xe907
        BeerMugEmpty              = 0xe908
        Bell                      = 0xe909
        BellConcierge             = 0xe90a
        BellExclamation           = 0xe90b
        BellOn                    = 0xe90c
        BellPlus                  = 0xe90d
        BellRing                  = 0xe90e
        Bells                     = 0xe90f
        BellSchool                = 0xe910
        BellSchoolSlash           = 0xe911
        BellSlash                 = 0xe912
        BenchTree                 = 0xe913
        BezierCurve               = 0xe914
        Bicycle                   = 0xe915
        Billboard                 = 0xe916
        Binary                    = 0xe917
        BinaryCircleCheck         = 0xe918
        BinaryLock                = 0xe919
        BinarySlash               = 0xe91a
        BinBottles                = 0xe91b
        BinBottlesRecycle         = 0xe91c
        Binoculars                = 0xe91d
        BinRecycle                = 0xe91e
        Biohazard                 = 0xe91f
        Bird                      = 0xe920
        BitcoinSign               = 0xe921
        Blanket                   = 0xe922
        BlanketFire               = 0xe923
        Blender                   = 0xe924
        BlenderPhone              = 0xe925
        Blinds                    = 0xe926
        BlindsOpen                = 0xe927
        BlindsRaised              = 0xe928
        Block                     = 0xe929
        BlockBrick                = 0xe92a
        BlockBrickFire            = 0xe92b
        BlockQuestion             = 0xe92c
        BlockQuote                = 0xe92d
        Blog                      = 0xe92e
        Blueberries               = 0xe92f
        Bluetooth                 = 0xe930
        Bold                      = 0xe931
        Bolt                      = 0xe932
        BoltAuto                  = 0xe933
        BoltLightning             = 0xe934
        BoltSlash                 = 0xe935
        Bomb                      = 0xe936
        Bone                      = 0xe937
        BoneBreak                 = 0xe938
        Bong                      = 0xe939
        Book                      = 0xe93a
        BookArrowRight            = 0xe93b
        BookArrowUp               = 0xe93c
        BookAtlas                 = 0xe93d
        BookBible                 = 0xe93e
        BookBlank                 = 0xe93f
        BookBookmark              = 0xe940
        BookCircleArrowRight      = 0xe941
        BookCircleArrowUp         = 0xe942
        BookCopy                  = 0xe943
        BookFont                  = 0xe944
        BookHeart                 = 0xe945
        BookJournalWhills         = 0xe946
        Bookmark                  = 0xe947
        BookmarkSlash             = 0xe948
        BookMedical               = 0xe949
        BookOpen                  = 0xe94a
        BookOpenCover             = 0xe94b
        BookOpenReader            = 0xe94c
        BookQuran                 = 0xe94d
        Books                     = 0xe94e
        BookSection               = 0xe94f
        BookSkull                 = 0xe950
        BooksMedical              = 0xe951
        BookSparkles              = 0xe952
        BookTanakh                = 0xe953
        BookUser                  = 0xe954
        Boombox                   = 0xe955
        Boot                      = 0xe956
        BoothCurtain              = 0xe957
        BootHeeled                = 0xe958
        BorderAll                 = 0xe959
        BorderBottom              = 0xe95a
        BorderBottomRight         = 0xe95b
        BorderCenterH             = 0xe95c
        BorderCenterV             = 0xe95d
        BorderInner               = 0xe95e
        BorderLeft                = 0xe95f
        BorderNone                = 0xe960
        BorderOuter               = 0xe961
        BorderRight               = 0xe962
        BorderTop                 = 0xe963
        BorderTopLeft             = 0xe964
        BoreHole                  = 0xe965
        BottleDroplet             = 0xe966
        BottleWater               = 0xe967
        BowArrow                  = 0xe968
        BowlChopsticks            = 0xe969
        BowlChopsticksNoodles     = 0xe96a
        BowlFood                  = 0xe96b
        BowlHot                   = 0xe96c
        BowlingBall               = 0xe96d
        BowlingBallPin            = 0xe96e
        BowlingPins               = 0xe96f
        BowlRice                  = 0xe970
        BowlScoop                 = 0xe971
        BowlScoops                = 0xe972
        BowlSoftServe             = 0xe973
        BowlSpoon                 = 0xe974
        Box                       = 0xe975
        BoxArchive                = 0xe976
        BoxBallot                 = 0xe977
        BoxCheck                  = 0xe978
        BoxCircleCheck            = 0xe979
        BoxDollar                 = 0xe97a
        BoxesPacking              = 0xe97b
        BoxesStacked              = 0xe97c
        BoxHeart                  = 0xe97d
        BoxingGlove               = 0xe97e
        BoxOpen                   = 0xe97f
        BoxOpenFull               = 0xe980
        BoxTaped                  = 0xe981
        BoxTissue                 = 0xe982
        BracketCurly              = 0xe983
        BracketCurlyRight         = 0xe984
        BracketRound              = 0xe985
        BracketRoundRight         = 0xe986
        BracketsCurly             = 0xe987
        BracketSquare             = 0xe988
        BracketSquareRight        = 0xe989
        BracketsRound             = 0xe98a
        BracketsSquare            = 0xe98b
        Braille                   = 0xe98c
        Brain                     = 0xe98d
        BrainArrowCurvedRight     = 0xe98e
        BrainCircuit              = 0xe98f
        BrakeWarning              = 0xe990
        BrazilianRealSign         = 0xe991
        BreadLoaf                 = 0xe992
        BreadSlice                = 0xe993
        BreadSliceButter          = 0xe994
        Bridge                    = 0xe995
        BridgeCircleCheck         = 0xe996
        BridgeCircleExclamation   = 0xe997
        BridgeCircleXmark         = 0xe998
        BridgeLock                = 0xe999
        BridgeSuspension          = 0xe99a
        BridgeWater               = 0xe99b
        Briefcase                 = 0xe99c
        BriefcaseArrowRight       = 0xe99d
        BriefcaseBlank            = 0xe99e
        BriefcaseMedical          = 0xe99f
        Brightness                = 0xe9a0
        BrightnessLow             = 0xe9a1
        BringForward              = 0xe9a2
        BringFront                = 0xe9a3
        Broccoli                  = 0xe9a4
        Clover                    = 0xe9a5
        BroomBall                 = 0xe9a6
        BroomWide                 = 0xe9a7
        Browser                   = 0xe9a8
        Browsers                  = 0xe9a9
        Brush                     = 0xe9aa
        Bucket                    = 0xe9ab
        Bug                       = 0xe9ac
        Bugs                      = 0xe9ad
        BugSlash                  = 0xe9ae
        Building                  = 0xe9af
        BuildingCircleArrowRight  = 0xe9b0
        BuildingCircleCheck       = 0xe9b1
        BuildingCircleExclamation = 0xe9b2
        BuildingCircleXmark       = 0xe9b3
        BuildingColumns           = 0xe9b4
        BuildingFlag              = 0xe9b5
        BuildingLock              = 0xe9b6
        BuildingMagnifyingGlass   = 0xe9b7
        BuildingMemo              = 0xe9b8
        BuildingNgo               = 0xe9b9
        Buildings                 = 0xe9ba
        BuildingShield            = 0xe9bb
        BuildingUn                = 0xe9bc
        BuildingUser              = 0xe9bd
        BuildingWheat             = 0xe9be
        Bulldozer                 = 0xe9bf
        Bullhorn                  = 0xe9c0
        Bullseye                  = 0xe9c1
        BullseyeArrow             = 0xe9c2
        BullseyePointer           = 0xe9c3
        Buoy                      = 0xe9c4
        BuoyMooring               = 0xe9c5
        Burger                    = 0xe9c6
        BurgerCheese              = 0xe9c7
        BurgerFries               = 0xe9c8
        BurgerGlass               = 0xe9c9
        BurgerLettuce             = 0xe9ca
        BurgerSoda                = 0xe9cb
        Burrito                   = 0xe9cc
        Burst                     = 0xe9cd
        Bus                       = 0xe9ce
        BusinessTime              = 0xe9cf
        BusSchool                 = 0xe9d0
        BusSimple                 = 0xe9d1
        Butter                    = 0xe9d2
        C                         = 0xe9d3
        Cabin                     = 0xe9d4
        CabinetFiling             = 0xe9d5
        CableCar                  = 0xe9d6
        Cactus                    = 0xe9d7
        CakeCandles               = 0xe9d8
        CakeSlice                 = 0xe9d9
        Calculator                = 0xe9da
        CalculatorSimple          = 0xe9db
        Calendar                  = 0xe9dc
        CalendarArrowDown         = 0xe9dd
        CalendarArrowUp           = 0xe9de
        CalendarCheck             = 0xe9df
        CalendarCircleExclamation = 0xe9e0
        CalendarCircleMinus       = 0xe9e1
        CalendarCirclePlus        = 0xe9e2
        CalendarCircleUser        = 0xe9e3
        CalendarClock             = 0xe9e4
        CalendarDay               = 0xe9e5
        CalendarDays              = 0xe9e6
        CalendarExclamation       = 0xe9e7
        CalendarImage             = 0xe9e8
        CalendarLines             = 0xe9e9
        CalendarMinus             = 0xe9ea
        CalendarHeart             = 0xe9eb
        CalendarLinesPen          = 0xe9ec
        CalendarPlus              = 0xe9ed
        Calendars                 = 0xe9ee
        CalendarPen               = 0xe9ef
        CalendarStar              = 0xe9f0
        CalendarWeek              = 0xe9f1
        CalendarXmark             = 0xe9f2
        CameraCctv                = 0xe9f3
        CalendarUsers             = 0xe9f4
        CameraMovie               = 0xe9f5
        Camcorder                 = 0xe9f6
        CameraRetro               = 0xe9f7
        CameraRotate              = 0xe9f8
        CameraSecurity            = 0xe9f9
        CameraPolaroid            = 0xe9fa
        CameraSlash               = 0xe9fb
        CalendarRange             = 0xe9fc
        CameraViewfinder          = 0xe9fd
        Camera                    = 0xe9fe
        CameraWeb                 = 0xe9ff
        Campground                = 0xea00
        CandleHolder              = 0xea01
        CameraWebSlash            = 0xea02
        Campfire                  = 0xea03
        Candy                     = 0xea04
        CandyCane                 = 0xea05
        CandyBar                  = 0xea06
        CanFood                   = 0xea07
        CandyCorn                 = 0xea08
        Cannabis                  = 0xea09
        Cannon                    = 0xea0a
        Capsules                  = 0xea0b
        Car                       = 0xea0c
        Caravan                   = 0xea0d
        CaravanSimple             = 0xea0e
        CarBattery                = 0xea0f
        CarBolt                   = 0xea10
        CarBuilding               = 0xea11
        CarBump                   = 0xea12
        CarBurst                  = 0xea13
        CarBus                    = 0xea14
        CarCircleBolt             = 0xea15
        CardClub                  = 0xea16
        CardDiamond               = 0xea17
        CardHeart                 = 0xea18
        Cards                     = 0xea19
        CardsBlank                = 0xea1a
        CardSpade                 = 0xea1b
        CaretDown                 = 0xea1c
        CaretLeft                 = 0xea1d
        CaretRight                = 0xea1e
        CaretUp                   = 0xea1f
        CarGarage                 = 0xea20
        CarMirrors                = 0xea21
        CarOn                     = 0xea22
        CarRear                   = 0xea23
        Carrot                    = 0xea24
        Cars                      = 0xea25
        CarSide                   = 0xea26
        CarSideBolt               = 0xea27
        CartArrowDown             = 0xea28
        CartArrowUp               = 0xea29
        CartCircleArrowDown       = 0xea2a
        CartCircleArrowUp         = 0xea2b
        CartCircleCheck           = 0xea2c
        CartCircleExclamation     = 0xea2d
        CartCirclePlus            = 0xea2e
        CartCircleXmark           = 0xea2f
        CartFlatbed               = 0xea30
        CartFlatbedBoxes          = 0xea31
        CartFlatbedEmpty          = 0xea32
        CartFlatbedSuitcase       = 0xea33
        CarTilt                   = 0xea34
        CartMinus                 = 0xea35
        CartShopping              = 0xea36
        CartPlus                  = 0xea37
        CartShoppingFast          = 0xea38
        CarTunnel                 = 0xea39
        CartXmark                 = 0xea3a
        CarWash                   = 0xea3b
        CarWrench                 = 0xea3c
        CashRegister              = 0xea3d
        CassetteBetamax           = 0xea3e
        CassetteTape              = 0xea3f
        CassetteVhs               = 0xea40
        Castle                    = 0xea41
        Cat                       = 0xea42
        CatSpace                  = 0xea43
        Cauldron                  = 0xea44
        CediSign                  = 0xea45
        CentSign                  = 0xea46
        Certificate               = 0xea47
        Chair                     = 0xea48
        ChairOffice               = 0xea49
        Chalkboard                = 0xea4a
        ChalkboardUser            = 0xea4b
        ChampagneGlass            = 0xea4c
        ChampagneGlasses          = 0xea4d
        ChargingStation           = 0xea4e
        ChartArea                 = 0xea4f
        ChartBar                  = 0xea50
        ChartBullet               = 0xea51
        ChartCandlestick          = 0xea52
        ChartColumn               = 0xea53
        ChartGantt                = 0xea54
        ChartKanban               = 0xea55
        ChartLine                 = 0xea56
        ChartLineDown             = 0xea57
        ChartLineUp               = 0xea58
        ChartLineUpDown           = 0xea59
        ChartMixed                = 0xea5a
        ChartMixedUpCircleCurrency = 0xea5b
        ChartMixedUpCircleDollar  = 0xea5c
        ChartNetwork              = 0xea5d
        ChartPie                  = 0xea5e
        ChartPieSimple            = 0xea5f
        ChartPieSimpleCircleCurrency = 0xea60
        ChartPieSimpleCircleDollar = 0xea61
        ChartPyramid              = 0xea62
        ChartRadar                = 0xea63
        ChartScatter              = 0xea64
        ChartScatter3d            = 0xea65
        ChartScatterBubble        = 0xea66
        ChartSimple               = 0xea67
        ChartSimpleHorizontal     = 0xea68
        ChartTreeMap              = 0xea69
        ChartUser                 = 0xea6a
        ChartWaterfall            = 0xea6b
        Check                     = 0xea6c
        CheckDouble               = 0xea6d
        CheckToSlot               = 0xea6e
        Cheese                    = 0xea6f
        CheeseSwiss               = 0xea70
        Cherries                  = 0xea71
        Chess                     = 0xea72
        ChessBishop               = 0xea73
        ChessBishopPiece          = 0xea74
        ChessBoard                = 0xea75
        ChessClock                = 0xea76
        ChessClockFlip            = 0xea77
        ChessKing                 = 0xea78
        ChessKingPiece            = 0xea79
        ChessKnight               = 0xea7a
        ChessKnightPiece          = 0xea7b
        ChessPawn                 = 0xea7c
        ChessPawnPiece            = 0xea7d
        ChessQueen                = 0xea7e
        ChessQueenPiece           = 0xea7f
        ChessRook                 = 0xea80
        ChessRookPiece            = 0xea81
        Chestnut                  = 0xea82
        ChevronDown               = 0xea83
        ChevronLeft               = 0xea84
        ChevronRight              = 0xea85
        ChevronsDown              = 0xea86
        ChevronsLeft              = 0xea87
        ChevronsRight             = 0xea88
        ChevronsUp                = 0xea89
        ChevronUp                 = 0xea8a
        ChfSign                   = 0xea8b
        Child                     = 0xea8c
        ChildCombatant            = 0xea8d
        ChildDress                = 0xea8e
        ChildReaching             = 0xea8f
        Children                  = 0xea90
        Chimney                   = 0xea91
        Chopsticks                = 0xea92
        Church                    = 0xea93
        Circle                    = 0xea94
        Circle0                   = 0xea95
        Circle1                   = 0xea96
        Circle2                   = 0xea97
        Circle3                   = 0xea98
        Circle4                   = 0xea99
        Circle5                   = 0xea9a
        Circle6                   = 0xea9b
        Circle7                   = 0xea9c
        Circle8                   = 0xea9d
        Circle9                   = 0xea9e
        CircleA                   = 0xea9f
        CircleAmpersand           = 0xeaa0
        CircleArrowDown           = 0xeaa1
        CircleArrowDownLeft       = 0xeaa2
        CircleArrowDownRight      = 0xeaa3
        CircleArrowLeft           = 0xeaa4
        CircleArrowRight          = 0xeaa5
        CircleArrowUp             = 0xeaa6
        CircleArrowUpLeft         = 0xeaa7
        CircleArrowUpRight        = 0xeaa8
        CircleB                   = 0xeaa9
        CircleBolt                = 0xeaaa
        CircleBookmark            = 0xeaab
        CircleBookOpen            = 0xeaac
        CircleC                   = 0xeaad
        CircleCalendar            = 0xeaae
        CircleCamera              = 0xeaaf
        CircleCaretDown           = 0xeab0
        CircleCaretLeft           = 0xeab1
        CircleCaretRight          = 0xeab2
        CircleCaretUp             = 0xeab3
        CircleCheck               = 0xeab4
        CircleChevronDown         = 0xeab5
        CircleChevronLeft         = 0xeab6
        CircleChevronRight        = 0xeab7
        CircleChevronUp           = 0xeab8
        CircleD                   = 0xeab9
        CircleDashed              = 0xeaba
        CircleDivide              = 0xeabb
        CircleDollar              = 0xeabc
        CircleDollarToSlot        = 0xeabd
        CircleDot                 = 0xeabe
        CircleDown                = 0xeabf
        CircleDownLeft            = 0xeac0
        CircleDownRight           = 0xeac1
        CircleE                   = 0xeac2
        CircleEllipsis            = 0xeac3
        CircleEllipsisVertical    = 0xeac4
        CircleEnvelope            = 0xeac5
        CircleEuro                = 0xeac6
        CircleExclamation         = 0xeac7
        CircleExclamationCheck    = 0xeac8
        CircleF                   = 0xeac9
        CircleG                   = 0xeaca
        CircleH                   = 0xeacb
        CircleHalf                = 0xeacc
        CircleHalfStroke          = 0xeacd
        CircleHeart               = 0xeace
        CircleI                   = 0xeacf
        CircleInfo                = 0xead0
        CircleJ                   = 0xead1
        CircleK                   = 0xead2
        CircleL                   = 0xead3
        CircleLeft                = 0xead4
        CircleLocationArrow       = 0xead5
        CircleM                   = 0xead6
        CircleMicrophone          = 0xead7
        CircleMicrophoneLines     = 0xead8
        CircleMinus               = 0xead9
        CircleN                   = 0xeada
        CircleNodes               = 0xeadb
        CircleNotch               = 0xeadc
        CircleO                   = 0xeadd
        CircleP                   = 0xeade
        CircleParking             = 0xeadf
        CirclePause               = 0xeae0
        CirclePhone               = 0xeae1
        CirclePhoneFlip           = 0xeae2
        CirclePhoneHangup         = 0xeae3
        CirclePlay                = 0xeae4
        CirclePlus                = 0xeae5
        CircleQ                   = 0xeae6
        CircleQuarter             = 0xeae7
        CircleQuarters            = 0xeae8
        CircleQuarterStroke       = 0xeae9
        CircleQuestion            = 0xeaea
        CircleR                   = 0xeaeb
        CircleRadiation           = 0xeaec
        CircleRight               = 0xeaed
        CircleS                   = 0xeaee
        CircleSmall               = 0xeaef
        CircleSort                = 0xeaf0
        CircleSortDown            = 0xeaf1
        CircleSortUp              = 0xeaf2
        CirclesOverlap            = 0xeaf3
        CircleStar                = 0xeaf4
        CircleSterling            = 0xeaf5
        CircleStop                = 0xeaf6
        CircleT                   = 0xeaf7
        CircleThreeQuarters       = 0xeaf8
        CircleThreeQuartersStroke = 0xeaf9
        CircleTrash               = 0xeafa
        CircleU                   = 0xeafb
        CircleUp                  = 0xeafc
        CircleUpLeft              = 0xeafd
        CircleUpRight             = 0xeafe
        CircleUser                = 0xeaff
        CircleV                   = 0xeb00
        CircleVideo               = 0xeb01
        CircleW                   = 0xeb02
        CircleWaveformLines       = 0xeb03
        CircleX                   = 0xeb04
        CircleXmark               = 0xeb05
        CircleY                   = 0xeb06
        CircleYen                 = 0xeb07
        CircleZ                   = 0xeb08
        Citrus                    = 0xeb09
        CitrusSlice               = 0xeb0a
        City                      = 0xeb0b
        Clapperboard              = 0xeb0c
        ClapperboardPlay          = 0xeb0d
        Clarinet                  = 0xeb0e
        ClawMarks                 = 0xeb0f
        Clipboard                 = 0xeb10
        ClipboardCheck            = 0xeb11
        ClipboardList             = 0xeb12
        ClipboardListCheck        = 0xeb13
        ClipboardMedical          = 0xeb14
        ClipboardPrescription     = 0xeb15
        ClipboardQuestion         = 0xeb16
        ClipboardUser             = 0xeb17
        Clock                     = 0xeb18
        ClockDesk                 = 0xeb19
        ClockEight                = 0xeb1a
        ClockEightThirty          = 0xeb1b
        ClockEleven               = 0xeb1c
        ClockElevenThirty         = 0xeb1d
        ClockFive                 = 0xeb1e
        ClockFiveThirty           = 0xeb1f
        ClockFourThirty           = 0xeb20
        ClockNine                 = 0xeb21
        ClockNineThirty           = 0xeb22
        ClockOne                  = 0xeb23
        ClockOneThirty            = 0xeb24
        ClockRotateLeft           = 0xeb25
        ClockSeven                = 0xeb26
        ClockSevenThirty          = 0xeb27
        ClockSix                  = 0xeb28
        ClockSixThirty            = 0xeb29
        ClockTen                  = 0xeb2a
        ClockTenThirty            = 0xeb2b
        ClockThree                = 0xeb2c
        ClockThreeThirty          = 0xeb2d
        ClockTwelve               = 0xeb2e
        ClockTwelveThirty         = 0xeb2f
        ClockTwo                  = 0xeb30
        ClockTwoThirty            = 0xeb31
        Clone                     = 0xeb32
        ClosedCaptioning          = 0xeb33
        ClosedCaptioningSlash     = 0xeb34
        ClothesHanger             = 0xeb35
        Cloud                     = 0xeb36
        CloudArrowDown            = 0xeb37
        CloudArrowUp              = 0xeb38
        CloudBinary               = 0xeb39
        CloudBolt                 = 0xeb3a
        CloudBoltMoon             = 0xeb3b
        CloudBoltSun              = 0xeb3c
        CloudCheck                = 0xeb3d
        CloudDrizzle              = 0xeb3e
        CloudExclamation          = 0xeb3f
        CloudFog                  = 0xeb40
        CloudHail                 = 0xeb41
        CloudHailMixed            = 0xeb42
        CloudMeatball             = 0xeb43
        CloudMinus                = 0xeb44
        CloudMoon                 = 0xeb45
        CloudMoonRain             = 0xeb46
        CloudMusic                = 0xeb47
        CloudPlus                 = 0xeb48
        CloudQuestion             = 0xeb49
        CloudRain                 = 0xeb4a
        CloudRainbow              = 0xeb4b
        Clouds                    = 0xeb4c
        CloudShowers              = 0xeb4d
        CloudShowersHeavy         = 0xeb4e
        CloudShowersWater         = 0xeb4f
        CloudSlash                = 0xeb50
        CloudSleet                = 0xeb51
        CloudsMoon                = 0xeb52
        CloudSnow                 = 0xeb53
        CloudsSun                 = 0xeb54
        CloudSun                  = 0xeb55
        CloudSunRain              = 0xeb56
        CloudWord                 = 0xeb57
        CloudXmark                = 0xeb58
        FaceSaluting              = 0xeb59
        Club                      = 0xeb5a
        Coconut                   = 0xeb5b
        Code                      = 0xeb5c
        CodeBranch                = 0xeb5d
        CodeCommit                = 0xeb5e
        CodeCompare               = 0xeb5f
        CodeFork                  = 0xeb60
        CodePullRequest           = 0xeb61
        CodePullRequestClosed     = 0xeb62
        CodeMerge                 = 0xeb63
        CodePullRequestDraft      = 0xeb64
        CodeSimple                = 0xeb65
        CoffeeBean                = 0xeb66
        CoffeeBeans               = 0xeb67
        CoffeePot                 = 0xeb68
        CoffinCross               = 0xeb69
        Coffin                    = 0xeb6a
        Coin                      = 0xeb6b
        CoinBlank                 = 0xeb6c
        CoinVertical              = 0xeb6d
        CoinFront                 = 0xeb6e
        Colon                     = 0xeb6f
        Coins                     = 0xeb70
        ColonSign                 = 0xeb71
        Columns3                  = 0xeb72
        Comet                     = 0xeb73
        Comma                     = 0xeb74
        Comment                   = 0xeb75
        CommentArrowDown          = 0xeb76
        CommentArrowUp            = 0xeb77
        CommentArrowUpRight       = 0xeb78
        CommentCaptions           = 0xeb79
        CommentCheck              = 0xeb7a
        CommentDollar             = 0xeb7b
        CommentDots               = 0xeb7c
        CommentCode               = 0xeb7d
        Command                   = 0xeb7e
        CommentImage              = 0xeb7f
        CommentHeart              = 0xeb80
        CommentExclamation        = 0xeb81
        CommentLines              = 0xeb82
        CommentMedical            = 0xeb83
        CommentMiddle             = 0xeb84
        CommentMiddleTop          = 0xeb85
        CommentMinus              = 0xeb86
        CommentMusic              = 0xeb87
        CommentPen                = 0xeb88
        CommentPlus               = 0xeb89
        CommentQuestion           = 0xeb8a
        CommentQuote              = 0xeb8b
        Comments                  = 0xeb8c
        CommentsDollar            = 0xeb8d
        CommentSlash              = 0xeb8e
        CommentSmile              = 0xeb8f
        CommentSms                = 0xeb90
        CommentsQuestion          = 0xeb91
        CommentsQuestionCheck     = 0xeb92
        CommentText               = 0xeb93
        CommentXmark              = 0xeb94
        CompactDisc               = 0xeb95
        Compass                   = 0xeb96
        CompassDrafting           = 0xeb97
        CompassSlash              = 0xeb98
        Compress                  = 0xeb99
        CompressWide              = 0xeb9a
        ComputerClassic           = 0xeb9b
        ComputerMouse             = 0xeb9c
        ComputerMouseScrollwheel  = 0xeb9d
        ComputerSpeaker           = 0xeb9e
        ContainerStorage          = 0xeb9f
        ConveyorBelt              = 0xeba0
        ConveyorBeltBoxes         = 0xeba1
        ConveyorBeltArm           = 0xeba2
        CookieBite                = 0xeba3
        Computer                  = 0xeba4
        Copyright                 = 0xeba5
        Cookie                    = 0xeba6
        Corn                      = 0xeba7
        Corner                    = 0xeba8
        Copy                      = 0xeba9
        CourtSport                = 0xebaa
        Cow                       = 0xebab
        Couch                     = 0xebac
        CowbellCirclePlus         = 0xebad
        Cowbell                   = 0xebae
        CrateEmpty                = 0xebaf
        CreditCardFront           = 0xebb0
        Crab                      = 0xebb1
        CreditCardBlank           = 0xebb2
        CreditCard                = 0xebb3
        CrateApple                = 0xebb4
        ConveyorBeltEmpty         = 0xebb5
        Crop                      = 0xebb6
        Crosshairs                = 0xebb7
        CropSimple                = 0xebb8
        Cross                     = 0xebb9
        Croissant                 = 0xebba
        CricketBatBall            = 0xebbb
        CrosshairsSimple          = 0xebbc
        Crow                      = 0xebbd
        Crown                     = 0xebbe
        Crutch                    = 0xebbf
        Crutches                  = 0xebc0
        CruzeiroSign              = 0xebc1
        CrystalBall               = 0xebc2
        Cube                      = 0xebc3
        Cubes                     = 0xebc4
        CubesStacked              = 0xebc5
        Cucumber                  = 0xebc6
        Cupcake                   = 0xebc7
        CupStraw                  = 0xebc8
        CupStrawSwoosh            = 0xebc9
        CupTogo                   = 0xebca
        CurlingStone              = 0xebcb
        Custard                   = 0xebcc
        D                         = 0xebcd
        Dagger                    = 0xebce
        Dash                      = 0xebcf
        Database                  = 0xebd0
        Deer                      = 0xebd1
        DeerRudolph               = 0xebd2
        DeleteLeft                = 0xebd3
        DeleteRight               = 0xebd4
        Desktop                   = 0xebd5
        Democrat                  = 0xebd6
        DesktopArrowDown          = 0xebd7
        Dharmachakra              = 0xebd8
        DiagramCells              = 0xebd9
        DiagramLeanCanvas         = 0xebda
        DiagramNested             = 0xebdb
        DiagramNext               = 0xebdc
        DiagramPredecessor        = 0xebdd
        DiagramPrevious           = 0xebde
        DiagramProject            = 0xebdf
        DiagramSankey             = 0xebe0
        DiagramSubtask            = 0xebe1
        DiagramSuccessor          = 0xebe2
        DiagramVenn               = 0xebe3
        Dial                      = 0xebe4
        DialHigh                  = 0xebe5
        DialLow                   = 0xebe6
        DialMax                   = 0xebe7
        DialMed                   = 0xebe8
        DialMedLow                = 0xebe9
        DialMin                   = 0xebea
        DialOff                   = 0xebeb
        Diamond                   = 0xebec
        DiamondExclamation        = 0xebed
        DiamondHalf               = 0xebee
        DiamondHalfStroke         = 0xebef
        DiamondTurnRight          = 0xebf0
        Dice                      = 0xebf1
        DiceD4                    = 0xebf2
        DiceD6                    = 0xebf3
        DiceD8                    = 0xebf4
        DiceD10                   = 0xebf5
        DiceD12                   = 0xebf6
        DiceD20                   = 0xebf7
        DiceFive                  = 0xebf8
        DiceFour                  = 0xebf9
        DiceOne                   = 0xebfa
        DiceSix                   = 0xebfb
        DiceThree                 = 0xebfc
        DiceTwo                   = 0xebfd
        Dinosaur                  = 0xebfe
        Diploma                   = 0xebff
        DiscDrive                 = 0xec00
        Disease                   = 0xec01
        Display                   = 0xec02
        DisplayArrowDown          = 0xec03
        DisplayChartUp            = 0xec04
        DisplayChartUpCircleCurrency = 0xec05
        DisplayChartUpCircleDollar = 0xec06
        DisplayCode               = 0xec07
        DisplayMedical            = 0xec08
        DisplaySlash              = 0xec09
        DistributeSpacingHorizontal = 0xec0a
        DistributeSpacingVertical = 0xec0b
        Ditto                     = 0xec0c
        Divide                    = 0xec0d
        Dna                       = 0xec0e
        Dog                       = 0xec0f
        DogLeashed                = 0xec10
        DollarSign                = 0xec11
        Dolly                     = 0xec12
        DollyEmpty                = 0xec13
        Dolphin                   = 0xec14
        DongSign                  = 0xec15
        DoNotEnter                = 0xec16
        Donut                     = 0xec17
        DoorClosed                = 0xec18
        DoorOpen                  = 0xec19
        Dove                      = 0xec1a
        Down                      = 0xec1b
        DownFromDottedLine        = 0xec1c
        DownFromLine              = 0xec1d
        DownLeft                  = 0xec1e
        DownLeftAndUpRightToCenter = 0xec1f
        Download                  = 0xec20
        DownLong                  = 0xec21
        DownRight                 = 0xec22
        DownToBracket             = 0xec23
        DownToDottedLine          = 0xec24
        DownToLine                = 0xec25
        Dragon                    = 0xec26
        DrawCircle                = 0xec27
        DrawPolygon               = 0xec28
        DrawSquare                = 0xec29
        Dreidel                   = 0xec2a
        Drone                     = 0xec2b
        DroneFront                = 0xec2c
        Droplet                   = 0xec2d
        DropletDegree             = 0xec2e
        DropletPercent            = 0xec2f
        DropletSlash              = 0xec30
        Drum                      = 0xec31
        DrumSteelpan              = 0xec32
        Drumstick                 = 0xec33
        DrumstickBite             = 0xec34
        Dryer                     = 0xec35
        DryerHeat                 = 0xec36
        Duck                      = 0xec37
        Dumbbell                  = 0xec38
        Dumpster                  = 0xec39
        DumpsterFire              = 0xec3a
        Dungeon                   = 0xec3b
        E                         = 0xec3c
        Ear                       = 0xec3d
        EarDeaf                   = 0xec3e
        EarListen                 = 0xec3f
        EarMuffs                  = 0xec40
        EarthAfrica               = 0xec41
        EarthAmericas             = 0xec42
        EarthAsia                 = 0xec43
        EarthEurope               = 0xec44
        EarthOceania              = 0xec45
        Eclipse                   = 0xec46
        Egg                       = 0xec47
        EggFried                  = 0xec48
        Eggplant                  = 0xec49
        Eject                     = 0xec4a
        Elephant                  = 0xec4b
        Elevator                  = 0xec4c
        Ellipsis                  = 0xec4d
        EllipsisStroke            = 0xec4e
        EllipsisStrokeVertical    = 0xec4f
        EllipsisVertical          = 0xec50
        EmptySet                  = 0xec51
        Engine                    = 0xec52
        EngineWarning             = 0xec53
        Envelope                  = 0xec54
        EnvelopeCircleCheck       = 0xec55
        EnvelopeDot               = 0xec56
        EnvelopeOpen              = 0xec57
        EnvelopeOpenDollar        = 0xec58
        EnvelopeOpenText          = 0xec59
        Envelopes                 = 0xec5a
        EnvelopesBulk             = 0xec5b
        Equals                    = 0xec5c
        Eraser                    = 0xec5d
        Escalator                 = 0xec5e
        Ethernet                  = 0xec5f
        EuroSign                  = 0xec60
        Excavator                 = 0xec61
        Exclamation               = 0xec62
        Expand                    = 0xec63
        ExpandWide                = 0xec64
        Explosion                 = 0xec65
        Eye                       = 0xec66
        EyeDropper                = 0xec67
        EyeDropperFull            = 0xec68
        EyeDropperHalf            = 0xec69
        EyeEvil                   = 0xec6a
        EyeLowVision              = 0xec6b
        Eyes                      = 0xec6c
        EyeSlash                  = 0xec6d
        F                         = 0xec6e
        FaceAngry                 = 0xec6f
        FaceAngryHorns            = 0xec70
        FaceAnguished             = 0xec71
        FaceAnxiousSweat          = 0xec72
        FaceAstonished            = 0xec73
        FaceAwesome               = 0xec74
        FaceBeamHandOverMouth     = 0xec75
        FaceClouds                = 0xec76
        FaceConfounded            = 0xec77
        FaceConfused              = 0xec78
        FaceCowboyHat             = 0xec79
        FaceDiagonalMouth         = 0xec7a
        FaceDisappointed          = 0xec7b
        FaceDisguise              = 0xec7c
        FaceDizzy                 = 0xec7d
        FaceDotted                = 0xec7e
        FaceDowncastSweat         = 0xec7f
        FaceDrooling              = 0xec80
        FaceExhaling              = 0xec81
        FaceExplode               = 0xec82
        FaceExpressionless        = 0xec83
        FaceEyesXmarks            = 0xec84
        FaceFearful               = 0xec85
        FaceFlushed               = 0xec86
        FaceFrown                 = 0xec87
        FaceFrownOpen             = 0xec88
        FaceFrownSlight           = 0xec89
        FaceGlasses               = 0xec8a
        FaceGrimace               = 0xec8b
        FaceGrin                  = 0xec8c
        FaceGrinBeam              = 0xec8d
        FaceGrinBeamSweat         = 0xec8e
        FaceGrinHearts            = 0xec8f
        FaceGrinSquint            = 0xec90
        FaceGrinSquintTears       = 0xec91
        FaceGrinStars             = 0xec92
        FaceGrinTears             = 0xec93
        FaceGrinTongue            = 0xec94
        FaceGrinTongueSquint      = 0xec95
        FaceGrinTongueWink        = 0xec96
        FaceGrinWide              = 0xec97
        FaceGrinWink              = 0xec98
        FaceHandOverMouth         = 0xec99
        FaceHandPeeking           = 0xec9a
        FaceHandYawn              = 0xec9b
        FaceHeadBandage           = 0xec9c
        FaceHoldingBackTears      = 0xec9d
        FaceHushed                = 0xec9e
        FaceIcicles               = 0xec9f
        FaceKiss                  = 0xeca0
        FaceKissBeam              = 0xeca1
        FaceKissClosedEyes        = 0xeca2
        FaceKissWinkHeart         = 0xeca3
        FaceLaugh                 = 0xeca4
        FaceLaughBeam             = 0xeca5
        FaceLaughSquint           = 0xeca6
        FaceLaughWink             = 0xeca7
        FaceLying                 = 0xeca8
        FaceMask                  = 0xeca9
        FaceMeh                   = 0xecaa
        FaceMehBlank              = 0xecab
        FaceMelting               = 0xecac
        FaceMonocle               = 0xecad
        FaceNauseated             = 0xecae
        FaceNoseSteam             = 0xecaf
        FaceParty                 = 0xecb0
        FacePensive               = 0xecb1
        FacePersevering           = 0xecb2
        FacePleading              = 0xecb3
        FacePouting               = 0xecb4
        FaceRaisedEyebrow         = 0xecb5
        FaceRelieved              = 0xecb6
        FaceRollingEyes           = 0xecb7
        FaceSadCry                = 0xecb8
        FaceSadSweat              = 0xecb9
        FaceSadTear               = 0xecba
        Hotdog                    = 0xecbb
        FaceScream                = 0xecbc
        FaceShush                 = 0xecbd
        FaceSleeping              = 0xecbe
        FaceSleepy                = 0xecbf
        FaceSmileBeam             = 0xecc0
        FaceSmile                 = 0xecc1
        FaceSmileHalo             = 0xecc2
        FaceSmileHearts           = 0xecc3
        FaceSmileHorns            = 0xecc4
        FaceSmilePlus             = 0xecc5
        FaceSmileRelaxed          = 0xecc6
        FaceSmileTear             = 0xecc7
        FaceSmileTongue           = 0xecc8
        FaceSmileUpsideDown       = 0xecc9
        FaceSmileWink             = 0xecca
        FaceSmilingHands          = 0xeccb
        FaceSpiralEyes            = 0xeccc
        FaceSmirking              = 0xeccd
        FaceSunglasses            = 0xecce
        FaceSurprise              = 0xeccf
        FaceSwear                 = 0xecd0
        FaceThermometer           = 0xecd1
        FaceThinking              = 0xecd2
        FaceTired                 = 0xecd3
        FaceTissue                = 0xecd4
        FaceTongueMoney           = 0xecd5
        FaceTongueSweat           = 0xecd6
        FaceUnamused              = 0xecd7
        FaceViewfinder            = 0xecd8
        FaceVomit                 = 0xecd9
        FaceWeary                 = 0xecda
        FaceWoozy                 = 0xecdb
        FaceWorried               = 0xecdc
        FaceZany                  = 0xecdd
        FaceZipper                = 0xecde
        Falafel                   = 0xecdf
        Family                    = 0xece0
        FamilyDress               = 0xece1
        FamilyPants               = 0xece2
        Fan                       = 0xece3
        FanTable                  = 0xece4
        Farm                      = 0xece5
        Faucet                    = 0xece6
        FaucetDrip                = 0xece7
        Fax                       = 0xece8
        Feather                   = 0xece9
        FeatherPointed            = 0xecea
        Fence                     = 0xeceb
        FerrisWheel               = 0xecec
        Ferry                     = 0xeced
        FieldHockeyStickBall      = 0xecee
        File                      = 0xecef
        FileArrowDown             = 0xecf0
        FileArrowUp               = 0xecf1
        FileAudio                 = 0xecf2
        FileBinary                = 0xecf3
        FileCertificate           = 0xecf4
        FileChartColumn           = 0xecf5
        FileChartPie              = 0xecf6
        FileCheck                 = 0xecf7
        FileCircleCheck           = 0xecf8
        FileCircleExclamation     = 0xecf9
        FileCircleInfo            = 0xecfa
        FileCircleMinus           = 0xecfb
        FileCirclePlus            = 0xecfc
        FileCircleQuestion        = 0xecfd
        FileCircleXmark           = 0xecfe
        FileCode                  = 0xecff
        FileContract              = 0xed00
        FileCsv                   = 0xed01
        FileDashedLine            = 0xed02
        FileDoc                   = 0xed03
        FileEps                   = 0xed04
        FileExclamation           = 0xed05
        FileGif                   = 0xed06
        FileExport                = 0xed07
        FileImport                = 0xed08
        FileExcel                 = 0xed09
        FileHeart                 = 0xed0a
        FileInvoiceDollar         = 0xed0b
        FileImage                 = 0xed0c
        FileInvoice               = 0xed0d
        FileJpg                   = 0xed0e
        FileLines                 = 0xed0f
        FileMagnifyingGlass       = 0xed10
        FileLock                  = 0xed11
        FileMedical               = 0xed12
        FileMinus                 = 0xed13
        FileMov                   = 0xed14
        FileMp4                   = 0xed15
        FileMp3                   = 0xed16
        FilePdf                   = 0xed17
        FileMusic                 = 0xed18
        FilePen                   = 0xed19
        FilePlusMinus             = 0xed1a
        FilePrescription          = 0xed1b
        FilePlus                  = 0xed1c
        FilePowerpoint            = 0xed1d
        FilePpt                   = 0xed1e
        Files                     = 0xed1f
        FileShield                = 0xed20
        FileSignature             = 0xed21
        FileSlash                 = 0xed22
        FilesMedical              = 0xed23
        FileSpreadsheet           = 0xed24
        FileSvg                   = 0xed25
        FileUser                  = 0xed26
        FileVector                = 0xed27
        FileVideo                 = 0xed28
        FileWaveform              = 0xed29
        FileWord                  = 0xed2a
        FileXls                   = 0xed2b
        FileXmark                 = 0xed2c
        FileXml                   = 0xed2d
        FileZip                   = 0xed2e
        FileZipper                = 0xed2f
        Fill                      = 0xed30
        FillDrip                  = 0xed31
        Film                      = 0xed32
        FilmCanister              = 0xed33
        Films                     = 0xed34
        FilmSimple                = 0xed35
        FilmSlash                 = 0xed36
        Filter                    = 0xed37
        FilterCircleDollar        = 0xed38
        FilterCircleXmark         = 0xed39
        FilterList                = 0xed3a
        Filters                   = 0xed3b
        FilterSlash               = 0xed3c
        Fingerprint               = 0xed3d
        Fire                      = 0xed3e
        FireBurner                = 0xed3f
        FireExtinguisher          = 0xed40
        FireFlame                 = 0xed41
        FireFlameCurved           = 0xed42
        FireFlameSimple           = 0xed43
        FireHydrant               = 0xed44
        Fireplace                 = 0xed45
        FireSmoke                 = 0xed46
        Fish                      = 0xed47
        FishBones                 = 0xed48
        FishCooked                = 0xed49
        FishFins                  = 0xed4a
        FishingRod                = 0xed4b
        Flag                      = 0xed4c
        FlagCheckered             = 0xed4d
        FlagPennant               = 0xed4e
        FlagSwallowtail           = 0xed4f
        FlagUsa                   = 0xed50
        Flashlight                = 0xed51
        Flask                     = 0xed52
        FlaskGear                 = 0xed53
        FlaskRoundPoison          = 0xed54
        FlaskRoundPotion          = 0xed55
        FlaskVial                 = 0xed56
        Flatbread                 = 0xed57
        FlatbreadStuffed          = 0xed58
        FloppyDisk                = 0xed59
        FloppyDiskCircleArrowRight = 0xed5a
        FloppyDiskCircleXmark     = 0xed5b
        FloppyDiskPen             = 0xed5c
        FloppyDisks               = 0xed5d
        FlorinSign                = 0xed5e
        Flower                    = 0xed5f
        FlowerDaffodil            = 0xed60
        FlowerTulip               = 0xed61
        Flute                     = 0xed62
        FluxCapacitor             = 0xed63
        FlyingDisc                = 0xed64
        Folder                    = 0xed65
        FolderArrowDown           = 0xed66
        FolderArrowUp             = 0xed67
        FolderBookmark            = 0xed68
        FolderCheck               = 0xed69
        FolderClosed              = 0xed6a
        FolderGear                = 0xed6b
        FolderGrid                = 0xed6c
        FolderHeart               = 0xed6d
        FolderImage               = 0xed6e
        FolderMagnifyingGlass     = 0xed6f
        FolderMedical             = 0xed70
        FolderMinus               = 0xed71
        FolderMusic               = 0xed72
        FolderOpen                = 0xed73
        FolderPlus                = 0xed74
        Folders                   = 0xed75
        FolderTree                = 0xed76
        FolderUser                = 0xed77
        FolderXmark               = 0xed78
        FonduePot                 = 0xed79
        Font                      = 0xed7a
        FontAwesome               = 0xed7b
        FontCase                  = 0xed7c
        Football                  = 0xed7d
        FootballHelmet            = 0xed7e
        Fork                      = 0xed7f
        ForkKnife                 = 0xed80
        Forklift                  = 0xed81
        Fort                      = 0xed82
        Forward                   = 0xed83
        ForwardFast               = 0xed84
        ForwardStep               = 0xed85
        Frame                     = 0xed86
        FrancSign                 = 0xed87
        FrenchFries               = 0xed88
        Frog                      = 0xed89
        Function                  = 0xed8a
        Futbol                    = 0xed8b
        G                         = 0xed8c
        Galaxy                    = 0xed8d
        GalleryThumbnails         = 0xed8e
        GameBoard                 = 0xed8f
        GameBoardSimple           = 0xed90
        GameConsoleHandheld       = 0xed91
        GameConsoleHandheldCrank  = 0xed92
        Gamepad                   = 0xed93
        GamepadModern             = 0xed94
        Garage                    = 0xed95
        GarageCar                 = 0xed96
        GarageOpen                = 0xed97
        Garlic                    = 0xed98
        GasPump                   = 0xed99
        GasPumpSlash              = 0xed9a
        Gauge                     = 0xed9b
        GaugeCircleBolt           = 0xed9c
        GaugeCircleMinus          = 0xed9d
        GaugeCirclePlus           = 0xed9e
        GaugeHigh                 = 0xed9f
        GaugeLow                  = 0xeda0
        GaugeMax                  = 0xeda1
        GaugeMin                  = 0xeda2
        GaugeSimple               = 0xeda3
        GaugeSimpleHigh           = 0xeda4
        GaugeSimpleLow            = 0xeda5
        GaugeSimpleMax            = 0xeda6
        GaugeSimpleMin            = 0xeda7
        Gavel                     = 0xeda8
        Gear                      = 0xeda9
        GearCode                  = 0xedaa
        GearComplex               = 0xedab
        GearComplexCode           = 0xedac
        Gears                     = 0xedad
        Gem                       = 0xedae
        Genderless                = 0xedaf
        Ghost                     = 0xedb0
        Gif                       = 0xedb1
        Gift                      = 0xedb2
        GiftCard                  = 0xedb3
        Gifts                     = 0xedb4
        GingerbreadMan            = 0xedb5
        Glass                     = 0xedb6
        GlassCitrus               = 0xedb7
        GlassEmpty                = 0xedb8
        Glasses                   = 0xedb9
        GlassesRound              = 0xedba
        GlassHalf                 = 0xedbb
        GlassWater                = 0xedbc
        GlassWaterDroplet         = 0xedbd
        Globe                     = 0xedbe
        GlobePointer              = 0xedbf
        GlobeSnow                 = 0xedc0
        GlobeStand                = 0xedc1
        GoalNet                   = 0xedc2
        GolfBallTee               = 0xedc3
        GolfClub                  = 0xedc4
        GolfFlagHole              = 0xedc5
        Gopuram                   = 0xedc6
        GraduationCap             = 0xedc7
        Gramophone                = 0xedc8
        Grapes                    = 0xedc9
        Grate                     = 0xedca
        GrateDroplet              = 0xedcb
        GreaterThan               = 0xedcc
        GreaterThanEqual          = 0xedcd
        Grid                      = 0xedce
        Grid2                     = 0xedcf
        Grid2Plus                 = 0xedd0
        Grid4                     = 0xedd1
        Grid5                     = 0xedd2
        GridDividers              = 0xedd3
        GridHorizontal            = 0xedd4
        GridRound                 = 0xedd5
        GridRound2                = 0xedd6
        GridRound2Plus            = 0xedd7
        GridRound4                = 0xedd8
        GridRound5                = 0xedd9
        Grill                     = 0xedda
        GrillFire                 = 0xeddb
        GrillHot                  = 0xeddc
        Grip                      = 0xeddd
        GripDots                  = 0xedde
        GripDotsVertical          = 0xeddf
        GripLines                 = 0xede0
        GripVertical              = 0xede1
        GripLinesVertical         = 0xede2
        GroupArrowsRotate         = 0xede3
        Gun                       = 0xede4
        GuitarElectric            = 0xede5
        Guitars                   = 0xede6
        Guitar                    = 0xede7
        GuaraniSign               = 0xede8
        GunSlash                  = 0xede9
        GunSquirt                 = 0xedea
        H                         = 0xedeb
        H1                        = 0xedec
        H2                        = 0xeded
        H3                        = 0xedee
        H4                        = 0xedef
        H5                        = 0xedf0
        H6                        = 0xedf1
        Hammer                    = 0xedf2
        HammerBrush               = 0xedf3
        HammerCrash               = 0xedf4
        HammerWar                 = 0xedf5
        Hamsa                     = 0xedf6
        Hand                      = 0xedf7
        HandBackFist              = 0xedf8
        HandBackPointDown         = 0xedf9
        HandBackPointLeft         = 0xedfa
        HandBackPointRibbon       = 0xedfb
        HandBackPointRight        = 0xedfc
        HandBackPointUp           = 0xedfd
        Handcuffs                 = 0xedfe
        HandDots                  = 0xedff
        HandFingersCrossed        = 0xee00
        HandFist                  = 0xee01
        HandHeart                 = 0xee02
        HandHolding               = 0xee03
        HandHoldingBox            = 0xee04
        HandHoldingCircleDollar   = 0xee05
        HandHoldingDollar         = 0xee06
        HandHoldingDroplet        = 0xee07
        HandHoldingHand           = 0xee08
        HandHoldingHeart          = 0xee09
        HandHoldingMagic          = 0xee0a
        HandHoldingMedical        = 0xee0b
        HandHoldingSeedling       = 0xee0c
        HandHoldingSkull          = 0xee0d
        HandHorns                 = 0xee0e
        HandLizard                = 0xee0f
        HandLove                  = 0xee10
        HandMiddleFinger          = 0xee11
        HandPeace                 = 0xee12
        HandPointDown             = 0xee13
        HandPointer               = 0xee14
        HandPointLeft             = 0xee15
        HandPointRibbon           = 0xee16
        HandPointRight            = 0xee17
        HandPointUp               = 0xee18
        Hands                     = 0xee19
        HandsAslInterpreting      = 0xee1a
        HandsBound                = 0xee1b
        HandsBubbles              = 0xee1c
        HandScissors              = 0xee1d
        HandsClapping             = 0xee1e
        Handshake                 = 0xee1f
        HandshakeAngle            = 0xee20
        HandshakeSimple           = 0xee21
        HandshakeSimpleSlash      = 0xee22
        HandshakeSlash            = 0xee23
        HandsHolding              = 0xee24
        HandsHoldingChild         = 0xee25
        HandsHoldingCircle        = 0xee26
        HandsHoldingDiamond       = 0xee27
        HandsHoldingDollar        = 0xee28
        HandsHoldingHeart         = 0xee29
        HandSparkles              = 0xee2a
        HandSpock                 = 0xee2b
        HandsPraying              = 0xee2c
        HandWave                  = 0xee2d
        Hanukiah                  = 0xee2e
        HardDrive                 = 0xee2f
        Hashtag                   = 0xee30
        HashtagLock               = 0xee31
        HatBeach                  = 0xee32
        HatChef                   = 0xee33
        HatCowboy                 = 0xee34
        HatCowboySide             = 0xee35
        HatSanta                  = 0xee36
        HatWinter                 = 0xee37
        HatWitch                  = 0xee38
        HatWizard                 = 0xee39
        Heading                   = 0xee3a
        Headphones                = 0xee3b
        HeadphonesSimple          = 0xee3c
        Headset                   = 0xee3d
        HeadSide                  = 0xee3e
        HeadSideBrain             = 0xee3f
        HeadSideCough             = 0xee40
        HeadSideCoughSlash        = 0xee41
        HeadSideGear              = 0xee42
        HeadSideGoggles           = 0xee43
        HeadSideHeadphones        = 0xee44
        HeadSideHeart             = 0xee45
        HeadSideMask              = 0xee46
        HeadSideMedical           = 0xee47
        HeadSideVirus             = 0xee48
        Heart                     = 0xee49
        HeartCircleBolt           = 0xee4a
        HeartCircleCheck          = 0xee4b
        HeartCircleExclamation    = 0xee4c
        HeartCircleMinus          = 0xee4d
        HeartCirclePlus           = 0xee4e
        HeartCircleXmark          = 0xee4f
        HeartCrack                = 0xee50
        HeartHalf                 = 0xee51
        HeartHalfStroke           = 0xee52
        HeartPulse                = 0xee53
        Heat                      = 0xee54
        Helicopter                = 0xee55
        HelicopterSymbol          = 0xee56
        HelmetBattle              = 0xee57
        HelmetSafety              = 0xee58
        HelmetUn                  = 0xee59
        Hexagon                   = 0xee5a
        HexagonCheck              = 0xee5b
        HexagonDivide             = 0xee5c
        HexagonExclamation        = 0xee5d
        HexagonImage              = 0xee5e
        HexagonMinus              = 0xee5f
        HexagonPlus               = 0xee60
        HexagonVerticalNft        = 0xee61
        HexagonVerticalNftSlanted = 0xee62
        HexagonXmark              = 0xee63
        HighDefinition            = 0xee64
        Highlighter               = 0xee65
        HighlighterLine           = 0xee66
        HillAvalanche             = 0xee67
        HillRockslide             = 0xee68
        Hippo                     = 0xee69
        HockeyMask                = 0xee6a
        HockeyPuck                = 0xee6b
        HockeyStickPuck           = 0xee6c
        HockeySticks              = 0xee6d
        HollyBerry                = 0xee6e
        HoneyPot                  = 0xee6f
        HoodCloak                 = 0xee70
        HorizontalRule            = 0xee71
        Horse                     = 0xee72
        HorseHead                 = 0xee73
        HorseSaddle               = 0xee74
        Hose                      = 0xee75
        HoseReel                  = 0xee76
        Hospital                  = 0xee77
        Hospitals                 = 0xee78
        HospitalUser              = 0xee79
        P                         = 0xee7a
        Hotel                     = 0xee7b
        HotTubPerson              = 0xee7c
        Hourglass                 = 0xee7d
        HourglassClock            = 0xee7e
        HourglassEnd              = 0xee7f
        HourglassHalf             = 0xee80
        HourglassStart            = 0xee81
        House                     = 0xee82
        HouseBlank                = 0xee83
        HouseBuilding             = 0xee84
        HouseChimney              = 0xee85
        HouseChimneyBlank         = 0xee86
        HouseChimneyCrack         = 0xee87
        HouseChimneyHeart         = 0xee88
        HouseChimneyUser          = 0xee89
        HouseChimneyWindow        = 0xee8a
        HouseChimneyMedical       = 0xee8b
        HouseCircleCheck          = 0xee8c
        HouseCircleExclamation    = 0xee8d
        HouseCircleXmark          = 0xee8e
        HouseDay                  = 0xee8f
        HouseCrack                = 0xee90
        HouseFire                 = 0xee91
        HouseFlag                 = 0xee92
        HouseFloodWater           = 0xee93
        HouseFloodWaterCircleArrowRight = 0xee94
        HouseHeart                = 0xee95
        HouseLaptop               = 0xee96
        HouseLock                 = 0xee97
        HouseMedical              = 0xee98
        HouseMedicalCircleCheck   = 0xee99
        HouseMedicalCircleExclamation = 0xee9a
        HouseMedicalCircleXmark   = 0xee9b
        HouseMedicalFlag          = 0xee9c
        HouseNight                = 0xee9d
        HousePersonLeave          = 0xee9e
        HousePersonReturn         = 0xee9f
        HouseSignal               = 0xeea0
        HouseTree                 = 0xeea1
        HouseTsunami              = 0xeea2
        HouseTurret               = 0xeea3
        HouseUser                 = 0xeea4
        HouseWater                = 0xeea5
        HouseWindow               = 0xeea6
        HryvniaSign               = 0xeea7
        HundredPoints             = 0xeea8
        Hurricane                 = 0xeea9
        Hyphen                    = 0xeeaa
        I                         = 0xeeab
        IceCream                  = 0xeeac
        IceSkate                  = 0xeead
        Icicles                   = 0xeeae
        Icons                     = 0xeeaf
        ICursor                   = 0xeeb0
        IdBadge                   = 0xeeb1
        IdCard                    = 0xeeb2
        IdCardClip                = 0xeeb3
        Igloo                     = 0xeeb4
        Image                     = 0xeeb5
        ImageLandscape            = 0xeeb6
        ImagePolaroid             = 0xeeb7
        ImagePolaroidUser         = 0xeeb8
        ImagePortrait             = 0xeeb9
        Images                    = 0xeeba
        ImageSlash                = 0xeebb
        ImagesUser                = 0xeebc
        ImageUser                 = 0xeebd
        Inboxes                   = 0xeebe
        InboxFull                 = 0xeebf
        InboxIn                   = 0xeec0
        Inbox                     = 0xeec1
        IndianRupeeSign           = 0xeec2
        Industry                  = 0xeec3
        InboxOut                  = 0xeec4
        IndustryWindows           = 0xeec5
        Infinity                  = 0xeec6
        Indent                    = 0xeec7
        Info                      = 0xeec8
        Inhaler                   = 0xeec9
        InputNumeric              = 0xeeca
        InputPipe                 = 0xeecb
        InputText                 = 0xeecc
        Integral                  = 0xeecd
        Interrobang               = 0xeece
        Intersection              = 0xeecf
        J                         = 0xeed0
        JackOLantern              = 0xeed1
        Jar                       = 0xeed2
        Italic                    = 0xeed3
        IslandTropical            = 0xeed4
        JarWheat                  = 0xeed5
        Jedi                      = 0xeed6
        JetFighter                = 0xeed7
        Joystick                  = 0xeed8
        Jug                       = 0xeed9
        JetFighterUp              = 0xeeda
        Joint                     = 0xeedb
        JugDetergent              = 0xeedc
        JugBottle                 = 0xeedd
        K                         = 0xeede
        Kaaba                     = 0xeedf
        Kazoo                     = 0xeee0
        Kerning                   = 0xeee1
        Key                       = 0xeee2
        Keyboard                  = 0xeee3
        KeyboardBrightness        = 0xeee4
        KeyboardBrightnessLow     = 0xeee5
        KeyboardDown              = 0xeee6
        KeyboardLeft              = 0xeee7
        Keynote                   = 0xeee8
        KeySkeleton               = 0xeee9
        KeySkeletonLeftRight      = 0xeeea
        Khanda                    = 0xeeeb
        Kidneys                   = 0xeeec
        KipSign                   = 0xeeed
        KitchenSet                = 0xeeee
        Kite                      = 0xeeef
        KitMedical                = 0xeef0
        KiwiBird                  = 0xeef1
        KiwiFruit                 = 0xeef2
        Knife                     = 0xeef3
        KnifeKitchen              = 0xeef4
        L                         = 0xeef5
        LacrosseStick             = 0xeef6
        LacrosseStickBall         = 0xeef7
        Lambda                    = 0xeef8
        Lamp                      = 0xeef9
        LampDesk                  = 0xeefa
        LampFloor                 = 0xeefb
        LampStreet                = 0xeefc
        Landmark                  = 0xeefd
        LandmarkDome              = 0xeefe
        LandmarkFlag              = 0xeeff
        LandmarkMagnifyingGlass   = 0xef00
        LandMineOn                = 0xef01
        Language                  = 0xef02
        Laptop                    = 0xef03
        LaptopArrowDown           = 0xef04
        LaptopBinary              = 0xef05
        LaptopCode                = 0xef06
        LaptopFile                = 0xef07
        LaptopMedical             = 0xef08
        LaptopMobile              = 0xef09
        LaptopSlash               = 0xef0a
        LariSign                  = 0xef0b
        Lasso                     = 0xef0c
        LassoSparkles             = 0xef0d
        LayerGroup                = 0xef0e
        LayerMinus                = 0xef0f
        LayerPlus                 = 0xef10
        Leaf                      = 0xef11
        LeafHeart                 = 0xef12
        LeafMaple                 = 0xef13
        LeafOak                   = 0xef14
        LeafyGreen                = 0xef15
        Left                      = 0xef16
        LeftFromLine              = 0xef17
        LeftLong                  = 0xef18
        LeftLongToLine            = 0xef19
        LeftRight                 = 0xef1a
        LeftToLine                = 0xef1b
        Lemon                     = 0xef1c
        LessThan                  = 0xef1d
        LessThanEqual             = 0xef1e
        LifeRing                  = 0xef1f
        Lightbulb                 = 0xef20
        LightbulbCfl              = 0xef21
        LightbulbCflOn            = 0xef22
        LightbulbDollar           = 0xef23
        LightbulbExclamation      = 0xef24
        LightbulbExclamationOn    = 0xef25
        LightbulbGear             = 0xef26
        LightbulbOn               = 0xef27
        LightbulbSlash            = 0xef28
        LightCeiling              = 0xef29
        LightEmergency            = 0xef2a
        LightEmergencyOn          = 0xef2b
        Lighthouse                = 0xef2c
        LightsHoliday             = 0xef2d
        LightSwitch               = 0xef2e
        LightSwitchOff            = 0xef2f
        LightSwitchOn             = 0xef30
        LineColumns               = 0xef31
        LineHeight                = 0xef32
        LinesLeaning              = 0xef33
        Link                      = 0xef34
        LinkHorizontal            = 0xef35
        LinkHorizontalSlash       = 0xef36
        LinkSimple                = 0xef37
        LinkSimpleSlash           = 0xef38
        LinkSlash                 = 0xef39
        Lips                      = 0xef3a
        LiraSign                  = 0xef3b
        List                      = 0xef3c
        ListCheck                 = 0xef3d
        ListDropdown              = 0xef3e
        ListMusic                 = 0xef3f
        ListOl                    = 0xef40
        ListRadio                 = 0xef41
        ListTimeline              = 0xef42
        ListTree                  = 0xef43
        ListUl                    = 0xef44
        LitecoinSign              = 0xef45
        Loader                    = 0xef46
        Lobster                   = 0xef47
        LocationArrow             = 0xef48
        LocationArrowUp           = 0xef49
        LocationCheck             = 0xef4a
        LocationCrosshairs        = 0xef4b
        LocationCrosshairsSlash   = 0xef4c
        LocationDot               = 0xef4d
        LocationDotSlash          = 0xef4e
        LocationExclamation       = 0xef4f
        LocationMinus             = 0xef50
        LocationPen               = 0xef51
        LocationPin               = 0xef52
        LocationPinLock           = 0xef53
        LocationPinSlash          = 0xef54
        LocationPlus              = 0xef55
        LocationQuestion          = 0xef56
        LocationSmile             = 0xef57
        LocationXmark             = 0xef58
        Lock                      = 0xef59
        LockA                     = 0xef5a
        LockHashtag               = 0xef5b
        LockKeyhole               = 0xef5c
        LockKeyholeOpen           = 0xef5d
        LockOpen                  = 0xef5e
        Locust                    = 0xef5f
        Lollipop                  = 0xef60
        Loveseat                  = 0xef61
        LuchadorMask              = 0xef62
        Lungs                     = 0xef63
        LungsVirus                = 0xef64
        M                         = 0xef65
        Mace                      = 0xef66
        Magnet                    = 0xef67
        MagnifyingGlass           = 0xef68
        MagnifyingGlassArrowRight = 0xef69
        MagnifyingGlassArrowsRotate = 0xef6a
        MagnifyingGlassChart      = 0xef6b
        MagnifyingGlassDollar     = 0xef6c
        MagnifyingGlassLocation   = 0xef6d
        MagnifyingGlassMinus      = 0xef6e
        MagnifyingGlassMusic      = 0xef6f
        MagnifyingGlassPlay       = 0xef70
        MagnifyingGlassPlus       = 0xef71
        MagnifyingGlassWaveform   = 0xef72
        Mailbox                   = 0xef73
        MailboxFlagUp             = 0xef74
        ManatSign                 = 0xef75
        Mandolin                  = 0xef76
        Mango                     = 0xef77
        Manhole                   = 0xef78
        Map                       = 0xef79
        MapLocation               = 0xef7a
        MapLocationDot            = 0xef7b
        MapPin                    = 0xef7c
        Marker                    = 0xef7d
        Mars                      = 0xef7e
        MarsAndVenus              = 0xef7f
        MarsAndVenusBurst         = 0xef80
        MarsDouble                = 0xef81
        MarsStroke                = 0xef82
        MarsStrokeRight           = 0xef83
        MarsStrokeUp              = 0xef84
        MartiniGlass              = 0xef85
        MartiniGlassCitrus        = 0xef86
        MartiniGlassEmpty         = 0xef87
        Mask                      = 0xef88
        MaskFace                  = 0xef89
        MaskSnorkel               = 0xef8a
        MasksTheater              = 0xef8b
        MaskVentilator            = 0xef8c
        MattressPillow            = 0xef8d
        Maximize                  = 0xef8e
        Meat                      = 0xef8f
        Medal                     = 0xef90
        Megaphone                 = 0xef91
        Melon                     = 0xef92
        MelonSlice                = 0xef93
        Memo                      = 0xef94
        MemoCircleCheck           = 0xef95
        MemoCircleInfo            = 0xef96
        MemoPad                   = 0xef97
        Memory                    = 0xef98
        Menorah                   = 0xef99
        Mercury                   = 0xef9a
        Merge                     = 0xef9b
        Message                   = 0xef9c
        MessageArrowDown          = 0xef9d
        MessageArrowUp            = 0xef9e
        MessageArrowUpRight       = 0xef9f
        MessageBot                = 0xefa0
        MessageCaptions           = 0xefa1
        MessageCheck              = 0xefa2
        MessageCode               = 0xefa3
        MessageDollar             = 0xefa4
        MessageDots               = 0xefa5
        MessageExclamation        = 0xefa6
        MessageHeart              = 0xefa7
        MessageImage              = 0xefa8
        MessageLines              = 0xefa9
        MessageMedical            = 0xefaa
        MessageMiddle             = 0xefab
        MessageMiddleTop          = 0xefac
        MessageMinus              = 0xefad
        MessageMusic              = 0xefae
        MessagePen                = 0xefaf
        MessagePlus               = 0xefb0
        MessageQuestion           = 0xefb1
        MessageQuote              = 0xefb2
        Messages                  = 0xefb3
        MessagesDollar            = 0xefb4
        MessageSlash              = 0xefb5
        MessageSmile              = 0xefb6
        MessageSms                = 0xefb7
        MessagesQuestion          = 0xefb8
        MessageText               = 0xefb9
        MessageXmark              = 0xefba
        Meteor                    = 0xefbb
        Meter                     = 0xefbc
        MeterBolt                 = 0xefbd
        MeterDroplet              = 0xefbe
        MeterFire                 = 0xefbf
        Microchip                 = 0xefc0
        MicrochipAi               = 0xefc1
        Microphone                = 0xefc2
        MicrophoneLines           = 0xefc3
        MicrophoneLinesSlash      = 0xefc4
        MicrophoneSlash           = 0xefc5
        MicrophoneStand           = 0xefc6
        Microscope                = 0xefc7
        Microwave                 = 0xefc8
        MillSign                  = 0xefc9
        Minimize                  = 0xefca
        Minus                     = 0xefcb
        Mistletoe                 = 0xefcc
        Mitten                    = 0xefcd
        Mobile                    = 0xefce
        MobileButton              = 0xefcf
        MobileNotch               = 0xefd0
        MobileRetro               = 0xefd1
        MobileScreen              = 0xefd2
        MobileScreenButton        = 0xefd3
        MobileSignal              = 0xefd4
        MobileSignalOut           = 0xefd5
        MoneyBill                 = 0xefd6
        MoneyBill1                = 0xefd7
        MoneyBill1Wave            = 0xefd8
        MoneyBills                = 0xefd9
        MoneyBillSimple           = 0xefda
        MoneyBillSimpleWave       = 0xefdb
        MoneyBillsSimple          = 0xefdc
        MoneyBillTransfer         = 0xefdd
        MoneyBillTrendUp          = 0xefde
        MoneyBillWave             = 0xefdf
        MoneyBillWheat            = 0xefe0
        MoneyCheck                = 0xefe1
        MoneyCheckDollar          = 0xefe2
        MoneyCheckDollarPen       = 0xefe3
        MoneyCheckPen             = 0xefe4
        MoneyFromBracket          = 0xefe5
        MoneySimpleFromBracket    = 0xefe6
        MonitorWaveform           = 0xefe7
        Monkey                    = 0xefe8
        Monument                  = 0xefe9
        Moon                      = 0xefea
        MoonCloud                 = 0xefeb
        MoonOverSun               = 0xefec
        MoonStars                 = 0xefed
        Moped                     = 0xefee
        MortarPestle              = 0xefef
        Mosque                    = 0xeff0
        Mosquito                  = 0xeff1
        MosquitoNet               = 0xeff2
        Motorcycle                = 0xeff3
        Mound                     = 0xeff4
        Mountain                  = 0xeff5
        MountainCity              = 0xeff6
        Mountains                 = 0xeff7
        MountainSun               = 0xeff8
        MouseField                = 0xeff9
        Mp3Player                 = 0xeffa
        Mug                       = 0xeffb
        MugHot                    = 0xeffc
        MugMarshmallows           = 0xeffd
        MugSaucer                 = 0xeffe
        MugTea                    = 0xefff
        MugTeaSaucer              = 0xf000
        Mushroom                  = 0xf001
        Music                     = 0xf002
        MusicMagnifyingGlass      = 0xf003
        MusicNote                 = 0xf004
        MusicNoteSlash            = 0xf005
        MusicSlash                = 0xf006
        Mustache                  = 0xf007
        N                         = 0xf008
        NairaSign                 = 0xf009
        Narwhal                   = 0xf00a
        NestingDolls              = 0xf00b
        NetworkWired              = 0xf00c
        Neuter                    = 0xf00d
        Newspaper                 = 0xf00e
        Nfc                       = 0xf00f
        NfcLock                   = 0xf010
        NfcMagnifyingGlass        = 0xf011
        NfcPen                    = 0xf012
        NfcSignal                 = 0xf013
        NfcSlash                  = 0xf014
        NfcSymbol                 = 0xf015
        NfcTrash                  = 0xf016
        Nose                      = 0xf017
        Notdef                    = 0xf018
        Note                      = 0xf019
        Notebook                  = 0xf01a
        NoteMedical               = 0xf01b
        NotEqual                  = 0xf01c
        Notes                     = 0xf01d
        NotesMedical              = 0xf01e
        NoteSticky                = 0xf01f
        O                         = 0xf020
        ObjectExclude             = 0xf021
        ObjectGroup               = 0xf022
        ObjectIntersect           = 0xf023
        ObjectsAlignBottom        = 0xf024
        ObjectsAlignCenterHorizontal = 0xf025
        ObjectsAlignCenterVertical = 0xf026
        ObjectsAlignLeft          = 0xf027
        ObjectsAlignRight         = 0xf028
        ObjectsAlignTop           = 0xf029
        ObjectsColumn             = 0xf02a
        ObjectSubtract            = 0xf02b
        ObjectUngroup             = 0xf02c
        ObjectUnion               = 0xf02d
        Octagon                   = 0xf02e
        OctagonCheck              = 0xf02f
        OctagonDivide             = 0xf030
        OctagonExclamation        = 0xf031
        OctagonMinus              = 0xf032
        OctagonPlus               = 0xf033
        OctagonXmark              = 0xf034
        OilCan                    = 0xf035
        OilCanDrip                = 0xf036
        OilTemperature            = 0xf037
        OilWell                   = 0xf038
        Olive                     = 0xf039
        OliveBranch               = 0xf03a
        Om                        = 0xf03b
        Omega                     = 0xf03c
        Onion                     = 0xf03d
        Option                    = 0xf03e
        Ornament                  = 0xf03f
        Otter                     = 0xf040
        Outdent                   = 0xf041
        Outlet                    = 0xf042
        Oven                      = 0xf043
        Overline                  = 0xf044
        SignalSlash               = 0xf045
        PageCaretDown             = 0xf046
        Page                      = 0xf047
        PageCaretUp               = 0xf048
        Pager                     = 0xf049
        Paintbrush                = 0xf04a
        PaintbrushFine            = 0xf04b
        PaintbrushPencil          = 0xf04c
        PaintRoller               = 0xf04d
        Pallet                    = 0xf04e
        Palette                   = 0xf04f
        PalletBox                 = 0xf050
        PalletBoxes               = 0xf051
        Pancakes                  = 0xf052
        PanelEws                  = 0xf053
        PanelFire                 = 0xf054
        PanFood                   = 0xf055
        PanFrying                 = 0xf056
        Panorama                  = 0xf057
        Paperclip                 = 0xf058
        PaperclipVertical         = 0xf059
        PaperPlane                = 0xf05a
        PaperPlaneTop             = 0xf05b
        ParachuteBox              = 0xf05c
        Paragraph                 = 0xf05d
        PartyBell                 = 0xf05e
        ParagraphLeft             = 0xf05f
        PartyHorn                 = 0xf060
        Passport                  = 0xf061
        Paste                     = 0xf062
        Pause                     = 0xf063
        Paw                       = 0xf064
        PawClaws                  = 0xf065
        PawSimple                 = 0xf066
        Peace                     = 0xf067
        Peach                     = 0xf068
        Peanut                    = 0xf069
        Peanuts                   = 0xf06a
        Peapod                    = 0xf06b
        Pear                      = 0xf06c
        Pedestal                  = 0xf06d
        Pegasus                   = 0xf06e
        Pen                       = 0xf06f
        Pencil                    = 0xf070
        PencilMechanical          = 0xf071
        PencilSlash               = 0xf072
        PenCircle                 = 0xf073
        PenClip                   = 0xf074
        PenClipSlash              = 0xf075
        PenFancy                  = 0xf076
        PenFancySlash             = 0xf077
        PenField                  = 0xf078
        PenNib                    = 0xf079
        PenLine                   = 0xf07a
        PenNibSlash               = 0xf07b
        PenPaintbrush             = 0xf07c
        PenRuler                  = 0xf07d
        PenSlash                  = 0xf07e
        PenSwirl                  = 0xf07f
        PenToSquare               = 0xf080
        People                    = 0xf081
        PeopleArrows              = 0xf082
        PeopleCarryBox            = 0xf083
        PeopleDress               = 0xf084
        PeopleDressSimple         = 0xf085
        PeopleGroup               = 0xf086
        PeopleLine                = 0xf087
        PeoplePants               = 0xf088
        PeoplePantsSimple         = 0xf089
        PeoplePulling             = 0xf08a
        PeopleRobbery             = 0xf08b
        PeopleRoof                = 0xf08c
        PeopleSimple              = 0xf08d
        Pepper                    = 0xf08e
        PepperHot                 = 0xf08f
        Person                    = 0xf090
        Percent                   = 0xf091
        Period                    = 0xf092
        PersonArrowDownToLine     = 0xf093
        PersonBiking              = 0xf094
        PersonArrowUpFromLine     = 0xf095
        PersonBikingMountain      = 0xf096
        PersonBooth               = 0xf097
        PersonBreastfeeding       = 0xf098
        PersonBurst               = 0xf099
        PersonCane                = 0xf09a
        PersonCarryBox            = 0xf09b
        PersonChalkboard          = 0xf09c
        PersonCircleCheck         = 0xf09d
        PersonCircleExclamation   = 0xf09e
        PersonCircleMinus         = 0xf09f
        PersonCirclePlus          = 0xf0a0
        PersonCircleQuestion      = 0xf0a1
        PersonCircleXmark         = 0xf0a2
        PersonDigging             = 0xf0a3
        PersonDollyEmpty          = 0xf0a4
        PersonDotsFromLine        = 0xf0a5
        PersonDressBurst          = 0xf0a6
        PersonDress               = 0xf0a7
        PersonDolly               = 0xf0a8
        PersonDressFairy          = 0xf0a9
        PersonDressSimple         = 0xf0aa
        PersonDrowning            = 0xf0ab
        PersonFairy               = 0xf0ac
        PersonFalling             = 0xf0ad
        PersonFallingBurst        = 0xf0ae
        PersonFromPortal          = 0xf0af
        PersonHalfDress           = 0xf0b0
        PersonHarassing           = 0xf0b1
        PersonHiking              = 0xf0b2
        PersonMilitaryPointing    = 0xf0b3
        PersonMilitaryRifle       = 0xf0b4
        PersonMilitaryToPerson    = 0xf0b5
        PersonPinball             = 0xf0b6
        PersonPraying             = 0xf0b7
        PersonPregnant            = 0xf0b8
        PersonRays                = 0xf0b9
        PersonRifle               = 0xf0ba
        PersonRunning             = 0xf0bb
        PersonRunningFast         = 0xf0bc
        PersonSeat                = 0xf0bd
        PersonSeatReclined        = 0xf0be
        PersonShelter             = 0xf0bf
        PersonSign                = 0xf0c0
        PersonSimple              = 0xf0c1
        PersonSkating             = 0xf0c2
        PersonSkiing              = 0xf0c3
        PersonSkiingNordic        = 0xf0c4
        PersonSkiJumping          = 0xf0c5
        PersonSkiLift             = 0xf0c6
        PersonSledding            = 0xf0c7
        PersonSnowboarding        = 0xf0c8
        PersonSnowmobiling        = 0xf0c9
        PersonSwimming            = 0xf0ca
        PersonThroughWindow       = 0xf0cb
        PersonToDoor              = 0xf0cc
        PersonToPortal            = 0xf0cd
        PersonWalking             = 0xf0ce
        PersonWalkingArrowLoopLeft = 0xf0cf
        PersonWalkingArrowRight   = 0xf0d0
        PersonWalkingDashedLineArrowRight = 0xf0d1
        PersonWalkingLuggage      = 0xf0d2
        PersonWalkingWithCane     = 0xf0d3
        PesetaSign                = 0xf0d4
        PesoSign                  = 0xf0d5
        Phone                     = 0xf0d6
        PhoneArrowDownLeft        = 0xf0d7
        PhoneArrowRight           = 0xf0d8
        PhoneArrowUpRight         = 0xf0d9
        PhoneFlip                 = 0xf0da
        PhoneHangup               = 0xf0db
        PhoneIntercom             = 0xf0dc
        PhoneMissed               = 0xf0dd
        PhoneOffice               = 0xf0de
        PhonePlus                 = 0xf0df
        PhoneRotary               = 0xf0e0
        PhoneSlash                = 0xf0e1
        PhoneVolume               = 0xf0e2
        PhoneXmark                = 0xf0e3
        PhotoFilm                 = 0xf0e4
        PhotoFilmMusic            = 0xf0e5
        Pi                        = 0xf0e6
        Piano                     = 0xf0e7
        PiggyBank                 = 0xf0e8
        Pig                       = 0xf0e9
        PianoKeyboard             = 0xf0ea
        Pickaxe                   = 0xf0eb
        Pinata                    = 0xf0ec
        Pinball                   = 0xf0ed
        Pie                       = 0xf0ee
        Pills                     = 0xf0ef
        Pickleball                = 0xf0f0
        Pineapple                 = 0xf0f1
        Pipe                      = 0xf0f2
        PipeCircleCheck           = 0xf0f3
        PipeCollar                = 0xf0f4
        PipeSection               = 0xf0f5
        PipeSmoking               = 0xf0f6
        PipeValve                 = 0xf0f7
        Pizza                     = 0xf0f8
        PizzaSlice                = 0xf0f9
        PlaceOfWorship            = 0xf0fa
        Plane                     = 0xf0fb
        PlaneArrival              = 0xf0fc
        PlaneCircleCheck          = 0xf0fd
        PlaneCircleExclamation    = 0xf0fe
        PlaneCircleXmark          = 0xf0ff
        PlaneDeparture            = 0xf100
        PlaneEngines              = 0xf101
        PlaneLock                 = 0xf102
        PlaneProp                 = 0xf103
        PlaneSlash                = 0xf104
        PlaneTail                 = 0xf105
        PlanetMoon                = 0xf106
        PlanetRinged              = 0xf107
        PlaneUp                   = 0xf108
        PlaneUpSlash              = 0xf109
        PlantWilt                 = 0xf10a
        PlateUtensils             = 0xf10b
        PlateWheat                = 0xf10c
        Play                      = 0xf10d
        PlayPause                 = 0xf10e
        Plug                      = 0xf10f
        PlugCircleBolt            = 0xf110
        PlugCircleCheck           = 0xf111
        PlugCircleExclamation     = 0xf112
        PlugCircleMinus           = 0xf113
        PlugCirclePlus            = 0xf114
        PlugCircleXmark           = 0xf115
        Plus                      = 0xf116
        PlusLarge                 = 0xf117
        PlusMinus                 = 0xf118
        Podcast                   = 0xf119
        Podium                    = 0xf11a
        PodiumStar                = 0xf11b
        PoliceBox                 = 0xf11c
        PollPeople                = 0xf11d
        Pompebled                 = 0xf11e
        Poo                       = 0xf11f
        Pool8Ball                 = 0xf120
        Poop                      = 0xf121
        PooStorm                  = 0xf122
        Popcorn                   = 0xf123
        Popsicle                  = 0xf124
        Potato                    = 0xf125
        PotFood                   = 0xf126
        PowerOff                  = 0xf127
        Prescription              = 0xf128
        PrescriptionBottle        = 0xf129
        PrescriptionBottleMedical = 0xf12a
        PrescriptionBottlePill    = 0xf12b
        PresentationScreen        = 0xf12c
        Pretzel                   = 0xf12d
        Print                     = 0xf12e
        PrintMagnifyingGlass      = 0xf12f
        PrintSlash                = 0xf130
        Projector                 = 0xf131
        Pump                      = 0xf132
        Pumpkin                   = 0xf133
        PumpMedical               = 0xf134
        PumpSoap                  = 0xf135
        Puzzle                    = 0xf136
        PuzzlePiece               = 0xf137
        PuzzlePieceSimple         = 0xf138
        Q                         = 0xf139
        Qrcode                    = 0xf13a
        Question                  = 0xf13b
        QuoteLeft                 = 0xf13c
        QuoteRight                = 0xf13d
        Quotes                    = 0xf13e
        R                         = 0xf13f
        Rabbit                    = 0xf140
        RabbitRunning             = 0xf141
        Raccoon                   = 0xf142
        Racquet                   = 0xf143
        Radar                     = 0xf144
        Radiation                 = 0xf145
        Radio                     = 0xf146
        RadioTuner                = 0xf147
        Rainbow                   = 0xf148
        Raindrops                 = 0xf149
        Ram                       = 0xf14a
        RampLoading               = 0xf14b
        RankingStar               = 0xf14c
        Raygun                    = 0xf14d
        Receipt                   = 0xf14e
        RecordVinyl               = 0xf14f
        Rectangle                 = 0xf150
        RectangleAd               = 0xf151
        RectangleBarcode          = 0xf152
        RectangleCode             = 0xf153
        RectangleHistory          = 0xf154
        RectangleHistoryCirclePlus = 0xf155
        RectangleHistoryCircleUser = 0xf156
        RectangleList             = 0xf157
        RectanglePro              = 0xf158
        RectanglesMixed           = 0xf159
        RectangleTerminal         = 0xf15a
        RectangleVertical         = 0xf15b
        RectangleVerticalHistory  = 0xf15c
        RectangleWide             = 0xf15d
        RectangleXmark            = 0xf15e
        Recycle                   = 0xf15f
        Reel                      = 0xf160
        ReflectHorizontal         = 0xf161
        ReflectVertical           = 0xf162
        Refrigerator              = 0xf163
        Registered                = 0xf164
        Repeat                    = 0xf165
        Repeat1                   = 0xf166
        Reply                     = 0xf167
        ReplyAll                  = 0xf168
        ReplyClock                = 0xf169
        Republican                = 0xf16a
        Restroom                  = 0xf16b
        RestroomSimple            = 0xf16c
        Retweet                   = 0xf16d
        Rhombus                   = 0xf16e
        Ribbon                    = 0xf16f
        Right                     = 0xf170
        RightFromBracket          = 0xf171
        RightFromLine             = 0xf172
        RightLeft                 = 0xf173
        RightLeftLarge            = 0xf174
        RightLong                 = 0xf175
        RightLongToLine           = 0xf176
        RightToBracket            = 0xf177
        RightToLine               = 0xf178
        Ring                      = 0xf179
        RingDiamond               = 0xf17a
        RingsWedding              = 0xf17b
        Road                      = 0xf17c
        RoadBarrier               = 0xf17d
        RoadBridge                = 0xf17e
        RoadCircleCheck           = 0xf17f
        RoadCircleExclamation     = 0xf180
        RoadCircleXmark           = 0xf181
        RoadLock                  = 0xf182
        RoadSpikes                = 0xf183
        Robot                     = 0xf184
        RobotAstromech            = 0xf185
        Rocket                    = 0xf186
        RocketLaunch              = 0xf187
        RollerCoaster             = 0xf188
        Rotate                    = 0xf189
        RotateExclamation         = 0xf18a
        RotateLeft                = 0xf18b
        RotateReverse             = 0xf18c
        RotateRight               = 0xf18d
        Route                     = 0xf18e
        RouteHighway              = 0xf18f
        RouteInterstate           = 0xf190
        Router                    = 0xf191
        Rss                       = 0xf192
        RubleSign                 = 0xf193
        Rug                       = 0xf194
        RugbyBall                 = 0xf195
        Ruler                     = 0xf196
        RulerCombined             = 0xf197
        RulerHorizontal           = 0xf198
        RulerTriangle             = 0xf199
        RulerVertical             = 0xf19a
        RupeeSign                 = 0xf19b
        RupiahSign                = 0xf19c
        Rv                        = 0xf19d
        S                         = 0xf19e
        Sack                      = 0xf19f
        SackDollar                = 0xf1a0
        SackXmark                 = 0xf1a1
        Sailboat                  = 0xf1a2
        Salad                     = 0xf1a3
        SaltShaker                = 0xf1a4
        Sandwich                  = 0xf1a5
        Satellite                 = 0xf1a6
        SatelliteDish             = 0xf1a7
        Sausage                   = 0xf1a8
        Saxophone                 = 0xf1a9
        SaxophoneFire             = 0xf1aa
        ScaleBalanced             = 0xf1ab
        ScaleUnbalanced           = 0xf1ac
        ScaleUnbalancedFlip       = 0xf1ad
        Scalpel                   = 0xf1ae
        ScalpelLineDashed         = 0xf1af
        ScannerGun                = 0xf1b0
        ScannerImage              = 0xf1b1
        ScannerKeyboard           = 0xf1b2
        ScannerTouchscreen        = 0xf1b3
        Scarecrow                 = 0xf1b4
        Scarf                     = 0xf1b5
        School                    = 0xf1b6
        SchoolCircleCheck         = 0xf1b7
        SchoolCircleExclamation   = 0xf1b8
        SchoolCircleXmark         = 0xf1b9
        SchoolFlag                = 0xf1ba
        SchoolLock                = 0xf1bb
        Scissors                  = 0xf1bc
        Screencast                = 0xf1bd
        ScreenUsers               = 0xf1be
        Screwdriver               = 0xf1bf
        ScrewdriverWrench         = 0xf1c0
        Scribble                  = 0xf1c1
        Scroll                    = 0xf1c2
        ScrollOld                 = 0xf1c3
        ScrollTorah               = 0xf1c4
        Scrubber                  = 0xf1c5
        Scythe                    = 0xf1c6
        SdCard                    = 0xf1c7
        SdCards                   = 0xf1c8
        Seal                      = 0xf1c9
        SealExclamation           = 0xf1ca
        SealQuestion              = 0xf1cb
        SeatAirline               = 0xf1cc
        Section                   = 0xf1cd
        Seedling                  = 0xf1ce
        Semicolon                 = 0xf1cf
        SendBack                  = 0xf1d0
        SendBackward              = 0xf1d1
        Sensor                    = 0xf1d2
        SensorCloud               = 0xf1d3
        SensorFire                = 0xf1d4
        SensorOn                  = 0xf1d5
        SensorTriangleExclamation = 0xf1d6
        Server                    = 0xf1d7
        Shapes                    = 0xf1d8
        Share                     = 0xf1d9
        ShareAll                  = 0xf1da
        ShareFromSquare           = 0xf1db
        ShareNodes                = 0xf1dc
        Sheep                     = 0xf1dd
        SheetPlastic              = 0xf1de
        ShekelSign                = 0xf1df
        Shelves                   = 0xf1e0
        ShelvesEmpty              = 0xf1e1
        Shield                    = 0xf1e2
        ShieldCat                 = 0xf1e3
        ShieldCheck               = 0xf1e4
        ShieldCross               = 0xf1e5
        ShieldDog                 = 0xf1e6
        ShieldExclamation         = 0xf1e7
        ShieldHalved              = 0xf1e8
        ShieldHeart               = 0xf1e9
        ShieldKeyhole             = 0xf1ea
        ShieldMinus               = 0xf1eb
        ShieldPlus                = 0xf1ec
        ShieldQuartered           = 0xf1ed
        ShieldSlash               = 0xf1ee
        ShieldVirus               = 0xf1ef
        ShieldXmark               = 0xf1f0
        Ship                      = 0xf1f1
        Shirt                     = 0xf1f2
        ShirtLongSleeve           = 0xf1f3
        ShirtRunning              = 0xf1f4
        ShirtTankTop              = 0xf1f5
        ShishKebab                = 0xf1f6
        ShoePrints                = 0xf1f7
        Shop                      = 0xf1f8
        ShopLock                  = 0xf1f9
        ShopSlash                 = 0xf1fa
        Shovel                    = 0xf1fb
        ShovelSnow                = 0xf1fc
        Shower                    = 0xf1fd
        ShowerDown                = 0xf1fe
        Shredder                  = 0xf1ff
        Shrimp                    = 0xf200
        Shuffle                   = 0xf201
        Shutters                  = 0xf202
        Shuttlecock               = 0xf203
        ShuttleSpace              = 0xf204
        Sickle                    = 0xf205
        Sidebar                   = 0xf206
        SidebarFlip               = 0xf207
        Sigma                     = 0xf208
        Signal                    = 0xf209
        SignalBars                = 0xf20a
        SignalBarsFair            = 0xf20b
        SignalBarsGood            = 0xf20c
        SignalBarsSlash           = 0xf20d
        SignalBarsWeak            = 0xf20e
        SignalFair                = 0xf20f
        SignalGood                = 0xf210
        UserHairBuns              = 0xf211
        SignalStream              = 0xf212
        SignalStreamSlash         = 0xf213
        SignalStrong              = 0xf214
        SignalWeak                = 0xf215
        Signature                 = 0xf216
        SignatureLock             = 0xf217
        SignatureSlash            = 0xf218
        SignHanging               = 0xf219
        SignPost                  = 0xf21a
        SignPosts                 = 0xf21b
        SignPostsWrench           = 0xf21c
        SignsPost                 = 0xf21d
        SimCard                   = 0xf21e
        SimCards                  = 0xf21f
        Sink                      = 0xf220
        Siren                     = 0xf221
        SirenOn                   = 0xf222
        Sitemap                   = 0xf223
        Skeleton                  = 0xf224
        SkeletonRibs              = 0xf225
        SkiBoot                   = 0xf226
        SkiBootSki                = 0xf227
        Skull                     = 0xf228
        SkullCow                  = 0xf229
        SkullCrossbones           = 0xf22a
        Slash                     = 0xf22b
        SlashBack                 = 0xf22c
        SlashForward              = 0xf22d
        Sleigh                    = 0xf22e
        Slider                    = 0xf22f
        Sliders                   = 0xf230
        SlidersSimple             = 0xf231
        SlidersUp                 = 0xf232
        SlotMachine               = 0xf233
        Smog                      = 0xf234
        Smoke                     = 0xf235
        Smoking                   = 0xf236
        Snake                     = 0xf237
        Snooze                    = 0xf238
        SnowBlowing               = 0xf239
        Snowflake                 = 0xf23a
        SnowflakeDroplets         = 0xf23b
        Snowflakes                = 0xf23c
        Snowman                   = 0xf23d
        SnowmanHead               = 0xf23e
        Snowplow                  = 0xf23f
        Soap                      = 0xf240
        Socks                     = 0xf241
        SoftServe                 = 0xf242
        SolarPanel                = 0xf243
        SolarSystem               = 0xf244
        Sort                      = 0xf245
        SortDown                  = 0xf246
        SortUp                    = 0xf247
        Spa                       = 0xf248
        SpaceStationMoon          = 0xf249
        SpaceStationMoonConstruction = 0xf24a
        Spade                     = 0xf24b
        SpaghettiMonsterFlying    = 0xf24c
        Sparkles                  = 0xf24d
        Speaker                   = 0xf24e
        Speakers                  = 0xf24f
        SpiderBlackWidow          = 0xf250
        SpiderWeb                 = 0xf251
        Sparkle                   = 0xf252
        Spinner                   = 0xf253
        Spider                    = 0xf254
        SpinnerScale              = 0xf255
        SpinnerThird              = 0xf256
        Splotch                   = 0xf257
        Split                     = 0xf258
        SprayCan                  = 0xf259
        SprayCanSparkles          = 0xf25a
        Sportsball                = 0xf25b
        Sprinkler                 = 0xf25c
        SprinklerCeiling          = 0xf25d
        Square                    = 0xf25e
        Square3                   = 0xf25f
        Square0                   = 0xf260
        Square1                   = 0xf261
        SpellCheck                = 0xf262
        Square4                   = 0xf263
        Square5                   = 0xf264
        Spoon                     = 0xf265
        Square2                   = 0xf266
        Square7                   = 0xf267
        Square8                   = 0xf268
        Square6                   = 0xf269
        Square9                   = 0xf26a
        SquareALock               = 0xf26b
        SquareA                   = 0xf26c
        SquareArrowDown           = 0xf26d
        SquareAmpersand           = 0xf26e
        SquareArrowDownRight      = 0xf26f
        SquareArrowDownLeft       = 0xf270
        SquareArrowLeft           = 0xf271
        SquareArrowRight          = 0xf272
        SquareArrowUp             = 0xf273
        SquareArrowUpLeft         = 0xf274
        SquareArrowUpRight        = 0xf275
        SquareB                   = 0xf276
        SquareBolt                = 0xf277
        SquareC                   = 0xf278
        SquareCaretDown           = 0xf279
        SquareCaretLeft           = 0xf27a
        SquareCaretRight          = 0xf27b
        SquareCaretUp             = 0xf27c
        SquareCheck               = 0xf27d
        SquareChevronDown         = 0xf27e
        SquareChevronLeft         = 0xf27f
        SquareChevronRight        = 0xf280
        SquareChevronUp           = 0xf281
        SquareCode                = 0xf282
        SquareD                   = 0xf283
        SquareDashed              = 0xf284
        SquareDashedCirclePlus    = 0xf285
        SquareDivide              = 0xf286
        SquareDollar              = 0xf287
        SquareDown                = 0xf288
        SquareDownLeft            = 0xf289
        SquareDownRight           = 0xf28a
        SquareE                   = 0xf28b
        SquareEllipsis            = 0xf28c
        SquareEllipsisVertical    = 0xf28d
        SquareEnvelope            = 0xf28e
        SquareExclamation         = 0xf28f
        SquareF                   = 0xf290
        SquareFragile             = 0xf291
        SquareFull                = 0xf292
        SquareG                   = 0xf293
        SquareH                   = 0xf294
        SquareHeart               = 0xf295
        SquareI                   = 0xf296
        SquareInfo                = 0xf297
        SquareJ                   = 0xf298
        SquareK                   = 0xf299
        SquareKanban              = 0xf29a
        SquareL                   = 0xf29b
        SquareLeft                = 0xf29c
        SquareList                = 0xf29d
        SquareM                   = 0xf29e
        SquareMinus               = 0xf29f
        SquareN                   = 0xf2a0
        SquareNfi                 = 0xf2a1
        SquareO                   = 0xf2a2
        SquareP                   = 0xf2a3
        SquareParking             = 0xf2a4
        SquareParkingSlash        = 0xf2a5
        SquarePen                 = 0xf2a6
        SquarePersonConfined      = 0xf2a7
        SquarePhone               = 0xf2a8
        SquarePhoneFlip           = 0xf2a9
        SquarePhoneHangup         = 0xf2aa
        SquarePlus                = 0xf2ab
        SquarePollHorizontal      = 0xf2ac
        SquarePollVertical        = 0xf2ad
        SquareQ                   = 0xf2ae
        SquareQuarters            = 0xf2af
        SquareQuestion            = 0xf2b0
        SquareQuote               = 0xf2b1
        SquareR                   = 0xf2b2
        SquareRight               = 0xf2b3
        SquareRing                = 0xf2b4
        SquareRoot                = 0xf2b5
        SquareRootVariable        = 0xf2b6
        SquareRss                 = 0xf2b7
        SquareS                   = 0xf2b8
        SquareShareNodes          = 0xf2b9
        SquareSliders             = 0xf2ba
        SquareSlidersVertical     = 0xf2bb
        SquareSmall               = 0xf2bc
        SquareStar                = 0xf2bd
        SquareT                   = 0xf2be
        SquareTerminal            = 0xf2bf
        SquareThisWayUp           = 0xf2c0
        SquareU                   = 0xf2c1
        SquareUp                  = 0xf2c2
        SquareUpLeft              = 0xf2c3
        SquareUpRight             = 0xf2c4
        SquareUser                = 0xf2c5
        SquareV                   = 0xf2c6
        SquareVirus               = 0xf2c7
        SquareW                   = 0xf2c8
        SquareX                   = 0xf2c9
        SquareXmark               = 0xf2ca
        SquareY                   = 0xf2cb
        SquareZ                   = 0xf2cc
        Squid                     = 0xf2cd
        Squirrel                  = 0xf2ce
        Staff                     = 0xf2cf
        StaffSnake                = 0xf2d0
        Stairs                    = 0xf2d1
        Stamp                     = 0xf2d2
        StandardDefinition        = 0xf2d3
        Stapler                   = 0xf2d4
        Star                      = 0xf2d5
        StarAndCrescent           = 0xf2d6
        StarChristmas             = 0xf2d7
        StarExclamation           = 0xf2d8
        Starfighter               = 0xf2d9
        StarfighterTwinIonEngine  = 0xf2da
        StarfighterTwinIonEngineAdvanced = 0xf2db
        StarHalf                  = 0xf2dc
        StarHalfStroke            = 0xf2dd
        StarOfDavid               = 0xf2de
        StarOfLife                = 0xf2df
        Stars                     = 0xf2e0
        StarSharp                 = 0xf2e1
        StarSharpHalf             = 0xf2e2
        StarSharpHalfStroke       = 0xf2e3
        Starship                  = 0xf2e4
        StarshipFreighter         = 0xf2e5
        StarShooting              = 0xf2e6
        Steak                     = 0xf2e7
        SteeringWheel             = 0xf2e8
        SterlingSign              = 0xf2e9
        Stethoscope               = 0xf2ea
        Stocking                  = 0xf2eb
        Stomach                   = 0xf2ec
        Stop                      = 0xf2ed
        Stopwatch                 = 0xf2ee
        Stopwatch20               = 0xf2ef
        Store                     = 0xf2f0
        StoreLock                 = 0xf2f1
        StoreSlash                = 0xf2f2
        Strawberry                = 0xf2f3
        StreetView                = 0xf2f4
        Stretcher                 = 0xf2f5
        Strikethrough             = 0xf2f6
        Stroopwafel               = 0xf2f7
        Subscript                 = 0xf2f8
        Subtitles                 = 0xf2f9
        SubtitlesSlash            = 0xf2fa
        Suitcase                  = 0xf2fb
        SuitcaseMedical           = 0xf2fc
        SuitcaseRolling           = 0xf2fd
        Sun                       = 0xf2fe
        SunBright                 = 0xf2ff
        SunCloud                  = 0xf300
        SunDust                   = 0xf301
        Sunglasses                = 0xf302
        SunHaze                   = 0xf303
        SunPlantWilt              = 0xf304
        Sunrise                   = 0xf305
        Sunset                    = 0xf306
        Superscript               = 0xf307
        Sushi                     = 0xf308
        SushiRoll                 = 0xf309
        Swap                      = 0xf30a
        SwapArrows                = 0xf30b
        Swatchbook                = 0xf30c
        Sword                     = 0xf30d
        SwordLaser                = 0xf30e
        SwordLaserAlt             = 0xf30f
        Swords                    = 0xf310
        SwordsLaser               = 0xf311
        Symbols                   = 0xf312
        Synagogue                 = 0xf313
        Syringe                   = 0xf314
        T                         = 0xf315
        Table                     = 0xf316
        TableCells                = 0xf317
        TableCellsLarge           = 0xf318
        TableColumns              = 0xf319
        TableLayout               = 0xf31a
        TableList                 = 0xf31b
        TablePicnic               = 0xf31c
        TablePivot                = 0xf31d
        TableRows                 = 0xf31e
        Tablet                    = 0xf31f
        TabletButton              = 0xf320
        TableTennisPaddleBall     = 0xf321
        TableTree                 = 0xf322
        TabletRugged              = 0xf323
        Tablets                   = 0xf324
        TabletScreen              = 0xf325
        TabletScreenButton        = 0xf326
        TachographDigital         = 0xf327
        Taco                      = 0xf328
        Tag                       = 0xf329
        Tags                      = 0xf32a
        Tally                     = 0xf32b
        Tally1                    = 0xf32c
        Tally2                    = 0xf32d
        Tally3                    = 0xf32e
        Tally4                    = 0xf32f
        Tamale                    = 0xf330
        TankWater                 = 0xf331
        Tape                      = 0xf332
        Tarp                      = 0xf333
        TarpDroplet               = 0xf334
        Taxi                      = 0xf335
        TaxiBus                   = 0xf336
        TeddyBear                 = 0xf337
        Teeth                     = 0xf338
        TeethOpen                 = 0xf339
        Telescope                 = 0xf33a
        TemperatureArrowDown      = 0xf33b
        TemperatureArrowUp        = 0xf33c
        TemperatureEmpty          = 0xf33d
        TemperatureFull           = 0xf33e
        TemperatureHalf           = 0xf33f
        TemperatureHigh           = 0xf340
        TemperatureList           = 0xf341
        TemperatureLow            = 0xf342
        TemperatureQuarter        = 0xf343
        TemperatureSnow           = 0xf344
        TemperatureSun            = 0xf345
        TemperatureThreeQuarters  = 0xf346
        TengeSign                 = 0xf347
        TennisBall                = 0xf348
        Tent                      = 0xf349
        TentArrowDownToLine       = 0xf34a
        TentArrowLeftRight        = 0xf34b
        TentArrowsDown            = 0xf34c
        TentArrowTurnLeft         = 0xf34d
        TentDoublePeak            = 0xf34e
        Tents                     = 0xf34f
        Terminal                  = 0xf350
        Text                      = 0xf351
        TextHeight                = 0xf352
        TextSize                  = 0xf353
        TextSlash                 = 0xf354
        TextWidth                 = 0xf355
        Thermometer               = 0xf356
        Theta                     = 0xf357
        ThoughtBubble             = 0xf358
        ThumbsDown                = 0xf359
        ThumbsUp                  = 0xf35a
        Thumbtack                 = 0xf35b
        Tick                      = 0xf35c
        Ticket                    = 0xf35d
        TicketAirline             = 0xf35e
        TicketPerforated          = 0xf35f
        Tickets                   = 0xf360
        TicketsAirline            = 0xf361
        TicketSimple              = 0xf362
        TicketsPerforated         = 0xf363
        TicketsSimple             = 0xf364
        Tilde                     = 0xf365
        Timeline                  = 0xf366
        TimelineArrow             = 0xf367
        Timer                     = 0xf368
        Tire                      = 0xf369
        TireFlat                  = 0xf36a
        TirePressureWarning       = 0xf36b
        TireRugged                = 0xf36c
        ToggleLargeOff            = 0xf36d
        ToggleLargeOn             = 0xf36e
        ToggleOff                 = 0xf36f
        ToggleOn                  = 0xf370
        Toilet                    = 0xf371
        ToiletPaper               = 0xf372
        ToiletPaperBlank          = 0xf373
        ToiletPaperBlankUnder     = 0xf374
        ToiletPaperCheck          = 0xf375
        ToiletPaperSlash          = 0xf376
        ToiletPaperUnder          = 0xf377
        ToiletPaperUnderSlash     = 0xf378
        ToiletPaperXmark          = 0xf379
        ToiletPortable            = 0xf37a
        ToiletsPortable           = 0xf37b
        Tomato                    = 0xf37c
        Tombstone                 = 0xf37d
        TombstoneBlank            = 0xf37e
        Toolbox                   = 0xf37f
        Tooth                     = 0xf380
        Toothbrush                = 0xf381
        ToriiGate                 = 0xf382
        Tornado                   = 0xf383
        TowerBroadcast            = 0xf384
        TowerCell                 = 0xf385
        TowerControl              = 0xf386
        TowerObservation          = 0xf387
        Tractor                   = 0xf388
        Trademark                 = 0xf389
        TrafficCone               = 0xf38a
        TrafficLight              = 0xf38b
        TrafficLightGo            = 0xf38c
        TrafficLightSlow          = 0xf38d
        TrafficLightStop          = 0xf38e
        Trailer                   = 0xf38f
        Train                     = 0xf390
        TrainSubway               = 0xf391
        TrainSubwayTunnel         = 0xf392
        TrainTrack                = 0xf393
        TrainTram                 = 0xf394
        TrainTunnel               = 0xf395
        TransformerBolt           = 0xf396
        Transgender               = 0xf397
        Transporter               = 0xf398
        Transporter1              = 0xf399
        Transporter2              = 0xf39a
        Transporter3              = 0xf39b
        Transporter4              = 0xf39c
        Transporter5              = 0xf39d
        Transporter6              = 0xf39e
        Transporter7              = 0xf39f
        TransporterEmpty          = 0xf3a0
        Trash                     = 0xf3a1
        TrashArrowUp              = 0xf3a2
        TrashCan                  = 0xf3a3
        TrashCanArrowUp           = 0xf3a4
        TrashCanCheck             = 0xf3a5
        TrashCanClock             = 0xf3a6
        TrashCanList              = 0xf3a7
        TrashCanPlus              = 0xf3a8
        TrashCanSlash             = 0xf3a9
        TrashCanUndo              = 0xf3aa
        TrashCanXmark             = 0xf3ab
        TrashCheck                = 0xf3ac
        TrashClock                = 0xf3ad
        TrashList                 = 0xf3ae
        TrashPlus                 = 0xf3af
        TrashSlash                = 0xf3b0
        TrashUndo                 = 0xf3b1
        TrashXmark                = 0xf3b2
        TreasureChest             = 0xf3b3
        Tree                      = 0xf3b4
        TreeChristmas             = 0xf3b5
        TreeCity                  = 0xf3b6
        TreeDeciduous             = 0xf3b7
        TreeDecorated             = 0xf3b8
        TreeLarge                 = 0xf3b9
        TreePalm                  = 0xf3ba
        Trees                     = 0xf3bb
        TRex                      = 0xf3bc
        Triangle                  = 0xf3bd
        TriangleExclamation       = 0xf3be
        TriangleInstrument        = 0xf3bf
        TrianglePersonDigging     = 0xf3c0
        Tricycle                  = 0xf3c1
        TricycleAdult             = 0xf3c2
        Trillium                  = 0xf3c3
        Trophy                    = 0xf3c4
        TrophyStar                = 0xf3c5
        Trowel                    = 0xf3c6
        TrowelBricks              = 0xf3c7
        Truck                     = 0xf3c8
        TruckArrowRight           = 0xf3c9
        TruckBolt                 = 0xf3ca
        TruckClock                = 0xf3cb
        TruckContainer            = 0xf3cc
        TruckContainerEmpty       = 0xf3cd
        TruckDroplet              = 0xf3ce
        TruckFast                 = 0xf3cf
        TruckField                = 0xf3d0
        TruckFieldUn              = 0xf3d1
        TruckFire                 = 0xf3d2
        TruckFlatbed              = 0xf3d3
        TruckFront                = 0xf3d4
        TruckLadder               = 0xf3d5
        TruckMedical              = 0xf3d6
        TruckMonster              = 0xf3d7
        TruckMoving               = 0xf3d8
        TruckPickup               = 0xf3d9
        TruckPlane                = 0xf3da
        TruckPlow                 = 0xf3db
        TruckRamp                 = 0xf3dc
        TruckRampBox              = 0xf3dd
        TruckRampCouch            = 0xf3de
        TruckTow                  = 0xf3df
        TruckUtensils             = 0xf3e0
        Trumpet                   = 0xf3e1
        Tty                       = 0xf3e2
        TtyAnswer                 = 0xf3e3
        TugrikSign                = 0xf3e4
        Turkey                    = 0xf3e5
        TurkishLiraSign           = 0xf3e6
        TurnDown                  = 0xf3e7
        TurnDownLeft              = 0xf3e8
        TurnDownRight             = 0xf3e9
        TurnLeft                  = 0xf3ea
        TurnLeftDown              = 0xf3eb
        TurnLeftUp                = 0xf3ec
        TurnRight                 = 0xf3ed
        Turntable                 = 0xf3ee
        TurnUp                    = 0xf3ef
        Turtle                    = 0xf3f0
        Tv                        = 0xf3f1
        TvMusic                   = 0xf3f2
        TvRetro                   = 0xf3f3
        Typewriter                = 0xf3f4
        U                         = 0xf3f5
        Ufo                       = 0xf3f6
        UfoBeam                   = 0xf3f7
        Umbrella                  = 0xf3f8
        UmbrellaBeach             = 0xf3f9
        UmbrellaSimple            = 0xf3fa
        Underline                 = 0xf3fb
        Unicorn                   = 0xf3fc
        UniformMartialArts        = 0xf3fd
        Union                     = 0xf3fe
        UniversalAccess           = 0xf3ff
        Unlock                    = 0xf400
        UnlockKeyhole             = 0xf401
        Up                        = 0xf402
        UpDown                    = 0xf403
        UpDownLeftRight           = 0xf404
        UpFromBracket             = 0xf405
        UpFromDottedLine          = 0xf406
        UpFromLine                = 0xf407
        UpLeft                    = 0xf408
        Upload                    = 0xf409
        UpLong                    = 0xf40a
        UpRight                   = 0xf40b
        UpRightAndDownLeftFromCenter = 0xf40c
        UpRightFromSquare         = 0xf40d
        UpToDottedLine            = 0xf40e
        UpToLine                  = 0xf40f
        UsbDrive                  = 0xf410
        User                      = 0xf411
        UserAlien                 = 0xf412
        UserAstronaut             = 0xf413
        UserBountyHunter          = 0xf414
        UserCheck                 = 0xf415
        UserChef                  = 0xf416
        UserClock                 = 0xf417
        UserCowboy                = 0xf418
        UserCrown                 = 0xf419
        UserDoctor                = 0xf41a
        UserDoctorHair            = 0xf41b
        UserDoctorHairLong        = 0xf41c
        UserDoctorMessage         = 0xf41d
        UserGear                  = 0xf41e
        UserGraduate              = 0xf41f
        UserGroup                 = 0xf420
        UserGroupCrown            = 0xf421
        UserGroupSimple           = 0xf422
        UserHair                  = 0xf423
        XmarksLines               = 0xf424
        XmarkToSlot               = 0xf425
        XRay                      = 0xf426
        Y                         = 0xf427
        YenSign                   = 0xf428
        YinYang                   = 0xf429
        Z                         = 0xf42a
        UserHairLong              = 0xf42b
        UserHairMullet            = 0xf42c
        UserHeadset               = 0xf42d
        UserHelmetSafety          = 0xf42e
        UserInjured               = 0xf42f
        UserLarge                 = 0xf430
        UserLargeSlash            = 0xf431
        UserLock                  = 0xf432
        UserMagnifyingGlass       = 0xf433
        UserMinus                 = 0xf434
        UserMusic                 = 0xf435
        UserNinja                 = 0xf436
        UserNurse                 = 0xf437
        UserNurseHair             = 0xf438
        UserNurseHairLong         = 0xf439
        UserPen                   = 0xf43a
        UserPilot                 = 0xf43b
        UserPilotTie              = 0xf43c
        UserPlus                  = 0xf43d
        UserPolice                = 0xf43e
        UserPoliceTie             = 0xf43f
        UserRobot                 = 0xf440
        UserRobotXmarks           = 0xf441
        Users                     = 0xf442
        UsersBetweenLines         = 0xf443
        UserSecret                = 0xf444
        UsersGear                 = 0xf445
        UserShakespeare           = 0xf446
        UserShield                = 0xf447
        UserSlash                 = 0xf448
        UsersLine                 = 0xf449
        UsersMedical              = 0xf44a
        UsersRectangle            = 0xf44b
        UsersSlash                = 0xf44c
        UsersViewfinder           = 0xf44d
        UserTag                   = 0xf44e
        UserTie                   = 0xf44f
        UserUnlock                = 0xf450
        UserTieHairLong           = 0xf451
        UserVisor                 = 0xf452
        UserVneck                 = 0xf453
        UserTieHair               = 0xf454
        UserVneckHair             = 0xf455
        UserVneckHairLong         = 0xf456
        UsersRays                 = 0xf457
        UserXmark                 = 0xf458
        Utensils                  = 0xf459
        UtensilsSlash             = 0xf45a
        UtilityPole               = 0xf45b
        UtilityPoleDouble         = 0xf45c
        V                         = 0xf45d
        Vacuum                    = 0xf45e
        VacuumRobot               = 0xf45f
        ValueAbsolute             = 0xf460
        VanShuttle                = 0xf461
        VectorCircle              = 0xf462
        Vault                     = 0xf463
        VectorPolygon             = 0xf464
        VectorSquare              = 0xf465
        Venus                     = 0xf466
        VenusDouble               = 0xf467
        VenusMars                 = 0xf468
        VestPatches               = 0xf469
        Vial                      = 0xf46a
        VialCircleCheck           = 0xf46b
        Vials                     = 0xf46c
        Vest                      = 0xf46d
        Video                     = 0xf46e
        VideoArrowDownLeft        = 0xf46f
        VideoSlash                = 0xf470
        VideoPlus                 = 0xf471
        Violin                    = 0xf472
        VirusCovidSlash           = 0xf473
        Viruses                   = 0xf474
        VirusSlash                = 0xf475
        Virus                     = 0xf476
        Vihara                    = 0xf477
        VirusCovid                = 0xf478
        Volcano                   = 0xf479
        VentDamper                = 0xf47a
        VolumeSlash               = 0xf47b
        VolumeXmark               = 0xf47c
        VrCardboard               = 0xf47d
        Volume                    = 0xf47e
        VolumeLow                 = 0xf47f
        Volleyball                = 0xf480
        VolumeOff                 = 0xf481
        Waffle                    = 0xf482
        VialVirus                 = 0xf483
        VolumeHigh                = 0xf484
        Voicemail                 = 0xf485
        W                         = 0xf486
        VideoArrowUpRight         = 0xf487
        WagonCovered              = 0xf488
        Walker                    = 0xf489
        WalkieTalkie              = 0xf48a
        Wallet                    = 0xf48b
        Wand                      = 0xf48c
        WandMagic                 = 0xf48d
        WandMagicSparkles         = 0xf48e
        WandSparkles              = 0xf48f
        Warehouse                 = 0xf490
        WarehouseFull             = 0xf491
        WashingMachine            = 0xf492
        Watch                     = 0xf493
        WatchApple                = 0xf494
        WatchCalculator           = 0xf495
        WatchFitness              = 0xf496
        WatchSmart                = 0xf497
        Water                     = 0xf498
        WaterArrowDown            = 0xf499
        WaterArrowUp              = 0xf49a
        WaterLadder               = 0xf49b
        WatermelonSlice           = 0xf49c
        Wave                      = 0xf49d
        Waveform                  = 0xf49e
        WaveformLines             = 0xf49f
        WavePulse                 = 0xf4a0
        WaveSine                  = 0xf4a1
        WaveSquare                = 0xf4a2
        WavesSine                 = 0xf4a3
        WaveTriangle              = 0xf4a4
        Webhook                   = 0xf4a5
        WeightHanging             = 0xf4a6
        WeightScale               = 0xf4a7
        Whale                     = 0xf4a8
        Wheat                     = 0xf4a9
        WheatAwn                  = 0xf4aa
        WheatAwnCircleExclamation = 0xf4ab
        WheatAwnSlash             = 0xf4ac
        WheatSlash                = 0xf4ad
        Wheelchair                = 0xf4ae
        WheelchairMove            = 0xf4af
        WhiskeyGlass              = 0xf4b0
        WhiskeyGlassIce           = 0xf4b1
        Whistle                   = 0xf4b2
        Wifi                      = 0xf4b3
        WifiExclamation           = 0xf4b4
        WifiFair                  = 0xf4b5
        WifiSlash                 = 0xf4b6
        WifiWeak                  = 0xf4b7
        Wind                      = 0xf4b8
        Window                    = 0xf4b9
        WindowFlip                = 0xf4ba
        WindowFrame               = 0xf4bb
        WindowFrameOpen           = 0xf4bc
        WindowMaximize            = 0xf4bd
        WindowMinimize            = 0xf4be
        WindowRestore             = 0xf4bf
        Windsock                  = 0xf4c0
        WindTurbine               = 0xf4c1
        WindWarning               = 0xf4c2
        WineBottle                = 0xf4c3
        WineGlass                 = 0xf4c4
        WineGlassCrack            = 0xf4c5
        WineGlassEmpty            = 0xf4c6
        WonSign                   = 0xf4c7
        Worm                      = 0xf4c8
        Wreath                    = 0xf4c9
        WreathLaurel              = 0xf4ca
        Wrench                    = 0xf4cb
        WrenchSimple              = 0xf4cc
        X                         = 0xf4cd
        Xmark                     = 0xf4ce
        XmarkLarge                = 0xf4cf


class ElaImageCard(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCardImage(self, /) -> PySide6.QtGui.QImage: ...
    def getIsPreserveAspectCrop(self, /) -> bool: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pCardImageChanged(self, /) -> None: ...
    def pIsPreserveAspectCropChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardImage(self, CardImage: PySide6.QtGui.QImage, /) -> None: ...
    def setIsPreserveAspectCrop(self, IsPreserveAspectCrop: bool, /) -> None: ...


class ElaInfoBadge(PySide6.QtWidgets.QWidget):

    class BadgeMode(enum.IntEnum):

        Dot                       = 0x0
        Value_                    = 0x1
        Icon                      = 0x2

    class Severity(enum.IntEnum):

        Attention                 = 0x0
        Informational             = 0x1
        Success                   = 0x2
        Caution                   = 0x3
        Critical                  = 0x4


    @typing.overload
    def __init__(self, icon: ElaWidgetTools.ElaIconType.IconName, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, value: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def attachTo(self, target: PySide6.QtWidgets.QWidget, /) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBadgeMode(self, /) -> ElaWidgetTools.ElaInfoBadge.BadgeMode: ...
    def getElaIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getMaxValue(self, /) -> int: ...
    def getSeverity(self, /) -> ElaWidgetTools.ElaInfoBadge.Severity: ...
    def getValue(self, /) -> int: ...
    def pElaIconChanged(self, /) -> None: ...
    def pValueChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBadgeMode(self, mode: ElaWidgetTools.ElaInfoBadge.BadgeMode, /) -> None: ...
    def setElaIcon(self, ElaIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setMaxValue(self, maxValue: int, /) -> None: ...
    def setSeverity(self, severity: ElaWidgetTools.ElaInfoBadge.Severity, /) -> None: ...
    def setValue(self, Value: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaInfoBar(PySide6.QtWidgets.QFrame):

    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pInfoBarIconChanged      : typing.ClassVar[Signal] = ... # pInfoBarIconChanged()
    pIsClosableChanged       : typing.ClassVar[Signal] = ... # pIsClosableChanged()
    pMessageChanged          : typing.ClassVar[Signal] = ... # pMessageChanged()
    pSeverityChanged         : typing.ClassVar[Signal] = ... # pSeverityChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clearActions(self, /) -> None: ...
    def closeInfoBar(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getInfoBarIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getIsClosable(self, /) -> bool: ...
    def getMessage(self, /) -> str: ...
    def getTitle(self, /) -> str: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setInfoBarIcon(self, InfoBarIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setIsClosable(self, IsClosable: bool, /) -> None: ...
    def setMessage(self, Message: str, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...


class ElaInputDialog(PySide6.QtWidgets.QDialog):

    doubleValueChanged       : typing.ClassVar[Signal] = ... # doubleValueChanged(double)
    intValueChanged          : typing.ClassVar[Signal] = ... # intValueChanged(int)
    pCancelButtonTextChanged : typing.ClassVar[Signal] = ... # pCancelButtonTextChanged()
    pDoubleValueChanged      : typing.ClassVar[Signal] = ... # pDoubleValueChanged()
    pInputMaximumWidthChanged: typing.ClassVar[Signal] = ... # pInputMaximumWidthChanged()
    pInputMinimumWidthChanged: typing.ClassVar[Signal] = ... # pInputMinimumWidthChanged()
    pIntValueChanged         : typing.ClassVar[Signal] = ... # pIntValueChanged()
    pLabelTextChanged        : typing.ClassVar[Signal] = ... # pLabelTextChanged()
    pOkButtonTextChanged     : typing.ClassVar[Signal] = ... # pOkButtonTextChanged()
    pPlaceholderTextChanged  : typing.ClassVar[Signal] = ... # pPlaceholderTextChanged()
    pSubTitleTextChanged     : typing.ClassVar[Signal] = ... # pSubTitleTextChanged()
    pTextValueChanged        : typing.ClassVar[Signal] = ... # pTextValueChanged()
    pTitleTextChanged        : typing.ClassVar[Signal] = ... # pTitleTextChanged()
    textValueChanged         : typing.ClassVar[Signal] = ... # textValueChanged(QString)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getCancelButtonText(self, /) -> str: ...
    @staticmethod
    def getDouble(parent: PySide6.QtWidgets.QWidget, title: str, subtitle: str, label: str, /, value: float = ..., minValue: float = ..., maxValue: float = ..., decimals: int = ..., okButtonText: str = ..., cancelButtonText: str = ..., inputMinWidth: int = ..., inputMaxWidth: int = ...) -> typing.Tuple[float, bool]: ...
    def getDoubleValue(self, /) -> float: ...
    def getInputMaximumWidth(self, /) -> int: ...
    def getInputMinimumWidth(self, /) -> int: ...
    @staticmethod
    def getInt(parent: PySide6.QtWidgets.QWidget, title: str, subtitle: str, label: str, /, value: int | None = ..., minValue: int = ..., maxValue: int = ..., step: int = ..., okButtonText: str = ..., cancelButtonText: str = ..., inputMinWidth: int = ..., inputMaxWidth: int = ...) -> typing.Tuple[int, bool]: ...
    def getIntValue(self, /) -> int: ...
    def getLabelText(self, /) -> str: ...
    @staticmethod
    def getMultiLineText(parent: PySide6.QtWidgets.QWidget, title: str, subtitle: str, label: str, /, text: str = ..., okButtonText: str = ..., cancelButtonText: str = ..., inputMinWidth: int = ..., inputMaxWidth: int = ...) -> typing.Tuple[str, bool]: ...
    def getOkButtonText(self, /) -> str: ...
    def getPlaceholderText(self, /) -> str: ...
    def getSubTitleText(self, /) -> str: ...
    @staticmethod
    def getText(parent: PySide6.QtWidgets.QWidget, title: str, subtitle: str, label: str, /, text: str = ..., okButtonText: str = ..., cancelButtonText: str = ..., inputMinWidth: int = ..., inputMaxWidth: int = ...) -> typing.Tuple[str, bool]: ...
    def getTextValue(self, /) -> str: ...
    def getTitleText(self, /) -> str: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setCancelButtonText(self, CancelButtonText: str, /) -> None: ...
    def setDoubleRange(self, minValue: float, maxValue: float, /, decimals: int = ...) -> None: ...
    def setDoubleValue(self, DoubleValue: float, /) -> None: ...
    def setInputMaximumWidth(self, InputMaximumWidth: int, /) -> None: ...
    def setInputMinimumWidth(self, InputMinimumWidth: int, /) -> None: ...
    def setIntRange(self, minValue: int, maxValue: int, /, step: int = ...) -> None: ...
    def setIntValue(self, IntValue: int, /) -> None: ...
    def setLabelText(self, LabelText: str, /) -> None: ...
    def setMultiLine(self, multiLine: bool, /) -> None: ...
    def setOkButtonText(self, OkButtonText: str, /) -> None: ...
    def setPlaceholderText(self, PlaceholderText: str, /) -> None: ...
    def setSubTitleText(self, SubTitleText: str, /) -> None: ...
    def setTextEchoMode(self, mode: PySide6.QtWidgets.QLineEdit.EchoMode, /) -> None: ...
    def setTextValue(self, TextValue: str, /) -> None: ...
    def setTitleText(self, TitleText: str, /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...
    def textEchoMode(self, /) -> PySide6.QtWidgets.QLineEdit.EchoMode: ...


class ElaInteractiveCard(PySide6.QtWidgets.QPushButton):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCardPixMode(self, /) -> ElaWidgetTools.ElaCardPixType.PixMode: ...
    def getCardPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getCardPixmapBorderRadius(self, /) -> int: ...
    def getCardPixmapSize(self, /) -> PySide6.QtCore.QSize: ...
    def getSubTitle(self, /) -> str: ...
    def getSubTitlePixelSize(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def getTitlePixelSize(self, /) -> int: ...
    def getTitleSpacing(self, /) -> int: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pCardPixModeChanged(self, /) -> None: ...
    def pCardPixmapBorderRadiusChanged(self, /) -> None: ...
    def pCardPixmapChanged(self, /) -> None: ...
    def pCardPixmapSizeChanged(self, /) -> None: ...
    def pSubTitleChanged(self, /) -> None: ...
    def pSubTitlePixelSizeChanged(self, /) -> None: ...
    def pTitleChanged(self, /) -> None: ...
    def pTitlePixelSizeChanged(self, /) -> None: ...
    def pTitleSpacingChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardPixMode(self, CardPixMode: ElaWidgetTools.ElaCardPixType.PixMode, /) -> None: ...
    def setCardPixmap(self, CardPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setCardPixmapBorderRadius(self, CardPixmapBorderRadius: int, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, CardPixmapSize: PySide6.QtCore.QSize, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, width: int, height: int, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setSubTitlePixelSize(self, SubTitlePixelSize: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTitlePixelSize(self, TitlePixelSize: int, /) -> None: ...
    def setTitleSpacing(self, TitleSpacing: int, /) -> None: ...


class ElaKeyBinder(PySide6.QtWidgets.QLabel):

    binderKeyTextChanged     : typing.ClassVar[Signal] = ... # binderKeyTextChanged(QString)
    nativeVirtualBinderKeyChanged: typing.ClassVar[Signal] = ... # nativeVirtualBinderKeyChanged(uint)
    pBinderKeyTextChanged    : typing.ClassVar[Signal] = ... # pBinderKeyTextChanged()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pNativeVirtualBinderKeyChanged: typing.ClassVar[Signal] = ... # pNativeVirtualBinderKeyChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBinderKeyText(self, /) -> str: ...
    def getBorderRadius(self, /) -> int: ...
    def getNativeVirtualBinderKey(self, /) -> int: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBinderKeyText(self, BinderKeyText: str, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setNativeVirtualBinderKey(self, NativeVirtualBinderKey: int, /) -> None: ...


class ElaLCDNumber(PySide6.QtWidgets.QLCDNumber):

    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, numDigits: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getAutoClockFormat(self, /) -> str: ...
    def getIsTransparent(self, /) -> bool: ...
    def getIsUseAutoClock(self, /) -> bool: ...
    def pAutoClockFormatChanged(self, /) -> None: ...
    def pIsTransparentChanged(self, /) -> None: ...
    def pIsUseAutoClockChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAutoClockFormat(self, AutoClockFormat: str, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setIsUseAutoClock(self, IsUseAutoClock: bool, /) -> None: ...


class ElaLineEdit(PySide6.QtWidgets.QLineEdit):

    focusIn                  : typing.ClassVar[Signal] = ... # focusIn(QString)
    focusOut                 : typing.ClassVar[Signal] = ... # focusOut(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsClearButtonEnableChanged: typing.ClassVar[Signal] = ... # pIsClearButtonEnableChanged()
    wmFocusOut               : typing.ClassVar[Signal] = ... # wmFocusOut(QString)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsClearButtonEnable(self, /) -> bool: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsClearButtonEnable(self, IsClearButtonEnable: bool, /) -> None: ...


class ElaListView(PySide6.QtWidgets.QListView):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getIsTransparent(self, /) -> bool: ...
    def getItemHeight(self, /) -> int: ...
    def pIsTransparentChanged(self, /) -> None: ...
    def pItemHeightChanged(self, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...


class ElaLog(PySide6.QtCore.QObject):

    logMessage               : typing.ClassVar[Signal] = ... # logMessage(QString)
    pIsLogFileNameWithTimeChanged: typing.ClassVar[Signal] = ... # pIsLogFileNameWithTimeChanged()
    pLogFileNameChanged      : typing.ClassVar[Signal] = ... # pLogFileNameChanged()
    pLogSavePathChanged      : typing.ClassVar[Signal] = ... # pLogSavePathChanged()
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaLog: ...
    def getIsLogFileNameWithTime(self, /) -> bool: ...
    def getLogFileName(self, /) -> str: ...
    def getLogSavePath(self, /) -> str: ...
    def initMessageLog(self, isEnable: bool, /) -> None: ...
    def setIsLogFileNameWithTime(self, IsLogFileNameWithTime: bool, /) -> None: ...
    def setLogFileName(self, LogFileName: str, /) -> None: ...
    def setLogSavePath(self, LogSavePath: str, /) -> None: ...


class ElaMarkdownViewer(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getMarkdown(self, /) -> str: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pMarkdownChanged(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setMarkdown(self, Markdown: str, /) -> None: ...


class ElaMenu(PySide6.QtWidgets.QMenu):

    menuShow                 : typing.ClassVar[Signal] = ... # menuShow()

    @typing.overload
    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, shortcut: PySide6.QtGui.QKeySequence | PySide6.QtCore.QKeyCombination | PySide6.QtGui.QKeySequence.StandardKey | str | int, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addMenu(self, icon: ElaWidgetTools.ElaIconType.IconName, title: str, /) -> ElaWidgetTools.ElaMenu: ...
    @typing.overload
    def addMenu(self, menu: PySide6.QtWidgets.QMenu, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addMenu(self, title: str, /) -> ElaWidgetTools.ElaMenu: ...
    @typing.overload
    def addMenu(self, icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap, title: str, /) -> ElaWidgetTools.ElaMenu: ...
    def getMenuItemHeight(self, /) -> int: ...
    def isHasChildMenu(self, /) -> bool: ...
    def isHasIcon(self, /) -> bool: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setMenuItemHeight(self, menuItemHeight: int, /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...


class ElaMenuBar(PySide6.QtWidgets.QMenuBar):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, shortcut: PySide6.QtGui.QKeySequence | PySide6.QtCore.QKeyCombination | PySide6.QtGui.QKeySequence.StandardKey | str | int, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addMenu(self, arg__1: ElaWidgetTools.ElaIconType.IconName, title: str, /) -> ElaWidgetTools.ElaMenu: ...
    @typing.overload
    def addMenu(self, menu: PySide6.QtWidgets.QMenu, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addMenu(self, title: str, /) -> ElaWidgetTools.ElaMenu: ...
    @typing.overload
    def addMenu(self, icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap, title: str, /) -> ElaWidgetTools.ElaMenu: ...


class ElaMessageBar(PySide6.QtWidgets.QWidget):
    @staticmethod
    def error(policy: ElaWidgetTools.ElaMessageBarType.PositionPolicy, title: str, text: str, displayMsec: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    @staticmethod
    def information(policy: ElaWidgetTools.ElaMessageBarType.PositionPolicy, title: str, text: str, displayMsec: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    @staticmethod
    def success(policy: ElaWidgetTools.ElaMessageBarType.PositionPolicy, title: str, text: str, displayMsec: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @staticmethod
    def warning(policy: ElaWidgetTools.ElaMessageBarType.PositionPolicy, title: str, text: str, displayMsec: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...


class ElaMessageBarType(Shiboken.Object):

    class MessageMode(enum.IntEnum):

        Success                   = 0x0
        Warning                   = 0x1
        Information               = 0x2
        Error                     = 0x3

    class PositionPolicy(enum.IntEnum):

        Top                       = 0x0
        Left                      = 0x1
        Bottom                    = 0x2
        Right                     = 0x3
        TopRight                  = 0x4
        TopLeft                   = 0x5
        BottomRight               = 0x6
        BottomLeft                = 0x7


class ElaMessageButton(PySide6.QtWidgets.QPushButton):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBarText(self, /) -> str: ...
    def getBarTitle(self, /) -> str: ...
    def getBorderRadius(self, /) -> int: ...
    def getDisplayMsec(self, /) -> int: ...
    def getMessageMode(self, /) -> ElaWidgetTools.ElaMessageBarType.MessageMode: ...
    def getMessageTargetWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getPositionPolicy(self, /) -> ElaWidgetTools.ElaMessageBarType.PositionPolicy: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def pBarTextChanged(self, /) -> None: ...
    def pBarTitleChanged(self, /) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pDisplayMsecChanged(self, /) -> None: ...
    def pMessageModeChanged(self, /) -> None: ...
    def pMessageTargetWidgetChanged(self, /) -> None: ...
    def pPositionPolicyChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBarText(self, BarText: str, /) -> None: ...
    def setBarTitle(self, BarTitle: str, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDisplayMsec(self, DisplayMsec: int, /) -> None: ...
    def setMessageMode(self, MessageMode: ElaWidgetTools.ElaMessageBarType.MessageMode, /) -> None: ...
    def setMessageTargetWidget(self, MessageTargetWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setPositionPolicy(self, PositionPolicy: ElaWidgetTools.ElaMessageBarType.PositionPolicy, /) -> None: ...


class ElaMessageDialog(PySide6.QtWidgets.QWidget):

    cancelled                : typing.ClassVar[Signal] = ... # cancelled()
    confirmed                : typing.ClassVar[Signal] = ... # confirmed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pContentChanged          : typing.ClassVar[Signal] = ... # pContentChanged()
    pContentPixelSizeChanged : typing.ClassVar[Signal] = ... # pContentPixelSizeChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()
    pTitlePixelSizeChanged   : typing.ClassVar[Signal] = ... # pTitlePixelSizeChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getContent(self, /) -> str: ...
    def getContentPixelSize(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def getTitlePixelSize(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setContent(self, Content: str, /) -> None: ...
    def setContentPixelSize(self, ContentPixelSize: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTitlePixelSize(self, TitlePixelSize: int, /) -> None: ...


class ElaMultiSelectComboBox(PySide6.QtWidgets.QComboBox):

    currentTextListChanged   : typing.ClassVar[Signal] = ... # currentTextListChanged(QStringList)
    itemSelectionChanged     : typing.ClassVar[Signal] = ... # itemSelectionChanged(QList<bool>)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pShowCheckBoxChanged     : typing.ClassVar[Signal] = ... # pShowCheckBoxChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCurrentSelection(self, /) -> typing.List[str]: ...
    def getCurrentSelectionIndex(self, /) -> typing.List[int]: ...
    def getShowCheckBox(self, /) -> bool: ...
    def hidePopup(self, /) -> None: ...
    def paintEvent(self, e: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    @typing.overload
    def setCurrentSelection(self, selection: str, /) -> None: ...
    @typing.overload
    def setCurrentSelection(self, selectionIndex: collections.abc.Sequence[int], /) -> None: ...
    @typing.overload
    def setCurrentSelection(self, selection: collections.abc.Sequence[str], /) -> None: ...
    @typing.overload
    def setCurrentSelection(self, index: int, /) -> None: ...
    def setShowCheckBox(self, ShowCheckBox: bool, /) -> None: ...
    def showPopup(self, /) -> None: ...


class ElaNavigationBar(PySide6.QtWidgets.QWidget):

    navigationNodeAdded      : typing.ClassVar[Signal] = ... # navigationNodeAdded(ElaNavigationType::NavigationNodeType,QString,QWidget*)
    navigationNodeClicked    : typing.ClassVar[Signal] = ... # navigationNodeClicked(ElaNavigationType::NavigationNodeType,QString,bool)
    navigationNodeRemoved    : typing.ClassVar[Signal] = ... # navigationNodeRemoved(ElaNavigationType::NavigationNodeType,QString)
    pIsAllowPageOpenInNewWindowChanged: typing.ClassVar[Signal] = ... # pIsAllowPageOpenInNewWindowChanged()
    pIsTransparentChanged    : typing.ClassVar[Signal] = ... # pIsTransparentChanged()
    pNavigationBarWidthChanged: typing.ClassVar[Signal] = ... # pNavigationBarWidthChanged()
    pageOpenInNewWindow      : typing.ClassVar[Signal] = ... # pageOpenInNewWindow(QString)
    userInfoCardClicked      : typing.ClassVar[Signal] = ... # userInfoCardClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addCategoryNode(self, categoryTitle: str, categoryKey: str, /) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addCategoryNode(self, categoryTitle: str, categoryKey: str, targetExpanderKey: str, /) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addExpanderNode(self, expanderTitle: str, expanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addExpanderNode(self, expanderTitle: str, expanderKey: str, targetExpanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addFooterNode(self, footerTitle: str, page: PySide6.QtWidgets.QWidget, footerKey: str, /, keyPoints: int | None = ..., awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addFooterNode(self, footerTitle: str, footerKey: str, /, keyPoints: int | None = ..., awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, targetExpanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, targetExpanderKey: str, keyPoints: int, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, keyPoints: int, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    def collapseNode(self, expanderKey: str, /) -> None: ...
    def expandNode(self, expanderKey: str, /) -> None: ...
    def getDisplayMode(self, /) -> ElaWidgetTools.ElaNavigationType.NavigationDisplayMode: ...
    def getIsAllowPageOpenInNewWindow(self, /) -> bool: ...
    def getIsTransparent(self, /) -> bool: ...
    def getNavigationBarWidth(self, /) -> int: ...
    def getNodeIsExpanded(self, expanderKey: str, /) -> bool: ...
    def getNodeKeyPoints(self, nodeKey: str, /) -> int: ...
    def getNodeTitle(self, nodeKey: str, /) -> str: ...
    def getPageOpenInNewWindowCount(self, nodeKey: str, /) -> int: ...
    def getSuggestDataList(self, /) -> typing.List[ElaWidgetTools.ElaSuggestBox.SuggestData]: ...
    def navigation(self, pageKey: str, /, isLogClicked: bool = ..., isRouteBack: bool = ...) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def removeNode(self, nodeKey: str, /) -> None: ...
    def setDisplayMode(self, displayMode: ElaWidgetTools.ElaNavigationType.NavigationDisplayMode, /, isAnimation: bool = ...) -> None: ...
    def setIsAllowPageOpenInNewWindow(self, IsAllowPageOpenInNewWindow: bool, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setNavigationBarWidth(self, NavigationBarWidth: int, /) -> None: ...
    def setNodeKeyPoints(self, nodeKey: str, keyPoints: int, /) -> None: ...
    def setNodeTitle(self, nodeKey: str, nodeTitle: str, /) -> None: ...
    def setUserInfoCardPixmap(self, pix: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setUserInfoCardSubTitle(self, subTitle: str, /) -> None: ...
    def setUserInfoCardTitle(self, title: str, /) -> None: ...
    def setUserInfoCardVisible(self, isVisible: bool, /) -> None: ...


class ElaNavigationRouter(PySide6.QtCore.QObject):

    navigationRouterStateChanged: typing.ClassVar[Signal] = ... # navigationRouterStateChanged(ElaNavigationRouterType::RouteMode)
    pMaxRouteCountChanged    : typing.ClassVar[Signal] = ... # pMaxRouteCountChanged()
    windowRouterStateChanged : typing.ClassVar[Signal] = ... # windowRouterStateChanged(QObject*,ElaNavigationRouterType::RouteMode)
    @typing.overload
    def clearNavigationRoute(self, /) -> None: ...
    @typing.overload
    def clearNavigationRoute(self, context: PySide6.QtCore.QObject, /) -> None: ...
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaNavigationRouter: ...
    def getMaxRouteCount(self, /) -> int: ...
    @typing.overload
    def navigationRoute(self, context: PySide6.QtCore.QObject, routeObject: PySide6.QtCore.QObject, routeFunctionName: str, /, routeData: typing.Dict[str, typing.Any] = ..., connectionType: PySide6.QtCore.Qt.ConnectionType = ...) -> ElaWidgetTools.ElaNavigationRouterType.NavigationRouteType: ...
    @typing.overload
    def navigationRoute(self, routeObject: PySide6.QtCore.QObject, routeFunctionName: str, /, routeData: typing.Dict[str, typing.Any] = ..., connectionType: PySide6.QtCore.Qt.ConnectionType = ...) -> ElaWidgetTools.ElaNavigationRouterType.NavigationRouteType: ...
    @typing.overload
    def navigationRouteBack(self, /) -> None: ...
    @typing.overload
    def navigationRouteBack(self, context: PySide6.QtCore.QObject, /) -> None: ...
    @typing.overload
    def navigationRouteForward(self, /) -> None: ...
    @typing.overload
    def navigationRouteForward(self, context: PySide6.QtCore.QObject, /) -> None: ...
    def setMaxRouteCount(self, MaxRouteCount: int, /) -> None: ...


class ElaNavigationRouterType(Shiboken.Object):

    class NavigationRouteType(enum.IntEnum):

        Success                   = 0x0
        ObjectInvalid             = 0x1
        FunctionNameInvalid       = 0x2

    class RouteMode(enum.IntEnum):

        BackValid                 = 0x0
        BackInvalid               = 0x1
        ForwardValid              = 0x2
        ForwardInvalid            = 0x3


class ElaNavigationType(Shiboken.Object):

    class NavigationDisplayMode(enum.IntEnum):

        Auto                      = 0x0
        Minimal                   = 0x1
        Compact                   = 0x2
        Maximal                   = 0x3

    class NavigationNodeType(enum.IntEnum):

        PageNode                  = 0x0
        FooterNode                = 0x1
        CategoryNode              = 0x2

    class NodeResult(enum.IntEnum):

        Success                   = 0x0
        TargetNodeInvalid         = 0x1
        TargetNodeTypeError       = 0x2
        TargetNodeDepthLimit      = 0x3
        PageInvalid               = 0x4
        FooterUpperLimit          = 0x5


class ElaNotificationCenter(PySide6.QtWidgets.QWidget):

    notificationClicked      : typing.ClassVar[Signal] = ... # notificationClicked(int)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pPanelWidthChanged       : typing.ClassVar[Signal] = ... # pPanelWidthChanged()
    panelVisibilityChanged   : typing.ClassVar[Signal] = ... # panelVisibilityChanged(bool)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clearAll(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getNotificationCount(self, /) -> int: ...
    def getPanelWidth(self, /) -> int: ...
    def hidePanel(self, /) -> None: ...
    def isPanelVisible(self, /) -> bool: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setPanelWidth(self, PanelWidth: int, /) -> None: ...
    def showPanel(self, anchor: PySide6.QtWidgets.QWidget, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaNumberBox(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pDecimalsChanged         : typing.ClassVar[Signal] = ... # pDecimalsChanged()
    pIsWrappingChanged       : typing.ClassVar[Signal] = ... # pIsWrappingChanged()
    pMaximumChanged          : typing.ClassVar[Signal] = ... # pMaximumChanged()
    pMinimumChanged          : typing.ClassVar[Signal] = ... # pMinimumChanged()
    pStepChanged             : typing.ClassVar[Signal] = ... # pStepChanged()
    pValueChanged            : typing.ClassVar[Signal] = ... # pValueChanged()
    valueChanged             : typing.ClassVar[Signal] = ... # valueChanged(double)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getDecimals(self, /) -> int: ...
    def getIsWrapping(self, /) -> bool: ...
    def getMaximum(self, /) -> float: ...
    def getMinimum(self, /) -> float: ...
    def getStep(self, /) -> float: ...
    def getValue(self, /) -> float: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDecimals(self, Decimals: int, /) -> None: ...
    def setIsWrapping(self, IsWrapping: bool, /) -> None: ...
    def setMaximum(self, Maximum: float, /) -> None: ...
    def setMinimum(self, Minimum: float, /) -> None: ...
    def setStep(self, Step: float, /) -> None: ...
    def setValue(self, Value: float, /) -> None: ...
    def stepDown(self, /) -> None: ...
    def stepUp(self, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaPagination(PySide6.QtWidgets.QWidget):

    currentPageChanged       : typing.ClassVar[Signal] = ... # currentPageChanged(int)
    pButtonSizeChanged       : typing.ClassVar[Signal] = ... # pButtonSizeChanged()
    pCurrentPageChanged      : typing.ClassVar[Signal] = ... # pCurrentPageChanged()
    pJumperVisibleChanged    : typing.ClassVar[Signal] = ... # pJumperVisibleChanged()
    pPagerCountChanged       : typing.ClassVar[Signal] = ... # pPagerCountChanged()
    pTotalPagesChanged       : typing.ClassVar[Signal] = ... # pTotalPagesChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getButtonSize(self, /) -> int: ...
    def getCurrentPage(self, /) -> int: ...
    def getJumperVisible(self, /) -> bool: ...
    def getPagerCount(self, /) -> int: ...
    def getTotalPages(self, /) -> int: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setButtonSize(self, ButtonSize: int, /) -> None: ...
    def setCurrentPage(self, CurrentPage: int, /) -> None: ...
    def setJumperVisible(self, JumperVisible: bool, /) -> None: ...
    def setPagerCount(self, PagerCount: int, /) -> None: ...
    def setTotalPages(self, TotalPages: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaPasswordBox(PySide6.QtWidgets.QLineEdit):

    focusIn                  : typing.ClassVar[Signal] = ... # focusIn(QString)
    focusOut                 : typing.ClassVar[Signal] = ... # focusOut(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsPasswordVisibleChanged: typing.ClassVar[Signal] = ... # pIsPasswordVisibleChanged()
    wmFocusOut               : typing.ClassVar[Signal] = ... # wmFocusOut(QString)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsPasswordVisible(self, /) -> bool: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsPasswordVisible(self, IsPasswordVisible: bool, /) -> None: ...


class ElaPersonPicture(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getDisplayName(self, /) -> str: ...
    def getPicture(self, /) -> PySide6.QtGui.QPixmap: ...
    def getPictureSize(self, /) -> int: ...
    def pDisplayNameChanged(self, /) -> None: ...
    def pPictureChanged(self, /) -> None: ...
    def pPictureSizeChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setDisplayName(self, DisplayName: str, /) -> None: ...
    def setPicture(self, Picture: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setPictureSize(self, PictureSize: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaPivot(PySide6.QtWidgets.QWidget):

    pCurrentIndexChanged     : typing.ClassVar[Signal] = ... # pCurrentIndexChanged()
    pMarkWidthChanged        : typing.ClassVar[Signal] = ... # pMarkWidthChanged()
    pPivotSpacingChanged     : typing.ClassVar[Signal] = ... # pPivotSpacingChanged()
    pTextPixelSizeChanged    : typing.ClassVar[Signal] = ... # pTextPixelSizeChanged()
    pivotClicked             : typing.ClassVar[Signal] = ... # pivotClicked(int)
    pivotDoubleClicked       : typing.ClassVar[Signal] = ... # pivotDoubleClicked(int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def appendPivot(self, pivotTitle: str, /) -> None: ...
    def getCurrentIndex(self, /) -> int: ...
    def getMarkWidth(self, /) -> int: ...
    def getPivotSpacing(self, /) -> int: ...
    def getTextPixelSize(self, /) -> int: ...
    def removePivot(self, pivotTitle: str, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def setMarkWidth(self, MarkWidth: int, /) -> None: ...
    def setPivotSpacing(self, PivotSpacing: int, /) -> None: ...
    def setTextPixelSize(self, TextPixelSize: int, /) -> None: ...


class ElaPlainTextEdit(PySide6.QtWidgets.QPlainTextEdit):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None: ...


class ElaPopconfirm(PySide6.QtWidgets.QWidget):

    cancelled                : typing.ClassVar[Signal] = ... # cancelled()
    closed                   : typing.ClassVar[Signal] = ... # closed()
    confirmed                : typing.ClassVar[Signal] = ... # confirmed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCancelButtonTextChanged : typing.ClassVar[Signal] = ... # pCancelButtonTextChanged()
    pConfirmButtonTextChanged: typing.ClassVar[Signal] = ... # pConfirmButtonTextChanged()
    pContentChanged          : typing.ClassVar[Signal] = ... # pContentChanged()
    pIconChanged             : typing.ClassVar[Signal] = ... # pIconChanged()
    pIsLightDismissChanged   : typing.ClassVar[Signal] = ... # pIsLightDismissChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def closePopconfirm(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getCancelButtonText(self, /) -> str: ...
    def getConfirmButtonText(self, /) -> str: ...
    def getContent(self, /) -> str: ...
    def getIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getIsLightDismiss(self, /) -> bool: ...
    def getTitle(self, /) -> str: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCancelButtonText(self, CancelButtonText: str, /) -> None: ...
    def setConfirmButtonText(self, ConfirmButtonText: str, /) -> None: ...
    def setContent(self, Content: str, /) -> None: ...
    def setIcon(self, Icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setIsLightDismiss(self, IsLightDismiss: bool, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def showPopconfirm(self, target: PySide6.QtWidgets.QWidget, /) -> None: ...


class ElaPopularCard(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCardButtonTextChanged   : typing.ClassVar[Signal] = ... # pCardButtonTextChanged()
    pCardFloatAreaChanged    : typing.ClassVar[Signal] = ... # pCardFloatAreaChanged()
    pCardFloatPixmapChanged  : typing.ClassVar[Signal] = ... # pCardFloatPixmapChanged()
    pCardPixmapChanged       : typing.ClassVar[Signal] = ... # pCardPixmapChanged()
    pDetailedTextChanged     : typing.ClassVar[Signal] = ... # pDetailedTextChanged()
    pInteractiveTipsChanged  : typing.ClassVar[Signal] = ... # pInteractiveTipsChanged()
    pSubTitleChanged         : typing.ClassVar[Signal] = ... # pSubTitleChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()
    popularCardButtonClicked : typing.ClassVar[Signal] = ... # popularCardButtonClicked()
    popularCardClicked       : typing.ClassVar[Signal] = ... # popularCardClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getCardButtonText(self, /) -> str: ...
    def getCardFloatArea(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getCardFloatPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getCardPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getDetailedText(self, /) -> str: ...
    def getInteractiveTips(self, /) -> str: ...
    def getSubTitle(self, /) -> str: ...
    def getTitle(self, /) -> str: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardButtonText(self, CardButtonText: str, /) -> None: ...
    def setCardFloatArea(self, CardFloatArea: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setCardFloatPixmap(self, CardFloatPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setCardPixmap(self, CardPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setDetailedText(self, DetailedText: str, /) -> None: ...
    def setInteractiveTips(self, InteractiveTips: str, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...


class ElaProgressBar(PySide6.QtWidgets.QProgressBar):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None: ...
    def setMaximum(self, maximum: int, /) -> None: ...
    def setMinimum(self, minimum: int, /) -> None: ...


class ElaProgressRing(PySide6.QtWidgets.QWidget):

    pBusyingDurationTimeChanged: typing.ClassVar[Signal] = ... # pBusyingDurationTimeChanged()
    pBusyingWidthChanged     : typing.ClassVar[Signal] = ... # pBusyingWidthChanged()
    pIsBusyingChanged        : typing.ClassVar[Signal] = ... # pIsBusyingChanged()
    pIsDisplayValueChanged   : typing.ClassVar[Signal] = ... # pIsDisplayValueChanged()
    pIsTransparentChanged    : typing.ClassVar[Signal] = ... # pIsTransparentChanged()
    pMaximumChanged          : typing.ClassVar[Signal] = ... # pMaximumChanged()
    pMinimumChanged          : typing.ClassVar[Signal] = ... # pMinimumChanged()
    pValueChanged            : typing.ClassVar[Signal] = ... # pValueChanged()
    pValueDisplayModeChanged : typing.ClassVar[Signal] = ... # pValueDisplayModeChanged()
    pValuePixelSizeChanged   : typing.ClassVar[Signal] = ... # pValuePixelSizeChanged()
    rangeChanged             : typing.ClassVar[Signal] = ... # rangeChanged(int,int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBusyingDurationTime(self, /) -> int: ...
    def getBusyingWidth(self, /) -> int: ...
    def getIsBusying(self, /) -> bool: ...
    def getIsDisplayValue(self, /) -> bool: ...
    def getIsTransparent(self, /) -> bool: ...
    def getMaximum(self, /) -> int: ...
    def getMinimum(self, /) -> int: ...
    def getValue(self, /) -> int: ...
    def getValueDisplayMode(self, /) -> ElaWidgetTools.ElaProgressRingType.ValueDisplayMode: ...
    def getValuePixelSize(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBusyingDurationTime(self, BusyingDurationTime: int, /) -> None: ...
    def setBusyingWidth(self, BusyingWidth: int, /) -> None: ...
    def setIsBusying(self, IsBusying: bool, /) -> None: ...
    def setIsDisplayValue(self, IsDisplayValue: bool, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setMaximum(self, Maximum: int, /) -> None: ...
    def setMinimum(self, Minimum: int, /) -> None: ...
    def setRange(self, min: int, max: int, /) -> None: ...
    def setValue(self, Value: int, /) -> None: ...
    def setValueDisplayMode(self, ValueDisplayMode: ElaWidgetTools.ElaProgressRingType.ValueDisplayMode, /) -> None: ...
    def setValuePixelSize(self, ValuePixelSize: int, /) -> None: ...


class ElaProgressRingType(Shiboken.Object):

    class ValueDisplayMode(enum.IntEnum):

        Actual                    = 0x0
        Percent                   = 0x1


class ElaPromotionCard(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCardPixmapChanged       : typing.ClassVar[Signal] = ... # pCardPixmapChanged()
    pCardTitleChanged        : typing.ClassVar[Signal] = ... # pCardTitleChanged()
    pCardTitleColorChanged   : typing.ClassVar[Signal] = ... # pCardTitleColorChanged()
    pCardTitlePixelSizeChanged: typing.ClassVar[Signal] = ... # pCardTitlePixelSizeChanged()
    pHorizontalCardPixmapRatioChanged: typing.ClassVar[Signal] = ... # pHorizontalCardPixmapRatioChanged()
    pPromotionTitleBaseColorChanged: typing.ClassVar[Signal] = ... # pPromotionTitleBaseColorChanged()
    pPromotionTitleChanged   : typing.ClassVar[Signal] = ... # pPromotionTitleChanged()
    pPromotionTitleColorChanged: typing.ClassVar[Signal] = ... # pPromotionTitleColorChanged()
    pPromotionTitlePixelSizeChanged: typing.ClassVar[Signal] = ... # pPromotionTitlePixelSizeChanged()
    pSubTitleChanged         : typing.ClassVar[Signal] = ... # pSubTitleChanged()
    pSubTitleColorChanged    : typing.ClassVar[Signal] = ... # pSubTitleColorChanged()
    pSubTitlePixelSizeChanged: typing.ClassVar[Signal] = ... # pSubTitlePixelSizeChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()
    pTitleColorChanged       : typing.ClassVar[Signal] = ... # pTitleColorChanged()
    pTitlePixelSizeChanged   : typing.ClassVar[Signal] = ... # pTitlePixelSizeChanged()
    pVerticalCardPixmapRatioChanged: typing.ClassVar[Signal] = ... # pVerticalCardPixmapRatioChanged()
    promotionCardClicked     : typing.ClassVar[Signal] = ... # promotionCardClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getCardPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getCardTitle(self, /) -> str: ...
    def getCardTitleColor(self, /) -> PySide6.QtGui.QColor: ...
    def getCardTitlePixelSize(self, /) -> int: ...
    def getHorizontalCardPixmapRatio(self, /) -> float: ...
    def getPromotionTitle(self, /) -> str: ...
    def getPromotionTitleBaseColor(self, /) -> PySide6.QtGui.QColor: ...
    def getPromotionTitleColor(self, /) -> PySide6.QtGui.QColor: ...
    def getPromotionTitlePixelSize(self, /) -> int: ...
    def getSubTitle(self, /) -> str: ...
    def getSubTitleColor(self, /) -> PySide6.QtGui.QColor: ...
    def getSubTitlePixelSize(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def getTitleColor(self, /) -> PySide6.QtGui.QColor: ...
    def getTitlePixelSize(self, /) -> int: ...
    def getVerticalCardPixmapRatio(self, /) -> float: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardPixmap(self, CardPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setCardTitle(self, CardTitle: str, /) -> None: ...
    def setCardTitleColor(self, CardTitleColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setCardTitlePixelSize(self, CardTitlePixelSize: int, /) -> None: ...
    def setHorizontalCardPixmapRatio(self, HorizontalCardPixmapRatio: float, /) -> None: ...
    def setPromotionTitle(self, PromotionTitle: str, /) -> None: ...
    def setPromotionTitleBaseColor(self, PromotionTitleBaseColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setPromotionTitleColor(self, PromotionTitleColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setPromotionTitlePixelSize(self, PromotionTitlePixelSize: int, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setSubTitleColor(self, SubTitleColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSubTitlePixelSize(self, SubTitlePixelSize: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTitleColor(self, TitleColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setTitlePixelSize(self, TitlePixelSize: int, /) -> None: ...
    def setVerticalCardPixmapRatio(self, VerticalCardPixmapRatio: float, /) -> None: ...


class ElaPromotionView(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def appendPromotionCard(self, card: ElaWidgetTools.ElaPromotionCard, /) -> None: ...
    def getAutoScrollInterval(self, /) -> int: ...
    def getCardCollapseWidth(self, /) -> int: ...
    def getCardExpandWidth(self, /) -> int: ...
    def getCurrentIndex(self, /) -> int: ...
    def getIsAutoScroll(self, /) -> bool: ...
    def pAutoScrollIntervalChanged(self, /) -> None: ...
    def pCardCollapseWidthChanged(self, /) -> None: ...
    def pCardExpandWidthChanged(self, /) -> None: ...
    def pCurrentIndexChanged(self, /) -> None: ...
    def pIsAutoScrollChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None: ...
    def setAutoScrollInterval(self, AutoScrollInterval: int, /) -> None: ...
    def setCardCollapseWidth(self, CardCollapseWidth: int, /) -> None: ...
    def setCardExpandWidth(self, CardExpandWidth: int, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def setIsAutoScroll(self, IsAutoScroll: bool, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaPushButton(PySide6.QtWidgets.QPushButton):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getDarkDefaultColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDarkHoverColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDarkPressColor(self, /) -> PySide6.QtGui.QColor: ...
    def getDarkTextColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightDefaultColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightHoverColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightPressColor(self, /) -> PySide6.QtGui.QColor: ...
    def getLightTextColor(self, /) -> PySide6.QtGui.QColor: ...
    def isHoverEnabled(self, /) -> bool: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pDarkDefaultColorChanged(self, /) -> None: ...
    def pDarkHoverColorChanged(self, /) -> None: ...
    def pDarkPressColorChanged(self, /) -> None: ...
    def pLightDefaultColorChanged(self, /) -> None: ...
    def pLightHoverColorChanged(self, /) -> None: ...
    def pLightPressColorChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDarkDefaultColor(self, DarkDefaultColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDarkHoverColor(self, DarkHoverColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDarkPressColor(self, DarkPressColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDarkTextColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    @typing.overload
    def setElaIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    @typing.overload
    def setElaIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, iconSize: int, /) -> None: ...
    def setHoverEnabled(self, enabled: bool, /) -> None: ...
    def setLightDefaultColor(self, LightDefaultColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLightHoverColor(self, LightHoverColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLightPressColor(self, LightPressColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLightTextColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...


class ElaQRCode(PySide6.QtWidgets.QWidget):

    class ErrorCorrectionLevel(enum.IntEnum):

        Low                       = 0x0
        Medium                    = 0x1
        Quartile                  = 0x2
        High                      = 0x3


    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBackgroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def getBorderRadius(self, /) -> int: ...
    def getErrorCorrectionLevel(self, /) -> ElaWidgetTools.ElaQRCode.ErrorCorrectionLevel: ...
    def getForegroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def getQuietZone(self, /) -> int: ...
    def getText(self, /) -> str: ...
    def pBackgroundColorChanged(self, /) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pForegroundColorChanged(self, /) -> None: ...
    def pQuietZoneChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBackgroundColor(self, BackgroundColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setErrorCorrectionLevel(self, level: ElaWidgetTools.ElaQRCode.ErrorCorrectionLevel, /) -> None: ...
    def setForegroundColor(self, ForegroundColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setQuietZone(self, QuietZone: int, /) -> None: ...
    def setText(self, text: str, /) -> None: ...
    def toPixmap(self, /, size: int = ...) -> PySide6.QtGui.QPixmap: ...


class ElaRadioButton(PySide6.QtWidgets.QRadioButton):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...


class ElaRatingControl(PySide6.QtWidgets.QWidget):

    pIsReadOnlyChanged       : typing.ClassVar[Signal] = ... # pIsReadOnlyChanged()
    pMaxRatingChanged        : typing.ClassVar[Signal] = ... # pMaxRatingChanged()
    pRatingChanged           : typing.ClassVar[Signal] = ... # pRatingChanged()
    pSpacingChanged          : typing.ClassVar[Signal] = ... # pSpacingChanged()
    pStarSizeChanged         : typing.ClassVar[Signal] = ... # pStarSizeChanged()
    ratingChanged            : typing.ClassVar[Signal] = ... # ratingChanged(int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getIsReadOnly(self, /) -> bool: ...
    def getMaxRating(self, /) -> int: ...
    def getRating(self, /) -> int: ...
    def getSpacing(self, /) -> int: ...
    def getStarSize(self, /) -> int: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setIsReadOnly(self, IsReadOnly: bool, /) -> None: ...
    def setMaxRating(self, MaxRating: int, /) -> None: ...
    def setRating(self, Rating: int, /) -> None: ...
    def setSpacing(self, Spacing: int, /) -> None: ...
    def setStarSize(self, StarSize: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaReminderCard(PySide6.QtWidgets.QPushButton):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCardPixMode(self, /) -> ElaWidgetTools.ElaCardPixType.PixMode: ...
    def getCardPixmap(self, /) -> PySide6.QtGui.QPixmap: ...
    def getCardPixmapBorderRadius(self, /) -> int: ...
    def getCardPixmapSize(self, /) -> PySide6.QtCore.QSize: ...
    def getSubTitle(self, /) -> str: ...
    def getSubTitlePixelSize(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def getTitlePixelSize(self, /) -> int: ...
    def getTitleSpacing(self, /) -> int: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pCardPixModeChanged(self, /) -> None: ...
    def pCardPixmapBorderRadiusChanged(self, /) -> None: ...
    def pCardPixmapChanged(self, /) -> None: ...
    def pCardPixmapSizeChanged(self, /) -> None: ...
    def pSubTitleChanged(self, /) -> None: ...
    def pSubTitlePixelSizeChanged(self, /) -> None: ...
    def pTitleChanged(self, /) -> None: ...
    def pTitlePixelSizeChanged(self, /) -> None: ...
    def pTitleSpacingChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardPixMode(self, CardPixMode: ElaWidgetTools.ElaCardPixType.PixMode, /) -> None: ...
    def setCardPixmap(self, CardPixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setCardPixmapBorderRadius(self, CardPixmapBorderRadius: int, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, CardPixmapSize: PySide6.QtCore.QSize, /) -> None: ...
    @typing.overload
    def setCardPixmapSize(self, width: int, height: int, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setSubTitlePixelSize(self, SubTitlePixelSize: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTitlePixelSize(self, TitlePixelSize: int, /) -> None: ...
    def setTitleSpacing(self, TitleSpacing: int, /) -> None: ...


class ElaRibbonBar(PySide6.QtWidgets.QWidget):

    collapsedChanged         : typing.ClassVar[Signal] = ... # collapsedChanged(bool)
    pCurrentIndexChanged     : typing.ClassVar[Signal] = ... # pCurrentIndexChanged()
    pinnedChanged            : typing.ClassVar[Signal] = ... # pinnedChanged(bool)
    tabClicked               : typing.ClassVar[Signal] = ... # tabClicked(int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addGroup(self, page: PySide6.QtWidgets.QWidget, title: str, /) -> ElaWidgetTools.ElaRibbonGroup: ...
    def addTab(self, title: str, /) -> PySide6.QtWidgets.QWidget: ...
    def bindTabBar(self, tabBar: ElaWidgetTools.ElaRibbonTabBar, /) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getAnimationDuration(self, /) -> int: ...
    def getCurrentIndex(self, /) -> int: ...
    def isCollapsed(self, /) -> bool: ...
    def isPinned(self, /) -> bool: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAnimationDuration(self, durationMs: int, /) -> None: ...
    def setCollapsed(self, collapsed: bool, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def setPinned(self, pinned: bool, /) -> None: ...
    def showPinContextMenu(self, globalPos: PySide6.QtCore.QPoint, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...
    def tabBar(self, /) -> ElaWidgetTools.ElaRibbonTabBar: ...
    def tabCount(self, /) -> int: ...
    def tabText(self, index: int, /) -> str: ...


class ElaRibbonGroup(PySide6.QtWidgets.QWidget):

    class ButtonSize(enum.IntEnum):

        Large                     = 0x1
        Small                     = 0x2


    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addToolButton(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, /, size: ElaWidgetTools.ElaRibbonGroup.ButtonSize = ...) -> ElaWidgetTools.ElaToolButton: ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def getTitle(self, /) -> str: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setTitle(self, title: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaRibbonTabBar(PySide6.QtWidgets.QWidget):

    pCurrentIndexChanged     : typing.ClassVar[Signal] = ... # pCurrentIndexChanged()
    tabClicked               : typing.ClassVar[Signal] = ... # tabClicked(int)
    tabReclicked             : typing.ClassVar[Signal] = ... # tabReclicked(int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def appendTab(self, title: str, /) -> int: ...
    def clear(self, /) -> None: ...
    def getCurrentIndex(self, /) -> int: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def removeTab(self, index: int, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def setTabText(self, index: int, title: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...
    def tabCount(self, /) -> int: ...
    def tabText(self, index: int, /) -> str: ...


class ElaRoller(PySide6.QtWidgets.QWidget):

    currentDataChanged       : typing.ClassVar[Signal] = ... # currentDataChanged(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCurrentIndexChanged     : typing.ClassVar[Signal] = ... # pCurrentIndexChanged()
    pIsContainerChanged      : typing.ClassVar[Signal] = ... # pIsContainerChanged()
    pIsEnableLoopChanged     : typing.ClassVar[Signal] = ... # pIsEnableLoopChanged()
    pItemHeightChanged       : typing.ClassVar[Signal] = ... # pItemHeightChanged()
    pItemListChanged         : typing.ClassVar[Signal] = ... # pItemListChanged()
    pMaxVisibleItemsChanged  : typing.ClassVar[Signal] = ... # pMaxVisibleItemsChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCurrentData(self, /) -> str: ...
    def getCurrentIndex(self, /) -> int: ...
    def getIsContainer(self, /) -> bool: ...
    def getIsEnableLoop(self, /) -> bool: ...
    def getItemHeight(self, /) -> int: ...
    def getItemList(self, /) -> typing.List[str]: ...
    def getMaxVisibleItems(self, /) -> int: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCurrentData(self, data: str, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def setIsContainer(self, IsContainer: bool, /) -> None: ...
    def setIsEnableLoop(self, IsEnableLoop: bool, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...
    def setItemList(self, ItemList: collections.abc.Sequence[str], /) -> None: ...
    def setMaxVisibleItems(self, MaxVisibleItems: int, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaRollerPicker(PySide6.QtWidgets.QPushButton):

    currentDataChanged       : typing.ClassVar[Signal] = ... # currentDataChanged(QStringList)
    currentDataSelectionChanged: typing.ClassVar[Signal] = ... # currentDataSelectionChanged(QStringList)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addRoller(self, itemList: collections.abc.Sequence[str], /, isEnableLoop: bool = ...) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    @typing.overload
    def getCurrentData(self, /) -> typing.List[str]: ...
    @typing.overload
    def getCurrentData(self, index: int, /) -> str: ...
    @typing.overload
    def getCurrentIndex(self, /) -> typing.List[int]: ...
    @typing.overload
    def getCurrentIndex(self, rollerIndex: int, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def removeRoller(self, index: int, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    @typing.overload
    def setCurrentData(self, dataList: collections.abc.Sequence[str], /) -> None: ...
    @typing.overload
    def setCurrentData(self, index: int, data: str, /) -> None: ...
    @typing.overload
    def setCurrentIndex(self, indexList: collections.abc.Sequence[int], /) -> None: ...
    @typing.overload
    def setCurrentIndex(self, rollerIndex: int, index: int, /) -> None: ...
    def setRollerItemList(self, index: int, itemList: collections.abc.Sequence[str], /) -> None: ...
    def setRollerWidth(self, index: int, width: int, /) -> None: ...


class ElaRouteConfig(Shiboken.Object):

    children                  = ...  # type: typing.List[ElaWidgetTools.ElaRouteConfig]
    icon                      = ...  # type: ElaWidgetTools.ElaIconType.IconName
    keyPoints                 = ...  # type: int
    meta                      = ...  # type: typing.Dict[str, typing.Any]
    path                      = ...  # type: str
    title                     = ...  # type: str

    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, ElaRouteConfig: ElaWidgetTools.ElaRouteConfig, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...


class ElaRouter(PySide6.QtCore.QObject):

    navigationBlocked        : typing.ClassVar[Signal] = ... # navigationBlocked(QString)
    routeChanged             : typing.ClassVar[Signal] = ... # routeChanged(QString,QVariantMap)
    routeTableChanged        : typing.ClassVar[Signal] = ... # routeTableChanged()
    def addDynamicRoute(self, parentPath: str, config: ElaWidgetTools.ElaRouteConfig, /) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def addRoute(self, config: ElaWidgetTools.ElaRouteConfig, /) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def addRoutes(self, configs: collections.abc.Sequence[ElaWidgetTools.ElaRouteConfig], /) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def back(self, /) -> None: ...
    def bindWindow(self, window: ElaWidgetTools.ElaWindow, /) -> None: ...
    def forward(self, /) -> None: ...
    def getBoundWindow(self, /) -> ElaWidgetTools.ElaWindow: ...
    def getCurrentParams(self, /) -> typing.Dict[str, typing.Any]: ...
    def getCurrentPath(self, /) -> str: ...
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaRouter: ...
    def getRouteMeta(self, path: str, /) -> typing.Dict[str, typing.Any]: ...
    def getRoutePaths(self, /) -> typing.List[str]: ...
    def hasRoute(self, path: str, /) -> bool: ...
    def installRoutes(self, /) -> None: ...
    def push(self, path: str, /, params: typing.Dict[str, typing.Any] = ...) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def removeAfterHook(self, hookId: int, /) -> None: ...
    def removeBeforeGuard(self, guardId: int, /) -> None: ...
    def removeRoute(self, path: str, /) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def replace(self, path: str, /, params: typing.Dict[str, typing.Any] = ...) -> ElaWidgetTools.ElaRouterType.NavigationResult: ...
    def resetRouter(self, /) -> None: ...


class ElaRouterType(Shiboken.Object):

    class NavigationResult(enum.IntEnum):

        Success                   = 0x0
        RouteNotFound             = 0x1
        GuardRejected             = 0x2
        FactoryFailed             = 0x3
        WindowNotBound            = 0x4
        RouteAlreadyExists        = 0x5
        ParentRouteNotFound       = 0x6


class ElaScreenCaptureManager(PySide6.QtCore.QObject):

    grabImageUpdate          : typing.ClassVar[Signal] = ... # grabImageUpdate(QImage)
    def getDisplayID(self, /) -> int: ...
    def getDisplayList(self, /) -> typing.List[str]: ...
    def getGrabArea(self, /) -> PySide6.QtCore.QRect: ...
    def getGrabFrameRate(self, /) -> int: ...
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaScreenCaptureManager: ...
    def getIsGrabScreen(self, /) -> bool: ...
    def grabScreenToImage(self, /) -> PySide6.QtGui.QImage: ...
    def setDisplayID(self, displayID: int, /) -> bool: ...
    @typing.overload
    def setGrabArea(self, width: int, height: int, /) -> None: ...
    @typing.overload
    def setGrabArea(self, x: int, y: int, width: int, height: int, /) -> None: ...
    def setGrabFrameRate(self, frameRateValue: int, /) -> None: ...
    def startGrabScreen(self, /) -> None: ...
    def stopGrabScreen(self, /) -> None: ...


class ElaScrollArea(PySide6.QtWidgets.QScrollArea):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getIsAnimation(self, orientation: PySide6.QtCore.Qt.Orientation, /) -> bool: ...
    def getIsOverShoot(self, orientation: PySide6.QtCore.Qt.Orientation, /) -> bool: ...
    def setIsAnimation(self, orientation: PySide6.QtCore.Qt.Orientation, isAnimation: bool, /) -> None: ...
    def setIsGrabGesture(self, isEnable: bool, /, mousePressEventDelay: float = ...) -> None: ...
    def setIsOverShoot(self, orientation: PySide6.QtCore.Qt.Orientation, isEnable: bool, /) -> None: ...


class ElaScrollBar(PySide6.QtWidgets.QScrollBar):

    pIsAnimationChanged      : typing.ClassVar[Signal] = ... # pIsAnimationChanged()
    pSpeedLimitChanged       : typing.ClassVar[Signal] = ... # pSpeedLimitChanged()
    rangeAnimationFinished   : typing.ClassVar[Signal] = ... # rangeAnimationFinished()

    @typing.overload
    def __init__(self, originScrollBar: PySide6.QtWidgets.QScrollBar, /, parent: PySide6.QtWidgets.QAbstractScrollArea | None = ...) -> None: ...
    @typing.overload
    def __init__(self, orientation: PySide6.QtCore.Qt.Orientation, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getIsAnimation(self, /) -> bool: ...
    def getSpeedLimit(self, /) -> float: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def setIsAnimation(self, IsAnimation: bool, /) -> None: ...
    def setSpeedLimit(self, SpeedLimit: float, /) -> None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaScrollPage(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addCentralWidget(self, centralWidget: PySide6.QtWidgets.QWidget, /, isWidgetResizeable: bool = ..., isVerticalGrabGesture: bool = ..., mousePressEventDelay: float = ...) -> None: ...
    def getCustomWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getPageTitleSpacing(self, /) -> int: ...
    def navigation(self, widgetIndex: int, /, isLogRoute: bool = ...) -> None: ...
    def pCustomWidgetChanged(self, /) -> None: ...
    def setCustomWidget(self, CustomWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setPageTitle(self, title: str, /) -> None: ...
    def setPageTitleSpacing(self, spacing: int, /) -> None: ...
    def setTitleVisible(self, isVisible: bool, /) -> None: ...


class ElaScrollPageArea(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...


class ElaSelectorBar(PySide6.QtWidgets.QWidget):

    currentIndexChanged      : typing.ClassVar[Signal] = ... # currentIndexChanged(int)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCurrentIndexChanged     : typing.ClassVar[Signal] = ... # pCurrentIndexChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addItem(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, /) -> None: ...
    @typing.overload
    def addItem(self, text: str, /) -> None: ...
    def clearItems(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getCurrentIndex(self, /) -> int: ...
    def getItemCount(self, /) -> int: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCurrentIndex(self, CurrentIndex: int, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaSheetPanel(PySide6.QtWidgets.QWidget):

    closed                   : typing.ClassVar[Signal] = ... # closed()
    detentChanged            : typing.ClassVar[Signal] = ... # detentChanged(ElaSheetPanelType::DetentLevel)
    opened                   : typing.ClassVar[Signal] = ... # opened()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCloseOnOverlayClickChanged: typing.ClassVar[Signal] = ... # pCloseOnOverlayClickChanged()
    pDirectionChanged        : typing.ClassVar[Signal] = ... # pDirectionChanged()
    pDragHandleVisibleChanged: typing.ClassVar[Signal] = ... # pDragHandleVisibleChanged()
    pFullRatioChanged        : typing.ClassVar[Signal] = ... # pFullRatioChanged()
    pHalfRatioChanged        : typing.ClassVar[Signal] = ... # pHalfRatioChanged()
    pOverlayOpacityChanged   : typing.ClassVar[Signal] = ... # pOverlayOpacityChanged()
    pPeekRatioChanged        : typing.ClassVar[Signal] = ... # pPeekRatioChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def close(self, /) -> None: ...
    def currentDetent(self, /) -> ElaWidgetTools.ElaSheetPanelType.DetentLevel: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getCloseOnOverlayClick(self, /) -> bool: ...
    def getDirection(self, /) -> ElaWidgetTools.ElaSheetPanelType.Direction: ...
    def getDragHandleVisible(self, /) -> bool: ...
    def getFullRatio(self, /) -> float: ...
    def getHalfRatio(self, /) -> float: ...
    def getOverlayOpacity(self, /) -> float: ...
    def getPeekRatio(self, /) -> float: ...
    def isOpened(self, /) -> bool: ...
    def open(self, /, level: ElaWidgetTools.ElaSheetPanelType.DetentLevel = ...) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCentralWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setCloseOnOverlayClick(self, CloseOnOverlayClick: bool, /) -> None: ...
    def setDirection(self, Direction: ElaWidgetTools.ElaSheetPanelType.Direction, /) -> None: ...
    def setDragHandleVisible(self, DragHandleVisible: bool, /) -> None: ...
    def setFullRatio(self, FullRatio: float, /) -> None: ...
    def setHalfRatio(self, HalfRatio: float, /) -> None: ...
    def setOverlayOpacity(self, OverlayOpacity: float, /) -> None: ...
    def setPeekRatio(self, PeekRatio: float, /) -> None: ...


class ElaSheetPanelType(Shiboken.Object):

    class DetentLevel(enum.IntEnum):

        Peek                      = 0x0
        Half                      = 0x1
        Full                      = 0x2

    class Direction(enum.IntEnum):

        Bottom                    = 0x0
        Left                      = 0x1
        Right                     = 0x2


class ElaSkeleton(PySide6.QtWidgets.QWidget):

    class SkeletonType(enum.IntEnum):

        Text                      = 0x0
        Circle                    = 0x1
        Rectangle                 = 0x2


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getIsAnimated(self, /) -> bool: ...
    def getSkeletonType(self, /) -> ElaWidgetTools.ElaSkeleton.SkeletonType: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pIsAnimatedChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsAnimated(self, IsAnimated: bool, /) -> None: ...
    def setSkeletonType(self, type: ElaWidgetTools.ElaSkeleton.SkeletonType, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaSlider(PySide6.QtWidgets.QSlider):

    @typing.overload
    def __init__(self, orientation: PySide6.QtCore.Qt.Orientation, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...


class ElaSnackbar(PySide6.QtWidgets.QWidget):

    actionClicked            : typing.ClassVar[Signal] = ... # actionClicked()
    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pDisplayMsecChanged      : typing.ClassVar[Signal] = ... # pDisplayMsecChanged()

    class SnackbarType(enum.IntEnum):

        Success                   = 0x0
        Info                      = 0x1
        Warning                   = 0x2
        Error                     = 0x3


    def dismiss(self, /) -> None: ...
    @staticmethod
    def error(text: str, /, actionText: str = ..., displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> ElaWidgetTools.ElaSnackbar: ...
    def getBorderRadius(self, /) -> int: ...
    def getDisplayMsec(self, /) -> int: ...
    @staticmethod
    def getMaxCount() -> int: ...
    @staticmethod
    def info(text: str, /, actionText: str = ..., displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> ElaWidgetTools.ElaSnackbar: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDisplayMsec(self, DisplayMsec: int, /) -> None: ...
    @staticmethod
    def setMaxCount(count: int, /) -> None: ...
    @staticmethod
    def success(text: str, /, actionText: str = ..., displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> ElaWidgetTools.ElaSnackbar: ...
    @staticmethod
    def warning(text: str, /, actionText: str = ..., displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> ElaWidgetTools.ElaSnackbar: ...


class ElaSpinBox(PySide6.QtWidgets.QSpinBox):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None: ...
    def getButtonMode(self, /) -> ElaWidgetTools.ElaSpinBoxType.ButtonMode: ...
    def pButtonModeChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setButtonMode(self, ButtonMode: ElaWidgetTools.ElaSpinBoxType.ButtonMode, /) -> None: ...


class ElaSpinBoxType(Shiboken.Object):

    class ButtonMode(enum.IntEnum):

        Inline                    = 0x0
        Compact                   = 0x1
        Side                      = 0x2
        PMSide                    = 0x3


class ElaSplashScreen(PySide6.QtWidgets.QWidget):

    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsClosableChanged       : typing.ClassVar[Signal] = ... # pIsClosableChanged()
    pIsShowProgressBarChanged: typing.ClassVar[Signal] = ... # pIsShowProgressBarChanged()
    pIsShowProgressRingChanged: typing.ClassVar[Signal] = ... # pIsShowProgressRingChanged()
    pMaximumChanged          : typing.ClassVar[Signal] = ... # pMaximumChanged()
    pMinimumChanged          : typing.ClassVar[Signal] = ... # pMinimumChanged()
    pValueChanged            : typing.ClassVar[Signal] = ... # pValueChanged()

    @typing.overload
    def __init__(self, logo: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def close(self, /) -> None: ...
    def finish(self, mainWindow: PySide6.QtWidgets.QWidget, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsClosable(self, /) -> bool: ...
    def getIsShowProgressBar(self, /) -> bool: ...
    def getIsShowProgressRing(self, /) -> bool: ...
    def getMaximum(self, /) -> int: ...
    def getMinimum(self, /) -> int: ...
    def getValue(self, /) -> int: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsClosable(self, IsClosable: bool, /) -> None: ...
    def setIsShowProgressBar(self, IsShowProgressBar: bool, /) -> None: ...
    def setIsShowProgressRing(self, IsShowProgressRing: bool, /) -> None: ...
    def setLogo(self, logo: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setMaximum(self, Maximum: int, /) -> None: ...
    def setMinimum(self, Minimum: int, /) -> None: ...
    def setStatusText(self, text: str, /) -> None: ...
    def setSubTitle(self, subTitle: str, /) -> None: ...
    def setTitle(self, title: str, /) -> None: ...
    def setValue(self, Value: int, /) -> None: ...
    def show(self, /) -> None: ...


class ElaSplitButton(PySide6.QtWidgets.QWidget):

    clicked                  : typing.ClassVar[Signal] = ... # clicked()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pElaIconChanged          : typing.ClassVar[Signal] = ... # pElaIconChanged()
    pTextChanged             : typing.ClassVar[Signal] = ... # pTextChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getElaIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getMenu(self, /) -> ElaWidgetTools.ElaMenu: ...
    def getText(self, /) -> str: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setElaIcon(self, ElaIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setMenu(self, menu: ElaWidgetTools.ElaMenu, /) -> None: ...
    def setText(self, Text: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaSplitter(PySide6.QtWidgets.QSplitter):

    @typing.overload
    def __init__(self, orientation: PySide6.QtCore.Qt.Orientation, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def createHandle(self, /) -> PySide6.QtWidgets.QSplitterHandle: ...
    def getGripLength(self, /) -> int: ...
    def getHandleWidth(self, /) -> int: ...
    def pGripLengthChanged(self, /) -> None: ...
    def pHandleWidthChanged(self, /) -> None: ...
    def setGripLength(self, GripLength: int, /) -> None: ...
    def setHandleWidth(self, HandleWidth: int, /) -> None: ...


class ElaSpotlight(PySide6.QtWidgets.QWidget):

    finished                 : typing.ClassVar[Signal] = ... # finished()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pContentChanged          : typing.ClassVar[Signal] = ... # pContentChanged()
    pIsCircleChanged         : typing.ClassVar[Signal] = ... # pIsCircleChanged()
    pOverlayAlphaChanged     : typing.ClassVar[Signal] = ... # pOverlayAlphaChanged()
    pPaddingChanged          : typing.ClassVar[Signal] = ... # pPaddingChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()
    stepChanged              : typing.ClassVar[Signal] = ... # stepChanged(int)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def currentStep(self, /) -> int: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def finish(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getContent(self, /) -> str: ...
    def getIsCircle(self, /) -> bool: ...
    def getOverlayAlpha(self, /) -> int: ...
    def getPadding(self, /) -> int: ...
    def getTitle(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def next(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def previous(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setContent(self, Content: str, /) -> None: ...
    def setIsCircle(self, IsCircle: bool, /) -> None: ...
    def setOverlayAlpha(self, OverlayAlpha: int, /) -> None: ...
    def setPadding(self, Padding: int, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def showSpotlight(self, target: PySide6.QtWidgets.QWidget, /, buttonText: str = ...) -> None: ...
    def start(self, /) -> None: ...
    def stepCount(self, /) -> int: ...


class ElaStatCard(PySide6.QtWidgets.QWidget):

    class TrendType(enum.IntEnum):

        None_                     = 0x0
        Up                        = 0x1
        Down                      = 0x2
        Neutral                   = 0x3


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCardIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getDescription(self, /) -> str: ...
    def getTitle(self, /) -> str: ...
    def getTrend(self, /) -> ElaWidgetTools.ElaStatCard.TrendType: ...
    def getTrendText(self, /) -> str: ...
    def getValue(self, /) -> str: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pCardIconChanged(self, /) -> None: ...
    def pDescriptionChanged(self, /) -> None: ...
    def pTitleChanged(self, /) -> None: ...
    def pValueChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCardIcon(self, CardIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setDescription(self, Description: str, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def setTrend(self, trend: ElaWidgetTools.ElaStatCard.TrendType, /) -> None: ...
    def setTrendText(self, text: str, /) -> None: ...
    def setValue(self, Value: str, /) -> None: ...


class ElaStatusBar(PySide6.QtWidgets.QStatusBar):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...


class ElaSteps(PySide6.QtWidgets.QWidget):

    currentStepChanged       : typing.ClassVar[Signal] = ... # currentStepChanged(int)
    pCurrentStepChanged      : typing.ClassVar[Signal] = ... # pCurrentStepChanged()
    pStepCountChanged        : typing.ClassVar[Signal] = ... # pStepCountChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getCurrentStep(self, /) -> int: ...
    def getStepCount(self, /) -> int: ...
    def getStepTitles(self, /) -> typing.List[str]: ...
    def next(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def previous(self, /) -> None: ...
    def setCurrentStep(self, CurrentStep: int, /) -> None: ...
    def setStepCount(self, StepCount: int, /) -> None: ...
    def setStepTitles(self, titles: collections.abc.Sequence[str], /) -> None: ...


class ElaSuggestBox(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCaseSensitivityChanged  : typing.ClassVar[Signal] = ... # pCaseSensitivityChanged()
    suggestionClicked        : typing.ClassVar[Signal] = ... # suggestionClicked(ElaSuggestBox::SuggestData)

    class SuggestData(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, icon: ElaWidgetTools.ElaIconType.IconName, suggestText: str, /, suggestData: typing.Dict[str, typing.Any] = ...) -> None: ...
        @typing.overload
        def __init__(self, SuggestData: ElaWidgetTools.ElaSuggestBox.SuggestData, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def getElaIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
        def getSuggestData(self, /) -> typing.Dict[str, typing.Any]: ...
        def getSuggestKey(self, /) -> str: ...
        def getSuggestText(self, /) -> str: ...
        def setElaIcon(self, ElaIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
        def setSuggestData(self, SuggestData: typing.Dict[str, typing.Any], /) -> None: ...
        def setSuggestKey(self, SuggestKey: str, /) -> None: ...
        def setSuggestText(self, SuggestText: str, /) -> None: ...


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addSuggestion(self, icon: ElaWidgetTools.ElaIconType.IconName, suggestText: str, /, suggestData: typing.Dict[str, typing.Any] = ...) -> str: ...
    @typing.overload
    def addSuggestion(self, suggestData: ElaWidgetTools.ElaSuggestBox.SuggestData, /) -> str: ...
    @typing.overload
    def addSuggestion(self, suggestText: str, /, suggestData: typing.Dict[str, typing.Any] = ...) -> str: ...
    @typing.overload
    def addSuggestion(self, suggestDataList: collections.abc.Sequence[ElaWidgetTools.ElaSuggestBox.SuggestData], /) -> typing.List[str]: ...
    def clearSuggestion(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getCaseSensitivity(self, /) -> PySide6.QtCore.Qt.CaseSensitivity: ...
    @typing.overload
    def removeSuggestion(self, suggestKey: str, /) -> None: ...
    @typing.overload
    def removeSuggestion(self, index: int, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCaseSensitivity(self, CaseSensitivity: PySide6.QtCore.Qt.CaseSensitivity, /) -> None: ...
    def setFixedHeight(self, h: int, /) -> None: ...
    @typing.overload
    def setFixedSize(self, size: PySide6.QtCore.QSize, /) -> None: ...
    @typing.overload
    def setFixedSize(self, w: int, h: int, /) -> None: ...
    def setPlaceholderText(self, placeholderText: str, /) -> None: ...


class ElaTabBar(PySide6.QtWidgets.QTabBar):

    pTabSizeChanged          : typing.ClassVar[Signal] = ... # pTabSizeChanged()
    tabDragCreate            : typing.ClassVar[Signal] = ... # tabDragCreate(QMimeData*)
    tabDragDrop              : typing.ClassVar[Signal] = ... # tabDragDrop(QMimeData*)
    tabDragEnter             : typing.ClassVar[Signal] = ... # tabDragEnter(QMimeData*)
    tabDragLeave             : typing.ClassVar[Signal] = ... # tabDragLeave(QMimeData*)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent, /) -> None: ...
    def dragLeaveEvent(self, event: PySide6.QtGui.QDragLeaveEvent, /) -> None: ...
    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent, /) -> None: ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent, /) -> None: ...
    def getTabSize(self, /) -> PySide6.QtCore.QSize: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setTabSize(self, TabSize: PySide6.QtCore.QSize, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None: ...


class ElaTabWidget(PySide6.QtWidgets.QTabWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent, /) -> None: ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent, /) -> None: ...
    def getIsContainerAcceptDrops(self, /) -> bool: ...
    def getIsTabTransparent(self, /) -> bool: ...
    def getTabSize(self, /) -> PySide6.QtCore.QSize: ...
    def pIsContainerAcceptDropsChanged(self, /) -> None: ...
    def pIsTabTransparentChanged(self, /) -> None: ...
    def pTabSizeChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setIsContainerAcceptDrops(self, IsContainerAcceptDrops: bool, /) -> None: ...
    def setIsTabTransparent(self, IsTabTransparent: bool, /) -> None: ...
    def setTabPosition(self, position: PySide6.QtWidgets.QTabWidget.TabPosition, /) -> None: ...
    def setTabSize(self, TabSize: PySide6.QtCore.QSize, /) -> None: ...
    def tabInserted(self, index: int, /) -> None: ...


class ElaTableView(PySide6.QtWidgets.QTableView):

    pHeaderMarginChanged     : typing.ClassVar[Signal] = ... # pHeaderMarginChanged()
    tableViewHide            : typing.ClassVar[Signal] = ... # tableViewHide()
    tableViewShow            : typing.ClassVar[Signal] = ... # tableViewShow()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getHeaderMargin(self, /) -> int: ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent, /) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def setHeaderMargin(self, HeaderMargin: int, /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...


class ElaTableWidget(PySide6.QtWidgets.QTableWidget):

    pHeaderMarginChanged     : typing.ClassVar[Signal] = ... # pHeaderMarginChanged()
    pIsTransparentChanged    : typing.ClassVar[Signal] = ... # pIsTransparentChanged()
    pItemHeightChanged       : typing.ClassVar[Signal] = ... # pItemHeightChanged()
    tableWidgetHide          : typing.ClassVar[Signal] = ... # tableWidgetHide()
    tableWidgetShow          : typing.ClassVar[Signal] = ... # tableWidgetShow()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getHeaderMargin(self, /) -> int: ...
    def getIsTransparent(self, /) -> bool: ...
    def getItemHeight(self, /) -> int: ...
    def getItemText(self, row: int, column: int, /) -> str: ...
    def getRowData(self, row: int, /) -> typing.List[str]: ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent, /) -> None: ...
    def insertColumns(self, column: int, count: int, /) -> None: ...
    def insertRows(self, row: int, count: int, /) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def removeColumns(self, column: int, count: int, /) -> None: ...
    def removeRows(self, row: int, count: int, /) -> None: ...
    def setHeaderMargin(self, HeaderMargin: int, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...
    def setItemText(self, row: int, column: int, text: str, /) -> None: ...
    def setRowData(self, row: int, data: collections.abc.Sequence[str], /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...


class ElaTag(PySide6.QtWidgets.QWidget):

    checkedChanged           : typing.ClassVar[Signal] = ... # checkedChanged(bool)
    clicked                  : typing.ClassVar[Signal] = ... # clicked()
    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsCheckableChanged      : typing.ClassVar[Signal] = ... # pIsCheckableChanged()
    pIsCheckedChanged        : typing.ClassVar[Signal] = ... # pIsCheckedChanged()
    pIsClosableChanged       : typing.ClassVar[Signal] = ... # pIsClosableChanged()
    pTagTextChanged          : typing.ClassVar[Signal] = ... # pTagTextChanged()

    class TagColor(enum.IntEnum):

        Default                   = 0x0
        Primary                   = 0x1
        Success                   = 0x2
        Warning                   = 0x3
        Danger                    = 0x4


    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getIsCheckable(self, /) -> bool: ...
    def getIsChecked(self, /) -> bool: ...
    def getIsClosable(self, /) -> bool: ...
    def getTagColor(self, /) -> ElaWidgetTools.ElaTag.TagColor: ...
    def getTagText(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsCheckable(self, IsCheckable: bool, /) -> None: ...
    def setIsChecked(self, IsChecked: bool, /) -> None: ...
    def setIsClosable(self, IsClosable: bool, /) -> None: ...
    def setTagColor(self, color: ElaWidgetTools.ElaTag.TagColor, /) -> None: ...
    def setTagText(self, TagText: str, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaTeachingTip(PySide6.QtWidgets.QWidget):

    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    closed                   : typing.ClassVar[Signal] = ... # closed()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pContentChanged          : typing.ClassVar[Signal] = ... # pContentChanged()
    pHeroImageChanged        : typing.ClassVar[Signal] = ... # pHeroImageChanged()
    pIsLightDismissChanged   : typing.ClassVar[Signal] = ... # pIsLightDismissChanged()
    pSubTitleChanged         : typing.ClassVar[Signal] = ... # pSubTitleChanged()
    pTipIconChanged          : typing.ClassVar[Signal] = ... # pTipIconChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    class TailPosition(enum.IntEnum):

        Auto                      = 0x0
        Top                       = 0x1
        Bottom                    = 0x2
        Left                      = 0x3
        Right                     = 0x4


    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clearActions(self, /) -> None: ...
    def closeTip(self, /) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getContent(self, /) -> str: ...
    def getHeroImage(self, /) -> PySide6.QtGui.QPixmap: ...
    def getIsLightDismiss(self, /) -> bool: ...
    def getSubTitle(self, /) -> str: ...
    def getTailPosition(self, /) -> ElaWidgetTools.ElaTeachingTip.TailPosition: ...
    def getTarget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getTipIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getTitle(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCloseButtonVisible(self, visible: bool, /) -> None: ...
    def setContent(self, Content: str, /) -> None: ...
    def setHeroImage(self, HeroImage: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setIsLightDismiss(self, IsLightDismiss: bool, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setTailPosition(self, position: ElaWidgetTools.ElaTeachingTip.TailPosition, /) -> None: ...
    def setTarget(self, target: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setTipIcon(self, TipIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent, /) -> None: ...
    def showTip(self, /) -> None: ...


class ElaTerminalWidget(PySide6.QtWidgets.QWidget):

    commandSubmitted         : typing.ClassVar[Signal] = ... # commandSubmitted(QString)
    pFontPixelSizeChanged    : typing.ClassVar[Signal] = ... # pFontPixelSizeChanged()
    pMaxHistorySizeChanged   : typing.ClassVar[Signal] = ... # pMaxHistorySizeChanged()
    pMaxLineCountChanged     : typing.ClassVar[Signal] = ... # pMaxLineCountChanged()
    pPromptChanged           : typing.ClassVar[Signal] = ... # pPromptChanged()
    tabPressed               : typing.ClassVar[Signal] = ... # tabPressed(QString)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def appendError(self, text: str, /) -> None: ...
    def appendHtml(self, html: str, /) -> None: ...
    def appendOutput(self, text: str, /, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int = ...) -> None: ...
    def appendSuccess(self, text: str, /) -> None: ...
    def clear(self, /) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getCommandHistory(self, /) -> typing.List[str]: ...
    def getFontPixelSize(self, /) -> int: ...
    def getMaxHistorySize(self, /) -> int: ...
    def getMaxLineCount(self, /) -> int: ...
    def getPrompt(self, /) -> str: ...
    def setFontPixelSize(self, FontPixelSize: int, /) -> None: ...
    def setMaxHistorySize(self, MaxHistorySize: int, /) -> None: ...
    def setMaxLineCount(self, MaxLineCount: int, /) -> None: ...
    def setPrompt(self, Prompt: str, /) -> None: ...


class ElaText(PySide6.QtWidgets.QLabel):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, text: str, pixelSize: int, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getElaIcon(self, /) -> ElaWidgetTools.ElaIconType.IconName: ...
    def getIsWrapAnywhere(self, /) -> bool: ...
    def getTextPixelSize(self, /) -> int: ...
    def getTextPointSize(self, /) -> int: ...
    def getTextStyle(self, /) -> ElaWidgetTools.ElaTextType.TextStyle: ...
    def pElaIconChanged(self, /) -> None: ...
    def pIsWrapAnywhereChanged(self, /) -> None: ...
    def pTextPixelSizeChanged(self, /) -> None: ...
    def pTextPointSizeChanged(self, /) -> None: ...
    def pTextStyleChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setElaIcon(self, ElaIcon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    def setIsWrapAnywhere(self, IsWrapAnywhere: bool, /) -> None: ...
    def setTextPixelSize(self, TextPixelSize: int, /) -> None: ...
    def setTextPointSize(self, TextPointSize: int, /) -> None: ...
    def setTextStyle(self, TextStyle: ElaWidgetTools.ElaTextType.TextStyle, /) -> None: ...


class ElaTextType(Shiboken.Object):

    class TextStyle(enum.IntEnum):

        NoStyle                   = 0x0
        Caption                   = 0x1
        Body                      = 0x2
        BodyStrong                = 0x3
        Subtitle                  = 0x4
        Title                     = 0x5
        TitleLarge                = 0x6
        Display                   = 0x7


class ElaTheme(PySide6.QtCore.QObject):

    pIsFollowSystemThemeChanged: typing.ClassVar[Signal] = ... # pIsFollowSystemThemeChanged(bool)
    themeModeChanged         : typing.ClassVar[Signal] = ... # themeModeChanged(ElaThemeType::ThemeMode)
    def drawEffectShadow(self, painter: PySide6.QtGui.QPainter, widgetRect: PySide6.QtCore.QRect, shadowBorderWidth: int, borderRadius: int, /) -> None: ...
    @staticmethod
    def getInstance() -> ElaWidgetTools.ElaTheme: ...
    def getIsFollowSystemTheme(self, /) -> bool: ...
    def getThemeColor(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, themeColor: ElaWidgetTools.ElaThemeType.ThemeColor, /) -> PySide6.QtGui.QColor: ...
    def getThemeMode(self, /) -> ElaWidgetTools.ElaThemeType.ThemeMode: ...
    def setIsFollowSystemTheme(self, isFollow: bool, /) -> None: ...
    def setThemeColor(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, themeColor: ElaWidgetTools.ElaThemeType.ThemeColor, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setThemeMode(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, /) -> None: ...


class ElaThemeType(Shiboken.Object):

    class ThemeColor(enum.IntEnum):

        ScrollBarHandle           = 0x0
        ToggleSwitchNoToggledCenter = 0x1
        WindowBase                = 0x2
        WindowCentralStackBase    = 0x3
        PrimaryNormal             = 0x4
        PrimaryHover              = 0x5
        PrimaryPress              = 0x6
        PopupBorder               = 0x7
        PopupBorderHover          = 0x8
        PopupBase                 = 0x9
        PopupHover                = 0xa
        DialogBase                = 0xb
        DialogLayoutArea          = 0xc
        BasicText                 = 0xd
        BasicTextInvert           = 0xe
        BasicDetailsText          = 0xf
        BasicTextNoFocus          = 0x10
        BasicTextDisable          = 0x11
        BasicTextPress            = 0x12
        BasicTextCategory         = 0x13
        BasicBorder               = 0x14
        BasicBorderDeep           = 0x15
        BasicBorderHover          = 0x16
        BasicBase                 = 0x17
        BasicBaseDeep             = 0x18
        BasicDisable              = 0x19
        BasicHover                = 0x1a
        BasicPress                = 0x1b
        BasicSelectedHover        = 0x1c
        BasicBaseLine             = 0x1d
        BasicHemline              = 0x1e
        BasicIndicator            = 0x1f
        BasicChute                = 0x20
        BasicAlternating          = 0x21
        BasicBaseAlpha            = 0x22
        BasicBaseDeepAlpha        = 0x23
        BasicHoverAlpha           = 0x24
        BasicPressAlpha           = 0x25
        BasicSelectedAlpha        = 0x26
        BasicSelectedHoverAlpha   = 0x27
        StatusDanger              = 0x28
        Win10BorderActive         = 0x29
        Win10BorderInactive       = 0x2a

    class ThemeMode(enum.IntEnum):

        Light                     = 0x0
        Dark                      = 0x1


class ElaTimeline(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clearItems(self, /) -> None: ...
    def getItemCount(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def sizeHint(self, /) -> PySide6.QtCore.QSize: ...


class ElaToast(PySide6.QtWidgets.QWidget):

    class ToastType(enum.IntEnum):

        Success                   = 0x0
        Info                      = 0x1
        Warning                   = 0x2
        Error                     = 0x3


    @staticmethod
    def error(text: str, /, displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getDisplayMsec(self, /) -> int: ...
    @staticmethod
    def info(text: str, /, displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pDisplayMsecChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDisplayMsec(self, DisplayMsec: int, /) -> None: ...
    @staticmethod
    def success(text: str, /, displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @staticmethod
    def warning(text: str, /, displayMsec: int = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...


class ElaToggleButton(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pTextChanged             : typing.ClassVar[Signal] = ... # pTextChanged()
    toggled                  : typing.ClassVar[Signal] = ... # toggled(bool)

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsToggled(self, /) -> bool: ...
    def getText(self, /) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsToggled(self, isToggled: bool, /) -> None: ...
    def setText(self, Text: str, /) -> None: ...


class ElaToggleSwitch(PySide6.QtWidgets.QWidget):

    toggled                  : typing.ClassVar[Signal] = ... # toggled(bool)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getIsToggled(self, /) -> bool: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setIsToggled(self, isToggled: bool, /) -> None: ...


class ElaToolBar(PySide6.QtWidgets.QToolBar):

    @typing.overload
    def __init__(self, title: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, /) -> PySide6.QtGui.QAction: ...
    @typing.overload
    def addElaIconAction(self, icon: ElaWidgetTools.ElaIconType.IconName, text: str, shortcut: PySide6.QtGui.QKeySequence | PySide6.QtCore.QKeyCombination | PySide6.QtGui.QKeySequence.StandardKey | str | int, /) -> PySide6.QtGui.QAction: ...
    def getToolBarSpacing(self, /) -> int: ...
    def getToolButtonSize(self, /) -> PySide6.QtCore.QSize: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setToolBarSpacing(self, spacing: int, /) -> None: ...
    def setToolButtonSize(self, size: PySide6.QtCore.QSize, /) -> None: ...


class ElaToolButton(PySide6.QtWidgets.QToolButton):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsSelected(self, /) -> bool: ...
    def getIsTransparent(self, /) -> bool: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pIsSelectedChanged(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    @typing.overload
    def setElaIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, /) -> None: ...
    @typing.overload
    def setElaIcon(self, icon: ElaWidgetTools.ElaIconType.IconName, rotate: int, /) -> None: ...
    def setIsSelected(self, IsSelected: bool, /) -> None: ...
    def setIsTransparent(self, isTransparent: bool, /) -> None: ...
    def setMenu(self, menu: ElaWidgetTools.ElaMenu, /) -> None: ...


class ElaToolTip(PySide6.QtWidgets.QWidget):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getBorderRadius(self, /) -> int: ...
    def getCustomWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getDisplayMsec(self, /) -> int: ...
    def getHideDelayMsec(self, /) -> int: ...
    def getShowDelayMsec(self, /) -> int: ...
    def getToolTip(self, /) -> str: ...
    def pBorderRadiusChanged(self, /) -> None: ...
    def pCustomWidgetChanged(self, /) -> None: ...
    def pDisplayMsecChanged(self, /) -> None: ...
    def pHideDelayMsecChanged(self, /) -> None: ...
    def pShowDelayMsecChanged(self, /) -> None: ...
    def pToolTipChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCustomWidget(self, CustomWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setDisplayMsec(self, DisplayMsec: int, /) -> None: ...
    def setHideDelayMsec(self, HideDelayMsec: int, /) -> None: ...
    def setShowDelayMsec(self, ShowDelayMsec: int, /) -> None: ...
    def setToolTip(self, ToolTip: str, /) -> None: ...
    def updatePos(self, /) -> None: ...


class ElaTransfer(PySide6.QtWidgets.QWidget):

    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsSearchVisibleChanged  : typing.ClassVar[Signal] = ... # pIsSearchVisibleChanged()
    pItemHeightChanged       : typing.ClassVar[Signal] = ... # pItemHeightChanged()
    pSourceTitleChanged      : typing.ClassVar[Signal] = ... # pSourceTitleChanged()
    pTargetTitleChanged      : typing.ClassVar[Signal] = ... # pTargetTitleChanged()
    transferChanged          : typing.ClassVar[Signal] = ... # transferChanged(QStringList,QStringList)

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addSourceItem(self, text: str, /) -> None: ...
    def addSourceItems(self, items: collections.abc.Sequence[str], /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsSearchVisible(self, /) -> bool: ...
    def getItemHeight(self, /) -> int: ...
    def getSourceItems(self, /) -> typing.List[str]: ...
    def getSourceTitle(self, /) -> str: ...
    def getTargetItems(self, /) -> typing.List[str]: ...
    def getTargetTitle(self, /) -> str: ...
    def moveAllToSource(self, /) -> None: ...
    def moveAllToTarget(self, /) -> None: ...
    def moveToSource(self, /) -> None: ...
    def moveToTarget(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setIsSearchVisible(self, IsSearchVisible: bool, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...
    def setSourceItems(self, items: collections.abc.Sequence[str], /) -> None: ...
    def setSourceTitle(self, SourceTitle: str, /) -> None: ...
    def setTargetTitle(self, TargetTitle: str, /) -> None: ...


class ElaTreeSelect(PySide6.QtWidgets.QWidget):

    currentIndexChanged      : typing.ClassVar[Signal] = ... # currentIndexChanged(QModelIndex)
    currentTextChanged       : typing.ClassVar[Signal] = ... # currentTextChanged(QString)
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pIsEditableChanged       : typing.ClassVar[Signal] = ... # pIsEditableChanged()
    pIsSearchVisibleChanged  : typing.ClassVar[Signal] = ... # pIsSearchVisibleChanged()
    pItemHeightChanged       : typing.ClassVar[Signal] = ... # pItemHeightChanged()
    pMaxVisibleItemsChanged  : typing.ClassVar[Signal] = ... # pMaxVisibleItemsChanged()
    pPlaceholderTextChanged  : typing.ClassVar[Signal] = ... # pPlaceholderTextChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def collapseAll(self, /) -> None: ...
    def currentIndex(self, /) -> PySide6.QtCore.QModelIndex: ...
    def currentText(self, /) -> str: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent, /) -> None: ...
    def expandAll(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getIsEditable(self, /) -> bool: ...
    def getIsSearchVisible(self, /) -> bool: ...
    def getItemHeight(self, /) -> int: ...
    def getMaxVisibleItems(self, /) -> int: ...
    def getPlaceholderText(self, /) -> str: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def model(self, /) -> PySide6.QtGui.QStandardItemModel: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCurrentIndex(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, /) -> None: ...
    def setIsEditable(self, IsEditable: bool, /) -> None: ...
    def setIsSearchVisible(self, IsSearchVisible: bool, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...
    def setMaxVisibleItems(self, MaxVisibleItems: int, /) -> None: ...
    def setModel(self, model: PySide6.QtGui.QStandardItemModel, /) -> None: ...
    def setPlaceholderText(self, PlaceholderText: str, /) -> None: ...


class ElaTreeView(PySide6.QtWidgets.QTreeView):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getHeaderMargin(self, /) -> int: ...
    def getItemHeight(self, /) -> int: ...
    def pHeaderMarginChanged(self, /) -> None: ...
    def pItemHeightChanged(self, /) -> None: ...
    def setHeaderMargin(self, HeaderMargin: int, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...


class ElaUploadArea(PySide6.QtWidgets.QWidget):

    fileAdded                : typing.ClassVar[Signal] = ... # fileAdded(QString)
    fileRejected             : typing.ClassVar[Signal] = ... # fileRejected(QString,QString)
    fileRemoved              : typing.ClassVar[Signal] = ... # fileRemoved(QString)
    filesSelected            : typing.ClassVar[Signal] = ... # filesSelected(QStringList)
    pAcceptedSuffixesChanged : typing.ClassVar[Signal] = ... # pAcceptedSuffixesChanged()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pDialogTitleChanged      : typing.ClassVar[Signal] = ... # pDialogTitleChanged()
    pIsMultipleChanged       : typing.ClassVar[Signal] = ... # pIsMultipleChanged()
    pMaxFileCountChanged     : typing.ClassVar[Signal] = ... # pMaxFileCountChanged()
    pMaxFileSizeChanged      : typing.ClassVar[Signal] = ... # pMaxFileSizeChanged()
    pSubTitleChanged         : typing.ClassVar[Signal] = ... # pSubTitleChanged()
    pTitleChanged            : typing.ClassVar[Signal] = ... # pTitleChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def clearFiles(self, /) -> None: ...
    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent, /) -> None: ...
    def dragLeaveEvent(self, event: PySide6.QtGui.QDragLeaveEvent, /) -> None: ...
    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent, /) -> None: ...
    def dropEvent(self, event: PySide6.QtGui.QDropEvent, /) -> None: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent, /) -> None: ...
    def getAcceptedMimeFilter(self, /) -> str: ...
    def getAcceptedSuffixes(self, /) -> typing.List[str]: ...
    def getBorderRadius(self, /) -> int: ...
    def getDialogTitle(self, /) -> str: ...
    def getIsMultiple(self, /) -> bool: ...
    def getMaxFileCount(self, /) -> int: ...
    def getMaxFileSize(self, /) -> int: ...
    def getSelectedFiles(self, /) -> typing.List[str]: ...
    def getSubTitle(self, /) -> str: ...
    def getTitle(self, /) -> str: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAcceptedMimeFilter(self, filter: str, /) -> None: ...
    def setAcceptedSuffixes(self, AcceptedSuffixes: collections.abc.Sequence[str], /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setDialogTitle(self, DialogTitle: str, /) -> None: ...
    def setIsMultiple(self, IsMultiple: bool, /) -> None: ...
    def setMaxFileCount(self, MaxFileCount: int, /) -> None: ...
    def setMaxFileSize(self, MaxFileSize: int, /) -> None: ...
    def setSubTitle(self, SubTitle: str, /) -> None: ...
    def setTitle(self, Title: str, /) -> None: ...


class ElaVirtualList(PySide6.QtWidgets.QListView):

    itemRequestData          : typing.ClassVar[Signal] = ... # itemRequestData(int,int)
    pIsAlternatingRowColorsChanged: typing.ClassVar[Signal] = ... # pIsAlternatingRowColorsChanged()
    pIsTransparentChanged    : typing.ClassVar[Signal] = ... # pIsTransparentChanged()
    pItemHeightChanged       : typing.ClassVar[Signal] = ... # pItemHeightChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getIsAlternatingRowColors(self, /) -> bool: ...
    def getIsTransparent(self, /) -> bool: ...
    def getItemCount(self, /) -> int: ...
    def getItemHeight(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setIsAlternatingRowColors(self, IsAlternatingRowColors: bool, /) -> None: ...
    def setIsTransparent(self, IsTransparent: bool, /) -> None: ...
    def setItemCount(self, count: int, /) -> None: ...
    def setItemHeight(self, ItemHeight: int, /) -> None: ...


class ElaWatermark(PySide6.QtWidgets.QWidget):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def getFontPixelSize(self, /) -> int: ...
    def getGapX(self, /) -> int: ...
    def getGapY(self, /) -> int: ...
    def getImage(self, /) -> PySide6.QtGui.QImage: ...
    def getImageHeight(self, /) -> int: ...
    def getImageWidth(self, /) -> int: ...
    def getOpacity(self, /) -> float: ...
    def getRotation(self, /) -> float: ...
    def getText(self, /) -> str: ...
    def getTextColor(self, /) -> PySide6.QtGui.QColor: ...
    def pFontPixelSizeChanged(self, /) -> None: ...
    def pGapXChanged(self, /) -> None: ...
    def pGapYChanged(self, /) -> None: ...
    def pImageChanged(self, /) -> None: ...
    def pImageHeightChanged(self, /) -> None: ...
    def pImageWidthChanged(self, /) -> None: ...
    def pOpacityChanged(self, /) -> None: ...
    def pRotationChanged(self, /) -> None: ...
    def pTextChanged(self, /) -> None: ...
    def pTextColorChanged(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setFontPixelSize(self, FontPixelSize: int, /) -> None: ...
    def setGapX(self, GapX: int, /) -> None: ...
    def setGapY(self, GapY: int, /) -> None: ...
    def setImage(self, Image: PySide6.QtGui.QImage, /) -> None: ...
    def setImageHeight(self, ImageHeight: int, /) -> None: ...
    def setImageWidth(self, ImageWidth: int, /) -> None: ...
    def setOpacity(self, Opacity: float, /) -> None: ...
    def setRotation(self, Rotation: float, /) -> None: ...
    def setText(self, Text: str, /) -> None: ...
    def setTextColor(self, TextColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...


class ElaWidget(PySide6.QtWidgets.QWidget):

    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    navigationButtonClicked  : typing.ClassVar[Signal] = ... # navigationButtonClicked()
    pAppBarHeightChanged     : typing.ClassVar[Signal] = ... # pAppBarHeightChanged()
    pIsDefaultClosedChanged  : typing.ClassVar[Signal] = ... # pIsDefaultClosedChanged()
    pIsFixedSizeChanged      : typing.ClassVar[Signal] = ... # pIsFixedSizeChanged()
    pIsStayTopChanged        : typing.ClassVar[Signal] = ... # pIsStayTopChanged()
    routeBackButtonClicked   : typing.ClassVar[Signal] = ... # routeBackButtonClicked()
    themeChangeButtonClicked : typing.ClassVar[Signal] = ... # themeChangeButtonClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def getAppBarHeight(self, /) -> int: ...
    def getIsDefaultClosed(self, /) -> bool: ...
    def getIsFixedSize(self, /) -> bool: ...
    def getIsStayTop(self, /) -> bool: ...
    def getWindowButtonFlags(self, /) -> ElaWidgetTools.ElaAppBarType.ButtonType: ...
    def moveToCenter(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def setAppBarHeight(self, AppBarHeight: int, /) -> None: ...
    def setIsDefaultClosed(self, IsDefaultClosed: bool, /) -> None: ...
    def setIsFixedSize(self, IsFixedSize: bool, /) -> None: ...
    def setIsStayTop(self, IsStayTop: bool, /) -> None: ...
    def setWindowButtonFlag(self, buttonFlag: ElaWidgetTools.ElaAppBarType.ButtonType, /, isEnable: bool = ...) -> None: ...
    def setWindowButtonFlags(self, buttonFlags: ElaWidgetTools.ElaAppBarType.ButtonType, /) -> None: ...


class ElaWindow(PySide6.QtWidgets.QMainWindow):

    centralCustomWidgetChanged: typing.ClassVar[Signal] = ... # centralCustomWidgetChanged()
    closeButtonClicked       : typing.ClassVar[Signal] = ... # closeButtonClicked()
    customMenuChanged        : typing.ClassVar[Signal] = ... # customMenuChanged()
    customWidgetChanged      : typing.ClassVar[Signal] = ... # customWidgetChanged()
    navigationNodeClicked    : typing.ClassVar[Signal] = ... # navigationNodeClicked(ElaNavigationType::NavigationNodeType,QString)
    pAppBarHeightChanged     : typing.ClassVar[Signal] = ... # pAppBarHeightChanged()
    pAppBarVisibleChanged    : typing.ClassVar[Signal] = ... # pAppBarVisibleChanged()
    pCurrentStackIndexChanged: typing.ClassVar[Signal] = ... # pCurrentStackIndexChanged()
    pIsAllowPageOpenInNewWindowChanged: typing.ClassVar[Signal] = ... # pIsAllowPageOpenInNewWindowChanged()
    pIsCentralStackedWidgetTransparentChanged: typing.ClassVar[Signal] = ... # pIsCentralStackedWidgetTransparentChanged()
    pIsDefaultClosedChanged  : typing.ClassVar[Signal] = ... # pIsDefaultClosedChanged()
    pIsFixedSizeChanged      : typing.ClassVar[Signal] = ... # pIsFixedSizeChanged()
    pIsNavigationBarEnableChanged: typing.ClassVar[Signal] = ... # pIsNavigationBarEnableChanged()
    pIsStayTopChanged        : typing.ClassVar[Signal] = ... # pIsStayTopChanged()
    pNavigationBarDisplayModeChanged: typing.ClassVar[Signal] = ... # pNavigationBarDisplayModeChanged()
    pNavigationBarWidthChanged: typing.ClassVar[Signal] = ... # pNavigationBarWidthChanged()
    pStackSwitchModeChanged  : typing.ClassVar[Signal] = ... # pStackSwitchModeChanged()
    pThemeChangeTimeChanged  : typing.ClassVar[Signal] = ... # pThemeChangeTimeChanged()
    pWindowPaintModeChanged  : typing.ClassVar[Signal] = ... # pWindowPaintModeChanged()
    pageOpenInNewWindow      : typing.ClassVar[Signal] = ... # pageOpenInNewWindow(QString)
    userInfoCardClicked      : typing.ClassVar[Signal] = ... # userInfoCardClicked()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    @typing.overload
    def addCategoryNode(self, categoryTitle: str, categoryKey: str, /) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addCategoryNode(self, categoryTitle: str, categoryKey: str, targetExpanderKey: str, /) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    def addCentralWidget(self, centralWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    @typing.overload
    def addExpanderNode(self, expanderTitle: str, expanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addExpanderNode(self, expanderTitle: str, expanderKey: str, targetExpanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addFooterNode(self, footerTitle: str, page: PySide6.QtWidgets.QWidget, footerKey: str, /, keyPoints: int | None = ..., awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addFooterNode(self, footerTitle: str, footerKey: str, /, keyPoints: int | None = ..., awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, targetExpanderKey: str, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, targetExpanderKey: str, keyPoints: int, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    @typing.overload
    def addPageNode(self, pageTitle: str, page: PySide6.QtWidgets.QWidget, keyPoints: int, /, awesome: ElaWidgetTools.ElaIconType.IconName = ...) -> ElaWidgetTools.ElaNavigationType.NodeResult: ...
    def backtrackNavigationNode(self, nodeKey: str, /) -> None: ...
    def centralWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def collapseNavigationNode(self, expanderKey: str, /) -> None: ...
    def createPopupMenu(self, /) -> PySide6.QtWidgets.QMenu: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent, /) -> bool: ...
    def expandNavigationNode(self, expanderKey: str, /) -> None: ...
    def getAppBar(self, /) -> ElaWidgetTools.ElaAppBar: ...
    def getAppBarHeight(self, /) -> int: ...
    def getAppBarVisible(self, /) -> bool: ...
    def getCentralCustomWidget(self, /) -> PySide6.QtWidgets.QWidget: ...
    def getCentralWidget(self, index: int, /) -> PySide6.QtWidgets.QWidget: ...
    def getCurrentNavigationIndex(self, /) -> int: ...
    def getCurrentNavigationPageKey(self, /) -> str: ...
    def getCurrentStackIndex(self, /) -> int: ...
    def getCustomMenu(self, /) -> PySide6.QtWidgets.QMenu: ...
    def getCustomWidget(self, customArea: ElaWidgetTools.ElaAppBarType.CustomArea, /) -> PySide6.QtWidgets.QWidget: ...
    def getIsAllowPageOpenInNewWindow(self, /) -> bool: ...
    def getIsCentralStackedWidgetTransparent(self, /) -> bool: ...
    def getIsDefaultClosed(self, /) -> bool: ...
    def getIsFixedSize(self, /) -> bool: ...
    def getIsNavigationBarEnable(self, /) -> bool: ...
    def getIsStayTop(self, /) -> bool: ...
    def getNavigationBarDisplayMode(self, /) -> ElaWidgetTools.ElaNavigationType.NavigationDisplayMode: ...
    def getNavigationBarWidth(self, /) -> int: ...
    def getNavigationNodeIsExpanded(self, expanderKey: str, /) -> bool: ...
    def getNavigationNodeTitle(self, nodeKey: str, /) -> str: ...
    def getNavigationSuggestDataList(self, /) -> typing.List[ElaWidgetTools.ElaSuggestBox.SuggestData]: ...
    def getNodeKeyPoints(self, nodeKey: str, /) -> int: ...
    def getPageOpenInNewWindowCount(self, nodeKey: str, /) -> int: ...
    def getStackSwitchMode(self, /) -> ElaWidgetTools.ElaWindowType.StackSwitchMode: ...
    def getThemeChangeTime(self, /) -> int: ...
    def getWindowButtonFlags(self, /) -> ElaWidgetTools.ElaAppBarType.ButtonType: ...
    def getWindowMoviePath(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, /) -> str: ...
    def getWindowMovieRate(self, /) -> float: ...
    def getWindowPaintMode(self, /) -> ElaWidgetTools.ElaWindowType.PaintMode: ...
    def getWindowPixmap(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, /) -> PySide6.QtGui.QPixmap: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def moveToCenter(self, /) -> None: ...
    def navigation(self, pageKey: str, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def removeNavigationNode(self, nodeKey: str, /) -> None: ...
    def setAppBarHeight(self, AppBarHeight: int, /) -> None: ...
    def setAppBarVisible(self, AppBarVisible: bool, /) -> None: ...
    def setCentralCustomWidget(self, customWidget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setCentralWidget(self, widget: PySide6.QtWidgets.QWidget, /) -> None: ...
    def setCurrentStackIndex(self, CurrentStackIndex: int, /) -> None: ...
    def setCustomMenu(self, customMenu: PySide6.QtWidgets.QMenu, /) -> None: ...
    def setCustomWidget(self, customArea: ElaWidgetTools.ElaAppBarType.CustomArea, customWidget: PySide6.QtWidgets.QWidget, /, hitTestObject: PySide6.QtCore.QObject | None = ..., hitTestFunctionName: str = ...) -> None: ...
    def setIsAllowPageOpenInNewWindow(self, IsAllowPageOpenInNewWindow: bool, /) -> None: ...
    def setIsCentralStackedWidgetTransparent(self, IsCentralStackedWidgetTransparent: bool, /) -> None: ...
    def setIsDefaultClosed(self, IsDefaultClosed: bool, /) -> None: ...
    def setIsFixedSize(self, IsFixedSize: bool, /) -> None: ...
    def setIsNavigationBarEnable(self, IsNavigationBarEnable: bool, /) -> None: ...
    def setIsStayTop(self, IsStayTop: bool, /) -> None: ...
    def setNavigationBarDisplayMode(self, NavigationBarDisplayMode: ElaWidgetTools.ElaNavigationType.NavigationDisplayMode, /) -> None: ...
    def setNavigationBarWidth(self, NavigationBarWidth: int, /) -> None: ...
    def setNavigationNodeTitle(self, nodeKey: str, nodeTitle: str, /) -> None: ...
    def setNodeKeyPoints(self, nodeKey: str, keyPoints: int, /) -> None: ...
    def setStackSwitchMode(self, StackSwitchMode: ElaWidgetTools.ElaWindowType.StackSwitchMode, /) -> None: ...
    def setThemeChangeTime(self, ThemeChangeTime: int, /) -> None: ...
    def setUserInfoCardPixmap(self, pix: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    def setUserInfoCardSubTitle(self, subTitle: str, /) -> None: ...
    def setUserInfoCardTitle(self, title: str, /) -> None: ...
    def setUserInfoCardVisible(self, isVisible: bool, /) -> None: ...
    def setWindowButtonFlag(self, buttonFlag: ElaWidgetTools.ElaAppBarType.ButtonType, /, isEnable: bool = ...) -> None: ...
    def setWindowButtonFlags(self, buttonFlags: ElaWidgetTools.ElaAppBarType.ButtonType, /) -> None: ...
    def setWindowMoviePath(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, moviePath: str, /) -> None: ...
    def setWindowMovieRate(self, rate: float, /) -> None: ...
    def setWindowPaintMode(self, WindowPaintMode: ElaWidgetTools.ElaWindowType.PaintMode, /) -> None: ...
    def setWindowPixmap(self, themeMode: ElaWidgetTools.ElaThemeType.ThemeMode, pixmap: PySide6.QtGui.QPixmap | PySide6.QtGui.QImage, /) -> None: ...
    @typing.overload
    def tabifyDockWidget(self, targetDockWidget: PySide6.QtWidgets.QDockWidget, dockWidget: PySide6.QtWidgets.QDockWidget, /) -> None: ...
    @typing.overload
    def tabifyDockWidget(self, area: PySide6.QtCore.Qt.DockWidgetArea, targetDockTitle: str, dockWidget: PySide6.QtWidgets.QDockWidget, /) -> None: ...


class ElaWindowType(Shiboken.Object):

    class PaintMode(enum.IntEnum):

        Normal                    = 0x0
        Pixmap                    = 0x1
        Movie                     = 0x2

    class StackSwitchMode(enum.IntEnum):

        None_                     = 0x0
        Popup                     = 0x1
        Scale                     = 0x2
        Flip                      = 0x3
        Blur                      = 0x4


class ElaWizard(PySide6.QtWidgets.QWidget):

    cancelled                : typing.ClassVar[Signal] = ... # cancelled()
    currentStepChanged       : typing.ClassVar[Signal] = ... # currentStepChanged(int)
    finished                 : typing.ClassVar[Signal] = ... # finished()
    pBorderRadiusChanged     : typing.ClassVar[Signal] = ... # pBorderRadiusChanged()
    pCurrentStepChanged      : typing.ClassVar[Signal] = ... # pCurrentStepChanged()

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def addStep(self, title: str, page: PySide6.QtWidgets.QWidget, /) -> None: ...
    def finish(self, /) -> None: ...
    def getBorderRadius(self, /) -> int: ...
    def getCurrentStep(self, /) -> int: ...
    def getStepCount(self, /) -> int: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def next(self, /) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def previous(self, /) -> None: ...
    def setBorderRadius(self, BorderRadius: int, /) -> None: ...
    def setCurrentStep(self, CurrentStep: int, /) -> None: ...


class QIntList: ...


# eof
