#ifndef ELARIBBONTABBARPRIVATE_H
#define ELARIBBONTABBARPRIVATE_H

#include <QObject>
#include <QRect>
#include <QStringList>

#include "ElaDef.h"
#include "ElaProperty.h"

class ElaRibbonTabBar;
class ElaRibbonTabBarPrivate : public QObject
{
    Q_OBJECT
    Q_D_CREATE(ElaRibbonTabBar)
    Q_PROPERTY_CREATE_D(int, CurrentIndex)
public:
    explicit ElaRibbonTabBarPrivate(QObject* parent = nullptr);
    ~ElaRibbonTabBarPrivate() override;

    QList<QRect> tabRects() const;
    int tabAt(const QPoint& pos) const;

private:
    friend class ElaRibbonTabBar;
    QStringList _tabTitles;
    int _hoveredIndex{-1};
    ElaThemeType::ThemeMode _themeMode;
};

#endif // ELARIBBONTABBARPRIVATE_H
