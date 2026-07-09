#ifndef ELARIBBONGROUPPRIVATE_H
#define ELARIBBONGROUPPRIVATE_H

#include <QObject>

#include "ElaDef.h"
#include "ElaProperty.h"

class QHBoxLayout;
class ElaRibbonGroup;
class ElaRibbonGroupPrivate : public QObject
{
    Q_OBJECT
    Q_D_CREATE(ElaRibbonGroup)
public:
    explicit ElaRibbonGroupPrivate(QObject* parent = nullptr);
    ~ElaRibbonGroupPrivate() override;

private:
    friend class ElaRibbonGroup;
    QString _title;
    QHBoxLayout* _contentLayout{nullptr};
    ElaThemeType::ThemeMode _themeMode;
};

#endif // ELARIBBONGROUPPRIVATE_H
