#!/bin/bash

#Path to the drive to mount/unmount
backup_files="$1"
dest="$2"
echo "Started mount script"

#Create a new mount directory, if it doesn't exist
mkdir -p ~/bu_mnt
echo "Made backup"

#Begin by mounting the drive from drive_path
mount -t auto /dest ~/bu_mnt

#Await signal from backup script or Python
#program that backup is done
source ./backup.sh

#Unmount drive after backup is complete
umount /bu_mnt/dest