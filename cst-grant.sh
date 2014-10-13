#!/usr/bin/env sh
#
#  Add permissions for the instructor to be able to chdir()
#  into 'handin' and also grant access to the contents therein
#

csthost=deepblue.cs.camosun.bc.ca
cstinstructor=rthorndy

# Git changes mode to 674 for some reason
chmod -R 755 .

if [ "x$HOSTNAME" = "x$csthost" ]; then
	setfacl    -m u:${cstinstructor}:x   ~
	setfacl    -m u:${cstinstructor}:x   .
	setfacl -R -m u:${cstinstructor}:rwx handin
else
	echo "This script should only be run on $csthost" 1>&2
	exit 1
fi

