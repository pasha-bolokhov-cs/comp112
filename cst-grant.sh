#!/usr/bin/env sh
#
#  Add permissions for the instructor to be able to chdir()
#  into 'handin' and also grant access to the contents therein
#

csthost=deepblue.cs.camosun.bc.ca
cstinstructor=rthorndy


if [ "x$HOSTNAME" != "x$csthost" ]; then
	echo "This script should only be run on $csthost" 1>&2
	exit 1
fi


# 'core.filemode' should be set to false
if [ "x$(git config core.filemode)" != "xfalse" ]; then
	echo "Setting 'core.filemode' to \"false\" to make Git ignore permission changes" 1>&2
	git config core.filemode false || exit 1
fi

setfacl    -m u:${cstinstructor}:x   ~
setfacl    -m u:${cstinstructor}:x   .
setfacl -R -m u:${cstinstructor}:rwx handin

