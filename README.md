# Padlock

Encrypted password mannager. Your passwords are safe thanks to the key based encryption; when you add credentials, the script will
ask you for a key to encrypt the data, and it is whit that same key that you can see them, so when you want to search X credentials,
the script will ask you for a key, and with that key it will decrypt the encrypted data.

## pre requirements

You need the cryptography, sqlite3 and pyperclip modules.

```
pip install cryptography sqlite3 pyperclip -y
```

## Installation


The installation is automatic, it generates the directory "Database" and adds the Padlock.db file with the requiered rows. But if you rather create your
own database instead of doing it automatically, you can using the following sqlite commands

This is the database structure:

### login:
username, password

### creds:
Name, Email_Username, Password, Link

**All text type.**

### Commands:

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

## Use

When starting the program for the first time, the database will be installed, it will ask for your username and password to log in, as
well as the key to decrypt your login credentials.

then the menu opens, in which you can search, add, edit and delete credentials from your favorite websites or applications.

### Search, add and edit credentials

When you do any of these actions, you will be asked for a key with which these credentials will be encrypted,
when editing any part make sure to use the same key with which you created it to avoid errors.
