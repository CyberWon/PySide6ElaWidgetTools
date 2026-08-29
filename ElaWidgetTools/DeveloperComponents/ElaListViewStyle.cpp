#include "ElaListViewStyle.h"

#include <QAbstractScrollArea>
#include <QPainter>
#include <QPainterPath>
#include <QPointer>
#include <QStyleOption>
#include <QVariantAnimation>

#include "ElaListView.h"
#include "ElaTheme.h"
ElaListViewStyle::ElaListViewStyle(QStyle* style)
{
    _pItemHeight = 35;
    _pIsTransparent = false;
    _themeMode = eTheme->getThemeMode();
    connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode) {
        _themeMode = themeMode;
    });
}

ElaListViewStyle::~ElaListViewStyle()
{
}

void ElaListViewStyle::drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    switch (element)
    {
    case QStyle::PE_PanelItemViewItem:
    {
        // Item背景
        if (const QStyleOptionViewItem* vopt = qstyleoption_cast<const QStyleOptionViewItem*>(option))
        {
            // 行悬停过渡（按行键控，旧行淡出、新行淡入）
            bool isHovered = vopt->state.testFlag(QStyle::State_MouseOver);
            QPersistentModelIndex rowKey = vopt->index.sibling(vopt->index.row(), 0);
            if (_firstPaint)
            {
                _firstPaint = false;
                _hoverIndex = isHovered ? rowKey : QPersistentModelIndex();
                _hoverInRatio = isHovered ? 1 : 0;
                _hoverInRect = isHovered ? vopt->rect : QRect();
            }
            else if (rowKey.isValid() && isHovered && rowKey != _hoverIndex)
            {
                // 悬停行切换
                _fadeOutIndex = _hoverIndex;
                if (_fadeOutIndex.isValid())
                {
                    _startRowHoverAnimation(false, _hoverInRect, widget);
                }
                _hoverIndex = rowKey;
                _startRowHoverAnimation(true, vopt->rect, widget);
            }
            else if (rowKey.isValid() && !isHovered && rowKey == _hoverIndex)
            {
                // 悬停移出行外
                _fadeOutIndex = _hoverIndex;
                _hoverIndex = QPersistentModelIndex();
                _startRowHoverAnimation(false, _hoverInRect, widget);
            }
            qreal hoverRatio = 0;
            if (rowKey.isValid())
            {
                hoverRatio = rowKey == _hoverIndex ? _hoverInRatio : rowKey == _fadeOutIndex ? _hoverOutRatio : 0;
            }
            painter->save();
            painter->setRenderHint(QPainter::Antialiasing);
            QRect itemRect = vopt->rect;
            itemRect.adjust(0, 2, 0, -2);
            QPainterPath path;
            path.addRoundedRect(itemRect, 4, 4);
            if (vopt->state & QStyle::State_Selected)
            {
                // 选中（悬停时覆盖高亮）
                painter->fillPath(path, elaMixColor(ElaThemeColor(_themeMode, BasicSelectedAlpha), ElaThemeColor(_themeMode, BasicSelectedHoverAlpha), hoverRatio));
            }
            else if (hoverRatio > 0)
            {
                // 覆盖时颜色
                QColor hoverColor = ElaThemeColor(_themeMode, BasicHoverAlpha);
                hoverColor.setAlphaF(hoverColor.alphaF() * hoverRatio);
                painter->fillPath(path, hoverColor);
            }
            painter->restore();
        }
        return;
    }
    case QStyle::PE_PanelItemViewRow:
    {
        // Item背景隔行变色
        if (const QStyleOptionViewItem* vopt = qstyleoption_cast<const QStyleOptionViewItem*>(option))
        {
            if (vopt->features == QStyleOptionViewItem::Alternate)
            {
                painter->save();
                painter->setRenderHint(QPainter::Antialiasing);
                painter->setPen(Qt::NoPen);
                painter->setBrush(ElaThemeColor(_themeMode, BasicAlternating));
                painter->drawRect(vopt->rect);
                painter->restore();
            }
        }
        return;
    }
    case QStyle::PE_Widget:
    {
        return;
    }
    default:
    {
        break;
    }
    }
    QProxyStyle::drawPrimitive(element, option, painter, widget);
}

