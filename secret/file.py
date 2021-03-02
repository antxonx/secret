from os import path, listdir

def openFile(name):
    fullPath = path.dirname(path.abspath(__file__))
    try:
        file = open(fullPath + '/' + name, 'r')
        return file
    except OSError as err:
        return False

def createFile(name):
    fullPath = path.dirname(path.abspath(__file__))
    try:
        file = open(fullPath + '/' + name, 'w+')
        return file
    except OSError as err:
        return False

def fileExists(name):
    fullPath = path.dirname(path.abspath(__file__))
    return path.exists(fullPath + '/' + name)

def fileList():
    fullPath = path.dirname(path.abspath(__file__))
    return listdir(fullPath + '/files')