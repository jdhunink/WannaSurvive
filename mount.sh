#!/bin/bash

#Path to the drive to mount/unmount
backup_files="$1"
dest="$2"
echo "Started mount script"
umount /dev/disk3s3
if [ $? -eq 1 ]; then
    echo "Using diskutil"
    diskutil unmount /dev/disk3s3
fi

#Create a new mount directory, if it doesn't exist
mkdir -p ~/bu_mnt
echo "Made backup"

id1="$(diskutil list | grep -A 10 external | grep -o '/dev/.* (')"
id2="${id1#/dev/}"
id2="${id2% (}"
driveNames="$(diskutil list | grep -A 10 external | grep -o $id2's.*')"
mountDriveName=""

while read -r line; do
    mount -t hfs -o rw /dev/$line ~/bu_mnt
    if [ $? -eq 0 ]; then
        mountDriveName=$line
        chmod 777 ~/bu_mnt/
        echo "Succeeded mounting $mountDriveName"
        break
    fi
done <<< "$driveNames"

#Begin by mounting the drive from drive_path

newDest=~/bu_mnt

#Await signal from backup script or Python
#program that backup is done
source ./backup.sh

#Unmount drive after backup is complete
umount ~/bu_mnt
if [ $? -eq 1 ]; then
    echo "Using diskutil"
    diskutil unmount ~/bu_mnt
fi

echo "Unmounted drive at "
echo ~/bu_mnt