# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainFrom(object):
    def setupUi(self, MainFrom):
        if not MainFrom.objectName():
            MainFrom.setObjectName(u"MainFrom")
        MainFrom.resize(647, 390)
        self.frame = QFrame(MainFrom)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 50, 241, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEditX1 = QLineEdit(self.frame)
        self.lineEditX1.setObjectName(u"lineEditX1")
        self.lineEditX1.setGeometry(QRect(80, 20, 151, 20))
        self.lineEditX2 = QLineEdit(self.frame)
        self.lineEditX2.setObjectName(u"lineEditX2")
        self.lineEditX2.setGeometry(QRect(80, 50, 151, 20))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 61, 20))
        self.frame_2 = QFrame(MainFrom)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(390, 50, 241, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEditY1 = QLineEdit(self.frame_2)
        self.lineEditY1.setObjectName(u"lineEditY1")
        self.lineEditY1.setGeometry(QRect(80, 20, 151, 20))
        self.lineEditY2 = QLineEdit(self.frame_2)
        self.lineEditY2.setObjectName(u"lineEditY2")
        self.lineEditY2.setGeometry(QRect(80, 50, 151, 20))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 61, 20))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 61, 20))
        self.lineEditError = QLineEdit(MainFrom)
        self.lineEditError.setObjectName(u"lineEditError")
        self.lineEditError.setGeometry(QRect(130, 150, 113, 20))
        self.pushButtonEnviar = QPushButton(MainFrom)
        self.pushButtonEnviar.setObjectName(u"pushButtonEnviar")
        self.pushButtonEnviar.setGeometry(QRect(310, 230, 75, 23))

        self.retranslateUi(MainFrom)

        QMetaObject.connectSlotsByName(MainFrom)
    # setupUi

    def retranslateUi(self, MainFrom):
        MainFrom.setWindowTitle(QCoreApplication.translate("MainFrom", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainFrom", u"Intervalo x1", None))
        self.label_2.setText(QCoreApplication.translate("MainFrom", u"Intervalo x2", None))
        self.label_5.setText(QCoreApplication.translate("MainFrom", u"Intervalo y1", None))
        self.label_6.setText(QCoreApplication.translate("MainFrom", u"Intervalo y2", None))
        self.lineEditError.setText("")
        self.pushButtonEnviar.setText(QCoreApplication.translate("MainFrom", u"PushButton", None))
    # retranslateUi

