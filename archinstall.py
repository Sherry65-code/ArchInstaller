from os import system
from time import sleep


system("clear")
print("WELCOME TO ARCH INSTALLER BY HECKER")
sleep(1)
print("Which Desktop Enviroment to Install?")
de = input(">>")
print("Updating system...")
sleep(1)
system("sudo pacman -Sy &> /dev/null")
print("Done")
sleep(1)
print("Now Partitioning...")
sleep(1)
system("clear")
print("Choose a disk from the following for installing Arch")
system("ls /dev/sd*")
diskname = input(">>")
if ("dev" in diskname):
        diskname = diskname.replace("dev/", "").replace(" ","")
system(f"(echo g; echo n; echo 1; echo; echo '+550M'; echo n; echo 2; echo ;echo '+2G';echo n;echo 3;echo ;echo ;echo t;echo 1;echo 1;echo t;echo 2;echo 19;echo w;) | fdisk /dev/{diskname}")
system(f"mkfs.fat -F32 /dev/{diskname}1")
system(f"mkswap /dev/{diskname}2")
system(f"swapon /dev/{diskname}2")
system(f"mkfs.ext4 /dev/{diskname}3")
system("clear")
print("Partion Over")
sleep(1)
print("Now Installing base system")
sleep(1)
system(f"mount /dev/{diskname}3 /mnt")
system("pacstrap /mnt base base-devel linux-lts linux-firmware linux-lts-headers")
system("genfstab -U /mnt >> /mnt/etc/fstab")
system("cp -r ./chroot.py /mnt")
system("(echo 'python3 chroot.py') | arch-chroot /mnt")
system("umount -l /mnt")
system("clear")
print("Installed, Now Rebooting")
sleep(2)
system("reboot")
