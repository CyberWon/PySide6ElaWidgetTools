#include "ElaIconButtonPrivate.h"

#include <QPropertyAnimation>

#include "ElaIconButton.h"

ElaIconButtonPrivate::ElaIconButtonPrivate(QObject *parent)
    : QObject{parent}
{}

ElaIconButtonPrivate::~ElaIconButtonPrivate()
{

}

void ElaIconButtonPrivate::_startHoverAlphaAnimation(qreal endValue)
{
    Q_Q(ElaIconButton);
    if (!_hoverAlphaAnimation)
    {
        _hoverAlphaAnimation = new QPropertyAnimation(this, "pHoverAlpha", q);
        connect(_hoverAlphaAnimation, &QPropertyAnimation::valueChanged, q, [=]() {
            if (q->isVisible())
            {
                q->update();
            }
        });
        connect(_hoverAlphaAnimation, &QPropertyAnimation::finished, q, [=]() {
            _isAlphaAnimationFinished = true;
        });
    }
    _hoverAlphaAnimation->stop();
    _hoverAlphaAnimation->setDuration(175);
    _hoverAlphaAnimation->setStartValue(_pHoverAlpha);
    _hoverAlphaAnimation->setEndValue(endValue);
    _hoverAlphaAnimation->start();
}
