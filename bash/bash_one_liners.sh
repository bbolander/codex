#
#   bash_one_liners.sh
#

#   To compare strings use "$s1" = "$s2" and >, <, >=, <=, !=
#   To compare numbers use $n1 -eq $n2 and -lt, -gt, -ne


#   Change all the filenames in a directory tree that start with a capital letter
#   to a lowercase letter.
#
for file in `find testdir -type f`; do echo $file; new_f_name=`echo $file | sed 's/\(.*\/\)\(.\)\(.*\)$/\1\L\2\E\3/'`; echo $new_f_name; mv $file $new_f_name; done

#   Monitor processes in a loop from the command line.
#
while true; do echo -en "\n\n-- TIME: ";date; ps -aef | grep -v grep | egrep "(supervisor|vidder-server-agent|tomcat7)"; sleep 5; done


#   Search a subnet for your machine after DHCP has changed the address on 
#   you. 
#
for i in {1..256}; do ssh -o ConnectTimeout=1 10.10.201.$i -i ~/.ssh/bbolander.private.rsa; done

#   Removes all core dump files from user's home directory.
#
find ~/ -name 'core*' -exec rm {} \;

#   Start multiple jobs to run in parallel in the background.
#
for i in {1..8}; do nohup ~/installers/athena-db/DeleteBackUpsFiles.sh /ngs${i}/app/aidep/data/disk/features/aggregate/backups 60 NORMAL  > backup_delete_${i}.log & done
