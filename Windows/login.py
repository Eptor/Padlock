# Vanilla Modueles
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Imported Modules
from Defs.crypto_defs import *


class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(240, 167)
        self.setWindowIcon(QtGui.QIcon("Icons/key.png"))
        self.centralwidget = QtWidgets.QWidget(Login_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.User_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.User_Input.setGeometry(QtCore.QRect(10, 30, 221, 20))
        self.User_Input.setMouseTracking(True)
        self.User_Input.setTabletTracking(False)
        self.User_Input.setFrame(True)
        self.User_Input.setObjectName("User_Input")
        self.User_Label = QtWidgets.QLabel(self.centralwidget)
        self.User_Label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.User_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.User_Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.User_Label.setObjectName("User_Label")
        self.Password_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_Input.setGeometry(QtCore.QRect(10, 90, 220, 20))
        self.Password_Input.setMouseTracking(True)
        self.Password_Input.setTabletTracking(False)
        self.Password_Input.setText("")
        self.Password_Input.setFrame(True)
        self.Password_Input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_Input.setObjectName("Password_Input")
        self.Password_Label = QtWidgets.QLabel(self.centralwidget)
        self.Password_Label.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.Password_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Password_Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Password_Label.setObjectName("Password_Label")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(10, 130, 221, 23))
        self.Login_Button.setObjectName("Login_Button")
        Login_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Login"))
        self.User_Input.setPlaceholderText(_translate("Login_Window", "USER"))
        self.User_Label.setText(_translate("Login_Window", "User:"))
        self.Password_Input.setPlaceholderText(_translate("Login_Window", "PASSWORD"))
        self.Password_Label.setText(_translate("Login_Window", "Password:"))
        self.Login_Button.setText(_translate("Login_Window", "LOGIN"))
        self.Login_Button.setShortcut(_translate("Login_Window", "Return"))

    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(
            self, "Key", "Your Key:", QtWidgets.QLineEdit.Normal, ""
        )
        if okPressed and key != "":
            return key
