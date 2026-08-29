#include "ElaWindowStyle.h"

#include <QDebug>
#include <QPainter>
#include <QPainterPath>
#include <QPointer>
#include <QStyleOption>
#include <QVariantAnimation>
#include <QtMath>

#include "ElaTheme.h"
ElaWindowStyle::ElaWindowStyle(QStyle* style)
{
    _themeMode = eTheme->getThemeMode();
    connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode) { _themeMode = themeMode; });
}

ElaWindowStyle::~ElaWindowStyle()
{
}

void ElaWindowStyle::drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    switch (element)
    {
    case QStyle::PE_FrameTabBarBase:
    {
        return;
    }
    case QStyle::PE_PanelButtonTool:
    {
        if (option->state.testFlag(QStyle::State_Enabled))
        {
            painter->save();
            painter->setRenderHint(QPainter::Antialiasing);
            painter->setPen(Qt::NoPen);
            if (option->state.testFlag(QStyle::State_Sunken))
            {
                painter->setBrush(ElaThemeColor(_themeMode, BasicHoverAlpha));
                painter->drawRect(option->rect);
            }
            else
            {
                // 悬停过渡（按 widget 键控）
                bool isHovered = option->state.testFlag(QStyle::State_MouseOver);
                const QWidget* targetWidget = qobject_cast<const QWidget*>(option->styleObject ? option->styleObject : widget);
                if (targetWidget)
                {
                    ButtonHoverState& state = _hoverStates[targetWidget];
                    if (state.hovered != isHovered)
                    {
                        _startHoverAnimation(targetWidget, isHovered ? 1 : 0);
                        state.hovered = isHovered;
                    }
                    if (state.ratio > 0)
                    {
                        painter->setBrush(elaMixColor(QColor(Qt::transparent), ElaThemeColor(_themeMode, BasicPressAlpha), state.ratio));
                        painter->drawRect(option->rect);
                    }
                }
            }
            painter->restore();
        }
        return;
    }
    case QStyle::PE_IndicatorArrowLeft:
    {
        painter->save();
        painter->setRenderHint(QPainter::Antialiasing);
        painter->setPen(Qt::NoPen);
        painter->setBrush(option->state.testFlag(QStyle::State_Enabled) ? ElaThemeColor(_themeMode, BasicText) : ElaThemeColor(_themeMode, BasicTextDisable));
        // 左三角
        int sideLength = 10;
        QRect indicatorRect = option->rect;
        QPainterPath path;
        path.moveTo(indicatorRect.center().x() - qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y());
        path.lineTo(indicatorRect.center().x() + qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y() - sideLength / 2);
        path.lineTo(indicatorRect.center().x() + qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y() + sideLength / 2);
        path.closeSubpath();
        painter->drawPath(path);
        painter->restore();
        return;
    }
    case QStyle::PE_IndicatorArrowRight:
    {
        painter->save();
        painter->setRenderHint(QPainter::Antialiasing);
        painter->setPen(Qt::NoPen);
        painter->setBrush(option->state.testFlag(QStyle::State_Enabled) ? ElaThemeColor(_themeMode, BasicText) : ElaThemeColor(_themeMode, BasicTextDisable));
        // 右三角
        int sideLength = 10;
        QRect indicatorRect = option->rect;
        QPainterPath path;
        path.moveTo(indicatorRect.center().x() - qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y() - sideLength / 2);
        path.lineTo(indicatorRect.center().x() + qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y());
        path.lineTo(indicatorRect.center().x() - qCos(30 * M_PI / 180.0) * sideLength / 2, indicatorRect.center().y() + sideLength / 2);
        path.closeSubpath();
        painter->drawPath(path);
        painter->restore();
        return;
    }
    case QStyle::PE_IndicatorTabTear:
    {
        return;
    }
    case QStyle::PE_IndicatorDockWidgetResizeHandle:
    {
        painter->save();
        painter->setRenderHint(QPainter::Antialiasing);
        painter->setPen(QPen(ElaThemeColor(_themeMode, BasicBaseLine), 2));
        QRectF handleRect = option->rect;
        if (option->state.testFlag(QStyle::State_Horizontal))
        {
            painter->drawLine(handleRect.x(), handleRect.center().y(), handleRect.right(), handleRect.center().y());
        }
        else
        {
            painter->drawLine(handleRect.center().x(), handleRect.y(), handleRect.center().x(), handleRect.bottom());
        }
        painter->restore();
        return;
    }
    default:
    {
        break;
    }
    }
    QProxyStyle::drawPrimitive(element, option, painter, widget);
}

