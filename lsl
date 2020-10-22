# Super hacky oneliner to reproduce ls -l but with the permissions in octal
stat -c "%a %h %U %G %s %y %n %F" * | tr ':' ' ' | awk '{print $1 "  " $2 "  " $3 ":" $4 "  " $5 "  " $6 "  " $7 ":" $8 "  " $11 "  " $12}' | column -t | sort -k 7
