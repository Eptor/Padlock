from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edit_Selection(object):
    def setupUi(self, Edit_Selection):
        Edit_Selection.setObjectName("Edit_Selection")
        Edit_Selection.resize(319, 53)
        self.centralwidget = QtWidgets.QWidget(Edit_Selection)
        self.centralwidget.setObjectName("centralwidget")
        self.Name_Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Name_Radio.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.Name_Radio.setObjectName("Name_Radio")
        self.Mail_User_Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Mail_User_Radio.setGeometry(QtCore.QRect(80, 20, 91, 17))
        self.Mail_User_Radio.setObjectName("Mail_User_Radio")
        self.Password_Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Password_Radio.setGeometry(QtCore.QRect(180, 20, 82, 17))
        self.Password_Radio.setObjectName("Password_Radio")
        self.Link_Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Link_Radio.setGeometry(QtCore.QRect(270, 20, 82, 17))
        self.Link_Radio.setObjectName("Link_Radio")
        Edit_Selection.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edit_Selection)
        QtCore.QMetaObject.connectSlotsByName(Edit_Selection)

        self.Name_Radio.toggled.connect(self.edit_action)
        self.Mail_User_Radio.toggled.connect(self.edit_action)
        self.Password_Radio.toggled.connect(self.edit_action)
        self.Link_Radio.toggled.connect(self.edit_action)

    def retranslateUi(self, Edit_Selection):
        _translate = QtCore.QCoreApplication.translate
        Edit_Selection.setWindowTitle(_translate("Edit_Selection", "Edit Selection"))
        self.Name_Radio.setText(_translate("Edit_Selection", "Name"))
        self.Mail_User_Radio.setText(_translate("Edit_Selection", "Mail / User"))
        self.Password_Radio.setText(_translate("Edit_Selection", "Password"))
        self.Link_Radio.setText(_translate("Edit_Selection", "Link"))

    def get_edit(self):
        text, okPressed = QtWidgets.QInputDialog.getText(
            self, "Text", "New: ", QtWidgets.QLineEdit.Normal, ""
        )
        if okPressed and text != "":
            return text

    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(
            self, "Key", "Your Key:", QtWidgets.QLineEdit.Normal, ""
        )
        if okPressed and key != "":
            return key