void ElaListViewStyle::drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    switch (element)
    {
    case QStyle::CE_ShapedFrame:
    {
        // viewport视口外的其他区域背景
        if (!_pIsTransparent)
        {
            QRect frameRect = option->rect;
            frameRect.adjust(1, 1, -1, -1);
            painter->save();
            painter->setRenderHints(QPainter::Antialiasing);
            painter->setPen(ElaThemeColor(_themeMode, PopupBorder));
            painter->setBrush(ElaThemeColor(_themeMode, BasicBaseAlpha));
            painter->drawRoundedRect(frameRect, 3, 3);
            painter->restore();
        }
        return;
    }
    case QStyle::CE_ItemViewItem:
    {
        if (const QStyleOptionViewItem* vopt = qstyleoption_cast<const QStyleOptionViewItem*>(option))
        {
            // 背景绘制
            this->drawPrimitive(QStyle::PE_PanelItemViewItem, option, painter, widget);

            // 内容绘制
            QRect itemRect = option->rect;
            painter->save();
            painter->setRenderHints(QPainter::Antialiasing | QPainter::SmoothPixmapTransform | QPainter::TextAntialiasing);
            const ElaListView* listView = dynamic_cast<const ElaListView*>(widget);
            QListView::ViewMode viewMode = listView->viewMode();
            // QRect checkRect = proxy()->subElementRect(SE_ItemViewItemCheckIndicator, vopt, widget);
            QRect iconRect = proxy()->subElementRect(SE_ItemViewItemDecoration, vopt, widget);
            QRect textRect = proxy()->subElementRect(SE_ItemViewItemText, vopt, widget);
            iconRect.adjust(_leftPadding, 0, 0, 0);
            textRect.adjust(_leftPadding, 0, 0, 0);
            // 图标绘制
            if (!vopt->icon.isNull())
            {
                QIcon::Mode mode = QIcon::Normal;
                if (!(vopt->state.testFlag(QStyle::State_Enabled)))
                {
                    mode = QIcon::Disabled;
                }
                else if (vopt->state.testFlag(QStyle::State_Selected))
                {
                    mode = QIcon::Selected;
                }
                QIcon::State state = vopt->state & QStyle::State_Open ? QIcon::On : QIcon::Off;
                vopt->icon.paint(painter, iconRect, vopt->decorationAlignment, mode, state);
            }
            // 文字绘制
            if (!vopt->text.isEmpty())
            {
                painter->setPen(ElaThemeColor(_themeMode, BasicText));
                painter->drawText(textRect, vopt->displayAlignment, vopt->text);
            }
            // 选中特效
            if (vopt->state.testFlag(QStyle::State_Selected) && viewMode == QListView::ListMode)
            {
                int heightOffset = itemRect.height() / 4;
                painter->setPen(Qt::NoPen);
                painter->setBrush(ElaThemeColor(_themeMode, PrimaryNormal));
                painter->drawRoundedRect(QRectF(itemRect.x() + 3, itemRect.y() + heightOffset, 3, itemRect.height() - 2 * heightOffset), 3, 3);
            }
            painter->restore();
        }

        return;
    }
    default:
    {
        break;
    }
    }
    QProxyStyle::drawControl(element, option, painter, widget);
}

QSize ElaListViewStyle::sizeFromContents(ContentsType type, const QStyleOption* option, const QSize& size, const QWidget* widget) const
{
    switch (type)
    {
    case QStyle::CT_ItemViewItem:
    {
        QSize itemSize = QProxyStyle::sizeFromContents(type, option, size, widget);
        const ElaListView* listView = dynamic_cast<const ElaListView*>(widget);
        QListView::ViewMode viewMode = listView->viewMode();
        if (viewMode == QListView::ListMode)
        {
            itemSize.setWidth(itemSize.width() + _leftPadding);
        }
        itemSize.setHeight(_pItemHeight);
        return itemSize;
    }
    default:
    {
        break;
    }
    }
    return QProxyStyle::sizeFromContents(type, option, size, widget);
}

void ElaListViewStyle::_startRowHoverAnimation(bool isFadeIn, const QRect& rowRect, const QWidget* widget) const
{
    QVariantAnimation*& rowAnimation = isFadeIn ? _hoverInAnimation : _hoverOutAnimation;
    if (!rowAnimation)
    {
        rowAnimation = new QVariantAnimation;
        const QAbstractScrollArea* scrollArea = dynamic_cast<const QAbstractScrollArea*>(widget);
        // 行悬停过渡的脏区域是视口上的整行条带（同 QAbstractItemView 自身悬停处理），
        // 必须走 viewport()->update(rect)，rect 为视口坐标
        QPointer<QWidget> widgetGuard = scrollArea ? const_cast<QAbstractScrollArea*>(scrollArea)->viewport() : const_cast<QWidget*>(widget);
        connect(rowAnimation, &QVariantAnimation::valueChanged, this, [=](const QVariant& value) {
            if (isFadeIn)
            {
                this->_hoverInRatio = value.toReal();
            }
            else
            {
                this->_hoverOutRatio = value.toReal();
            }
            if (widgetGuard && widgetGuard->isVisible())
            {
                const QRect& animRect = isFadeIn ? this->_hoverInRect : this->_hoverOutRect;
                if (animRect.isValid())
                {
                    widgetGuard->update(QRect(0, animRect.y(), widgetGuard->width(), animRect.height()).adjusted(0, -2, 0, 2));
                }
            }
        });
    }
    if (isFadeIn)
    {
        _hoverInRect = rowRect;
    }
    else
    {
        _hoverOutRect = rowRect;
    }
    rowAnimation->stop();
    rowAnimation->setDuration(150);
    rowAnimation->setEasingCurve(QEasingCurve::OutCubic);
    rowAnimation->setStartValue(isFadeIn ? _hoverInRatio : _hoverOutRatio);
    rowAnimation->setEndValue(isFadeIn ? 1.0 : 0.0);
    rowAnimation->start();
}
