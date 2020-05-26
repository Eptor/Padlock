from Windows.login import *
from Windows.menu import *
from Windows.data import *
from Windows.add import *
from Windows.edit_selection import *
from install import install

from Defs.sql_queries import *
import pyperclip
import os

critical_icon = "Icons/alert-triangle.png"


class login(QtWidgets.QMainWindow, Ui_Login_Window):

            """ Ventana del login """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.data = SQL_QUERIES()

        self.Login_Button.clicked.connect(self.Check)

    def Check(self):

        """ Verifica que las credenciales dadas sean las correctas """
        self.key = self.get_key()

        self.user = self.User_Input.text()
        self.password = self.Password_Input.text()
        if self.data.get_login_credentials(self.user, self.password, self.key):
            self.close()
            self.menu = menu()
            self.menu.show()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon(critical_icon))
            msg.setText("Contraseña incorrecta")
            msg.setWindowTitle("Contraseña incorrecta")
            msg.exec_()


class menu(QtWidgets.QMainWindow, Ui_Menu_Window):

            """ Ventana del menu """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.data = SQL_QUERIES()
        self.update()

        self.Search_Button.clicked.connect(self.search_by_name)
        self.Add_Button.clicked.connect(self.add_creds)
        self.Delete_Button.clicked.connect(self.delete_data)
        self.Edit_Button.clicked.connect(self.edit)
        self.Update_Button.clicked.connect(self.update)

    def edit(self):

        """ Editar credenciales """

        try:
            self.name = self.All_List.selectedIndexes()[0].data()  # Esta funcion es importante, de aqui se saca el valor de la seleccion en la lista
        except IndexError:  # Si no hay ninguna seleccionada no se hace nada
            pass
        else:
            self.edit_window = edit_data(self.name)
            self.edit_window.show()

    def update(self):

        """ Actualiza la lista de credenciales """

        self.All_List.clear()
        self.data.get_all(self.All_List)

    def search_by_name(self):

        """ Busca las credenciales con el nombre dado """

        try:
            self.name = self.All_List.selectedIndexes()[0].data()

        except IndexError:
            pass

        else:
            self.key = self.get_key()

            if not self.data.get_by_name(self.name, self.key):
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(critical_icon))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Llave incorrecta")
                msg.setWindowTitle("Llave incorrecta")
                msg.exec_()

            else:
                creds = self.data.get_by_name(self.name, self.key)
                self.show_data = see_data(creds)
                self.show_data.show()

    def delete_data(self):

        """ Borra las credenciales seleccionadas """

        self.name = self.name = self.All_List.selectedIndexes()[0].data()
        if self.get_confirmation():
            self.data.delete(self.name)
        else:
            pass

    def add_creds(self):

        """ Añade credenciales """

        self.add = add()
        self.add.show()

    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(
            self, "Llave", "Tu llave:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and key != "":
            return key

    def get_confirmation(self):
        ok, okPressed = QtWidgets.QInputDialog.getText(
            self, "Confirmacion", "SI o NO:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and ok.upper() == "SI":
            return True
        else:
            return False


class see_data(QtWidgets.QMainWindow, Ui_Data):

    """ Ventana donde se miran los datos de las credenciales seleccionadas """

    def __init__(self, creds, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icons/search.png"))

        for i in creds:
            self.Data_List.addItem(i)

    def copy(self):
        self.copy_data = self.Data_List.selectedIndexes()[0].data()
        pyperclip.copy(self.copy_data)


class add(QtWidgets.QMainWindow, Ui_ADD):

    """ Ventana para añadir las credenciales """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.data = SQL_QUERIES()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icons/pencil-create.png"))


class edit_data(QtWidgets.QMainWindow, Ui_Edit_Selection):

    """ Ventana para editar las credenciales seleccionadas """

    def __init__(self, name, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.data = SQL_QUERIES()
        self.name = name
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("Icons/pencil-edit.png"))

    def edit_action(self):
        new_text = self.get_edit()
        key = self.get_key()
        selection = self.sender()
        if selection.text() == "Nombre":
            self.data.edit_credentials(self.name, "Name", new_text, key)
        elif selection.text() == "Mail / Usuario":
            self.data.edit_credentials(self.name, "Email_Username", new_text, key)
        elif selection.text() == "Contraseña":
            self.data.edit_credentials(self.name, "Password", new_text, key)
        elif selection.text() == "Link":
            self.data.edit_credentials(self.name, "Link", new_text, key)

        self.close()


class install_functions(QtWidgets.QMainWindow):

    """ Funciones necesarias para obtener los datos necesarios
        para la instalacion, tales como el usuario, la contraseña
        y la llave """

    def get_key(self):
        key, okPressed = QtWidgets.QInputDialog.getText(
            self, "Llave", "Tu llave:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and key != "":
            return key

    def get_user(self):
        text, okPressed = QtWidgets.QInputDialog.getText(
            self, "Usuario", "Tu usuario:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and text != "":
            return text

    def get_password(self):
        text, okPressed = QtWidgets.QInputDialog.getText(
            self, "Contraseña", "Tu contraseña:", QtWidgets.QLineEdit.Normal, ""
        )

        if okPressed and text != "":
            return text


# si la instalacion existe
if __name__ == "__main__" and os.path.exists("Database/Padlock.db"):
    app = QtWidgets.QApplication([])
    app.setStyleSheet(open("style.css").read())
    login_gui = login()
    login_gui.show()
    app.exec_()

# si la instalacion no existe
elif __name__ == "__main__" and not os.path.exists("Database/Padlock.db"):
    try:
        app = QtWidgets.QApplication([])
        app.setStyleSheet(open("style.css").read())
        login_gui = login()
        login_gui.show()

        install_texts = all_functions()
        # Asks for Key
        key = install_texts.get_key()

        # Asks for user and password
        user = install_texts.get_user()
        password = install_texts.get_password()

        install(login_gui, user, password, key)

    except Exception as e:
        print(e)
