#ifndef ELARADIOBUTTONSTYLE_H
#define ELARADIOBUTTONSTYLE_H

#include <QEasingCurve>
#include <QProxyStyle>

#include "ElaDef.h"
class QVariantAnimation;
class ElaRadioButtonStyle : public QProxyStyle
{
    Q_OBJECT
public:
    explicit ElaRadioButtonStyle(QStyle* style = nullptr);
    ~ElaRadioButtonStyle();
    void drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;
    int pixelMetric(PixelMetric metric, const QStyleOption* option = nullptr, const QWidget* widget = nullptr) const override;

private:
    ElaThemeType::ThemeMode _themeMode;
    mutable qreal _hoverRatio{0};
    mutable qreal _checkRatio{0};
    mutable QVariantAnimation* _hoverRatioAnimation{nullptr};
    mutable QVariantAnimation* _checkRatioAnimation{nullptr};
    mutable bool _lastHovered{false};
    mutable bool _lastChecked{false};
    mutable bool _firstPaint{true};
    void _startRatioAnimation(qreal* targetRatio, qreal endRatio, int duration, QEasingCurve::Type curve, const QWidget* widget) const;
};

#endif // ELARADIOBUTTONSTYLE_H
