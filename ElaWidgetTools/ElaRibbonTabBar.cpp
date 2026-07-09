#include "ElaRibbonTabBar.h"

#include <QFontMetrics>
#include <QMouseEvent>
#include <QPainter>

#include "ElaTheme.h"
#include "private/ElaRibbonTabBarPrivate.h"

ElaRibbonTabBar::ElaRibbonTabBar(QWidget *parent) : QWidget{parent}, d_ptr(new ElaRibbonTabBarPrivate())
{
	Q_D(ElaRibbonTabBar);
	d->q_ptr = this;
	d->_pCurrentIndex = 0;

	setObjectName("ElaRibbonTabBar");
	setMouseTracking(true);
	setAttribute(Qt::WA_StyledBackground, false);
	setFixedHeight(32);

	d->_themeMode = eTheme->getThemeMode();
	connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode)
	{
		d->_themeMode = themeMode;
		update();
	});
}

ElaRibbonTabBar::~ElaRibbonTabBar()
{
}

int ElaRibbonTabBar::appendTab(const QString &title)
{
	Q_D(ElaRibbonTabBar);
	d->_tabTitles.append(title);
	update();
	updateGeometry();
	return d->_tabTitles.size() - 1;
}

void ElaRibbonTabBar::removeTab(int index)
{
	Q_D(ElaRibbonTabBar);
	if (index < 0 || index >= d->_tabTitles.size())
	{
		return;
	}
	d->_tabTitles.removeAt(index);
	if (d->_pCurrentIndex >= d->_tabTitles.size())
	{
		d->_pCurrentIndex = qMax(0, d->_tabTitles.size() - 1);
		Q_EMIT pCurrentIndexChanged();
	}
	update();
	updateGeometry();
}

void ElaRibbonTabBar::clear()
{
	Q_D(ElaRibbonTabBar);
	d->_tabTitles.clear();
	d->_pCurrentIndex = 0;
	d->_hoveredIndex = -1;
	update();
	updateGeometry();
}

int ElaRibbonTabBar::tabCount() const
{
	Q_D(const ElaRibbonTabBar);
	return d->_tabTitles.size();
}

QString ElaRibbonTabBar::tabText(int index) const
{
	Q_D(const ElaRibbonTabBar);
	if (index < 0 || index >= d->_tabTitles.size())
	{
		return {};
	}
	return d->_tabTitles.at(index);
}

void ElaRibbonTabBar::setTabText(int index, const QString &title)
{
	Q_D(ElaRibbonTabBar);
	if (index < 0 || index >= d->_tabTitles.size())
	{
		return;
	}
	d->_tabTitles[index] = title;
	update();
	updateGeometry();
}

void ElaRibbonTabBar::setCurrentIndex(int currentIndex)
{
	Q_D(ElaRibbonTabBar);
	if (currentIndex < 0 || currentIndex >= d->_tabTitles.size())
	{
		return;
	}
	if (d->_pCurrentIndex == currentIndex)
	{
		return;
	}
	d->_pCurrentIndex = currentIndex;
	Q_EMIT pCurrentIndexChanged();
	update();
}

int ElaRibbonTabBar::getCurrentIndex() const
{
	Q_D(const ElaRibbonTabBar);
	return d->_pCurrentIndex;
}

void ElaRibbonTabBar::paintEvent(QPaintEvent *event)
{
	Q_UNUSED(event);
	Q_D(ElaRibbonTabBar);
	QPainter painter(this);
	painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);

	QFont tabFont = font();
	tabFont.setPixelSize(14);
	painter.setFont(tabFont);

	QList<QRect> rects = d->tabRects();
	for (int i = 0; i < rects.size(); ++i)
	{
		const QRect &r = rects.at(i);
		const QString &title = d->_tabTitles.at(i);
		bool isSelected = (i == d->_pCurrentIndex);
		bool isHovered = (i == d->_hoveredIndex);

		if (isSelected)
		{
			painter.setPen(Qt::NoPen);
			painter.setBrush(ElaThemeColor(d->_themeMode, PrimaryNormal));
			QRect markRect(r.x() + 8, r.bottom() - 2, r.width() - 16, 2);
			painter.drawRect(markRect);
			painter.setPen(ElaThemeColor(d->_themeMode, BasicText));
		}
		else if (isHovered)
		{
			painter.setPen(Qt::NoPen);
			painter.setBrush(ElaThemeColor(d->_themeMode, BasicHover));
			painter.drawRoundedRect(r.adjusted(4, 4, -4, -4), 4, 4);
			painter.setPen(ElaThemeColor(d->_themeMode, BasicText));
		}
		else
		{
			painter.setPen(ElaThemeColor(d->_themeMode, BasicTextNoFocus));
		}
		painter.drawText(r, Qt::AlignCenter, title);
	}
}

void ElaRibbonTabBar::mouseMoveEvent(QMouseEvent *event)
{
	Q_D(ElaRibbonTabBar);
	int idx = d->tabAt(event->pos());
	if (idx != d->_hoveredIndex)
	{
		d->_hoveredIndex = idx;
		update();
	}
	QWidget::mouseMoveEvent(event);
}

void ElaRibbonTabBar::mousePressEvent(QMouseEvent *event)
{
	Q_D(ElaRibbonTabBar);
	if (event->button() == Qt::LeftButton)
	{
		int idx = d->tabAt(event->pos());
		if (idx >= 0)
		{
			const bool isReclick = (idx == d->_pCurrentIndex);
			if (!isReclick)
			{
				d->_pCurrentIndex = idx;
				Q_EMIT pCurrentIndexChanged();
				update();
			}
			else
			{
				Q_EMIT tabReclicked(idx);
			}
			Q_EMIT tabClicked(idx);
		}
	}
	QWidget::mousePressEvent(event);
}

void ElaRibbonTabBar::leaveEvent(QEvent *event)
{
	Q_D(ElaRibbonTabBar);
	if (d->_hoveredIndex != -1)
	{
		d->_hoveredIndex = -1;
		update();
	}
	QWidget::leaveEvent(event);
}

QSize ElaRibbonTabBar::sizeHint() const
{
	Q_D(const ElaRibbonTabBar);
	QFont tabFont = font();
	tabFont.setPixelSize(14);
	QFontMetrics fm(tabFont);
	int total = 16;
	for (const QString &t: d->_tabTitles)
	{
		total += fm.horizontalAdvance(t) + 28;
	}
	return QSize(qMax(total, 80), 32);
}

ElaRibbonTabBarPrivate::ElaRibbonTabBarPrivate(QObject *parent)
	: QObject{parent}
{
}

ElaRibbonTabBarPrivate::~ElaRibbonTabBarPrivate()
{
}

QList<QRect> ElaRibbonTabBarPrivate::tabRects() const
{
	QList<QRect> rects;
	if (_tabTitles.isEmpty())
	{
		return rects;
	}
	QFont tabFont = q_ptr->font();
	tabFont.setPixelSize(14);
	QFontMetrics fm(tabFont);
	int x = 16;
	for (const QString &t: _tabTitles)
	{
		int w = fm.horizontalAdvance(t) + 28;
		rects.append(QRect(x, 0, w, q_ptr->height()));
		x += w;
	}
	return rects;
}

int ElaRibbonTabBarPrivate::tabAt(const QPoint &pos) const
{
	QList<QRect> rects = tabRects();
	for (int i = 0; i < rects.size(); ++i)
	{
		if (rects.at(i).contains(pos))
		{
			return i;
		}
	}
	return -1;
}