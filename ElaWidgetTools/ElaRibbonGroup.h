#ifndef ELARIBBONGROUP_H
#define ELARIBBONGROUP_H

#include <QWidget>

#include "ElaDef.h"
#include "ElaProperty.h"

class QHBoxLayout;
class ElaToolButton;
class ElaRibbonGroupPrivate;

class ELA_EXPORT ElaRibbonGroup : public QWidget
{
    Q_OBJECT
    Q_Q_CREATE(ElaRibbonGroup)
public:
    enum ButtonSize
    {
        Large = 0x0001,
        Small = 0x0002,
    };

    explicit ElaRibbonGroup(const QString& title, QWidget* parent = nullptr);
    ~ElaRibbonGroup() override;

    void setTitle(const QString& title);
    QString getTitle() const;

    ElaToolButton* addToolButton(ElaIconType::IconName icon, const QString& text, ButtonSize size = Large);
    void addWidget(QWidget* widget);

protected:
    void paintEvent(QPaintEvent* event) override;
    QSize sizeHint() const override;
};

#endif // ELARIBBONGROUP_H
