#include "ElaRadioButtonStyle.h"

#include <QPainter>
#include <QPainterPath>
#include <QPointer>
#include <QStyleOption>
#include <QVariantAnimation>

#include "ElaTheme.h"
ElaRadioButtonStyle::ElaRadioButtonStyle(QStyle* style)
{
    _themeMode = eTheme->getThemeMode();
    connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode) { _themeMode = themeMode; });
}

ElaRadioButtonStyle::~ElaRadioButtonStyle()
{
}

void ElaRadioButtonStyle::drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget) const
{
    switch (element)
    {
    case PE_IndicatorRadioButton:
    {
        const QStyleOptionButton* bopt = qstyleoption_cast<const QStyleOptionButton*>(option);
        if (!bopt)
        {
            break;
        }
        // 悬停与勾选过渡
        bool isHovered = bopt->state.testFlag(QStyle::State_MouseOver);
        bool isChecked = !bopt->state.testFlag(QStyle::State_Off);
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
        QRect buttonRect = bopt->rect;
        buttonRect.adjust(1, 1, -1, -1);
        painter->save();
        painter->setRenderHints(QPainter::Antialiasing | QPainter::SmoothPixmapTransform);

        if (bopt->state & QStyle::State_Off)
        {
            painter->setPen(QPen(ElaThemeColor(_themeMode, BasicBorder), 1.5));
            painter->setBrush(elaMixColor(ElaThemeColor(_themeMode, BasicBase), ElaThemeColor(_themeMode, BasicHover), _hoverRatio));
            painter->drawEllipse(QPointF(buttonRect.center().x() + 1, buttonRect.center().y() + 1), 8.5, 8.5);
        }
        else
        {
            painter->setPen(Qt::NoPen);
            // 外圆形
            painter->setBrush(ElaThemeColor(_themeMode, PrimaryNormal));
            painter->drawEllipse(QPointF(buttonRect.center().x() + 1, buttonRect.center().y() + 1), buttonRect.width() / 2, buttonRect.width() / 2);
            // 内圆形（勾选弹出）
            painter->setBrush(ElaThemeColor(_themeMode, BasicTextInvert));
            qreal dotScale = 0.6 + 0.4 * _checkRatio;
            if (bopt->state & QStyle::State_Sunken)
            {
                if (bopt->state & QStyle::State_MouseOver)
                {
                    painter->drawEllipse(QPointF(buttonRect.center().x() + 1, buttonRect.center().y() + 1), buttonRect.width() / 4.5 * dotScale, buttonRect.width() / 4.5 * dotScale);
                }
            }
            else
            {
                if (bopt->state & QStyle::State_MouseOver)
                {
                    painter->drawEllipse(QPointF(buttonRect.center().x() + 1, buttonRect.center().y() + 1), buttonRect.width() / 3.5 * dotScale, buttonRect.width() / 3.5 * dotScale);
                }
                else
                {
                    painter->drawEllipse(QPointF(buttonRect.center().x() + 1, buttonRect.center().y() + 1), buttonRect.width() / 4 * dotScale, buttonRect.width() / 4 * dotScale);
                }
            }
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

int ElaRadioButtonStyle::pixelMetric(PixelMetric metric, const QStyleOption* option, const QWidget* widget) const
{
    switch (metric)
    {
    case QStyle::PM_ExclusiveIndicatorWidth:
    {
        return 20;
    }
    case QStyle::PM_ExclusiveIndicatorHeight:
    {
        return 20;
    }
    default:
    {
        break;
    }
    }
    return QProxyStyle::pixelMetric(metric, option, widget);
}

void ElaRadioButtonStyle::_startRatioAnimation(qreal* targetRatio, qreal endRatio, int duration, QEasingCurve::Type curve, const QWidget* widget) const
{
    QVariantAnimation* ratioAnimation = new QVariantAnimation;
    QPointer<QWidget> widgetGuard = const_cast<QWidget*>(widget);
    connect(ratioAnimation, &QVariantAnimation::valueChanged, this, [=](const QVariant& value) {
        *targetRatio = value.toReal();
        if (widgetGuard && widgetGuard->isVisible())
        {
            widgetGuard->update();
        }
    });
    ratioAnimation->setDuration(duration);
    ratioAnimation->setEasingCurve(QEasingCurve(curve));
    ratioAnimation->setStartValue(*targetRatio);
    ratioAnimation->setEndValue(endRatio);
    ratioAnimation->start(QAbstractAnimation::DeleteWhenStopped);
}
