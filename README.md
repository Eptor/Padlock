# Padlock

Administrador de contraseñas cifradas. Sus contraseñas están seguras gracias al cifrado basado en claves; cuando agrega credenciales, el script
pedirle una clave para cifrar los datos, y es con esa misma clave que puede verlos, por lo que cuando desee buscar credenciales X,
el script le pedirá una clave y con esa clave descifrará los datos cifrados.

## pre requisitos

Necesitas los modulos cryptography, sqlite3 y pyperclip.

`` `
pip install cryptography sqlite3 pyperclip -y
`` `

## Instalación


La instalación es automática, genera el directorio "Base de datos" y agrega el archivo Padlock.db con las filas requeridas. Pero si prefieres crear tu
propia base de datos en lugar de hacerlo automáticamente, puede usar los siguientes comandos sqlite

Esta es la estructura de la base de datos:

### login:
username, password

### creds:
Name, Email_Username, Password, Link

**Todos de tipo texto.**

### Comandos:

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

Al iniciar el programa por primera vez, se instalará la base de datos, se le pedirá su nombre de usuario y contraseña para iniciar sesión, como
así como la clave para descifrar sus credenciales de inicio de sesión.

luego se abre el menú, en el que puede buscar, agregar, editar y eliminar credenciales de sus sitios web o aplicaciones favoritas.

### Buscar, agregar y editar credenciales

Cuando realice alguna de estas acciones, se le pedirá una clave con la que se cifrarán estas credenciales,
Al editar cualquier parte, asegúrese de utilizar la misma clave con la que la creó para evitar errores.
