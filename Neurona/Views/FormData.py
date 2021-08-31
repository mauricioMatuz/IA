# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormData.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(537, 300)
        self.pushButtonValor = QPushButton(Form)
        self.pushButtonValor.setObjectName(u"pushButtonValor")
        self.pushButtonValor.setGeometry(QRect(230, 190, 75, 23))
        self.lineEditErro1 = QLineEdit(Form)
        self.lineEditErro1.setObjectName(u"lineEditErro1")
        self.lineEditErro1.setGeometry(QRect(280, 21, 111, 16))
        self.lineEditErro2 = QLineEdit(Form)
        self.lineEditErro2.setObjectName(u"lineEditErro2")
        self.lineEditErro2.setGeometry(QRect(280, 61, 111, 16))
        self.lineEditErro3 = QLineEdit(Form)
        self.lineEditErro3.setObjectName(u"lineEditErro3")
        self.lineEditErro3.setGeometry(QRect(280, 101, 111, 16))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 211, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 60, 211, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 100, 211, 16))
        self.lineEditLambda = QLineEdit(Form)
        self.lineEditLambda.setObjectName(u"lineEditLambda")
        self.lineEditLambda.setGeometry(QRect(280, 141, 111, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 140, 211, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonValor.setText(QCoreApplication.translate("Form", u"ENVIAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">INGRESE EL VALOR DEL ERROR 1:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">INGRESE EL VALOR DEL ERROR 2:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">INGRESE EL VALOR DEL ERROR 3:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">INGRESE EL VALOR DE lambda :</span></p></body></html>", None))
    # retranslateUi

