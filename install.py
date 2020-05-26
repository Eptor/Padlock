import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from Defs.crypto_defs import encrypt
import os


def install(login_gui, user, password, key):

    """ Hace toda la instalacion automatica """

    os.mkdir("Database")  # Crea el directorio
    connection = sqlite3.connect("Database/Padlock.db")  # Crea la coneccion con la base de datos
    cursor = connection.cursor()  # Crea el cursor sql

    # Funcion para crear la clase del login
    create_login_table = """CREATE TABLE `login` (
    `username`  TEXT,
    `password`  TEXT
    );"""

    # Funcion para crear tabla de credenciales
    create_creds_table = """CREATE TABLE `creds` (
    `Name`  TEXT,
    `Email_Username`    TEXT,
    `Password`  TEXT,
    `Link`  TEXT
    );"""

    try:
        # Crea la app pyqt
        cursor.execute(create_login_table)
        cursor.execute(create_creds_table)
        app = QtWidgets.QApplication([])
        app.setStyleSheet(open("style.css").read())
        login_gui.show()

        # Inserta las variables en la tabla login
        cursor.execute(
            f"INSERT INTO login (username, password) VALUES ('{encrypt(user, key)}', '{encrypt(password, key)}') "
        )
        connection.commit()

        # Popup de completado
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Base de datos completada!")
        msg.setWindowIcon(QtGui.QIcon("Icons/database.png"))
        msg.setWindowTitle("Instalacion completa")
        msg.exec_()
        app.exec_()

    except Exception as e:
        print(e)
