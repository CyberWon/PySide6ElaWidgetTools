#include "ElaCocoaWindowHelper.h"

#ifdef Q_OS_MACOS

#include <QWidget>

#import <AppKit/AppKit.h>

void ElaCocoaWindowHelper::setupFramelessWindow(QWidget* window)
{
    if (!window)
    {
        return;
    }
    NSView* view = reinterpret_cast<NSView*>(window->winId());
    if (!view)
    {
        return;
    }
    NSWindow* nsWindow = [view window];
    if (!nsWindow)
    {
        return;
    }
    // 保留 Titled mask，仅让内容视图延伸到标题栏下并隐藏标题栏外观。
    // 移除 Titled（即 Qt::FramelessWindowHint 的效果）会让 NSWindow 丢失
    // 原生最大化（zoom）/还原、全屏、分屏等系统行为。
    nsWindow.styleMask |= NSWindowStyleMaskFullSizeContentView;
    nsWindow.titlebarAppearsTransparent = YES;
    nsWindow.titleVisibility = NSWindowTitleHidden;
    // 窗口拖拽由 ElaAppBar 自行处理，避免背景拖拽与拖拽逻辑冲突。
    nsWindow.movableByWindowBackground = NO;
    // 隐藏原生红绿灯按钮（ElaAppBar 自绘最小化/最大化/关闭按钮）。
    [[nsWindow standardWindowButton:NSWindowCloseButton] setHidden:YES];
    [[nsWindow standardWindowButton:NSWindowMiniaturizeButton] setHidden:YES];
    [[nsWindow standardWindowButton:NSWindowZoomButton] setHidden:YES];
}

#endif // Q_OS_MACOS
