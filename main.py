from Windows.login import *
from Windows.menu import *
from Windows.data import *
from Windows.add import *
from Windows.edit_selection import *

from Defs.sql_queries import SQL_QUERIES
import pyperclip


class login(QtWidgets.QMainWindow, Ui_Login_Window):

    ''' Creates the window with the given template '''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.data = SQL_QUERIES()

        self.Login_Button.clicked.connect(self.Check)


    def Check(self):

        ''' Verificates if the given credentials are correct '''

        self.user = self.User_Input.text()
        self.password = self.Password_Input.text()
        if self.data.get_login_credentials(self.user, self.password):
            self.close()
            self.menu = menu()
            self.menu.show()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Contraseña incorrecta")
            msg.setWindowTitle("Contraseña incorrecta")
            msg.exec_()


class menu(QtWidgets.QMainWindow, Ui_Menu_Window):

    ''' Creates the window with the given template '''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.data = SQL_QUERIES()
        self.update()

        self.Search_Button.clicked.connect(self.search_by_name)
        self.Add_Button.clicked.connect(self.add_creds)
        # self.Delete_Button.clicked.connect(self.delete_data)
        self.Edit_Button.clicked.connect(self.edit)
        self.Update_Button.clicked.connect(self.update)


    def edit(self):
        try:
            self.name = self.All_List.selectedIndexes()[0].data()
        except IndexError:
            pass
        else:
            self.edit_window = edit_data(self.name)
            self.edit_window.show()


    def update(self):
        self.All_List.clear()
        self.data.get_all(self.All_List)


    def search_by_name(self):
        try:
            name = self.All_List.selectedIndexes()[0].data()

        except IndexError:
            pass

        else:
            key = self.get_key()
            creds = self.data.get_by_name(name, key)

            try:
                self.show_data = see_data(creds)

            except InvalidToken:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Key incorrecta")
                msg.setWindowTitle("Key incorrecta")
                msg.exec_()

            self.show_data.show()


    def add_creds(self):
        self.add = add()
        self.add.show()


    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(self, "Key","Your Key:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and key != '':
            return key


class see_data(QtWidgets.QMainWindow, Ui_Data):

    ''' Creates the window with the given template '''

    def __init__(self, creds, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        for i in creds:
            self.Data_List.addItem(i)


    def copy(self):
        self.copy_data = self.Data_List.selectedIndexes()[0].data()
        pyperclip.copy(self.copy_data)


class add(QtWidgets.QMainWindow, Ui_ADD):

    ''' Creates the window with the given template '''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.data = SQL_QUERIES()
        self.setupUi(self)


class edit_data(QtWidgets.QMainWindow, Ui_Edit_Selection):

    ''' Creates the window with the given template '''

    def __init__(self, name , *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.data = SQL_QUERIES()
        self.name = name
        self.setupUi(self)


    def edit_action(self):
        new_text = self.get_edit()
        key = self.get_key()
        selection = self.sender()
        if selection.text() == 'Nombre':
            self.data.edit_credentials(self.name, 'Name', new_text, key)
        elif selection.text() == 'Mail / Usuario':
            self.data.edit_credentials(self.name, 'Email_Username', new_text, key)
        elif selection.text() == 'Contraseña':
            self.data.edit_credentials(self.name, 'Password', new_text, key)
        elif selection.text() == 'Link':
            self.data.edit_credentials(self.name, 'Link', new_text, key)

        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet(open('style.css').read())
    login_gui = login()
    login_gui.show()
    app.exec_()
