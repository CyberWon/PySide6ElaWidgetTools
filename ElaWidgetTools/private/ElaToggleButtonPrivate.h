#ifndef ELATOGGLEBUTTONPRIVATE_H
#define ELATOGGLEBUTTONPRIVATE_H

#include <QObject>

#include "ElaDef.h"
class ElaToggleButton;
class QPropertyAnimation;
class ElaToggleButtonPrivate : public QObject
{
    Q_OBJECT
    Q_D_CREATE(ElaToggleButton)
    Q_PROPERTY_CREATE_D(int, BorderRadius)
    Q_PROPERTY_CREATE_D(QString, Text)
    Q_PROPERTY_CREATE(int, ToggleAlpha)
    Q_PROPERTY_CREATE(int, HoverAlpha)
public:
    explicit ElaToggleButtonPrivate(QObject* parent = nullptr);
    ~ElaToggleButtonPrivate() override;

private:
    bool _isAlphaAnimationFinished{true};
    bool _isToggled{false};
    bool _isPressed{false};
    ElaThemeType::ThemeMode _themeMode;
    QPropertyAnimation* _hoverAlphaAnimation{nullptr};
    QPropertyAnimation* _toggleAlphaAnimation{nullptr};

    void _startHoverAlphaAnimation(qreal endValue);
    void _startToggleAlphaAnimation(qreal endValue);
};

#endif // ELATOGGLEBUTTONPRIVATE_H
