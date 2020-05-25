import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from Defs.crypto_defs import encrypt
import os


def install(login_gui, user, password, key):
    os.mkdir('Database')
    connection = sqlite3.connect('Database/Padlock.db')
    cursor = connection.cursor()

    create_login_table = """CREATE TABLE `login` (
    `username`  TEXT,
    `password`  TEXT
    );"""

    create_creds_table = """CREATE TABLE `creds` (
    `Name`  TEXT,
    `Email_Username`    TEXT,
    `Password`  TEXT,
    `Link`  TEXT
    );"""

    try:
        # Creates app
        cursor.execute(create_login_table)
        cursor.execute(create_creds_table)
        app = QtWidgets.QApplication([])
        app.setStyleSheet(open('style.css').read())
        login_gui.show()



        # Inserts login credentials
        cursor.execute(f"INSERT INTO login (username, password) VALUES ('{encrypt(user, key)}', '{encrypt(password, key)}') ")
        connection.commit()

        # Complete
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Base de datos creada!')
        msg.setWindowIcon(QtGui.QIcon('Icons/database.png'))
        msg.setWindowTitle("Instalacion completa")
        msg.exec_()
        app.exec_()


    except Exception as e:
        print(e)

