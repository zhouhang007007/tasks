# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_clinet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 160, 541, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_Mesage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Mesage.setGeometry(QtCore.QRect(10, 460, 541, 31))
        self.lineEdit_Mesage.setObjectName("lineEdit_Mesage")
        self.PushButton_Send = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Send.setGeometry(QtCore.QRect(10, 500, 541, 41))
        self.PushButton_Send.setObjectName("PushButton_Send")
        self.PushButton_Upadte = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Upadte.setGeometry(QtCore.QRect(350, 110, 201, 41))
        self.PushButton_Upadte.setObjectName("PushButton_Upadte")
        self.lineEdit_NPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_NPassword.setGeometry(QtCore.QRect(140, 110, 201, 41))
        self.lineEdit_NPassword.setObjectName("lineEdit_NPassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 61, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 109, 121, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setGeometry(QtCore.QRect(80, 60, 171, 41))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(260, 60, 171, 41))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.PushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Login.setGeometry(QtCore.QRect(440, 60, 111, 41))
        self.PushButton_Login.setObjectName("PushButton_Login")
        self.textBrowser_Pinroom = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Pinroom.setGeometry(QtCore.QRect(10, 10, 541, 41))
        self.textBrowser_Pinroom.setObjectName("textBrowser_Pinroom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PushButton_Send.setText(_translate("MainWindow", "Send"))
        self.PushButton_Upadte.setText(_translate("MainWindow", "update password"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.label_2.setText(_translate("MainWindow", "change password"))
        self.PushButton_Login.setText(_translate("MainWindow", "Login"))

