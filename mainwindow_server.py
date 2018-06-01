# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_server.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 461, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.PushButton_Send = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Send.setGeometry(QtCore.QRect(10, 500, 461, 41))
        self.PushButton_Send.setObjectName("PushButton_Send")
        self.PushButton_Upadte = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_Upadte.setGeometry(QtCore.QRect(10, 40, 461, 31))
        self.PushButton_Upadte.setObjectName("PushButton_Upadte")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label.setObjectName("label")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setGeometry(QtCore.QRect(80, 10, 171, 21))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(310, 10, 161, 21))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 51, 21))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 120, 73, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 150, 73, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 180, 73, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 210, 73, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 240, 73, 21))
        self.checkBox_6.setObjectName("checkBox_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
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
        self.PushButton_Send.setText(_translate("MainWindow", "Del"))
        self.PushButton_Upadte.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.checkBox.setText(_translate("MainWindow", "A"))
        self.checkBox_2.setText(_translate("MainWindow", "B"))
        self.checkBox_3.setText(_translate("MainWindow", "C"))
        self.checkBox_4.setText(_translate("MainWindow", "D"))
        self.checkBox_5.setText(_translate("MainWindow", "E"))
        self.checkBox_6.setText(_translate("MainWindow", "F"))

