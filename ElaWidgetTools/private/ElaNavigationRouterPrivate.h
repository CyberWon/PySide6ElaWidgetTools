#ifndef ELANAVIGATIONROUTERPRIVATE_H
#define ELANAVIGATIONROUTERPRIVATE_H
#include <QMap>
#include <QObject>
#include <QVariantMap>
#include <QVector>

#include "ElaProperty.h"
class ElaNavigationRouter;
class ElaNavigationRouterPrivate : public QObject
{
    Q_OBJECT
    Q_D_CREATE(ElaNavigationRouter)
    Q_PROPERTY_CREATE_D(int, MaxRouteCount)
public:
    explicit ElaNavigationRouterPrivate(QObject* parent = nullptr);
    ~ElaNavigationRouterPrivate() override;

private:
    int _currentIndex{-1};
    QVector<QVariantMap> _routeList;

    struct RouteContext
    {
        int currentIndex{-1};
        QVector<QVariantMap> routeList;
    };
    QMap<QObject*, RouteContext> _contextMap;
};

#endif // ELANAVIGATIONROUTERPRIVATE_H
