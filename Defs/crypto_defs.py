import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The base process was grabbed from the Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(data, password):
    """ Encrypts the data given by the user """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"g\xe0\\F\x90\x15Dr\x1e-\xa8u\xd9Y\x0c\x82",
        iterations=100000,
        backend=default_backend(),
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    EncryptedToken = f.encrypt(data.encode())
    return EncryptedToken.decode()


def decrypt(data, password):
    """ Decrypts the data given by the user """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"g\xe0\\F\x90\x15Dr\x1e-\xa8u\xd9Y\x0c\x82",
        iterations=100000,
        backend=default_backend(),
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    DecryptedToken = f.decrypt(data.encode())
    return DecryptedToken.decode()
