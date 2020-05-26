from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Data(object):
    def setupUi(self, Data):
        Data.setObjectName("Data")
        Data.resize(301, 190)
        self.Data_List = QtWidgets.QListWidget(Data)
        self.Data_List.setGeometry(QtCore.QRect(10, 10, 281, 141))
        self.Data_List.setObjectName("Data_List")
        self.Copy_Button = QtWidgets.QPushButton(Data)
        self.Copy_Button.setGeometry(QtCore.QRect(70, 160, 75, 23))
        self.Copy_Button.setObjectName("Copy_Button")
        self.Close_Button = QtWidgets.QPushButton(Data)
        self.Close_Button.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.Close_Button.setObjectName("Close_Button")

        self.retranslateUi(Data)
        QtCore.QMetaObject.connectSlotsByName(Data)

        self.Close_Button.clicked.connect(self.close)
        self.Copy_Button.clicked.connect(self.copy)

    def retranslateUi(self, Data):
        _translate = QtCore.QCoreApplication.translate
        Data.setWindowTitle(_translate("Data", "Data"))
        self.Copy_Button.setText(_translate("Data", "COPIAR"))
        self.Close_Button.setText(_translate("Data", "CERRAR"))
