#!/usr/bin/env python
from auth import auth
from file import *
from cryptography.fernet import Fernet
from constants import OPTIONS, COMMANDS
import os
import time

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def createSecretFile(key):
    name = input("Nombre: ")
    if(name == COMMANDS.BACK):
        return
    fullPath = "files/" + name
    if(fileExists(fullPath)):
        print("El archivo ya existe")
    else:
        clearScreen()
        file = createFile(fullPath)
        print("Ingresa el contenido ('{0}' para finalizar):".format(COMMANDS.END))
        line = lines = ""
        while(line != COMMANDS.END.__str__()):
            if line != "":
                if len(lines) <= 0:
                    lines += line
                else:
                    lines += "\n" + line
            line = input()
        f = Fernet(key)
        file.write(f.encrypt(lines.encode()).decode())
        file.close()

def openSecretFile(key):
    files = fileList()
    for i, file in enumerate(files):
        if(file != ".gitignore"):
            print("{0}->{1}".format(i, file))
    print("")
    name = input("Nombre: ")
    if(name == COMMANDS.BACK):
        return
    try:
        position = int(name)
    except ValueError as err:
        position = 0
    if(position >= 1 and position < len(files)):
        name = files[position]
    fullPath = "files/" + name
    file = openFile(fullPath)
    clearScreen()
    if(file == False):
        print("No se pudo abrir el archivo")
    else:
        f = Fernet(key)
        text = f.decrypt(file.read().encode())
        print("-------.-------")
        print("{0}".format(name))
        print("-----start-----")
        print("")
        print(text.decode())
        print("")
        print("------end------")
        print("")
        print("")
        file.close()

def menu(key):
    op = 0
    run = True
    while(run):
        ok = True
        print("{0}. Crear archivo".format(OPTIONS.CREATE))
        print("{0}. Leer archivo".format(OPTIONS.READ))
        try:
            op = input("Elija una opción: ")
        except ValueError:
            print("Debe seleccionar un número")
            ok = False
        if(op == COMMANDS.EXIT.__str__() or op == COMMANDS.BACK.__str__()):
            run = False
            ok = False
        if(ok):
            if(int(op) == OPTIONS.CREATE):
                createSecretFile(key)
            elif(int(op) == OPTIONS.READ):
                openSecretFile(key)

def main():
    key = auth()
    if(key):
        menu(key)
    else:
        print("No se pudo comprobar su identidad")

if __name__ == "__main__":
   main()