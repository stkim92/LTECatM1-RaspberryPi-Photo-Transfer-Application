# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os
from PIL import Image

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        im = Image.open('test.jpg') # Image Open & Resize
        size = (500,500)
        im.thumbnail(size)
        im.save('test.jpg')         # added by tom
        
        
        Dialog.setObjectName(_fromUtf8("LTE Cat.M1 Picture Receiver"))
        Dialog.resize(566, 464)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(60, 50, 301, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(400, 37, 141, 52))
        self.pushButton.setObjectName(_fromUtf8("Server Open"))


        self.label = QtGui.QLabel(Dialog)                           # Label Image
        self.label.setGeometry(QtCore.QRect(70, 140, 431, 281))     #
        self.label.setPixmap(QPixmap("test.jpg"))                   # aaded by tom

        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 361, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 100, 511, 351))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LTE Cat.M1 Picture Receiver", None))
        self.pushButton.setText(_translate("Dialog", "Server Open", None))
        self.groupBox.setTitle(_translate("Dialog", "Status", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Picture Preview", None))
  
