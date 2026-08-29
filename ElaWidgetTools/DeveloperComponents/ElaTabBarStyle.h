#ifndef ELATABBARSTYLE_H
#define ELATABBARSTYLE_H

#include <QProxyStyle>

#include "ElaDef.h"
class ElaTabBarStyle : public QProxyStyle
{
    Q_OBJECT
    Q_PRIVATE_CREATE(QSize, TabSize)
public:
    explicit ElaTabBarStyle(QStyle* style = nullptr);
    ~ElaTabBarStyle() override;
    void drawPrimitive(QStyle::PrimitiveElement pe, const QStyleOption* opt, QPainter* p, const QWidget* w) const override;
    void drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;
    QSize sizeFromContents(ContentsType type, const QStyleOption* option, const QSize& size, const QWidget* widget) const override;
    QRect subElementRect(SubElement element, const QStyleOption* option, const QWidget* widget) const override;

private:
    ElaThemeType::ThemeMode _themeMode;
    mutable QRect _hoverRect;
    mutable QRect _fadeRect;
    mutable qreal _hoverInRatio{0};
    mutable qreal _hoverOutRatio{0};
    mutable bool _firstPaint{true};
    void _startTabHoverAnimation(bool isFadeIn, const QWidget* widget) const;
};

#endif // ELATABBARSTYLE_H
