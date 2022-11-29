from time import time
from os import remove, system

def sleep(timetosleep=1):
    s = time()
    while s+timetosleep > time():
        pass

def checkusername(username):
    if (any(map(str.isupper, username))):
        return False
    else:
        return True
    
def checkForNet():
    try:
        remove("check.txt")
    except Exception as e:
        pass
    system("ping -c 1 google.com > check.txt")
    if (open("check.txt","r").read() == ""):
        return False
    else:
        return True

def run(what):
        system(f"sudo {what}")

def checkForDisk(diskname):
    try:
        remove("check.txt")
    except Exception as e:
        pass
    system("ls /dev/ > check.txt")
    if (diskname in open("check.txt","r").read()):
        return True
    else:
        return False
