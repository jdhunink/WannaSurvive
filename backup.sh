#!/bin/sh
#What files or folders to backup (should this be passed in?)
#This should be passed in from the users selection in the gui
# backup_files="$1" 
# dest="$2"
#create backup directory if it does not already exist
#This should be probably be configured by th user and passed in
mkdir -p $dest/backups
#set destination of backup to created directory.

echo $dest
#create archive filename
day=$(date +%Y-%m-%d-%T)
hostname=$(hostname -s)
archive_file="$hostname-$day.tar.gz"
echo "$1"
echo "$2"
#print start message
echo "Backing up $backup_files to $dest/backups/$archive_file"

#backup files
tar czf $dest/backups/$archive_file $backup_files

#print end message
echo "Backup complete"