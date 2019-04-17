#!/bin/bash

#Path to the drive to mount/unmount
backup_files = "$1"
dest="$2"

#Create a new mount directory, if it doesn't exist
mkdir -p ~/bu_mnt

#Begin by mounting the drive from drive_path
usr/bin/mount /dest ~/bu_mnt

#Await signal from backup script or Python
#program that backup is done
source backup_script.sh

#Unmount drive after backup is complete
usr/bin/umount /bu_mnt/dest