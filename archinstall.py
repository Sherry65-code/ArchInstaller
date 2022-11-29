from sleeper import sleep, checkusername, checkForNet, run,checkForDisk
from os import system
from sys import exit
# Checking for internet
if checkForNet():
        print("Internet Avaliable")
else:
        system("clear")
        print("Internet Not Found")
        sleep()
        exit()
sleep()
system("clear")
print("Welcome to ArchInstaller by Hecker <Parambir Singh>")
sleep()
print("WARNING: This installer is only for UEFI !")
sleep()
# Checks if username has wrong character or not
while True:
        username = input("Type username to set in arch:")
        if (checkusername(username)):
                break
        else:
                system("clear")
                print("Wrong Username, Try correcting it!")
sleep()
system("clear")
while True:
        print("Select your disk for installation")
        run("fdisk -l | grep /dev/")
        diskname = input(">>").strip()
        if checkForDisk(diskname=diskname):
                print("Setting Disk...")
                sleep()
                break
        else:
                print("Wrong Disk name. Try again.")
        sleep()
        system("clear")
yon = input("Should I start partitioning (y or n):")
if (yon == "y"):
        system(f"(echo d; echo d; echo d; echo d; echo d; echo d; echo w;) | sudo fdisk /dev/{diskname}")
        system(f"(echo g; echo n; echo 1; echo; echo '+550M'; echo y; echo n; echo 2; echo ; echo +2G; echo y; echo n; echo 3; echo ; echo ; echo y; echo t; echo 1; echo 1; echo y; echo t; echo 2; echo 19; echo y; echo w;) | sudo fdisk /dev/{diskname}")
        system(f"mkfs.fat -F32 /dev/{diskname}1")
        system(f"mkswap /dev/{diskname}2")
        system(f"swapon /dev/{diskname}2")
        system(f"mkfs.ext4 /dev/{diskname}3")
else:
        print("Ok, Exiting Intallation Script...")
        sleep()
        exit()
system("clear")
print("Partition Over")
