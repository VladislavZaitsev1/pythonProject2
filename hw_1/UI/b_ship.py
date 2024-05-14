# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_ship.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget_ship(object):
    def setupUi(self, widget_ship):
        if not widget_ship.objectName():
            widget_ship.setObjectName(u"widget_ship")
        widget_ship.resize(385, 372)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_ship.sizePolicy().hasHeightForWidth())
        widget_ship.setSizePolicy(sizePolicy)
        widget_ship.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(widget_ship)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(widget_ship)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 340))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_boardtemperature = QLabel(self.groupBox)
        self.label_boardtemperature.setObjectName(u"label_boardtemperature")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.label_boardtemperature.sizePolicy().hasHeightForWidth())
        self.label_boardtemperature.setSizePolicy(sizePolicy1)
        self.label_boardtemperature.setMinimumSize(QSize(0, 0))
        self.label_boardtemperature.setMaximumSize(QSize(125, 200))
        self.label_boardtemperature.setBaseSize(QSize(0, 0))
        self.label_boardtemperature.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_boardtemperature)

        self.lineEdit_boardtemperature = QLineEdit(self.groupBox)
        self.lineEdit_boardtemperature.setObjectName(u"lineEdit_boardtemperature")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_boardtemperature.sizePolicy().hasHeightForWidth())
        self.lineEdit_boardtemperature.setSizePolicy(sizePolicy2)
        self.lineEdit_boardtemperature.setMinimumSize(QSize(50, 20))
        self.lineEdit_boardtemperature.setMaximumSize(QSize(100, 20))
        self.lineEdit_boardtemperature.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lineEdit_boardtemperature.setStyleSheet(u"color: rgb(218, 255, 115);")
        self.lineEdit_boardtemperature.setCursorPosition(2)
        self.lineEdit_boardtemperature.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_boardtemperature.setReadOnly(True)
        self.lineEdit_boardtemperature.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout.addWidget(self.lineEdit_boardtemperature)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_razgerm = QLabel(self.groupBox)
        self.label_razgerm.setObjectName(u"label_razgerm")
        self.label_razgerm.setMinimumSize(QSize(0, 0))
        self.label_razgerm.setMaximumSize(QSize(125, 200))
        self.label_razgerm.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_razgerm)

        self.lineEdit_razgerm = QLineEdit(self.groupBox)
        self.lineEdit_razgerm.setObjectName(u"lineEdit_razgerm")
        self.lineEdit_razgerm.setMaximumSize(QSize(100, 20))
        self.lineEdit_razgerm.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lineEdit_razgerm.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_razgerm)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_Bak1 = QLabel(self.groupBox)
        self.label_Bak1.setObjectName(u"label_Bak1")
        self.label_Bak1.setMinimumSize(QSize(0, 0))
        self.label_Bak1.setMaximumSize(QSize(125, 200))
        self.label_Bak1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_Bak1)

        self.lineEdit_Bak1 = QLineEdit(self.groupBox)
        self.lineEdit_Bak1.setObjectName(u"lineEdit_Bak1")
        sizePolicy2.setHeightForWidth(self.lineEdit_Bak1.sizePolicy().hasHeightForWidth())
        self.lineEdit_Bak1.setSizePolicy(sizePolicy2)
        self.lineEdit_Bak1.setMaximumSize(QSize(100, 20))
        self.lineEdit_Bak1.setStyleSheet(u"color: rgb(85, 255, 127);")

        self.horizontalLayout_3.addWidget(self.lineEdit_Bak1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Bak2 = QLabel(self.groupBox)
        self.label_Bak2.setObjectName(u"label_Bak2")
        self.label_Bak2.setMinimumSize(QSize(0, 0))
        self.label_Bak2.setMaximumSize(QSize(125, 200))
        self.label_Bak2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_Bak2)

        self.lineEdit_Bak2 = QLineEdit(self.groupBox)
        self.lineEdit_Bak2.setObjectName(u"lineEdit_Bak2")
        self.lineEdit_Bak2.setMaximumSize(QSize(100, 20))
        self.lineEdit_Bak2.setStyleSheet(u"color: rgb(85, 255, 127);")

        self.horizontalLayout_4.addWidget(self.lineEdit_Bak2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Bak3 = QLabel(self.groupBox)
        self.label_Bak3.setObjectName(u"label_Bak3")
        self.label_Bak3.setMinimumSize(QSize(0, 0))
        self.label_Bak3.setMaximumSize(QSize(125, 200))
        self.label_Bak3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_Bak3)

        self.lineEdit_Bak3 = QLineEdit(self.groupBox)
        self.lineEdit_Bak3.setObjectName(u"lineEdit_Bak3")
        self.lineEdit_Bak3.setMaximumSize(QSize(100, 20))
        self.lineEdit_Bak3.setStyleSheet(u"color: rgb(85, 255, 127);")

        self.horizontalLayout_5.addWidget(self.lineEdit_Bak3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(widget_ship)

        QMetaObject.connectSlotsByName(widget_ship)
    # setupUi

    def retranslateUi(self, widget_ship):
        widget_ship.setWindowTitle(QCoreApplication.translate("widget_ship", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("widget_ship", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_boardtemperature.setText(QCoreApplication.translate("widget_ship", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.lineEdit_boardtemperature.setText(QCoreApplication.translate("widget_ship", u"22C", None))
        self.label_razgerm.setText(QCoreApplication.translate("widget_ship", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_razgerm.setText(QCoreApplication.translate("widget_ship", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_Bak1.setText(QCoreApplication.translate("widget_ship", u"\u0411\u0430\u043a \u2116 1", None))
        self.lineEdit_Bak1.setText(QCoreApplication.translate("widget_ship", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_Bak2.setText(QCoreApplication.translate("widget_ship", u"\u0411\u0430\u043a \u2116 2", None))
        self.lineEdit_Bak2.setText(QCoreApplication.translate("widget_ship", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_Bak3.setText(QCoreApplication.translate("widget_ship", u"\u0411\u0430\u043a \u2116 3", None))
        self.lineEdit_Bak3.setText(QCoreApplication.translate("widget_ship", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

