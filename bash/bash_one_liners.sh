#
#   bash_one_liners.sh
#

#   Change all the filenames in a directory tree that start with a capital letter
#   to a lowercase letter.
#
for file in `find testdir -type f`; do echo $file; new_f_name=`echo $file | sed 's/\(.*\/\)\(.\)\(.*\)$/\1\L\2\E\3/'`; echo $new_f_name; mv $file $new_f_name; done

#   Monitor processes in a loop from the command line.
#
while true; do echo -en "\n\n-- TIME: ";date; ps -aef | grep -v grep | egrep "(supervisor|vidder-server-agent|tomcat7)"; sleep 5; done

