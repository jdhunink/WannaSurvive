#!/bin/bash

#Path to the drive to mount/unmount
drive_path = "$1"

#Begin by mounting the drive from drive_path
usr/bin/mount /drive_path /bu_mnt

#Await signal from backup script or Python
#program that backup is done
source backup_script.sh

#Unmount drive after backup is complete
usr/bin/umount /bu_mnt
