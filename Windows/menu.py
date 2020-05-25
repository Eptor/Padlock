from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_Window(object):
    def setupUi(self, Menu_Window):
        Menu_Window.setObjectName("Menu_Window")
        Menu_Window.resize(442, 171)
        self.setWindowIcon(QtGui.QIcon('Icons/lock.png'))
        self.centralwidget = QtWidgets.QWidget(Menu_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(200, 10, 221, 23))
        self.Search_Button.setObjectName("Search_Button")
        self.Add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Button.setGeometry(QtCore.QRect(200, 40, 221, 23))
        self.Add_Button.setObjectName("Add_Button")
        self.Edit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Edit_Button.setGeometry(QtCore.QRect(200, 70, 221, 23))
        self.Edit_Button.setObjectName("Edit_Button")
        self.Delete_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_Button.setGeometry(QtCore.QRect(200, 100, 221, 23))
        self.Delete_Button.setObjectName("Delete_Button")
        self.All_List = QtWidgets.QListWidget(self.centralwidget)
        self.All_List.setGeometry(QtCore.QRect(10, 10, 161, 151))
        self.All_List.setObjectName("listWidget")
        self.Update_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Update_Button.setGeometry(QtCore.QRect(200, 130, 221, 23))
        self.Update_Button.setObjectName("Update_Button")
        Menu_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_Window)
        QtCore.QMetaObject.connectSlotsByName(Menu_Window)

    def retranslateUi(self, Menu_Window):
        _translate = QtCore.QCoreApplication.translate
        Menu_Window.setWindowTitle(_translate("Menu_Window", "Menu"))
        self.Search_Button.setText(_translate("Menu_Window", "BUSCAR"))
        self.Add_Button.setText(_translate("Menu_Window", "AÑADIR"))
        self.Edit_Button.setText(_translate("Menu_Window", "EDITAR"))
        self.Delete_Button.setText(_translate("Menu_Window", "BORRAR"))
        self.Update_Button.setText(_translate("Menu_Window", "ACTUALIZAR LISTA"))
