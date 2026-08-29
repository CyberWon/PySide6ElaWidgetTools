#ifndef ELALISTVIEWSTYLE_H
#define ELALISTVIEWSTYLE_H

#include <QModelIndex>
#include <QProxyStyle>

#include "ElaDef.h"
class ElaListViewStyle : public QProxyStyle
{
    Q_OBJECT
    Q_PROPERTY_CREATE(int, ItemHeight)
    Q_PROPERTY_CREATE(bool, IsTransparent)
public:
    explicit ElaListViewStyle(QStyle* style = nullptr);
    ~ElaListViewStyle();
    void drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;
    void drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;
    QSize sizeFromContents(ContentsType type, const QStyleOption* option, const QSize& size, const QWidget* widget) const override;

private:
    ElaThemeType::ThemeMode _themeMode;
    int _leftPadding{11};
    mutable QPersistentModelIndex _hoverIndex;
    mutable QPersistentModelIndex _fadeOutIndex;
    mutable qreal _hoverInRatio{0};
    mutable qreal _hoverOutRatio{0};
    mutable bool _firstPaint{true};
    void _startRowHoverAnimation(bool isFadeIn, const QWidget* widget) const;
};

#endif // ELALISTVIEWSTYLE_H
