# Padlock

Encrypted password mannager

## Pre requisitos

Necesitas los modulos cryptography sqlite3 y pyperclip.

```
pip install cryptography sqlite3 pyperclip -y
```

## Instalación

La instalacion es automatica, pero si deseas crear la base de datos tu mismo deberas crearla con el nombre "Padlock.db" en el directorio "Database" dentro de la
raiz del proyecto. La base de datos debera contener las siguientes tablas con sus respectivas filas.


### login:
username, password

### creds:
Name, Email_Username, Password, Link

**Todos de tipo texto.**

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

