#!/usr/bin/env sh

csthost=deepblue.cs.camosun.bc.ca

if [ "x$HOSTNAME" = "x$csthost" ]; then
	setfacl -R -m u:rthorndy:rwx handin
else
	echo "This script should only be run on $csthost" 1>&2
	exit 1
fi

