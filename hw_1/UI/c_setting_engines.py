# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_setting_engines.ui'
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
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(510, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(510, 250))
        Form.setMaximumSize(QSize(900, 380))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSlider_16 = QSlider(self.groupBox)
        self.verticalSlider_16.setObjectName(u"verticalSlider_16")
        self.verticalSlider_16.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_16.addWidget(self.verticalSlider_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)


        self.horizontalLayout_2.addLayout(self.verticalLayout_16)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSlider_19 = QSlider(self.groupBox)
        self.verticalSlider_19.setObjectName(u"verticalSlider_19")
        self.verticalSlider_19.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_19.addWidget(self.verticalSlider_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_19.addWidget(self.label_19)


        self.horizontalLayout_2.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSlider_18 = QSlider(self.groupBox)
        self.verticalSlider_18.setObjectName(u"verticalSlider_18")
        self.verticalSlider_18.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_18.addWidget(self.verticalSlider_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_18.addWidget(self.label_18)


        self.horizontalLayout_2.addLayout(self.verticalLayout_18)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSlider_17 = QSlider(self.groupBox)
        self.verticalSlider_17.setObjectName(u"verticalSlider_17")
        self.verticalSlider_17.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_17.addWidget(self.verticalSlider_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_17.addWidget(self.label_17)


        self.horizontalLayout_2.addLayout(self.verticalLayout_17)

        self.horizontalSpacer = QSpacerItem(41, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSlider_20 = QSlider(self.groupBox)
        self.verticalSlider_20.setObjectName(u"verticalSlider_20")
        self.verticalSlider_20.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_20.addWidget(self.verticalSlider_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_20.addWidget(self.label_20)


        self.horizontalLayout_2.addLayout(self.verticalLayout_20)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 1", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 2", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 3", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 4", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

