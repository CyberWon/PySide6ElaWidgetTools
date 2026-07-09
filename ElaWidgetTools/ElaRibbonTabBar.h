#ifndef ELARIBBONTABBAR_H
#define ELARIBBONTABBAR_H

#include <QWidget>

#include "ElaDef.h"
#include "ElaProperty.h"

class ElaRibbonTabBarPrivate;

class ELA_EXPORT ElaRibbonTabBar : public QWidget
{
    Q_OBJECT
    Q_Q_CREATE(ElaRibbonTabBar)
    Q_PROPERTY_CREATE_Q_H(int, CurrentIndex)
public:
    explicit ElaRibbonTabBar(QWidget* parent = nullptr);
    ~ElaRibbonTabBar() override;

    int appendTab(const QString& title);
    void removeTab(int index);
    void clear();

    int tabCount() const;
    QString tabText(int index) const;
    void setTabText(int index, const QString& title);

Q_SIGNALS:
    Q_SIGNAL void tabClicked(int index);
    Q_SIGNAL void tabReclicked(int index);

protected:
    void paintEvent(QPaintEvent* event) override;
    void mouseMoveEvent(QMouseEvent* event) override;
    void mousePressEvent(QMouseEvent* event) override;
    void leaveEvent(QEvent* event) override;
    QSize sizeHint() const override;
};

#endif // ELARIBBONTABBAR_H
