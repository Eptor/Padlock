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

## Uso

Al iniciar el programa por primera vez, se instalará la base de datos, te pedirá tu usuario y tu contraseña para iniciar sesion, al igual que la llave
para desencriptar tus credenciales de login.

luego se abrirá el menu, en el cual podras buscar, agregar, editar y eliminar credenciales de tus sitios web o aplicaciones favoritas.

### Buscar, añadir y editar credenciales

Cuando hagas cualqueira de estas acciones, se te pedira una llave con la cual se encriptarán esas credenciales, al editar alguna parte asegurate de usar
la misma llave con la que la creaste para evitar errores.
