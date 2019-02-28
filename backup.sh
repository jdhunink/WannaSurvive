
#What files or folders to backup (should this be passed in?)
#This should be passed in from the users selection in the gui
backup_files="" 

#create backup directory if it does not already exist
#This should be probably be configured by th user and passed in
mkdir -p backups
#set destination of backup to created directory.
dest="backups"

#create archive filename
day=$(date +%Y-%m-%d-%T)
hostname=$(hostname -s)
archive_file="$hostname-$day.tar.gz"

#print start message
echo "Backing up $backup_files to $dest/$archive_file"

#backup files
tar czf $dest/$archive_file $backup_files

#print end message
echo "Backup complete"