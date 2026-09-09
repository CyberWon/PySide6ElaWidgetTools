#ifndef ELACOCAOWINDOWHELPER_H
#define ELACOCAOWINDOWHELPER_H

#include <QtGlobal>

#ifdef Q_OS_MACOS

class QWidget;

class ElaCocoaWindowHelper
{
public:
    /**
     * @brief 将窗口设置为“原生无边框”样式。
     *
     * 与 Qt::FramelessWindowHint 不同，本函数保留 NSWindow 的原生标题栏
     * （Titled style mask），仅将其透明化并隐藏标题文字，同时开启
     * FullSizeContentView 让内容延伸到标题栏区域。
     *
     * 这样窗口仍然拥有完整的原生系统行为：原生最大化（zoom）/还原、
     * 全屏、拖拽到屏幕边缘分屏、Mission Control 等。
     */
    static void setupFramelessWindow(QWidget* window);
};

#endif // Q_OS_MACOS
#endif // ELACOCAOWINDOWHELPER_H