void ElaWindowStyle::drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    // qDebug() << element << option->rect;
    switch (element)
    {
    case QStyle::CE_RubberBand:
    {
        // 预览颜色
        QRect rubberBandRect = option->rect;
        painter->save();
        painter->setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
        painter->setPen(Qt::NoPen);
        painter->setBrush(ElaThemeColor(_themeMode, BasicHoverAlpha));
        painter->drawRect(rubberBandRect);
        painter->restore();
        return;
    }
    case QStyle::CE_TabBarTabShape:
    {
        // 背景绘制
        if (const QStyleOptionTab* topt = qstyleoption_cast<const QStyleOptionTab*>(option))
        {
            QRect tabRect = topt->rect;
            painter->save();
            painter->setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
            painter->setPen(Qt::NoPen);
            if (topt->state & QStyle::State_Selected)
            {
                if (topt->state & QStyle::State_Sunken)
                {
                    // 选中时点击
                    painter->setBrush(ElaThemeColor(_themeMode, BasicHoverAlpha));
                }
                else
                {
                    if (topt->state & QStyle::State_MouseOver)
                    {
                        // 选中时覆盖
                        painter->setBrush(ElaThemeColor(_themeMode, BasicSelectedHoverAlpha));
                    }
                    else
                    {
                        // 选中
                        painter->setBrush(ElaThemeColor(_themeMode, BasicSelectedAlpha));
                    }
                }
            }
            else
            {
                if (topt->state & QStyle::State_Sunken)
                {
                    // 点击时颜色
                    painter->setBrush(ElaThemeColor(_themeMode, BasicSelectedHoverAlpha));
                }
                else
                {
                    if (topt->state & QStyle::State_MouseOver)
                    {
                        // 覆盖时颜色
                        painter->setBrush(ElaThemeColor(_themeMode, BasicHoverAlpha));
                    }
                }
            }
            painter->drawRect(tabRect);
            // 间隔符绘制
            if (topt->position != QStyleOptionTab::End)
            {
                painter->setPen(Qt::NoPen);
                painter->setBrush(ElaThemeColor(_themeMode, PrimaryNormal));
                painter->drawRoundedRect(QRectF(tabRect.right() - 3, tabRect.y() + 7, 3, tabRect.height() - 14), 2, 2);
            }
            painter->restore();
        }
        return;
    }
    case QStyle::CE_TabBarTabLabel:
    {
        // 文字绘制
        if (const QStyleOptionTab* topt = qstyleoption_cast<const QStyleOptionTab*>(option))
        {
            painter->save();
            painter->setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
            painter->setPen(ElaThemeColor(_themeMode, BasicText));
            painter->drawText(topt->rect, Qt::AlignCenter, topt->text);
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

void ElaWindowStyle::_startHoverAnimation(const QWidget* targetWidget, qreal endRatio) const
{
    QVariantAnimation* hoverAnimation = new QVariantAnimation;
    QPointer<QWidget> widgetGuard = const_cast<QWidget*>(targetWidget);
    connect(hoverAnimation, &QVariantAnimation::valueChanged, this, [=](const QVariant& value) {
        if (!widgetGuard)
        {
            return;
        }
        ButtonHoverState state = _hoverStates.value(widgetGuard.data());
        state.ratio = value.toReal();
        _hoverStates[widgetGuard.data()] = state;
        widgetGuard->update();
    });
    hoverAnimation->setDuration(150);
    hoverAnimation->setEasingCurve(QEasingCurve::OutCubic);
    hoverAnimation->setStartValue(_hoverStates.value(targetWidget).ratio);
    hoverAnimation->setEndValue(endRatio);
    hoverAnimation->start(QAbstractAnimation::DeleteWhenStopped);
}
