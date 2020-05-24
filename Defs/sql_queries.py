# Vanilla Python Modules

# Installed Modules
import sqlite3
import pyperclip
from PyQt5 import QtWidgets, QtGui, QtCore

# Local Modules
from Defs.crypto_defs import encrypt, decrypt

database = 'Database/Sample.db'

class SQL_QUERIES:

    ''' Handles all related to the sqlite database '''

    def __init__(self):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()


    def get_login_credentials(self, user, password):
        self.cursor.execute("SELECT username, password FROM login")
        self.creds = self.cursor.fetchall()[0]
        self.real_user = decrypt(self.creds[0], '')
        self.real_password = decrypt(self.creds[1], '')
        if self.real_user == user and self.real_password == password:
            return True
        else:
            return False


    def get_all(self, list):

        ''' Retrives all the Names on the database '''

        self.cursor.execute("SELECT Name FROM creds")
        self.creds = self.cursor.fetchall()

        for i in self.creds:
            list.addItem(i[0])


    def get_by_name(self, name, key):

        ''' Retrives the data of a specific Name on the database '''

        # Checks if the credentials exist
        self.cursor.execute(f"SELECT * FROM creds WHERE Name = '{name}'")
        self.creds = self.cursor.fetchall()[0]
        nombre, mail, password, link = self.creds[:]
        return nombre, decrypt(mail, key), decrypt(password, key), decrypt(link, key)

    def add_credentials(self, name, mail_user, password, link, key):

        ''' Adds a new record to the database '''

        try:
            self.cursor.execute(f"INSERT INTO creds (Name, Email_Username, Password, Link) VALUES ('{name}', '{encrypt(mail_user, key)}', '{encrypt(password, key)}', '{encrypt(link, key)}')")

        except Exception as e:
            return e

        else:
            self.conn.commit()
            return True



    def edit_credentials(self, name, edit_option, new_data, key):

        ''' Edits an specific part of the data on a specific Name '''

        try:

            if edit_option == 'Name':
                self.cursor.execute(f"UPDATE creds SET {edit_option} = '{new_data}' WHERE Name = '{name}'")

            else:
                self.cursor.execute(f"UPDATE creds SET {edit_option} = '{encrypt(new_data, key)}' WHERE Name = '{name}'")

        except Exception as e:
            print(e)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText('ocurrio un error')
            msg.setWindowTitle("Error!")
            msg.exec_()

        else:

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(f'{name} actualizado')
            msg.setWindowTitle("Actualizado!")
            msg.exec_()
            self.conn.commit()


    def delete_all(self):

        ''' Deletes every record on the database '''

        try:
            self.cursor.execute(f"DELETE * FROM creds")

        except Exception as e:
            print(f'AN ERROR OCURRED.\nERROR: {e}')

        finally:
            input('\nPRESS {ENTER} TO RETURN')


    def test():
        print('hola')
