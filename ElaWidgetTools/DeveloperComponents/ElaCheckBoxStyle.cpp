#include "ElaCheckBoxStyle.h"

#include <QDebug>
#include <QPainter>
#include <QPointer>
#include <QStyleOption>
#include <QVariantAnimation>

#include "ElaTheme.h"
ElaCheckBoxStyle::ElaCheckBoxStyle(QStyle* style)
{
    _pCheckIndicatorWidth = 21;
    _themeMode = eTheme->getThemeMode();
    connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode) {
        _themeMode = themeMode;
    });
}

ElaCheckBoxStyle::~ElaCheckBoxStyle()
{
}

void ElaCheckBoxStyle::drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    // qDebug() << element << option->rect;
    switch (element)
    {
    case QStyle::CE_CheckBox:
    {
        if (const QStyleOptionButton* bopt = qstyleoption_cast<const QStyleOptionButton*>(option))
        {
            bool isEnabled = bopt->state.testFlag(QStyle::State_Enabled);
            // 悬停与勾选过渡
            bool isHovered = bopt->state.testFlag(QStyle::State_MouseOver);
            bool isChecked = bopt->state.testFlag(QStyle::State_On) || bopt->state.testFlag(QStyle::State_NoChange);
            if (_firstPaint)
            {
                _firstPaint = false;
                _lastHovered = isHovered;
                _lastChecked = isChecked;
                _hoverRatio = isHovered ? 1 : 0;
                _checkRatio = isChecked ? 1 : 0;
            }
            else
            {
                if (isHovered != _lastHovered)
                {
                    _startRatioAnimation(&_hoverRatio, isHovered ? 1 : 0, 150, QEasingCurve::OutCubic, widget);
                    _lastHovered = isHovered;
                }
                if (isChecked != _lastChecked)
                {
                    _startRatioAnimation(&_checkRatio, isChecked ? 1 : 0, 200, QEasingCurve::OutBack, widget);
                    _lastChecked = isChecked;
                }
            }
            painter->save();
            painter->setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
            QRect checkBoxRect = bopt->rect;
            int yOffset = (checkBoxRect.height() - _pCheckIndicatorWidth) / 2;
            QRect checkRect(checkBoxRect.x(), checkBoxRect.y() + yOffset, _pCheckIndicatorWidth, _pCheckIndicatorWidth);
            checkRect.adjust(1, 1, -1, -1);
            //复选框绘制
            painter->setPen(Qt::NoPen);
            if (isChecked)
            {
                painter->setPen(Qt::NoPen);
                painter->setBrush(bopt->state.testFlag(QStyle::State_Sunken) ? ElaThemeColor(_themeMode, PrimaryPress) : elaMixColor(ElaThemeColor(_themeMode, PrimaryNormal), ElaThemeColor(_themeMode, PrimaryHover), _hoverRatio));
            }
            else
            {
                painter->setPen(ElaThemeColor(_themeMode, BasicBorderDeep));
                if (!bopt->state.testFlag(QStyle::State_Sunken))
                {
                    painter->setBrush(elaMixColor(ElaThemeColor(_themeMode, BasicBase), ElaThemeColor(_themeMode, BasicHover), _hoverRatio));
                }
            }
            painter->drawRoundedRect(checkRect, 2, 2);
            //图标绘制
            painter->setPen(ElaThemeColor(ElaThemeType::Dark, BasicText));
            if (bopt->state.testFlag(QStyle::State_On))
            {
                painter->save();
                QFont iconFont = QFont("ElaAwesome");
                iconFont.setPixelSize(_pCheckIndicatorWidth * 0.75);
                painter->setFont(iconFont);
                // 勾选弹出（缩放+透明度）
                qreal scale = 0.6 + 0.4 * _checkRatio;
                painter->translate(checkRect.center());
                painter->scale(scale, scale);
                painter->translate(-checkRect.center());
                painter->setOpacity(qBound(0.0, _checkRatio, 1.0));
                painter->drawText(checkRect, Qt::AlignCenter, QChar((unsigned short)ElaIconType::Check));
                painter->restore();
            }
            else if (bopt->state.testFlag(QStyle::State_NoChange))
            {
                QLine checkLine(checkRect.x() + 3, checkRect.center().y(), checkRect.right() - 3, checkRect.center().y());
                painter->drawLine(checkLine);
            }
            //文字绘制
            painter->setPen(isEnabled ? ElaThemeColor(_themeMode, BasicText) : ElaThemeColor(_themeMode, BasicTextDisable));
            QRect textRect(checkRect.right() + 10, checkBoxRect.y() + yOffset, checkBoxRect.width() - checkRect.right() - 10, _pCheckIndicatorWidth);
            painter->drawText(textRect, Qt::AlignLeft | Qt::AlignVCenter, bopt->text);
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

int ElaCheckBoxStyle::pixelMetric(PixelMetric metric, const QStyleOption* option, const QWidget* widget) const
{
    // qDebug() << metric << QProxyStyle::pixelMetric(metric, option, widget);
    switch (metric)
    {
    case QStyle::PM_IndicatorWidth:
    {
        return _pCheckIndicatorWidth;
    }
    case QStyle::PM_IndicatorHeight:
    {
        return _pCheckIndicatorWidth;
    }
    case QStyle::PM_CheckBoxLabelSpacing:
    {
        return 10;
    }
    default:
    {
        break;
    }
    }
    return QProxyStyle::pixelMetric(metric, option, widget);
}

void ElaCheckBoxStyle::_startRatioAnimation(qreal* targetRatio, qreal endRatio, int duration, QEasingCurve::Type curve, const QWidget* widget) const
{
    QVariantAnimation*& ratioAnimation = targetRatio == &_hoverRatio ? _hoverRatioAnimation : _checkRatioAnimation;
    if (!ratioAnimation)
    {
        ratioAnimation = new QVariantAnimation;
        QPointer<QWidget> widgetGuard = const_cast<QWidget*>(widget);
        connect(ratioAnimation, &QVariantAnimation::valueChanged, this, [=](const QVariant& value) {
            *targetRatio = value.toReal();
            if (widgetGuard && widgetGuard->isVisible())
            {
                widgetGuard->update();
            }
        });
    }
    ratioAnimation->stop();
    ratioAnimation->setDuration(duration);
    ratioAnimation->setEasingCurve(QEasingCurve(curve));
    ratioAnimation->setStartValue(*targetRatio);
    ratioAnimation->setEndValue(endRatio);
    ratioAnimation->start();
}
