from file import *
from hashlib import sha256
from getpass import getpass
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

HASH_FILENAME = 'hash.hash'

def createKey(passwordA):
    password_provided = passwordA
    password = password_provided.encode()
    salt = passwordA[::-1].encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(password))

def createPassword():
    correct = False
    file = createFile(HASH_FILENAME)
    while not correct:
        password = getpass('Crea una nueva la contraseña: ')
        passwordConf = getpass('confirma la contraseña: ')
        if(password == passwordConf):
            correct = True
        file.write(sha256(password.encode('utf-8')).hexdigest().encode())
        file.close()
        return createKey(password)

def auth():
    state = False
    file = openFile(HASH_FILENAME)
    if(file == False):
        passlen = 0
    else:
        passw = file.readline()
        passlen = len(passw)
        file.close()
    if(passlen <= 0):
        state = createPassword()
    else:
        password = getpass('Ingrese la contraseña: ')
        if(sha256(password.encode('utf-8')).hexdigest() == passw.decode()):
            state = createKey(password)
        else:
            state = False
    return state