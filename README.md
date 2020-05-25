# Padlock

Encrypted password mannager

## Pre requisitos

Necesitas los modulos cryptography sqlite3 y pyperclip.

```
pip install cryptography sqlite3 pyperclip -y
```

## Instalación

En el GUI viene automatizado, pero si quieres hacerlo manualmente deberas crear una base de datos sqlite (con el nombre que desees)
con las tablas "login" y "creds", ambas con las siguientes filas:


### login:
username, password

### creds:
Name, Email_Username, Password, Link

Todos de tipo texto.

Puedes usar estos comandos:

```
CREATE TABLE 'creds' (
    'Name'  TEXT,
    'Email_Username'    TEXT,
    'Password'  TEXT,
    'Link'  TEXT
);
```

```
CREATE TABLE 'login' (
    'username'  TEXT,
    'password'  TEXT
);
```

