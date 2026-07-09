#include "ElaRibbonGroup.h"

#include <QFontMetrics>
#include <QHBoxLayout>
#include <QPainter>
#include <QVBoxLayout>

#include "ElaIcon.h"
#include "ElaTheme.h"
#include "ElaToolButton.h"
#include "private/ElaRibbonGroupPrivate.h"

ElaRibbonGroup::ElaRibbonGroup(const QString &title, QWidget *parent) : QWidget{parent}, d_ptr(new ElaRibbonGroupPrivate())
{
	Q_D(ElaRibbonGroup);
	d->q_ptr = this;
	d->_title = title;

	setObjectName("ElaRibbonGroup");
	setAttribute(Qt::WA_StyledBackground, false);

	QVBoxLayout *mainLayout = new QVBoxLayout(this);
	mainLayout->setContentsMargins(4, 2, 10, 2);
	mainLayout->setSpacing(0);

	QWidget *contentWidget = new QWidget(this);
	contentWidget->setAttribute(Qt::WA_TranslucentBackground);
	d->_contentLayout = new QHBoxLayout(contentWidget);
	d->_contentLayout->setContentsMargins(0, 0, 0, 0);
	d->_contentLayout->setSpacing(1);
	d->_contentLayout->addStretch();
	mainLayout->addWidget(contentWidget, 1);
	mainLayout->addSpacing(16);

	d->_themeMode = eTheme->getThemeMode();
	connect(eTheme, &ElaTheme::themeModeChanged, this, [=](ElaThemeType::ThemeMode themeMode)
	{
		d->_themeMode = themeMode;
		update();
	});
}

ElaRibbonGroup::~ElaRibbonGroup()
{
}

void ElaRibbonGroup::setTitle(const QString &title)
{
	Q_D(ElaRibbonGroup);
	d->_title = title;
	update();
}

QString ElaRibbonGroup::getTitle() const
{
	Q_D(const ElaRibbonGroup);
	return d->_title;
}

ElaToolButton *ElaRibbonGroup::addToolButton(ElaIconType::IconName icon, const QString &text, ButtonSize size)
{
	Q_D(ElaRibbonGroup);
	ElaToolButton *button = new ElaToolButton(this);
	button->setElaIcon(icon);
	button->setText(text);
	if (size == Large)
	{
		button->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
		button->setIconSize(QSize(24, 24));
		button->setFixedSize(52, 52);
		QFont f = button->font();
		f.setPixelSize(11);
		button->setFont(f);
	}
	else
	{
		button->setToolButtonStyle(Qt::ToolButtonIconOnly);
		button->setIconSize(QSize(18, 18));
		button->setFixedSize(30, 30);
	}
	d->_contentLayout->insertWidget(d->_contentLayout->count() - 1, button);
	return button;
}

void ElaRibbonGroup::addWidget(QWidget *widget)
{
	Q_D(ElaRibbonGroup);
	d->_contentLayout->insertWidget(d->_contentLayout->count() - 1, widget);
}

void ElaRibbonGroup::paintEvent(QPaintEvent *event)
{
	Q_UNUSED(event);
	Q_D(ElaRibbonGroup);
	QPainter painter(this);
	painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);

	if (!d->_title.isEmpty())
	{
		QFont titleFont = font();
		titleFont.setPixelSize(11);
		painter.setFont(titleFont);
		QFontMetrics fm(titleFont);
		const int textW = fm.horizontalAdvance(d->_title);

		const int titleTop = height() - 16;
		const int titleH = 14;
		const int lineY = titleTop + titleH / 2;
		const int leftStart = 4;
		const int rightEnd = width() - 8;
		const int center = (leftStart + rightEnd) / 2;
		const int textGap = 6;
		const int textLeft = center - textW / 2 - textGap;
		const int textRight = center + textW / 2 + textGap;

		painter.setPen(QPen(ElaThemeColor(d->_themeMode, BasicBorder), 1));
		if (textLeft > leftStart)
		{
			painter.drawLine(leftStart, lineY, textLeft, lineY);
		}
		if (rightEnd > textRight)
		{
			painter.drawLine(textRight, lineY, rightEnd, lineY);
		}

		painter.setPen(ElaThemeColor(d->_themeMode, BasicTextCategory));
		QRect titleRect(leftStart, titleTop, rightEnd - leftStart, titleH);
		painter.drawText(titleRect, Qt::AlignCenter, d->_title);
	}

	painter.setPen(QPen(ElaThemeColor(d->_themeMode, BasicBorder), 1));
	int sepX = width() - 5;
	int sepTop = 4;
	int sepBottom = height() - 4;
	painter.drawLine(sepX, sepTop, sepX, sepBottom);
}

QSize ElaRibbonGroup::sizeHint() const
{
	Q_D(const ElaRibbonGroup);
	QSize hint = QWidget::sizeHint();
	QFont f = font();
	f.setPixelSize(11);
	QFontMetrics fm(f);
	int titleW = fm.horizontalAdvance(d->_title) + 20;
	if (hint.width() < titleW)
	{
		hint.setWidth(titleW);
	}
	if (hint.height() < 80)
	{
		hint.setHeight(80);
	}
	return hint;
}

ElaRibbonGroupPrivate::ElaRibbonGroupPrivate(QObject *parent)
	: QObject{parent}
{
}

ElaRibbonGroupPrivate::~ElaRibbonGroupPrivate()
{
}