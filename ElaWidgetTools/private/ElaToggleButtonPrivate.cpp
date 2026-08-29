#include "ElaToggleButtonPrivate.h"

#include <QPropertyAnimation>

#include "ElaTheme.h"
#include "ElaToggleButton.h"
ElaToggleButtonPrivate::ElaToggleButtonPrivate(QObject* parent)
    : QObject{parent}
{
}

ElaToggleButtonPrivate::~ElaToggleButtonPrivate()
{
}

void ElaToggleButtonPrivate::_startHoverAlphaAnimation(qreal endValue)
{
    Q_Q(ElaToggleButton);
    if (!_hoverAlphaAnimation)
    {
        _hoverAlphaAnimation = new QPropertyAnimation(this, "pHoverAlpha", q);
        connect(_hoverAlphaAnimation, &QPropertyAnimation::valueChanged, q, [=]() {
            if (q->isVisible())
            {
                q->update();
            }
        });
    }
    _hoverAlphaAnimation->stop();
    _hoverAlphaAnimation->setDuration(175);
    _hoverAlphaAnimation->setStartValue(_pHoverAlpha);
    _hoverAlphaAnimation->setEndValue(endValue);
    _hoverAlphaAnimation->start();
}

void ElaToggleButtonPrivate::_startToggleAlphaAnimation(qreal endValue)
{
    Q_Q(ElaToggleButton);
    if (!_toggleAlphaAnimation)
    {
        _toggleAlphaAnimation = new QPropertyAnimation(this, "pToggleAlpha", q);
        connect(_toggleAlphaAnimation, &QPropertyAnimation::valueChanged, q, [=]() {
            if (q->isVisible())
            {
                q->update();
            }
        });
        connect(_toggleAlphaAnimation, &QPropertyAnimation::finished, q, [=]() {
            _isAlphaAnimationFinished = true;
        });
    }
    _toggleAlphaAnimation->stop();
    _toggleAlphaAnimation->setDuration(250);
    _toggleAlphaAnimation->setStartValue(_pToggleAlpha);
    _toggleAlphaAnimation->setEndValue(endValue);
    _toggleAlphaAnimation->start();
}
