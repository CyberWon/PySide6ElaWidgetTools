#ifndef ELANAVIGATIONROUTER_H
#define ELANAVIGATIONROUTER_H

#include <QObject>
#include <QVariantMap>

#include "ElaDef.h"
#include "ElaSingleton.h"

class ElaNavigationRouterPrivate;
class ELA_EXPORT ElaNavigationRouter : public QObject
{
    Q_OBJECT
    Q_Q_CREATE(ElaNavigationRouter)
    Q_SINGLETON_CREATE_H(ElaNavigationRouter)
    Q_PROPERTY_CREATE_Q_H(int, MaxRouteCount)
private:
    explicit ElaNavigationRouter(QObject* parent = nullptr);
    ~ElaNavigationRouter() override;

Q_SIGNALS:
    Q_SIGNAL void navigationRouterStateChanged(ElaNavigationRouterType::RouteMode routeMode);
    Q_SIGNAL void windowRouterStateChanged(QObject* context, ElaNavigationRouterType::RouteMode routeMode);

public:
    // 全局路由（向后兼容）
    ElaNavigationRouterType::NavigationRouteType navigationRoute(QObject* routeObject, QString routeFunctionName, const QVariantMap& routeData = {}, Qt::ConnectionType connectionType = Qt::AutoConnection);
    void clearNavigationRoute();
    void navigationRouteBack();
    void navigationRouteForward();

    // 每窗口独立路由
    ElaNavigationRouterType::NavigationRouteType navigationRoute(QObject* context, QObject* routeObject, QString routeFunctionName, const QVariantMap& routeData = {}, Qt::ConnectionType connectionType = Qt::AutoConnection);
    void clearNavigationRoute(QObject* context);
    void navigationRouteBack(QObject* context);
    void navigationRouteForward(QObject* context);
};

#endif // ELANAVIGATIONROUTER_H
