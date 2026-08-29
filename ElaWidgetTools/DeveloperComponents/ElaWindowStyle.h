#ifndef ELAWINDOWSTYLE_H
#define ELAWINDOWSTYLE_H

#include <QHash>
#include <QProxyStyle>

#include "ElaDef.h"
class ElaWindowStyle : public QProxyStyle
{
    Q_OBJECT
public:
    explicit ElaWindowStyle(QStyle* style = nullptr);
    ~ElaWindowStyle();
    void drawPrimitive(PrimitiveElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;
    void drawControl(ControlElement element, const QStyleOption* option, QPainter* painter, const QWidget* widget = nullptr) const override;

private:
    // 同一样式实例服务多个标题栏按钮，悬停状态按 widget 分别跟踪
    struct ButtonHoverState
    {
        qreal ratio{0};
        bool hovered{false};
    };
    ElaThemeType::ThemeMode _themeMode;
    mutable QHash<const QWidget*, ButtonHoverState> _hoverStates;
    void _startHoverAnimation(const QWidget* targetWidget, qreal endRatio) const;
};

#endif // ELAWINDOWSTYLE_H
