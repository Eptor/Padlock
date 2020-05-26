from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ADD(object):
    def setupUi(self, ADD):
        ADD.setObjectName("ADD")
        ADD.resize(133, 192)
        self.Name_Input = QtWidgets.QLineEdit(ADD)
        self.Name_Input.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.Name_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Input.setObjectName("Name_Input")
        self.Mail_Input = QtWidgets.QLineEdit(ADD)
        self.Mail_Input.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.Mail_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Mail_Input.setObjectName("Mail_Input")
        self.Password_Input = QtWidgets.QLineEdit(ADD)
        self.Password_Input.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.Password_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_Input.setObjectName("Password_Input")
        self.Link_Input = QtWidgets.QLineEdit(ADD)
        self.Link_Input.setGeometry(QtCore.QRect(10, 100, 113, 20))
        self.Link_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Link_Input.setObjectName("Link_Input")
        self.Add_Action_Button = QtWidgets.QPushButton(ADD)
        self.Add_Action_Button.setGeometry(QtCore.QRect(24, 130, 81, 23))
        self.Add_Action_Button.setObjectName("Add_Action_Button")
        self.Cancel_Button = QtWidgets.QPushButton(ADD)
        self.Cancel_Button.setGeometry(QtCore.QRect(24, 160, 81, 23))
        self.Cancel_Button.setObjectName("Cancel_Button")

        self.retranslateUi(ADD)
        QtCore.QMetaObject.connectSlotsByName(ADD)

        # Connection
        self.Cancel_Button.clicked.connect(self.close)
        self.Add_Action_Button.clicked.connect(self.add_credentials)

    def retranslateUi(self, ADD):
        _translate = QtCore.QCoreApplication.translate
        ADD.setWindowTitle(_translate("ADD", "ADD"))
        self.Name_Input.setPlaceholderText(_translate("ADD", "Nombre"))
        self.Mail_Input.setPlaceholderText(_translate("ADD", "Email/Usuario"))
        self.Password_Input.setPlaceholderText(_translate("ADD", "Contraseña"))
        self.Link_Input.setPlaceholderText(_translate("ADD", "Link"))
        self.Add_Action_Button.setText(_translate("ADD", "AÑADIR"))
        self.Cancel_Button.setText(_translate("ADD", "CANCELAR"))

    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(
            self, "Key", "Your Key:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and key != "":
            return key

    def add_credentials(self, key):

        """ Adds a new record to the database """
        key = self.get_key()
        self.name = self.Name_Input.text()
        self.mail_user = self.Mail_Input.text()
        self.password = self.Password_Input.text()
        self.link = self.Link_Input.text()
        if self.data.add_credentials(
            self.name, self.mail_user, self.password, self.link, key
        ):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(f"{self.name} agregado con exito!")
            msg.setWindowTitle("Completado")
            msg.exec_()
            self.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(f"{self.name} no se pudo agregar")
            msg, informativeText(e)
            msg.setWindowTitle("Error")
            msg.exec_()
            self.close()
