#include "ElaExponentialBlur.h"

#include <QPainter>
#include <QPixmap>

#include "ElaExponentialBlurPrivate.h"
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
#include <cmath>
#endif
Q_SINGLETON_CREATE_CPP(ElaExponentialBlur)
ElaExponentialBlur::ElaExponentialBlur(QObject* parent)
    : QObject{parent}, d_ptr(new ElaExponentialBlurPrivate())
{
    Q_D(ElaExponentialBlur);
    d->q_ptr = this;
}

ElaExponentialBlur::~ElaExponentialBlur()
{
}

QPixmap ElaExponentialBlur::doExponentialBlur(QImage img, const quint16& blurRadius)
{
    QImage shadowImage = img.convertToFormat(QImage::Format_ARGB32);
    // 指数模糊的计算量随像素数线性增长。先按 1/4 边长降采样、用同步缩小的半径模糊，
    // 再平滑放大回原尺寸：衰减长度与图像尺寸的比例不变，结果视觉几乎无差，
    // 计算量降约 16 倍（Mica/亚克力背景在窗口 resize 时会反复全量调用）
    const int kDownScale = 4;
    if (blurRadius >= kDownScale && shadowImage.width() > kDownScale && shadowImage.height() > kDownScale)
    {
        QSize smallSize(shadowImage.width() / kDownScale, shadowImage.height() / kDownScale);
        QImage smallImage = shadowImage.scaled(smallSize, Qt::IgnoreAspectRatio, Qt::SmoothTransformation);
        ElaExponentialBlur::getInstance()->d_ptr->_drawExponentialBlur(smallImage, blurRadius / kDownScale);
        shadowImage = smallImage.scaled(shadowImage.size(), Qt::IgnoreAspectRatio, Qt::SmoothTransformation);
        return QPixmap::fromImage(shadowImage);
    }
    ElaExponentialBlur::getInstance()->d_ptr->_drawExponentialBlur(shadowImage, blurRadius);
    return QPixmap::fromImage(shadowImage);
}
